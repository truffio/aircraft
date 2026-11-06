## EF — Effectors

The effector requirements (task C3). The subject of each statement is the effector subsystem (EF), one of the three subsystems of the vehicle model with the dynamics model (DYN) and the FU subsystem, behind the vehicle-model boundary (D55, L1-AER-430). EF implements function F-AER-01 (FUNCTIONAL_ANALYSIS §6.1). It runs at each simulation step `[P-SYS-300]`. Its inputs are the effector commands of the current control frame (one command per effector and the effector activation state, from flight control across the vehicle-model boundary), the fuel availability (from FU) and the vehicle parameter set. Its outputs are the effector output of each effector and the control force and control moment about the centre of gravity that they produce, given to DYN, to FU and, for the outputs, to the operational data.

**The effector model.** The physics is stated in the **effector model** of MS-DYN (section 7.1, proposed in `work/C3/ms_dyn_s7_effectors.md`); these records point to it by name, because a statement cannot carry a section number. In short: each effector is a force emitter along a fixed unit direction through a fixed point of application in the body frame (DD-150); its command is clipped to its output limits and followed through a first-order lag of time constant `[P-EF-020]` (DD-160); its output is zero while fuel is not available or the effectors are off (DD-180); and EF sums the outputs, once per step, into the one control force and control moment that DYN and FU both use (DD-190). Nothing else defines an effector (L0-CON-080, L1-AER-100).

**Solution-free.** The number of effectors and their layout are a design decision, not a requirement. The records constrain the effector set only through what it must achieve (the authority records L2-AER-EF-300 to -330 and the response record -340) and through the closed list of what defines an effector (-010). A reference layout that meets every record is proposed as DD-200 with TBR values (`work/C3/param_proposals.md`); replacing it is a parameter change, with no change to these records.

**Ground operations (D69, D73).** The effector commands carry an effector activation state, on or off, set by the flight software. While it is off, each effector output is zero, so the control force, the control moment and, under DD-110, the fuel mass flow are zero: this is how the effectors are off on the ground before Takeoff and after Land. EF does not model the landing gear. The off state is the EF share of L1-AER-930 (effectors off on the ground, B3, D73), so L2-AER-EF-210 traces to it; the design decision is DD-180.

**Verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would describe the implementation (D4), so each record is verified directly by its own method, and the L1 parents are verified by roll-up (D40, D58). Procedure IDs follow the record number (IN-, AN-, TP-, DM-EF-nnn); Phase 5 (V1) writes the procedures. Several analyses read the effector commands, the effector outputs and the control force and moment at every simulation step; the TST records the vehicle-model interfaces at each step for those runs, as for FU (IN-C2-30, IN-C3-31). The tests that drive EF with scripted effector commands use a test command source in place of flight control (IN-C3-33).

**Coverage of the L1 parents.** Every live L1 record allocated to EF has at least one EF child, except L1-AER-960 and -970 (takeoff and landing capability), added by B3 (D73) after this section was drafted: their EF children are for the C3 rework. L1-AER-230 is Deleted (D54) and has none.

| L1 parent | What EF guarantees, in the parent's terms | EF children |
| --- | --- | --- |
| L1-AER-020 | Each effector output is independent of the other effectors' commands and of the vehicle motion; the only effector cross-term is the fixed, linear control effectiveness, which flight control allocates out (pure wrenches exist, -300 to -320) | -040 |
| L1-AER-040 | The effector set has no aerodynamic control surface and no output that depends on a surface deflection | -030 |
| L1-AER-080 | The control force and moment are the sum of the effector outputs through their control effectiveness, and EF gives them to DYN | -120, -130 |
| L1-AER-090 | The direction of action and the point of application of each effector are constant in the body frame over the run | -020 |
| L1-AER-100 | Each effector is defined only by its direction, point of application (control effectiveness), output limits and command response, all from the run's parameter set; consumption is FU's (L2-AER-FU-060) | -010, -050 |
| L1-AER-110 | Each effector output stays within its output limits, the largest being its maximum force magnitude, whatever the command | -110 |
| L1-AER-120 | A pure upward control force of at least [P-SYS-400] exists within the output limits | -300 |
| L1-AER-130 | A pure control force of at least [P-SYS-410] exists along each of the five other body directions | -310 |
| L1-AER-140 | A pure control moment of at least [P-SYS-420] exists about each body axis in each sense | -320 |
| L1-AER-160 | The control force and moment FU consumes on are the same, computed once from the effector outputs, as those DYN integrates | -120, -140 |
| L1-AER-200 | Each effector output is zero from the first step at which fuel is not available | -200 |
| L1-AER-310 | The effector set produces the drag at maximum speed into the largest wind plus the manoeuvre force, together with the weight and a heading moment | -330 |
| L1-AER-320 | The effector set produces the weight, the vertical drag of the fastest climb at maximum horizontal airspeed and the manoeuvre force, together with the horizontal force | -330 |
| L1-AER-330 | The effector set produces the vertical force of the fastest descent at maximum horizontal airspeed, together with the horizontal force | -330 |
| L1-AER-350 | The effector set produces the moment that reaches [P-SYS-270] at maximum inertia, together with the forces | -330 |
| L1-AER-360 | In a hold, the effector outputs settle on their commands with no steady-state difference and the resultant is exactly their sum, so the fuel used is that of the commanded resultant | -100, -120 |
| L1-AER-380 | No effector cross-coupling, and each force and moment component can change over its whole range while the others are held | -040, -330 |
| L1-AER-430 | EF takes only the effector commands from the flight software and gives it nothing | -400 |
| L1-AER-460 | The effector set produces the gust drag and the regulation force together, and its response time fits the latency budget | -330, -340 |
| L1-AER-630 | EF gives the operational data output the effector output of each effector at each step | -410 |
| L1-AER-690 | Each effector output depends only on the run's parameter set, commands and fuel availability | -420 |
| L1-AER-710 | A command is used from the first step of its control frame, and the output reaches it within [P-EF-010], so one control frame plus [P-EF-010] is at most [P-SYS-480] | -100, -150, -340 |
| L1-AER-720 | MS-DYN states the effector model | -430 |
| L1-AER-930 | While the effector activation state is off, each effector output, and so the control force and moment, is zero | -210 |

