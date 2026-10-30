## AER — Aeronef

The Aeronef system requirements (task B1). The subject of each statement is the Aeronef, treated as a whole. Modes, mode groups, combinations and mode logic are defined at L2 (AF, D33); these records state only the aircraft-level guidance capability. There is one Aeronef configuration (D42). The functions, the N² matrix, the logical architecture, the allocation to the L2 subsystems and the budgets are in [specs/FUNCTIONAL_ANALYSIS.md](../specs/FUNCTIONAL_ANALYSIS.md).

**Verification.** A record allocated to L2 subsystems is verified by roll-up (D40): it passes when each of its children has passed and the decomposition has been reviewed. Its rationale says what the children must show. A record with `Allocated to: —` is a leaf at L1 and is verified directly by its own method.

### L1-AER-010

```req
ID:            L1-AER-010
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute its motion as a rigid body with six degrees of freedom in
  accordance with the model specification MS-DYN.
Rationale:     For a simulated vehicle the physics is the requirement (METHODOLOGY §7). The model
  specification holds the equations of motion so that this record can point to them (INCOSE
  R23). Structural flexibility and fuel slosh are excluded (L0-ASM-080). The local reference
  frame is inertial (L0-ASM-030, CV-140). Children must show (D40): (Analysis) the simulated
  motion matches independent solutions for free fall, free fall with drag to terminal velocity
  and torque-free rotation (METHODOLOGY §10.3, N-290).
  Sufficiency: with L1-AER-050 to -070 (external forces) and L1-AER-180, -220 (mass and
  inertia), this record makes the executable model conform to MS-DYN (L0-OBJ-010) and fixes six
  rigid-body degrees of freedom (L0-CON-010).
Parent(s):     L0-OBJ-010, L0-CON-010
Source:        N-270, N-290; AIRCRAFT_CHARACTERISTICS.md §2
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-020

```req
ID:            L1-AER-020
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall exclude from its dynamics each term by which motion along one degree
  of freedom produces a force or moment along another degree of freedom in the body frame, other
  than the rigid-body kinematic terms that MS-DYN retains.
Rationale:     Owner definition D18 of "no coupling between axes". The rigid-body kinematic and
  gyroscopic terms are decided in MS-DYN under #81 (C1, closes at G2); the exception is named so
  that this record does not prejudge #81. The effector set must not couple axes either: each
  axis demand is met with the other force and moment components at zero (L1-AER-120 to -140).
  Children must show (D40): (Inspection) MS-DYN and the effector requirements define no
  aerodynamic or effector cross-coupling term, and list each retained kinematic term.
  Sufficiency: the dynamics (DYN) and effector (EF) children together exclude every coupling
  source the model contains, which is what L0-CON-030 constrains.
