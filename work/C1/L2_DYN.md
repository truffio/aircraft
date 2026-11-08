## DYN — Dynamics model

The dynamics model requirements (task C1). The subject of each statement is the dynamics model, the DYN subsystem of the vehicle model (glossary *Dynamics model*). The physics is stated in [specs/MS-DYN.md](../specs/MS-DYN.md); these records point to its named sections, because a statement cannot carry a section number. DYN implements functions F-AER-03, F-AER-04, F-AER-12, F-AER-15 and its part of F-AER-14 (FUNCTIONAL_ANALYSIS §6.1 as revised by CR-B3-38, CR-B3-40).

**Depth.** Each record below is a leaf: the next layer would be the implementation (integration method, code structure), so DYN has no L3 section (D4). Each record is verified directly by its own method (D40). Procedure IDs follow the record number (IN-, AN-, TP-, DM-DYN-nnn); Phase 5 (V1) writes the procedures.

**Owner answers.** D64: the rotation-during-translation term is retained (#81.1, option T1) and #81 is closed with the MS-DYN kinematic terms list; drag is isotropic quadratic with no aerodynamic moment (option D1); the gust shape and the 2 s rise time, the capsule and its dimensions (TBR) and standard gravity (Set) are accepted. D69 and D73 (the approved B3 package, L1-AER-900 to -970 and CR-B3-01 to -41): a retractable landing gear, a rest on the ground under a ground reaction, runs that start on the ground (airborne starts for test runs and credibility checks only, B3-1), and any contact other than a landing on the extended gear within the envelope with fuel remaining is a crash (B3-3). D72: no long checks (the torque-free and rotation-during-translation checks run gravity-free over [P-DYN-270]); isotropic drag meets D18; [P-SYS-230] is a ground speed. This version 2 applies the G2 findings and D69; `work/C1/rework_G2_D69.md` gives the disposition of each finding and each change.

**Coverage of the L1 parents.** Every L1 record allocated to DYN has at least one DYN child. L1-AER-230 is Deleted (D54) and has none. The L1 records cited are those of AER-L1-baseline-1 as changed by CR-B3-01 to -41, with the new records L1-AER-900 to -970 (D73).

| L1 parent | What DYN guarantees, in the parent's terms | DYN children |
| --- | --- | --- |
| L1-AER-010 | The motion is that of a six-degree-of-freedom rigid body by the MS-DYN equations, and it matches the free-fall, terminal-velocity and torque-free rotation solutions | -010, -020, -030, -040, -060, -440, -600, -610, -620, -630, -640 |
| L1-AER-020 | The DYN equations contain no cross-axis term other than the kinematic terms MS-DYN lists; drag along one axis for motion along that axis, with the shared airspeed of oblique flow accepted as meeting D18 (D72); the rotation uses principal moments only | -040, -050, -110, -190, -640 |
| L1-AER-030 | The model computes no aerodynamic force other than drag | -160 |
| L1-AER-040 | The dynamics define no control surface | -170 |
| L1-AER-050 | The total force is gravity plus drag plus the control force plus, on the ground, the ground reaction; the total moment is the control moment plus, on the ground, the moment of the ground reaction | -100, -110, -180, -580 |
| L1-AER-060 | Gravity is uniform, of magnitude [P-DYN-010], downward; free fall matches the closed form | -120, -600 |
| L1-AER-070 | Drag uses the air-relative velocity with the TST wind held over each step and the standard-atmosphere density; terminal speed matches, with and without wind | -130, -140, -150, -410, -610 |
| L1-AER-180 | The motion uses the vehicle mass FU gives at each step, so a lower mass gives a larger acceleration | -030, -210, -630 |
| L1-AER-210 | The body origin is the centre of gravity at each fuel state | -200 |
| L1-AER-220 | The body shape is stated with its dimensions; the rotation uses FU's diagonal tensor | -040, -210, -220 |
| L1-AER-240 | The nose is on the positive body x axis | -230 |
| L1-AER-250 | The crew station is at [P-DYN-400] | -240 |
| L1-AER-260 | A contact on the extended gear within the envelope with fuel available is detected, classified as a landing, output as one event at the contact step, and followed by the rest on the ground, so the run goes on | -370, -500, -510, -530, -560 |
| L1-AER-270 | Any other contact (outside the envelope, gear retracted or in transit, body first, fuel not available) is detected, classified as a crash, output as one event at the contact step, and the state is then held | -370, -500, -520, -530, -550 (and the Derived -540) |
| L1-AER-280 | Classification by the two speed limits at the contact step; gear and fuel are conditions of a landing, not of the envelope | -500, -510, -520 |
| L1-AER-290 | The sensed acceleration at the centre of gravity is computed exactly; gravity is the budgeted [P-DYN-010]; the landing arrest on the ideal gear adds no shock | -120, -300, -560 |
| L1-AER-430 | DYN passes only the vehicle state and the gear state across the vehicle-model boundary, and takes only the landing gear command from it | -290, -320, -340, -360 |
| L1-AER-440 | NAV and FC receive the exact recorded state of the frame-start step | -330 |
| L1-AER-640 | DYN gives TM the vehicle state (with Euler angles and vehicle acceleration), the gear state, the sensed acceleration and the landing and crash events | -070, -290, -300, -310, -350, -530 |
| L1-AER-660 | Step zero is the TST's initial condition: the rest state for a start on the ground, the given position, velocity, attitude and body rates for an airborne start; an airborne start with the body at or below the ground is rejected | -430, -450, -470 |
| L1-AER-670 | One step of [P-SYS-300] per command, with the wind of that command held over the step | -140, -400, -410 |
| L1-AER-690 | Each step depends only on the run's state, inputs and parameters | -420 |
| L1-AER-720 | MS-DYN is baselined with a named section for each DYN model, the landing gear model and the ground contact model included; FU and EF fill theirs | -700 |
| L1-AER-900 | The vehicle geometry places the extended gear contact points [P-DYN-040] below the lowest point of the body and the retracted gear inside the body; the gear position changes no drag, moment or mass property | -250, -260 |
| L1-AER-910 | The gear follows the landing gear command from autoflight while airborne and reaches the commanded position within [P-DYN-050], in transit until then, and stays extended on the ground; the gear state makes it observable | -270, -280, -290, -360 |
| L1-AER-920 | On the ground the vehicle is held at the rest state on its extended gear, under the ground reaction, with a sensed acceleration of [P-DYN-010], until the upward control force exceeds the weight | -280, -300, -560, -570, -580, -590 |
| L1-AER-950 | A start on the ground is the rest state at the given horizontal position and heading, with the gear extended and the vehicle on the ground; an inconsistent ground initial condition is rejected | -450, -460 |

One record is Derived: L2-AER-DYN-540 (DD-070, as revised by DD-240).

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
  equations retain the rotation-during-translation term (D64, MS-DYN §4.2, §4.5). They propagate
  the motion while the vehicle is airborne; on the ground the integrated state is held at the rest
  state (L2-AER-DYN-570).
  Sufficiency (L1-AER-010): L1-AER-010 asks for six-degree-of-freedom rigid-body motion in
  accordance with MS-DYN, shown against free fall, free fall with drag and torque-free rotation.
  This record fixes the equations; -020 the integrated state; -030 and -040 the translational and
  rotational laws with the mass properties of the step; -060 the attitude; -440 the parameters.
  L2-AER-DYN-600, -610 and -620 are the three checks L1-AER-010 names, and -630 and -640 add the
  variable mass and the rotation-during-translation term. Together they make the executable model
  conform to MS-DYN.
Parent(s):     L1-AER-010
Source:        N-270, N-290; MS-DYN §4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-010; success criteria: the implementation integrates exactly the
  elements of the integrated state of the MS-DYN vehicle state section, and it implements one term
  for each term of the MS-DYN equations of motion and no other term.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-020

```req
ID:            L2-AER-DYN-020
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall hold, at each simulation step, an integrated state made of
  the position and the velocity of the centre of gravity in the local reference frame, the
  attitude quaternion and the body rates.
Rationale:     These are the thirteen integrated quantities of a rigid body (MS-DYN §3.1). The
  quaternion is the authoritative attitude (D22, CV-250). The *vehicle state* of the glossary is
  this integrated state plus the quantities derived from it: the Euler angles, the body-axis
  velocity and the vehicle acceleration (L2-AER-DYN-070, -310; G2-F15). The gear state is a
  separate DYN item, not part of either (L2-AER-DYN-290). The list is closed (D30: one state).
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        MS-DYN §3; CV-250, CV-410, CV-460; G2-F15
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-020; success criteria: the integrated state held at each step
  has exactly these elements, in the frames and SI units of the MS-DYN vehicle state section, and
  the attitude is the scalar-first unit quaternion of CV-250.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
  the vehicle velocity" and not "total force divided by mass"; with the term retained (D64) the
  two are the same in the local reference frame (MS-DYN §4.2).
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
  is the one MS-DYN §4.2 gives with the rotation-during-translation term retained (D64), it uses
  the vehicle mass that FU provides for the step, and it has no term in the fuel mass flow.
Parameters:    —
TBD/TBR:       —
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
  gyroscopic term (K-1), the rotation-during-translation term (K-2) and the resolution of gravity,
  drag, the control force and the ground reaction through the attitude (K-3), all retained by the
  owner (D64, #81, #81.1). With pitch and roll held at zero (D57) K-1 is zero in normal operation,
  and K-2 has no vertical component. The drag is not a cross-axis term: motion along one body axis
  gives drag along that axis only (L2-AER-DYN-190), and for an oblique flow the drag along each
  axis depends on the other components only through the shared airspeed magnitude, which the owner
  accepts as meeting D18 (D72, G2 Q3). MS-DYN §4.5 records that reading, so that the roll-up of
  L0-CON-030 has an explicit basis (G2-F06).
  Sufficiency (L1-AER-020): the coupling sources the model contains are the equations of motion,
  the drag, the effectors and the inertia. DYN covers the equations (this record), the drag
  (L2-AER-DYN-190, with the D72 reading for oblique flow; L2-AER-DYN-110: no aerodynamic moment)
  and uses only the principal moments (L2-AER-DYN-040); EF excludes effector coupling and FU gives
  zero products of inertia. L2-AER-DYN-640 checks the K-2 behaviour. With MS-DYN listing each
  retained term and the drag reading, the DYN part of what L1-AER-020 asks its children to show
  is met.
Parent(s):     L1-AER-020
Source:        D18, D57, D61, D64, D72; #81
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-050; success criteria: each implemented term that relates two
  degrees of freedom is a term of the MS-DYN kinematic terms list, and the list states the owner's
  decisions (D64) and the reading of the drag against D18 (D72).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
TBD/TBR:       P-DYN-230 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
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
  gravity force, the drag force, the control force and, while the vehicle is on the ground, the
  ground reaction, with no other contribution.
Rationale:     L0-CON-090 limits the external effects to gravity, drag on the air-relative velocity
  and ground contact; ground contact includes the ground reaction that holds the vehicle at rest on
  its gear (CR-B3-03, D69). A ground contact of the airborne vehicle is not a force: it is detected
  and classified (MS-DYN §5.1, §9). The control force is the only other force (L0-CON-060, which
  excludes the ground reaction from the control forces, CR-B3-02). Consumed fuel adds no force
  (L0-ASM-090). The list is closed.
  Sufficiency (L1-AER-050): L1-AER-050 closes the forces and moments to gravity, drag, the control
  forces and moments and, on the ground, the ground reaction. This record closes the force;
  L2-AER-DYN-110 the moment; L2-AER-DYN-180 takes the control part from EF; L2-AER-DYN-120 and -130
  fix gravity and drag; L2-AER-DYN-580 defines the ground reaction. The free-fall and
  terminal-velocity checks that L1-AER-050 cites are L2-AER-DYN-600 and -610, and the zero total
  force at rest on the ground is check C-9 (L2-AER-DYN-580).
Parent(s):     L1-AER-050
Source:        L0-CON-090; D69; MS-DYN §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-100; success criteria: the implemented total force has exactly
  four contributions, gravity, drag, the control force from EF and, only while the vehicle is on
  the ground, the ground reaction, as the MS-DYN total force and moment section states.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-110

```req
ID:            L2-AER-DYN-110
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the total moment about the centre of gravity as the
  control moment plus, while the vehicle is on the ground, the moment of the ground reaction, with
  no moment from gravity or from drag.
Rationale:     Gravity is uniform and acts at the centre of gravity, so it gives no moment. Drag
  acts at the centre of gravity and there is no rotational damping moment (DD-050, accepted, D64):
  a vehicle at fuel exhaustion keeps its angular momentum, as CONOPS SC-110 and the L1-AER-200 and
  -390 rationales describe. A drag moment depending on the translation would also be a cross-axis
  term (D18). The drag-moment lines of the moment budget (L1-AER-140) are then zero. On the ground
  the moment of the ground reaction balances the control moment, so that the vehicle neither
  turns nor tips (L1-AER-920).
  Sufficiency (L1-AER-050): see L2-AER-DYN-100. Sufficiency (L1-AER-020): see L2-AER-DYN-050.
Parent(s):     L1-AER-050, L1-AER-020
Source:        DD-050; MS-DYN §5.1, §5.5, §9.6
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-110; success criteria: gravity and drag are applied at the
  centre of gravity, and the only moments in the implemented rotational equation and in the ground
  reaction are the control moment from EF and, on the ground only, the moment of the ground
  reaction.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-120

```req
ID:            L2-AER-DYN-120
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall apply at the centre of gravity a gravity force equal to the
  vehicle mass times [P-DYN-010], along the positive z axis of the local reference frame.
Rationale:     Uniform gravity on a flat, non-rotating world (L0-ASM-040, CV-110, CV-180). It gives
  the closed-form free fall of check C-1. [P-DYN-010] is standard gravity (Set, D64), which is also
  the gravity share of the crew budget (FUNCTIONAL_ANALYSIS §7.2). The gravity-free check
  configuration of checks C-3 and C-5 sets it to zero in the check's vehicle parameter set only
  (D72, L2-AER-DYN-440).
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
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
  rationale): MS-DYN §5.5 uses isotropic quadratic drag with one drag area [P-DYN-100]
  (DD-060, D64); the per-axis form stays documented as the alternative. It acts at the centre of
  gravity.
  Sufficiency (L1-AER-070): L1-AER-070 asks for drag computed from the air-relative velocity and
  the standard-atmosphere density. This record ties the drag to both; L2-AER-DYN-140 defines the
  air-relative velocity with the wind of each step and L2-AER-DYN-410 holds that wind over the
  step; L2-AER-DYN-150 the density; L2-AER-DYN-610 is the terminal-velocity check, with and
  without wind, that L1-AER-070 asks for.
Parent(s):     L1-AER-070
Source:        D17, D20, D51; MS-DYN §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-130; success criteria: for air-relative velocities along each body
  axis and oblique to them, at several attitudes and at altitudes across the range of the
  atmosphere model, the drag force the model computes equals the MS-DYN drag formula evaluated
  independently, to floating-point rounding.
Parameters:    P-DYN-100
TBD/TBR:       P-DYN-100 value TBR (TT-750), Martin, G2 (I1)
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
  the MS-DYN wind model; the TST applies only winds inside it. The test of the air-relative velocity
  starts the fall with the horizontal velocity of the wind (check C-2), because a fall from rest
  relative to the ground does not settle to the wind within the band of the check (G2-F02); a drag
  computed on the ground velocity would then fail both the horizontal and the vertical part.
  Sufficiency (L1-AER-070): see L2-AER-DYN-130. Sufficiency (L1-AER-670): see L2-AER-DYN-400.
Parent(s):     L1-AER-070, L1-AER-670
Source:        CV-470; I-25; MS-DYN §5.4, §11 (C-2)
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-140; success criteria: (1) in check C-2 of MS-DYN in a steady wind of
  [P-SYS-430], at each step of the checked band, the horizontal velocity differs from the wind
  velocity by at most [P-DYN-210] of the wind speed; (2) with zero fuel and drag on, and a wind
  that changes at one step command, the drag force recovered from the per-step records (vehicle
  mass times the vehicle acceleration minus the gravity force) first changes at the step that
  this command produces, and not at an earlier one.
Parameters:    P-DYN-210, P-SYS-430
TBD/TBR:       P-DYN-210 value TBR (TT-760), P-SYS-430 value TBR (TT-030), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-150

```req
ID:            L2-AER-DYN-150
Level:         L2
Type:          Model fidelity
Statement:     The dynamics model shall compute the air density at the vehicle altitude by the
  atmosphere model of MS-DYN.
Rationale:     The density follows the standard atmosphere (D20) and depends on altitude only
  (L0-ASM-060). MS-DYN names it: the U.S. Standard Atmosphere, 1976, with the geopotential altitude
  taken equal to the altitude (DD-090). Its seven layers are used up to the top of the standard's
  lower atmosphere, layer 0 is continued below the datum plane, and the density is zero above the
  top, so that the density is defined at every altitude an integrator can evaluate (DD-210; G2-F08). Its constants are constants of the named standard, not parameters. The check
  reads the standard by geopotential altitude, because the published table is indexed by geometric
  altitude and would fail a correct model by up to 4.8·10⁻² at 47 km (G2-F07).
  Sufficiency (L1-AER-070): see L2-AER-DYN-130.
Parent(s):     L1-AER-070
Source:        D20; L0-ASM-060; DD-090; MS-DYN §5.3, §11 (C-7)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-150; success criteria: (1) check C-7 of MS-DYN: at the base
  altitude and at the midpoint of each layer of the atmosphere model, and at its top, the computed
  density differs from the density of the standard computed independently at the geopotential
  altitude equal to the altitude by at most [P-DYN-260] of that value; (2) the computed density is
  the layer-0 value at altitudes below the datum plane and zero at and above the top of the model.
Parameters:    P-DYN-260
TBD/TBR:       P-DYN-260 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-160

```req
ID:            L2-AER-DYN-160
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall compute no aerodynamic force other than the drag force of
  the drag model.
Rationale:     Lift would couple attitude and translation (L1-AER-030 rationale). "Shall compute no"
  is a true prohibition (METHODOLOGY §8.4 rule 11). Under the drag form the owner chose (MS-DYN
  §5.5, option D1, D64) the drag force is opposite to the air-relative velocity, so no part of it
  is perpendicular to the flow.
  Sufficiency (L1-AER-030): the dynamics model is the only place an aerodynamic force can arise
  (L1-AER-030 rationale), so this record satisfies the inspection L1-AER-030 asks for.
Parent(s):     L1-AER-030
Source:        L0-CON-040; MS-DYN §5.1, §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-160; success criteria: MS-DYN and the implementation define no
  aerodynamic force other than the drag force of the drag model, and that force has no component
  perpendicular to the air-relative velocity.
Parameters:    —
TBD/TBR:       —
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
  L1-AER-080). EF computes the resultant once from its effector outputs through their control
  effectiveness (L1-AER-100; DD-190, D73) and gives one force and one moment per step (I-02,
  MS-DYN §7.1); DYN holds them over the step (MS-DYN §10.2). With the effectors off on the ground,
  and at fuel exhaustion, EF gives zero (L1-AER-930, -200). The interface is internal to the
  vehicle model.
  Sufficiency (L1-AER-050): see L2-AER-DYN-100.
Parent(s):     L1-AER-050
Source:        I-02; MS-DYN §7.1, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-180; success criteria: the only input of the equations of motion
  and of the ground reaction that carries a control force or a control moment is the EF output of
  MS-DYN §7.1, resolved in the body frame and about the centre of gravity.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-190

```req
ID:            L2-AER-DYN-190
Level:         L2
Type:          Constraint
Statement:     While the air-relative velocity lies along one body axis, the dynamics model shall
  compute a drag force along that body axis only.
Rationale:     The DYN share of D18 for the drag: a translation along one axis does not cause an
  acceleration along another. The isotropic drag of MS-DYN §5.5 (D64) meets it, as the per-axis
  alternative would. For an oblique flow the drag along each axis shares the airspeed magnitude;
  the owner accepts that as meeting D18 (D72), and MS-DYN §4.5 records it (G2-F06), so this record
  states the single-axis property only.
  Sufficiency (L1-AER-020): see L2-AER-DYN-050.
Parent(s):     L1-AER-020
Source:        D18, D72; MS-DYN §4.5, §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-190; success criteria: for an air-relative velocity along each of
  the six body axis directions, at several attitudes and altitudes, the drag components along the
  other two body axes are zero to floating-point rounding.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
Statement:     The dynamics model shall take the vehicle mass and the inertia tensor of each
  simulation step from FU.
Rationale:     FU owns the mass properties (FUNCTIONAL_ANALYSIS §6.1, I-04). DYN keeps no mass or
  inertia value of its own, so the mass decrease and any change of inertia with fuel reach the
  dynamics. The inertia tensor is diagonal, its three principal moments about the body axes (D61,
  CV-350). The values are held over the step (MS-DYN §10.2). The centre of gravity is the body
  origin at every fuel state (L2-AER-DYN-200, FU child), so its position does not cross this
  interface. This is the resolution recommended by G2-F05 and aligned in FUNCTIONAL_ANALYSIS I-04
  by CR-B3-39; one name, "inertia tensor", is used on both sides (IN-C1-01).
  Sufficiency (L1-AER-180): see L2-AER-DYN-030. Sufficiency (L1-AER-220): see L2-AER-DYN-040.
Parent(s):     L1-AER-180, L1-AER-220
Source:        I-04; MS-DYN §6, §10.2; G2-F05
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-210; success criteria: the equations of motion use the vehicle
  mass and the three principal moments of the inertia tensor that FU provides for the step, and
  the dynamics model holds no mass or inertia constant of its own.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
  axes (D61). The owner accepted the capsule (D64); the shape stays provisional until
  2026-11-30 (L0-CON-140). The same shape gives the lowest point of the body for the height above
  the ground (CV-400) and the ground contact (MS-DYN §2.6); the landing gear is not part of it
  (L2-AER-DYN-250).
  Sufficiency (L1-AER-220): see L2-AER-DYN-040.
Parent(s):     L1-AER-220
Source:        L0-CON-140; AIRCRAFT_CHARACTERISTICS.md §1; MS-DYN §2.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-220; success criteria: MS-DYN states the capsule, its axis
  along the body x axis, its centre at the centre of gravity and its dimensions as [P-DYN-020] and
  [P-DYN-030], and [P-DYN-020] is at least [P-DYN-030] in the parameter database.
Parameters:    P-DYN-020, P-DYN-030
TBD/TBR:       Body shape provisional (L0-CON-140), Martin, 2026-11-30; P-DYN-020 and
  P-DYN-030 values TBR (TT-740), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       2
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
TBD/TBR:       P-DYN-400 value TBR (TT-140), Martin, G2; P-DYN-020 and P-DYN-030 values TBR
  (TT-740), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-250

```req
ID:            L2-AER-DYN-250
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall place the contact points of the landing gear at the
  body-frame positions of the vehicle geometry of MS-DYN, [P-DYN-040] below the lowest point of the
  body shape at level attitude when the gear is extended and inside the body shape when it is
  retracted.
Rationale:     L1-AER-900: the gear contact points of the extended gear lie [P-DYN-040] below the
  lowest point of the body at level attitude, and the retracted gear has no part below the body.
  MS-DYN §2.5 fixes four contact points under the cylindrical part of the capsule, a C1 geometry
  choice (DD-220), with the positions in transit between the two. On the ground at
  level attitude the centre of gravity is then at [P-DYN-030]/2 plus [P-DYN-040], the rest
  altitude, and the height above the ground is [P-DYN-040] (CV-400). The record is one geometry
  with its two end positions (D30).
  Sufficiency (L1-AER-900): L1-AER-900 asks the children to show that the MS-DYN vehicle geometry
  states the contact points of the extended gear and places the retracted gear inside the body,
  and that the gear position has no effect on the mass properties or the drag. This record gives
  the geometry; L2-AER-DYN-260 and the FU child give the absence of any other effect. The contact
  itself is detected at these points (L2-AER-DYN-500).
Parent(s):     L1-AER-900
Source:        D69; L1-AER-900; MS-DYN §2.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-250; success criteria: MS-DYN states the contact points of the
  landing gear as body-frame positions in terms of [P-DYN-020], [P-DYN-030] and [P-DYN-040], with
  the extended points [P-DYN-040] below the lowest point of the capsule at level attitude and the
  retracted points inside the capsule, and the implementation uses those positions.
Parameters:    P-DYN-040, P-DYN-020, P-DYN-030
TBD/TBR:       P-DYN-040 value TBR (TT-830), Martin, G2; P-DYN-020 and P-DYN-030 values TBR
  (TT-740), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-260

```req
ID:            L2-AER-DYN-260
Level:         L2
Type:          Constraint
Statement:     The dynamics model shall make no drag force, no moment and no mass property depend
  on the gear position.
Rationale:     The gear is ideal (L0-ASM-110 as revised by CR-B3-07): it has no mass, inertia or
  drag of its own, and its position changes no mass property and no drag (L1-AER-900). This keeps
  the centre of gravity fixed (L0-CON-130) and the single drag area of D64. The only force the gear
  carries is the ground reaction on the ground, where the gear is always extended (L2-AER-DYN-280),
  so the ground reaction does not depend on the gear position either. The mass properties come from
  FU (L2-AER-DYN-210), whose child excludes the gear from the mass distribution.
  Sufficiency (L1-AER-900): see L2-AER-DYN-250.
Parent(s):     L1-AER-900
Source:        D69; L0-ASM-110; L1-AER-900; MS-DYN §2.5, §5.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-260; success criteria: in two airborne runs that differ only in the
  gear position, extended throughout in one and retracted throughout in the other, with the same
  initial state, inputs and wind, the vehicle states and the mass properties used are the same at
  each step up to the first contact step of either run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-270

```req
ID:            L2-AER-DYN-270
Level:         L2
Type:          Functional
Statement:     While the vehicle is airborne, when the landing gear command changes, the dynamics
  model shall bring the landing gear to the commanded position within [P-DYN-050], by the landing
  gear model of MS-DYN.
Rationale:     L1-AER-910: Takeoff retracts the gear at the hover height and Land extends it before
  the descent (D69). The MS-DYN landing gear model moves the gear at a constant rate, one full
  travel in [P-DYN-050] (DD-220), with the gear position in transit meanwhile, so the
  transit is observable (L2-AER-DYN-290). A reversal in transit returns from where the gear is, so
  it takes less time. A command given on the ground takes effect from the first airborne step,
  because the gear is held extended on the ground (L2-AER-DYN-280). The time is counted in
  simulation steps, so the gear reaches the position within one step of [P-DYN-050].
  Sufficiency (L1-AER-910): L1-AER-910 asks DYN and AF to show that after each change of the gear
  command in flight the gear state shows the gear in transit and then in the commanded position
  within [P-DYN-050]. DYN moves the gear (this record), takes the command from AF
  (L2-AER-DYN-360), reports the gear position (L2-AER-DYN-290) and holds it extended on the ground
  (L2-AER-DYN-280); AF issues the command in Takeoff and Land (AF child).
Parent(s):     L1-AER-910
Source:        D69; L1-AER-910; MS-DYN §9.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-270; success criteria: while airborne, for a change of the command from
  retracted to extended, from extended to retracted, and for a reversal half way through a
  transit, the gear position is in transit from the step after the change, and it is the commanded
  position at the step [P-DYN-050] after the change, to within one simulation step, or sooner for
  the reversal.
Parameters:    P-DYN-050
TBD/TBR:       P-DYN-050 value TBR (TT-850), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-280

```req
ID:            L2-AER-DYN-280
Level:         L2
Type:          Functional
Statement:     While the vehicle is on the ground, the dynamics model shall hold the landing gear
  extended.
Rationale:     The vehicle rests on its extended gear (L1-AER-920), and a retraction on the ground
  would drop the body onto the ground, so the gear does not respond to a retraction command there
  (L1-AER-910 rationale). The gear is extended at the contact step of every landing (a landing
  needs it, L2-AER-DYN-510) and at the start of a run on the ground (L2-AER-DYN-450), so holding it
  is enough. After the liftoff the gear follows its command again (L2-AER-DYN-270).
  Sufficiency (L1-AER-910): see L2-AER-DYN-270. Sufficiency (L1-AER-920): see L2-AER-DYN-570.
Parent(s):     L1-AER-910, L1-AER-920
Source:        D69; L1-AER-910, -920; MS-DYN §9.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-280; success criteria: after a landing and in a start on the ground,
  with the landing gear command set to retracted, the gear position is extended at each step on the
  ground, and it is in transit from the first airborne step after the liftoff.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-290

```req
ID:            L2-AER-DYN-290
Level:         L2
Type:          Functional
Statement:     The dynamics model shall determine, at each simulation step, a gear state made of the
  gear position, as extended, retracted or in transit, and whether the vehicle is on the ground.
Rationale:     The gear state is the perfect-knowledge counterpart of a weight-on-gear signal
  (L0-ASM-010, L1-AER-430 as revised by CR-B3-19): autoflight needs the gear position to descend
  only with the gear extended and to switch the effectors off after a landing (C5), the crew sees
  the gear position (L1-AER-470 as revised), and the TST assesses the takeoffs, landings and rests
  from it (L1-AER-640 as revised). "On the ground" holds from the start of a run on the ground or
  the contact step of a landing to the liftoff step (MS-DYN §3.3, §9.2). It is a DYN item separate
  from the vehicle state (glossary *Gear state*).
  Sufficiency (L1-AER-910): see L2-AER-DYN-270. Sufficiency (L1-AER-430): see L2-AER-DYN-320.
  Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-910, L1-AER-430, L1-AER-640
Source:        D69; L1-AER-430, -640, -910; MS-DYN §3.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-290; success criteria: in a run of the takeoff and landing scenario
  SC-130 and in the tests of L2-AER-DYN-270, the gear state of each step reports the gear position
  of the MS-DYN landing gear model, and reports the vehicle on the ground exactly from the start of
  the run or the contact step of the landing to the liftoff step.
Parameters:    —
TBD/TBR:       —
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
  the centre of gravity as the sum of the control force, the drag force and the ground reaction
  divided by the vehicle mass, resolved in the body frame.
Rationale:     The crew limit is on the sensed acceleration, evaluated at the centre of gravity
  (D38, D45). DYN computes it from its definition (glossary as revised by CR-B3-37; MS-DYN §8), so
  that the limit FC enforces can be measured in every run. The ground reaction is zero while
  airborne. The instant at which it is evaluated is MS-DYN §3.4 (DD-080 with DD-250): the inputs
  of the step that produced the state, and at a contact step the propagated state. With the
  rotation-during-translation term retained (D64) it equals the vehicle acceleration minus gravity,
  resolved in the body frame. At rest on the ground it is [P-DYN-010] upward (L1-AER-920).
  Sufficiency (L1-AER-290): FC limits the resultant control force at the current mass, AF limits
  the manoeuvres and FU supplies the mass (their children). DYN's share is the measured quantity
  (this record), the gravity that the budget counts as [P-DYN-010] (L2-AER-DYN-120), and no shock
  at a landing: the arrest on the ideal gear is reported as a state, not as an acceleration
  (L2-AER-DYN-560). With these, L1-AER-290 can be assessed in every automated test run.
  Sufficiency (L1-AER-920): see L2-AER-DYN-570. Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-290, L1-AER-920, L1-AER-640
Source:        D38, D45, D69; MS-DYN §3.4, §8
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-300; success criteria: (1) in check C-1 the sensed acceleration is
  zero at each step; (2) with DYN driven by a prescribed control force of the vehicle mass times
  [P-DYN-010] along the negative body z axis, airborne at level attitude, zero velocity and in still
  air, the sensed acceleration magnitude is [P-DYN-010] and the vehicle acceleration is zero;
  (3) in check C-9 (a), at each step on the ground, the sensed acceleration magnitude is
  [P-DYN-010], directed up; (4) airborne with drag and a control force, the recorded sensed
  acceleration of each step equals the control force plus the drag divided by the mass computed
  independently with the control force, the vehicle mass and the wind of the previous step, from
  the per-step records of the vehicle-model interfaces (G2-F12); (5) at each contact step, the
  recorded value equals that of the propagated state. Each to floating-point rounding.
Parameters:    P-DYN-010
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
  on the inputs; MS-DYN §3.4 fixes the instant at which it is evaluated (DD-080): the inputs of the
  step that produced the state. On the ground the total force includes the ground reaction, so
  the vehicle acceleration is zero; at a contact step it is the value of the propagated state,
  because the arrest on the ideal gear computes no shock (DD-250; D53). The inputs of
  the previous step are not in the operational data, so the analysis uses per-step records of the
  vehicle-model interfaces (G2-F12, IN-C1-26).
  Sufficiency (L1-AER-640): see L2-AER-DYN-350.
Parent(s):     L1-AER-640
Source:        Glossary *Vehicle acceleration*; MS-DYN §3.2, §3.4, §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-310; success criteria: at each step of a run of the reference
  mission, the recorded vehicle acceleration equals the MS-DYN translational equation evaluated
  independently from the recorded state and the control force, the vehicle mass and the wind of
  the previous step, from the per-step records of the vehicle-model interfaces, at the instant of
  MS-DYN §3.4, to floating-point rounding; it is zero at each step on the ground; in check C-1 it
  equals the gravitational acceleration.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-320

```req
ID:            L2-AER-DYN-320
Level:         L2
Type:          Interface
Statement:     The dynamics model shall provide the vehicle state and the gear state of each
  simulation step at the vehicle-model boundary, as the vehicle-model boundary ICD defines it.
Rationale:     A fixed boundary lets the control law and the autoflight be replaced without
  touching the vehicle model (L0-CON-200, -210). The state carries the frames and units of
  CONVENTIONS and the quaternion attitude (IN-B1-01). The gear state goes to autoflight, which
  commands the gear and needs to know when the vehicle is on the ground (L1-AER-430 as revised by
  CR-B3-19). The ICD home is decided at I1 (TT-720).
  Sufficiency (L1-AER-430): L1-AER-430 closes the boundary to effector commands and the landing
  gear command in, and the vehicle state, gear state, mass properties and fuel state out. DYN's
  part is the vehicle state and the gear state out (this record, with L2-AER-DYN-290), nothing else
  out (L2-AER-DYN-340), and the landing gear command in (L2-AER-DYN-360). The effector commands go
  to EF; the mass properties and the fuel state are FU's.
Parent(s):     L1-AER-430
Source:        IN-B1-01; I-07, I-09, I-10, I-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-320; success criteria: each element of the vehicle state and of
  the gear state that DYN provides is defined in the vehicle-model boundary ICD with its frame and
  SI unit, or its set of values.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
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
  vehicle state and the gear state.
Rationale:     The boundary list of L1-AER-430 is closed. In particular the wind, which DYN
  receives with each step, does not reach the flight software (L1-AER-670 rationale), and the
  sensed acceleration, the ground reaction and the landing and crash events go to TM and the TST,
  not to the flight software. Autoflight learns of a landing from the gear state (on the ground).
  Sufficiency (L1-AER-430): see L2-AER-DYN-320.
Parent(s):     L1-AER-430
Source:        L1-AER-670 rationale; FUNCTIONAL_ANALYSIS §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-340; success criteria: the only DYN outputs that a flight
  software function reads are the vehicle state and the gear state of the vehicle-model boundary
  ICD.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-350

```req
ID:            L2-AER-DYN-350
Level:         L2
Type:          Interface
Statement:     The dynamics model shall provide to the operational data output, at each simulation
  step, its vehicle state, its gear state and its sensed acceleration at the centre of gravity.
Rationale:     Vehicle responses are one of the things the operational data relate (L0-OBJ-140),
  and the TST measures the performance records from them (L1-AER-290, -300, -460, -920 to -970).
  DYN gives the values of every step; TM records them at each output sample.
  Sufficiency (L1-AER-640): L1-AER-640 (as revised by CR-B3-25) records the vehicle state, the
  navigation quantities with the height above the ground, the sensed acceleration, the masses, the
  gear state and the landing and crash events. DYN provides the vehicle state (with the Euler
  angles of L2-AER-DYN-070 and the vehicle acceleration of -310), the gear state (-290) and the
  sensed acceleration (this record, with -300), and the landing and crash events (-530); NAV
  provides the navigation quantities, the height above the ground included, and FU the masses; TM
  records them. Together they cover the list.
Parent(s):     L1-AER-640
Source:        N-250, N-340; I-32, I-37, I-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-350; success criteria: at each output sample of a run of the
  reference mission, the operational data hold the DYN vehicle state, gear state and sensed
  acceleration of that sample's step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-360

```req
ID:            L2-AER-DYN-360
Level:         L2
Type:          Interface
Statement:     The dynamics model shall take the landing gear command from autoflight at the
  vehicle-model boundary, as the vehicle-model boundary ICD defines it.
Rationale:     The landing gear is part of the vehicle model, and autoflight commands it, retracting
  it in Takeoff and extending it in Land (L1-AER-430 as revised by CR-B3-19, L1-AER-910;
  FUNCTIONAL_ANALYSIS I-43). The command is issued once per control frame and held over the steps
  of the frame, like the effector commands (MS-DYN §9.1, §10.2). Before the first command of a run
  the commanded position is the gear position of the initial condition. No other flight software
  data reaches DYN.
  Sufficiency (L1-AER-430): see L2-AER-DYN-320. Sufficiency (L1-AER-910): see L2-AER-DYN-270.
Parent(s):     L1-AER-430, L1-AER-910
Source:        D69; I-43; MS-DYN §9.1, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-360; success criteria: the only input that moves the landing gear
  is the landing gear command of the vehicle-model boundary ICD, held over the steps of its control
  frame, and DYN reads no other flight software data.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-370

```req
ID:            L2-AER-DYN-370
Level:         L2
Type:          Interface
Statement:     The dynamics model shall take the fuel availability of each simulation step from FU.
Rationale:     A ground contact at fuel exhaustion is a crash whatever the speeds (D68, D73 B3-3;
  L1-AER-260 and -270 as revised by CR-B3-12, -13), so the classification needs to know whether
  fuel remains. FU gives the fuel availability of each step (glossary; DD-130), and
  FUNCTIONAL_ANALYSIS I-03 now carries it to the ground contact function F-AER-12 as well as to EF
  (CR-B3-39). The classification at a contact step uses the availability of that step (MS-DYN
  §9.4, §10.2). DYN uses no other fuel quantity.
  Sufficiency (L1-AER-260, L1-AER-270): see L2-AER-DYN-500.
Parent(s):     L1-AER-260, L1-AER-270
Source:        D68; I-03; MS-DYN §7.2, §9.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-370; success criteria: the contact classification uses the fuel
  availability that FU gives for the contact step, and the dynamics model uses no other fuel
  quantity.
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
  MS-DYN §11 a known input (MS-DYN §10.2, DD-100). The gusts of the wind envelope build up over at
  least [P-SYS-570], so a hold over one step of [P-SYS-300] is a small discretisation of a smooth
  wind (MS-DYN §5.4).
  Sufficiency (L1-AER-670): see L2-AER-DYN-400. Sufficiency (L1-AER-070): see L2-AER-DYN-130.
Parent(s):     L1-AER-670, L1-AER-070
Source:        D62; DD-100; MS-DYN §5.4, §10.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-410; success criteria: the implementation uses the wind of the
  command for a step at each evaluation within that step, and no other wind value.
Parameters:    P-SYS-570, P-SYS-300
TBD/TBR:       P-SYS-570 value TBR (TT-650), Martin, G2; P-SYS-300 value TBR (TT-070), Martin, G2
  (I1)
Owner:         Martin
Status:        Draft
Version:       2
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
  properties, the fuel availability, the landing gear command and the wind (MS-DYN §10.2). The
  gear state and the on-ground state are part of what the previous step determines.
  Sufficiency (L1-AER-690): the TST inputs (step commands and wind) are part of the run's
  condition (L1-AER-690 rationale); with them fixed, this record makes the DYN contribution to
  the operational data the same from run to run, which is DYN's share of the same verdicts.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59; MS-DYN §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-420; success criteria: repeated executions of the same run, on
  separate simulation instances, give the same verdict for each success criterion of the DYN
  records and vehicle states and gear states that agree within the tolerances of those criteria
  (D59, D63).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-430

```req
ID:            L2-AER-DYN-430
Level:         L2
Type:          Interface
Statement:     When a run starts with the landing gear retracted, the dynamics model shall set the
  vehicle state of step zero to the position, the velocity, the attitude and the body rates of the
  initial condition that the TST gives.
Rationale:     A run may start airborne only for test runs and credibility checks (D73, B3-1;
  L1-AER-660 as revised by CR-B3-26). An airborne start has the gear retracted (CONOPS §5 as revised
  by CR-B3-33), so the gear position of the initial condition marks the kind of start (DD-230). The list is the kinematic part of the initial condition; the fuel mass is FU's, the
  mode state and targets are AF's and FCP's. The attitude is given as a unit quaternion (IN-C1-21).
  A start on the ground is L2-AER-DYN-450.
  Sufficiency (L1-AER-660): DYN takes the position, velocity, attitude, body rates and landing gear
  position of the initial condition: an airborne start (this record), a start on the ground
  (L2-AER-DYN-450), and an airborne start with the body at or below the ground rejected
  (L2-AER-DYN-470). FU, AF and FCP take the rest (their children). Together the initial condition
  of L1-AER-660 is accepted in full, for a ground start and for an airborne start.
Parent(s):     L1-AER-660
Source:        N-310; CONOPS §4.6, §5; D73; MS-DYN §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-430; success criteria: for several airborne initial conditions with the
  landing gear retracted, the first output sample reports the given position, velocity and body
  rates, the given attitude (the same rotation, with the quaternion sign of CV-250), the gear
  retracted and the vehicle not on the ground.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
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
  and the credibility checks can run the vacuum-equivalent configuration and the gravity-free check
  configuration (MS-DYN §5.2, §5.5, §11; D72). The constants of the standard atmosphere are not
  parameters (MS-DYN §5.3).
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        F-AER-14; N-020, N-350; D72; MS-DYN §12
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-DYN-440; success criteria: two runs that differ only in the
  value of [P-DYN-100], one of them zero, and a run with [P-DYN-010] set to zero, run with no
  software change and show the free fall of check C-1, the drag behaviour of check C-2 and the
  gravity-free motion of check C-5.
Parameters:    P-DYN-100, P-DYN-010
TBD/TBR:       P-DYN-100 value TBR (TT-750), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-450

```req
ID:            L2-AER-DYN-450
Level:         L2
Type:          Functional
Statement:     When a run starts with the landing gear extended, the dynamics model shall set the
  vehicle state of step zero to the rest state at the horizontal position and the heading of the
  initial condition, with the vehicle on the ground.
Rationale:     D69: runs start on the ground, on the extended gear, with the effectors off. An
  initial condition with the gear extended is a start on the ground (DD-230), since an
  airborne start has the gear retracted (L2-AER-DYN-430). The rest state of the MS-DYN ground
  contact model is the centre of gravity at the rest altitude, [P-DYN-030]/2 plus [P-DYN-040], over
  the given horizontal position, zero velocity and body rates, and level attitude at the given
  heading (L1-AER-950). The altitude of the initial condition is replaced by the rest altitude;
  whether ICD-AER-TST carries it for a ground start is for I1 (IN-C1-21). The effectors off are
  EF, FC and AF's (L1-AER-930).
  Sufficiency (L1-AER-950): L1-AER-950 asks the children to show that the first output sample of a
  ground start reports the given horizontal position and heading, the altitude [P-DYN-030]/2 plus
  [P-DYN-040], zero velocity and body rates, level attitude, the gear extended with the vehicle on
  the ground, and zero effector output. DYN sets the rest state and the gear state (this record),
  and rejects an inconsistent ground initial condition (L2-AER-DYN-460); AF and FC give the
  effectors-off reference and the zero commands (their children), so EF produces nothing.
  Sufficiency (L1-AER-660): see L2-AER-DYN-430.
Parent(s):     L1-AER-950, L1-AER-660
Source:        D69; L1-AER-950; MS-DYN §9.6, §9.9, §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-450; success criteria: for starts on the ground at several horizontal
  positions and headings, the first output sample reports the given horizontal position and
  heading, the altitude [P-DYN-030]/2 plus [P-DYN-040], zero velocity and body rates, zero pitch
  and roll angles, the gear extended and the vehicle on the ground.
Parameters:    P-DYN-030, P-DYN-040
TBD/TBR:       P-DYN-030 value TBR (TT-740), Martin, 2026-11-30; P-DYN-040 value TBR (TT-830),
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-460

```req
ID:            L2-AER-DYN-460
Level:         L2
Type:          Functional
Statement:     When a run starts with the landing gear extended and a non-zero velocity, non-zero
  body rates or a non-zero pitch or roll angle in the initial condition, the dynamics model shall
  raise an initial-condition error naming each such item.
Rationale:     L1-AER-950 rationale: an initial condition on the ground with any other velocity,
  body rates or attitude than those of the rest state is rejected with an initial-condition error.
  A non-zero value of these items shows an error in the test procedure, which a silent replacement
  would hide (as DD-140 does for the fuel). The altitude is not checked here: the rest altitude
  replaces it (L2-AER-DYN-450). The items form one consistency condition of one initial condition
  (D30). The run does not start (glossary *Initial-condition error*).
  Sufficiency (L1-AER-950): see L2-AER-DYN-450.
Parent(s):     L1-AER-950
Source:        D69; L1-AER-950 rationale; IN-C2-31; MS-DYN §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-460; success criteria: initial conditions with the gear extended and,
  one at a time, a non-zero velocity component, a non-zero body rate, a non-zero pitch angle and a
  non-zero roll angle each give one initial-condition error naming that item, and the dynamics
  model produces no vehicle state for that run; a consistent ground initial condition gives
  none.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-470

```req
ID:            L2-AER-DYN-470
Level:         L2
Type:          Functional
Statement:     When a run starts with the landing gear retracted and a height above the ground of
  at most zero, the dynamics model shall raise an initial-condition error naming the altitude.
Rationale:     No point of the vehicle is below the datum plane in a run (CV-420 as revised by
  CR-B3-36), and an airborne start must be airborne. With the gear retracted the body is the lowest
  point of the vehicle, so its clearance is the height above the ground of CV-400 (MS-DYN §2.6).
  Without this check the first step would detect a contact at once, which would not be the test
  the procedure intended.
  Sufficiency (L1-AER-660): see L2-AER-DYN-430.
Parent(s):     L1-AER-660
Source:        CV-400, CV-420; MS-DYN §2.6, §10.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-470; success criteria: airborne initial conditions with the gear
  retracted and a height above the ground of zero and below zero, at level attitude and at a
  non-zero pitch angle, each give one initial-condition error naming the altitude; a height above
  the ground just above zero gives none.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-500

```req
ID:            L2-AER-DYN-500
Level:         L2
Type:          Functional
Statement:     While the vehicle is airborne, when the lowest point of the vehicle reaches the datum
  plane, the dynamics model shall raise one ground-contact event at that simulation step.
Rationale:     Ground contact is contact of the lowest point of the vehicle with the datum plane
  while airborne: the contact points of the extended gear, or the body when the gear is not
  extended (glossary *Ground contact* and *Contact step* as revised by CR-B3-37; CV-400, CV-420).
  "Reaches" is the first step at which the propagated altitude of that point is at most zero
  (CV-940). That step is the contact step, the "contact sample" of L1-AER-280. There is no
  detection on the ground or after a crash; after a liftoff the detection resumes, so a run can
  have several landings (MS-DYN §9.2, §9.3).
  Sufficiency (L1-AER-260, L1-AER-270): these records ask for a landing or a crash to be reported
  at contact, and for the run to go on after a landing. DYN detects the contact (this record),
  takes the fuel availability (L2-AER-DYN-370), classifies the contact (L2-AER-DYN-510, -520),
  outputs one event record (-530), brings the vehicle to rest after a landing (-560) and reports
  and holds the state after a crash (-540, -550); TM records the event in the operational data.
  Together they give one correctly classified event at each contact step.
  Sufficiency (L1-AER-280): see L2-AER-DYN-510.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-280
Source:        D8, D37, D69; CV-400, CV-420, CV-940; MS-DYN §2.6, §9.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-500; success criteria: in descents to the ground at several vertical
  and horizontal speeds, with the gear extended, retracted and in transit, and at level attitude
  and at a non-zero pitch angle, the model raises exactly one ground-contact event, at the first
  step at which the propagated lowest point of the vehicle is at or below the datum plane, and
  none at an earlier step; it raises none while the vehicle is on the ground, and it raises one at
  the next landing after a liftoff.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-510

```req
ID:            L2-AER-DYN-510
Level:         L2
Type:          Functional
Statement:     When the dynamics model raises a ground-contact event at a simulation step at which
  the landing gear is extended, a contact point of the gear is the lowest point of the vehicle,
  fuel is available, the vertical speed magnitude is at most [P-SYS-500] and the horizontal speed
  is at most [P-SYS-510], the dynamics model shall classify the contact as a landing.
Rationale:     Ideal landing on the ideal gear (D37 as revised by D69, L0-CON-290, L1-AER-260 as
  revised by CR-B3-12): a contact on the extended gear within the envelope, with fuel remaining.
  The envelope is two speed limits at the contact sample, with no acceleration limit (D53); the
  gear position and the fuel are conditions of a landing, not of the envelope (L1-AER-280 as
  revised by CR-B3-14). "A contact point of the gear is the lowest point" makes the contact one on
  the gear, not on the body of a tilted vehicle (MS-DYN §2.6). The conditions are one set, whose
  complement is L2-AER-DYN-520 (D30). The speeds are ground-referenced (CV-480, CV-490) and are
  those of the propagated state of the contact step, not interpolated (MS-DYN §9.4). The limits
  are inclusive (CV-940).
  Sufficiency (L1-AER-280): this record and L2-AER-DYN-520 partition the contacts, with the two
  speed limits at the contact step as the envelope L1-AER-280 states; L2-AER-DYN-500 fixes the
  contact step.
  Sufficiency (L1-AER-260): see L2-AER-DYN-500.
Parent(s):     L1-AER-280, L1-AER-260
Source:        D37, D53, D68, D69; MS-DYN §9.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-510; success criteria: contacts on the extended gear with fuel
  available and the vertical speed magnitude and the horizontal speed each at its limit, and each
  just inside it, at level attitude and at a small pitch angle, are classified as landings.
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (TT-090), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-520

```req
ID:            L2-AER-DYN-520
Level:         L2
Type:          Functional
Statement:     When the dynamics model raises a ground-contact event that it does not classify as a
  landing, the dynamics model shall classify the contact as a crash.
Rationale:     A ground contact that is not a landing is a crash, which ends the run (D37, D68, D69;
  L1-AER-270 as revised by CR-B3-13): a contact outside the speed envelope, with the gear retracted
  or in transit, on the body first, or at fuel exhaustion, whatever the speeds (D73, B3-3). Stating
  it as the complement of L2-AER-DYN-510 leaves no contact unclassified. The reference mission ends
  this way, after fuel exhaustion (SC-110).
  Sufficiency (L1-AER-280): see L2-AER-DYN-510. Sufficiency (L1-AER-270): see L2-AER-DYN-500.
Parent(s):     L1-AER-280, L1-AER-270
Source:        D37, D53, D68, D69, D73; CONOPS SC-110; MS-DYN §9.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-520; success criteria: each of the following is classified as a crash:
  a contact on the extended gear with the vertical speed magnitude just above its limit, and one
  with the horizontal speed just above its limit; a contact with the gear retracted, and one with
  the gear in transit, both within the speed limits; a contact of the body first, with the gear
  extended, at a large pitch angle; a contact on the extended gear within the speed limits with
  fuel not available; and a free fall to the ground from fuel exhaustion.
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (TT-090), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
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
  run on a crash; a landing does not end the run (I-41, CONOPS §4.6 as revised by CR-B3-33). A run
  can therefore hold several landing events and at most one crash event. The timestamp is the step
  index and the simulation time of the contact step (CV-840). An event record is not tied to an
  output sample, so the classification instant is the contact step even when it falls between
  output samples.
  Sufficiency (L1-AER-260, L1-AER-270): see L2-AER-DYN-500. Sufficiency (L1-AER-640): see
  L2-AER-DYN-350.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-640
Source:        I-37, I-41; CV-840
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-530; success criteria: in each contact test of L2-AER-DYN-510 and
  -520, and at each landing of a run of SC-130 with a second takeoff and landing, one event record
  is output per contact, with the expected classification and the step index and simulation time
  of the contact step, in the ICD-AER-TST format.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-540

```req
ID:            L2-AER-DYN-540
Level:         L2
Type:          Functional
Statement:     When the dynamics model classifies a ground contact as a crash, the dynamics model
  shall report the vehicle state of the contact step with its altitude raised so that the lowest
  point of the vehicle lies on the datum plane.
Rationale:     Derived from a design decision: DD-070, as revised for the landing gear by DD-240. With a fixed step the propagated lowest point at the contact step is at or
  slightly below the datum plane. CV-420 (as revised by CR-B3-36) states that no point of the
  vehicle is below the datum plane in a run, so the reported state is raised onto it; the
  horizontal position, the velocity, the attitude and the body rates stay as propagated, and the
  classification uses the propagated state. The alternative, interpolating the state to the
  crossing instant, puts a state off the CV-820 time grid. With the gear, the centre of gravity is
  no longer at altitude zero at contact, so the earlier "altitude of zero" no longer applies; a
  landing reports the rest state instead (L2-AER-DYN-560).
Parent(s):     Derived (DD-240)
Source:        CV-420, CV-820; DD-070, DD-240; MS-DYN §9.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-540; success criteria: in each crash test of L2-AER-DYN-520, the
  reported state of the contact step has its lowest point on the datum plane to floating-point
  rounding, its horizontal position, velocity, attitude and body rates equal the propagated values,
  and no recorded state of the run has a point of the vehicle below the datum plane.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-550

```req
ID:            L2-AER-DYN-550
Level:         L2
Type:          Functional
Statement:     While the dynamics model has classified a ground contact as a crash, the dynamics
  model shall keep the vehicle state of the contact step.
Rationale:     A crash ends the run (L1-AER-270 as revised by CR-B3-13). The TST ends the run on the
  crash event; if it commands a further step, the state does not change, no ground reaction is
  applied and no second event is raised (MS-DYN §9.7). After a landing the vehicle rests on the
  ground instead (L2-AER-DYN-560 to -590), so this hold applies to a crash only.
  Sufficiency (L1-AER-270): see L2-AER-DYN-500.
Parent(s):     L1-AER-270
Source:        D37, D69; L0-ASM-110; MS-DYN §9.7
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-550; success criteria: when further steps are commanded after a
  crash, the vehicle state and the gear state stay those of the contact step and no further
  ground-contact event is raised.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-560

```req
ID:            L2-AER-DYN-560
Level:         L2
Type:          Functional
Statement:     When the dynamics model classifies a ground contact as a landing, the dynamics model
  shall report the vehicle state of the contact step as the rest state at the propagated horizontal
  position and heading of that step.
Rationale:     L1-AER-920: the gear is ideal, so at the contact step of a landing the vehicle comes
  to rest, with no bounce, sliding or tipping and no touchdown shock (D53, D69). The rest state of
  the MS-DYN ground contact model is the centre of gravity at the rest altitude over the given
  horizontal position, zero velocity and body rates, and level attitude at the given heading. The
  propagated horizontal position and heading are kept, so the vehicle does not jump sideways or
  turn at the touchdown (DD-240). The vehicle is on the ground from this step and the
  run goes on (L1-AER-260 as revised). The acceleration quantities of the contact step are those of
  the propagated state (L2-AER-DYN-300, -310), so the arrest itself adds no acceleration.
  Sufficiency (L1-AER-920): see L2-AER-DYN-570. Sufficiency (L1-AER-260): see L2-AER-DYN-500.
  Sufficiency (L1-AER-290): see L2-AER-DYN-300.
Parent(s):     L1-AER-920, L1-AER-260, L1-AER-290
Source:        D53, D69; L0-ASM-110; MS-DYN §9.5, §9.6
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-DYN-560; success criteria: at each landing of a run of SC-130 and in each
  landing test of L2-AER-DYN-510, the reported state of the contact step is the rest state at the
  propagated horizontal position and heading, the gear state reports the vehicle on the ground from
  that step, and the recorded vehicle acceleration and sensed acceleration of that step equal the
  values evaluated from the propagated state.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-570

```req
ID:            L2-AER-DYN-570
Level:         L2
Type:          Model fidelity
Statement:     While the vehicle is on the ground, the dynamics model shall hold the integrated state
  at the rest state of the ground contact model of MS-DYN.
Rationale:     D69 and L1-AER-920: the Aeronef rests on the ground, stable and stationary, whatever
  the wind. With the ideal gear the rest is a static equilibrium, so the state is held, not
  integrated: the position, the level attitude and the heading stay those of the rest state, and
  the velocity and the body rates stay zero (DD-250). Holding the state, rather than
  integrating a zero total force, keeps the rest exact, without a drift from rounding. The hold
  ends at the liftoff step (L2-AER-DYN-590).
  Sufficiency (L1-AER-920): L1-AER-920 asks the children to show, after a landing and in a ground
  start, at each step until liftoff, zero velocity and body rates, level attitude and a constant
  position, in still air and in the strongest wind of the wind envelope; a sensed acceleration
  magnitude of [P-DYN-010]; and a liftoff at the first step at which the upward component of the
  control force exceeds the weight. DYN brings the vehicle to rest at a landing (L2-AER-DYN-560) or
  at the start (L2-AER-DYN-450), holds it (this record) on its extended gear (L2-AER-DYN-280) under
  the ground reaction (L2-AER-DYN-580), with the sensed acceleration of L2-AER-DYN-300, and ends
  the rest at the liftoff (L2-AER-DYN-590). Check C-9 of MS-DYN shows all of it.
Parent(s):     L1-AER-920
Source:        D69; L0-ASM-110; MS-DYN §9.6, §11 (C-9)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-570; success criteria: check C-9 (a) of MS-DYN, in still air and in
  the steady wind of [P-SYS-430] with a gust event of [P-SYS-560], and the rest after each landing
  of a run of SC-130: at each step on the ground the integrated state equals the rest state, and
  the gear state reports the gear extended and the vehicle on the ground.
Parameters:    P-SYS-430, P-SYS-560
TBD/TBR:       P-SYS-430, P-SYS-560 values TBR (TT-030), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-580

```req
ID:            L2-AER-DYN-580
Level:         L2
Type:          Model fidelity
Statement:     While the vehicle is on the ground, the dynamics model shall apply to it the ground
  reaction that the ground contact model of MS-DYN defines.
Rationale:     L1-AER-920 and L1-AER-050 as revised by CR-B3-08: on the ground the ground reaction
  is the force and moment that balance the gravity force, the drag of the wind, and the control
  force and moment, so that the total force and moment are zero and the vehicle stays at rest
  whatever the wind. MS-DYN §9.6 defines it as minus the sum of those forces and minus the control
  moment, over each step on the ground other than the liftoff step, where the ground would have to
  pull. It is not a control force (CR-B3-02). It gives the sensed acceleration at rest, [P-DYN-010]
  upward (L2-AER-DYN-300).
  Sufficiency (L1-AER-920): see L2-AER-DYN-570. Sufficiency (L1-AER-050): see L2-AER-DYN-100.
Parent(s):     L1-AER-920, L1-AER-050
Source:        D69; CR-B3-02, CR-B3-08; MS-DYN §5.1, §9.6, §11 (C-9)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-580; success criteria: check C-9 (a) of MS-DYN, with the per-step
  records of the vehicle-model interfaces: at each step on the ground the ground reaction equals
  minus the sum of the gravity force, the drag of the wind on the vehicle at rest and the control
  force, its moment equals minus the control moment, and the total force and moment are zero, to
  floating-point rounding.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-DYN-590

```req
ID:            L2-AER-DYN-590
Level:         L2
Type:          Functional
Statement:     While the vehicle is on the ground, when the upward component of the control force
  exceeds the vehicle mass times [P-DYN-010], the dynamics model shall propagate the next
  simulation step by the equations of motion with no ground reaction.
Rationale:     L1-AER-920: liftoff comes at the first step at which the upward component of the
  control force exceeds the weight, where the ground would have to pull to hold the vehicle
  (glossary *Liftoff*). The wind is horizontal (D51), so the drag at rest has no vertical component
  and the condition is that of the total force. The condition is evaluated with the control force
  and the mass of the step, the inputs held over the next step (DD-100). That step is the liftoff
  step, the last on the ground; the next one is airborne, and the detection of ground contact and
  the gear movement resume from it (MS-DYN §9.6). At liftoff in a wind the drag of the wind acts at
  once, which L1-AER-960 limits with [P-SYS-580] (TST).
  Sufficiency (L1-AER-920): see L2-AER-DYN-570.
Parent(s):     L1-AER-920
Source:        D69; L1-AER-920; MS-DYN §9.6, §11 (C-9)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-590; success criteria: check C-9 (b) of MS-DYN: the liftoff step is
  the first step at which the prescribed upward control force exceeds the vehicle mass times
  [P-DYN-010], the vehicle stays on the ground at every earlier step, including a step at which the
  force equals that product, and the motion after the liftoff step matches the closed form within
  [P-DYN-200].
Parameters:    P-DYN-010, P-DYN-200
TBD/TBR:       P-DYN-200 value TBR (TT-760), Martin, G2
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
  (L1-AER-200), and with a zero drag area there is no drag, so only gravity acts. The check starts
  airborne with the gear retracted, as credibility checks may (D73, B3-1), and runs to the first
  contact step. The tolerance bounds the numerical error of the integration (MS-DYN §10.3). The
  relative error is defined from step one, against the largest change of the expected value so
  far, so it is defined for every component and every initial state (G2-F14).
  Sufficiency (L1-AER-060): see L2-AER-DYN-120. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-060, L1-AER-010
Source:        N-290; METHODOLOGY §10.3; MS-DYN §11 (C-1)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-600; success criteria: check C-1 from several airborne initial
  states (including non-zero horizontal velocity, an upward vertical velocity and non-zero body
  rates) down to the contact step: the relative errors of the position and of the velocity, as the
  MS-DYN credibility checks define them, are at most [P-DYN-200] at each step from step one.
Parameters:    P-DYN-200, P-DYN-010
TBD/TBR:       P-DYN-200 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
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
  quasi-steady correction of MS-DYN §11. Its neglected higher-order terms grow with altitude, so
  C-2 states its configuration: a release at rest vertically from a fixed altitude, with the
  horizontal velocity of the wind, and a checked band from a fixed altitude down to the contact
  step, inside layer 0 of the atmosphere (G2-F02). With the database values the residual there is
  at most about a third of [P-DYN-210], so a correct model passes. With the vehicle moving with the
  wind the air-relative velocity is vertical, so the wind case has the same expected value, which
  checks the air-relative velocity.
  Sufficiency (L1-AER-070): see L2-AER-DYN-130. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-070, L1-AER-010
Source:        N-290; METHODOLOGY §9.3, §10.3; MS-DYN §11 (C-2)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-610; success criteria: check C-2 of MS-DYN in its configuration,
  in still air and in a steady wind of [P-SYS-430]: at each step from the top of the checked band
  of C-2 down to the contact step, the vertical speed magnitude differs from the expected terminal
  value by at most [P-DYN-210] of that value.
Parameters:    P-DYN-210, P-DYN-100, P-SYS-430
TBD/TBR:       P-DYN-210 value TBR (TT-760), P-DYN-100 value TBR (TT-750), P-SYS-430 value TBR
  (TT-030), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-620

```req
ID:            L2-AER-DYN-620
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero in the gravity-free check configuration, the dynamics
  model shall conserve the angular momentum in the local reference frame and the rotational
  kinetic energy within [P-DYN-220] over [P-DYN-270].
Rationale:     With no control moment, and drag acting at the centre of gravity, the rotation is
  torque-free, so the angular momentum in the inertial frame and the rotational kinetic energy are
  constant (check C-3, METHODOLOGY §10.3). The check exercises the gyroscopic term K-1, which is
  zero in normal operation (MS-DYN §4.5). It runs in the gravity-free check configuration, with
  gravity set to zero in the check's vehicle parameter set, so that no fall and no ground contact
  ends it before the accuracy horizon (D72, G2-F01): a falling vehicle reaches the ground in at
  most a few minutes. No check runs for the duration of a long hold (D72). The body rates are
  bounded by the largest heading rate, so the integrator is checked at rates the vehicle reaches.
  Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-010
Source:        D72; METHODOLOGY §10.3; MS-DYN §5.2, §11 (C-3)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-620; success criteria: check C-3 of MS-DYN in its configuration,
  with body rates non-zero about each body axis and each of magnitude at most [P-SYS-270]: at each
  step over [P-DYN-270], the relative change of the angular momentum magnitude, the change of its
  direction and the relative change of the rotational kinetic energy are each at most [P-DYN-220].
Parameters:    P-DYN-220, P-DYN-270, P-SYS-270
TBD/TBR:       P-DYN-220, P-DYN-270 values TBR (TT-760), Martin, G2; P-SYS-270 value TBR
  (TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
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
  FU's check C-8 (L1-AER-190). The relative error is defined from step one (G2-F14).
  Sufficiency (L1-AER-180): see L2-AER-DYN-030. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-180, L1-AER-010
Source:        L0-ASM-090; METHODOLOGY §10.3; MS-DYN §11 (C-4)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-630; success criteria: check C-4 of MS-DYN: the relative error of
  the north velocity, as the MS-DYN credibility checks define it, is at most [P-DYN-240] at each
  step from step one.
Parameters:    P-DYN-240
TBD/TBR:       P-DYN-240 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-640

```req
ID:            L2-AER-DYN-640
Level:         L2
Type:          Model fidelity
Statement:     While the fuel mass is zero in the gravity-free check configuration and the
  vacuum-equivalent configuration with a non-zero yaw rate, the dynamics model shall match the horizontal velocity of the
  rotation-during-translation check of MS-DYN, with the rotation-during-translation term
  retained, within [P-DYN-250] over [P-DYN-270].
Rationale:     The rotation-during-translation term (K-2) is retained (D64, #81.1). Check C-5
  states the expected horizontal velocity with the term retained: with no force the velocity
  stays fixed in the local reference frame while the body turns, which shows that the model
  contains the term the owner chose. Like C-3 it runs gravity-free, so that no ground contact ends
  it before [P-DYN-270] (D72, G2-F01), and with no drag, so that the speed does not decay. The
  pitch and roll angles start at zero, so they are bounded in absolute terms (G2-F14).
  Sufficiency (L1-AER-020): see L2-AER-DYN-050. Sufficiency (L1-AER-010): see L2-AER-DYN-010.
Parent(s):     L1-AER-020, L1-AER-010
Source:        D18, D64, D72; #81.1; MS-DYN §4.5, §11 (C-5)
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-DYN-640; success criteria: check C-5 of MS-DYN, with an initial
  horizontal speed of at most [P-SYS-230] and a yaw rate of magnitude at most [P-SYS-270]: at each
  step over [P-DYN-270], the horizontal velocity error divided by the initial horizontal speed and
  the yaw rate error divided by the initial yaw rate magnitude are each at most [P-DYN-250], and the
  pitch angle and the roll angle stay within [P-DYN-250] radian of zero.
Parameters:    P-DYN-250, P-DYN-270, P-SYS-230, P-SYS-270
TBD/TBR:       P-DYN-250, P-DYN-270 values TBR (TT-760), Martin, G2; P-SYS-270 value TBR
  (TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-DYN-700

```req
ID:            L2-AER-DYN-700
Level:         L2
Type:          Documentation
Statement:     The dynamics model shall have its model specification MS-DYN baselined with one named
  section for each of the vehicle geometry, the vehicle state, the equations of motion, the
  kinematic terms, the total force and moment, the gravity, atmosphere, wind and drag models, the
  sensed acceleration, the landing gear model, the ground contact model, the simulation step and
  the credibility checks.
Rationale:     L0-OBJ-010 requires the executable model to conform to a baselined model
  specification. The list is the DYN content of MS-DYN; the sections are named because the
  requirements cite them by name (MS-DYN §0).
  Sufficiency (L1-AER-720): L1-AER-720 (as revised by CR-B3-27) asks for a baselined MS-DYN that
  states the equations of motion, the gravity, drag and wind model, the landing gear and ground
  contact model, and the effector, fuel and mass-properties models. DYN writes the first four
  groups (this record). FU and EF write the mass-properties, effector and fuel sections into
  MS-DYN §6 and §7 (their children). Together they give the whole content L1-AER-720 lists.
Parent(s):     L1-AER-720
Source:        N-270; plan §6 C1; TT-660; CR-B3-27
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-DYN-700; success criteria: MS-DYN is baselined at G2, and it has a
  section under each listed name that states that model.
Parameters:    —
TBD/TBR:       MS-DYN not yet baselined (TT-780), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```
