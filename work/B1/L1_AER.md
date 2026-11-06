## AER — Aeronef

The Aeronef system requirements (task B1). The subject of each statement is the Aeronef, treated as a whole. Modes, mode groups, combinations and mode logic are defined at L2 (AF, D33); these records state only the aircraft-level guidance capability. There is one Aeronef configuration (D42). The functions, the N² matrix, the logical architecture, the allocation to the L2 subsystems and the budgets are in [specs/FUNCTIONAL_ANALYSIS.md](../specs/FUNCTIONAL_ANALYSIS.md).

**Verification.** A record allocated to L2 subsystems is verified by roll-up (D40, D58): it passes when each of its children has passed and the decomposition has been reviewed. Its rationale says what the children must show. A record with `Allocated to: —` is a leaf at L1 and is verified directly by its own method.

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
  frame is inertial (L0-ASM-030, CV-140). Children must show (D58): (Analysis) the simulated
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
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-020

```req
ID:            L1-AER-020
Level:         L1
Type:          Constraint
Statement:     The Aeronef dynamics shall contain no term by which motion along one degree of freedom
  produces an acceleration along another degree of freedom in the body frame, other than the
  rigid-body kinematic terms of the MS-DYN kinematic terms list.
Rationale:     Owner definition D18 of "no coupling between axes", stated in acceleration terms as
  L0-CON-030 is. The rigid-body kinematic terms that are kept are listed in the kinematic terms
  list of MS-DYN (#81, closed by D64): the gyroscopic term, the rotation-during-translation term
  and the resolution of forces through the attitude. The body
  axes are principal axes of inertia, so the products of inertia are zero and a moment about one
  body axis gives no angular acceleration about another (D61, L1-AER-220). The effector set must
  not couple axes either: FC allocates each axis demand with the other force and moment
  components at zero, using the effector geometry that EF defines (L1-AER-120 to -140).
  Children must show (D58): (Inspection) MS-DYN and the effector requirements define no
  aerodynamic or effector cross-coupling term, the mass-properties requirements give zero
  products of inertia, and MS-DYN lists each retained kinematic term.
  Sufficiency: the dynamics (DYN), effector (EF) and mass-properties (FU) children together
  exclude every coupling source the model contains (drag, effectors, inertia), which is what
  L0-CON-030 constrains.
Parent(s):     L0-CON-030
Source:        D18, D61; OBJECTIVES.md §2
Allocated to:  DYN, EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  (D58): (Inspection) MS-DYN defines no aerodynamic force other than drag.
  Sufficiency: the dynamics model is the only place an aerodynamic force could arise, so a DYN
  child that excludes lift satisfies L0-CON-040.
Parent(s):     L0-CON-040
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §7
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-040

```req
ID:            L1-AER-040
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have no aerodynamic control surface.
Rationale:     Motion comes from the effectors, not from control surfaces (OBJECTIVES §2;
  AIRCRAFT_CHARACTERISTICS §2, §7). Children must show (D58): (Inspection) neither MS-DYN nor
  the effector requirements define a control surface or a force that depends on a surface
  deflection.
  Sufficiency: a control surface would appear either in the dynamics (as an aerodynamic force)
  or in the effector set (as an actuator); excluding it in both covers L0-CON-050.
Parent(s):     L0-CON-050
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2, §7
Allocated to:  DYN, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-050

```req
ID:            L1-AER-050
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute the total force and moment on the vehicle as the sum of
  gravity, aerodynamic drag, the control forces and control moments and, while the Aeronef is on the
  ground, the ground reaction, in accordance with MS-DYN.
Rationale:     L0-CON-090 limits the external effects to gravity, drag on the air-relative velocity
  and ground contact; L0-CON-060 makes the effectors the only source of control force and moment.
  Ground contact acts as a force only while the Aeronef rests on its landing gear on the ground:
  there the ground reaction of the MS-DYN ground contact model holds it at rest (L1-AER-920, D69). A
  ground contact of the airborne vehicle is classified as a landing or a crash (L1-AER-260 to -280;
  L0-ASM-110) and computes no touchdown shock (D53). Consumed fuel adds no force (L0-ASM-090).
  Children must show (D58): (Inspection) MS-DYN lists these four contributions and no other, with
  the ground reaction only on the ground; (Analysis) the free-fall and terminal-velocity checks of
  L1-AER-010 pass, and at rest on the ground the total force and the total moment are zero.
  Sufficiency: with L1-AER-060 (gravity), -070 (drag) and -920 (ground reaction), this record closes
  the list of forces and moments, which covers the force part of L0-CON-090 and the model side of
  L0-CON-060.
Parent(s):     L0-CON-090, L0-CON-060
Source:        AIRCRAFT_CHARACTERISTICS.md §2, §7; D17, D37, D69
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  standard gravity, so that the hover figure of the glossary entry *Sensed acceleration* is
  exact against the crew limit L0-CON-310 (G0-F25, R-F06). Children must show (D58): (Analysis) simulated free fall in vacuum-equivalent
  conditions matches the closed-form solution.
  Sufficiency: gravity is one of the three effects L0-CON-090 allows; this record fixes its
  model, and L1-AER-050 makes it part of the total force.
Parent(s):     L0-CON-090
Source:        L0-ASM-040; CV-110, CV-180
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-010
TBD/TBR:       P-DYN-010 value TBR (D48, TT-150), Martin, G2 (C1)
Owner:         Martin
Status:        Baselined
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
  (elongated body) is an MS-DYN choice bounded by L1-AER-020. Children must show (D58):
  (Analysis) simulated free fall with drag reaches the closed-form terminal velocity for the
  drag model, with and without wind.
  Sufficiency: drag is the second effect L0-CON-090 allows; this record fixes its dependence on
  the air-relative velocity, which is the part of L0-CON-090 that involves the wind.
Parent(s):     L0-CON-090
Source:        D17, D20; L0-ASM-050, L0-ASM-060
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-080

```req
ID:            L1-AER-080
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall generate each control force and each control moment with its
  effectors.
Rationale:     Fictional force emitters replace engines, wings and control surfaces (OBJECTIVES §2;
  AIRCRAFT_CHARACTERISTICS §3). A control force or moment is any force or moment other than gravity,
  drag and the ground reaction (glossary, CR-B3-02). Children must show (D58): (Inspection) the
  effector requirements and MS-DYN identify the effectors as the only source of control force and
  moment.
  Sufficiency: with L1-AER-050, which makes gravity, drag and, on the ground, the ground reaction
  the only other contributions, this record covers L0-CON-060.
Parent(s):     L0-CON-060
Source:        AIRCRAFT_CHARACTERISTICS.md §3
Allocated to:  EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  Children must show (D58): (Inspection) the effector requirements and MS-DYN define a
  constant body-frame direction for each effector.
  Sufficiency: the effector subsystem is the only place the direction of action is defined, so
  one EF child covers L0-CON-070.
Parent(s):     L0-CON-070
Source:        D19; AIRCRAFT_CHARACTERISTICS.md §3
Allocated to:  EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  AIRCRAFT_CHARACTERISTICS §3, §7). The list is closed. The control effectiveness is the control
  force and control moment about the centre of gravity per unit of effector command, so it
  carries the point of application and the moment arm (glossary). The consumption parameters
  belong to FU (L1-AER-160, -170); they may be common to the effector set rather than one set
  per effector (L2-AER-FU-060). Children must show (D58): (Inspection) each effector parameter in the
  parameter database belongs to one of the five listed kinds.
  Sufficiency: the EF children define the first four kinds and the FU children the fifth;
  together they are the whole effector model, which is what L0-CON-080 constrains.
Parent(s):     L0-CON-080
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §7
Allocated to:  EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  (D58): (Inspection) each effector has a maximum-force parameter; (Test) no automated test run
  produces an effector force above its maximum.
  Sufficiency: EF enforces the limit at the effector, and FC never relies on output beyond it;
  together they keep every effector within its maximum, as L0-CON-300 requires.
Parent(s):     L0-CON-300
Source:        Owner review at G0 (L0-CON-300)
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       Per-effector maximum force values TBD, Martin, G2 (C3)
Owner:         Martin
Status:        Baselined
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
Rationale:     Effector authority budget, weight-bearing direction. Pitch and roll are held at zero
  (D57, which revises D10), so the negative body z axis points up, so this force holds the vehicle
  up and accelerates it vertically. Budget (FUNCTIONAL_ANALYSIS §7.1): [P-SYS-400] is at least the
  maximum vehicle mass times the sum of [P-DYN-010] and [P-SYS-440], plus the vertical drag in a
  climb at [P-SYS-240] at the largest horizontal airspeed (CR-C3-02). The zero side components show
  the independent control of L0-CON-020. The usable force at low mass is capped by the crew limit
  (L1-AER-290), not by this record. Children must show (D58): (Analysis) the effector set produces
  the pure force at maximum mass.
  Sufficiency: with L1-AER-130 (the other five force directions) and L1-AER-140 (moments), this
  record gives a pure control force or moment in each of the six degrees of freedom, as L0-CON-020
  requires.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D19, D46, D57
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-400, P-DYN-010, P-SYS-440, P-SYS-240
TBD/TBR:       P-SYS-400 value TBD (computed when the maximum vehicle mass is known), Martin, G2
  (I1); P-SYS-440 value TBR (TT-040), P-SYS-240 value TBD (TT-010)
Owner:         Martin
Status:        Baselined
Version:       2
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
  directions other than the one in L1-AER-120. Children must show (D58): (Analysis) the
  effector set produces each pure force at maximum mass.
  Sufficiency: see L1-AER-120.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D17, D19
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-410, P-SYS-440, P-SYS-230, P-SYS-430, P-SYS-560
TBD/TBR:       P-SYS-410 value TBD (computed when the maximum vehicle mass is known), Martin, G2
  (I1)
Owner:         Martin
Status:        Baselined
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
  rate [P-SYS-270], plus the drag moment, plus the moment needed to hold pitch and roll at zero
  against that drag moment. Each term is a named line of FUNCTIONAL_ANALYSIS §7.1, sized at I1
  when the inertia and the drag model are known. Pitch and roll are held at zero (D57, which
  revises D10); yaw sets the heading. Children must show (D58): (Analysis) the
  effector set produces each pure moment at maximum inertia.
  Sufficiency: see L1-AER-120.
