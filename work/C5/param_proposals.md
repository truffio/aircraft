# C5 — Parameter proposals (AF)

Proposals for `parameters/PARAMETERS.yaml` from task C5 (AF). The orchestrator merges them; C5 does not edit the database. The YAML block uses the database field layout. **No new parameter is proposed**: every quantity the AF records and AF_MODE_LOGIC need is an existing P-AF, P-SYS, P-DYN or P-NAV parameter, and the derived limits (the horizontal acceleration limit, the level-off distance, the stopping position) are formulas of existing parameters (DD-C5-03, DD-C5-07). P-AF-250 and the next IDs stay free. P-AF-050, -070, -080 and -150 stay withdrawn (D56).

**Values.** Every value below is a C5 proposal, TBR, for the owner to set or confirm at G2 (L1 TBD fields P-AF-170, P-AF-180, P-AF-060, P-SYS-460) or to refine at G3 with the mode sections (TT-180: P-AF-090 to -140, -190). C5 has not seen the control-law design (C4 in parallel); the tracking tolerances in particular are judgement values, chosen so that they are consistent with each other, with the selection resolutions and with the gear clearance, and FC may ask to change them at I1. Nothing in the L2 records depends on a value.

**TBD/TBR register.** TT-060 (P-SYS-460): the "start of the hold" is defined by rule PR-4 of AF_MODE_LOGIC; the value stays 30 s TBR. TT-070: P-AF-060 TBD to TBR. TT-180: P-AF-090, -100, -110, -120, -130, -170, -190 TBD to TBR, P-AF-140 stays TBD for M5. TT-190: P-AF-180 stays TBR with a value. TT-610 and TT-900 (valid initial mode states): closed by AF_MODE_LOGIC §14 (rows IC-1 to IC-7). TT-580 (annunciations after fuel exhaustion): closed by L2-AER-AF-860 (DD-C5-05), pending the owner's answer to C5-Q04.

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-AF-060 | Value null to **0.04** s; TBD to TBR. | L2-AER-AF-810; FUNCTIONAL_ANALYSIS §7.5: a selection is taken at the next control frame and processed in that frame, two periods of [P-SYS-310] = 0.02 s; with [P-TM-010] = 0.02 s the total is 0.06 s, within [P-SYS-470] = 0.5 s. |
| P-AF-090 | Value null to **0.1** m/s; TBD to TBR. Description adds: "Also the largest vertical speed magnitude of a vehicle that is stationary at the hover height (L2-AER-AF-260)." | About 20 ft/min, a third of [P-AF-240] (0.3048 m/s) and a fifth of the selection resolution [P-AF-020] (0.508 m/s). Gives the Hover handover a vertical speed of at most 0.1 m/s, which is 0.5 s of drift against the 0.05 m altitude tolerance. |
| P-AF-100 | Value null to **1.0** m; TBD to TBR. | The vertical reference does not overshoot (L2-AER-AF-560), so this is the tracking overshoot of the vehicle at a level-off of up to 473 m (the climb at [P-SYS-240] at [P-AF-230]); 1 m is large against the hold tolerance and leaves room for the control law. Refined at G3 (M3). |
| P-AF-110 | Value null to **0.05** m; TBD to TBR. Note replaced (below). | The gear clearance in Hover is [P-AF-210] - [P-DYN-040] = 0.124 m (IN-C1-44). With the tilt allowed by [P-AF-180], the height above the ground changes by up to ((P-DYN-020 - P-DYN-030)/2) x sin(P-AF-180) = 4 m x sin(0.5 deg) = 0.035 m (CV-400). 0.05 m + 0.035 m = 0.085 m is inside 0.124 m with 0.039 m of margin. FC must confirm that it can hold 0.05 m in the gust envelope at I1; the horizontal wind produces no vertical force, so the vertical disturbance is small (D51). |
| P-AF-120 | Value null to **0.5** m/s; TBD to TBR. | One selection step of the horizontal speed ([P-AF-030] = 1 kt = 0.514 m/s): a selected speed is settled when it is within one step. Ground speed (D72). Refined at G3 (M5). |
| P-AF-130 | Value null to **0.0175** rad (1 deg); TBD to TBR. | One selection step of the heading ([P-AF-040] = 1 deg). Refined at G3 (M0, M5). |
| P-AF-140 | Stays TBD. Description note: "Applies only at a horizontal speed of at least P-NAV-010, where the track is valid; at lower speeds a cross-track velocity tolerance is the meaningful measure. The mode section M5 sets the value and the measure." | A track tolerance in degrees is meaningless at 1 kt: a lateral velocity error of [P-AF-120] (0.5 m/s) is a track error of 44 deg there. AF does not use the track (IN-C6-10). |
| P-AF-170 | Value null to **0.25** m/s; TBD to TBR. | Half of [P-SYS-510] (0.5 m/s), so that a gust response at the touchdown stays inside the landing envelope (L1-AER-970, L2-AER-AF-650). Below [P-NAV-010] (0.514 m/s), so the track is invalid in a hold, as C6 assumed. |
| P-AF-180 | Value null to **0.008727** rad (0.5 deg); stays TBR. | Pitch and roll are held at zero at all times (D57). A tilt this size moves the height above the ground by 0.035 m (above), and the heading stays valid at any attitude below [P-NAV-030] (80 deg). FC confirms at I1. |
| P-AF-190 | Value null to **5** s; TBD to TBR. **Description changed** to: "Longest time from the instant the reference of a mode reaches its target until the controlled quantity is within its tolerance and stays there." | The present description ("from a capture onset or target change") cannot be a constant: a heading change of 180 deg takes 50 s, a climb of 10 000 ft at the standard speed 5 min, whatever the settling (conflict C5-C01). Needs the matching change of CONOPS §5 (CR-C5-03). |
| P-SYS-460 | Value unchanged (30 s, TBR). Description adds: "The hold starts as rule PR-4 of AF_MODE_LOGIC defines it: at the frame in which a mode that holds the horizontal position becomes active from a mode that does not, or from autoflight not engaged; a handover between holding modes does not restart it." | Closes the "when the hold starts is set by the mode logic (#78, C5)" part of TT-060. |
| P-AF-200, P-AF-230 | Value unchanged. Note added to P-AF-200: "The horizontal part of the manoeuvre acceleration is limited to the square root of (P-AF-200 squared minus P-AF-230 squared), 9.757 m/s2, so that the three-dimensional acceleration of the velocity reference stays within P-AF-200 (DD-C5-07)." | L2-AER-AF-420. The deceleration from [P-SYS-230] then takes 15.8 s, inside [P-SYS-460], and the turn at [P-SYS-230] allows 3.62 deg/s, above [P-SYS-270] (3.6 deg/s). |

