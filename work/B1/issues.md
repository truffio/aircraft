# B1 — Issues, change requests, design decisions and questions for the project owner

Task B1 (plan §6, Phase 2): L1 Aeronef requirements (`work/B1/L1_AER.md`, 84 records) and `specs/FUNCTIONAL_ANALYSIS.md`. Questions are at L1 level: the Aeronef as a whole, its budgets, its interfaces and its architecture. Mode-level questions stay deferred at L2 (D33); they are listed in §7 only where L1 touches them. The local IDs B1-Qnn need GitHub issues; cite them by issue number once filed.

## 1. Summary

| Item | Count |
| --- | --- |
| L1 records | 84: Functional 14, Performance 19, Interface 10, Constraint 22, Model fidelity 8, Documentation 11 |
| Allocated to L2 subsystems | 69 (DYN 24, FU 21, EF 24, FC 24, AF 20, NAV 9, TM 16 allocations) |
| Leaves at L1 (`Allocated to: —`), verified directly | 15: L1-AER-510, -520, -700, -730 to -840 |
| Derived | 2: L1-AER-680 (DD-010), L1-AER-710 (DD-020) |
| L0 records allocated to AER without an L1 child | 0 of 40 |
| New parameters proposed | 23 (`param_proposals.md` §1) |
| Owner questions | 10 (§2) plus Q5 (#6, §3) |
| Change requests to L0 | 2 (§4) |

## 2. Questions for the project owner (L1 level)

| ID | Question | Proposed answer | Affects |
| --- | --- | --- | --- |
| B1-Q01 (#95) | **Logical architecture and the flight control panel (#80.3).** Approve the architecture of FUNCTIONAL_ANALYSIS §5: a three-layer cascade (autoflight guidance → flight control → effectors) around a vehicle model (DYN, FU, EF) behind one fixed boundary, a separate NAV that derives every guidance quantity from the true state, and TM as an observer. And: is the flight control panel a separate L2 subsystem (#80.3)? | Approve the cascade. Do not add an FCP subsystem now: crew input sits in AF (F-AER-10) and crew presentation in TM (F-AER-13), so the seven planned subsystems stay as they are. The panel content (#79) is then an AF section at L2. If the owner prefers an FCP, the records that move are listed in FUNCTIONAL_ANALYSIS §5.3. | L1-AER-480, -490, -500, -560 to -580; plan §3, §6 (C5, C7) |
| B1-Q02 (#96) | **How L1 is verified.** D40 says a higher-level requirement passes when its children have passed and the decomposition is reviewed. Apply it to L1 as D41 does to L0? | Yes. Each L1 record allocated to subsystems has the roll-up verification "Inspection — each child requirement has passed its verification and the decomposition has been reviewed (D40)", and its rationale says what the children must show. The 15 leaves at L1 (cross-cutting constraints, documentation) keep their own direct method. | Every L1 record; Phase 5 (V4) |
| B1-Q03 (#97) | **Crew acceleration limit.** (a) L0-CON-310 leaves the evaluation point to a lower level: centre of gravity or crew station? (b) The 3 g value of P-SYS-120 is TBR "for now" and closes at G1: confirm it? | (a) The crew station (DD-030): that is where the crew feels the load, and under rotation it sees more than the centre of gravity. The cost is a crew station position (P-DYN-400) and a rotational share in the budget. (b) Confirm 3 g. | L1-AER-250, -290; P-SYS-120<br>**Answered (D45):** centre of gravity; 3 g confirmed. |
| B1-Q04 (#98) | **Effector authority shape.** Must the Aeronef hold itself up along any body axis (any attitude), or only along the negative body z axis (up at level attitude)? | Only along the negative body z axis (P-SYS-400), with a smaller authority on the other five directions (P-SYS-410). Pitch and roll stay level in autoflight (D10), so weight is always carried on that axis; equal authority on every axis would size the effectors for attitudes that serve no purpose. | L1-AER-120, -130; C3<br>**Answered (D46):** as proposed; weight is carried along the negative body z axis. |
| B1-Q05 (#99) | **Wind limit.** Performance (speed capability, position holding) applies up to a maximum wind speed, P-SYS-430. Accept the concept? What value? And is the wind horizontal only (IN-B1-07)? | Accept. Horizontal wind only in version 1. Value TBD by the owner; it drives the drag share of the effector budget. | L1-AER-130, -310, -460; P-SYS-430<br>**Answered (D51):** steady wind 0 to 100 kt plus gusts of up to 50 kt on top (150 kt instantaneous), horizontal only; L0-ASM-050 changed (CR-B1-03). |
| B1-Q06 (#100) | **Landing envelope quantities.** L0-CON-290 leaves the envelope to a lower level. Which quantities define it? | Three: vertical speed magnitude (P-SYS-500), horizontal speed (P-SYS-510) and sensed acceleration (P-SYS-520 ≤ P-SYS-120), at the contact sample. Values TBD at G2. | L1-AER-280<br>**Answered in part:** vertical speed of a 2 ft fall (3.458 m/s), horizontal 0.5 m/s, acceleration 1/4 g. Open: #100.1. |
| B1-Q07 (#101) | **Performance envelope values.** P-SYS-200 to P-SYS-280 (operating volume, maximum horizontal speed, climb and descent vertical speeds, flight path angle, heading rate, hover endurance) are still TBD. Set them now, or leave them TBD until the L2 budgets close (I1)? | The owner gives target values at G1 if the owner has them in mind (they set the effector and fuel budgets); otherwise they stay TBD and I1 proposes values that close the budgets. | L1-AER-120 to -140, -310 to -360<br>**Answered (D47):** TBD for now. |
| B1-Q08 (#102) | **Budget proposals.** Accept as TBR: vehicle acceleration 1.5 g (1 g autoflight, 0.5 g flight-control transients); position holding 1 m (0.5 m guidance, 0.5 m regulation); simulation step 0.01 s, control frame and output sample 0.02 s, control-loop latency 0.1 s, annunciation latency 0.5 s; low-fuel threshold 0.1 of capacity; gravity = standard gravity? | Accept all as TBR (FUNCTIONAL_ANALYSIS §7). Each closes at G2 when the L2 values exist. | P-SYS-440, -450, -300, -310, -470, -480, P-TM-010, P-FU-020, P-DYN-010, P-AF-160, -200, P-FC-010, -020<br>**Answered (D48):** accepted as TBR. |
| B1-Q09 (#103) | **Manual control as an optional feature.** Plan §1 says manual control is "recorded as an optional feature (EARS 'Where' pattern)". L0-CON-180 excludes direct manual flight controls. Write the "Where" record? | No. A "Where a manual control is installed" record would contradict L0-CON-180. Keep N-180 in the ConOps only, and amend plan §1 to say so. | L1-AER-520; plan §1<br>**Answered (D49):** no record now; a lower-level matter. |
| B1-Q10 (#104) | **Determinism and headless running.** L0-OBJ-110 (reproducible runs) and L0-CON-190 (no graphical display) are allocated to the TST only, but the Aeronef's own software decides both. Add AER to their allocation (CR-B1-01, CR-B1-02)? | Yes. The Aeronef children L1-AER-690 and -700 are written against them already. | L0-OBJ-110, L0-CON-190<br>**Answered (D50):** approved; CR-B1-01 and -02 applied to L0. |

## 3. Q5 (#6) — mode combinations: proposal for the owner

**Status.** The owner deferred Q5 to L2, where the modes are defined (D33, #6 comments). B1 does not write any of this as an L1 requirement (L1-AER-450 only references the catalogue). The proposal is offered for a decision at G1 so that C5 starts from an agreed rule. It revises the plan's proposal to match D11, as the owner asked on #6.

### 3.1 Proposal (recommended: option A, three airliner-style groups)

| Group | Modes (D3) | Armed modes |
| --- | --- | --- |
| Vertical | Climb or descent on flight path angle (FPA), climb or descent on vertical speed (V/S), altitude capture, altitude hold (ALT), hover at altitude (HOVER) | Altitude capture |
| Lateral | Heading hold (HDG), track hold (TRK), VOR radial tracking (VOR), position hold (POS HOLD) | VOR |
| Speed | Horizontal speed (SPD) | — |

Rules:

1. **One per group.** Each group has at most one active mode and at most one armed mode.
2. **Arm, then capture (D16).** Altitude capture arms with FPA or V/S when the selected altitude lies in the direction of motion; VOR arms while HDG or TRK is active. At capture the armed mode becomes active and replaces the active mode of its group; the other groups do not change.
3. **Groups are independent** except where the compatibility matrix below forbids a combination.
4. **POS HOLD covers the speed group.** POS HOLD holds the horizontal position, so the horizontal speed is fixed at zero: while POS HOLD is active, the speed group has no active mode (SPD suspended, and annunciated as such). Because D11 says the vehicle stops on every axis, the vertical mode with POS HOLD is ALT or HOVER.
5. **HOVER brings POS HOLD (D11).** Engaging HOVER makes POS HOLD active in the lateral group if it is not already.
6. **FPA needs horizontal velocity (D13).** FPA is compatible with HDG, TRK and VOR, with SPD active at a target above a minimum horizontal speed that C5 sets (at least the flight-path-angle validity speed P-NAV-020). It is not compatible with POS HOLD.
7. **TRK and VOR need a valid track.** They are compatible with SPD at a target at or above the track validity speed P-NAV-010.
8. **A new selection wins.** If the crew selects a mode that is incompatible with the active mode of another group, the selection takes effect, and the other group reverts to its hold mode at its current value: vertical to ALT at the current altitude, lateral to HDG at the current heading, speed to SPD at the current horizontal speed. This matches N-100 ("choose a different mode at any time") and A2-Q10. The alternative, rejecting the selection with no change, is simpler but leaves the crew guessing why nothing happened.

Compatibility matrix, vertical × lateral (✓ compatible, ✗ not compatible; the speed condition is in brackets):

| Vertical \ Lateral | HDG | TRK | VOR | POS HOLD |
| --- | --- | --- | --- | --- |
| FPA | ✓ (SPD above the FPA minimum) | ✓ (SPD above the FPA minimum) | ✓ (SPD above the FPA minimum) | ✗ (D13) |
| V/S | ✓ (any SPD, including zero) | ✓ (SPD ≥ track validity) | ✓ (SPD ≥ track validity) | ✗ (see note) |
| Altitude capture (armed or active) | ✓ | ✓ | ✓ | — (arms only with FPA or V/S) |
| ALT | ✓ | ✓ | ✓ | ✓ (speed group covered) |
| HOVER | ✗ (HOVER brings POS HOLD) | ✗ | ✗ | ✓ (required, D11) |

Note on V/S with POS HOLD: forbidden under the "stops on every axis" reading of D11. A vertical climb or descent over a point is still possible with HDG, V/S and SPD at zero (SC-040, SC-110 leg 8). If the owner reads D11 as "POS HOLD holds the horizontal position", V/S with POS HOLD becomes ✓ and gives a climb that also holds the point against the wind.

Heading in TRK, VOR, POS HOLD and HOVER: held at its value when the mode became active (ConOps reading A2-Q03, confirmed at L2).

### 3.2 Option B (recorded alternative): a fourth, heading group

Heading and track are independent on the Aeronef (CV-550, N-110). Option B moves HDG into its own heading group, so the lateral group holds only the horizontal path (TRK, VOR, POS HOLD) and the crew can select a heading while flying a track. It uses the vehicle's independence more fully, but it departs from the airliner concept that manuals and the RVS can relate to, and it needs a path mode for "fly where the nose points". **B1 recommends option A for this cycle**, with B kept for a later version.

### 3.3 Why this answers Q5 at the right level

It fixes which modes can be active together and what happens on a conflict, which is all that Q5 asks. It does not fix capture conditions, transition criteria, labels or per-mode accuracies; those stay with C5 and Phase 4. It respects D11 (POS HOLD lateral, HOVER vertical, HOVER needs POS HOLD), D13 (FPA not with POS HOLD) and D16 (arm, then capture).

## 4. Change requests to L0 (for `registers/CHANGE_REQUESTS.md`)

| ID | Against | Requested change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-B1-01 | L0-OBJ-110 | `Allocated to: TST` → `TST, AER`; add to the rationale that the Aeronef software must be deterministic (L1-AER-690). | Reproducibility rests on L0-ASM-020 (deterministic runs). The Aeronef runs inside every run, so its software can break reproducibility; the TST alone cannot guarantee it. | Approved (D50, #104) |
| CR-B1-02 | L0-CON-190 | `Allocated to: TST` → `TST, AER`; add that no Aeronef function needs a display (L1-AER-700). | The simulation core executes the Aeronef; a display dependency inside the Aeronef would break the headless core. | Approved (D50, #104) |

No other change to L0 is needed: every AER-allocated L0 record has at least one L1 child, and no L1 record contradicts L0.

## 5. Proposed design decisions (for `registers/DECISIONS.md`)

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-010 | The flight software (NAV, AF, FC) runs once per control frame of fixed period, an integer multiple of the simulation step, in the order NAV → AF → FC (FUNCTIONAL_ANALYSIS §4.2). | Execute at every simulation step; asynchronous or event-driven execution. | A whole number of steps per frame keeps sampling exact on the CV-840 time base and decouples the integration step (accuracy) from the software rate. Execution at every step ties the two; asynchronous execution breaks determinism (L1-AER-690). | L1-AER-680 |
| DD-020 | The control-loop latency is bounded at aircraft level and split into one control frame plus the effector command response time. | No latency requirement (leave it to C4); a separate budget per axis. | A single number lets C3 (effector response) and C4 (control-law margins) size against the same budget (METHODOLOGY §7 rule 4). Per-axis budgets are a C4 refinement if needed. | L1-AER-710 |
| DD-030 | Withdrawn: the owner chose the centre of gravity (D45, #97). | | | | 
| DD-040 | Logical architecture: three-layer cascade around a vehicle model behind one fixed boundary; separate NAV; TM as an observer; crew input in AF and crew presentation in TM (no FCP subsystem). | Integrated guidance and control; NAV inside AF; a separate FCP subsystem (FUNCTIONAL_ANALYSIS §5.3). | Replaceable control laws and autoflight (L0-CON-200, -210, D15); one definition of each navigation quantity; observation without interference. Awaiting B1-Q01. | None (allocation basis for every L1 record) |

Until DD-010 and DD-020 are in `registers/DECISIONS.md`, `trace_check.py` reports two DERIVED errors (L1-AER-680, -710).

## 6. Notes for the orchestrator

| ID | Note | Proposed action |
| --- | --- | --- |
| N-B1-01 | Expected check results after assembly: lint 0 errors, 48 COMPOUND warnings on L1 (judged in §8); trace 69 CHILDLESS (L1 records, no L2 yet) and 2 DERIVED (DD-010, -020 not yet in the register), and no CHILDLESS L0 record; param PARAM-MISSING for every referenced parameter (the database is empty until B2). | Accept at G1; DD-010 and DD-020 go in the register; B2 seeds the parameters. |
| N-B1-02 | `requirements/L1.md` was restored after the self-check (task instruction); the draft is `work/B1/L1_AER.md`. The L1.md header says "Skeleton (T0)"; update it at assembly. | Orchestrator. |
| N-B1-03 | P-AF-160 changes meaning, from the whole position-hold tolerance (CONOPS SC-090) to the AF guidance share of P-SYS-450. CONOPS SC-090 and SC-100 should cite P-SYS-450 for the scenario tolerance. The ConOps mode material is parked for L2 (#89), so the edit can wait for C5. | B2 seeds the new description; log on #89. |
| N-B1-04 | P-AF-070 (minimum horizontal speed for FPA) supports the A2-Q06 behaviour that the owner rejected (D13, #61, #89 item b). The Q5 proposal (§3 rule 6) gives C5 a different use for a minimum speed. | B2 does not seed it, or seeds it marked superseded. |
| N-B1-05 | METHODOLOGY §12 example "L1-AER-001 The Aeronef shall provide a Position Hold autoflight mode" conflicts with D33. The example is illustrative; L1 follows D33 and states no mode. | None (no change to METHODOLOGY). |
| N-B1-06 | METHODOLOGY §5 lists "failures" as an input of F-AER-08. Removed under the tailoring note (hazards deferred). | None. |
| N-B1-07 | A new ICD is proposed for the vehicle-model boundary (IN-B1-01): plan §3 lists only ICD-AER-TST, ICD-FC-AF and ICD-NAV-AF. | I1 decides: new `icd/ICD-VM-FS.md` or a section of ICD-AER-TST. |
| N-B1-08 | L0-CON-100 guidance asks for "an initial fuel quantity as a parameter". L1 reads it as the capacity P-FU-010 (a parameter) plus the initial fuel of each run (initial condition), so that tests can start at any fuel state (N-310). | Accept the reading at G1, or raise a CR if the owner wants a fixed initial quantity. |
| N-B1-09 | `tools/lint.py` `SUBSYSTEMS` and `param_check.py` `PARAM_ID_RE` would need an `FCP` code if B1-Q01 adds a flight control panel subsystem. | Only if the owner adds FCP. |
| N-B1-10 | The L1 performance records use the phrase "under autoflight" and "holding a fixed position" without mode names, to stay at aircraft level (D33). The per-mode accuracies (P-AF-080 to -150) are not L1 budgets; they are C5 and Phase 4 parameters. | None. |

## 7. Deferred questions that L1 touches (not asked again)

| Issue | Where L1 meets it | Handling in L1 |
| --- | --- | --- |
| #6 (Q5) mode combinations | L1-AER-450 | Proposal in §3; nothing written as an L1 requirement. |
| #59 modes after fuel exhaustion | L1-AER-200, -580 | L1 fixes only the effector behaviour (zero output) and the annunciation; mode state left to C2/C5. |
| #60 can a group have no active mode | L1-AER-660 | Initial mode state is a data item; validity left to C5. |
| #78 hold point and deceleration | L1-AER-460 | Reference position and the start of the hold left to C5; the budget applies from P-SYS-460. |
| #79 flight control panel | L1-AER-480 | Selections are data items; panel content left to C5 (or FCP, B1-Q01). |
| #80.3 FCP subsystem | Architecture | Asked as B1-Q01 (it was deferred "to B1/L2"). |
| #81 kinematic and gyroscopic terms | L1-AER-020 | Exception named, decision left to C1. |
| #54 course deviation sign | L1-AER-540 | Left to C6. |
| #55 display rounding | L1-AER-500 | Left to C5/C7 (CV-780). |
| #69 releasable or protected signals | L1-AER-630 | TBD with the RVS plan extension (D44, G0-F22). |
| #83 sensor models | L1-AER-440 | Perfect knowledge now; NAV isolates a later sensor model. |

## 8. Self-check (METHODOLOGY §13.1 and §13.2)

**§13.1, per record.**

- One "shall", subject the Aeronef (L1-AER-790: the Aeronef configuration), EARS pattern: lint reports 0 errors over 84 records.
- No numbers in statements; every quantity is a parameter reference listed under Parameters; SI units in the parameters (crew-facing units only through CV-740 in L1-AER-500).
- No vague terms, escape clauses, open lists or absolutes (lint clean). Two TIMING warnings were fixed (L1-AER-460, -680).
- COMPOUND warnings (48 on 46 records), judged one thought each (D30):
  - closed enumerations of one object (23): L1-AER-050, -070, -100, -230, -280, -490, -530, -540, -590, -610 to -660, -690, -720 to -760, -810, -840;
  - a pair that is one constraint (20): L1-AER-020 (force or moment), -080, -160, -170, -200, -220, -380, -390, -420, -430, -440, -450, -470, -480, -500, -510, -520, -550, -680, -830;
  - "with the other components at zero" qualifiers (3): L1-AER-120, -130, -140.
  None forms a tree of cases.
- Solution-free: no layout, algorithm, gain or law. The two design choices that L1 does make are recorded as DD-010 and DD-020 (derived records) and DD-030, DD-040 (choices inside parented records).
- Terms: glossary terms, or proposals in `glossary_proposals.md`. Axes per CONVENTIONS.
- Rationale, parent or Derived, source, sufficiency argument per parent: present on each record.
- Verification method and success criteria: roll-up (D40) on the 69 allocated records, direct methods on the 15 leaves (B1-Q02).
- Criticality Not assessed; TBD/TBR items carry an owner and a closure point (G1, G2 or the RVS extension).

**§13.2, the set.**

- Each L0 record allocated to AER is covered (FUNCTIONAL_ANALYSIS §8); the sufficiency argument is in the first child of each sibling group.
- Types considered: functional, performance, interface, constraint, model fidelity and documentation are all present; failure handling is deferred (tailoring).
- Each boundary of the architecture has an interface record and an ICD home (FUNCTIONAL_ANALYSIS §5.1, `interface_needs.md`).
- Derived records are flagged with their DD; they are reviewed at G1.
- No mode, mode group, combination or mode logic is written as an L1 requirement (D33); one control-law set, one configuration (D42).
- Manual sections affected: the operational manuals (L1-AER-840) are written after the requirements baseline.
