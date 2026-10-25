# A2 — Parameter proposals

Parameters referenced by `specs/CONOPS.md`. All values are TBD. The orchestrator assigns the final IDs (B2). Field layout follows `parameters/PARAMETERS.yaml`.

Notes for the orchestrator:

- The IDs below are the ones used in CONOPS.md. If B2 renumbers them, CONOPS.md needs the same renumbering.
- These are **system** values: envelope, tolerances, thresholds. Scenario values (initial altitude, selected targets, leg durations) are not proposed as parameters. CONOPS.md writes them as scenario variables in `CODE` font, and the test procedures set them (question A2-Q12).
- The METHODOLOGY §12 worked example uses `P-AF-012` (position hold tolerance) and `P-AF-014`. Those IDs are illustrative and do not follow the steps-of-10 rule. This proposal uses `P-AF-160` for the position hold tolerance.
- The tolerances P-AF-080 to P-AF-170 and the settling time P-AF-190 are placeholders, one per quantity. The Phase 4 mode agents (M0 to M8) are expected to split them per mode where needed.
- The crew-facing unit is given in the description where the crew selects or sees the quantity (D7). The database unit is always SI.

```yaml
parameters:
  # --- System envelope and operating volume ---
  - id: P-SYS-200
    name: Maximum operating altitude
    description: Highest altitude above the ground plane for nominal operation. Upper limit of the selected altitude (crew-facing ft).
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.2, SC-010
    owner: Martin
  - id: P-SYS-210
    name: Minimum operating altitude
    description: Lowest altitude above the ground plane for nominal operation. Lower limit of the selected altitude and of scenario initial altitudes (crew-facing ft).
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.2, §5, SC-020
    owner: Martin
  - id: P-SYS-220
    name: Horizontal operating radius
    description: Radius, around the local frame origin, of the horizontal region of nominal operation (crew-facing NM).
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.2
    owner: Martin
  - id: P-SYS-230
    name: Maximum horizontal speed
    description: Highest horizontal speed reached in autoflight. Upper limit of the selected horizontal speed (crew-facing kt).
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5, N-170
    owner: Martin
  - id: P-SYS-240
    name: Maximum climb vertical speed
    description: Highest upward vertical speed reached in autoflight. Upper limit of a positive selected vertical speed (crew-facing ft/min).
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5, SC-040, N-170
    owner: Martin
  - id: P-SYS-250
    name: Maximum descent vertical speed
    description: Highest downward vertical speed (magnitude) reached in autoflight. Limit of a negative selected vertical speed (crew-facing ft/min).
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5, SC-020, SC-030, N-170
    owner: Martin
  - id: P-SYS-260
    name: Maximum flight path angle magnitude
    description: Largest magnitude of selectable flight path angle, climb or descent (crew-facing degrees).
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5, SC-010, N-170
    owner: Martin
  - id: P-SYS-270
    name: Maximum heading rate in autoflight
    description: Highest rate of change of heading during an autoflight heading change.
    unit: rad/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5, SC-050, SC-060, N-170
    owner: Martin
  - id: P-SYS-280
    name: Minimum hover endurance at full fuel
    description: Shortest time from engagement of Hover at Altitude with full fuel at maximum mass to fuel exhaustion.
    unit: s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-110 (variation hover endurance)
    owner: Martin

  # --- Fuel ---
  - id: P-FU-010
    name: Usable fuel mass at full capacity
    description: Mass of usable fuel when the tank is full. Initial fuel of the reference mission.
    unit: kg
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.5, SC-110
    owner: Martin
  - id: P-FU-020
    name: Low-fuel threshold
    description: Remaining fuel, as a fraction of P-FU-010, below which LOW FUEL is annunciated.
    unit: "1"
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.5, SC-110, N-150
    owner: Martin

  # --- Autoflight: crew selection resolution (D7 crew-facing units) ---
  - id: P-AF-010
    name: Altitude selection resolution
    description: Smallest step of the selected altitude. Expected to be a round value in ft; stored in SI.
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.3, §5, N-070
    owner: Martin
  - id: P-AF-020
    name: Vertical speed selection resolution
    description: Smallest step of the selected vertical speed. Expected to be a round value in ft/min; stored in SI.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.3, §5, N-070
    owner: Martin
  - id: P-AF-030
    name: Horizontal speed selection resolution
    description: Smallest step of the selected horizontal speed. Expected to be a round value in kt; stored in SI.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.3, §5, N-070
    owner: Martin
  - id: P-AF-040
    name: Heading, track and course selection resolution
    description: Smallest step of the selected heading, selected track and selected VOR course. Expected to be a round value in degrees; stored in SI.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.3, §5, N-070
    owner: Martin
  - id: P-AF-050
    name: Flight path angle selection resolution
    description: Smallest step of the selected flight path angle. Expected to be a round value in degrees; stored in SI.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.3, §5, N-070
    owner: Martin

  # --- Autoflight: annunciation and mode availability ---
  - id: P-AF-060
    name: Annunciation latency
    description: Longest time from a change of active mode, armed mode, target or alert condition to its annunciation.
    unit: s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §4.4, §5, SC-110, N-060
    owner: Martin
  - id: P-AF-070
    name: Minimum horizontal speed for FPA mode
    description: Horizontal speed below which the FPA mode does not engage (question A2-Q06).
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010, SC-040
    owner: Martin

  # --- Autoflight: tracking and hold tolerances (placeholders, split per mode in Phase 4) ---
  - id: P-AF-080
    name: Flight path angle tracking tolerance
    description: Largest settled difference between flight path angle and selected flight path angle in FPA mode.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010, SC-030
    owner: Martin
  - id: P-AF-090
    name: Vertical speed tracking tolerance
    description: Largest settled difference between vertical speed and selected vertical speed in V/S mode.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-020, SC-040, SC-050
    owner: Martin
  - id: P-AF-100
    name: Altitude capture maximum overshoot
    description: Largest distance by which the altitude passes the selected altitude during altitude capture.
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010, SC-020
    owner: Martin
  - id: P-AF-110
    name: Altitude hold tolerance
    description: Largest settled difference between altitude and the held altitude in altitude hold and in Hover at Altitude.
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010 to SC-100
    owner: Martin
  - id: P-AF-120
    name: Horizontal speed tracking tolerance
    description: Largest settled difference between horizontal speed and selected horizontal speed in SPD mode.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010, SC-040, SC-050, SC-060, SC-070
    owner: Martin
  - id: P-AF-130
    name: Heading hold tolerance
    description: Largest settled difference between heading and the selected or held heading.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-010, SC-060, SC-070, SC-080, SC-090
    owner: Martin
  - id: P-AF-140
    name: Track hold tolerance
    description: Largest settled difference between track and the selected track (TRK) or selected course (VOR), and between track and heading in HDG.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-060, SC-070, SC-080
    owner: Martin
  - id: P-AF-150
    name: VOR radial tracking tolerance
    description: Largest settled angular deviation of the vehicle from the selected radial, seen from the station.
    unit: rad
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-080
    owner: Martin
  - id: P-AF-160
    name: Position hold tolerance
    description: Largest settled distance between the vehicle position and the Position Hold reference position.
    unit: m
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-090
    owner: Martin
  - id: P-AF-170
    name: Hover horizontal speed tolerance
    description: Largest settled horizontal speed in Hover at Altitude.
    unit: m/s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS SC-100
    owner: Martin
  - id: P-AF-180
    name: Level attitude tolerance
    description: Largest magnitude of pitch angle and of roll angle while autoflight holds them level (Q2).
    unit: rad
    value: null
    tolerance: null
    status: TBR
    source: CONOPS §4.4, Q2
    owner: Martin
  - id: P-AF-190
    name: Settling time
    description: Longest time from a capture onset or target change until the controlled quantity is within its tolerance.
    unit: s
    value: null
    tolerance: null
    status: TBD
    source: CONOPS §5
    owner: Martin

  # --- Navigation ---
  - id: P-NAV-050
    name: VOR reception range
    description: Distance from a VOR station within which its signal is received (Q4). Crew-facing NM where shown.
    unit: m
    value: null
    tolerance: null
    status: TBR
    source: CONOPS §4.2, SC-080, Q4
    owner: Martin
```
