# C3 — Issues, owner questions, change requests and design decisions (EF)

Task C3 (plan §6, Phase 3): the EF section of L2 (`work/C3/L2_EF.md`) and the content of the MS-DYN effector model (`work/C3/ms_dyn_s7_effectors.md`, for MS-DYN §7.1). Written at branch c1_c2, commit 63499b8 (D1–D72). Questions are at L2 level: the effector subsystem. Local IDs C3-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 EF records | 22: Constraint 6, Performance 5, Interface 5, Functional 3, Model fidelity 2, Documentation 1 |
| Verification methods | Inspection 8, Test 7, Analysis 6, Demonstration 1 |
| L1 parents covered | 23 of 23 live L1 records allocated to EF (L1-AER-230 is Deleted, D54, and has none) |
| Derived records | 1: L2-AER-EF-210 (DD-C3-04, effector activation state, D69) |
| L3 records | None: each EF record is a leaf; the next layer is the implementation (D4) |
| MS-DYN | §7.1 effector model written (C3 slot); merge at I1 |
| Parameters | 6 new (P-EF-020, -030, -100, -110, -120, -130); 4 existing given values (P-EF-010, P-SYS-400, -410, -420) |
| Owner questions | 8 (§2) |
| Change requests | 3 (§3): FA §7.1 budget line, an optional editorial L1-AER-120 rationale clarification, glossary refinements |
| Design decisions proposed | 6 (§4) |
| Lint | 0 errors, 18 COMPOUND warnings (judged in §6) |

**Proposed authority values (TBR):** [P-SYS-400] = 60 kN upward (FA §7.1 formula 39.6 kN, the combined climb-at-speed case 58.6 kN); [P-SYS-410] = 190 kN in the other five directions (186.2 kN FA §7.1, 187.6 kN combined); [P-SYS-420] = 2000 N·m per axis (reaches [P-SYS-270] in 0.50 s at 15 975 kg·m²). G2-F04's 39.6 kN and 186 kN are verified (`ms_dyn_s7_effectors.md` §7.1.6).

**Command response (TBR):** first-order lag, [P-EF-020] = 0.015 s; [P-EF-010] = 0.06 s to the band [P-EF-030] = 5 %; the model reaches the band in 0.04 s; [P-SYS-310] + [P-EF-010] = 0.08 s ≤ [P-SYS-480] = 0.1 s.

## 2. Questions for the project owner

Each question has a recommended answer. The records are written for the recommended answer; where another answer changes a record, the question says which.

### C3-Q01 — Command response model

**Question.** How does an effector output follow its command (MS-DYN §7.1.4, L1-AER-100 "command response", P-EF-010)?

| | Option R1 — first-order lag on the clipped command (recommended) | Option R2 — ideal: output = clipped command from the step it applies | Option R3 — pure delay of a whole number of steps |
| --- | --- | --- | --- |
| Parameters | Time constant [P-EF-020]; response time [P-EF-010] to the band [P-EF-030] | None ([P-EF-010] = 0) | Delay in steps |
| Control laws | A finite actuator response to design against, the minimal one used in practice (L0-OBJ-020) | No actuator dynamics; the latency budget is one control frame only | A delay with no smoothing |
| Limits | Output stays within the limits by construction, no overshoot | Same | Same |
| Off state | Needs the explicit off state (a lag never reaches exactly zero) | Zero command gives zero output | Zero after the delay |

**Recommended answer: R1**, with [P-EF-020] = 0.015 s, [P-EF-010] = 0.06 s, [P-EF-030] = 0.05 (TBR). It gives the command-response kind of L1-AER-100 real content, closes the latency budget with 0.02 s to spare, and is verified exactly by an independent recursion (check E-1). Under R2 or R3, L2-AER-EF-100 and -340 keep their form with other values; P-EF-020 and -030 are withdrawn (R2).

**Affects.** L2-AER-EF-010, -100, -340; MS-DYN §7.1.4; P-EF-010, -020, -030; DD-C3-02; FC margins (IN-C3-22).

### C3-Q02 — Upward authority [P-SYS-400]: 60 kN or 40 kN