No record is Derived: L2-AER-EF-210 (DD-180, the effector activation state; D69) traces to L1-AER-930 since B3 (D73).

### L2-AER-EF-010

```req
ID:            L2-AER-EF-010
Level:         L2
Type:          Constraint
Statement:     The effector subsystem shall define each effector only by its direction of action in
  [P-EF-100], its point of application in [P-EF-110], its output limits in [P-EF-120] and
  [P-EF-130] and its command response through [P-EF-020].
Rationale:     No physical explanation of the emitter is required (L0-CON-080); an effector is
  characterised by a closed list of kinds (L1-AER-100). The direction of action is the fixed unit
  vector along which the effector pushes (CV-330). The control effectiveness, the force and moment
  about the centre of gravity per newton of output, follows from the direction and the point of
  application: the force is the direction and the moment is the cross product of the point of
  application with the direction (DD-150). The centre of gravity is the body origin at every
  fuel state (L2-AER-FU-150), so the moment arm is constant. The output limits are the smallest
  output [P-EF-130] and the largest output [P-EF-120], which is the maximum force magnitude of
  L0-CON-300. The command response is the first-order lag of time constant [P-EF-020] (DD-160);
  [P-EF-010] and [P-EF-030] state the response it must achieve (L2-AER-EF-340). The number of
  effectors is the number of entries in these lists; it is part of the layout, which is a design
  decision (DD-200). The consumption parameters are FU's and common to the effector set
  (L2-AER-FU-060, D65).
  Sufficiency (L1-AER-100): this record gives the first four kinds (direction, effectiveness, limits,
  command response), L2-AER-EF-050 takes them from the run's parameter set, and L2-AER-FU-060 makes
  the two FU consumption sets the only parameters of the fifth kind, so together each effector is
  defined only by the five listed kinds.
Parent(s):     L1-AER-100
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §7; L0-CON-080; CV-330; D19, D65
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-010; success criteria: each EF parameter in the parameter database
  is of one of the kinds direction of action ([P-EF-100]), control effectiveness ([P-EF-110]),
  output limits ([P-EF-120], [P-EF-130]) or command response ([P-EF-010], [P-EF-020],
  [P-EF-030]); the MS-DYN effector model uses no other parameter to compute an effector output or
  the control force and moment; and no EF parameter enters a consumption relationship.
Parameters:    P-EF-100, P-EF-110, P-EF-120, P-EF-130, P-EF-020, P-EF-010, P-EF-030
TBD/TBR:       P-EF-010 value TBR (TT-080), P-EF-020, P-EF-030, P-EF-100, P-EF-110, P-EF-120,
  P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-020

```req
ID:            L2-AER-EF-020
Level:         L2
Type:          Constraint
Statement:     The effector subsystem shall keep the direction of action and the point of application
  of each effector constant in the body frame over each run.
Rationale:     Nothing swivels (D19, L0-CON-070): each effector acts along a fixed direction in the
  body frame (CV-330). The point of application is fixed as well, so the control effectiveness of
  each effector is a constant of the run. A force that turns with the attitude in the local frame
  is the rigid-body resolution of a body-fixed force (MS-DYN kinematic term K-3), not a swivel.
  The layout of the directions is a design decision (DD-200), not a requirement.
  Sufficiency (L1-AER-090): the effector subsystem is the only place the direction of action is
  defined (L1-AER-090 rationale), and this record makes it constant in the body frame for each
  effector, which is the whole of L1-AER-090.
Parent(s):     L1-AER-090
Source:        D19; CV-330; AIRCRAFT_CHARACTERISTICS.md §3
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-020; success criteria: the MS-DYN effector model defines the
  direction of action and the point of application of each effector as constants of the run's
  vehicle parameter set, with no dependence on time, on the effector commands or on the vehicle
  state, and the implementation reads them only at the start of the run.
Parameters:    P-EF-100, P-EF-110
TBD/TBR:       P-EF-100, P-EF-110 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-030

```req
ID:            L2-AER-EF-030
Level:         L2
Type:          Constraint
Statement:     The effector subsystem shall produce the control force and the control moment only from
  effector outputs along the fixed directions of action, with no aerodynamic control surface and no
  output that depends on a surface deflection.
Rationale:     Motion comes from the effectors, not from control surfaces (OBJECTIVES §2;
  AIRCRAFT_CHARACTERISTICS §2, §7). An effector output depends only on its command, the effector
  activation state and the fuel availability (L2-AER-EF-040), so no output can depend on the
  airflow over a surface. The parts of the statement are one prohibition (D30).
  Sufficiency (L1-AER-040): a control surface would appear either in the dynamics or in the
  effector set (L1-AER-040 rationale). L2-AER-DYN-170 excludes it from the dynamics; this record
  excludes it from the effector set.
Parent(s):     L1-AER-040
Source:        L0-CON-050; OBJECTIVES.md §2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-030; success criteria: the MS-DYN effector model and the
  implementation define no control surface, no surface deflection and no effector output or
  control force or moment that depends on one or on the air-relative velocity.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-040

```req
ID:            L2-AER-EF-040
Level:         L2
Type:          Constraint
Statement:     The effector subsystem shall make the output of each effector independent of the
  effector commands of the other effectors, of the vehicle state and of the wind.
