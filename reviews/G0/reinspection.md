# Gate G0 delta re-inspection — A1 (L0), A2 (ConOps), A3 (Conventions, Glossary)

```markdown
Artifact / version:   L0 + CONOPS + CONVENTIONS + GLOSSARY at branch g0_review, commit d46831e
                      (requirements/L0.md assembled from work/A1/L0_*.md; specs/CONOPS.md,
                      specs/CONVENTIONS.md, specs/GLOSSARY.md; AIRCRAFT_REQUIREMENTS_PLAN.md §6, §9;
                      tools/trace_check.py and tests). Delta read: git diff -w e1e08d1 d46831e.
Review type:          Inspection (delta re-inspection, METHODOLOGY §13.4), of the rework of
                      reviews/G0/inspection_A1-A3.md (G0-F01 to F31) and reviews/G0/checklist_L0.md
Moderator / author / reader / recorder / reviewers:
                      moderator: orchestrator / author of the rework: orchestrator (owner: Martin) /
                      reader, recorder, reviewer: independent Opus re-inspector (did not author or
                      rework any of the material)
Date:                 2026-10-27
Entry criteria met:   yes:
                      - Working tree clean at d46831e; dispositions recorded (reviews/G0/dispositions.md).
                      - Owner rulings on #90 to #93 recorded as D41 to D44 (plan §9); the four issues are closed.
                      - L0.md in sync with work/A1 (assemble.py L0 --dry-run: "already up to date").
                      - lint 0 errors; trace, param and test results as in section 4.
Findings:             verdicts in sections 1 and 2; new findings in section 3
TBD/TBR list checked: yes (record TBD/TBR fields of every live L0 record; staging register table in
                      work/A1/param_proposals.md; registers/TBD_TBR.md is still empty, seeded at B2)
Exit decision:        Rework, moderator closes (recommended; see section 5)
```

Scope. Every live L0 record (60 `req`, 14 `asm`) was read in full in its work/A1 source after the rework, together with the whole diff of CONOPS, CONVENTIONS, GLOSSARY, the plan, DECISIONS and tools. Decisions D1 to D44 are taken as settled. Items deferred to L2, to the REE plan extension (D44), #69, #86 or #89 are accepted as deferred. "(check)" marks a finding the re-inspector is less certain of.

## 1. Major findings: verdicts

### 1.1 Inspection Majors

