# Aeronef Concept of Operations (Aeronef-relevant)

**Status:** Reviewed at Gate G0 (2026-10-27). The mode material (§4.4 and the mode details of the scenarios) is provisional input for L2 (#89).
**Date:** 2026-10-27
**Owner:** Martin
**Information class:** Protected design material. This document is not released to the Reverse-Engineering Effort, and it is not operator-facing manual text.

## 1. Purpose and scope

This document describes how the Aeronef is used, from the point of view of the people and procedures that operate it. It gives:

- the stakeholders and their needs, each need with an ID (`N-nnn`) that L0 and L1 requirements cite in their Source attribute;
- the operational context: the simulated environment, the role of the crew, the autoflight operating concept, and how the Simulation and Testing Platform (STP) and the Reverse-Engineering Effort (REE) use the Aeronef's operational data;
- nominal scenarios (`SC-nnn`) that cover the autoflight mode catalogue (AIRCRAFT_REQUIREMENTS_PLAN.md §9, D3), a reference mission to fuel exhaustion, and the platform uses of the Aeronef;
- the parts of the scenarios that are still open, marked **TBR** with the issue that tracks them. The owner decided the plan's questions Q2 to Q4 on 2026-10-25 (D10 to D12). Mode combinations (Q5, #6) and the detailed mode logic are deferred to L2 (D33), so the mode behaviour in the scenarios is provisional;
- a traceability table from scenario to needs and modes.

The document follows the NASA ConOps outline (METHODOLOGY 4.2), trimmed to the Aeronef. It describes operations, not design. It contains no control laws, algorithms or emitter layouts.

**Tailoring.** Hazard and failure analysis is deferred (METHODOLOGY, tailoring note). There are no failure scenarios. Fuel exhaustion is nominal behaviour (SC-110). Effector saturation is nominal behaviour and is not a scenario of its own.

**Not covered.** The Simulation and Testing Platform's and the Reverse-Engineering Effort's own operations, except where they use the Aeronef (Section 6.3). Take-off and ground operations. Landing is covered only as an ideal landing (Section 4.2, D37). Manual control, which is an optional feature that is not developed (Section 4.3).

### 1.1 Conventions used in this document

- Physical quantities in descriptions are in SI units. Crew selections and annunciations use the crew-facing units of D7, D9 and D34: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track, course, flight path angle), lb (fuel), and hours or minutes (durations). The unit table and the conversions are in `specs/CONVENTIONS.md` (CV-740, CV-750).
- System and scenario values never appear as numbers in the text; only definitional constants do (for example the 180 degrees between a radial and its reciprocal). System values are parameters `[P-<SUB>-<NNN>]`, proposed in `work/A2/param_proposals.md` with their values TBD. Scenario values (initial altitude, selected targets, durations) are **scenario variables** written in `CODE` font. The test procedures choose their values within the ranges this document states.
- The frame, axis and angle conventions are those of `specs/CONVENTIONS.md`. Until that document is baselined, this document assumes the definitions in Section 4.2. The assumptions are recorded in `work/A2/interface_needs.md`.
- Mode names are the D3 names. The short labels (FPA, V/S, ALT*, and so on) are **provisional annunciation labels** used to make the scenarios readable. The autoflight mode logic (`specs/AF_MODE_LOGIC.md`, task C5) owns the final labels.

### 1.2 Reference documents

| Document | Used for |
| --- | --- |
| OBJECTIVES.md | Stakeholders, project objectives, success criteria |
| AIRCRAFT_CHARACTERISTICS.md | Vehicle concept and modelling boundaries |
| TESTING_ENVIRONMENT.md | STP use of the Aeronef |
| REVERSE_ENGINEERING.md | REE use of the Aeronef, information separation |
| AIRCRAFT_REQUIREMENTS_PLAN.md | Decisions D1 to D44 (§9) |
| METHODOLOGY.md | Stakeholder and ConOps method (Section 4), writing rules (Section 8), worked example (Section 12) |

## 2. Stakeholders

| ID | Stakeholder | Interest in the Aeronef |
| --- | --- | --- |
| SH-01 | Project owner | Owns the experiment, decides open questions, approves baselines. Wants a vehicle that is simple enough to understand completely and rich enough to exercise the whole lifecycle. |
| SH-02 | Crew (human operator, scripted test procedure or REE agent) | Commands the vehicle through autoflight selections and monitors it through annunciations and indications. |
| SH-03 | Autoflight designers | Adapt airliner autoflight modes to a vehicle whose attitude and translation are independent; develop the autoflight implementation (one, D24). |
| SH-04 | Control-law designers | Develop the flight-control-law design (one for now, D42); more designs may be added later. |
| SH-05 | Vehicle model developers | Build the dynamics, effector, fuel and mass model that the simulation reproduces. |
| SH-06 | Simulation and test engineers (STP) | Run the Aeronef unattended, in parallel and reproducibly; assess results against requirements; explore it interactively. |
| SH-07 | Reverse-engineering team (REE) | Reconstruct the Aeronef's functions and logic from manuals, observed behaviour and operational data, without the design. |
| SH-08 | Project evaluators | Compare the REE's reconstruction with the authoritative design and requirements. |
| SH-09 | Operational documentation authors | Write the human-oriented manuals and procedures that become REE evidence. |
| SH-10 | Peer reviewers | Judge each artifact against its inputs and the checklists. |

## 3. Needs

Each need is recorded in the stakeholder's words, then restated as what it means for the Aeronef. Needs are not requirements: L0 and L1 requirements are written from them and cite them as Source. IDs are numbered in steps of 10 and never reused.

