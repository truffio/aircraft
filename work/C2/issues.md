# C2 — Issues, change requests, design decisions and questions for the project owner

Task C2 (plan §6, Phase 3): the L2 FU section, fuel and mass properties (`work/C2/L2_FU.md`). **Rework** (2026-11-05, TT-840): the G2 findings on FU with the owner rulings of D72, the landing gear and ground operations of D69 from the approved B3 package (D73), and the C3 answer that EF computes the resultant control force and moment once (DD-C3-05). The finding-by-finding dispositions are in `rework_G2_D69.md`; the MS-DYN content that C2 supplies is in `ms_dyn_s6_s7_fu.md`.

## 1. Summary

| Item | Count |
| --- | --- |
| L2 FU records | 34: 26 changed (v2), 3 unchanged (L2-AER-FU-210, -240, -260), 5 new (L2-AER-FU-300 to -340), 0 deleted |
| Types | Functional 9, Constraint 8, Interface 8, Model fidelity 7, Performance 1, Documentation 1 |
| Verification methods | Test 15, Inspection 12, Analysis 6, Demonstration 1 |
| L1 parents covered | 26: the 22 of the first draft, L1-AER-940 (new, allocated to FU), and L1-AER-900, -260, -270 (FU added by CR-C2-04) |
| Derived records | 0 |
| G2 findings closed on the FU side | 12 (G2-F05, -F10, -F11, -F13, -F16 to -F22, -F24), plus the G2 §4 EF note |
| New DD proposals | DD-C2-05, DD-C2-06 (revises DD-130), DD-C2-07 (§4) |
| Parameters | No new parameter; values proposed for P-FU-070, -080 (TBD → TBR); notes and descriptions updated (`param_proposals.md`) |
| Change requests | CR-C2-04 (L1 allocations), CR-C2-05 (glossary, five terms) (§3) |
| Owner questions | 1 (§2) |
| Interface needs | `interface_needs.md`: IN-C2-19, -24, -50 to -54 new; IN-C2-10 to -18, -20 to -23 closed or superseded |

**Coverage, L1 parent → FU children.**

| L1 record | FU children |
| --- | --- |
| L1-AER-020 | L2-AER-FU-180 |
| L1-AER-100 | L2-AER-FU-060 |
| L1-AER-150 | L2-AER-FU-010, -020, -030 |
| L1-AER-160 | L2-AER-FU-040, -050, -070 |
| L1-AER-170 | L2-AER-FU-010 |
| L1-AER-180 | L2-AER-FU-090, -100, -110, -120 |
| L1-AER-190 | L2-AER-FU-050, -080, -090, -340 |
| L1-AER-200 | L2-AER-FU-200, -340 |
| L1-AER-210 | L2-AER-FU-150, -160, -310 |
| L1-AER-220 | L2-AER-FU-120, -170, -180, -190, -310, -330 |
| L1-AER-260 | L2-AER-FU-320 (with CR-C2-04) |
| L1-AER-270 | L2-AER-FU-320 (with CR-C2-04) |
| L1-AER-290 | L2-AER-FU-140 |
| L1-AER-360 | L2-AER-FU-290 |
| L1-AER-430 | L2-AER-FU-130 |
| L1-AER-560 | L2-AER-FU-210, -240 |
| L1-AER-570 | L2-AER-FU-220, -240 |
| L1-AER-580 | L2-AER-FU-230, -240 |
| L1-AER-630 | L2-AER-FU-250 |
| L1-AER-640 | L2-AER-FU-260 |
| L1-AER-660 | L2-AER-FU-020, -030 |
| L1-AER-690 | L2-AER-FU-270 |
| L1-AER-720 | L2-AER-FU-280 |
| L1-AER-880 | L2-AER-FU-240 |
| L1-AER-900 | L2-AER-FU-310 (with CR-C2-04) |
| L1-AER-940 | L2-AER-FU-300, -040, -060 |

L1-AER-210 lost L2-AER-FU-120 as a child (G2-F05: the centre of gravity no longer crosses I-04); it keeps three FU children and DYN's L2-AER-DYN-200.

## 2. Questions for the project owner

