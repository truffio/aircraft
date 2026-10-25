# Tools

Python 3 scripts that check and assemble the requirement files. They need only the standard library and PyYAML. Run them from the repository root. Every script takes `--root DIR` (default: the repository containing `tools/`), which the tests use to point at fixtures.

Exit code is 0 when clean and 1 when there are errors. Warnings are printed but do not fail the run unless you add `--strict`. Output lines look like `file:line: severity [CODE] ID: message`.

| Script | Purpose | Run |
| --- | --- | --- |
| `reqlib.py` | Shared parser (not run directly). Reads `requirements/L*.md`, the `req` and `asm` blocks, section markers, `parameters/PARAMETERS.yaml`. Reports malformed blocks with file:line. | |
| `lint.py` | METHODOLOGY 13.1 checks on each requirement: one "shall", vague terms, escape clauses, open lists, absolutes (errors); "and", "or", "unless", timing words, "must/may/should/will" (warnings); numbers in the Statement; all 13.3 fields present; ID format; Level matches file; Type, Status and Verification method in allowed sets; Criticality `Not assessed`; Safety rejected. The word lists are at the top of the file. | `python tools/lint.py [--file PATH] [--section AF]` |
| `trace_check.py` | Duplicate IDs, missing parents, orphans, childless parents (allocated but no child), no verification method, Derived without a DD in `registers/DECISIONS.md`. | `python tools/trace_check.py` |
| `param_check.py` | `[P-..]` references exist; duplicate or bad parameter IDs; unused parameters; non-SI unit hints; TBD/TBR parameters missing from `registers/TBD_TBR.md` (warning). | `python tools/param_check.py` |
| `vcrm.py` | Writes `verification/VCRM.md` from the records. `--check` writes nothing and fails if any requirement lacks a method. | `python tools/vcrm.py [--check] [--out FILE]` |
| `assemble.py` | Replaces each section between `<!-- BEGIN SECTION X -->` and `<!-- END SECTION X -->` with the draft `work/<agent>/<level>_<SECTION>.md`. Sections without a draft stay as they are; two drafts for one section, or a draft for an unknown section, is an error and nothing is written. | `python tools/assemble.py L2 [--dry-run]` or `python tools/assemble.py --all` |

## Reviewing one draft or section

`lint.py --file` accepts a level file or a draft, for example `python tools/lint.py --file work/C5/L2_AF.md`. In a draft the section comes from the file name. `--section AF` limits any run to one section of the level files.

## Tests

```
python tools/tests/test_tools.py
```

Fixtures (a clean set and a deliberately broken set) are in `tools/tests/fixtures/`.