Rationale:     The EF share of D18: no effector cross-coupling (L1-AER-020 rationale). Each effector
  output follows its own command only (MS-DYN effector model); it does not change with the
  position, altitude, velocity, airspeed, attitude or body rates, so a motion along one degree of
  freedom changes no effector output and adds no term to the equations of motion. The one place
  where effectors meet is the sum of their outputs through the fixed control effectiveness
  (L2-AER-EF-120). That sum is linear with constant coefficients, so flight control can allocate
  each axis demand with the other five components at zero (L1-AER-020 rationale), and the
  effector set can produce each pure force and moment (L2-AER-EF-300 to -320).
  Sufficiency (L1-AER-020): DYN excludes drag and kinematic cross-terms beyond its list
  (L2-AER-DYN-050, -190), FU excludes products of inertia (L2-AER-FU-180), and this record excludes
  effector cross-coupling, the third source L1-AER-020 names; with the pure authorities, the
  geometric coupling of the layout is one that allocation removes.
  Sufficiency (L1-AER-380): with L2-AER-EF-330 (each component can change while the others are
  held), this record makes the effector set add no cross-axis response of its own, so the
  cross-axis tolerances [P-SYS-540] and [P-SYS-550] depend only on flight control, which owns
  them (L1-AER-380 rationale).
Parent(s):     L1-AER-020, L1-AER-380
Source:        D18; L1-AER-020 rationale; MS-DYN kinematic terms list
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-040; success criteria: in the MS-DYN effector model and the
  implementation, the output of each effector is computed from that effector's command, the
  effector activation state, the fuel availability and the EF parameters only, and no vehicle
  state element, wind value or other effector's command enters the computation.
Parameters:    P-SYS-540, P-SYS-550
TBD/TBR:       P-SYS-540, P-SYS-550 values TBD (TT-100), Martin, G2 (C4)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-050

```req
ID:            L2-AER-EF-050
Level:         L2
Type:          Constraint
Statement:     When a run starts, the effector subsystem shall take [P-EF-020], [P-EF-100], [P-EF-110],
  [P-EF-120] and [P-EF-130] from the vehicle parameter set of the run's configuration.
Rationale:     The effector parameters are configurable values of the vehicle model, like the drag
  area and the masses (N-020, L2-AER-DYN-440, L2-AER-FU-010), so a campaign can change the layout,
  the limits or the response without a software change, and EF holds them constant for the run
  (L2-AER-EF-020). The identity and version of the parameter set are output by TM (L1-AER-650).
  [P-EF-010] and [P-EF-030] are requirement values, not model inputs.
  Sufficiency (L1-AER-100): see L2-AER-EF-010; this record makes the listed kinds the parameters
  the model actually runs with.
Parent(s):     L1-AER-100
Source:        N-020, N-350; F-AER-14
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-EF-050; success criteria: two runs from the same initial
  condition and effector command script, with two vehicle parameter sets that differ in
  [P-EF-120] and [P-EF-020] and with no software change, each give at each output sample effector
  outputs that equal the independent computation of AN-EF-100 with that run's values, and each
  run outputs the identity of the parameter set it used.
Parameters:    P-EF-020, P-EF-100, P-EF-110, P-EF-120, P-EF-130
TBD/TBR:       P-EF-020, P-EF-100, P-EF-110, P-EF-120, P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-100

```req
ID:            L2-AER-EF-100
Level:         L2
Type:          Model fidelity
Statement:     The effector subsystem shall compute the effector output of each effector at each
  simulation step from its effector command by the effector model of MS-DYN, with the time
  constant [P-EF-020] and the output limits [P-EF-120] and [P-EF-130].
Rationale:     The command response is one of the kinds that define an effector (L1-AER-100), and the
  effector is part of the control loop whose latency is budgeted (L1-AER-710, DD-020). The MS-DYN
  effector model clips the command to the output limits and follows the clipped command through a
  first-order lag, stepped exactly once per simulation step, with the output of a step already
  responding to the command of that step (DD-160). It is the minimal actuator dynamics: it gives
  the control laws a finite response to work against (L0-OBJ-020), it never overshoots, it stays
  within the output limits, and its steady-state gain is one, so a held command is produced
  exactly. The output is zero while fuel is not available or the effectors are off, and before
  the first effector commands of a run (L2-AER-EF-200, -210; IN-C1-12). Each output is one value per
  step, held over the step (DD-100, IN-C2-12).
  Sufficiency (L1-AER-710): see L2-AER-EF-340.
  Sufficiency (L1-AER-360): with L2-AER-EF-120, this record makes the control force and moment of a
  hold equal to the resultant of the commands flight control holds, with no steady-state difference
  and no output beyond it, so the fuel used in the hold is that of the commanded resultant; FC
  keeps that resultant at the weight within the margin [P-FU-100] (IN-C3-24) and FU sizes the fuel
  for it (L2-AER-FU-290).
Parent(s):     L1-AER-710, L1-AER-360
Source:        L0-CON-080; DD-020; D65; IN-C1-12, IN-C2-12
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-100; success criteria: with the effector commands and outputs
  recorded at each simulation step (IN-C3-31), in a run with commanded steps of each sign for each
  effector, commands beyond each output limit, an off period and a fuel exhaustion, and in the
  reference mission (SC-110), each recorded effector output, from step zero, equals the independent
  computation of the MS-DYN effector model from the recorded commands, effector activation state,
  fuel availability and the run's [P-EF-020], [P-EF-120], [P-EF-130] and [P-SYS-300], to
  floating-point rounding.