Parent(s):     L0-CON-030
Source:        D18; OBJECTIVES.md §2
Allocated to:  DYN, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Treatment of rigid-body kinematic and gyroscopic terms (#81), Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-030

```req
ID:            L1-AER-030
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall produce no aerodynamic lift force.
Rationale:     Lift would couple attitude and translation and defeat the independent control of
  L0-CON-020 (AIRCRAFT_CHARACTERISTICS §1, §7). Drag is the only aerodynamic force (L1-AER-070).
  "Shall produce no" is a true prohibition (METHODOLOGY §8.4 rule 11). Children must show
  (D40): (Inspection) MS-DYN defines no aerodynamic force other than drag.
  Sufficiency: the dynamics model is the only place an aerodynamic force could arise, so a DYN
  child that excludes lift satisfies L0-CON-040.
Parent(s):     L0-CON-040
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §7
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-040

```req
ID:            L1-AER-040
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have no aerodynamic control surface.
Rationale:     Motion comes from the effectors, not from control surfaces (OBJECTIVES §2;
  AIRCRAFT_CHARACTERISTICS §2, §7). Children must show (D40): (Inspection) neither MS-DYN nor
  the effector requirements define a control surface or a force that depends on a surface
  deflection.
  Sufficiency: a control surface would appear either in the dynamics (as an aerodynamic force)
  or in the effector set (as an actuator); excluding it in both covers L0-CON-050.
Parent(s):     L0-CON-050
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2, §7
Allocated to:  DYN, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-050

```req
ID:            L1-AER-050
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute the total force and moment on the vehicle as the sum of
  gravity, aerodynamic drag and the control forces and control moments, in accordance with
  MS-DYN.
Rationale:     L0-CON-090 limits the external effects to gravity, drag on the air-relative
  velocity and ground contact; L0-CON-060 makes the effectors the only source of control force
  and moment. Ground contact is not a force: it ends the run as a landing or a crash
  (L1-AER-260, -270; L0-ASM-110). Consumed fuel adds no force (L0-ASM-090). Children must show
  (D40): (Inspection) MS-DYN lists these three contributions and no other; (Analysis) the
  free-fall and terminal-velocity checks of L1-AER-010 pass.
  Sufficiency: with L1-AER-060 (gravity) and -070 (drag), this record closes the list of forces
  and moments, which covers the force part of L0-CON-090 and the model side of L0-CON-060.
Parent(s):     L0-CON-090, L0-CON-060
Source:        AIRCRAFT_CHARACTERISTICS.md §2, §7; D17, D37
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-060

```req
ID:            L1-AER-060
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall apply a uniform gravitational acceleration of magnitude
  [P-DYN-010] along the downward vertical of the local reference frame.
Rationale:     Uniform gravity on a flat, non-rotating world (L0-ASM-030, L0-ASM-040, CV-110,
  CV-180). It gives closed-form free-fall solutions for verification. The value is proposed as
  standard gravity, so that the crew limit L0-CON-310 reads 1 g in a hover exactly (G0-F25,
  R-F06). Children must show (D40): (Analysis) simulated free fall in vacuum-equivalent
  conditions matches the closed-form solution.
  Sufficiency: gravity is one of the three effects L0-CON-090 allows; this record fixes its
  model, and L1-AER-050 makes it part of the total force.
Parent(s):     L0-CON-090
Source:        L0-ASM-040; CV-110, CV-180
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-DYN-010
TBD/TBR:       P-DYN-010 value TBR (proposed 9.806 65 m/s²), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-070

```req
ID:            L1-AER-070
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute aerodynamic drag from its air-relative velocity and from the
  air density of the standard atmosphere at its altitude, in accordance with MS-DYN.
Rationale:     Drag acts on the velocity relative to the air, which includes the wind the TST gives
  with each step, steady wind plus gusts (L0-CON-090, L0-ASM-050, D17, D51, CV-470). Density follows the standard
  atmosphere (D20) and depends on altitude only (L0-ASM-060). Whether drag depends on attitude
  (elongated body) is an MS-DYN choice bounded by L1-AER-020. Children must show (D40):
  (Analysis) simulated free fall with drag reaches the closed-form terminal velocity for the
  drag model, with and without wind.
  Sufficiency: drag is the second effect L0-CON-090 allows; this record fixes its dependence on
  the air-relative velocity, which is the part of L0-CON-090 that involves the wind.
Parent(s):     L0-CON-090
Source:        D17, D20; L0-ASM-050, L0-ASM-060
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-080

```req
ID:            L1-AER-080
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall generate each control force and each control moment with its
  effectors.
Rationale:     Fictional force emitters replace engines, wings and control surfaces (OBJECTIVES
  §2; AIRCRAFT_CHARACTERISTICS §3). A control force or moment is any force or moment other than
  gravity and drag (glossary). Children must show (D40): (Inspection) the effector
  requirements and MS-DYN identify the effectors as the only source of control force and
  moment.
  Sufficiency: with L1-AER-050, which makes gravity and drag the only other contributions, this
  record covers L0-CON-060.
Parent(s):     L0-CON-060
Source:        AIRCRAFT_CHARACTERISTICS.md §3
Allocated to:  EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-090

```req
ID:            L1-AER-090
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall keep the direction of action of each effector constant in the body
  frame.
Rationale:     Nothing swivels (D19). The direction vector of each effector is fixed in the body
  frame (CV-330). The layout of the directions is an EF design decision, not an L1 requirement.
  Children must show (D40): (Inspection) the effector requirements and MS-DYN define a
  constant body-frame direction for each effector.
  Sufficiency: the effector subsystem is the only place the direction of action is defined, so
  one EF child covers L0-CON-070.
Parent(s):     L0-CON-070
Source:        D19; AIRCRAFT_CHARACTERISTICS.md §3
Allocated to:  EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-100

```req
ID:            L1-AER-100
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall define each effector only by its direction of action, its control
  effectiveness, its output limits, its command response and its fuel consumption parameters.
Rationale:     No physical explanation of the emitter technology is required (L0-CON-080;
  AIRCRAFT_CHARACTERISTICS §3, §7). The list is closed. The consumption parameters belong to FU
  (L1-AER-160, -170). Children must show (D40): (Inspection) each effector parameter in the
  parameter database belongs to one of the five listed kinds.
  Sufficiency: the EF children define the first four kinds and the FU children the fifth;
  together they are the whole effector model, which is what L0-CON-080 constrains.
Parent(s):     L0-CON-080
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §7
Allocated to:  EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-110

```req
ID:            L1-AER-110
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall limit the force of each effector to the maximum force magnitude
  that the parameter database defines for that effector.
Rationale:     Each effector has a maximum force (L0-CON-300). The per-effector maxima are EF
  parameters set at C3. Allocation (FC) must handle a demand beyond the limit as nominal
  behaviour; the priority rule is a derived requirement at L3/L4 (FC1). Children must show
  (D40): (Inspection) each effector has a maximum-force parameter; (Test) no automated test run
  produces an effector force above its maximum.
  Sufficiency: EF enforces the limit at the effector, and FC never relies on output beyond it;
  together they keep every effector within its maximum, as L0-CON-300 requires.
Parent(s):     L0-CON-300
Source:        Owner review at G0 (L0-CON-300)
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Per-effector maximum force values TBD, Martin, G2 (C3)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-120

```req
ID:            L1-AER-120
Level:         L1
Type:          Performance
Statement:     While fuel remains, the Aeronef shall be able to produce a control force of at least
  [P-SYS-400] along the negative body z axis with the other control force and control moment
  components at zero.
Rationale:     Effector authority budget, weight-bearing direction. At level attitude (D10) the
  negative body z axis points up, so this force holds the vehicle up and accelerates it
  vertically. Budget (FUNCTIONAL_ANALYSIS §7.1): [P-SYS-400] is at least the maximum vehicle
  mass times the sum of [P-DYN-010] and [P-SYS-440], plus the drag at the climb vertical speed
  [P-SYS-240]. The zero side components show the independent control of L0-CON-020. The usable
  force at low mass is capped by the crew limit (L1-AER-290), not by this record. Children must
  show (D40): (Analysis) the effector set produces the pure force at maximum mass.
  Sufficiency: with L1-AER-130 (the other five force directions) and L1-AER-140 (moments), this
  record gives a pure control force or moment in each of the six degrees of freedom, as
  L0-CON-020 requires.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D10, D19
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-400, P-DYN-010, P-SYS-440, P-SYS-240
TBD/TBR:       P-SYS-400 value TBD (computed when the maximum vehicle mass is known), Martin, G2
  (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-130

```req
ID:            L1-AER-130
Level:         L1
Type:          Performance
Statement:     While fuel remains, the Aeronef shall be able to produce a control force of at least
  [P-SYS-410] along each of the positive and negative body x axis, the positive and negative body
  y axis and the positive body z axis, with the other control force and control moment
  components at zero.
Rationale:     Effector authority budget, non-weight-bearing directions (FUNCTIONAL_ANALYSIS
  §7.1): [P-SYS-410] is at least the maximum vehicle mass times [P-SYS-440], plus the drag at
  the maximum horizontal speed [P-SYS-230] into the largest instantaneous wind, [P-SYS-430]
  plus [P-SYS-560] (D51). The list is the five body
  directions other than the one in L1-AER-120. Children must show (D40): (Analysis) the
  effector set produces each pure force at maximum mass.
  Sufficiency: see L1-AER-120.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D17, D19
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-410, P-SYS-440, P-SYS-230, P-SYS-430, P-SYS-560
TBD/TBR:       P-SYS-410 value TBD (computed when the maximum vehicle mass is known), Martin, G2
  (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-140

```req
ID:            L1-AER-140
Level:         L1
Type:          Performance
Statement:     While fuel remains, the Aeronef shall be able to produce a control moment of at least
  [P-SYS-420] about each body axis in each sense, with the other control force and control moment
  components at zero.
Rationale:     Effector authority budget, rotation (FUNCTIONAL_ANALYSIS §7.1): [P-SYS-420] is at
  least the largest moment of inertia times the angular acceleration needed to reach the heading
  rate [P-SYS-270], plus the drag moment, with a margin for holding level attitude. Pitch and
  roll are held level (D10); yaw sets the heading. Children must show (D40): (Analysis) the
  effector set produces each pure moment at maximum inertia.
  Sufficiency: see L1-AER-120.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D10, D19
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-420, P-SYS-270
TBD/TBR:       P-SYS-420 value TBD (computed when the inertia is known), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-150

```req
ID:            L1-AER-150
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall start each run with the fuel mass of its initial condition, of at
  most [P-FU-010].
Rationale:     A finite onboard quantity of fuel supplies the effectors (L0-CON-100). The capacity
  is a parameter; the fuel at the start of a run is part of the initial condition (N-310,
  L1-AER-660), so that test procedures can start at any fuel state. Children must show (D40):
  (Inspection) the parameter database holds the capacity; (Test) a run started with a stated
  fuel mass reports that mass at its first output sample.
  Sufficiency: with L1-AER-200 (output depends on fuel), this record gives the finite supply
  and the initial-quantity parameter that L0-CON-100 asks for.
Parent(s):     L0-CON-100
Source:        N-150, N-310; CONOPS §4.5
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-010
TBD/TBR:       P-FU-010 value TBD, Martin, G2 (C2, fuel budget §7.3)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-160

```req
ID:            L1-AER-160
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute its fuel mass flow from the control forces and control
  moments its effectors produce, through a translational consumption relationship and a rotational
  consumption relationship defined in MS-DYN.
Rationale:     Fuel is consumed to produce the commanded forces and rotational effects, with
  separate terms for linear and rotational actuation (L0-CON-120; AIRCRAFT_CHARACTERISTICS §4).
  The form of each relationship is a C2 decision recorded in MS-DYN. Because the effectors
  counter gravity, fuel is consumed in every flight condition, hover included (CONOPS §4.5).
  Children must show (D40): (Analysis) the simulated fuel mass flow matches an independent
  computation from the recorded effector outputs.
  Sufficiency: with L1-AER-170 (the parameters are configurable), this record covers both
  relationships of L0-CON-120, and it makes the fuel used depend on effector output
  (L0-CON-100).
Parent(s):     L0-CON-120, L0-CON-100
Source:        N-280; AIRCRAFT_CHARACTERISTICS.md §4
Allocated to:  FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-170

```req
ID:            L1-AER-170
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall take its translational consumption parameters [P-FU-040] and its
  rotational consumption parameters [P-FU-050] from the parameter database at the start of each
  run.
Rationale:     Configurable consumption lets campaigns vary it without a software change
  (L0-CON-120, N-020). Children must show (D40): (Demonstration) two runs with different values
  of the consumption parameters, and no software change, give the fuel mass flows that each set
  of values predicts.
  Sufficiency: see L1-AER-160.
Parent(s):     L0-CON-120
Source:        N-020, N-280
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-040, P-FU-050
TBD/TBR:       P-FU-040, P-FU-050 values TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-180

```req
ID:            L1-AER-180
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute its vehicle mass as its dry mass [P-FU-030] plus its
  remaining fuel mass.
Rationale:     Fuel consumption decreases the vehicle mass (L0-CON-110; CV-340). The mass loss is a
  real effect on the dynamics: the same force gives a larger acceleration (L0-ASM-090). The
  maximum vehicle mass, used by the authority budgets, is [P-FU-030] plus [P-FU-010]. Children
  must show (D40): (Analysis) at each output sample of a run, the reported vehicle mass equals
  the dry mass plus the reported remaining fuel mass.
  Sufficiency: with L1-AER-190 (remaining fuel is the initial fuel minus the integral of the
  flow), this record makes the vehicle mass decrease by the fuel consumed (L0-CON-110).
Parent(s):     L0-CON-110
Source:        N-280; CV-340
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-030, P-FU-010
TBD/TBR:       P-FU-030 value TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-190

```req
ID:            L1-AER-190
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall keep its remaining fuel mass within [P-FU-060] of its initial fuel
  mass minus the time integral of its fuel mass flow.
Rationale:     The fuel-mass integral is one of the independent credibility checks of METHODOLOGY
  §10.3. The tolerance covers the numerical integration only. Children must show (D40):
  (Analysis) over the reference mission (SC-110), an independent integration of the recorded
  fuel mass flow agrees with the reported remaining fuel mass within [P-FU-060].
  Sufficiency: see L1-AER-180.
Parent(s):     L0-CON-110
Source:        METHODOLOGY §10.3; N-290
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-060
TBD/TBR:       P-FU-060 value TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-200

```req
ID:            L1-AER-200
Level:         L1
Type:          Functional
Statement:     When the remaining fuel mass reaches zero, the Aeronef shall produce zero control
  force and zero control moment.
Rationale:     The output of each effector depends on the availability of fuel (L0-CON-100).
  Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070): the vehicle then moves under
  gravity and drag alone and keeps its angular rate (CONOPS SC-110 leg 10). What the autoflight
  modes do at exhaustion is open at L2 (#59). Children must show (D40): (Test) in the reference
  mission, each effector output is zero from the first sample at which the remaining fuel mass
  is zero.
  Sufficiency: with L1-AER-150 and -160, this record ties every effector output to the fuel
  supply (L0-CON-100).
Parent(s):     L0-CON-100
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-210

```req
ID:            L1-AER-210
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall keep its centre of gravity at one fixed position in the body frame
  at each fuel state.
Rationale:     The centre of gravity is fixed, including while fuel is consumed (L0-CON-130). It
  is the body-frame origin (CV-160), so the effector moment arms stay constant. Children must
  show (D40): (Inspection) MS-DYN and the mass-properties requirements give one centre-of-gravity
  position for every fuel mass.
  Sufficiency: FU defines the mass distribution and DYN uses the centre of gravity as origin;
  both fixing it covers L0-CON-130.
Parent(s):     L0-CON-130
Source:        AIRCRAFT_CHARACTERISTICS.md §4
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-220

```req
ID:            L1-AER-220
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall derive its inertia tensor at each fuel state from the elongated body
  shape and the simplified mass distribution stated in MS-DYN.
Rationale:     The shape matters only through its mass properties (L0-CON-140;
  AIRCRAFT_CHARACTERISTICS §1, §4). Whether the inertia changes with the fuel state is a C2
  decision; this record requires that the answer be stated for each fuel state. The body shape
  is provisional (TBR in L0-CON-140). Children must show (D40): (Inspection) MS-DYN derives each
  moment and product of inertia from the stated shape and distribution, with the CV-350 sign
  convention.
  Sufficiency: one derivation covers L0-CON-140; the fuel-state dependence closes the question
  L0-CON-140 leaves to the mass-properties requirements.
Parent(s):     L0-CON-140
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §4; CV-350
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Elongated body shape provisional (L0-CON-140), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-230

```req
ID:            L1-AER-230
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have no electrical power generation, distribution or consumption
  function.
Rationale:     Electrical power is outside the modelling scope (L0-CON-160;
  AIRCRAFT_CHARACTERISTICS §4, §7). The effectors draw only on fuel (L1-AER-160). Children must
  show (D40): (Inspection) no DYN, FU or EF requirement and no part of MS-DYN defines an
  electrical quantity.
  Sufficiency: the three vehicle-model subsystems are where a power system would sit; excluding
  it in each covers L0-CON-160.
Parent(s):     L0-CON-160
Source:        AIRCRAFT_CHARACTERISTICS.md §4, §7
Allocated to:  DYN, FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-240

```req
ID:            L1-AER-240
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have its nose on the positive body x axis.
Rationale:     The nose marks the designated forward direction (L0-CON-150), which fixes the body x
  axis (CV-170) and the heading (CV-530). Children must show (D40): (Inspection) the MS-DYN
  geometry places the nose on the positive body x axis.
  Sufficiency: with L1-AER-250 (crew station), this record gives the forward direction and the
  crew position that L0-CON-150 asks for.
Parent(s):     L0-CON-150
Source:        AIRCRAFT_CHARACTERISTICS.md §1; CV-170
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-250

```req
ID:            L1-AER-250
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have its crew station at the body-frame position [P-DYN-400].
Rationale:     The crew sits in the cockpit toward the nose (L0-CON-150, CV-170). The position
  places the crew in the body frame; the crew acceleration limit is evaluated at the centre of
  gravity (D45, L1-AER-290), not here. Children must show (D40): (Inspection) the MS-DYN geometry states the crew
  station position.
  Sufficiency: see L1-AER-240.
Parent(s):     L0-CON-150
Source:        AIRCRAFT_CHARACTERISTICS.md §1; CV-170
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-DYN-400
TBD/TBR:       P-DYN-400 value TBD, Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-260

```req
ID:            L1-AER-260
Level:         L1
Type:          Functional
Statement:     When the Aeronef makes ground contact within the landing envelope, the Aeronef shall
  report a landing in its operational data.
Rationale:     Ideal landing (D37, L0-CON-290, L0-ASM-110): contact at altitude zero within the
  envelope (L1-AER-280) is a landing. There is no gear, bounce or friction model; the TST ends
  the run on the event (CONOPS §4.6). Children must show (D40): (Test) a descent to the ground
  within the envelope produces one landing event at the contact sample.
  Sufficiency: with L1-AER-270 (crash) and -280 (envelope), this record defines ground contact,
  the envelope and both outcomes, as L0-CON-290 requires.
Parent(s):     L0-CON-290
Source:        D8, D37; CONOPS §4.2, §4.6
Allocated to:  DYN, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-270

```req
ID:            L1-AER-270
Level:         L1
Type:          Functional
Statement:     When the Aeronef makes ground contact outside the landing envelope, the Aeronef shall
  report a crash in its operational data.
Rationale:     Contact outside the envelope is a crash that ends the run (D37, L0-CON-290). The
  reference mission normally ends this way after fuel exhaustion (SC-110). Children must show
  (D40): (Test) a free fall to the ground from fuel exhaustion produces one crash event at the
  contact sample.
  Sufficiency: see L1-AER-260.
Parent(s):     L0-CON-290
Source:        D37; CONOPS SC-110
Allocated to:  DYN, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-280

```req
ID:            L1-AER-280
Level:         L1
Type:          Performance
Statement:     The Aeronef shall classify a ground contact as within the landing envelope when the
  vertical speed magnitude is at most [P-SYS-500], the horizontal speed is at most [P-SYS-510]
  and the sensed acceleration magnitude is at most [P-SYS-520] at the contact sample.
Rationale:     The envelope limits velocity and acceleration at contact (L0-CON-290, D37). The
  three limits are one envelope, so they are one requirement (D30). [P-SYS-520] is at most
  [P-SYS-120], so that the envelope never admits a sensed acceleration the crew limit forbids
  (L0-CON-310 guidance). Children must show (D40): (Test) contacts on each side of each limit
  are classified correctly.
  Sufficiency: see L1-AER-260. The relation of [P-SYS-520] to [P-SYS-120] covers the
  landing-envelope part of L0-CON-310.
Parent(s):     L0-CON-290, L0-CON-310
Source:        D37; L0-CON-310
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-500, P-SYS-510, P-SYS-520, P-SYS-120
TBD/TBR:       P-SYS-500, P-SYS-510, P-SYS-520 values TBD, Martin, G2; envelope quantities TBR
  (B1-Q06), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-290

```req
ID:            L1-AER-290
Level:         L1
Type:          Performance
Statement:     While the Aeronef is airborne, the Aeronef shall keep the magnitude of the sensed
  acceleration at the centre of gravity at most [P-SYS-120].
Rationale:     Crew g-limit (L0-CON-310, D38). L0 leaves the evaluation point to a lower level;
  the owner chose the centre of gravity (D45, #97), which keeps the limit simple. Budget
  (FUNCTIONAL_ANALYSIS §7.2): [P-SYS-120] is at least [P-DYN-010] (holding the vehicle up) plus
  [P-SYS-440] (vehicle acceleration), with the rest as margin. As
  fuel burns, the allowed resultant control force falls with the mass (D38); FC owns that limit,
  AF keeps its manoeuvres within [P-SYS-440], and FU supplies the mass. Children must show
  (D40): (Test) in every automated test run, at every fuel state, while airborne, the sensed
  acceleration at the centre of gravity does not exceed [P-SYS-120].
  Sufficiency: with L1-AER-300 (vehicle acceleration limit) and L1-AER-280 (envelope limit),
  this record covers L0-CON-310 in flight and at contact.
Parent(s):     L0-CON-310
Source:        D38; N-170
Allocated to:  FC, AF, FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-120, P-DYN-010, P-SYS-440
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-300

```req
ID:            L1-AER-300
Level:         L1
Type:          Performance
Statement:     While the Aeronef is airborne with fuel remaining, the Aeronef shall keep the
  magnitude of its vehicle acceleration at most [P-SYS-440].
Rationale:     Manoeuvres are g-limited, and the maximum acceleration and deceleration are design
  parameters (D16). This record is the vehicle-acceleration share of the crew budget
  (L1-AER-290, FUNCTIONAL_ANALYSIS §7.2). Its split: the autoflight manoeuvre limit [P-AF-200]
  plus the flight-control transient allowance [P-FC-020] is at most [P-SYS-440]. It also bounds
  the effector authority budget (L1-AER-120, -130). Children must show (D40): (Test) in every
  automated test run, while fuel remains, the vehicle acceleration does not exceed
  [P-SYS-440].
  Sufficiency: see L1-AER-290.
Parent(s):     L0-CON-310
Source:        D16, D38; N-170
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-440, P-AF-200, P-FC-020
TBD/TBR:       P-SYS-440 value TBR (proposed 14.709 975 m/s², 1.5 g), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-310

```req
ID:            L1-AER-310
Level:         L1
Type:          Performance
Statement:     While in level flight in the operating volume with a steady wind speed of at most [P-SYS-430] plus gusts of at most [P-SYS-560], the
  Aeronef shall sustain a horizontal speed of [P-SYS-230] under autoflight.
Rationale:     Performance envelope (N-170, CONOPS §5). The crew needs known limits to plan, and
  the limit is the top of the selectable horizontal speed. Horizontal speed is ground-referenced
  (CV-480), so a headwind raises the airspeed and the drag the effectors must overcome; that is
  why the wind limit enters the authority budget (L1-AER-130). Children must show (D40): (Test)
  the vehicle holds [P-SYS-230] in level flight at both ends of the operating altitude range,
  into a steady wind of [P-SYS-430] with gusts of [P-SYS-560].
  Sufficiency: with L1-AER-320 to -350 (vertical speeds, flight path angle, heading rate) and
  -360 (endurance), this record sets the aircraft-level envelope inside which the modes of the
  catalogue operate (L0-OBJ-030).
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS §4.2, §5
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-430, P-SYS-230, P-SYS-560
TBD/TBR:       P-SYS-230, P-SYS-430 values TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-320

```req
ID:            L1-AER-320
Level:         L1
Type:          Performance
Statement:     While climbing in the operating volume, the Aeronef shall sustain a vertical speed of
  [P-SYS-240] under autoflight.
Rationale:     Performance envelope (N-170). The Aeronef can climb with no horizontal motion and
  without tilting (SC-040). The value bounds the upward authority budget (L1-AER-120). Children
  must show (D40): (Test) the vehicle holds [P-SYS-240] at zero and at maximum horizontal speed.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-040
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-240
TBD/TBR:       P-SYS-240 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-330

```req
ID:            L1-AER-330
Level:         L1
Type:          Performance
Statement:     While descending in the operating volume, the Aeronef shall sustain a vertical speed
  magnitude of [P-SYS-250] under autoflight.
Rationale:     Performance envelope (N-170). Descent is "similar to climb" (D3) with its own
  limit. Children must show (D40): (Test) the vehicle holds a descent at [P-SYS-250] at zero and
  at maximum horizontal speed, and levels off above the minimum operating altitude.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-020, SC-030
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-250
TBD/TBR:       P-SYS-250 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-340

```req
ID:            L1-AER-340
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall sustain a flight path angle of
  magnitude [P-SYS-260] under autoflight.
Rationale:     Performance envelope (N-170). The flight path angle depends on velocity only
  (CV-560); with the horizontal and vertical speed limits it bounds the climbs and descents on
  flight path angle of the catalogue. [P-SYS-260] is consistent with [P-SYS-240], [P-SYS-250]
  and [P-SYS-230] when the horizontal speed allows it. Children must show (D40): (Test) climbs
  and descents at [P-SYS-260] are held within the vertical speed limits.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-010, SC-030
Allocated to:  AF, FC, NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-260, P-SYS-240, P-SYS-250, P-SYS-230
TBD/TBR:       P-SYS-260 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-350

```req
ID:            L1-AER-350
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall sustain a heading rate of
  [P-SYS-270] under autoflight.
Rationale:     Performance envelope (N-170). Heading rate is dψ/dt (CV-290). Heading is
  independent of track on the Aeronef (CV-550), so a heading change does not change the
  direction of motion unless a mode asks for it (L2). The value bounds the moment authority
  budget (L1-AER-140) and the rotational term of the crew budget (L1-AER-290). Children must
  show (D40): (Test) a heading change at [P-SYS-270] at maximum inertia.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-050, SC-060
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-270
TBD/TBR:       P-SYS-270 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-360

```req
ID:            L1-AER-360
Level:         L1
Type:          Performance
Statement:     While holding a fixed position with no wind applied, from an initial fuel mass of
  [P-FU-010], the Aeronef shall stay airborne with fuel remaining for at least [P-SYS-280].
Rationale:     Fuel budget (FUNCTIONAL_ANALYSIS §7.3). Holding a fixed position is the condition
  in which the effectors only counter gravity, so it sets the endurance at full fuel and maximum
  mass (CONOPS SC-110 variation). With a consumption proportional to force, [P-FU-010] must be at
  least [P-FU-030] times the exponential of the product of the translational consumption
  coefficient, [P-DYN-010] and [P-SYS-280], minus one; C2 confirms the form. Children must show
  (D40): (Test) from full fuel, the time to fuel exhaustion while holding position is at least
  [P-SYS-280].
  Sufficiency: the finite supply of L0-CON-100 must still allow useful missions; this record
  turns that into a measurable endurance, and with L1-AER-310 to -350 it completes the envelope
  for L0-OBJ-030.
Parent(s):     L0-CON-100, L0-OBJ-030
Source:        N-150, N-250; CONOPS SC-110
Allocated to:  FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-010, P-SYS-280, P-FU-030, P-DYN-010
TBD/TBR:       P-SYS-280 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-370

```req
ID:            L1-AER-370
Level:         L1
Type:          Functional
Statement:     The Aeronef shall regulate each of its six degrees of freedom toward a separate
  reference for that degree of freedom.
Rationale:     Flight control regulates motion independently in each of the three translational
  and three rotational degrees of freedom (L0-OBJ-020; AIRCRAFT_CHARACTERISTICS §5). The
  references come from autoflight (L1-AER-420). Which quantity is regulated per axis (velocity,
  position, rate, attitude) and in which frame is a C4 decision. One control-law set is developed
  (D42). Children must show (D40): (Test) a step in the reference of each degree of freedom is
  followed by that degree of freedom.
  Sufficiency: with L1-AER-380 (independence) and -440 (state), this record gives a regulation
  requirement for each of the six degrees of freedom (L0-OBJ-020), each acting on its own
  (L0-CON-020).
Parent(s):     L0-OBJ-020, L0-CON-020
Source:        N-240; AIRCRAFT_CHARACTERISTICS.md §5
Allocated to:  FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-380

```req
ID:            L1-AER-380
Level:         L1
Type:          Performance
Statement:     When the reference of one degree of freedom changes, the Aeronef shall keep the
  velocity along each other translational axis within [P-SYS-540] of its reference and the body
  rate about each other rotational axis within [P-SYS-550] of its reference.
Rationale:     Measurable form of independent control authority (L0-CON-020) and of the absence
  of cross-axis coupling (L0-CON-030, D18): a manoeuvre on one axis leaves the others where they
  were. The two tolerances are the cross-axis budget shared by FC (regulation) and EF
  (allocation without side components). Children must show (D40): (Test) for a step on each
  degree of freedom in turn, the other five stay within the tolerances.
  Sufficiency: see L1-AER-370.
Parent(s):     L0-CON-020, L0-OBJ-020
Source:        N-240; D18
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-540, P-SYS-550
TBD/TBR:       P-SYS-540, P-SYS-550 values TBD, Martin, G2 (C4)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-390

```req
ID:            L1-AER-390
Level:         L1
Type:          Performance
Statement:     While autoflight guides the vehicle, the Aeronef shall hold its pitch angle and its
  roll angle within [P-AF-180] of zero.
Rationale:     Owner decision D10: pitch and roll stay level, because the Aeronef does not need to
  pitch or roll to move; those manoeuvres are possible but serve no purpose. This is a rule for
  every mode, not a mode definition, so it is stated once at aircraft level; the heading
  behaviour of each mode is L2 (D33, A2-Q03). Level attitude also keeps the negative body z axis
  pointing up for the upward authority budget (L1-AER-120). Children must show (D40): (Test) in
  each mode of the catalogue, pitch and roll angles stay within [P-AF-180].
  Sufficiency: the attitude references come from AF and are held by FC; both children together
  give the predictable attitude the autoflight operating concept needs (L0-OBJ-030, N-160)
  while keeping attitude independent of translation (L0-CON-020).
Parent(s):     L0-OBJ-030, L0-CON-020
Source:        D10; N-160
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-AF-180
TBD/TBR:       P-AF-180 value TBR, Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-400

```req
ID:            L1-AER-400
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall take its flight-control-law design from its configuration, so that
  replacing the design changes no vehicle model file.
Rationale:     Control-law designers swap controllers without touching the vehicle model
  (L0-CON-200, N-230). One design exists now (D42); a test variant is enough to show the
  replacement (R-F02). The vehicle model is DYN, FU and EF (FUNCTIONAL_ANALYSIS §5). Children
  must show (D40): (Demonstration) a test variant of the control-law design is selected through
  the configuration, the run uses it, and the vehicle model files have unchanged checksums.
  Sufficiency: with L1-AER-420 (common FC-AF interface) and -430 (vehicle-model boundary), this
  record makes the control law replaceable without modifying the vehicle model (L0-CON-200).
Parent(s):     L0-CON-200
Source:        N-230; D15, D42
Allocated to:  FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-410

```req
ID:            L1-AER-410
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall take its autoflight implementation from its configuration, so that
  replacing the implementation changes no vehicle model file.
Rationale:     Same reason as L1-AER-400 for autoflight (L0-CON-210). There is one autoflight
  implementation (D24). Children must show (D40): (Demonstration) a test variant of the
  autoflight implementation is selected through the configuration, the run uses it, and the
  vehicle model files have unchanged checksums.
  Sufficiency: with L1-AER-420 and -430, this record covers L0-CON-210.
Parent(s):     L0-CON-210
Source:        N-220; D15, D24
Allocated to:  AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-420

```req
ID:            L1-AER-420
Level:         L1
Type:          Interface
Statement:     The Aeronef shall pass the axis references and mode status from autoflight to flight
  control through the one interface defined in ICD-FC-AF, for each flight-control-law design and
  each autoflight implementation.
Rationale:     Modes and controllers are decoupled: any autoflight implementation pairs with any
  control law behind a common mode logic (D15, #72). A single interface is what makes that true.
  Children must show (D40): (Inspection) the FC and AF requirements each cite ICD-FC-AF as their
  only mutual interface; (Demonstration) the test variants of L1-AER-400 and -410 run against
  the same interface.
  Sufficiency: see L1-AER-400 and L1-AER-410.
Parent(s):     L0-CON-200, L0-CON-210
Source:        D15
Allocated to:  FC, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-430

```req
ID:            L1-AER-430
Level:         L1
Type:          Interface
Statement:     The Aeronef shall exchange data between its vehicle model and its flight software
  only as effector commands into the vehicle model and as vehicle state, vehicle mass and fuel
  state out of it.
Rationale:     A fixed vehicle-model boundary is what lets the control law and the autoflight be
  replaced without modifying the vehicle model (L0-CON-200, -210). The list is closed. The data
  definitions go in a vehicle-model boundary ICD (IN-B1-01). Children must show (D40):
  (Inspection) each data item crossing the boundary in the DYN, FU, EF and FC requirements is one
  of the listed kinds and is defined in the ICD.
  Sufficiency: see L1-AER-400 and L1-AER-410.
Parent(s):     L0-CON-200, L0-CON-210
Source:        TESTING_ENVIRONMENT.md §2; D15
Allocated to:  DYN, FU, EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-440

```req
ID:            L1-AER-440
Level:         L1
Type:          Interface
Statement:     The Aeronef shall provide its navigation and flight-control functions with the
  exact simulated vehicle state of the first simulation step of each control frame.
Rationale:     Perfect state knowledge (L0-ASM-010, confirmed at G0) is turned into a requirement
  here, as METHODOLOGY §4.4 asks before L1 is baselined. The only delay is the control-frame
  sampling, which the timing budget accounts for (L1-AER-680, -710). Sensor models are a later
  upgrade (#83). Children must show (D40): (Test) the state the navigation and flight-control
  functions receive equals the recorded vehicle state of the frame-start step.
  Sufficiency: regulation (L0-OBJ-020) and guidance (L0-OBJ-030) need the state; with
  L1-AER-370 and -530 this record supplies it on a defined basis.
Parent(s):     L0-OBJ-020, L0-OBJ-030
Source:        L0-ASM-010; METHODOLOGY §4.4
Allocated to:  DYN, NAV, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-450

```req
ID:            L1-AER-450
Level:         L1
Type:          Functional
Statement:     The Aeronef shall guide its translation and its heading toward the targets the crew
  selects, through the autoflight modes of the baselined mode catalogue.
Rationale:     Autoflight is the primary means of operating the Aeronef (L0-OBJ-030, N-050). The
  catalogue is plan decision D3 and is taken as given. The modes, their groups and combinations
  (Q5, #6), arming, capture and transitions, and their annunciation labels are defined at L2 by
  AF (C5, D33). This record states only the aircraft-level capability. Children must show (D40):
  (Inspection) each mode of the catalogue is covered by an AF requirement that traces to this
  record, and the mode logic is specified in AF_MODE_LOGIC.
  Sufficiency: with L1-AER-460 (position accuracy budget), -470 (annunciation), -480
  (selections), -530 and -540 (navigation) and the envelope L1-AER-310 to -360, this record
  covers the autoflight objective at aircraft level; the per-mode coverage is shown at L2.
Parent(s):     L0-OBJ-030
Source:        N-050, N-190; D3, D33
Allocated to:  AF, NAV, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Mode combinations (#6, proposal in B1 issues), Martin, G1 (decision) and G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-460

```req
ID:            L1-AER-460
Level:         L1
Type:          Performance
Statement:     While autoflight holds a fixed position with a steady wind speed of at most [P-SYS-430] plus gusts of at most [P-SYS-560], the
  Aeronef shall keep its position within [P-SYS-450] of the reference position at each output
  sample that follows the start of the hold by at least [P-SYS-460].
Rationale:     Position error budget (FUNCTIONAL_ANALYSIS §7.4), the aircraft-level accuracy of
  the hold capability (N-130, D11, D17). Split: the autoflight guidance share [P-AF-160] plus the
  translational regulation share [P-FC-010] is at most [P-SYS-450]; the navigation share is zero
  under perfect state knowledge (L1-AER-440). Which position is the reference, and when the hold
  begins, are L2 (#78). Children must show (D40): (Test) holds in zero wind, and in a steady
  wind of [P-SYS-430] with gusts of [P-SYS-560] from several directions, stay within
  [P-SYS-450].
  Sufficiency: L0-OBJ-020 needs regulation accuracy and L0-OBJ-030 a usable hold; this record
  sets the one aircraft-level number both are measured against.
Parent(s):     L0-OBJ-030, L0-OBJ-020
Source:        N-130, N-140; D11, D17; METHODOLOGY §12
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-430, P-SYS-450, P-SYS-460, P-AF-160, P-FC-010, P-SYS-560
TBD/TBR:       P-SYS-450 value TBR (proposed 1 m), P-SYS-460 value TBD, Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-470

```req
ID:            L1-AER-470
Level:         L1
Type:          Performance
Statement:     When an autoflight mode becomes armed or active, or when a target changes, the Aeronef
  shall annunciate the new mode state or target to the crew within [P-SYS-470].
Rationale:     The crew needs to know which mode is active, which is armed and what the vehicle
  will do next (N-060, N-210); annunciations are data items of the crew interface
  (L0-CON-170). Timing budget (FUNCTIONAL_ANALYSIS §7.5): [P-SYS-470] is at least two control
  frames [P-SYS-310] plus one output sample period [P-TM-010]; AF's share is [P-AF-060]. The
  labels are L2 (C5). Children must show (D40): (Test) each change of mode state or target in the
  mode-transition tests is annunciated within [P-SYS-470].
  Sufficiency: with L1-AER-490 (output as data), this record makes the crew interface carry the
  autoflight state (L0-CON-170) that operating by autoflight requires (L0-OBJ-030).
Parent(s):     L0-OBJ-030, L0-CON-170
Source:        N-060, N-210; CONOPS §4.4
Allocated to:  AF, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-470, P-SYS-310, P-TM-010, P-AF-060
TBD/TBR:       P-SYS-470 value TBR (proposed 0.5 s), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-480

```req
ID:            L1-AER-480
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept each crew selection of a mode or a target as a time-stamped
  data item of the crew interface defined in ICD-AER-TST.
Rationale:     The crew interface is data, with no model of physical controls (L0-CON-170). A
  human through the TST, a test procedure and an RVS agent all use the same interface
  (L0-ASM-120, N-320, SC-230), so a scripted selection at a given time behaves as an interactive
  one. The selections are those of the flight control panel (#79, deferred); the panel is not a
  separate subsystem in this draft (B1-Q01, #80.3). Children must show (D40): (Test) a selection
  scripted at a stated simulation time and the same selection made interactively at that time
  give the same operational data.
  Sufficiency: with L1-AER-490 (output side) and -510 (no device or format), this record makes
  each crew selection a data item, as L0-CON-170 requires, and gives autoflight its crew input
  (L0-OBJ-030).
Parent(s):     L0-CON-170, L0-OBJ-030
Source:        N-300, N-320, N-360; L0-ASM-120
Allocated to:  AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Flight control panel content (#79), Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-490

```req
ID:            L1-AER-490
Level:         L1
Type:          Interface
Statement:     The Aeronef shall output its annunciations and indications as data items of the crew
  interface defined in ICD-AER-TST, at each output sample.
Rationale:     The crew receives annunciations and indications as data (L0-CON-170). The
  indications are the vehicle quantities the crew sees: altitude, vertical speed, horizontal
  speed, heading, track, flight path angle, VOR deviation and distance, and remaining fuel
  (CONOPS §4.3). TM owns the output; AF, NAV and FU supply the content (FUNCTIONAL_ANALYSIS §5).
  Children must show (D40): (Inspection) each annunciation and indication is defined as a data
  item in ICD-AER-TST; (Test) the data items are present at each output sample.
  Sufficiency: see L1-AER-480.
Parent(s):     L0-CON-170
Source:        N-060, N-380; CONOPS §4.3
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-500

```req
ID:            L1-AER-500
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall state each crew selection and each annunciated or indicated quantity
  in the crew-facing unit that CONVENTIONS CV-740 assigns to it, converted to and from SI by the
  exact factors of CV-750.
Rationale:     North American aviation units for everything the crew selects or sees (D7, D9,
  D34; L0-CON-270). The unit rule and its limits are CV-760; selections convert without
  intermediate rounding (CV-770). Display resolution and rounding are L2 (CV-780, #55). Children
  must show (D40): (Inspection) each crew selection and each crew-facing output in the AF and TM
  requirements names its CV-740 unit; (Test) a selected value and its shown value convert by
  the CV-750 factor.
  Sufficiency: AF owns the selection side and TM the presentation side; together they cover
  every crew-facing quantity of L0-CON-270.
Parent(s):     L0-CON-270
Source:        N-070; D7, D9, D34; CV-740 to CV-770
Allocated to:  AF, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-510

```req
ID:            L1-AER-510
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall define no physical control device and no display format for its
  crew interface.
Rationale:     Detailed pilot controls and displays are excluded (L0-CON-170;
  AIRCRAFT_CHARACTERISTICS §7). A graphical interface for the panel belongs to the TST and does
  not change this boundary. This is a leaf at L1: it is checked directly over the whole Aeronef
  branch. "Shall define no" is a true prohibition.
  Sufficiency: with L1-AER-480 and -490, which make the crew interface data, this record covers
  the exclusion part of L0-CON-170.
Parent(s):     L0-CON-170
Source:        AIRCRAFT_CHARACTERISTICS.md §7
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: no requirement of the Aeronef branch at L1 or
  below defines a physical control device or a display format, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-520

```req
ID:            L1-AER-520
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall take each crew input through the flight control panel data of its
  crew interface and through no direct manual flight control.
Rationale:     A stick or yoke is out of scope; the flight control panel is as manual as flying the
  Aeronef gets (L0-CON-180, owner at G0). Plan §1 mentions manual control as an optional "Where"
  feature; B1 does not write one, because it would contradict L0-CON-180 (B1-Q09). Leaf at L1,
  checked directly over the Aeronef branch.
  Sufficiency: one inspection over the branch covers L0-CON-180.
Parent(s):     L0-CON-180
Source:        L0-CON-180; plan §1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: no requirement of the Aeronef branch at L1 or
  below defines a direct manual flight control, and each crew input requirement cites the crew
  interface, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-530

```req
ID:            L1-AER-530
Level:         L1
Type:          Functional
Statement:     The Aeronef shall compute, at each control frame, its altitude, horizontal speed,
  vertical speed, heading, track and flight path angle from its vehicle state, as CONVENTIONS
  CV-430 to CV-560 define them.
Rationale:     Navigation function F-AER-09: one definition of each guidance quantity, used by
  autoflight, the crew indications and the operational data (FUNCTIONAL_ANALYSIS §5.2).
  Validity thresholds for track, flight path angle and heading are NAV requirements (CV-580,
  P-NAV-010 to -030). Children must show (D40): (Analysis) each computed quantity matches an
  independent computation from the recorded state, inside its validity range.
  Sufficiency: with L1-AER-540 (VOR), this record gives autoflight every quantity the mode
  catalogue guides (L0-OBJ-030).
Parent(s):     L0-OBJ-030
Source:        N-110, N-190; CV-430 to CV-580
Allocated to:  NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-540

```req
ID:            L1-AER-540
Level:         L1
Type:          Functional
Statement:     While the vehicle is within the reception range [P-NAV-050] of a VOR station, the
  Aeronef shall compute its radial from that station, the TO/FROM sense, the course deviation from
  the selected course and the horizontal distance to the station.
Rationale:     The catalogue includes VOR radial tracking (D3). Ideal VOR (D12): fixed stations,
  true north, no noise, an ideal signal within the reception range; the crew flies a course
  (D14). Definitions CV-610 to CV-670; the deviation sign is deferred to L2 (#54). Behaviour
  outside reception and over the station is NAV and AF (A2-Q08). Children must show (D40):
  (Analysis) the computed quantities match an independent computation from the recorded position
  and station.
  Sufficiency: see L1-AER-530.
Parent(s):     L0-OBJ-030
Source:        N-120; D12, D14; CV-610 to CV-670
Allocated to:  NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-NAV-050
TBD/TBR:       P-NAV-050 value TBR; course deviation sign (#54), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-550

```req
ID:            L1-AER-550
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept from the TST, at the start of each run, the identifier and
  the position in the local reference frame of each VOR station of the run.
Rationale:     Stations are part of the world definition that the TST sets per run (CONOPS §4.2,
  CV-610). Zero stations is a valid set. Children must show (D40): (Test) the stations of the
  initial condition are the ones the navigation function uses.
  Sufficiency: the VOR computation of L1-AER-540 needs the stations; this record supplies them
  across the TST boundary.
Parent(s):     L0-OBJ-030
Source:        CONOPS §4.2; CV-610
Allocated to:  NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-560

```req
ID:            L1-AER-560
Level:         L1
Type:          Functional
Statement:     The Aeronef shall indicate its remaining fuel mass to the crew at each output sample.
Rationale:     The crew needs to see how much fuel is left (N-150); the finite supply bounds every
  mission (L0-CON-100), and the indication is a data item of the crew interface (L0-CON-170).
  It is shown in lb (D9, L1-AER-500). Children must show (D40): (Test) the indicated fuel equals
  the remaining fuel mass converted to lb, at each output sample.
  Sufficiency: with L1-AER-570 and -580 (alerts), this record makes the fuel state known to the
  crew, which completes the crew side of L0-CON-100 through the interface of L0-CON-170.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; D9; CONOPS §4.3, §4.5
Allocated to:  FU, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-570

```req
ID:            L1-AER-570
Level:         L1
Type:          Functional
Statement:     When the remaining fuel mass falls below the fraction [P-FU-020] of [P-FU-010], the
  Aeronef shall annunciate a low-fuel alert within [P-SYS-470].
Rationale:     The crew needs a warning before the fuel runs out (N-150, METHODOLOGY §8.5). The
  threshold is a fraction (CV-720). The alert label is L2. Children must show (D40): (Test) in
  the reference mission, the alert appears within [P-SYS-470] of the first sample below the
  threshold.
  Sufficiency: see L1-AER-560.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  FU, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FU-020, P-FU-010, P-SYS-470
TBD/TBR:       P-FU-020 value TBR (proposed 0.1), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-580

```req
ID:            L1-AER-580
Level:         L1
Type:          Functional
Statement:     When the remaining fuel mass reaches zero, the Aeronef shall annunciate fuel
  exhaustion within [P-SYS-470].
Rationale:     The crew needs to know when the fuel has run out and what follows (N-150): the
  effectors stop (L1-AER-200). What the modes do then is L2 (#59). Children must show (D40):
  (Test) in the reference mission, the annunciation appears within [P-SYS-470] of the first
  sample with zero fuel.
  Sufficiency: see L1-AER-560.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  FU, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-470
TBD/TBR:       Autoflight state after fuel exhaustion (#59), Martin, G2 (C2, C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-590

```req
ID:            L1-AER-590
Level:         L1
Type:          Interface
Statement:     The Aeronef shall attach to each output sample, crew selection record and event
  record the timestamp that CONVENTIONS CV-840 defines.
Rationale:     The operational data must relate inputs, mode changes, control activity and
  responses in time (L0-OBJ-140, N-390). One time base, with the step index authoritative
  (CV-820, CV-840), is what makes that correlation possible. Children must show (D40):
  (Inspection) each record kind in ICD-AER-TST carries the step index and simulation time;
  (Test) the timestamps of a run are consistent with the simulation step.
  Sufficiency: with L1-AER-600 (rate) and L1-AER-610 to -640 (content), this record gives the
  time-stamped records of crew inputs, mode changes, control activity and vehicle responses that
  L0-OBJ-140 asks for.
Parent(s):     L0-OBJ-140
Source:        N-340, N-390; CV-840
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-600

```req
ID:            L1-AER-600
Level:         L1
Type:          Performance
Statement:     The Aeronef shall produce one operational data output sample every [P-TM-010] of
  simulation time.
Rationale:     The TST needs the data at each step it assesses (N-340), and the RVS needs a rate
  fine enough to see cause and effect. [P-TM-010] is an integer multiple of the simulation step
  (timing budget, FUNCTIONAL_ANALYSIS §7.5); it is proposed equal to the control frame period.
  Children must show (D40): (Test) the output samples of a run are spaced by [P-TM-010].
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-340; CV-830
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (proposed equal to P-SYS-310), Martin, G2 (C7)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-610

```req
ID:            L1-AER-610
Level:         L1
Type:          Functional
Statement:     The Aeronef shall record in its operational data each crew selection it receives and
  each target that results from it.
Rationale:     Crew inputs are the first of the four things L0-OBJ-140 relates (OBJECTIVES §4;
  REVERSE_ENGINEERING §3C, §5). The target is recorded in SI with, where the crew selected it,
  the crew-facing value (CV-760 group 4). Children must show (D40): (Test) each scripted
  selection of a run appears once in the operational data with its timestamp and its target.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-340, N-390
Allocated to:  TM, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-620

```req
ID:            L1-AER-620
Level:         L1
Type:          Functional
Statement:     The Aeronef shall record in its operational data, at each output sample, the armed
  and active autoflight modes and the annunciations presented to the crew.
Rationale:     Mode changes are the second thing L0-OBJ-140 relates; they are what the RVS
  reconstructs (L0-SUC-100, -110) and what mode-transition tests assess. Children must show
  (D40): (Test) each mode change of a mode-transition test appears in the operational data at
  the sample where it occurs.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-060, N-340, N-390
Allocated to:  TM, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-630

```req
ID:            L1-AER-630
Level:         L1
Type:          Functional
Statement:     The Aeronef shall record in its operational data, at each output sample, the axis
  references, the axis demands, the effector commands, the effector outputs and the fuel mass
  flow.
Rationale:     Control activity is the third thing L0-OBJ-140 relates (TESTING_ENVIRONMENT §8).
  The list is closed. Whether a signal is released to the RVS is decided with the RVS (#69,
  G0-F22). Children must show (D40): (Inspection) each listed signal is defined in ICD-AER-TST;
  (Test) each is present at each output sample.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-250, N-340
Allocated to:  TM, FC, EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Releasable or protected classification of each signal (#69), Martin, RVS plan
  extension (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-640

```req
ID:            L1-AER-640
Level:         L1
Type:          Functional
Statement:     The Aeronef shall record in its operational data, at each output sample, its vehicle
  state, its navigation quantities, its sensed acceleration at the centre of gravity, its vehicle mass,
  its remaining fuel mass and each ground-contact event.
Rationale:     Vehicle responses are the fourth thing L0-OBJ-140 relates. These are also the
  measurements the TST needs to assess the performance records (L1-AER-290, -300, -460) and the
  fuel used per leg of the reference mission (N-250). The list is closed. Children must show
  (D40): (Inspection) each listed signal is defined in ICD-AER-TST; (Test) each is present at
  each output sample, and each event at its sample.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-250, N-340, N-390
Allocated to:  TM, DYN, NAV, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-650

```req
ID:            L1-AER-650
Level:         L1
Type:          Interface
Statement:     The Aeronef shall output, for each run, the identifier and version of its vehicle
  parameter set, its flight-control-law design and its autoflight implementation.
Rationale:     A result is evidence only if the configuration that produced it is known (N-350).
  There is one configuration to pass every requirement (L0-SUC-020, D42), and the control law and
  autoflight are replaceable (L0-CON-200, -210), so each run must say which design ran. The TST
  adds its own run metadata (CV-870). Children must show (D40): (Test) the identifiers output by
  a run match the configuration it was started with, including a test variant.
  Sufficiency: with L1-AER-400, -410 and -790, this record lets the verification results be tied
  to the one Aeronef configuration and to the design actually loaded.
Parent(s):     L0-CON-200, L0-CON-210, L0-SUC-020
Source:        N-350; CV-870
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-660

```req
ID:            L1-AER-660
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept from the TST, at the start of each run, an initial condition
  of position, velocity, attitude, body rates, fuel mass, autoflight mode state and targets.
Rationale:     The TST sets the whole starting state of a run (N-310, CONOPS §4.6), and every
  scenario starts airborne (CONOPS §4.2). The mode state is a data item here; which mode states
  are valid at start is L2 (#60). Children must show (D40): (Test) the first output sample of a
  run reports the initial condition it was given.
  Sufficiency: an executable model (L0-OBJ-010) must be started from a defined state, and
  autoflight (L0-OBJ-030) from a defined mode state; this record supplies both.
Parent(s):     L0-OBJ-010, L0-OBJ-030
Source:        N-310; CONOPS §4.6, SC-200
Allocated to:  DYN, FU, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Valid initial mode states (#60), Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-670

```req
ID:            L1-AER-670
Level:         L1
Type:          Interface
Statement:     The Aeronef shall advance its vehicle model by one simulation step of [P-SYS-300] each
  time the TST commands a step.
Rationale:     The TST executes the simulation at a fixed step (F-TST-01, CV-820) and controls
  time, so that a run can execute faster or slower than real time with the same result (CV-810).
  The wind of the run comes with the step command (I-25). Children must show (D40): (Test) after
  k commanded steps, the simulation time is k times [P-SYS-300].
  Sufficiency: with L1-AER-660, this record makes the model executable by the TST (L0-OBJ-010).
Parent(s):     L0-OBJ-010
Source:        N-300, N-360; CV-810, CV-820
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-300
TBD/TBR:       P-SYS-300 value TBR (proposed 0.01 s), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-680

```req
ID:            L1-AER-680
Level:         L1
Type:          Performance
Statement:     The Aeronef shall execute its navigation, autoflight and flight-control functions at
  a control frame period of [P-SYS-310] that is an integer multiple of [P-SYS-300].
Rationale:     Derived from the architecture (DD-010 proposed): the flight software runs at a fixed
  rate, synchronised with the simulation step, in the order of FUNCTIONAL_ANALYSIS §4.2. A whole
  number of steps per frame keeps the sampling exact on the CV-840 time base. The frame period
  is part of the timing budget (§7.5). Children must show (D40): (Test) the effector commands
  change only at control-frame boundaries.
Parent(s):     Derived (DD-010)
Source:        Trade study: FUNCTIONAL_ANALYSIS §4.2, §5; CV-830
Allocated to:  NAV, AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-310, P-SYS-300
TBD/TBR:       P-SYS-310 value TBR (proposed 0.02 s), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-690

```req
ID:            L1-AER-690
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall produce identical operational data from an identical configuration,
  initial condition, crew selection sequence and execution host.
Rationale:     Runs must be reproducible (L0-OBJ-110, N-330), and the assumption behind it is a
  deterministic run (L0-ASM-020). The Aeronef's own software is part of every run, so it must not
  add any unrecorded variation. L0-OBJ-110 is allocated to the TST only; CR-B1-01 asks to add AER.
  Bit-identical runs are not checked across hosts (D25); on one host they are the simple test.
  Children must show (D40): (Test) two executions of the same run on one host give identical
  operational data.
  Sufficiency: every subsystem contributes to the operational data, so a determinism child in
  each covers the Aeronef's share of L0-OBJ-110.
Parent(s):     L0-OBJ-110
Source:        N-330; L0-ASM-020; D25
Allocated to:  DYN, FU, EF, FC, AF, NAV, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       Allocation of L0-OBJ-110 to AER (CR-B1-01), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-700

```req
ID:            L1-AER-700
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall execute each of its functions without a graphical display.
Rationale:     The simulation core must work without graphics so that campaigns run unattended
  (L0-CON-190, N-300). The Aeronef runs inside the core, so none of its functions may need a
  display; its crew output is data (L1-AER-490). L0-CON-190 is allocated to the TST only;
  CR-B1-02 asks to add AER. Leaf at L1.
  Sufficiency: the Aeronef's share of L0-CON-190 is that it needs no display; one demonstration
  covers it.
Parent(s):     L0-CON-190
Source:        N-300; TESTING_ENVIRONMENT.md §2
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: an automated run of the reference mission
  (SC-110) completes on an execution host with no graphical display attached and records its
  operational data.
Parameters:    —
TBD/TBR:       Allocation of L0-CON-190 to AER (CR-B1-02), Martin, G1
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-710

```req
ID:            L1-AER-710
Level:         L1
Type:          Performance
Statement:     The Aeronef shall change its effector outputs in response to a vehicle state within
  [P-SYS-480] of the simulation time of that state.
Rationale:     Derived from the timing budget (DD-020 proposed). A discrete flight software and a
  finite effector response add latency to the control loop; bounding it lets the control-law
  design and the effector model be sized against one number. Split (FUNCTIONAL_ANALYSIS §7.5):
  one control frame [P-SYS-310] plus the effector command response time [P-EF-010] is at most
  [P-SYS-480]. Children must show (D40): (Test) a step in a reference produces the first change
  of effector output within [P-SYS-480].
Parent(s):     Derived (DD-020)
Source:        METHODOLOGY §7 rule 4 (timing budget)
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-480, P-SYS-310, P-EF-010
TBD/TBR:       P-SYS-480 value TBR (proposed 0.1 s), P-EF-010 value TBD, Martin, G2 (C3, C4)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-720

```req
ID:            L1-AER-720
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have a baselined model specification, MS-DYN, that states its
  equations of motion, its gravity, drag and wind model, its ground contact model, and its
  effector, fuel and mass-properties models.
Rationale:     L0-OBJ-010 requires the executable model to conform to a baselined model
  specification. The list is the closed content of MS-DYN (plan C1; glossary). Children must
  show (D40): (Inspection) MS-DYN is baselined at G2 and each listed model has a section.
  Sufficiency: with L1-AER-010 and the model-fidelity records it points to, this record gives
  the baselined specification L0-OBJ-010 names.
Parent(s):     L0-OBJ-010
Source:        N-270; plan §6 C1
Allocated to:  DYN, FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-730

```req
ID:            L1-AER-730
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall state in SI units each quantity of its requirements, models,
  interface signals and parameters that is not a crew-facing quantity.
Rationale:     L0-CON-260, METHODOLOGY §8.4 rule 12, CV-710 to CV-730 (radians on the SI side,
  D23). It applies to every subsystem in the same way, so it is a leaf at L1, checked directly at
  each gate rather than restated in each L2 section.
  Sufficiency: one inspection over the Aeronef branch and the parameter database covers the
  Aeronef share of L0-CON-260.
Parent(s):     L0-CON-260
Source:        METHODOLOGY §8.4; CV-710 to CV-730
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each Aeronef parameter that is not marked
  crew-facing has an SI unit, and each requirement of the Aeronef branch states its non-crew
  quantities in SI units, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-740

```req
ID:            L1-AER-740
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall use the frames, axes, sign conventions and quantity definitions of
  the conventions document in each of its requirements, models, interface signals and
  parameters.
Rationale:     L0-CON-280; CV-010. The conventions are fixed (D43) and consistent with R-004
  practice as checked against public sources (D36). Leaf at L1, checked directly.
  Sufficiency: one inspection over the Aeronef branch covers L0-CON-280.
Parent(s):     L0-CON-280
Source:        CV-010; D36, D43
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each frame, axis, sign and quantity name used in
  the Aeronef branch, MS-DYN and the Aeronef ICDs is one defined in CONVENTIONS, checked at each
  gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-750

```req
ID:            L1-AER-750
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have its requirements in one level file per level, with each
  requirement below L0 stating its level and either its parent requirements or the design
  decision it derives from.
Rationale:     Top-down hierarchy (L0-OBJ-180, plan §3, D2, D31). Depth is decided per branch
  (D4). Leaf at L1: the trace check and the record format check it directly.
  Sufficiency: the Aeronef part of L0-OBJ-180 is its own branch of the hierarchy; this record
  covers it.
Parent(s):     L0-OBJ-180
Source:        Plan §3; D2, D4, D31
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the lint and trace check report no LEVEL,
  ID-FORMAT, ORPHAN or DERIVED error in the Aeronef branch, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-760

```req
ID:            L1-AER-760
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall link each of its requirements to a verification method, a
  verification procedure and a recorded verification result.
Rationale:     Bidirectional traceability down to verification results (L0-OBJ-190, METHODOLOGY
  §10.4). The verification matrix is generated by the tools (`tools/vcrm.py`). Leaf at L1.
  Sufficiency: the Aeronef part of L0-OBJ-190 is the trace from its requirements to their
  results; this record covers it, and L1-AER-750 covers the parent-child links.
Parent(s):     L0-OBJ-190
Source:        METHODOLOGY §10.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the verification matrix at AER-REQ-baseline-1
  lists, for each Aeronef requirement, a method, a procedure ID and a last result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-770

```req
ID:            L1-AER-770
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have each of its requirements whose verification method is Test
  verified by an automated test procedure that runs on the TST without operator action.
Rationale:     Behaviour and performance are verified by repeatable, automatically assessed tests
  (L0-SUC-030; OBJECTIVES §6). Leaf at L1.
  Sufficiency: the Aeronef part of L0-SUC-030 is its Test-method requirements; this record
  covers them.
Parent(s):     L0-SUC-030
Source:        OBJECTIVES.md §6; METHODOLOGY §9.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the verification matrix links each Aeronef
  requirement whose method is Test to an automated test procedure with a recorded result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-780

```req
ID:            L1-AER-780
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have each of its engineering artifacts peer reviewed before the
  artifact is baselined.
Rationale:     L0-OBJ-200; METHODOLOGY §11. The Aeronef artifacts are its level-file sections,
  MS-DYN, FUNCTIONAL_ANALYSIS, AF_MODE_LOGIC, its ICDs and its parameters. Leaf at L1.
  Sufficiency: the Aeronef part of L0-OBJ-200 is the review of its own artifacts.
Parent(s):     L0-OBJ-200
Source:        METHODOLOGY §11.1, §11.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each baselined Aeronef artifact has a review
  record in the METHODOLOGY §13.4 format whose exit decision is Baseline.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-790

```req
ID:            L1-AER-790
Level:         L1
Type:          Documentation
Statement:     The Aeronef configuration shall pass the verification of each baselined Aeronef
  requirement.
Rationale:     One configuration: one autoflight implementation with one flight-control-law design
  on the vehicle model, and it must pass every requirement (L0-SUC-020, D26, D39, D42). Leaf at
  L1: the verification matrix shows it directly.
  Sufficiency: the Aeronef part of L0-SUC-020 is exactly this pass.
Parent(s):     L0-SUC-020
Source:        D26, D39, D42
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the verification matrix shows a passing last
  result for each baselined Aeronef requirement, each obtained with the configuration
  identified by L1-AER-650.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-800

```req
ID:            L1-AER-800
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have its requirements baselined down to the last requirement layer of
  each subsystem branch, with no open major review finding, at the requirements baseline.
Rationale:     L0-SUC-010: the baselined set is the definition of the vehicle. The last layer is
  the one above implementation (D4). The requirements baseline is AER-REQ-baseline-1 (G4). Leaf
  at L1.
  Sufficiency: this is the Aeronef part of L0-SUC-010 in full.
Parent(s):     L0-SUC-010
Source:        Plan §6 G4; D4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the tag AER-REQ-baseline-1 exists and the G4
  review record lists no open major finding.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-810

```req
ID:            L1-AER-810
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall pass the automated trace check at the requirements baseline with no
  orphan requirement, no childless parent requirement and no requirement without a verification
  method in its branch.
Rationale:     L0-SUC-150 applies at the complete baseline (G4); intermediate baselines have
  childless records by construction (R-F03). Records allocated only to TST or RVS are not
  counted (D44). Leaf at L1.
  Sufficiency: this is the Aeronef part of L0-SUC-150.
Parent(s):     L0-SUC-150
Source:        METHODOLOGY §10.4; D44
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the trace check output stored with
  AER-REQ-baseline-1 reports no ORPHAN, CHILDLESS or NO-VERIFICATION finding in the Aeronef
  branch.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-820

```req
ID:            L1-AER-820
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall contribute to the final test report the last result of each
  verification procedure performed against each Aeronef requirement.
Rationale:     L0-SUC-170: the report of completion lists every test against every level. Each
  element contributes its section and the orchestrator compiles it (D28). Leaf at L1.
  Sufficiency: this is the Aeronef part of L0-SUC-170.
Parent(s):     L0-SUC-170
Source:        D28
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the Aeronef section of the final test report
  lists each Aeronef verification procedure, the requirements it verifies and its last result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-830

```req
ID:            L1-AER-830
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall contribute to the method assessment report one section that
  assesses the AI-assisted methods used to design and to verify the Aeronef.
Rationale:     L0-OBJ-210 (important to the owner): the assessment of the AI-assisted methods is an
  objective in its own right. Each element contributes; the owner audits (D28). The
  reverse-engineering section comes from the RVS. Leaf at L1.
  Sufficiency: the Aeronef covers the system-design and automated-verification parts of
  L0-OBJ-210 that concern it.
Parent(s):     L0-OBJ-210
Source:        D28; OBJECTIVES.md §1, §6
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the method assessment report contains an
  Aeronef section that assesses the methods used for its design and for its verification.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-840

```req
ID:            L1-AER-840
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have a Vehicle Operating Manual, normal procedures and quick
  reference checklists, each of which states the requirements baseline it describes.
Rationale:     L0-OBJ-150; METHODOLOGY §11.2. The manuals are written after the requirements
  baseline and describe observable behaviour and operator actions. Abnormal and emergency
  procedures are deferred with the hazard analysis. The TST user guide belongs to the TST. Leaf
  at L1.
  Sufficiency: these three documents are the Aeronef part of the set L0-OBJ-150 names.
Parent(s):     L0-OBJ-150
Source:        METHODOLOGY §11.2; N-380, N-430
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the three documents exist and each names the
  requirements baseline it describes.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
