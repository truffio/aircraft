"""Traceability checks over all level files.

Checks: duplicate IDs, missing parents, orphans, childless parents,
requirements without a verification method, Derived without a design decision.
Records with Status "Deleted" are ignored except for duplicate-ID checks.

Usage: python tools/trace_check.py [--root DIR] [--strict]
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

import reqlib
from reqlib import Finding, DASH

METHODS = ["Inspection", "Analysis", "Demonstration", "Test"]


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
        if not children.get(r.id) and allocated not in ("", DASH):
            add(r, "CHILDLESS", f"allocated to {allocated!r} but no requirement lists it as parent",
                "Allocated to")

        method = reqlib.split_verification(r.get("Verification"))[0]
        if method not in METHODS:
            add(r, "NO-VERIFICATION", "no verification method (Inspection/Analysis/Demonstration/Test)",
                "Verification")
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
