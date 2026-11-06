# B3 — New L1 records (landing gear and ground operations, D69)

Proposed by task B3 for owner approval (CR-B3-32). These records join the AER section of L1 (source of record `work/B1/L1_AER.md`) after L1-AER-890, in ID order. All are Draft, version 1, owner Martin, Criticality "Not assessed". Each is allocated to L2 subsystems, so each is verified by roll-up (D40, D58) and its rationale says what its children must show.

**IDs.** L1-AER-900 to -970 are the next free IDs in steps of 10 (L1-AER-230, -340, -540 and -550 are Deleted and are not reused). After them only L1-AER-980 and -990 remain in the three-digit space the lint allows (`^L1-AER-\d{3}$`); see `issues.md` note N-03.

**Terms.** The new glossary terms these records use (*Landing gear*, *Landing gear command*, *Gear state*, *On the ground*, *Liftoff*, *Ground reaction*, *Effectors off*, *Height above the ground*, *Takeoff*) are proposed in `glossary_proposals.md` §1. The parameters P-DYN-050 and P-SYS-580 are proposed in `param_proposals.md`.

**Mode names at L1.** As in L1-AER-360, the statements say what autoflight does ("takes off", "lands") and do not name modes. The modes Takeoff and Land are defined at L2 by AF (C5, D33).

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
TBD/TBR:       P-DYN-050 value TBR (new register row, B3), Martin, G2 (C1)
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
  (#60); the recommendation is that no mode is active. A test run may also start airborne (owner
  question B3-Q1); this record covers the ground start. Children must show (D58): (Test) the first
  output sample of a ground start reports: the given horizontal position and heading; the altitude
  [P-DYN-030]/2 plus [P-DYN-040]; zero velocity and body rates; level attitude; the gear extended,
  with the vehicle on the ground; and zero effector output.
  Sufficiency: DYN sets the rest state and the gear, AF sets the effectors-off reference and FC
  commands zero, so that EF produces nothing (L1-AER-930). This gives the executable model a defined
  ground start (L0-OBJ-010), and gives autoflight a defined start for a takeoff (L0-OBJ-030).
Parent(s):     L0-OBJ-010, L0-OBJ-030
Source:        D69; N-310; CONOPS §4.6, §5
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
Rationale:     Takeoff (D69) is engaged on the ground. It powers up, climbs at [P-AF-240] to the hover
  height over the current position, retracts the gear and hands over to Hover. This record states
  the aircraft-level capability; the mode, its engagement and its handover to Hover are AF (C5, D33).
  The hover height is a height above the ground (CV-400, D70). The wind limit has this reason. On the
  ground, the ground reaction holds the vehicle against the drag of the wind, and the flight software
  does not know the wind (L1-AER-670). At liftoff that drag acts at once, as a step. At dry mass and
  sea-level density, a wind of [P-SYS-580] gives a drag step within the flight-control transient
  allowance [P-FC-020], so the vehicle acceleration stays within [P-SYS-440] (L1-AER-300). See owner
  question B3-Q2; *Wind envelope* carries the same limit at liftoff. Children must show (D58): (Test)
  from ground starts at full fuel and near dry mass, in still air and in a steady wind of [P-SYS-580]
  from several directions, the vehicle reaches the hover height with the gear retracted and its
  horizontal position within [P-SYS-450] of the ground position.
  Sufficiency: with L1-AER-970 (landing) and L1-AER-450 (the catalogue, now with Takeoff and Land),
  this record gives the takeoff capability that operating the Aeronef by autoflight now needs, since
  every run starts on the ground (L0-OBJ-030, D69).
Parent(s):     L0-OBJ-030
Source:        D69, D70; CONOPS SC-130, SC-110
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40, D58).
Parameters:    P-AF-210, P-SYS-580, P-SYS-450, P-AF-240, P-FC-020, P-SYS-440
TBD/TBR:       P-SYS-580 value TBR (new register row, B3-Q2), P-SYS-450 value TBR (TT-050), P-AF-240
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