| F-ID | Disposition claimed | Verified against | Verdict |
| --- | --- | --- | --- |
| G0-F01 | D41 roll-up on every live L0 record | All 60 live records: Verification is "Inspection — TBD; success criteria: each child requirement has passed its verification and the decomposition has been reviewed (D41)". Former criteria moved to the rationale as "Children must show (D41): (method) …". L0.md header states the rule. Versions were bumped on every changed record. No guidance contradicts its statement (CON-030 see F07). | **Closed** |
| G0-F02 | L0-OBJ-030 guidance without naming L1 | Guidance: "each mode of the baselined mode catalogue (D3) is covered by a requirement in the Aeronef branch". Rationale: "The modes themselves are defined at L2 (D33)"; manual control now "excluded (L0-CON-180)". | **Closed** |
| G0-F03 | D42: one configuration | "Reference configuration" no longer appears in any live record, spec or glossary entry. L0-SUC-020 states one Aeronef configuration that must pass every requirement (D42). Glossary adds *Aeronef configuration*. D24 is annotated "Refined by D42". | **Closed** |
| G0-F04 | L0-OBJ-210 points to the method assessment report | Guidance: method assessment report compiled per D28 with the three sections; rationale says L0-SUC-170 is the final test report. Glossary adds *Method assessment report*. | **Closed** |
| G0-F05 | L0-CON-270 points to the CV-740 unit table | Statement: "in the crew-facing unit that the conventions document assigns to its quantity". CV-740 has lb (D9) and h/min (D34). Glossary *Crew-facing unit* and CONOPS §1.1 now include lb and durations. | **Closed** |
| G0-F06 | L0-CON-280 guidance per D36 | Guidance: "states that it is consistent with R-004 practice as checked against the public sources of D36, and identifies each documented departure". No clause citation is required any more. | **Closed** |
| G0-F07 | L0-CON-030 rationale corrected | The Q-A1-01 sentence is gone; the rationale says the scope is D18 and the kinematic terms are decided under #81 (L2). The guidance names the #81 terms as the only exception, which matches D18 ("How this treats the rigid-body kinematic terms is open (#81)"). TBR closes at G2 (C1). | **Closed** |
| G0-F08 | L0-CON-310 scoped to airborne | Statement: "While the Aeronef is airborne, …". Glossary *Airborne* ("between the start of a run and ground contact") is consistent with CONOPS §4.2 ("Each run starts with the vehicle airborne. There is no take-off") and with ground contact ending the run. Guidance requires the landing-envelope acceleration limit to be consistent with P-SYS-120. P-SYS-120 proposal updated ("while airborne"). | **Closed** (wording nit in R-F05 d) |
| G0-F09 | 30 glossary terms merged | All the terms the finding listed are now defined (*Aeronef project*, *Automated test procedure*, *Reconstructed model*, *Control force, control moment*, *Crew-facing quantity*, *Withheld assessment scenario*, *Parallel efficiency*, *Force effector* as a synonym of *Effector*, *Test run*, *Test campaign*, *Simulation instance*, *Execution host*, *Evaluator*, *Protected design baseline*, *Manual trace register*, *Mode catalogue* "also called the autoflight mode catalogue", and more). Two proposals that live statements use were not merged, and two other L0 terms were never proposed. | **Closed with new issue** (R-F01, Minor) |
| G0-F10 | D43: all conventions Fixed | 73 CV items are "Fixed" (D43 or their own decision); CV-650 and CV-660 are "Deferred to L2 (G0-12, #54)". CONVENTIONS and GLOSSARY headers say Fixed at G0 (D43). | **Closed** |
| G0-F11 | Comparison wording removed | L0-OBJ-020, -120, L0-CON-200, -210 rationales are re-based on D15, D24 and D42. CONOPS SH-03, SH-04, N-220 (kept for later), N-250, §4.6 (row removed), SC-110 ("Recorded results") and SC-220 ("Out of scope this cycle") are aligned. Two "comparisons fair" phrases remain, and the out-of-scope SC-220 was the only scenario exercising the live need N-230. | **Closed with new issue** (R-F02, R-F05 a; Minor) |
| G0-F12 | D44: STP/REE-only records not childless | trace_check.py: `OUT_OF_SCOPE = {"STP", "REE"}` exempts records allocated only to those elements from CHILDLESS (tests added). The trace check now reports 40 CHILDLESS = 60 live minus the 20 STP/REE-only records, each of which says so in its rationale. Plan G4 exit amended; G1 to G3 have no childless exit. Glossary *Childless parent* excludes these records (D44), which reconciles the L0-SUC-150 statement. Two residues: L0-SUC-150 "at each baseline", and the exemption is not limited to L0. | **Closed with new issue** (R-F03, R-F04; Minor) |

### 1.2 Checklist Majors