**Question.** FA §7.1 sizes [P-SYS-400] with the drag of the vertical speed [P-SYS-240] alone: 39.6 kN (G2-F04). Under the isotropic drag of D64, the vertical drag of a climb depends on the whole airspeed (G2-F06): climbing at [P-SYS-240] at the largest horizontal airspeed (231.5 m/s) gives 21.8 kN of vertical drag, not 2.85 kN, and the need becomes 58.6 kN with the full manoeuvre share (still air: 51.5 kN; a steady climb into the wind with the AF and FC accelerations only: 45.3 kN). L1-AER-320's children must show the climb "at maximum horizontal speed". Which value?

**Recommended answer: 60 kN (TBR)** and the FA §7.1 line corrected (CR-C3-01). Oversizing costs no fuel, because consumption is charged on the resultant actually produced (DD-110); 40 kN would make the fastest climb at maximum speed unflyable into wind. It stays smaller than the other five directions, as D72 allows. No change to L1-AER-120: its rationale says "at least" (an editorial clarification is offered as CR-C3-02).

**Affects.** P-SYS-400; L2-AER-EF-300, -330; FA §7.1; TT-020.

### C3-Q03 — Simultaneous authority (the authority box)

**Question.** L1-AER-120 to -140 ask for the six pure forces and moments one at a time. The performance records (L1-AER-310, -320, -330, -350, -460) need them together: at maximum speed into the wind the vehicle carries its weight, overcomes 186 kN of drag in any body direction and turns. Should EF guarantee the whole box (each force component within its authority, each moment within [P-SYS-420], all at once; L2-AER-EF-330, DD-C3-03)?