Parameters:    P-EF-020, P-EF-120, P-EF-130, P-SYS-300, P-FU-100
TBD/TBR:       P-EF-020, P-EF-120, P-EF-130 values TBR (TT-930), P-SYS-300 value TBR (TT-070),
  P-FU-100 value TBR (TT-790), Martin, G2 (I1); MS-DYN effector model content (TT-780), Martin, G2
  (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-110

```req
ID:            L2-AER-EF-110
Level:         L2
Type:          Functional
Statement:     The effector subsystem shall keep the effector output of each effector within the output
  limits that [P-EF-130] and [P-EF-120] give for that effector.
Rationale:     Each effector has a maximum force (L0-CON-300, L1-AER-110). The largest output
  [P-EF-120] is the maximum force magnitude of each effector, and the smallest output [P-EF-130]
  lies between its negative and zero: a negative value makes an effector able to push both ways,
  zero makes it push one way only (CV-330 leaves this to EF). The limit holds whatever the command:
  the model clips a command beyond a limit, and the lag keeps the output between the previous
  output and the clipped command (MS-DYN effector model), so a demand beyond the limit is nominal
  behaviour, not a failure. Flight control's share is to handle such a demand by its priority rule
  (FC1) and not to rely on output beyond the limit.
  Sufficiency (L1-AER-110): EF enforces the limit at each effector (this record, with the maximum
  force of each effector defined as a parameter by L2-AER-EF-010), and FC never relies on output
  beyond it (its child); together each effector stays within its maximum, as L1-AER-110 requires.
Parent(s):     L1-AER-110
Source:        L0-CON-300; owner review at G0; CV-330
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-110; success criteria: (1) with scripted effector commands of twice
  [P-EF-120] and of twice the negative of [P-EF-120] for each effector in turn, each recorded
  effector output lies within the limits of [P-EF-130] and [P-EF-120] for that effector at each
  output sample, and settles on the limit the command exceeds; (2) in each automated test run of
  the regression campaign, no recorded effector output lies outside the output limits of its
  effector.
Parameters:    P-EF-120, P-EF-130
TBD/TBR:       P-EF-120, P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-120

```req
ID:            L2-AER-EF-120
Level:         L2
Type:          Model fidelity
Statement:     The effector subsystem shall compute the control force and the control moment about the
  centre of gravity of each simulation step as the sum, over the effectors, of each effector output
  of that step times its control effectiveness from the effector model of MS-DYN.
Rationale:     The effectors are the only source of control force and moment (L0-CON-060,
  L1-AER-080). The control effectiveness of an effector is its direction of action for the force
  and the cross product of its point of application with its direction for the moment, per newton
  of output (DD-150). EF computes the sum once per step, and DYN and FU both use that one result
  (DD-190, IN-C2-11), so the motion and the fuel used come from the same control force and
  moment. The sum is the whole of the control force and moment: there is no bias, no interaction
  term and no other contribution.
  Sufficiency (L1-AER-080): with L2-AER-EF-130 (given to DYN) and L2-AER-DYN-180 (DYN takes the
  control force and moment from EF only), this record makes each control force and moment the
  product of the effectors, as L1-AER-080 requires.
  Sufficiency (L1-AER-160): with L2-AER-EF-140 (given to FU) and L2-AER-FU-040 (the consumption
  relationships), this record supplies the control forces and moments that the fuel mass flow is
  computed from.
  Sufficiency (L1-AER-360): see L2-AER-EF-100.
Parent(s):     L1-AER-080, L1-AER-160, L1-AER-360
Source:        L0-CON-060; I-01, I-02; IN-C2-11; MS-DYN effector model
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-120; success criteria: with the effector outputs and the control
  force and moment recorded at each simulation step (IN-C3-31), in the reference mission (SC-110)
  and in runs with each effector commanded alone, the recorded control force and control moment
  of each step equal the independent sum of the recorded outputs through the effectiveness computed
  from [P-EF-100] and [P-EF-110], to floating-point rounding, and are zero at each step whose
  outputs are zero.
Parameters:    P-EF-100, P-EF-110
TBD/TBR:       P-EF-100, P-EF-110 values TBR (TT-930), Martin, G2 (I1); MS-DYN effector model
  content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-130

```req
ID:            L2-AER-EF-130
Level:         L2
Type:          Interface
Statement:     The effector subsystem shall give the dynamics model, at each simulation step, the
  control force and the control moment of that step, in the body frame and about the centre of
  gravity, through the interface that MS-DYN defines between the two subsystems.
Rationale:     Interface I-02 is internal to the vehicle model, so it is defined in MS-DYN, not in an
  ICD (IN-C1-10). DYN holds the value over the step (DD-100, MS-DYN step input hold). The frame and
  the reference point follow CV-310, CV-320 and CV-340.
  Sufficiency (L1-AER-080): see L2-AER-EF-120.
Parent(s):     L1-AER-080
Source:        FUNCTIONAL_ANALYSIS §3.2 I-02; IN-C1-10
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-130; success criteria: MS-DYN defines the interface from EF to DYN
  with the control force in the body frame and the control moment about the centre of gravity, in
  N and N·m, one value per simulation step, and the equations of motion take their control force
  and moment from it only.
Parameters:    —
TBD/TBR:       MS-DYN effector model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-140

```req
ID:            L2-AER-EF-140
Level:         L2
Type:          Interface
Statement:     The effector subsystem shall give the FU subsystem, at each simulation step, the
  effector outputs of that step with the control force and the control moment that it gives the
  dynamics model for that step, through the interface that MS-DYN defines between the two
  subsystems.
Rationale:     Interface I-01 is internal to the vehicle model. FU charges the fuel on the magnitude
  of the resultant control force and moment (DD-110), so the resultant it uses must be the one DYN
  integrates (IN-C2-11; inspection G2 §4 note to EF). EF computes it once and gives both
  subsystems the same value (DD-190); it also gives FU the effector outputs, which
  L2-AER-FU-070 names. One value per step, held over the step, so the fuel used in the step is the
  flow times the step exactly (IN-C2-12).
  Sufficiency (L1-AER-160): see L2-AER-EF-120.
Parent(s):     L1-AER-160
Source:        FUNCTIONAL_ANALYSIS §3.2 I-01; IN-C2-11, IN-C2-21
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-140; success criteria: MS-DYN defines the interface from EF to FU
  with the effector outputs and the control force and moment of each simulation step; the control
  force and moment that FU uses and those DYN uses come from one computation; no FU requirement
  takes a control force or moment from another source.
Parameters:    —
TBD/TBR:       MS-DYN effector model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-150

```req
ID:            L2-AER-EF-150
Level:         L2
Type:          Interface
Statement:     The effector subsystem shall use, at each simulation step, the effector commands that
  flight control issues for the control frame that contains that step.
Rationale:     Flight control computes the effector commands at the start of each control frame
  from the state of its first step and holds them for the frame (FUNCTIONAL_ANALYSIS §4.2). Using
  them from the first step of that frame, not from the next one, keeps the first change of effector
  output at the frame start, so the time from a vehicle state to the first change of output that
  responds to it is at most one control frame [P-SYS-310] (DD-020). Whether a TST input timestamped
  k first affects step k or k + 1 is an ICD-AER-TST matter (CV-840); this record concerns only
  the flight-software commands.
  Sufficiency (L1-AER-710): see L2-AER-EF-340.
Parent(s):     L1-AER-710
Source:        FUNCTIONAL_ANALYSIS §4.2, §7.5; DD-010, DD-020
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-150; success criteria: with the effector commands and outputs recorded
  at each simulation step (IN-C3-31), for each control frame of a run whose effector commands
  differ from those of the previous frame, the effector outputs of the first step of that frame
  respond to the new commands, as the computation of AN-EF-100 gives.
Parameters:    P-SYS-310
TBD/TBR:       P-SYS-310 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-200

```req
ID:            L2-AER-EF-200
Level:         L2
Type:          Functional
Statement:     While the fuel availability is not available, the effector subsystem shall produce zero
  effector output from each effector.
Rationale:     The output of each effector depends on the availability of fuel (L0-CON-100, I-03).
  Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070): the vehicle then moves under
  gravity and drag alone (D68). FU gives not available from the first step whose remaining fuel mass
  is zero (L2-AER-FU-200, DD-130). In a step that starts with fuel available, EF produces its
  commanded output for the whole step and FU limits the fuel used in that step (IN-C2-20). The
  output is set to zero at once, not through the lag, and the lag starts again from zero (MS-DYN
  effector model), so there is no output on fuel that is not there. Sufficiency (L1-AER-200): FU
  makes fuel not available from the first step with zero fuel (L2-AER-FU-200); this record makes
  each output, and so the control force and moment (L2-AER-EF-120), zero while it is, so the two
  give zero control force and moment from that step, as L1-AER-200 requires. A run started with zero
  fuel stays on the ground (B3, CONOPS SC-130 variation zero fuel).
