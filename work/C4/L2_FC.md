## FC — Flight control

The flight control requirements (task C4). The subject of each statement is the flight control subsystem (FC), part of the flight software with AF, NAV and FCP. FC implements the functions F-AER-05 (regulate each degree of freedom) and F-AER-06 (allocate the axis demands to the effectors) and its share of F-AER-14 (FUNCTIONAL_ANALYSIS §6.1). It runs once per control frame `[P-SYS-310]`. Its inputs are the axis references of autoflight (ICD-FC-AF), the vehicle state of the first simulation step of the frame, the gear state and the mass properties (vehicle-model boundary), the vehicle parameter set (effector layout and limits) and the flight-control-law design of the configuration. Its outputs are the effector commands and the effector activation state, given to EF across the vehicle-model boundary, and the signals for the operational data. FC takes no mode information from AF (L1-AER-420), no fuel state, no wind and no navigation quantity.

**Decomposition.** FC has three sub-functions, which `work/C4/L3_FC.md` specifies as L3 sections: translational regulation (TR: three axes, from references to force demands), rotational regulation (RO: three axes, from references to moment demands) and control allocation (AL: from the six axis demands to the effector commands). The six axis demands are the force along and the moment about each body axis (glossary *Axis demand*; I-11). An L2 record that has L3 children is allocated to them and is verified by roll-up (D40); the others are leaves, each verified directly by its own method. Gains and algorithms are design decisions, not requirements (D4): they are proposed as DD-300 to DD-350 in `work/C4/issues.md`.

**The axis references (DD-290).** L1-AER-370 leaves to C4 which quantity each axis regulates and in which frame. The decision: each of the six axes has one axis reference made of a reference value, a reference rate and a reference acceleration. The translational axes are the north, east and vertical axes of the vehicle-carried local frame V (CV-150, CV-950); the vertical axis is expressed as altitude and vertical speed, positive up (CV-430, CV-490). Each translational axis reference states which quantity is regulated: the position (the reference value, with the rate and the acceleration as feed-forward) or the velocity (the reference rate, with the acceleration as feed-forward). The rotational axes are roll, pitch and heading, each regulated to its reference angle, with the body rate about the axis as the reference rate; with pitch and roll held at zero (D57) the reference rate of the heading is the heading rate. Autoflight supplies absolute references and never a command such as "hold the present position" (that would put a latched state and the mode logic into FC, L1-AER-420). In place of the six references, autoflight can send the **off value**, which carries no mode information (L1-AER-420).

**Independent regulation.** The six regulations are separate loops: each uses only the reference and the vehicle state of its own axis (L2-AER-FC-010 and its L3 children). The vehicle has no coupling between axes (D18, D61), so none needs another axis's reference. The frame V keeps the translational axes uncoupled when the heading changes: a heading change at constant velocity is a rotation of the force resolution, not a manoeuvre of the translational axes (DD-300). Independence is measured by L2-AER-FC-120.

**Saturation is nominal behaviour (N-260, L1-AER-110).** An axis demand beyond what the effector set can produce, or beyond the crew limit, is limited and the regulation continues, with no failure state and no change to the effector activation state (L2-AER-FC-130, -160, -170, -180). The effector set guarantees the authority box together (DD-170, L2-AER-EF-330), so a demand limited to the box is always producible. The rule that limits the demands (each component on its own) is a derived requirement with its design decision (L3-AER-FC-AL-020, DD-310). The crew limit is applied to the vehicle acceleration that FC demands, which scales the force with the vehicle mass (DD-320, D38).

**Replaceable control law (L0-CON-200, N-230).** FC meets AF only at ICD-FC-AF and the vehicle model only at the vehicle-model boundary, and takes its design from the configuration (L2-AER-FC-020, -030, -050). It reads the effector layout and limits from the vehicle parameter set, so a different layout or a different control law changes no vehicle-model file and no FC requirement (L2-AER-FC-060).

**Ground operations (D69, D73).** With the effectors off on the ground, FC commands zero and switches the effector activation state off while the axis references carry the off value (L2-AER-FC-190). It switches it on when the references leave the off value, which is how a takeoff powers up (L2-AER-FC-200). While the gear is extended and the vertical reference calls for a descent, it keeps the upward control force below the weight, so that a touchdown is not followed by a second liftoff (L2-AER-FC-210). In a liftoff in wind it keeps the horizontal position (L2-AER-FC-220). FC does not command the gear and does not read the mode.

**Verification.** Each leaf record carries its method and a procedure ID that follows the record number (IN-, AN-, TP-, DM-FC-nnn); Phase 5 (V1) writes the procedures. The tests drive FC with scripted axis references from a test autoflight variant selected through the configuration, the way the control-law variant of L1-AER-400 is selected, and record the axis demands and the effector commands at each control frame (IN-C4-30, IN-C4-31). Scenario values (step sizes, headings, winds) are set by the procedures (D32).

