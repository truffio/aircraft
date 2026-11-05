# C1 — Parameter proposals (DYN)

Proposals for `parameters/PARAMETERS.yaml` from task C1 (DYN, MS-DYN). The orchestrator merges them; C1 does not edit the database. The YAML block uses the database field layout. Existing IDs are reused where they exist (P-DYN-010, P-DYN-400, P-SYS-570). No withdrawn ID is used.

**P-DYN number blocks proposed.** 010–090 gravity and geometry; 100–190 aerodynamics; 200–290 model accuracy (credibility-check tolerances and horizon); 400 is the existing crew station (B1). 300–390 are left free.

**Values.** Every value below is a C1 proposal and is TBR unless it says otherwise; the owner sets or confirms them at G2. Tolerances are dimensionless ratios (CV-720: "1", written as a fraction).

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-DYN-010 | Value unchanged (9.80665). Status TBR → **Set** proposed at G2 (owner question C1-Q06). Source extended with MS-DYN §5.2. | Standard gravity is a definition; nothing in the L2 work argues for another value, and the crew budget reads exactly 1 g in a hover with it. |
| P-DYN-400 | Value null → `[4.0, 0.0, -1.0]` (TBR). Description: add "inside the capsule of P-DYN-020 and P-DYN-030, forward of the CG". | MS-DYN §2.3, L2-AER-DYN-240. |
| P-SYS-570 | Value null → `2.0` (TBD → TBR). Source extended with MS-DYN §5.4. | D62 asks C1 to set it at G2 with the TST wind model; rationale in MS-DYN §5.4 (owner question C1-Q04). |

## 2. YAML block

