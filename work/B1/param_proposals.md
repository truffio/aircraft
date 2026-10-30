# B1 — Parameter proposals

Parameters referenced by `work/B1/L1_AER.md` and `specs/FUNCTIONAL_ANALYSIS.md`. B2 seeds them. Field layout follows `parameters/PARAMETERS.yaml`. Values are `null` when TBD; a proposed value is marked TBR. Owner Martin for each.

**ID blocks.** B1 uses the free P-SYS block 400–590 for the L1 budgets (the PARAMETERS.yaml header reserves 010–190 for L0, 200–290 for the ConOps and 300–390 for the time base). Subsystem IDs proposed here are the budget shares that the L2 agents will own; they are numbered so as not to collide with the IDs the ConOps and conventions already use (P-AF-010 to -190, P-NAV-010 to -050, P-TM-010 to -070, P-DYN-010). C1 to C7 may renumber their own shares at L2, provided they update the L1 rationale that cites them through a change request.

## 1. New parameters

```yaml
parameters:
  # --- L1 budgets: effector authority (FUNCTIONAL_ANALYSIS §7.1) ---
  - id: P-SYS-400
    name: Minimum upward control force
    description: Control force the effector set can produce along the negative body z axis (up at level attitude), with the other five force and moment components at zero, while fuel remains. Budget - at least m_max x (P-DYN-010 + P-SYS-440) + drag at P-SYS-240.
    unit: N
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-120; FUNCTIONAL_ANALYSIS §7.1; computed at I1 once P-FU-010 and P-FU-030 are set
    owner: Martin
  - id: P-SYS-410
    name: Minimum control force, other body directions
    description: Control force the effector set can produce along each of +x_B, -x_B, +y_B, -y_B and +z_B, with the other five components at zero, while fuel remains. Budget - at least m_max x P-SYS-440 + drag at (P-SYS-230 + P-SYS-430 + P-SYS-560).
    unit: N
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-130; FUNCTIONAL_ANALYSIS §7.1
    owner: Martin
  - id: P-SYS-420
    name: Minimum control moment per body axis
    description: Control moment the effector set can produce about each body axis in each sense, with the other five components at zero, while fuel remains. Budget - at least J_max x angular acceleration to reach P-SYS-270 + drag moment + level-attitude margin.
    unit: N*m
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-140; FUNCTIONAL_ANALYSIS §7.1
    owner: Martin

  # --- L1 budgets: environment and envelope ---
  - id: P-SYS-430
    name: Maximum steady wind speed
    description: Largest steady horizontal wind speed at which the speed capability and the position-holding accuracy apply, with gusts of up to P-SYS-560 on top. The wind has no vertical component. Enters the effector authority budget through drag.
    unit: m/s
    value: 51.444
    tolerance: null
    note: 100 kt (owner, #99, D51).
    status: TBR
    source: L1-AER-130, -310, -460; D17, D51; #99
    owner: Martin
  - id: P-SYS-560
    name: Maximum gust speed
    description: Largest horizontal wind speed that gusts and bursts add to the steady wind (P-SYS-430). The largest instantaneous wind is P-SYS-430 + P-SYS-560. The gust shape (onset and duration) is defined in MS-DYN and set by the TST for each run.
    unit: m/s
    value: 25.722
    tolerance: null
    note: 50 kt (owner, #99, D51); 150 kt instantaneous with the steady wind.
    status: TBR
    source: L1-AER-130, -310, -460; L0-ASM-050; D51; #99
    owner: Martin
  - id: P-SYS-440
    name: Maximum vehicle acceleration magnitude
    description: Largest magnitude of the vehicle acceleration (time derivative of the vehicle velocity) while airborne with fuel remaining. Aircraft-level share of the crew budget; split into P-AF-200 (autoflight manoeuvre limit) and P-FC-020 (flight-control transient allowance).
    unit: m/s^2
    value: 14.709975
    tolerance: null
    note: 1.5 g (1.5 x 9.80665 m/s^2). With 1 g to hold the vehicle up, the sensed acceleration at the centre of gravity is at most 2.5 g, leaving 0.5 g of margin to the 3 g of P-SYS-120 (D45). Accepted as TBR (D48, #102).
    status: TBR
    source: L1-AER-300; D16, D38; FUNCTIONAL_ANALYSIS §7.2
    owner: Martin

  # --- L1 budgets: position error ---
  - id: P-SYS-450
    name: Position-holding error budget
    description: Largest distance between the vehicle position and the reference position while autoflight holds a fixed position, in a wind up to P-SYS-430, from P-SYS-460 after the start of the hold. Split into P-AF-160 (guidance) and P-FC-010 (translational regulation); navigation share zero (L1-AER-440).
    unit: m
    value: 1.0
    tolerance: null
    status: TBR
    source: L1-AER-460; METHODOLOGY §12 example; FUNCTIONAL_ANALYSIS §7.4
    owner: Martin
  - id: P-SYS-460
    name: Position-hold settling time
    description: Time from the start of a position hold after which the position-holding error budget applies. When the hold starts is set by the mode logic (#78, C5).
    unit: s
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-460
    owner: Martin

  # --- L1 budgets: timing ---
  - id: P-SYS-470
    name: Annunciation latency, aircraft level
    description: Longest time from a change of mode state, a target change or a fuel alert condition to its annunciation in the crew interface output. Budget - at least 2 x P-SYS-310 + P-TM-010; AF share P-AF-060.
    unit: s
    value: 0.5
    tolerance: null
    status: TBR
    source: L1-AER-470, -570, -580; FUNCTIONAL_ANALYSIS §7.5
    owner: Martin
  - id: P-SYS-480
    name: Control-loop latency
    description: Longest time from the simulation time of a vehicle state to the first change of effector output that responds to it. Budget - at least P-SYS-310 + P-EF-010.
    unit: s
    value: 0.1
    tolerance: null
    status: TBR
    source: L1-AER-710; DD-020; FUNCTIONAL_ANALYSIS §7.5
    owner: Martin

  # --- Landing envelope (L0-CON-290, D37) ---
  - id: P-SYS-500
    name: Landing envelope, maximum vertical speed magnitude
    description: Largest vertical speed magnitude at the ground-contact sample for the contact to be a landing.
    unit: m/s
    value: 3.458
    tolerance: null
    note: Impact speed of a free fall from 2 ft (0.6096 m), sqrt(2 x 9.80665 x 0.6096) (owner, #100).
    status: TBR
    source: L1-AER-280; #100
    owner: Martin
  - id: P-SYS-510
    name: Landing envelope, maximum horizontal speed
    description: Largest horizontal speed at the ground-contact sample for the contact to be a landing.
    unit: m/s
    value: 0.5
    tolerance: null
    status: TBR
    source: L1-AER-280; #100
    owner: Martin
  - id: P-SYS-520
    name: Landing envelope, maximum sensed acceleration
    description: Largest sensed acceleration magnitude at the ground-contact sample for the contact to be a landing. At most P-SYS-120 (L0-CON-310 guidance).
    unit: m/s^2
    value: 2.451663
    tolerance: null
    note: 1/4 g (owner, #100). Which acceleration it limits is asked in #100.1.
    status: TBR
    source: L1-AER-280; L0-CON-310; #100
    owner: Martin

  # --- Axis independence (L0-CON-020, -030) ---
  - id: P-SYS-540
    name: Cross-axis velocity tolerance
    description: Largest departure of the velocity along each translational axis from its reference while the reference of another degree of freedom changes.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-380
    owner: Martin
  - id: P-SYS-550
    name: Cross-axis body rate tolerance
    description: Largest departure of the body rate about each rotational axis from its reference while the reference of another degree of freedom changes.
    unit: rad/s
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-380
    owner: Martin

  # --- Fuel and mass properties (C2) ---
  - id: P-FU-030
    name: Dry mass
    description: Vehicle mass with no fuel. The maximum vehicle mass is P-FU-030 + P-FU-010.
    unit: kg
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-180, -360; FUNCTIONAL_ANALYSIS §7.3
    owner: Martin
  - id: P-FU-040
    name: Translational fuel consumption parameters
    description: Parameters of the translational consumption relationship (fuel mass flow per unit of control force). The form, and therefore the number of coefficients, is set by C2 in MS-DYN; the unit is that of a linear coefficient.
    unit: kg/(N*s)
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-170; L0-CON-120
    owner: Martin
  - id: P-FU-050
    name: Rotational fuel consumption parameters
    description: Parameters of the rotational consumption relationship (fuel mass flow per unit of control moment). Form set by C2 in MS-DYN.
    unit: kg/(N*m*s)
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-170; L0-CON-120
    owner: Martin
  - id: P-FU-060
    name: Fuel mass accounting tolerance
    description: Largest difference between the remaining fuel mass and the initial fuel mass minus the integral of the fuel mass flow (numerical integration only).
    unit: kg
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-190; METHODOLOGY §10.3
    owner: Martin

  # --- Geometry (C1) ---
  - id: P-DYN-400
    name: Crew station position
    description: Position of the crew station in the body frame (three components, x forward of the CG). The crew acceleration limit is evaluated at the centre of gravity, not here (D45).
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-250, -290; L0-CON-150
    owner: Martin

  # --- Budget shares owned by L2 subsystems ---
  - id: P-AF-200
    name: Autoflight manoeuvre acceleration limit
    description: Largest vehicle acceleration magnitude that autoflight guidance commands (D16 g-limited manoeuvres). Share of P-SYS-440.
    unit: m/s^2
    value: 9.80665
    tolerance: null
    note: 1.0 g
    status: TBR
    source: L1-AER-300; D16; FUNCTIONAL_ANALYSIS §7.2
    owner: Martin
  - id: P-FC-010
    name: Translational regulation position share
    description: Largest distance between the vehicle position and the autoflight reference position while a fixed position is held. Share of P-SYS-450.
    unit: m
    value: 0.5
    tolerance: null
    status: TBR
    source: L1-AER-460; FUNCTIONAL_ANALYSIS §7.4
    owner: Martin
  - id: P-FC-020
    name: Flight-control transient acceleration allowance
    description: Largest vehicle acceleration magnitude that flight-control transients may add to the commanded manoeuvre acceleration. Share of P-SYS-440.
    unit: m/s^2
    value: 4.903325
    tolerance: null
    note: 0.5 g
    status: TBR
    source: L1-AER-300; FUNCTIONAL_ANALYSIS §7.2
    owner: Martin
  - id: P-EF-010
    name: Effector command response time
    description: Longest time from a change of effector command to the effector output reaching the commanded value (definition of "reaching" set by C3). Share of P-SYS-480.
    unit: s
    value: null
    tolerance: null
    status: TBD
    source: L1-AER-710; FUNCTIONAL_ANALYSIS §7.5
    owner: Martin
```

