# B1 — Glossary proposals

Terms used in the L1 statements (`work/B1/L1_AER.md`) or in `specs/FUNCTIONAL_ANALYSIS.md` that the fixed glossary does not define. Each is new; none changes a fixed definition. Format as in `specs/GLOSSARY.md`.

| Term | Proposed definition | Ref. | Used in |
| --- | --- | --- | --- |
| Axis demand | A force along, or a moment about, one body axis that the regulation function of *flight control* asks the allocation function to produce. Six per *control frame*. | FUNCTIONAL_ANALYSIS F-AER-05, -06 | L1-AER-630 |
| Axis reference | The value toward which *flight control* regulates one *degree of freedom*, produced by *autoflight*. Which quantity each reference is (velocity, position, rate, attitude) is set at L2 (C4, C5). | FUNCTIONAL_ANALYSIS F-AER-07; ICD-FC-AF | L1-AER-370, -420, -630 |
| Configuration (run) | The items a run is started with besides its *initial condition*: the *vehicle parameter set*, the *flight-control-law design* and the *autoflight implementation*, each with an identifier and a version. Not to be confused with *Aeronef configuration* (D42), which is the one verified combination. | CONOPS §4.6; N-350 | L1-AER-400, -410, -650, -690 |
| Crew selection | One data item of the *crew interface* by which the *crew* selects a mode or a *target* value, with its *timestamp*. | L0-CON-170; CONOPS §4.3 | L1-AER-480, -610, -690 |
| Dry mass | Vehicle mass with no fuel, `[P-FU-030]`. | CV-340 | L1-AER-180 |
| Effector command | The value the flight-control function sends to one *effector* for a *control frame*. | CV-330 | L1-AER-430, -630 |
| Effector output | The force (or moment) one *effector* produces along its fixed direction at a *simulation step*. | CV-330 | L1-AER-630, -710 |
| Event record | A time-stamped record of a discrete event in the *operational data*, for example a *ground contact* classified as a *landing* or a *crash*, or a fuel alert. | CV-840 | L1-AER-590, -640 |
| Final test report | The report that records the result of each verification procedure performed against the requirements of each level (L0-SUC-170). Each element contributes its section (D28). | L0-SUC-170 | L1-AER-820 |
| Flight software | The Aeronef functions that are replaceable through the *configuration*: navigation, autoflight and flight control, with the operational data output. Opposite of *vehicle model*. | FUNCTIONAL_ANALYSIS §5 | L1-AER-430 |
| Fuel mass flow | Mass of fuel consumed per unit of time, in kg/s, computed from the *effector outputs* through the consumption relationships. | CV-720 | L1-AER-160, -190, -630 |
| Fuel state | The *remaining fuel mass* and whether it is below the low-fuel threshold or at *fuel exhaustion*. | CONOPS §4.5 | L1-AER-430 |
| Heading rate | Rate of change of *heading*, dψ/dt, in rad/s. Not a *body rate* (CV-290). | CV-290 | L1-AER-350 |
| Indication | A vehicle quantity shown to the *crew* in its *crew-facing unit*, for example altitude, horizontal speed or remaining fuel. Distinct from an *annunciation*, which shows the autoflight state or an alert. | CONOPS §4.3; CV-760 | L1-AER-490, -500, -560 |
| Initial condition | The state a run starts from: position, velocity, attitude, *body rates*, fuel mass, autoflight mode state and *targets*, and the *VOR stations* of the run. Set by the TST. | CONOPS §4.6; N-310 | L1-AER-150, -660, -690 |
| Level file | The file `requirements/L<n>.md` that holds the requirements of one level, assembled from draft sections (plan §3, D2). | Plan §3 | L1-AER-750 |
| Low-fuel alert | The *annunciation* given when the *remaining fuel mass* falls below the fraction `[P-FU-020]` of `[P-FU-010]`. Its label is set at L2. | CONOPS §4.5 | L1-AER-570 |
| Maximum vehicle mass | *Dry mass* plus usable fuel mass at full capacity: `[P-FU-030]` + `[P-FU-010]`. | FUNCTIONAL_ANALYSIS §7 | L1-AER-120 to -140 rationales |
| Mode status | The autoflight information that *flight control* receives with the *axis references* across ICD-FC-AF (for example whether autoflight is *engaged*). Content set in ICD-FC-AF (I1). | ICD-FC-AF | L1-AER-420 |
| Operating volume | The region of nominal operation: *altitudes* from `[P-SYS-210]` to `[P-SYS-200]`, within a *horizontal distance* `[P-SYS-220]` of the local reference frame origin. | CONOPS §4.2 | L1-AER-310 to -350 |
| Operational manuals | The Vehicle Operating Manual, the normal procedures and the quick reference checklists of METHODOLOGY §11.2, written for an operator after the requirements baseline. | L0-OBJ-150 | L1-AER-840 |
| Reference position | The position that autoflight holds while it holds a fixed position. Whether it is the position at engagement or where the vehicle stops is set at L2 (#78). | Glossary *Position Hold*; D11 | L1-AER-460 |
| Remaining fuel mass | The usable fuel mass on board at a given time, in kg (crew-facing: lb). | CV-340 | L1-AER-180 to -200, -560 to -580, -640 |
| Requirements baseline | The complete baselined Aeronef requirement set, tag `AER-REQ-baseline-1`, approved at Gate G4. | Plan §6 G4 | L1-AER-800, -810 |
| Vehicle acceleration | Time derivative of the vehicle velocity in the local reference frame, in m/s². Not the *sensed acceleration*, which excludes gravity. | CV-460 | L1-AER-300 |
| Vehicle mass | *Dry mass* plus *remaining fuel mass*, in kg. | CV-340 | L1-AER-180, -430, -640 |
| Vehicle model | The part of the Aeronef that reproduces its physics: the DYN, FU and EF subsystems and MS-DYN. It is unchanged when the *flight-control-law design* or the *autoflight implementation* is replaced. | L0-CON-200, -210; FUNCTIONAL_ANALYSIS §5 | L1-AER-400, -410, -430, -670 |
| Vehicle model file | A source or data file of the *vehicle model*; its checksum shows that a replacement did not modify the model. | L0-CON-200 guidance | L1-AER-400, -410 |
| Vehicle parameter set | The values of the vehicle model parameters used in a run, identified by a version. | N-350 | L1-AER-650 |
| Vehicle state | Position, velocity, attitude (quaternion, with Euler angles derived), *body rates* and *vehicle acceleration* of the vehicle at a *simulation step*. | CV-250, CV-410, CV-460 | L1-AER-430, -440, -640 |
| Wind speed | Magnitude of the *wind* velocity, in m/s. | CV-470 | L1-AER-310, -460 |

**Not proposed.** "Holding a fixed position" (L1-AER-360, -460) is used in its plain meaning, without a mode name, so that L1 stays mode-free (D33). The mode that does it is *Position Hold* at L2.