| ID | Stakeholder | Need (stakeholder's words) | What it means for the Aeronef |
| --- | --- | --- | --- |
| N-010 | SH-01 | "I want a vehicle simple enough to understand completely, but rich enough to exercise design, test and reverse engineering." | The Aeronef is bounded by the modelling boundaries of AIRCRAFT_CHARACTERISTICS §7, and every behaviour it has is specified. |
| N-020 | SH-01 | "Every value should be changeable without rewriting requirements." | Every configurable value of the Aeronef is a parameter with an ID, an SI unit and a status. |
| N-030 | SH-01 | "The original design must stay hidden from the reverse-engineering team." | The Aeronef's outputs are split into releasable and protected data; nothing released exposes protected design. |
| N-040 | SH-01 | "Everything must trace from an objective down to a test." | Each Aeronef behaviour in this ConOps is traceable to a need, and from there to requirements and verification. |
| N-050 | SH-02 | "I fly this vehicle through autoflight. Flying six axes by hand isn't practical." | Autoflight is the primary means of controlling the vehicle; each nominal operation in this ConOps is flown in autoflight. |
| N-060 | SH-02 | "I need to know which mode is active, which is armed, and what the vehicle will do next." | The Aeronef annunciates the active mode of each mode group, the armed modes and the selected targets. |
| N-070 | SH-02 | "I want to enter targets in the units I'm used to: feet, feet per minute, knots, nautical miles and degrees." | Crew selections and annunciations use the D7 crew-facing units. |
| N-080 | SH-02 | "When the climb reaches the altitude I set, I want it to level off and hold without me doing anything." | Altitude capture arms with the climb or descent mode and leads automatically to altitude hold. |
| N-090 | SH-02 | "I want to change a target while a mode is flying it, and see the vehicle go to the new target." | Targets of active modes can be changed at any time, and the vehicle acquires the new target. |
| N-100 | SH-02 | "I want to choose a different mode at any time." | The crew can select another mode in any group at any time; the new mode replaces the old one. |
| N-110 | SH-02 | "I need to point the nose one way and move another way." | The Aeronef's heading (where the nose points) and track (the direction of horizontal motion) can differ, and the modes say which one they control. |
| N-120 | SH-02 | "I want to fly to and along a radial of a radio station." | The Aeronef provides VOR radial interception and tracking. |
| N-130 | SH-02 | "I need to stop and stay in one place." | The Aeronef can hold a three-dimensional position. |
| N-140 | SH-02 | "I need to stop moving horizontally and stay at my altitude." | The Aeronef can hover at an altitude. |
| N-150 | SH-02 | "I need to see how much fuel is left, get a warning before it runs out, and know what happens when it does." | The Aeronef indicates the remaining fuel, alerts at a low-fuel threshold and has a defined behaviour at fuel exhaustion. |
| N-160 | SH-02 | "The vehicle's attitude should be predictable while the modes fly the path." | Each mode states what the pitch, roll and heading do while it is active (D10). |
| N-170 | SH-02 | "Climb rate, speed and turn rate should stay within known limits so I can plan." | The Aeronef has a stated performance envelope, including the crew acceleration limit (L0-CON-310), and autoflight keeps the vehicle within it. |
| N-180 | SH-02 | "If a manual control option is ever added, I want to command the axes directly." | Manual control is an optional feature; it is recorded and not developed. |
| N-190 | SH-03 | "We need airliner-like modes, adapted to a vehicle that can translate without turning or tilting." | The D3 modes are defined in terms of the Aeronef's independent attitude and translation. |
| N-200 | SH-03 | "We need to know which modes can be active together." | The modes are organised in groups with defined combinations (#6, L2). |
| N-210 | SH-03 | "We need modes a crew can understand from the annunciations alone." | Each mode, arming, capture and transition is annunciated with a distinct label. |
| N-220 | SH-03 | "We need to compare autoflight versions under the same conditions." | The autoflight implementation can be swapped without changing the vehicle model, the crew interface or the scenarios. Comparing versions is not an objective this cycle (D24, D42); the need is kept for later. |
| N-230 | SH-04 | "We need to swap controllers without touching the vehicle model." | The flight-control law can be swapped through configuration; the vehicle model and parameter set stay the same. |
| N-240 | SH-04 | "We need each axis regulated on its own, since nothing couples the axes." | Each of the three translational and three rotational axes can be commanded independently. |
| N-250 | SH-04 | "We need to measure the control law's accuracy and fuel used, flying the same profile." | A reference mission with a fixed profile exists, and the Aeronef reports the data needed to measure accuracy and fuel used. |
| N-260 | SH-04 | "We need the vehicle to behave in a defined way when the effectors reach their limits." | Effector saturation is nominal, defined behaviour. |
| N-270 | SH-05 | "We need the physics written down: six degrees of freedom, gravity, drag, mass and inertia." | The Aeronef's motion follows a model specification (MS-DYN). |
| N-280 | SH-05 | "Fuel use for translation and for rotation must be configurable, and mass must go down as fuel burns." | Fuel consumption has configurable linear and rotational terms; vehicle mass decreases with fuel used. |
| N-290 | SH-05 | "We need to check the model against hand calculations." | The Aeronef's behaviour in simple cases (free fall after fuel exhaustion, steady hover) can be compared with independent solutions. |
| N-300 | SH-06 | "Every requirement should have a test that runs unattended." | Every Aeronef operation can be driven by a script, without a human and without graphics. |
| N-310 | SH-06 | "I need to set up the whole starting state: position, velocity, attitude, fuel, modes and targets." | The Aeronef accepts a complete initial condition at the start of a run, including the active and armed modes and their targets. |
| N-320 | SH-06 | "My script must make crew selections at given times." | Crew selections can be applied at a stated simulation time, through the same crew interface a human uses. |
| N-330 | SH-06 | "The same inputs must give the same results, and many runs must go in parallel without affecting each other." | An Aeronef run is reproducible from its configuration, initial condition and selection script, and instances are independent. |
| N-340 | SH-06 | "I need the vehicle to report its state, modes, targets and commands at each step, so the test can judge them." | The Aeronef outputs operational data at each simulation step. |
| N-350 | SH-06 | "I need to know which version and configuration produced a result." | Each run identifies the vehicle parameter set, the control-law version and the autoflight version it used. |
| N-360 | SH-06 | "I want to fly it interactively and watch what happens." | The same Aeronef can run in real time and accept selections from a human at any time. |
| N-370 | SH-06 | "Runs must end in a defined way." | Each run has defined end conditions (Section 4.6). |
| N-380 | SH-07 | "We need manuals and logs written for people, not for us." | The Aeronef's behaviour is describable in operator terms, and its releasable data uses operator terms and crew-facing units where the crew sees them. |
| N-390 | SH-07 | "We need to tie a crew action to the mode change and the vehicle's response." | Crew selections, mode changes, annunciations and vehicle state are time-stamped on one time base. |
| N-400 | SH-07 | "We need to run our own experiments, not just read recorded runs." | The REE can operate the released Aeronef through the crew interface and record its releasable data. |
| N-410 | SH-08 | "We need an answer key: the authoritative requirements, and which manual section describes which requirement." | The Aeronef's requirements are baselined and traceable to the manual sections (METHODOLOGY 11.2). |
| N-420 | SH-08 | "We need scenarios the reverse-engineering team hasn't seen, to test their predictions." | The scenarios in this ConOps, and their variations, can be run as unseen test cases; this document is protected. |
| N-430 | SH-09 | "I need to know, for each scenario, what the crew selects, what they see and what the vehicle does." | Each scenario states crew selections, annunciations and observable vehicle behaviour. |
| N-440 | SH-10 | "Each requirement must say why it exists." | Requirements cite a need or a scenario in their Source, and carry a rationale. |

## 4. Operational context

### 4.1 System of interest and boundary

The system of interest is the **Aeronef**: the simulated vehicle (dynamics, effectors, fuel and mass properties), its flight control, its autoflight, its navigation function and its operational data output. It always runs inside the STP. The Aeronef receives an initial condition, a configuration and crew selections from the STP, and returns operational data.

| Outside the Aeronef | What it exchanges with the Aeronef |
| --- | --- |
| Crew (SH-02) | Gives crew selections; receives annunciations and indications. |
| STP | Provides the configuration, the initial condition, the simulated environment (VOR stations) and the time steps; receives operational data; ends the run. |
| REE | Through a released STP package only: gives crew selections, receives releasable operational data. |

### 4.2 Operating environment

The Aeronef operates in a simulated world. This document assumes the following. Each item is recorded as an interface need on CONVENTIONS (A3) and MS-DYN (C1):

- **Local reference frame.** An Earth-fixed frame with a flat ground plane, north and east axes, and a vertical axis. Position is expressed in this frame.
- **Altitude** is the height of the centre of gravity above the ground plane, positive up (CV-430). The ground plane is at zero altitude.
- **North reference.** Heading, track and VOR radials are referenced to the local frame's north axis (true north). There is no magnetic variation.
- **Gravity** acts toward the ground plane.
- **Air.** There is wind (D17, #49). When a wind is applied, the same wind velocity exists everywhere; the STP sets it for each run, and there are no gusts or turbulence (L0-ASM-050). Drag acts against the vehicle's velocity relative to the air. With wind, the horizontal speed relative to the air differs from the horizontal speed relative to the ground. Position Hold compensates for the wind.
- **Ground.** The ground plane is at altitude zero, with no terrain (D8). Ground contact is an ideal landing: contact within the landing envelope (limits on velocity and acceleration) is a successful landing, and contact outside it is a crash that ends the run (D37, L0-CON-290). Each run starts with the vehicle airborne. There is no take-off.
- **Operating volume.** Nominal operations take place between a minimum operating altitude `[P-SYS-210]` and a maximum operating altitude `[P-SYS-200]`, within a horizontal radius `[P-SYS-220]` of the local frame origin.
- **VOR stations.** Zero or more VOR stations at fixed positions in the local frame, defined by the STP for each run. They are ideal: no noise, and a signal everywhere within a reception range `[P-NAV-050]` of the station (ideal VOR, D12).
- **Vehicle state knowledge.** The Aeronef's functions use the exact simulated state (L0-ASM-010).

Definitions used in the scenarios (fixed in the conventions: CV-430, CV-480, CV-490, CV-530, CV-540, CV-560):

- **Heading:** the direction the nose points, projected on the horizontal plane, measured clockwise from north.
- **Track:** the direction of the horizontal velocity, measured clockwise from north. It is not defined when the horizontal speed is zero.
- **Horizontal speed:** the magnitude of the horizontal velocity.
- **Vertical speed:** the rate of change of altitude, positive up.
- **Flight path angle:** the angle of the velocity vector above the horizontal plane, positive up. It is not defined when the vehicle is not moving, and it is close to ±90° when the horizontal speed is close to zero.

On the Aeronef, heading and track are independent: the vehicle can move in any horizontal direction whatever its heading.

### 4.3 Crew and operator role

The **crew** is whoever makes crew selections and reads the annunciations: a human using the STP interactive interface, a scripted test procedure, or an REE agent. All three use the same **crew interface**. The crew interface is a logical set of selections, annunciations and indications, inspired by an airliner's mode control panel and flight mode annunciator. Its physical form (panels, displays, graphics) is not defined; detailed controls and displays are excluded (AIRCRAFT_CHARACTERISTICS §7).

**Crew selections** (crew-facing units):

| Selection | Unit | Used by |
| --- | --- | --- |
| Selected altitude | ft | Altitude capture |
| Selected flight path angle (signed, positive up) | degrees | FPA climb or descent |
| Selected vertical speed (signed, positive up) | ft/min | V/S climb or descent |
| Selected horizontal speed | kt | Horizontal speed |
| Selected heading | degrees | Heading hold |
| Selected track | degrees | Track hold |
| Selected VOR station (identifier) and selected course | —, degrees | VOR radial tracking |
| Mode engage or arm commands: FPA, V/S, ALT, SPD, HDG, TRK, VOR, POS HOLD, HOVER | — | Mode logic |

**Annunciations** show, for each mode group, the active mode, the armed modes and the selected targets (Section 4.4). **Indications** show the vehicle's current altitude (ft), vertical speed (ft/min), horizontal speed (kt), heading and track (degrees), flight path angle (degrees), the VOR course deviation and the distance to the selected station (NM), the remaining fuel (lb, D9), and the LOW FUEL and FUEL EXHAUSTED alerts.

**Manual control** is an optional feature. Where it is installed, the crew could command the axes directly. It is not developed in this cycle, and no scenario uses it.

**The crew's role** is to choose modes and targets on the flight control panel, and to monitor the annunciations. The panel is defined at lower levels (#79); there is no stick or yoke (L0-CON-180). Autoflight flies the vehicle in every scenario. The crew does not act on the effectors or on the flight control.

### 4.4 Autoflight operating concept

**Mode groups (TBR, #6, deferred to L2).** The modes are organised in three groups: one **vertical** mode, one **lateral** mode and one **speed** mode are active at a time. The owner placed Position Hold in the lateral group and Hover in the vertical group (D11); the compatibility matrix of lateral, vertical and speed modes is designed at L2 (D13). A flight-path-angle mode needs horizontal velocity, so it cannot be combined with Position Hold (D13).

**Exactly one mode per group.** While autoflight controls the vehicle, each group always has one active mode, or a hold mode covers it. A run starts with the modes and targets given in its initial condition (TBR, #60, deferred to L2).

**Armed and active.** As a general rule a selected mode first arms, and engages when its conditions are met; while it is armed, the active mode manoeuvres the vehicle into those conditions within g-limited accelerations (D16). The state terms are TBR (#56). A mode is **active** when it controls its group. A mode is **armed** when it waits for a condition before it becomes active. Two modes arm: altitude capture (with a climb or descent mode) and VOR radial tracking (with a heading or track mode). When the condition is met, the armed mode **captures**: it becomes active, the previous mode of its group stops, and the annunciation changes. A capture is shown by a capture label (ALT*, VOR*) until the vehicle is established on the target, and then by the tracking or hold label (ALT, VOR).

**Annunciation.** Each change of an active mode, an armed mode or a target is annunciated within `[P-AF-060]` s.

**Targets.** Changing a target does not change the mode. The vehicle goes to the new target.

**Attitude during the modes (D10).** Pitch and roll are held level, within `[P-AF-180]`, in every mode: the Aeronef does not need to pitch or roll to move. Heading (this document's reading, TBR at L2, A2-Q03):

- in Heading Hold, the heading is the selected heading, and the track follows the heading;
- in Track Hold and VOR radial tracking, the heading is held at its value when the mode became active;
- in Position Hold and Hover at Altitude, the heading is held at its value when the mode became active.

The vertical and speed modes do not change the attitude. The heading rule for Track Hold, VOR radial tracking and the hold modes, and the rule that the track follows the heading in Heading Hold, are this document's reading of "heading set by the lateral mode or held" (A2-Q03, to confirm at L2).

**Mode catalogue (D3).**

| Mode | Group | Crew selection | What it controls | Provisional labels (armed / capture / active) | Scenarios |
| --- | --- | --- | --- | --- | --- |
| Climb or descent on flight path angle | Vertical | Selected flight path angle (degrees) | Flight path angle | — / — / FPA | SC-010, SC-030, SC-110 |
| Climb or descent on vertical speed | Vertical | Selected vertical speed (ft/min) | Vertical speed | — / — / V/S | SC-020, SC-040, SC-050, SC-110 |
| Altitude capture | Vertical (armed, then active) | Selected altitude (ft) | Transition from climb or descent to the selected altitude | ALT / ALT* / — | SC-010 to SC-040, SC-110 |
| Altitude hold | Vertical | None (captured altitude, or altitude at engagement) | Altitude | — / — / ALT | SC-010 to SC-080, SC-110 |
| Horizontal speed | Speed | Selected horizontal speed (kt) | Horizontal speed | — / — / SPD | SC-010 to SC-080, SC-110 |
| Heading hold | Lateral | Selected heading (degrees) | Heading (track follows, TBR A2-Q03) | — / — / HDG | SC-010 to SC-060, SC-080, SC-110 |
| Track hold | Lateral | Selected track (degrees) | Track | — / — / TRK | SC-070, SC-110 |
| VOR radial tracking | Lateral (armed, then active) | Station and course (degrees) | Track along the radial | VOR / VOR* / VOR | SC-080, SC-110 |
| Position hold | Lateral (D11) | None | Position: the vehicle stops moving on all axes and holds its position at any altitude, compensating for wind | — / — / POS HOLD | SC-090, SC-110 |
| Hover at altitude | Vertical (D11) | Hover altitude (ft), set on the flight control panel | Descent from the current altitude to the hover altitude, then Position Hold | — / — / HOVER | SC-100, SC-110 |

In the scenario tables, the active modes are written `speed · lateral · vertical`, for example `SPD · HDG · ALT`. A hold mode is still written alone, for example `POS HOLD`, until the compatibility matrix is designed at L2 (#6).

### 4.5 Fuel concept

The Aeronef carries a finite quantity of fuel, at most `[P-FU-010]`. Fuel is consumed to produce effector forces and moments, with separate configurable terms for translation and rotation. Because the effectors must counter gravity, fuel is consumed in every flight condition, including hover and position hold. Vehicle mass decreases as fuel is consumed; the centre of gravity stays fixed.

Fuel is shown to the crew in pounds (D9). When the remaining fuel falls below `[P-FU-020]` of full capacity, the Aeronef annunciates LOW FUEL. When the fuel is exhausted, the Aeronef annunciates FUEL EXHAUSTED and the effectors produce zero force and zero moment. The vehicle then moves under gravity and drag alone. Fuel exhaustion is nominal behaviour (SC-110). What the autoflight modes do after exhaustion is defined in detailed design (TBR, #59).

### 4.6 Runs and the use of operational data

**A run** is one execution of the Aeronef in the STP. It is defined by:

- a **configuration**: the vehicle parameter set, the flight-control-law version and the autoflight version;
- an **initial condition**: position, velocity, attitude, angular rate, fuel quantity, active and armed modes, selected targets, and the VOR stations;
- a **selection script**: crew selections, each with the simulation time at which it applies (empty for an interactive run, where the selections come from a human).

The run ends when the STP's end condition is met: the scenario's end condition, a maximum run time set by the STP, or ground contact (a landing within the envelope, or a crash; D37).

**Operational data.** At each simulation step the Aeronef outputs data on one time base (simulation time since the start of the run): the crew selections received, the selected targets, the active and armed modes, the annunciations and indications, the vehicle state, the fuel quantity, and the flight-control and effector activity. The operational data output (TM, task C7) classifies each signal as **releasable** or **protected**.

| User | Uses the operational data to |
| --- | --- |
| STP (automated tests) | Assess results against requirement success criteria; report pass or fail. |
| Interactive operator | See cause and effect while exploring. |
| REE | Correlate crew selections, mode changes, annunciations and vehicle response, using releasable signals only. |
| Evaluators | Score the REE's predictions on unseen runs. |

## 5. Common scenario format

Each flight scenario gives: purpose; initial conditions; crew selections; a sequence table; expected vehicle behaviour; end conditions; the needs it exercises; and the parts that are TBR.

Common to all flight scenarios unless a scenario says otherwise:

- The vehicle is airborne, inside the operating volume, at a position and altitude `H_INIT` at least `[P-SYS-210]` above the ground plane.
- Fuel is `FUEL_INIT`, more than the low-fuel threshold `[P-FU-020]` and enough to complete the scenario.
- Pitch and roll are level; the angular rate is zero.
- The air is still, and no disturbance is applied.
- Every selected value is within the performance envelope: horizontal speed up to `[P-SYS-230]`, climb vertical speed up to `[P-SYS-240]`, descent vertical speed up to `[P-SYS-250]`, flight path angle magnitude up to `[P-SYS-260]`, heading rate up to `[P-SYS-270]`. The acceleration sensed by the crew stays within `[P-SYS-120]` (gravity included; L0-CON-310). Selected values are multiples of the selection resolutions `[P-AF-010]` to `[P-AF-050]`.
- "Settled" means within the stated tolerance, reached within `[P-AF-190]` s of the capture onset or target change, and kept until the end of the scenario. Each tolerance is a placeholder until the per-mode requirements (Phase 4) fix it.
- Each annunciation change in the sequence tables occurs within `[P-AF-060]` s of its trigger.
- The scenario ends when the stated end condition holds for an observation time `T_OBS`, chosen by the test procedure.

In the sequence tables, **Trigger** is a crew selection or a condition reached by the vehicle. **Active** and **Armed** are the annunciated modes after the trigger.

## 6. Scenarios

### 6.1 Vertical scenarios

#### SC-010 — Climb on flight path angle, capture and hold an altitude

**Purpose.** Show a climb at a selected flight path angle, the arming and capture of the selected altitude, and the automatic transition to altitude hold, with the speed and lateral modes active at the same time.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT`, holding altitude `H_INIT`, horizontal speed `SPD_INIT` at least `[P-AF-070]`, heading `HDG_INIT`. Nothing armed.

**Crew selections.** Selected altitude `H_SEL` (ft), above `H_INIT` and below `[P-SYS-200]`. Selected flight path angle `FPA_SEL` (degrees), positive. Then FPA engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `H_SEL` | SPD · HDG · ALT | — | No change. Altitude, speed and heading held. |
| 2 | Crew engages FPA with `FPA_SEL` | SPD · HDG · FPA | ALT | The vehicle climbs. The flight path angle goes to `FPA_SEL`; the vertical speed follows from the flight path angle and the horizontal speed. Speed and heading held. Pitch and roll level (D10). |
| 3 | Capture onset, as the altitude approaches `H_SEL` (onset set by the mode logic) | SPD · HDG · ALT* | — | The vertical speed decreases toward zero. The vehicle levels off at `H_SEL` without passing it by more than `[P-AF-100]`. |
| 4 | Vehicle established on `H_SEL` (criterion set by the mode logic) | SPD · HDG · ALT | — | Altitude held at `H_SEL`. |

**Expected vehicle behaviour.** During the climb, the flight path angle settles within `[P-AF-080]` of `FPA_SEL`. The horizontal speed stays within `[P-AF-120]` of `SPD_INIT` and the heading within `[P-AF-130]` of `HDG_INIT` throughout. During capture, the altitude overshoot stays within `[P-AF-100]`. After capture, the altitude settles within `[P-AF-110]` of `H_SEL`.

**End conditions.** `SPD · HDG · ALT` active, nothing armed, altitude within `[P-AF-110]` of `H_SEL`.

**Needs exercised.** N-050, N-060, N-070, N-080, N-160, N-170, N-200, N-210.

**TBR.** Concurrent speed, lateral and vertical modes (#6, L2). Attitude is level (D10).

#### SC-020 — Descend on vertical speed, capture and hold an altitude

**Purpose.** Show a descent at a selected vertical speed, entered in ft/min, ending in altitude capture and hold.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT`, holding `H_INIT`, horizontal speed `SPD_INIT`, heading `HDG_INIT`.

**Crew selections.** Selected altitude `H_SEL` (ft), below `H_INIT` and at least `[P-SYS-210]`. Selected vertical speed `VS_SEL` (ft/min), negative. Then V/S engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `H_SEL` | SPD · HDG · ALT | — | No change. |
| 2 | Crew engages V/S with `VS_SEL` | SPD · HDG · V/S | ALT | The vehicle descends; the vertical speed goes to `VS_SEL`. Speed and heading held. |
| 3 | Capture onset | SPD · HDG · ALT* | — | The vertical speed decreases toward zero; the vehicle levels off at `H_SEL`. |
| 4 | Vehicle established on `H_SEL` | SPD · HDG · ALT | — | Altitude held at `H_SEL`. |

**Expected vehicle behaviour.** During the descent, the vertical speed settles within `[P-AF-090]` of `VS_SEL`. Speed and heading are held as in SC-010. The altitude overshoot below `H_SEL` stays within `[P-AF-100]`, and the altitude then settles within `[P-AF-110]` of `H_SEL`.

**End conditions.** `SPD · HDG · ALT` active, altitude within `[P-AF-110]` of `H_SEL`.

**Needs exercised.** N-050, N-060, N-070, N-080, N-170, N-210.

**TBR.** Q2 and Q5, as in SC-010.

#### SC-030 — Descend on flight path angle, capture and hold an altitude

**Purpose.** Show that a descent on flight path angle works as the climb does (D3: "descent ... similar to climb").

**Initial conditions, selections and sequence.** As SC-010, except that `H_SEL` is below `H_INIT`, at least `[P-SYS-210]`, and `FPA_SEL` is negative.

**Expected vehicle behaviour.** As SC-010, with the vehicle descending. The vertical speed stays within the descent limit `[P-SYS-250]`.

**End conditions.** As SC-010.

**Needs exercised.** N-050, N-060, N-070, N-080, N-170.

**TBR.** Q2 and Q5, as in SC-010.

#### SC-040 — Climb on vertical speed with zero horizontal speed

**Purpose.** Show a climb on vertical speed (D3), and the Aeronef's ability to climb vertically: the vehicle climbs with no horizontal motion and without tilting.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT`, with the selected horizontal speed at zero and the vehicle stationary at `H_INIT`, heading `HDG_INIT`.

**Crew selections.** Selected altitude `H_SEL` (ft), above `H_INIT`. Selected vertical speed `VS_SEL` (ft/min), positive. Then V/S engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `H_SEL` | SPD · HDG · ALT | — | No change. |
| 2 | Crew engages V/S with `VS_SEL` | SPD · HDG · V/S | ALT | The vehicle climbs vertically. Horizontal speed stays near zero; heading held; pitch and roll level. |
| 3 | Capture onset | SPD · HDG · ALT* | — | Vertical speed decreases toward zero. |
| 4 | Vehicle established on `H_SEL` | SPD · HDG · ALT | — | Altitude held at `H_SEL`; the vehicle is stationary. |

**Expected vehicle behaviour.** Vertical speed settles within `[P-AF-090]` of `VS_SEL`. Horizontal speed stays within `[P-AF-120]` of zero. Heading stays within `[P-AF-130]` of `HDG_INIT`. Altitude capture and hold as in SC-020.

**Variation SC-040 / FPA not available.** With horizontal speed below `[P-AF-070]`, the crew engages FPA. Because the flight path angle is not usable near zero horizontal speed, FPA does not engage and the annunciations do not change (question A2-Q06).

**End conditions.** `SPD · HDG · ALT` active, the vehicle stationary at `H_SEL` within `[P-AF-110]`.

**Needs exercised.** N-050, N-060, N-070, N-080, N-110, N-190, N-240.

**TBR.** Q2 (attitude), Q5 (SPD at zero with a lateral mode active).

#### SC-050 — Change targets and modes in flight

**Purpose.** Show that targets can be changed while their modes are active, that the crew can change the mode of a group at any time, and that the crew can level off by engaging altitude hold directly.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT` at `H_INIT`, `SPD_INIT`, `HDG_INIT`.

**Crew selections.** In order, each after the previous one has settled: a new selected speed `SPD_2`; a new selected heading `HDG_2`; `H_SEL` above `H_INIT` with V/S engaged at `VS_SEL`; a new selected vertical speed `VS_2` during the climb; ALT engaged before the capture onset.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `SPD_2` | SPD · HDG · ALT | — | Horizontal speed goes to `SPD_2`. |
| 2 | Crew sets `HDG_2` | SPD · HDG · ALT | — | The vehicle yaws toward `HDG_2` at a heading rate up to `[P-SYS-270]`, in the shorter direction (mode logic to confirm). The track follows the heading (TBR, A2-Q03, L2). |
| 3 | Crew sets `H_SEL` and engages V/S at `VS_SEL` | SPD · HDG · V/S | ALT | Climb at `VS_SEL`. |
| 4 | Crew sets `VS_2` | SPD · HDG · V/S | ALT | Vertical speed goes to `VS_2`. |
| 5 | Crew engages ALT before capture onset | SPD · HDG · ALT | — | The vehicle stops climbing and holds the altitude reached when ALT was engaged. Altitude capture is no longer armed. |

**Expected vehicle behaviour.** Each new target is settled within its tolerance: `[P-AF-120]` for speed, `[P-AF-130]` for heading, `[P-AF-090]` for vertical speed, `[P-AF-110]` for the level-off altitude. Changing one group's target or mode leaves the other groups' targets held.

**End conditions.** `SPD · HDG · ALT` active, all targets settled.

**Needs exercised.** N-060, N-090, N-100, N-170, N-200, N-210.

**TBR.** Q2 (track follows heading), Q5 (independence of the groups). The level-off altitude in step 5 (the altitude at engagement, or the altitude where the vertical speed reaches zero) is for the mode logic to define (C5).

### 6.2 Lateral and speed scenarios

#### SC-060 — Fly a constant heading at a set horizontal speed

**Purpose.** Show heading hold and horizontal speed together: the vehicle turns its nose to the selected heading and moves along it at the selected speed.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT` at `H_INIT`, horizontal speed `SPD_INIT`, heading and track `HDG_INIT`.

**Crew selections.** Selected heading `HDG_SEL` (degrees), different from `HDG_INIT`. Selected speed `SPD_SEL` (kt), different from `SPD_INIT`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `HDG_SEL` and `SPD_SEL` | SPD · HDG · ALT | — | The vehicle yaws toward `HDG_SEL`; the track follows the heading (TBR, A2-Q03, L2). The horizontal speed goes to `SPD_SEL`. Altitude held. |
| 2 | Heading and speed reached | SPD · HDG · ALT | — | Straight, level flight on `HDG_SEL` at `SPD_SEL`. |

**Expected vehicle behaviour.** Heading settles within `[P-AF-130]` of `HDG_SEL`; track settles within `[P-AF-140]` of `HDG_SEL`; horizontal speed within `[P-AF-120]` of `SPD_SEL`; altitude within `[P-AF-110]` of `H_INIT` throughout. Pitch and roll stay level within `[P-AF-180]`. The heading rate stays within `[P-SYS-270]`.

**End conditions.** Heading, track, speed and altitude settled.

**Needs exercised.** N-050, N-060, N-070, N-090, N-160, N-170.

**TBR.** Q2 (track follows heading; pitch and roll level), Q5.

#### SC-070 — Fly a constant track

**Purpose.** Show track hold, and that the direction of motion is independent of the heading: the vehicle moves along the selected track while its nose keeps its heading.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT` at `H_INIT`, horizontal speed `SPD_INIT` greater than zero, heading and track `HDG_INIT`.

**Crew selections.** Selected track `TRK_SEL` (degrees), different from `HDG_INIT` by `TRK_OFFSET`. Then TRK engaged. Later, a second selected track `TRK_2`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages TRK with `TRK_SEL` | SPD · TRK · ALT | — | The direction of motion turns to `TRK_SEL`. The heading stays at `HDG_INIT` (TBR, A2-Q03, L2). The vehicle moves at an angle `TRK_OFFSET` to its nose. Speed and altitude held. |
| 2 | Crew sets `TRK_2` | SPD · TRK · ALT | — | The direction of motion turns to `TRK_2`; the heading still stays at `HDG_INIT`. |

**Expected vehicle behaviour.** Track settles within `[P-AF-140]` of `TRK_SEL`, then of `TRK_2`. Heading stays within `[P-AF-130]` of `HDG_INIT` throughout. Horizontal speed within `[P-AF-120]` of `SPD_INIT`; altitude within `[P-AF-110]` of `H_INIT`. `TRK_OFFSET` may take any value in the full circle, including flight sideways and backwards (TBR, A2-Q03, L2).

**End conditions.** `SPD · TRK · ALT` active; track on `TRK_2`, heading on `HDG_INIT`.

**Needs exercised.** N-050, N-060, N-090, N-110, N-160, N-190, N-240.

**TBR.** Q2 (the heading held while TRK is active), Q5.

#### SC-080 — Intercept and track a VOR radial

**Purpose.** Show VOR radial tracking: arming while another lateral mode flies an intercept, capture, and tracking of the selected radial.

**Initial conditions.** Common conditions. A VOR station `STN` at a known position in the local frame. The vehicle is within the reception range `[P-NAV-050]` of `STN`, away from the radial, and at a distance from the station such that the scenario ends before the vehicle passes over it (question A2-Q08). Active `SPD · HDG · ALT` at `H_INIT`, `SPD_INIT`, on an intercept heading `HDG_INT` that crosses the selected radial at an intercept angle `ANG_INT`.

**Crew selections.** Station `STN`; selected course `CRS_SEL` (degrees). Then VOR armed. In this scenario the vehicle tracks outbound, so the course equals the radial; for an inbound track the course is the radial plus 180 degrees (D14).

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew selects `STN` and `CRS_SEL` | SPD · HDG · ALT | — | No change. The course deviation and the distance to `STN` are indicated. |
| 2 | Crew arms VOR | SPD · HDG · ALT | VOR | The vehicle continues on `HDG_INT` toward the radial. |
| 3 | Capture onset as the vehicle nears the radial | SPD · VOR* · ALT | — | The track turns toward `CRS_SEL`. The heading is held at its value when VOR became active (TBR, A2-Q03, L2). |
| 4 | Vehicle established on the radial | SPD · VOR · ALT | — | The vehicle tracks the radial outbound. |

**Expected vehicle behaviour.** After capture, the angular deviation from the radial settles within `[P-AF-150]`. The track settles on `CRS_SEL` within `[P-AF-140]`. Speed and altitude are held throughout. Heading stays within `[P-AF-130]` of `HDG_INT` from VOR capture onwards (TBR, A2-Q03, L2).

**Variation SC-080 / intercept on track.** As SC-080, but the intercept is flown in TRK on `TRK_INT` before VOR is armed. The heading stays at its earlier value through the intercept and the capture.

**End conditions.** `SPD · VOR · ALT` active; deviation within `[P-AF-150]`; the vehicle still within `[P-NAV-050]` and not over the station.

**Needs exercised.** N-050, N-060, N-070, N-110, N-120, N-200, N-210.

**TBR.** Heading during VOR tracking (A2-Q03, L2). VOR replacing HDG or TRK in the lateral group (#6, L2). The VOR model is fixed: ideal VOR (D12), and the crew flies a course (D14).

### 6.3 Hold scenarios

#### SC-090 — Hold a position

**Purpose.** Show Position Hold (D11): the vehicle stops moving on all axes and holds its position, compensating for wind.

**Initial conditions.** Common conditions. Active `SPD · HDG · ALT` at `H_INIT`, horizontal speed `SPD_INIT` (which can be zero), heading `HDG_INIT`.

**Crew selections.** POS HOLD engaged at time `T_ENG`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages POS HOLD | POS HOLD | — | The vehicle decelerates within its acceleration limits (D16) and holds a reference position. Whether the reference is the position at `T_ENG`, so that the vehicle comes back to it, or the point where it stops is TBR (#78); this scenario shows the first reading. Altitude held at its value at `T_ENG`. Heading held at `HDG_INIT`; pitch and roll level (D10). |
| 2 | Vehicle at the reference position | POS HOLD | — | Position held. |

**Expected vehicle behaviour.** The position settles within `[P-AF-160]` of the reference position, and the heading within `[P-AF-130]` of `HDG_INIT`. With a non-zero `SPD_INIT`, the vehicle passes the reference position while it decelerates and then comes back to it.

**Variation SC-090 / leave Position Hold.** The crew engages SPD, HDG and ALT. Position Hold ends and the three groups become active with their targets (A2-Q10; TBR, #6, L2).

**Variation SC-090 / wind.** As SC-090 with a wind applied: the vehicle holds the reference position against the wind.

**End conditions.** POS HOLD active; position within `[P-AF-160]` of the reference position.

**Needs exercised.** N-050, N-060, N-130, N-160, N-200, N-210.

**TBR.** Reference position and deceleration (#78); heading held (A2-Q03, L2); combination with the other groups (#6, L2).

#### SC-100 — Hover at an altitude

**Purpose.** Show Hover (D11): a vertical mode. When it engages, the vehicle descends from its current altitude to the hover altitude set on the flight control panel, then holds position.

**Initial conditions.** As SC-090, with `H_INIT` above the hover altitude.

**Crew selections.** Hover altitude `H_HOV` (ft), below `H_INIT`, set on the flight control panel. HOVER engaged at time `T_ENG`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages HOVER | HOVER | — | The vehicle decelerates within its acceleration limits (D16) and descends from `H_INIT` toward `H_HOV`. Heading held at `HDG_INIT`; pitch and roll level (D10). |
| 2 | Vehicle at `H_HOV` | HOVER, with Position Hold | — | The vehicle holds `H_HOV` and holds its position (as SC-090). |

**Expected vehicle behaviour.** Altitude settles within `[P-AF-110]` of `H_HOV`. Horizontal speed settles within `[P-AF-170]` of zero, and the position is then held within `[P-AF-160]`.

**Difference from SC-090.** Position Hold holds the position at the current altitude. Hover first descends to the hover altitude, then holds position there. Whether the horizontal reference is set at engagement or once the vehicle has stopped is TBR (#78).

**End conditions.** HOVER active at `H_HOV`; position held within `[P-AF-160]`.

**Needs exercised.** N-050, N-060, N-140, N-160, N-200, N-210.

**TBR.** Reference position and deceleration (#78); the hover-altitude selector (#79); combination with the other groups (#6, L2).

### 6.4 Reference mission

#### SC-110 — Reference mission to fuel exhaustion

**Purpose.** Fly a fixed, repeatable profile that uses every mode of the catalogue, with translation and rotation, until the fuel is exhausted. The mission is the common basis for measuring accuracy and fuel used (N-250), and it shows the nominal behaviour at low fuel and at fuel exhaustion.

**Initial conditions.** Fuel at full capacity `[P-FU-010]`, so mass at its maximum. Vehicle at `H_INIT`, stationary, heading `HDG_INIT`. Active `POS HOLD`. One VOR station `STN`, placed so that the cruise leg crosses its radial within reception range.

**Profile.** Each leg starts when the previous leg's end condition is met. The scenario variables (altitudes, angles, speeds, headings, courses and leg durations `T_n`) form one fixed reference set, chosen so that fuel remains at the start of leg 9.

| Leg | Crew selections | Active (after captures) | Armed | Vehicle behaviour | Leg ends when |
| --- | --- | --- | --- | --- | --- |
| 1 | None | POS HOLD | — | Holds position for `T_1`. | `T_1` elapsed |
| 2 | `SPD_1`, `HDG_1`, `H_1` above `H_INIT`, then FPA at `FPA_1` | SPD · HDG · FPA, then ALT*, then SPD · HDG · ALT | ALT | Accelerates, turns, climbs on flight path angle, captures `H_1` (TBR, #6, L2: leaving POS HOLD). | Established on `H_1` |
| 3 | VOR: `STN`, `CRS_1`; VOR armed | SPD · HDG · ALT, then VOR*, then SPD · VOR · ALT | VOR | Cruises on `HDG_1`, intercepts and tracks the radial outbound. | `T_3` elapsed on the radial |
| 4 | `H_2` below `H_1`, V/S at `VS_2` | SPD · VOR · V/S, then ALT*, then SPD · VOR · ALT | ALT | Descends on vertical speed while tracking the radial; captures `H_2`. | Established on `H_2` |
| 5 | `TRK_1`, TRK engaged; `SPD_2` | SPD · TRK · ALT | — | Leaves the radial on a track that differs from the heading. | `T_5` elapsed |
| 6 | `HDG_2` and HDG engaged; then FPA at a negative `FPA_2` with `H_3` | SPD · HDG · FPA, then ALT*, then SPD · HDG · ALT | ALT | Turns, descends on flight path angle, captures `H_3`. | Established on `H_3` |
| 7 | `H_HOV` below `H_3`, then HOVER | HOVER | — | Descends to `H_HOV` and holds position there (as SC-100). | `T_7` elapsed |
| 8 | `SPD` at zero, `HDG_3`, `H_4` above `H_HOV`, V/S at `VS_4` | SPD · HDG · V/S, then ALT*, then SPD · HDG · ALT | ALT | Climbs vertically to `H_4` (as SC-040) (TBR, #6, L2: leaving HOVER). | Established on `H_4` |
| 9 | POS HOLD | POS HOLD | — | Holds position until the fuel is exhausted. LOW FUEL is annunciated when the fuel falls below `[P-FU-020]`. | Fuel exhausted |
| 10 | None | (TBR, #59) | — | FUEL EXHAUSTED annunciated. Effectors produce zero force and zero moment. The vehicle falls under gravity and drag, and keeps the angular rate it had at exhaustion. | Ground contact, or STP maximum run time |

**Expected vehicle behaviour.** Each leg meets the expected behaviour of the scenario it repeats: SC-010 (leg 2), SC-080 (leg 3), SC-020 (leg 4), SC-070 (leg 5), SC-030 (leg 6), SC-100 (leg 7), SC-040 (leg 8), SC-090 (leg 9). The fuel quantity decreases throughout the mission and never increases. The vehicle mass decreases by the mass of fuel consumed. LOW FUEL is annunciated within `[P-AF-060]` s of the fuel falling below `[P-FU-020]`, and FUEL EXHAUSTED within `[P-AF-060]` s of exhaustion. After exhaustion, the motion is free fall with drag, which can be compared with an independent solution (N-290). The run ends at ground contact, normally a crash, because the vehicle is outside the landing envelope (D37).

**Variation SC-110 / hover endurance.** From the same initial condition, HOVER is engaged at the start and kept until the fuel is exhausted. The time to exhaustion is at least `[P-SYS-280]`.

**Recorded results.** Total fuel used per leg, mission duration to exhaustion, and the tracking errors per leg against the tolerances above.

**End conditions.** Ground contact, or STP maximum run time.

**Needs exercised.** N-050, N-060, N-080, N-100, N-110, N-120, N-130, N-140, N-150, N-170, N-200, N-250, N-280, N-290.

**TBR.** As in the scenarios each leg repeats (#6, #78, A2-Q03). Autoflight state after fuel exhaustion (#59).

### 6.5 Platform and evidence scenarios

These scenarios describe how the STP and the REE use the Aeronef. They exercise the Aeronef's configuration, run and operational-data needs, not its flight modes.

#### SC-200 — Unattended verification run

**Purpose.** A test procedure verifies a requirement with no human involved.

**Sequence.**

1. The STP creates an Aeronef instance with a configuration (parameter set, control-law version, autoflight version), each identified by a version.
2. The STP sets the initial condition, including the active and armed modes, the targets and the VOR stations.
3. The STP runs the simulation without graphics, faster than real time, and applies the crew selections of the selection script at their simulation times. The selections go through the crew interface.
4. At each step, the Aeronef outputs its operational data.
5. The run ends on the procedure's end condition, the maximum run time or ground contact.
6. The STP assesses the data against the procedure's success criteria and reports the result with the configuration identification.

**Expected behaviour of the Aeronef.** The same configuration, initial condition and selection script give the same operational data on each repetition (the same verification result, D25). The Aeronef needs no input other than the configuration, the initial condition, the selection script and the time steps.

**Needs exercised.** N-300, N-310, N-320, N-330, N-340, N-350, N-370.

#### SC-210 — Parallel and Monte Carlo campaign

**Purpose.** Run many independent Aeronef instances at once, for example a regression campaign overnight or a Monte Carlo campaign over parameters and initial conditions.

**Sequence.** The STP starts many instances in parallel, each with its own configuration, initial condition and selection script. Variations change parameter values (within their stated ranges), initial conditions and selected targets. Each instance runs as in SC-200.

**Expected behaviour of the Aeronef.** Instances do not share state, and the results of one instance do not depend on how many others are running or in what order. Each run is reproducible on its own.

**Needs exercised.** N-020, N-300, N-330, N-350.

#### SC-220 — Comparative evaluation of control laws

**Out of scope this cycle.** There is one autoflight implementation (D24) and one set of control laws for now (D42), so there is nothing to compare. The scenario is kept for when a second control-law design is added.

**Purpose.** Compare two control-law versions under the same conditions.

**Sequence.** The STP runs the same set of scenarios (for example SC-010 to SC-110) once with version A and once with version B. Only the version under comparison changes; the vehicle model, the parameter set, the initial conditions and the selection scripts are the same. The STP compares tracking accuracy, mode-transition behaviour and fuel used.

**Expected behaviour of the Aeronef.** The swap is a configuration change. The vehicle model, the crew interface and the operational data format stay the same for both versions.

**Needs exercised.** N-220, N-230, N-250, N-350.

#### SC-230 — Interactive exploration

**Purpose.** An engineer explores cause and effect by flying the Aeronef interactively.

**Sequence.** The STP runs one instance in real time. The engineer makes crew selections at any time, as in the flight scenarios, and watches the annunciations, the indications and the vehicle state. Graphics are optional.

**Expected behaviour of the Aeronef.** It accepts a selection at any simulation step and behaves as it does when the same selection comes from a script at the same time.

**Needs exercised.** N-320, N-360, N-390.

#### SC-240 — Reverse-engineering experiment

**Purpose.** The REE runs its own experiments on the released Aeronef.

**Sequence.**

1. The REE receives a released package: the operational manuals and an executable STP configuration that outputs releasable data only. It does not receive requirements, design, source code, this ConOps or protected signals.
2. An REE agent, acting as the crew, chooses an initial condition from those the package allows, and applies crew selections through the crew interface.
3. The REE records the releasable operational data and correlates its selections with the mode changes, the annunciations and the vehicle response, on the common time base.
4. The REE predicts the response to new selections and checks the prediction with new runs.

**Expected behaviour of the Aeronef.** The released Aeronef behaves the same as the protected one. Its releasable data is enough to relate each selection to its effect, and contains nothing classified protected.

**Needs exercised.** N-030, N-380, N-390, N-400, N-420.

## 7. Open questions and TBR items

### 7.1 Dependencies on the plan's questions

The owner answered the plan's questions on 2026-10-25 (plan §9). Where a question is still open, the marked parts may change.

| Question | Status | Where it applies |
| --- | --- | --- |
| Q2 — Attitude during the guidance modes | **Decided (D10):** pitch and roll level in every mode. The heading rules are this document's reading, to confirm at L2 (A2-Q03). | Section 4.4; SC-010 to SC-110 |
| Q3 — Hover versus Position Hold | **Decided (D11):** Position Hold is a lateral mode that stops all motion and holds position, compensating for wind. Hover is a vertical mode that descends to the panel altitude, then holds position. The reference position and the deceleration are open (#78). | SC-090, SC-100, SC-110 legs 7 and 9 |
| Q4 — VOR model | **Decided (D12):** ideal VOR. The crew flies a course (D14). | Section 4.2; SC-080; SC-110 leg 3 |
| Q5 — Mode combinations | **Deferred to L2 (#6).** A compatibility matrix of lateral, vertical and speed modes is designed there (D13). | Section 4.4; every sequence table |

### 7.2 Questions raised by this document

Each question has a proposed answer, used in the scenarios. They are recorded in `work/A2/issues.md`; the owner's answers of 2026-10-25 are marked **Owner**.

| ID | Question | Proposed answer |
| --- | --- | --- |
| A2-Q01 | Is the air still (no wind) in this cycle? | Yes. Drag is relative to still air; horizontal speed is the same relative to air and ground. **Owner: no.** There is wind, uniform and configurable per run (D17, #49). |
| A2-Q02 | Are take-off, landing and ground contact in scope? | No. Runs start airborne; reaching the ground plane ends the run. **Owner:** landing is in scope as an ideal landing; contact outside the landing envelope is a crash (D8, D37). |
| A2-Q03 | In HDG, does the track follow the heading? In TRK and VOR, what does the heading do? | HDG sets the heading, and the track follows it. TRK and VOR hold the heading at its value when the mode became active. Deferred to L2 (D33). |
| A2-Q04 | After fuel exhaustion, do the autoflight modes stay engaged? | Yes. The modes stay engaged and annunciated; FUEL EXHAUSTED is annunciated; there is no automatic disengagement. **Owner:** defined in detailed design (#59, deferred). |
| A2-Q05 | Can a mode group have no active mode? | No. Each group has one active mode, or a hold mode covers it; the run's initial condition sets the starting modes. **Owner:** deferred to L2 (#60). |
| A2-Q06 | What happens when FPA is selected with horizontal speed near zero? | FPA does not engage below `[P-AF-070]`; the active vertical mode stays as it was. **Owner: rejected.** A flight-path-angle mode needs horizontal velocity; compatibility is designed at L2 (D13, #61). |
| A2-Q07 | Do Position Hold and Hover also replace the speed group? | Yes, because both hold zero horizontal speed. Superseded: Position Hold is lateral and Hover vertical (D11); combinations at L2 (#6). |
| A2-Q08 | What happens when the vehicle passes over a VOR station? | Not covered in this cycle's scenarios; the navigation and autoflight agents (C6, C5) define the behaviour, and the scenarios avoid it until then. Deferred to L2 (D33). |
| A2-Q09 | In what crew-facing unit is fuel shown? D7 does not cover fuel. | Percent of full fuel capacity. **Owner:** pounds (lb), not percent (D9, #51). |
| A2-Q10 | How does the crew leave Position Hold or Hover? | By engaging a mode in any group. The groups not selected start in their hold mode at their current values: ALT, HDG, SPD. Deferred to L2 (#6). |
| A2-Q11 | Which altitude does Hover hold? | The altitude at engagement, as Position Hold does. **Owner:** Hover descends to the altitude set on the flight control panel (D11). |
| A2-Q12 | Do scenario values belong in the parameter database? | No. Scenario values are scenario variables set by the test procedures; the parameter database holds system values only. **Owner: yes.** Test procedures set scenario values; they are not design parameters (D32, #62). |

## 8. Traceability

### 8.1 Scenario → needs → D3 modes

| Scenario | Needs exercised | D3 modes |
| --- | --- | --- |
| SC-010 | N-050, N-060, N-070, N-080, N-160, N-170, N-200, N-210 | Climb on FPA, altitude capture, altitude hold, horizontal speed, heading hold |
| SC-020 | N-050, N-060, N-070, N-080, N-170, N-210 | Descent on V/S, altitude capture, altitude hold, horizontal speed, heading hold |
| SC-030 | N-050, N-060, N-070, N-080, N-170 | Descent on FPA, altitude capture, altitude hold, horizontal speed, heading hold |
| SC-040 | N-050, N-060, N-070, N-080, N-110, N-190, N-240 | Climb on V/S, altitude capture, altitude hold, horizontal speed, heading hold |
| SC-050 | N-060, N-090, N-100, N-170, N-200, N-210 | Climb on V/S, altitude capture (armed), altitude hold, horizontal speed, heading hold |
| SC-060 | N-050, N-060, N-070, N-090, N-160, N-170 | Heading hold, horizontal speed, altitude hold |
| SC-070 | N-050, N-060, N-090, N-110, N-160, N-190, N-240 | Track hold, horizontal speed, altitude hold |
| SC-080 | N-050, N-060, N-070, N-110, N-120, N-200, N-210 | VOR radial tracking, heading hold, track hold (variation), horizontal speed, altitude hold |
| SC-090 | N-050, N-060, N-130, N-160, N-200, N-210 | Position hold |
| SC-100 | N-050, N-060, N-140, N-160, N-200, N-210 | Hover at altitude |
| SC-110 | N-050, N-060, N-080, N-100, N-110, N-120, N-130, N-140, N-150, N-170, N-200, N-250, N-280, N-290 | All ten modes |
| SC-200 | N-300, N-310, N-320, N-330, N-340, N-350, N-370 | — |
| SC-210 | N-020, N-300, N-330, N-350 | — |
| SC-220 | N-220, N-230, N-250, N-350 | — |
| SC-230 | N-320, N-360, N-390 | — |
| SC-240 | N-030, N-380, N-390, N-400, N-420 | — |

Each of the ten D3 modes is exercised by at least one scenario of its own and by SC-110.

### 8.2 Needs not exercised by a scenario

These needs apply to the requirements, the parameter database or the documentation, not to an operation. L0 and L1 requirements cite them directly.

| Need | Covered by |
| --- | --- |
| N-010 | L0 constraints (modelling boundaries) |
| N-040, N-410, N-440 | L0 and the traceability rules of METHODOLOGY 10.4 |
| N-180 | An optional-feature (EARS "Where") requirement; not developed |
| N-260 | Flight-control requirements on saturation (task C4); saturation may occur in any scenario but is not a scenario of its own |
| N-270 | MS-DYN (task C1) |
| N-430 | The scenario format of this document (Section 5) and the operational manuals |

## 9. Parameters referenced

All values are TBD. Definitions, SI units and crew-facing equivalents are in `work/A2/param_proposals.md`.

| ID | Name |
| --- | --- |
| P-SYS-200 | Maximum operating altitude |
| P-SYS-210 | Minimum operating altitude |
| P-SYS-220 | Horizontal operating radius |
| P-SYS-230 | Maximum horizontal speed |
| P-SYS-240 | Maximum climb vertical speed |
| P-SYS-250 | Maximum descent vertical speed |
| P-SYS-260 | Maximum flight path angle magnitude |
| P-SYS-270 | Maximum heading rate in autoflight |
| P-SYS-280 | Minimum hover endurance at full fuel |
| P-FU-010 | Usable fuel mass at full capacity |
| P-FU-020 | Low-fuel threshold |
| P-AF-010 | Altitude selection resolution |
| P-AF-020 | Vertical speed selection resolution |
| P-AF-030 | Horizontal speed selection resolution |
| P-AF-040 | Heading, track and course selection resolution |
| P-AF-050 | Flight path angle selection resolution |
| P-AF-060 | Annunciation latency |
| P-AF-070 | Minimum horizontal speed for FPA mode |
| P-AF-080 | Flight path angle tracking tolerance |
| P-AF-090 | Vertical speed tracking tolerance |
| P-AF-100 | Altitude capture maximum overshoot |
| P-AF-110 | Altitude hold tolerance |
| P-AF-120 | Horizontal speed tracking tolerance |
| P-AF-130 | Heading hold tolerance |
| P-AF-140 | Track hold tolerance |
| P-AF-150 | VOR radial tracking tolerance |
| P-AF-160 | Position hold tolerance |
| P-AF-170 | Hover horizontal speed tolerance |
| P-AF-180 | Level attitude tolerance |
| P-AF-190 | Settling time |
| P-NAV-050 | VOR reception range |