## 2. Existing proposals that B1 uses, with value proposals or changes

These come from `work/A1`, `work/A2` and `work/A3`. B2 seeds them from there; B1 adds only the changes in the last column.

| ID | Source | Used by (L1) | B1 change |
| --- | --- | --- | --- |
| P-SYS-120 | A1 | L1-AER-280, -290 | None (3 g confirmed by the owner, #97, D45). |
| P-SYS-230, -240, -250, -260, -270, -280 | A2 | L1-AER-120 to -140, -310 to -360 | None. Values TBD; the owner sets the envelope (B1-Q07). |
| P-SYS-300 | A3 | L1-AER-670, -680 | Propose value 0.01 s, TBR. |
| P-SYS-310 | A3 | L1-AER-470, -680, -710 | Propose value 0.02 s, TBR. |
| P-TM-010 | A3 | L1-AER-470, -600 | Propose value 0.02 s (equal to P-SYS-310), TBR. |
| P-DYN-010 | A3 | L1-AER-060, -120, -290, -360 | Propose value 9.806 65 m/s² (standard gravity), TBR, so that the 3 g limit reads 1 g in a hover exactly (G0-F25, R-F06). |
| P-FU-010 | A2 | L1-AER-150, -180, -360, -570 | None (TBD). |
| P-FU-020 | A2 | L1-AER-570 | Propose value 0.1 (fraction of P-FU-010), TBR. |
| P-AF-060 | A2 | L1-AER-470 | Description: the AF share of P-SYS-470, at most P-SYS-470 − P-TM-010. |
| P-AF-160 | A2 | L1-AER-460 | **Changed meaning:** the AF guidance share of P-SYS-450 (reference position versus target), not the whole tolerance. Propose 0.5 m, TBR. CONOPS SC-090 then cites P-SYS-450 (issues N-B1-03). |
| P-AF-180 | A2 | L1-AER-390 | None (TBR, value set at C5). |
| P-NAV-050 | A3 | L1-AER-540 | None (TBR). |
| P-AF-070 | A2 | — | Not used. The FPA minimum-speed behaviour it supports was rejected by the owner (D13, #61; #89 item b). Recommend B2 does not seed it, or seeds it marked superseded for C5 to retire. |

## 3. TBD/TBR register entries to open (for B2)

| Item | Type | Location | Owner | Proposed closure |
| --- | --- | --- | --- | --- |
| Effector authority values | TBD | P-SYS-400, -410, -420 (L1-AER-120 to -140) | Martin | G2 (I1 budget closure) |
| Wind: steady 100 kt, gusts 50 kt (D51) | TBR | P-SYS-430, P-SYS-560 | Martin | G2 |
| Vehicle acceleration limit 1.5 g | TBR | P-SYS-440, P-AF-200, P-FC-020 | Martin | G1 |
| Position-holding budget 1 m and its split | TBR | P-SYS-450, P-AF-160, P-FC-010 | Martin | G1 |
| Position-hold settling time | TBD | P-SYS-460 | Martin | G2 (C5) |
| Timing budget | TBR | P-SYS-300, -310, -470, -480, P-TM-010 | Martin | G2 (I1) |
| Effector command response time | TBD | P-EF-010 | Martin | G2 (C3) |
| Landing envelope limits (2 ft fall, 0.5 m/s, 1/4 g; acceleration meaning #100.1) | TBR | P-SYS-500, -510, -520 | Martin | G1 (#100) |
| Cross-axis tolerances | TBD | P-SYS-540, -550 | Martin | G2 (C4) |
| Dry mass, consumption parameters, accounting tolerance | TBD | P-FU-030 to -060 | Martin | G2 (C2) |
| Crew station position | TBD | P-DYN-400 | Martin | G2 (C1) |
| Gravity value | TBR | P-DYN-010 | Martin | G1 |
| Low-fuel threshold 0.1 | TBR | P-FU-020 | Martin | G1 |
| Mode combinations | TBR | L1-AER-450 (#6) | Martin | G1 decision, G2 (C5) |
| Allocation of L0-OBJ-110 and L0-CON-190 to AER | TBR | L1-AER-690, -700 (CR-B1-01, -02) | Martin | G1 |
