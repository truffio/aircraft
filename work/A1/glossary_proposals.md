# A1 — Glossary proposals

Terms used in the L0 requirements. A3 owns the glossary; these are proposals to merge or reconcile with A3's definitions.

| Term | Proposed definition | Used in |
| --- | --- | --- |
| Aeronef project | The project of interest at L0: design of the Aeronef, the Simulation and Testing Platform and the Reverse-Engineering Effort. Subject of every L0 requirement. | All L0 records |
| Aeronef configuration | One flight-control-law design and one autoflight implementation, running on the same vehicle model. | L0-OBJ-100, L0-SUC-020 |
| Reference configuration | The Aeronef configuration designated by the project owner for verification of the Aeronef requirements. | L0-SUC-020, L0-OBJ-020 |
| Flight-control-law design | One design of the flight-control function's control laws, replaceable without modifying the vehicle model. | L0-OBJ-040, L0-CON-200, L0-SUC-080 |
| Autoflight implementation | One implementation of the autoflight functions (mode logic and guidance), replaceable without modifying the vehicle model. | L0-OBJ-050, L0-CON-210, L0-SUC-090 |
| Force effector | A fictional, gravity-like force emitter that produces a commanded force or moment on the Aeronef in a fixed direction relative to the body, consuming fuel. Characterised by control effectiveness, limits and fuel consumption. | L0-CON-060, -070, -080, -100 |
| Control force / control moment | A force or moment on the Aeronef other than gravity and aerodynamic drag; produced only by the force effectors. | L0-CON-060 |
| Degree of freedom | One independent coordinate of rigid-body motion: translation along, or rotation about, one of three axes. The Aeronef has six. | L0-OBJ-020, L0-CON-010, -020, -030 |
| Centre of gravity | Spelling note: METHODOLOGY uses British spelling ("centre", "behaviour", "modelled"); AIRCRAFT_CHARACTERISTICS uses "center". A1 follows METHODOLOGY. A3 to fix one spelling project-wide. | L0-CON-130 |
| Crew-facing quantity | A quantity that the crew selects or that is annunciated to the crew. Stated in crew-facing units (D7); every other quantity is in SI units. | L0-CON-260, L0-CON-270 |
| Crew-facing unit | The unit of plan decision D7 for a crew-facing quantity: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track, flight path angle, radial). | L0-CON-270 |
| Crew interface | The data exchanged between the crew and the Aeronef: mode selections, target selections and annunciations. No physical controls or display formats are modelled. | L0-CON-170 |
| Automated test procedure | A procedure that sets initial conditions, applies stimuli, records results and assesses observed outcomes against expected outcomes, without operator action. | L0-OBJ-080, L0-OBJ-090, L0-SUC-030 |
| Test run | One execution of one automated test procedure (or one interactive session) in one simulation instance. | L0-OBJ-120, L0-SUC-040 |
| Test campaign | A set of test runs launched together as one batch. | L0-OBJ-130, L0-SUC-050, L0-SUC-060 |
| Simulation instance | One isolated, independently started copy of the simulation, running one test run at a time. | L0-OBJ-090, L0-SUC-060 |
| Execution host | The single computer whose CPU cores run the simulation instances of a campaign (L0-ASM-130). | L0-OBJ-090, L0-CON-190, L0-SUC-060 |
| Parallel efficiency | Single-instance campaign duration divided by (parallel campaign duration × number of parallel instances). Dimensionless. | L0-SUC-060 |
| Test category | One of: functional and logic tests, mode-transition tests, performance tests, statistical campaigns (OBJECTIVES §3). | L0-SUC-070 |
| Operational data | Time-stamped data output by the Aeronef describing crew inputs, autoflight mode changes, control activity and vehicle responses. Each signal is classified releasable or protected. | L0-OBJ-140, L0-CON-230, L0-CON-240 |
| Protected design material | The closed set withheld from the reverse-engineering effort: requirements, design specifications, the model specification, the parameter database, the interface control documents, implementation and source code, ground-truth test expectations, assessment answers and the manual trace register. | L0-CON-220, -250, L0-SUC-140 |
| Protected design baseline | The baselined requirements and design against which the reconstructed model is assessed. Part of the protected design material. | L0-OBJ-170 |
| Released evidence | The material given to the reverse-engineering effort: operational manuals and procedures, black-box access to the executable simulation, and released operational data. | L0-OBJ-160, L0-CON-230, L0-CON-240 |
| Evidence package | One versioned release of released evidence, with a release record listing its items. | L0-CON-220, L0-CON-230 |
| Black-box access | Running and stimulating the executable simulation through its operator interface, without access to source code or internal state. | L0-CON-230 |
| Reconstructed model | The reverse-engineering effort's inferred description of the Aeronef's functions, operating modes, mode transitions and control logic, each element citing the evidence it rests on. | L0-OBJ-160, -170, L0-SUC-100 to -130 |
| Withheld assessment scenario | A scenario defined by the evaluators and not shown to the reverse-engineering effort, used to test whether the reconstructed model predicts unseen behaviour. | L0-SUC-120 |
| Manual trace register | The protected register tracing each operational manual section to the requirements it describes; the answer key for scoring the reconstruction (METHODOLOGY §11.2). | L0-SUC-130, L0-SUC-160 |
| Evaluator | A project team member on the protected side who assesses the reconstructed model; not a reverse-engineering agent. | L0-OBJ-170, L0-SUC-100 to -130 |
| Autoflight mode catalogue | The baselined list of autoflight modes (initially plan decision D3). | L0-OBJ-030, L0-SUC-100 |
| Major review finding | A review finding classed Major in the METHODOLOGY §13.4 record. | L0-SUC-010 |
| Orphan requirement / childless parent | Trace-check terms (METHODOLOGY §10.4): a requirement below L0 with no parent and no Derived flag; a requirement with no child at the next level where one is expected. | L0-SUC-150 |
