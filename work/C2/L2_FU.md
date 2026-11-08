## FU — Fuel and mass properties

The fuel and mass-properties requirements (task C2; reworked for the G2 findings and the landing gear, D69, D72, D73: `work/C2/rework_G2_D69.md`). The subject of each statement is the FU subsystem, the fuel and mass-properties subsystem of the Aeronef, one of the three subsystems of the vehicle model, with the dynamics model (DYN) and the effector subsystem (EF), behind the vehicle-model boundary (D55, L1-AER-430). FU runs at each simulation step `[P-SYS-300]`. Its inputs are the fuel mass of the initial condition, the vehicle parameter set and the control force and control moment that EF computes from its effector outputs at each step (DD-190). Its outputs are the fuel mass flow, the remaining fuel mass, the mass properties (vehicle mass, centre-of-gravity position, inertia tensor), the fuel availability for the effectors and the dynamics model, and the fuel state. FU takes nothing from the landing gear: the gear has no mass and moves no mass property (L1-AER-900).

**What FU decides.** The consumption relationships are linear in the magnitude of the resultant control force and of the resultant control moment (DD-110, owner D65), so the fuel mass flow is zero whenever the effectors produce nothing: on the ground with the effectors off (L1-AER-930, -940), and after fuel exhaustion. The inertia tensor changes with the fuel: it runs linearly from the dry-mass tensor at fuel exhaustion to its full-capacity value, because the fuel depletes uniformly over a fixed volume centred on the centre of gravity (DD-120, D65), taken equal to the body shape (DD-280). In the exhaustion step the flow is limited to the fuel left, and the remaining fuel mass is set to zero at the end of the step (DD-130, revised by DD-270). The equations go in the MS-DYN mass-properties model and fuel model, which C1 merges; `work/C2/ms_dyn_s6_s7_fu.md` gives the text.

**Exhaustion is nominal.** Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070). FU then gives the dry-mass properties, zero fuel mass flow, a fuel availability of not available and the exhaustion indication, and it keeps doing so to the end of the run. In flight, the vehicle then falls, and its ground contact is a crash (D68, L1-AER-270); DYN classifies the contact with the fuel availability that FU gives it. A run that starts on the ground with no fuel stays on the ground.

**Ground operations (D69).** Runs start on the ground, at rest on the extended landing gear with the effectors off (L1-AER-950), and take their fuel mass from the initial condition as before. A run no longer ends at the first ground contact: a landing is followed by a rest on the ground with a constant remaining fuel mass, and the run ends at a crash or at the TST's end condition. The hover endurance now counts from a takeoff at full fuel (L1-AER-360 v2), and the fuel of the takeoff lies inside the margin `[P-FU-100]` (L2-AER-FU-290).

**Verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would describe the implementation (D4), so each record is verified directly by its own method. The L1 parents are verified by roll-up (D40, D58). Several tests read FU outputs that the operational data do not carry (the centre of gravity, the inertia tensor, the fuel availability) or need each simulation step; they read them at the vehicle-model boundary or at the interfaces of MS-DYN, recorded by the TST for the test run (IN-C2-30). The `Parameters` field of each record lists the parameters that its statement and its success criteria use, and the `TBD/TBR` field lists the open ones among them (G2-F20).

### L2-AER-FU-010

```req
ID:            L2-AER-FU-010
Level:         L2
Type:          Constraint
Statement:     When a run starts, the FU subsystem shall take [P-FU-010], [P-FU-020], [P-FU-030],
  [P-FU-040], [P-FU-050], [P-FU-070] and [P-FU-080] from the vehicle parameter set of the run's
  configuration.
Rationale:     The fuel capacity, the low-fuel fraction, the dry mass, the consumption parameters
  and the two inertia tensors are configurable values (N-020, L0-CON-120), so a campaign can vary
  them without a software change. FU holds them constant for the whole run. The identity and
  version of the parameter set are output by TM (L1-AER-650), so each result names the values
  that produced it. The two inertia tensors are derived values: a campaign that changes the dry
  mass, the capacity or the body dimensions must re-derive them, and FU rejects a parameter set
  in which they do not match (L2-AER-FU-330, G2-F17).
  Sufficiency (L1-AER-170): this record takes the translational and rotational consumption
  parameters from the parameter database at the start of each run, which is the whole of
  L1-AER-170; L2-AER-FU-040 then uses them in the fuel mass flow.
  Sufficiency (L1-AER-150): with L2-AER-FU-020 (the run starts with the fuel of its initial
  condition) and L2-AER-FU-030 (that fuel is at most the capacity), this record makes the
  capacity a parameter of the run, so L1-AER-150 is covered.
Parent(s):     L1-AER-170, L1-AER-150
Source:        N-020, N-280; CONOPS §4.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-FU-010; success criteria: two runs from the same initial
  condition and selection script, with two vehicle parameter sets that differ in [P-FU-040] and
  [P-FU-050] and with no software change, each give at each output sample a fuel mass flow that
  agrees within the relative tolerance [P-FU-090] with the independent computation of
  AN-FU-040 using that run's values, and each run outputs the identity of the parameter set it
  used.
Parameters:    P-FU-010, P-FU-020, P-FU-030, P-FU-040, P-FU-050, P-FU-070, P-FU-080, P-FU-090
TBD/TBR:       P-FU-010 value TBR (TT-120), P-FU-030, P-FU-040, P-FU-050 values TBR (TT-110),
  Martin, G2 (I1); P-FU-020 value TBR (TT-130), Martin, G2; P-FU-070, P-FU-080 values TBR
  (TT-770), Martin, G2 (I1); P-FU-090 value TBR (TT-790), Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-020

```req
ID:            L2-AER-FU-020
Level:         L2
Type:          Functional
Statement:     When a run starts, the FU subsystem shall set the remaining fuel mass to the fuel
  mass of the initial condition.
Rationale:     The fuel at the start of a run is part of its initial condition, so a test procedure
  can start at any fuel state (N-310, L1-AER-660). This is the owner's reading of L0-CON-100: the
  capacity [P-FU-010] is the parameter, and the initial fuel is set per run (D63 Q3). A run starts
  on the ground, at rest on the extended landing gear with the effectors off (D69, L1-AER-950);
  a test run or a credibility check may start airborne (D73 B3-1). FU takes the fuel mass the same
  way in both cases, because the fuel does not depend on where the run starts. The reference
  mission starts on the ground at [P-FU-010] (SC-110). The value applies at simulation time zero
  (CV-810), before any fuel is consumed, so the first output sample reports it unchanged; on the
  ground the effectors are off, so nothing is consumed until a takeoff (L2-AER-FU-300). A run that
  starts with no fuel stays on the ground (SC-130 zero-fuel variation; L2-AER-FU-200).
  Sufficiency (L1-AER-150): see L2-AER-FU-010.
  Sufficiency (L1-AER-660): the fuel mass is the FU item of the initial condition; DYN, AF and
  FCP take the other items, the landing gear position included (L1-AER-660 v2). With
  L2-AER-FU-030 (the range check), this record makes FU start from the fuel mass it is given,
  which is FU's share of L1-AER-660.
Parent(s):     L1-AER-150, L1-AER-660
Source:        N-310; CONOPS §4.6, SC-110, SC-130, SC-200; D63, D69, D73
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-020; success criteria: for runs started on the ground with an initial
  fuel mass of zero, of one half of [P-FU-010] and of [P-FU-010], and for one run started airborne
  with an initial fuel mass of [P-FU-010], the remaining fuel mass at the first output sample
  equals the initial fuel mass within [P-FU-060].
Parameters:    P-FU-010, P-FU-060
TBD/TBR:       P-FU-010 value TBR (TT-120), P-FU-060 value TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-030

