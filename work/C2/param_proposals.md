# C2 — Parameter proposals (FU), rework for G2 and D69

The first C2 proposals (P-FU-010 to -100) were merged into `parameters/PARAMETERS.yaml` with the owner's values (D65, D66). This file now holds only the **changes** that the C2 rework proposes to the merged entries (§1), the register rows (§2) and the parameters cited but not owned (§3). Field layout as in `parameters/PARAMETERS.yaml`; owner Martin for each; SI units (CV-720); no FU parameter is crew-facing. **No new FU parameter is proposed**, and no ID is withdrawn: the fuel volume is the body shape (DD-C2-07), so G2-F16 needs no fuel-volume dimension.

The B3 package already changes the `P-SYS-280` note and the `P-FU-100` description for the takeoff (`work/B3/param_proposals.md`); C2 agrees with both and does not repeat them.

## 1. Changes to merged parameters

Only the fields shown change.

```yaml
parameters:
  - id: P-FU-040
    note: 'Range: zero or more (zero switches off translational consumption, for model checks). Derived from the anchor P-SYS-290 (D66, D72 Q4) by the MS-DYN fuel model, parameter derivation (work/C2/ms_dyn_s6_s7_fu.md §7.2.4): 8 h at P-SYS-230 at sea level in still air, from full fuel, with the drag of P-DYN-100 and the masses P-FU-010, P-FU-030; k_t = (asinh(m_max g/D) - asinh(m_dry g/D)) / (g P-SYS-290) = 2.347e-7, rounded down so that the endurance at speed is at least 8 h (8.02 h). Re-derived, with P-FU-050 and then P-SYS-280, whenever P-DYN-100, P-SYS-230, P-FU-010 or P-FU-030 changes (TT-110, TT-750, TT-800).'
  - id: P-FU-050
    note: 'Range: zero or more. Equal in number to P-FU-040 (D66), so that a control moment of 1 N*m costs as much fuel as a control force of 1 N; rotation is then a small share of the reference-mission fuel. Re-derived with P-FU-040.'
  - id: P-FU-060
    note: 'Range: greater than zero. About 2e-9 of P-FU-010, ample for double-precision per-step sums over a reference mission of up to P-SYS-280 at P-SYS-300 = 0.01 s, the rest on the ground included (D69). Setting the remaining fuel to zero at the end of the exhaustion step (L2-AER-FU-340) differs from the sum by rounding only. The check uses the flow of each simulation step (D65, IN-C2-30).'
  - id: P-FU-070
    description: Principal moments of inertia (Ixx, Iyy, Izz) of the dry mass about the centre of gravity, in the body axes, three components. Products of inertia are zero (D61; CV-350 sign convention). The inertia tensor at fuel exhaustion (L2-AER-FU-170). Derived in the MS-DYN mass-properties model from the body dimensions P-DYN-020, P-DYN-030 and P-FU-030, with the dry mass uniform over the capsule (L2-AER-FU-190, DD-C2-07); not set independently, and checked against each vehicle parameter set at run start (L2-AER-FU-330).
    value: [1900.0, 10650.0, 10650.0]
    note: 'Range: each component greater than zero, and each at most the sum of the other two (triangle inequality of a physical body). 12 m x 4 m capsule, 1000 kg uniform: the cylinder holds 0.75 of the mass, each hemisphere 0.125 (MS-DYN §6 reference derivation; rederived by the G2 inspector). Re-derived when P-DYN-020, P-DYN-030 or P-FU-030 changes.'
    status: TBR
    source: L1-AER-220; L0-CON-140; L2-AER-FU-170, -180, -190, -330; MS-DYN mass-properties model (C2 content, work/C2/ms_dyn_s6_s7_fu.md §6.3); DD-120, DD-C2-07
  - id: P-FU-080
    description: Principal moments of inertia (Ixx, Iyy, Izz) of the fuel at full capacity P-FU-010 about the centre of gravity, in the body axes, three components. Products of inertia are zero. The fuel share of the inertia tensor is this value times the ratio of the remaining fuel mass to P-FU-010 (L2-AER-FU-170; uniform depletion, DD-120). Derived in the MS-DYN mass-properties model from P-DYN-020, P-DYN-030 and P-FU-010, with the fuel uniform over the capsule (L2-AER-FU-190, DD-C2-07); checked against each vehicle parameter set at run start (L2-AER-FU-330).
    value: [950.0, 5325.0, 5325.0]
    note: 'Range: each component zero or more. The owner chose an inertia that changes with fuel (D65). With the fuel volume equal to the body shape (DD-C2-07), P-FU-080 = P-FU-070 x P-FU-010 / P-FU-030. Full-fuel tensor P-FU-070 + P-FU-080 = (2850, 15975, 15975) kg*m^2, used by the moment budget P-SYS-420 (C3).'
    status: TBR
    source: L1-AER-220; L0-CON-140; L2-AER-FU-170, -180, -190, -330; MS-DYN mass-properties model (C2 content, work/C2/ms_dyn_s6_s7_fu.md §6.3); DD-120, DD-C2-07
  - id: P-FU-090
    description: Largest relative difference between an FU output (fuel mass flow, principal moment of inertia) and its independent computation from the recorded inputs, in the FU analyses and tests (AN-FU-040, -050, -170; DM-FU-010), and between a principal moment of P-FU-070 or P-FU-080 in a vehicle parameter set and its value derived from that set (L2-AER-FU-330). Floating-point agreement only.
    source: L2-AER-FU-010, -040, -050, -170, -330; C2 proposal; D65
  - id: P-SYS-290
    description: Time, from full fuel at maximum mass, during which the vehicle sustains the maximum horizontal speed P-SYS-230 at sea level in still air before fuel exhaustion. The anchor from which the consumption coefficients P-FU-040 and P-FU-050 and the hover endurance P-SYS-280 are derived (D66, MS-DYN fuel model, parameter derivation); not a requirement to verify (D72), so no requirement cites it and PARAM-UNUSED is expected. A change of P-DYN-100 re-derives them. 8 h.
```

