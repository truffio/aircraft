# C3 — Parameter proposals (EF)

Proposals for `parameters/PARAMETERS.yaml` from task C3 (EF). The orchestrator merges them; C3 does not edit the database. The YAML block uses the database field layout. Existing IDs are reused: P-EF-010 and the authority budgets P-SYS-400, P-SYS-410, P-SYS-420. New P-EF IDs are in steps of 10; no withdrawn ID is used.

**P-EF number blocks proposed.** 010–090 command response; 100–190 effector set (direction, point of application, output limits), one list entry per effector. 200–990 free.

**Values.** Every value is a C3 proposal, TBR, for the owner to set or confirm at G2. The per-effector lists hold the reference layout DD-200 (six effectors); a different layout is a change of these four lists only. All values computed with the database of commit 63499b8 (`work/C3/ms_dyn_s7_effectors.md` §7.1.6, §7.1.7).

**TBD/TBR register.** P-EF-010 stays on TT-080 (TBD → TBR). P-SYS-400 to -420 stay on TT-020 (TBD → TBR). A new row is proposed for P-EF-020, -030, -100 to -130: "Effector model values and reference layout (DD-160, DD-200)", TBR, Martin, G2 (I1). TT-260 (L0-CON-300 field, per-effector maximum force values, closes at G2 (C3)) can close when P-EF-120 is accepted.

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-EF-010 | Value null → **0.06** s; TBD → TBR. Description: "reaching" defined as entering the band P-EF-030 (see YAML). | L2-AER-EF-340; FUNCTIONAL_ANALYSIS §7.5: P-SYS-310 + P-EF-010 = 0.08 s ≤ P-SYS-480 = 0.1 s. The model reaches the band in 0.04 s with P-EF-020. |
| P-SYS-400 | Value null → **60 000** N; TBD → TBR. Description: the drag term is the vertical drag of a climb at P-SYS-240 at the largest horizontal airspeed. | FA §7.1 as written gives 39 620 N (G2-F04, verified); under isotropic drag a climb at P-SYS-240 at an airspeed of 231.5 m/s has a vertical drag of 21.8 kN, so the need is 58 571 N (CR-C3-01, C3-Q02). |
| P-SYS-410 | Value null → **190 000** N; TBD → TBR. | FA §7.1: 186 190 N (G2-F04, verified); 187 606 N with the climb at that airspeed. |
| P-SYS-420 | Value null → **2000** N·m; TBD → TBR. | J_max × P-SYS-270 / 0.50 s with J_max = 15 975 kg·m² (uniform capsule at full fuel, MS-DYN §6 reference derivation); drag-moment lines zero (DD-050). Re-derived when P-FU-070, -080 are set. |

## 2. YAML block