```req
ID:            L2-AER-FU-030
Level:         L2
Type:          Functional
Statement:     If the fuel mass of the initial condition is outside the range from zero to
  [P-FU-010], then the FU subsystem shall reject the initial condition with an initial-condition
  error to the TST.
Rationale:     L1-AER-150 bounds the initial fuel by the capacity. A negative fuel mass, or more
  fuel than the vehicle holds, has no physical meaning: it would give a vehicle mass below the
  dry mass or above the maximum vehicle mass that the authority budgets assume (L1-AER-120 to
  -140). Rejecting the initial condition, rather than clamping the value, keeps the run what the
  test procedure asked for, so a run cannot pass against a fuel state it did not have (D59). The
  check is the same for a ground start and an airborne start (D69, D73 B3-1). The error item is
  defined in ICD-AER-TST (IN-C2-31); the TST decides what to do with the run, so whether output
  samples follow is a TST and ICD-AER-TST matter, not an FU one (G2-F11). This is checking the run
  set-up, not failure handling (tailoring note). Zero and [P-FU-010] are valid. Rejection chosen
  by the owner (D65, DD-140).
  Sufficiency (L1-AER-150): see L2-AER-FU-010.
  Sufficiency (L1-AER-660): see L2-AER-FU-020.
Parent(s):     L1-AER-150, L1-AER-660
Source:        N-310; CONOPS §4.6; DD-140
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-030; success criteria: ground initial conditions with a fuel mass of
  zero and of [P-FU-010] give no initial-condition error and FU outputs from the first simulation
  step; ground initial conditions with a fuel mass of 1.01 times [P-FU-010] and of minus 0.01
  times [P-FU-010] each give one initial-condition error that names the fuel mass and its value,
  and FU produces no output for that run.
Parameters:    P-FU-010
TBD/TBR:       P-FU-010 value TBR (TT-120), Martin, G2 (I1); initial-condition error item in
  ICD-AER-TST (IN-C2-31, TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-040

```req
ID:            L2-AER-FU-040
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the consumption rate of each simulation step as the
  sum of a translational term from the control force and a rotational term from the control
  moment that the effector subsystem gives for that step, with the consumption relationships and
  the parameters [P-FU-040] and [P-FU-050] that MS-DYN defines.
Rationale:     Fuel is consumed to produce the control forces and control moments, with separate
  terms for translation and rotation (L0-CON-120; AIRCRAFT_CHARACTERISTICS §4). The form of each
  relationship is a C2 decision recorded in the MS-DYN fuel model (L1-AER-160). Under DD-110
  (accepted, D65) the translational term is [P-FU-040] times the magnitude of the resultant control
  force, and the rotational term is [P-FU-050] times the magnitude of the resultant control moment
  about the centre of gravity. EF computes the resultant once per step and gives the same value to
  DYN and to FU (DD-190, L2-AER-FU-070), so the fuel used and the motion come from one control
  force and moment. Both terms are linear, so the hover endurance has the closed form of
  FUNCTIONAL_ANALYSIS §7.3 (L2-AER-FU-290). Both are zero when the control force and moment are
  zero, so no fuel is used with the effectors off on the ground, in free fall or in torque-free
  rotation (L1-AER-940, L2-AER-FU-300), which also keeps the MS-DYN credibility checks exact
  (N-290); D69 therefore needs no new consumption term. Both are at least zero for non-negative
  parameters, so the remaining fuel never increases (L2-AER-FU-100). Using the resultant keeps the
  consumption independent of the effector layout, which stays an EF design decision. The effectors
  counter gravity, so fuel is consumed in each airborne condition, hover included (CONOPS §4.5,
  L1-AER-160 v2). The consumption rate is the fuel mass flow except in the exhaustion step
  (L2-AER-FU-050).
  Sufficiency (L1-AER-160): with L2-AER-FU-050 (the flow, limited in the exhaustion step) and
  L2-AER-FU-070 (the control force and moment as input), this record computes the fuel mass flow
  from the control forces and control moments of the effectors through the two relationships of
  MS-DYN, and it makes the fuel used depend on the effector output (L0-CON-100).
  Sufficiency (L1-AER-940): see L2-AER-FU-300; this record gives the relationships whose value at
  zero control force and moment is zero, which the AN-FU-040 criteria check.
Parent(s):     L1-AER-160, L1-AER-940
Source:        N-280; AIRCRAFT_CHARACTERISTICS.md §4; CONOPS §4.5; DD-110; DD-190
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-040; success criteria: in the reference mission (SC-110), in a run
  with translational effector output only and in a run with rotational effector output only, at
  each simulation step that is not an exhaustion step, with the FU inputs and outputs recorded at
  each simulation step (IN-C2-30), the fuel mass flow agrees within the relative tolerance
  [P-FU-090] with an independent computation of the MS-DYN relationships from the recorded control
  force and control moment and the run's [P-FU-040] and [P-FU-050]; at each simulation step with
  zero control force and zero control moment the fuel mass flow is zero.
Parameters:    P-FU-040, P-FU-050, P-FU-090
TBD/TBR:       P-FU-040, P-FU-050 values TBR (TT-110), Martin, G2 (I1); P-FU-090 value TBR
  (TT-790), Martin, G2; MS-DYN fuel model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-050

```req
ID:            L2-AER-FU-050
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the fuel mass flow of each simulation step as the
  consumption rate of that step, or, in an exhaustion step, as the remaining fuel mass at the start
  of that step divided by [P-SYS-300].
Rationale:     The effectors produce their output during a step whose remaining fuel mass is above
  zero at its start (L2-AER-FU-200), so in the step that ends at fuel exhaustion the consumption
  rate can ask for more fuel than is left. That step is the exhaustion step (glossary proposal): a
  step that starts with fuel and whose consumption rate times [P-SYS-300] is at least the
  remaining fuel mass at its start. Limiting the flow to what is left there keeps the fuel
  accounting within [P-FU-060] (L2-AER-FU-080), and L2-AER-FU-340 then sets the remaining fuel
  mass to exactly zero at the end of the step, so exactness does not depend on floating-point
  rounding (G2-F10) and the remaining fuel stays at or above zero (L2-AER-FU-090). The exhaustion
  step is identified by comparing the fuel the step would use with the fuel left, the same product
  that the accounting subtracts in every other step, so no other step can end below zero
  (MS-DYN fuel model, DD-270). The control force and moment are one value per simulation step
  (glossary *Effector output*, DD-190), so the fuel consumed in a step is the flow times
  [P-SYS-300] exactly (DD-130, IN-C2-12).
  Sufficiency (L1-AER-160): see L2-AER-FU-040.
  Sufficiency (L1-AER-190): with L2-AER-FU-080 (the accounting), L2-AER-FU-090 (at or above zero)
  and L2-AER-FU-340 (zero at the end of the exhaustion step), this record keeps the remaining fuel
  mass equal to the initial fuel mass minus the integral of the reported flow, including the
  exhaustion step, which is the check of L1-AER-190.
Parent(s):     L1-AER-160, L1-AER-190
Source:        METHODOLOGY §10.3; CONOPS SC-110; DD-130; G2-F10
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-050; success criteria: in the reference mission (SC-110), with the
  FU outputs recorded at each simulation step (IN-C2-30), exactly one simulation step is an
  exhaustion step; its fuel mass flow equals the remaining fuel mass at its start divided by
  [P-SYS-300] within the relative tolerance [P-FU-090]; and the fuel mass flow of each other step
  equals the consumption rate of AN-FU-040 within [P-FU-090].
Parameters:    P-SYS-300, P-FU-090
TBD/TBR:       P-SYS-300 value TBR (TT-070), Martin, G2 (I1); P-FU-090 value TBR (TT-790), Martin,
  G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-060

```req
ID:            L2-AER-FU-060
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall define the fuel consumption of the effectors only through the
  translational consumption parameters [P-FU-040] and the rotational consumption parameters
  [P-FU-050].
Rationale:     L1-AER-100 closes the list of the kinds of parameter that define an effector; the
  fifth kind, fuel consumption, belongs to FU (L1-AER-100 rationale). A further consumption term,
  for example an idle flow or a per-effector efficiency outside these two sets, would add a sixth
  kind; an idle flow would also break the zero flow with the effectors off that L1-AER-940
  requires (D69). Under the owner's choice (D65, DD-110) each set is one coefficient, common to the
  effector set. The step duration that limits the flow in the exhaustion step (L2-AER-FU-050) is
  the time base, not a consumption parameter.
  Sufficiency (L1-AER-100): the EF children define the direction of action, the control
  effectiveness, the output limits and the command response; this record makes the two
  consumption sets the only parameters of the fifth kind, so the EF and FU children together are
  the closed list of L1-AER-100.
  Sufficiency (L1-AER-940): see L2-AER-FU-300; this record excludes any consumption parameter
  that could give a flow at zero control force and moment.
