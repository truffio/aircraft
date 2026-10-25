## SUC — Success criteria (L0-SUC)

### L0-SUC-010

```req
ID:            L0-SUC-010
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall baseline the Aeronef requirements down to the last
  requirement layer of each branch with no open major review findings.
Rationale:     Success criterion 1 of OBJECTIVES §6: a coherent fictional vehicle with defined
  dynamics, control laws and autoflight behaviour. The baselined requirement set, reviewed at gate
  G4 and tagged AER-REQ-baseline-1, is the definition of that vehicle.
Parent(s):     —
Source:        OBJECTIVES.md §6; AIRCRAFT_REQUIREMENTS_PLAN.md §6 (G4)
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the baseline tag exists, and the gate review
  record lists no open major finding.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       1
```

### L0-SUC-020

```req
ID:            L0-SUC-020
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall achieve a passing verification result for each baselined
  Aeronef requirement.
Rationale:     Coherence is shown by verification: the design meets its own requirements (OBJECTIVES
  §6, criteria 1 and 2). The reference configuration (glossary) is the Aeronef
  configuration designated for verification; alternative configurations may fail
  performance requirements, and that result is comparison data, not a project failure.
  G0 owner review (2026-10-25): every requirement defined along the way is verified,
  not a fraction of them. Each one has a verification procedure that is executed
  successfully (D26). The reference-configuration wording is dropped, since there is
  one configuration. The owner added that coverage is 100%: every requirement is
  verified by the method chosen for it (test, demonstration, analysis or inspection), and every
  verification passes (D39). A higher-level requirement passes when all its children have passed
  and the decomposition has been reviewed (D40).
Parent(s):     —
Source:        OBJECTIVES.md §6
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the verification matrix shows a passing last
  result for every baselined Aeronef requirement.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-030

```req
ID:            L0-SUC-030
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall verify each Aeronef requirement whose verification method
  is Test with an automated test procedure.
Rationale:     Success criterion 2 of OBJECTIVES §6: behaviour and performance verified through
  repeatable, automatically assessed tests (METHODOLOGY §4.3 example).
Parent(s):     —
Source:        OBJECTIVES.md §6; METHODOLOGY.md §4.3
Allocated to:  STP, AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the verification matrix links each Aeronef
  requirement whose method is Test to an automated test procedure that has a recorded result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       1
```

### L0-SUC-040

```req
ID:            L0-SUC-040
Level:         L0
Type:          Performance
Statement:     When a recorded test run is re-executed with its recorded configuration, software
  version and inputs, the Aeronef project shall obtain the same verification result as
  the recorded run.
Rationale:     Success criterion 2 of OBJECTIVES §6 requires repeatable tests; L0-OBJ-110 requires
  reproducible runs. The tolerance is a parameter so that the owner can choose between
  bit-identical reproduction on the same host and a tolerance across hosts (issues.md,
  Q-A1-05). It rests on L0-ASM-020. G0 owner review (2026-10-25): runs are not checked
  for bit-identical outputs; a repeated run must give the same expected result (D25).
Parent(s):     —
Source:        OBJECTIVES.md §3, §6; TESTING_ENVIRONMENT.md §5
Allocated to:  STP
Criticality:   Not assessed
Verification:  Test — TBD; success criteria: re-execution of a sample of recorded runs gives, for
  each run, the same pass or fail result against the same expected results as the
  recorded run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-050

```req
ID:            L0-SUC-050
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall execute an automated test campaign as a single batch
  without operator action.
Rationale:     Success criterion 2 of OBJECTIVES §6 calls for large-scale parallel campaigns;
  TESTING_ENVIRONMENT §5 asks the platform to scale to high test volumes. The campaign
  size makes 'large-scale' measurable. G0 owner review (2026-10-25): accepted without a
  campaign size. A campaign is as big as it needs to be (#68).
Parent(s):     —
Source:        OBJECTIVES.md §3, §6; TESTING_ENVIRONMENT.md §5, §6
Allocated to:  STP
Criticality:   Not assessed
Verification:  Test — TBD; success criteria: a campaign is launched once, completes without operator
  action, and records a result for each run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-060

```req
ID:            L0-SUC-060
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall achieve a parallel efficiency of at least [P-SYS-060] when
  a test campaign runs on [P-SYS-070] parallel simulation instances.
