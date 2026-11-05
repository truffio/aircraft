"""Assemble level files from draft sections.

For each section of requirements/<level>.md (between its BEGIN/END SECTION
markers) the content is replaced by the draft work/<agent-id>/<level>_<SECTION>.md.
Sections without a draft are left untouched; nothing outside the markers changes.
Errors (two agents with the same section, draft for an unknown section, bad
markers) stop the run before anything is written.

Usage: python tools/assemble.py (L0|L1|... | --all) [--root DIR] [--dry-run]
"""
import argparse
import difflib
import re
import sys
from collections import defaultdict
from pathlib import Path

import reqlib

DRAFT_RE = re.compile(r"^(L\d+)_(.+)\.md$")


def find_drafts(root):
    """Return {level: {section: [draft paths]}}."""
    found = defaultdict(lambda: defaultdict(list))
    for p in sorted((Path(root) / "work").glob("*/L*_*.md")):
        m = DRAFT_RE.match(p.name)
        if m:
            found[m.group(1)][m.group(2)].append(p)
    return found


def assemble_level(root, level, drafts):
    """Return (new_text or None, old_text, errors, replaced_sections)."""
    path = Path(root) / "requirements" / f"{level}.md"
    errors, replaced = [], []
    if not path.exists():
        return None, "", [f"{path}: level file does not exist"], replaced
    raw = path.read_bytes().decode("utf-8")
    eol = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.replace("\r\n", "\n").split("\n")
    sections, problems = reqlib.find_sections("\n".join(lines))
    errors += [f"{path}:{n}: {msg}" for n, msg in problems]

    for section, paths in sorted(drafts.items()):
        if section not in sections:
            errors.append(f"{paths[0]}: level file {level} has no section {section}")
        if len(paths) > 1:
            errors.append(f"section {level}/{section} provided by several drafts: "
                          + ", ".join(str(p) for p in paths))
    if errors:
        return None, raw, errors, replaced

    # replace from the last section backwards so earlier indexes stay valid
    for section in sorted(drafts, key=lambda s: -sections[s][0]):
        begin, end = sections[section]
        text = drafts[section][0].read_bytes().decode("utf-8").replace("\r\n", "\n").strip("\n")
        if reqlib.BEGIN_RE.search(text) or reqlib.END_RE.search(text) or \
                any(reqlib.BEGIN_RE.match(l) or reqlib.END_RE.match(l) for l in text.split("\n")):
            errors.append(f"{drafts[section][0]}: draft must not contain section markers")
            continue
        lines[begin + 1:end] = text.split("\n")
        replaced.append(section)
    if errors:
        return None, raw, errors, []
    return eol.join(lines), raw, errors, sorted(replaced)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("level", nargs="?", help="level to assemble, e.g. L2")
    ap.add_argument("--all", action="store_true", help="assemble every level that has drafts")
    ap.add_argument("--root", type=Path, default=reqlib.REPO_ROOT)
    ap.add_argument("--dry-run", action="store_true", help="show what would change; write nothing")
    args = ap.parse_args(argv)
    if bool(args.level) == args.all:
        ap.error("give a level (e.g. L2) or --all")

    drafts = find_drafts(args.root)
    levels = sorted(drafts, key=lambda s: int(s[1:])) if args.all else [args.level]
    if not levels:
        print("no drafts found under work/")
    results, all_errors = [], []
    for level in levels:
        new, old, errors, replaced = assemble_level(args.root, level, drafts.get(level, {}))
        all_errors += errors
        results.append((level, new, old, replaced))

    if all_errors:
        for e in all_errors:
            print(f"error: {e}")
        print("nothing written")
        return 1

    for level, new, old, replaced in results:
        path = Path(args.root) / "requirements" / f"{level}.md"
        if not replaced:
            print(f"{level}: no drafts, unchanged")
        elif new == old:
            print(f"{level}: sections {', '.join(replaced)} already up to date")
        elif args.dry_run:
            print(f"{level}: would update sections {', '.join(replaced)}")
            diff = difflib.unified_diff(old.splitlines(), new.splitlines(),
                                        f"{path} (current)", f"{path} (assembled)", lineterm="")
            print("\n".join(diff))
        else:
            path.write_bytes(new.encode("utf-8"))
            print(f"{level}: updated sections {', '.join(replaced)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