Parent(s):     L1-AER-100, L1-AER-940
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §4, §7; D69
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-060; success criteria: the MS-DYN consumption relationships use
  no parameter other than [P-FU-040] and [P-FU-050], and the parameter database holds no FU or EF
  parameter that enters a consumption relationship other than these two.
Parameters:    P-FU-040, P-FU-050
TBD/TBR:       P-FU-040, P-FU-050 values TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-070

```req
ID:            L2-AER-FU-070
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall take, at each simulation step, the control force and the
  control moment that the effector subsystem computes from its effector outputs for that step,
  through the interface that MS-DYN defines between the two subsystems.
Rationale:     Interface I-01 (FUNCTIONAL_ANALYSIS §3.2) is internal to the vehicle model, so it is
  defined in MS-DYN, not in an ICD. EF sums its effector outputs, once per step, into the resultant
  control force and the resultant control moment about the centre of gravity, through its control
  effectiveness, and gives the same values to DYN and to FU (DD-190, L2-AER-EF-140; answers
  IN-C2-11 and IN-C3-10). FU therefore makes no second computation from the effector outputs, and
  the fuel used and the motion come from one control force and moment. FU uses no per-effector
  output: the consumption is charged on the resultant (DD-110), which keeps FU independent of the
  effector layout. The values are held over the step (DD-100), so the fuel used in the step is the
  flow times the step exactly (IN-C2-12).
  Sufficiency (L1-AER-160): see L2-AER-FU-040; this record supplies the control force and control
  moment that the computation needs.
Parent(s):     L1-AER-160
Source:        FUNCTIONAL_ANALYSIS §3.2 I-01; DD-190; IN-C3-10
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-070; success criteria: MS-DYN defines the interface from EF to
  FU with the control force and control moment of each simulation step, computed once by EF and
  equal to those it gives the dynamics model; the MS-DYN consumption relationships use them; no
  FU requirement takes a control force or moment from another source or computes one from the
  effector outputs.
Parameters:    —
TBD/TBR:       MS-DYN effector and fuel model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-080

```req
ID:            L2-AER-FU-080
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall keep the remaining fuel mass of each simulation step within
  [P-FU-060] of the initial fuel mass minus the sum, over the preceding simulation steps, of the
  fuel mass flow times [P-SYS-300].
Rationale:     The fuel-mass integral is one of the independent credibility checks of METHODOLOGY
  §10.3 (MS-DYN check C-8). The flow is constant over each step (L2-AER-FU-050), so the time
  integral of the flow is this sum, and the tolerance covers the arithmetic only. The check uses
  the flow of each simulation step; an integration of the output samples would add a sampling
  error that the tolerance is not meant to cover; the owner chose per-step data (D65, G2-F22).
  With the landing gear a run no longer ends at the first ground contact (D69): the reference
  mission includes a rest on the ground (SC-110 leg 7a), where the summed flow is zero, and it
  ends at the crash after fuel exhaustion (D68). Setting the remaining fuel to zero at the end of
  the exhaustion step (L2-AER-FU-340) differs from the sum by rounding only, well inside
  [P-FU-060].
  Sufficiency (L1-AER-190): see L2-AER-FU-050.
Parent(s):     L1-AER-190
Source:        METHODOLOGY §10.3; N-290; D65, D68, D69
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-080; success criteria: over the reference mission (SC-110), from a
  ground start at [P-FU-010] to the end of the run at the crash after fuel exhaustion, with the FU
  outputs recorded at each simulation step (IN-C2-30), an independent summation of the fuel mass
  flow of each step times [P-SYS-300], subtracted from the initial fuel mass, agrees with the
  remaining fuel mass of each step within [P-FU-060].
Parameters:    P-FU-060, P-SYS-300, P-FU-010
TBD/TBR:       P-FU-060 value TBR (TT-110), P-SYS-300 value TBR (TT-070), P-FU-010 value TBR
  (TT-120), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-090

```req
ID:            L2-AER-FU-090
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall keep the remaining fuel mass of each simulation step no less
  than zero.
Rationale:     A negative fuel mass has no physical meaning and would give a vehicle mass below the
  dry mass. The fuel used in the exhaustion step is limited to the fuel left (L2-AER-FU-050), and
  the remaining fuel mass is set to zero at its end (L2-AER-FU-340), so the fuel reaches exactly
  zero at exhaustion whatever the rounding (G2-F10). It then stays at zero: the effectors produce
  no output (L2-AER-FU-200, L1-AER-200), so the consumption rate is zero (L2-AER-FU-040, -300). A
  run started with zero fuel is a run that stays on the ground (D69, SC-130 zero-fuel variation):
  its remaining fuel mass is zero from the first step.
  Sufficiency (L1-AER-190): see L2-AER-FU-050.
  Sufficiency (L1-AER-180): with L2-AER-FU-110 (vehicle mass), this record keeps the vehicle mass
  at or above the dry mass, so the mass decreases only by fuel that was on board.
Parent(s):     L1-AER-190, L1-AER-180
Source:        CONOPS §4.5, SC-110, SC-130; G2-F10
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-090; success criteria: in the reference mission (SC-110) and in a run
  started on the ground with zero fuel, the remaining fuel mass is at or above zero at each
  simulation step (IN-C2-30), and it is exactly zero at each step from the end of the exhaustion
  step, or from the first step of the zero-fuel run, to the end of the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-100

```req
ID:            L2-AER-FU-100
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall keep the remaining fuel mass of each simulation step no
  greater than the remaining fuel mass of the previous simulation step.
Rationale:     Fuel is only consumed during a run; nothing refuels the Aeronef, on the ground
  included (CONOPS §4.5; SC-110: the fuel quantity never increases; it decreases in every airborne
  leg and is constant during the rest on the ground). The consumption rate is at least zero
  because the consumption parameters are at least zero (L2-AER-FU-040; the ranges are in the
  PARAMETERS.yaml notes of [P-FU-040] and [P-FU-050]).
  Sufficiency (L1-AER-180): with L2-AER-FU-110 (the vehicle mass is the dry mass plus the
  remaining fuel), L2-AER-FU-080 (the remaining fuel is the initial fuel minus the fuel consumed)
  and L2-AER-FU-120 (the mass goes to DYN), this record makes the vehicle mass decrease by the
  fuel consumed and never increase, which is L0-CON-110 as L1-AER-180 states it.
Parent(s):     L1-AER-180
Source:        N-280; CONOPS §4.5, SC-110
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-100; success criteria: in the reference mission (SC-110), the
  remaining fuel mass at each output sample is at or below its value at the previous output
  sample.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-110

```req
ID:            L2-AER-FU-110
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the vehicle mass of each simulation step as [P-FU-030]
  plus the remaining fuel mass of that step.
Rationale:     Fuel consumption decreases the vehicle mass (L0-CON-110, CV-340). The mass loss is a
  real effect on the dynamics: consumed fuel leaves the vehicle with no force or moment
  (L0-ASM-090), so the same control force gives a larger acceleration. At fuel exhaustion the
  vehicle mass is the dry mass. The maximum vehicle mass is [P-FU-030] plus [P-FU-010]
  (glossary), the value the authority budgets use (L1-AER-120, -130). The landing gear adds no
  mass (L1-AER-900, L2-AER-FU-310).
  Sufficiency (L1-AER-180): see L2-AER-FU-100.
Parent(s):     L1-AER-180
Source:        N-280; CV-340; L0-ASM-090
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-110; success criteria: at each output sample of the reference
  mission (SC-110), including the rest on the ground and the samples from fuel exhaustion to the
  crash, the recorded vehicle mass equals [P-FU-030] plus the recorded remaining fuel mass within
  [P-FU-060].
Parameters:    P-FU-030, P-FU-060
TBD/TBR:       P-FU-030, P-FU-060 values TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-120

```req
ID:            L2-AER-FU-120
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the dynamics model, at each simulation step, the
  vehicle mass and the inertia tensor of that step through the interface that MS-DYN defines
  between the two subsystems.
