## FU — Fuel and mass properties

The fuel and mass-properties requirements (task C2). The subject of each statement is the FU subsystem, the fuel and mass-properties subsystem of the Aeronef, one of the three subsystems of the vehicle model, with the dynamics model (DYN) and the effector subsystem (EF), behind the vehicle-model boundary (D55, L1-AER-430). FU runs at each simulation step `[P-SYS-300]`. Its inputs are the fuel mass of the initial condition, the vehicle parameter set and the effector outputs of each step. Its outputs are the fuel mass flow, the remaining fuel mass, the mass properties (vehicle mass, centre-of-gravity position, inertia tensor), the fuel availability for the effectors and the fuel state.

**What FU decides.** The consumption relationships are linear in the magnitude of the resultant control force and of the resultant control moment (DD-110, owner D65). The inertia tensor changes with the fuel: it runs linearly from the dry-mass tensor at fuel exhaustion to its full-capacity value, because the fuel depletes uniformly over a fixed volume centred on the centre of gravity (DD-120, D65); a constant inertia is the special case of a zero fuel tensor. In the step that ends at fuel exhaustion, the flow is limited to the fuel left (DD-130). The equations themselves go in MS-DYN, which C1 writes; `work/C2/interface_needs.md` IN-C2-10 to -16 gives them.

**Exhaustion is nominal.** Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070). FU then gives the dry-mass properties, zero fuel mass flow, a fuel availability of not available and the exhaustion indication, and it keeps doing so to the end of the run.

**Verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would describe the implementation (D4), so each record is verified directly by its own method. The L1 parents are verified by roll-up (D40, D58). Several tests read FU outputs that the operational data do not carry (the centre of gravity, the inertia tensor, the fuel availability); they read them at the vehicle-model boundary or at the interfaces of MS-DYN, recorded by the TST for the test run (IN-C2-30).

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
  that produced it.
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
TBD/TBR:       P-FU-010, P-FU-030, P-FU-040, P-FU-050 values TBR (TT-110, TT-120), P-FU-020 value
  TBR (TT-130), Martin, G2 (I1); P-FU-070, P-FU-080 values TBD (TT-770), Martin, G2 (I1);
  P-FU-090 value TBR (TT-790), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
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
  capacity [P-FU-010] is the parameter, and the initial fuel is set per run (D63 Q3). The
  reference mission starts at [P-FU-010] (SC-110). The value applies at simulation time zero
  (CV-810), before any fuel is consumed, so the first output sample reports it unchanged.
  Sufficiency (L1-AER-150): see L2-AER-FU-010.
  Sufficiency (L1-AER-660): the fuel mass is the FU item of the initial condition; DYN, AF and
  FCP take the other items. With L2-AER-FU-030 (the range check), this record makes FU start
  from the fuel mass it is given, which is FU's share of L1-AER-660.
Parent(s):     L1-AER-150, L1-AER-660
Source:        N-310; CONOPS §4.6, SC-110, SC-200; D63
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-020; success criteria: for runs started with an initial fuel mass of
  zero, of one half of [P-FU-010] and of [P-FU-010], the remaining fuel mass at the first output
  sample equals the initial fuel mass within [P-FU-060].
Parameters:    P-FU-010, P-FU-060
TBD/TBR:       P-FU-010, P-FU-060 values TBR (TT-110, TT-120), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  error item is defined in ICD-AER-TST (IN-C2-31); the TST decides what to do with the run. This
  is checking the run set-up, not failure handling (tailoring note). Zero and [P-FU-010] are
  valid. Rejection chosen by the owner (D65, DD-140).
  Sufficiency (L1-AER-150): see L2-AER-FU-010.
  Sufficiency (L1-AER-660): see L2-AER-FU-020.
Parent(s):     L1-AER-150, L1-AER-660
Source:        N-310; CONOPS §4.6
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-030; success criteria: initial conditions with a fuel mass of zero and
  of [P-FU-010] start a run; initial conditions with a fuel mass of 1.01 times [P-FU-010] and of
  minus 0.01 times [P-FU-010] each produce one initial-condition error that names the fuel mass,
  and no output sample.
