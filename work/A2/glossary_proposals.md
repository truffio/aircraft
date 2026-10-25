# A2 — Glossary proposals

Terms used in `specs/CONOPS.md`. Definitions are proposals for A3, who owns `specs/GLOSSARY.md`. Where A3's definition differs, A3's wins and CONOPS is updated.

| Term | Proposed definition |
| --- | --- |
| Active mode | The autoflight mode that currently controls its mode group. |
| Altitude | Height of the vehicle reference point above the ground plane, positive up. |
| Altitude capture | The autoflight mode that takes the vehicle from a climb or descent to the selected altitude, then hands over to altitude hold. Annunciated ALT when armed and ALT* while capturing (provisional labels). |
| Altitude hold | The autoflight vertical mode that holds an altitude. |
| Annunciation | A crew-visible indication of the active modes, the armed modes, the selected targets or an alert. |
| Arm | To set a mode so that it becomes active automatically when its capture condition is met. |
| Armed mode | A mode that waits for its capture condition and does not yet control its group. |
| Capture | The change of an armed mode to active when its condition is met. |
| Capture onset | The moment an armed mode starts to capture. |
| Course (selected course) | The direction of motion, along a VOR radial line, that VOR radial tracking flies. Outbound course equals the radial; inbound course is the radial plus 180 degrees. |
| Crew | Whoever makes crew selections and reads annunciations: a human operator, a scripted test procedure or an REE agent. |
| Crew interface | The logical set of crew selections, annunciations and indications of the Aeronef. Not a physical panel or display design. |
| Crew selection | A crew input: a selected target or a mode engage or arm command. |
| Crew-facing units | The units of crew selections and annunciations (D7): ft, ft/min, kt, NM, degrees. |
| Disengage | To stop a mode, by selecting another mode in its group or a hold mode. |
| Engage | To make a mode active by a crew selection. |
| Flight path angle | Angle of the vehicle velocity above the horizontal plane, positive up. |
| Fuel exhaustion | The state where usable fuel is zero. Nominal behaviour: the effectors produce zero force and moment. Annunciated FUEL EXHAUSTED (provisional). |
| Ground plane | The flat plane at zero altitude in the local reference frame. |
| Heading | Direction the vehicle nose points, projected on the horizontal plane, measured clockwise from north. Independent of track on the Aeronef. |
| Heading hold | The autoflight lateral mode that holds the selected heading (provisional label HDG). |
| Hold mode | Position Hold or Hover at Altitude: a mode that replaces the vertical, lateral and speed groups while active. |
| Horizontal speed | Magnitude of the horizontal velocity. |
| Horizontal speed mode | The autoflight speed mode that holds the selected horizontal speed (provisional label SPD). |
| Hover at altitude | The hold mode that holds altitude and zero horizontal velocity, without holding a horizontal position (TBR Q3). |
| Indication | A crew-visible value of the vehicle state, fuel or navigation (for example the current altitude). |
| Initial condition | The vehicle state, fuel, modes, targets and VOR stations at the start of a run. |
| Level attitude | Pitch angle and roll angle both zero within tolerance. |
| Low fuel | The state where remaining fuel is below the low-fuel threshold. Annunciated LOW FUEL. |
| Mode group | A set of autoflight modes of which exactly one is active at a time: vertical, lateral or speed (TBR Q5). |
| Need | A stakeholder's expectation, in their words, recorded with an ID (`N-nnn`) in the ConOps. |
| Operating volume | The altitude band and horizontal region within which nominal operations take place. |
| Operational data | Data the Aeronef outputs at each step: selections, targets, modes, annunciations, state, fuel, control activity. |
| Position hold | The hold mode that holds the three-dimensional position the vehicle had at engagement (provisional label POS HOLD). |
| Protected (data) | Operational data or documents that must not reach the REE. |
| Radial | A line from a VOR station, identified by its bearing from the station, measured from true north. |
| Reception range | Distance from a VOR station within which its signal is received. |
| Reference mission | The fixed, repeatable profile of SC-110, flown to fuel exhaustion, used to compare versions. |
| Releasable (data) | Operational data that may be given to the REE. |
| Run | One execution of the Aeronef in the STP, defined by a configuration, an initial condition and a selection script. |
| Scenario | A described sequence of operations in the ConOps (`SC-nnn`). |
| Scenario variable | A named value in a scenario (for example `H_SEL`) whose number the test procedure chooses. |
| Selected altitude, heading, track, speed, vertical speed, flight path angle | The crew-selected target of the corresponding mode. |
| Selection script | The list of crew selections, each with a simulation time, applied during a run. |
| Settled | Within the stated tolerance, reached within the settling time and kept. |
| Stakeholder | A person or group that uses, builds, tests, reviews or consumes the project's outputs (`SH-nn`). |
| Still air | Air at rest relative to the ground plane. |
| Track | Direction of the horizontal velocity, measured clockwise from north. Undefined at zero horizontal speed. |
| Track hold | The autoflight lateral mode that holds the selected track (provisional label TRK). |
| Vertical speed | Rate of change of altitude, positive up. |
| VOR radial tracking | The autoflight lateral mode that intercepts and tracks a selected radial of a selected VOR station (provisional labels VOR armed, VOR*, VOR). |
| VOR station | A simulated ground radio station at a fixed position in the local frame, used by VOR radial tracking. |