**Not in this section.** Manual control (D49, L0-CON-180), failure handling (deferred) and a sensor model (#83): FC uses the exact vehicle state (L2-AER-FC-040). After fuel exhaustion FC does nothing special: the effector outputs are zero whatever it commands (L2-AER-EF-200, D68).

**Coverage of the L1 parents.** Every live L1 record allocated to FC in FUNCTIONAL_ANALYSIS §6.2 has at least one FC child. L1-AER-360 is not allocated to FC; its FC child (L2-AER-FC-240) needs CR-C4-01. The L2 children are in the table; the L3 children are in `work/C4/L3_FC.md`.

| L1 parent | What FC guarantees, in the parent's terms | FC children |
| --- | --- | --- |
| L1-AER-110 | FC reads the output limits from the vehicle parameter set, never commands an effector beyond them, and handles a demand beyond them as nominal behaviour | -060, -160, -170, -180 |
| L1-AER-120 | FC can command the pure upward force that the effector set can produce, up to the bound of the authority box | -150 |
| L1-AER-130 | FC can command each of the other five pure forces up to the bound of the authority box | -150 |
| L1-AER-140 | FC can command each pure moment up to the bound of the authority box | -150 |
| L1-AER-290 | FC never demands more vehicle acceleration than the budget leaves for the crew limit; the force it commands scales with the mass | -130 |
| L1-AER-300 | FC demands at most the vehicle-acceleration limit and adds at most the transient allowance to the reference acceleration, gusts and the liftoff step included | -130, -140 |
| L1-AER-310 | FC tracks horizontal velocity references up to the maximum horizontal speed | -100 |
| L1-AER-320 | FC tracks climb rate references up to the maximum climb rate | -100 |
| L1-AER-330 | FC tracks descent rate references up to the maximum descent rate | -100 |
| L1-AER-350 | FC tracks heading rate references up to the maximum heading rate | -110 |
| L1-AER-370 | Six separate regulations, each with a tracking tolerance, a settling time and a recovery from saturation | -010, -020, -100, -110, -180 |
| L1-AER-380 | A change of one reference moves no other axis beyond the cross-axis tolerances | -120 |
| L1-AER-390 | FC holds pitch and roll at their references, which autoflight sets to zero | -110 |
| L1-AER-400 | The control-law design comes from the configuration and the effector layout from the vehicle parameter set | -050, -060 |
| L1-AER-420 | The only data FC takes from AF are the axis references or the off value, defined in ICD-FC-AF | -020 |
| L1-AER-430 | FC's side of the vehicle-model boundary is the closed list of its items | -030 |
| L1-AER-440 | FC uses the exact frame-start state as provided | -040 |
| L1-AER-450 | FC regulates the vehicle toward the references that autoflight derives from the crew targets | -010 |
| L1-AER-460 | FC keeps the horizontal position within its share of the position error budget | -100 |
| L1-AER-630 | FC gives the operational data the references it received, the axis demands and the effector commands | -250 |
| L1-AER-680 | FC runs once per control frame and changes its commands only at frame boundaries | -070, -080 |
| L1-AER-690 | FC computes only from the inputs of the run | -260 |
| L1-AER-710 | FC issues its commands in the frame of the state they respond to, which is its share of the latency | -070 |
| L1-AER-930 | While the references carry the off value, FC commands zero and the activation state off; it switches on only when the references leave the off value | -190, -200, -210 |
| L1-AER-950 | A ground start has the off value, so FC commands zero from the first control frame | -190 |
| L1-AER-960 | FC powers up with the takeoff and keeps the horizontal position in the liftoff wind | -200, -220 |
| L1-AER-970 | FC tracks the touchdown speeds and does not lift the vehicle off again | -100, -210 |
| L1-AER-360 | (CR-C4-01) FC's hold commands use at most the fuel margin | -240 |

Records that are Derived: L3-AER-FC-AL-020 (the priority rule, DD-310). No L2 record is Derived.

### L2-AER-FC-010

```req
ID:            L2-AER-FC-010
Level:         L2
Type:          Functional
Statement:     While the axis references do not carry the off value, the flight control subsystem
  shall regulate each of the three translational axes and each of the three rotational axes toward
  the axis reference of that axis.
Rationale:     L1-AER-370 asks for six separate regulations, one for each degree of freedom
  (L0-OBJ-020, L0-CON-020, AIRCRAFT_CHARACTERISTICS §5). The six axes are the north, east and
  vertical axes of the vehicle-carried local frame V for translation and the roll, pitch and
  heading axes for rotation (DD-290). The vehicle has no coupling between axes (D18, D61), so no
  regulation needs another axis's reference; TR regulates the translational three and RO the
  rotational three, and AL turns the six axis demands into effector commands (L2-AER-FC-150). The
  statement holds while the references are not the off value: with the off value there is nothing
  to regulate (L2-AER-FC-190). The accuracy, the settling and the independence of the regulations
  are L2-AER-FC-100, -110 and -120.
  Sufficiency (L1-AER-370): L3-AER-FC-TR-010 and L3-AER-FC-RO-010 give a separate regulation for
  each of the six axes, each on its own reference; L2-AER-FC-100 and -110 give it a tracking
  tolerance and a settling time; L2-AER-FC-180 gives the recovery from saturation; L2-AER-FC-120
  gives the independence that L0-CON-020 asks for.
  Sufficiency (L1-AER-450): the catalogue, the arming and the guidance laws are AF's and the
  navigation quantities are NAV's. FC's part of guiding the translation and the heading toward the
  targets is to regulate the vehicle toward the references that AF derives from them, which is
  this record with L2-AER-FC-100 and -110.
Parent(s):     L1-AER-370, L1-AER-450
Source:        N-240; L0-OBJ-020; AIRCRAFT_CHARACTERISTICS.md §5; D18, D56, D57; DD-290
Allocated to:  TR, RO
Criticality:   Not assessed
Verification:  Inspection — IN-FC-010; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-020

```req
ID:            L2-AER-FC-020
Level:         L2
Type:          Interface
Statement:     The flight control subsystem shall take from autoflight, at the start of each control
  frame, only the six axis references, or the off value in their place, as ICD-FC-AF defines them.
Rationale:     Modes and controllers are decoupled (D15): the one interface is what lets any
  autoflight implementation pair with any control-law design (L1-AER-420). Only the axis
  references cross it, so flight control receives no mode information and no control law can depend
  on the mode logic (G1-F04). The content that DD-290 proposes for ICD-FC-AF is: for each axis a
  reference value, a reference rate and a reference acceleration, in SI and with the angle and
  altitude conventions of CONVENTIONS; for each translational axis, which quantity is regulated
  (position or velocity); and the off value, a single value that replaces the six references and
  means that the effectors are off (D69). The reference value is absolute, so FC latches nothing
  at an engagement (DD-290). ICD-FC-AF is written at integration (I1) from this record and the
  AF counterpart (C5).
  Sufficiency (L1-AER-420): this record is FC's side of the one interface; AF's side is its own
  child, and the two cite ICD-FC-AF as their only mutual interface, which is what L1-AER-420
  asks.
  Sufficiency (L1-AER-370): the interface carries a separate reference for each of the six degrees
  of freedom, which is what the six regulations of L2-AER-FC-010 need.
Parent(s):     L1-AER-420, L1-AER-370
Source:        D15, G1-F04; IN-B1-03; FUNCTIONAL_ANALYSIS I-13; DD-290
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FC-020; success criteria: ICD-FC-AF defines, for each of the six
  axes, the reference value, rate and acceleration with unit, frame and sign, defines for each
  translational axis the regulated quantity, and defines the off value; the FC requirements cite
  ICD-FC-AF as the only interface with AF; and the FC implementation reads no other data item
  from AF.
Parameters:    —
TBD/TBR:       ICD-FC-AF home and content (IN-B1-03), Martin, G2 (I1, C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-030

```req
ID:            L2-AER-FC-030
Level:         L2
Type:          Interface
Statement:     The flight control subsystem shall exchange data with the vehicle model only as the
  vehicle state, the gear state and the mass properties taken from it and the effector commands
  with the effector activation state given to it, as the vehicle-model boundary ICD defines them.
Rationale:     A fixed vehicle-model boundary lets the control law be replaced without modifying the
  vehicle model (L0-CON-200, L1-AER-430). FC's share is the closed list: the vehicle state (I-09:
  position, velocity, attitude, body rates and vehicle acceleration of the frame-start step), the
  gear state (the gear position and whether the vehicle is on the ground, I-45), the mass
  properties (vehicle mass and the principal moments of inertia, I-05) and, out, the effector
  commands and the effector activation state (I-12). The gear state is needed for the descent
  guard of L2-AER-FC-210; FUNCTIONAL_ANALYSIS I-45 lists AF as its user, so CR-C4-02 adds FC.
  FC takes no fuel state (the fuel is FU's and the effects of exhaustion are EF's, D68), no wind
  (L1-AER-670), no sensed acceleration (it goes to the operational data, IN-C1-35) and no
  navigation quantity (IN-C6-20).
  Sufficiency (L1-AER-430): FC's data items are all of the listed kinds (vehicle state, gear
  state, mass properties in; effector commands out), and none else, so FC's share of the boundary
  is covered.
Parent(s):     L1-AER-430
Source:        FUNCTIONAL_ANALYSIS §3.2 I-05, I-09, I-12, I-45, §5.1; D55
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FC-030; success criteria: each FC data item crossing the
  vehicle-model boundary is a vehicle state element, a gear state item, a mass property or an
  effector command or the effector activation state, defined in the vehicle-model boundary ICD
  with its unit and frame, and the FC implementation reads no other vehicle-model output.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-040

```req
ID:            L2-AER-FC-040
Level:         L2
Type:          Interface
Statement:     The flight control subsystem shall use the vehicle state of the first simulation step
  of each control frame, as the vehicle model provides it, for every regulation of that frame.
Rationale:     Perfect state knowledge (L0-ASM-010) is a requirement on the Aeronef (L1-AER-440);
  FC's share is to use the state as given. No estimate or filter replaces an element of the state,
  so a sensor model (#83) later changes the source of the state and not the regulation. The only
  delay in the loop that the timing budget does not count is the sampling to the frame start
  (L1-AER-680, -710). A quantity that FC derives from the state (the velocity error, or a
  disturbance acceleration estimated from the vehicle acceleration) is not an estimate of the
  state.
  Sufficiency (L1-AER-440): DYN gives the exact state of the frame-start step (L2-AER-DYN-330),
  NAV takes it unmodified, and this record makes FC use it unmodified, so the regulation acts on
  the state L1-AER-440 describes.
Parent(s):     L1-AER-440
Source:        L0-ASM-010; METHODOLOGY §4.4; FUNCTIONAL_ANALYSIS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FC-040; success criteria: the FC implementation reads the vehicle
  state once per control frame from the vehicle-model boundary input, passes it unmodified to the
  regulation, and contains no estimator of a state element or filter that replaces one.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-050

```req
ID:            L2-AER-FC-050
Level:         L2
Type:          Constraint
Statement:     The flight control subsystem shall take its flight-control-law design from the
  configuration of the run.
Rationale:     Control-law designers swap controllers without touching the vehicle model (L0-CON-200,
  N-230). One design exists now (D42); a test variant is enough to show the replacement (R-F02).
  The configuration names the design (I-22), and the design is identified in the run's
  configuration identity (L1-AER-650). The vehicle model is DYN, FU and EF, and the design
  meets it only at the vehicle-model boundary (L2-AER-FC-030).
  Sufficiency (L1-AER-400): with L2-AER-FC-020 (the AF interface) and -060 (the layout from the
  parameter set), this record makes the design a configuration choice, with no vehicle-model file
  changed by the replacement, which is the whole of L1-AER-400.
Parent(s):     L1-AER-400
Source:        N-230; D15, D42; FUNCTIONAL_ANALYSIS I-22
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-FC-050; success criteria: a test variant of the control-law
  design is selected through the configuration; the run uses it (the axis demands for the same
  scripted references differ from those of the reference design, and the configuration identity
  names the variant); and the files of the vehicle model (DYN, FU, EF) have unchanged checksums.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-060

```req
ID:            L2-AER-FC-060
Level:         L2
Type:          Constraint
Statement:     When a run starts, the flight control subsystem shall take the number, the directions
  of action, the points of application and the output limits of the effectors from the vehicle
  parameter set of the run.
Rationale:     The effector layout (number, directions, points of application) and the limits are
  EF parameters that a campaign can change without a software change (L2-AER-EF-050, DD-200).
  FC allocates against that layout, so it reads it from the parameter set at the start and
  holds no copy in its design (IN-C3-20). Then a different layout, or a different control law
  with the same parameter set, changes no vehicle-model file and no requirement. The output limits
  are the ones the database defines for each effector, which L1-AER-110 names. The layout is
  constant over a run (L2-AER-EF-020).
  Sufficiency (L1-AER-400): the replacement of the design leaves the vehicle model unchanged and,
  by this record, a change of the vehicle parameter set leaves FC unchanged.
  Sufficiency (L1-AER-110): with L2-AER-EF-010 (the maximum force of each effector is a
  parameter), FC uses the limit the database defines for each effector, not a value of its own.
Parent(s):     L1-AER-400, L1-AER-110
Source:        IN-C3-20; L2-AER-EF-010, -050; DD-200
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-FC-060; success criteria: two runs with vehicle parameter sets
  that differ in the number or the directions of the effectors ([P-EF-100], [P-EF-110]) and in
  [P-EF-120] and [P-EF-130], both meeting the authority box of L2-AER-EF-330, with no change to
  the FC software, give effector commands that meet L2-AER-FC-150 and -160 for the set of that
  run.
Parameters:    P-EF-100, P-EF-110, P-EF-120, P-EF-130
TBD/TBR:       P-EF-100 to P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-070

```req
ID:            L2-AER-FC-070
Level:         L2
Type:          Performance
Statement:     The flight control subsystem shall issue the effector commands of each control frame,
  computed from the vehicle state of the first simulation step of that frame, for use from that
  step.
Rationale:     Flight control computes the effector commands at the start of each control frame from
  the state of its first step (FUNCTIONAL_ANALYSIS §4.2) and EF uses them from the first step
  of that frame (L2-AER-EF-150). Flight control adds no delay of its own in simulation time, so
  the first change of effector command that responds to a vehicle state comes at the next frame
  start, at most one control frame later (DD-020). The first control frame of a run starts at
  step zero (IN-C7-32, DD-480).
  Sufficiency (L1-AER-710): the time from the simulation time of a vehicle state to the first
  change of effector command is at most [P-SYS-310]; EF brings the output to the command
  within [P-EF-010] (L2-AER-EF-340); and [P-SYS-310] plus [P-EF-010] is at most [P-SYS-480], so
  the first change of output responds within the latency budget.
  Sufficiency (L1-AER-680): the control frame period is the flight software period, an integer
  multiple of the simulation step; FC runs once in each frame, as this record and L2-AER-FC-080
  state.
Parent(s):     L1-AER-710, L1-AER-680
Source:        DD-010, DD-020; METHODOLOGY §7 rule 4; FUNCTIONAL_ANALYSIS §4.2, §7.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-070; success criteria: with scripted wind steps and axis reference
  steps applied at steps that are not frame starts and at frame starts, the time from the
  simulation time of the first vehicle state that shows the change to the first recorded change
  of an effector command that responds to it is at most [P-SYS-310]; and the effector commands
  of the control frame that starts at step zero are present at step zero.
Parameters:    P-SYS-310, P-SYS-480, P-EF-010
TBD/TBR:       P-SYS-310, P-SYS-480 values TBR (TT-070), P-EF-010 value TBR (TT-080), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-080

```req
ID:            L2-AER-FC-080
Level:         L2
Type:          Constraint
Statement:     The flight control subsystem shall hold each effector command and the effector
  activation state constant over each control frame.
Rationale:     The flight software runs at a fixed rate (DD-010); between frames the effector
  commands do not change, so the effector outputs follow one command per frame (L2-AER-EF-150).
  A whole number of simulation steps per frame keeps the sampling exact on the CV-840 time base
  (L1-AER-680).
  Sufficiency (L1-AER-680): the L1 test is that the effector commands change only at frame
  boundaries; this record states it for FC, the only source of effector commands.
Parent(s):     L1-AER-680
Source:        DD-010; CV-830; FUNCTIONAL_ANALYSIS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-080; success criteria: with the effector commands recorded at each
  simulation step (IN-C3-31), in the reference mission (SC-110) and in the scripted runs of
  TP-FC-100 and TP-FC-110, each effector command and the effector activation state differ from
  the value of the previous step only at a step that starts a control frame.
Parameters:    P-SYS-310, P-SYS-300
TBD/TBR:       P-SYS-300, P-SYS-310 values TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-100

```req
ID:            L2-AER-FC-100
Level:         L2
Type:          Performance
Statement:     While the vehicle is airborne with fuel remaining and the axis references do not carry
  the off value, the flight control subsystem shall keep each translational axis within the
  tracking tolerance of that axis and regulated quantity of its axis reference.
Rationale:     The accuracy of the translational regulation: the north, east and vertical axes follow
  the position or the velocity that autoflight asks for. The tracking tolerance depends on the
  axis group (horizontal or vertical) and on the regulated quantity (position or velocity); TR
  states the four values as parameters, as L1-AER-370 asks of the FC children, together with the
  speed ranges, the wind and the settling time. The statement is limited to airborne flight with
  fuel, because on the ground the ground reaction holds the vehicle and after fuel exhaustion the
  effectors give no force (D68).
  Sufficiency (L1-AER-310): L3-AER-FC-TR-020 keeps the horizontal velocity within [P-FC-040] of the
  reference for horizontal speeds up to [P-SYS-230]; the authority for it is EF's (L2-AER-EF-330).
  Sufficiency (L1-AER-320, L1-AER-330): L3-AER-FC-TR-030 keeps the vertical velocity within
  [P-FC-050] of the reference for climb rates up to [P-SYS-240] and descent rates up to [P-SYS-250].
  Sufficiency (L1-AER-460): L3-AER-FC-TR-040 keeps the horizontal position within [P-FC-010] of the
  reference position; with the AF share [P-AF-160] the sum is at most [P-SYS-450] (closure rule,
  FUNCTIONAL_ANALYSIS §7.4); L3-AER-FC-TR-050 does the same for the altitude.
  Sufficiency (L1-AER-970): at the touchdown the vertical speed is within [P-FC-050] of the
  descent rate [P-AF-240] and the horizontal speed within [P-FC-040] of the reference, so with
  the AF hover tolerance [P-AF-170] the touchdown speeds are inside the landing envelope
  ([P-SYS-500], [P-SYS-510]) when [P-AF-240] plus [P-FC-050] is at most [P-SYS-500] and the sum
  of the horizontal shares is at most [P-SYS-510] (closure at I1).
  Sufficiency (L1-AER-370): L3-AER-FC-TR-060 gives the settling time of a reference step for each
  of the four cases, so each translational axis settles on its reference.
Parent(s):     L1-AER-310, L1-AER-320, L1-AER-330, L1-AER-370, L1-AER-460, L1-AER-970
Source:        N-170, N-240; FUNCTIONAL_ANALYSIS §7.4; D51, D60
Allocated to:  TR
Criticality:   Not assessed
Verification:  Inspection — IN-FC-100; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FC-010, P-FC-040, P-FC-050, P-SYS-230, P-SYS-240, P-SYS-250, P-AF-160, P-SYS-450,
  P-AF-170, P-AF-240, P-SYS-500, P-SYS-510
TBD/TBR:       P-FC-040, P-FC-050 values TBR (TT-C4-1), P-FC-010 value TBR (TT-050), P-AF-160 value
  TBR (TT-050), P-AF-170 value TBD (C5), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-110

```req
ID:            L2-AER-FC-110
Level:         L2
Type:          Performance
Statement:     While the vehicle is airborne with fuel remaining and the axis references do not carry
  the off value, the flight control subsystem shall keep each rotational axis within the tracking
  tolerance of that axis of its axis reference.
Rationale:     The accuracy of the rotational regulation: the heading follows the reference heading
  and its rate (a change of heading in place, or at speed), and pitch and roll stay at their
  references, which are zero (D57). RO states the tolerances as parameters (L1-AER-370). The
  vehicle has no aerodynamic moment (DD-050), so there is no disturbance moment to reject; the
  moments only follow the references. The statement is limited to airborne flight with fuel for
  the reason given in L2-AER-FC-100.
  Sufficiency (L1-AER-350): L3-AER-FC-RO-030 keeps the heading rate within [P-FC-080] of the
  reference for heading rates up to [P-SYS-270], at maximum inertia; the moment authority is
  EF's (L2-AER-EF-320), and L3-AER-FC-RO-060 scales the moment demand with the inertia of the
  frame.
  Sufficiency (L1-AER-390): the attitude references come from AF and are zero for pitch and roll;
  L3-AER-FC-RO-040 holds pitch and roll within [P-AF-180] of them, which is FC's share of
  L1-AER-390, AF's being to set the references.
  Sufficiency (L1-AER-370): L3-AER-FC-RO-020 keeps the heading within [P-FC-070] of the reference;
  L3-AER-FC-RO-050 gives the settling time of a reference step; L3-AER-FC-RO-070 makes the turn
  the shorter way round (CV-930).
Parent(s):     L1-AER-350, L1-AER-370, L1-AER-390
Source:        N-170, N-240; D57; CV-930
Allocated to:  RO
Criticality:   Not assessed
Verification:  Inspection — IN-FC-110; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FC-070, P-FC-080, P-SYS-270, P-AF-180
TBD/TBR:       P-FC-070, P-FC-080 values TBR (TT-C4-1), P-AF-180 value TBR (TT-190), P-SYS-270 value
  TBR (TT-010), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-120

```req
ID:            L2-AER-FC-120
Level:         L2
Type:          Performance
Statement:     While no axis demand is limited, when the axis reference of one axis changes, the
  flight control subsystem shall keep the velocity along each other translational axis within
  [P-SYS-540] of its reference rate and the body rate about each other rotational axis within
  [P-SYS-550] of its reference rate.
Rationale:     The measurable form of independent control (L0-CON-020) and of the absence of
  cross-axis coupling (L0-CON-030, D18): a manoeuvre on one axis leaves the other five where they
  were. The translational axes are those of the references, the axes of the vehicle-carried
  local frame V (DD-290); with the heading at zero they are the body axes, and at another
  heading the body components of a steady reference turn with the heading, which the force
  resolution of TR follows (DD-300). L1-AER-380 says "body axis" and CR-C4-03 aligns the
  wording. The tolerances are the cross-axis budget that FC shares with EF; EF adds no cross
  response of its own (L2-AER-EF-040), so they depend on FC alone. The statement is limited to
  steps that no demand limit touches: a limited axis demand is the nominal saturation of
  L2-AER-FC-170.
  Sufficiency (L1-AER-380): the six axes of L2-AER-FC-010 are regulated separately
  (L3-AER-FC-TR-010, L3-AER-FC-RO-010) and this record bounds the departure of the other five from
  their references for a step on each in turn, which is the L1 test.
Parent(s):     L1-AER-380
Source:        N-240; D18; L1-AER-380 rationale
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-120; success criteria: in still air, for a step of the axis reference of
  each of the six axes in turn (translational steps from hover and from a horizontal speed of a
  tenth of [P-SYS-230], at headings of zero and of a quarter turn; rotational steps of the
  heading and of the pitch and roll angles), sized so that no axis demand is limited, the
  velocity along each other translational axis stays within [P-SYS-540] of its reference rate and
  the body rate about each other rotational axis stays within [P-SYS-550] of its reference rate
  at each control frame, at full fuel and near dry mass.
Parameters:    P-SYS-540, P-SYS-550, P-SYS-230
TBD/TBR:       P-SYS-540, P-SYS-550 values TBR (TT-100, TT-C4-1), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-130

```req
ID:            L2-AER-FC-130
Level:         L2
Type:          Performance
Statement:     While the vehicle is airborne with fuel remaining, the flight control subsystem shall
  limit the magnitude of the vehicle acceleration that it demands from the translational axes to
  [P-SYS-440].
Rationale:     The crew limit (L0-CON-310, D38, D45) is a limit on the acceleration the crew senses,
  which is the vehicle acceleration minus the gravity vector, so its magnitude is at most the
  vehicle acceleration plus [P-DYN-010] (FUNCTIONAL_ANALYSIS §7.2). Applying the limit to the
  vehicle acceleration that FC demands, and converting it to a force with the current vehicle mass
  (L3-AER-FC-TR-090), makes the allowed resultant force fall with the mass as D38 asks and leaves
  the drag, which the control force must also overcome, outside the limit (DD-320). A limit on
  the resultant force alone, at the mass times [P-SYS-120], would make the maximum speed
  unreachable against the drag of L1-AER-130. FC meets the demand limit even when a large
  position or velocity error asks for more, as nominal saturation (N-260). The demand is not the
  vehicle acceleration: the part of the vehicle acceleration that a disturbance adds is bounded
  by L2-AER-FC-140.
  Sufficiency (L1-AER-290): the closure rule [P-DYN-010] plus [P-SYS-440] at most [P-SYS-120]
  (FUNCTIONAL_ANALYSIS §7.2) makes the sensed acceleration at most [P-SYS-120] when the vehicle
  acceleration is at most [P-SYS-440]; this record limits the demand to it and L2-AER-FC-140
  bounds the disturbance residual, with AF's reference acceleration at most [P-AF-200].
  Sufficiency (L1-AER-300): this record is FC's hard limit and L2-AER-FC-140 its transient
  allowance; AF's share is [P-AF-200], and [P-AF-200] plus [P-FC-020] is at most [P-SYS-440].
Parent(s):     L1-AER-290, L1-AER-300
Source:        D38, D45; N-170; FUNCTIONAL_ANALYSIS §7.1 (upper side), §7.2; DD-320
Allocated to:  TR
Criticality:   Not assessed
Verification:  Inspection — IN-FC-130; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-440, P-SYS-120, P-DYN-010, P-AF-200, P-FC-020
TBD/TBR:       P-SYS-440, P-AF-200, P-FC-020 values TBR (TT-040), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-140

```req
ID:            L2-AER-FC-140
Level:         L2
Type:          Performance
Statement:     While the vehicle is airborne with fuel remaining in a wind within the wind envelope,
  when the magnitude of the acceleration of the translational reference rates is at most
  [P-AF-200], the flight control subsystem shall keep the magnitude of the difference between the
  vehicle acceleration and that reference acceleration at most [P-FC-020].
Rationale:     The split of the vehicle-acceleration budget (L1-AER-300, FUNCTIONAL_ANALYSIS §7.2):
  autoflight commands at most [P-AF-200] and the transients of flight control add at most
  [P-FC-020], their sum being at most [P-SYS-440]. The reference acceleration is the rate of
  change of the translational reference rates, resolved in the local frame V (the reference
  acceleration of the axis references). The difference covers the correction FC adds for an
  error and the acceleration a disturbance causes before FC compensates: a gust that builds up
  over at least [P-SYS-570] changes the drag at a bounded rate (D62), the liftoff of a takeoff in
  the wind [P-SYS-580] gives a step of drag (D73), and both are compensated within the control-loop
  latency [P-SYS-480] and a short settling. TR states both cases (L3-AER-FC-TR-080, -100).
  Sufficiency (L1-AER-300): AF's reference acceleration is at most [P-AF-200] by its own record;
  with this record the vehicle acceleration is at most [P-AF-200] plus [P-FC-020], which is at
  most [P-SYS-440]; L2-AER-FC-130 limits the demand beyond the nominal envelope.
Parent(s):     L1-AER-300
Source:        D16, D51, D62, D73; FUNCTIONAL_ANALYSIS §7.2; IN-C1-34
Allocated to:  TR
Criticality:   Not assessed
Verification:  Inspection — IN-FC-140; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-AF-200, P-FC-020, P-SYS-440, P-SYS-570, P-SYS-580, P-SYS-480
TBD/TBR:       P-SYS-440, P-AF-200, P-FC-020 values TBR (TT-040), P-SYS-570 value TBR (TT-650),
  P-SYS-580 value TBR (TT-860), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-150

```req
ID:            L2-AER-FC-150
Level:         L2
Type:          Functional
Statement:     While the effector activation state is on, the flight control subsystem shall allocate
  the axis demands to effector commands whose resultant control force and control moment equal the
  axis demands, for each set of axis demands within the authority box.
Rationale:     F-AER-06: the six axis demands (a force along and a moment about each body axis) become
  one command for each effector, such that the effectors' resultant is the demand. The authority
  box is the set of combinations that EF guarantees together (L2-AER-EF-330, DD-170), and it
  contains the six pure authorities of L1-AER-120 to -140 (L2-AER-EF-300 to -320), so a demand
  with one component at the limit and the other five at zero is a set within the box. The
  resultant is computed from the commands through the control effectiveness of the vehicle
  parameter set (L2-AER-EF-010, -120); the effector lag is EF's (L2-AER-EF-340). AL states the
  allocation accuracy as parameters.
  Sufficiency (L1-AER-120): L2-AER-EF-300 makes the pure upward force of [P-SYS-400] exist within
  the output limits and this record, through L3-AER-FC-AL-010, commands it, so the Aeronef can
  produce it; FC's share is the allocation, EF's the existence.
  Sufficiency (L1-AER-130): the same for the five other directions and [P-SYS-410]
  (L2-AER-EF-310).
  Sufficiency (L1-AER-140): the same for each pure moment and [P-SYS-420] (L2-AER-EF-320).
Parent(s):     L1-AER-120, L1-AER-130, L1-AER-140
Source:        FUNCTIONAL_ANALYSIS F-AER-06, §7.1; D46, D72; L2-AER-EF-300 to -330
Allocated to:  AL
Criticality:   Not assessed
Verification:  Inspection — IN-FC-150; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-SYS-400, P-SYS-410, P-SYS-420
TBD/TBR:       P-SYS-400, P-SYS-410, P-SYS-420 values TBR (TT-020), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-160

```req
ID:            L2-AER-FC-160
Level:         L2
Type:          Constraint
Statement:     The flight control subsystem shall command each effector within the output limits of
  that effector.
Rationale:     Each effector has a maximum force (L0-CON-300, L1-AER-110). EF clips a command beyond a
  limit (L2-AER-EF-110), so a command beyond it would be harmless to the vehicle but would hide a
  demand that cannot be produced; FC does not rely on output beyond the limits (IN-C3-21).
  The limits are the smallest output [P-EF-130] and the largest output [P-EF-120] of each effector,
  read from the vehicle parameter set (L2-AER-FC-060). The statement holds with the effectors on
  and off, and in the stress case of a demand beyond the authority box (L2-AER-FC-170).
  Sufficiency (L1-AER-110): EF enforces the limit at the effector and this record keeps FC's
  commands within it; together every effector stays within its maximum, as L0-CON-300 asks.
Parent(s):     L1-AER-110
Source:        L0-CON-300; IN-C3-21; owner review at G0
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-160; success criteria: in each automated test run of the regression
  campaign and in a run whose scripted references demand more than the authority box, each
  recorded effector command lies within the output limits of its effector at each control frame.
Parameters:    P-EF-120, P-EF-130
TBD/TBR:       P-EF-120, P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-170

```req
ID:            L2-AER-FC-170
Level:         L2
Type:          Functional
Statement:     When an axis demand lies outside the authority box, the flight control subsystem shall
  allocate that axis demand limited to the authority box, with the effector activation state
  unchanged.
Rationale:     Saturation is nominal behaviour, not a failure (N-260, L1-AER-110 rationale): the
  Aeronef does something defined when a demand exceeds what the effectors can produce. The
  defined behaviour is to limit the demand to the box that EF guarantees, so the limited demand is
  always producible (L2-AER-EF-330), and to carry on. No annunciation, no failure state and no
  change of the activation state follow. The rule that limits the components is a derived
  requirement: each demand component on its own, the others unchanged (L3-AER-FC-AL-020, DD-310).
  The limits of the crew g-limit (L2-AER-FC-130) act earlier, on the acceleration demand.
  Sufficiency (L1-AER-110): L2-AER-FC-160 keeps every command within the output limits and this
  record gives the demand beyond them a defined, producible meaning, so a demand beyond the limit
  is handled as nominal behaviour, as the L1 rationale asks; the priority rule is the derived
  requirement.
Parent(s):     L1-AER-110
Source:        N-260; L1-AER-110 rationale; CONOPS §8.2; D4
Allocated to:  AL
Criticality:   Not assessed
Verification:  Inspection — IN-FC-170; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-180

```req
ID:            L2-AER-FC-180
Level:         L2
Type:          Functional
Statement:     When a limited axis demand returns within its limit, the flight control subsystem
  shall bring that axis within its tracking tolerance, crossing its reference by at most that
  tolerance, within the settling time of that axis.
Rationale:     Saturation as nominal behaviour (N-260) includes the way out of it: a regulator that
  keeps accumulating an error while its demand is limited overshoots long after the limit has
  gone (integrator windup). The requirement is the observable form of a regulation that is aware
  of its limit: once the demand is back within its range the axis settles within the settling
  time of its group (TR, RO) and does not cross the reference by more than its tolerance. How the
  regulation achieves it (back-calculation, conditional integration) is a design decision
  (DD-350). "Limited" covers the demand limit of the effector set (L2-AER-FC-170) and the crew
  limit (L2-AER-FC-130).
  Sufficiency (L1-AER-110): the demand beyond the limit is limited (L2-AER-FC-170) and the axis
  recovers (this record), so the nominal behaviour is defined from the onset of the saturation to
  its end.
  Sufficiency (L1-AER-370): the settling of an axis after a step is L3-AER-FC-TR-060 and
  L3-AER-FC-RO-050; this record extends it to the step that saturates, so each axis settles on its
  reference in all the cases of the L1 test.
Parent(s):     L1-AER-110, L1-AER-370
Source:        N-260; CONOPS §8.2
Allocated to:  TR, RO
Criticality:   Not assessed
Verification:  Inspection — IN-FC-180; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D40).
Parameters:    P-FC-060, P-FC-090
TBD/TBR:       P-FC-060, P-FC-090 values TBR (TT-C4-1), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-190

```req
ID:            L2-AER-FC-190
Level:         L2
Type:          Functional
Statement:     While the axis references carry the off value, the flight control subsystem shall set
  the effector activation state to off and each effector command to zero.
Rationale:     D69: on the ground the effectors are off, so that no fuel is used (L1-AER-930,
  L1-AER-940). Autoflight sends the off value on the ground, after a Land touchdown and at a ground
  start, and the off value carries no mode information (L1-AER-420). FC derives the activation
  state from the off value alone (DD-340): off while it is received, on while it is not
  (L2-AER-FC-200). Both the state and a zero command are set because the effector lag decays to
  zero without reaching it (L2-AER-EF-210). Timing of a landing: a contact at some step of a
  frame is seen in the gear state of the next frame start, at most [P-SYS-310] later; autoflight
  sets the off value in that frame, before FC runs (FUNCTIONAL_ANALYSIS §4.2); FC sets the state
  off in the same frame; EF gives zero output from its first step (L2-AER-EF-210). The effector
  outputs are therefore zero within [P-SYS-310] of the contact, inside the [P-SYS-480] of
  L1-AER-930. Until then the commanded upward force stays below the weight (L2-AER-FC-210).
  Sufficiency (L1-AER-930): AF sets the off value (its child), this record switches the state off
  and commands zero, and L2-AER-EF-210 makes each output zero, so the effectors are off in the
  on-ground state of L1-AER-930; the takeoff is the other case (L2-AER-FC-200).
  Sufficiency (L1-AER-950): a run on the ground starts with the off value from the first control
  frame (AF's child), so FC commands zero and EF produces nothing from step zero.
Parent(s):     L1-AER-930, L1-AER-950
Source:        D69, D73; CONOPS §4.5, SC-130; IN-C3-26; DD-340
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-190; success criteria: in a ground start, and in each landing of the
  takeoff and landing tests, at each control frame that carries the off value the recorded
  effector activation state is off and every recorded effector command is zero; and each effector
  output is zero at each step from [P-SYS-480] after the contact step of a landing, or from step
  zero of a ground start, until the references leave the off value.
Parameters:    P-SYS-310, P-SYS-480
TBD/TBR:       P-SYS-310, P-SYS-480 values TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-200

```req
ID:            L2-AER-FC-200
Level:         L2
Type:          Functional
Statement:     When the axis references change from the off value to axis references, the flight
  control subsystem shall set the effector activation state to on in the control frame that
  carries them.
Rationale:     A takeoff powers up the effectors (D69, glossary *Takeoff*): autoflight engages the
  takeoff and replaces the off value by axis references that hold the position and call for a
  climb, and FC switches the effectors on in the same frame (DD-340). It is the only time the
  effectors work on the ground (L1-AER-930), and the state stays on until the off value returns.
  An airborne test start (D73, B3-1) has axis references from the first frame, so the state is on
  from step zero. Fuel exhaustion needs no case here: EF gives zero output whatever the state
  (L2-AER-EF-200, D68).
  Sufficiency (L1-AER-960): the climb of the takeoff needs the effectors on; this record is FC's
  share of the power-up, AF's being the engagement and the references, and L2-AER-FC-100 and -220
  the tracking and the position in the liftoff wind.
  Sufficiency (L1-AER-930): the effectors work on the ground only while the references are not
  the off value, which is this record with L2-AER-FC-190.
Parent(s):     L1-AER-960, L1-AER-930
Source:        D69; IN-C3-26, IN-C3-30; DD-340
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-200; success criteria: in a ground start in which the first axis
  references that are not the off value are sent at a frame start, the recorded effector
  activation state is on in that control frame and the earlier ones are off, and the vehicle
  lifts off.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-210

```req
ID:            L2-AER-FC-210
Level:         L2
Type:          Functional
Statement:     While the gear state shows the landing gear extended and the reference rate of the
  vertical axis is below zero, the flight control subsystem shall keep the upward control force
  that it commands at most the product of the vehicle mass and [P-DYN-010] reduced by the fraction
  [P-FC-120].
Rationale:     The liftoff rule of the ground contact model: the vehicle leaves the ground at the
  first step at which the upward control force exceeds the weight (MS-DYN §9.6, IN-C1-43). A Land
  descent ends at a contact in some step of a control frame, and the commands of that frame were
  computed before the contact, when the gear state could not yet show it. If those commands carry
  more than the weight, the vehicle lifts off again and makes a second landing. FC therefore
  caps the upward force as long as the gear is extended and the vertical reference rate is
  negative: that is the descent to touchdown, and nothing else in flight, because the gear is
  retracted in flight except between a liftoff and the retraction, when the reference rate is
  positive or zero, and in the Hover that precedes the Land, when it is zero (DD-330). The
  fraction [P-FC-120] keeps the cap below the weight at the rounding of the model; the steady
  descent needs a force below the weight by the drag only, so the cap does not bind in a nominal
  descent. FC reads the gear state only here (CR-C4-02); the contact itself is detected by DYN and
  autoflight, and FC does not detect it.
  Sufficiency (L1-AER-970): the L1 test requires one landing event per landing and no crash;
  with the touchdown speeds of L2-AER-FC-100 inside the landing envelope, this record prevents
  the liftoff after the contact, so the landing is a single event.
  Sufficiency (L1-AER-930): the effectors are off after a landing (L2-AER-FC-190); this record
  keeps the vehicle on the ground in the frame before they are, so that the ground state of
  L1-AER-930 holds.
Parent(s):     L1-AER-970, L1-AER-930
Source:        IN-C1-43; L1-AER-930 rationale; MS-DYN §9.6; DD-330
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-210; success criteria: in each landing from Hover (full fuel and near
  dry mass, in still air and in a steady wind of [P-SYS-430] with gusts of [P-SYS-560] built up
  over [P-SYS-570], from several directions) exactly one landing event occurs and no liftoff
  event follows it; and in a scripted run on the extended gear with a descent reference and a
  vertical speed error that would call for more than the weight, the recorded upward component
  of the commanded control force never exceeds the cap.
Parameters:    P-DYN-010, P-FC-120, P-SYS-430, P-SYS-560, P-SYS-570
TBD/TBR:       P-FC-120 value TBR (TT-C4-1), P-SYS-430, P-SYS-560 values TBR (TT-030), P-SYS-570
  value TBR (TT-650), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-220

```req
ID:            L2-AER-FC-220
Level:         L2
Type:          Performance
Statement:     When the vehicle lifts off in a wind of speed at most [P-SYS-580], the flight control
  subsystem shall keep the horizontal distance between the vehicle position and the reference
  position within [P-SYS-450] at each control frame of the interval of [P-FC-060] that starts at
  the liftoff.
Rationale:     On the ground the ground reaction holds the vehicle against the drag of the wind and
  the flight software does not know the wind (L1-AER-670, FUNCTIONAL_ANALYSIS §7.2). At liftoff
  that drag acts at once, as a step, and the takeoff has to keep the position within the
  budget of L1-AER-960 while the vehicle climbs to the hover height. The reference position of a
  takeoff is the position on the ground (AF), so the guidance share of the budget is zero and FC's
  share is [P-SYS-450]; the interval [P-FC-060] is the translational settling time, long enough
  for the climb to the hover height at [P-AF-240] (a fraction of a second) and for the gear
  retraction. The acceleration the step causes is within [P-FC-020] at dry mass for the limit
  [P-SYS-580] (L3-AER-FC-TR-100); after the interval L3-AER-FC-TR-040 applies.
  Sufficiency (L1-AER-960): the effectors come on (L2-AER-FC-200), the vehicle climbs at the
  reference rate (L3-AER-FC-TR-030) and this record keeps the position in the wind of the liftoff;
  AF's share is the references, the gear retraction and the handover to Hover.
Parent(s):     L1-AER-960
Source:        D69, D73 (B3-Q2); FUNCTIONAL_ANALYSIS §7.2; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-220; success criteria: from ground starts at full fuel and near dry mass,
  in still air and in a steady wind of [P-SYS-580] from several directions, with a takeoff engaged,
  the horizontal distance between the recorded position and the position on the ground is at most
  [P-SYS-450] at each output sample from the liftoff until [P-FC-060] after it.
Parameters:    P-SYS-580, P-SYS-450, P-FC-060, P-AF-240, P-FC-020
TBD/TBR:       P-SYS-580 value TBR (TT-860), P-SYS-450 value TBR (TT-050), P-AF-240 value TBR
  (TT-830), P-FC-060 value TBR (TT-C4-1), P-FC-020 value TBR (TT-040), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-240

```req
ID:            L2-AER-FC-240
Level:         L2
Type:          Performance
Statement:     When the horizontal position and the altitude are held in still air at level attitude,
  the flight control subsystem shall command a resultant control force and control moment whose
  fuel mass, by the consumption relationship of MS-DYN, over a hold of duration [P-DYN-270] is at
  most the product of the sum of one and [P-FU-100] with the fuel mass of a control force equal to
  the vehicle weight over the same time.
Rationale:     Fuel budget (FUNCTIONAL_ANALYSIS §7.3, L1-AER-360, CR-C4-01). The endurance is sized
  for a hold in which the control force only balances the weight; the margin [P-FU-100] covers the
  regulation of the hold, the moments that keep the attitude, the transient at the start and the
  takeoff (L2-AER-FU-290). EF adds nothing to it (the lag has unit gain and no overshoot, the
  resultant is the sum of the outputs: IN-C3-24). FC's commanded resultant is therefore the quantity
  that spends the margin, and this record states that it stays inside it. The consumption relationship
  is on the magnitude of the resultant force and of the resultant moment (DD-110), so the allocation
  of the resultant to the effectors changes nothing. The share of the margin the takeoff uses is
  a few hundredths of a second of hover (L2-AER-FU-290).
  Sufficiency (L1-AER-360): FU sizes the capacity for the margin (L2-AER-FU-290) and EF produces the
  commanded resultant exactly; this record keeps the commanded resultant inside the margin, so
  the endurance holds. It is FC's child once CR-C4-01 allocates L1-AER-360 to FC.
Parent(s):     L1-AER-360
Source:        IN-C2-23, IN-C3-24; FUNCTIONAL_ANALYSIS §7.3; L2-AER-FU-290; D74
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FC-240; success criteria: in a simulated run from a ground start at full
  fuel in still air, with a takeoff engaged at the start and Hover then kept over [P-DYN-270]
  (the run of AN-FU-290), the fuel mass that the consumption relationship of MS-DYN gives for the
  recorded effector commands applied to the effectors' control effectiveness is at most the stated
  product, from the control frame at which the vertical axis first reaches its tolerance of the hover
  height to the end of the hold, and the fuel mass of the takeoff is at most the margin share that
  L2-AER-FU-290 gives it.
Parameters:    P-FU-100, P-DYN-270, P-FU-040, P-FU-050, P-DYN-010
TBD/TBR:       P-FU-100 value TBR (TT-790), P-DYN-270 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-250

```req
ID:            L2-AER-FC-250
Level:         L2
Type:          Interface
Statement:     The flight control subsystem shall provide to the operational data output, at each
  control frame, the axis references it received, the axis demands, the effector commands and the
  effector activation state.
Rationale:     Control activity is one of the three things the operational data relate (L0-OBJ-140,
  L1-AER-630). The effector commands and the axis demands are FC's own signals (the axis demands
  are internal to FC, I-11); the axis references are AF's, and FC provides them as it received them,
  so that what the regulation acted on is recorded (IN-C7-20). The control frame is the output
  sample when the output sample period equals it (IN-C7-32). Whether each signal is releasable or
  protected is decided with the RVS (#69, D44).
  Sufficiency (L1-AER-630): the axis references, axis demands and effector commands are three of
  the five listed signals; the effector outputs are EF's and the fuel mass flow FU's.
Parent(s):     L1-AER-630
Source:        N-250, N-340; IN-C7-20; FUNCTIONAL_ANALYSIS I-33
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-250; success criteria: each listed signal is defined in ICD-AER-TST
  with its unit and frame, and is present in the operational data at each output sample of the
  reference mission (SC-110), with the values that FC received and issued in that control frame.
Parameters:    P-TM-010
TBD/TBR:       Releasable or protected classification (#69), Martin, closes when the plan is extended to
  the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FC-260

```req
ID:            L2-AER-FC-260
Level:         L2
Type:          Constraint
Statement:     The flight control subsystem shall compute each effector command only from the axis
  references, the vehicle state, the gear state, the mass properties, the vehicle parameter set and
  the configuration of the run, and from its own state at the preceding control frames of the run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59, D63 Q4). FC adds
  no variation if its commands depend on nothing but the run's inputs and its own memory of the run:
  no wall-clock time, no random source and no state carried from another run or another simulation
  instance. Bit-identical results are not required (D25, D59).
  Sufficiency (L1-AER-690): FC's commands are part of the operational data and the inputs of EF;
  this record makes them a function of the run's inputs, so a repeated run gives the same FC
  signals and verdicts, which is FC's share.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59, D63
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FC-260; success criteria: two executions of the reference mission (SC-110)
  and of the scripted runs of TP-FC-100, -110 and -120, with the same configuration, initial
  condition, selection or reference script and TST step and wind inputs, in two simulation
  instances, give the same verdict on each success criterion of those procedures.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
