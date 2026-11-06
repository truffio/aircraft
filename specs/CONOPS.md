# Aeronef Concept of Operations (Aeronef-relevant)

**Status:** Reviewed at Gate G0 (2026-10-27). Mode material revised for the owner's mode catalogue D56 and attitude rule D57 (2026-11-04). Aligned with L1 and D49 to D62 at the G1 rework (CR-B1-12, 2026-11-04). The mode details (§4.4 and the scenario sequences) remain provisional input for L2 (#89). Landing gear, ground start, Takeoff and Land added (D68 to D71, CR-B3-29 to -35, 2026-11-05).
**Date:** 2026-10-27
**Owner:** Martin
**Information class:** Protected design material. This document is not released to the Reverse-Engineering Effort, and it is not operator-facing manual text.

## 1. Purpose and scope

This document describes how the Aeronef is used, from the point of view of the people and procedures that operate it. It gives:

- the stakeholders and their needs, each need with an ID (`N-nnn`) that L0 and L1 requirements cite in their Source attribute;
- the operational context: the simulated environment, the role of the crew, the autoflight operating concept, and how the Simulation and Testing Platform (TST) and the Reverse-Engineering Effort (RVS) use the Aeronef's operational data;
- nominal scenarios (`SC-nnn`) that cover the autoflight mode catalogue (AIRCRAFT_REQUIREMENTS_PLAN.md §9, D56, with Takeoff and Land added by D69), a reference mission from the ground to fuel exhaustion, and the platform uses of the Aeronef;
- the parts of the scenarios that are still open, marked **TBR** with the issue that tracks them. The owner decided the plan's questions Q2 to Q4 on 2026-10-25 (D10 to D12) and replaced the mode catalogue on 2026-11-04 (D56, which also answers Q5, #6). The detailed mode logic is defined at L2 (D33), so the mode behaviour in the scenarios is provisional;
- a traceability table from scenario to needs and modes.

The document follows the NASA ConOps outline (METHODOLOGY 4.2), trimmed to the Aeronef. It describes operations, not design. It contains no control laws, algorithms or emitter layouts.

**Tailoring.** Hazard and failure analysis is deferred (METHODOLOGY, tailoring note). There are no failure scenarios. Fuel exhaustion is nominal behaviour (SC-110). Effector saturation is nominal behaviour and is not a scenario of its own.

**Not covered.** The Simulation and Testing Platform's and the Reverse-Engineering Effort's own operations, except where they use the Aeronef (Section 6.3). Movement on the ground (taxiing): the vehicle is stationary on the ground. Takeoff and landing are covered with an ideal landing gear (Section 4.2, D37, D69). Manual control: there is none; the crew acts only through the flight control panel (Section 4.3, D49, D55).

### 1.1 Conventions used in this document

- Physical quantities in descriptions are in SI units. Crew selections and annunciations use the crew-facing units of D7, D9 and D34: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track), lb (fuel), and hours or minutes (durations). The unit table and the conversions are in `specs/CONVENTIONS.md` (CV-740, CV-750).
- System and scenario values never appear as numbers in the text; only definitional constants do (for example the 180 degrees between a radial and its reciprocal). System values are parameters `[P-<SUB>-<NNN>]`, held in `parameters/PARAMETERS.yaml` with their status (TBD, TBR or Set). Scenario values (initial altitude, selected targets, durations) are **scenario variables** written in `CODE` font. The test procedures choose their values within the ranges this document states.
- The frame, axis and angle conventions are those of `specs/CONVENTIONS.md`, which is fixed (D43). Section 4.2 repeats the definitions the scenarios use.
- Mode names are the D56 names. The short labels (STAT, HDG, ALT, GO ALT, V/S, GO HOVER, HOVER, TAKEOFF, LAND) are **provisional annunciation labels** used to make the scenarios readable. The autoflight mode logic (`specs/AF_MODE_LOGIC.md`, task C5) owns the final labels.

### 1.2 Reference documents

| Document | Used for |
| --- | --- |
| OBJECTIVES.md | Stakeholders, project objectives, success criteria |
| AIRCRAFT_CHARACTERISTICS.md | Vehicle concept and modelling boundaries |
| TESTING_ENVIRONMENT.md | TST use of the Aeronef |
| REVERSE_ENGINEERING.md | RVS use of the Aeronef, information separation |
| AIRCRAFT_REQUIREMENTS_PLAN.md | Decisions D1 to D72 (§9) |
| METHODOLOGY.md | Stakeholder and ConOps method (Section 4), writing rules (Section 8), worked example (Section 12) |

## 2. Stakeholders

| ID | Stakeholder | Interest in the Aeronef |
| --- | --- | --- |
| SH-01 | Project owner | Owns the experiment, decides open questions, approves baselines. Wants a vehicle that is simple enough to understand completely and rich enough to exercise the whole lifecycle. |
| SH-02 | Crew (human operator, scripted test procedure or RVS agent) | Commands the vehicle through autoflight selections and monitors it through annunciations and indications. |
| SH-03 | Autoflight designers | Adapt airliner autoflight modes to a vehicle whose attitude and translation are independent; develop the autoflight implementation (one, D24). |
| SH-04 | Control-law designers | Develop the flight-control-law design (one for now, D42); more designs may be added later. |
| SH-05 | Vehicle model developers | Build the dynamics, effector, fuel and mass model that the simulation reproduces. |
| SH-06 | Simulation and test engineers (TST) | Run the Aeronef unattended, in parallel and reproducibly; assess results against requirements; explore it interactively. |
| SH-07 | Reverse-engineering team (RVS) | Reconstruct the Aeronef's functions and logic from manuals, observed behaviour and operational data, without the design. |
| SH-08 | Project evaluators | Compare the RVS's reconstruction with the authoritative design and requirements. |
| SH-09 | Operational documentation authors | Write the human-oriented manuals and procedures that become RVS evidence. |
| SH-10 | Peer reviewers | Judge each artifact against its inputs and the checklists. |

## 3. Needs

Each need is recorded in the stakeholder's words, then restated as what it means for the Aeronef. Needs are not requirements: L0 and L1 requirements are written from them and cite them as Source. IDs are numbered in steps of 10 and never reused.

