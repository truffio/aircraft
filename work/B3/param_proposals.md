# B3 — Parameter proposals (landing gear and ground operations, D69)

Field layout follows `parameters/PARAMETERS.yaml`. Owner Martin for each. §1 has the new parameters, §2 the changes to existing entries (descriptions and notes only; values are unchanged), and §3 the derived quantities that are deliberately not parameters.

**IDs.** P-DYN-050 is in the "010-090 gravity and geometry" block of the P-DYN header and follows P-DYN-040 (gear length). P-SYS-580 is in the L1 budget block 400–590 (P-SYS-570 is the last one used; P-SYS-520 is withdrawn and not reused).

## 1. New parameters

```yaml
  # --- DYN: landing gear (D69) ---
  - id: P-DYN-050
    name: Landing gear transit time
    description: Time from a change of the landing gear command to the gear reaching the commanded position (extended or retracted), while the Aeronef is airborne (L1-AER-910). The gear is in transit meanwhile; a ground contact in transit is a crash (L1-AER-270). Zero would make the gear move instantly.
    unit: s
    value: 3.0
    tolerance: null
    note: 'B3 proposal. Short against the hover and long enough for the gear state to be observed and annunciated (L1-AER-470): a Takeoff or a Land takes about 0.7 s of vertical motion (0.124 m at P-AF-240 with the P-AF-230 ramps) plus one transit. No effect on the fuel or endurance budgets.'
    status: TBR
    source: L1-AER-910; D69; B3 proposal
    owner: Martin

  # --- SYS: takeoff wind limit (D69, owner question B3-Q2) ---
  - id: P-SYS-580
    name: Maximum wind speed at liftoff
    description: Largest wind speed (steady wind plus gust, CV-470) at the liftoff of a takeoff for which the takeoff capability L1-AER-960 applies; part of the wind envelope at liftoff (glossary). On the ground the ground reaction holds the vehicle against the drag; at liftoff the drag acts as a step that the flight software cannot anticipate (L1-AER-670). Sized so that the drag step at dry mass P-FU-030 and sea-level density stays within the flight-control transient allowance P-FC-020 - that is, P-SYS-580 is at most sqrt(2 x P-FC-020 x P-FU-030 / (1.225 x P-DYN-100)).
    unit: m/s
    value: 38.583
    tolerance: null
    note: '75 kt. With P-FC-020 = 4.903 m/s^2, P-FU-030 = 1000 kg and P-DYN-100 = 5 m^2 the bound is 40.0 m/s (77.8 kt); the drag at 75 kt is 4.56 kN, 0.47 g at dry mass. Re-derive if P-DYN-100, P-FU-030 or P-FC-020 change (TT-750, TT-110, TT-040). Without a limit, a liftoff into the largest wind (P-SYS-430 + P-SYS-560, 150 kt) gives 18.2 kN, 1.86 g at dry mass, above P-SYS-440 (L1-AER-300).'
    status: TBR
    source: L1-AER-960; D69; owner question B3-Q2
    owner: Martin
```

New register rows to open (`registers/TBD_TBR.md`; the next free IDs are after TT-840):

| ID | Item | Type | Location | Owner | Closure | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TT-850 | Landing gear transit time 3 s (D69, B3) | TBR | P-DYN-050 | Martin | G2 (C1) | Open |
| TT-860 | Maximum wind speed at liftoff 75 kt (D69, B3-Q2) | TBR | P-SYS-580 | Martin | G2 (I1, C4 check against P-FC-020) | Open |

## 2. Changes to existing entries

Values and status are unchanged unless stated.

