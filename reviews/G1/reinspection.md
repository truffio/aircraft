# Gate G1 delta re-inspection — B1 (L1 Aeronef requirements, functional analysis, allocation, budgets)

```markdown
Artifact / version:   requirements/L1.md (section AER: 85 live records, L1-AER-850 to -890 new; L1-AER-230, -340,
                      -540, -550 Deleted) + specs/FUNCTIONAL_ANALYSIS.md, at branch b2_params, commit e77d653.
                      Read with them: requirements/L0.md (CR-B1-07 to -09 applied), specs/CONOPS.md, specs/CONVENTIONS.md,
                      specs/GLOSSARY.md, parameters/PARAMETERS.yaml, registers/*, AIRCRAFT_REQUIREMENTS_PLAN.md (§1, §3,
                      §6, §9 D53–D63, §10), work/B1/*, work/A1/* (sync only).
                      Delta read: git diff -w b0a96de e77d653 (b0a96de is the inspected state).
Review type:          Inspection (delta re-inspection, METHODOLOGY §13.4), of the rework of
                      reviews/G1/inspection_B1.md (G1-F01 to F32) and reviews/G1/checklist_L1.md, as disposed of in
                      reviews/G1/dispositions.md
Moderator / author / reader / recorder / reviewers:
                      moderator: orchestrator / author of the rework: B1 rework agent (owner: Martin) /
                      reader, recorder, reviewer: independent Opus re-inspector (did not author, inspect or rework
                      any of the material)
Date:                 2026-11-04
Entry criteria met:   yes:
                      - Working tree clean at e77d653; dispositions recorded (reviews/G1/dispositions.md).
                      - Owner rulings recorded as D59 to D63 (plan §9); the four owner questions are answered (D63).
                      - L0.md and L1.md in sync with work/A1 and work/B1 (assemble.py --all --dry-run: up to date).
                      - lint 0 errors; trace, param, VCRM and test results as in section 4.
Findings:             verdicts in sections 1 and 2; new findings in section 3
TBD/TBR list checked: yes (registers/TBD_TBR.md checked by script against the TBD/TBR field of every live L0 and L1
                      record and against every TBD/TBR parameter: 73 rows, every field copied verbatim, no record or
                      parameter missing)
Exit decision:        Baseline (recommended; see section 5)
```

Scope. The whole delta of every file listed above was read. Every L1 record changed by the rework (74 records) and the five new records were compared field by field with their b0a96de text. The FUNCTIONAL_ANALYSIS §6.2 and §8 tables, the TBD/TBR register and the record parameter lists were checked by script against the records. Decisions D1 to D63 are taken as settled. Items deferred to L2, #69, #81 or I1 are accepted as deferred when the deferral is registered. "(check)" marks a finding the re-inspector is less certain of.

## 1. Major findings: verdicts

### 1.1 Inspection Majors

