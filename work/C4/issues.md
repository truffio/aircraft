# C4 — Issues, owner questions, change requests and design decisions (FC)

Task C4 (plan §6, Phase 3): the FC section of L2 (`work/C4/L2_FC.md`) and the L3 sections for translational regulation (TR), rotational regulation (RO) and control allocation (AL) (`work/C4/L3_FC.md`). Written at branch c1_c2, commit 0b19af0 (D1–D75). Questions are at L2 level: the flight control subsystem. Local IDs C4-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused). Gains and algorithms are design decisions, not requirements (D4): they appear only as DD proposals (§4).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 FC records | 24: Performance 8, Functional 7, Constraint 5, Interface 4 |
| L3 records | 22: Performance 13, Functional 5, Constraint 4 (TR 11, RO 8, AL 3) |
| Verification methods (L2 + L3) | Test 27, Inspection 15, Demonstration 2, Analysis 2 (the 8 L2 records allocated to TR, RO and AL are roll-ups, Inspection by D40) |
| L1 parents covered | 27 of 27 live L1 records allocated to FC in FUNCTIONAL_ANALYSIS §6.2, plus L1-AER-360 (CR-C4-01) |
| Derived records | 1: L3-AER-FC-AL-020 (the allocation priority rule, DD-C4-03) |
| Parameters | 10 new (P-FC-030 to P-FC-120); 2 given values (P-SYS-540, P-SYS-550); P-FC-010, P-FC-020 used as they stand |
| Owner questions | 7 (§2) |
| Change requests | 5 (§3) |
| Design decisions proposed | 7 (§4) |
| Lint | 0 errors on both files; 29 COMPOUND warnings (judged in §6) |

**Decisions in one paragraph.** Each of the six axes has one axis reference (value, rate, acceleration; for the translational axes also which of position or velocity is regulated), in the vehicle-carried local frame V, absolute, plus an off value for the ground (DD-C4-01). The regulation is six separate loops that meet only in the change of frame to the body axes (DD-C4-02). Saturation is nominal: each of the six demand components is limited on its own to the authority box and the others are untouched (DD-C4-03, the derived requirement); the crew limit is applied to the vehicle acceleration demand with the direction kept, so the force scales with the mass (DD-C4-04). A takeoff powers the effectors up and a landing switches them off, both through the off value (DD-C4-06), and the upward force is capped below the weight during the descent to touchdown so that a touchdown is not followed by a second liftoff (DD-C4-05).

## 2. Questions for the project owner

Each question has a recommended answer. The records are written for the recommended answer; where another answer changes a record, the question says which.

### C4-Q01 — What does each axis reference contain? (DD-C4-01, L1-AER-370)

**Question.** L1-AER-370 leaves to C4 which quantity each of the six references is. Which?

| | Option A — value, rate and acceleration per axis, with the regulated quantity of each translational axis (recommended) | Option B — velocity (rate) references only; autoflight closes every position loop | Option C — position (value) references only |
| --- | --- | --- | --- |
| Position hold | FC regulates position; the position share P-FC-010 of L1-AER-460 is FC's, as the budget says | AF closes the position loop on FC's velocity loop; P-FC-010 has no owner and the budget of FA §7.4 changes | FC regulates position |
| Speed and vertical-speed modes | FC regulates velocity with the acceleration as feed-forward | Same | A position reference has to run ahead of the vehicle; in saturation it runs away |
| Control-law comparison | Each law owns its position and velocity loops; AF is unchanged | AF is tuned to the velocity lag of each law: a law change touches AF | Each law owns all loops |
| Interface | Three numbers per axis and a flag per translational axis | One number per axis | One number per axis |

**Recommended answer: A.** It is the only option under which the position budget split of FA §7.4 and the replacement of the control law without touching AF (L0-CON-200, D15) both stay true. The flag is not mode information: it says which quantity to regulate, not why. Under B, L2-AER-FC-100 loses its position cases (TR-040, TR-050), P-FC-010 and P-FC-030 are withdrawn and FA §7.4 is redistributed; under C, the velocity cases are withdrawn.
**Affects.** L2-AER-FC-020, -100; L3-AER-FC-TR-020 to -050; ICD-FC-AF (IN-C4-40); glossary *Axis reference*.

