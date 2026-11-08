# C8 — Parameter proposals (FCP)

Proposals for `parameters/PARAMETERS.yaml` from task C8 (flight control panel). The orchestrator merges them; C8 does not edit the database. Field layout as in the database; owner Martin for each. Written at branch c1_c2, commit 55c6c29 (D1–D74).

**What FCP uses.** The selection resolutions P-AF-010 to -040 and the display resolutions P-TM-020 to -050 are FCP's (D55, D71; their prefixes kept, as the database notes say). The selector ranges use the existing envelope parameters P-SYS-200, -210, -230, -240, -250 and the body diameter P-DYN-030, so no range parameter is added: the lowest selectable altitude follows from them (20 ft with the present values, L2-AER-FCP-120). Two new FCP parameters are proposed (§1), and one stored value is corrected (§2).

**P-FCP number blocks proposed.** 010–090 display and conversion; 100–990 free.

## 1. New parameters

```yaml
  # --- FCP --- (C8 proposals)
  - id: P-FCP-010
    name: Fuel display resolution
    description: Resolution of the remaining fuel mass shown to the crew, in pounds (L2-AER-FCP-210, -380). The shown value is the remaining fuel mass divided by the CV-750 factor and rounded half away from zero to a multiple of this resolution.
    unit: lb
    crew_facing: true
    value: 1
    tolerance: null
    note: 'C8 proposal (C8-Q06). The full capacity P-FU-010 (500 kg) is 1102.3 lb, so 1 lb is about 0.1 % of it, finer than the low-fuel threshold P-FU-020 (110.2 lb) by two orders of magnitude. A remaining fuel below 0.5 lb shows as 0 before exhaustion; the FUEL EXHAUSTED alert marks the exhaustion.'
    status: TBR
    source: L1-AER-560; L2-AER-FCP-210, -380; CV-780; C8 proposal
    owner: Martin
  - id: P-FCP-020
    name: Crew-unit conversion agreement tolerance
    description: Largest relative difference between a target or shown value that the flight control panel computes and its independent computation by the exact CV-750 factor, in the FCP tests (TP-FCP-200, -210). Floating-point agreement only; not a rounding allowance.
    unit: '1'
    value: 1.0e-12
    tolerance: null
    note: 'C8 proposal. One multiplication or division by an exact factor in double precision differs from the exact result by at most about 1.1e-16 relative, a few rounding steps if the factor is itself computed (1852/3600, 0.3048/60, pi/180); 1e-12 leaves four orders of magnitude of margin and is far below each display resolution relative to its range (1 ft in 150 000 ft is 6.7e-6).'
    status: TBR
    source: L1-AER-870; L2-AER-FCP-200; CV-750, CV-770; C8 proposal
    owner: Martin
```

## 2. Changes to existing entries

Only the fields shown change.

```yaml
  - id: P-SYS-230
    value: 154.33333333333334
    note: '300 kt exactly by the CV-750 factor (300 x 1852/3600 = 463/3 m/s), stored as the nearest double, which is above the exact value; the earlier 154.333 is 299.9994 kt and would make 300 kt unselectable (L2-AER-FCP-110, C8-Q07). The value is unchanged in intent (D66, D72).'
  - id: P-AF-010
    description: Smallest step of the selected altitude. The selectable altitudes are the multiples of P-AF-010 whose exact conversion is from P-SYS-210 + P-DYN-030/2 to P-SYS-200 (L2-AER-FCP-120); 20 ft to 150 000 ft with the present values. A multiple of the altitude display resolution P-TM-020.
    source: D71; L2-AER-FCP-120
  - id: P-AF-020
    description: Smallest step of the selected vertical speed (signed, positive when climbing). The selectable vertical speeds are the multiples of P-AF-020 whose exact conversion is from -P-SYS-250 to P-SYS-240, zero included (L2-AER-FCP-130). A multiple of the vertical speed display resolution P-TM-030.
    source: D71; L2-AER-FCP-130
  - id: P-AF-030
    description: Smallest step of the selected horizontal speed (a ground speed, CV-480, D72). The selectable horizontal speeds are the multiples of P-AF-030 from zero whose exact conversion is at most P-SYS-230 (L2-AER-FCP-110). A multiple of the speed display resolution P-TM-040.
    source: D71; L2-AER-FCP-110
  - id: P-AF-040
    description: Smallest step of the selected heading. The selectable headings are the multiples of P-AF-040 in [0, 360) deg, north selected as 0 (L2-AER-FCP-100, CV-520). A multiple of the direction angle display resolution P-TM-050.
    source: D71; L2-AER-FCP-100
  - id: P-TM-050
    description: Resolution of heading and track values shown to the crew. A value that rounds to 360 deg is shown as 0 (L2-AER-FCP-220).
    source: D71; L2-AER-FCP-210, -220
```

P-TM-020 to -040 change only in their `source` (add L2-AER-FCP-210). P-AF-010 to -040 and P-TM-020 to -050 keep their values (D71) and status TBR.

**Consistency rule** (for the descriptions above and for I1): each selection resolution must be a multiple of the display resolution of its quantity, so that a target from a selected value is annunciated as the selected value (L2-AER-FCP-210, -330). With the D71 values: 10 ft / 1 ft, 100 ft/min / 10 ft/min, 1 kt / 1 kt, 1° / 1°. It holds.

## 3. Register rows (`registers/TBD_TBR.md`)

| ID | Change | Reason |
| --- | --- | --- |
| New row (next free, after TT-930) | "Fuel display resolution 1 lb and crew-unit conversion tolerance 1e-12 (C8)", TBR, P-FCP-010, P-FCP-020, Martin, G2 (I1) | New TBR parameters. |
| TT-170 | Location unchanged; add "Checked by C8 against the selector ranges (20 ft to 150 000 ft, ±6000 ft/min, 0 to 300 kt, 0 to 359°): no conflict. Owner confirms at G2." | C8 was named as the closure (G2 (C8)). C8 found nothing against the D71 values; the owner closes them. |
| TT-210 | Same note: "Checked by C8: each selection resolution is a multiple of its display resolution. Owner confirms at G2." | As above. |
| TT-010 | Add P-SYS-230 to the location (stored precision, C8-Q07). | The value is Set, but its stored digits change. Alternatively record the change under the C8-Q07 answer only. |

## 4. Parameters cited but not owned

| ID | Used in | Note |
| --- | --- | --- |
| P-SYS-200, -210, -240, -250 | L2-AER-FCP-120, -130 | Selector range limits; their values are the envelope (D67), TBR on TT-010. |
| P-SYS-230 | L2-AER-FCP-110 | §2 stored precision. |
| P-DYN-030, P-DYN-040 | L2-AER-FCP-120, -360 | Lowest selectable altitude; the altitude shown on the ground. |
| P-NAV-010, P-NAV-030 | L2-AER-FCP-370 | Validity thresholds, NAV's (C6). |
| P-FU-010, P-FU-020 | L2-AER-FCP-390 | Low-fuel threshold, FU's. |
| P-SYS-310, P-SYS-470, P-TM-010, P-AF-060 | L2-AER-FCP-080, -090, -300, -310, -340 | Timing budget (FUNCTIONAL_ANALYSIS §7.5). The FCP share of P-SYS-470 is P-TM-010; for the fuel alerts P-SYS-310 + P-TM-010 (0.04 s ≤ 0.5 s). |
| P-AF-220 | L2-AER-FCP-130 | The standard vertical speed is not a selected value; AF's. |
