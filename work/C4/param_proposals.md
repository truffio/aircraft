# C4 — Parameter proposals (FC)

Proposals for `parameters/PARAMETERS.yaml` from task C4 (FC). The orchestrator merges them; C4 does not edit the database. The YAML block uses the database field layout. Existing IDs are reused: P-SYS-540 and P-SYS-550 (cross-axis tolerances, owner C4) get values, and P-FC-010 and P-FC-020 are used as they stand. New P-FC IDs are in steps of 10; no withdrawn ID is used.

**P-FC number blocks proposed.** 010–020 existing (position share, transient allowance); 030–090 tracking tolerances and settling times; 100–110 allocation accuracy; 120 ground descent; 130–990 free.

**Values.** Every value is a C4 proposal, TBR, for the owner to set or confirm at G2. They are first estimates from the authority and inertia of the C3 reference layout and the C1/C2 masses; the confirmation is a prototype run of the reference law (a hover, a gust, a step set; `work/C4/issues.md` §5). They are requirement values, not model inputs: the control-law gains are design (DD-C4-07) and are not in this database.

**TBD/TBR register.** A new row is proposed: "FC tracking tolerances, settling times, allocation accuracy and ground-force margin" (TT-C4-1, to be numbered by the orchestrator), TBR, P-FC-030 to P-FC-120, Martin, G2 (I1). TT-100 (cross-axis tolerances, P-SYS-540, P-SYS-550) moves from TBD to TBR with the values below. P-FC-010 stays on TT-050 and P-FC-020 on TT-040. TT-860 (liftoff wind) and TT-650 (gust rise time): the C4 checks are in `work/C4/issues.md` §5; neither value needs to change.

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-SYS-540 | Value null → **0.1** m/s; TBD → TBR. Description: "velocity along each translational axis of the axis references" (CR-C4-03). | L2-AER-FC-120. Of the order of the vertical velocity tolerance P-FC-050; the cross-axis response of an uncoupled vehicle with an exact force resolution is far below it. |
| P-SYS-550 | Value null → **0.005** rad/s; TBD → TBR. | L2-AER-FC-120. Equal to the heading rate tolerance P-FC-080 (about 8 % of P-SYS-270). |

## 2. YAML block