Parameters:    P-FU-010
TBD/TBR:       P-FU-010 value TBR (TT-120), Martin, G2 (I1); initial-condition
  error item in ICD-AER-TST (IN-C2-31, TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-040

```req
ID:            L2-AER-FU-040
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the consumption rate of each simulation step as the
  sum of a translational term from the control forces of the effector outputs of that step and a
  rotational term from their control moments, with the consumption relationships and the parameters
  [P-FU-040] and [P-FU-050] that MS-DYN defines.
Rationale:     Fuel is consumed to produce the control forces and control moments, with separate
  terms for translation and rotation (L0-CON-120; AIRCRAFT_CHARACTERISTICS §4). The form of each
  relationship is a C2 decision recorded in MS-DYN (L1-AER-160). C2 proposes (DD-110,
  IN-C2-10): the translational term is [P-FU-040] times the magnitude of the resultant control
  force, and the rotational term is [P-FU-050] times the magnitude of the resultant control
  moment about the centre of gravity. Both terms are linear, so the hover endurance has the
  closed form of FUNCTIONAL_ANALYSIS §7.3 (L2-AER-FU-290). Both are zero when the effector
  outputs are zero, so no fuel is used in free fall or in torque-free rotation, which keeps the
  MS-DYN credibility checks exact (N-290). Both are at least zero for non-negative parameters,
  so the remaining fuel never increases (L2-AER-FU-100). Using the resultant keeps the
  consumption independent of the effector layout, which stays an EF design decision. The owner
  chose this resultant form over charging each effector (D65); MS-DYN holds the form. The effectors counter gravity, so fuel is consumed in
  each flight condition, hover included (CONOPS §4.5). The consumption rate is the fuel mass
  flow except in the step that ends at fuel exhaustion (L2-AER-FU-050).
  Sufficiency (L1-AER-160): with L2-AER-FU-050 (the flow, limited at exhaustion) and
  L2-AER-FU-070 (the effector outputs as input), this record computes the fuel mass flow from
  the control forces and control moments of the effectors through the two relationships of
  MS-DYN, and it makes the fuel used depend on the effector output (L0-CON-100).
Parent(s):     L1-AER-160
Source:        N-280; AIRCRAFT_CHARACTERISTICS.md §4; CONOPS §4.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-040; success criteria: in the reference mission (SC-110), in a run
  with translational effector output only and in a run with rotational effector output only, at
  each output sample whose simulation step does not end at fuel exhaustion, the recorded fuel
  mass flow agrees within the relative tolerance [P-FU-090] with an independent computation of
  the MS-DYN relationships from the recorded effector outputs and the run's [P-FU-040] and
  [P-FU-050]; at each output sample with zero effector outputs the recorded fuel mass flow is
  zero.
Parameters:    P-FU-040, P-FU-050, P-FU-090
TBD/TBR:       P-FU-040, P-FU-050 values TBR (TT-110), Martin, G2 (I1); MS-DYN fuel model content
  (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-050

```req
ID:            L2-AER-FU-050
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the fuel mass flow of each simulation step as the
  smaller of the consumption rate of that step and the remaining fuel mass at the start of that step
  divided by [P-SYS-300].
Rationale:     The effectors produce their output during a step whose remaining fuel mass is above
  zero at its start (L2-AER-FU-200), so in the step that ends at fuel exhaustion the consumption
  rate can ask for more fuel than is left. Limiting the flow to what is left makes the remaining
  fuel exactly zero at the end of that step, keeps the fuel accounting within [P-FU-060]
  (L2-AER-FU-080) and keeps the remaining fuel at or above zero (L2-AER-FU-090). In each other
  step the flow equals the consumption rate. The effector output is one value per simulation
  step (glossary *Effector output*), so the fuel consumed in a step is the flow times
  [P-SYS-300] exactly (DD-130, IN-C2-12).
  Sufficiency (L1-AER-160): see L2-AER-FU-040.
  Sufficiency (L1-AER-190): with L2-AER-FU-080 (the accounting) and L2-AER-FU-090 (at or above
  zero), this record keeps the remaining fuel mass equal to the initial fuel mass minus the
  integral of the reported flow, including the exhaustion step, which is the check of
  L1-AER-190.
Parent(s):     L1-AER-160, L1-AER-190
Source:        METHODOLOGY §10.3; CONOPS SC-110
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-050; success criteria: in the reference mission (SC-110), with the
  FU outputs recorded at each simulation step (IN-C2-30), the fuel mass flow of the step that ends
  at fuel exhaustion equals the remaining fuel mass at its start divided by [P-SYS-300] within the
  relative tolerance [P-FU-090], the remaining fuel mass of the next step is zero, and the fuel
  mass flow of each other step equals the consumption rate of AN-FU-040 within [P-FU-090].
Parameters:    P-SYS-300, P-FU-090, P-FU-060
TBD/TBR:       P-SYS-300 value TBR (TT-070), Martin, G2 (I1); P-FU-090 value TBR (TT-790), Martin, G2
  (C2)
Owner:         Martin
Status:        Draft
Version:       1
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
  kind. Under the owner's choice (D65, DD-110) each set is one coefficient, common to the
  effector set. The step duration that limits the flow at exhaustion
  (L2-AER-FU-050) is the time base, not a consumption parameter.
  Sufficiency (L1-AER-100): the EF children define the direction of action, the control
  effectiveness, the output limits and the command response; this record makes the two
  consumption sets the only parameters of the fifth kind, so the EF and FU children together are
  the closed list of L1-AER-100.
Parent(s):     L1-AER-100
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §4, §7
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-060; success criteria: the MS-DYN consumption relationships use
  no parameter other than [P-FU-040] and [P-FU-050], and the parameter database holds no FU or EF
  parameter that enters a consumption relationship other than these two.
Parameters:    P-FU-040, P-FU-050
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-070

```req
ID:            L2-AER-FU-070
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall take the effector outputs of each simulation step from the
  effector subsystem through the interface that MS-DYN defines between the two subsystems.
Rationale:     Interface I-01 (FUNCTIONAL_ANALYSIS §3.2) is internal to the vehicle model, so it is
  defined in MS-DYN, not in an ICD. FU uses the same effector outputs as the dynamics model,
  so the fuel used and the motion come from one set of control forces and control moments. MS-DYN
  states one mapping from the effector outputs to the resultant control force and control moment
  about the centre of gravity, through the EF control effectiveness, and DYN and FU both use it
  (IN-C2-11).
  Sufficiency (L1-AER-160): see L2-AER-FU-040; this record supplies the effector outputs that the
  computation needs.
Parent(s):     L1-AER-160
Source:        FUNCTIONAL_ANALYSIS §3.2 I-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-070; success criteria: MS-DYN defines the interface from EF to
  FU with the effector outputs of each simulation step, and one mapping from effector outputs to
  control force and control moment that both the equations of motion and the consumption
  relationships use; no FU requirement takes effector output from another source.
Parameters:    —
TBD/TBR:       MS-DYN content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  §10.3. The flow is constant over each step (L2-AER-FU-050), so the time integral of the flow
  is this sum, and the tolerance covers the arithmetic only. The check uses the flow of each
  simulation step; an integration of the output samples at [P-TM-010] would add a sampling error
  that the tolerance is not meant to cover; the owner chose per-step data (D65).
  Sufficiency (L1-AER-190): see L2-AER-FU-050.
Parent(s):     L1-AER-190
Source:        METHODOLOGY §10.3; N-290
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-080; success criteria: over the reference mission (SC-110), from
  [P-FU-010] to ground contact, with the FU outputs recorded at each simulation step (IN-C2-30),
  an independent summation of the fuel mass flow of each step times [P-SYS-300], subtracted from
  the initial fuel mass, agrees with the remaining fuel mass of each step within [P-FU-060].
Parameters:    P-FU-060, P-SYS-300, P-TM-010, P-FU-010
TBD/TBR:       P-FU-060 value TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-090

```req
ID:            L2-AER-FU-090
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall keep the remaining fuel mass of each simulation step no less
  than zero.
Rationale:     A negative fuel mass has no physical meaning and would give a vehicle mass below the
  dry mass. The fuel used in the last step is limited to the fuel left (L2-AER-FU-050), so the
  fuel reaches exactly zero at exhaustion. It then stays at zero: the effectors produce no output
  (L2-AER-FU-200, L1-AER-200), so the consumption rate is zero (L2-AER-FU-040).
  Sufficiency (L1-AER-190): see L2-AER-FU-050.
  Sufficiency (L1-AER-180): with L2-AER-FU-110 (vehicle mass), this record keeps the vehicle mass
  at or above the dry mass [P-FU-030], so the mass decreases only by fuel that was on board.
Parent(s):     L1-AER-190, L1-AER-180
Source:        CONOPS §4.5, SC-110
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-090; success criteria: in the reference mission (SC-110) and in a run
  started with zero fuel, the remaining fuel mass is at or above zero at each output sample, and
  it is exactly zero at each output sample from the first sample at fuel exhaustion to the end of
  the run.
Parameters:    P-FU-030
TBD/TBR:       P-FU-030 value TBR (TT-110), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-100

```req
ID:            L2-AER-FU-100
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall keep the remaining fuel mass of each simulation step no
  greater than the remaining fuel mass of the previous simulation step.
Rationale:     Fuel is only consumed during a run; nothing refuels the Aeronef (CONOPS §4.5; SC-110:
  the fuel quantity decreases throughout the mission and never increases). The consumption rate
  is at least zero because the consumption parameters are at least zero (L2-AER-FU-040; ranges in
  `work/C2/param_proposals.md`).
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
Version:       1
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
  (glossary), the value the authority budgets use (L1-AER-120, -130).
  Sufficiency (L1-AER-180): see L2-AER-FU-100.
Parent(s):     L1-AER-180
Source:        N-280; CV-340; L0-ASM-090
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-110; success criteria: at each output sample of the reference
  mission (SC-110), including the samples from fuel exhaustion to ground contact, the recorded
  vehicle mass equals [P-FU-030] plus the recorded remaining fuel mass within [P-FU-060].
Parameters:    P-FU-030, P-FU-010, P-FU-060
TBD/TBR:       P-FU-030, P-FU-010, P-FU-060 values TBR (TT-110, TT-120),
  Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-120

```req
ID:            L2-AER-FU-120
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the dynamics model, at each simulation step, the
  vehicle mass, the centre-of-gravity position and the inertia tensor of that step through the
  interface that MS-DYN defines between the two subsystems.
Rationale:     Interface I-04 is internal to the vehicle model. The equations of motion of a step
  use the mass properties of that step: the vehicle mass in the translational equations and in
  the sensed acceleration, the inertia tensor in the rotational equations, and the centre of
  gravity as the body-frame origin (MS-DYN, IN-C2-14). The equations carry no thrust term and no
  rate-of-change-of-inertia term, because consumed fuel leaves with no force or moment
  (L0-ASM-090).
  Sufficiency (L1-AER-180): see L2-AER-FU-100; this record delivers the vehicle mass to DYN, the
  other subsystem of L1-AER-180.
  Sufficiency (L1-AER-210): see L2-AER-FU-150.
  Sufficiency (L1-AER-220): see L2-AER-FU-170.
Parent(s):     L1-AER-180, L1-AER-210, L1-AER-220
Source:        FUNCTIONAL_ANALYSIS §3.2 I-04; CV-340, CV-350
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-120; success criteria: MS-DYN defines the interface from FU to
  DYN with the vehicle mass, the centre-of-gravity position and the inertia tensor, with their
  units and frame (CV-340, CV-350), and states that the equations of motion of a step use the
  mass properties of that step.
Parameters:    —
TBD/TBR:       MS-DYN content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  vehicle state (L1-AER-440). FU takes no input from the flight software. The fuel mass flow goes
  to the operational data, which observes the boundary without being a party to it
  (L2-AER-FU-250). The home of the boundary ICD is open (IN-B1-01, TT-720).
  Sufficiency (L1-AER-430): FU's outputs across the boundary are two of the listed kinds, and FU
  takes none of the listed inputs, so FU's share of L1-AER-430 is covered.
Parent(s):     L1-AER-430
Source:        FUNCTIONAL_ANALYSIS §3.2 I-05, I-06, §5.1; D55
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
Version:       1
```

### L2-AER-FU-140

```req
ID:            L2-AER-FU-140
Level:         L2
Type:          Interface
Statement:     The FU subsystem shall give the flight software the same vehicle mass as it gives the
  dynamics model for the same simulation step.
Rationale:     Flight control holds the sensed acceleration within [P-SYS-120] by limiting the
  resultant control force at the current mass (D38, L1-AER-290), and DYN computes the sensed
  acceleration with the mass it receives. Both must use one value, or the limit would be set
  against a mass the vehicle does not have. Within a control frame the mass falls by the fuel
  used in that frame; flight control reads the mass at the frame start, so it covers that fall
  in its share of the budget margin (IN-C2-41 gives the bound).
  Sufficiency (L1-AER-290): FC owns the limit, AF keeps its manoeuvres within [P-SYS-440] and DYN
  computes the sensed acceleration (L1-AER-290 rationale); FU supplies the mass to both sides,
  and this record makes it one mass, which is FU's share.
Parent(s):     L1-AER-290
Source:        D38, D45; N-170
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-140; success criteria: in the reference mission (SC-110), at the first
  simulation step of each control frame, the vehicle mass across the vehicle-model boundary
  equals the vehicle mass given to the dynamics model for that step.
Parameters:    P-SYS-120, P-SYS-440
TBD/TBR:       P-SYS-440 value TBR (TT-040), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-150

```req
ID:            L2-AER-FU-150
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall give the centre-of-gravity position as the body-frame origin
  at each fuel state.
Rationale:     The centre of gravity is fixed, including while fuel is consumed (L0-CON-130,
  L1-AER-210), and it is the body-frame origin (CV-160), so the effector moment arms stay
  constant. Giving it as an output, zero in each body axis, lets FC and DYN read it rather than
  assume it, and gives one place to change if a later version lets it move (CV-160). The dry-mass
  and fuel-mass distributions are centred on it (L2-AER-FU-160), so the output is also the
  physical centre of gravity.
  Sufficiency (L1-AER-210): FU defines the mass distribution and DYN uses the centre of gravity
  as origin (L1-AER-210 rationale). With L2-AER-FU-160 (both distributions centred on the origin)
  and L2-AER-FU-120 (given to DYN), this record keeps the centre of gravity at one body-frame
  position for each fuel mass.
Parent(s):     L1-AER-210
Source:        AIRCRAFT_CHARACTERISTICS.md §4; CV-160
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-150; success criteria: MS-DYN and the vehicle-model boundary ICD
  define the centre-of-gravity output as the body-frame origin, with no dependence on the
  remaining fuel mass.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-160

```req
ID:            L2-AER-FU-160
Level:         L2
Type:          Constraint
Statement:     The FU subsystem shall use a dry-mass distribution and a fuel-mass distribution that
  each have the body-frame origin as centre of mass at each fuel state.
Rationale:     The centre of gravity stays fixed while fuel is consumed only if neither part moves it
  (L0-CON-130). The fuel does not slosh (L0-ASM-080). C2 proposes that the fuel depletes
  uniformly over a fixed fuel volume centred on the centre of gravity (DD-120), so the centre
  of mass of the fuel stays at the origin at each fuel mass and its inertia scales with its mass
  (L2-AER-FU-170). MS-DYN states both distributions, with their dimensions as DYN parameters
  (L1-AER-220; IN-C2-13).
  Sufficiency (L1-AER-210): see L2-AER-FU-150.
Parent(s):     L1-AER-210
Source:        AIRCRAFT_CHARACTERISTICS.md §4; L0-ASM-080
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-160; success criteria: MS-DYN states the dry-mass and the
  fuel-mass distributions, and the first moment of each about the body-frame origin is zero for
  each remaining fuel mass from zero to [P-FU-010].
Parameters:    P-FU-010
TBD/TBR:       MS-DYN content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-170

```req
ID:            L2-AER-FU-170
Level:         L2
Type:          Model fidelity
Statement:     The FU subsystem shall compute the inertia tensor of each simulation step as the sum
  of [P-FU-070] and the product of [P-FU-080] with the ratio of the remaining fuel mass of that
  step to [P-FU-010].
Rationale:     L1-AER-220 leaves to C2 whether the inertia changes with the fuel state. C2 decides
  that it does, and the owner confirmed it (DD-120, D65). First, the vehicle mass changes with the
  fuel (L1-AER-180), and an inertia that kept its full-fuel value while the fuel burns would
  contradict it. Second, the control laws then meet a varying inertia as well as a varying mass,
  which is what comparing control laws needs (L0-OBJ-020); the vehicle-model boundary carries the
  inertia for that reason (L1-AER-430 rationale). With the fuel depleting uniformly over a fixed
  volume centred on the centre of gravity (L2-AER-FU-160), the fuel's share of the inertia is
  proportional to the remaining fuel mass, so the tensor runs linearly from [P-FU-070] at fuel
  exhaustion to [P-FU-070] plus [P-FU-080] at full capacity. The maximum inertia, used by the
  moment authority budget (L1-AER-140, -350), is the full-capacity value. A constant inertia is
  the case of [P-FU-080] at zero.
  MS-DYN uses the inertia of each step with no rate-of-change term, because consumed fuel leaves
  with no moment (L0-ASM-090, IN-C2-14).
  Sufficiency (L1-AER-220): with L2-AER-FU-180 (diagonal), L2-AER-FU-190 (derived from the shape
  and the distributions) and L2-AER-FU-120 (given to DYN), this record states the inertia tensor
  at each fuel state, derived as MS-DYN states it, and answers the fuel-state question that
  L0-CON-140 leaves open.
Parent(s):     L1-AER-220
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §4; L0-CON-140; D61
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-170; success criteria: at each output sample of the reference
  mission (SC-110), the inertia tensor given across the vehicle-model boundary equals [P-FU-070]
  plus [P-FU-080] times the ratio of the recorded remaining fuel mass to [P-FU-010], within the
  relative tolerance [P-FU-090] on each principal moment.
Parameters:    P-FU-070, P-FU-080, P-FU-010, P-FU-090
TBD/TBR:       P-FU-070, P-FU-080 values TBD, derived in MS-DYN (TT-770), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  principal moments each and no product of inertia; MS-DYN states zero products of inertia, with
  the CV-350 sign convention, for both distributions; the vehicle-model boundary ICD defines the
  inertia tensor with zero off-diagonal terms.
Parameters:    P-FU-070, P-FU-080
TBD/TBR:       P-FU-070, P-FU-080 values TBD, derived in MS-DYN (TT-770), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  triangle inequality. The body shape is provisional (TBR in L0-CON-140), so the derived values
  change with it.
  Sufficiency (L1-AER-220): see L2-AER-FU-170.
Parent(s):     L1-AER-220
Source:        L0-CON-140; AIRCRAFT_CHARACTERISTICS.md §1, §4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-190; success criteria: MS-DYN derives each principal moment of
  [P-FU-070] and [P-FU-080] from the stated shape dimensions, [P-FU-030], [P-FU-010] and the
  stated distributions, and the parameter database values equal the derived values, with a
  source that cites MS-DYN.
Parameters:    P-FU-070, P-FU-080, P-FU-030, P-FU-010
TBD/TBR:       Body shape provisional (L0-CON-140, TT-430), Martin, 2026-11-30; P-FU-070, P-FU-080
  values TBD (TT-770), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
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
  holds to the end of the run, and the vehicle then moves under gravity and drag alone (SC-110
  leg 11). The remaining fuel mass of a step is its value at the start of the step (CV-840), so a
  step that starts with fuel left still produces output, and the flow limit of L2-AER-FU-050
  keeps it to the fuel left. The interface is internal to the vehicle model and is defined in
  MS-DYN (IN-C2-15).
  Sufficiency (L1-AER-200): EF produces zero output while fuel is not available; this record
  makes fuel not available from the first simulation step at which the remaining fuel mass is
  zero, so the two give zero control force and moment from that step, as L1-AER-200 requires.
Parent(s):     L1-AER-200
Source:        N-150; CONOPS §4.5, SC-110; L0-ASM-070
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-200; success criteria: in the reference mission (SC-110) and in a run
  started with zero fuel, the fuel availability is available at each simulation step whose
  remaining fuel mass is above zero, and not available at each step whose remaining fuel mass is
  zero, from the first such step to the end of the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
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
Rationale:     The crew needs a warning before the fuel runs out (N-150). The threshold is a
  fraction of the capacity, not of the initial fuel (L1-AER-570, CV-720), so a run that starts
  below it shows the low-fuel indication from its first step. FU sets the indication in the step
  in which the fuel first falls below the threshold, so FU's share of the alert latency
  [P-SYS-470] is zero; the flight software reads it at the next control frame and FCP presents it
  at an output sample (FUNCTIONAL_ANALYSIS §7.5). The indication stays set at fuel exhaustion;
  which annunciation the panel shows then, and the alert label, are FCP's (IN-C2-43).
  Sufficiency (L1-AER-570): FCP annunciates the low-fuel alert from the fuel state within its
  share of [P-SYS-470]; this record gives it the condition at the simulation step at which it
  first holds, and L2-AER-FU-240 carries it to the panel, so the alert meets [P-SYS-470].
Parent(s):     L1-AER-570
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-220; success criteria: in the reference mission (SC-110), the low-fuel
  indication is clear at each simulation step whose remaining fuel mass is at or above [P-FU-020]
  times [P-FU-010], and set at each step whose remaining fuel mass is below it, including the
  first such step; in a run started below the threshold, it is set at the first step.
Parameters:    P-FU-020, P-FU-010, P-SYS-470
TBD/TBR:       P-FU-020 value TBR (TT-130), P-SYS-470 value TBR (TT-070), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-230

```req
ID:            L2-AER-FU-230
Level:         L2
Type:          Functional
Statement:     The FU subsystem shall indicate, in the fuel state of each simulation step, whether
  the vehicle is at fuel exhaustion at that step.
Rationale:     The crew needs to know when the fuel has run out (N-150, L1-AER-580). Autoflight
  takes the fuel state too (F-AER-08), to set its mode state at exhaustion; what the modes do then
  is C5's (#59), and FU gives the indication whatever C5 decides (D65). The remaining fuel
  mass reaches exactly zero (L2-AER-FU-050, -090), so the indication is set at the first step
  with zero fuel, and FU's share of [P-SYS-470] is zero. Fuel exhaustion is a nominal state
  (L0-ASM-070): the indication is not a failure annunciation.
  Sufficiency (L1-AER-580): as for L2-AER-FU-220, with the exhaustion condition: FCP annunciates
  it within its share of [P-SYS-470], and L2-AER-FU-240 carries it to the panel.
Parent(s):     L1-AER-580
Source:        N-150; CONOPS §4.5, SC-110
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FU-230; success criteria: in the reference mission (SC-110), the
  fuel-exhaustion indication is clear at each simulation step with remaining fuel mass above zero,
  and set from the first step with zero remaining fuel mass to the end of the run.
Parameters:    P-SYS-470
TBD/TBR:       Autoflight state after fuel exhaustion (#59, TT-580), Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
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
Parameters:    P-TM-010
TBD/TBR:       Releasable or protected classification (#69, TT-600), Martin, closes when the plan
  is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
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
  vehicle parameter set, the fuel mass of the initial condition and the effector outputs of that
  step and of the preceding steps of the run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59). FU adds no
  variation if its outputs depend on nothing but the run's own inputs: no wall-clock time, no
  random source and no state carried over from another run or another simulation instance.
  Bit-identical results are not required (D25, D59); the tolerances are those of each success
  criterion (D63 Q4).
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
  TP-FU-260.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
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
  MS-DYN. C1 writes MS-DYN; C2 supplies the content (IN-C2-10 to -16). The list is closed.
  Sufficiency (L1-AER-720): this record gives MS-DYN its fuel and mass-properties sections; the
  DYN and EF children give the other sections.
Parent(s):     L1-AER-720
Source:        N-270; plan §6 C1, C2
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FU-280; success criteria: MS-DYN, at its G2 baseline, has a section
  for each of the five listed FU models, and each FU model-fidelity requirement (L2-AER-FU-040,
  -050, -080, -110, -170) cites the section it rests on.
Parameters:    —
TBD/TBR:       MS-DYN content (TT-780), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FU-290

```req
ID:            L2-AER-FU-290
Level:         L2
Type:          Performance
Statement:     The FU subsystem shall have a fuel capacity [P-FU-010] of at least the product of
  [P-FU-030] with the quantity E minus one, where E is the exponential of the product of one plus
  [P-FU-100], [P-FU-040], [P-DYN-010] and [P-SYS-280].
Rationale:     Fuel budget (FUNCTIONAL_ANALYSIS §7.3, L1-AER-360). In symbols: [P-FU-010] ≥
  [P-FU-030] · (exp((1 + [P-FU-100]) · [P-FU-040] · [P-DYN-010] · [P-SYS-280]) − 1). In a hold in still air at level
  attitude, the control force balances the weight and the control moment is zero, so with the
  C2 relationships (L2-AER-FU-040) the fuel mass flow is [P-FU-040] times [P-DYN-010] times the
  vehicle mass, and the mass decays exponentially. From full fuel the endurance is then the
  natural logarithm of the ratio of the maximum vehicle mass to the dry mass, divided by
  [P-FU-040] times [P-DYN-010]; it is at least [P-SYS-280] when the capacity meets this record
  with [P-FU-100] at zero. C2 confirms the form that B1 assumed. The margin [P-FU-100] adds the
  consumption the closed form leaves out, as FUNCTIONAL_ANALYSIS §7.3 asks: the regulation of the
  hold, the moments that hold the attitude, and the transient at the start of the hold. The
  consumption coefficient comes from the owner's endurance at maximum speed (D66), and
  [P-SYS-280] is set from this inequality with it, so the database values meet this record.
  Sufficiency (L1-AER-360): the endurance depends on the capacity and the consumption (FU) and on
  the control force the effectors produce in the hold (EF, with FC and AF holding still); this
  record sizes the capacity for the hold with margin, which is FU's share, and the EF child shows
  that the hold uses no more control force than the weight.
Parent(s):     L1-AER-360
Source:        N-150, N-250; CONOPS SC-110 (hover endurance variation); FUNCTIONAL_ANALYSIS §7.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-FU-290; success criteria: the parameter database values of [P-FU-010],
  [P-FU-030], [P-FU-040], [P-FU-100], [P-DYN-010] and [P-SYS-280] meet the inequality; and a
  simulated hold in still air at level attitude from full fuel (SC-110 hover endurance variation)
  reaches fuel exhaustion no earlier than [P-SYS-280] from the start of the hold.
Parameters:    P-FU-010, P-FU-030, P-FU-040, P-FU-100, P-DYN-010, P-SYS-280
TBD/TBR:       P-SYS-280 value TBR (TT-800), Martin, G2 (I1); P-FU-010, P-FU-030, P-FU-040
  values TBR (TT-110, TT-120), Martin, G2 (I1); P-FU-100 value TBR (TT-790), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```
