# A1 — Interface needs

L0 sets no interface details; these are the interfaces the L0 records imply, for B1 (L1 architecture) and I1 (ICDs).

| ID | From → To | Need | Driven by | Proposed home |
| --- | --- | --- | --- | --- |
| IN-A1-01 | AER → STP | Identity of the Aeronef configuration in each run: vehicle model version, flight-control-law design and version, autoflight implementation and version, parameter set. Recorded with each run. | L0-OBJ-100, L0-OBJ-110, L0-SUC-040 | ICD-AER-STP |
| IN-A1-02 | STP → AER | Configuration-time selection of the flight-control-law design and the autoflight implementation, without modifying the vehicle model. | L0-CON-200, L0-CON-210 | ICD-AER-STP |
| IN-A1-03 | STP (operator or test procedure) → AER | Crew interface as data: mode selections and target selections in crew-facing units. | L0-CON-170, L0-CON-270, L0-ASM-120 | ICD-AER-STP |
| IN-A1-04 | AER → STP | Annunciations and operational data (time-stamped crew inputs, mode changes, control activity, vehicle state), each signal classified releasable or protected. | L0-OBJ-140, L0-CON-240 | ICD-AER-STP (TM, C7) |
| IN-A1-05 | STP → REE | Released evidence package: released operational data, black-box access to the executable simulation, with a release record. | L0-CON-220, L0-CON-230 | New ICD for the evidence package (see issues.md, Q-A1-12) |
| IN-A1-06 | AER, STP → REE | Operational manuals and procedures, versioned against a requirements baseline. | L0-OBJ-150, L0-CON-240 | Evidence-package ICD |
| IN-A1-07 | AER → STP | True vehicle state to the control functions and to recording (perfect knowledge). | L0-ASM-010 | ICD-AER-STP, ICD-NAV-AF |