The first-draft questions C2-Q1 to C2-Q6 are answered (D65, D66; C2-Q5 by D68). C2-Q7 is answered too: CR-C2-04 approved (D74, 2026-11-08).

| ID | Question | Recommended answer | Affects |
| --- | --- | --- | --- |
| C2-Q7 | **FU in the allocation of three L1 records (CR-C2-04).** L1-AER-900 asks the FU requirements to show that the landing gear moves no mass property, and L1-AER-260 v2 and -270 v2 make fuel remaining a condition of a landing and a contact at exhaustion a crash, which DYN can only classify with FU's fuel availability (CR-B3-39 already sends I-03 to the ground contact function). All three are allocated without FU (B3: "allocations do not change"). Add FU to their allocation? | **Yes, approve CR-C2-04.** The trace then shows the FU children (L2-AER-FU-310, -320) under parents that are allocated to FU, and FUNCTIONAL_ANALYSIS §6.2 shows the FU share. If the owner declines, L2-AER-FU-310 keeps L1-AER-210 and -220 as its parents, and L2-AER-FU-320 becomes Derived, with a DD recording that DYN's contact classification needs FU's availability. | L1-AER-260, -270, -900; FUNCTIONAL_ANALYSIS §6.2; L2-AER-FU-310, -320 |

**Answered earlier (for the record):** C2-Q1 varying inertia (D65, DD-120); C2-Q2 resultant consumption form (D65, DD-110); C2-Q3 per-step data for the fuel integral (D65); C2-Q4 reject an out-of-range initial fuel (D65, DD-140); C2-Q5 #59 (FU share closed by D65; the autoflight behaviour answered by D68); C2-Q6 masses 1000 kg and 500 kg (D65), coefficients and hover endurance from the endurance at maximum speed (D66).

## 3. Change requests

### 3.1 Against L1 (baselined; proposed, not applied)

| ID | Against | Requested change | Reason | Recommendation |
| --- | --- | --- | --- | --- |
| CR-C2-01 | L1-AER-100 rationale | — | — | Applied (D65). |
| CR-C2-02 | L1-AER-190 rationale | — | — | Withdrawn (D65). |
| CR-C2-04 | L1-AER-260 v2, L1-AER-270 v2, L1-AER-900 (field `Allocated to`); FUNCTIONAL_ANALYSIS §6.2 rows | L1-AER-260: "DYN, TM" → "DYN, TM, FU". L1-AER-270: "DYN, TM" → "DYN, TM, FU". L1-AER-900: "DYN" → "DYN, FU". Add the children-must-show sentence to L1-AER-260 and -270: "(Inspection) the fuel availability that the effectors use is the one the ground contact model uses." Version + 1 (on top of the B3 versions). FA §6.2: tick FU in the three rows; FU count 23 → 26. | L1-AER-900's rationale already names the FU requirements; the "fuel remaining" and "at fuel exhaustion" conditions of CR-B3-12 and -13 need FU's fuel availability (D68, D73 B3-3; I-03 to F-AER-12 by CR-B3-39). See C2-Q7. | Approve with the B3 records. |

### 3.2 Against a fixed specification

| ID | Against | Requested change | Reason | Recommendation |
| --- | --- | --- | --- | --- |
| CR-C2-03 | GLOSSARY *Fuel state* | — | — | Applied (D65). |
| CR-C2-05 | GLOSSARY *Consumption rate*, *Consumption relationship*, *Fuel availability*, *Initial-condition error*, *Dry-mass distribution, fuel-mass distribution*; new term *Exhaustion step* | As in `glossary_proposals.md` §2 and §1. | DD-C3-05 (FU charges the resultant EF computes), G2-F10 (exhaustion step), D68 and CR-B3-39 (availability to the ground contact model), G2-F11 and G2-F17 (error item), DD-C2-07 and L1-AER-900 (distributions, gear). | Editorial; apply at the I1 glossary merge. |

### 3.3 Notes on L1, the functional analysis and other drafts (no change request)