Parent(s):     L1-AER-200
Source:        N-150; CONOPS §4.5, SC-110; L0-ASM-070; D68
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-200; success criteria: in the reference mission (SC-110) and in a run
  started with zero fuel, with non-zero effector commands, each recorded effector output is zero at
  each output sample from the first sample whose simulation step has fuel not available to the end
  of the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-210

```req
ID:            L2-AER-EF-210
Level:         L2
Type:          Functional
Statement:     While the effector activation state is off, the effector subsystem shall produce zero
  effector output from each effector.
Rationale:     D69: runs start on the ground with the effectors off, and after a Land touchdown the
  effectors switch off so that fuel use stops (L1-AER-930, D73). The design decision DD-180 puts the
  off state in the effector commands: the flight software sets the effector activation state, on or
  off, with the effector commands, so it crosses the vehicle-model boundary as a kind already listed
  by L1-AER-430. While it is off, each output is zero, so the control force and moment are zero and,
  under DD-110, the fuel mass flow is zero with no new consumption term (L1-AER-940). The state is
  off before the first effector commands of a run (MS-DYN effector model; IN-C1-12). An exactly zero
  command would not do: the lag decays to zero but does not reach it in a finite time. Which
  subsystem decides the state is for C4 and C5 (L1-AER-420 off value of the axis references).
  Sufficiency (L1-AER-930): AF sets the off value of the axis references and FC sets the effector
  activation state off (C4, C5); this record makes each output, and so the control force and moment
  (L2-AER-EF-120), zero while the state is off, which is the EF share of L1-AER-930.
Parent(s):     L1-AER-930
Source:        D69, D73; DD-180; IN-C1-12; work/C3/issues.md C3-Q06
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-210; success criteria: in a run that starts with the effector activation
  state off and non-zero effector commands, and in a run that sets it off during flight, each
  recorded effector output is zero at each output sample whose simulation step has the state off,
  and, when the state returns to on, the outputs follow the computation of AN-EF-100 from zero.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-300

```req
ID:            L2-AER-EF-300
Level:         L2
Type:          Performance
Statement:     While the fuel availability is available and the effector activation state is on, the
  effector subsystem shall be able to produce a control force of at least [P-SYS-400] along the
  negative body z axis with the other control force and control moment components at zero.
Rationale:     Weight-bearing authority (FUNCTIONAL_ANALYSIS §7.1; D46 as revised by D72). The
  budget is the maximum vehicle mass times the sum of [P-DYN-010] and [P-SYS-440], plus the drag
  in the fastest climb: 39.6 kN with the current database (G2-F04, verified). Under isotropic drag
  the vertical drag in a climb at [P-SYS-240] is shared with the horizontal airspeed (G2-F06), and
  at the largest horizontal airspeed it raises the need to 58.6 kN; C3 proposes [P-SYS-400] at
  60 kN TBR to cover it (C3-Q02, CR-C3-01). The force does not depend on the mass: the effectors
  produce it at every fuel state, and the crew limit caps the usable force at low mass
  (L1-AER-290, FC). The upward authority may be smaller than the other five (D72).
  Sufficiency (L1-AER-120): this record makes the pure upward force exist within the output
  limits; FC's child commands it. Together they give the authority of L1-AER-120.