```yaml
  - id: P-SYS-210
    name: Minimum operating height above the ground
    description: Lowest height above the ground (CV-400) of nominal flight, the lower bound of the operating volume (glossary). Equal to the hover height P-AF-210 (D67) and measured the same way, at the lowest point of the body (D70). The selected altitude is bounded below by the altitude at which the height above the ground is P-SYS-210 at level attitude, that is P-SYS-210 + P-DYN-030/2 (C8). Takeoff and Land fly below it, between the ground and the hover height (crew-facing ft).
    unit: m
    value: 1.524
    note: '5 ft, the hover height (D67, D70). As a CG altitude this would put the body 0.48 m below the ground; CV-400 resolves TT-820. The corresponding CG altitude at level attitude is 3.524 m (11.56 ft).'
    status: TBR
    source: CONOPS §4.2, §5, SC-020; owner (D67, D70); CV-400 (CR-B3-36)

  - id: P-AF-210
    name: Hover height above the ground
    description: Height above the ground (CV-400) of the lowest point of the body that Go to hover brings the vehicle to, from above or from below (D70), that Hover holds and that Takeoff climbs to (D69). A project constant, not a crew selection (D56). At level attitude the CG altitude is P-AF-210 + P-DYN-030/2.
    note: '5 ft (owner, D70). TT-820 closed by CV-400 (CR-B3-36).'

  - id: P-DYN-040
    name: Landing gear length
    description: Distance, at level attitude, from the lowest point of the body down to the ground contact points of the extended landing gear (D69, L1-AER-900). On the ground the height above the ground is P-DYN-040 and the CG altitude P-DYN-030/2 + P-DYN-040. Less than P-AF-210, so that the Land descent from the hover is short; at the hover height the extended gear clears the ground by P-AF-210 - P-DYN-040.
    note: '1.4 m (owner, D69): on the ground the CG is at 3.4 m; at the hover height the extended gear clears the ground by 0.124 m, so the altitude-hold error in Hover with the gear extended must stay below 0.124 m (C5, P-AF-110).'
    source: owner (D69); L1-AER-900

  - id: P-SYS-280
    name: Minimum hover endurance at full fuel
    description: Shortest time from a takeoff at full fuel and maximum mass, followed by a hold of the horizontal position and the hover height in still air (Takeoff then Hover; D69), to fuel exhaustion (L1-AER-360).
    note: '46 h. Derived (D66) from the endurance at maximum speed through the fuel budget of L2-AER-FU-290: ln(1500/1000) / (1.05 x 2.34e-7 x 9.80665) = 46.7 h, rounded down. The takeoff (about 0.7 s of climb and one gear transit) is inside the margin P-FU-100.'
    source: CONOPS SC-110 (variation hover endurance); L1-AER-360; D66, D69

  - id: P-FU-100
    description: Fraction by which the fuel mass flow in a still-air hold may exceed the translational term that balances the weight, used to size the fuel capacity P-FU-010 (L2-AER-FU-290). Covers the regulation of the hold, the attitude-holding moments, the transient at the start of the hold and the takeoff that precedes it (D69, L1-AER-360).

  - id: P-SYS-500
    description: Largest vertical speed magnitude at the contact step for a ground contact on the extended landing gear, with fuel remaining, to be a landing (L1-AER-260, -280).

  - id: P-SYS-510
    description: Largest horizontal speed at the contact step for a ground contact on the extended landing gear, with fuel remaining, to be a landing (L1-AER-260, -280). Bounds the hover horizontal speed tolerance P-AF-170 for Land (L1-AER-970).
```

Notes to add to entries owned by C5 (no value change):

- **P-AF-110** (altitude hold tolerance, TBD): "In Hover with the landing gear extended (before Land descends, after Takeoff reaches the hover height), the altitude error must stay below P-AF-210 - P-DYN-040 (0.124 m), or the gear touches the ground (C5, B3)."
- **P-AF-170** (hover horizontal speed tolerance, TBD): "At most P-SYS-510, so that a Land from Hover meets the landing envelope (L1-AER-970)."
- **P-AF-240** (takeoff and landing vertical speed): source add "L1-AER-960, -970".

## 3. Derived quantities, not parameters

These follow from the parameters above and are not stored, to avoid two values for one quantity:

| Quantity | Expression | Value |
| --- | --- | --- |
| CG altitude at rest on the ground (level attitude) | P-DYN-030/2 + P-DYN-040 | 3.4 m (11.15 ft) |
| CG altitude at the hover height (level attitude) | P-DYN-030/2 + P-AF-210 | 3.524 m (11.56 ft) |
| Gear clearance at the hover height, gear extended | P-AF-210 − P-DYN-040 | 0.124 m |
| Takeoff and Land vertical travel | P-AF-210 − P-DYN-040 | 0.124 m; about 0.7 s with the P-AF-230 ramps at P-AF-240 |
| Touchdown vertical speed under Land | P-AF-240 | 0.3048 m/s, 8.8 % of P-SYS-500 |