Rationale:     Interface I-04 is internal to the vehicle model. The equations of motion of a step
  use the mass properties of that step: the vehicle mass in the translational equations and in
  the sensed acceleration, and the inertia tensor in the rotational equations (MS-DYN, IN-C2-14).
  The inertia tensor is given as its three principal moments about the centre of gravity in the
  body axes, with zero products of inertia (L2-AER-FU-180), which are the "principal moments of
  inertia" that DYN takes (L2-AER-DYN-040, -210; IN-C2-19). The centre-of-gravity position does
  not cross I-04: it is the body-frame origin at each fuel state (L2-AER-FU-150, L2-AER-DYN-200),
  so DYN needs no value, and FU gives it as a mass-properties item at the vehicle-model boundary
  only (L2-AER-FU-130; G2-F05, FUNCTIONAL_ANALYSIS I-04 as aligned by CR-B3-39). The equations
  carry no thrust term and no rate-of-change-of-inertia term, because consumed fuel leaves with no
  force or moment (L0-ASM-090). The fuel availability that DYN uses to classify a ground contact
  crosses interface I-03 (L2-AER-FU-320).
  Sufficiency (L1-AER-180): see L2-AER-FU-100; this record delivers the vehicle mass to DYN, the
  other subsystem of L1-AER-180.
  Sufficiency (L1-AER-220): see L2-AER-FU-170.
Parent(s):     L1-AER-180, L1-AER-220
Source:        FUNCTIONAL_ANALYSIS §3.2 I-04; CV-340, CV-350; G2-F05
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-120; success criteria: MS-DYN defines the interface from FU to
  DYN with the vehicle mass and the inertia tensor as three principal moments, with their units
  and frame (CV-340, CV-350), and with no centre-of-gravity item; and it states that the equations
  of motion of a step use the mass properties of that step.
Parameters:    —
TBD/TBR:       MS-DYN mass-properties model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-130

```req
ID:            L2-AER-FU-130
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the flight software only the mass properties and the fuel
  state of each simulation step, as the vehicle-model boundary ICD defines them.
Rationale:     A fixed vehicle-model boundary lets the control law and the autoflight be replaced
  without modifying the vehicle model (L0-CON-200, -210). FU's share of the boundary is the mass
  properties (vehicle mass, centre-of-gravity position, inertia tensor; glossary) for flight
  control (I-05), and the fuel state for autoflight and the flight control panel (I-06). The
  flight software reads them at the first simulation step of each control frame, as it reads the
  vehicle state (L1-AER-440). FU takes no input from the flight software: neither the effector
  commands nor the landing gear command (L1-AER-430 v2) reaches FU. The gear state is DYN's
  output, not FU's. The fuel mass flow goes to the operational data, which observes the boundary
  without being a party to it (L2-AER-FU-250). The home of the boundary ICD is open (IN-B1-01,
  TT-720).
  Sufficiency (L1-AER-430): FU's outputs across the boundary are two of the listed kinds, and FU
  takes none of the listed inputs, so FU's share of L1-AER-430 is covered.
Parent(s):     L1-AER-430
Source:        FUNCTIONAL_ANALYSIS §3.2 I-05, I-06, §5.1; D55, D69
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-130; success criteria: each FU data item crossing the
  vehicle-model boundary is a mass-properties item or a fuel-state item defined in the
  vehicle-model boundary ICD with its unit and frame, and no FU requirement takes an input from
  the flight software.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-140

```req
ID:            L2-AER-FU-140
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the flight software the same vehicle mass as it gives the
  dynamics model for the same simulation step.
Rationale:     Flight control holds the sensed acceleration within the crew limit by limiting the
  resultant control force at the current mass (D38, L1-AER-290), and DYN computes the sensed
  acceleration with the mass it receives. Both must use one value, or the limit would be set
  against a mass the vehicle does not have. Within a control frame the mass falls by the fuel
  used in that frame; flight control reads the mass at the frame start, so it covers that fall
  in its share of the budget margin. The relative fall over one frame is at most about 1e-5 for
  the largest output of the reference effector layout at dry mass (IN-C2-41, corrected for
  G2-F24), negligible against the limit.
  Sufficiency (L1-AER-290): FC owns the limit, AF keeps its manoeuvres within the vehicle
  acceleration limit and DYN computes the sensed acceleration (L1-AER-290 rationale); FU supplies
  the mass to both sides, and this record makes it one mass, which is FU's share.
Parent(s):     L1-AER-290
Source:        D38, D45; N-170
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-140; success criteria: in the reference mission (SC-110), at the first
  simulation step of each control frame, the vehicle mass across the vehicle-model boundary
  equals the vehicle mass given to the dynamics model for that step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-150

```req
ID:            L2-AER-FU-150
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall give the centre-of-gravity position as the body-frame origin
  at each fuel state.
Rationale:     The centre of gravity is fixed, including while fuel is consumed and while the
  landing gear moves (L0-CON-130, L1-AER-210, L1-AER-900), and it is the body-frame origin
  (CV-160), so the effector moment arms stay constant. FU gives it, zero in each body axis, as a
  mass-properties item at the vehicle-model boundary (L2-AER-FU-130), so that FC reads it rather
  than assumes it, and so that there is one place to change if a later version lets it move
  (CV-160). It does not cross the FU-to-DYN interface: DYN uses the origin as the centre of
  gravity by definition (L2-AER-DYN-200; G2-F05). The dry-mass and fuel-mass distributions are
  centred on it (L2-AER-FU-160), so the output is also the physical centre of gravity.
  Sufficiency (L1-AER-210): FU defines the mass distribution and DYN uses the centre of gravity
  as origin (L1-AER-210 rationale). With L2-AER-FU-160 (both distributions centred on the origin)
  and L2-AER-FU-310 (no effect of the gear), this record keeps the centre of gravity at one
  body-frame position for each fuel mass, and L2-AER-DYN-200 makes it the origin of the motion.
Parent(s):     L1-AER-210
Source:        AIRCRAFT_CHARACTERISTICS.md §4; CV-160; G2-F05
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-150; success criteria: the MS-DYN mass-properties model states
  the centre of gravity at the body-frame origin with no dependence on the remaining fuel mass,
  and the vehicle-model boundary ICD defines the centre-of-gravity item as the body-frame origin.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD (TT-680, TT-720), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-160

```req
ID:            L2-AER-FU-160
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall use a dry-mass distribution and a fuel-mass distribution that
  each have the body-frame origin as centre of mass at each fuel state.
Rationale:     The centre of gravity stays fixed while fuel is consumed only if neither part moves it
  (L0-CON-130). The fuel does not slosh (L0-ASM-080). Under DD-120 (accepted, D65) the fuel
  depletes uniformly over a fixed fuel volume centred on the centre of gravity, so the centre of
  mass of the fuel stays at the origin at each fuel mass and its inertia scales with its mass
  (L2-AER-FU-170). C2 proposes that the fuel volume is the body shape itself, and the dry mass a
  uniform solid of the same shape (DD-280): both are then fixed by the body dimensions
  [P-DYN-020] and [P-DYN-030], and no fuel-volume parameter is needed (G2-F16). The MS-DYN
  mass-properties model states both distributions, as C2 writes them (`work/C2/ms_dyn_s6_s7_fu.md`).
  The landing gear has no mass (L1-AER-900), so it is in neither distribution.
  Sufficiency (L1-AER-210): see L2-AER-FU-150.
Parent(s):     L1-AER-210
Source:        AIRCRAFT_CHARACTERISTICS.md §4; L0-ASM-080; DD-120
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-160; success criteria: the MS-DYN mass-properties model states
  the dry-mass and the fuel-mass distributions, and the first moment of each about the body-frame
  origin is zero for each remaining fuel mass from zero to [P-FU-010].
