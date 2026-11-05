# Gate G1 inspection — B1 (L1 Aeronef requirements, functional analysis, allocation, budgets)

```markdown
Artifact / version:   requirements/L1.md (section AER, 80 live records; L1-AER-230, -340, -540, -550 Deleted)
                      + specs/FUNCTIONAL_ANALYSIS.md, at branch b2_params, commit b0a96de
                      (read with them: requirements/L0.md (L0-baseline-1 plus CR-B1-01 to -06), specs/CONOPS.md,
                      specs/CONVENTIONS.md, specs/GLOSSARY.md, parameters/PARAMETERS.yaml, registers/*;
                      staging work/B1/* read as supporting material only)
Review type:          Inspection (IEEE 1028; METHODOLOGY §11.3, checklists §13.1–13.2)
Moderator / author / reader / recorder / reviewers:
                      moderator: orchestrator / author: task B1 (owner: Martin) /
                      reader, recorder, reviewer: independent Opus inspector (did not author any of the material)
Date:                 2026-11-04
Entry criteria met:   yes, with notes:
                      - L1.md is in sync with work/B1/L1_AER.md (assemble.py L1 --dry-run: "sections AER already up to date").
                      - lint: 0 errors, 62 COMPOUND warnings (14 on L0, 48 on L1; warnings only, D30).
                      - trace_check: 67 errors = 65 CHILDLESS (exactly the 65 live L1 records allocated to subsystems;
                        no L2 yet) + 2 DERIVED (L1-AER-680 DD-010, L1-AER-710 DD-020; register empty). Accepted.
                        No L0 record allocated to AER is childless; the 18 TST/RVS-only L0 records are exempt (D44).
                      - param_check: 0 errors, 23 PARAM-UNUSED. Not all are ConOps-only: P-NAV-010, P-NAV-030
                        (CV-580) and P-TM-020 (CV-780) are cited only by CONVENTIONS; P-TM-030, -040, -050 are cited
                        by no file (CV-780 names the range "P-TM-020 to P-TM-070"); P-SYS-200, -210, -220 are the
                        bounds of the "operating volume" that L1-AER-310 to -350 rely on (G1-F27).
                      - vcrm --check: clean.
                      - Header of L1.md still "Draft (task B1, 2026-10-28)"; FUNCTIONAL_ANALYSIS header cites D1–D44.
                      - An untracked Haiku checklist record (reviews/G1/checklist_L1.md) exists in the working tree.
                        It was not an input to this inspection; overlaps are noted in section 6.
Findings:             table below
TBD/TBR list checked: yes (see section 5)
Exit decision:        Rework and re-review (recommended; see section 7)
```

