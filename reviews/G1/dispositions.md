# Gate G1 — Finding dispositions

Rework of the findings in `inspection_B1.md` (G1-F01 to G1-F32) and `checklist_L1.md`, on branch `b2_params`, 2026-11-04. Author-side rework of task B1 (L1 Aeronef requirements, functional analysis, allocation, budgets).

**Owner rulings for this rework** (plan §9):

| ID | Ruling | Answers |
| --- | --- | --- |
| D59 | Repeat runs of the same configuration, initial condition and selection script give the same pass/fail verdicts and agree within stated tolerances; they are not required to be bit-identical (confirms D25). | G1-F09; checklist L1-AER-690 |
| D60 | The position-holding budget [P-SYS-450] is a horizontal position error, in Stationary and in Hover; the altitude error is covered by the altitude-hold tolerance. | G1-F06; checklist L1-AER-360, -460 |
| D61 | The body axes are the principal axes of inertia: zero products of inertia. | G1-F12; constrains L1-AER-220 |
| D62 | A gust or burst builds up over a minimum rise time (new parameter P-SYS-570, TBD, set at G2); no instantaneous steps; the budgets close against it. | G1-F08 |

**How the changes were made.** L1 records were edited in `work/B1/L1_AER.md` and assembled into `requirements/L1.md`; they stay Draft, Version 1. L0 records were changed through change requests CR-B1-07 to CR-B1-12 (`registers/CHANGE_REQUESTS.md`, all Applied), with Versions bumped and Status kept Baselined. New L1 records: L1-AER-850, -860 (split of -750), -870 (split of -500), -880 (flight control panel interface), -890 (navigation → autoflight interface). New parameter: P-SYS-570. New TBD/TBR rows: TT-650 to TT-730.

## Inspection findings

