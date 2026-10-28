# What the requirement checks do

Three scripts read the requirement files and report problems. They check form, not content: a requirement can pass every check and still be wrong. Judging the content is the job of the reviews.

| Script | Looks at | Question it answers |
| --- | --- | --- |
| `lint.py` | One requirement at a time | Is it written well? |
| `trace_check.py` | The links between requirements | Does everything connect? |
| `param_check.py` | Parameter references | Does every `[P-…]` exist? |

Each finding is an **error** or a **warning**. An error is a defect: fix it. A warning is a prompt to look: often fine, sometimes not.

## lint.py — is each requirement written well?

| Code | Severity | Flags | Example that fails |
| --- | --- | --- | --- |
| SHALL | error | Not exactly one "shall" | "…shall hold altitude and shall annunciate ALT" |
| VAGUE | error | Untestable words: fast, adequate, robust, approximately… | "…shall respond quickly" |
| ESCAPE | error | Escape clauses: if possible, as far as possible… | "…shall hold altitude where practicable" |
| OPEN-LIST | error | Unbounded lists: etc., such as, and/or | "…controls such as a stick" |
| ABSOLUTE | error | Words that cannot be verified: always, never, all, 100% | "…shall never exceed…" (rewrite as "each", or put a limit in a parameter) |
| NUMBER | error | A number in the statement. Values go in a parameter `[P-…]` | "…within 50 ft" → "…within [P-AF-110]" |
| ID-FORMAT, LEVEL | error | ID does not match the level, for example `L2-AER-AF-010` in L1 | — |
| MISSING, TYPE, STATUS, VERIFICATION… | error | An attribute is missing, or has a value outside the allowed list | — |
| COMPOUND | warning | "and", "or", "unless" in the statement | Fine if it is one thought; split it if it becomes a tree of cases (D30) |
| TIMING, KEYWORD | warning | Vague timing (after, eventually) or must/may/will instead of shall | — |

## trace_check.py — does everything connect?

| Code | Flags |
| --- | --- |
| ORPHAN, NO-PARENT | A requirement below L0 with no parent, or a parent that does not exist |
| CHILDLESS | A requirement that nothing below it covers. Every L0 requirement shows this until L1 exists. Not reported for records allocated only to STP or REE, whose branches the plan does not write yet (D44) |
| DELETED-REF (warning) | A live statement, verification, parent or assumption "Affects" cites a Deleted record |
| NO-VERIFICATION | No verification method |
| DUPLICATE | Two records with the same ID |
| DERIVED | "Derived" with no design-decision reference |

## param_check.py — do the parameters exist?

It flags `[P-…]` references missing from `PARAMETERS.yaml` (PARAM-MISSING), parameters nobody uses, and bad IDs, units or values.

## Where L0 stands today

| Check | Result | Meaning |
| --- | --- | --- |
| lint | 0 errors, 17 warnings | All COMPOUND, each judged at G0 (`reviews/G0/checklist_L0.md`) |
| trace | 40 CHILDLESS | Expected: there is no L1 yet. The 20 STP/REE-only records are not counted (D44) |
| param | 3 PARAM-MISSING | Expected: P-SYS-120, -060, -070 are seeded into `PARAMETERS.yaml` at B2 |

Deleted records are not linted and their parameters are not checked: a deleted record keeps only its ID and history.

**Run them:** `python tools/lint.py`, `python tools/trace_check.py`, `python tools/param_check.py`. Each script exits with a failure on errors. Adding `--strict` makes warnings fail too. The viewer (`python tools/viewer.py`) shows the same findings, linked to each requirement.

**Question #43:** do warnings block a gate? Your answer was case by case. In practice: errors always block. Each warning is either fixed or accepted with a one-line reason in the review record.
