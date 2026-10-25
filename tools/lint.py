"""Mechanical single-requirement checks (METHODOLOGY 13.1, rules in section 8.4).

Usage: python tools/lint.py [--root DIR] [--file PATH] [--section NAME] [--strict]
Exit code 1 if any error is found (warnings too with --strict).
"""
import argparse
import re
import sys

import reqlib
from reqlib import Finding

# --------------------------------------------------------------------------
# Editable word lists (METHODOLOGY section 8.4). (severity, code, words)
# --------------------------------------------------------------------------
WORD_LISTS = [
    ("error", "VAGUE", [
        "quickly", "adequate", "appropriate", "appropriately", "user-friendly",
        "robust", "efficient", "efficiently", "sufficient", "minimize",
        "maximize", "approximately", "fast", "slow", "easy", "reasonable",
        "flexible", "as needed",
    ]),
    ("error", "ESCAPE", [
        "as far as possible", "if necessary", "where practicable",
        "as required", "if possible", "when possible", "where possible",
    ]),
    ("error", "OPEN-LIST", [
        "etc.", "including but not limited to", "and so on",
        "and/or", "such as",
    ]),
    ("error", "ABSOLUTE", [
        "always", "never", "all", "100 %", "100%", "every time", "any and all",
    ]),
    ("warning", "TIMING", ["after", "once", "eventually", "instantaneous"]),
    ("warning", "KEYWORD", ["must", "may", "should", "will"]),
]
# Words that make a statement compound (rule 1): warnings.
COMPOUND_WORDS = ["and", "or", "unless"]

# --------------------------------------------------------------------------
# Allowed values
# --------------------------------------------------------------------------
TYPES = ["Functional", "Performance", "Interface", "Constraint",
         "Model fidelity", "Documentation"]
STATUSES = ["Draft", "Reviewed", "Baselined", "Verified", "Deleted"]
METHODS = ["Inspection", "Analysis", "Demonstration", "Test"]
CRITICALITY = "Not assessed"
SUBSYSTEMS = "DYN|FU|EF|FC|AF|NAV|TM"

ID_PATTERNS = {   # level -> pattern of valid IDs
    "L0": re.compile(r"^L0-(OBJ|CON|SUC)-\d{3}$"),
    "L1": re.compile(r"^AER-\d{3}$"),
    "other": re.compile(rf"^AER-({SUBSYSTEMS})(-[A-Z0-9]+)*-\d{{3}}$"),
}

ID_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b")  # AER-AF-010, P-FC-004
LEVEL_TOKEN_RE = re.compile(r"\bL\d+\b")


def word_re(word):
    return re.compile(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", re.IGNORECASE)


COMPILED = [(sev, code, [(w, word_re(w)) for w in words])
            for sev, code, words in WORD_LISTS]
COMPOUND = [(w, word_re(w)) for w in COMPOUND_WORDS]
SHALL_RE = word_re("shall")


def lint_record(rec):
    """Return the findings for one requirement record."""
    out = []
    f = str(rec.file)
    rid = rec.id

    def add(sev, code, msg, field=None):
        out.append(Finding(f, rec.where(field), sev, code, rid, msg))

    # all 13.3 fields present and non-empty
    for name in reqlib.REQ_FIELDS:
        if name not in rec.fields:
            add("error", "MISSING", f"field {name!r} is missing")
        elif not rec.fields[name].strip():
            add("error", "EMPTY", f"field {name!r} is empty", name)

    # ID format and level
    level = rec.get("Level")
    if rid:
        pat = ID_PATTERNS.get(level, ID_PATTERNS["other"])
        if level and not pat.match(rid):
            add("error", "ID-FORMAT", f"ID does not match the format for level {level} "
                "(L0-OBJ|CON|SUC-nnn, AER-nnn, AER-<SUB>[-<ITEM>]-<NNN>)", "ID")
        else:
            if not re.search(r"-\d{3}$", rid):
                add("error", "ID-FORMAT", "ID must end in a three-digit number", "ID")
            elif int(rid[-3:]) % 10 != 0:
                add("warning", "ID-STEP", "numbers go in steps of 10", "ID")
    if level and rec.file_level and level != rec.file_level:
        add("error", "LEVEL", f"Level {level} does not match file level {rec.file_level}", "Level")

    # allowed sets
    typ = rec.get("Type")
    if typ == "Safety":
        add("error", "TYPE", "Safety type is not used this cycle", "Type")
    elif typ and typ not in TYPES:
        add("error", "TYPE", f"Type {typ!r} not in {TYPES}", "Type")
    status = rec.get("Status")
    if status and status not in STATUSES:
        add("error", "STATUS", f"Status {status!r} not in {STATUSES}", "Status")
    crit = rec.get("Criticality")
    if crit and crit != CRITICALITY:
        add("error", "CRITICALITY", f"Criticality must be {CRITICALITY!r} this cycle", "Criticality")
    ver = rec.get("Verification")
    if ver:
        method = reqlib.split_verification(ver)[0]
        if method not in METHODS:
            add("error", "VERIFICATION", f"verification method {method!r} not in {METHODS}",
                "Verification")
    version = rec.get("Version")
    if version and not version.isdigit():
        add("error", "VERSION", "Version must be a whole number", "Version")

    lint_statement(rec, add)
    return out


def lint_statement(rec, add):
    text = rec.get("Statement")
    if not text:
        return
    n = len(SHALL_RE.findall(text))
    if n != 1:
        add("error", "SHALL", f'Statement has {n} "shall"; exactly one is required', "Statement")
    for sev, code, words in COMPILED:
        for word, rx in words:
            if rx.search(text):
                add(sev, code, f"Statement contains {word!r}", "Statement")
    for word, rx in COMPOUND:
        if rx.search(text):
            add("warning", "COMPOUND", f"Statement contains {word!r}: one thought per statement",
                "Statement")
    bare = LEVEL_TOKEN_RE.sub("", ID_TOKEN_RE.sub("", text))   # drop IDs and parameter refs
    if re.search(r"\d", bare):
        add("error", "NUMBER", "Statement contains a number; use a parameter reference [P-XX-NNN]",
            "Statement")


def lint_assumption(rec):
    out = []
    for name in reqlib.ASM_FIELDS:
        if not rec.fields.get(name, "").strip():
            out.append(Finding(str(rec.file), rec.where(), "error", "MISSING", rec.id,
                               f"assumption field {name!r} is missing or empty"))
    if rec.id and not re.match(r"^L0-ASM-\d{3}$", rec.id):
        out.append(Finding(str(rec.file), rec.where("ID"), "error", "ID-FORMAT", rec.id,
                           "assumption ID must be L0-ASM-nnn"))
    return out


def run(root, file=None, section=None):
    repo = reqlib.load_repo(root, file, section)
    findings = list(repo.problems)
    for rec in repo.records:
        findings += lint_record(rec)
    for rec in repo.assumptions:
        findings += lint_assumption(rec)
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    reqlib.add_common_args(ap)
    ap.add_argument("--file", help="lint one file (level file or work/ draft)")
    ap.add_argument("--section", help="lint one section only")
    args = ap.parse_args(argv)
    return reqlib.report(run(args.root, args.file, args.section), args.strict)


if __name__ == "__main__":
    sys.exit(main())