### C4-Q02 — In which frame are the translational references? (DD-C4-01, CR-C4-03)

**Question.** The vehicle-carried local frame V (north, east, vertical) or the body axes?

**Recommended answer: frame V.** With the references in V a heading change at constant velocity is not a manoeuvre of the translational axes: the force resolution through the attitude follows it (DD-C4-02), and the ω × v term of the dynamics (D64) needs no explicit compensation in the translational loops. Position holds are in V by nature (north and east do not turn with the heading). Autoflight in Heading mode then gives a velocity vector along the selected heading without knowing the present heading. The cost is that L1-AER-380 speaks of "each other body axis" (D18 states the absence of coupling in the body frame): at zero heading the two are the same, at another heading the body components of a steady reference turn with the heading. CR-C4-03 aligns the L1 wording; the cross-axis tolerances are then stated along the axes of the references, and for the rotational axes about the body axes, as before.
**Under the body-frame option:** the references would be body-axis velocities, AF would rotate every horizontal reference into the body frame each frame, and a position hold would need a body-frame position error that rotates with the heading; L2-AER-FC-020, -120 and TR-010 change and CR-C4-03 is not needed.

### C4-Q03 — How is the crew limit applied? (DD-C4-04, L1-AER-290, D38)

**Question.** D38 says "as fuel is used up and the mass falls, the resultant effector force is reduced to keep within the limit" and FA §7.1 says "the crew limit caps the usable resultant control force at the current mass times P-SYS-120, minus drag". Read literally as a cap on the resultant force, 3 g times the maximum mass is 44 kN, while holding the maximum horizontal speed needs about 187 kN against the drag (L1-AER-130, L1-AER-310), and the sensed acceleration there is about 1 g. What is the intended limit?

**Recommended answer: the limit is on the vehicle acceleration that FC demands (at most P-SYS-440, direction kept), and the force follows from it with the current mass.** The sensed acceleration is the vehicle acceleration minus gravity (FA §7.2), so [P-DYN-010] + [P-SYS-440] ≤ [P-SYS-120] is the budget, the drag is outside the limit, and D38's intent holds: the resultant force that gives the limited acceleration falls with the mass. CR-C4-05 rewords the FA §7.1 paragraph. The alternative (a cap on the control force alone) makes L1-AER-130 and L1-AER-310 unsatisfiable together with L1-AER-290.
**Affects.** L2-AER-FC-130; L3-AER-FC-TR-070, -090.

### C4-Q04 — Which demand is given up first in saturation? (DD-C4-03, L3-AER-FC-AL-020)

**Question.** When the six axis demands cannot all be produced, what is the priority rule?

| | Option 1 — each component limited on its own to the authority box (recommended) | Option 2 — the whole demand scaled by one factor | Option 3 — moments first (attitude over translation) | Option 4 — weight first (vertical force over the rest) |
| --- | --- | --- | --- | --- |
| Other axes when one saturates | Untouched | All degrade together | Translation gives way | Moments and horizontal force give way |
| Fits the guaranteed box (DD-170) | Yes: always producible | Yes | Needs a rule beyond the box | Needs a rule beyond the box |
| Cross-axis behaviour in saturation (L1-AER-380) | Kept | Broken | Kept for moments | Kept for the vertical force |
| Depends on layout or mass | No | No | Yes | Yes |

**Recommended answer: Option 1.** The authority box is guaranteed together, so a demand limited component by component is always producible and a saturated axis disturbs no other. Options 3 and 4 need a ranking of the axes that the project has no basis for yet; option 2 degrades the held altitude when the horizontal demand saturates. The rule is one derived requirement (AL-020); another answer changes only that record and its test.