| F-ID | Disposition claimed | Verified against | Verdict |
| --- | --- | --- | --- |
| G1-F01 | Capabilities, D63 Q2 | L1-AER-310: "shall be able to sustain each horizontal speed up to [P-SYS-230] under autoflight"; -320 "be able to climb at each vertical speed up to [P-SYS-240]"; -330 "be able to descend at each vertical speed magnitude up to [P-SYS-250]"; -350 "be able to change its heading at each heading rate magnitude up to [P-SYS-270]". Each rationale: "The record states a capability, not a state the Aeronef is always in", and the tracking tolerance is L2 (P-AF-090, P-AF-120). Matches D63 Q2 ("each value from zero up to the maximum"). | **Closed** |
| G1-F02 | D53, CR-B1-07 | L0-CON-290 v3 guidance: "a landing envelope of vertical and horizontal speed limits at the contact sample". L0-CON-310 v6: the clause "the acceleration limit of the landing envelope … does not exceed [P-SYS-120]" is gone; rationale: "the vertical speed limit of the landing envelope stands in for the impact (D53, CR-B1-07)". L0-ASM-110: "limits on the vertical and horizontal speed at the contact sample, D53". Glossary *Landing envelope*: "There is no acceleration limit (D53)". CONOPS §4.2: "limits on the vertical and horizontal speed at contact, D53". FA F-AER-12 inputs "vertical and horizontal speed at the contact sample"; I-08 "Altitude and velocity at the contact sample (D53)". No live file still asks for an envelope acceleration limit. | **Closed** |
| G1-F03 | D56, CR-B1-08 | L0-OBJ-030 v3: "The mode catalogue is plan decision D56, which replaced D3"; "Children must show (D41): (Inspection) each mode of the mode catalogue (D56) is covered"; Source "§9 D56". Plan §1: "The autoflight mode catalogue in Section 9, D56 (which replaced D3)". | **Closed** |
| G1-F04 | "mode status" removed | L1-AER-420: "shall pass the axis references from autoflight to flight control through the one interface defined in ICD-FC-AF"; rationale: "flight control receives no mode information, so no control law can depend on the mode logic (D15, D33)". FA I-13 and §5.1 carry axis references only; IN-B1-03 marks "and mode status" superseded; glossary *Axis reference*: "The only data autoflight passes to flight control (D15)". | **Closed** |
| G1-F05 | L1-AER-880, -890, ICD-FCP | L1-AER-880 (Interface, FCP, AF, NAV, FU): closed list across the panel boundary, "as defined in ICD-FCP". L1-AER-890 (Interface, NAV, AF): the five quantities with validity "through the one interface defined in ICD-NAV-AF". FA §5.1 boundary table has the FCP row and cites L1-AER-890 for NAV → AF (no -540). I-06, I-16, I-18, I-19 point to ICD-FCP. Plan §3 lists `ICD-FCP.md`; I1 writes it; TT-680 registers it; IN-B1-08 added; D63 confirms a separate ICD-FCP. | **Closed** (new issues R-03, R-04) |
| G1-F06 | D60 | L1-AER-460: "While autoflight holds the horizontal position over the ground … keep its horizontal position within [P-SYS-450] of the reference position"; test "in Stationary with each vertical mode and in Hover"; altitude error to [P-AF-110]. L1-AER-360: "While autoflight holds the horizontal position and the altitude with no wind applied". P-SYS-450, P-SYS-460, P-FC-010, P-AF-160 descriptions, FA §7.3 and §7.4, CONOPS SC-090 and SC-100 ("horizontal position … (D60)"), glossary *Reference position* all agree. | **Closed** |
| G1-F07 | Scope "with fuel remaining" | L1-AER-390: "While the Aeronef is airborne with fuel remaining, the Aeronef shall hold its pitch angle and its roll angle within [P-AF-180] of zero"; rationale explains the free attitude after exhaustion (L1-AER-200, SC-110); test "while fuel remains". No conflict with L1-AER-200 remains. | **Closed** |
| G1-F08 | D62, P-SYS-570 | P-SYS-570 "Minimum gust rise time", TBD, TT-650 (G2, C1 with the TST wind model). Glossary *Wind envelope* and amended *Gust*. L1-AER-300, -310, -460 are stated "in a wind within the wind envelope" and list P-SYS-570; -310 and -460 tests name the gust class ("gusts of [P-SYS-560] built up over [P-SYS-570]"). FA §7.2 "Disturbance share (D62, G1-F08)" puts the gust response inside [P-FC-020], and §7.4 inside [P-FC-010], each to be shown by C4 at G2. P-SYS-560, CONOPS §4.2, IN-B1-02 and IN-B1-07 updated. | **Closed** |
| G1-F09 | D59, D63 Q4 | L1-AER-690: "When a run is repeated with the same configuration, initial condition, crew selection script and TST step and wind inputs, the Aeronef shall produce operational data that give the same pass or fail verdict against each success criterion assessed on the run." Execution host dropped, TST inputs added. Rationale cites D59 and D63's reading of "stated tolerances". CONOPS SC-200 aligned. One test guidance elsewhere still requires identical data. | **Closed** (residue in R-05) |
| G1-F10 | Superseded material marked | work/B1/issues.md: status note, §3 headed "SUPERSEDED by D56" with "not an input to C5", DD-040 "Superseded (D55)". work/B1/interface_needs.md: VOR, flight-path-angle, mode-status and TM-presentation text struck through and marked superseded; C5 row: "not from the superseded Q5 proposal"; new C8 row; IN-B1-08. FA §9 now says the Q5 proposal "is not an input to C5". | **Closed** |
| G1-F11 | 44 terms merged | 44 new glossary rows (counted against b0a96de), none duplicated, alphabetical. Every term the finding listed is defined (*Indication*, *Operating volume*, *Vehicle state*, *Vehicle model*, *Flight software* with FCP, *Axis reference*, *Axis demand*, *Effector command*, *Effector output*, *Fuel state*, *Vehicle mass*, *Fuel mass flow*, *Remaining fuel mass*, *Dry mass*, *Vehicle acceleration*, *Reference position*, *Initial condition* without VOR, *Crew selection*, *Heading rate*, *Control effectiveness*, *Command response*); *Mode status* replaced by *Mode state*; *Subsystem* lists FCP. One new statement uses an undefined term. | **Closed** (new issue R-03) |
| G1-F12 | D61 | L1-AER-020: "no term by which motion along one degree of freedom produces an acceleration along another degree of freedom in the body frame"; Allocated to "DYN, EF, FU"; sufficiency covers "drag, effectors, inertia". L1-AER-220: "derive, at each fuel state, a diagonal inertia tensor in the body frame". Glossary *Mass properties*, FA I-04 and F-AER-03 cite D61. | **Closed** |