## 2. YAML block

```yaml
  - id: P-AF-060
    name: Annunciation latency
    description: 'AF share of the aircraft-level annunciation latency P-SYS-470: at most P-SYS-470 minus P-TM-010.'
    unit: s
    value: 0.04
    tolerance: null
    note: 'C5. Two control frames (2 x P-SYS-310): the selection is taken at the next frame and processed in that frame (FUNCTIONAL_ANALYSIS §7.5). With P-TM-010 the total is 0.06 s, within P-SYS-470.'
    status: TBR
    source: L1-AER-470; L2-AER-AF-810; FUNCTIONAL_ANALYSIS §7.5; CONOPS §4.4, N-060
    owner: Martin
  - id: P-AF-090
    name: Vertical speed tracking tolerance
    description: Largest settled difference between vertical speed and selected vertical speed in Vertical speed mode, or in Go to altitude at a selected vertical speed. Also the largest vertical speed magnitude of a vehicle that is stationary at the hover height (L2-AER-AF-260).
    unit: m/s
    value: 0.1
    tolerance: null
    note: 'C5. About 20 ft/min. Refined at G3 (M2, M3, M8).'
    status: TBR
    source: CONOPS SC-020, SC-040, SC-050; L2-AER-AF-260, -600
    owner: Martin
  - id: P-AF-100
    name: Altitude capture maximum overshoot
    description: Largest overshoot of the selected altitude when Altitude hold captures it from Go to altitude or Vertical speed.
    unit: m
    value: 1.0
    tolerance: null
    note: 'C5. Tracking overshoot of the vehicle; the vertical reference itself does not overshoot (L2-AER-AF-560). Refined at G3 (M3).'
    status: TBR
    source: CONOPS SC-020; L2-AER-AF-590
    owner: Martin
  - id: P-AF-110
    name: Altitude hold tolerance
    description: Largest altitude error while Altitude hold or Hover holds an altitude.
    unit: m
    value: 0.05
    tolerance: null
    note: 'C5. In Hover with the landing gear extended (before Land descends, after Takeoff reaches the hover height, after a go-around) the altitude error plus the tilt effect must stay below P-AF-210 - P-DYN-040 (0.124 m): 0.05 m + 4 m x sin(P-AF-180) = 0.085 m, margin 0.039 m (IN-C1-44). FC confirms at I1.'
    status: TBR
    source: CONOPS SC-020 to SC-120; L2-AER-AF-260, -580, -720
    owner: Martin
  - id: P-AF-120
    name: Horizontal speed tracking tolerance
    description: Largest settled difference between horizontal speed (ground speed) and selected horizontal speed in Heading (there is no separate speed mode, D56).
    unit: m/s
    value: 0.5
    tolerance: null
    note: 'C5. One selection step (P-AF-030, 1 kt = 0.514 m/s). Refined at G3 (M5).'
    status: TBR
    source: CONOPS SC-040, SC-050, SC-060; L2-AER-AF-610
    owner: Martin
  - id: P-AF-130
    name: Heading tolerance
    description: Largest settled difference between heading and the selected or held heading.
    unit: rad
    value: 0.0175
    tolerance: null
    note: 'C5. 1 deg, one selection step (P-AF-040). Refined at G3 (M0, M5).'
    status: TBR
    source: CONOPS SC-060, SC-090
    owner: Martin
  - id: P-AF-140
    name: Track tolerance in Heading
    description: Largest difference between the track and the selected heading once Heading has settled at a non-zero horizontal speed. Applies only at a horizontal speed of at least P-NAV-010, where the track is valid.
    unit: rad
    value: null
    tolerance: null
    note: 'C5. Stays TBD for the mode section M5: an angular tolerance is meaningless at low speed (a lateral velocity error of P-AF-120 is 44 deg at 1 kt); M5 may replace it by a cross-track velocity tolerance.'
    status: TBD
    source: CONOPS SC-060; L2-AER-AF-530
    owner: Martin
  - id: P-AF-170
    name: Hover horizontal speed tolerance
    description: Largest horizontal speed once Go to hover or Hover has stopped the vehicle.
    unit: m/s
    value: 0.25
    tolerance: null
    note: 'C5. Half of P-SYS-510, so that a Land from Hover meets the landing envelope (L1-AER-970); below P-NAV-010, so the track is invalid in a hold.'
    status: TBR
    source: CONOPS SC-100; L2-AER-AF-260, -650
    owner: Martin
  - id: P-AF-180
    name: Level attitude tolerance
    description: Largest pitch or roll angle magnitude; pitch and roll are held at zero at all times (D10, D57).
    unit: rad
    value: 0.008727
    tolerance: null
    note: 'C5. 0.5 deg. Moves the height above the ground by at most 4 m x sin(0.5 deg) = 0.035 m (CV-400). FC confirms at I1.'
    status: TBR
    source: CONOPS §4.4, Q2; L2-AER-AF-400
    owner: Martin
  - id: P-AF-190
    name: Settling time
    description: Longest time from the instant the reference of a mode reaches its target until the controlled quantity is within its tolerance and stays there.
    unit: s
    value: 5
    tolerance: null
    note: 'C5. Changed from "from a capture onset or target change" (conflict C5-C01): the manoeuvre time depends on its size; the settling after the reference arrives does not. CONOPS §5 needs the matching change (CR-C5-03). Refined at G3.'
    status: TBR
    source: CONOPS §5; L2-AER-AF-580, -600, -610
    owner: Martin
```