### C4-Q05 — The gear state to FC and the descent cap (DD-C4-05, CR-C4-02, L1-AER-930 rationale)

**Question.** L1-AER-930's rationale says FC keeps the vehicle from lifting off again after a touchdown. The liftoff rule is the first step at which the upward control force exceeds the weight, and the commands of the contact frame were computed before the contact. How is a second liftoff prevented?

| | Option a — cap the upward force while the gear is extended and the vertical reference rate is below zero (recommended) | Option b — cap it when the gear state says on the ground | Option c — leave it to AF | Option d — change the ground contact model |
| --- | --- | --- | --- | --- |
| Works in the contact frame | Yes | No: the gear state reaches FC at the next frame start | No: AF does not command the effectors | Yes |
| Needs | The gear state (extended) at FC; AF's Land references (IN-C4-43) | The gear state at FC | Nothing | A change to D69 and L1-AER-920 |
| Side effects | None in flight: the gear is retracted | None | Two landing events possible | A liftoff condition different from the one baselined |

**Recommended answer: option a.** It is the only option that acts before the contact is known, and it costs one added destination of an existing interface item (I-45, CR-C4-02) and a rule in the Land references that AF has anyway. Under option b, L2-AER-FC-210 is withdrawn for a weaker record and the first frame after a contact can still carry more than the weight (a second landing event is then possible and L1-AER-970's test is at risk).

### C4-Q06 — The FC share of the fuel margin (CR-C4-01, L2-AER-FC-240)

**Question.** C2 (IN-C2-23) and C3 (IN-C3-24) both put the commanded hold resultant, within the margin [P-FU-100], on FC, but L1-AER-360 is allocated to FU and EF only. Add FC?

**Recommended answer: yes, CR-C4-01.** Nobody else can show the margin: EF adds nothing (unit gain, no overshoot) and FU only sizes the capacity for it. The FC child is an analysis of the same takeoff-and-hold run that AN-FU-290 uses. Without the CR the record L2-AER-FC-240 has no L1 parent in the allocation and would be removed; the margin would then have no owner.

### C4-Q07 — The values of the tolerances and the recovery requirement

**Question.** Accept as TBR the values of `param_proposals.md` (P-FC-030 to P-FC-120, P-SYS-540, P-SYS-550) and keep the recovery requirement L2-AER-FC-180 (an axis whose demand was limited settles without crossing its reference by more than its tolerance)?

**Recommended answer: accept the values as TBR and confirm them at G2 from a prototype run of the baseline law (DD-C4-07); keep L2-AER-FC-180.** The values follow from the authority, the inertia and the loop latency of the C3 reference layout (§5). L2-AER-FC-180 is the observable form of "saturation is nominal": it forces the law to know its limits. A plain proportional-derivative position loop does not meet it for large position steps (the velocity at the end of the limited phase is too high); a position loop with a velocity limit does. If the law designer shows a cost, the fallback is a bounded overshoot parameter in place of "at most its tolerance", which changes L2-AER-FC-180, TR-110 and RO-080 only.

## 3. Change requests

| ID | Against | Requested change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-C4-01 | L1-AER-360 (Allocated to: FU, EF); FUNCTIONAL_ANALYSIS §6.2 | Allocated to: FU, EF, **FC**; tick the FC column of the L1-AER-360 row; in the rationale add to "Children must show": "(Analysis) the control force and moment that flight control commands in the hold stay inside the margin [P-FU-100]". | The hold commands spend the margin (IN-C2-23, IN-C3-24); L2-AER-FC-240 is the child (C4-Q06). | Proposed |
| CR-C4-02 | FUNCTIONAL_ANALYSIS §3.2 I-45 | "F-12, F-15 → F-08, F-11" → "F-12, F-15 → F-05, F-06, F-08, F-11"; add FC to the users of the gear state in the N² matrix of §3.1. No L1 text changes (L1-AER-430 lists the gear state; L2-AER-DYN-340 allows it). | The descent cap (L2-AER-FC-210, C4-Q05). | Proposed |
| CR-C4-03 | L1-AER-380 statement and rationale; L1-AER-370 rationale (optional, editorial); P-SYS-540 description | L1-AER-380: "each other body axis" (velocity) → "each other translational axis of the axis references"; "each other body axis" (body rate) → "each other rotational axis"; the rationale says the translational axes are those of the references, the axes of frame V, which are the body axes at zero heading. L1-AER-370 rationale: "Which quantity is regulated per axis … is a C4 decision" → "(DD-C4-01)". P-SYS-540 description: "along each translational axis of the axis references". | The references are in frame V (C4-Q02). | Proposed (needs C4-Q02) |
| CR-C4-04 | GLOSSARY *Axis reference*, *Axis demand*, *Reference position*, *Control law*, *Gear state* (Fixed, D43) | As in `work/C4/glossary_proposals.md` §2. | The content and the frame of the axis reference (DD-C4-01). | Proposed |
| CR-C4-05 | FUNCTIONAL_ANALYSIS §7.1, "Upper side of the budget" | "the crew limit caps the usable resultant control force at the current mass times [P-SYS-120], minus drag (L1-AER-290)" → "the crew limit is applied to the vehicle acceleration that flight control demands (at most [P-SYS-440]), so the resultant control force that gives it falls with the current mass (D38, DD-C4-04)". In §6.1 the FC row: "crew g-limit as a force limit at the current mass" → "crew limit applied to the acceleration demand". | C4-Q03. | Proposed |

No L1 record is unsatisfiable: no corrective CR is needed.

## 4. Design decisions proposed

Local IDs DD-C4-01 to -07; the orchestrator numbers them in the register (the next free is DD-210 at the time of writing). DD-C4-07 is a design proposal for the control-law designers, not a requirement and not a parameter (D4).

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-C4-01 | Each of the six axes has one axis reference: a reference value, a reference rate and a reference acceleration; each translational axis states whether the position or the velocity is regulated. The translational axes are north, east and vertical (altitude, vertical speed positive up) of frame V; the rotational axes are roll, pitch and heading, with the body rate as the rate. Absolute values only; an off value replaces the six references on the ground. | Velocity-only references; position-only references; body-frame references; a "hold present position" command resolved in FC (C4-Q01, Q02). | The position budget split of FA §7.4 stays with FC; no mode information crosses (L1-AER-420); the rate and acceleration make the tracking of a shaped reference lag-free; frame V keeps the axes uncoupled when the heading changes. | — (content of L2-AER-FC-020) |
| DD-C4-02 | Control structure: three translational loops in frame V, each from its own reference and state elements to an acceleration demand; the three acceleration demands become the force demands along the body axes by the attitude, the mass, the gravity and the disturbance compensation; three rotational loops from reference to angular acceleration demand, and the moment demands by the principal moments of inertia. The only place where the axes meet is the change of frame. | Body-frame loops with explicit ω × v compensation; one multivariable law with decoupling. | Independence (L0-CON-020, D18) in the structure, not only in the tolerances; the law comparison is axis by axis (L0-CON-200). | — (choice inside L3-AER-FC-TR-010, -090, RO-010, -060) |
| DD-C4-03 | The priority rule: each demand component is limited on its own to its range in the authority box; the other components are allocated unchanged. | Uniform scaling of the demand; moments first; weight first; the largest set the layout can produce (C4-Q04). | The box is guaranteed together (DD-170), so the limited demand is always producible; a saturated axis disturbs no other (L1-AER-380); independent of layout and mass. | L3-AER-FC-AL-020 |
| DD-C4-04 | The crew and vehicle-acceleration limit is applied to the vehicle acceleration demand (the vector of the three axis acceleration demands), scaled by one common factor above [P-SYS-440], so the direction is kept; the force follows with the mass of the frame. | A cap on the resultant force; per-axis limits; limiting the sensed acceleration directly (C4-Q03). | D38 and FA §7.2 (sensed = vehicle acceleration minus gravity); drag outside the limit; the force falls with the mass without a second rule. | — (choice inside L3-AER-FC-TR-070, -090) |
| DD-C4-05 | The descent cap: while the gear state shows the gear extended and the vertical reference rate is below zero, the upward control force that FC commands is at most the weight reduced by [P-FC-120]. | Cap on the on-ground flag; leave it to AF; change the ground contact model (C4-Q05). | The contact frame's commands precede the contact; the gear is retracted in flight, so the cap acts only in the descent to touchdown. | — (choice inside L2-AER-FC-210) |
| DD-C4-06 | FC derives the effector activation state from the off value alone: off while it is received, on while it is not. | A separate on/off item from AF; AF mode information in FC; ground logic in the vehicle model. | No mode information crosses (L1-AER-420, G1-F04); one interface; the exact zero of EF-210 is reached. | — (choice inside L2-AER-FC-190, -200) |
| DD-C4-07 | **Baseline control-law design (proposal, not a requirement).** Translation: per axis a velocity loop (proportional-integral, about 4 rad/s) inside a position loop (about 1.5 rad/s, velocity-limited for large errors), with the reference rate and acceleration as feed-forward, the exact weight as feed-forward (the mass is known), and a disturbance estimate (a first-order observer of about 20 rad/s on the difference between the measured vehicle acceleration and the acceleration the commanded force would give) added to the force: it cancels drag and gusts within the loop latency. Rotation: per axis a proportional-derivative loop (heading about 1 rad/s, pitch and roll about 2 rad/s) on the attitude error from the quaternion (heading by the shorter angle) with the reference rate and acceleration as feed-forward. Anti-windup by back-calculation from the limited demand. Allocation: the effectiveness matrix of P-EF-100 and P-EF-110; for the reference layout (three opposed pairs, each pair giving one force and one moment) a closed form per pair; for another layout a minimum-norm solution with output limits (a linear program), after the limiting of DD-C4-03. | Gain-scheduled PID without a disturbance estimate; model-predictive allocation; dynamic inversion. | Meets the indicative tolerances (§5): without a disturbance estimate the drag step of a gust (10 m/s^2 uncompensated) exceeds the transient allowance; the exact weight and the known mass remove the largest term; the quaternion error avoids the Euler singularity; the closed form is exact and fast. The numbers are first estimates for a prototype to confirm (C4-Q07). | — |

## 5. Budget checks and other findings for I1

All numbers use the database of commit 0b19af0: drag area 5 m², sea-level density 1.225 kg/m³, dry mass 1000 kg, steady wind 51.444 m/s, gust 25.722 m/s over 2 s, ground speed limit 154.333 m/s.

1. **TT-860 (liftoff wind against P-FC-020).** The drag of [P-SYS-580] = 38.583 m/s is 4559 N, which is 4.56 m/s² at dry mass against the allowance [P-FC-020] = 4.903 m/s²: 93 % used, margin 7 %. It holds, with little room. It grows with the square of the wind and falls with the mass, so a larger [P-SYS-580] or a smaller dry mass would break it (TT-860 stays Open for I1; L3-AER-FC-TR-100 tests it).
2. **TT-650 (gust rise time against the transient allowance).** The drag changes at the rate ρ × [P-DYN-100] × V_a × dV_a/dt. In a hover in the steady wind, with the gust, the peak is 8.1 m/s³ at dry mass, so the allowance holds if the compensation takes at most 0.60 s. At the maximum speed into the wind the peak is 27.1 m/s³ (air-relative speed 219 m/s at the middle of the ramp), so the compensation may take at most 0.18 s; the control-loop latency [P-SYS-480] is 0.10 s (0.08 s with [P-EF-010] = 0.06 s), which leaves 0.08 s to 0.10 s for the dynamics of the compensation. The total drag step of the gust in a hover is 10.1 kN, which is 10.1 m/s^2 at dry mass if nothing compensated it, so the allowance holds only with an active compensation driven by the measured acceleration (DD-C4-07). The requirement is feasible and tight; [P-SYS-570] = 2 s is acceptable (a shorter rise time would not be).
3. **Horizontal speed at touchdown in gusts (L1-AER-970).** In the gust of the envelope the position error reaches [P-FC-010] = 0.5 m on a time scale of about 2 s, which is a velocity excursion of 0.2 m/s to 0.5 m/s without a disturbance estimate and about 0.2 m/s with it. [P-FC-040] is 0.3 m/s, TBR; [P-AF-170] has to lie between [P-FC-040] and [P-SYS-510] = 0.5 m/s. Recommended for I1: [P-AF-170] = 0.4 m/s.
4. **Heading-rate onset (IN-C3-25) confirmed.** [P-SYS-420] = 2000 N·m over I_zz = 15 975 kg·m² gives 0.125 rad/s², so [P-SYS-270] = 0.0628 rad/s is reached in 0.50 s at full torque. FC asks for no faster onset (settling [P-FC-090] = 4 s); the authority is sufficient and its sizing (P-SYS-420) can stay.
5. **Gear clearance.** At the hover height with the gear extended the clearance is [P-AF-210] − [P-DYN-040] = 0.124 m (IN-C1-44). The vertical tolerances have to be small against it: [P-FC-030] = 0.05 m, so [P-AF-110] = 0.1 m (recommended for C5) leaves 0.02 m of margin. A hover below the reference by more than 0.124 m with the gear extended is a touch (a landing, if within the envelope).
6. **Turn at speed.** The lateral acceleration of a turn at [P-SYS-230] and [P-SYS-270] is 9.70 m/s², against [P-AF-200] = 9.81 m/s²: it fits with 1 % of room, which is C5's to keep (IN-C1-32). With the references in frame V it is the reference acceleration AF sends and FC feeds forward; FC adds no turn term of its own.
7. **Effector authority against the acceleration limit.** The demand limit is [P-SYS-440] times the maximum mass, 22 kN, far below the box (190 kN); FC never runs the effectors to their limits in nominal manoeuvres, only to cancel the drag (up to about 187 kN at the maximum speed into the largest wind). The authority box is reached by the drag compensation only in the extreme case; a stronger gust than the envelope would saturate the horizontal force first, which is the nominal saturation of L2-AER-FC-170.
8. **Fuel exhaustion (D68).** FC takes no fuel state and does nothing after exhaustion: the commands keep going and EF gives zero (L2-AER-EF-200). A regulator that integrates a falling vehicle is harmless, since the ground contact is a crash.
9. **Second layout fixture.** DM-FC-060, AN-FC-AL-010 and TP-FC-AL-020 need a parameter set with another layout that meets the box (IN-C4-36); it is a V1 fixture.
10. **ICD-FC-AF.** Its content is C4's proposal (IN-C4-40 to -44). C5 drafts in parallel and may choose differently; I1 reconciles. The points that must agree are the regulated-quantity flag, the absolute references and the off value.

## 6. Self-check (METHODOLOGY 13.1, 13.2)

**13.1, each record:**

- [x] One "shall", one subject (the flight control subsystem; the translational regulation, rotational regulation or control allocation at L3), one thought. The 29 COMPOUND warnings are closed enumerations (the six axes, the kinds of data at a boundary, the force and moment of a resultant, the north, east and vertical axes, the wind and the gust), one computation with its inputs, or two quantities of one tolerance; none is a tree of cases (D30).
- [x] Subject is the element at this level, never a person.
- [x] EARS pattern: ubiquitous (L2 -030, -040, -050, -070, -080, -160, -250, -260; L3 -TR-010, -TR-090, -RO-010, -RO-060, -AL-030), state-driven (L2 -010, -100, -110, -130, -150, -190, -210; L3 -TR-020 to -050, -TR-070, -RO-020 to -040, -AL-010), event-driven (L2 -060, -170, -180, -200, -220, -240; L3 -TR-060, -TR-100, -TR-110, -RO-050, -RO-070, -RO-080, -AL-020), complex (L2 -120, -140; L3 -TR-080). Conditions explicit: airborne, fuel remaining, wind within the envelope, activation state, gear state.
- [x] Every quantity is a parameter ID with an SI unit; no number in a statement (lint).
- [x] No vague terms, escape clauses, open lists or absolutes (lint).
- [x] Solution-free: gains, loop structure and the allocation algorithm are in DD-C4-02 and DD-C4-07, not in the records. The constraints that restrict the design (separate loops, the vehicle mass and inertia in the conversion, the shorter turn, the priority rule) carry their reason in the rationale (METHODOLOGY §8.5).
- [x] Terms in the glossary or proposed (`glossary_proposals.md`: *Axis (of regulation)*, *Reference value*, *Regulated quantity*, *Off value*, *Reference step*, *Tracking tolerance*, *Acceleration demand*, *Limited axis demand*, *Descent call*); axes per CONVENTIONS (CV-150, CV-280, CV-310, CV-320, CV-430, CV-490, CV-930, CV-950).
- [x] Rationale, parent (or Derived with DD), source: on each record; a sufficiency argument for each parent.
- [x] Verification method, procedure ID and success criteria on each record; the allocated L2 records are roll-ups (D40).
- [x] Criticality "Not assessed"; each TBD/TBR item has an owner and a closure.

**13.2, the set:**

- [x] Each of the 27 live L1 parents allocated to FC is covered, with a sufficiency argument (coverage table at the head of the L2 section); L1-AER-360 needs CR-C4-01.
- [x] Each L2 record allocated to TR, RO or AL has at least one L3 child (coverage table of the L3 section). The L3 records are leaves: the next layer is the control law (D4).
- [x] No conflicts. Overlaps, stated: L2-AER-FC-130 (a hard limit on the demand) and -140 (the allowance on the actual acceleration) are different properties of the same budget (L1-AER-300); L2-AER-FC-100 and -180 differ by the state (settled or recovering); L2-AER-FC-170 (limit at the box) and -130 (limit at the crew limit) act on different quantities, the force and the acceleration.
- [x] Types considered: functional, performance, interface, constraint; model fidelity and documentation: none arise in FC (the model is C1's to C3's; the control-law design documents are DD). Failure handling deferred (tailoring); saturation and fuel exhaustion are nominal.
- [n/a] Hazard rows and fault injection: deferred (tailoring).
- [x] Interfaces: each FC interface has an FC record and a counterpart (AF pending, DYN-320/-330/-340, FU-130/-140, EF-150/-400, TM pending); ICD items in `interface_needs.md` §9.
- [x] One Derived record (L3-AER-FC-AL-020, DD-C4-03), for review at the parent level.
- [x] Trace checks: expected results in §7.
- [n/a] Manual sections: none yet.

## 7. Expected check results (scratch run outside the repository)

Run on a scratch copy of the repository, with both drafts assembled into `requirements/L2.md` and `L3.md` and the §2 YAML of `param_proposals.md` merged into `parameters/PARAMETERS.yaml`:

| Check | Result | Meaning |
| --- | --- | --- |
| `lint.py --section FC` | 0 errors, 29 warnings (COMPOUND) | Judged in §6 |
| `trace_check.py` | 14 errors: 13 CHILDLESS, 1 DERIVED | CHILDLESS: L1 records allocated only to AF, FCP, NAV, TM (L1-AER-410, -470, -480, -490, -500, -530, -590, -600, -610, -620, -650, -870, -890), none to FC. DERIVED: L3-AER-FC-AL-020 cites DD-C4-03, not yet in the register; it clears when I1 registers it (as the next free number). Every L1 record allocated to FC has an FC child |
| `param_check.py` | 0 errors; 10 PARAM-TBD warnings for P-FC-030 to P-FC-120 | Clears when I1 opens the proposed TT row; the other warnings (PARAM-UNUSED on AF, NAV, TM and P-SYS-290) are pre-existing |
