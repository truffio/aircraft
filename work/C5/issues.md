# C5 — Issues, owner questions, change requests and design decisions (AF)

Task C5 (plan §6, Phase 3): the AF section of L2 (`work/C5/L2_AF.md`) and the mode logic draft (`work/C5/AF_MODE_LOGIC.md`, for `specs/AF_MODE_LOGIC.md`). Written at branch c1_c2, commit 0b19af0 (D1 to D75). Local IDs C5-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused). Questions are at L2: the autoflight subsystem. The records and the mode logic are written for the **recommended answer** of each; where another answer changes a record, the question says which.

## 1. Summary

| Item | Count |
| --- | --- |
| L2 AF records | 73: Functional 46, Performance 12, Interface 10, Constraint 5 |
| Verification methods | Test 64, Inspection 5, Analysis 3, Demonstration 1 |
| L1 parents covered | 25 of 25 live L1 records allocated to AF (L1-AER-340 is Deleted, D56) |
| Derived records | 2: L2-AER-AF-860, -870 (DD-C5-05, fuel exhaustion, D68) |
| Allocated below L2 | 16 mode and tolerance records name AF (Phase 4 mode sections), FC or EF; they are childless until Phase 4 and C4 |
| Mode logic | AF_MODE_LOGIC: 25 decision rows (DT), 5 transitions (TR), target, reference-position, heading, gear and initial-state rules |
| Parameters | None new; 10 existing values proposed (`param_proposals.md`) |
| Owner questions | 13 (§2) |
| Change requests | 3 (§4): L1-AER-530/-890, glossary refinements, CONOPS wording |
| Design decisions proposed | 7 (§5) |
| Conflicts | 5 (§3) |
| Lint | 0 errors; warnings: COMPOUND (the statements join one thought, D30) and TIMING (explicit parameter times, accepted) |

## 2. Questions for the project owner

### C5-Q01 — How the crew leaves Hover and Go to hover

**Question.** The panel has no Hover selection (D71). What does a selection of a horizontal or a vertical mode do while Hover or Go to hover is active, when each group must have a mode (A2-Q05)?

| | Option A (recommended): the other group takes its hold mode | Option B: refuse until both groups are chosen | Option C: the selected mode replaces Hover and the other group takes a fixed default |
| --- | --- | --- | --- |
| Result | HDG over Hover gives HDG with Altitude hold at the hover altitude; GO ALT gives Stationary with Go to altitude | The crew can never leave Hover in one step | Same as A for STAT and ALT, but a fixed altitude (hover) instead of the altitude reached |
| SC-110 legs 2 and 8 | Reproduced (HDG, then GO ALT; STAT, then V/S) | Impossible with one selection per step | Reproduced |
| Continuity | No step: the hold modes carry the reference position and the level-off altitude | n/a | Altitude step from a go to hover that is still descending |

**Recommended answer: A.** Rows DT-12 to DT-16, TG-5, TG-6, PR-1; L2-AER-AF-190. Under B, L2-AER-AF-190 becomes a refusal and SC-110 needs both groups selected in one frame.

### C5-Q02 — Takeoff and Land are committed

**Question.** May the crew select other modes during Takeoff or Land?

**Options.** A (recommended): Takeoff accepts only itself; Land accepts Land and Go to hover (the go-around of D70); everything else is refused. B: every group selection is accepted with the hold-mode continuation of C5-Q01. C: A, plus Go to hover during Takeoff.

**Recommended answer: A.** Both modes fly the vehicle below the operating volume with the gear extended or in transit, where the altitude tolerance [P-AF-110] has been sized for the hover height only. Under B a Stationary or Altitude hold could be left at a height of centimetres, with a contact outside any landing. C adds nothing, since Takeoff ends in Hover. L2-AER-AF-200, -210; rows DT-05 to DT-09.

### C5-Q03 — Selections on the ground, and Takeoff with no fuel

**Question.** On the ground, which selections are accepted, and is Takeoff accepted with the fuel exhausted?

