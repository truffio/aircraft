"""Tests for the requirement tools. Run: python tools/tests/test_tools.py"""
import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))

import assemble, lint, param_check, reqlib, trace_check, vcrm, viewer  # noqa: E402

GOOD = HERE / "fixtures" / "good"
BAD = HERE / "fixtures" / "bad"


def codes(findings, item=None):
    return {f.code for f in findings if item is None or f.item == item}


def run_main(module, argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = module.main(argv)
    return rc, buf.getvalue()


class ParserTests(unittest.TestCase):
    def test_good_fixture_parses(self):
        repo = reqlib.load_repo(GOOD)
        self.assertEqual(repo.problems, [])
        ids = [r.id for r in repo.records]
        self.assertEqual(ids, ["L0-OBJ-010", "L1-AER-010", "L2-AER-AF-010", "L2-AER-AF-020"])
        self.assertEqual([a.id for a in repo.assumptions], ["L0-ASM-010"])
        rec = repo.records[2]
        self.assertEqual(rec.section, "AF")
        self.assertEqual(rec.file_level, "L2")
        self.assertIn("altitude error", rec.get("Statement"))   # continuation line joined

    def test_continuation_in_rationale(self):
        rec = reqlib.load_repo(GOOD).records[1]
        self.assertIn("Sufficiency:", rec.get("Rationale"))

    def test_malformed_blocks_reported(self):
        repo = reqlib.load_repo(BAD)
        msgs = " | ".join(f"{p.line}:{p.message}" for p in repo.problems)
        self.assertIn("not a 'Field: value' line", msgs)
        text = "```req\nID: X\nStatement: a\n"
        pf = reqlib.parse_text(text, "L2.md")
        self.assertTrue(any("unclosed" in p.message for p in pf.problems))

    def test_parameters_and_sections(self):
        params, problems = reqlib.load_parameters(GOOD)
        self.assertEqual([p["id"] for p in params], ["P-AF-010"])
        text = (GOOD / "requirements" / "L2.md").read_text(encoding="utf-8")
        sections, probs = reqlib.find_sections(text)
        self.assertEqual(sorted(sections), ["AF", "FC"])
        self.assertEqual(probs, [])

    def test_real_repo_skeleton_parses(self):
        repo = reqlib.load_repo(reqlib.REPO_ROOT)
        self.assertEqual(repo.problems, [])


class LintTests(unittest.TestCase):
    def test_good_is_clean(self):
        self.assertEqual(lint.run(GOOD), [])

    def test_bad_statement(self):
        f = lint.run(BAD)
        c = codes(f, "L2-AER-AF-010")
        self.assertTrue({"SHALL", "VAGUE", "ABSOLUTE", "OPEN-LIST", "NUMBER", "COMPOUND"} <= c, c)

    def test_bad_attributes(self):
        f = lint.run(BAD)
        c = codes([x for x in f if x.item == "L2-AER-AF-020"])
        self.assertTrue({"TYPE", "CRITICALITY", "STATUS", "VERIFICATION", "LEVEL"} <= c, c)

    def test_id_and_missing_field(self):
        f = lint.run(BAD)
        self.assertIn("ID-FORMAT", codes(f, "WRONG-ID"))
        self.assertIn("MISSING", codes(f, "L2-AER-AF-030"))
        self.assertIn("ID-STEP", codes(f, "L2-AER-AF-025"))

    def test_id_carries_level(self):
        # D31: the level prefix must match the Level field; old unprefixed IDs fail
        def id_codes(rid, level):
            rec = reqlib.Record("req", Path("L2.md"), 1, "AF", level, {"ID": rid, "Level": level})
            return {x.code for x in lint.lint_record(rec)}
        self.assertNotIn("ID-FORMAT", id_codes("L2-AER-AF-010", "L2"))
        self.assertNotIn("ID-FORMAT", id_codes("L1-AER-010", "L1"))
        self.assertIn("ID-FORMAT", id_codes("L3-AER-AF-010", "L2"))
        self.assertIn("ID-FORMAT", id_codes("AER-AF-010", "L2"))
        self.assertIn("ID-FORMAT", id_codes("AER-010", "L1"))

    def test_deleted_statement_not_linted(self):
        def stmt_codes(status):
            rec = reqlib.Record("req", Path("L0.md"), 1, "OBJ", "L0",
                                {"ID": "L0-OBJ-100", "Level": "L0", "Status": status,
                                 "Statement": "The project shall compare designs and implementations quickly."})
            return {x.code for x in lint.lint_record(rec)}
        self.assertTrue({"COMPOUND", "VAGUE"} <= stmt_codes("Reviewed"))
        self.assertFalse({"COMPOUND", "VAGUE"} & stmt_codes("Deleted"))

    def test_parameter_digits_not_flagged(self):
        # L2-AER-AF-025 only has a parameter ref, ID-like tokens and no other digits
        self.assertNotIn("NUMBER", codes(lint.run(BAD), "L2-AER-AF-025"))

    def test_filters(self):
        self.assertEqual(lint.run(BAD, file="requirements/L1.md"), [])
        self.assertEqual(lint.run(BAD, section="NOPE"), [])
        self.assertTrue(lint.run(BAD, section="AF"))

    def test_exit_codes(self):
        rc, _ = run_main(lint, ["--root", str(GOOD)])
        self.assertEqual(rc, 0)
        rc, out = run_main(lint, ["--root", str(BAD)])
        self.assertEqual(rc, 1)
        self.assertIn("error", out)


class TraceTests(unittest.TestCase):
    def test_good_is_clean(self):
        self.assertEqual(trace_check.run(GOOD), [])

    def test_bad(self):
        f = trace_check.run(BAD)
        self.assertIn("NO-PARENT", codes(f, "L2-AER-AF-010"))
        self.assertIn("ORPHAN", codes(f, "L2-AER-AF-020"))
        self.assertIn("NO-VERIFICATION", codes(f, "L2-AER-AF-020"))
        self.assertIn("DUPLICATE", codes(f, "L2-AER-AF-020"))
        self.assertIn("DERIVED", codes(f, "L2-AER-AF-025"))
        self.assertIn("CHILDLESS", codes(f, "L2-AER-AF-025"))

    def test_leaf_is_not_childless(self):
        self.assertNotIn("CHILDLESS", codes(trace_check.run(GOOD)))

    @staticmethod
    def _l0(rid, alloc="AER", status="Reviewed", **extra):
        return reqlib.Record("req", Path("L0.md"), 1, "OBJ", "L0",
                             {"ID": rid, "Level": "L0", "Allocated to": alloc, "Status": status,
                              "Verification": "Inspection — TBD", **extra})

    def test_out_of_scope_not_childless(self):
        # D44: L0 records allocated only to TST or RVS wait for their branch
        repo = SimpleNamespace(records=[self._l0("L0-OBJ-060", "TST"), self._l0("L0-OBJ-170", "RVS"),
                                        self._l0("L0-OBJ-140", "AER, TST")], assumptions=[])
        f = trace_check.check(repo, set())
        self.assertEqual(codes(f, "L0-OBJ-060") | codes(f, "L0-OBJ-170"), set())
        self.assertIn("CHILDLESS", codes(f, "L0-OBJ-140"))
        # the exemption is for L0 only: a stray L1 record allocated to TST is still reported
        l1 = reqlib.Record("req", Path("L1.md"), 1, "AER", "L1",
                           {"ID": "L1-AER-010", "Level": "L1", "Allocated to": "TST", "Status": "Draft",
                            "Parent(s)": "L0-OBJ-060", "Verification": "Test — TBD"})
        f = trace_check.check(SimpleNamespace(records=[self._l0("L0-OBJ-060", "TST"), l1], assumptions=[]), set())
        self.assertIn("CHILDLESS", codes(f, "L1-AER-010"))

    def test_deleted_ref_warned(self):
        asm = reqlib.Record("asm", Path("L0.md"), 1, "ASM", "L0", {"ID": "L0-ASM-020", "Affects": "L0-OBJ-100"})
        repo = SimpleNamespace(records=[self._l0("L0-OBJ-100", status="Deleted"),
                                        self._l0("L0-OBJ-110", "TST", Statement="As L0-OBJ-100 says.")],
                               assumptions=[asm])
        f = trace_check.check(repo, set())
        self.assertIn("DELETED-REF", codes(f, "L0-OBJ-110"))
        self.assertIn("DELETED-REF", codes(f, "L0-ASM-020"))
        self.assertEqual({x.severity for x in f if x.code == "DELETED-REF"}, {"warning"})


class ParamTests(unittest.TestCase):
    def test_good_is_clean(self):
        self.assertEqual(param_check.run(GOOD), [])

    def test_bad(self):
        f = param_check.run(BAD)
        c = codes(f)
        self.assertTrue({"PARAM-DUP", "PARAM-ID", "PARAM-UNIT", "PARAM-TBD",
                         "PARAM-MISSING", "PARAM-UNUSED"} <= c, c)
        sev = {x.code: x.severity for x in f}
        self.assertEqual(sev["PARAM-TBD"], "warning")

    def test_unit_hint(self):
        self.assertEqual(param_check.unit_tokens("m/s^2"), ["m", "s", "2"])

    def test_deleted_record_refs_ignored(self):
        def missing(status):
            rec = reqlib.Record("req", Path("L0.md"), 1, "SUC", "L0",
                                {"ID": "L0-SUC-080", "Statement": "… shall reach [P-SYS-010].",
                                 "Parameters": "P-SYS-010", "Status": status})
            out, _ = param_check.check_references(SimpleNamespace(records=[rec]), {})
            return {x.code for x in out}
        self.assertIn("PARAM-MISSING", missing("Draft"))
        self.assertNotIn("PARAM-MISSING", missing("Deleted"))


class VcrmTests(unittest.TestCase):
    def test_render_good(self):
        text = vcrm.render(reqlib.load_repo(GOOD))
        self.assertIn("| L2-AER-AF-010 | L2 | Performance | Test | TP-020 |", text)
        self.assertIn("| ID | Level | Type | Method | Procedure | Success criteria | Status |", text)

    def test_check_mode(self):
        rc, _ = run_main(vcrm, ["--root", str(GOOD), "--check"])
        self.assertEqual(rc, 0)
        rc, out = run_main(vcrm, ["--root", str(BAD), "--check"])
        self.assertEqual(rc, 1)
        self.assertIn("NO-VERIFICATION", out)

    def test_write(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "VCRM.md"
            rc, _ = run_main(vcrm, ["--root", str(GOOD), "--out", str(out)])
            self.assertEqual(rc, 0)
            self.assertIn("L1-AER-010", out.read_text(encoding="utf-8"))


class AssembleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.root = self.tmp / "repo"
        shutil.copytree(GOOD, self.root)
        self.l2 = self.root / "requirements" / "L2.md"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_dry_run_changes_nothing(self):
        before = self.l2.read_bytes()
        rc, out = run_main(assemble, ["L2", "--root", str(self.root), "--dry-run"])
        self.assertEqual(rc, 0)
        self.assertIn("would update sections AF, FC", out)
        self.assertEqual(self.l2.read_bytes(), before)

    def test_assemble_replaces_only_sections(self):
        before = self.l2.read_text(encoding="utf-8")
        rc, _ = run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertEqual(rc, 0)
        after = self.l2.read_text(encoding="utf-8")
        self.assertIn("L2-AER-AF-030", after)
        self.assertNotIn("L2-AER-AF-020", after)           # old AF content replaced
        self.assertIn("Draft FC text.", after)
        # text outside the markers is untouched
        self.assertTrue(after.startswith("# L2 fixture\n\n<!-- BEGIN SECTION AF -->"))
        self.assertTrue(after.rstrip().endswith("<!-- END SECTION FC -->"))
        self.assertNotIn("# L2 fixture", before.split("<!-- BEGIN SECTION AF -->")[1])
        # idempotent
        rc, out = run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertIn("already up to date", out)
        self.assertEqual(self.l2.read_text(encoding="utf-8"), after)

    def test_sections_without_draft_untouched(self):
        (self.root / "work" / "X2" / "L2_FC.md").unlink()
        rc, _ = run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertEqual(rc, 0)
        self.assertIn("No requirements yet", self.l2.read_text(encoding="utf-8"))

    def test_two_agents_same_section_is_error(self):
        other = self.root / "work" / "X3"
        other.mkdir()
        (other / "L2_AF.md").write_text("dup\n", encoding="utf-8")
        before = self.l2.read_bytes()
        rc, out = run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertEqual(rc, 1)
        self.assertIn("several drafts", out)
        self.assertEqual(self.l2.read_bytes(), before)

    def test_unknown_section_is_error(self):
        (self.root / "work" / "X2" / "L2_ZZZ.md").write_text("x\n", encoding="utf-8")
        rc, out = run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertEqual(rc, 1)
        self.assertIn("no section ZZZ", out)

    def test_all(self):
        rc, out = run_main(assemble, ["--all", "--root", str(self.root)])
        self.assertEqual(rc, 0)
        self.assertIn("L2: updated sections AF, FC", out)

    def test_assembled_output_lints(self):
        run_main(assemble, ["L2", "--root", str(self.root)])
        self.assertEqual(lint.run(self.root, file="requirements/L2.md"), [])


class ViewerTests(unittest.TestCase):
    def test_graph_from_good_fixture(self):
        data = viewer.build(GOOD)
        kinds = {n["id"]: n["kind"] for n in data["nodes"]}
        self.assertEqual(kinds["L1-AER-010"], "req")
        self.assertEqual(kinds["L0-ASM-010"], "asm")
        edges = {(e["from"], e["to"], e["kind"]) for e in data["edges"]}
        self.assertIn(("L0-OBJ-010", "L1-AER-010", "parent"), edges)
        self.assertIn(("L1-AER-010", "L2-AER-AF-010", "parent"), edges)
        self.assertTrue(any(k == "uses" for _, _, k in edges))

    def test_function_ids_are_not_requirement_refs(self):
        self.assertEqual(viewer.ID_RE.findall("see F-AER-04 and L2-AER-AF-010"), ["L2-AER-AF-010"])

    def test_render_embeds_data_safely(self):
        html = viewer.render({"nodes": [{"id": "X", "title": "</script><b>"}], "edges": [],
                              "findings": {}, "sections": [], "problems": []})
        self.assertNotIn("/*DATA*/null", html)
        self.assertNotIn("</script><b>", html)

    def test_writes_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "v.html"
            rc, _ = run_main(viewer, ["--root", str(GOOD), "--out", str(out)])
            self.assertEqual(rc, 0)
            self.assertIn("L2-AER-AF-010", out.read_text(encoding="utf-8"))


class CliTests(unittest.TestCase):
    def test_scripts_run_as_commands(self):
        for name in ["lint", "trace_check", "param_check"]:
            r = subprocess.run([sys.executable, str(TOOLS / f"{name}.py"), "--root", str(GOOD)],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        r = subprocess.run([sys.executable, str(TOOLS / "lint.py"), "--root", str(BAD)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
