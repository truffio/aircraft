# A3 — Parameter proposals

Proposed by A3 (conventions). The orchestrator assigns final IDs in `parameters/PARAMETERS.yaml` (task B2). The IDs below are the ones CONVENTIONS.md cites; if B2 renumbers, CONVENTIONS.md must be updated with them. All values are TBD; owner Martin.

The subsystem prefixes are proposals: `P-SYS` for timing shared across subsystems, `P-DYN` for the gravity magnitude (owned by MS-DYN, C1), `P-NAV` for validity thresholds (C6), `P-TM` for crew display resolution (C7, with AF for the selection side).

| Proposed ID | Name | Description | Unit | Value | Status | Source / cited by |
| --- | --- | --- | --- | --- | --- | --- |
| P-SYS-300 | Simulation step | Fixed duration `Δt` of one vehicle-model simulation step | s | null | TBD | CV-820; F-TST-01; ICD-AER-TST |
| P-SYS-310 | Control frame period | Period of one execution of the flight-control and autoflight functions | s | null | TBD | CV-830; ICD-AER-TST, ICD-FC-AF |
| P-TM-010 | Output sample period | Period of one operational data record | s | null | TBD | CV-830; TM (C7) |
| P-DYN-010 | Gravitational acceleration | Magnitude of the uniform gravitational acceleration along `+z_L` | m/s² | null (candidate: 9.80665, standard gravity) | TBD | CV-110; MS-DYN (C1) |
| P-NAV-010 | Track validity speed | Minimum horizontal speed for which track is valid | m/s | null | TBD | CV-540, CV-580; NAV (C6) |
| P-NAV-020 | Flight path angle validity speed | Minimum total speed for which flight path angle is valid | m/s | null | TBD | CV-560, CV-580; NAV (C6) |
| P-NAV-030 | Heading validity pitch limit | Maximum absolute pitch angle for which heading and roll angle are valid | rad | null | TBD | CV-260, CV-580; NAV (C6) |
| P-NAV-040 | VOR radial validity distance | Minimum horizontal distance from a VOR station for which the radial is valid | m | null | TBD | CV-580, CV-620; NAV (C6) |
| P-NAV-050 | VOR reception range | Distance from a VOR station within which its signal is received (horizontal distance or slant range per Q4) | m | null | TBD (Q4) | CV-670; NAV (C6) |
| P-TM-020 | Altitude display resolution | Resolution of altitude values shown to the crew | ft (crew-facing, if G0-10 adopted) | null | TBD | CV-780 |
| P-TM-030 | Vertical speed display resolution | Resolution of vertical speed values shown to the crew | ft/min (crew-facing) | null | TBD | CV-780 |
| P-TM-040 | Speed display resolution | Resolution of horizontal speed values shown to the crew | kt (crew-facing) | null | TBD | CV-780 |
| P-TM-050 | Direction angle display resolution | Resolution of heading, track, course and radial values shown to the crew | deg (crew-facing) | null | TBD | CV-780 |
| P-TM-060 | Distance display resolution | Resolution of horizontal distance values shown to the crew | NM (crew-facing) | null | TBD | CV-780 |
| P-TM-070 | Flight path angle display resolution | Resolution of flight path angle values shown to the crew | deg (crew-facing) | null | TBD | CV-780 |

Notes:

1. **Crew-facing units.** P-TM-020 to P-TM-070 are in crew-facing units only if G0-10 is decided as recommended (crew-facing parameters stored in crew units and marked). Otherwise their units become m, m/s and rad.
2. **Selection resolutions.** The selection steps for each selectable target (altitude, vertical speed, horizontal speed, heading, track, flight path angle, course) are AF parameters. They are left to C5 and the Phase 4 mode agents, which own those requirements. They follow the same crew-facing rule.
3. **Display rounding rule.** The rounding rule from SI to the shown value (CV-780) is a requirement decision for TM and AF, not a numeric parameter. It is listed in `issues.md`.
4. **No numbers for conventions.** The conversion factors (CV-750) and the angle ranges (CV-230) are exact definitions, not parameters.