## 2. Register rows (`registers/TBD_TBR.md`)

| ID | Change | Reason |
| --- | --- | --- |
| TT-770 | Item: "Dry-mass and full-fuel principal moments of inertia, derived in the MS-DYN mass-properties model (C2): (1900, 10650, 10650) and (950, 5325, 5325) kg·m²". Type TBD → **TBR**. Closure: "with the body shape (TT-740, 2026-11-30)". | Values proposed (§1); they follow the shape. |
| TT-110 | Item: append "; P-FU-040, -050 derived from P-SYS-290 with P-DYN-100 (D66); re-derive with TT-750 and TT-800 (D72 Q4)". | G2-F18: link the derivation chain. |
| TT-750 | Item: append "; a change re-derives P-FU-040, -050 (TT-110) and P-SYS-280 (TT-800), and P-SYS-580 (TT-860)". | G2-F18; B3 P-SYS-580 note. |
| TT-800 | Item: append "; set from L2-AER-FU-290 with P-FU-040 (TT-110); re-derived after TT-110". | G2-F18. |
| TT-580 | As B3 proposes ("Annunciations after fuel exhaustion (D68), C5"). L2-AER-FU-230 no longer cites it. | G2-F13. |
| New, L2 field copies | None needed: each FU TBD/TBR field cites existing rows (TT-070, -110, -120, -130, -600, -680, -720, -740, -770, -780, -790, -800). The two allocation items of L2-AER-FU-310 and -320 close with CR-C2-04. | — |

## 3. Parameters cited but not owned by FU

`P-SYS-300` (simulation step), `P-SYS-480` (control-loop latency, L2-AER-FU-300), `P-DYN-010` (gravity), `P-DYN-020`, `P-DYN-030` (body dimensions, L2-AER-FU-190, -330) and `P-SYS-280` (hover endurance) are cited by ID. The rationales also name `P-SYS-230`, `P-SYS-290`, `P-DYN-100`, `P-DYN-040`, `P-DYN-050`, `P-AF-210`, `P-AF-230`, `P-AF-240` and `P-TM-010`, which no FU statement or criterion uses (G2-F20 rule). No change is proposed to them, except the P-SYS-290 description above.