Parent(s):     L1-AER-120
Source:        FUNCTIONAL_ANALYSIS §7.1; D46, D57, D72; G2-F04, G2-F06
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-300; success criteria: from the parameter database values of
  [P-EF-100], [P-EF-110], [P-EF-120] and [P-EF-130], an independent linear-programming computation
  finds effector outputs within the output limits whose control force is [P-SYS-400] along the
  negative body z axis and whose other force and moment components are zero, to floating-point
  rounding; and [P-SYS-400] is at least the budget of FUNCTIONAL_ANALYSIS §7.1 with the database
  values.
Parameters:    P-SYS-400, P-EF-100, P-EF-110, P-EF-120, P-EF-130, P-DYN-010, P-SYS-440, P-SYS-240
TBD/TBR:       P-SYS-400 value TBR (TT-020), P-SYS-440 value TBR (TT-040), P-SYS-240 value TBR
  (TT-010), P-EF-100 to P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-310

```req
ID:            L2-AER-EF-310
Level:         L2
Type:          Performance
Statement:     While the fuel availability is available and the effector activation state is on, the
  effector subsystem shall be able to produce a control force of at least [P-SYS-410] along each of
  the positive and negative body x axis, the positive and negative body y axis and the positive
  body z axis, with the other control force and control moment components at zero.
Rationale:     Non-weight-bearing authority (FUNCTIONAL_ANALYSIS §7.1). The budget is the maximum
  vehicle mass times [P-SYS-440] plus the drag at the maximum horizontal speed [P-SYS-230], a
  ground speed (D72), into the largest instantaneous wind [P-SYS-430] plus [P-SYS-560]: an airspeed
  of 231.5 m/s and 186.2 kN at sea level (G2-F04, verified). In a climb at that airspeed the
  horizontal drag rises to 187.6 kN (shared magnitude, G2-F06); C3 proposes [P-SYS-410] at 190 kN
  TBR. The downward direction is listed with the four horizontal ones by L1-AER-130; it needs
  about 29 kN, and oversizing it costs no fuel, because consumption is charged on the resultant
  (DD-110), so no change request is raised (C3-Q08). These five directions exceed the upward
  authority, as D72 allows.
  Sufficiency (L1-AER-130): this record makes each of the five pure forces exist within the output
  limits; FC's child commands them.
Parent(s):     L1-AER-130
Source:        FUNCTIONAL_ANALYSIS §7.1; D51, D72; G2-F03, G2-F04
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-310; success criteria: from the parameter database values of
  [P-EF-100], [P-EF-110], [P-EF-120] and [P-EF-130], an independent linear-programming computation
  finds, for each of the five directions, effector outputs within the output limits whose control
  force is [P-SYS-410] along that direction and whose other force and moment components are zero,
  to floating-point rounding; and [P-SYS-410] is at least the budget of FUNCTIONAL_ANALYSIS §7.1
  with the database values.
Parameters:    P-SYS-410, P-EF-100, P-EF-110, P-EF-120, P-EF-130, P-SYS-440, P-SYS-230, P-SYS-430,
  P-SYS-560
TBD/TBR:       P-SYS-410 value TBR (TT-020), P-SYS-440 value TBR (TT-040), P-SYS-430, P-SYS-560
  values TBR (TT-030), P-EF-100 to P-EF-130 values TBR (TT-930), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-320

```req
ID:            L2-AER-EF-320
Level:         L2
Type:          Performance
Statement:     While the fuel availability is available and the effector activation state is on, the
  effector subsystem shall be able to produce a control moment of at least [P-SYS-420] about each
  body axis in each sense, with the other control force and control moment components at zero.
Rationale:     Rotational authority (FUNCTIONAL_ANALYSIS §7.1). The drag-moment lines of the budget
  are zero, because drag acts at the centre of gravity (DD-050), and so is the moment to hold pitch
  and roll against it. The remaining line is the largest moment of inertia times the angular
  acceleration that reaches [P-SYS-270] within the heading-rate onset time. With the capsule and a
  uniform mass and fuel distribution (MS-DYN mass-properties model reference derivation), the
  largest moment of inertia at full fuel is 15 975 kg·m²; C3 proposes [P-SYS-420] at 2000 N·m
  TBR, which reaches [P-SYS-270] in 0.50 s from rest at that inertia. C4 confirms that it needs no
  shorter onset (IN-C3-25), and the value is re-derived when [P-FU-070] and [P-FU-080] are set.
  Sufficiency (L1-AER-140): this record makes each pure moment exist within the output limits;
  FC's child commands them.
Parent(s):     L1-AER-140
Source:        FUNCTIONAL_ANALYSIS §7.1; D57, D61; DD-050
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-320; success criteria: from the parameter database values of
  [P-EF-100], [P-EF-110], [P-EF-120] and [P-EF-130], an independent linear-programming computation
  finds, for each body axis and each sense, effector outputs within the output limits whose control
  moment is [P-SYS-420] about that axis and whose other force and moment components are zero, to
  floating-point rounding; and [P-SYS-420] is at least the largest principal moment of
  [P-FU-070] plus [P-FU-080] times [P-SYS-270] divided by the onset time C4 sets.
