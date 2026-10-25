## OBJ — Objectives (L0-OBJ)

### L0-OBJ-010

```req
ID:            L0-OBJ-010
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide an executable dynamics model of the Aeronef that
  conforms to a baselined model specification.
Rationale:     Objective 1 asks for a deliberately simplified fictional vehicle whose behaviour is
  fully understood. For a simulated vehicle the physics is the requirement (METHODOLOGY §7), so the
  vehicle is delivered as an executable model held to a model specification (MS-DYN) that can be
  verified by analysis against independent solutions. The modelling boundaries are the L0-CON
  constraints.
Parent(s):     —
Source:        OBJECTIVES.md §1 (objective 1), §2; AIRCRAFT_CHARACTERISTICS.md §2, §4
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the model specification is baselined, and each
  Aeronef model-fidelity requirement traces to this objective and has a passing verification result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-020

```req
ID:            L0-OBJ-020
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall develop a flight-control function that regulates the motion
  of the Aeronef in each of its six degrees of freedom.
Rationale:     Objective 1 names flight control as one of the three parts of the Aeronef the project
  designs. Flight control closes the loop between the autoflight references and the force effectors,
  and it is the layer at which alternative control laws are compared (L0-OBJ-040). Independence of
  the degrees of freedom is constrained by L0-CON-020.
Parent(s):     —
Source:        OBJECTIVES.md §1 (objective 1), §2; AIRCRAFT_CHARACTERISTICS.md §5
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the Aeronef system requirements allocate a
  regulation requirement to each of the six degrees of freedom, and each of them has a passing
  verification result in the reference configuration.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-030

```req
ID:            L0-OBJ-030
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall develop autoflight functions, adapted from airliner
  autoflight modes, as the primary means of operating the Aeronef.
Rationale:     Direct manual control of a vehicle with six independent degrees of freedom is
  expected to be impractical, so autoflight is developed first (OBJECTIVES §2,
  AIRCRAFT_CHARACTERISTICS §6). Airliner modes give an operating concept that a crew can follow from
  annunciations and that operational manuals can describe. The initial mode catalogue is fixed by
  plan decision D3; manual control is optional (L0-CON-180).
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §6; AIRCRAFT_REQUIREMENTS_PLAN.md §9 D3
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each mode in the baselined autoflight mode
  catalogue is covered by at least one Aeronef system requirement that traces to this objective.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-040

```req
ID:            L0-OBJ-040
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall develop at least [P-SYS-010] flight-control-law designs for
  the Aeronef.
Rationale:     The project develops and compares different flight-control laws (OBJECTIVES §2, §6).
  A comparison needs at least two designs; the count is a parameter so that the project owner can
  raise it without rewording the requirement.
Parent(s):     —
Source:        OBJECTIVES.md §2, §6; AIRCRAFT_CHARACTERISTICS.md §5
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the design descriptions record at least
  [P-SYS-010] distinct flight-control-law designs, each of which runs in the STP as part of an
  Aeronef configuration.
Parameters:    P-SYS-010
TBD/TBR:       P-SYS-010 value TBR (proposed 2), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-050

```req
ID:            L0-OBJ-050
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall develop at least [P-SYS-020] autoflight implementations for
  the Aeronef.
Rationale:     The project develops and compares different autoflight implementations (OBJECTIVES
  §2, §6). As for control laws, the count is a parameter.
Parent(s):     —
Source:        OBJECTIVES.md §2, §6
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the design descriptions record at least
  [P-SYS-020] distinct autoflight implementations, each of which runs in the STP as part of an
  Aeronef configuration.
Parameters:    P-SYS-020
TBD/TBR:       P-SYS-020 value TBR (proposed 2), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-060

```req
ID:            L0-OBJ-060
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide a simulation and testing platform that executes the
  Aeronef model.
Rationale:     Objective 2. The Simulation and Testing Platform (STP) is the L1 element that runs
  the Aeronef and evaluates it against its requirements; it is the only means of exercising a
  vehicle that does not physically fly.
Parent(s):     —
Source:        OBJECTIVES.md §1 (objective 2), §3; TESTING_ENVIRONMENT.md §1, §2
Allocated to:  STP
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: the STP executes a run of the reference
  configuration from defined initial conditions and records the time histories of the vehicle state.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-070

