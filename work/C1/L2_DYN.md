## DYN — Dynamics model

The dynamics model requirements (task C1). The subject of each statement is the dynamics model, the DYN subsystem of the vehicle model (glossary proposal). The physics is stated in [specs/MS-DYN.md](../specs/MS-DYN.md); these records point to its named sections, because a statement cannot carry a section number. DYN implements functions F-AER-03, F-AER-04, F-AER-12 and its part of F-AER-14 (FUNCTIONAL_ANALYSIS §6.1).

**Depth.** Each record below is a leaf: the next layer would be the implementation (integration method, code structure), so DYN has no L3 section (D4). Each record is verified directly by its own method (D40). Procedure IDs follow the record number (IN-, AN-, TP-, DM-DYN-nnn); Phase 5 (V1) writes the procedures.

**Open owner questions that the records are written around** (`work/C1/issues.md`): the rotation-during-translation term (#81.1, C1-Q01), the retained kinematic terms (#81, C1-Q02), the drag form (C1-Q03), the gust shape and rise time (C1-Q04) and the body shape (C1-Q05). Each affected record is correct under either answer, because it points to the MS-DYN section that records the answer, and carries the item in its TBD/TBR field.

**Coverage of the L1 parents.** Every L1 record allocated to DYN has at least one DYN child. L1-AER-230 is Deleted (D54) and has none.

| L1 parent | What DYN guarantees, in the parent's terms | DYN children |
| --- | --- | --- |
| L1-AER-010 | The motion is that of a six-degree-of-freedom rigid body by the MS-DYN equations, and it matches the free-fall, terminal-velocity and torque-free rotation solutions | -010, -020, -030, -040, -060, -440, -600, -610, -620, -630, -640 |
| L1-AER-020 | The DYN equations contain no cross-axis term other than the kinematic terms MS-DYN lists; drag couples no axis; the rotation uses principal moments only | -040, -050, -110, -190, -640 |
| L1-AER-030 | The model computes no aerodynamic force other than drag | -160 |
| L1-AER-040 | The dynamics define no control surface | -170 |
| L1-AER-050 | The total force is gravity plus drag plus the control force, and the total moment is the control moment | -100, -110, -180 |
| L1-AER-060 | Gravity is uniform, of magnitude [P-DYN-010], downward; free fall matches the closed form | -120, -600 |
| L1-AER-070 | Drag uses the air-relative velocity with the TST wind and the standard-atmosphere density; terminal speed matches, with and without wind | -130, -140, -150, -610 |
| L1-AER-180 | The motion uses the vehicle mass FU gives at each step, so a lower mass gives a larger acceleration | -030, -210, -630 |
| L1-AER-210 | The body origin is the centre of gravity at each fuel state | -200 |
| L1-AER-220 | The body shape is stated with its dimensions; the rotation uses FU's diagonal tensor | -040, -210, -220 |
| L1-AER-240 | The nose is on the positive body x axis | -230 |
| L1-AER-250 | The crew station is at [P-DYN-400] | -240 |
| L1-AER-260 | Contact within the envelope is detected, classified as a landing and output as one event at the contact step | -500, -510, -530, -550 |
| L1-AER-270 | Contact outside the envelope is detected, classified as a crash and output as one event at the contact step | -500, -520, -530, -550 |
| L1-AER-280 | Classification by the two speed limits at the contact step | -500, -510, -520 |
| L1-AER-290 | The sensed acceleration at the centre of gravity is computed exactly, gravity is the budgeted [P-DYN-010], and contact adds no shock | -120, -300, -550 |
| L1-AER-430 | DYN passes only the vehicle state across the vehicle-model boundary | -320, -340 |
| L1-AER-440 | NAV and FC receive the exact recorded state of the frame-start step | -330 |
| L1-AER-640 | DYN gives TM the vehicle state (with Euler angles and vehicle acceleration), the sensed acceleration and the ground-contact events | -070, -300, -310, -350, -530 |
| L1-AER-660 | Step zero is the TST's initial position, velocity, attitude and body rates | -430 |
| L1-AER-670 | One step of [P-SYS-300] per command, with the wind of that command held over the step | -140, -400, -410 |
| L1-AER-690 | Each step depends only on the run's state, inputs and parameters | -420 |
| L1-AER-720 | MS-DYN is baselined with a named section for each DYN model; FU and EF fill theirs | -700 |

One record is Derived: L2-AER-DYN-540 (DD-C1-03).

### L2-AER-DYN-010

```req
ID:            L2-AER-DYN-010
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall propagate the vehicle state as the motion of a rigid body
  with six degrees of freedom by the equations of motion of MS-DYN.
Rationale:     For a simulated vehicle the physics is the requirement (METHODOLOGY §7); MS-DYN holds
  the equations so that this record can point to them (INCOSE R23). The body is rigid, with no
  flexibility or fuel slosh (L0-ASM-080), and the local reference frame is inertial (CV-140). The
  equations are written so that the open question #81.1 does not change this record (MS-DYN §4.2,
  §4.5).
  Sufficiency (L1-AER-010): L1-AER-010 asks for six-degree-of-freedom rigid-body motion in
  accordance with MS-DYN, shown against free fall, free fall with drag and torque-free rotation.
  This record fixes the equations; -020 the state; -030 and -040 the translational and rotational
  laws with the mass properties of the step; -060 the attitude; -440 the parameters. L2-AER-DYN-600,
  -610 and -620 are the three checks L1-AER-010 names, and -630 and -640 add the variable mass and
  the rotation-during-translation term. Together they make the executable model conform to MS-DYN.
Parent(s):     L1-AER-010
Source:        N-270, N-290; MS-DYN §4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-010; success criteria: the implementation holds exactly the
  state elements of the MS-DYN vehicle state section, and it implements one term for each term of
  the MS-DYN equations of motion and no other term.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-020

```req
ID:            L2-AER-DYN-020
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall hold, at each simulation step, a vehicle state made of the
  position and the velocity of the centre of gravity in the local reference frame, the attitude
  quaternion and the body rates.
Rationale:     These are the thirteen integrated quantities of a rigid body (MS-DYN §3.1). The
  quaternion is the authoritative attitude (D22, CV-250); the Euler angles, the body-axis velocity
  and the accelerations are derived from the state (L2-AER-DYN-070, -300, -310). The list is
  closed (D30: one state).
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        MS-DYN §3; CV-250, CV-410, CV-460
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-020; success criteria: the state held at each step has exactly
  these elements, in the frames and SI units of the MS-DYN vehicle state section, and the attitude
  is the scalar-first unit quaternion of CV-250.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-030

```req
ID:            L2-AER-DYN-030
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the rate of change of the vehicle velocity from the
  total force and the vehicle mass of the current simulation step, by the translational equation
  of MS-DYN.
Rationale:     The mass loss is a real effect on the dynamics: the same force gives a larger
  acceleration as fuel burns (L0-ASM-090, L1-AER-180). The equation takes the instantaneous mass and
  has no thrust term from the fuel mass flow (MS-DYN §4.1). The statement says "rate of change of
  the vehicle velocity" and not "total force divided by mass" so that it holds under both options
  of #81.1 (MS-DYN §4.2).
  Sufficiency (L1-AER-180): FU computes the vehicle mass as the dry mass plus the remaining fuel
  mass (FU child). DYN's share is to make that mass act on the motion: this record uses it,
  L2-AER-DYN-210 takes it from FU at each step, and L2-AER-DYN-630 checks the result against the
  closed-form variable-mass solution. Together they make the mass decrease of L1-AER-180 change the
  dynamics.
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-180, L1-AER-010
Source:        L0-ASM-090; MS-DYN §4.1, §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-030; success criteria: the implemented translational equation
  is the one MS-DYN §4.2 gives for the #81.1 option recorded in the kinematic terms list, it uses
  the vehicle mass that FU provides for the step, and it has no term in the fuel mass flow.
Parameters:    —
TBD/TBR:       Rotation-during-translation term (#81.1, C1-Q01), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-040

```req
ID:            L2-AER-DYN-040
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the rate of change of the body rates from the total
  moment about the centre of gravity and the principal moments of inertia of the current
  simulation step, by the rotational equation of MS-DYN.
Rationale:     The body axes are principal axes, so the tensor is diagonal and a moment about one
  body axis gives no angular acceleration about another (D61). The equation uses the inertia of the
  current fuel state, with no inertia-rate term (L0-ASM-090, MS-DYN §4.1, §4.3).
  Sufficiency (L1-AER-220): FU derives the diagonal tensor at each fuel state from the mass
  distribution over the body shape (FU child). DYN states the shape and its dimensions
  (L2-AER-DYN-220), takes the three principal moments from FU at each step (L2-AER-DYN-210) and
  uses them, with no product of inertia, in the rotational equation (this record). So the tensor of
  L1-AER-220 is the one that drives the rotation.
  Sufficiency (L1-AER-020): see L2-AER-DYN-050. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-220, L1-AER-020, L1-AER-010
Source:        D61; MS-DYN §4.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-040; success criteria: the implemented rotational equation is
  the one of MS-DYN §4.3, it uses the three principal moments of inertia that FU provides for the
  step, and it contains no product of inertia.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-050

```req
ID:            L2-AER-DYN-050
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall include, as terms that relate motion along one degree of
  freedom to an acceleration along another degree of freedom in the body frame, only the
  rigid-body kinematic terms that the kinematic terms list of MS-DYN gives.
Rationale:     Owner definition D18 and the exception of L1-AER-020. MS-DYN §4.5 lists the
  gyroscopic term (K-1, retained as proposed), the rotation-during-translation term (K-2, open:
  #81.1) and the resolution of gravity, drag and control force through the attitude (K-3). The
  record holds under either answer to #81.1, because the list records the answer. With pitch and
  roll held at zero (D57) K-1 is zero in normal operation, and K-2 has no vertical component.
  Sufficiency (L1-AER-020): the coupling sources the model contains are the equations of motion,
  the drag, the effectors and the inertia. DYN covers the equations (this record), the drag
  (L2-AER-DYN-190: drag along one axis for flow along that axis; L2-AER-DYN-110: no aerodynamic
  moment) and uses only the principal moments (L2-AER-DYN-040); EF excludes effector coupling and FU
  gives zero products of inertia. L2-AER-DYN-640 checks the K-2 behaviour. With MS-DYN listing each
  retained term, the DYN part of what L1-AER-020 asks its children to show is met.
Parent(s):     L1-AER-020
Source:        D18, D57, D61; #81
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-050; success criteria: each implemented term that relates two
  degrees of freedom is a term of the MS-DYN kinematic terms list, and the list states the owner's
  decisions on #81 and #81.1.
Parameters:    —
TBD/TBR:       Rotation-during-translation term (#81.1, C1-Q01), Martin, G2; retained terms K-1 and
  K-3 to be confirmed (#81, C1-Q02), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-060

```req
ID:            L2-AER-DYN-060
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall keep the norm of the attitude quaternion within [P-DYN-230]
  of one at each simulation step.
Rationale:     The attitude is a unit quaternion (CV-250); a drifting norm distorts the direction
  cosine matrix and with it every body-axis quantity. How the norm is kept (normalisation, the
  integrator) is a design matter (D4); the tolerance is the requirement (MS-DYN §4.4, check C-6).
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        CV-250; MS-DYN §4.4, §11 (C-6)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-060; success criteria: in checks C-3 and C-5 of MS-DYN and in a
  run of the reference mission SC-110, the norm of the recorded quaternion differs from one by at
  most [P-DYN-230] at each step.
Parameters:    P-DYN-230
TBD/TBR:       P-DYN-230 value TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-070

```req
ID:            L2-AER-DYN-070
Level:         L2
Type:          Functional
Statement:     The dynamics model shall derive the heading, the pitch angle and the roll angle of
  each vehicle state from the attitude quaternion by CONVENTIONS CV-260.
Rationale:     The quaternion is authoritative and the Euler angles are derived from it (D22,
  CV-250). The vehicle state includes them (glossary *Vehicle state*). Deriving them once, in the
  model, gives NAV, TM and the TST one definition, including the singular case at a pitch angle of
  plus or minus a right angle (CV-260).
  Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-640
Source:        D22; CV-250, CV-260
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-070; success criteria: for attitudes spanning the heading range, the
  pitch-angle range including its two end points and the roll-angle range of CV-230, the reported
  Euler angles equal the CV-260 formulas applied to the recorded quaternion, to floating-point
  rounding, and lie in the CV-230 ranges.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-100

```req
ID:            L2-AER-DYN-100
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the total force on the vehicle as the sum of the
  gravity force, the drag force and the control force, with no other contribution.
Rationale:     L0-CON-090 limits the external effects to gravity, drag on the air-relative velocity
  and ground contact; ground contact is not a force (MS-DYN §5.1, §9). The control force is the only
  other force (L0-CON-060). Consumed fuel adds no force (L0-ASM-090). The list is closed.
  Sufficiency (L1-AER-050): L1-AER-050 closes the forces and moments to gravity, drag and the
  control forces and moments. This record closes the force; L2-AER-DYN-110 the moment;
  L2-AER-DYN-180 takes the control part from EF; L2-AER-DYN-120 and -130 fix gravity and drag. The
  free-fall and terminal-velocity checks that L1-AER-050 cites are L2-AER-DYN-600 and -610.
Parent(s):     L1-AER-050
Source:        L0-CON-090; MS-DYN §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-100; success criteria: the implemented total force has exactly
  three contributions, gravity, drag and the control force from EF, as the MS-DYN total force and
  moment section states.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-110

```req
ID:            L2-AER-DYN-110
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the total moment about the centre of gravity as the
  control moment, with no moment from gravity or from drag.
Rationale:     Gravity is uniform and acts at the centre of gravity, so it gives no moment. Drag
  acts at the centre of gravity and there is no rotational damping moment (DD-C1-01, proposed): a
  vehicle at fuel exhaustion keeps its angular momentum, as CONOPS SC-110 and the L1-AER-200 and
  -390 rationales describe. A drag moment depending on the translation would also be a cross-axis
  term (D18). The drag-moment lines of the moment budget (L1-AER-140) are then zero.
  Sufficiency (L1-AER-050): see L2-AER-DYN-100. Sufficiency (L1-AER-020): see L2-AER-DYN-050.
Parent(s):     L1-AER-050, L1-AER-020
Source:        DD-C1-01 (proposed); MS-DYN §5.1, §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-110; success criteria: gravity and drag are applied at the
  centre of gravity, and the only moment in the implemented rotational equation is the control
  moment from EF.
Parameters:    —
TBD/TBR:       No aerodynamic moment (DD-C1-01, C1-Q03), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-120

```req
ID:            L2-AER-DYN-120
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall apply at the centre of gravity a gravity force equal to the
  vehicle mass times [P-DYN-010], along the positive z axis of the local reference frame.
Rationale:     Uniform gravity on a flat, non-rotating world (L0-ASM-040, CV-110, CV-180). It gives
  the closed-form free fall of check C-1. [P-DYN-010] is standard gravity (TBR, TT-150), which is
  also the gravity share of the crew budget (FUNCTIONAL_ANALYSIS §7.2).
  Sufficiency (L1-AER-060): this record gives the uniform gravity of L1-AER-060, and L2-AER-DYN-600
  is the free-fall check it asks for.
  Sufficiency (L1-AER-290): see L2-AER-DYN-300.
Parent(s):     L1-AER-060, L1-AER-290
Source:        L0-ASM-040; CV-110, CV-180; MS-DYN §5.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-120; success criteria: the implemented gravity force is the
  vehicle mass of the step times [P-DYN-010] from the vehicle parameter set, along the positive z
  axis of the local reference frame, the same at each position and time, applied at the centre of
  gravity.
Parameters:    P-DYN-010
TBD/TBR:       P-DYN-010 value TBR (TT-150), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-130

```req
ID:            L2-AER-DYN-130
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the drag force from the air-relative velocity and
  the air density at the vehicle altitude by the drag model of MS-DYN.
Rationale:     Drag acts on the velocity relative to the air, which includes the wind (L0-CON-090,
  L0-ASM-050, CV-470). The form is a C1 choice bounded by L1-AER-020 and -030 (L1-AER-070
  rationale): MS-DYN §5.5 recommends isotropic quadratic drag with one drag area [P-DYN-100]
  (DD-C1-02), with a per-axis form as the alternative (C1-Q03). Both act at the centre of gravity.
  Sufficiency (L1-AER-070): L1-AER-070 asks for drag computed from the air-relative velocity and
  the standard-atmosphere density. This record ties the drag to both; L2-AER-DYN-140 defines the
  air-relative velocity with the wind of each step; L2-AER-DYN-150 the density; L2-AER-DYN-610 is
  the terminal-velocity check, with and without wind, that L1-AER-070 asks for.
Parent(s):     L1-AER-070
Source:        D17, D20, D51; MS-DYN §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-130; success criteria: for air-relative velocities along each body
  axis and oblique to them, at several attitudes and at altitudes across the range of the
  atmosphere model, the drag force the model computes equals the MS-DYN drag formula evaluated
  independently, to floating-point rounding.
Parameters:    P-DYN-100
TBD/TBR:       Drag form (DD-C1-02, C1-Q03), Martin, G2; P-DYN-100 value TBR, Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-140

```req
ID:            L2-AER-DYN-140
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the air-relative velocity of each simulation step as
  the vehicle velocity minus the wind velocity that the TST gives with the command for that step.
Rationale:     The wind of the run, steady wind plus gusts within the wind envelope, comes with each
  step command (L1-AER-670, I-25, D51, D62). The model uses it only through the air-relative
  velocity. The wind envelope itself, including the gust shape and the rise time, is defined in
  the MS-DYN wind model; the TST applies only winds inside it.
  Sufficiency (L1-AER-070): see L2-AER-DYN-130. Sufficiency (L1-AER-670): see L2-AER-DYN-400.
Parent(s):     L1-AER-070, L1-AER-670
Source:        CV-470; I-25; MS-DYN §5.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-140; success criteria: with zero fuel and drag on, (1) in a steady
  wind the horizontal velocity tends to the wind velocity, within [P-DYN-210] of the wind speed
  once settled; (2) with a wind that changes at one step command, the drag force recovered from
  the recorded vehicle acceleration (vehicle mass times the vehicle acceleration minus the gravity
  force) changes at that step and not at an earlier one.
Parameters:    P-DYN-210
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-150

```req
ID:            L2-AER-DYN-150
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the air density at the vehicle altitude by the
  atmosphere model of MS-DYN.
Rationale:     The density follows the standard atmosphere (D20) and depends on altitude only
  (L0-ASM-060). MS-DYN names it: the U.S. Standard Atmosphere, 1976, up to the top of its layer 3
  (glossary *Standard atmosphere*: "MS-DYN names the model"). Its constants are constants of the
  named standard, not parameters.
  Sufficiency (L1-AER-070): see L2-AER-DYN-130.
Parent(s):     L1-AER-070
Source:        D20; L0-ASM-060; MS-DYN §5.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-150; success criteria: check C-7 of MS-DYN: at the base altitude
  and at the midpoint of each layer of the atmosphere model, the computed density differs from the
  published table of the standard by at most [P-DYN-260] of the table value.
Parameters:    P-DYN-260
TBD/TBR:       P-DYN-260 value TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-160

```req
ID:            L2-AER-DYN-160
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall compute no aerodynamic force other than the drag force of
  the drag model.
Rationale:     Lift would couple attitude and translation (L1-AER-030 rationale). "Shall compute no"
  is a true prohibition (METHODOLOGY §8.4 rule 11). Under the recommended drag form (MS-DYN §5.5,
  option D1) the drag force is opposite to the air-relative velocity, so no part of it is
  perpendicular to the flow. Under option D2 a cross-flow component exists for oblique flow; the
  owner's ruling on C1-Q03 says whether it is accepted as drag.
  Sufficiency (L1-AER-030): the dynamics model is the only place an aerodynamic force can arise
  (L1-AER-030 rationale), so this record satisfies the inspection L1-AER-030 asks for.
Parent(s):     L1-AER-030
Source:        L0-CON-040; MS-DYN §5.1, §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-160; success criteria: MS-DYN and the implementation define no
  aerodynamic force other than the drag force of the drag model, and that force has no component
  perpendicular to the air-relative velocity (option D1) or the C1-Q03 ruling accepts its
  cross-flow component (option D2).
Parameters:    —
TBD/TBR:       Drag form (C1-Q03), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-170

```req
ID:            L2-AER-DYN-170
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall define no aerodynamic control surface and no force or moment
  that depends on a surface deflection.
Rationale:     Motion comes from the effectors, not from control surfaces (OBJECTIVES §2;
  AIRCRAFT_CHARACTERISTICS §2, §7). The two halves are one prohibition: no surface, and therefore
  nothing that a surface would produce (D30).
  Sufficiency (L1-AER-040): a control surface would appear either in the dynamics or in the
  effector set (L1-AER-040 rationale). This record excludes it from the dynamics; the EF child
  excludes it from the effector set.
Parent(s):     L1-AER-040
Source:        L0-CON-050; MS-DYN §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-170; success criteria: MS-DYN and the implementation define no
  control surface, no surface deflection and no force or moment that depends on one.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-180

```req
ID:            L2-AER-DYN-180
Level:         L2
Type:          Interface
Statement:     The dynamics model shall take the control force and the control moment of each
  simulation step from the effector outputs that EF provides for that step, in the body frame and
  about the centre of gravity.
Rationale:     The effectors are the only source of control force and moment (L0-CON-060,
  L1-AER-080). EF sums its effector outputs through their control effectiveness (L1-AER-100) and
  gives one force and one moment per step (I-02, MS-DYN §7.1); DYN holds them over the step
  (MS-DYN §10.2). The interface is internal to the vehicle model.
  Sufficiency (L1-AER-050): see L2-AER-DYN-100.
Parent(s):     L1-AER-050
Source:        I-02; MS-DYN §7.1, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-180; success criteria: the only input of the equations of motion
  that carries a control force or a control moment is the EF output of MS-DYN §7.1, resolved in
  the body frame and about the centre of gravity.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-190

```req
ID:            L2-AER-DYN-190
Level:         L2
Type:          Constraint
Statement:     While the air-relative velocity lies along one body axis, the dynamics model shall
  compute a drag force along that body axis only.
Rationale:     The DYN share of D18 for the drag: a translation along one axis does not cause an
  acceleration along another. Both drag forms of MS-DYN §5.5 meet it, so the record holds whatever
  the answer to C1-Q03.
  Sufficiency (L1-AER-020): see L2-AER-DYN-050.
Parent(s):     L1-AER-020
Source:        D18; MS-DYN §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-190; success criteria: for an air-relative velocity along each of
  the six body axis directions, at several attitudes and altitudes, the drag components along the
  other two body axes are zero to floating-point rounding.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-200

```req
ID:            L2-AER-DYN-200
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall place the origin of the body frame at the centre of gravity
  at each fuel state.
Rationale:     The centre of gravity is fixed in the body (L0-CON-130) and is the body origin
  (CV-160). The moments, the inertia and the effector moment arms then refer to one fixed point.
  Sufficiency (L1-AER-210): FU keeps the centre of gravity at one body point at each fuel state
  (FU child); DYN uses that point as the body origin (this record) and takes no other reference
  point. Together they give one centre-of-gravity position for every fuel mass, as L1-AER-210
  requires.
Parent(s):     L1-AER-210
Source:        CV-160; MS-DYN §4.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-200; success criteria: MS-DYN and the implementation place the
  body origin at the centre of gravity, with no fuel-state-dependent offset.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-210

```req
ID:            L2-AER-DYN-210
Level:         L2
Type:          Interface
Statement:     The dynamics model shall take the vehicle mass and the principal moments of inertia
  of each simulation step from FU.
Rationale:     FU owns the mass properties (FUNCTIONAL_ANALYSIS §6.1, I-04). DYN keeps no mass or
  inertia value of its own, so the mass decrease and any change of inertia with fuel reach the
  dynamics. The values are held over the step (MS-DYN §10.2). The centre of gravity is the body
  origin (L2-AER-DYN-200), so its position does not cross this interface.
  Sufficiency (L1-AER-180): see L2-AER-DYN-030. Sufficiency (L1-AER-220): see L2-AER-DYN-040.
Parent(s):     L1-AER-180, L1-AER-220
Source:        I-04; MS-DYN §6, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-210; success criteria: the equations of motion use the vehicle
  mass and the three principal moments of inertia that FU provides for the step, and the dynamics
  model holds no mass or inertia constant of its own.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-220

```req
ID:            L2-AER-DYN-220
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall define the body shape as the capsule of the vehicle geometry
  of MS-DYN, of overall length [P-DYN-020] along the body x axis and of diameter [P-DYN-030],
  centred on the centre of gravity.
Rationale:     L0-CON-140 asks for the inertia to be derived from an elongated body shape,
  provisionally a "Tic Tac" (AIRCRAFT_CHARACTERISTICS §1). L1-AER-220 places the shape in MS-DYN
  with its dimensions as DYN parameters (G1 disposition of L1-AER-220). A capsule is symmetric in
  each body coordinate plane, so a mass distribution with the same symmetry gives principal body
  axes (D61). The shape is provisional (C1-Q05).
  Sufficiency (L1-AER-220): see L2-AER-DYN-040.
Parent(s):     L1-AER-220
Source:        L0-CON-140; AIRCRAFT_CHARACTERISTICS.md §1; MS-DYN §2.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-220; success criteria: MS-DYN states the capsule, its axis
  along the body x axis, its centre at the centre of gravity and its dimensions as [P-DYN-020] and
  [P-DYN-030], and [P-DYN-020] is at least [P-DYN-030] in the parameter database.
Parameters:    P-DYN-020, P-DYN-030
TBD/TBR:       Body shape provisional (L0-CON-140, C1-Q05), Martin, 2026-11-30; P-DYN-020 and
  P-DYN-030 values TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-230

```req
ID:            L2-AER-DYN-230
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall place the nose of the body shape on the positive body x
  axis.
Rationale:     The nose marks the designated forward direction (L0-CON-150), which fixes the body x
  axis (CV-170) and the heading (CV-530). On the capsule it is the end of the body on the
  positive x axis (MS-DYN §2.2).
  Sufficiency (L1-AER-240): the MS-DYN geometry is the only place the nose is defined, so this
  record is the whole of what L1-AER-240 asks its children to show.
Parent(s):     L1-AER-240
Source:        L0-CON-150; CV-170; MS-DYN §2.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-230; success criteria: the MS-DYN vehicle geometry places the
  nose at the end of the capsule on the positive body x axis.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-240

```req
ID:            L2-AER-DYN-240
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall define the crew station at the body-frame position
  [P-DYN-400], forward of the centre of gravity and inside the body shape.
Rationale:     The crew sits in the cockpit toward the nose (L0-CON-150, CV-170). The crew
  acceleration limit is evaluated at the centre of gravity, not here (D45), so no model quantity
  is computed at the crew station; it fixes the crew position for the geometry and the manuals.
  Sufficiency (L1-AER-250): the MS-DYN geometry is the only place the crew station is defined, so
  this record covers L1-AER-250.
Parent(s):     L1-AER-250
Source:        L0-CON-150; CV-170; MS-DYN §2.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-240; success criteria: MS-DYN states the crew station as
  [P-DYN-400], and the value has a positive x component and lies inside the capsule of
  [P-DYN-020] and [P-DYN-030].
Parameters:    P-DYN-400, P-DYN-020, P-DYN-030
TBD/TBR:       P-DYN-400 value TBR (TT-140), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-300

```req
ID:            L2-AER-DYN-300
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute, at each simulation step, the sensed acceleration at
  the centre of gravity as the sum of the control force and the drag force divided by the vehicle
  mass, resolved in the body frame.
Rationale:     The crew limit is on the sensed acceleration, evaluated at the centre of gravity
  (D38, D45). DYN computes it from its definition (glossary; MS-DYN §8), so that the limit FC
  enforces can be measured in every run. The instant at which it is evaluated is MS-DYN §3.3
  (DD-C1-04). Under option T2 of #81.1 it differs from the vehicle acceleration minus gravity
  (C1-Q01).
  Sufficiency (L1-AER-290): FC limits the resultant control force at the current mass, AF limits
  the manoeuvres and FU supplies the mass (their children). DYN's share is the measured quantity
  (this record), the gravity that the budget counts as [P-DYN-010] (L2-AER-DYN-120), and no shock
  at contact: the state is held at the contact step, so contact adds no acceleration
  (L2-AER-DYN-550). With these, L1-AER-290 can be assessed in every automated test run.
  Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-290, L1-AER-640
Source:        D38, D45; MS-DYN §8
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-300; success criteria: (1) in check C-1 the sensed acceleration is
  zero at each step; (2) with DYN driven by a prescribed control force of the vehicle mass times
  [P-DYN-010] along the negative body z axis, at level attitude, zero velocity and in still air,
  the sensed acceleration magnitude is [P-DYN-010] and the vehicle acceleration is zero; (3) with
  drag and a control force, the recorded sensed acceleration equals the control force plus the
  drag divided by the mass, computed independently. Each to floating-point rounding.
Parameters:    P-DYN-010
TBD/TBR:       Evaluation instant of the acceleration quantities (DD-C1-04), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-310

```req
ID:            L2-AER-DYN-310
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute, at each simulation step, the vehicle acceleration
  as the rate of change of the vehicle velocity in the local reference frame that the
  translational equation of MS-DYN gives.
Rationale:     The vehicle acceleration is part of the vehicle state (glossary) and is what the
  TST measures for the vehicle acceleration limit (L1-AER-300). It is a derivative, so it depends
  on the inputs; MS-DYN §3.3 fixes the instant at which it is evaluated (DD-C1-04). The statement
  holds under both options of #81.1.
  Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-640
Source:        Glossary *Vehicle acceleration*; MS-DYN §3.2, §3.3, §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-310; success criteria: at each step of a run of the reference
  mission, the recorded vehicle acceleration equals the MS-DYN translational equation evaluated
  independently from the recorded state and inputs at the instant of MS-DYN §3.3, to
  floating-point rounding; in check C-1 it equals the gravitational acceleration.
Parameters:    —
TBD/TBR:       Evaluation instant of the acceleration quantities (DD-C1-04), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-320

```req
ID:            L2-AER-DYN-320
Level:         L2
Type:          Interface
Statement:     The dynamics model shall provide the vehicle state of each simulation step at the
  vehicle-model boundary, as the vehicle-model boundary ICD defines it.
Rationale:     A fixed boundary lets the control law and the autoflight be replaced without
  touching the vehicle model (L0-CON-200, -210). The state carries the frames and units of
  CONVENTIONS and the quaternion attitude (IN-B1-01). The ICD home is decided at I1 (TT-720).
  Sufficiency (L1-AER-430): L1-AER-430 closes the boundary to effector commands in and the
  vehicle state, mass properties and fuel state out. DYN's part is the vehicle state out (this
  record) and nothing else (L2-AER-DYN-340). DYN receives no data from the flight software: the
  effector commands go to EF. The mass properties and the fuel state are FU's.
Parent(s):     L1-AER-430
Source:        IN-B1-01; I-07, I-09, I-10
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-320; success criteria: each element of the vehicle state that
  DYN provides is defined in the vehicle-model boundary ICD with its frame and SI unit.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-330

```req
ID:            L2-AER-DYN-330
Level:         L2
Type:          Interface
Statement:     The dynamics model shall provide to the navigation and flight-control functions, at
  the start of each control frame, the vehicle state of the first simulation step of that frame,
  equal to the vehicle state it records for that step.
Rationale:     Perfect state knowledge is a requirement (L0-ASM-010, L1-AER-440). The only delay is
  the control-frame sampling, which the timing budget counts (FUNCTIONAL_ANALYSIS §7.5). Sensor
  models are a later upgrade (#83).
  Sufficiency (L1-AER-440): DYN gives the exact state of the frame-start step (this record); NAV
  and FC use it without modification (their children). Together NAV and FC receive the exact
  simulated state, as L1-AER-440 requires.
Parent(s):     L1-AER-440
Source:        L0-ASM-010; FUNCTIONAL_ANALYSIS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-330; success criteria: in a run of the reference mission, at each
  control frame, the state that NAV and FC receive equals, element by element, the recorded
  vehicle state of the frame-start step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-340

```req
ID:            L2-AER-DYN-340
Level:         L2
Type:          Interface
Statement:     The dynamics model shall limit the data it passes to the flight software to the
  vehicle state.
Rationale:     The boundary list of L1-AER-430 is closed. In particular the wind, which DYN
  receives with each step, does not reach the flight software (L1-AER-670 rationale), and the
  sensed acceleration and the ground-contact events go to TM and the TST, not to the flight
  software.
  Sufficiency (L1-AER-430): see L2-AER-DYN-320.
Parent(s):     L1-AER-430
Source:        L1-AER-670 rationale; FUNCTIONAL_ANALYSIS §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-340; success criteria: the only DYN output that a flight
  software function reads is the vehicle state of the vehicle-model boundary ICD.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-350

```req
ID:            L2-AER-DYN-350
Level:         L2
Type:          Interface
Statement:     The dynamics model shall provide to the operational data output, at each simulation
  step, its vehicle state and its sensed acceleration at the centre of gravity.
Rationale:     Vehicle responses are one of the things the operational data relate (L0-OBJ-140),
  and the TST measures the performance records from them (L1-AER-290, -300, -460). DYN gives the
  values of every step; TM records them at each output sample.
  Sufficiency (L1-AER-640): L1-AER-640 records the vehicle state, the navigation quantities, the
  sensed acceleration, the masses and the ground-contact events. DYN provides the vehicle state
  (with the Euler angles of L2-AER-DYN-070 and the vehicle acceleration of -310), the sensed
  acceleration (this record) and the ground-contact events (-530); NAV provides the navigation
  quantities and FU the masses; TM records them. Together they cover the list.
Parent(s):     L1-AER-640
Source:        N-250, N-340; I-32, I-37
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-350; success criteria: at each output sample of a run of the
  reference mission, the operational data hold the DYN vehicle state and sensed acceleration of
  that sample's step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-400

```req
ID:            L2-AER-DYN-400
Level:         L2
Type:          Interface
Statement:     When the TST commands a step, the dynamics model shall advance the vehicle state by
  one simulation step of [P-SYS-300], by the simulation step section of MS-DYN.
Rationale:     The TST executes the model at a fixed step and controls time, so a run can go faster
  or slower than real time with the same result (F-TST-01, CV-810, CV-820). Simulation time is
  the step index times the step, not an accumulated sum (CV-820). The integration method is free
  within the accuracy of the credibility checks (MS-DYN §10.3, D4).
  Sufficiency (L1-AER-670): L1-AER-670 asks for one step of [P-SYS-300] per command with the wind
  of that command. This record gives the step; L2-AER-DYN-140 uses the wind of the command in the
  drag and L2-AER-DYN-410 holds it over the step.
Parent(s):     L1-AER-670
Source:        F-TST-01; CV-810, CV-820; MS-DYN §10.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-400; success criteria: from step zero, each commanded step adds one
  to the step index, and the simulation time of the state is the step index times [P-SYS-300].
Parameters:    P-SYS-300
TBD/TBR:       P-SYS-300 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-410

```req
ID:            L2-AER-DYN-410
Level:         L2
Type:          Interface
Statement:     The dynamics model shall hold the wind velocity given with each step command constant
  over that simulation step.
Rationale:     A defined hold makes the step reproducible and gives the independent solutions of
  MS-DYN §11 a known input (MS-DYN §10.2). The gusts of the wind envelope build up over at least
  [P-SYS-570], so a hold over one step of [P-SYS-300] is a small discretisation of a smooth wind
  (MS-DYN §5.4).
  Sufficiency (L1-AER-670): see L2-AER-DYN-400. Sufficiency (L1-AER-070): see L2-AER-DYN-130.
Parent(s):     L1-AER-670, L1-AER-070
Source:        D62; MS-DYN §5.4, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-410; success criteria: the implementation uses the wind of the
  command for a step at each evaluation within that step, and no other wind value.
Parameters:    P-SYS-570, P-SYS-300
TBD/TBR:       P-SYS-570 value TBD (TT-650; proposed TBR value in work/C1/param_proposals.md),
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-420

```req
ID:            L2-AER-DYN-420
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall compute the vehicle state of each simulation step from the
  vehicle state of the previous step, the inputs of the previous step and the vehicle parameter
  set only.
Rationale:     Repeat runs must give the same verdicts (L0-OBJ-110, D59). A step that depends only
  on the run's own state, inputs and parameters (no wall-clock time, no random number, no
  dependence on scheduling) gives the same states for the same run. Bit-identical results are
  not required (D25, D59). The inputs of a step are the control force and moment, the mass
  properties and the wind (MS-DYN §10.2).
  Sufficiency (L1-AER-690): the TST inputs (step commands and wind) are part of the run's
  condition (L1-AER-690 rationale); with them fixed, this record makes the DYN contribution to
  the operational data the same from run to run, which is DYN's share of the same verdicts.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59; MS-DYN §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-420; success criteria: repeated executions of the same run, on
  separate simulation instances, give the same verdict for each success criterion of the DYN
  records and vehicle states that agree within the tolerances of those criteria (D59, D63).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-430

```req
ID:            L2-AER-DYN-430
Level:         L2
Type:          Interface
Statement:     When a run starts, the dynamics model shall set the vehicle state of step zero to the
  position, the velocity, the attitude and the body rates of the initial condition that the TST
  gives.
Rationale:     The TST sets the whole starting state of a run (N-310, CONOPS §4.6). The list is the
  kinematic part of the initial condition; the fuel mass is FU's, the mode state and targets are
  AF's and FCP's. The attitude is given as a unit quaternion (IN-C1-21).
  Sufficiency (L1-AER-660): DYN takes the position, velocity, attitude and body rates (this
  record); FU, AF and FCP take the rest (their children). Together the initial condition of
  L1-AER-660 is accepted in full.
Parent(s):     L1-AER-660
Source:        N-310; CONOPS §4.6; MS-DYN §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-430; success criteria: for several initial conditions, the first
  output sample reports the given position, velocity and body rates, and the given attitude (the
  same rotation, with the quaternion sign of CV-250).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-440

```req
ID:            L2-AER-DYN-440
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall take the value of each of its parameters from the vehicle
  parameter set of the run.
Rationale:     The vehicle parameter set is part of the run's configuration (glossary
  *Configuration (run)*, F-AER-14), so a campaign can change a value without a software change,
  and the credibility checks can run the vacuum-equivalent configuration (MS-DYN §5.5, §11). The
  constants of the standard atmosphere are not parameters (MS-DYN §5.3).
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        F-AER-14; N-020, N-350; MS-DYN §12
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-DYN-440; success criteria: two runs that differ only in the
  value of [P-DYN-100], one of them zero, run with no software change and show the free fall of
  check C-1 and the drag behaviour of check C-2.
Parameters:    P-DYN-100
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-500

```req
ID:            L2-AER-DYN-500
Level:         L2
Type:          Functional
Statement:     When the altitude reaches zero, the dynamics model shall raise one ground-contact
  event at that simulation step.
Rationale:     Ground contact is contact with the datum plane at altitude zero (D8, CV-420).
  "Reaches" is the first step at which the propagated altitude is at most zero (CV-940). That step
  is the contact step, the "contact sample" of L1-AER-280 (glossary proposal). The model checks
  from step zero (MS-DYN §9).
  Sufficiency (L1-AER-260, L1-AER-270): these records ask for a landing or a crash to be
  reported at contact. DYN detects the contact (this record), classifies it (L2-AER-DYN-510,
  -520), outputs one event record (-530), reports a non-negative altitude (-540) and holds the
  state so that there is no further event (-550); TM records the event in the operational data.
  Together they give one correctly classified event at the contact step.
  Sufficiency (L1-AER-280): see L2-AER-DYN-510.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-280
Source:        D8, D37; CV-420, CV-940; MS-DYN §9
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-500; success criteria: in descents to the ground at several vertical
  and horizontal speeds, the model raises exactly one ground-contact event, at the first step at
  which the propagated altitude is at most zero, and none at an earlier step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-510

```req
ID:            L2-AER-DYN-510
Level:         L2
Type:          Functional
Statement:     When the dynamics model raises a ground-contact event with a vertical speed magnitude
  of at most [P-SYS-500] and a horizontal speed of at most [P-SYS-510] at the contact step, the
  dynamics model shall classify the contact as a landing.
Rationale:     Ideal landing (D37, L0-CON-290): the envelope is two speed limits at the contact
  sample, with no acceleration limit (D53). The two limits are one envelope (D30). The speeds are
  ground-referenced (CV-480, CV-490) and are those of the contact step's state, not interpolated
  (MS-DYN §9). The limits are inclusive (CV-940).
  Sufficiency (L1-AER-280): this record and L2-AER-DYN-520 partition the contacts by the two
  limits at the contact step, which is the classification L1-AER-280 states; L2-AER-DYN-500 fixes
  the contact step.
  Sufficiency (L1-AER-260): see L2-AER-DYN-500.
Parent(s):     L1-AER-280, L1-AER-260
Source:        D37, D53; MS-DYN §9
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-510; success criteria: contacts with the vertical speed magnitude and
  the horizontal speed each at its limit, and each just inside it, are classified as landings.
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (TT-090), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-520

```req
ID:            L2-AER-DYN-520
Level:         L2
Type:          Functional
Statement:     When the dynamics model raises a ground-contact event with a vertical speed magnitude
  that exceeds [P-SYS-500] or a horizontal speed that exceeds [P-SYS-510] at the contact step,
  the dynamics model shall classify the contact as a crash.
Rationale:     Contact outside the envelope is a crash that ends the run (D37). The reference
  mission normally ends this way, after fuel exhaustion (SC-110). "Exceeds" is strictly above
  (CV-940), so this record and L2-AER-DYN-510 leave no contact unclassified.
  Sufficiency (L1-AER-280): see L2-AER-DYN-510. Sufficiency (L1-AER-270): see L2-AER-DYN-500.
Parent(s):     L1-AER-280, L1-AER-270
Source:        D37, D53; CONOPS SC-110; MS-DYN §9
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-520; success criteria: contacts with the vertical speed magnitude
  just above its limit, with the horizontal speed just above its limit, and a free fall to the
  ground from fuel exhaustion are each classified as a crash.
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (TT-090), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-530

```req
ID:            L2-AER-DYN-530
Level:         L2
Type:          Interface
Statement:     When the dynamics model classifies a ground contact, the dynamics model shall output
  one event record with the classification and the timestamp of the contact step, as ICD-AER-TST
  defines it.
Rationale:     The event goes to TM for the operational data (I-37) and to the TST, which ends the
  run on it (I-41, CONOPS §4.6). The timestamp is the step index and the simulation time of the
  contact step (CV-840). An event record is not tied to an output sample, so the classification
  instant is the contact step even when it falls between output samples.
  Sufficiency (L1-AER-260, L1-AER-270): see L2-AER-DYN-500. Sufficiency (L1-AER-640): see
  L2-AER-DYN-350.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-640
Source:        I-37, I-41; CV-840
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-530; success criteria: in each contact test of L2-AER-DYN-510 and
  -520, one event record is output, with the expected classification and the step index and
  simulation time of the contact step, in the ICD-AER-TST format.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-540

```req
ID:            L2-AER-DYN-540
Level:         L2
Type:          Functional
Statement:     When the dynamics model raises a ground-contact event, the dynamics model shall
  report the vehicle position of the contact step with an altitude of zero.
Rationale:     Derived from a design decision (DD-C1-03, proposed). With a fixed step the
  propagated altitude at the contact step is at most zero and can be slightly negative. CV-420
  states that the altitude is never negative in a run, so the reported position is set onto the
  datum plane; the horizontal position and the velocity stay as propagated, and the
  classification uses that velocity. The alternative, interpolating the state to the crossing
  instant, puts a state off the CV-820 time grid.
Parent(s):     Derived (DD-C1-03)
Source:        CV-420, CV-820; MS-DYN §9
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-540; success criteria: in each contact test, the reported altitude of
  the contact step is zero, its horizontal position and velocity equal the propagated values, and
  no recorded altitude of the run is negative.
Parameters:    —
TBD/TBR:       DD-C1-03 to be accepted, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-550

```req
ID:            L2-AER-DYN-550
Level:         L2
Type:          Functional
Statement:     While a ground-contact event has been raised, the dynamics model shall keep the
  vehicle state of the contact step.
Rationale:     The ideal landing has no gear, bounce, friction or ground reaction (D37, L0-ASM-110):
  contact ends the motion. The TST ends the run on the event; if it commands a further step, the
  state does not change and no second event is raised. Holding the state also means no
  touchdown acceleration is computed (D53).
  Sufficiency (L1-AER-260, L1-AER-270): see L2-AER-DYN-500. Sufficiency (L1-AER-290): see
  L2-AER-DYN-300.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-290
Source:        D37, D53; L0-ASM-110; MS-DYN §9
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-550; success criteria: when further steps are commanded after a
  contact, the vehicle state stays that of the contact step and no further ground-contact event
  is raised.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-600

```req
ID:            L2-AER-DYN-600
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero in the vacuum-equivalent configuration, the dynamics
  model shall match the free-fall solution of the credibility checks of MS-DYN within
  [P-DYN-200] at each simulation step.
Rationale:     Free fall in vacuum-equivalent conditions has a closed-form solution (L0-ASM-040,
  METHODOLOGY §10.3, N-290): check C-1. With zero fuel the effectors produce nothing
  (L1-AER-200), and with a zero drag area there is no drag, so only gravity acts. The tolerance
  bounds the numerical error of the integration (MS-DYN §10.3).
  Sufficiency (L1-AER-060): see L2-AER-DYN-120. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-060, L1-AER-010
Source:        N-290; METHODOLOGY §10.3; MS-DYN §11 (C-1)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-600; success criteria: check C-1 from several initial states
  (including non-zero horizontal velocity and non-zero body rates) down to the contact step: the
  position and velocity errors, relative to their change since the start, are at most
  [P-DYN-200] at each step.
Parameters:    P-DYN-200, P-DYN-010
TBD/TBR:       P-DYN-200 value TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-610

```req
ID:            L2-AER-DYN-610
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero at level attitude with zero body rates, the dynamics
  model shall produce a settled vertical speed within [P-DYN-210] of the terminal vertical speed
  of the credibility checks of MS-DYN, in still air and in a steady wind of up to [P-SYS-430].
Rationale:     A free fall with drag settles at the speed where drag balances weight (check C-2,
  METHODOLOGY §9.3). The density changes with altitude, so the expected value carries the
  quasi-steady correction of MS-DYN §11. With a steady wind the horizontal velocity tends to the
  wind and the vertical speed to the same terminal value, which checks the air-relative velocity.
  Sufficiency (L1-AER-070): see L2-AER-DYN-130. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-070, L1-AER-010
Source:        N-290; METHODOLOGY §9.3, §10.3; MS-DYN §11 (C-2)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-610; success criteria: check C-2 in still air and in a steady
  wind of [P-SYS-430]: from the end of the procedure's settling interval to the contact step, the
  vertical speed magnitude differs from the expected terminal value by at most [P-DYN-210] of
  that value at each step.
Parameters:    P-DYN-210, P-DYN-100, P-SYS-430
TBD/TBR:       P-DYN-210 value TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-620

```req
ID:            L2-AER-DYN-620
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero, the dynamics model shall conserve the angular momentum
  in the local reference frame and the rotational kinetic energy within [P-DYN-220] over
  [P-DYN-270].
Rationale:     With no control moment, and gravity and drag acting at the centre of gravity, the
  rotation is torque-free, so the angular momentum in the inertial frame and the rotational
  kinetic energy are constant (check C-3, METHODOLOGY §10.3). The check exercises the gyroscopic
  term K-1, which is zero in normal operation (MS-DYN §4.5). The horizon covers the longest run.
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        METHODOLOGY §10.3; MS-DYN §11 (C-3)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-620; success criteria: check C-3 with body rates non-zero about
  each body axis: over [P-DYN-270], the relative change of the angular momentum magnitude, the
  change of its direction and the relative change of the rotational kinetic energy are each at
  most [P-DYN-220].
Parameters:    P-DYN-220, P-DYN-270
TBD/TBR:       P-DYN-220, P-DYN-270 values TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-630

```req
ID:            L2-AER-DYN-630
Level:         L2
Type:          Model fidelity
Statement:     While a prescribed constant control force acts with a prescribed decreasing vehicle
  mass in the vacuum-equivalent configuration, the dynamics model shall match the variable-mass
  solution of the credibility checks of MS-DYN within [P-DYN-240].
Rationale:     The mass loss is a real effect on the dynamics (L0-ASM-090). Check C-4 drives DYN
  with a prescribed force and mass in place of the EF and FU outputs, so it checks DYN's use of
  the mass against a closed form, independently of the fuel model; the fuel-mass integral is
  FU's check C-8 (L1-AER-190).
  Sufficiency (L1-AER-180): see L2-AER-DYN-030. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-180, L1-AER-010
Source:        L0-ASM-090; METHODOLOGY §10.3; MS-DYN §11 (C-4)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-630; success criteria: check C-4: the north velocity error,
  relative to its change since the start, is at most [P-DYN-240] at each step.
Parameters:    P-DYN-240
TBD/TBR:       P-DYN-240 value TBR, Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-640

```req
ID:            L2-AER-DYN-640
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero in the vacuum-equivalent configuration with a non-zero
  yaw rate, the dynamics model shall match the horizontal velocity of the rotation-during-
  translation check of MS-DYN, for the option that the kinematic terms list records, within
  [P-DYN-250] over [P-DYN-270].
Rationale:     The rotation-during-translation term (K-2) is the one kinematic term whose treatment
  is open (#81.1). Check C-5 states the expected horizontal velocity under each option, so the
  record is correct under either answer and shows that the model contains the term the owner
  chose.
  Sufficiency (L1-AER-020): see L2-AER-DYN-050. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-020, L1-AER-010
Source:        D18; #81.1; MS-DYN §4.5, §11 (C-5)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-640; success criteria: check C-5 for the recorded option: over
  [P-DYN-270], the horizontal velocity error relative to the initial horizontal speed is at most
  [P-DYN-250] at each step, and the yaw rate, pitch angle and roll angle keep their initial values
  to within the same relative tolerance.
Parameters:    P-DYN-250, P-DYN-270
TBD/TBR:       Rotation-during-translation term (#81.1, C1-Q01), Martin, G2; P-DYN-250 value TBR,
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-700

```req
ID:            L2-AER-DYN-700
Level:         L2
Type:          Documentation
Statement:     The dynamics model shall have its model specification MS-DYN baselined with one named
  section for each of the vehicle geometry, the vehicle state, the equations of motion, the
  kinematic terms, the total force and moment, the gravity, atmosphere, wind and drag models, the
  sensed acceleration, the ground contact model, the simulation step and the credibility checks.
Rationale:     L0-OBJ-010 requires the executable model to conform to a baselined model
  specification. The list is the DYN content of MS-DYN; the sections are named because the
  requirements cite them by name (MS-DYN §0).
  Sufficiency (L1-AER-720): L1-AER-720 asks for a baselined MS-DYN that states the equations of
  motion, the gravity, drag and wind model, the ground contact model and the effector, fuel and
  mass-properties models. DYN writes the first four groups (this record). FU and EF write the
  mass-properties, effector and fuel sections into MS-DYN §6 and §7 (their children). Together
  they give the whole content L1-AER-720 lists.
Parent(s):     L1-AER-720
Source:        N-270; plan §6 C1; TT-660
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-700; success criteria: MS-DYN is baselined at G2, and it has a
  section under each listed name that states that model.
Parameters:    —
TBD/TBR:       MS-DYN not yet baselined (TT-660), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```