Parameters:    P-SYS-420, P-EF-100, P-EF-110, P-EF-120, P-EF-130, P-SYS-270, P-FU-070, P-FU-080
TBD/TBR:       P-SYS-420 value TBR (TT-020), P-SYS-270 value TBR (TT-010), P-FU-070, P-FU-080 values
  TBD (TT-770), heading-rate onset time (C4, IN-C3-25), P-EF-100 to P-EF-130 values TBR (TT-930),
  Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-330

```req
ID:            L2-AER-EF-330
Level:         L2
Type:          Performance
Statement:     While the fuel availability is available and the effector activation state is on, the
  effector subsystem shall be able to produce together each control force and control moment whose
  components along the body x and y axes are each within [P-SYS-410] of zero, whose component along
  the body z axis lies from the negative of [P-SYS-400] to [P-SYS-410], and whose component about
  each body axis is within [P-SYS-420] of zero.
Rationale:     The performance records need the forces and the moment together, not one at a time.
  At maximum speed into the largest wind the vehicle carries its weight upward, overcomes up to
  186 kN of horizontal drag in any body direction (heading and track are independent, CV-550) and
  turns; in the fastest climb at that airspeed it needs up to 58.6 kN upward with the horizontal
  force. The pure authorities (L2-AER-EF-300 to -320) do not give that. This record asks for the
  whole authority box (DD-170): each component can take any value in its range whatever the
  others are, so flight control can allocate and saturate each axis on its own, and a change on
  one degree of freedom never forces another (L1-AER-380). The box contains the six pure
  authorities; they stay as their own records because they are the direct children of
  L1-AER-120 to -140, and the box can be revised without them. The achievable set is convex
  (MS-DYN effector model), so the box is inside it when its corners are. The reference layout
  meets the box with a margin of 4.5 % (DD-200).
  Sufficiency (L1-AER-310): the box covers the drag at [P-SYS-230] into the largest wind plus the
  manoeuvre force in any horizontal direction, with the weight and a heading moment; FC and AF
  regulate within it.
  Sufficiency (L1-AER-320): the box covers the weight, the manoeuvre force and the vertical drag
  of a climb at [P-SYS-240] at the largest horizontal airspeed, with the horizontal force.
  Sufficiency (L1-AER-330): a descent at [P-SYS-250] needs less upward force than the weight, or
  a downward force of at most 29 kN at speed; both are inside the box.
  Sufficiency (L1-AER-350): the box gives [P-SYS-420] about the vertical axis together with the
  forces, which reaches [P-SYS-270] at maximum inertia (L2-AER-EF-320).
  Sufficiency (L1-AER-380): see L2-AER-EF-040.
  Sufficiency (L1-AER-460): the drag of the largest instantaneous wind on a hold, 18.2 kN, plus the
  regulation force, is inside the box; with L2-AER-EF-340 (response) the EF share of the hold
  accuracy is met, and FC's share [P-FC-010] is its own.
Parent(s):     L1-AER-310, L1-AER-320, L1-AER-330, L1-AER-350, L1-AER-380, L1-AER-460
Source:        FUNCTIONAL_ANALYSIS §7.1; D18, D51, D72; G2-F06; MS-DYN drag model
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-EF-330; success criteria: from the parameter database values of
  [P-EF-100], [P-EF-110], [P-EF-120] and [P-EF-130], an independent linear-programming computation
  finds, for each corner of the box that [P-SYS-400], [P-SYS-410] and [P-SYS-420] define, effector
  outputs within the output limits that produce that control force and moment, to floating-point
  rounding.
Parameters:    P-SYS-400, P-SYS-410, P-SYS-420, P-EF-100, P-EF-110, P-EF-120, P-EF-130, P-SYS-230,
  P-SYS-240, P-SYS-250, P-SYS-270, P-FC-010
TBD/TBR:       P-SYS-400, P-SYS-410, P-SYS-420 values TBR (TT-020), P-SYS-240, P-SYS-250, P-SYS-270
  values TBR (TT-010), P-FC-010 value TBR (TT-050), P-EF-100 to P-EF-130 values TBR (TT-930),
  Martin, G2 (I1); authority box shape (DD-170, C3-Q03), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-340

```req
ID:            L2-AER-EF-340
Level:         L2
Type:          Performance
Statement:     When the effector command of an effector changes while the fuel availability is
  available and the effector activation state is on, the effector subsystem shall bring that
  effector output within the fraction [P-EF-030] of the size of the change of its clipped command
  from the new clipped command, within [P-EF-010] of the change.
Rationale:     The EF share of the control-loop latency (L1-AER-710, DD-020): one control frame
  [P-SYS-310] plus the effector command response time [P-EF-010] is at most [P-SYS-480]
  (FUNCTIONAL_ANALYSIS §7.5). "Reaching" the command, which the P-EF-010 description leaves to C3,
  is entering the band [P-EF-030] around it, measured as CV-860 states from the step at which the
  new command applies. C3 proposes [P-EF-010] = 0.06 s and [P-EF-030] = 0.05, TBR. With the lag
  time constant [P-EF-020] = 0.015 s and [P-SYS-300] = 0.01 s the model enters the band 0.04 s
  after the change; 0.02 s plus 0.06 s is 0.08 s, inside the 0.1 s of [P-SYS-480]. The lag does not
  overshoot, so the output stays in the band while the command is held. The clipped command is the
  command within the output limits (L2-AER-EF-110).
  Sufficiency (L1-AER-710): L2-AER-EF-150 makes the first change of output fall at the start of
  the frame that carries the new command, at most [P-SYS-310] after the state it responds to, and
  this record brings the output to the command within [P-EF-010] of that; with the model of
  L2-AER-EF-100 and FC's share of the frame, both the first change and the reaching of the command
  are within [P-SYS-480].
  Sufficiency (L1-AER-460): the response time is the EF delay inside the latency that FC's
  regulation share [P-FC-010] is designed against; this record bounds it.