Parent(s):     L0-CON-020
Source:        N-170, N-240; D19, D57
Allocated to:  EF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-420, P-SYS-270
TBD/TBR:       P-SYS-420 value TBD (computed when the inertia is known), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
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
  L1-AER-660), so that test procedures can start at any fuel state. Children must show (D58):
  (Inspection) the parameter database holds the capacity; (Test) a run started with a stated
  fuel mass reports that mass at its first output sample.
  Sufficiency: with L1-AER-200 (output depends on fuel), this record gives the finite supply
  and the initial-quantity parameter that L0-CON-100 asks for.
Parent(s):     L0-CON-100
Source:        N-150, N-310; CONOPS §4.5
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-010
TBD/TBR:       P-FU-010 value TBD, Martin, G2 (C2, fuel budget §7.3)
Owner:         Martin
Status:        Baselined
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
  separate terms for linear and rotational actuation (L0-CON-120; AIRCRAFT_CHARACTERISTICS §4). The
  form of each relationship is a C2 decision recorded in MS-DYN. Because the effectors counter
  gravity, fuel is consumed in every airborne condition, hover included (CONOPS §4.5). On the
  ground, with the effectors off, no fuel is consumed (D69, L1-AER-930, -940). Children must show
  (D58): (Analysis) the simulated fuel mass flow matches an independent computation from the
  recorded effector outputs.
  Sufficiency: with L1-AER-170 (the parameters are configurable), this record covers both
  relationships of L0-CON-120, and it makes the fuel used depend on effector output (L0-CON-100).
Parent(s):     L0-CON-120, L0-CON-100
Source:        N-280; AIRCRAFT_CHARACTERISTICS.md §4
Allocated to:  FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  (L0-CON-120, N-020). Children must show (D58): (Demonstration) two runs with different values
  of the consumption parameters, and no software change, give the fuel mass flows that each set
  of values predicts.
  Sufficiency: see L1-AER-160.
Parent(s):     L0-CON-120
Source:        N-020, N-280
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-040, P-FU-050
TBD/TBR:       P-FU-040, P-FU-050 values TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Baselined
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
  must show (D58): (Analysis) at each output sample of a run, the reported vehicle mass equals
  the dry mass plus the reported remaining fuel mass.
  Sufficiency: with L1-AER-190 (remaining fuel is the initial fuel minus the integral of the
  flow), this record makes the vehicle mass decrease by the fuel consumed (L0-CON-110).
Parent(s):     L0-CON-110
Source:        N-280; CV-340
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-030, P-FU-010
TBD/TBR:       P-FU-030 value TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Baselined
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
  §10.3. The tolerance covers the numerical integration only. Children must show (D58):
  (Analysis) over the reference mission (SC-110), an independent integration of the recorded
  fuel mass flow agrees with the reported remaining fuel mass within [P-FU-060].
  Sufficiency: see L1-AER-180.
Parent(s):     L0-CON-110
Source:        METHODOLOGY §10.3; N-290
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-060
TBD/TBR:       P-FU-060 value TBD, Martin, G2 (C2)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-200

```req
ID:            L1-AER-200
Level:         L1
Type:          Functional
Statement:     When the remaining fuel mass reaches zero, the Aeronef shall produce zero control
  force and zero control moment.
Rationale:     The output of each effector depends on the availability of fuel (L0-CON-100). Fuel
  exhaustion is nominal behaviour, not a failure (L0-ASM-070): the vehicle then moves under gravity
  and drag alone and keeps its angular rate (CONOPS SC-110 leg 11), and its ground contact is a
  crash (D68, L1-AER-270). What autoflight annunciates after exhaustion is set at L2 (C5, D68).
  Children must show (D58): (Test) in the reference mission, each effector output is zero from the
  first sample at which the remaining fuel mass is zero.
  Sufficiency: with L1-AER-150 and -160, this record ties every effector output to the fuel supply
  (L0-CON-100).
Parent(s):     L0-CON-100
Source:        N-150; CONOPS §4.5, SC-110; D68
Allocated to:  EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  show (D58): (Inspection) MS-DYN and the mass-properties requirements give one centre-of-gravity
  position for every fuel mass.
  Sufficiency: FU defines the mass distribution and DYN uses the centre of gravity as origin;
  both fixing it covers L0-CON-130.
Parent(s):     L0-CON-130
Source:        AIRCRAFT_CHARACTERISTICS.md §4
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-220

```req
ID:            L1-AER-220
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall derive, at each fuel state, a diagonal inertia tensor in the body
  frame from the body shape and the mass distribution that MS-DYN states.
Rationale:     The shape matters only through its mass properties (L0-CON-140;
  AIRCRAFT_CHARACTERISTICS §1, §4). The body axes are the principal axes of inertia, so the
  products of inertia are zero and the tensor is diagonal (D61); a rotation about one body axis
  then produces no torque about another, which supports L1-AER-020. L0-CON-140 describes the
  concept as an elongated shape with a simplified mass distribution; at L1 the shape and the
  distribution are the ones MS-DYN states, with their dimensions as DYN parameters (C1).
  Whether the inertia changes with the fuel state is a C2 decision; this record requires that
  the answer be stated for each fuel state. The body shape is provisional (TBR in L0-CON-140).
  Children must show (D58): (Inspection) MS-DYN derives each principal moment of inertia from
  the stated shape and distribution, and states zero products of inertia with the CV-350 sign
  convention.
  Sufficiency: one derivation covers L0-CON-140; the fuel-state dependence closes the question
  L0-CON-140 leaves to the mass-properties requirements.
Parent(s):     L0-CON-140
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §4; CV-350; D61
Allocated to:  FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       Body shape provisional (L0-CON-140), Martin, 2026-11-30
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-230

```req
ID:            L1-AER-230
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have no electrical power generation, distribution or consumption
  function.
Rationale:     Owner review (2026-11-04): deleted. No requirement is written for a system the
  Aeronef does not have; the design simply does not include it (D54). L0-CON-160 is now a leaf
  checked directly (CR-B1-04). Original rationale: Electrical power is outside the modelling
  scope (L0-CON-160; AIRCRAFT_CHARACTERISTICS §4, §7). The effectors draw only on fuel (L1-AER-160). Children must
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
Status:        Deleted
Version:       2
```

### L1-AER-240

```req
ID:            L1-AER-240
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have its nose on the positive body x axis.
Rationale:     The nose marks the designated forward direction (L0-CON-150), which fixes the body x
  axis (CV-170) and the heading (CV-530). Children must show (D58): (Inspection) the MS-DYN
  geometry places the nose on the positive body x axis.
  Sufficiency: with L1-AER-250 (crew station), this record gives the forward direction and the
  crew position that L0-CON-150 asks for.
Parent(s):     L0-CON-150
Source:        AIRCRAFT_CHARACTERISTICS.md §1; CV-170
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  gravity (D45, L1-AER-290), not here. Children must show (D58): (Inspection) the MS-DYN geometry states the crew
  station position.
  Sufficiency: see L1-AER-240.
Parent(s):     L0-CON-150
Source:        AIRCRAFT_CHARACTERISTICS.md §1; CV-170
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-400
TBD/TBR:       P-DYN-400 value TBD, Martin, G2 (C1)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-260

```req
ID:            L1-AER-260
Level:         L1
Type:          Functional
Statement:     When the Aeronef makes ground contact on its extended landing gear within the landing
  envelope with fuel remaining, the Aeronef shall report a landing in its operational data.
Rationale:     Ideal landing on the gear (D37 revised by D69, L0-CON-290, L0-ASM-110): a contact of
  the extended gear within the envelope (L1-AER-280) is a landing. The gear is ideal. The vehicle
  comes to rest on it at the contact step and stays there until liftoff (L1-AER-920), and the run
  goes on. A contact after fuel exhaustion is a crash (D68, D73), so fuel remaining is part of the
  condition. Children must show (D58): (Test) a descent to the ground on the extended gear, within
  the envelope and with fuel remaining, produces one landing event at the contact sample and no
  crash event.
  Sufficiency: with L1-AER-270 (crash), -280 (envelope), -900 (gear) and -920 (rest on the ground),
  this record defines ground contact, the envelope and both outcomes, as L0-CON-290 requires.
Parent(s):     L0-CON-290
Source:        D8, D37, D68, D69, D73; CONOPS §4.2, §4.6, SC-130
Allocated to:  DYN, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-270

```req
ID:            L1-AER-270
Level:         L1
Type:          Functional
Statement:     When the Aeronef makes a ground contact that is outside the landing envelope, or with
  its landing gear not extended, or at fuel exhaustion, the Aeronef shall report a crash in its
  operational data.
Rationale:     A ground contact that is not a landing (L1-AER-260) is a crash, which ends the run
  (D37, D68, D69, L0-CON-290). The three conditions are the complement of those of L1-AER-260, so
  the two records partition the contacts (D30). They are: a contact outside the speed envelope; a
  contact with the gear retracted or in transit, so that the body or a moving gear meets the ground;
  and a contact after fuel exhaustion (D68). The owner confirmed that the last two are crashes
  whatever the speed (D73). The reference mission ends this way after fuel exhaustion (SC-110).
  Children must show (D58): (Test) each of the following produces one crash event at the contact
  sample: a free fall to the ground from fuel exhaustion, a contact just outside each speed limit,
  and a contact with the gear retracted within the speed limits.
  Sufficiency: see L1-AER-260.
Parent(s):     L0-CON-290
Source:        D37, D68, D69, D73; CONOPS SC-110
Allocated to:  DYN, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-280

```req
ID:            L1-AER-280
Level:         L1
Type:          Functional
Statement:     The Aeronef shall classify a ground contact as within the landing envelope when the
  vertical speed magnitude is at most [P-SYS-500] and the horizontal speed is at most
  [P-SYS-510] at the contact sample.