**Options.** A (recommended): only Takeoff, and Takeoff only with fuel remaining; all else refused. B: the other modes are armed for after the takeoff. C: Takeoff is accepted with no fuel and never completes.

**Recommended answer: A.** A stale armed selection would act at a later time (B), and Takeoff with no fuel would be annunciated for a vehicle that cannot lift (C); SC-130 zero-fuel variation then shows FUEL EXHAUSTED only. A low-fuel state does not refuse it. L2-AER-AF-140, -150; DT-01 to DT-03. The ConOps TBR of SC-130 is closed.

### C5-Q04 — Autoflight after fuel exhaustion, and after Land

**Question.** D68 leaves to C5 what the annunciations show after exhaustion (TT-580). And after a landing, is any mode annunciated?

**Options.** A (recommended): at exhaustion autoflight disengages (no mode active, nothing armed, the off value) in the frame in which the fuel state shows it, and every selection is refused; after Land the same state is reached (no mode active); there is no crew disengage selection at any time. B: the modes stay engaged and annunciated (A2-Q04's proposal), or freeze at their last state. C: LAND stays annunciated on the ground.

**Recommended answer: A.** With the effectors stopped nothing flies the vehicle; B would annunciate a guidance that no longer acts and mislead the crew and the RVS. FUEL EXHAUSTED comes from FCP (C8). The off value keeps FC from saturating on an unreachable reference. L2-AER-AF-270, -860, -870; TR-01, TR-02. This also closes the "mode state after the landing" TBR of SC-130.

### C5-Q05 — The reference position of a hold

**Question.** Which position do Stationary, Go to hover, Takeoff, Land and Heading at zero speed hold (#78, SC-090 TBR), and from when does [P-SYS-460] count?

**Options.** A (recommended): the stopping position (where the vehicle stops under the horizontal acceleration limit), carried over unchanged between holding modes; the hold starts when a holding mode becomes active from a non-holding one or from the ground. B: the position at engagement, with the vehicle moving. C: the position where the vehicle actually stops, captured when the speed is within [P-AF-170].

**Recommended answer: A.** B demands an instantaneous stop and a return, and breaks [P-AF-200]. C leaves the reference undefined during the deceleration and makes the AF share [P-AF-160] unmeasurable. A makes the reference a known function of the engagement state (AN-AF-330). L2-AER-AF-330, -340, -510; PR-1 to PR-4.

### C5-Q06 — Altitude hold selected directly; Vertical speed with a target behind

**Question.** (a) Which altitude does Altitude hold hold when the crew selects ALT during a climb (SC-050 step 5 TBR)? (b) What does Vertical speed do when the selected altitude is behind the direction of motion, or the selected rate is zero (SC-040 TBR)?

**Options.** (a) A (recommended): the altitude where the vertical speed reference reaches zero under [P-AF-230] (the level-off altitude); B: the altitude at the instant of the selection (needs an instantaneous stop, then a return). (b) A (recommended): Vertical speed ends at once in Altitude hold, by the ordinary capture, with the level-off altitude as target; B: the selection is refused; C: Vertical speed flies on with no capture.

**Recommended answer: A for both.** The level-off altitude is "the altitude reached" of the ConOps wording and needs no return (DD-C5-03). The capture mechanism covers (b) without a second rule, and C would climb without limit. L2-AER-AF-350, -360; TG-4, CAPT.

### C5-Q07 — Heading with a selected horizontal speed of zero

**Question.** Does Heading at zero speed hold the position against the wind, as Stationary does (SC-120 TBR)?

**Options.** A (recommended): yes, it holds the reference position and turns in place. B: no, it regulates a zero velocity only.

**Recommended answer: A.** Regulating a zero velocity alone lets the position drift in a wind, so a turn in place moves the vehicle by an amount that depends on the control law. L2-AER-AF-540; HD-4. Under B the record is deleted and SC-120 and SC-110 leg 9 need a drift tolerance.

### C5-Q08 — Go to altitude: the standard and the selected vertical speed

**Question.** (a) When does Go to altitude use [P-AF-220] and when the selected vertical speed? (b) A selected vertical speed of the wrong sign, or zero?

**Options.** (a) A (recommended): Go to altitude starts at [P-AF-220] at each selection of GO ALT; a selected vertical speed accepted in that frame or later replaces it; B: Go to altitude uses the selector's held value, so the standard speed is only the initial one. (b) A (recommended): the magnitude is used, the direction is always toward the selected altitude, zero is ignored; B: a wrong sign is refused.

**Recommended answer: A for both.** B(a) would let a stale value from an earlier manoeuvre fly the next one (C8 holds whatever was last accepted, IN-C8-03). A is the reading of "until the crew selects another" (D56). L2-AER-AF-320; TG-2.

### C5-Q09 — The heading rate bound and the acceleration split

**Question.** D72 Q1 asks C5 to bound the commanded heading rate so that the horizontal speed times the heading rate stays within [P-AF-200]. How is the budget shared when a turn and a speed change go together, and with the vertical acceleration?

**Options.** A (recommended): the heading rate reference is at most [P-SYS-270] and at most [P-AF-200] over the horizontal speed reference; the horizontal acceleration of the velocity reference, turn and speed change together, is at most the square root of ([P-AF-200] squared minus [P-AF-230] squared), so the three-dimensional acceleration is within [P-AF-200]; the turn takes its share first (DD-C5-07). B: the bound on the heading rate only, with the speed change free to add (resultant up to 1.41 times [P-AF-200]). C: the bound with the speed held while turning.

**Recommended answer: A.** B breaks the budget [P-AF-200] + [P-FC-020] ≤ [P-SYS-440] when turning and accelerating together. C makes a curved acceleration impossible (SC-060 starts from rest while turning). L2-AER-AF-420, -440; §11 of AF_MODE_LOGIC.

### C5-Q10 — Valid initial mode states

**Question.** Which initial mode states does a run accept (#60, TT-610, TT-900)?

**Options.** A (recommended): on the ground, none; airborne (test runs and credibility checks only, D73), any horizontal and vertical mode pair, Go to hover or Hover, or no mode with the fuel exhausted; Takeoff, Land, any mode on the ground, and no mode airborne with fuel are initial-condition errors. B: any state, with AF repairing an invalid one. C: ground start only.

**Recommended answer: A.** The run is what the test asked for (D59, DD-140); repairing hides a test error, and C leaves the mode-transition tests unable to start at altitude. L2-AER-AF-900, -910; IC-1 to IC-7.

### C5-Q11 — Landing gear rules

**Question.** Who commands the gear, and when (L1-AER-910)? May Hover hold with the gear extended?

**Options.** A (recommended): only Takeoff retracts, at the hover height with the vehicle airborne; only Land extends, at its activation; the command is otherwise held, and it is extend on the ground; the first command is the initial gear position; Land descends only with the gear extended; Hover with the gear extended (after a go-around) is allowed and meets [P-AF-110] inside the gear clearance. B: Go to hover and Hover also retract the gear. C: the gear follows the height (retract above the hover height).

**Recommended answer: A.** B would retract the gear on a go-around that may have to land again at once; C makes the gear a function of the height with no mode meaning and would retract it in a Land. L2-AER-AF-700 to -740; GR-1 to GR-4.

### C5-Q12 — The axis references (with C4)

**Question.** Which quantity is each of the six references that cross ICD-FC-AF (IN-B1-03: "a joint C4/C5 decision")?

**Options.** A (recommended): reference value, its rate and a regulated indication, in the local frame, plus one off value (`interface_needs.md` §2). B: velocity references only, with the position loop inside AF (AF would close the loop on the measured position and the budget split [P-AF-160] / [P-FC-010] would lose its meaning). C: body-axis references.

**Recommended answer: A**, which keeps the budget split of L1-AER-460 and lets AF shape the reference without closing the loop (D15, D55). C is the same data rotated by the heading; if C4 prefers it, AF applies the rotation. L2-AER-AF-090 states only the composition, so a change of frame leaves it.

### C5-Q13 — Horizontal position and velocity from NAV

**Question.** Does NAV give AF the horizontal position (CR-C6-01) and the horizontal velocity components (CR-C5-01)?

**Options.** A (recommended): both, always valid, added to L1-AER-530 and -890. B: position only; AF takes the velocity from the horizontal speed and the track, and uses zero velocity where the track is invalid (below [P-NAV-010], 0.51 m/s). C: neither; AF integrates its own reference.

**Recommended answer: A.** B leaves the stopping position off by up to 13 mm and the initial velocity reference off by up to 0.51 m/s where the track is invalid, and the logic needs a special case for that range; C cannot start a hold from a moving state. L2-AER-AF-040, -330, -920.

## 3. Conflicts

| ID | Conflict | Resolution proposed |
| --- | --- | --- |
| C5-C01 | CONOPS §5 and the P-AF-190 description define "settled" as within [P-AF-190] of "the capture onset or target change", which cannot be one constant (a 180 deg heading change takes 50 s). | Redefine P-AF-190 as the time from the instant the reference reaches its target (`param_proposals.md`); change CONOPS §5 (CR-C5-03). |
| C5-C02 | L2-AER-FU-240 gives the fuel state to FCP only; FUNCTIONAL_ANALYSIS I-06 and §3.3 give it to AF as well. AF needs the exhaustion indication. | IN-C5-30: extend L2-AER-FU-240 (or add a record) at I1; no L1 change. |
| C5-C03 | Glossary *Armed (mode)* ("selected by the crew but not yet captured") against D16 and D56, where Altitude hold and Hover are armed by another mode and are not selectable (Hover) or selected to be active (Altitude hold). | CR-C5-02 refines the definition (`glossary_proposals.md`). |
| C5-C04 | L2-AER-AF-820 and -830 give the targets and the gear command to TM; L1-AER-620 and -630 ask for them only after CR-C7-01 and CR-C7-02. L1-AER-630 does not allocate to AF. | Those CRs are C7's; if they are refused, -820 loses "the target of each armed and active mode" and "the landing gear command" and the TST records them from the interface (IN-C7-40). |
| C5-C05 | L1-AER-530 and -890 list altitude, height above the ground, horizontal speed, vertical speed, heading and track; the AF logic needs the horizontal position (CR-C6-01) and velocity components. | CR-C5-01. |

## 4. Change requests

| ID | Target | Change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-C5-01 | L1-AER-530 (Statement, Rationale, children must show), L1-AER-890 (Statement, Rationale), FUNCTIONAL_ANALYSIS I-17, GLOSSARY *Navigation quantity* | Add the horizontal velocity components (north, east), always valid, beside the horizontal position of CR-C6-01. Allocation unchanged (NAV, AF). Versions 2 to 3. | The stopping position and the initial references of a hold need the velocity vector at any speed (C5-Q13, IN-C5-10). | Proposed |
| CR-C5-02 | GLOSSARY (Fixed, D43) | The refinements of `glossary_proposals.md` §2: *Active*, *Armed*, *Capture*, *Disengagement*, *Engaged*, *Engagement*, *Mode state*, *Axis reference*, *Reference position*, *Hover*, *Land*, *Takeoff*, *Go to hover*, *Mode group*. | The seed definitions marked TBR (C5) are refined; *Armed* conflicts with D16 and D56 (C5-C03). | Proposed |
| CR-C5-03 | CONOPS §4.4 and §5, TBR notes of SC-020 to SC-130 | §5: "settled" means within the tolerance a time [P-AF-190] after the reference reaches the target (C5-C01). §4.4: the armed Hover and Altitude hold are armed by the mode that precedes them; the label tables; the TBRs of SC-040, SC-050, SC-090, SC-100, SC-110, SC-120 and SC-130 are closed as §6 of this file says. | Consistency of the ConOps with the mode logic. | Proposed |

No change to L1 is needed for the mode logic itself: L1-AER-450 states the catalogue and leaves the logic to L2. B3 asked for AF children of L1-AER-360; L1-AER-360 v3 is allocated to FU and EF only (D74), so none is written (the constant references of Hover, L2-AER-AF-640, support its premise).

## 5. Design decisions proposed (DD-C5-nn; I1 numbers them in the register)

| ID | Decision | Alternatives considered | Rationale | Derived records |
| --- | --- | --- | --- | --- |
| DD-C5-01 | An axis reference is a value, its rate and a regulated indication; six in the local frame, plus one off value (`interface_needs.md` §2). | Velocity-only references; body-axis references; separate position and velocity channels. | Keeps the AF and FC shares of the position budget; AF shapes the reference and FC tracks it; the regulated indication separates a hold from a motion at a rate (C5-Q12). | L2-AER-AF-090 (traces to L1-AER-420) |
| DD-C5-02 | The mode logic is a set of tables with row IDs in `specs/AF_MODE_LOGIC.md`, binding on every implementation; a selection is decided accepted or refused by a table of state class and selection; a refusal changes nothing; the decision is recorded. | Mode logic in prose in the L2 records; refusals as errors. | METHODOLOGY §8.3 (mode logic as a decision table); D15 (any implementation with any law); tests row by row. | L2-AER-AF-010, -120, -130, -840 |
| DD-C5-03 | Capture and level-off: the armed Altitude hold becomes active when the altitude to go is within [P-AF-110], or at most the distance in which the vertical speed reference stops at [P-AF-230]; its target is the selected altitude, or the level-off altitude for a direct selection. | A capture window of fixed size; a proportional approach; a target at the altitude of the selection. | Exact stop on the target with the ramp of D70; no tuning constant; the same mechanism covers Vertical speed with a target behind. | L2-AER-AF-230, -350, -360 |
| DD-C5-04 | The reference position of a hold entered with the vehicle moving is the stopping position under the horizontal acceleration limit; it is carried over between holding modes; the hold starts where a holding mode follows a non-holding one. | Position at engagement; the position where the vehicle stops, captured late. | A defined reference during the deceleration; one reference per hold for the budget [P-SYS-450] (C5-Q05). | L2-AER-AF-330, -340, -510 |
| DD-C5-05 | At fuel exhaustion autoflight disengages (no mode, off value) and refuses every selection. | Keep the modes engaged and annunciated; freeze the last state. | D68 leaves it to C5; C2 suggested it; the truth to the crew and the RVS (C5-Q04). | L2-AER-AF-860, -870 (Derived) |
| DD-C5-06 | The landing gear command: retract only by Takeoff at the hover height with the vehicle airborne; extend by Land at its activation and throughout the on-ground state; held otherwise; first value the initial gear position. | Retract in Go to hover and Hover; command by height. | L1-AER-910 and its rationale; a go-around keeps the gear for a second landing (C5-Q11). | L2-AER-AF-700 to -740 |
| DD-C5-07 | The horizontal acceleration limit is the square root of ([P-AF-200] squared minus [P-AF-230] squared); a turn and a speed change share it, the turn first; the heading rate reference is at most [P-SYS-270] and [P-AF-200] over the horizontal speed reference. | Limit each axis separately; bound the heading rate only. | The 3D acceleration of the reference stays within [P-AF-200] (budget [P-AF-200] + [P-FC-020] ≤ [P-SYS-440]); D72 Q1 (C5-Q09). | L2-AER-AF-420, -430, -440 |

## 6. ConOps points left to C5 and how they are closed

| Scenario | Point | Closed as |
| --- | --- | --- |
| SC-020 | The capture label | None: the armed and active label of Altitude hold is ALT; the capture is the mode state change (AF_MODE_LOGIC §2). |
| SC-040 | What V/S does with no selected altitude, or one behind | The altitude selector always holds a value; one behind, or a zero rate, ends in Altitude hold at once (C5-Q06). |
| SC-050 | Which altitude ALT holds in step 5; the shorter direction of a heading change | The level-off altitude (C5-Q06); the smaller angle, clockwise on an exact half turn (HD-1). |
| SC-060 | Selected speed and heading in a wind, over the ground or through the air | Over the ground: a ground speed (D72), the vehicle moves along its heading over the ground (L2-AER-AF-530). |
| SC-090 | The reference position | The stopping position (C5-Q05). |
| SC-100, SC-110 | How the crew leaves Hover; go to hover from below | By a group selection, the other group taking its hold mode (C5-Q01); a go-around climbs to the hover height (DT-07). |
| SC-110 | Annunciations after exhaustion | The empty mode state; FUEL EXHAUSTED is FCP's (C5-Q04). |
| SC-120 | Heading at zero speed against the wind | Holds the reference position (C5-Q07). |
| SC-130 | The mode state after the landing; LAND annunciated on the ground; selections accepted on the ground; zero-fuel Takeoff; the gear labels; the gear after a go-around | Empty; no; only Takeoff, and not with no fuel (C5-Q03, Q04); the labels are FCP's; the gear stays extended (C5-Q11). |

## 7. Self-check against METHODOLOGY 13.1 and 13.2

| Item | Result |
| --- | --- |
| One "shall", one subject, one thought | Yes: 0 SHALL errors. The COMPOUND warnings are statements of one thought (a definition, a closed list or a two-case rule); L2-AER-AF-190 and -260 are the longest and stay one rule each (D30). |
| Subject is the element, not a person | Yes: the autoflight subsystem; the crew never. |
| EARS pattern, explicit conditions and timing | Yes; the TIMING warnings (after, once) are explicit frame orders and parameter times. |
| Numbers as parameters, SI | Yes: 0 NUMBER errors; crew units appear in no statement. |
| No vague terms, escape clauses, open lists, absolutes | Yes: 0 errors of these kinds; "each" is used for universal quantification. |
| Solution-free | The guidance laws, the gains and the capture shape are not in any record; the reference composition, the acceleration split and the stopping position are DD proposals with the reason in the rationale. |
| Glossary terms | Used as defined; new and refined terms in `glossary_proposals.md`. |
| Rationale, parent, source, verification | Present in every record; sufficiency per parent in the coverage table and in the records. |
| Parents fully covered | 25 of 25 (coverage table). Each mode of the catalogue has a mode record: Stationary (-500), Heading (-520 to -540), Altitude hold (-560), Go to altitude (-320), Vertical speed (-620), Go to hover (-630), Hover (-640), Takeoff (-660), Land (-670). |
| Interfaces on both sides | ICD-FC-AF, ICD-NAV-AF, ICD-FCP, the boundary ICD and ICD-AER-TST: AF side in -030 to -060, the others in the needs of `interface_needs.md`. |
| Derived requirements | L2-AER-AF-860, -870 only. |
| TBD/TBR | P-AF values TBR proposed; P-AF-140 TBD (M5). |

## 8. Notes for I1 and for Phase 4

1. **Plan edits.** §6 C5 row: "the catalogue of D56 and D69 (Takeoff, Land)"; M8 covers Takeoff and Land with Go to hover and Hover (B3 impact list).
2. **Childless until Phase 4.** The records with `Allocated to: AF` (the mode records) and FC or EF (the tolerances) show as CHILDLESS in the trace check until M0 to M8 and FC1 exist.
3. **Budgets to split.** [P-AF-090] to [P-AF-130] and [P-AF-170] are vehicle-level; M0 to M8 split each into the AF reference share and the FC tracking share, as [P-AF-160] and [P-FC-010] split [P-SYS-450].
4. **Items for C4 at I1.** The axis references (C5-Q12); the effector activation state from the off value; the upward force at the Land contact (IN-C1-43); the holds of [P-AF-110] and [P-AF-180] in gusts.
5. **Tests that need the TST.** The recording of ICD-FCP and ICD-FC-AF (IN-C5-70), a way to run the 25 decisions from each state class, and an airborne test start in each valid mode state.
