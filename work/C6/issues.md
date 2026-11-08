# C6 — Issues, owner questions, change requests and design decisions (NAV)

Task C6 (plan §6, Phase 3): the NAV section of L2 (`work/C6/L2_NAV.md`). Written at branch c1_c2, commit 55c6c29 (D1–D74), with the finished DYN, FU and EF sections of `requirements/L2.md` and MS-DYN as inputs. Questions are at L2 level: the navigation subsystem. Local IDs C6-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 NAV records | 26: Functional 13, Interface 6, Constraint 4, Performance 2, Documentation 1 |
| Verification methods | Test 13, Analysis 7, Inspection 6 |
| L1 parents covered | 9 of 9 live L1 records allocated to NAV (L1-AER-430, -440, -450, -530, -640, -680, -690, -880, -890); the Deleted L1-AER-340, -540, -550 (flight path angle and VOR, D56) have none |
| Derived records | None. The choices inside the records are DD-C6-01 to -04 (§4) |
| L3 records | None: each NAV record is a leaf; the next layer is the implementation (D4) |
| Parameters | 3 new (P-NAV-060, -070, -080, agreement tolerances); 2 existing given values (P-NAV-010 = 1 kt, P-NAV-030 = 80°), all TBR |
| Owner questions | 8 (§2) |
| Change requests | 3 (§3): horizontal position in the navigation quantities (L1-AER-530, -890, glossary, FA); validity in the operational data (L1-AER-640); glossary refinements |
| Design decisions proposed | 4 (§4) |
| Lint | 0 errors, 12 COMPOUND warnings (judged in §6) |

**What NAV computes.** At each control frame, from the frame-start state and nothing else: altitude (CV-430), height above the ground (CV-400, at the lowest point of the body, gear excluded), horizontal position (CV-410), horizontal speed (CV-480, a ground speed, D72 Q1), vertical speed (CV-490), heading (CV-530 by CV-260) and track (CV-540), each with its validity. Track valid at a horizontal speed of at least [P-NAV-010], value zero while invalid; heading valid at a pitch magnitude of at most [P-NAV-030]; the others valid at each frame. To autoflight (ICD-NAV-AF), the panel (ICD-FCP, without the position) and the operational data, the same values. No VOR and no flight path angle (D56).

## 2. Questions for the project owner

Each question has a recommended answer. The records are written for the recommended answer; where another answer changes a record, the question says which.

### C6-Q01 — Horizontal position as a navigation quantity

**Question.** L1-AER-530 and -890 list six navigation quantities and no position, while the glossary *Navigation* says NAV provides the position and the plan C6 row lists it. Stationary, Hover, Takeoff and Land hold a horizontal position over the ground (D56, D60, D69), and autoflight receives no vehicle state (L1-AER-440 gives it to NAV and FC only). Should NAV give autoflight the horizontal position?