Parent(s):     L1-AER-710, L1-AER-460
Source:        DD-020; FUNCTIONAL_ANALYSIS §7.5; CV-860
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-340; success criteria: for each effector, with scripted effector
  commands stepping from zero to [P-EF-120], from [P-EF-120] to [P-EF-130], and by a tenth of
  [P-EF-120], the time from the step at which the new command applies to the first output sample
  at which the output is within [P-EF-030] of the size of the change from the new clipped command
  is at most [P-EF-010], and the output stays within that band at each later sample while the
  command is held.
Parameters:    P-EF-030, P-EF-010, P-EF-020, P-EF-120, P-EF-130, P-SYS-310, P-SYS-480, P-SYS-300,
  P-FC-010
TBD/TBR:       P-EF-010 value TBR (TT-080), P-EF-020, P-EF-030, P-EF-120, P-EF-130 values TBR
  (TT-930), P-SYS-300, P-SYS-310, P-SYS-480 values TBR (TT-070), P-FC-010 value TBR (TT-050),
  Martin, G2 (I1); command response model (DD-160, C3-Q01), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-400

```req
ID:            L2-AER-EF-400
Level:         L2
Type:          Interface
Statement:     The effector subsystem shall take from the flight software only the effector commands,
  made of one effector command for each effector and the effector activation state, as the
  vehicle-model boundary ICD defines them.
Rationale:     A fixed vehicle-model boundary lets the control law and the autoflight be replaced
  without modifying the vehicle model (L0-CON-200, -210). EF's share of the boundary is the
  effector commands in. An effector command is a force in N along the effector's direction of
  action; the effector activation state is on or off (DD-180). EF gives the flight software
  nothing: the effector outputs go to the operational data output, which observes the boundary
  without being a party to it (L2-AER-EF-410), and the fuel availability is internal to the
  vehicle model. The home of the boundary ICD is open (IN-B1-01, TT-720).
  Sufficiency (L1-AER-430): EF's only boundary input is of the listed kind "effector commands",
  and EF has no boundary output, so EF's share of L1-AER-430 is covered.
Parent(s):     L1-AER-430
Source:        FUNCTIONAL_ANALYSIS §3.2 I-12, §5.1; D55
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-400; success criteria: each EF data item crossing the
  vehicle-model boundary is an effector command or the effector activation state, defined in the
  vehicle-model boundary ICD with its unit, and no flight software function reads an EF output.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-410

```req
ID:            L2-AER-EF-410
Level:         L2
Type:          Interface
Statement:     The effector subsystem shall give the operational data output the effector output of
  each effector at each simulation step, as ICD-AER-TST defines the signal.
Rationale:     Control activity is one of the things the operational data relate in time
  (L0-OBJ-140, L1-AER-630). The effector outputs are EF's item of the closed list; the axis
  references, axis demands and effector commands are FC's and the fuel mass flow is FU's. TM
  samples them at each output sample [P-TM-010]. Whether they are released to the RVS is decided
  with the RVS (#69).
  Sufficiency (L1-AER-630): the effector outputs are EF's item of the closed list; TM records them.
Parent(s):     L1-AER-630
Source:        N-250, N-340; TESTING_ENVIRONMENT.md §8
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-410; success criteria: each output sample of the reference mission
  (SC-110) holds the ICD-AER-TST effector output signal of each effector, in N, equal to the EF
  output of its simulation step.
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (TT-070), Martin, G2 (I1); releasable or protected classification
  (#69, TT-600), Martin, closes when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-420

```req
ID:            L2-AER-EF-420
Level:         L2
Type:          Constraint
Statement:     The effector subsystem shall compute each of its outputs of a simulation step only from
  the vehicle parameter set, the effector commands and the fuel availability of that step and of
  the preceding steps of the run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59). EF adds no
  variation if its outputs depend on nothing but the run's own inputs: no wall-clock time, no
  random source and no state carried over from another run or another simulation instance. The
  lag carries state from step to step within the run only, and starts from zero in each run.
  Bit-identical results are not required (D25, D59); the tolerances are those of each success
  criterion (D63 Q4).
  Sufficiency (L1-AER-690): EF's outputs are part of the operational data and inputs of DYN and
  FU; this record makes them a function of the run's inputs, so a repeated run gives the same EF
  outputs and verdicts, which is EF's share.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-EF-420; success criteria: two executions of the reference mission (SC-110),
  and of the scripted runs of TP-EF-110 and TP-EF-340, with the same configuration, initial
  condition, selection or command script and TST step and wind inputs, in two simulation
  instances, give the same verdict on each success criterion of TP-EF-110, -200, -340 and -410.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-EF-430

```req
ID:            L2-AER-EF-430
Level:         L2
Type:          Documentation
Statement:     The effector subsystem shall have its effector model stated in MS-DYN, with the
  direction of action, the control effectiveness, the output limits and the command response of
  each effector, the response to the fuel availability and to the effector activation state, and
  the computation of the control force and the control moment.
Rationale:     L1-AER-720 lists the effector model in the closed content of MS-DYN. C1 owns the
  document and left the effector model slot to C3 (MS-DYN effector and fuel models, IN-C1-11); C3
  supplies the content (`work/C3/ms_dyn_s7_effectors.md`), merged at I1. The list is closed.
  Sufficiency (L1-AER-720): this record gives MS-DYN its effector model section; the DYN and FU
  children give the other sections.
Parent(s):     L1-AER-720
Source:        N-270; plan §6 C1, C3; IN-C1-11
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-EF-430; success criteria: MS-DYN, at its G2 baseline, has an effector
  model section with each listed item, and each EF model-fidelity requirement (L2-AER-EF-100,
  -120) cites it.
Parameters:    —
TBD/TBR:       MS-DYN effector model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```