Rationale:     The envelope limits the velocity at contact (L0-CON-290, D37). The two limits are one
  envelope, so they are one requirement (D30). There is no acceleration limit: the ideal landing
  gear computes no touchdown shock, and the vertical speed limit stands in for the impact (D53, D69,
  #100). The gear position and the fuel are conditions of a landing, not part of the envelope
  (L1-AER-260, -270). Children must show (D58): (Test) contacts on each side of each limit are
  classified correctly.
  Sufficiency: see L1-AER-260.
Parent(s):     L0-CON-290
Source:        D37, D53
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (owner, #100), Martin, G2
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-290

```req
ID:            L1-AER-290
Level:         L1
Type:          Performance
Statement:     While the Aeronef is airborne, the Aeronef shall keep the magnitude of the sensed
  acceleration at the centre of gravity at most [P-SYS-120].
Rationale:     Crew g-limit (L0-CON-310, D38). L0 leaves the evaluation point to a lower level; the
  owner chose the centre of gravity (D45, #97), which keeps the limit simple. Budget
  (FUNCTIONAL_ANALYSIS §7.2): [P-SYS-120] is at least [P-DYN-010] (holding the vehicle up) plus
  [P-SYS-440] (vehicle acceleration), with the rest as margin. As fuel burns, the allowed resultant
  control force falls with the mass (D38); FC owns that limit, AF keeps its manoeuvres within
  [P-SYS-440], and FU supplies the mass. Children must show (D58): (Test) in every automated test
  run, at every fuel state, while airborne, the sensed acceleration at the centre of gravity does
  not exceed [P-SYS-120]. The budget closes for the winds the TST applies, which stay within the
  wind envelope, whose gusts build up over at least [P-SYS-570] (D51, D62, FUNCTIONAL_ANALYSIS
  §7.2).
  Sufficiency: with L1-AER-300 (vehicle acceleration limit), this record covers L0-CON-310. The
  ideal landing gear computes no touchdown shock (D53, D69), so contact adds no further share. At
  rest on the ground the sensed acceleration is that of the ground reaction, [P-DYN-010] upward,
  which is within the limit (L1-AER-920).
Parent(s):     L0-CON-310
Source:        D38; N-170
Allocated to:  FC, AF, FU, DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-120, P-DYN-010, P-SYS-440, P-SYS-570
TBD/TBR:       P-DYN-010 value TBR (TT-150), P-SYS-440 value TBR (TT-040), P-SYS-570 value TBD
  (TT-650), Martin, G2
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-300

```req
ID:            L1-AER-300
Level:         L1
Type:          Performance
Statement:     While the Aeronef is airborne with fuel remaining in a wind within the wind envelope,
  the Aeronef shall keep the magnitude of its vehicle acceleration at most [P-SYS-440].
Rationale:     Manoeuvres are g-limited, and the maximum acceleration and deceleration are design
  parameters (D16). This record is the vehicle-acceleration share of the crew budget
  (L1-AER-290, FUNCTIONAL_ANALYSIS §7.2). Its split: the autoflight manoeuvre limit [P-AF-200]
  plus the flight-control transient allowance [P-FC-020] is at most [P-SYS-440]. The transient
  allowance also covers the response to a gust: the wind envelope bounds the steady wind
  [P-SYS-430] and the gusts [P-SYS-560], and each gust builds up over at least [P-SYS-570], so the
  drag changes at a bounded rate that FC can follow within the control-loop latency [P-SYS-480]
  (D51, D62). It also bounds the effector authority budget (L1-AER-120, -130). Children must
  show (D58): (Test) in every automated test run, while fuel remains, in winds within the wind
  envelope including gusts of the shortest rise time, the vehicle acceleration does not exceed
  [P-SYS-440].
  Sufficiency: see L1-AER-290.
Parent(s):     L0-CON-310
Source:        D16, D38, D51, D62; N-170
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-440, P-AF-200, P-FC-020, P-SYS-430, P-SYS-560, P-SYS-570, P-SYS-480
TBD/TBR:       P-SYS-440, P-AF-200, P-FC-020 values TBR (D48, TT-040); P-SYS-570 value TBD (D62,
  TT-650), Martin, G2
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-310

```req
ID:            L1-AER-310
Level:         L1
Type:          Performance
Statement:     While in level flight in the operating volume in a wind within the wind envelope, the
  Aeronef shall be able to sustain each horizontal speed up to [P-SYS-230] under autoflight.
Rationale:     Performance envelope (N-170, CONOPS §5). The crew needs known limits to plan, and
  [P-SYS-230] is the top of the selectable horizontal speed, which runs from zero to the maximum
  (D56). The record states a capability, not a state the Aeronef is always in: the holds and the
  selected speeds below the maximum stay valid. How closely a selected speed is tracked is a
  per-mode tolerance set at L2 (C5, P-AF-120). The operating volume is bounded below by the minimum
  operating height above the ground [P-SYS-210] (CV-400), above by the altitude [P-SYS-200] and
  horizontally by [P-SYS-220], and the wind envelope by [P-SYS-430], [P-SYS-560] and the gust rise
  time [P-SYS-570] (glossary; D51, D62). Horizontal speed is ground-referenced (CV-480), so a
  headwind raises the airspeed and the drag the effectors must overcome; that is why the wind limit
  enters the authority budget (L1-AER-130). Children must show (D58): (Test) the vehicle reaches and
  holds horizontal speeds up to and including [P-SYS-230] in level flight at the lowest altitude of
  the operating volume and at [P-SYS-200], into a steady wind of [P-SYS-430] with gusts of
  [P-SYS-560] built up over [P-SYS-570].
  Sufficiency: with L1-AER-320, -330 (vertical speeds), -350 (heading rate) and -360 (endurance),
  this record sets the aircraft-level envelope inside which the modes of the catalogue operate
  (L0-OBJ-030).
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS §4.2, §5; D51, D56, D62
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-230, P-SYS-200, P-SYS-210, P-SYS-220, P-SYS-430, P-SYS-560, P-SYS-570
TBD/TBR:       P-SYS-200, P-SYS-210, P-SYS-220, P-SYS-230 values TBD (D47, TT-010), Martin, G2
  (I1); P-SYS-430, P-SYS-560 values TBR (D51, TT-030), Martin, G2; P-SYS-570 value TBD (D62,
  TT-650), Martin, G2
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-320

```req
ID:            L1-AER-320
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall be able to climb at each vertical speed
  up to [P-SYS-240] under autoflight.
Rationale:     Performance envelope (N-170). The Aeronef can climb with no horizontal motion and
  without tilting (SC-040). [P-SYS-240] is the top of the selectable climb vertical speed (D56);
  the record is a capability, and the tracking tolerance of a selected vertical speed is set at
  L2 (C5, P-AF-090). The value bounds the upward authority budget (L1-AER-120). Children must
  show (D58): (Test) the vehicle reaches and holds climb vertical speeds up to and including
  [P-SYS-240], at zero and at maximum horizontal speed.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-040
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-240
TBD/TBR:       P-SYS-240 value TBD (D47, TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-330

```req
ID:            L1-AER-330
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall be able to descend at each vertical
  speed magnitude up to [P-SYS-250] under autoflight.
Rationale:     Performance envelope (N-170). Descent has its own limit, like climb (D56: Go to
  altitude and Vertical speed work in both senses). The record is a capability; the tracking
  tolerance of a selected vertical speed is set at L2 (C5, P-AF-090). Where a descent levels off is
  mode logic, not part of this record: Go to altitude and Vertical speed arm Altitude hold, which
  levels off at the selected altitude (D56), and the selectable altitude is bounded below by the
  altitude at which the height above the ground is [P-SYS-210] at level attitude, that is
  [P-SYS-210] plus half of [P-DYN-030] (CV-400; L2, C8). Children must show (D58): (Test) the
  vehicle reaches and holds descent vertical speed magnitudes up to and including [P-SYS-250], at
  zero and at maximum horizontal speed.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-020
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-250, P-SYS-210, P-DYN-030
TBD/TBR:       P-SYS-250, P-SYS-210 values TBD (D47, TT-010), Martin, G2 (I1); P-DYN-030 value TBR
  (TT-740)
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-340

```req
ID:            L1-AER-340
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall sustain a flight path angle of
  magnitude [P-SYS-260] under autoflight.
Rationale:     Owner review (2026-11-04): deleted. The flight path angle mode is dropped from the catalogue (D56), so no flight path angle capability is required. Original rationale: Performance envelope (N-170). The flight path angle depends on velocity only
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
Status:        Deleted
Version:       2
```

### L1-AER-350

```req
ID:            L1-AER-350
Level:         L1
Type:          Performance
Statement:     While in the operating volume, the Aeronef shall be able to change its heading at each
  heading rate magnitude up to [P-SYS-270] under autoflight.
Rationale:     Performance envelope (N-170). Heading rate is dψ/dt (CV-290). Heading is
  independent of track on the Aeronef (CV-550), so a heading change does not change the
  direction of motion unless a mode asks for it (L2). The record is a capability; the heading
  rate a mode commands is set at L2 (C5). The value bounds the moment authority budget
  (L1-AER-140). The crew limit is evaluated at the centre of gravity, so rotation adds no share
  to the crew budget (D45, FUNCTIONAL_ANALYSIS §7.2). Children must show (D58): (Test) heading
  changes at heading rates up to and including [P-SYS-270], at maximum inertia.
  Sufficiency: see L1-AER-310.
Parent(s):     L0-OBJ-030
Source:        N-170; CONOPS SC-050, SC-060
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-270
TBD/TBR:       P-SYS-270 value TBD (D47, TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-360

```req
ID:            L1-AER-360
Level:         L1
Type:          Performance
Statement:     When autoflight takes off from the ground with an initial fuel mass of [P-FU-010] and
  then holds the horizontal position and the hover height with no wind applied, the Aeronef shall
  stay airborne with fuel remaining for at least [P-SYS-280] from the start of the takeoff.
Rationale:     Fuel budget (FUNCTIONAL_ANALYSIS §7.3). Runs start on the ground (D69), so the
  endurance from full fuel begins with a takeoff: a climb to the hover height and the gear
  retraction, followed by Hover (D69). Holding the horizontal position and the hover height in still
  air is the condition in which the effectors only counter gravity. It therefore sets the endurance
  at full fuel and maximum mass (CONOPS SC-110 variation). With no wind and no motion there is no
  drag. With a consumption proportional to force, [P-FU-010] must be at least [P-FU-030] times the
  exponential of the product of the translational consumption coefficient [P-FU-040], [P-DYN-010]
  and [P-SYS-280], minus one (L2-AER-FU-290). The fuel of the takeoff is a small part of the margin
  [P-FU-100]: it covers a climb of [P-AF-210] minus [P-DYN-040] at [P-AF-240] and the gear
  retraction. Stationary with Altitude hold, which this record also covered before D69, now needs a
  climb first and is not the endurance case. Children must show (D58): (Test) from a ground start at
  full fuel, the time from the takeoff to fuel exhaustion while autoflight holds the horizontal
  position and the hover height in still air is at least [P-SYS-280].
  Sufficiency: the finite supply of L0-CON-100 must still allow useful missions. This record turns
  that into a measurable endurance, and with L1-AER-310 to -350 and -960 it completes the envelope
  for L0-OBJ-030.
Parent(s):     L0-CON-100, L0-OBJ-030
Source:        N-150, N-250; CONOPS SC-110; D69
Allocated to:  FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-010, P-SYS-280, P-FU-030, P-FU-040, P-DYN-010, P-FU-100, P-AF-210, P-DYN-040,
  P-AF-240
TBD/TBR:       P-SYS-280 value TBR (TT-800), P-FU-010, P-FU-030, P-FU-040, P-FU-100 values TBR
  (TT-110, TT-120, TT-790), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       2
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
  (D42). Children must show (D58): (Test) after a step in the reference of each degree of
  freedom, that degree of freedom settles on its reference within the tracking tolerance and the
  settling time that the FC children state as parameters (C4); the other degrees of freedom stay
  within the L1-AER-380 tolerances.
  Sufficiency: with L1-AER-380 (independence) and -440 (state), this record gives a regulation
  requirement for each of the six degrees of freedom (L0-OBJ-020), each acting on its own
  (L0-CON-020).
Parent(s):     L0-OBJ-020, L0-CON-020
Source:        N-240; AIRCRAFT_CHARACTERISTICS.md §5
Allocated to:  FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-380

```req
ID:            L1-AER-380
Level:         L1
Type:          Performance
Statement:     When the reference of one degree of freedom changes, the Aeronef shall keep the
  velocity along each other body axis within [P-SYS-540] of its reference and the body rate about
  each other body axis within [P-SYS-550] of its reference.
Rationale:     Measurable form of independent control authority (L0-CON-020) and of the absence
  of cross-axis coupling (L0-CON-030, D18): a manoeuvre on one axis leaves the others where they
  were. The tolerances apply in the body frame, the frame in which D18 states the absence of
  coupling; with pitch and roll at zero the body z axis is the local vertical (D57), and in
  Heading the body x and y axes turn with the heading (D56). The two tolerances are the
  cross-axis budget shared by FC (regulation and allocation) and EF (the effector geometry that
  lets a pure force or moment be produced). Children must show (D58): (Test) for a step on each
  degree of freedom in turn, the other five stay within the tolerances.
  Sufficiency: see L1-AER-370.
Parent(s):     L0-CON-020, L0-OBJ-020
Source:        N-240; D18
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-540, P-SYS-550
TBD/TBR:       P-SYS-540, P-SYS-550 values TBD (TT-100), Martin, G2 (C4)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-390

```req
ID:            L1-AER-390
Level:         L1
Type:          Performance
Statement:     While the Aeronef is airborne with fuel remaining, the Aeronef shall hold its pitch
  angle and its roll angle within [P-AF-180] of zero.
Rationale:     Owner decision D57 (which revises D10): the dynamics keep all six degrees of freedom,
  but pitch and roll are not used for now and are held at zero at all times; the craft translates
  along three axes and rotates about the vertical axis only. This is a rule for every mode, not a
  mode definition, so it is stated once at aircraft level; the heading behaviour of each mode is L2
  (D33; the ConOps reading is parked for C5 under #89). The record applies while fuel remains: at
  fuel exhaustion the effectors produce no moment (L1-AER-200), so the attitude is then free and
  keeps the angular rate it had (CONOPS SC-110). Level attitude also keeps the negative body z axis
  pointing up for the upward authority budget (L1-AER-120). Children must show (D58): (Test) in each
  automated test run, while fuel remains, the pitch and roll angles stay within [P-AF-180]. On the
  ground the landing gear holds the attitude level (L1-AER-920), so the record needs no on-ground
  case.
  Sufficiency: the attitude references come from AF and are held by FC; both children together give
  the predictable attitude the autoflight operating concept needs (L0-OBJ-030, N-160) while keeping
  attitude independent of translation (L0-CON-020).
Parent(s):     L0-OBJ-030, L0-CON-020
Source:        D57; N-160
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-AF-180
TBD/TBR:       P-AF-180 value TBR (TT-190), Martin, G2 (C5)
Owner:         Martin
Status:        Baselined
Version:       2
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
  must show (D58): (Demonstration) a test variant of the control-law design is selected through
  the configuration, the run uses it, and the vehicle model files have unchanged checksums.
  Sufficiency: with L1-AER-420 (common FC-AF interface) and -430 (vehicle-model boundary), this
  record makes the control law replaceable without modifying the vehicle model (L0-CON-200).
Parent(s):     L0-CON-200
Source:        N-230; D15, D42
Allocated to:  FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  implementation (D24). Children must show (D58): (Demonstration) a test variant of the
  autoflight implementation is selected through the configuration, the run uses it, and the
  vehicle model files have unchanged checksums.
  Sufficiency: with L1-AER-420 and -430, this record covers L0-CON-210.
Parent(s):     L0-CON-210
Source:        N-220; D15, D24
Allocated to:  AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-420

```req
ID:            L1-AER-420
Level:         L1
Type:          Interface
Statement:     The Aeronef shall pass the axis references from autoflight to flight control through
  the one interface defined in ICD-FC-AF, for each flight-control-law design and each autoflight
  implementation.
Rationale:     Modes and controllers are decoupled: any autoflight implementation pairs with any
  control law behind a common mode logic (D15, #72). A single interface is what makes that true.
  Only the axis references cross it (FUNCTIONAL_ANALYSIS I-13): flight control receives no mode
  information, so no control law can depend on the mode logic (D15, D33). On the ground the axis
  references take an off value, with which flight control commands zero effector output (the
  effectors off, D69, L1-AER-930); the off value carries no mode information. Children must show
  (D58): (Inspection) the FC and AF requirements each cite ICD-FC-AF as their only mutual interface;
  (Demonstration) the test variants of L1-AER-400 and -410 run against the same interface.
  Sufficiency: see L1-AER-400 and L1-AER-410.
Parent(s):     L0-CON-200, L0-CON-210
Source:        D15
Allocated to:  FC, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-430

```req
ID:            L1-AER-430
Level:         L1
Type:          Interface
Statement:     The Aeronef shall exchange data between its vehicle model and its flight software
  only as effector commands and the landing gear command into the vehicle model and as vehicle
  state, gear state, mass properties and fuel state out of it.
Rationale:     A fixed vehicle-model boundary is what lets the control law and the autoflight be
  replaced without modifying the vehicle model (L0-CON-200, -210). The list is closed. The landing
  gear is part of the vehicle model (DYN, D69). Autoflight commands it, retracting it in Takeoff and
  extending it in Land, and reads the gear state: the gear position and whether the vehicle is on
  the ground (glossary). The gear state is the perfect-knowledge counterpart of a weight-on-gear
  signal (L0-ASM-010). Mass properties are the vehicle mass, the centre-of-gravity position and the
  inertia tensor (glossary), so that FC can use the inertia as it changes with fuel (L1-AER-220).
  The data definitions go in a vehicle-model boundary ICD (IN-B1-01, I1). TM observes the boundary
  without being a party to it (FUNCTIONAL_ANALYSIS §5). Children must show (D58): (Inspection) each
  data item crossing the boundary in the DYN, FU, EF, FC, AF, FCP and NAV requirements is one of the
  listed kinds and is defined in the ICD.
  Sufficiency: see L1-AER-400 and L1-AER-410.
Parent(s):     L0-CON-200, L0-CON-210
Source:        TESTING_ENVIRONMENT.md §2; D15, D55
Allocated to:  DYN, FU, EF, FC, AF, FCP, NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       2
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
  upgrade (#83). Children must show (D58): (Test) the state the navigation and flight-control
  functions receive equals the recorded vehicle state of the frame-start step.
  Sufficiency: regulation (L0-OBJ-020) and guidance (L0-OBJ-030) need the state; with
  L1-AER-370 and -530 this record supplies it on a defined basis.
Parent(s):     L0-OBJ-020, L0-OBJ-030
Source:        L0-ASM-010; METHODOLOGY §4.4
Allocated to:  DYN, NAV, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-450

```req
ID:            L1-AER-450
Level:         L1
Type:          Functional
Statement:     The Aeronef shall guide its translation and its heading toward the targets the crew
  selects, through the autoflight modes of the mode catalogue.
Rationale:     Autoflight is the primary means of operating the Aeronef (L0-OBJ-030, N-050). The
  catalogue is plan decision D56, extended by D69: independent horizontal modes (Stationary,
  Heading) and vertical modes (Altitude hold, Go to altitude, Vertical speed), plus Go to hover,
  Hover, Takeoff and Land, which govern both axes. Arming, capture and transitions, and the
  annunciation labels, are defined at L2 by AF (C5, D33). This record states only the aircraft-level
  capability. Children must show (D58): (Inspection) each mode of the catalogue is covered by an AF
  requirement that traces to this record, and the mode logic is specified in AF_MODE_LOGIC.
  Sufficiency: with L1-AER-460 (position accuracy budget), -470 (annunciation), -480 (selections),
  -530 and -890 (navigation), -880 (panel interface) and the envelope L1-AER-310 to -360, and the
  takeoff and landing capabilities L1-AER-960 and -970, this record covers the autoflight objective
  at aircraft level; the per-mode coverage is shown at L2.
Parent(s):     L0-OBJ-030
Source:        N-050, N-190; D33, D56, D69
Allocated to:  AF, NAV, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-460

```req
ID:            L1-AER-460
Level:         L1
Type:          Performance
Statement:     While autoflight holds the horizontal position over the ground in a wind within the
  wind envelope, the Aeronef shall keep its horizontal position within [P-SYS-450] of the
  reference position at each output sample that follows the start of the hold by at least
  [P-SYS-460].
Rationale:     Position error budget (FUNCTIONAL_ANALYSIS §7.4), the aircraft-level accuracy of
  the hold capability (N-130, D17). The budget is a horizontal position error, in Stationary and
  in Hover, whatever the vertical mode with Stationary (D60); the altitude error is covered
  separately by the altitude-hold tolerance [P-AF-110] at L2. Split: the autoflight guidance
  share [P-AF-160] plus the translational regulation share [P-FC-010] is at most [P-SYS-450]; the
  navigation share is zero under perfect state knowledge (L1-AER-440). The wind envelope bounds
  the steady wind [P-SYS-430] and the gusts [P-SYS-560], and each gust builds up over at least
  [P-SYS-570] (D51, D62), so the gust response falls inside the FC share. Which position is the
  reference is L2 (C5, #78); Hover begins its hold once the craft is stationary at the hover
  height (D56). Children must show (D58): (Test) holds in zero wind, and in a steady wind of
  [P-SYS-430] with gusts of [P-SYS-560] built up over [P-SYS-570] from several directions, keep
  the horizontal position within [P-SYS-450] of the reference position at each output sample
  from [P-SYS-460] after the start of the hold, in Stationary with each vertical mode and in
  Hover.
  Sufficiency: L0-OBJ-020 needs regulation accuracy and L0-OBJ-030 a usable hold; this record
  sets the one aircraft-level number both are measured against.
Parent(s):     L0-OBJ-030, L0-OBJ-020
Source:        N-130, N-140; D17, D51, D56, D60, D62; METHODOLOGY §12
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-450, P-SYS-460, P-AF-160, P-FC-010, P-AF-110, P-SYS-430, P-SYS-560, P-SYS-570
TBD/TBR:       P-SYS-450, P-AF-160, P-FC-010 values TBR (D48, TT-050), Martin, G2; P-SYS-460 value
  TBD (TT-060), Martin, G2 (C5); P-SYS-430, P-SYS-560 values TBR (D51, TT-030), Martin, G2;
  P-SYS-570 value TBD (D62, TT-650), Martin, G2
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-470

```req
ID:            L1-AER-470
Level:         L1
Type:          Performance
Statement:     When the mode state, a target or the landing gear position changes, the Aeronef shall
  annunciate the new mode state, target or gear position to the crew within [P-SYS-470].
Rationale:     The crew needs to know which mode is active, which is armed and what the vehicle will
  do next (N-060, N-210); annunciations are data items of the crew interface (L0-CON-170). The
  landing gear position (extended, retracted, in transit) is annunciated too, because a landing
  needs the gear extended (L1-AER-260) and the crew needs to know what the vehicle will do next
  (N-060). AF passes it to FCP as annunciation content, from the gear state (L1-AER-430, -880). The
  mode state covers the armed and active modes and whether autoflight is engaged (glossary), so a
  mode that arms, becomes active, leaves the armed state or is disengaged is a change of mode state.
  Timing budget (FUNCTIONAL_ANALYSIS §7.5): [P-SYS-470] is at least two control frames [P-SYS-310]
  plus one output sample period [P-TM-010]. AF decides the content and its share is [P-AF-060]; the
  flight control panel (FCP) presents it at each output sample (L1-AER-490), so the FCP share is one
  output sample period [P-TM-010] (D55). The labels are L2 (C5). Children must show (D58): (Test)
  each change of mode state or target in the mode-transition tests is annunciated within
  [P-SYS-470].
  Sufficiency: with L1-AER-490 (output as data), this record makes the crew interface carry the
  autoflight state (L0-CON-170) that operating by autoflight requires (L0-OBJ-030).
Parent(s):     L0-OBJ-030, L0-CON-170
Source:        N-060, N-210; CONOPS §4.4
Allocated to:  AF, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-470, P-SYS-310, P-TM-010, P-AF-060
TBD/TBR:       P-SYS-470, P-SYS-310, P-TM-010 values TBR (D48, TT-070), P-AF-060 value TBD
  (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-480

```req
ID:            L1-AER-480
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept each crew selection of a mode or a target as a time-stamped
  data item of the crew interface defined in ICD-AER-TST.
Rationale:     The crew interface is data, with no model of physical controls (L0-CON-170). A human
  through the TST, a test procedure and an RVS agent all use the same interface (L0-ASM-120, N-320,
  SC-230), so a scripted selection at a given time behaves as an interactive one. The selections are
  those of the flight control panel: a button that engages each mode, Takeoff and Land included, and
  the heading, horizontal speed, target altitude and vertical speed selectors (D56, D69, D71). The
  panel is its own subsystem, FCP (D55, #80.3); its content is set by D71 (#79). Children must show
  (D58): (Test) a selection scripted at a stated simulation time and the same selection made
  interactively at that time give the same pass/fail verdict on the scenario's success criteria
  (D59).
  Sufficiency: with L1-AER-490 (output side) and -510 (no device or format), this record makes each
  crew selection a data item, as L0-CON-170 requires, and gives autoflight its crew input
  (L0-OBJ-030).
Parent(s):     L0-CON-170, L0-OBJ-030
Source:        N-300, N-320, N-360; L0-ASM-120
Allocated to:  FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-490

```req
ID:            L1-AER-490
Level:         L1
Type:          Interface
Statement:     The Aeronef shall output its annunciations and indications as data items of the crew
  interface defined in ICD-AER-TST, at each output sample.
Rationale:     The crew receives annunciations and indications as data (L0-CON-170). The
  indications are the vehicle quantities the crew sees: altitude, vertical speed,
  horizontal speed, heading, track and remaining fuel (CONOPS §4.3; glossary *Indication*). FCP
  owns the presentation (D55); AF, NAV and FU supply the content across the panel interface
  (L1-AER-880, FUNCTIONAL_ANALYSIS §5).
  Children must show (D58): (Inspection) each annunciation and indication is defined as a data
  item in ICD-AER-TST; (Test) the data items are present at each output sample.
  Sufficiency: see L1-AER-480.
Parent(s):     L0-CON-170
Source:        N-060, N-380; CONOPS §4.3
Allocated to:  FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-500

```req
ID:            L1-AER-500
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall state each crew selection and each annunciated or indicated quantity
  in the crew-facing unit that CONVENTIONS CV-740 assigns to it.
Rationale:     North American aviation units for everything the crew selects or sees (D7, D9,
  D34; L0-CON-270). The unit rule and its limits are CV-760. The conversion to and from SI is
  L1-AER-870 (split from this record at G1, D30). Display resolution and rounding are L2
  (CV-780, #55). Children must show (D58): (Inspection) each crew selection and each crew-facing
  output in the FCP requirements names its CV-740 unit.
  Sufficiency: FCP owns both the selection and the presentation side of the crew interface
  (D55), so with L1-AER-870 (conversion) it covers every crew-facing quantity of L0-CON-270.
Parent(s):     L0-CON-270
Source:        N-070; D7, D9, D34; CV-740 to CV-770
Allocated to:  FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  not change this boundary. A display format is the layout, graphics and symbology of the
  shown data (glossary); the value resolution and rounding of a crew-interface data item
  (CV-780) are not a display format, so the FCP requirements on them do not breach this
  record. This is a leaf at L1: it is checked directly over the whole Aeronef
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
Status:        Baselined
Version:       1
```

### L1-AER-520

```req
ID:            L1-AER-520
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall take each crew input through the flight control panel data of its
  crew interface and through no direct manual flight control.
Rationale:     The flight control panel is the only crew input (L0-CON-180, D55): there is no stick
  or yoke. No manual-control requirement is written at L1 (D49). Leaf at L1, checked directly
  over the Aeronef branch.
  Sufficiency: one inspection over the branch covers L0-CON-180.
Parent(s):     L0-CON-180
Source:        L0-CON-180; D49, D55
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: no requirement of the Aeronef branch at L1 or
  below defines a direct manual flight control, and each crew input requirement cites the crew
  interface, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-530

```req
ID:            L1-AER-530
Level:         L1
Type:          Functional
Statement:     The Aeronef shall compute, at each control frame, its altitude, height above the
  ground, horizontal speed, vertical speed, heading and track from its vehicle state, as CONVENTIONS
  CV-400 to CV-550 define them.
Rationale:     Navigation function F-AER-09: one definition of each guidance quantity, used by
  autoflight, the crew indications and the operational data (FUNCTIONAL_ANALYSIS §5.2). Validity
  thresholds for track and heading are NAV requirements (CV-580). There is no flight path angle and
  no VOR quantity (D56). The height above the ground (CV-400, D70) is the guidance quantity of Go to
  hover, Hover, Takeoff and Land; it uses the body geometry [P-DYN-020] and [P-DYN-030]. Autoflight
  receives the quantities across ICD-NAV-AF (L1-AER-890). Children must show (D58): (Analysis) each
  computed quantity matches an independent computation from the recorded state, inside the validity
  range of CV-580.
  Sufficiency: this record gives autoflight every quantity the mode catalogue guides (L0-OBJ-030).
Parent(s):     L0-OBJ-030
Source:        N-190; CV-400 to CV-580; D70
Allocated to:  NAV
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-540

```req
ID:            L1-AER-540
Level:         L1
Type:          Functional
Statement:     While the vehicle is within the reception range [P-NAV-050] of a VOR station, the
  Aeronef shall compute its radial from that station, the TO/FROM sense, the course deviation from
  the selected course and the horizontal distance to the station.
Rationale:     Owner review (2026-11-04): deleted. VOR radial tracking and the VOR function are dropped (D56). Original rationale: The catalogue includes VOR radial tracking (D3). Ideal VOR (D12): fixed stations,
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
Status:        Deleted
Version:       2
```

### L1-AER-550

```req
ID:            L1-AER-550
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept from the TST, at the start of each run, the identifier and
  the position in the local reference frame of each VOR station of the run.
Rationale:     Owner review (2026-11-04): deleted. VOR radial tracking and the VOR function are dropped (D56). Original rationale: Stations are part of the world definition that the TST sets per run (CONOPS §4.2,
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
Status:        Deleted
Version:       2
```

### L1-AER-560

```req
ID:            L1-AER-560
Level:         L1
Type:          Functional
Statement:     The Aeronef shall indicate its remaining fuel mass to the crew at each output sample.
Rationale:     The crew needs to see how much fuel is left (N-150); the finite supply bounds every
  mission (L0-CON-100), and the indication is a data item of the crew interface (L0-CON-170).
  It is shown in lb (D9, L1-AER-500). Children must show (D58): (Test) the indicated fuel equals
  the remaining fuel mass converted to lb, at each output sample.
  Sufficiency: with L1-AER-570 and -580 (alerts), this record makes the fuel state known to the
  crew, which completes the crew side of L0-CON-100 through the interface of L0-CON-170.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; D9; CONOPS §4.3, §4.5
Allocated to:  FU, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  threshold is a fraction (CV-720). The alert label is L2. Children must show (D58): (Test) in
  the reference mission, the alert appears within [P-SYS-470] of the first sample below the
  threshold.
  Sufficiency: see L1-AER-560.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  FU, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-FU-020, P-FU-010, P-SYS-470
TBD/TBR:       P-FU-020 value TBR (D48, TT-130), Martin, G2
Owner:         Martin
Status:        Baselined
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
  effectors stop (L1-AER-200), and the ground contact that follows is a crash (D68). What autoflight
  annunciates then is set at L2 (C5, D68). Children must show (D58): (Test) in the reference
  mission, the annunciation appears within [P-SYS-470] of the first sample with zero fuel.
  Sufficiency: see L1-AER-560.
Parent(s):     L0-CON-100, L0-CON-170
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  FU, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-470
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  (CV-820, CV-840), is what makes that correlation possible. The record kinds are glossary
  terms (*Output sample*, *Crew selection*, *Event record*). Children must show (D58):
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
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  Children must show (D58): (Test) the output samples of a run are spaced by [P-TM-010].
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-340; CV-830
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (D48, TT-070), Martin, G2 (C7)
Owner:         Martin
Status:        Baselined
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
  the crew-facing value (CV-760 group 4). Children must show (D58): (Test) each scripted
  selection of a run appears once in the operational data with its timestamp and its target.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-340, N-390
Allocated to:  TM, AF, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  (D58): (Test) each mode change of a mode-transition test appears in the operational data at
  the sample where it occurs.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-060, N-340, N-390
Allocated to:  TM, AF, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  G0-F22). Children must show (D58): (Inspection) each listed signal is defined in ICD-AER-TST;
  (Test) each is present at each output sample.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-250, N-340
Allocated to:  TM, FC, EF, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       Releasable or protected classification of each signal (#69), Martin, closes when the
  plan is extended to the RVS (D44)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-640

```req
ID:            L1-AER-640
Level:         L1
Type:          Functional
Statement:     The Aeronef shall record in its operational data, at each output sample, its vehicle
  state, its altitude, height above the ground, horizontal speed, vertical speed, heading and track,
  its sensed acceleration at the centre of gravity, its vehicle mass, its remaining fuel mass, its
  gear state and each landing and crash event.
Rationale:     Vehicle responses are the fourth thing L0-OBJ-140 relates. These are also the
  measurements the TST needs to assess the performance records (L1-AER-290, -300, -460) and the fuel
  used per leg of the reference mission (N-250). The list is closed. The gear state and the height
  above the ground let the TST assess the takeoffs, landings and rests on the ground (L1-AER-920 to
  -970). Children must show (D58): (Inspection) each listed signal is defined in ICD-AER-TST; (Test)
  each is present at each output sample, and each event at its sample.
  Sufficiency: see L1-AER-590.
Parent(s):     L0-OBJ-140
Source:        N-250, N-340, N-390
Allocated to:  TM, DYN, NAV, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
  adds its own run metadata (CV-870). Children must show (D58): (Test) the identifiers output by
  a run match the configuration it was started with, including a test variant.
  Sufficiency: with L1-AER-400, -410 and -790, this record lets the verification results be tied
  to the one Aeronef configuration and to the design actually loaded.
Parent(s):     L0-CON-200, L0-CON-210, L0-SUC-020
Source:        N-350; CV-870
Allocated to:  TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-660

```req
ID:            L1-AER-660
Level:         L1
Type:          Interface
Statement:     The Aeronef shall accept from the TST, at the start of each run, an initial condition
  of position, velocity, attitude, body rates, landing gear position, fuel mass, autoflight mode
  state and targets.
Rationale:     The TST sets the whole starting state of a run (N-310, CONOPS §4.6). A run starts on
  the ground, at rest on its extended landing gear with the effectors off (D69, L1-AER-950). Only a
  test run or a credibility check may start airborne, with the gear retracted, for example for a
  test at altitude (D73, B3-Q1); the operational start, the reference mission SC-110 and SC-130
  start on the ground. The mode state is a data item here; which mode states are valid at start is
  L2 (#60, C5), and on the ground the recommendation is that no mode is active. The targets are the
  initial selector values, which the flight control panel holds (D55), so FCP is allocated with AF.
  Children must show (D58): (Test) the first output sample of a run reports the initial condition it
  was given, for a ground start and for an airborne start.
  Sufficiency: an executable model (L0-OBJ-010) must be started from a defined state, and autoflight
  (L0-OBJ-030) from a defined mode state; this record supplies both.
Parent(s):     L0-OBJ-010, L0-OBJ-030
Source:        N-310; CONOPS §4.6, SC-200; D69, D73
Allocated to:  DYN, FU, AF, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       Valid initial mode states (#60), Martin, G2 (C5)
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-670

```req
ID:            L1-AER-670
Level:         L1
Type:          Interface
Statement:     Each time the TST commands a step, the Aeronef shall advance its vehicle model by one
  simulation step of [P-SYS-300] with the wind velocity that the TST gives with that command.
Rationale:     The TST executes the simulation at a fixed step (F-TST-01, CV-820) and controls
  time, so that a run can execute faster or slower than real time with the same result (CV-810).
  The wind of the run, steady wind plus gusts within the wind envelope, comes with the step
  command (I-25, D51, D62); drag uses it through the air-relative velocity (L1-AER-070). Only the
  vehicle model receives the wind: the flight software does not know it. Children must show
  (D58): (Test) after k commanded steps, the simulation time is k times [P-SYS-300]; (Analysis)
  the air-relative velocity of each step uses the wind velocity given with that step.
  Sufficiency: with L1-AER-660, this record makes the model executable by the TST (L0-OBJ-010).
Parent(s):     L0-OBJ-010
Source:        N-300, N-360; CV-810, CV-820
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-300
TBD/TBR:       P-SYS-300 value TBR (D48, TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-680

```req
ID:            L1-AER-680
Level:         L1
Type:          Performance
Statement:     The Aeronef shall execute its crew-selection, navigation, autoflight and flight-control
  functions at a control frame period of [P-SYS-310] that is an integer multiple of
  [P-SYS-300].
Rationale:     Derived from the architecture (DD-010 proposed): the flight software runs at a fixed
  rate, synchronised with the simulation step, in the order of FUNCTIONAL_ANALYSIS §4.2; the
  flight control panel takes the crew selections at step 2 of the frame (F-AER-10). A whole
  number of steps per frame keeps the sampling exact on the CV-840 time base. The frame period
  is part of the timing budget (§7.5). Children must show (D58): (Test) the effector commands
  change only at control-frame boundaries.
Parent(s):     Derived (DD-010)
Source:        Trade study: FUNCTIONAL_ANALYSIS §4.2, §5; CV-830
Allocated to:  NAV, AF, FC, FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-310, P-SYS-300
TBD/TBR:       P-SYS-310 value TBR (D48, TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-690

```req
ID:            L1-AER-690
Level:         L1
Type:          Constraint
Statement:     When a run is repeated with the same configuration, initial condition, crew selection
  script and TST step and wind inputs, the Aeronef shall produce operational data that give the
  same pass or fail verdict against each success criterion assessed on the run.
Rationale:     Runs must be reproducible (L0-OBJ-110, N-330). The owner ruled that repeat runs give
  the same pass or fail verdicts and agree within the stated tolerances, and are not required to
  be bit-identical (D59, confirming D25); the tolerances are those each success criterion states.
  L0-ASM-020 (deterministic runs) is a stronger assumption that this record does not need. The
  TST inputs (the step commands and the wind of L1-AER-670) are part of the run, so they are
  part of the condition. The Aeronef's own software is part of every run, so it must not add
  any variation that changes a verdict. L0-OBJ-110 is allocated to the TST and the Aeronef
  (CR-B1-01, D50). Children must show (D58): (Test) repeated executions of the same automated
  test run give the same verdict for each success criterion.
  Sufficiency: every subsystem contributes to the operational data, so a reproducibility child
  in each covers the Aeronef's share of L0-OBJ-110.
Parent(s):     L0-OBJ-110
Source:        N-330; L0-ASM-020; D25, D59
Allocated to:  DYN, FU, EF, FC, AF, FCP, NAV, TM
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  display; its crew output is data (L1-AER-490). L0-CON-190 is allocated to the TST and the
  Aeronef (CR-B1-02, D50). Leaf at L1.
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
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
  [P-SYS-480]. Children must show (D58): (Test) for a change of vehicle state, the time from the
  simulation time of that state to the first change of effector output that responds to it is
  at most [P-SYS-480].
Parent(s):     Derived (DD-020)
Source:        METHODOLOGY §7 rule 4 (timing budget)
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-480, P-SYS-310, P-EF-010
TBD/TBR:       P-SYS-480 value TBR (D48, TT-070), P-EF-010 value TBD (TT-080), Martin, G2 (C3, C4)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-720

```req
ID:            L1-AER-720
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have a baselined model specification, MS-DYN, that states its
  equations of motion, its gravity, drag and wind model, its landing gear and ground contact model,
  and its effector, fuel and mass-properties models.
Rationale:     L0-OBJ-010 requires the executable model to conform to a baselined model
  specification. The list is the closed content of MS-DYN (plan C1; glossary). Children must
  show (D58): (Inspection) MS-DYN is baselined at G2 and each listed model has a section.
  MS-DYN does not exist yet; it is written by C1 (TT-660).
  Sufficiency: with L1-AER-010 and the model-fidelity records it points to, this record gives
  the baselined specification L0-OBJ-010 names.
Parent(s):     L0-OBJ-010
Source:        N-270; plan §6 C1
Allocated to:  DYN, FU, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
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
Status:        Baselined
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
Status:        Baselined
Version:       1
```

### L1-AER-750

```req
ID:            L1-AER-750
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall hold its requirements in one level file per requirement level.
Rationale:     Top-down hierarchy (L0-OBJ-180, plan §3, D2, D31). Depth is decided per branch
  (D4). The former second half of this record was split at G1 (D30) into L1-AER-850 (each record
  states its level) and L1-AER-860 (each record traces to its parents or to its design
  decision). Leaf at L1: the record format check verifies it directly.
  Sufficiency: the Aeronef part of L0-OBJ-180 is its own branch of the hierarchy; with
  L1-AER-850 and -860 this record covers it.
Parent(s):     L0-OBJ-180
Source:        Plan §3; D2, D4, D31
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each Aeronef requirement is held in the level
  file requirements/L<n>.md of its level, one file per level, and the assembler reports no
  section error, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
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
Status:        Baselined
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
Status:        Baselined
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
Status:        Baselined
Version:       1
```

### L1-AER-790

```req
ID:            L1-AER-790
Level:         L1
Type:          Performance
Statement:     The Aeronef configuration shall pass the verification of each baselined Aeronef
  requirement.
Rationale:     One configuration: one autoflight implementation with one flight-control-law design
  on the vehicle model, and it must pass every requirement (L0-SUC-020, D26, D39, D42). Typed
  Performance like its parent L0-SUC-020. Leaf at L1: the verification matrix shows it
  directly.
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
Status:        Baselined
Version:       1
```

### L1-AER-800

```req
ID:            L1-AER-800
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall have its requirements baselined down to the lowest requirement level
  of each subsystem branch, with no open major review finding, at the requirements baseline.
Rationale:     L0-SUC-010: the baselined set is the definition of the vehicle. The lowest
  requirement level of a branch is the level whose next layer would describe the
  implementation (D4); it is reached branch by branch in Phases 3 and 4 of the plan. The requirements baseline is AER-REQ-baseline-1 (G4). Leaf
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
Status:        Baselined
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
Status:        Baselined
Version:       1
```

### L1-AER-820

```req
ID:            L1-AER-820
Level:         L1
Type:          Documentation
Statement:     When the requirements baseline is approved, the Aeronef shall contribute to the final
  test report the last result of each verification procedure performed against each Aeronef
  requirement.
Rationale:     L0-SUC-170: the report of completion lists every test against every level. Each
  element contributes its section and the orchestrator compiles it (D28). The report is issued
  for the complete requirements baseline, approved at Gate G4 (plan §6); *Requirements baseline*
  and *Final test report* are glossary terms. Leaf at L1.
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
Status:        Baselined
Version:       1
```

### L1-AER-830

```req
ID:            L1-AER-830
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall contribute to the method assessment report one section that
  assesses the AI-assisted methods used to design and to verify the Aeronef.
Rationale:     L0-OBJ-210; OBJECTIVES §1: the assessment of the AI-assisted methods is an objective
  in its own right, because the project exists to try those methods. Each element contributes; the owner audits (D28). The
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
Status:        Baselined
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
  procedures are deferred with the hazard analysis (tailoring note, L0-ASM-070); the deferral
  is recorded in the TBD/TBR field. The TST user guide belongs to the TST. Leaf at L1.
  Sufficiency: these three documents are the Aeronef part of the set L0-OBJ-150 names.
Parent(s):     L0-OBJ-150
Source:        METHODOLOGY §11.2; N-380, N-430
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the three documents exist and each names the
  requirements baseline it describes.
Parameters:    —
TBD/TBR:       Abnormal and emergency procedures deferred with the hazard analysis, Martin,
  closes when failures are introduced (#85)
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-850

```req
ID:            L1-AER-850
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall state in each of its requirements below L0 the level of that
  requirement.
Rationale:     Split from L1-AER-750 at G1 (D30). L0-OBJ-180 asks that each requirement below L0
  has a level attribute; the ID starts with the level and the Level field must match it (D31).
  Leaf at L1: the lint checks it directly.
  Sufficiency: see L1-AER-750.
Parent(s):     L0-OBJ-180
Source:        Plan §3; D31; METHODOLOGY §9.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the lint reports no LEVEL or ID-FORMAT error in
  the Aeronef branch, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-860

```req
ID:            L1-AER-860
Level:         L1
Type:          Documentation
Statement:     The Aeronef shall trace each of its requirements below L0 to its parent requirements,
  or, for a derived requirement, to the design decision it derives from.
Rationale:     Split from L1-AER-750 at G1 (D30). L0-OBJ-180 asks for a parent or a Derived flag
  with its design decision for each requirement below L0. The two cases are the two values of
  one trace attribute (Parent(s)), checked by one tool. Leaf at L1: the trace check verifies it
  directly.
  Sufficiency: see L1-AER-750.
Parent(s):     L0-OBJ-180
Source:        METHODOLOGY §9.2, §10.4; D31
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the trace check reports no ORPHAN or DERIVED
  error in the Aeronef branch, checked at each gate.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-870

```req
ID:            L1-AER-870
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall convert each crew selection to SI, and each annunciated or
  indicated quantity from SI, by the exact factors of CONVENTIONS CV-750.
Rationale:     Split from L1-AER-500 at G1 (D30): the unit assignment and the conversion are two
  checks. Selections convert without intermediate rounding (CV-770); display resolution and
  rounding are L2 (CV-780, #55). The conversion sits in the flight control panel, so only SI
  values cross into autoflight (D55, L1-AER-880). Children must show (D58): (Test) a selected
  value and its SI target, and an SI quantity and its shown value, convert by the CV-750 factor;
  (Inspection) no FCP requirement rounds a selected value before conversion.
  Sufficiency: see L1-AER-500.
Parent(s):     L0-CON-270
Source:        N-070; D7, D9, D34; CV-750, CV-770
Allocated to:  FCP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       1
```

### L1-AER-880

```req
ID:            L1-AER-880
Level:         L1
Type:          Interface
Statement:     The Aeronef shall exchange data between its flight control panel and its other
  functions only as crew selections, with each selected value converted to its SI target, out of
  the panel, and as annunciation content, navigation quantities and fuel state into it, as
  defined in ICD-FCP.
Rationale:     The flight control panel is its own subsystem (D55). C8 writes the panel while C5, C6
  and C2 write its neighbours, in parallel (plan §6), so they need one definition of what crosses
  the panel boundary. The list is closed. Only SI values cross into autoflight, so the crew units
  stay in the panel (CV-760, L1-AER-500, -870). Autoflight gives the annunciation content (which
  modes, which targets and the landing gear position, D55, D69; L1-AER-470), navigation the
  indicated quantities (L1-AER-530) and FU the fuel state for the fuel indication and alerts
  (L1-AER-560 to -580); the fuel state itself is defined once, at the vehicle-model boundary
  (L1-AER-430), and ICD-FCP refers to that definition. TM records the panel signals without being a
  party to the exchange (L1-AER-610, -620). ICD-FCP is a new ICD, added to the plan §3 list
  (TT-680). Children must show (D58): (Inspection) each data item crossing the panel boundary in the
  FCP, AF, NAV and FU requirements is one of the listed kinds and is defined in ICD-FCP;
  (Demonstration) the FCP and AF implementations run against the same ICD-FCP definition.
  Sufficiency: with L1-AER-480 and -490 (the crew side of the panel), this record defines the
  Aeronef side of the panel, so the crew interface is data end to end (L0-CON-170) and autoflight
  receives its crew input in one form (L0-OBJ-030).
Parent(s):     L0-CON-170, L0-OBJ-030
Source:        D55, D56; FUNCTIONAL_ANALYSIS §3.2 I-06, I-16, I-18, I-19, §5.1
Allocated to:  FCP, AF, NAV, FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-890

```req
ID:            L1-AER-890
Level:         L1
Type:          Interface
Statement:     The Aeronef shall pass its altitude, height above the ground, horizontal speed,
  vertical speed, heading and track, with their validity, from navigation to autoflight through the
  one interface defined in ICD-NAV-AF.
Rationale:     The navigation → autoflight boundary of the architecture (FUNCTIONAL_ANALYSIS §5.1,
  I-17) needs an interface record on both sides (METHODOLOGY §13.2); L1-AER-530 states the
  computation, not the interface. One definition of each quantity is used by autoflight
  and the crew indications (D55). Validity follows the CV-580 thresholds. There is no VOR and no
  flight path angle (D56). Children must show (D58): (Inspection) the NAV and AF requirements
  each cite ICD-NAV-AF for these quantities, and each quantity is defined there with its unit,
  frame and validity.
  Sufficiency: with L1-AER-530 (the computation), this record delivers every quantity the mode
  catalogue guides on to autoflight across a defined boundary (L0-OBJ-030).
Parent(s):     L0-OBJ-030
Source:        N-190; CV-400 to CV-580; FUNCTIONAL_ANALYSIS §3.2 I-17, §5.1
Allocated to:  NAV, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L1-AER-900

```req
ID:            L1-AER-900
Level:         L1
Type:          Constraint
Statement:     The Aeronef shall have a retractable landing gear whose ground contact points, when the
  gear is extended, lie [P-DYN-040] below the lowest point of its body at level attitude.
Rationale:     Owner decision D69 (answers #60): the Aeronef gets an extendable landing gear so that it
  can rest on the ground, stable and stationary, with the effectors off. The gear length is measured
  from the lowest point of the body (D69, CV-400). On the ground at level attitude, the height above
  the ground is therefore [P-DYN-040], and the centre of gravity is at the altitude [P-DYN-030]/2 plus
  [P-DYN-040]. At the hover height [P-AF-210], the extended gear clears the ground by [P-AF-210] minus
  [P-DYN-040]. When the gear is retracted, no part of it is below the body, so the body makes the
  ground contact and the contact is a crash (L1-AER-270). The gear is ideal (L0-ASM-110). It has no
  mass, inertia or drag of its own, and its position changes no mass property and no drag. This keeps
  the centre of gravity fixed (L0-CON-130) and keeps the single drag area of D64. The number and
  footprint of the contact points are an MS-DYN geometry choice (C1). Children must show (D58):
  (Inspection) the MS-DYN vehicle geometry states the contact points of the extended gear and places
  the retracted gear inside the body; MS-DYN and the FU requirements give the gear position no effect
  on the mass properties or the drag.
  Sufficiency: with L1-AER-910 (movement), -920 (rest on the ground) and -260 to -280 (landing and
  crash), this record gives the landing gear that L0-CON-290 now needs (D69). It also stops the gear
  from moving the centre of gravity (L0-CON-130).
Parent(s):     L0-CON-290, L0-CON-130
Source:        D69; #60
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-040, P-DYN-030, P-AF-210
TBD/TBR:       P-DYN-040 value TBR (TT-830), P-DYN-030 value TBR (TT-740), Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-910

```req
ID:            L1-AER-910
Level:         L1
Type:          Functional
Statement:     While the Aeronef is airborne, when the landing gear command changes, the Aeronef shall
  bring its landing gear to the commanded position within [P-DYN-050].
Rationale:     Takeoff retracts the gear once the vehicle is at the hover height, and Land extends it
  before the descent (D69). Autoflight issues the landing gear command. The command crosses the
  vehicle-model boundary (L1-AER-430), and the vehicle model moves the gear. Between the two
  positions the gear is in transit. A contact in transit is a crash (L1-AER-270), so autoflight
  descends only once the gear is extended (C5). A transit time makes the gear state observable and
  lets the crew see the change annunciated (L1-AER-470). [P-DYN-050] is proposed at 3 s (TBR); a value
  of zero would make the gear move instantly. On the ground the gear stays extended and does not
  respond to a retraction command (L1-AER-920), because a retraction there would drop the body onto
  the ground. Children must show (D58): (Test) after each change of the gear command in flight, the
  gear state shows the gear in transit and then in the commanded position within [P-DYN-050].
  Sufficiency: DYN moves the gear and reports its state, and AF commands it in Takeoff and Land.
  Together they give the extendable gear of D69, on which the landing outcome of L0-CON-290 depends,
  and the gear part of the Takeoff and Land modes of the catalogue (L0-OBJ-030).
Parent(s):     L0-CON-290, L0-OBJ-030
Source:        D69; CONOPS SC-130
Allocated to:  DYN, AF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-050
TBD/TBR:       P-DYN-050 value TBR (TT-850), Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-920

```req
ID:            L1-AER-920
Level:         L1
Type:          Model fidelity
Statement:     While the Aeronef is on the ground, the Aeronef shall rest on its extended landing gear
  at level attitude with zero vehicle velocity and zero body rates, under the ground reaction of the
  ground contact model of MS-DYN.
Rationale:     D69: the Aeronef rests on the ground, stable and stationary. The on-ground state begins
  at the contact step of a landing (L1-AER-260) or at the start of a run on the ground (L1-AER-950).
  It ends at liftoff (glossary). The gear is ideal (L0-ASM-110): at the contact step of a landing the
  vehicle comes to rest, with no bounce, sliding or tipping and no touchdown shock (D53). While the
  vehicle is on the ground, the ground reaction is the force and moment that balance the gravity
  force, the drag of the wind, and the control force and moment. The vehicle therefore stays at rest
  whatever the wind. Liftoff comes at the first step at which the upward component of the control
  force exceeds the weight, where the ground would have to pull to hold the vehicle (MS-DYN). At rest,
  the sensed acceleration is that of the ground reaction, [P-DYN-010] upward (L1-AER-290). The gear is
  held extended on the ground. Children must show (D58): (Analysis) after a landing and in a ground
  start, at each step until liftoff, the velocity and the body rates are zero, the attitude is level
  and the position is constant, in still air and in the strongest wind of the wind envelope; the
  sensed acceleration magnitude is [P-DYN-010]; (Analysis) the vehicle leaves the ground at the first
  step at which the upward component of the control force exceeds the weight.
  Sufficiency: with L1-AER-050 (the ground reaction in the total force), this record defines the
  ground-contact effect that L0-CON-090 allows while the vehicle rests. It also defines the outcome
  that a landing now has under L0-CON-290: rest on the gear (D69).
Parent(s):     L0-CON-090, L0-CON-290
Source:        D53, D69; L0-ASM-110
Allocated to:  DYN
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-010
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-930

```req
ID:            L1-AER-930
Level:         L1
Type:          Functional
Statement:     While the Aeronef is on the ground and autoflight is not taking off, the Aeronef shall
  produce zero control force and zero control moment at each simulation step that follows the start
  of that state by at least [P-SYS-480].
Rationale:     D69: on the ground the effectors are off, so that no fuel is used (L1-AER-940). Land
  switches them off after the touchdown, and a run on the ground starts with them off (L1-AER-950).
  At a landing the effectors are still holding the vehicle up. Switching them off takes one control
  frame plus the effector response, which is the control-loop latency [P-SYS-480] (L1-AER-710). Until
  then, the ground reaction carries what the effectors do not (L1-AER-920), and FC keeps the vehicle
  from lifting off again (C4). "Taking off" is the interval from the engagement of a takeoff to
  liftoff (glossary *Takeoff*), the only time the effectors work on the ground. Proposed mechanism:
  autoflight switches the effectors off with an off value of the axis references (L1-AER-420), flight
  control then commands zero output, and the effectors produce none (C3, C4, C5). Children must show
  (D58): (Test) in each landing of the takeoff and landing tests and in each ground start, every
  effector output is zero at each step from [P-SYS-480] after the start of the on-ground state until
  a takeoff is engaged.
  Sufficiency: AF sets the off reference, FC commands zero and EF produces zero. Together they give
  the effectors-off ground state of D69. With L1-AER-940, this keeps the finite fuel for flight
  (L0-CON-100), and it is part of the takeoff and landing operations of the catalogue (L0-OBJ-030).
Parent(s):     L0-CON-100, L0-OBJ-030
Source:        D69; CONOPS §4.5, SC-130
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-480
TBD/TBR:       P-SYS-480 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-940

```req
ID:            L1-AER-940
Level:         L1
Type:          Model fidelity
Statement:     The Aeronef shall compute a zero fuel mass flow for each simulation step in which its
  effectors produce zero control force and zero control moment.
Rationale:     D69: on the ground, with the effectors off, there is no fuel consumption. Fuel is
  consumed to produce the control forces and control moments (L0-CON-120, L1-AER-160). This record
  excludes any idle flow, so that effectors off means no fuel used, on the ground and in free fall
  alike. The consumption relationships of D65 (DD-110) already meet it. This record makes the property
  a requirement, so that a later relationship cannot add an idle flow. It also keeps the free-fall and
  torque-free credibility checks exact (N-290). Children must show (D58): (Analysis) the MS-DYN
  consumption relationships give zero at zero control force and zero control moment; (Test) the
  remaining fuel mass is constant over each rest on the ground in the takeoff and landing tests.
  Sufficiency: FU computes the flow (L1-AER-160). A zero flow at zero output is the FU share of the
  no-fuel ground state of D69, and it ties the fuel used to the effector output only (L0-CON-100,
  L0-CON-120).
Parent(s):     L0-CON-120, L0-CON-100
Source:        D65, D69; DD-110
Allocated to:  FU
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-950

```req
ID:            L1-AER-950
Level:         L1
Type:          Functional
Statement:     When a run starts on the ground, the Aeronef shall start at rest on its extended
  landing gear at level attitude, at the horizontal position and the heading of its initial
  condition, with its effectors off.
Rationale:     D69: runs start on the ground, on the extended gear, with the effectors off. A ground
  start needs only these items of the initial condition (L1-AER-660): the horizontal position, the
  heading, the fuel mass, the mode state and the targets. The altitude follows from the gear
  (L1-AER-900), the velocity and the body rates are zero, and the attitude is level. An initial
  condition on the ground with any other altitude, velocity, body rates or attitude is rejected with
  an initial-condition error (ICD-AER-TST, I1). Which mode states are valid on the ground is for C5
  (#60); the recommendation is that no mode is active. Only a test run or a credibility check may
  start airborne (D73, B3-Q1); this record covers the ground start. Children must show (D58): (Test)
  the first output sample of a ground start reports: the given horizontal position and heading; the
  altitude [P-DYN-030]/2 plus [P-DYN-040]; zero velocity and body rates; level attitude; the gear
  extended, with the vehicle on the ground; and zero effector output.
  Sufficiency: DYN sets the rest state and the gear, AF sets the effectors-off reference and FC
  commands zero, so that EF produces nothing (L1-AER-930). This gives the executable model a defined
  ground start (L0-OBJ-010), and gives autoflight a defined start for a takeoff (L0-OBJ-030).
Parent(s):     L0-OBJ-010, L0-OBJ-030
Source:        D69, D73; N-310; CONOPS §4.6, §5
Allocated to:  DYN, AF, FC
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-DYN-030, P-DYN-040
TBD/TBR:       P-DYN-030 value TBR (TT-740), P-DYN-040 value TBR (TT-830), Martin, G2 (C1); valid
  initial mode states (#60), Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-960

```req
ID:            L1-AER-960
Level:         L1
Type:          Performance
Statement:     When autoflight takes off from the ground with fuel remaining in a wind of speed at
  most [P-SYS-580], the Aeronef shall reach the hover height [P-AF-210] with its landing gear
  retracted and its horizontal position within [P-SYS-450] of its position on the ground.
Rationale:     Takeoff (D69) is engaged on the ground. It powers up, climbs at [P-AF-240] to the
  hover height over the current position, retracts the gear and hands over to Hover. This record
  states the aircraft-level capability; the mode, its engagement and its handover to Hover are AF
  (C5, D33). The hover height is a height above the ground (CV-400, D70). The wind limit has this
  reason. On the ground, the ground reaction holds the vehicle against the drag of the wind, and the
  flight software does not know the wind (L1-AER-670). At liftoff that drag acts at once, as a step.
  At dry mass and sea-level density, a wind of [P-SYS-580] gives a drag step within the
  flight-control transient allowance [P-FC-020], so the vehicle acceleration stays within
  [P-SYS-440] (L1-AER-300). The owner set this limit (D73, B3-Q2); the wind envelope carries the
  same limit at liftoff. Children must show (D58): (Test) from ground starts at full fuel and near
  dry mass, in still air and in a steady wind of [P-SYS-580] from several directions, the vehicle
  reaches the hover height with the gear retracted and its horizontal position within [P-SYS-450] of
  the ground position.
  Sufficiency: with L1-AER-970 (landing) and L1-AER-450 (the catalogue, now with Takeoff and Land),
  this record gives the takeoff capability that operating the Aeronef by autoflight now needs, since
  every run starts on the ground (L0-OBJ-030, D69).
Parent(s):     L0-OBJ-030
Source:        D69, D70, D73; CONOPS SC-130, SC-110
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-AF-210, P-SYS-580, P-SYS-450, P-AF-240, P-FC-020, P-SYS-440
TBD/TBR:       P-SYS-580 value TBR (TT-860), P-SYS-450 value TBR (TT-050), P-AF-240
  value TBR (TT-830), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L1-AER-970

```req
ID:            L1-AER-970
Level:         L1
Type:          Performance
Statement:     When autoflight lands the Aeronef from the hover height in a wind within the wind
  envelope, the Aeronef shall make its ground contact on its extended landing gear within the
  landing envelope.
Rationale:     Land (D69) is engaged only from Hover. It extends the gear, descends at [P-AF-240] and
  touches down within the landing envelope, then switches the effectors off (L1-AER-930). [P-AF-240]
  is well inside the vertical speed limit [P-SYS-500]. The horizontal speed limit [P-SYS-510] bounds
  the drift that Hover allows at the touchdown, so the hover horizontal speed tolerance [P-AF-170]
  must be at most [P-SYS-510] (C5). Landing in the strongest wind needs no wind limit: Hover holds the
  position against the wind, and after the contact the ground reaction takes the drag (L1-AER-920).
  Children must show (D58): (Test) each landing from Hover produces one landing event (L1-AER-260) and
  no crash, at full fuel and near dry mass, in still air and in a steady wind of [P-SYS-430] with
  gusts of [P-SYS-560] built up over [P-SYS-570] from several directions.
  Sufficiency: with L1-AER-960, this record gives the landing capability of the catalogue
  (L0-OBJ-030). It also shows that the autoflight landing achieves the landing outcome of L0-CON-290.
Parent(s):     L0-OBJ-030, L0-CON-290
Source:        D53, D69, D70; CONOPS SC-130
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-SYS-500, P-SYS-510, P-AF-240, P-AF-170, P-SYS-430, P-SYS-560, P-SYS-570
TBD/TBR:       P-SYS-500, P-SYS-510 values TBR (TT-090), P-AF-240 value TBR (TT-830), Martin, G2;
  P-AF-170 value TBD, Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```