| | Option P1 — NAV gives the horizontal position across ICD-NAV-AF (recommended) | Option P2 — autoflight reads the vehicle state directly | Option P3 — no position in AF: FC holds the position on a "hold here" reference |
| --- | --- | --- | --- |
| L1 change | CR-C6-01: add it to L1-AER-530, -890, the glossary and FA I-17 | L1-AER-440 adds AF; FA §5.1 "NAV derives every guidance quantity" changes | None to NAV; ICD-FC-AF carries a capture command; AF's share [P-AF-160] loses its meaning |
| Architecture | One derivation of every guidance quantity (FA §5.2 item 3) | Two derivations; a later sensor model (#83) has two inputs to replace | Guidance moves into FC, against D15 |

**Recommended answer: P1.** It keeps NAV the single source of guidance quantities and matches the glossary and the plan. L2-AER-NAV-030 and -230 trace to L1-AER-450 in the meantime, so no L1 change is needed for the draft to be consistent; after CR-C6-01, -230 can merge into -220. Under P2 or P3, -030 and -230 are deleted.

**Affects.** L2-AER-NAV-030, -150, -230; L1-AER-530, -890; glossary *Navigation quantities*; FA F-AER-09, I-17; IN-C6-11.

### C6-Q02 — Track validity threshold [P-NAV-010]

**Question.** Below which horizontal speed is the track invalid (CV-580)?

| | 1 kt = 0.514444 m/s (recommended) | 0.5 m/s ([P-SYS-510]) | 0.1 kt |
| --- | --- | --- | --- |
| Meaning | The selection and display resolution of the horizontal speed ([P-AF-030], [P-TM-040]): the smallest speed Heading can fly has a valid track | The landing envelope speed | Track shown at speeds the panel rounds to 0 kt |
| In a hold | Invalid (holds settle below [P-AF-170] ≤ [P-SYS-510]) | Invalid at the limit, valid just above it | Valid while the hold drifts in a gust: a direction that wanders over 360° |

**Recommended answer: 1 kt (0.514444 m/s, TBR)**, rounded down so that a selected 1 kt is valid. The state is exact, so the threshold is a usefulness bound, not an accuracy bound.

**Affects.** P-NAV-010; L2-AER-NAV-070, -100, -110, -140; TT-200.

### C6-Q03 — Heading validity pitch limit [P-NAV-030]

**Question.** Above which pitch magnitude is the heading invalid (CV-580)?

**Recommended answer: 80° (1.396263 rad, TBR).** At 80° a small roll perturbation moves the heading by about tan 80° ≈ 5.7 times its size, the most at which the nose direction is still a usable indication; toward 90° the sensitivity has no bound (CV-260). Alternatives: 89° (heading kept almost to the singularity, unstable indication), 60° (sensitivity 1.7, but the heading is lost early in a tumble). Pitch is held within [P-AF-180] of zero in every mode (D57), so the threshold acts only in airborne test starts and after fuel exhaustion.

**Affects.** P-NAV-030; L2-AER-NAV-060, -120, -130; TT-200.

### C6-Q04 — Value of an invalid track

**Question.** What value does the track item carry while the track is invalid?

| | Zero (recommended) | The last valid track | The CV-540 formula wherever it is computable |
| --- | --- | --- | --- |
| NAV memory | None: a function of the frame-start state (F-AER-14: "NAV has no state to initialise") | NAV holds a value across frames and needs an initial value (the heading?) | None |
| Determinism | Exact | Depends on the run's history | At exactly zero speed the floating-point arc tangent depends on the signs of the zero components |
| For the consumers | Clearly a placeholder; they read the flag | Plausible but stale | Noise at near-zero speed |

**Recommended answer: zero** (L2-AER-NAV-140, DD-C6-01). The heading needs no rule: CV-260 gives it a value at every attitude (DD-C6-04).

**Affects.** L2-AER-NAV-140; ICD-NAV-AF; IN-C6-10, -30, -40.

### C6-Q05 — Hysteresis on the validity thresholds

**Question.** Should the track and heading validity switch with a hysteresis band, so that a quantity near its threshold does not flicker between valid and invalid?

**Recommended answer: no hysteresis** (DD-C6-02). The state is exact and deterministic, so the validity is a function of the frame-start state; a band would add memory to NAV and a second parameter per threshold. A horizontal speed that stays near 1 kt is either a hold, in which the track is not used, or a Heading at the minimum speed, which is valid. The panel can smooth the presentation if C8 wants (IN-C6-30). If yes: two parameters (lower and upper thresholds) per quantity, and -100 to -130 become state-dependent records.

**Affects.** L2-AER-NAV-100 to -130.

### C6-Q06 — Where the NAV parameters sit in the run configuration

**Question.** The run configuration has three items: the vehicle parameter set, the flight-control-law design and the autoflight implementation (glossary *Configuration (run)*). NAV is flight software but neither a control law nor the autoflight. Where do [P-NAV-010] and [P-NAV-030] come from?

**Recommended answer: the vehicle parameter set**, which already carries [P-DYN-020] and [P-DYN-030] that NAV must share with DYN (L2-AER-NAV-330), and whose identifier and version L1-AER-650 already reports. The glossary *Vehicle parameter set* then names the navigation parameters too (CR-C6-03). Alternative: a fourth configuration item for the flight software parameters, which needs a change to L1-AER-650 and ICD-AER-TST for two values.

**Affects.** L2-AER-NAV-330; glossary *Vehicle parameter set*; ICD-AER-TST; IN-C6-62.

### C6-Q07 — Horizontal velocity components to autoflight

**Question.** Should NAV also give autoflight the north and east components of the horizontal velocity (always valid)? The horizontal speed and the track give them only while the track is valid; below [P-NAV-010] the direction of a residual motion is not available to autoflight, which Stationary and Go to hover may want to stop it.

**Recommended answer: not now; decide at I1 from C5's ICD-FC-AF choice** (IN-C6-12). If C5's horizontal references are velocities or positions, the horizontal position (C6-Q01) is enough to close a hold; if C5 asks for the components, they are added with the CR-C6-01 extension (one Functional and one Interface record, like -030 and -230). No record is written for them, to keep NAV to its L1 list.

**Affects.** Possibly two new records at I1 (proposed IDs L2-AER-NAV-080 and -280); CR-C6-01; IN-C6-12.

### C6-Q08 — Height of the gear above the ground

**Question.** The height above the ground is that of the body (CV-400, TT-820), not of the gear. Should NAV also give the height of the lowest extended gear contact point, for Land and for the clearance at the hover height?

**Recommended answer: no.** CV-400 and the closure of TT-820 (CR-B3-36, D73) put the reference at the body, and the hover height [P-AF-210] and the minimum operating height [P-SYS-210] are stated on it (D67, D70). At level attitude, which every mode holds, the gear clearance is the height above the ground minus [P-DYN-040] when the gear is extended (0.124 m at the hover height), which autoflight can use directly; touchdown is signalled by the gear state "on the ground" from the vehicle model (L1-AER-430), not by a NAV quantity. A gear height would need the gear extension fraction, which is internal to the model (MS-DYN §3.3), so it could not be computed from the vehicle state.

**Affects.** None if accepted; otherwise a CR to L1-AER-430 (the extension fraction across the boundary) and a new NAV record.

## 3. Change requests (to L1 and the specifications)

### CR-C6-01 — Horizontal position among the navigation quantities

- **Against.** L1-AER-530 v2 → v3, L1-AER-890 v2 → v3; GLOSSARY *Navigation quantities*; FUNCTIONAL_ANALYSIS §2 F-AER-09 (outputs), §3.2 I-17 (data).
- **L1-AER-530 statement**, new: "The Aeronef shall compute, at each control frame, its altitude, height above the ground, horizontal position, horizontal speed, vertical speed, heading and track from its vehicle state, as CONVENTIONS CV-400 to CV-550 define them." (CV-410 is already inside the cited range.) Rationale: add "The horizontal position is the guidance quantity of Stationary, Hover, Takeoff and Land (D56, D60, D69); autoflight receives no vehicle state (L1-AER-440)."
- **L1-AER-890 statement**, new: "The Aeronef shall pass its altitude, height above the ground, horizontal position, horizontal speed, vertical speed, heading and track, with their validity, from navigation to autoflight through the one interface defined in ICD-NAV-AF."
- **Glossary** *Navigation quantities*: add *horizontal position* (see `glossary_proposals.md` §2).
- **FA** F-AER-09: "Vehicle state → altitude, height above the ground, horizontal position, horizontal speed, vertical speed, heading, track, validity". I-17: "Navigation quantities (horizontal position included) and their validity".
- **Not changed.** L1-AER-880 (the panel gets no position: it is not an indication), L1-AER-640 (the position is in the recorded vehicle state).
- **Reason.** C6-Q01. Resolves the conflict between the glossary *Navigation* (position) and L1-AER-530 (no position).
- **Impact.** NAV: -230 merges into -220 (optional). AF (C5): reads the position from ICD-NAV-AF.

### CR-C6-02 — Validity of the navigation quantities in the operational data

- **Against.** L1-AER-640 v2 → v3.
- **Change.** Statement: "… its altitude, height above the ground, horizontal speed, vertical speed, heading and track, with their validity, …". Rationale: "The validity is recorded so that the data show what autoflight and the panel used (L1-AER-890)." The list stays closed.
- **Reason.** A test or the RVS cannot tell from the recorded track whether autoflight and the panel saw it as valid; with the zero value of an invalid track (DD-C6-01), the flag removes the ambiguity of a true northbound track. L1-AER-640 is a closed list, so the addition needs a CR.
- **Impact.** TM (C7) records two more booleans per sample (track and heading validity; the others are valid at each frame). L2-AER-NAV-250 already provides them.

### CR-C6-03 — Glossary refinements

- **Against.** GLOSSARY (Fixed, D43): *Navigation*, *Validity range*, and, if C6-Q06 is answered as recommended, *Vehicle parameter set*.
- **Change.** As `glossary_proposals.md` §2; new terms *Navigation subsystem*, *Frame-start state*, *Validity (of a navigation quantity)* need no CR.
- **Reason.** Name the horizontal position rather than "position" (the altitude is the vertical one), state the inclusive bounds of CV-580 in the definition, and place the NAV parameters in the configuration.

No change is needed to CONVENTIONS: CV-400 to CV-580 define every NAV quantity, and CV-580 leaves the behaviour with an invalid quantity to the NAV, AF and FCP requirements.

## 4. Design decisions proposed (for `registers/DECISIONS.md`)

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-C6-01 | While the track is invalid, its value is zero. | Hold the last valid track; output the CV-540 formula wherever computable. | No memory in NAV (FA F-AER-14), exact determinism (L1-AER-690, D59), a value clearly marked by its flag (C6-Q04). | — (choice inside L2-AER-NAV-140) |
| DD-C6-02 | The validity thresholds have no hysteresis: each validity is a function of the frame-start state alone, inclusive at the threshold. | A hysteresis band per threshold. | Exact deterministic state; no memory; one parameter per threshold; the near-threshold cases are holds in which the track is not used (C6-Q05). | — (choice inside L2-AER-NAV-100 to -130) |
| DD-C6-03 | NAV computes each quantity in closed form from its CONVENTIONS definition applied to the exact frame-start state: no estimator, filter, predictor or memory between frames. A sensor model (#83) would bring an estimator as a new design decision. | A complementary filter or Kalman estimator on the exact state; prediction to the middle of the frame. | Perfect state knowledge is a requirement (L1-AER-440); an estimator on exact data only adds error and state; estimation algorithms are design, not requirements (D4). | — (choice inside L2-AER-NAV-320) |
| DD-C6-04 | The heading value is the CV-260 yaw angle at every attitude, including while the heading is invalid; only the flag changes. | A substitute value (zero, the last valid heading) while invalid. | CV-260 defines the yaw angle in the singular case, so a value exists and stays a function of the state; consistent with the recorded Euler angles (L2-AER-DYN-070). | — (choice inside L2-AER-NAV-060, -130) |

## 5. Other findings and notes for I1

1. **Altitude reference of the hover height (TT-820, D69, D70, D73).** Closed by CV-400; NAV applies it. The altitude (CG) and the height above the ground (lowest point of the body) differ by [P-DYN-030]/2 at level attitude (2 m). On the ground at rest: altitude [P-DYN-030]/2 + [P-DYN-040] = 3.4 m (about 11 ft, what the panel indicates as altitude, IN-C6-30), height above the ground [P-DYN-040] = 1.4 m. At the hover height [P-AF-210] = 1.524 m the extended gear clears the ground by 0.124 m (MS-DYN §2.5), an AF tolerance matter (C5, [P-AF-110]).
2. **Horizontal speed is a ground speed (D72 Q1).** NAV's horizontal speed is the ground-referenced CV-480 speed that [P-SYS-230] and the panel selector refer to. There is no airspeed in the flight software (L2-AER-DYN-340).
3. **NAV has no budget share.** Its share of the position budget is zero (FA §7.4, L1-AER-440), and its latency share is zero inside the frame (it completes before AF, L2-AER-NAV-310).
4. **Records at the frame-start steps.** The NAV analyses need the recorded state at the frame-start steps (IN-C6-50): with the proposed [P-TM-010] = [P-SYS-310] the output samples must also fall on the frame-start steps (phase), which ICD-AER-TST fixes.
5. **Frame order.** DD-010 puts NAV after FCP and before AF; the NAV records rely on "before AF" only. If I1 changes the order, -310 changes.
6. **VOR withdrawn.** P-NAV-020, -040, -050 stay withdrawn; P-NAV-060 to -080 are new IDs.

## 6. Self-check (METHODOLOGY 13.1, 13.2)

**13.1, each record:**

- [x] One "shall", one subject (the navigation subsystem), one thought. The 12 COMPOUND warnings are closed enumerations (the quantities passed across an interface, -150, -220, -240, -250; the parameters taken, -330; the receivers, -260; the parts of an item's definition, -270, -400), one computation with its inputs (-020, -040, -070), or one restriction (-320); none is a tree of cases (D30).
- [x] Subject is the element at this level, never a person.
- [x] EARS pattern: ubiquitous (-010 to -060, -150, -200 to -330, -400), state-driven (-070, -100 to -140). Conditions explicit: the validity conditions are stated on the frame-start state.
- [x] Every quantity is a parameter ID with an SI unit; no number in a statement (lint).
- [x] No vague terms, escape clauses, open lists or absolutes (lint).
- [x] Solution-free: each quantity is its CONVENTIONS definition; the closed-form computation, the value of an invalid track and the absence of hysteresis are DD proposals (§4).
- [x] Terms in the glossary or proposed (`glossary_proposals.md`: *Navigation subsystem*, *Frame-start state*, *Validity*, *Tumbling test run*); axes and quantities per CONVENTIONS (CV-400 to CV-580, CV-950, CV-960).
- [x] Rationale, parent, source: on each record; a sufficiency argument for each parent (coverage table at the head of the section).
- [x] Verification method, procedure ID and success criteria on each record.
- [x] Criticality "Not assessed"; each TBD/TBR item has an owner and a closure.

**13.2, the set:**

- [x] Each of the 9 live L1 parents is covered, with a sufficiency argument.
- [x] No conflicts within NAV. One conflict upstream (glossary *Navigation* lists the position, L1-AER-530 does not): CR-C6-01.
- [x] Types considered: functional, performance, interface, constraint, documentation. Model fidelity: none (NAV is not part of the vehicle model). Failure handling deferred (tailoring); invalid quantities are nominal, defined behaviour.
- [n/a] Hazard rows and fault injection: deferred (tailoring).
- [x] Interfaces: each NAV interface has a NAV record and a counterpart (DYN-320, -330 for the state; AF, FCP, TM pending in C5, C8, C7); ICD items in `interface_needs.md` §2.
- [x] No Derived record.
- [x] Trace checks: expected results below.
- [n/a] Manual sections: none yet.

## 7. Expected check results (scratch run in the C6 worktree, reverted)

Run with the draft assembled into `requirements/L2.md` and the §2 YAML of `param_proposals.md` merged into a copy of `parameters/PARAMETERS.yaml`, then both reverted:

| Check | Result | Meaning |
| --- | --- | --- |
| `lint.py --file work/C6/L2_NAV.md` | 0 errors, 12 warnings (COMPOUND) | Judged in §6 |
| `lint.py --section NAV` (assembled) | 0 errors, 12 warnings | Same |
| `trace_check.py` | 18 errors, all CHILDLESS (22 before NAV) | NAV clears L1-AER-450, -530, -680, -890. The 18 left are L1 records allocated only to FC, AF, FCP or TM (C4, C5, C7, C8), and L1-AER-960, -970 (their EF children are for the C3 rework). None is a NAV parent |
| `param_check.py` | 0 errors; 3 PARAM-TBD warnings for P-NAV-060, -070, -080 | Clears when I1 opens the proposed TT row (IN-C6-60); the other 14 warnings are pre-existing |
| `vcrm.py --check` | 0 errors | Every NAV record has a method |
