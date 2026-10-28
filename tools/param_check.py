"""Parameter-reference checks against parameters/PARAMETERS.yaml.

Checks: [P-..] references in statements and the Parameters field exist, duplicate
or badly formed parameter IDs, unused parameters, non-SI unit hints, and TBD/TBR
parameters without an entry in registers/TBD_TBR.md (warning). References from
records with Status "Deleted" are ignored.

Usage: python tools/param_check.py [--root DIR] [--strict]
"""
import argparse
import re
import sys
from pathlib import Path

import reqlib
from reqlib import Finding, DASH

PARAM_ID_RE = re.compile(r"^P-(SYS|DYN|FU|EF|FC|AF|NAV|TM)-\d{3}$")

# Unit tokens that are clearly not SI (lower case). Editable.
NON_SI_UNITS = {
    "ft", "feet", "foot", "kt", "kts", "kn", "knot", "knots", "nm", "nmi", "mi", "mph",
    "fpm", "lb", "lbs", "lbf", "in", "inch", "gal", "deg", "degree", "degrees", "°",
    "min", "minute", "minutes", "h", "hr", "hrs", "hour", "hours", "km", "%", "percent",
}


def unit_tokens(unit):
    return [t for t in re.split(r"[\s/*·.^()\-]+", str(unit).lower()) if t]


def check_parameters(params, path, tbd_text):
    out = []
    seen = {}
    for p in params:
        pid = str(p.get("id", ""))
        loc = (str(path), 0)

        def add(sev, code, msg):
            out.append(Finding(loc[0], loc[1], sev, code, pid, msg))

        if not PARAM_ID_RE.match(pid):
            add("error", "PARAM-ID", "ID must look like P-<SYS|DYN|FU|EF|FC|AF|NAV|TM>-NNN")
        if pid in seen:
            add("error", "PARAM-DUP", "duplicate parameter ID")
        seen[pid] = p
        if "unit" not in p or p["unit"] in (None, ""):
            add("error", "PARAM-UNIT", "unit is missing (use \"1\" for dimensionless)")
        else:
            bad = [t for t in unit_tokens(p["unit"]) if t in NON_SI_UNITS]
            if bad:
                add("warning", "PARAM-UNIT", f"unit {p['unit']!r} looks non-SI ({', '.join(bad)})")
        status = p.get("status")
        if status not in ("TBD", "TBR", "Set"):
            add("error", "PARAM-STATUS", f"status {status!r} must be TBD, TBR or Set")
        if status == "Set" and p.get("value") is None:
            add("error", "PARAM-VALUE", "status is Set but value is null")
        if status in ("TBD", "TBR") and pid not in tbd_text:
            add("warning", "PARAM-TBD", f"{status} parameter has no entry in registers/TBD_TBR.md")
    return out, seen


def check_references(repo, known):
    out = []
    used = set()
    for r in repo.records:
        if r.get("Status") == "Deleted":   # its parameters are withdrawn with it
            continue

        def add(sev, code, msg, field):
            out.append(Finding(str(r.file), r.where(field), sev, code, r.id, msg))

        stmt_refs = reqlib.param_refs(r.get("Statement"))
        listed = r.get("Parameters").strip()
        listed_ids = []
        if listed and listed != DASH:
            for tok in [t for t in re.split(r"[,;\s]+", listed) if t]:
                if reqlib.PARAM_REF_RE.fullmatch(tok):
                    listed_ids.append(tok)
                else:
                    add("error", "PARAM-REF", f"{tok!r} in Parameters is not a parameter ID", "Parameters")
        for pid in set(stmt_refs) | set(listed_ids):
            used.add(pid)
            if pid not in known:
                where = "Statement" if pid in stmt_refs else "Parameters"
                add("error", "PARAM-MISSING", f"{pid} is not in PARAMETERS.yaml", where)
        for pid in set(stmt_refs) - set(listed_ids):
            add("warning", "PARAM-UNLISTED", f"{pid} is used in the Statement but not listed under Parameters",
                "Parameters")
    return out, used


def run(root):
    root = Path(root)
    path = root / "parameters" / "PARAMETERS.yaml"
    params, problems = reqlib.load_parameters(root)
    repo = reqlib.load_repo(root)
    tbd = root / "registers" / "TBD_TBR.md"
    tbd_text = tbd.read_text(encoding="utf-8") if tbd.exists() else ""
    out = problems + repo.problems
    f, known = check_parameters(params, path, tbd_text)
    out += f
    f, used = check_references(repo, known)
    out += f
    for pid in known:
        if pid not in used:
            out.append(Finding(str(path), 0, "warning", "PARAM-UNUSED", pid,
                               "parameter is not referenced by any requirement"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    reqlib.add_common_args(ap)
    args = ap.parse_args(argv)
    return reqlib.report(run(args.root), args.strict)


if __name__ == "__main__":
    sys.exit(main())