| Record | Checklist issue | Verified | Verdict |
| --- | --- | --- | --- |
| L0-CON-030 | "any coupling" vs the #81 branch; TBR undated | As G0-F07. The guidance exception is exactly the D18 open point. TBR "closes at G2 (C1)". | **Closed** |
| L0-CON-290 | No condition, no crash outcome; TBR undated | Statement: "as a landing within the landing envelope and as a crash outside it". Guidance requires envelope limits and both outcomes. TBR "closes at G2". The envelope limits are TBD with no parameter ID yet, which is acceptable at L0 (set at a lower level). | **Closed** |
| L0-SUC-100, -120, -130 | "identified", "correctly", "covered" undefined; TBRs undated | Deferred with the REE scoring rules (D44, #69): TBD fields now "closes when the plan is extended to REE (D44)". *Reconstructed model* and *Withheld assessment scenario* are now in the glossary. The undefined scoring words are what the deferred TBDs will define. | **Closed** (accepted as deferred, D44) |
| L0-CON-270 | Unit case table in the statement; "speed" ambiguous; durations open | The statement now points to the CV-740 table, which names *horizontal speed* (and "any other speed shown to the crew"), fuel in lb and durations in h or min. "Hours or minutes" stays open by owner decision D34. No longer COMPOUND. | **Closed** |
| L0-CON-300 | Inspection cannot show "never exceeds"; no parameter | Guidance: "(Inspection) the effector requirements define a maximum force magnitude for each force effector as a parameter; (Test) no automated test run produces an effector force above it". Per-effector maxima TBD at C3 (G2). | **Closed** |

## 2. Minor findings: spot-check verdicts

| F-ID | Verified | Verdict |
| --- | --- | --- |
| G0-F13 | L0-OBJ-020, -140, L0-CON-250 no longer cite deleted records. L0-OBJ-160 and L0-SUC-140 mention "deletion of L0-CON-220 to -240" as history, which is intended. L0-ASM-020 and L0-ASM-140 Affects corrected. New DELETED-REF warning: 0 hits. | Closed |
| G0-F14 | "Wind is excluded" removed from L0-CON-090. The guidance separates forces (gravity, drag on the air-relative velocity including wind) from ground contact as "the only other external effect". | Closed |
| G0-F15 | L0-CON-020 cites D10 and D33; L0-CON-070 no longer says "is TBR"; L0-CON-210 cites D15 and D24; L0-SUC-040 tolerance sentence removed. No live record cites Q-A1 or issues.md. | Closed |
| G0-F16 | L0-ASM-140 Affects only Draft records (CON-250, SUC-140); accepted until #69. L0-ASM-130 still lists L0-SUC-050, which no longer concerns parallelism. | Accepted (residue in R-F05 c) |
| G0-F17 | Every open TBD/TBR now has a date or gate: CON-030 G2 (C1), CON-140 2026-11-30, CON-290 G2, CON-300 G2 (C3), CON-310 G1, SUC-060 2026-12-31, SUC-100 to -130 "when the plan is extended to REE (D44)". | Closed |
| G0-F18 | work/A1/param_proposals.md YAML holds only P-SYS-060, -070, -120. Withdrawn IDs are in prose, and the register table is regenerated from the live records (matches the TBD/TBR fields). Not done: the work/A2/param_proposals.md note "The database unit is always SI", which conflicts with D34 and CV-790. | Closed with new issue (R-F06) |
| G0-F19 | L0.md, CONOPS (status, date, D1 to D44 reference) and DECISIONS headers updated. | Closed |
| G0-F20 | CONOPS §4.2: altitude of the CG (CV-430); definitions cite the CVs; state knowledge cites L0-ASM-010. L0-ASM-050 Affects "CONOPS §4.2". | Closed |
| G0-F21 | CV-550 (D10, D33), §7 intro (D12), CV-630 and glossary *Selected course* (D14), glossary *VOR* (D12). | Closed |
| G0-F22 | Logged on #69 (comment seen). | Deferred (accepted) |
| G0-F23 | Logged on #89 (comment seen). | Deferred (accepted) |
| G0-F24 | CONOPS §5 common conditions and N-170 include the P-SYS-120 limit. | Closed (wording nit in R-F05 e) |
| G0-F25 | L0-CON-310 rationale: evaluation point set at a lower level. Second part not addressed: "g" is standard gravity, but model gravity P-DYN-010 is still TBD, so "hovering is 1 g" holds only if they are equal. | Partly closed (R-F06) |
| G0-F26 | L0.md "Descoped at G0" table covers the OBJECTIVES §2, §3, §4, §5 and §6 clauses. | Closed |
| G0-F27 | L0-OBJ-190 guidance: "and each requirement links to a verification procedure with a recorded result". | Closed |
| G0-F28 | Deferred with the REE scoring rules (D44). | Deferred (accepted) |
| G0-F29 | L0-SUC-040 guidance: "each run of one complete recorded campaign". | Closed |
| G0-F30 | L0-CON-120 guidance Demonstration; L0-CON-300 Inspection plus Test; L0-SUC-050 Type Functional. | Closed |
| G0-F31 | (a) Deleted records are skipped by lint and param_check (committed in e1e08d1). (b) DELETED-REF added, with a test. (c) STP/REE exemption added, with a test. (d) TBD/TBR date check and (e) param_check over specs/ are open for B2. | Closed for (a) to (c); (d), (e) deferred to B2 (accepted) |

## 3. New findings

None is Major. All can be closed by the moderator.

| F-ID | Location | Description | Major/Minor | Proposed fix |
| --- | --- | --- | --- | --- |
| R-F01 | GLOSSARY vs L0 statements (residue of G0-F09) | These L0 terms are still undefined. *Degree of freedom* appears in the statements of L0-OBJ-020, L0-CON-010, -020 and -030, and *Crew interface* in the L0-CON-170 statement. Both are in work/A1/glossary_proposals.md but were not merged, although live records use them. *Model specification* (MS-DYN) appears in the L0-OBJ-010 statement and in 14 places in total. *Verification matrix* is used in the L0-SUC-020 and -030 guidance, and *Crew station* in the L0-CON-150 guidance. | Minor | Add the five entries (DoF and crew interface from the A1 proposals; model specification → MS-DYN, METHODOLOGY §7; verification matrix → VCRM, METHODOLOGY §10; crew station → CV-170). |
| R-F02 | L0-CON-200, -210 guidance; CONOPS N-230, SC-220, §8 | (check) The guidance says "the flight-control-law design [autoflight implementation] is changed through configuration". There is only one design (D42) and one implementation (D24), so the child has nothing to change to unless a substitute is provided. Also, the live need N-230 (swap controllers, backed by L0-CON-200) is exercised only by SC-220, which is now out of scope. §8.1 still lists SC-220 as exercising N-220, N-230 and N-250, and §8.2 does not list N-230. | Minor | Guidance: "…is replaced through configuration by a substitute design (for example a test variant), and the vehicle model files are unchanged…". CONOPS: list N-230 (and the swap part of N-220) in §8.2, or keep SC-220's swap step in scope with a substitute law. |
| R-F03 | L0-SUC-150 statement and guidance | The statement and guidance say "at each baseline … no childless parent". Every intermediate baseline necessarily has childless records: L0-baseline-1 (40 CHILDLESS now, no L1), AER-L1-baseline-1 and AER-L2-baseline-1. Only G4 (AER-REQ-baseline-1) requires the check in the plan. The rationale does not cite D44, although the glossary *Childless parent* now carries the exemption. | Minor | Scope it to "the requirements baseline (AER-REQ-baseline-1, G4)" or "at each baseline, for the levels that have a level below them". Add "(D44, glossary *Childless parent*)" to the rationale. |
| R-F04 | tools/trace_check.py (`out_of_scope`) | The OUT_OF_SCOPE exemption applies at every level, but D44 exempts only "L0 requirements allocated only to STP or REE". An L1 or L2 AER record wrongly allocated to STP would be silently left unreported instead of flagged. | Minor | Apply the exemption only when `Level == "L0"`, and add a test with an L1 record allocated to STP that is still reported CHILDLESS. |
| R-F05 | Several records and specs (wording residue) | (a) "comparisons fair" is still in the L0-OBJ-110 and L0-ASM-020 rationales (G0-F11 theme). (b) The L0-SUC-050 rationale says "The campaign size makes 'large-scale' measurable" and then "accepted without a campaign size". (c) L0-ASM-110 Affects says "L0-CON-090 (ground reaction)" but omits L0-CON-290 and L0-CON-310, which rest on the ideal landing; L0-ASM-130 Affects still lists L0-SUC-050. (d) L0-CON-310 guidance: "is consistent with [P-SYS-120]" is vague. (e) CONOPS §5 writes "3 g", against its own §1.1 rule that system values never appear as numbers. (f) L0-CON-270 rationale cites a review finding "(G0-F05)"; a baselined record should cite D7, D9, D34 instead. (g) The GLOSSARY and CONVENTIONS headers still explain "TBR (Qn)" markings, though none remain; CV-250 keeps the label "Proposed use (G0-03)" on a Fixed item. | Minor | (a) "makes runs repeatable"; (b) delete the sentence; (c) Affects "L0-CON-090, L0-CON-290, L0-CON-310"; drop L0-SUC-050 from L0-ASM-130; (d) "does not exceed [P-SYS-120]"; (e) "within `[P-SYS-120]` (L0-CON-310)"; (f) drop "(G0-F05)"; (g) delete the TBR (Qn) sentence and relabel "Use (G0-03, D22)". |
| R-F06 | Staging inputs for B1, B2, I1, C1 | (a) work/A2/param_proposals.md says "The database unit is always SI", which conflicts with D34 and CV-790 (crew-facing parameters stored in crew units). B2 seeds from it. (b) work/A1/interface_needs.md still drives IN-A1-01 from L0-OBJ-100, IN-A1-04 and -06 from L0-CON-240, and IN-A1-05 from L0-CON-220 and -230 (all deleted), with a pointer to issues.md Q-A1-12. B1 and I1 read it. (c) G0-F25 second part: P-SYS-120 uses standard gravity, while model gravity P-DYN-010 is TBD. | Minor | (a) Correct the A2 note to CV-790 before B2. (b) Re-drive IN-A1-01 from L0-OBJ-110 and L0-SUC-040 only, IN-A1-04 and -06 from L0-OBJ-140 and -150 only, and mark IN-A1-05 deferred with #69 (G0-F22). (c) Record for C1: P-DYN-010 = 9.806 65 m/s², or note that the hover figure is approximate. |

## 4. Tool results (at d46831e)

| Check | Result | Assessment |
| --- | --- | --- |
| `python tools/assemble.py L0 --dry-run` | "L0: sections ASM, CON, OBJ, SUC already up to date" | In sync |
| `python tools/lint.py` | 0 errors, 17 warnings, all COMPOUND | 16 were judged "accept" in checklist_L0.md. L0-CON-270 is gone. **L0-CON-290 is new** (reworded statement) and was not judged. Re-inspector's judgement: accept (one thought): one classification rule with two complementary outcomes, not a tree of cases (D30). tools/LINT_GUIDE.md "each judged at G0" is true with this record. |
| `python tools/trace_check.py` | 40 errors, all CHILDLESS; 0 DELETED-REF; no orphan, duplicate or missing method | Expected: no L1 yet. 40 = 60 live minus 20 STP/REE-only records (D44). |
| `python tools/param_check.py` | 3 PARAM-MISSING: P-SYS-120 (L0-CON-310), P-SYS-060, P-SYS-070 (L0-SUC-060, Draft) | Expected: seeded at B2. |
| `python -m pytest -q tools/tests` | 38 passed | New tests cover the D44 exemption and DELETED-REF. |
| `python tools/vcrm.py --check` | 0 errors, 0 warnings | Clean |

These match the "Checks after rework" line in dispositions.md.

## 5. Gate G0 exit criteria and recommendation

Plan, Gate G0 exit: "no open major findings, conventions fixed, L0 baselined and tagged `L0-baseline-1`".

- **No open major findings: met.** All 12 inspection Majors and all 7 checklist Major records (5 rows) are closed. The checklist REE scoring items are accepted as deferred under D44. The new findings R-F01 to R-F06 are Minor.
- **Conventions fixed: met.** D43 is recorded. 73 CV items are Fixed and CV-650/660 are deferred to L2 (#54). The CONVENTIONS and GLOSSARY headers are Fixed.
- **L0 ready to be baselined: yes.** L0 is assembled and in sync. Every live record has the D41 verification and a dated TBD/TBR. The trace and parameter exceptions are the expected ones with a recorded basis (D44, B2). What remains is the owner's approval and the `L0-baseline-1` tag.

**Recommended exit decision: Rework, moderator closes.** The six Minor findings are wording, glossary and tooling fixes that need no owner ruling and no further review. R-F04 and R-F06 touch inputs that B1 and B2 read first, so they should be closed before Phase 2 starts. Once the moderator has closed them, the owner can approve and tag `L0-baseline-1`. If the owner prefers to baseline at d46831e as it stands, nothing found here makes L0 unsafe as a basis for B1: the residues would then carry as Minor items into the G1 inspection.
