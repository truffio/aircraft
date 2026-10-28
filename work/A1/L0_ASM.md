## ASM — Assumptions register

### L0-ASM-010

```asm
ID:            L0-ASM-010
Assumption:    The flight-control, autoflight and navigation functions receive the true simulated
  vehicle state, without sensor noise, bias or latency.
Rationale:     Perfect state knowledge keeps the first version focused on control laws and mode
  logic (METHODOLOGY §4.4, §5 F-AER-04). Sensor and estimation models can be added in a later
  version through a change request: sensor disturbances are planned as a future upgrade (#83).
  Confirmed by the owner at G0, 2026-10-25.
Affects:       L0-OBJ-020, L0-OBJ-030, L0-OBJ-140; Aeronef navigation, flight-control and autoflight
  subsystems; function F-AER-04
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-020

```asm
ID:            L0-ASM-020
Assumption:    Each simulation run is deterministic: one configuration, software version, input set
  and execution host produce identical outputs, and any random variation comes from a recorded
  random seed.
Rationale:     Determinism makes runs reproducible, and it lets statistical campaigns be replayed
  run by run (TESTING_ENVIRONMENT §5, §6).
Affects:       L0-OBJ-110, L0-SUC-040; STP execution and campaign generation
Owner:         Martin
Status:        Confirmed
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
Status:        Confirmed
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
Status:        Confirmed
```

### L0-ASM-050

```asm
ID:            L0-ASM-050
Assumption:    Wind is present and uniform: when a wind is applied, the same wind velocity exists
  everywhere in the operating volume. The test environment sets it for each run; there are no
  gusts or turbulence. Aerodynamic drag depends on the vehicle velocity relative to the air.
Rationale:     Owner decision D17 (#49): there is wind in the system, configurable in the test
  environment, and position hold compensates for it. A uniform wind is the simplest model; a
  refined wind model is planned for a future release (#84). With wind, the velocity through the
  air differs from the velocity over the ground; the conventions define both. Revised by the owner
  at G0, 2026-10-25.
Affects:       L0-CON-090; model specification (drag and wind model); navigation subsystem (track,
  horizontal speed, airspeed); STP (wind configuration); CONVENTIONS CV-470; CONOPS
  §4.2
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-060

```asm
ID:            L0-ASM-060
Assumption:    Air properties vary with altitude only and do not vary with time.
Rationale:     The drag model needs air density; a time-invariant, horizontally uniform atmosphere
  is the simplest model consistent with L0-ASM-050. Density follows the standard atmosphere
  (D20). Confirmed by the owner at G0, 2026-10-25.
Affects:       L0-CON-090; model specification (drag model)
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-070

```asm
ID:            L0-ASM-070
Assumption:    Each Aeronef component operates without failure in this development cycle.
Rationale:     Hazard and failure analysis is deferred by the project tailoring (METHODOLOGY,
  tailoring note). Fuel exhaustion and effector saturation are nominal behaviour, not failures.
  Failures will be introduced in a future version to study how the dynamics evolve (#85).
  Confirmed by the owner at G0, 2026-10-25.
Affects:       All L0 requirements; Criticality attribute; verification planning (no fault-injection
  cases)
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-080

```asm
ID:            L0-ASM-080
Assumption:    The Aeronef structure is rigid, and its fuel does not slosh.
Rationale:     Consistent with the rigid-body constraint L0-CON-010 and the fixed centre of gravity
  L0-CON-130.
Affects:       L0-CON-010, L0-CON-130; model specification; fuel and mass-properties subsystem
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-090

```asm
ID:            L0-ASM-090
Assumption:    Consumed fuel leaves the vehicle without imparting force or moment to it. Its only
  effect is the loss of mass: as fuel is consumed, the same effector force produces a larger
  acceleration (L0-CON-110).
Rationale:     The effectors are fictional gravity-like emitters, not reaction engines, so the mass
  flow of consumed fuel produces no thrust term in the equations of motion; the instantaneous mass
  alone changes (L0-CON-110). The owner stressed at G0 (2026-10-25) that the mass loss is a real
  effect on the dynamics.
Affects:       L0-CON-110; model specification (variable-mass equations of motion); fuel and
  mass-properties subsystem
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-100

```asm
ID:            L0-ASM-100
Assumption:    The operating environment contains no terrain, obstacles or other vehicles.
Rationale:     The project studies the control and mode logic of a single vehicle; the environment
  is free space above an altitude datum.
Affects:       Concept of operations scenarios; navigation subsystem; STP scenario definition
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-110

```asm
ID:            L0-ASM-110
Assumption:    Ground contact is an ideal landing. Contact with the ground within the landing
  envelope (limits on velocity and acceleration at contact) is a successful landing; contact outside
  the envelope is a crash that ends the run. No landing gear, bounce, friction or ground handling is
  modelled.
Rationale:     Owner decisions D8 and D37: the ground is at altitude zero on a flat Earth, and a
  landing model is required. An ideal landing keeps it to one envelope check. The envelope limits
  are parameters, set at a lower level. Revised by the owner at G0, 2026-10-25.
Affects:       L0-CON-090 (ground reaction), L0-CON-290, L0-CON-310; model specification (ground
  contact); STP run termination conditions; fuel-exhaustion reference mission;
  CONVENTIONS CV-420
Owner:         Martin
Status:        Confirmed
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
Status:        Confirmed
```

### L0-ASM-130

```asm
ID:            L0-ASM-130
Assumption:    Parallel test campaigns run on the CPU cores of a single execution host.
Rationale:     OBJECTIVES §3 speaks of the available CPU resources; a single multi-core host is the
  simplest reading and fixes the reference for the parallel-efficiency criterion. The working
  assumption is that a campaign that runs as independent instances on one host will scale;
  running on a CPU cluster, and assessing that scalability, comes at a later stage (#86).
  Confirmed by the owner at G0, 2026-10-25.
Affects:       L0-OBJ-090, L0-SUC-060; STP execution architecture
Owner:         Martin
Status:        Confirmed
```

### L0-ASM-140

```asm
ID:            L0-ASM-140
Assumption:    The project can enforce information separation by keeping the protected design
  material in workspaces that the reverse-engineering agents cannot read.
Rationale:     The blind experiment depends on access control that the project can apply and record
  (REVERSE_ENGINEERING §7). If workspace separation proves insufficient, the separation constraints
  need another means.
Affects:       L0-CON-250, L0-SUC-140; reverse-engineering effort requirements
Owner:         Martin
Status:        Confirmed
```