```yaml
  # --- SYS (C3 values for the authority budgets; replaces the existing entries) ---
  - id: P-SYS-400
    name: Minimum upward control force
    description: Control force the effector set can produce along the negative body z axis (up at level attitude), with the other five force and moment components at zero, while fuel remains and the effectors are on. Budget - at least m_max x (P-DYN-010 + P-SYS-440) + the vertical drag of a climb at P-SYS-240 at the largest horizontal airspeed P-SYS-230 + P-SYS-430 + P-SYS-560 (isotropic drag, MS-DYN §5.5). Also the upward bound of the authority box (L2-AER-EF-330).
    unit: N
    value: 60000
    tolerance: null
    note: 'C3 (MS-DYN §7.1.6). m_max = 1500 kg - weight plus manoeuvre 36 775 N; vertical drag 0.5 x 1.225 x 5 x 233.50 x 30.48 = 21 796 N; total 58 571 N, rounded up. The FA §7.1 formula with the drag of the vertical speed alone gives 39 620 N (G2-F04). Smaller than P-SYS-410, as D72 allows.'
    status: TBR
    source: L1-AER-120; FUNCTIONAL_ANALYSIS §7.1; L2-AER-EF-300, -330; D46, D72; C3 proposal
    owner: Martin
  - id: P-SYS-410
    name: Minimum control force, other body directions
    description: Control force the effector set can produce along each of +x_B, -x_B, +y_B, -y_B and +z_B, with the other five components at zero, while fuel remains and the effectors are on. Budget - at least m_max x P-SYS-440 + drag at the largest horizontal airspeed P-SYS-230 + P-SYS-430 + P-SYS-560 (P-SYS-230 is a ground speed, D72). Also the bound of the authority box along x_B, y_B and down (L2-AER-EF-330).
    unit: N
    value: 190000
    tolerance: null
    note: 'C3 (MS-DYN §7.1.6). Manoeuvre 22 065 N; drag at 231.50 m/s 164 125 N, total 186 190 N (G2-F04); 187 606 N with the horizontal drag of a climb at P-SYS-240 at that airspeed. Rounded up. The downward direction needs about 29 kN; it shares the value because L1-AER-130 lists it with the horizontal ones (C3-Q08).'
    status: TBR
    source: L1-AER-130; FUNCTIONAL_ANALYSIS §7.1; L2-AER-EF-310, -330; D51, D72; C3 proposal
    owner: Martin
  - id: P-SYS-420
    name: Minimum control moment per body axis
    description: Control moment the effector set can produce about each body axis in each sense, with the other five components at zero, while fuel remains and the effectors are on. Budget - at least J_max x P-SYS-270 / (heading-rate onset time); the drag-moment lines are zero (DD-050). Also the moment bound of the authority box (L2-AER-EF-330).
    unit: N*m
    value: 2000
    tolerance: null
    note: 'C3 (MS-DYN §7.1.6). J_max = 15 975 kg*m^2 (I_yy = I_zz of a uniform capsule of P-DYN-020 x P-DYN-030 at 1500 kg); reaches P-SYS-270 from rest in 0.50 s. C4 confirms the onset time; re-derived when P-FU-070 and P-FU-080 are set.'
    status: TBR
    source: L1-AER-140; FUNCTIONAL_ANALYSIS §7.1; L2-AER-EF-320, -330; C3 proposal
    owner: Martin

  # --- EF --- (C3 proposals; replaces the existing P-EF-010 entry)
  - id: P-EF-010
    name: Effector command response time
    description: Longest time from the simulation step at which a changed effector command applies to the first output sample at which the effector output is within the fraction P-EF-030 of the size of the change of the clipped command from the new clipped command (L2-AER-EF-340; measured as CV-860). Share of P-SYS-480 - P-SYS-310 + P-EF-010 is at most P-SYS-480.
    unit: s
    value: 0.06
    tolerance: null
    note: 'C3. With P-EF-020 = 0.015 s and P-SYS-300 = 0.01 s the model enters the band in 0.04 s. 0.02 + 0.06 = 0.08 s, inside the 0.1 s of P-SYS-480.'
    status: TBR
    source: L1-AER-710; FUNCTIONAL_ANALYSIS §7.5; L2-AER-EF-340; DD-020; C3 proposal
    owner: Martin
  - id: P-EF-020
    name: Effector time constant
    description: Time constant tau of the first-order lag by which each effector output follows its clipped effector command (MS-DYN effector model, DD-160). Common to the effector set. Command-response kind (L1-AER-100).
    unit: s
    value: 0.015
    tolerance: null
    note: 'C3. Range - greater than zero. Per-step factor exp(-P-SYS-300 / P-EF-020) = 0.513 at 0.01 s. A per-effector list is a later option if a layout needs it.'
    status: TBR
    source: L1-AER-100, -710; L2-AER-EF-010, -050, -100, -340; DD-160; C3 proposal
    owner: Martin
  - id: P-EF-030
    name: Effector response band
    description: Fraction of the size of a change of clipped effector command within which the effector output counts as having reached the new command (L2-AER-EF-340). Defines "reaching" for P-EF-010. Command-response kind (L1-AER-100).
    unit: '1'
    value: 0.05
    tolerance: null
    note: 'C3. Range - greater than zero and less than one. 5 % (about three time constants).'
    status: TBR
    source: L1-AER-710; L2-AER-EF-010, -340; C3 proposal
    owner: Martin
  - id: P-EF-100
    name: Effector directions of action
    description: Unit direction vector d_i of each effector in the body frame, one entry per effector; a positive output acts along +d_i (CV-330). The number of entries is the number of effectors, the same in P-EF-100 to P-EF-130. Constant over a run (L1-AER-090). Direction-of-action kind (L1-AER-100).
    unit: '1'
    value: [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]
    tolerance: null
    note: 'C3 reference layout DD-200 (three pairs, each parallel to one body axis). Range - each entry of unit length. A design value, not a requirement.'
    status: TBR
    source: L1-AER-090, -100; L2-AER-EF-010, -020, -120, -300 to -330; DD-150, DD-200; C3 proposal
    owner: Martin
  - id: P-EF-110
    name: Effector points of application
    description: Point of application r_i of each effector, a body-frame position from the centre of gravity, one entry per effector, in the order of P-EF-100. With P-EF-100 it gives the control effectiveness (d_i, r_i x d_i) per newton of output (MS-DYN effector model). Constant over a run. Control-effectiveness kind (L1-AER-100).
    unit: m
    value: [[0.0, 1.5, 0.0], [0.0, -1.5, 0.0], [0.0, 0.0, 1.5], [0.0, 0.0, -1.5], [4.0, 0.0, 0.0], [-4.0, 0.0, 0.0]]
    tolerance: null
    note: 'C3 reference layout DD-200. Each point inside the capsule of P-DYN-020 x P-DYN-030. A design value, not a requirement.'
    status: TBR
    source: L1-AER-090, -100; L2-AER-EF-010, -020, -120, -300 to -330; DD-150, DD-200; C3 proposal
    owner: Martin
  - id: P-EF-120
    name: Effector maximum force
    description: Largest output U_i of each effector, which is its maximum force magnitude (L0-CON-300, L1-AER-110), one entry per effector in the order of P-EF-100. Output-limits kind (L1-AER-100).
    unit: N
    value: [100000, 100000, 100000, 100000, 100000, 100000]
    tolerance: null
    note: 'C3 reference layout DD-200. Range - each entry greater than zero. Each pair gives 200 kN along its axis; the authority box of L2-AER-EF-330 is met with a 4.5 % margin. Closes TT-260 (L0-CON-300).'
    status: TBR
    source: L0-CON-300; L1-AER-100, -110; L2-AER-EF-010, -110, -300 to -330; DD-200; C3 proposal
    owner: Martin
  - id: P-EF-130
    name: Effector smallest output
    description: Smallest output L_i of each effector, one entry per effector in the order of P-EF-100, from the negative of its P-EF-120 entry (pushes both ways) to zero (pushes one way only). Output-limits kind (L1-AER-100).
    unit: N
    value: [-100000, -100000, -100000, -100000, -100000, -100000]
    tolerance: null
    note: 'C3 reference layout DD-200 (each effector pushes both ways). Range - from minus the P-EF-120 entry to zero, so that zero output is valid.'
    status: TBR
    source: L1-AER-100, -110; L2-AER-EF-010, -100, -110; CV-330; DD-200; C3 proposal
    owner: Martin
```

## 3. Parameters used but not owned by EF

P-SYS-230, -240, -250, -270, -300, -310, -430, -440, -480, -540, -550, -560; P-DYN-010, -100; P-FU-010, -030, -070, -080, -100; P-FC-010; P-TM-010. No change proposed, except that P-FU-070 and P-FU-080 (TBD) feed P-SYS-420.

## 4. No EF verification tolerance

The EF analyses compare with independent computations "to floating-point rounding" (as L2-AER-DYN-300 does), so no EF tolerance parameter is proposed: an EF parameter that is not one of the five kinds would fail the inspection of L1-AER-100 (IN-EF-010).
