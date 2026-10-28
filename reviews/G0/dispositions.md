# Gate G0 — Finding dispositions

Rework of the findings in `inspection_A1-A3.md` (G0-F01 to F31) and `checklist_L0.md`, on branch `g0_review`, 2026-10-27. Owner rulings: #90 to #93, recorded as D41 to D44 (plan §9).

## Inspection findings

| F-ID | Sev. | Disposition |
| --- | --- | --- |
| G0-F01 | Major | **Fixed (D41).** Every live L0 record now has Verification "Inspection — TBD; success criteria: each child requirement has passed its verification and the decomposition has been reviewed (D41)". The former criteria, corrected where a finding applied, are kept in the rationale as "Children must show (D41): (method) …". L0.md header states the rule. |
| G0-F02 | Major | **Fixed.** L0-OBJ-030 guidance: each mode of the baselined catalogue is covered by a requirement in the Aeronef branch (no level named). Rationale: modes are defined at L2 (D33). |
| G0-F03 | Major | **Fixed (D42).** One configuration. "Reference configuration" removed from L0-SUC-020 and L0-OBJ-020/-060; glossary adds *Aeronef configuration*. |
| G0-F04 | Major | **Fixed.** L0-OBJ-210 guidance points to the method assessment report (D28), not L0-SUC-170; rationale corrected; glossary adds *Method assessment report*. |
| G0-F05 | Major | **Fixed.** L0-CON-270 statement points to the conventions unit table (CV-740), which includes lb and h/min; guidance names lb (D9) and durations (D34). Glossary *Crew-facing unit* and CONOPS §1.1 aligned. |
| G0-F06 | Major | **Fixed.** L0-CON-280 guidance: consistent with R-004 practice per the public sources of D36, departures identified. |
| G0-F07 | Major | **Fixed.** L0-CON-030 rationale: superseded Q-A1-01 sentence removed; scope is D18; kinematic terms #81. Guidance names the #81 terms as the only exception. |
| G0-F08 | Major | **Fixed.** L0-CON-310 statement scoped "While the Aeronef is airborne"; guidance requires the landing-envelope acceleration limit to be consistent with P-SYS-120; glossary adds *Airborne*. |
| G0-F09 | Major | **Fixed.** 30 terms added to the glossary from `work/A1/glossary_proposals.md` and the findings (terms used only by deleted records were not merged). |
| G0-F10 | Major | **Fixed (D43).** All remaining conventions set to Fixed (D43); CV-650/660 Deferred to L2 (#54). CONVENTIONS and GLOSSARY headers Fixed. |
| G0-F11 | Major | **Fixed.** Comparison wording removed from L0-OBJ-020, -120 and L0-CON-200, -210 rationales (re-based on D15, D24, D42). CONOPS SH-03, SH-04, N-220 (kept for later), N-250, §4.6 row, SC-110 and SC-220 (out of scope this cycle) aligned. |
| G0-F12 | Major | **Fixed (D44).** trace_check no longer reports records allocated only to STP or REE as childless (`OUT_OF_SCOPE`); the 20 records say so in their rationale; plan G4 exit amended. |
| G0-F13 | Minor | **Fixed.** References to deleted records removed from L0-OBJ-020, -140, -160, L0-CON-250 and the Affects of L0-ASM-020, -140. New trace warning DELETED-REF guards this. |
| G0-F14 | Minor | **Fixed.** L0-CON-090 "Wind is excluded" removed; guidance separates forces from the ground-contact effect. |
| G0-F15 | Minor | **Fixed.** L0-CON-020 (D10, D33), -070, -210 (D15) and L0-SUC-040 rationales no longer point to decided questions. |
| G0-F16 | Minor | **Accepted.** L0-ASM-140 now affects only Draft records (L0-CON-250, L0-SUC-140); it stays Confirmed and is revisited with the REE (#69). L0-ASM-130 likewise with #86. |
| G0-F17 | Minor | **Fixed.** Closure points added: G1, G2, or the REE plan extension (D44). |
| G0-F18 | Minor | **Fixed.** `work/A1/param_proposals.md`: YAML holds only P-SYS-060, -070, -120; withdrawn IDs moved to a prose section; register table regenerated from the live records. The crew-unit schema flag (D34) is left to B2. |
| G0-F19 | Minor | **Fixed.** L0.md, CONOPS and DECISIONS headers updated. |
| G0-F20 | Minor | **Fixed.** CONOPS §4.2 altitude per CV-430, definitions cite the conventions, state knowledge cites L0-ASM-010; L0-ASM-050 Affects points to CONOPS §4.2. |
| G0-F21 | Minor | **Fixed.** CV-550 (D10, D33), §7 intro (D12), CV-630 and glossary *Selected course* (D14), glossary *VOR* (D12). |
| G0-F22 | Minor | **Deferred** with the REE (#69, D44); logged on #69. |
| G0-F23 | Minor | **Logged** on #89 for C5. |
| G0-F24 | Minor | **Fixed.** CONOPS §5 envelope and N-170 include the crew acceleration limit. |
| G0-F25 | Minor | **Fixed.** L0-CON-310 rationale: the evaluation point (CG or crew station) is set at a lower level. |
| G0-F26 | Minor | **Fixed.** L0.md header has a "Descoped at G0" table. |
| G0-F27 | Minor | **Fixed.** L0-OBJ-190 guidance adds the procedure-and-result link. |
| G0-F28 | Minor | **Deferred** with the REE scoring rules (D44). |
| G0-F29 | Minor | **Fixed.** L0-SUC-040 guidance: each run of one complete recorded campaign. |
| G0-F30 | Minor | **Fixed.** L0-CON-120 guidance Demonstration; L0-CON-300 guidance Inspection plus Test; L0-SUC-050 Type Functional. |
| G0-F31 | Minor | **Fixed** (a) Deleted records skipped by lint and param_check; (b) DELETED-REF warning; (c) STP/REE exemption. **Open:** (d) TBD/TBR date check, (e) param_check over `specs/`, both for B2. |

## Checklist findings (Major)

| Record | Disposition |
| --- | --- |
| L0-CON-030 | Fixed with G0-F07. |
| L0-CON-290 | Fixed: statement now "as a landing within the landing envelope and as a crash outside it". |
| L0-SUC-100, -120, -130 | Deferred: the scoring rules and definitions are written with the REE branch (D44); TBDs dated to that extension. |
| L0-CON-270 | Fixed with G0-F05 (COMPOUND split resolved: one thought). |
| L0-CON-300 | Fixed with G0-F30. Per-effector maxima become EF parameters at C3. |

Checklist Minors are closed by the moderator except: L0-CON-110 tolerance, L0-CON-140 shape wording, L0-SUC-010 "last layer", L0-SUC-170 timing, and "craft" in rationales. These are wording and carry to the L1 children, where the measurable versions belong.

## Checks after rework

lint 0 errors, 17 COMPOUND warnings (16 accepted in the checklist; L0-CON-270 no longer compound). trace 40 CHILDLESS (no L1 yet), 0 DELETED-REF. param 3 PARAM-MISSING (seeded at B2). Tests: 38 passed.
