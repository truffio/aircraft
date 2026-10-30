# A1 — Interface needs

L0 sets no interface details; these are the interfaces the L0 records imply, for B1 (L1 architecture) and I1 (ICDs).

| ID | From → To | Need | Driven by | Proposed home |
| --- | --- | --- | --- | --- |
| IN-A1-01 | AER → TST | Identity of the Aeronef configuration in each run: vehicle model version, flight-control-law design and version, autoflight implementation and version, parameter set. Recorded with each run. | L0-OBJ-110, L0-SUC-040 | ICD-AER-TST |
| IN-A1-02 | TST → AER | Configuration-time selection of the flight-control-law design and the autoflight implementation, without modifying the vehicle model. | L0-CON-200, L0-CON-210 | ICD-AER-TST |
| IN-A1-03 | TST (operator or test procedure) → AER | Crew interface as data: mode selections and target selections in crew-facing units. | L0-CON-170, L0-CON-270, L0-ASM-120 | ICD-AER-TST |
| IN-A1-04 | AER → TST | Annunciations and operational data (time-stamped crew inputs, mode changes, control activity, vehicle state), each signal classified releasable or protected. | L0-OBJ-140 | ICD-AER-TST (TM, C7) |
| IN-A1-05 | TST → RVS | Released evidence package: released operational data, black-box access to the executable simulation, with a release record. | L0-OBJ-160 (L0-CON-220, -230 deleted) | Deferred with the RVS (D44, #69) |
| IN-A1-06 | AER, TST → RVS | Operational manuals and procedures, versioned against a requirements baseline. | L0-OBJ-150 | Evidence-package ICD |
| IN-A1-07 | AER → TST | True vehicle state to the control functions and to recording (perfect knowledge). | L0-ASM-010 | ICD-AER-TST, ICD-NAV-AF |