Rationale:     Scalable parallelism across the available CPU resources is an objective (OBJECTIVES
  §3; TESTING_ENVIRONMENT §5). Parallel efficiency (glossary) is the single-instance
  campaign duration divided by the product of the parallel campaign duration and the
  number of instances, which makes scaling measurable. G0 owner review (2026-10-25):
  deferred. Scaling up the testing effort and running in parallel is a future
  expansion. It will be done, but not in version 1, and the project does not have to
  scale from its first instances (#86, #68).
Parent(s):     —
Source:        OBJECTIVES.md §3, §6; TESTING_ENVIRONMENT.md §5
Allocated to:  STP
Criticality:   Not assessed
Verification:  Test — TBD; success criteria: the same campaign is timed on one instance and on
  [P-SYS-070] instances on the execution host, and the computed parallel efficiency is at least
  [P-SYS-060].
Parameters:    P-SYS-060, P-SYS-070
TBD/TBR:       P-SYS-060 value TBR (proposed 0.8), Martin, 2026-12-31; P-SYS-070 value TBR (proposed
  8, the physical core count of the execution host), Martin, 2026-12-31
Owner:         Martin
Status:        Draft
Version:       2
```

### L0-SUC-070

```req
ID:            L0-SUC-070
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall demonstrate parallel batch execution for each of the
  following test categories: functional and logic tests, mode-transition tests, performance tests
  and statistical campaigns.
Rationale:     OBJECTIVES §3 states that any test procedure, not only Monte Carlo experiments, must
  run in parallel instances, and names these categories. Demonstrating each category
  shows that parallelism is not tied to one kind of test (TESTING_ENVIRONMENT, core
  principle). G0 owner review (2026-10-25): deferred. Scaling up the testing effort and
  running in parallel is a future expansion. It will be done, but not in version 1, and
  the project does not have to scale from its first instances (#86, #68).
Parent(s):     —
Source:        OBJECTIVES.md §3, §6; TESTING_ENVIRONMENT.md §5, §6
Allocated to:  STP
Criticality:   Not assessed
Verification:  Demonstration — TBD; success criteria: a batch containing procedures of each listed
  category runs in parallel simulation instances and records a result for each procedure.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L0-SUC-080

```req
ID:            L0-SUC-080
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall compare at least [P-SYS-010] flight-control-law designs by
  executing the same test procedures on each under identical initial conditions.
Rationale:     G0 owner review (2026-10-25): deleted. Only one flight-control design is developed to
  start with. The flight controls may be iterated later, but comparing designs is not a
  goal of the project. Original rationale: Success criterion 3 of OBJECTIVES §6:
  compare alternative implementations under equivalent test conditions. The count is
  the one set by L0-OBJ-040.
Parent(s):     —
Source:        OBJECTIVES.md §6; TESTING_ENVIRONMENT.md §7
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: a comparison report shows, for at least
  [P-SYS-010] flight-control-law designs, results from the same set of procedures with identical
  initial conditions.
Parameters:    P-SYS-010
TBD/TBR:       P-SYS-010 value TBR (proposed 2), Martin, 2026-11-30
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-SUC-090

```req
ID:            L0-SUC-090
Level:         L0
Type:          Functional
Statement:     The Aeronef project shall compare at least [P-SYS-020] autoflight implementations by
  executing the same test procedures on each under identical initial conditions.
Rationale:     G0 owner review (2026-10-25): deleted. One autoflight implementation (D24); there is
  nothing to compare. Original rationale: Success criterion 3 of OBJECTIVES §6, for
  autoflight. The count is the one set by L0-OBJ-050.
Parent(s):     —
Source:        OBJECTIVES.md §6; TESTING_ENVIRONMENT.md §7
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: a comparison report shows, for at least
  [P-SYS-020] autoflight implementations, results from the same set of procedures with identical
  initial conditions.
Parameters:    P-SYS-020
TBD/TBR:       P-SYS-020 value TBR (proposed 2), Martin, 2026-11-30
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-SUC-100

```req
ID:            L0-SUC-100
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall obtain a reconstructed model that identifies each
  autoflight mode in the baselined autoflight mode catalogue.
Rationale:     Success criterion 4 of OBJECTIVES §6 asks for meaningful aspects of behaviour to be
  reconstructed; REVERSE_ENGINEERING §6 names the accuracy of identified functions and
  operating modes as the first assessment dimension. The scoring rule is defined in the
  reverse-engineering effort requirements. G0 owner review (2026-10-25): the target is
  100% coverage of the functionality: every mode is identified.
Parent(s):     —
Source:        OBJECTIVES.md §4, §6; REVERSE_ENGINEERING.md §6
Allocated to:  REE
Criticality:   Not assessed
Verification:  Analysis — TBD; success criteria: the evaluators score the reconstructed model
  against the protected mode catalogue, and every catalogue mode is identified.
Parameters:    —
TBD/TBR:       Scoring rule TBD in the reverse-engineering requirements (#69), Martin
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-110

```req
ID:            L0-SUC-110
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall obtain a reconstructed model that reproduces each
  autoflight mode transition defined in the protected autoflight mode logic.
Rationale:     REVERSE_ENGINEERING §6 names the accuracy of inferred logic, state transitions and
  conditions. A transition counts as reproduced when its source mode, destination mode
  and triggering condition match the protected mode logic; the detailed scoring rule is
  defined in the reverse-engineering effort requirements. G0 owner review (2026-10-25):
  100% coverage: every mode transition is reproduced.
Parent(s):     —
Source:        OBJECTIVES.md §4, §6; REVERSE_ENGINEERING.md §6
Allocated to:  REE
Criticality:   Not assessed
Verification:  Analysis — TBD; success criteria: the evaluators score each transition of the
  protected mode logic, and every transition is reproduced.
Parameters:    —
TBD/TBR:       Scoring rule TBD in the reverse-engineering requirements (#69), Martin
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-120

```req
ID:            L0-SUC-120
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall obtain a reconstructed model that predicts the observed
  outcome of each assessment scenario withheld from the reverse-engineering effort.
Rationale:     The assessment must distinguish a model that reproduces observed examples from one
  that generalises (REVERSE_ENGINEERING §6). Withheld assessment scenarios (glossary)
  test prediction in unseen situations. The definition of a correct prediction and its
  tolerance are set in the reverse-engineering effort requirements. G0 owner review
  (2026-10-25): 100% coverage: the outcome of every withheld scenario is predicted.
Parent(s):     —
Source:        OBJECTIVES.md §4, §6; REVERSE_ENGINEERING.md §6
Allocated to:  REE
Criticality:   Not assessed
Verification:  Analysis — TBD; success criteria: the evaluators compare the predictions of the
  reconstructed model with the simulated outcomes of the withheld scenarios, and every
  outcome is predicted correctly.
Parameters:    —
TBD/TBR:       Definition of a correct prediction TBD in the reverse-engineering requirements (#69),
  Martin
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-130

```req
ID:            L0-SUC-130
Level:         L0
Type:          Performance
Statement:     The Aeronef project shall obtain a reconstructed model that covers each baselined
  Aeronef system requirement.
Rationale:     REVERSE_ENGINEERING §6 names coverage of important behaviours as an assessment
  dimension, and METHODOLOGY §11.2 makes the manual trace register the answer key for
  scoring the reconstruction. Aeronef system requirements are the L1 Aeronef
  requirements. G0 owner review (2026-10-25): full coverage. Every coverage criterion
  is 100%, not a fraction (D39).
Parent(s):     —
Source:        OBJECTIVES.md §4, §6; REVERSE_ENGINEERING.md §6; METHODOLOGY.md §11.2
Allocated to:  REE
Criticality:   Not assessed
Verification:  Analysis — TBD; success criteria: the evaluators score the reconstructed model
  against the manual trace register, and every baselined Aeronef system (L1)
  requirement is covered.
Parameters:    —
TBD/TBR:       Scoring rule TBD in the reverse-engineering requirements (#69), Martin
Owner:         Martin
Status:        Reviewed
Version:       2
```

### L0-SUC-140

```req
ID:            L0-SUC-140
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall complete the reverse-engineering effort with no recorded
  access by a reverse-engineering agent to the protected design material.
Rationale:     Success criterion 4 of OBJECTIVES §6 requires reconstruction without access to the
  original design. A reconstruction made after a leak is not evidence for the
  experiment, so the absence of access is itself a success criterion
  (REVERSE_ENGINEERING §7). G0 owner review (2026-10-25): deferred with the rest of the
  reverse-engineering work (#69). The constraints it rested on (L0-CON-220 to -240)
  were deleted, and L0-CON-250 is deferred. Stays Draft.
Parent(s):     —
Source:        OBJECTIVES.md §4, §6; REVERSE_ENGINEERING.md §2, §7
Allocated to:  REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the access records of each reverse-engineering
  agent for the whole effort show no read of an item of protected design material.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       2
```

### L0-SUC-150

```req
ID:            L0-SUC-150
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall pass the automated trace check at each baseline with no
  orphan requirements, no childless parent requirements and no requirements without a verification
  method.
Rationale:     Success criterion 5 of OBJECTIVES §6: a reviewed, traceable chain from objectives
  through requirements, design artifacts and tests. METHODOLOGY §10.4 defines the automated checks.
Parent(s):     —
Source:        OBJECTIVES.md §5, §6; METHODOLOGY.md §10.4
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the trace check output stored with each baseline
  reports no orphan, no childless parent and no requirement without a verification method.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       1
```

### L0-SUC-160

```req
ID:            L0-SUC-160
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall trace each released operational manual section to at least
  one baselined requirement in the protected manual trace register.
Rationale:     G0 owner review (2026-10-25): deleted. Traceability is wanted and kept (L0-OBJ-190),
  and the owner prefers no gaps. But the project does not have to be certifiable, and
  imperfect traceability would not make the result a failure, so it is not a success
  criterion. Original rationale: Success criterion 5 of OBJECTIVES §6 extends the chain
  to the manuals, and METHODOLOGY §11.2 (rule 2) keeps that trace in a register outside
  the released manual, where it serves as the answer key for scoring the
  reconstruction.
Parent(s):     —
Source:        OBJECTIVES.md §5, §6; METHODOLOGY.md §10.4, §11.2
Allocated to:  AER, STP
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each section of each released manual appears in
  the manual trace register with at least one baselined requirement ID.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-SUC-170

```req
ID:            L0-SUC-170
Level:         L0
Type:          Documentation
Statement:     The Aeronef project shall issue a final test report that records the result of each
  verification procedure performed against the requirements of each level.
Rationale:     Success criteria state what 'done' means for each objective so that L0 itself can be
  validated at the end (METHODOLOGY §4.4). OBJECTIVES §6 names the intended outcome: a
  functioning model and a practical assessment of the methods (L0-OBJ-210). G0 owner
  review (2026-10-25): the final report is the report of completion: every test
  performed, against all levels of requirements and all the verification procedures
  defined. The assessment of the methods stays an objective (L0-OBJ-210).
Parent(s):     —
Source:        OBJECTIVES.md §6; METHODOLOGY.md §4.4
Allocated to:  AER, STP, REE
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the report lists every verification procedure,
  the requirements of each level it verifies and its last result.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Reviewed
Version:       2
```