```yaml
  # --- DYN --- (C1 proposals; replaces the existing P-DYN-010 and P-DYN-400 entries)
  - id: P-DYN-010
    name: Gravitational acceleration
    description: Magnitude of the uniform gravitational acceleration along +z_L. Equal to standard gravity, so that the 3 g crew limit reads 1 g in a hover exactly. Not used by the standard atmosphere, whose own g_0 is a constant of that standard (MS-DYN §5.3).
    unit: m/s^2
    value: 9.80665
    tolerance: null
    status: TBR
    note: 'C1 proposes status Set at G2 (C1-Q06).'
    source: CV-110; L1-AER-060; L2-AER-DYN-120; MS-DYN §5.2; B1 proposal (G0-F25)
    owner: Martin
  - id: P-DYN-020
    name: Body overall length
    description: Overall length of the capsule body shape along the body x axis, nose to tail (MS-DYN §2.1). At least P-DYN-030.
    unit: m
    value: 12.0
    tolerance: null
    status: TBR
    source: 'L0-CON-140 (shape provisional, closes 2026-11-30); L1-AER-220; L2-AER-DYN-220; MS-DYN §2.1; C1 proposal (C1-Q05)'
    owner: Martin
  - id: P-DYN-030
    name: Body diameter
    description: Diameter of the capsule body shape, which is also the diameter of its two hemispherical ends (MS-DYN §2.1).
    unit: m
    value: 4.0
    tolerance: null
    status: TBR
    source: 'L0-CON-140 (shape provisional, closes 2026-11-30); L1-AER-220; L2-AER-DYN-220; MS-DYN §2.1; C1 proposal (C1-Q05)'
    owner: Martin
  - id: P-DYN-100
    name: Drag area
    description: Product of the drag coefficient and the reference area (C_D x A) of the isotropic quadratic drag model; drag = 0.5 x density x P-DYN-100 x airspeed x air-relative velocity, opposite to the air-relative velocity (MS-DYN §5.5, option D1). Zero gives the vacuum-equivalent configuration used by the credibility checks.
    unit: m^2
    value: 5.0
    tolerance: null
    status: TBR
    note: 'Estimate for a round-nosed capsule of P-DYN-020 x P-DYN-030 - C_D about 0.3 on the 12.6 m^2 frontal area gives 3.8 m^2, more in cross-flow (Hoerner, Fluid-Dynamic Drag, 1965). Confirmed at I1 with the authority budgets. If the owner chooses option D2 (C1-Q03), this entry is replaced by three per-axis drag coefficients.'
    source: L1-AER-070; L2-AER-DYN-130; MS-DYN §5.5; DD-C1-02; FUNCTIONAL_ANALYSIS §7.1
    owner: Martin
  - id: P-DYN-200
    name: Free-fall check tolerance
    description: Largest error of the simulated position and velocity in vacuum-equivalent free fall, relative to their change since the start of the check (MS-DYN check C-1).
    unit: '1'
    value: 1.0e-4
    tolerance: null
    status: TBR
    source: L1-AER-010, -060; L2-AER-DYN-600; MS-DYN §11; METHODOLOGY §10.3
    owner: Martin
  - id: P-DYN-210
    name: Terminal vertical speed check tolerance
    description: Largest difference between the settled vertical speed magnitude in a free fall with drag and the expected terminal value of MS-DYN check C-2, relative to that value. Also bounds the settled horizontal velocity error relative to the wind speed in the same check.
    unit: '1'
    value: 1.0e-3
    tolerance: null
    status: TBR
    source: L1-AER-010, -070; L2-AER-DYN-140, -610; MS-DYN §11; METHODOLOGY §10.3
    owner: Martin
  - id: P-DYN-220
    name: Torque-free rotation check tolerance
    description: Largest relative change of the angular momentum magnitude, change of its direction (rad) and relative change of the rotational kinetic energy over P-DYN-270 in a torque-free rotation (MS-DYN check C-3).
    unit: '1'
    value: 1.0e-4
    tolerance: null
    status: TBR
    source: L1-AER-010; L2-AER-DYN-620; MS-DYN §11; METHODOLOGY §10.3
    owner: Martin
  - id: P-DYN-230
    name: Quaternion norm tolerance
    description: Largest difference between the norm of the attitude quaternion and one, at each simulation step (MS-DYN check C-6).
    unit: '1'
    value: 1.0e-6
    tolerance: null
    status: TBR
    source: CV-250; L1-AER-010; L2-AER-DYN-060; MS-DYN §4.4, §11
    owner: Martin
  - id: P-DYN-240
    name: Variable-mass check tolerance
    description: Largest error of the simulated velocity under a prescribed constant control force and a prescribed decreasing mass, relative to its change since the start of the check (MS-DYN check C-4).
    unit: '1'
    value: 1.0e-4
    tolerance: null
    status: TBR
    source: L1-AER-010, -180; L2-AER-DYN-630; MS-DYN §11
    owner: Martin
  - id: P-DYN-250
    name: Rotation-during-translation check tolerance
    description: Largest error of the simulated horizontal velocity, relative to the initial horizontal speed, in a vacuum-equivalent free fall with a yaw rate, against the expected result for the option of #81.1 that MS-DYN records (MS-DYN check C-5).
    unit: '1'
    value: 1.0e-4
    tolerance: null
    status: TBR
    source: 'L1-AER-020; L2-AER-DYN-640; MS-DYN §4.5, §11; #81.1'
    owner: Martin
  - id: P-DYN-260
    name: Atmosphere density tolerance
    description: Largest difference between the density of the atmosphere model and the published table of the U.S. Standard Atmosphere 1976, relative to the table value, at the base altitude and the midpoint of each modelled layer (MS-DYN check C-7).
    unit: '1'
    value: 1.0e-4
    tolerance: null
    status: TBR
    source: D20; L1-AER-070; L2-AER-DYN-150; MS-DYN §5.3, §11
    owner: Martin
  - id: P-DYN-270
    name: Model accuracy horizon
    description: Simulation time over which the credibility-check tolerances P-DYN-220 and P-DYN-250 apply. At least the longest run; raised to P-SYS-280 if that is set longer.
    unit: s
    value: 3600.0
    tolerance: null
    status: TBR
    source: L1-AER-010; L2-AER-DYN-620, -640; MS-DYN §10.3, §11
    owner: Martin
  - id: P-DYN-400
    name: Crew station position
    description: Position of the crew station in the body frame (three components, x forward of the CG, z down), inside the capsule of P-DYN-020 and P-DYN-030 and forward of the CG. The crew acceleration limit is evaluated at the centre of gravity, not here (D45).
    unit: m
    value: [4.0, 0.0, -1.0]
    tolerance: null
    status: TBR
    source: L1-AER-250, -290; L0-CON-150; L2-AER-DYN-240; MS-DYN §2.3; C1 proposal
    owner: Martin

  # --- SYS --- (C1 update of the existing entry)
  - id: P-SYS-570
    name: Minimum gust rise time
    description: Shortest time over which a gust or burst builds up from the steady wind to its full speed, and decays back; the shape is the one-minus-cosine ramp of MS-DYN §5.4. Instantaneous wind steps are not allowed, so the drag changes at a bounded rate (at most (pi/2) x P-SYS-560 / P-SYS-570 for the wind) and the vehicle acceleration, position-holding and speed budgets close against it (D62).
    unit: s
    value: 2.0
    tolerance: null
    status: TBR
    note: 'C1 proposal (C1-Q04) - about the passage time of the longest FAR 25.341 gust gradient (350 ft, 107 m) at the steady wind P-SYS-430, and 20 times P-SYS-480. C4 confirms the gust shares of P-FC-020 and P-FC-010 against it at I1.'
    source: 'D62 (G1-F08); L1-AER-290, -300, -310, -460; L2-AER-DYN-410; MS-DYN §5.4 (C1)'
    owner: Martin
```

## 3. TBD/TBR register rows proposed (for `registers/TBD_TBR.md`)

| Item | Type | Location | Owner | Closure |
| --- | --- | --- | --- | --- |
| Body dimensions (with the provisional shape, L0-CON-140) | TBR | P-DYN-020, P-DYN-030 | Martin | 2026-11-30 |
| Drag area, and the drag form (C1-Q03) | TBR | P-DYN-100 | Martin | G2 (I1 budget closure) |
| Model accuracy tolerances and horizon | TBR | P-DYN-200 to P-DYN-270 | Martin | G2 |
| Crew station position proposed (TT-140: TBD → TBR) | TBR | P-DYN-400 | Martin | G2 |
| Gust rise time proposed (TT-650: TBD → TBR) | TBR | P-SYS-570 | Martin | G2 (C4 budget check at I1) |
| Rotation-during-translation term (#81.1) | TBD | MS-DYN §4.5; L2-AER-DYN-030, -050, -640 | Martin | G2 |
| No aerodynamic moment, drag form (DD-C1-01, -02, C1-Q03) | TBR | MS-DYN §5.5; L2-AER-DYN-110, -130, -160 | Martin | G2 |
| Evaluation instant of the acceleration quantities (DD-C1-04) | TBR | MS-DYN §3.3; L2-AER-DYN-300, -310 | Martin | G2 |
| Contact-step altitude reported as zero (DD-C1-03) | TBR | MS-DYN §9; L2-AER-DYN-540 | Martin | G2 |