Parameters:    P-FU-010
TBD/TBR:       P-FU-010 value TBR (TT-120), Martin, G2 (I1); MS-DYN mass-properties model content
  (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-170

```req
ID:            L2-AER-FU-170
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the inertia tensor of each simulation step as the sum
  of [P-FU-070] and the product of [P-FU-080] with the ratio of the remaining fuel mass of that
  step to [P-FU-010].
Rationale:     L1-AER-220 leaves to C2 whether the inertia changes with the fuel state. C2 decided
  that it does, and the owner confirmed it (DD-120, D65). First, the vehicle mass changes with the
  fuel (L1-AER-180), and an inertia that kept its full-fuel value while the fuel burns would
  contradict it. Second, the control laws then meet a varying inertia as well as a varying mass,
  which is what comparing control laws needs (L0-OBJ-020); the vehicle-model boundary carries the
  inertia for that reason (L1-AER-430 rationale). With the fuel depleting uniformly over a fixed
  volume centred on the centre of gravity (L2-AER-FU-160), the fuel's share of the inertia is
  proportional to the remaining fuel mass, so the tensor runs linearly from [P-FU-070] at fuel
  exhaustion to [P-FU-070] plus [P-FU-080] at full capacity. The maximum inertia, used by the
  moment authority budget (L1-AER-140, -350), is the full-capacity value. With the proposed
  distributions (DD-280) the values follow from the body dimensions and the masses (MS-DYN
  mass-properties model; `work/C2/param_proposals.md`). MS-DYN uses the inertia of each step with
  no rate-of-change term, because consumed fuel leaves with no moment (L0-ASM-090, IN-C2-14).
  Sufficiency (L1-AER-220): with L2-AER-FU-180 (diagonal), L2-AER-FU-190 (derived from the shape
  and the distributions), L2-AER-FU-330 (checked for each parameter set) and L2-AER-FU-120 (given
  to DYN), this record states the inertia tensor at each fuel state, derived as MS-DYN states it,
  and answers the fuel-state question that L0-CON-140 leaves open.
Parent(s):     L1-AER-220
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §4; L0-CON-140; D61; DD-120
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-170; success criteria: at each output sample of the reference
  mission (SC-110), the inertia tensor given across the vehicle-model boundary equals [P-FU-070]
  plus [P-FU-080] times the ratio of the recorded remaining fuel mass to [P-FU-010], within the
  relative tolerance [P-FU-090] on each principal moment.
Parameters:    P-FU-070, P-FU-080, P-FU-010, P-FU-090
TBD/TBR:       P-FU-070, P-FU-080 values TBR, derived in the MS-DYN mass-properties model (TT-770),
  Martin, G2 (I1); P-FU-010 value TBR (TT-120), Martin, G2 (I1); P-FU-090 value TBR (TT-790),
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-180

```req
ID:            L2-AER-FU-180
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall give an inertia tensor with zero products of inertia at each
  fuel state.
Rationale:     The body axes are the principal axes of inertia (D61), so a moment about one body
  axis gives no angular acceleration about another (L1-AER-020). [P-FU-070] and [P-FU-080] each
  hold three principal moments and no product of inertia (CV-350 sign convention), and the sum of
  two diagonal tensors is diagonal. Both distributions of MS-DYN are symmetric about the body
  axes (L2-AER-FU-190).
  Sufficiency (L1-AER-020): DYN excludes drag cross-coupling and EF excludes effector
  cross-coupling; this record excludes inertia cross-coupling, the third source that L1-AER-020
  names.
  Sufficiency (L1-AER-220): see L2-AER-FU-170.
Parent(s):     L1-AER-020, L1-AER-220
Source:        D61; CV-350
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-180; success criteria: [P-FU-070] and [P-FU-080] hold three
  principal moments each and no product of inertia; the MS-DYN mass-properties model states zero
  products of inertia, with the CV-350 sign convention, for both distributions; the vehicle-model
  boundary ICD defines the inertia tensor with zero off-diagonal terms.
Parameters:    P-FU-070, P-FU-080
TBD/TBR:       P-FU-070, P-FU-080 values TBR (TT-770), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-190

```req
ID:            L2-AER-FU-190
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall use the values of [P-FU-070] and [P-FU-080] that MS-DYN
  derives from the body shape and the mass distributions it states.
Rationale:     The exterior shape matters only through its mass properties (L0-CON-140). The two
  tensors are derived values, not free ones: set apart from the shape and the distributions, they
  could describe a tensor that no body has, for example one whose principal moments break the
  triangle inequality. The derivation is C2's content of the MS-DYN mass-properties model
  (G2-F16), from the body dimensions [P-DYN-020] and [P-DYN-030] of the MS-DYN vehicle geometry
  and the masses [P-FU-030] and [P-FU-010]. The body shape is provisional (TBR in L0-CON-140), so
  the derived values change with it. This record fixes the database values; L2-AER-FU-330 extends
  the equality to each vehicle parameter set that a run uses (G2-F17).
  Sufficiency (L1-AER-220): see L2-AER-FU-170.
Parent(s):     L1-AER-220
Source:        L0-CON-140; AIRCRAFT_CHARACTERISTICS.md §1, §4; G2-F16
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-190; success criteria: the MS-DYN mass-properties model derives
  each principal moment of [P-FU-070] and [P-FU-080] from [P-DYN-020], [P-DYN-030], [P-FU-030],
  [P-FU-010] and the stated distributions, and the parameter database values equal the derived
  values to the precision stored, with a source that cites MS-DYN.
Parameters:    P-FU-070, P-FU-080, P-FU-030, P-FU-010, P-DYN-020, P-DYN-030
TBD/TBR:       Body shape provisional (L0-CON-140), P-DYN-020, P-DYN-030 values TBR (TT-740),
  Martin, 2026-11-30; P-FU-070, P-FU-080 values TBR (TT-770), Martin, G2 (I1); P-FU-030 value TBR
  (TT-110), P-FU-010 value TBR (TT-120), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-200

```req
ID:            L2-AER-FU-200
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall give the effector subsystem, at each simulation step, a fuel
  availability that is available when the remaining fuel mass of that step is above zero and not
  available when it is zero.
Rationale:     The output of each effector depends on the availability of fuel (L0-CON-100, I-03);
  EF produces zero control force and zero control moment while fuel is not available (the EF
  child of L1-AER-200). Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070): the
  fuel availability is a normal state of the model, with no failure flag and no recovery. Nothing
  refuels the vehicle during a run (L2-AER-FU-100), so a fuel availability of not available
  holds to the end of the run. In flight the vehicle then moves under gravity and drag alone
  (SC-110 leg 11), and its ground contact is a crash (D68); DYN classifies it with the same fuel
  availability (L2-AER-FU-320). A run started on the ground with zero fuel has fuel not available
  from its first step, so a takeoff produces no output and the vehicle stays on the ground
  (SC-130 zero-fuel variation). The remaining fuel mass of a step is its value at the start of the
  step (CV-840), so a step that starts with fuel left still produces output, and the flow limit of
  L2-AER-FU-050 keeps it to the fuel left; the remaining fuel is exactly zero from the end of the
  exhaustion step (L2-AER-FU-340). The interface is internal to the vehicle model and is defined in
  MS-DYN (IN-C2-15).
  Sufficiency (L1-AER-200): EF produces zero output while fuel is not available; this record
  makes fuel not available from the first simulation step at which the remaining fuel mass is
  zero, so the two give zero control force and moment from that step, as L1-AER-200 requires.
Parent(s):     L1-AER-200
Source:        N-150; CONOPS §4.5, SC-110, SC-130; L0-ASM-070; D68
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-200; success criteria: in the reference mission (SC-110) and in a run
  started on the ground with zero fuel in which a takeoff is engaged, with the FU outputs recorded
  at each simulation step (IN-C2-30), the fuel availability is available at each simulation step
  whose remaining fuel mass is above zero, and not available at each step whose remaining fuel
  mass is zero, from the first such step to the end of the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-210

