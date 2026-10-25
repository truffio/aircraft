# A2 — Interface needs

What `specs/CONOPS.md` assumes from, or provides to, other tasks. The CONOPS section is given for each item.

## From A3 — Conventions and glossary

CONOPS §4.2 assumes the following. If CONVENTIONS chooses differently, the affected CONOPS text changes, but the scenarios stay valid.

| Item | Assumed in CONOPS |
| --- | --- |
| Local reference frame | Earth-fixed, flat ground plane, axes north, east and vertical. NED versus ENU does not matter to the ConOps. |
| Altitude datum | Height of the vehicle reference point above the ground plane, positive up; ground plane at zero altitude. |
| North reference | Local frame north axis (true north). Heading, track, course and VOR radials are referenced to it. No magnetic variation. |
| Heading | Direction the nose points, projected on the horizontal plane, clockwise from north. |
| Track | Direction of the horizontal velocity, clockwise from north. Undefined at zero horizontal speed. |
| Heading versus track | Independent on the Aeronef. CONOPS uses both and never treats one as the other. |
| Horizontal speed | Magnitude of the horizontal velocity. Same relative to air and ground in still air (A2-Q01). |
| Vertical speed | Rate of change of altitude, positive up. Crew-facing sign: positive for climb. |
| Flight path angle | Angle of the velocity vector above the horizontal plane, positive up. Undefined at rest. |
| VOR radial and course | Radial: bearing from the station, from true north. Course: the selected direction of motion along the radial line; outbound course = radial; inbound course = radial + 180°. |
| Angle display range | Crew-facing headings, tracks and courses shown 000 to 359 degrees (A3 to decide 000 or 360 for north). |
| Time base | Simulation time from the start of the run, used for selections, annunciations and data. |
| Crew-facing conversions | ft, ft/min, kt, NM, degrees (D7). Fuel unit not covered by D7 (A2-Q09; proposed percent of full capacity). |
| Glossary | Terms in `glossary_proposals.md`. |

## To A1 — L0

- CONOPS needs N-010 to N-440 are available as Source for L0-OBJ, L0-CON and L0-SUC statements.
- CONOPS §4.2 relies on these L0 assumptions or constraints: exact state knowledge (assumption); still air (A2-Q01, constraint or assumption); no ground contact, take-off or landing (A2-Q02); fixed centre of gravity; no electrical system.

## To B1 — Functional analysis and L1

- Mode groups, armed versus active, capture and the attitude rules in CONOPS §4.4 are the operational view of Q2 and Q5. B1 proposes the final answers; CONOPS will be updated.
- Performance envelope parameters P-SYS-200 to P-SYS-280 are proposed for L1 budgets.
- The crew interface (CONOPS §4.3) is a logical interface of the Aeronef. B1 to decide whether it is an L1 interface (Aeronef ↔ STP, carrying crew selections) or an Aeronef-internal function.

## To C2 — Fuel and mass properties

- Fuel quantity indication to the crew (unit: A2-Q09).
- LOW FUEL at P-FU-020; FUEL EXHAUSTED at zero usable fuel.
- At exhaustion, the effectors produce zero force and zero moment.
- Fuel is consumed in every flight condition, including hover (gravity must be countered).
- Hover endurance at full fuel and maximum mass, P-SYS-280.

## To C1 — Dynamics model

- Uniform gravity toward the ground plane (or the gravity model MS-DYN defines).
- Drag relative to still air.
- After fuel exhaustion, the motion is free fall with drag and the angular rate continues (torque-free unless drag moments are modelled). CONOPS SC-110 leg 10 relies on this as an analytical check (N-290).
- Ground plane reached ends the run; no ground-contact model.

## To C4 — Flight control

- Pitch and roll held level within P-AF-180 in every autoflight mode (TBR Q2). The references come from autoflight.
- Heading and track commanded independently (SC-070).
- Vertical climb at zero horizontal speed without tilting (SC-040).

## To C5 — Autoflight core (AF_MODE_LOGIC)

- Provisional annunciation labels used in CONOPS: FPA, V/S, ALT (armed and hold), ALT*, SPD, HDG, TRK, VOR (armed and tracking), VOR*, POS HOLD, HOVER; alerts LOW FUEL, FUEL EXHAUSTED. C5 owns the final labels and how armed and active are distinguished.
- Behaviours CONOPS assumes and C5 must define:
  - arming of altitude capture when a climb or descent mode is engaged with the selected altitude in the direction of motion (and what happens when it is not);
  - capture onset and the criterion for ALT* → ALT and VOR* → VOR;
  - direct engagement of ALT: which altitude is held (SC-050 step 5);
  - heading change direction (shorter way) in HDG;
  - FPA not engaging below P-AF-070 (A2-Q06);
  - one active mode per group always (A2-Q05);
  - hold modes replacing all three groups (A2-Q07) and how they are left (A2-Q10);
  - mode state after fuel exhaustion (A2-Q04);
  - whether a change of selected altitude during ALT* or ALT changes anything.

## To C6 — Navigation

- VOR stations defined per run by the STP, fixed in the local frame, identified by an identifier.
- Indications: course deviation, distance to station in NM (TBR Q4).
- Reception range P-NAV-050. CONOPS scenarios start within range and end before station passage (A2-Q08).
- Navigation quantities CONOPS uses: position, altitude, heading, track, horizontal speed, vertical speed, flight path angle.

## To C7 — Operational data output

- Every item below on one time base, at each simulation step: crew selections received; selected targets; active and armed modes; annunciations; indications; vehicle state; fuel quantity; flight-control and effector activity (CONOPS §4.6).
- Releasable versus protected classification for each signal (SC-240).
- Data needed to compare versions on the reference mission: fuel used per leg, tracking errors per leg (SC-110, SC-220). The leg boundaries are crew-selection events, so they can be found from the selection log.

## To the STP side of ICD-AER-STP (I1)

- Configuration input: parameter set, control-law version, autoflight version, each identified (N-350).
- Initial condition input: position, velocity, attitude, angular rate, fuel, active and armed modes, targets, VOR stations (N-310).
- Crew selections applied at stated simulation times, through the same crew interface a human uses (N-320, SC-230).
- Run end: scenario end condition, maximum run time, ground plane reached (N-370).
- Reproducibility: same configuration, initial condition and selection script give the same data (N-330). The STP must state the criterion (bit-identical on the same build and platform is proposed).
- Instance independence for parallel runs (SC-210).
- Faster than real time without graphics; real time for interactive runs.