| ID | Stakeholder | Need (stakeholder's words) | What it means for the Aeronef |
| --- | --- | --- | --- |
| N-010 | SH-01 | "I want a vehicle simple enough to understand completely, but rich enough to exercise design, test and reverse engineering." | The Aeronef is bounded by the modelling boundaries of AIRCRAFT_CHARACTERISTICS §7, and every behaviour it has is specified. |
| N-020 | SH-01 | "Every value should be changeable without rewriting requirements." | Every configurable value of the Aeronef is a parameter with an ID, an SI unit and a status. |
| N-030 | SH-01 | "The original design must stay hidden from the reverse-engineering team." | The Aeronef's outputs can be split into releasable and protected data, and nothing released exposes protected design; the split is decided with the RVS (#69). |
| N-040 | SH-01 | "Everything must trace from an objective down to a test." | Each Aeronef behaviour in this ConOps is traceable to a need, and from there to requirements and verification. |
| N-050 | SH-02 | "I fly this vehicle through autoflight. Flying six axes by hand isn't practical." | Autoflight is the primary means of controlling the vehicle; each nominal operation in this ConOps is flown in autoflight. |
| N-060 | SH-02 | "I need to know which mode is active, which is armed, and what the vehicle will do next." | The Aeronef annunciates the active mode of each mode group, the armed modes and the selected targets. |
| N-070 | SH-02 | "I want to enter targets in the units I'm used to: feet, feet per minute, knots, nautical miles and degrees." | Crew selections and annunciations use the D7 crew-facing units. |
| N-080 | SH-02 | "When the climb reaches the altitude I set, I want it to level off and hold without me doing anything." | Go to altitude and Vertical speed arm Altitude hold, which captures the selected altitude automatically (D56). |
| N-090 | SH-02 | "I want to change a target while a mode is flying it, and see the vehicle go to the new target." | Targets of active modes can be changed at any time, and the vehicle acquires the new target. |
| N-100 | SH-02 | "I want to choose a different mode at any time." | The crew can select another mode in any group at any time; the new mode replaces the old one. |
| N-110 | SH-02 | "I need to point the nose one way and move another way." | **Withdrawn (D56, owner 2026-11-04):** no mode separates heading and track; in Heading the craft moves along its heading. |
| N-120 | SH-02 | "I want to fly to and along a radial of a radio station." | **Withdrawn (D56):** there is no VOR. |
| N-130 | SH-02 | "I need to stop and stay in one place." | The Aeronef can hold a three-dimensional position: Stationary with Altitude hold, or Hover (D56). |
| N-140 | SH-02 | "I need to stop moving horizontally and stay at my altitude." | Stationary stops the horizontal motion at any altitude; Hover holds a fixed height above the ground (D56). |
| N-150 | SH-02 | "I need to see how much fuel is left, get a warning before it runs out, and know what happens when it does." | The Aeronef indicates the remaining fuel, alerts at a low-fuel threshold and has a defined behaviour at fuel exhaustion. |
| N-160 | SH-02 | "The vehicle's attitude should be predictable while the modes fly the path." | Pitch and roll are held at zero at all times (D57); each mode states what the heading does. |
| N-170 | SH-02 | "Climb rate, speed and turn rate should stay within known limits so I can plan." | The Aeronef has a stated performance envelope, including the crew acceleration limit (L0-CON-310), and autoflight keeps the vehicle within it. |
| N-180 | SH-02 | "If a manual control option is ever added, I want to command the axes directly." | No manual control in this cycle (D49, D55); the need is kept for later. |
| N-190 | SH-03 | "We need airliner-like modes, adapted to a vehicle that can translate without turning or tilting." | The D56 modes are defined in terms of the Aeronef's independent horizontal and vertical motion. |
| N-200 | SH-03 | "We need to know which modes can be active together." | One horizontal and one vertical mode are active at a time, independently; Go to hover and Hover govern both (D56). |
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
| N-310 | SH-06 | "I need to set up the whole starting state: position, velocity, attitude, fuel, landing gear, modes and targets." | The Aeronef accepts a complete initial condition at the start of a run, on the ground (D69) or, for a test, airborne, including the active and armed modes and their targets. |
| N-320 | SH-06 | "My script must make crew selections at given times." | Crew selections can be applied at a stated simulation time, through the same crew interface a human uses. |
| N-330 | SH-06 | "The same inputs must give the same results, and many runs must go in parallel without affecting each other." | An Aeronef run is reproducible from its configuration, initial condition and selection script, and instances are independent. |
| N-340 | SH-06 | "I need the vehicle to report its state, modes, targets and commands at each step, so the test can judge them." | The Aeronef outputs operational data at each output sample, every `[P-TM-010]` (L1-AER-600). |
| N-350 | SH-06 | "I need to know which version and configuration produced a result." | Each run identifies the vehicle parameter set, the control-law version and the autoflight version it used. |
| N-360 | SH-06 | "I want to fly it interactively and watch what happens." | The same Aeronef can run in real time and accept selections from a human at any time. |
| N-370 | SH-06 | "Runs must end in a defined way." | Each run has defined end conditions (Section 4.6). A crash ends a run; a landing does not. |
| N-380 | SH-07 | "We need manuals and logs written for people, not for us." | The Aeronef's behaviour is describable in operator terms, and its releasable data uses operator terms and crew-facing units where the crew sees them. |
| N-390 | SH-07 | "We need to tie a crew action to the mode change and the vehicle's response." | Crew selections, mode changes, annunciations and vehicle state are time-stamped on one time base. |
| N-400 | SH-07 | "We need to run our own experiments, not just read recorded runs." | The RVS can operate the released Aeronef through the crew interface and record its releasable data. |
| N-410 | SH-08 | "We need an answer key: the authoritative requirements, and which manual section describes which requirement." | The Aeronef's requirements are baselined and traceable to the manual sections (METHODOLOGY 11.2). |
| N-420 | SH-08 | "We need scenarios the reverse-engineering team hasn't seen, to test their predictions." | The scenarios in this ConOps, and their variations, can be run as unseen test cases; this document is protected. |
| N-430 | SH-09 | "I need to know, for each scenario, what the crew selects, what they see and what the vehicle does." | Each scenario states crew selections, annunciations and observable vehicle behaviour. |
| N-440 | SH-10 | "Each requirement must say why it exists." | Requirements cite a need or a scenario in their Source, and carry a rationale. |
| N-450 | SH-01 | "I want the craft to sit on the ground with everything off, take off from there, and land again, without burning fuel while it waits." | The Aeronef rests on an extendable landing gear with its effectors off and no fuel use. Runs start there, and it takes off and lands under autoflight (D69). |

## 4. Operational context

### 4.1 System of interest and boundary

The system of interest is the **Aeronef**: the simulated vehicle (dynamics, effectors, fuel and mass properties), its flight control, its autoflight, its flight control panel (D55), its navigation function and its operational data output. It always runs inside the TST. The Aeronef receives an initial condition, a configuration and crew selections from the TST, and returns operational data.

| Outside the Aeronef | What it exchanges with the Aeronef |
| --- | --- |
| Crew (SH-02) | Gives crew selections; receives annunciations and indications. |
| TST | Provides the configuration, the initial condition, the simulated environment (wind) and the time steps; receives operational data; ends the run. |
| RVS | Through a released TST package only: gives crew selections, receives releasable operational data. |

### 4.2 Operating environment

The Aeronef operates in a simulated world. This document assumes the following. Each item is recorded as an interface need on CONVENTIONS (A3) and MS-DYN (C1):

- **Local reference frame.** An Earth-fixed frame with a flat ground plane, north and east axes, and a vertical axis. Position is expressed in this frame.
- **Altitude** is the height of the centre of gravity above the ground plane, positive up (CV-430). The ground plane is at zero altitude. The **height above the ground** is the height of the lowest point of the body above the ground plane (CV-400). The hover height `[P-AF-210]` and the minimum operating height `[P-SYS-210]` are heights above the ground (D67, D70). At level attitude the height above the ground is the altitude minus half the body diameter `[P-DYN-030]`. On the ground, on the extended gear, it equals the gear length `[P-DYN-040]`.
- **North reference.** Heading and track are referenced to the local frame's north axis (true north). There is no magnetic variation.
- **Gravity** acts toward the ground plane.
- **Air.** There is wind (D17, #49). When a wind is applied, the same wind velocity exists everywhere at a given time; the TST sets it for each run. It is horizontal, a steady wind of up to 100 kt plus gusts and bursts of up to 50 kt, so up to 150 kt at an instant (L0-ASM-050, D51). A gust builds up over at least `[P-SYS-570]`; there are no instantaneous steps (D62). Drag acts against the vehicle's velocity relative to the air. With wind, the horizontal speed relative to the air differs from the horizontal speed relative to the ground. Stationary and Hover compensate for the wind.
- **Ground.** The ground plane is at altitude zero, with no terrain (D8). The Aeronef has an extendable landing gear (D69). It rests on the ground on the extended gear, stationary and at level attitude, with the effectors off and no fuel consumption. A contact of the extended gear with the ground within the landing envelope (limits on the vertical and horizontal speed at contact, D53), with fuel remaining, is a landing: the vehicle comes to rest and the run goes on. Any other ground contact is a crash that ends the run (L0-CON-290): outside the envelope, with the gear not extended, or after fuel exhaustion (D68, D73). Each run starts on the ground (D69). Section 5 covers test runs that start airborne.
- **Operating volume.** Nominal flight takes place between a minimum operating height above the ground `[P-SYS-210]` and a maximum operating altitude `[P-SYS-200]`, within a horizontal radius `[P-SYS-220]` of the local frame origin. Takeoff and Land fly between the ground and the hover height.
- **Vehicle state knowledge.** The Aeronef's functions use the exact simulated state (L0-ASM-010).

Definitions used in the scenarios (fixed in the conventions: CV-400, CV-430, CV-480, CV-490, CV-530, CV-540):

- **Heading:** the direction the nose points, projected on the horizontal plane, measured clockwise from north.
- **Track:** the direction of the horizontal velocity, measured clockwise from north. It is not defined when the horizontal speed is zero.
- **Horizontal speed:** the magnitude of the horizontal velocity.
- **Vertical speed:** the rate of change of altitude, positive up.
- **Height above the ground:** the height of the lowest point of the body above the ground plane (CV-400).

On the Aeronef, heading and track are physically independent: the vehicle can move in any horizontal direction whatever its heading. The D56 modes do not use this: in Heading the craft moves along its heading.

### 4.3 Crew and operator role

The **crew** is whoever makes crew selections and reads the annunciations: a human using the TST interactive interface, a scripted test procedure, or an RVS agent. All three use the same **crew interface**. The crew interface is a logical set of selections, annunciations and indications, inspired by an airliner's mode control panel and flight mode annunciator. Its physical form (panels, displays, graphics) is not defined; detailed controls and displays are excluded (AIRCRAFT_CHARACTERISTICS §7).

**Crew selections** (crew-facing units):

| Selection | Unit | Used by |
| --- | --- | --- |
| Selected altitude | ft | Go to altitude; Vertical speed (the level-off altitude) |
| Selected vertical speed (signed, positive up) | ft/min | Vertical speed; Go to altitude, where it replaces the standard vertical speed `[P-AF-220]` |
| Selected horizontal speed | kt | Heading (from zero to the maximum horizontal speed `[P-SYS-230]`) |
| Selected heading | degrees | Heading |
| Mode engage commands: STAT, HDG, ALT, GO ALT, V/S, GO HOVER, TAKEOFF, LAND (D71) | — | Mode logic |

**Annunciations** show the active horizontal and vertical modes, the armed mode, the selected targets and the landing gear position (extended, retracted or in transit) (Section 4.4). **Indications** show the vehicle's current altitude (ft), vertical speed (ft/min), horizontal speed (kt), heading and track (degrees), the remaining fuel (lb, D9), and the LOW FUEL and FUEL EXHAUSTED alerts.

**There is no manual control** (D49, D55): no stick or yoke, and no option for one in this cycle. No scenario uses it.

**The crew's role** is to choose modes and targets on the flight control panel, and to monitor the annunciations. The panel is its own subsystem (FCP, D55) and its content is defined at L2 (#79); there is no stick or yoke (L0-CON-180). Autoflight flies the vehicle in every scenario. The crew does not act on the effectors or on the flight control.

### 4.4 Autoflight operating concept

**Mode groups (D56).** The horizontal and vertical motions are independent. One **horizontal** mode and one **vertical** mode are active at a time, and changing one does not change the other. **Go to hover**, **Hover**, **Takeoff** and **Land** are the only modes that govern both axes: while one of them is active, it replaces both the horizontal and the vertical mode.

**Starting modes.** A run starts on the ground with the effectors off and, as recommended to C5, no mode active (D69, #60). Takeoff is the mode engaged from there. A test run that starts airborne (Section 5) starts with the modes and targets of its initial condition.

**Armed and active.** As a general rule a selected mode first arms, and engages when its conditions are met; while it is armed, the active mode manoeuvres the vehicle into those conditions within g-limited accelerations (D16). The state terms are TBR (#56). Two modes arm others. **Altitude hold** arms with Go to altitude and with Vertical speed, and captures the selected altitude. **Hover** arms with Go to hover and with Takeoff, and engages once the vehicle is stationary at the hover height `[P-AF-210]`; after a Takeoff, it engages once the gear is retracted (C5 confirms).

**Annunciation.** Each change of an active mode, an armed mode or a target is annunciated within `[P-SYS-470]` (L1-AER-470); `[P-AF-060]` is the autoflight share of that time.

**Targets.** Changing a target does not change the mode. The vehicle goes to the new target.

**Attitude (D10, D57).** Pitch and roll are held at zero, within `[P-AF-180]`, at all times. The vehicle translates along three axes and rotates about the vertical axis only. Heading:

- in Heading, the heading is the selected heading and the vehicle moves along it; with no horizontal speed, a heading change turns the vehicle in place;
- in Stationary, Go to hover, Hover, Takeoff and Land, the heading is held at its value when the mode became active.

The vertical modes do not change the heading.

**Mode catalogue (D56).**

| Mode | Axes | Crew selection | What it does | Provisional labels (armed / active) | Scenarios |
| --- | --- | --- | --- | --- | --- |
| Stationary | Horizontal | None | Stops the horizontal motion within the acceleration limits (D16) and holds the horizontal position over the ground, against the wind | — / STAT | SC-040, SC-090, SC-110 |
| Heading | Horizontal | Selected heading (degrees), selected horizontal speed (kt) | Turns to the selected heading and moves along it at the selected horizontal speed; at zero speed, a heading change turns the vehicle in place | — / HDG | SC-050, SC-060, SC-120, SC-110 |
| Altitude hold | Vertical | None (captured altitude, or altitude at engagement) | Holds the altitude | ALT / ALT | SC-020, SC-040, SC-050, SC-060, SC-090, SC-110 |
| Go to altitude | Vertical | Selected altitude (ft); optionally a selected vertical speed (ft/min) | Climbs or descends toward the selected altitude at the standard vertical speed `[P-AF-220]`, or at the selected vertical speed if the crew sets one; arms Altitude hold | — / GO ALT | SC-020, SC-050, SC-110 |
| Vertical speed | Vertical | Selected vertical speed (ft/min), selected altitude (ft) | Climbs or descends at the selected constant rate toward the selected altitude; arms Altitude hold, so it levels off there | — / V/S | SC-040, SC-050, SC-110 |
| Go to hover | Both | None | From whatever the vehicle is flying, brings it to zero velocity on all axes at the hover height `[P-AF-210]`, descending from above or climbing from below (D70); arms Hover | — / GO HOVER | SC-100, SC-110, SC-130 |
| Hover | Both | None | Holds the hover height and the position over the ground, against the wind | HOVER / HOVER | SC-100, SC-110, SC-130 |
| Takeoff | Both | None | Engaged on the ground: switches the effectors on, climbs vertically at `[P-AF-240]` to the hover height `[P-AF-210]` over its ground position, retracts the gear and hands over to Hover (D69) | — / TAKEOFF (HOVER armed) | SC-130, SC-110 |
| Land | Both | None | Engaged only from Hover: extends the gear, descends vertically at `[P-AF-240]`, lands within the landing envelope, then switches the effectors off, so that no more fuel is used (D69) | — / LAND | SC-130, SC-110 |

In the scenario tables, the active modes are written `horizontal · vertical`, for example `HDG · ALT`. Go to hover and Hover are written alone.

### 4.5 Fuel concept

The Aeronef carries a finite quantity of fuel, at most `[P-FU-010]`. Fuel is consumed to produce effector forces and moments, with separate configurable terms for translation and rotation. Because the effectors must counter gravity, fuel is consumed in every airborne condition, including Hover and Stationary. On the ground the effectors are off and no fuel is consumed (D69). Vehicle mass decreases as fuel is consumed; the centre of gravity stays fixed.

Fuel is shown to the crew in pounds (D9). When the remaining fuel falls below `[P-FU-020]` of full capacity, the Aeronef annunciates LOW FUEL. When the fuel is exhausted, the Aeronef annunciates FUEL EXHAUSTED and the effectors produce zero force and zero moment. The vehicle then moves under gravity and drag alone, and its ground contact is a crash (D68). Fuel exhaustion is nominal behaviour (SC-110); running out of fuel is the crew's to avoid, with the LOW FUEL alert. What the annunciations show after exhaustion is set by C5 (D68).

### 4.6 Runs and the use of operational data

**A run** is one execution of the Aeronef in the TST. It is defined by:

- a **configuration**: the vehicle parameter set, the flight-control-law version and the autoflight version;
- an **initial condition**: position, velocity, attitude, angular rate, landing gear position, fuel quantity, active and armed modes, and selected targets. A run starts on the ground (D69);
- a **selection script**: crew selections, each with the simulation time at which it applies (empty for an interactive run, where the selections come from a human).

The run ends when the TST's end condition is met: the scenario's end condition, a maximum run time set by the TST, or a crash (D37, D68, D69). A landing does not end the run.

**Operational data.** At each output sample, every `[P-TM-010]` (L1-AER-600), the Aeronef outputs data on one time base (simulation time since the start of the run): the crew selections received, the selected targets, the active and armed modes, the annunciations and indications, the vehicle state, the fuel quantity, and the flight-control and effector activity. Whether each signal is **releasable** or **protected** is decided with the RVS (#69, D44; L1-AER-630).

| User | Uses the operational data to |
| --- | --- |
| TST (automated tests) | Assess results against requirement success criteria; report pass or fail. |
| Interactive operator | See cause and effect while exploring. |
| RVS | Correlate crew selections, mode changes, annunciations and vehicle response, using releasable signals only. |
| Evaluators | Score the RVS's predictions on unseen runs. |

## 5. Common scenario format

Each flight scenario gives: purpose; initial conditions; crew selections; a sequence table; expected vehicle behaviour; end conditions; the needs it exercises; and the parts that are TBR.

Common to all flight scenarios unless a scenario says otherwise:

- The vehicle starts on the ground, at rest on its extended gear with the effectors off and no mode active (D69). For the flight scenarios SC-020 to SC-120, a test procedure may instead start the run airborne (D73): the vehicle is then inside the operating volume at `H_INIT`, with a height above the ground of at least `[P-SYS-210]`, the gear retracted, the effectors on and the modes of the scenario active. Otherwise each such scenario begins with a Takeoff and the selections that reach its initial condition.
- Fuel is `FUEL_INIT`, more than the low-fuel threshold `[P-FU-020]` and enough to complete the scenario.
- Pitch and roll are zero (D57); the angular rate is zero.
- The air is still, and no disturbance is applied.
- Every selected value is within the performance envelope: horizontal speed up to `[P-SYS-230]`, climb vertical speed up to `[P-SYS-240]`, descent vertical speed up to `[P-SYS-250]`, heading rate up to `[P-SYS-270]`. The acceleration sensed by the crew stays within `[P-SYS-120]` (gravity included; L0-CON-310). Selected values are multiples of the selection resolutions `[P-AF-010]` to `[P-AF-040]`.
- "Settled" means within the stated tolerance, reached within `[P-AF-190]` s of the capture onset or target change, and kept until the end of the scenario. Each tolerance is a placeholder until the per-mode requirements (Phase 4) fix it.
- Each annunciation change in the sequence tables occurs within `[P-SYS-470]` of its trigger.
- The scenario ends when the stated end condition holds for an observation time `T_OBS`, chosen by the test procedure.

In the sequence tables, **Trigger** is a crew selection or a condition reached by the vehicle. **Active** and **Armed** are the annunciated modes after the trigger.

## 6. Scenarios

### 6.1 Vertical scenarios

#### SC-010 — Withdrawn

Climb on flight path angle. Withdrawn with the flight path angle mode (D56). The ID is not reused.

#### SC-020 — Go to an altitude and hold it

**Purpose.** Show Go to altitude: a climb or descent to a selected altitude at the standard vertical speed, a change of the vertical speed during the manoeuvre, and the automatic capture and hold of the selected altitude.

**Initial conditions.** Common conditions. Active `HDG · ALT`, holding `H_INIT`, horizontal speed `SPD_INIT`, heading `HDG_INIT`.

**Crew selections.** Selected altitude `H_SEL` (ft), below `H_INIT` and at least `[P-SYS-210]`. Then GO ALT engaged. During the descent, a selected vertical speed `VS_SEL` (ft/min), negative.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `H_SEL` | HDG · ALT | — | No change. |
| 2 | Crew engages GO ALT | HDG · GO ALT | ALT | The vehicle descends at the standard vertical speed `[P-AF-220]`. Heading and horizontal speed held. |
| 3 | Crew sets `VS_SEL` | HDG · GO ALT | ALT | The vertical speed goes to `VS_SEL`. |
| 4 | Capture onset, as the altitude approaches `H_SEL` (onset set by the mode logic) | HDG · ALT | — | The vertical speed decreases toward zero; the vehicle levels off at `H_SEL` without passing it by more than `[P-AF-100]`. |
| 5 | Vehicle established on `H_SEL` | HDG · ALT | — | Altitude held at `H_SEL`. |

**Expected vehicle behaviour.** Before step 3, the vertical speed settles within `[P-AF-090]` of `[P-AF-220]`; after it, within `[P-AF-090]` of `VS_SEL`. Heading and horizontal speed are held throughout, within `[P-AF-130]` and `[P-AF-120]`. The altitude overshoot stays within `[P-AF-100]`, and the altitude then settles within `[P-AF-110]` of `H_SEL`.

**Variation SC-020 / climb.** As SC-020 with `H_SEL` above `H_INIT` and a positive `VS_SEL`.

**End conditions.** `HDG · ALT` active, nothing armed, altitude within `[P-AF-110]` of `H_SEL`.

**Needs exercised.** N-050, N-060, N-070, N-080, N-090, N-170, N-210.

**TBR.** The capture label, if any (C5).

#### SC-030 — Withdrawn

Descent on flight path angle. Withdrawn with the flight path angle mode (D56). The ID is not reused.

#### SC-040 — Climb on vertical speed with zero horizontal speed

**Purpose.** Show Vertical speed, and the Aeronef's ability to climb vertically: the vehicle climbs with no horizontal motion and without tilting.

**Initial conditions.** Common conditions. Active `STAT · ALT`, the vehicle stationary at `H_INIT`, heading `HDG_INIT`.

**Crew selections.** Selected altitude `H_SEL` (ft), above `H_INIT`. Selected vertical speed `VS_SEL` (ft/min), positive. Then V/S engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `H_SEL` | STAT · ALT | — | No change. |
| 2 | Crew engages V/S with `VS_SEL` | STAT · V/S | ALT | The vehicle climbs vertically at `VS_SEL`. It holds its horizontal position; heading held; pitch and roll zero. |
| 3 | Capture onset | STAT · ALT | — | The vertical speed decreases toward zero; the vehicle levels off at `H_SEL`. |
| 4 | Vehicle established on `H_SEL` | STAT · ALT | — | Altitude held at `H_SEL`; the vehicle stays stationary. |

**Expected vehicle behaviour.** Vertical speed settles within `[P-AF-090]` of `VS_SEL`. The horizontal position stays within `[P-SYS-450]` of its value at the start. Heading stays within `[P-AF-130]` of `HDG_INIT`. The altitude overshoot stays within `[P-AF-100]`, and the altitude then settles within `[P-AF-110]` of `H_SEL`.

**End conditions.** `STAT · ALT` active, the vehicle stationary at `H_SEL` within `[P-AF-110]`.

**Needs exercised.** N-050, N-060, N-070, N-080, N-100, N-190, N-240.

**TBR.** What V/S does with no selected altitude, or one behind the direction of motion (C5).

#### SC-050 — Change targets and modes in flight

**Purpose.** Show that targets can be changed while their modes are active, that the crew can change either mode at any time, and that the crew can level off by engaging Altitude hold directly.

**Initial conditions.** Common conditions. Active `HDG · ALT` at `H_INIT`, `SPD_INIT`, `HDG_INIT`.

**Crew selections.** In order, each after the previous one has settled: a new selected speed `SPD_2`; a new selected heading `HDG_2`; `H_SEL` above `H_INIT` with GO ALT engaged; V/S engaged at `VS_2` during the climb; ALT engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `SPD_2` | HDG · ALT | — | Horizontal speed goes to `SPD_2`. |
| 2 | Crew sets `HDG_2` | HDG · ALT | — | The vehicle yaws toward `HDG_2` at a heading rate up to `[P-SYS-270]`, in the shorter direction (mode logic to confirm), and its motion turns with it. |
| 3 | Crew sets `H_SEL` and engages GO ALT | HDG · GO ALT | ALT | Climb at the standard vertical speed. |
| 4 | Crew engages V/S at `VS_2` | HDG · V/S | ALT | Vertical speed goes to `VS_2`; Altitude hold stays armed on `H_SEL`. |
| 5 | Crew engages ALT before the capture onset | HDG · ALT | — | The vehicle stops climbing and holds the altitude reached, below `H_SEL`. |

**Expected vehicle behaviour.** Each new target is settled within its tolerance: `[P-AF-120]` for speed, `[P-AF-130]` for heading, `[P-AF-090]` for vertical speed, `[P-AF-110]` for the level-off altitude. Changing the horizontal mode or target leaves the vertical one held, and the reverse.

**End conditions.** `HDG · ALT` active, all targets settled.

**Needs exercised.** N-060, N-090, N-100, N-170, N-200, N-210.

**TBR.** Which altitude ALT holds in step 5: the altitude at engagement, or where the vertical speed reaches zero (C5).

### 6.2 Horizontal scenarios

#### SC-060 — Fly a heading at a set horizontal speed

**Purpose.** Show Heading: the vehicle turns its nose to the selected heading and moves along it at the selected speed.

**Initial conditions.** Common conditions. Active `STAT · ALT` at `H_INIT`, stationary, heading `HDG_INIT`.

**Crew selections.** Selected heading `HDG_SEL` (degrees), different from `HDG_INIT`. Selected speed `SPD_SEL` (kt). Then HDG engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `HDG_SEL`, `SPD_SEL` and engages HDG | HDG · ALT | — | The vehicle yaws toward `HDG_SEL` and accelerates along its heading toward `SPD_SEL`, within its acceleration limits (D16). Altitude held. |
| 2 | Heading and speed reached | HDG · ALT | — | Straight, level flight on `HDG_SEL` at `SPD_SEL`. |

**Expected vehicle behaviour.** Heading settles within `[P-AF-130]` of `HDG_SEL`; track settles within `[P-AF-140]` of `HDG_SEL`; horizontal speed within `[P-AF-120]` of `SPD_SEL`; altitude within `[P-AF-110]` of `H_INIT` throughout. Pitch and roll stay within `[P-AF-180]` of zero. The heading rate stays within `[P-SYS-270]`.

**Variation SC-060 / wind.** With a wind applied, the vehicle still moves along its heading over the ground (this reading; C5).

**End conditions.** Heading, track, speed and altitude settled.

**Needs exercised.** N-050, N-060, N-070, N-090, N-160, N-170.

**TBR.** Whether the selected speed and the heading are over the ground or through the air when there is wind (C5).

#### SC-070 — Withdrawn

Fly a constant track. Withdrawn with the track hold mode (D56). The ID is not reused.

#### SC-080 — Withdrawn

Intercept and track a VOR radial. Withdrawn with the VOR function (D56). The ID is not reused.

#### SC-120 — Turn in place

**Purpose.** Show that with no horizontal speed a heading change turns the vehicle about its vertical axis without moving it (D56).

**Initial conditions.** Common conditions. Active `HDG · ALT` with the selected horizontal speed at zero; the vehicle stationary at `H_INIT`, heading `HDG_INIT`.

**Crew selections.** Selected heading `HDG_SEL` (degrees), different from `HDG_INIT`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew sets `HDG_SEL` | HDG · ALT | — | The vehicle yaws toward `HDG_SEL` at a heading rate up to `[P-SYS-270]`, without moving horizontally. |
| 2 | Heading reached | HDG · ALT | — | Heading held; the vehicle stays where it is. |

**Expected vehicle behaviour.** Heading settles within `[P-AF-130]` of `HDG_SEL`. Horizontal speed stays within `[P-AF-120]` of zero. Altitude within `[P-AF-110]` of `H_INIT`.

**End conditions.** Heading settled, the vehicle not moving.

**Needs exercised.** N-050, N-060, N-160, N-190, N-240.

**TBR.** Whether Heading at zero speed holds the position against the wind, as Stationary does (C5).

### 6.3 Hold scenarios

#### SC-090 — Stop and hold a position

**Purpose.** Show Stationary: the vehicle stops its horizontal motion and holds its position over the ground, against the wind, at its altitude.

**Initial conditions.** Common conditions. Active `HDG · ALT` at `H_INIT`, horizontal speed `SPD_INIT` (which can be zero), heading `HDG_INIT`.

**Crew selections.** STAT engaged at time `T_ENG`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages STAT | STAT · ALT | — | The vehicle decelerates within its acceleration limits (D16) and holds a reference position. Altitude held; heading held at its value at `T_ENG`; pitch and roll zero. |
| 2 | Vehicle at the reference position | STAT · ALT | — | Position held. |

**Expected vehicle behaviour.** The horizontal position settles within `[P-SYS-450]` of the reference position (D60), and the heading within `[P-AF-130]` of its value at `T_ENG`.

**Variation SC-090 / wind.** As SC-090 with a wind applied: the vehicle holds the reference position against the wind.

**Variation SC-090 / leave Stationary.** The crew engages HDG; the vehicle accelerates to the selected speed on the selected heading, and the vertical mode is unchanged.

**End conditions.** `STAT · ALT` active; horizontal position within `[P-SYS-450]` of the reference position.

**Needs exercised.** N-050, N-060, N-130, N-140, N-160, N-210.

**TBR.** The reference position: where the vehicle stops, or its position at `T_ENG` (C5).

#### SC-100 — Go to hover, then hover

**Purpose.** Show Go to hover and Hover (D56): from whatever the vehicle is flying, it stops on all axes at the hover height above the ground, then Hover engages and holds height and position against the wind.

**Initial conditions.** Common conditions. Active `HDG · ALT` at `H_INIT` above the hover height `[P-AF-210]`, horizontal speed `SPD_INIT`, heading `HDG_INIT`.

**Crew selections.** GO HOVER engaged at time `T_ENG`.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages GO HOVER | GO HOVER | HOVER | The vehicle stops its horizontal motion and descends toward `[P-AF-210]`, within its acceleration limits (D16), at its current heading. Pitch and roll zero. |
| 2 | Vehicle stationary at `[P-AF-210]` | HOVER | — | The vehicle holds the hover height and its position over the ground. |

**Expected vehicle behaviour.** The altitude settles within `[P-AF-110]` of `[P-AF-210]`. Horizontal speed settles within `[P-AF-170]` of zero, and the horizontal position is then held within `[P-SYS-450]` (D60). The heading stays within `[P-AF-130]` of `HDG_INIT`.

**Variation SC-100 / wind.** As SC-100 with a wind applied: Hover holds the position against it.

**Variation SC-100 / from below.** GO HOVER is engaged during a Land, below the hover height. The vehicle climbs back to the hover height and Hover engages (D70). Whether the gear retracts is set by C5.

**End conditions.** HOVER active at `[P-AF-210]`; horizontal position held within `[P-SYS-450]`.

**Needs exercised.** N-050, N-060, N-130, N-160, N-200, N-210.

**Answered (D70):** engaged below the hover height, Go to hover climbs to it. **TBR.** How the crew leaves Hover (C5).

#### SC-130 — Take off, hover, land and rest

**Purpose.** Show the ground operations of D69. A run starts on the ground with the effectors off. Takeoff lifts the vehicle to the hover height and retracts the gear. Land extends the gear and touches down within the landing envelope. The vehicle then rests on the ground with no fuel used.

**Initial conditions.** On the ground at rest on the extended gear, effectors off, no mode active, heading `HDG_INIT`, fuel `FUEL_INIT` above the low-fuel threshold. Still air.

**Crew selections.** TAKEOFF at `T_TO`; LAND at `T_LD`, after Hover has engaged.

| Step | Trigger | Active | Armed | Vehicle behaviour |
| --- | --- | --- | --- | --- |
| 1 | Crew engages TAKEOFF | TAKEOFF | HOVER | The effectors power up. The vehicle lifts off and climbs vertically at `[P-AF-240]`, heading and horizontal position held, pitch and roll zero. |
| 2 | Height above the ground reaches `[P-AF-210]` | TAKEOFF | HOVER | The vehicle holds the hover height. The gear retracts within `[P-DYN-050]`, and the gear position is annunciated. |
| 3 | Gear retracted, vehicle stationary at the hover height | HOVER | — | Holds the hover height and the position over the ground. |
| 4 | Crew engages LAND | LAND | — | The gear extends within `[P-DYN-050]`; the vehicle then descends vertically at `[P-AF-240]`. |
| 5 | Ground contact on the extended gear | LAND, then none (C5) | — | Landing event. The vehicle is at rest on the gear; the effectors are off within `[P-SYS-480]`. |
| 6 | On the ground for `T_REST` | None | — | The vehicle stays at rest; the remaining fuel is constant; the sensed acceleration is 1 g. |

**Expected vehicle behaviour.** The horizontal position stays within `[P-SYS-450]` of its value on the ground. At the contact, the vertical speed magnitude is at most `[P-SYS-500]` and the horizontal speed at most `[P-SYS-510]`, and the gear is extended. From `[P-SYS-480]` after the contact, every effector output is zero and the remaining fuel mass does not change. The heading stays within `[P-AF-130]` of `HDG_INIT`.

**Variation SC-130 / wind.** As SC-130 with a steady wind and gusts within the wind envelope during the hover and the landing. The takeoff is made in a wind of at most `[P-SYS-580]` (D73).

**Variation SC-130 / zero fuel.** The run starts with no fuel. FUEL EXHAUSTED is annunciated; the vehicle stays on the ground. Whether TAKEOFF is accepted is set by C5.

**Variation SC-130 / go to hover during the landing.** GO HOVER is engaged during step 4. The vehicle climbs back to the hover height and Hover engages (D70).

**Variation SC-130 / second takeoff.** After step 6, TAKEOFF is engaged again, and the vehicle repeats steps 1 to 3.

**End conditions.** On the ground at rest, effectors off, for `T_REST`.

**Needs exercised.** N-050, N-060, N-150, N-210, N-310, N-450.

**TBR.** The mode state after the landing, and the selections accepted on the ground (C5, #60). Whether LAND stays annunciated on the ground (C5). The gear labels (C5, C8).

### 6.4 Reference mission

#### SC-110 — Reference mission to fuel exhaustion

**Purpose.** Fly a fixed, repeatable profile that uses every mode of the catalogue, with translation and rotation, until the fuel is exhausted. The mission is the common basis for measuring accuracy and fuel used (N-250), and it shows the nominal behaviour at low fuel and at fuel exhaustion.

**Initial conditions.** On the ground at rest on the extended gear, effectors off, no mode active. Fuel at full capacity `[P-FU-010]`, so mass at its maximum. Heading `HDG_INIT`.

**Profile.** Each leg starts when the previous leg's end condition is met. The scenario variables (altitudes, speeds, headings, vertical speeds and leg durations `T_n`) form one fixed reference set, chosen so that fuel remains at the start of leg 10.

| Leg | Crew selections | Active (after captures) | Armed | Vehicle behaviour | Leg ends when |
| --- | --- | --- | --- | --- | --- |
| 0 | TAKEOFF | TAKEOFF, then HOVER | HOVER | Powers up, lifts off, climbs vertically at `[P-AF-240]` to the hover height, retracts the gear (as SC-130). | HOVER active |
| 1 | None | HOVER | — | Holds the hover height and position for `T_1`. | `T_1` elapsed |
| 2 | `HDG_1`, `SPD_1`, HDG engaged; `H_1` above the hover height, GO ALT | HDG · GO ALT, then HDG · ALT | ALT | Leaves Hover, turns, accelerates along the heading, climbs at the standard vertical speed, captures `H_1`. | Established on `H_1` |
| 3 | None | HDG · ALT | — | Cruises on `HDG_1`. | `T_3` elapsed |
| 4 | `H_2` below `H_1`, GO ALT, then `VS_2` | HDG · GO ALT, then HDG · ALT | ALT | Descends, first at the standard vertical speed, then at `VS_2`; captures `H_2`. | Established on `H_2` |
| 5 | `HDG_2`, `SPD_2` | HDG · ALT | — | Turns to `HDG_2` and changes speed. | `T_5` elapsed |
| 6 | `H_3` below `H_2`, V/S at a negative `VS_3` | HDG · V/S, then HDG · ALT | ALT | Descends at `VS_3`, captures `H_3`. | Established on `H_3` |
| 7 | GO HOVER | GO HOVER, then HOVER | HOVER | Stops and descends to the hover height, then hovers (as SC-100). | `T_7` elapsed in HOVER |
| 7a | LAND | LAND | — | Extends the gear, descends at `[P-AF-240]`, lands within the envelope, switches the effectors off; rests on the ground for `T_7A` with the remaining fuel constant (as SC-130). | `T_7A` elapsed on the ground |
| 7b | TAKEOFF | TAKEOFF, then HOVER | HOVER | As leg 0. | HOVER active |
| 8 | STAT, `H_4` above the hover height, V/S at a positive `VS_4` | STAT · V/S, then STAT · ALT | ALT | From HOVER (after leg 7b), climbs vertically and captures `H_4` (as SC-040). | Established on `H_4` |
| 9 | HDG engaged with `SPD` at zero, `HDG_3` | HDG · ALT | — | Turns in place to `HDG_3` (as SC-120). | Heading settled |
| 10 | STAT | STAT · ALT | — | Holds position until the fuel is exhausted. LOW FUEL is annunciated when the fuel falls below `[P-FU-020]`. | Fuel exhausted |
| 11 | None | (C5, D68) | — | FUEL EXHAUSTED annunciated. Effectors produce zero force and zero moment. The vehicle falls under gravity and drag, keeps the angular rate it had at exhaustion, and its ground contact is a crash (D68). | Crash, or TST maximum run time |

**Expected vehicle behaviour.** Each leg meets the expected behaviour of the scenario it repeats: SC-060 and SC-020 (leg 2), SC-060 (legs 3 and 5), SC-020 (leg 4), SC-040 (legs 6 and 8, vertical part), SC-100 (leg 7), SC-040 (leg 8), SC-120 (leg 9), SC-090 (leg 10). The fuel quantity never increases; it decreases in every airborne leg and is constant during the rest of leg 7a. Leg 0 and leg 7b meet SC-130 (takeoff), and leg 7a meets SC-130 (landing and rest). The vehicle mass decreases by the mass of fuel consumed. LOW FUEL is annunciated within `[P-SYS-470]` of the fuel falling below `[P-FU-020]`, and FUEL EXHAUSTED within `[P-SYS-470]` of exhaustion. After exhaustion, the motion is free fall with drag, which can be compared with an independent solution (N-290). The run ends at the ground contact after exhaustion, which is a crash (D68).

**Variation SC-110 / hover endurance.** From the same initial condition, TAKEOFF is engaged at the start and HOVER kept until the fuel is exhausted. The time from the TAKEOFF engagement to exhaustion is at least `[P-SYS-280]` (L1-AER-360).

**Recorded results.** Total fuel used per leg, mission duration to exhaustion, and the tracking errors per leg against the tolerances above.

**End conditions.** Crash, or TST maximum run time.

**Needs exercised.** N-050, N-060, N-080, N-100, N-130, N-140, N-150, N-170, N-200, N-250, N-280, N-290, N-450.

**TBR.** As in the scenarios each leg repeats. How the crew leaves Hover in legs 2 and 8 (C5). Annunciations after fuel exhaustion (C5, D68).

### 6.5 Platform and evidence scenarios

These scenarios describe how the TST and the RVS use the Aeronef. They exercise the Aeronef's configuration, run and operational-data needs, not its flight modes.

#### SC-200 — Unattended verification run

**Purpose.** A test procedure verifies a requirement with no human involved.

**Sequence.**

1. The TST creates an Aeronef instance with a configuration (parameter set, control-law version, autoflight version), each identified by a version.
2. The TST sets the initial condition, including the active and armed modes and the targets.
3. The TST runs the simulation without graphics, faster than real time, and applies the crew selections of the selection script at their simulation times. The selections go through the crew interface.
4. At each output sample, the Aeronef outputs its operational data.
5. The run ends on the procedure's end condition, the maximum run time or a crash.
6. The TST assesses the data against the procedure's success criteria and reports the result with the configuration identification.

**Expected behaviour of the Aeronef.** The same configuration, initial condition and selection script give the same pass or fail verdict for each success criterion on each repetition, with the data agreeing within the stated tolerances; the runs need not be bit-identical (D25, D59). The Aeronef needs no input other than the configuration, the initial condition, the selection script and the time steps.

**Needs exercised.** N-300, N-310, N-320, N-330, N-340, N-350, N-370.

#### SC-210 — Parallel and Monte Carlo campaign

**Purpose.** Run many independent Aeronef instances at once, for example a regression campaign overnight or a Monte Carlo campaign over parameters and initial conditions.

**Sequence.** The TST starts many instances in parallel, each with its own configuration, initial condition and selection script. Variations change parameter values (within their stated ranges), initial conditions and selected targets. Each instance runs as in SC-200.

**Expected behaviour of the Aeronef.** Instances do not share state, and the results of one instance do not depend on how many others are running or in what order. Each run is reproducible on its own.

**Needs exercised.** N-020, N-300, N-330, N-350.

#### SC-220 — Comparative evaluation of control laws

**Out of scope this cycle.** There is one autoflight implementation (D24) and one set of control laws for now (D42), so there is nothing to compare. The scenario is kept for when a second control-law design is added.

**Purpose.** Compare two control-law versions under the same conditions.

**Sequence.** The TST runs the same set of scenarios (for example SC-020 to SC-120) once with version A and once with version B. Only the version under comparison changes; the vehicle model, the parameter set, the initial conditions and the selection scripts are the same. The TST compares tracking accuracy, mode-transition behaviour and fuel used.

**Expected behaviour of the Aeronef.** The swap is a configuration change. The vehicle model, the crew interface and the operational data format stay the same for both versions.

**Needs exercised.** N-220, N-230, N-250, N-350.

#### SC-230 — Interactive exploration

**Purpose.** An engineer explores cause and effect by flying the Aeronef interactively.

**Sequence.** The TST runs one instance in real time. The engineer makes crew selections at any time, as in the flight scenarios, and watches the annunciations, the indications and the vehicle state. Graphics are optional.

**Expected behaviour of the Aeronef.** It accepts a selection at any simulation step and behaves as it does when the same selection comes from a script at the same time.

**Needs exercised.** N-320, N-360, N-390.

#### SC-240 — Reverse-engineering experiment

**Purpose.** The RVS runs its own experiments on the released Aeronef.

**Sequence.**

1. The RVS receives a released package: the operational manuals and an executable TST configuration that outputs releasable data only. It does not receive requirements, design, source code, this ConOps or protected signals.
2. An RVS agent, acting as the crew, chooses an initial condition from those the package allows, and applies crew selections through the crew interface.
3. The RVS records the releasable operational data and correlates its selections with the mode changes, the annunciations and the vehicle response, on the common time base.
4. The RVS predicts the response to new selections and checks the prediction with new runs.

**Expected behaviour of the Aeronef.** The released Aeronef behaves the same as the protected one. Its releasable data is enough to relate each selection to its effect, and contains nothing classified protected.

**Needs exercised.** N-030, N-380, N-390, N-400, N-420.

## 7. Open questions and TBR items

### 7.1 Dependencies on the plan's questions

The owner answered the plan's questions on 2026-10-25 (plan §9). Where a question is still open, the marked parts may change.

| Question | Status | Where it applies |
| --- | --- | --- |
| Q2 — Attitude during the guidance modes | **Decided (D10, revised by D57):** pitch and roll at zero at all times. The heading rules of Section 4.4 are this document's reading, to confirm at L2 (A2-Q03). | Section 4.4; every scenario |
| Q3 — Hover versus Position Hold | **Replaced (D56):** Stationary is a horizontal mode; Go to hover and Hover govern both axes, Hover engaging once the vehicle is stationary at the hover height. | SC-090, SC-100, SC-110 legs 7 and 10 |
| Q4 — VOR model | **Withdrawn (D56):** there is no VOR. | — |
| Q5 — Mode combinations | **Decided (D56):** one horizontal and one vertical mode at a time, independent; Go to hover and Hover govern both. | Section 4.4; every sequence table |

### 7.2 Questions raised by this document

Each question has a proposed answer, used in the scenarios. They are recorded in `work/A2/issues.md`; the owner's answers of 2026-10-25 are marked **Owner**.

| ID | Question | Proposed answer |
| --- | --- | --- |
| A2-Q01 | Is the air still (no wind) in this cycle? | Yes. Drag is relative to still air; horizontal speed is the same relative to air and ground. **Owner: no.** There is wind, uniform and configurable per run (D17, #49). |
| A2-Q02 | Are take-off, landing and ground contact in scope? | No. Runs start airborne; reaching the ground plane ends the run. **Owner:** landing is in scope as an ideal landing; contact outside the landing envelope is a crash (D8, D37). **Revised (D69):** runs start on the ground on a landing gear; Takeoff and Land are modes; a landing does not end the run. |
| A2-Q03 | In HDG, does the track follow the heading? In TRK and VOR, what does the heading do? | HDG sets the heading, and the track follows it. TRK and VOR hold the heading at its value when the mode became active. Deferred to L2 (D33). **Superseded in part (D56):** no TRK or VOR; in Heading the vehicle moves along its heading. |
| A2-Q04 | After fuel exhaustion, do the autoflight modes stay engaged? | Yes. The modes stay engaged and annunciated; FUEL EXHAUSTED is annunciated; there is no automatic disengagement. **Owner:** defined in detailed design (#59, deferred). **Owner (D68):** the effectors stop, the vehicle falls and its ground contact is a crash; the annunciations after exhaustion are C5's. |
| A2-Q05 | Can a mode group have no active mode? | No. Each group has one active mode, or a hold mode covers it; the run's initial condition sets the starting modes. **Owner:** deferred to L2 (#60). On the ground, no mode is active (recommended to C5, D69, #60). |
| A2-Q06 | What happens when FPA is selected with horizontal speed near zero? | FPA does not engage below `[P-AF-070]`; the active vertical mode stays as it was. **Owner: rejected** (D13, #61). **Withdrawn with the FPA mode (D56).** |
| A2-Q07 | Do Position Hold and Hover also replace the speed group? | Yes, because both hold zero horizontal speed. **Superseded (D56):** Stationary is horizontal only; Hover governs both axes. |
| A2-Q08 | What happens when the vehicle passes over a VOR station? | Not covered in this cycle's scenarios. **Withdrawn (D56):** there is no VOR. |
| A2-Q09 | In what crew-facing unit is fuel shown? D7 does not cover fuel. | Percent of full fuel capacity. **Owner:** pounds (lb), not percent (D9, #51). |
| A2-Q10 | How does the crew leave Position Hold or Hover? | By engaging a mode in any group. **Revised (D56):** Stationary is left by engaging HDG, and the vertical mode is unchanged. How Hover is left is for C5. |
| A2-Q11 | Which altitude does Hover hold? | The altitude at engagement, as Position Hold does. **Owner:** Hover descends to the altitude set on the flight control panel (D11). **Revised (D56):** the hover height is a project constant `[P-AF-210]`, not a panel selection. |
| A2-Q12 | Do scenario values belong in the parameter database? | No. Scenario values are scenario variables set by the test procedures; the parameter database holds system values only. **Owner: yes.** Test procedures set scenario values; they are not design parameters (D32, #62). |

## 8. Traceability

### 8.1 Scenario → needs → D56 modes

| Scenario | Needs exercised | D56 modes |
| --- | --- | --- |
| SC-010 | — | Withdrawn (D56) |
| SC-020 | N-050, N-060, N-070, N-080, N-090, N-170, N-210 | Go to altitude, Altitude hold, Heading |
| SC-030 | — | Withdrawn (D56) |
| SC-040 | N-050, N-060, N-070, N-080, N-100, N-190, N-240 | Vertical speed, Altitude hold, Stationary |
| SC-050 | N-060, N-090, N-100, N-170, N-200, N-210 | Heading, Go to altitude, Vertical speed, Altitude hold |
| SC-060 | N-050, N-060, N-070, N-090, N-160, N-170 | Heading, Stationary, Altitude hold |
| SC-070 | — | Withdrawn (D56) |
| SC-080 | — | Withdrawn (D56) |
| SC-090 | N-050, N-060, N-130, N-140, N-160, N-210 | Stationary, Altitude hold, Heading |
| SC-100 | N-050, N-060, N-130, N-160, N-200, N-210 | Go to hover, Hover |
| SC-110 | N-050, N-060, N-080, N-100, N-130, N-140, N-150, N-170, N-200, N-250, N-280, N-290, N-450 | All nine modes |
| SC-120 | N-050, N-060, N-160, N-190, N-240 | Heading (at zero speed), Altitude hold |
| SC-130 | N-050, N-060, N-150, N-210, N-310, N-450 | Takeoff, Hover, Land, Go to hover |
| SC-200 | N-300, N-310, N-320, N-330, N-340, N-350, N-370 | — |
| SC-210 | N-020, N-300, N-330, N-350 | — |
| SC-220 | N-220, N-230, N-250, N-350 | — |
| SC-230 | N-320, N-360, N-390 | — |
| SC-240 | N-030, N-380, N-390, N-400, N-420 | — |

Each of the nine modes of D56 and D69 is exercised by at least one scenario of its own and by SC-110.

### 8.2 Needs not exercised by a scenario

These needs apply to the requirements, the parameter database or the documentation, not to an operation. L0 and L1 requirements cite them directly.

| Need | Covered by |
| --- | --- |
| N-010 | L0 constraints (modelling boundaries) |
| N-040, N-410, N-440 | L0 and the traceability rules of METHODOLOGY 10.4 |
| N-180 | None: no manual control in this cycle (D49, D55); kept for later |
| N-260 | Flight-control requirements on saturation (task C4); saturation may occur in any scenario but is not a scenario of its own |
| N-110, N-120 | Withdrawn (D56) |
| N-270 | MS-DYN (task C1) |
| N-430 | The scenario format of this document (Section 5) and the operational manuals |

## 9. Parameters referenced

Values, status (TBD, TBR or Set), SI units and crew-facing flags are in `parameters/PARAMETERS.yaml`.

| ID | Name |
| --- | --- |
| P-SYS-200 | Maximum operating altitude |
| P-SYS-210 | Minimum operating height above the ground |
| P-SYS-220 | Horizontal operating radius |
| P-SYS-230 | Maximum horizontal speed |
| P-SYS-240 | Maximum climb vertical speed |
| P-SYS-250 | Maximum descent vertical speed |
| P-SYS-270 | Maximum heading rate in autoflight |
| P-SYS-280 | Minimum hover endurance at full fuel |
| P-FU-010 | Usable fuel mass at full capacity |
| P-FU-020 | Low-fuel threshold |
| P-AF-010 | Altitude selection resolution |
| P-AF-020 | Vertical speed selection resolution |
| P-AF-030 | Horizontal speed selection resolution |
| P-AF-040 | Heading selection resolution |
| P-AF-060 | Annunciation latency, autoflight share of `[P-SYS-470]` |
| P-AF-090 | Vertical speed tracking tolerance |
| P-AF-100 | Altitude capture maximum overshoot |
| P-AF-110 | Altitude hold tolerance |
| P-AF-120 | Horizontal speed tracking tolerance |
| P-AF-130 | Heading hold tolerance |
| P-AF-140 | Track tolerance in Heading |
| P-AF-160 | Autoflight share of the position-holding budget |
| P-AF-170 | Hover horizontal speed tolerance |
| P-AF-180 | Level attitude tolerance |
| P-AF-190 | Settling time |
| P-AF-210 | Hover height above the ground (D56, D70; CV-400) |
| P-AF-220 | Standard vertical speed of Go to altitude (D56) |
| P-AF-240 | Takeoff and landing vertical speed |
| P-DYN-030 | Body diameter |
| P-DYN-040 | Landing gear length |
| P-DYN-050 | Landing gear transit time |
| P-SYS-450 | Position-holding accuracy, horizontal (Stationary and Hover, D60) |
| P-SYS-120 | Maximum crew-sensed acceleration magnitude (Set) |
| P-SYS-430 | Maximum steady wind speed |
| P-SYS-470 | Annunciation latency, aircraft level |
| P-SYS-480 | Control-loop latency |
| P-SYS-500, P-SYS-510 | Landing envelope |
| P-SYS-560 | Maximum gust speed |
| P-SYS-570 | Minimum gust rise time (D62) |
| P-SYS-580 | Maximum wind speed at liftoff (D73) |
| P-TM-010 | Output sample period |
