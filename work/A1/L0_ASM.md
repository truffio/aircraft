## ASM — Assumptions register

### L0-ASM-010

```asm
ID:            L0-ASM-010
Assumption:    The flight-control, autoflight and navigation functions receive the true simulated
  vehicle state, without sensor noise, bias or latency.
Rationale:     Perfect state knowledge keeps the first version focused on control laws and mode
  logic (METHODOLOGY §4.4, §5 F-AER-04). Sensor and estimation models can be added in a later
  version through a change request.
Affects:       L0-OBJ-020, L0-OBJ-030, L0-OBJ-140; Aeronef navigation, flight-control and autoflight
  subsystems; function F-AER-04
Owner:         Martin
Status:        Open
```

### L0-ASM-020

```asm
ID:            L0-ASM-020
Assumption:    Each simulation run is deterministic: one configuration, software version, input set
  and execution host produce identical outputs, and any random variation comes from a recorded
  random seed.
Rationale:     Determinism makes runs reproducible and comparisons fair, and it lets statistical
  campaigns be replayed run by run (TESTING_ENVIRONMENT §5, §6).
Affects:       L0-OBJ-100, L0-OBJ-110, L0-SUC-040, L0-SUC-080, L0-SUC-090; STP execution and
  campaign generation
Owner:         Martin
Status:        Open
```

### L0-ASM-030

```asm
ID:            L0-ASM-030
Assumption:    The Earth is flat and non-rotating, and the local reference frame is an inertial
  frame.
Rationale:     The Aeronef is a fictional low-complexity vehicle; Earth curvature, rotation and
  Coriolis effects add no value to the study of control laws and mode logic, and a flat Earth keeps
  VOR radial geometry planar.
Affects:       L0-CON-010, L0-CON-090, L0-CON-280; model specification; navigation subsystem (VOR
  geometry); conventions document
Owner:         Martin
Status:        Open
```

### L0-ASM-040

```asm
ID:            L0-ASM-040
Assumption:    Gravity is uniform over the operating volume, with constant magnitude and a constant
  direction along the local vertical.
Rationale:     Consistent with L0-ASM-030. A uniform field gives closed-form free-fall solutions for
  model verification (METHODOLOGY §10.3). The value of gravitational acceleration is a dynamics
  parameter.
Affects:       L0-CON-090; model specification (gravity model); dynamics analytical checks
Owner:         Martin
Status:        Open
```

### L0-ASM-050

```asm
ID:            L0-ASM-050
Assumption:    The air is still: there is no wind, gust or turbulence, so aerodynamic drag depends
  on the vehicle velocity relative to the local reference frame.
Rationale:     The concept lists gravity and drag as the only external effects
  (AIRCRAFT_CHARACTERISTICS §2). Still air also makes the velocity through the air equal to the
  velocity over the ground, which keeps track and horizontal speed unambiguous.
Affects:       L0-CON-090; model specification (drag model); navigation subsystem (track, horizontal
  speed)
Owner:         Martin
Status:        Open
```

### L0-ASM-060

```asm
ID:            L0-ASM-060
Assumption:    Air properties vary with altitude only and do not vary with time.
Rationale:     The drag model needs air density; a time-invariant, horizontally uniform atmosphere
  is the simplest model consistent with L0-ASM-050. Whether density is constant or follows a
  standard atmosphere is a model-specification choice.
Affects:       L0-CON-090; model specification (drag model)
Owner:         Martin
Status:        Open
```

### L0-ASM-070

```asm
ID:            L0-ASM-070
Assumption:    Each Aeronef component operates without failure in this development cycle.
Rationale:     Hazard and failure analysis is deferred by the project tailoring (METHODOLOGY,
  tailoring note). Fuel exhaustion and effector saturation are nominal behaviour, not failures.
Affects:       All L0 requirements; Criticality attribute; verification planning (no fault-injection
  cases)
Owner:         Martin
Status:        Open
```

### L0-ASM-080

```asm
ID:            L0-ASM-080
Assumption:    The Aeronef structure is rigid, and its fuel does not slosh.
Rationale:     Consistent with the rigid-body constraint L0-CON-010 and the fixed centre of gravity
  L0-CON-130.
Affects:       L0-CON-010, L0-CON-130; model specification; fuel and mass-properties subsystem
Owner:         Martin
Status:        Open
```

### L0-ASM-090

```asm
ID:            L0-ASM-090
Assumption:    Consumed fuel leaves the vehicle without imparting force or moment to it.
Rationale:     The effectors are fictional gravity-like emitters, not reaction engines, so the mass
  flow of consumed fuel produces no thrust term in the equations of motion; the instantaneous mass
  alone changes (L0-CON-110).
Affects:       L0-CON-110; model specification (variable-mass equations of motion); fuel and
  mass-properties subsystem
Owner:         Martin
Status:        Open
```

### L0-ASM-100

```asm
ID:            L0-ASM-100
Assumption:    The operating environment contains no terrain, obstacles or other vehicles.
Rationale:     The project studies the control and mode logic of a single vehicle; the environment
  is free space above an altitude datum.
Affects:       Concept of operations scenarios; navigation subsystem; STP scenario definition
Owner:         Martin
Status:        Open
```

### L0-ASM-110

```asm
ID:            L0-ASM-110
Assumption:    The Aeronef is airborne for the whole of each run, and ground contact is not
  modelled.
Rationale:     No ground operations are in the concept. A run in which the vehicle reaches the
  altitude datum, for example after fuel exhaustion, ends at that event (issues.md, Q-A1-03).
Affects:       Model specification; STP run termination conditions; fuel-exhaustion reference
  mission
Owner:         Martin
Status:        Open
```

### L0-ASM-120

```asm
ID:            L0-ASM-120
Assumption:    The crew is represented by an interactive operator of the STP or by an automated test
  procedure, with no model of human performance.
Rationale:     Crew selections and annunciations are data items (L0-CON-170); test procedures play
  the crew so that autoflight can be verified unattended.
Affects:       L0-OBJ-030, L0-OBJ-070, L0-OBJ-080, L0-CON-170; autoflight annunciation requirements
Owner:         Martin
Status:        Open
```

### L0-ASM-130

```asm
ID:            L0-ASM-130
Assumption:    Parallel test campaigns run on the CPU cores of a single execution host.
Rationale:     OBJECTIVES §3 speaks of the available CPU resources; a single multi-core host is the
  simplest reading and fixes the reference for the parallel-efficiency criterion. A distributed
  cluster would need a change request.
Affects:       L0-OBJ-090, L0-SUC-050, L0-SUC-060; STP execution architecture
Owner:         Martin
Status:        Open
```

### L0-ASM-140

```asm
ID:            L0-ASM-140
Assumption:    The project can enforce information separation by keeping the protected design
  material in workspaces that the reverse-engineering agents cannot read.
Rationale:     The blind experiment depends on access control that the project can apply and record
  (REVERSE_ENGINEERING §7). If workspace separation proves insufficient, the separation constraints
  need another means.
Affects:       L0-CON-220, L0-CON-250, L0-SUC-140; reverse-engineering effort requirements
Owner:         Martin
Status:        Open
```