| F-ID | Sev. | Disposition |
| --- | --- | --- |
| G1-F01 | Major | **Fixed (D63, owner Q2).** Applied in the recommended form so that L2 is not misled meanwhile: L1-AER-310, -320, -330, -350 now state capabilities ("shall be able to sustain each horizontal speed up to [P-SYS-230]", "be able to climb at each vertical speed up to [P-SYS-240]", "descend at each vertical speed magnitude up to [P-SYS-250]", "change its heading at each heading rate magnitude up to [P-SYS-270]"). Each rationale says the record is a capability and that the tracking tolerance of a selected value is a per-mode L2 matter (P-AF-090, P-AF-120). |
| G1-F02 | Major | **Fixed (D53, CR-B1-07).** L0-CON-290 v3 (rationale and guidance: two speed limits at the contact sample), L0-CON-310 v6 (rationale: no touchdown shock, the vertical speed limit stands in for the impact; guidance clause on the envelope acceleration limit removed), L0-ASM-110 (assumption text). Glossary *Landing envelope* (CR-B1-11), CONOPS §4.2 (CR-B1-12), FUNCTIONAL_ANALYSIS F-AER-12 and I-08 aligned. |
| G1-F03 | Major | **Fixed (D56, CR-B1-08).** L0-OBJ-030 v3: rationale, children-must-show guidance and Source cite D56. Plan §1 cites D56. Glossary *Mode catalogue* no longer says "baselined" (CR-B1-11). |
| G1-F04 | Major | **Fixed.** "and mode status" removed from L1-AER-420; the rationale says only the axis references cross ICD-FC-AF, so no control law can depend on the mode logic (D15, D33, FA I-13). IN-B1-03 marked superseded; *Mode status* not merged into the glossary. |
| G1-F05 | Major | **Fixed.** New L1-AER-880 (Interface): the closed list of data crossing the flight control panel boundary (SI selections out; annunciation content, navigation quantities, fuel state in), allocated FCP, AF, NAV, FU, ICD `ICD-FCP`. New L1-AER-890 (Interface): navigation → autoflight through ICD-NAV-AF, allocated NAV, AF. FA §5.1 boundary table: FCP row added, NAV row cites L1-AER-890 and no longer the deleted -540; I-06, I-16, I-18, I-19 point to ICD-FCP. Plan §3 ICD list and task I1 add `icd/ICD-FCP.md`. New IN-B1-08. |
| G1-F06 | Major | **Fixed (D60).** L1-AER-460: "While autoflight holds the horizontal position over the ground in a wind within the wind envelope, … keep its horizontal position within [P-SYS-450] …"; rationale names Stationary and Hover and points the altitude error to P-AF-110. L1-AER-360: "While autoflight holds the horizontal position and the altitude with no wind applied …" (Stationary with Altitude hold, or Hover; altitude has no effect in still air). P-SYS-450, P-SYS-460, P-FC-010 descriptions, FA §7.3 and §7.4, CONOPS SC-090 and SC-100 aligned; glossary *Reference position*. |
| G1-F07 | Major | **Fixed.** L1-AER-390: "While the Aeronef is airborne with fuel remaining, …"; rationale explains the attitude is free after exhaustion (L1-AER-200); test guidance "in each automated test run, while fuel remains". |
| G1-F08 | Major | **Fixed (D62).** New P-SYS-570 (minimum gust rise time, TBD, TT-650, G2 with C1 and the TST wind model). New glossary term *Wind envelope* (steady wind ≤ [P-SYS-430] plus gusts ≤ [P-SYS-560], each built up over ≥ [P-SYS-570]); *Gust* amended (CR-B1-11). L1-AER-300, -310 and -460 are stated "in a wind within the wind envelope"; L1-AER-290 rationale states the budget closes for those winds. FA §7.2 has a disturbance share (the gust response is inside [P-FC-020]); §7.4 likewise inside [P-FC-010]. P-SYS-560 description, CONOPS §4.2, IN-B1-02 and IN-B1-07 updated. |
| G1-F09 | Major | **Fixed (D59).** L1-AER-690: "When a run is repeated with the same configuration, initial condition, crew selection script and TST step and wind inputs, the Aeronef shall produce operational data that give the same pass or fail verdict against each success criterion assessed on the run." Execution host dropped; TST inputs added (the second part of the finding). Rationale cites D59, notes that L0-ASM-020 is stronger than needed and that CR-B1-01 is applied. CONOPS SC-200 aligned. The reading of "stated tolerances" is confirmed in owner question Q4; the fix stands under either answer. |
| G1-F10 | Major | **Fixed.** `work/B1/issues.md`: status note; §3 (Q5 proposal) headed and boxed as superseded by D56 and "not an input to C5"; DD-040 marked superseded by D55; N-B1-04, -08, -09, -10 and the §7 rows for #6, #54, #55, #79, #80.3 updated. `work/B1/interface_needs.md` rewritten: VOR, flight-path-angle, position-hold, speed-mode and "mode status" material struck through and marked superseded; C5, C6, C7 rows rewritten; new C8 (FCP) row; IN-B1-08 (ICD-FCP). FA §9 no longer sends L2 agents to the Q5 proposal. |
| G1-F11 | Major | **Fixed.** 44 terms merged into `specs/GLOSSARY.md` in alphabetical order, corrected for D55 to D62 (for example *Initial condition* without VOR stations, *Reference position* on Stationary and Hover, *Flight software* with FCP, *Mode state* instead of *Mode status*). *Subsystem* lists FCP (CR-B1-11). *Control effectiveness* and *Command response* defined (see G1-F29). `work/B1/glossary_proposals.md` marked merged. |
| G1-F12 | Major | **Fixed (D61).** L1-AER-020 stated in acceleration terms ("produces an acceleration along another degree of freedom"), FU allocated, sufficiency covers drag, effectors and inertia. L1-AER-220: "derive, at each fuel state, a diagonal inertia tensor in the body frame …" (principal axes, D61). FA I-04, glossary *Mass properties*. |
| G1-F13 | Minor | **Fixed (CR-B1-09).** L1-AER-120 and -140 rationale and Source cite D57. L0-CON-020 v3 (D57). L0-ASM-050 rationale: "Stationary and Hover compensate for it (D56)". |
| G1-F14 | Minor | **Fixed.** L1-AER-690 and -700 rationales state CR-B1-01 and -02 as applied (D50). FA §8 regenerated from the Parent(s) fields: rows "TST, AER", count 18. L1-AER-520 rationale cites D49 and D55, no B1-Q09; Source "L0-CON-180; D49, D55". |
| G1-F15 | Minor | **Fixed.** FA header (date, D1–D62, rework note); §2 cites D49; §5.1 NAV row without -540; §7.4 N-B1-03 note dropped; §9 rewritten as open items only. |
| G1-F16 | Minor | **Fixed.** (a) F-13 diagonal moved to the F-13 column. (b) §5.1 diagram: the wind goes to the vehicle model only. (c) TM → TST edge carries operational data only. (d) F-AER-14 allocated to DYN, FU, FC, AF, FCP (NAV removed, it has no state to initialise); new I-28 (initial selector values to FCP), N² row F-14 and §3.3 TST → FCP updated; §6.1 aligned. |
| G1-F17 | Minor | **Fixed.** L1-AER-350 rationale: rotation adds no share to the crew budget (evaluated at the CG, D45). |
| G1-F18 | Minor | **Fixed.** L1-AER-470 rationale: FCP presents at each output sample, so its share is one output sample period [P-TM-010]; FA §7.5 likewise. CONOPS §4.4, §5 and SC-110 use [P-SYS-470] (CR-B1-12); P-AF-060 source and the CONOPS §9 row say it is the AF share. |
| G1-F19 | Minor | **Fixed.** L1-AER-430 allocated also to AF, FCP, NAV; "vehicle mass" → "mass properties" (vehicle mass, CG, inertia; glossary) so FC can use the inertia as it changes with fuel. L1-AER-680 adds the crew-selection function and FCP. L1-AER-660 adds FCP (initial selector values). FA §6.2 regenerated. |
| G1-F20 | Minor | **Fixed.** L1-AER-380 rationale: "FC (regulation and allocation) and EF (the effector geometry …)"; statement and rationale name the frame: "along each other body axis" (D18 body frame; D56, D57). L1-AER-020 rationale attributes allocation to FC. P-SYS-540 description aligned. |
| G1-F21 | Minor | **Fixed.** L1-AER-360 cites [P-FU-040] and lists it. P-SYS-280 (no D3 mode name), P-AF-120 (Heading, no SPD mode), P-AF-090, P-SYS-450 (gusts, horizontal) descriptions updated; P-AF-210 and -220 sources no longer cite L1-AER-450. |
| G1-F22 | Minor | **Fixed (CR-B1-10).** P-AF-010 to -040 carry the FCP ownership note. CV-780: requirement matter for FCP, parameters P-TM-020 to -050 (P-TM-060, -070 withdrawn), status Changed. |
| G1-F23 | Minor | **Fixed (CR-B1-12).** (a) Manual control: CONOPS §1, §4.3, N-180, §8.2 and plan §1 say there is none (D49, D55). (b) Rate: §4.6, N-340 and SC-200 step 4 use the output sample [P-TM-010]. (c) Classification: §4.6, N-030, glossary *Operational data* (CR-B1-11), plan C7 and §7 defer it to the RVS (#69). (d) §1.1 and §9 point to PARAMETERS.yaml and the fixed conventions; §9 adds P-SYS-120, -430, -470, -560, -570, P-TM-010. (e) §4.1 includes the flight control panel. (f) SC-220 "SC-020 to SC-120". |
| G1-F24 | Minor | **Fixed.** L1-AER-280 Type Functional. L1-AER-790 Type Performance, like its parent L0-SUC-020. L1-AER-710 test guidance measures the time from a change of vehicle state to the first responding change of effector output. |
| G1-F25 | Minor | **Fixed.** The 68 allocated L1 records cite "(D40, D58)" in Verification and "Children must show (D58)" in the rationale; the section introduction cites D40, D58. The procedure IDs ("Inspection — TBD") are registered once as TT-690 (Phase 5, V4, G4). |
| G1-F26 | Minor | **Fixed.** Plan: Phase 3 "Eight agents"; G2 eight lint agents and FCP in the second inspector's scope; V3 covers FCP; §10 rows (Opus ×8, Haiku ×8; Phase 4 "1, then 5", Opus ×3 (M3, M8, FC1), Sonnet ×2). `requirements/L2.md` and `L3.md` have an FCP section between AF and NAV. |
| G1-F27 | Minor | **Fixed.** Glossary *Operating volume* with P-SYS-210, -200, -220; L1-AER-310 lists them and its test guidance names the minimum and maximum operating altitudes (P-SYS-200 to -220 no longer PARAM-UNUSED). |
| G1-F28 | Minor | **Fixed.** L1-AER-470: "When the mode state or a target changes, …"; glossary *Mode state* covers armed, active, leaving the armed state and disengagement. L1-AER-500 split: unit assignment stays, the CV-750 conversion is new L1-AER-870 (FCP). L1-AER-750 split: see checklist L1-AER-750. |
| G1-F29 | Minor | **Fixed.** Glossary *Control effectiveness*: control force and moment about the CG per unit of effector command, which carries the point of application and the moment arm; *Command response*, *Output limits*, *Consumption parameters* defined. L1-AER-100 rationale says so. |
| G1-F30 | Minor | **Fixed.** Glossary *Display format* (layout, graphics, symbology; not value resolution or rounding, CV-780). L1-AER-510 rationale states that FCP resolution and rounding requirements do not breach it. |
| G1-F31 | Minor | **Fixed.** L1-AER-670: "Each time the TST commands a step, the Aeronef shall advance its vehicle model by one simulation step of [P-SYS-300] with the wind velocity that the TST gives with that command"; test guidance checks the air-relative velocity of each step. FA I-25 cites it. |
| G1-F32 | Minor | **Fixed.** DECISIONS.md header D1–D62. L0.md "Changed since" lists every CR-B1 change. CONVENTIONS §0 without "VOR definitions", header no longer defers CV-650/660, Related D7–D62, G0-12 Withdrawn (CR-B1-10). Closing GitHub #54 is left to the orchestrator (no GitHub action in this rework). |

## Checklist findings

| Record | Sev. | Disposition |
| --- | --- | --- |
| L1-AER-330 | Major | **Fixed (D56).** Not escalated: D56 settles it (Go to altitude and Vertical speed arm Altitude hold, which levels off at the selected altitude). The levelling clause is removed from the criterion; the rationale says levelling is mode logic and that the selectable altitude is bounded below by [P-SYS-210] (L2, C8). "Minimum operating altitude" is now inside the glossary *Operating volume*. |
| L1-AER-690 | Major | **Fixed (D59)** with G1-F09. |
| L1-AER-360, -460 | Major | **Fixed (D60)** with G1-F06. |
| L1-AER-460 | Minor | **Fixed.** The test guidance gates the check "at each output sample from [P-SYS-460] after the start of the hold". |
| L1-AER-370 | Minor | **Fixed.** Guidance: the degree of freedom settles on its reference within the tracking tolerance and settling time the FC children state as parameters (C4), the others staying within the L1-AER-380 tolerances. The statement stays functional; its measures are L1-AER-380 and the L2 children. |
| L1-AER-220 | Minor | **Fixed.** "elongated" and "simplified" removed from the statement ("from the body shape and the mass distribution that MS-DYN states"); the rationale says the shape dimensions are DYN parameters set by C1. No shape parameter is invented at L1. D61 applied (diagonal tensor). |
| L1-AER-020 | Minor | **Deferred** to #81 (C1, G2; TT-330). The exception stays named until MS-DYN lists the retained terms. The record is restated in acceleration terms (G1-F12). |
| L1-AER-450 | Minor | **Fixed.** "baselined" removed from the statement; glossary *Mode catalogue* likewise (CR-B1-11). |
| L1-AER-640 | Minor | **Fixed.** "its navigation quantities" → "its altitude, horizontal speed, vertical speed, heading and track". |
| L1-AER-530 | Minor | **Fixed.** Criterion "inside the validity range of CV-580"; glossary *Validity range*. |
| L1-AER-120, -140 | Minor | **Fixed (D57)** with G1-F13. |
| L1-AER-390 | Minor | **Fixed.** "A2-Q03" replaced by #89, the issue under which the ConOps mode readings (A2-Q03 among them) are parked for C5; A2-Q03 has no GitHub issue of its own. |
| L1-AER-060 | Minor | **Fixed.** Rationale cites the glossary *Sensed acceleration* instead of the literal "1 g"; TBD/TBR field without the value (see systemic row). |
| L1-AER-140 | Minor | **Fixed.** The "margin" is now a named term: the moment to hold pitch and roll at zero against the drag moment, a line of FA §7.1 sized at I1. |
| L1-AER-520 | Minor | **Fixed** with G1-F14: "The flight control panel is the only crew input (L0-CON-180, D55) … No manual-control requirement is written at L1 (D49)." |
| L1-AER-830 | Minor | **Fixed.** Rationale: "OBJECTIVES §1: the assessment of the AI-assisted methods is an objective in its own right, because the project exists to try those methods." |
| L1-AER-800 | Minor | **Fixed.** "last requirement layer" → "lowest requirement level of each subsystem branch"; the rationale defines it by D4. |
| L1-AER-820 | Minor | **Fixed.** "When the requirements baseline is approved, the Aeronef shall contribute to the final test report …"; *Requirements baseline* and *Final test report* are glossary terms. |
| L1-AER-840 | Minor | **Fixed.** TBD/TBR field records the deferral of abnormal and emergency procedures (Martin, closes when failures are introduced, #85); TT-730. |
| L1-AER-630 | Minor | **Accepted.** The closure cannot be a G2 gate: D44 and #69 defer the classification to the RVS plan extension. The field now reads "closes when the plan is extended to the RVS (D44)", the form the L0 RVS items use (TT-290 to TT-320). |
| L1-AER-750 | Minor | **Fixed** (also G1-F28). Split three ways: L1-AER-750 (one level file per level), new L1-AER-850 (each record states its level; lint LEVEL, ID-FORMAT), new L1-AER-860 (each record traces to its parents or, if derived, to its design decision; trace ORPHAN, DERIVED). All leaves on L0-OBJ-180. |
| L1-AER-750 to -830 (subject) | Minor | **Accepted (D63, owner Q1):** kept at L1 as leaves. The wording findings on these records are fixed above; whether they belong at L1 is a scope question. |
| Systemic: terms not in the glossary | Minor | **Fixed** with G1-F11. Each term listed is now defined, or reworded: "operating altitude range" (L1-AER-310 guidance now names the minimum and maximum operating altitudes), "minimum operating altitude" (L1-AER-330), "navigation quantities" (L1-AER-640). |
| Systemic: values in TBD/TBR fields | Minor | **Fixed.** L1-AER-060, -300, -460, -470, -570, -600, -670, -680, -710 cite the parameter, its status and its TT row, with no value. Values live only in PARAMETERS.yaml. The inspection's §5 list of fields that named only the record's own parameter (L1-AER-120, -290, -300, -310, -460, -470) is completed the same way. |
| Systemic: documents cited that do not exist | Minor | **Fixed.** TT-660 (MS-DYN, C1, G2), TT-670 (AF_MODE_LOGIC, C5, G2), TT-680 (ICD-AER-TST, ICD-FC-AF, ICD-NAV-AF, ICD-FCP and the vehicle-model boundary ICD home, I1, G2). L1-AER-430 field records the ICD home (TT-720). |

**COMPOUND verdicts (checklist §2).** The 42 "accept" verdicts stand; the one "split" (L1-AER-750) is done. Statements changed or added at this rework that the lint flags, all judged one thought (D30): L1-AER-360 (one hold condition, horizontal position and altitude), -470 (mode state or target, one response), -500 (unchanged list), -690 (the inputs that define one run), -860 (the two values of one trace attribute), -870 (one conversion rule, both directions), -880 and -890 (closed lists at one boundary, as L1-AER-430).

## Other items from the inspection (§2, §5)

| Item | Disposition |
| --- | --- |
| L0-CON-100 reading (N-B1-08; §2 sufficiency table, §5) | **Accepted (D63, owner Q3):** no change request; TT-700 closed. |
| TT-270 opened for a closed field | **Fixed.** Status Closed (D45). |
| TT-600 closure "RVS plan extension" | **Accepted** with checklist L1-AER-630. |
| Roll-up procedure IDs not registered | **Fixed** with G1-F25 (TT-690). |
| Vehicle-model boundary ICD home (IN-B1-01, N-B1-07) | **Deferred** to I1 (G2): TT-680, TT-720. |
| DD-010, DD-020 not in DECISIONS.md | **Accepted** at this stage (DERIVED errors); the orchestrator enters them in the register. |
| PARAM-UNUSED (19) | **Accepted.** P-NAV-010, -030 and P-TM-020 to -050 are cited by CONVENTIONS and belong to NAV and FCP requirements at L2 (C6, C8); P-AF-010 to -040, -090, -100, -120 to -140, -170, -190, -210, -220 are ConOps and mode parameters for L2 and Phase 4 (D33). |

## Checks after rework

- `python tools/assemble.py L1`: sections AER assembled (no other level changed; the stale `work/A1/L0_*.md` drafts were re-synced from `requirements/L0.md`, see notes).
- `python tools/lint.py`: 0 errors, 66 warnings, all COMPOUND (17 on L0, decided at G0; 49 on L1, decided above and in the checklist).
- `python tools/trace_check.py`: 70 errors, all accepted at G1: 68 CHILDLESS (the 68 L1 records allocated to subsystems; no L2 yet) and 2 DERIVED (L1-AER-680 DD-010, L1-AER-710 DD-020). No L0 record allocated to AER is childless.
- `python tools/param_check.py`: 0 errors, 19 warnings, all PARAM-UNUSED (down from 23; P-SYS-200, -210, -220 and P-AF-110 are now referenced).
- `python tools/vcrm.py`: wrote `verification/VCRM.md` (145 requirements); `--check` clean.
- `python -m pytest -q tools/tests`: 39 passed.

## Notes for the orchestrator

- **Stale L0 drafts.** `work/A1/L0_*.md` predated CR-B1-04 to -06, so `assemble.py L0` or `--all` would have reverted the applied CRs. They are now re-synced from `requirements/L0.md`, so the assembler reports L0 up to date.
- The `requirements/L1.md` header (outside the section) still reads "Draft (task B1, 2026-10-28)"; it was not edited, per the rule that L1.md is only assembled.
- GitHub #54 (VOR deviation sign) is moot under D56 and can be closed.
- ICD-FCP was added to the plan §3 list and task I1 as the author's fix for G1-F05; it can be folded into ICD-FC-AF and ICD-NAV-AF instead if the owner prefers (L1-AER-880 would then name those ICDs).
- Plan §9 (D59 to D62) was not touched; the edits to the plan are in §1, §3, §6 (C7, I1, Phase 3, G2, V3), §7 and §10.

## Questions for the owner

**Answered by the owner on 2026-11-04 (D63):** Q1 keep at L1; Q2 each value up to the maximum; Q3 and Q4 accepted as recommended; ICD-FCP kept as a separate ICD.

| Q | Question | Recommended answer | Findings |
| --- | --- | --- | --- |
| Q1 | **Subject of the process and document records.** L1-AER-750 to -830 (and the new -850, -860) have the Aeronef as subject but state project process and documents (one level file per level, peer review, trace check, final test report, method assessment). Keep them as Aeronef-branch leaves at L1, or move them to the plan and make their L0 parents (L0-OBJ-180, -190, -200, -210, L0-SUC-010, -020, -030, -150, -170) leaves checked directly, as D54 did for L0-CON-160? | **Keep them as L1 leaves (`Allocated to: —`) with the Aeronef as subject.** Their L0 parents are allocated to AER, so each needs an Aeronef child (D44, D58); the leaves are already verified directly and cost nothing at L2. Moving them would need nine L0 change requests for no gain in verifiability. | Checklist L1-AER-750 to -830 |
| Q2 | **Form of the envelope records.** Should L1-AER-310, -320, -330, -350 say the Aeronef can fly **each value up to** the maximum (the whole selectable range), or **at least** the maximum? | **"Each value up to the maximum"** (applied provisionally). It matches the D56 selectors "from zero to the vehicle's maximum", so the whole selectable range is a tested capability; "at least" would test only the top. The per-mode tracking tolerances stay at L2. | G1-F01 |
| Q3 | **Reading of L0-CON-100.** Its guidance asks for "an initial fuel quantity as a parameter". L1 reads it as the capacity [P-FU-010] (a parameter) plus the initial fuel of each run's initial condition (L1-AER-150), so tests can start at any fuel state (N-310). Accept the reading, or raise a CR for a fixed initial quantity? | **Accept the reading; no CR.** The reference mission still starts at [P-FU-010] (full fuel), and other scenarios need other fuel states. Close TT-700. | Inspection §2, §5 (N-B1-08) |
| Q4 | **"Stated tolerances" in D59.** Are they the tolerances of each success criterion, or a separate run-to-run tolerance on the operational data (a new parameter)? | **The tolerances of each success criterion; no new parameter.** The verdict is what the tests and the RVS use; a separate data tolerance would need one value per signal and adds nothing the criteria do not already bound. L1-AER-690 is written this way. | G1-F09 (clarification) |

## Moderator closure of the re-inspection findings (2026-11-04)

`reviews/G1/reinspection.md` closed all 15 Majors and recommended **Baseline**, with seven new Minors for the moderator. Closed by the orchestrator:

| F-ID | Disposition |
| --- | --- |
| G1-R01 | **Fixed.** DD-010 and DD-020 entered in `registers/DECISIONS.md` (DD-010 updated for FCP: order FCP → NAV → AF → FC). trace_check no longer reports DERIVED errors, so L1-AER-860 meets its criterion. |
| G1-R02 | **Fixed.** L1-AER-330 Source no longer cites the withdrawn SC-030. |
| G1-R03 | **Fixed.** Glossary adds *Navigation quantities* (with their validity, CV-580). |
| G1-R04 | **Fixed.** FA §4.2 and DD-010 name FCP; FA §5.3 FCP list adds -430 and -690; CV-580 names FCP (CR-B1-13); L1-AER-880 rationale says the fuel state is defined once at the vehicle-model boundary (L1-AER-430) and ICD-FCP refers to it. |
| G1-R05 | **Fixed.** L1-AER-480 test guidance asks for the same pass/fail verdict (D59). |
| G1-R06 | **Fixed.** DECISIONS.md and FA header cite D1–D63; FA §9 and interface_needs.md §3 say the owner questions are answered. FA header no longer points to the draft (G1-F15 residue). |
| G1-R07 | **Fixed.** ConOps §9 drops "3 g"; CR-B1-12 lists SC-090, SC-100 and cites D60, D62; glossary *Mode state* no longer says "disengaged". |

Checks after closure: lint 0 errors, 66 COMPOUND warnings (judged); trace 68 CHILDLESS only (no L2 yet); param 0 errors, 19 PARAM-UNUSED; vcrm clean; 39 tests pass. **Exit decision: Baseline.** Approved by the owner on 2026-11-04; 85 L1 records Baselined; tagged `AER-L1-baseline-1`.