Inputs read in full: AIRCRAFT_REQUIREMENTS_PLAN.md (incl. §4, Phase 2, Gate G1, §9 D1–D58), METHODOLOGY.md §8–§13, requirements/L0.md, requirements/L1.md, specs/FUNCTIONAL_ANALYSIS.md, specs/CONOPS.md, specs/CONVENTIONS.md (§4–§8), specs/GLOSSARY.md, parameters/PARAMETERS.yaml, registers/TBD_TBR.md, CHANGE_REQUESTS.md, DECISIONS.md, work/B1/*, reviews/G0/inspection_A1-A3.md; OBJECTIVES.md and AIRCRAFT_CHARACTERISTICS.md skimmed. Decisions D1–D58 are taken as settled; findings flag where an artifact contradicts or fails to implement one. Mode detail in the ConOps (parked for L2, #89) is flagged only where it contradicts L1 or a decision.

## 1. Findings

Severity: **Major** = would mislead L2 work, a real conflict or contradiction, or an unverifiable requirement. **Minor** = wording, polish, small inconsistencies. "(check)" marks a finding the inspector is less certain of.

| F-ID | Location | Description | Major/Minor | Proposed disposition |
| --- | --- | --- | --- | --- |
| G1-F01 | L1-AER-310, -320, -330, -350 `Statement` | The envelope records are written as unconditional states, not capabilities. "While in level flight in the operating volume … the Aeronef shall sustain a horizontal speed of [P-SYS-230] under autoflight"; "While climbing … shall sustain a vertical speed of [P-SYS-240]"; "While in the operating volume, the Aeronef shall sustain a heading rate of [P-SYS-270] under autoflight". Read literally, the Aeronef must always fly at the maximum speed when level, always climb at the maximum rate, and always rotate at the maximum heading rate. That contradicts every hold (L1-AER-460, Stationary, Altitude hold) and the selectors from zero to the maximum (D56). There is no "at least", "up to" or tolerance, so the statement cannot be tested as written; only the rationale ("the limit is the top of the selectable horizontal speed") shows the intent. Compare L1-AER-120: "shall be able to produce … of at least". | Major | Rewrite as capabilities, e.g. "…the Aeronef shall be able to sustain a horizontal speed of at least [P-SYS-230] under autoflight", and give the tolerance or the settling condition (or say that the per-mode tolerances of L2 apply). Same for -320, -330, -350. |
| G1-F02 | L0-CON-290 rationale; L0-CON-310 rationale and "Children must show"; L0-ASM-110; GLOSSARY *Landing envelope*; CONOPS §4.2; FUNCTIONAL_ANALYSIS F-AER-12, I-08 | D53 ("There is no acceleration limit … P-SYS-520 is withdrawn") is implemented in L1-AER-280 but not upstream or in the analysis. L0-CON-290: "Children must show (D41): (Inspection) the model specification defines … a landing envelope of velocity and acceleration limits". L0-CON-310: "the landing envelope's own acceleration limit covers ground contact" and "Children must show: … the acceleration limit of the landing envelope (L0-CON-290) does not exceed [P-SYS-120]". L0-ASM-110: "(limits on velocity and acceleration at contact)". Glossary: "The limits on velocity and acceleration at ground contact". CONOPS §4.2: "(limits on velocity and acceleration)". FA F-AER-12 inputs "Vehicle state, sensed acceleration", I-08 "sensed acceleration at contact". At roll-up, L0-CON-290 and -310 would be checked against guidance that L1-AER-280 and the L1-AER-290 sufficiency ("contact adds no further share") contradict. | Major | Raise a CR against L0-CON-290, L0-CON-310 and L0-ASM-110 (as CR-B1-05 did for L0-ASM-030): envelope = vertical and horizontal speed at the contact sample (D53). Align the glossary, CONOPS §4.2, and FA F-AER-12 and I-08. |
| G1-F03 | L0-OBJ-030 rationale and Source; plan §1 | L0-OBJ-030, the parent of L1-AER-450 and twelve other L1 records, still names the replaced catalogue: "The initial mode catalogue is fixed by plan decision D3" and "Children must show (D41): (Inspection) each mode of the baselined mode catalogue (D3) is covered by a requirement in the Aeronef branch". Its Source is "AIRCRAFT_REQUIREMENTS_PLAN.md §9 D3". D3 is replaced by D56, so the roll-up of L0-OBJ-030 at G4 would check coverage of VOR tracking, flight path angle and track hold, which no longer exist. L1-AER-450 correctly cites D56. Plan §1 also says "The autoflight mode catalogue in Section 9, D3". | Major | CR against L0-OBJ-030: cite D56 in the rationale, the children-must-show note and the Source. Fix plan §1. |
| G1-F04 | L1-AER-420 `Statement`; FUNCTIONAL_ANALYSIS §3.2 I-13, §4.1, §5.1; work/B1/glossary_proposals *Mode status* | L1 and the architecture disagree on the AF→FC interface. L1-AER-420: "The Aeronef shall pass the axis references and mode status from autoflight to flight control through the one interface defined in ICD-FC-AF". FA I-13 carries only "Axis references for the six degrees of freedom"; §5.1: "Autoflight → flight control \| Axis references, the same for any law (D15)"; §4.1: "Autoflight sits outside the flight-control loop and changes only its references (D15)". Sending mode status to FC invites control laws that depend on the mode logic, against D15 ("The modes say how the aircraft flies; the controllers implement them, so the two are decoupled") and D33. It also fixes ICD-FC-AF content at L1. The only definition is a staging proposal ("for example whether autoflight is engaged"). | Major | Owner or author decides. Either drop "and mode status", or define it in FA I-13 and §5.1 (for example "autoflight engaged / not engaged" only) and state in the rationale why FC needs it. |
| G1-F05 | FUNCTIONAL_ANALYSIS §5.1 boundary table, §3.2 I-16, I-18, I-19; plan §3 ICD list; L1 Interface records | The FCP boundaries, new with D55, have no L1 interface requirement and no ICD. §5.1 lists four boundaries ("each is an L1 interface requirement"). None covers FCP ↔ AF (I-19 "Mode selections, targets in SI \| FCP → AF", with no ICD; I-16 "Annunciation content … \| AF → FCP (ICD-AER-TST for the output)"), NAV → FCP (I-18, indications) or FU → FCP (I-06). Plan §3 plans only ICD-AER-TST, ICD-FC-AF and ICD-NAV-AF. C5, C6 and C8 are coupled agents (plan §6) and will have no shared definition of the selections or the annunciation content. Also, the "Navigation → autoflight" boundary is backed only by L1-AER-530, which is Functional, and by the deleted L1-AER-540. | Major | Add an L1 interface record for the panel ↔ autoflight boundary (selections in SI, annunciation content), and name its ICD (new ICD-FCP-AF, or sections of ICD-FC-AF and ICD-NAV-AF). Extend §5.1 with the FCP rows. Remove L1-AER-540 from the NAV row and decide whether NAV → AF needs its own Interface record. Update the plan §3 ICD list. |
| G1-F06 | L1-AER-460 `Statement`; L1-AER-360; P-SYS-450 description; FUNCTIONAL_ANALYSIS §7.4; CONOPS SC-040, SC-090 | After D56, "fixed position" does not say which position. L1-AER-460: "While autoflight holds a fixed position … keep its position within [P-SYS-450] of the reference position". D56 splits the hold: *Stationary* "holds the horizontal position over the ground" with any vertical mode; *Hover* holds "the height and the position". It is not clear whether P-SYS-450 bounds the horizontal or the three-dimensional error. The ConOps applies it to the horizontal position during a climb ("SC-040 … STAT · V/S … The horizontal position stays within [P-SYS-450]"), which 460's condition ("holds a fixed position") does not cover, and keeps the altitude error separate (P-AF-110). §7.4 and P-SYS-450 ("distance between the vehicle position and the reference position") do not say. L1-AER-360 ("While holding a fixed position with no wind applied") has the same gap (SC-110 variation uses Go to hover then Hover). | Major | State the dimension: e.g. "While autoflight holds the horizontal position, … keep its horizontal position within [P-SYS-450] …", which applies whatever the vertical mode. Align P-SYS-450, §7.4, SC-040 and SC-090. Say which hold L1-AER-360 means (at what height). |
| G1-F07 | L1-AER-390 `Statement` vs L1-AER-200, L1-AER-300; CONOPS SC-110 leg 11 | Real conflict at fuel exhaustion. L1-AER-390: "While airborne, the Aeronef shall hold its pitch angle and its roll angle within [P-AF-180] of zero." L1-AER-200: "When the remaining fuel mass reaches zero, the Aeronef shall produce zero control force and zero control moment." After exhaustion the vehicle is still airborne. SC-110 leg 11 says it "keeps the angular rate it had at exhaustion", and any drag moment (an attitude-dependent drag is allowed by the L1-AER-070 rationale) changes the attitude with no means to correct it. L1-AER-300 is correctly scoped "While the Aeronef is airborne with fuel remaining"; 390 is not. Its test guidance ("in each mode of the catalogue") is narrower than its statement. | Major | "While the Aeronef is airborne with fuel remaining, …" (or "while autoflight is engaged"). |
| G1-F08 | L1-AER-300, -310, -460; P-SYS-560 description; FUNCTIONAL_ANALYSIS §7.2, §7.4; registers/TBD_TBR.md | (check) The gust disturbance is bounded in size only, so two budgets cannot close. L1-AER-300 limits the vehicle acceleration to [P-SYS-440] "while airborne with fuel remaining", and L1-AER-460 requires [P-SYS-450] "with … gusts of at most [P-SYS-560]" (50 kt). P-SYS-560: "The gust shape (onset and duration) is defined in MS-DYN and set by the TST for each run". A gust step faster than the control-loop latency [P-SYS-480] gives a drag-force step that accelerates the vehicle before FC can respond. That acceleration depends on the gust shape and the drag, not on the design, so neither L1-AER-300 nor the 1 m hold can be shown to hold for "any gust of at most 50 kt". §7.2 has no disturbance share. No TBD records the gust shape. | Major | Open a TBD for the gust shape bound (onset rate and duration; owner Martin; closure G2, C1/MS-DYN). Add a disturbance share to §7.2 and §7.4, or scope L1-AER-300 to commanded manoeuvres and transients. State the gust class that L1-AER-310 and -460 are tested against. |
| G1-F09 | L1-AER-690 `Statement`, rationale, children-must-show; D25; L0-SUC-040; L0-ASM-020 | (check) Possible conflict with D25. D25: "Runs are not checked for bit-identical results, which is out of scope and too costly. A repeated run must give the same expected result." L0-SUC-040 follows it ("same verification result"). L1-AER-690: "shall produce identical operational data from an identical configuration, initial condition, crew selection sequence and execution host", with the test "two executions of the same run on one host give identical operational data". The rationale narrows D25 to "Bit-identical runs are not checked across hosts (D25)". D25 does not say "across hosts". L0-ASM-020 does assume identical outputs on one host, so both readings have support. Separately, the input list leaves out the TST inputs (the wind and the step commands of L1-AER-670), and the list is presented as complete. | Major | Owner rules between "identical operational data on one host" (and records it against D25) and "the same verification result" (L0-SUC-040 wording). Add the TST step and wind inputs to the condition. |
| G1-F10 | work/B1/issues.md §3; FUNCTIONAL_ANALYSIS §9; work/B1/interface_needs.md (C5, C6, C7 rows, IN-B1-02, IN-B1-04, §3); issues.md §5 DD-040 | Superseded material is still given to the L2 agents and to I1. issues.md §3, the Q5 proposal, has three groups with FPA, TRK, VOR, POS HOLD and SPD and is built on D3, D11 and D13 ("It respects D11 … D13"). It is not marked superseded by D56. FA §9 sends the reader there ("the Q5 (#6) proposal are in work/B1/issues.md"). interface_needs C5 row: "Q5 proposal (issues §4) as input to AF_MODE_LOGIC". C6 row: "flight path angle at each control frame; VOR radial … stations from the TST … L1-AER-340, -440, -450, -530 to -550". IN-B1-02: "VOR stations". IN-B1-04: "the selected VOR station and selected course". C7 row gives TM the annunciations, indications and crew units, which D55 gave to FCP. There is no C8 row. DD-040 still says "crew input in AF and crew presentation in TM (no FCP subsystem)". | Major | Mark issues.md §3 and DD-040 as superseded (D56, D55). Remove the pointer in FA §9, or point to D56. Rewrite the interface_needs rows (C5, C6, C7, IN-B1-02, -04), add a C8 row, and remove the deleted records. |
| G1-F11 | specs/GLOSSARY.md vs L1 statements; work/B1/glossary_proposals.md | Terms used in L1 statements are not in the glossary (METHODOLOGY §8.4 rule 12, §13.1). This is the same defect as G0-F09. The B1 proposals were not merged. Examples: "indications" (L1-AER-490, -500; "indicate", -560), "operating volume" (-310 to -350), "vehicle state" (-430, -440, -640, -710), "vehicle model", "flight software" (-430), "axis references", "axis demands", "effector commands", "effector outputs" (-630), "fuel state", "vehicle mass" (-430), "fuel mass flow" (-160, -190), "remaining fuel mass", "dry mass" (-180), "vehicle acceleration" (-300), "reference position" (-460), "initial condition" (-150, -660), "crew selection" (-480, -610), "mode status" (-420), "heading rate" (-350), "control effectiveness", "command response" (-100). The glossary *Subsystem* entry still lists seven subsystems without FCP (D55). The proposals are partly stale: *Initial condition* "… and the VOR stations of the run"; *Reference position* cites "Glossary *Position Hold*; D11"; *Flight software* omits FCP; "The mode that does it is *Position Hold* at L2". | Major | Merge the proposals after correcting them for D55, D56 and D57. Add FCP to *Subsystem*. Add "control effectiveness" and "command response", or reword L1-AER-100. |
| G1-F12 | L1-AER-020 `Statement` and allocation vs L0-CON-030; L1-AER-220 | (check) The child is narrower than its parent. L0-CON-030 excludes "any coupling by which motion along one degree of freedom induces an acceleration along another degree of freedom in the body frame", and its guidance lists "a force, moment or acceleration". L1-AER-020 excludes only terms that produce "a force or moment along another degree of freedom". Non-zero products of inertia are allowed by L1-AER-220 ("each moment and product of inertia, with the CV-350 sign convention"). They couple a moment about one axis into angular acceleration about another. That is neither excluded nor named in the kinematic-term exception (#81). FU, which owns the inertia, is not in "Allocated to: DYN, EF". The sufficiency argument ("DYN and EF … exclude every coupling source the model contains") does not hold for the inertia tensor. | Major | State L1-AER-020 in acceleration terms (D18 wording) and allocate FU. Alternatively, require body axes that are principal axes (zero products of inertia), or list the inertia coupling explicitly under #81. |
| G1-F13 | L1-AER-120, -140 rationale and Source; L0-CON-020 rationale; L0-ASM-050 rationale | Revised or replaced decisions cited as current. L1-AER-120: "At level attitude (D10)", Source "D10, D19". L1-AER-140: "Pitch and roll are held level (D10)", Source "D10, D19". L0-CON-020: "pitch and roll stay level (D10)". D10 is revised by D57. L0-ASM-050: "position hold compensates for it" (D56: Stationary and Hover). | Minor | Cite D57. Replace "position hold" with "Stationary and Hover". |
| G1-F14 | L1-AER-690, -700, -520 rationales; FUNCTIONAL_ANALYSIS §8 | Change requests and questions already applied or answered are described as pending. L1-AER-690: "L0-OBJ-110 is allocated to the TST only; CR-B1-01 asks to add AER". L1-AER-700: "L0-CON-190 is allocated to the TST only; CR-B1-02 asks to add AER". L0 now reads "TST, AER" (D50, CR applied). FA §8: rows "TST (CR)" and "The 20 L0 records allocated only to TST or RVS have none … except the two marked '(CR)'". The correct count is 18. L1-AER-520 cites "B1-Q09" and "Plan §1 mentions manual control as an optional 'Where' feature" instead of D49. | Minor | Update the wording to the applied state (D50, D49). Correct the FA §8 table and count. |
| G1-F15 | FUNCTIONAL_ANALYSIS header, §2, §5.1, §7.4, §9 | Stale cross-references in the analysis. Header: "plan §6 (B1) and §9 (D1–D44)" and "L1 (draft `work/B1/L1_AER.md`)". §2: "manual flight control (excluded by L0-CON-180; see `work/B1/issues.md` B1-Q09)", which D49 has decided. §5.1: "Navigation → autoflight \| … \| L1-AER-530, -540", where -540 is Deleted. §7.4: "CONOPS SC-090 should cite [P-SYS-450] (N-B1-03)", already done. §9: "Owner questions at L1 (B1-Q01 to B1-Q10) … proposed design decisions (DD-010, DD-020, DD-040)", all answered or superseded. | Minor | Refresh the header (D1–D58). Remove -540. Cite D49. Drop the done N-B1-03 note. Rewrite §9 as open items only. |
| G1-F16 | FUNCTIONAL_ANALYSIS §3.1, §3.3, §5.1 diagram, §2 F-AER-14 | Small inconsistencies in the N² and the architecture figure. (a) §3.1 row F-13: the diagonal "**Present**" sits in the F-14 column. (b) §5.1 diagram: "TST -- configuration, initial condition, step, wind --> SW". The wind goes to DYN (I-25, §3.3 "TST → DYN step, wind"), not to the flight software, which would otherwise know the wind. (c) The §5.1 diagram has "TM -- operational data, annunciations, indications --> TST" as well as "FCP -- annunciations, indications --> TST". I-42 is FCP's, and TM "keeps only the operational data" (§5.3). (d) F-AER-14 is allocated to "DYN, FU, FC, AF, NAV", but N² row F-14 has no NAV consumer, and §3.3 gives no initial selector values to FCP. | Minor | Move the F-13 diagonal. Route the wind to VM only. Remove the annunciations and indications from the TM → TST edge. Align F-AER-14 with the N² rows. |
| G1-F17 | L1-AER-350 rationale vs FUNCTIONAL_ANALYSIS §7.2 | Budget contradiction. L1-AER-350: "The value bounds … the rotational term of the crew budget (L1-AER-290)". §7.2: "It is evaluated at the centre of gravity (D45, #97), so rotation adds nothing". | Minor | Delete the crew-budget clause from L1-AER-350. |
| G1-F18 | L1-AER-470 rationale and allocation; FUNCTIONAL_ANALYSIS §7.5; P-TM-010; CONOPS §4.4, §5, SC-110 | The annunciation timing budget is inconsistent with D55. L1-AER-470: "[P-SYS-470] is at least two control frames [P-SYS-310] plus one output sample period [P-TM-010]; AF's share is [P-AF-060]. AF decides the content; the flight control panel (FCP) presents it". TM is not allocated. The presentation share is a TM parameter, and FCP has no named share. The ConOps uses the AF share as the aircraft-level figure: §4.4 "Each change … is annunciated within `[P-AF-060]` s"; §5 the same; SC-110 "LOW FUEL is annunciated within `[P-AF-060]` s". L1-AER-570 and -580 use [P-SYS-470] and are FU/FCP, with no AF in the path. | Minor | Name the FCP presentation share (or state that FCP output is at each output sample, so its share is [P-TM-010]). Change the ConOps to [P-SYS-470], as was done for P-SYS-450 (N-B1-03). |
| G1-F19 | L1-AER-430, -660, -680 `Allocated to`; FUNCTIONAL_ANALYSIS §3.3, §4.2 | Allocation gaps for subsystems that take part. L1-AER-430 (the closed list of data crossing the vehicle-model boundary) is allocated to DYN, FU, EF and FC. NAV (state, §3.3 "DYN → NAV × state"), AF and FCP ("FU → AF × fuel state", "FU → FCP × fuel state") also receive data across that boundary and get no child. L1-AER-680 (control frame) is not allocated to FCP, although F-AER-10 runs at step 2 of the frame (§4.2). L1-AER-660 includes "targets" in the initial condition, but FCP, which owns the selector values (D55), is not allocated. (check) The closed list of L1-AER-430 has no inertia, which FC may need when the inertia changes with fuel (L1-AER-220). | Minor | Add NAV, AF and FCP to L1-AER-430, FCP to -680 and -660 (or state why not). Decide whether "vehicle mass" should be "mass properties". |
| G1-F20 | L1-AER-380 rationale; L1-AER-020 rationale vs FUNCTIONAL_ANALYSIS F-AER-06 | Allocation work is attributed to EF. L1-AER-380: "shared by FC (regulation) and EF (allocation without side components)". L1-AER-020: "each axis demand is met with the other force and moment components at zero". F-AER-06 "Allocate axis demands to the effectors" is FC's (§6.1). (check) L1-AER-380 does not give the frame of "the velocity along each other translational axis" (body or local). In Heading the velocity turns with the heading (D56), so the frame matters. | Minor | Say "FC (regulation and allocation) and EF (effector geometry)". Name the frame. |
| G1-F21 | L1-AER-360 rationale and Parameters; P-SYS-280, P-AF-120, P-SYS-450, P-AF-210, P-AF-220 in PARAMETERS.yaml | Parameter references and descriptions. L1-AER-360 names "the translational consumption coefficient" in the budget formula without its ID [P-FU-040], and Parameters omits P-FU-040. P-SYS-280: "from engagement of Hover at Altitude", a D3 mode name. P-AF-120: "in SPD mode" (no speed mode, D56). P-SYS-450: "in a wind up to P-SYS-430", without the gusts that L1-AER-460 includes. P-AF-210 and -220 give "L1-AER-450" as a source, but L1-AER-450 does not reference them (correctly, D33). | Minor | Cite [P-FU-040] and list it. Update the four descriptions and sources. |
| G1-F22 | PARAMETERS.yaml P-AF-010 to -040, P-TM-020 to -050; CONVENTIONS CV-780; TBD_TBR TT-170, TT-210 | Parameter ownership after D55 is half done. P-TM-020 to -050 carry the note "Owned by the flight control panel (FCP, D55)". The selection resolutions P-AF-010 to -040 (closure "G2 (C8)" in TT-170) carry no such note. CV-780 still says "requirement matters for AF and TM … proposed `P-TM-020` to `P-TM-070`". P-TM-060 and -070 are withdrawn, and P-TM-030 to -050 are cited by nothing. | Minor | Add the FCP note to P-AF-010 to -040. Update CV-780 to FCP and P-TM-020 to -050 (CR on a fixed convention, D43). |
| G1-F23 | CONOPS §1, §1.1, §4.1, §4.3, §4.6, §9, N-030, N-180, N-340, §8.2, SC-200, SC-220; GLOSSARY *Operational data*; plan C7 | ConOps leftovers that contradict L1 or the decisions. (a) Manual control: §4.3 "Manual control is an optional feature. Where it is installed, the crew could command the axes directly", N-180 and §8.2 "An optional-feature (EARS 'Where') requirement". These conflict with D49, D55 ("There is no manual control") and the L1-AER-520 rationale. (b) Rate: §4.6 "At each simulation step the Aeronef outputs data", N-340, SC-200 step 4, vs L1-AER-600 one sample every [P-TM-010] (proposed two steps). (c) Classification: §4.6 "The operational data output (TM, task C7) classifies each signal as releasable or protected", N-030, glossary *Operational data*, plan C7, vs L1-AER-630 TBD "decided with the RVS (#69)". (d) §1.1 "proposed in `work/A2/param_proposals.md` with their values TBD" and "Until that document is baselined" (CONVENTIONS fixed, D43). §9 "All values are TBD" (several are TBR, and P-SYS-120, -430, -560 are missing). (e) §4.1 system of interest omits the flight control panel. (f) SC-220 "SC-010 to SC-110": SC-010 is withdrawn. | Minor | Align with D49/D55, L1-AER-600 and L1-AER-630. Refresh §1.1 and §9. Add FCP to §4.1. Fix SC-220. |
| G1-F24 | L1-AER-280, -790 `Type`; L1-AER-710 children-must-show | Attribute mismatches. L1-AER-280 is typed Performance but states a classification rule (Functional). L1-AER-790 ("shall pass the verification of each baselined Aeronef requirement") is typed Documentation, while its parent L0-SUC-020 is Performance. L1-AER-710 states the response "to a vehicle state", but its test guidance is "a step in a reference produces the first change of effector output". | Minor | Correct the types. Make the 710 test match the statement (a state change, with the state-to-output time measured). |
| G1-F25 | All 65 allocated L1 records, `Verification`; L1.md header | The roll-up wording matches D58, but the records cite "(D40)" only. D58 is the decision that applies D40 to L1, as D41 does for L0, and L0 cites D41. Each "Inspection — TBD" procedure ID is an open item with no register entry. | Minor | Cite "(D40, D58)". Either register the roll-up procedure (e.g. one IN- procedure for all roll-ups) or state that roll-up records need none. |
| G1-F26 | Plan §6 Phase 3, G2, §10; requirements/L2.md, L3.md | The plan and the level files do not yet carry FCP (D55) everywhere. Phase 3: "Seven agents run in parallel", but C1 to C8 are eight. G2: "Seven Haiku / low lint agents", and the two inspectors cover "DYN, FU and EF" and "FC, AF, NAV and TM", so FCP is inspected by nobody. §10: "Opus ×7"; Phase 4 "Opus ×3 (M3, M7, FC1)", but M7 is withdrawn and M8 is Opus. requirements/L2.md and L3.md have no `FCP` section, although plan §3 orders "DYN, FU, EF, FC, AF, FCP, NAV, TM", so C8's draft cannot be assembled. | Minor | Update the plan counts and the G2 inspector scope. Add the FCP sections to L2.md and L3.md before Phase 3. |
| G1-F27 | L1-AER-310 to -350 `Statement`; P-SYS-200, -210, -220 | The "operating volume" condition is not tied to its parameters. The envelope records apply "in the operating volume", and the -310 test "at both ends of the operating altitude range". The bounds are P-SYS-210, -200 and -220 (CONOPS §4.2), which no requirement references (PARAM-UNUSED). | Minor | Define *Operating volume* in the glossary with the three IDs (G1-F11), or cite them in the records. |
| G1-F28 | L1-AER-470, -500, -750 `Statement` (COMPOUND, D30) | (check) Three COMPOUND warnings are more than a closed list. L1-AER-470: "When an autoflight mode becomes armed or active, or when a target changes" is a tree of triggers. It also leaves out disengagement and a mode leaving the armed state, which are mode changes the crew must see (N-060). L1-AER-500 states two thoughts: the unit assignment (CV-740) and the exact conversion (CV-750). L1-AER-750 states two: one file per level, and each record's level and parent or design decision. | Minor | Split L1-AER-500 and -750. Make L1-AER-470 "When the mode state or a target changes …", with mode state covering armed, active and disengaged. |
| G1-F29 | L1-AER-100 `Statement` | (check) The closed list of effector properties, "direction of action, … control effectiveness, … output limits, … command response and … fuel consumption parameters", has no point of application or moment arm, which a force effector needs in order to produce a moment. It also uses two undefined terms (G1-F11). If "control effectiveness" is meant as a six-component force-and-moment vector per unit command, say so. | Minor | Define "control effectiveness" (force and moment per unit command), or add the point of application to the list. |
| G1-F30 | L1-AER-510 success criteria vs CV-780, P-TM-020 to -050 | (check) L1-AER-510 is verified by "no requirement of the Aeronef branch at L1 or below defines … a display format". FCP will write display resolution and rounding requirements (CV-780, P-TM-020 to -050). Without a definition of "display format", an inspector could fail L1-AER-510 on them. | Minor | Define "display format" (layout, graphics, symbology) as distinct from the value resolution of a crew-interface data item. |
| G1-F31 | L1-AER-070, -660, -670; FUNCTIONAL_ANALYSIS §5.1 Aeronef ↔ TST row | The wind input has no L1 interface statement. The wind appears only in rationales: L1-AER-070 "the wind the TST gives with each step", and L1-AER-670 "The wind of the run comes with the step command (I-25)". Neither L1-AER-670 nor -660 states that the Aeronef accepts the wind. | Minor | Add the wind velocity to the L1-AER-670 statement, or write a separate interface record. |
| G1-F32 | registers/DECISIONS.md header; L0.md header; CONVENTIONS §0, §11 G0-12 | Stale metadata. DECISIONS.md: "Plan-level decisions D1–D52". L0.md "Changed since" omits L0-CON-160 (CR-B1-04), L0-ASM-030 (CR-B1-05) and L0-CON-310 (CR-B1-06). CONVENTIONS §0 still names "VOR definitions" among the departures from R-004. G0-12 (VOR deviation sign) is "Deferred to L2 (#54)", but D56 makes it moot. | Minor | Refresh the headers. Mark G0-12 Withdrawn (D56) and close #54. |

**Counts:** 12 Major (G1-F01 to G1-F12), 20 Minor (G1-F13 to G1-F32). Eight findings are marked "(check)": G1-F08, G1-F09, G1-F12 (Major), and G1-F19 (inertia part), G1-F20 (frame part), G1-F28, G1-F29, G1-F30.

## 2. Sufficiency and allocation check

**L0 → L1 coverage.** All 41 live L0 records allocated to AER have at least one L1 child (computed from the Parent(s) fields; FUNCTIONAL_ANALYSIS §8 matches). L0-CON-160 is a leaf (`Allocated to: —`, D54) with a direct criterion. The 18 records allocated only to TST or RVS (L0-OBJ-060, -070, -080, -090, -120, -130, -160, -170, L0-CON-250, L0-SUC-040, -050, -060, -070, -100, -110, -120, -130, -140) have no children by design (D44). No L1 record cites a deleted or unknown parent.

**Sufficiency arguments.** Each sibling group carries a sufficiency argument. The arguments cover their parent, except in the following cases:

| L0 parent | L1 children | Problem | Finding |
| --- | --- | --- | --- |
| L0-OBJ-030 | L1-AER-310 … -660 (13 records) | The parent's guidance asks for coverage of the D3 catalogue. The children are written against D56. | G1-F03 |
| L0-CON-030 | L1-AER-020 | The child excludes force and moment coupling only. The parent excludes acceleration coupling, and products of inertia fall between the two. | G1-F12 |
| L0-CON-290, L0-CON-310 | L1-AER-260 to -300 | The parents' guidance asks for a landing-envelope acceleration limit that D53 withdrew. | G1-F02 |
| L0-OBJ-110 | L1-AER-690 | Identical data versus the same verification result (D25). | G1-F09 |
| L0-CON-100 | L1-AER-150 | The parent's guidance asks for "an initial fuel quantity as a parameter". L1 reads it as a capacity parameter plus the initial fuel in each run's initial condition. N-B1-08 asks the owner to accept that reading "at G1". No decision is recorded. | §5 |
| L0-OBJ-020, L0-OBJ-030 | L1-AER-460 | The hold accuracy has no stated dimension after D56. | G1-F06 |

The other groups are sufficient: L0-OBJ-010, -020, -140, -150, -180, -190, -200, -210; L0-CON-010, -020, -040 to -150, -170, -180, -190, -200, -210, -260, -270, -280, -300; L0-SUC-010, -020, -030, -150, -170.

**D33 (aircraft as a whole).** No L1 statement defines a mode, a mode group, a combination or a transition. Mode names appear only in rationales (L1-AER-450, -460, -330), which is acceptable. L1-AER-470 and -620 use "armed" and "active", which are the state vocabulary of D16 and D56, not mode definitions. These L1 records over-constrain L2:

- L1-AER-420: "mode status" to FC (G1-F04).
- L1-AER-310 to -350: literal "sustain" (G1-F01).
- L1-AER-430: the closed list that omits inertia (G1-F19, check).

**Allocation matrix (§6.2) against the L1 `Allocated to` fields.** The matrix was checked by script for all 80 live records. Allocation, type and parent are identical for every record, and no record is missing. The counts match §6.2: DYN 23, FU 20, EF 23, FC 23, AF 17, FCP 10, NAV 6, TM 10, leaves 15. The shares fit what §6.1 says each subsystem owns, except for the gaps in G1-F19 and the attribution in G1-F20. FCP's ten records (L1-AER-470, -480, -490, -500, -560 to -580, -610, -620, -690) cover selections, presentation, units and the fuel indications, as D55 assigns.

**Interfaces (§5.1, §13.2).** Status of each boundary:

- Vehicle-model boundary: L1-AER-430 and -440. Its ICD home is open (IN-B1-01, an I1 decision).
- AF → FC: L1-AER-420. Content conflict, G1-F04.
- NAV → AF: no Interface-type record; the boundary table cites the deleted L1-AER-540 (G1-F05).
- Aeronef ↔ TST: L1-AER-480, -490, -590 to -670. Wind gap, G1-F31.
- FCP ↔ AF, NAV → FCP and FU → FCP: no interface record and no ICD (G1-F05).

The function-level and subsystem-level N² matrices are consistent with each other and with §5.1, apart from the defects in G1-F16.

## 3. Budget check (FUNCTIONAL_ANALYSIS §7)

| Budget | Closure as written | Consistent with L1 rationale and PARAMETERS.yaml | Problem |
| --- | --- | --- | --- |
| §7.1 effector authority | Symbolic only, as the values wait for m_max and J_max (TBD, I1). The upward force m_max·(g + [P-SYS-440]) + D([P-SYS-240]) is correct, since the wind has no vertical component (D51). The other directions use m_max·[P-SYS-440] + D([P-SYS-230] + 150 kt). | Yes: L1-AER-120, -130, -140 and the P-SYS-400, -410, -420 descriptions agree. | None for the forces. The moment line needs the C4 onset time. |
| §7.2 crew and vehicle acceleration | 1 g + 1.5 g + 0.5 g margin = 3 g, and \|a − g\| ≤ \|a\| + g, a conservative bound. 1.0 g + 0.5 g = 1.5 g. Values check: 14.709 975 = 1.5 × 9.806 65; 4.903 325 = 0.5 g; 29.419 95 = 3 g. | Yes for L1-AER-290 and -300. No for L1-AER-350 ("rotational term"). | No disturbance share (G1-F08). L1-AER-350 conflict (G1-F17). |
| §7.3 fuel | [P-FU-010] ≥ m_dry·(exp(k_t·g·[P-SYS-280]) − 1) follows from dm/dt = −k_t·g·m and is dimensionless (kg/(N·s) · m/s² · s). | Yes, with L1-AER-360. The ID is missing in the record (G1-F21). | The attitude-holding consumption is left to C2, as stated. Which hold is meant is unclear (G1-F06). |
| §7.4 position | 0.5 m + 0.5 m ≤ 1 m; the NAV share is 0 by L1-AER-440. | Yes for L1-AER-460, P-AF-160 and P-FC-010. P-SYS-450 omits the gusts (G1-F21). | Dimension (G1-F06). Gust shape (G1-F08). |
| §7.5 timing | Annunciation 2 × 0.02 s + 0.02 s = 0.06 s ≤ 0.5 s. Control loop 0.02 s + [P-EF-010] ≤ 0.1 s, which leaves 0.08 s for EF. [P-TM-010] = [P-SYS-310] = 2 × [P-SYS-300]. | Yes for L1-AER-600, -670, -680 and -710 and for PARAMETERS.yaml. | The FCP share is unnamed, the TM parameter has no TM allocation, and the ConOps uses [P-AF-060] (G1-F18). |

Landing-envelope values check: [P-SYS-500] = √(2 × 9.806 65 × 0.6096) = 3.458 m/s. Wind values check: [P-SYS-430] = 100 kt = 51.444 m/s and [P-SYS-560] = 50 kt = 25.722 m/s.

## 4. Confirmed OK

- **D53.** L1-AER-280 has two speed limits at the contact sample, P-SYS-500 and P-SYS-510 TBR, and no acceleration limit. P-SYS-520 is withdrawn in the PARAMETERS.yaml header and referenced by no live record. The upstream gap is G1-F02.
- **D54.** L1-AER-230 is Deleted, with its reason. L0-CON-160 is a leaf (`Allocated to: —`) with a direct inspection criterion (CR-B1-04 applied, v3). FA §2 and §8 agree.
- **D55.** FCP appears in the allocation, §6.1, §5.3, the lint and param_check subsystem codes and the PARAMETERS.yaml schema. The gaps are G1-F05, G1-F19, G1-F22 and G1-F26.
- **D56.** L1-AER-450 states only the aircraft-level capability and cites D56. L1-AER-340, -540 and -550 are Deleted with reasons. CV-560 and CV-610 to CV-670 are Deleted. SC-010, -030, -070 and -080 are withdrawn and SC-120 added. N-110 and N-120 are withdrawn. The glossary mode entries match D56 (one horizontal and one vertical mode, Go to hover and Hover over both, Hover arming from Go to hover, the hover height as a constant, the standard vertical speed). I-15, I-20 and I-24 are withdrawn and not reused. P-SYS-260, P-NAV-050 and the other withdrawn IDs are referenced only by Deleted records.
- **D57.** L1-AER-390, F-AER-05, CONVENTIONS CV-550 and CONOPS §4.4 and §5 hold pitch and roll at zero. The conflict at exhaustion is G1-F07.
- **D58.** The 65 allocated records use the roll-up criterion, and the 15 leaves (L1-AER-510, -520, -700, -730 to -840) have their own direct method and criteria. Only the citation is missing (G1-F25).
- **D45, D46, D51.** The crew limit is at the centre of gravity (L1-AER-290). Weight is carried along −z_B only (L1-AER-120 and -130). The wind is horizontal, steady plus gusts, in L1-AER-070, -130, -310 and -460, CV-470, the glossary *Gust* and P-SYS-560.
- **No literal numbers in L1 statements.** Every quantity is a parameter ID that exists in PARAMETERS.yaml (param_check: 0 PARAM-MISSING). The crew units appear only through CV-740 in L1-AER-500.
- **Registers.** CR-B1-01 to -06 are all Applied, and the L0 records show the changes. Every record-level TBD/TBR field has an owner and a closure gate or date.
- **COMPOUND warnings.** Apart from G1-F28, the L1 warnings are closed enumerations or one-constraint pairs that D30 allows.

## 5. TBD/TBR list checked: yes

registers/TBD_TBR.md was checked against the TBD/TBR fields of every live L1 record and every TBD/TBR parameter. All 64 rows have owner Martin and a closure gate. The L1 record fields TT-330 to TT-640 are copied correctly, and every TBD or TBR parameter in PARAMETERS.yaml is in a TT-010 to TT-220 row. Gaps:

- **Not in the register:**
  - The gust-shape bound (G1-F08).
  - The roll-up and leaf procedure IDs, "Inspection — TBD" on all 80 records (G1-F25).
  - The owner's acceptance of the L0-CON-100 reading (N-B1-08, "Accept the reading at G1").
  - The vehicle-model-boundary ICD home (IN-B1-01, N-B1-07; I1).
  - DD-010 and DD-020 (accepted at this stage; registers/DECISIONS.md is empty).
- **Record fields that list only the record's own parameter:**
  - L1-AER-290: "—", although P-DYN-010 and P-SYS-440 are TBR.
  - L1-AER-300: omits P-AF-200 and P-FC-020.
  - L1-AER-310: omits P-SYS-560.
  - L1-AER-460: omits P-SYS-430, -560, P-AF-160 and P-FC-010.
  - L1-AER-470: omits P-AF-060 (TBD), P-SYS-310 and P-TM-010.
  - L1-AER-120: omits P-SYS-440 and -240.

  The register covers each of these at parameter level, so this is consistency only.
- **TT-270** is opened "Open" for L0-CON-310's field "— (3 g confirmed by the owner, D45, CR-B1-06)", which is a closed item.
- **The closure "as stated"** for TT-230 to TT-640 relies on the field text; for TT-600 that text is "RVS plan extension (D44)", which is not a gate.

## 6. Items left to L2 (not findings), and overlap with the checklist pass

Left to L2 as decided, and checked only for contradictions:

- the heading behaviour of each mode (A2-Q03);
- the reference position of a hold (#78);
- the mode state after exhaustion (#59) and the valid initial mode states (#60);
- Go to hover engaged below the hover height (#88);
- the kinematic and gyroscopic terms (#81, apart from G1-F12);
- the panel content (#79);
- display rounding (#55);
- signal classification (#69).

The ConOps sequence tables were read against D56 and show no contradiction beyond G1-F06 and G1-F18.

The untracked reviews/G1/checklist_L1.md reaches the same conclusion independently on the following items:

- L1-AER-690 against D25 (G1-F09);
- "fixed position" in L1-AER-360 and -460 (G1-F06);
- D10 cited in L1-AER-120 and -140 (G1-F13);
- the undefined terms (G1-F11).

It also raises wording items that this record does not repeat, for example:

- the L1-AER-370 criterion "followed";
- the L1-AER-330 criterion "levels off above the minimum operating altitude";
- "baselined" in L1-AER-450.

The moderator can merge the two lists.

## 7. Recommended exit decision

**Rework and re-review.**

L1 is close to usable. Coverage is complete, the allocation matrix is exactly consistent with the records, and the budgets close arithmetically. But several Major findings would mislead the L2 agents or need an owner ruling first:

- **Owner rulings:**
  - G1-F04: mode status across ICD-FC-AF.
  - G1-F09: identical data versus the same result (D25).
  - G1-F08: gust-shape bound and disturbance share.
  - G1-F02 and G1-F03: change requests against the baselined L0-CON-290, -310, L0-ASM-110 and L0-OBJ-030.
- **Statement fixes in L1:**
  - G1-F01: the envelope records read as permanent states.
  - G1-F06: dimension of the hold accuracy.
  - G1-F07: pitch and roll after fuel exhaustion.
  - G1-F12: acceleration coupling and inertia.
- **Architecture and support material for the L2 agents:**
  - G1-F05: FCP interfaces and ICD.
  - G1-F10: superseded Q5 proposal and interface needs.
  - G1-F11: glossary merge, corrected for D55 to D57.

After rework, a short delta re-inspection should cover the changed records, FUNCTIONAL_ANALYSIS §5.1, §7 and §9, the glossary merge, the L0 CRs, and the 12 Major dispositions. The moderator can close the Minor findings. The main risks if L1 were baselined as it stands:

- C5 would start from a Q5 proposal that contradicts D56 (G1-F10).
- C5 and C8 would have no common definition of the panel ↔ autoflight interface (G1-F05).
- C4 would read L1-AER-420 as licence for mode-dependent control laws (G1-F04).
- The G4 roll-up of L0-OBJ-030, -CON-290 and -CON-310 would fail on guidance that the decisions have withdrawn (G1-F02, G1-F03).
