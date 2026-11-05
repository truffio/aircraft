# Design decisions register

Design decisions (DD-nnn) behind derived requirements. Plan-level decisions D1–D63 are in AIRCRAFT_REQUIREMENTS_PLAN.md §9.

| ID | Decision | Alternatives considered | Rationale | Derived requirements | Date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DD-010 | The flight software (FCP, NAV, AF, FC) runs once per control frame of fixed period, an integer multiple of the simulation step, in the order FCP → NAV → AF → FC (FUNCTIONAL_ANALYSIS §4.2). | Execute at every simulation step; asynchronous or event-driven execution. | A whole number of steps per frame keeps sampling exact on the CV-840 time base and decouples the integration step (accuracy) from the software rate. Execution at every step ties the two; asynchronous execution breaks reproducibility (L1-AER-690, D59). | L1-AER-680 | 2026-11-04 | Accepted (G1) |
| DD-020 | The control-loop latency is bounded at aircraft level and split into one control frame plus the effector command response time. | No latency requirement (leave it to C4); a separate budget per axis. | A single number lets C3 (effector response) and C4 (control-law margins) size against the same budget (METHODOLOGY §7 rule 4). Per-axis budgets are a C4 refinement if needed. | L1-AER-710 | 2026-11-04 | Accepted (G1) |