```req
ID:            L0-OBJ-070
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide an interactive testing capability in which an
  operator applies commands to a running simulation and observes the response of the Aeronef.
Rationale:     OBJECTIVES §3 names interactive testing as one of the two uses of the environment. It
  is used to explore cause and effect and to understand system operation; it does not need a
  complete graphical flight simulator or a conventional manual piloting interface
  (TESTING_ENVIRONMENT §3).
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §3
Allocated to:  STP
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: an operator changes an autoflight mode
  selection during a running simulation, and the resulting change in vehicle state is presented to
  the operator during the same run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-080

```req
ID:            L0-OBJ-080
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide unattended execution of automated test procedures.
Rationale:     OBJECTIVES §3 names automated testing as the second use of the environment. An
  automated test procedure (glossary) sets the initial conditions, applies stimuli, records the
  results and assesses the observed outcomes against the expected outcomes; unattended execution is
  what makes requirement-based verification scale.
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §4
Allocated to:  STP
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: an automated test procedure runs from its
  initial conditions to a recorded pass or fail verdict without operator action.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-090

```req
ID:            L0-OBJ-090
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide parallel execution of each automated test procedure
  in independent simulation instances across the CPU cores of the execution host.
Rationale:     OBJECTIVES §3 requires that any test procedure, not only Monte Carlo experiments, can
  run in independent parallel simulation instances. Parallelism is therefore a property of the
  platform, not of one kind of test (TESTING_ENVIRONMENT, core principle). The execution host is
  described in L0-ASM-130.
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §5, §6
Allocated to:  STP
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: procedures from each test category of
  L0-SUC-070 run concurrently in separate simulation instances, and each produces the same results
  as its serial execution.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-100

```req
ID:            L0-OBJ-100
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall provide comparison of alternative Aeronef configurations
  under identical test procedures and initial conditions.
Rationale:     Comparing control laws and autoflight versions is a stated objective (OBJECTIVES §2,
  §3, §6; TESTING_ENVIRONMENT §7). An Aeronef configuration (glossary) is one flight-control-law
  design and one autoflight implementation on the same vehicle model; a comparison is meaningful
  only when both configurations see the same procedures and conditions.
Parent(s):     —
Source:        OBJECTIVES.md §3, §6; TESTING_ENVIRONMENT.md §7
Allocated to:  STP, AER
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: two Aeronef configurations run through the
  same set of procedures from identical initial conditions, and the STP reports the results of both
  configurations for each procedure.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-110

```req
ID:            L0-OBJ-110
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall make each simulation run reproducible from its recorded
  configuration, software version and inputs.
Rationale:     OBJECTIVES §3 asks for repeatable scenarios, and TESTING_ENVIRONMENT §5 for isolated,
  reproducible runs whose configuration, software version, inputs and results are identifiable.
  Reproducibility is what turns a test result into evidence and makes comparisons fair. It rests on
  L0-ASM-020; the measure is L0-SUC-040.
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §5
Allocated to:  STP
Criticality:   Not assessed
Verification:  Test — TBD; success criteria: L0-SUC-040 is met.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-120

```req
ID:            L0-OBJ-120
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall record the results of each test run in one results format
  defined by the STP.
Rationale:     OBJECTIVES §3 requires results in a consistent format. One format lets results be
  assessed automatically, compared across Aeronef configurations and analysed later by the
  reverse-engineering effort. The format itself is an STP design item.
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §8
Allocated to:  STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the recorded results of runs from each test
  category of L0-SUC-070 conform to the single results format defined by the STP.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-130

```req
ID:            L0-OBJ-130
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall produce a human-readable report for each test campaign.
Rationale:     OBJECTIVES §3 requires human-readable reports with enough data to understand outcomes
  and investigate deviations. TESTING_ENVIRONMENT §8 lists the content: procedures executed,
  conditions and versions used, observed outcomes and departures from expectations. The report
  format is specified in the STP requirements.
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §8
Allocated to:  STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the report of a campaign lists each executed
  procedure, the Aeronef configuration and software version used, the observed outcome and each
  departure from the expected outcome.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-140

```req
ID:            L0-OBJ-140
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall equip the Aeronef with an operational data output that
  relates crew inputs, autoflight mode changes, control activity and vehicle responses in time.
Rationale:     Objective 3 depends on operational data that let the reverse-engineering agents
  correlate inputs, actions, mode changes and vehicle responses (OBJECTIVES §4; REVERSE_ENGINEERING
  §3C, §5). The same data support requirement-based verification (TESTING_ENVIRONMENT §8). What the
  output may contain is constrained by L0-CON-240.
Parent(s):     —
Source:        OBJECTIVES.md §4; REVERSE_ENGINEERING.md §3C, §5; TESTING_ENVIRONMENT.md §8
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the operational data recorded for a run contain
  time-stamped records of crew inputs, autoflight mode changes, control activity and vehicle state.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-150