```yaml
  # --- SYS (C4 values for the cross-axis tolerances; replaces the existing entries) ---
  - id: P-SYS-540
    name: Cross-axis velocity tolerance
    description: Largest departure of the velocity along each translational axis of the axis references (north, east, vertical of the local frame V) from its reference rate while the reference of another degree of freedom changes and no axis demand is limited (L2-AER-FC-120).
    unit: m/s
    value: 0.1
    tolerance: null
    note: 'C4 proposal. At zero heading the translational axes are the body axes (CR-C4-03).'
    status: TBR
    source: L1-AER-380; L2-AER-FC-120; C4 proposal
    owner: Martin
  - id: P-SYS-550
    name: Cross-axis body rate tolerance
    description: Largest departure of the body rate about each rotational axis from its reference rate while the reference of another degree of freedom changes and no axis demand is limited (L2-AER-FC-120).
    unit: rad/s
    value: 0.005
    tolerance: null
    note: 'C4 proposal. Equal to P-FC-080.'
    status: TBR
    source: L1-AER-380; L2-AER-FC-120; C4 proposal
    owner: Martin

  # --- FC (C4 proposals; P-FC-010 and P-FC-020 are unchanged) ---
  - id: P-FC-030
    name: Vertical position tracking tolerance
    description: Largest difference between the altitude and the reference altitude while the vertical axis regulates position, outside the settling time of a reference step (L3-AER-FC-TR-050). FC share of the altitude-hold tolerance P-AF-110.
    unit: m
    value: 0.05
    tolerance: null
    note: 'C4 proposal. Smaller than the gear clearance at the hover height, P-AF-210 - P-DYN-040 = 0.124 m (IN-C1-44). P-AF-110 is at least this value plus the AF share.'
    status: TBR
    source: L3-AER-FC-TR-050; L2-AER-FC-100; C4 proposal
    owner: Martin
  - id: P-FC-040
    name: Horizontal velocity tracking tolerance
    description: Largest magnitude of the difference between the horizontal velocity and the reference velocity of the horizontal axes, outside the settling time of a reference step, in a wind within the wind envelope with gusts (L3-AER-FC-TR-020).
    unit: m/s
    value: 0.3
    tolerance: null
    note: 'C4 proposal. Closure: P-FC-040 is at most P-AF-170 (the AF tolerance on the horizontal speed once stopped), which is at most P-SYS-510 (0.5 m/s, the landing envelope). The gust response with a disturbance estimate driven by the measured acceleration is about 0.2 m/s (DD-C4-07); without it about 0.5 m/s.'
    status: TBR
    source: L3-AER-FC-TR-020; L1-AER-310, L1-AER-970; C4 proposal
    owner: Martin
  - id: P-FC-050
    name: Vertical velocity tracking tolerance
    description: Largest difference between the vertical speed and the reference rate of the vertical axis, outside the settling time of a reference step (L3-AER-FC-TR-030). FC share of the vertical speed tracking tolerance P-AF-090.
    unit: m/s
    value: 0.1
    tolerance: null
    note: 'C4 proposal. P-AF-240 (0.305 m/s) plus this value is far inside P-SYS-500 (3.458 m/s).'
    status: TBR
    source: L3-AER-FC-TR-030; L1-AER-320, L1-AER-330, L1-AER-970; C4 proposal
    owner: Martin
  - id: P-FC-060
    name: Translational settling time
    description: Longest time from a step of the reference of a translational axis (that limits no axis demand) until the axis is within its tracking tolerance (L3-AER-FC-TR-060); also the interval after a liftoff for which the liftoff records apply (L2-AER-FC-220, L3-AER-FC-TR-100).
    unit: s
    value: 3.0
    tolerance: null
    note: 'C4 proposal. Position loop of about 1.5 rad/s over a velocity loop of about 4 rad/s (DD-C4-07). Smaller than the position-hold settling time P-SYS-460, which includes the capture (AF).'
    status: TBR
    source: L3-AER-FC-TR-060; L1-AER-370; C4 proposal
    owner: Martin
  - id: P-FC-070
    name: Heading tracking tolerance
    description: Largest difference between the heading and the reference heading (shortest angle, CV-930), outside the settling time of a reference step (L3-AER-FC-RO-020). FC share of the heading tolerance P-AF-130.
    unit: rad
    value: 0.0087
    tolerance: null
    note: 'C4 proposal. 0.5 degree, below the heading selection resolution P-AF-040 (1 degree).'
    status: TBR
    source: L3-AER-FC-RO-020; L1-AER-370; C4 proposal
    owner: Martin
  - id: P-FC-080
    name: Heading rate tracking tolerance
    description: Largest difference between the body rate about the body z axis (the heading rate at level attitude) and the reference rate, outside the settling time of a reference step (L3-AER-FC-RO-030).
    unit: rad/s
    value: 0.005
    tolerance: null
    note: 'C4 proposal. About 8 % of P-SYS-270.'
    status: TBR
    source: L3-AER-FC-RO-030; L1-AER-350; C4 proposal
    owner: Martin
  - id: P-FC-090
    name: Rotational settling time
    description: Longest time from a step of the reference of a rotational axis (that limits no axis demand) until the axis is within its tracking tolerance (L3-AER-FC-RO-050).
    unit: s
    value: 4.0
    tolerance: null
    note: 'C4 proposal. Longer than the heading-rate onset time of 0.5 s that sizes P-SYS-420 (IN-C3-25), so the sizing holds; the heading loop is about 1 rad/s (DD-C4-07).'
    status: TBR
    source: L3-AER-FC-RO-050; L1-AER-370; IN-C3-25; C4 proposal
    owner: Martin
  - id: P-FC-100
    name: Allocation force tolerance
    description: Largest difference, along each body axis, between the force that the commanded effectors give through the control effectiveness and the demanded force, for a demand within the authority box (L3-AER-FC-AL-010, -020).
    unit: N
    value: 0.1
    tolerance: null
    note: 'C4 proposal. The arithmetic of the allocation, far below the regulation tolerances (about 1e-5 of the weight).'
    status: TBR
    source: L3-AER-FC-AL-010; L2-AER-FC-150; C4 proposal
    owner: Martin
  - id: P-FC-110
    name: Allocation moment tolerance
    description: Largest difference, about each body axis, between the moment that the commanded effectors give through the control effectiveness and the demanded moment, for a demand within the authority box (L3-AER-FC-AL-010, -020).
    unit: N*m
    value: 0.1
    tolerance: null
    note: 'C4 proposal.'
    status: TBR
    source: L3-AER-FC-AL-010; L2-AER-FC-150; C4 proposal
    owner: Martin
  - id: P-FC-120
    name: Ground-descent upward-force margin
    description: Fraction of the weight (vehicle mass times P-DYN-010) by which flight control keeps its commanded upward control force below the weight while the gear is extended and the vertical reference rate is below zero (L2-AER-FC-210).
    unit: '1'
    value: 0.001
    tolerance: null
    note: 'C4 proposal. Range: zero or more. Keeps the cap below the liftoff condition of the ground contact model (MS-DYN §9.6) at the rounding of the model; the steady descent needs a force below the weight by the drag only (about 3e-5 of the weight at P-AF-240), so the cap binds by about 1e-3 g at most.'
    status: TBR
    source: L2-AER-FC-210; IN-C1-43; C4 proposal
    owner: Martin
```