```req
ID:            L2-AER-FU-210
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall include the remaining fuel mass of each simulation step, in
  kilograms, in the fuel state of that step.
Rationale:     The crew needs to see how much fuel is left (N-150, L1-AER-560). FU gives the SI
  value; the flight control panel converts it to pounds by the CV-750 factor and presents it
  (D9, D55, L1-AER-870), so no crew-facing unit crosses the vehicle-model boundary (CV-760).
  Sufficiency (L1-AER-560): FCP indicates the fuel at each output sample; this record gives it
  the remaining fuel mass at each simulation step, so at each output sample, and L2-AER-FU-240
  carries it to the panel. That is FU's share of L1-AER-560.
Parent(s):     L1-AER-560
Source:        N-150; D9; CONOPS §4.3, §4.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-210; success criteria: at each output sample of the reference mission
  (SC-110), the remaining fuel mass in the fuel state, in kg, equals the recorded remaining fuel
  mass within [P-FU-060].
Parameters:    P-FU-060
TBD/TBR:       P-FU-060 value TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-220

```req
ID:            L2-AER-FU-220
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall indicate, in the fuel state of each simulation step, whether
  the remaining fuel mass of that step is below the fraction [P-FU-020] of [P-FU-010].
Rationale:     The crew needs a warning before the fuel runs out (N-150), and running out is the
  crew's to avoid, with the LOW FUEL alert (D68). The threshold is a fraction of the capacity, not
  of the initial fuel (L1-AER-570, CV-720), so a run that starts below it shows the low-fuel
  indication from its first step, on the ground included. FU sets the indication in the step in
  which the fuel first falls below the threshold, so FU's share of the alert latency [P-SYS-470]
  is zero; the flight software reads it at the next control frame and FCP presents it at an
  output sample (FUNCTIONAL_ANALYSIS §7.5). The indication stays set at fuel exhaustion; which
  annunciation the panel shows then, and the alert label, are FCP's (IN-C2-43).
  Sufficiency (L1-AER-570): FCP annunciates the low-fuel alert from the fuel state within its
  share of [P-SYS-470]; this record gives it the condition at the simulation step at which it
  first holds, and L2-AER-FU-240 carries it to the panel, so the alert meets [P-SYS-470].
Parent(s):     L1-AER-570
Source:        N-150; CONOPS §4.5, SC-110; D68
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-220; success criteria: in the reference mission (SC-110), the low-fuel
  indication is clear at each simulation step whose remaining fuel mass is at or above [P-FU-020]
  times [P-FU-010], and set at each step whose remaining fuel mass is below it, including the
  first such step; in a run started on the ground below the threshold, it is set at the first
  step.