```req
ID:            L0-OBJ-150
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall produce human-oriented operational manuals and procedures
  for the Aeronef.
Rationale:     OBJECTIVES §4 and §5 require operational documents written for a human audience; they
  are the main documentary evidence for the reverse-engineering effort (REVERSE_ENGINEERING §3A).
  METHODOLOGY §11.2 lists the set: Vehicle Operating Manual, normal procedures, quick reference
  checklists and the STP user guide. Abnormal and emergency procedures are deferred with the hazard
  analysis. The manuals are written after the requirements baseline.
Parent(s):     —
Source:        OBJECTIVES.md §4, §5; REVERSE_ENGINEERING.md §3A; METHODOLOGY.md §11.2
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the Vehicle Operating Manual, the normal
  procedures, the quick reference checklists and the STP user guide exist, and each states the
  requirements baseline it describes.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-160

```req
ID:            L0-OBJ-160
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall conduct a reverse-engineering effort that produces a
  reconstructed model of the Aeronef from the released evidence.
Rationale:     Objective 3: evaluate whether independent AI agents can reconstruct the functional
  rules and control logic of the Aeronef from evidence instead of from its specifications. The
  reconstructed model (glossary) covers functions, operating modes, mode transitions and control
  logic. The released evidence is bounded by L0-CON-230.
Parent(s):     —
Source:        OBJECTIVES.md §1 (objective 3), §4; REVERSE_ENGINEERING.md §1, §4
Allocated to:  REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the reverse-engineering effort delivers a
  reconstructed model in which each element cites the released evidence it rests on.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-170

```req
ID:            L0-OBJ-170
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall assess the reconstructed model against the protected design
  baseline.
Rationale:     OBJECTIVES §4: project evaluators compare the inferred model with the original design
  and requirements to assess accuracy, coverage and limitations. The evaluators work on the
  protected side of the separation and are not reverse-engineering agents. REVERSE_ENGINEERING §6
  lists the assessment dimensions; L0-SUC-100 to L0-SUC-130 make them measurable.
Parent(s):     —
Source:        OBJECTIVES.md §4; REVERSE_ENGINEERING.md §6
Allocated to:  REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: an assessment report scores the reconstructed
  model against each of L0-SUC-100, L0-SUC-110, L0-SUC-120 and L0-SUC-130.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-180

```req
ID:            L0-OBJ-180
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall develop its requirements top-down in a hierarchy of levels
  rooted at the L0 requirements.
Rationale:     OBJECTIVES §5 prescribes a hierarchical, requirements-driven process: L0 for the
  mission, L1 for the Aeronef, the STP and the reverse-engineering effort, and as many lower levels
  as each element needs. Depth is decided per branch: decomposition stops when the next layer would
  be implementation (plan decision D4).
Parent(s):     —
Source:        OBJECTIVES.md §5; METHODOLOGY.md §3; AIRCRAFT_REQUIREMENTS_PLAN.md §9 D4
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each L1 element has one requirements
  specification, and each requirement below L0 has a level attribute and a parent or a Derived flag
  with its design decision.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-190

```req
ID:            L0-OBJ-190
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall maintain bidirectional traceability from the L0
  requirements through each lower-level requirement and its verification procedure to its
  verification result.
Rationale:     OBJECTIVES §5 requires traceability between parent and child requirements and between
  requirements and verification procedures; OBJECTIVES §6 asks for a traceable chain from objectives
  to findings. METHODOLOGY §10.4 defines the mandatory link types and the automated checks.
Parent(s):     —
Source:        OBJECTIVES.md §5, §6; METHODOLOGY.md §10.4
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: L0-SUC-150 is met.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-200

```req
ID:            L0-OBJ-200
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall peer review each engineering artifact before it is
  baselined.
Rationale:     OBJECTIVES §5 requires that engineering artifacts be subjected to peer review, and
  OBJECTIVES §6 asks for a reviewed chain. METHODOLOGY §11 assigns a review type to each artifact.
Parent(s):     —
Source:        OBJECTIVES.md §5, §6; METHODOLOGY.md §11.1, §11.3
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each baselined artifact has a review record in
  the METHODOLOGY §13.4 format whose exit decision is Baseline.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L0-OBJ-210

```req
ID:            L0-OBJ-210
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall produce a documented assessment of the AI-assisted methods
  used for system design, automated verification and evidence-based reverse engineering.
Rationale:     The purpose of the project is to evaluate AI-assisted engineering methods across the
  lifecycle, and its intended outcome is a practical assessment of those methods as well as a
  functioning model (OBJECTIVES §1, §6; REVERSE_ENGINEERING §8). L0-SUC-170 is the closing report.
Parent(s):     —
Source:        OBJECTIVES.md §1, §6; REVERSE_ENGINEERING.md §8
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the final assessment report of L0-SUC-170
  contains one assessment section for each of system design, automated verification and
  evidence-based reverse engineering.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