| ID | Note | Proposed action |
| --- | --- | --- |
| N-C2-01 | FUNCTIONAL_ANALYSIS §7.3 rule: add the margin [P-FU-100] and "from a takeoff" (CR-B3-41 does the second). | I1, with CR-B3-41. |
| N-C2-02 | The mass distributions: closed by G2-F16 (C2 owns the derivation; fuel volume = body shape, DD-C2-07). | Closed. |
| N-C2-03 | TT-580: rewrite as the C5 annunciation item (B3 impact list §6). | I1, with B3. |
| N-C2-04 | *FU subsystem* as the subject: merged in the glossary. | Closed. |
| N-C2-05 | Expected checks after assembly: lint 0 errors, 18 COMPOUND warnings on FU (each judged, §5); trace: NO-PARENT for L1-AER-900 and -940 until the B3 records are merged, then none; param_check: PARAM-UNUSED for P-SYS-290 (expected, D72 Q4). | Orchestrator. |
| N-C2-06 | Several FU tests read outputs that the operational data do not carry (centre of gravity, inertia, fuel availability, per-step values). They use the TST recording of IN-C2-30. | TST plan extension. |
| N-C2-07 | **L2-AER-FU-290 criterion 2 is a long run.** D72 rules out long *credibility checks*. The simulated hover from a takeoff to exhaustion (about 47 h) is the performance test that L1-AER-360 v2 asks its children to show, not a credibility check, so C2 keeps it. If the owner wants no run of that length at all, the alternative is an analysis: the per-step fuel accounting checked over a short hold (C-8) plus the closed form. | Owner chose the analysis (D74, CR-C2-05): L2-AER-FU-290 v3 confirms the closed form over a hold of [P-DYN-270]. |
| N-C2-08 | **L2-AER-EF-140** still gives FU "the effector outputs … with the control force and the control moment". FU uses only the resultant (L2-AER-FU-070 v2). | C3 may drop the effector outputs from L2-AER-EF-140 at I1 (editorial, IN-C2-21). |
| N-C2-09 | B3 impact list §2 suggested adding the fuel availability for DYN to L2-AER-FU-120. C2 made it a separate record, L2-AER-FU-320, because it crosses I-03, not I-04, and has different parents. | Information for I1. |
| N-C2-10 | B3's P-SYS-280 note ("about 0.7 s of climb and one gear transit") and P-FU-100 description (the takeoff) agree with L2-AER-FU-290 v2: the climb lasts about 0.7 s, and the gear transit is flown at the hover height, inside the hold. | None. |

## 4. Design decisions

DD-C2-01 to -04 are accepted as DD-110 to DD-140 (D65). The rework proposes three more. The orchestrator assigns the DD-nnn numbers.

| ID | Decision | Alternatives considered | Rationale | Requirements |
| --- | --- | --- | --- | --- |
| DD-C2-05 | At the start of each run FU checks that the inertia tensors `[P-FU-070]` and `[P-FU-080]` of the vehicle parameter set match, within `[P-FU-090]`, the values that the MS-DYN mass-properties model derives from that set's body dimensions and masses, and rejects the set otherwise (G2-F17). | (a) FU derives the tensors at run start and ignores the set's values. (b) Check the database values only (the G2 state). | The run uses only values its parameter set states, and the parameter set named in the operational data is what the run used (L1-AER-650); consistent with the rejection of DD-140. (a) would run values that no parameter set records; (b) lets a campaign run a body that no mass distribution gives. | L2-AER-FU-330 |
| DD-C2-06 | **Revises DD-130.** The exhaustion step is the step whose remaining fuel at its start is above zero and at most the fuel `fl(q·Δt)` it would use at its consumption rate. In it the flow is the fuel left divided by the step, and the remaining fuel at its end is set to zero. In every other step the remaining fuel is reduced by the same `fl(q·Δt)` used in the comparison (G2-F10). | (a) Compute `m_f − ṁ_f·Δt` in every step (the G2 state: residuals of either sign). (b) Clamp a negative result to zero (leaves positive residuals, so one more step of full output on almost no fuel). | Exactness at exhaustion does not depend on floating-point rounding; no step can end below zero; the fuel-mass integral holds within rounding; the effector model stays free of fuel bookkeeping, as DD-130 intended. | L2-AER-FU-050, -090, -200, -340 |
| DD-C2-07 | **Refines DD-120.** The fuel volume is the body shape: the fuel, like the dry mass, is uniform over the capsule of the MS-DYN vehicle geometry, with its density falling in proportion to the remaining fuel mass. Hence `[P-FU-080] = [P-FU-070]·[P-FU-010]/[P-FU-030]` (G2-F16). | (a) A smaller fuel volume centred on the centre of gravity, with its own dimension parameters. (b) Fuel as a point mass at the centre of gravity (a constant inertia, excluded by D65). | No new parameter; centred and symmetric by construction; the inertia follows the shape when the provisional shape changes (L0-CON-140); C3 already uses the resulting full-fuel inertia for the moment budget. (a) adds parameters for no effect that the requirements use. | L2-AER-FU-160, -170, -190, -330 |