Parameters:    P-FU-020, P-FU-010
TBD/TBR:       P-FU-020 value TBR (TT-130), Martin, G2; P-FU-010 value TBR (TT-120), Martin, G2
  (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-230

```req
ID:            L2-AER-FU-230
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall indicate, in the fuel state of each simulation step, whether
  the vehicle is at fuel exhaustion at that step.
Rationale:     The crew needs to know when the fuel has run out (N-150, L1-AER-580). Autoflight
  takes the fuel state too (F-AER-08). D68 answered #59: the effectors stop, the vehicle falls and
  its ground contact is a crash; what the annunciations show after exhaustion is C5's (D68,
  TT-580). FU gives the indication whatever C5 decides (D65), so this record has no open item.
  The remaining fuel mass reaches exactly zero at the end of the exhaustion step (L2-AER-FU-340),
  so the indication is set at the first step with zero fuel, and FU's share of [P-SYS-470] is
  zero. Fuel exhaustion is a nominal state (L0-ASM-070): the indication is not a failure
  annunciation.
  Sufficiency (L1-AER-580): as for L2-AER-FU-220, with the exhaustion condition: FCP annunciates
  it within its share of [P-SYS-470], and L2-AER-FU-240 carries it to the panel.
Parent(s):     L1-AER-580
Source:        N-150; CONOPS §4.5, SC-110; D65, D68
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-230; success criteria: in the reference mission (SC-110) and in a run
  started on the ground with zero fuel, the fuel-exhaustion indication is clear at each
  simulation step with remaining fuel mass above zero, and set from the first step with zero
  remaining fuel mass to the end of the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-240

```req
ID:            L2-AER-FU-240
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the fuel state to the flight control panel through
  ICD-FCP, as the one fuel-state item that the vehicle-model boundary ICD defines.
Rationale:     The flight control panel presents the fuel indication and the two alerts (D55), and
  L1-AER-880 closes the list of what crosses its boundary. The fuel state is defined once, at the
  vehicle-model boundary, and ICD-FCP refers to that definition (L1-AER-880 rationale), so the
  panel and autoflight read the same item. The fuel state is in SI; the crew-facing units stay in
  the panel (CV-760).
  Sufficiency (L1-AER-880): FU gives only the fuel state into the panel and takes nothing from it,
  which is FU's share of the closed list.
  Sufficiency (L1-AER-560, L1-AER-570, L1-AER-580): with L2-AER-FU-210, -220 and -230 (the
  content), this record carries the fuel state to the panel that presents it, which is the FU
  side of each of the three records.
Parent(s):     L1-AER-880, L1-AER-560, L1-AER-570, L1-AER-580
Source:        D55; FUNCTIONAL_ANALYSIS §3.2 I-06, §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-240; success criteria: ICD-FCP lists the fuel state as the only
  FU item crossing the panel boundary, by reference to its vehicle-model boundary definition (the
  remaining fuel mass in kg, the low-fuel indication and the fuel-exhaustion indication), and no
  FU requirement takes an input from the panel.
Parameters:    —
TBD/TBR:       ICD-FCP and the vehicle-model boundary ICD not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-250

```req
ID:            L2-AER-FU-250
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the operational data output the fuel mass flow of each
  simulation step, as ICD-AER-TST defines the signal.
Rationale:     The fuel mass flow is part of the control activity that the operational data relate
  in time (L0-OBJ-140, L1-AER-630), and the input of the fuel-mass integral check. TM samples it
  at each output sample [P-TM-010]. Whether it is released to the RVS is decided with the RVS
  (#69).
  Sufficiency (L1-AER-630): the fuel mass flow is FU's item of the closed list; TM records it.
Parent(s):     L1-AER-630
Source:        N-250, N-340; TESTING_ENVIRONMENT.md §8
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-250; success criteria: each output sample of the reference mission
  (SC-110) holds the ICD-AER-TST fuel mass flow signal, in kg/s, equal to the FU fuel mass flow
  of its simulation step.
Parameters:    —
TBD/TBR:       Releasable or protected classification (#69, TT-600), Martin, closes when the plan
  is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-260

```req
ID:            L2-AER-FU-260
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the operational data output the vehicle mass and the
  remaining fuel mass of each simulation step, as ICD-AER-TST defines the signals.
Rationale:     The vehicle responses include the mass and the fuel (L1-AER-640). The TST needs them
  for the fuel used per leg of the reference mission (N-250), for the crew-limit check
  (L1-AER-290) and for the fuel checks of this section.
  Sufficiency (L1-AER-640): the vehicle mass and the remaining fuel mass are FU's items of the
  closed list; TM records them.
Parent(s):     L1-AER-640
Source:        N-250, N-340, N-390
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-260; success criteria: each output sample of the reference mission
  (SC-110) holds the ICD-AER-TST vehicle mass and remaining fuel mass signals, in kg, equal to
  the FU values of its simulation step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-270

```req
ID:            L2-AER-FU-270
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall compute each of its outputs of a simulation step only from the
  vehicle parameter set, the fuel mass of the initial condition and the control forces and
  control moments that the effector subsystem gives for that step and for the preceding steps of
  the run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59). FU adds no
  variation if its outputs depend on nothing but the run's own inputs: no wall-clock time, no
  random source and no state carried over from another run or another simulation instance. The
  inputs are those of L2-AER-FU-010, -020 and -070; the landing gear position and the vehicle
  state are not among them, so neither the gear nor where the vehicle is changes an FU output
  except through the effector output (L2-AER-FU-310). Bit-identical results are not required (D25,
  D59); the tolerances are those of each success criterion (D63 Q4).
  Sufficiency (L1-AER-690): FU's outputs are part of the operational data and inputs of DYN, EF
  and the flight software; this record makes them a function of the run's inputs, so a repeated
  run gives the same FU outputs and the same FU verdicts, which is FU's share.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-270; success criteria: two executions of the reference mission (SC-110)
  with the same configuration, initial condition, selection script and TST step and wind inputs,
  in two simulation instances, give the same verdict on each success criterion of TP-FU-020 to
  TP-FU-260 and TP-FU-300.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-280

```req
ID:            L2-AER-FU-280
Level:         L2
Type:          Documentation
Statement:     The FU subsystem shall have its consumption relationships, its fuel accounting, its
  fuel availability, its vehicle mass and centre-of-gravity model and its inertia model stated in
  MS-DYN.
Rationale:     L1-AER-720 lists the fuel and mass-properties models in the closed content of
  MS-DYN. C1 writes MS-DYN; C2 supplies the content of its mass-properties model and fuel model
  (`work/C2/ms_dyn_s6_s7_fu.md`), which has one subsection for each of the five listed models, so
  the MS-DYN slots and this record match (G2-F16). The fuel accounting includes the exhaustion
  step (DD-130 as revised by DD-270); the consumption relationships include their zero value at
  zero control force and moment (L1-AER-940). The list is closed.
  Sufficiency (L1-AER-720): this record gives MS-DYN its fuel and mass-properties sections; the
  DYN and EF children give the other sections, the landing gear and ground contact model included
  (L1-AER-720 v2).
Parent(s):     L1-AER-720
Source:        N-270; plan §6 C1, C2; G2-F16
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-280; success criteria: MS-DYN, at its G2 baseline, has a section
  for each of the five listed FU models, and each FU model-fidelity requirement (L2-AER-FU-040,
  -050, -080, -110, -170, -300, -340) names the model it rests on.
Parameters:    —
TBD/TBR:       MS-DYN mass-properties model and fuel model content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       2
```

### L2-AER-FU-290

```req
ID:            L2-AER-FU-290
Level:         L2
Type:          Performance
Statement:     The FU subsystem shall have a fuel capacity [P-FU-010] of at least the product of
  [P-FU-030] with the quantity E minus one, where E is the exponential of the product of
  [P-FU-040], [P-DYN-010], [P-SYS-280] and the sum of one and [P-FU-100].
Rationale:     Fuel budget (FUNCTIONAL_ANALYSIS §7.3, L1-AER-360 v3). In symbols: [P-FU-010] ≥
  [P-FU-030] · (exp([P-FU-040] · [P-DYN-010] · [P-SYS-280] · (1 + [P-FU-100])) − 1). In a hold of
  the hover in still air at level attitude, the control force balances the weight and the control
  moment is zero, so with the DD-110 relationships (L2-AER-FU-040) the fuel mass flow is [P-FU-040]
  times [P-DYN-010] times the vehicle mass, and the mass decays exponentially. From full fuel the
  endurance is then the natural logarithm of the ratio of the maximum vehicle mass to the dry
  mass, divided by [P-FU-040] times [P-DYN-010]; it is at least [P-SYS-280] when the capacity meets
  this record with [P-FU-100] at zero. The margin [P-FU-100] adds the consumption the closed form
  leaves out, as FUNCTIONAL_ANALYSIS §7.3 asks: the regulation of the hold, the moments that hold
  the attitude, and the takeoff.
  Takeoff (D69, L1-AER-360 v3): runs start on the ground, so the endurance counts from the
  engagement of the takeoff at full fuel. Until liftoff the control force is below the weight, so
  the flow is below the hover flow while the time counts. The climb from the gear height
  [P-DYN-040] to the hover height [P-AF-210] at [P-AF-240], with its vertical-speed ramps at
  [P-AF-230], uses more than the hover flow only while it accelerates upward: with the database
  values about 1e-4 kg, the fuel of a few hundredths of a second of hover. The gear retraction
  over [P-DYN-050] is flown at the hover height and is part of the hold. The takeoff therefore lies
  far inside the margin, whose worth is a twentieth of [P-SYS-280] of hover, and the inequality
  keeps its form. The gear has no mass or drag (L1-AER-900), so it changes neither term.
  Derivation chain (D66, D72 Q4, G2-F18): [P-SYS-290] is the anchor, not a requirement. With
  [P-DYN-100], [P-SYS-230], [P-FU-010] and [P-FU-030] it gives [P-FU-040] and [P-FU-050], and
  [P-SYS-280] is then set from this inequality with them, rounded down, so the database values meet
  this record. A change of any anchor input at I1, [P-DYN-100] first, re-derives [P-FU-040],
  [P-FU-050] and [P-SYS-280] in that order and re-checks this record (MS-DYN fuel model,
  parameter derivation; TT-110, TT-750, TT-800 linked).
  Sufficiency (L1-AER-360): the endurance depends on the capacity and the consumption (FU) and on
  the control force the effectors produce in the takeoff and the hold (EF, with FC and AF holding
  still); this record sizes the capacity for the takeoff and the hold with margin, which is FU's
  share, and the EF child shows that the hold uses no more control force than the weight.
Parent(s):     L1-AER-360
Source:        N-150, N-250; CONOPS SC-110 (hover endurance variation); FUNCTIONAL_ANALYSIS §7.3;
  D66, D69, D72, D74
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-290; success criteria: the parameter database values of [P-FU-010],
  [P-FU-030], [P-FU-040], [P-FU-100], [P-DYN-010] and [P-SYS-280] meet the inequality; and in a
  simulated run from a ground start at full fuel in still air, with a takeoff engaged at the start
  and Hover then kept over [P-DYN-270] (SC-110 hover endurance variation, no run to exhaustion,
  D74), the fuel used from the engagement of the takeoff is at most the product of the sum of one
  and [P-FU-100] with the fuel that the closed form gives for a hover of the same duration.
Parameters:    P-FU-010, P-FU-030, P-FU-040, P-FU-100, P-DYN-010, P-SYS-280, P-DYN-270
TBD/TBR:       P-SYS-280 value TBR (TT-800), Martin, G2 (I1); P-FU-010 value TBR (TT-120), P-FU-030,
  P-FU-040 values TBR (TT-110), Martin, G2 (I1); P-FU-100 value TBR (TT-790), Martin, G2;
  P-DYN-270 value TBR (TT-760), Martin, G2
Owner:         Martin
Status:        Draft
Version:       3
```

### L2-AER-FU-300

```req
ID:            L2-AER-FU-300
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute a zero fuel mass flow for each simulation step in
  which the control force and the control moment that the effector subsystem gives for that step
  are both zero.
Rationale:     D69: on the ground, with the effectors off, there is no fuel consumption, and
  L1-AER-940 makes this a requirement so that a later consumption relationship cannot add an idle
  flow. The DD-110 relationships already give it (L2-AER-FU-040), and no other consumption term
  exists (L2-AER-FU-060). The condition is on the control force and moment that FU takes
  (L2-AER-FU-070), not on where the vehicle is, so the same record covers the effectors off on the
  ground (L1-AER-930), the free fall after fuel exhaustion and the credibility checks that run
  with no effector output (N-290). With a zero flow the remaining fuel mass of the next step is
  the same value exactly, since nothing is subtracted (L2-AER-FU-080). During the effector switch-off
  after a landing ([P-SYS-480], L1-AER-930) the effectors still produce output, and FU charges it.
  Sufficiency (L1-AER-940): with L2-AER-FU-040 (the relationships give zero at zero force and
  moment, AN-FU-040) and L2-AER-FU-060 (no other consumption parameter), this record gives a zero
  flow at each step with zero control force and moment and a constant remaining fuel over each
  rest on the ground, which is what L1-AER-940 asks its children to show.
Parent(s):     L1-AER-940
Source:        D65, D69; DD-110; CONOPS SC-130, SC-110 leg 7a
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-300; success criteria: in SC-130, in the rest on the ground of SC-110
  leg 7a and in a ground start held on the ground with no takeoff, with the FU inputs and outputs
  recorded at each simulation step (IN-C2-30), at each step whose control force and control
  moment are both zero the fuel mass flow is zero and the remaining fuel mass of the next step
  equals that of the step; and over each rest on the ground, from [P-SYS-480] after the contact
  step, or from the start of the run, until a takeoff is engaged, the remaining fuel mass is
  constant.
Parameters:    P-SYS-480
TBD/TBR:       P-SYS-480 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-310

```req
ID:            L2-AER-FU-310
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall compute the mass properties of each simulation step with no
  dependence on the gear position.
Rationale:     The landing gear is ideal: it has no mass and no inertia, and its position changes no
  mass property (L1-AER-900, D69; glossary *Landing gear*). Its position therefore enters neither
  mass distribution (L2-AER-FU-160), and FU takes no gear state (L2-AER-FU-270). This keeps the
  centre of gravity fixed while the gear moves (L0-CON-130) and the inertia a function of the fuel
  only (L2-AER-FU-170). L1-AER-900 asks the FU requirements to show it; it is allocated to DYN only
  as baselined, so CR-C2-04 adds FU to its allocation.
  Sufficiency (L1-AER-900): DYN states the gear geometry and its movement; this record makes the
  gear position change no mass property, which is the FU side of the "no effect on the mass
  properties" that L1-AER-900 asks its children to show.
  Sufficiency (L1-AER-210): see L2-AER-FU-150; this record excludes the gear as a cause of a
  centre-of-gravity shift.
  Sufficiency (L1-AER-220): see L2-AER-FU-170; this record keeps the inertia a function of the
  fuel state only.
Parent(s):     L1-AER-900, L1-AER-210, L1-AER-220
Source:        D69; L1-AER-900; work/B3/impact_list.md §2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-310; success criteria: the MS-DYN mass-properties model gives the
  vehicle mass, the centre of gravity and the inertia tensor with no term in the gear position and
  states that the landing gear has no mass; no FU requirement and no FU interface of MS-DYN takes
  the gear position, the gear state or the landing gear command as an input.
Parameters:    —
TBD/TBR:       MS-DYN mass-properties model content (TT-780), Martin, G2 (I1); FU allocation of
  L1-AER-900 (CR-C2-04), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-320

```req
ID:            L2-AER-FU-320
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the dynamics model, at each simulation step, the fuel
  availability that it gives the effector subsystem for that step, through the interface that
  MS-DYN defines between the two subsystems.
Rationale:     A landing needs fuel remaining, and a ground contact at fuel exhaustion is a crash
  whatever the speed (D68, D73 B3-3; L1-AER-260 v2, L1-AER-270 v2). DYN classifies the contact
  (F-AER-12), so it needs the fuel availability: interface I-03 now runs from FU to EF and to the
  ground contact function of DYN (FUNCTIONAL_ANALYSIS I-03 as changed by CR-B3-39). Giving DYN the
  same item as EF, for the same step, means the effectors stop and a contact becomes a crash from
  the same step, with no window in which they disagree. The item is internal to the vehicle model
  and is defined in MS-DYN (IN-C2-15). L1-AER-260 and -270 are allocated to DYN and TM as
  baselined, so CR-C2-04 adds FU to their allocation.
  Sufficiency (L1-AER-270): DYN classifies a contact at fuel exhaustion as a crash; this record
  gives it the fuel availability from which it reads "at fuel exhaustion", which is FU's share.
  Sufficiency (L1-AER-260): see L1-AER-270; the same item gives DYN the "fuel remaining" of a
  landing.
Parent(s):     L1-AER-270, L1-AER-260
Source:        D68, D69, D73; FUNCTIONAL_ANALYSIS §3.2 I-03 (CR-B3-39)
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-320; success criteria: MS-DYN defines interface I-03 from FU to
  the effector model and to the ground contact model, with one fuel availability item per
  simulation step that both use, and the ground contact model classifies a contact with fuel not
  available as a crash.
Parameters:    —
TBD/TBR:       MS-DYN fuel model and ground contact model content (TT-780), Martin, G2 (I1); FU
  allocation of L1-AER-260, -270 (CR-C2-04), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-330

```req
ID:            L2-AER-FU-330
Level:         L2
Type:          Functional
Statement:     If a principal moment of [P-FU-070] or [P-FU-080] in the vehicle parameter set of a
  run differs by more than the relative tolerance [P-FU-090] from the value that the MS-DYN
  mass-properties model derives from [P-DYN-020], [P-DYN-030], [P-FU-030] and [P-FU-010] of that
  set, then the FU subsystem shall reject the vehicle parameter set with an initial-condition error
  to the TST.
Rationale:     G2-F17: the two inertia tensors are derived from the body dimensions and the masses
  (L2-AER-FU-190), but each run takes them from its own parameter set (L2-AER-FU-010). A campaign
  that varies the dry mass, the capacity or the body dimensions without re-deriving them would run
  a body that no mass distribution gives, and L2-AER-FU-190 checks the database values only. FU
  checks the equality at the start of each run and rejects the set rather than correcting it, as
  it rejects an initial fuel out of range (DD-140): the run then uses only values that the
  parameter set states, and the parameter set named in the operational data (L1-AER-650) is what
  the run used (DD-260). The error item is the initial-condition error of ICD-AER-TST, extended
  to the vehicle parameter set (IN-C2-31, glossary change CR-C2-06). This is checking the run
  set-up, not failure handling (tailoring note).
  Sufficiency (L1-AER-220): see L2-AER-FU-170; this record makes the tensor of each run the one
  that MS-DYN derives from that run's shape and masses.
Parent(s):     L1-AER-220
Source:        G2-F17; L0-CON-140; DD-140
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-330; success criteria: a run with the database parameter set starts
  with no initial-condition error; a run whose parameter set has [P-FU-030] changed and the two
  tensors re-derived starts with no error; runs whose parameter sets have [P-FU-030] changed
  without re-deriving the tensors, or one principal moment of [P-FU-080] changed by ten times
  [P-FU-090], each give one initial-condition error that names the inertia item, and FU produces
  no output for those runs.
Parameters:    P-FU-070, P-FU-080, P-FU-090, P-DYN-020, P-DYN-030, P-FU-030, P-FU-010
TBD/TBR:       P-FU-070, P-FU-080 values TBR (TT-770), P-FU-030 value TBR (TT-110), P-FU-010 value
  TBR (TT-120), Martin, G2 (I1); P-FU-090 value TBR (TT-790), Martin, G2; P-DYN-020, P-DYN-030
  values TBR (TT-740), Martin, 2026-11-30; initial-condition error item in ICD-AER-TST (IN-C2-31,
  TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-340

```req
ID:            L2-AER-FU-340
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall set the remaining fuel mass at the end of each exhaustion
  step to zero.
Rationale:     G2-F10: with the flow limited to the fuel left divided by [P-SYS-300]
  (L2-AER-FU-050), the remaining fuel computed as the fuel at the start minus the flow times the
  step is not exactly zero in floating point; the inspector found a positive residual in about
  7 % and a negative one in about 7 % of random cases. A positive residual would keep the fuel
  available for one more step of full effector output on almost no fuel (L2-AER-FU-200), and a
  negative one would break L2-AER-FU-090. Setting the value to zero at the end of the exhaustion
  step makes exhaustion exact whatever the rounding. The difference from the summed flow is
  rounding only, inside [P-FU-060] (L2-AER-FU-080). In every other step the product of the
  consumption rate and the step is below the fuel left, and the accounting subtracts that same
  product, so the result stays above zero (MS-DYN fuel model, DD-270).
  Sufficiency (L1-AER-190): see L2-AER-FU-050; this record closes the exhaustion step of the
  accounting at exactly zero.
  Sufficiency (L1-AER-200): see L2-AER-FU-200; this record makes the first step with zero fuel the
  step after the exhaustion step, so the effectors stop there.
Parent(s):     L1-AER-190, L1-AER-200
Source:        G2-F10; DD-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-340; success criteria: in the reference mission (SC-110) and in a set
  of runs that reach fuel exhaustion from initial fuel masses chosen so that the fuel left at the
  start of the exhaustion step is spread over the range from zero to the fuel of one step at the
  consumption rate of that step, with the FU outputs recorded at each simulation step (IN-C2-30),
  the remaining fuel mass is exactly zero at the step that follows each exhaustion step, and the
  fuel availability is not available from that step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
