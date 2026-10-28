"""Traceability checks over all level files.

Checks: duplicate IDs, missing parents, orphans, childless parents,
requirements without a verification method, Derived without a design decision,
and live records whose statement, verification, parents or assumption Affects
cite a Deleted record (warning). Records with Status "Deleted" are ignored
except for duplicate-ID checks. Records allocated only to elements outside the
plan's scope (OUT_OF_SCOPE, decision D44) are not reported as childless.

Usage: python tools/trace_check.py [--root DIR] [--strict]
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import reqlib
from reqlib import Finding, DASH

METHODS = ["Inspection", "Analysis", "Demonstration", "Test"]
# L1 elements whose branch this plan does not write yet (D44). Editable.
OUT_OF_SCOPE = {"STP", "REE"}
REQ_ID_RE = re.compile(r"\bL\d+-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3}\b")


def check(repo, decisions):
    out = []
    by_id = defaultdict(list)
    for r in repo.records + repo.assumptions:
        by_id[r.id].append(r)

    def add(rec, code, msg, field=None, sev="error"):
        out.append(Finding(str(rec.file), rec.where(field), sev, code, rec.id, msg))

    for rid, recs in by_id.items():
        for dup in recs[1:]:
            add(dup, "DUPLICATE", f"ID also defined at {recs[0].file}:{recs[0].line}", "ID")

    live = [r for r in repo.records if r.get("Status") != "Deleted"]
    children = defaultdict(list)
    for r in live:
        for pid in reqlib.parent_ids(r.get("Parent(s)")):
            children[pid].append(r.id)

    for r in live:
        parents_value = r.get("Parent(s)")
        parents = reqlib.parent_ids(parents_value)
        dd = reqlib.derived_dd(parents_value)
        is_l0 = r.get("Level") == "L0" or r.file_level == "L0"

        for pid in parents:
            if pid not in by_id:
                add(r, "NO-PARENT", f"parent {pid} does not exist", "Parent(s)")
        if parents_value.strip().startswith("Derived"):
            if dd is None:
                add(r, "DERIVED", "Derived must name a decision: Derived (DD-nnn)", "Parent(s)")
            elif dd not in decisions:
                add(r, "DERIVED", f"{dd} is not in registers/DECISIONS.md", "Parent(s)")
        elif not parents and not is_l0:
            add(r, "ORPHAN", "no parent and not Derived (DD-nnn)", "Parent(s)")

        # leaf = nobody lists it as parent AND nothing allocated
        allocated = r.get("Allocated to").strip()
        out_of_scope = {a.strip() for a in allocated.split(",")} <= OUT_OF_SCOPE
        if not children.get(r.id) and allocated not in ("", DASH) and not out_of_scope:
            add(r, "CHILDLESS", f"allocated to {allocated!r} but no requirement lists it as parent",
                "Allocated to")

        method = reqlib.split_verification(r.get("Verification"))[0]
        if method not in METHODS:
            add(r, "NO-VERIFICATION", "no verification method (Inspection/Analysis/Demonstration/Test)",
                "Verification")

    deleted = {r.id for r in repo.records if r.get("Status") == "Deleted"}
    fields = {"req": ["Statement", "Verification", "Parent(s)"], "asm": ["Affects"]}
    for r in live + repo.assumptions:
        for f in fields[r.kind]:
            for cited in sorted(set(REQ_ID_RE.findall(r.get(f))) & deleted):
                add(r, "DELETED-REF", f"{f} cites {cited}, which is Deleted", f, sev="warning")
    return out


def run(root):
    root = Path(root)
    repo = reqlib.load_repo(root)
    decisions = reqlib.table_ids(root / "registers" / "DECISIONS.md", "DD")
    return repo.problems + check(repo, decisions)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    reqlib.add_common_args(ap)
    args = ap.parse_args(argv)
    return reqlib.report(run(args.root), args.strict)


if __name__ == "__main__":
    sys.exit(main())