## 5. Self-check (METHODOLOGY §13.1 and §13.2)

**§13.1, per record.**

- One "shall" each; subject the FU subsystem; EARS patterns: ubiquitous (most records), event-driven (L2-AER-FU-010, -020: "When a run starts"), unwanted behaviour (L2-AER-FU-030, -330: "If … then"). Lint: 0 errors on 34 records.
- No number in a statement; each quantity is a parameter ID under Parameters. "Zero" and "one" are definitional constants only.
- No vague terms, escape clauses, open lists or absolutes (lint clean); no TIMING or KEYWORD warning.
- COMPOUND warnings (18), each judged one thought (D30):
  - closed lists of one object (6): L2-AER-FU-010 (the FU parameters), -120 (two mass properties), -260 (two signals), -270 (the inputs of one function), -280 (the five MS-DYN models), -330 (the inputs of one derivation);
  - one relationship with its operands (8): -040 (the two terms of one sum), -050 (the flow in a step, with its one exception, the exhaustion step), -060 (the two consumption sets), -070 (the resultant pair), -170 (the two tensors of one sum), -190 (the shape and the distributions behind one derivation), -290 (one inequality), -300 (both resultants zero);
  - a pair that is one constraint (4): -130 (the two kinds of boundary output), -160 (both distributions centred), -200 (the two values of one signal), -330 ("or" over the two tensors of one check).
  None forms a tree of cases.
- Solution-free: no algorithm, data structure or code in a statement. The consumption form, the depletion model, the exhaustion step and the run-start check are model physics or run set-up, recorded as DDs with alternatives; the equations are in `ms_dyn_s6_s7_fu.md`, not in the statements.
- Terms: glossary terms, the B3 terms (*gear position*, *effectors off*, *on the ground*), or the proposals of `glossary_proposals.md` (*exhaustion step*). Axes and signs per CONVENTIONS (CV-160, CV-340, CV-350).
- A rationale with a "Sufficiency" argument per L1 parent in each record; parent, source, verification method, procedure ID and success criteria in each record; Parameters and TBD/TBR fields follow the G2-F20 rule.
- Criticality Not assessed; each TBD or TBR names an owner and a closure point.

**§13.2, the set.**

- Each L1 record allocated to FU, L1-AER-940 included, has at least one FU child, with the sufficiency argument in the first child and "see …" in the others (coverage table, §1). The three records of CR-C2-04 have their FU child ready.
- Types: functional, interface, constraint, model fidelity, performance and documentation are present. Failure handling is deferred (tailoring), and fuel exhaustion is nominal behaviour throughout; in flight its consequence, a crash at contact, is DYN's classification (D68).
- Interfaces: each FU interface has an FU record and a home (MS-DYN, the boundary ICD, ICD-FCP, ICD-AER-TST); the other side is in `interface_needs.md`. I-04 now matches DYN (G2-F05); I-01 matches EF (DD-C3-05); I-03 goes to EF and DYN.
- No derived records.
- D69 consistency: no FU record assumes a run ends at the first ground contact or starts airborne; zero flow with the effectors off follows from DD-110 with no new term; the hover endurance counts from a takeoff, and the inequality still closes (490.35 kg of 500 kg).
- Manual sections affected (written after the requirements baseline, L1-AER-840): the Vehicle Operating Manual fuel limitations, the LOW FUEL and FUEL EXHAUSTED procedures, and the fuel on the ground (none used with the effectors off).