### 1.2 Checklist Majors

| Record | Checklist issue | Verified | Verdict |
| --- | --- | --- | --- |
| L1-AER-330 | Criterion adds "levels off above the minimum operating altitude" | Criterion now "the vehicle reaches and holds descent vertical speed magnitudes up to and including [P-SYS-250], at zero and at maximum horizontal speed". The rationale leaves levelling to the mode logic (D56: Go to altitude and Vertical speed arm Altitude hold). "Minimum operating altitude" is inside the glossary *Operating volume* ([P-SYS-210]). Not escalating is justified: D56 settles the question. | **Closed** (stale Source in R-02) |
| L1-AER-690 | Bit-identical versus same verdict (D25) | As G1-F09. | **Closed** |
| L1-AER-360, -460 | "fixed position" undefined | As G1-F06. Both statements use "holds the horizontal position", which the glossary *Reference position* ties to Stationary and Hover. | **Closed** |

## 2. Minor findings: sample verdicts

Twenty-nine of the 41 Minor dispositions were verified (20 inspection, 9 checklist), including every disposition marked Accepted or Deferred and every item in the dispositions' "Other items" table.

| F-ID / record | Verified | Verdict |
| --- | --- | --- |
| G1-F13 | L1-AER-120, -140: "(D57, which revises D10)", Source D57. L0-CON-020 v3: "held at zero (D57, which revises D10; CR-B1-09)". L0-ASM-050: "Stationary and Hover compensate for it (D56, CR-B1-09)". | Closed |
| G1-F14 | L1-AER-690 and -700: "allocated to the TST and the Aeronef (CR-B1-01/-02, D50)". FA §8: count 18, rows "TST, AER"; the table matches the Parent(s) fields exactly (checked by script). L1-AER-520 cites D49, D55; no B1-Q09. | Closed |
| G1-F15 | Header D1–D62, §2 cites D49, §5.1 without -540, §7.4 N-B1-03 note gone. Residues: the header still says "L1 (draft `work/B1/L1_AER.md`)", and the first §9 open item points to owner questions that D63 has answered. | Partly closed (R-06) |
| G1-F16 | (a) the F-13 diagonal is in the F-13 column; (b) "TST -- step, wind, initial state --> VM"; (c) "TM -- operational data --> TST"; (d) F-AER-14 allocated "DYN, FU, FC, AF, FCP", I-28 added, §3.3 TST → FCP "initial selector values". | Closed |
| G1-F17 | L1-AER-350: "rotation adds no share to the crew budget (D45, FUNCTIONAL_ANALYSIS §7.2)". | Closed |
| G1-F18 | L1-AER-470 and FA §7.5: FCP share "one output sample period [P-TM-010]"; P-AF-060 "AF share … at most P-SYS-470 minus P-TM-010". CONOPS §4.4, §5 and SC-110 use `[P-SYS-470]`. | Closed |
| G1-F19 | L1-AER-430 allocated also to AF, FCP, NAV; "mass properties" (glossary: mass, CG, inertia). L1-AER-680 "crew-selection, navigation, autoflight and flight-control functions", FCP allocated. L1-AER-660 FCP allocated. FA §6.2 matches every live record (allocation, type, parents; checked by script). | Closed (FA §4.2 residue in R-04) |
| G1-F20 | L1-AER-380: "along each other body axis"; "FC (regulation and allocation) and EF (the effector geometry …)". P-SYS-540 "along each body axis". | Closed |
| G1-F21 | L1-AER-360 cites and lists [P-FU-040]. P-SYS-280, P-AF-120 ("in Heading (there is no separate speed mode, D56)"), P-SYS-450 descriptions updated; P-AF-210, -220 sources no longer cite L1-AER-450. No record cites a parameter it does not list, or the reverse (script). | Closed |
| G1-F22 | P-AF-010 to -040 carry the FCP note. CV-780: "requirement matters for the flight control panel (FCP, D55)", `P-TM-020` to `P-TM-050`, Status "Changed (D55, CR-B1-10)". The same D55 correction was not made in CV-580. | Closed (residue in R-04) |
| G1-F23 | (a) CONOPS §1, §4.3 ("There is no manual control (D49, D55)"), N-180, §8.2, plan §1. (b) §4.6, N-340, SC-200 use the output sample. (c) §4.6, N-030, glossary *Operational data*, plan C7 and §7 defer the classification to the RVS (#69). (d) §1.1 and §9 point to PARAMETERS.yaml. (e) §4.1 includes the flight control panel. (f) SC-220 "SC-020 to SC-120". | Closed (new "3 g" in §9, R-07) |
| G1-F24 | L1-AER-280 Type Functional; L1-AER-790 Type Performance; L1-AER-710 test "for a change of vehicle state, the time … to the first change of effector output that responds to it". | Closed |
| G1-F25 | All 68 allocated records cite "(D40, D58)" in Verification and "Children must show (D58)" in the rationale; no leaf uses the roll-up criterion (script). TT-690 registers the procedure IDs (G4, V4). | Closed |
| G1-F26 | Plan: Phase 3 "Eight agents", G2 "Eight Haiku" and FCP in the second inspector's scope, V3 "AF, FCP and NAV", §10 counts. L2.md and L3.md have an FCP section between AF and NAV. | Closed |
| G1-F27 | Glossary *Operating volume* with [P-SYS-210], [P-SYS-200], [P-SYS-220]; L1-AER-310 lists them; they are no longer PARAM-UNUSED. | Closed |
| G1-F28 | L1-AER-470: "When the mode state or a target changes"; glossary *Mode state*. L1-AER-500 split (new -870); L1-AER-750 split (new -850, -860). | Closed (wording nit in R-07) |
| G1-F29 | Glossary *Control effectiveness*: "control force and control moment … about the centre of gravity … per unit of its effector command. It carries the effector's point of application and moment arm." *Command response*, *Output limits*, *Consumption parameters* defined. | Closed |
| G1-F30 | Glossary *Display format* excludes "the value resolution or the rounding". L1-AER-510 rationale says the FCP requirements on them do not breach the record. | Closed |
| G1-F31 | L1-AER-670: "advance its vehicle model by one simulation step of [P-SYS-300] with the wind velocity that the TST gives with that command"; test checks the air-relative velocity of each step; I-25 cites it. | Closed |
| G1-F32 | DECISIONS.md header "D1–D62"; L0.md "Changed since" lists every CR-B1 change; CONVENTIONS §0 without VOR, G0-12 "Withdrawn". D63 was added after these headers were refreshed, so DECISIONS.md and the FA header stop at D62. Closing GitHub #54 is outside this review (not verified). | Closed (residue in R-06) |
| Chk L1-AER-460 | Test gated "at each output sample from [P-SYS-460] after the start of the hold". | Closed |
| Chk L1-AER-370 | Test: "settles on its reference within the tracking tolerance and the settling time that the FC children state as parameters (C4)". | Closed |
| Chk L1-AER-020 | **Deferred** to #81: the statement keeps "other than the rigid-body kinematic terms that MS-DYN retains"; TBD/TBR field and TT-330 "(#81), Martin, G2 (C1)", Open. | Deferred (accepted) |
| Chk L1-AER-640 | "its altitude, horizontal speed, vertical speed, heading and track". | Closed |
| Chk L1-AER-630 | **Accepted**: field "closes when the plan is extended to the RVS (D44)", the same form as the L0 RVS items TT-290 to TT-320; TT-600 copies it. A G2 gate would be wrong, because #69 waits for the RVS plan. | Accepted |
| Chk L1-AER-750 | Split into -750 (one level file per level), -850 (level stated; lint LEVEL, ID-FORMAT) and -860 (parents or design decision; trace ORPHAN, DERIVED). Lint has the LEVEL and ID-FORMAT codes and trace_check the ORPHAN and DERIVED codes. Both new records are leaves on L0-OBJ-180, and §6.2 and §8 show them. | Closed (new issue R-01) |
| Chk L1-AER-750 to -830 subject | **Accepted** by D63 Q1 ("stay at L1 as leaves with the Aeronef as subject"; D63 covers -850 and -860 too). | Accepted |
| Chk systemic: values in TBD/TBR fields | No live L1 TBD/TBR field contains a numeric value (script); each cites the parameter, its status and its TT row. | Closed |
| Chk systemic: missing documents | TT-660 (MS-DYN), TT-670 (AF_MODE_LOGIC), TT-680 (the four ICDs and the vehicle-model boundary home), TT-720 (L1-AER-430 field). | Closed |
| Other: L0-CON-100 reading | **Accepted** by D63 Q3; TT-700 "Closed (D63)". | Accepted |
| Other: TT-270 | "Closed (D45; nothing open in the field)". | Closed |
| Other: TT-600 | As checklist L1-AER-630. | Accepted |
| Other: vehicle-model ICD home | **Deferred** to I1: TT-680, TT-720; plan I1 "decide the home of the vehicle-model boundary definitions (IN-B1-01)". | Deferred (accepted) |
| Other: DD-010, DD-020 | **Accepted**: the 2 DERIVED errors remain, as expected. This now conflicts with the new leaf L1-AER-860. | Accepted (see R-01) |
| Other: PARAM-UNUSED (19) | Exactly the 19 IDs listed in the disposition (section 4). | Accepted |
| COMPOUND verdicts | The rework's statements flagged by lint (L1-AER-360, -470, -500, -690, -860, -870, -880, -890) are judged one thought in dispositions.md. The re-inspector agrees: closed lists at one boundary (-880, -890, like -430), one rule in two directions (-870), and the two values of one attribute (-860). | Accepted |

## 3. New findings

None is Major. The moderator can close all of them; none needs an owner ruling.

| F-ID | Location | Description | Major/Minor | Proposed fix |
| --- | --- | --- | --- | --- |
| G1-R01 | L1-AER-860 success criteria; registers/DECISIONS.md | The new leaf says "the trace check reports no ORPHAN or DERIVED error in the Aeronef branch, checked at each gate". At this gate the trace check reports two DERIVED errors ("L1-AER-680: DD-010 is not in registers/DECISIONS.md", "L1-AER-710: DD-020 …"), which the dispositions accept and leave to the orchestrator. If L1 is baselined as it stands, a leaf of that baseline fails its own criterion at the gate that creates it. L1-AER-850 (LEVEL, ID-FORMAT) passes. | Minor | Enter DD-010 and DD-020 in registers/DECISIONS.md (from work/B1/issues.md §5) before the baseline tag; trace_check then reports only CHILDLESS. Alternatively, scope the criterion like L1-AER-810 (at the requirements baseline). |
| G1-R02 | L1-AER-330 `Source` | "N-170; CONOPS SC-020, SC-030". SC-030 ("Descent on flight path angle") is withdrawn (D56). This is the only live L0 or L1 record that still cites a withdrawn scenario, need, CV item, parameter or record (script over all fields, for SC-010/-030/-070/-080, N-110/-120, CV-560, CV-610 to -670, P-SYS-260/-520, P-NAV-020/-040/-050, P-AF-050/-070/-080/-150, P-TM-060/-070, L1-AER-230/-340/-540/-550). It is a residue of the original draft that the inspection did not catch. | Minor | Source "N-170; CONOPS SC-020" (or add SC-040, whose Vertical speed mode also descends). |
| G1-R03 | L1-AER-880 `Statement`; L1-AER-890 `Statement`; GLOSSARY | The new interface statements use terms that are not in the glossary: "navigation quantities" (-880, "annunciation content, navigation quantities and fuel state into it"). The checklist fixed this same term in L1-AER-640 by listing the quantities. -890's "with their validity" relies on *Validity range*, which covers only direction quantities. (G1-F11 theme.) | Minor | -880: "… annunciation content, the indicated quantities of L1-AER-890 and fuel state into it", or add a glossary *Navigation quantities* entry (the F-AER-09 list: altitude, horizontal speed, vertical speed, heading, track, with validity). For -890, add *Validity (flag)* to the glossary or cite CV-580 in the statement. |
| G1-R04 | FA §4.2, §5.3, I-06; CONVENTIONS CV-580 | (check) Residues of D55 in the analysis and conventions. (a) FA §4.2: "the flight software (NAV, AF, FC) runs once per control frame", but L1-AER-680 and glossary *Flight software* now include FCP. (b) FA §5.3: "FCP owns L1-AER-480, -490, -500, -870 and shares -470, -610, -620, -660, -680, -880 … and -560 to -580". This omits -430 and -690; §6.2 gives FCP 15 records. (c) CV-580: "How the Aeronef behaves when a quantity is invalid (validity flags, annunciation, mode reversion) is a requirement matter for NAV, AF and TM". After D55, annunciation is FCP's, and TM only observes. This is the CV-780 correction (G1-F22) not carried to CV-580. (d) Fuel state FU → FCP is in the closed list of both L1-AER-430 (vehicle-model boundary ICD) and L1-AER-880 (ICD-FCP). I-06 names both homes, so the same signal could be defined twice by different authors (I1, C8). | Minor | (a) "(FCP, NAV, AF, FC)". (b) Add -430 and -690 to the shared list. (c) "NAV, AF and FCP" (a CR on a fixed convention, as CR-B1-10). (d) Say in IN-B1-08 or the L1-AER-880 rationale that ICD-FCP references the vehicle-model boundary definition of the fuel state rather than redefining it, and do the same for the NAV quantities, which are defined once in ICD-NAV-AF. |
| G1-R05 | L1-AER-480 rationale ("Children must show") | Residue of G1-F09 and D59: "(Test) a selection scripted at a stated simulation time and the same selection made interactively at that time give the same operational data." D59 says that repeat runs "are not required to be bit-identical", and that the comparison is the verdict and agreement within the stated tolerances (D63 Q4). This guidance asks for more than L1-AER-690. | Minor | "… give the same pass or fail verdict against each success criterion assessed on the run (D59)". |
| G1-R06 | registers/DECISIONS.md header; FA header and §9; work/B1/interface_needs.md §3 | Stale metadata after D63. DECISIONS.md: "Plan-level decisions D1–D62"; the FA header: "§9 (D1–D62)" and "L1 (draft `work/B1/L1_AER.md`)" (G1-F15). FA §9 first item: "Owner questions raised at the G1 rework: … 'Questions for the owner'", and interface_needs §3: "Remaining: the G1 owner questions". All four were answered by D63 on the same day. | Minor | D1–D63 in both headers; link L1 to requirements/L1.md; replace both owner-question pointers with "answered by D63". |
| G1-R07 | CONOPS §9; CHANGE_REQUESTS CR-B1-12; GLOSSARY *Mode state* | Wording and record residue. (a) CONOPS §9 row "P-SYS-120 \| … (Set, 3 g)" adds a system value as a number, against CONOPS §1.1 ("System values never appear as numbers in the text"). G0 R-F05(e) removed "3 g" from §5 for the same reason. §4.2 still states "100 kt … 50 kt … 150 kt" (pre-existing). (b) CR-B1-12 lists the CONOPS sections changed but omits SC-090 and SC-100, which the rework edited for D60 ("horizontal position … (D60)"). Its approval line cites "D49, D53, D55, D59" but not D60 or D62 (§4.2 gust rise time). (c) Glossary *Mode state* and the L1-AER-470 rationale: "a mode that arms, becomes active, leaves the armed state or is disengaged". The glossary *Active (mode)* says "'engaged' is not used for modes"; disengagement applies to autoflight. | Minor | (a) "(Set)" only, or cite D45. Replace the §4.2 numbers with `[P-SYS-430]`, `[P-SYS-560]`. (b) Add SC-090, SC-100 to the CR-B1-12 affected list and D60, D62 to its approval. (c) "… a mode that arms, becomes active or leaves the armed or active state, or autoflight being disengaged, changes the mode state." |

Observations, not findings: the plan's Phase 1 task rows A2 ("They cover the catalogue in D3") and A3 ("VOR radials") and the CONVENTIONS §1 NED trade table ("as aviation and VOR radials use it") describe completed or historical work. The deleted sections of CONVENTIONS §7 and the deleted L1 records keep their original text for the record, as intended. The L1.md header outside the section still reads "Draft (task B1, 2026-10-28), awaiting Gate G1 (#15)", as the dispositions note. It is updated when L1 is baselined.

Checked and found consistent (no finding):

- **New records L1-AER-850 to -890.** Each has a parent that exists, is live and is allocated to AER. Each has a sufficiency argument, a Type and a verification consistent with D58 (-850 and -860 are leaves with direct criteria; -870, -880, -890 use roll-up with "Children must show (D58)"). Allocations are consistent with FA §6.1. Each appears in §6.2 and §8 and in the VCRM.
- **Interface definitions.** L1-AER-880 matches FA I-06, I-16, I-18, I-19, §3.3 and §5.1. L1-AER-890 matches I-17 and IN-B1-04. ICD-FCP is in plan §3, task I1 and TT-680.
- **L0 change requests.** CR-B1-07 to -12 rows match the edits. The version bumps are L0-OBJ-030 v2→3, L0-CON-020 v2→3, L0-CON-290 v2→3 and L0-CON-310 v5→6. L0-ASM-050 and -110 have no version field (asm). Status stays Baselined on every changed L0 record. No L0 record changed outside the CRs. The L0.md "Changed since" line lists them all. work/A1 is in sync (assembler: up to date).
- **P-SYS-570 and the register.** P-SYS-570 is TBD with owner and source. It is cited and listed by L1-AER-290, -300, -310 and -460, and registered in TT-650 and in each of those records' TT field rows. TT-650 to TT-730 are present; TT-700 is closed (D63).
- **Glossary merge.** 44 new terms, no duplicates, alphabetical. Every term the inspection and the checklist listed is now defined or reworded away, except R-03.
- **FUNCTIONAL_ANALYSIS §6.2 and §8.** They are identical to the record fields for all 85 live records (allocation, type, parents). The subsystem counts are DYN 23, FU 22, EF 23, FC 23, AF 20, FCP 15, NAV 9, TM 10, leaves 17. Every L0 record allocated to AER has an L1 child. The 18 TST/RVS-only records have none.
- **Budgets §7.** §7.2 closure and disturbance share, §7.3 endurance formula (matching L1-AER-360), §7.4 split, and §7.5 annunciation split (P-AF-060 ≤ P-SYS-470 − P-TM-010) are consistent with the record rationales and PARAMETERS.yaml.
- **Withdrawn items.** VOR, flight path angle, track hold and position hold as a mode, and P-SYS-260, P-SYS-520 and P-NAV-050, appear only in Deleted records or sections, in withdrawal notes, and in the history columns of the plan and the ConOps question log. The one exception is R-02.

## 4. Tool results (at e77d653)

| Check | Result | Assessment |
| --- | --- | --- |
| `python tools/assemble.py --all --dry-run` | "L0: sections ASM, CON, OBJ, SUC already up to date"; "L1: sections AER already up to date" | In sync; work/A1 drafts match L0.md |
| `python tools/lint.py` | 0 errors, 66 warnings, all COMPOUND: 17 on L0 (decided at G0), 49 on L1 (46 records) | All L1 warnings are judged in checklist_L1.md §2 or dispositions.md; the new -860 to -890 are judged there and the re-inspector agrees |
| `python tools/trace_check.py` | 70 errors: 68 CHILDLESS (exactly the 68 allocated L1 records; no L2 yet) and 2 DERIVED (L1-AER-680 DD-010, L1-AER-710 DD-020); 0 ORPHAN, 0 DELETED-REF, no other code | Accepted at G1. See G1-R01 for the DERIVED pair against L1-AER-860 |
| `python tools/param_check.py` | 0 errors, 19 warnings, all PARAM-UNUSED: P-AF-010 to -040, -090, -100, -120, -130, -140, -170, -190, -210, -220; P-NAV-010, -030; P-TM-020 to -050 | Accepted (ConOps, conventions and L2 parameters, D33). P-SYS-570 and P-SYS-200 to -220 are referenced |
| `python tools/vcrm.py --check` | 0 errors, 0 warnings | Clean |
| `python -m pytest -q tools/tests` | 39 passed | Clean |

These match the "Checks after rework" section of dispositions.md. Nothing outside the accepted classes was reported.

## 5. Gate G1 exit and recommendation

- **Open Major findings: none.** All 12 inspection Majors and the three checklist Majors are closed against the text. The Accepted and Deferred dispositions have a recorded basis: D63 for the subject records, the L0-CON-100 reading and L1-AER-630; #81 and TT-330 for L1-AER-020; I1 and TT-680/-720 for the vehicle-model ICD home.
- **New findings: seven, all Minor** (G1-R01 to G1-R07). None of them would mislead the L2 agents about content. R-01 and R-06 are register and metadata actions for the orchestrator. R-02, R-03, R-05 and R-07(c) are one-line record or glossary edits in work/B1 and the glossary. R-04 and R-07(a, b) are FA, ConOps, CR-row and one CV edits.
- **Tools:** clean apart from the accepted CHILDLESS, DERIVED and PARAM-UNUSED classes.

**Recommended exit decision: Baseline.** No Major is open. The moderator can close the seven Minors without an owner ruling or a further review. Close G1-R01 before tagging, by entering DD-010 and DD-020 in registers/DECISIONS.md, so that the baselined L1-AER-860 passes its own criterion. Then refresh the L1.md header and tag L1 once the owner approves.