**Recommended answer: yes, the box.** It is the simplest set that covers every combined demand, it lets FC allocate and saturate each axis on its own (L1-AER-380), and its check is 64 linear-programming feasibility problems. A disc-shaped horizontal demand (less than the box's corners) would be enough physically but is harder to check and to allocate. The reference layout meets the box with 4.5 % margin. If rejected, L2-AER-EF-330 is replaced by one record per performance parent with its own combined demand.

**Affects.** L2-AER-EF-330; DD-C3-03; FC allocation (IN-C3-23).

### C3-Q04 — Force effectors only

**Question.** CV-330 allows "a moment-producing effector" with a moment axis. Should EF allow pure-moment emitters, or model each effector as a force emitter at a fixed point, its moment coming from the moment arm (DD-C3-01)?

**Recommended answer: force emitters only.** L0-CON-060 and -300 speak of force effectors with a maximum force, which L1-AER-110 limits; a pure-moment emitter would have no force to limit and would need a sixth parameter kind. The glossary *Control effectiveness* already says it "carries the point of application and moment arm". A couple is made by two force effectors. Refines the glossary *Effector* (CR-C3-03).

**Affects.** DD-C3-01; L2-AER-EF-010, -120; glossary *Effector*, *Effector output*.

### C3-Q05 — Reference layout

**Question.** Accept the reference layout of DD-C3-06 (six effectors in three pairs, each parallel to a body axis and offset across the centre of gravity, each pushing both ways at up to 100 kN) as the TBR values of [P-EF-100] to [P-EF-130]?

**Recommended answer: yes, as TBR.** It meets every authority record (pure forces 200 kN, pure moments 300 to 800 kN·m, the box with 4.5 % margin), each pair acts on one force axis and one moment axis only, which makes allocation simple, and each point lies inside the capsule. The layout is a design decision: the records do not depend on it, and a different layout is a change to four parameters, checked again by AN-EF-300 to -330. Alternatives: twelve one-way effectors in opposed pairs (the spacecraft reaction-control pattern; L_i = 0); a canted set of fewer effectors (harder to allocate). Both pass the same records if sized.

**Affects.** P-EF-100 to -130; DD-C3-06; closes TT-260 (L0-CON-300).

### C3-Q06 — Effectors off (D69)

**Question.** D69 needs the effectors off on the ground (before Takeoff, after Land) with no fuel use. Should the off state be part of the effector commands (an effector activation state set by the flight software, DD-C3-04), with each output zero while it is off and off before the first commands of a run?

**Recommended answer: yes.** It keeps the vehicle-model boundary to its listed kinds (L1-AER-430: effector commands in), gives exactly zero output and so exactly zero fuel flow under DD-110 with no new consumption term, and keeps the gear and the ground logic out of EF. A zero command alone would not do with a lag (it never reaches exactly zero). L2-AER-EF-210 is Derived until B3 provides the L1 parent; then it is re-parented and DD-C3-04 is registered (or withdrawn into the B3 change). Which function decides on/off (FC on an AF mode state) is C4/C5 (IN-C3-26, -30).

**D69-dependent items in EF:** L2-AER-EF-210 (parent); the "while the effector activation state is on" condition of L2-AER-EF-300 to -340 (L1-AER-120 to -140 say "while fuel remains": B3 may add "and the effectors are on", editorial); L2-AER-EF-200 zero-fuel run (a zero-fuel run now stays on the ground: the criterion still holds, trivially); MS-DYN §7.1.4 property 6 (step-zero outputs under the ground start); IN-C3-03, -11, -26, -30. EF does not model the gear (allocation pending in B3).

**Affects.** DD-C3-04; L2-AER-EF-210, -400; glossary *Effector activation state*; boundary ICD (IN-C3-34).

### C3-Q07 — Who computes the resultant

**Question.** The G2 inspection (§4, note to EF) asks I1 to fix who computes the resultant control force and moment, so that it is computed once. EF, or MS-DYN as a shared mapping that DYN and FU each apply?

**Recommended answer: EF computes it once and gives the same value to DYN (I-02) and, with the outputs, to FU (I-01)** (DD-C3-05). The control effectiveness is EF's parameter, and one computation guarantees the motion and the fuel come from the same force. L2-AER-DYN-180 already reads so; L2-AER-FU-070 needs an editorial addition (IN-C3-10).

**Affects.** DD-C3-05; L2-AER-EF-120, -130, -140; L2-AER-FU-070 (editorial).

### C3-Q08 — Downward authority sized as the horizontal

**Question.** L1-AER-130 puts the positive body z axis (down) with the four horizontal directions under [P-SYS-410] = 190 kN. The downward need is about 29 kN (the fastest descent at maximum airspeed plus the manoeuvre). Split [P-SYS-410] by a change request on the baselined L1-AER-130, or keep it?

**Recommended answer: keep it.** D72 accepted that the five non-weight-bearing directions are sized by the drag at maximum speed. Oversizing costs no fuel (DD-110) and nothing else in this model; a split would reopen a baselined record for no effect. No CR.

**Affects.** P-SYS-410 note only.

## 3. Change requests

| ID | Against | Requested change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-C3-01 | FUNCTIONAL_ANALYSIS §7.1 (P-SYS-400 line); P-SYS-400 description | "m_max · (g + [P-SYS-440]) + D([P-SYS-240])" → "m_max · (g + [P-SYS-440]) + the vertical drag of a climb at [P-SYS-240] at the largest horizontal airspeed [P-SYS-230] + [P-SYS-430] + [P-SYS-560], ½·ρ·[P-DYN-100]·V_a·[P-SYS-240] with V_a the airspeed magnitude (MS-DYN §5.5)". Optionally the same refinement on the P-SYS-410 line (horizontal drag in that climb). | Under isotropic drag (D64) the vertical drag shares the airspeed magnitude (G2-F06); the line as written understates the need by 19 kN (C3-Q02). | Proposed |
| CR-C3-02 | L1-AER-120 rationale (editorial, optional) | "plus the drag at the climb vertical speed [P-SYS-240]" → "plus the vertical drag in a climb at [P-SYS-240] at the largest horizontal airspeed". Recommended to batch with the B3 L1 change requests (which may also add "and the effectors are on" to L1-AER-120 to -140). | Same as CR-C3-01; the record already reads "at least", so this is a clarification, not a correction. | Proposed (optional) |
| CR-C3-03 | GLOSSARY *Effector*, *Effector command*, *Effector output*, *Control effectiveness*, *Command response*, *Output limits* (Fixed, D43) | As in `work/C3/glossary_proposals.md` §2. | Force emitters only (DD-C3-01); command and output in N; effectiveness per unit output; the lag and the band (DD-C3-02); limits by parameter. | Proposed |

No L1 record is unsatisfiable: no corrective CR is needed.

## 4. Design decisions proposed

Numbers DD-C3-nn are local; I1 assigns register numbers (the next free is DD-150).

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-C3-01 | Each effector is a force emitter: a force in N along a fixed unit direction through a fixed point of application in the body frame. Its control effectiveness is (d_i, r_i × d_i) per newton of output. No pure-moment emitter. | Pure-moment emitters with a moment axis (CV-330 allows them); a free 6-component effectiveness per effector. | L0-CON-060 and -300 speak of force effectors with a maximum force; every effector then has a force to limit (L1-AER-110); the effectiveness carries the moment arm as the glossary says; two kinds of parameter (direction, point) fix it. | — (choice inside L2-AER-EF-010, -120) |
| DD-C3-02 | Command response: the command is clipped to the output limits, then followed by a first-order lag of time constant [P-EF-020], stepped exactly once per simulation step, with the output of a step responding to that step's command; the lag starts from zero at the start of a run and after each off or not-available step. | Ideal response; pure delay; rate limit; second-order response. | Minimal actuator dynamics with an exact independent check; within the limits by construction; no overshoot; unit steady-state gain (L1-AER-360); first change at the frame start (DD-020). | — (choice inside L2-AER-EF-100, -340) |
| DD-C3-03 | The effector set guarantees the whole authority box together (forces within [P-SYS-410] along x_B, y_B and down, [P-SYS-400] up; moments within [P-SYS-420]), not only the six pure authorities. | Pure authorities only; a disc-shaped horizontal demand; one combined demand per performance record. | Covers every combined demand of the performance records; lets FC saturate each axis on its own (L1-AER-380); checked at 64 corners because the achievable set is convex. | — (choice inside L2-AER-EF-330) |
| DD-C3-04 | The effector commands carry an effector activation state, on or off, set by the flight software; while off, each output is zero; off before the first commands of a run. | A zero command as "off"; an off state inside the vehicle model driven by ground contact; a separate boundary item. | D69 (effectors off on the ground, no fuel use); exact zero with the lag; keeps the boundary to its listed kinds (L1-AER-430) and the ground logic out of EF. | L2-AER-EF-210 |
| DD-C3-05 | EF computes the control force and moment once per step and gives the same value to DYN (I-02) and FU (I-01). | A shared MS-DYN mapping applied separately by DYN and FU. | One computation guarantees that the motion and the fuel come from the same force (IN-C2-11, G2 §4 note). | — (choice inside L2-AER-EF-120, -130, -140) |
| DD-C3-06 | Reference layout: six bidirectional effectors of 100 kN in three pairs, along x_B at y = ±1.5 m, along y_B at z = ±1.5 m, along z_B at x = ±4 m (P-EF-100 to -130, TBR). | Twelve one-way effectors in opposed pairs; a canted set; a larger set with redundancy (failures deferred). | Meets each authority record and the box; each pair acts on one force axis and one moment axis; inside the capsule. A design value, replaceable by parameter change. | — (parameter values only) |

## 5. Other findings and notes for I1

1. **G2-F04 verified.** With m_max = 1500 kg, ρ = 1.225 kg/m³, [P-DYN-100] = 5 m²: [P-SYS-400] ≥ 39 620 N and [P-SYS-410] ≥ 186 190 N (airspeed 231.50 m/s, the ground speed [P-SYS-230] plus the largest wind, D72). The combined climb case of C3-Q02 adds 18.9 kN up and 1.4 kN horizontally.
2. **J_max for [P-SYS-420]** uses the uniform-capsule derivation of MS-DYN §6 with the fuel distributed as the dry mass (IN-C2-13 simplest choice): I_yy = I_zz = 15 975 kg·m², I_xx = 2850 kg·m² at full fuel. P-FU-070 and P-FU-080 are still TBD (TT-770); re-derive [P-SYS-420] when they are set or when the body dimensions change (TT-740, 2026-11-30).
3. **No drag or gravity moment** (DD-050): the moment budget is the onset term only; there is no disturbance moment in the model, so pitch and roll need authority only for transients and initial body rates.
4. **Fuel.** Oversizing the authority does not change the fuel budget (DD-110 charges the resultant). The fuel budget of L2-AER-FU-290 is unaffected by EF.
5. **Credibility checks C-1 to C-5** need no EF change: zero fuel (or effectors off) gives exactly zero control force and moment.
6. **TST.** Per-step recording (IN-C3-31) and an open-loop test command source (IN-C3-33) are needed for the EF analyses and tests.

## 6. Self-check (METHODOLOGY 13.1, 13.2)

**13.1, each record:**

- [x] One "shall", one subject (the effector subsystem), one thought. The 18 COMPOUND warnings are closed enumerations (the kinds that define an effector, the components of the box, the effector commands), one computation with its inputs, or one prohibition (-030); none is a tree of cases (D30).
- [x] Subject is the element at this level, never a person.
- [x] EARS pattern: ubiquitous (-010 to -040, -100 to -150, -400 to -430), state-driven (-200, -210, -300 to -330), event-driven (-050, -340). Conditions explicit: fuel availability and activation state on each authority and response record.
- [x] Every quantity is a parameter ID with an SI unit; no number in a statement (lint).
- [x] No vague terms, escape clauses, open lists or absolutes (lint).
- [x] Solution-free: the layout is DD-C3-06, outside the records; the lag is the physics of the fictional effector (MS-DYN), justified in DD-C3-02.
- [x] Terms in the glossary or proposed (`glossary_proposals.md`: *Effector subsystem*, *Effector activation state*, *Point of application*, *Direction of action*, *Clipped command*, *Authority box*); axes per CONVENTIONS (CV-310 to CV-330, CV-950).
- [x] Rationale, parent (or Derived with DD), source: on each record; a sufficiency argument for each parent.
- [x] Verification method, procedure ID and success criteria on each record.
- [x] Criticality "Not assessed"; each TBD/TBR item has an owner and a closure.

**13.2, the set:**

- [x] Each of the 23 live L1 parents is covered, with a sufficiency argument (coverage table at the head of the section).
- [x] No conflicts. Containment, stated: the box (-330) contains the pure authorities (-300 to -320); they are kept as the direct children of L1-AER-120 to -140 (L0-CON-020's pure-axis criterion) and so the box can be revised alone (C3-Q03). -040 (independence from other channels and motion) and -420 (dependence on the run's inputs only) are different properties for different parents.
- [x] Types considered: functional, performance, interface, constraint, model fidelity, documentation. Failure handling deferred (tailoring); saturation and fuel exhaustion are nominal.
- [n/a] Hazard rows and fault injection: deferred (tailoring).
- [x] Interfaces: each EF interface has an EF record and a counterpart (DYN-180, FU-070, FU-200, FC pending, TM pending); ICD items listed in `interface_needs.md` §8.
- [x] One Derived record (-210, DD-C3-04), for review at the parent level once B3 gives its L1 parent.
- [x] Trace checks: expected results below.
- [n/a] Manual sections: none yet.

## 7. Expected check results (scratch run in the C3 worktree, reverted)

Run with the draft assembled into `requirements/L2.md` and the §2 YAML of `param_proposals.md` merged into a copy of `parameters/PARAMETERS.yaml`, then both reverted:

| Check | Result | Meaning |
| --- | --- | --- |
| `lint.py --section EF` | 0 errors, 18 warnings (COMPOUND) | Judged in §6 |
| `trace_check.py` | 21 errors: 20 CHILDLESS, 1 DERIVED | CHILDLESS: L1 records allocated only to FC, AF, FCP, NAV, TM (none allocated to EF); 33 before EF. DERIVED: L2-AER-EF-210 cites DD-C3-04, not yet in the register; clears when I1 registers it (as DD-150 or the next free number) |
| `param_check.py` | 0 errors; 6 PARAM-TBD warnings for P-EF-020, -030, -100 to -130 | Clears when I1 opens the proposed TT row; the other warnings (PARAM-UNUSED on AF, NAV, TM, P-DYN-040, P-SYS-290) are pre-existing |