The description-only changes of P-SYS-460 and the note of P-AF-200 are in §1; they have no YAML block here because their value is unchanged.

## 3. Checks and consequences

| Check | Result |
| --- | --- |
| Horizontal acceleration limit a_H | sqrt(9.80665^2 - 0.980665^2) = 9.7575 m/s2 |
| Deceleration from [P-SYS-230] (154.333 m/s) to zero | 15.8 s and 1221 m; inside [P-SYS-460] (30 s) |
| Heading rate allowed at [P-SYS-230] | 9.7575 / 154.333 = 0.06322 rad/s = 3.62 deg/s, at least [P-SYS-270] (0.062832 rad/s): [P-SYS-270] governs at the highest speed |
| Lateral acceleration at [P-SYS-230] and [P-SYS-270] | 154.333 x 0.062832 = 9.70 m/s2, within a_H |
| Level-off distance at [P-AF-220] and [P-AF-230] | 10.16^2 / (2 x 0.980665) = 52.6 m (173 ft), as the P-AF-230 note says |
| Level-off at [P-SYS-240] | 30.48^2 / (2 x 0.980665) = 473 m; the ramp takes 31 s |
| Gear clearance in Hover | 0.124 m against 0.085 m (P-AF-110 plus the tilt term): margin 0.039 m |
| [P-AF-170] against [P-SYS-510] and [P-NAV-010] | 0.25 m/s is at most 0.5 m/s and below 0.514 m/s |
| Annunciation latency | P-AF-060 (0.04 s) + P-TM-010 (0.02 s) = 0.06 s, at most [P-SYS-470] (0.5 s) |
| Position budget | [P-AF-160] (0.5 m) + [P-FC-010] (0.5 m) = 1.0 m = [P-SYS-450] |
| Vehicle acceleration | [P-AF-200] (1 g) + [P-FC-020] (0.5 g) = 1.5 g = [P-SYS-440] |
