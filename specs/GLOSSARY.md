# Aeronef — Glossary

**Status:** Fixed at Gate G0 (D43), 2026-10-27. Extended at later gates from agents' `glossary_proposals.md`; changes to a fixed definition go through a change request. G1 rework (2026-11-04): B1 terms merged, corrected for D55 to D62; *Crew interface*, *Gust*, *Landing envelope*, *Mode catalogue*, *Operational data* and *Subsystem* changed by CR-B1-11.
**Date:** 2026-10-27
**Owner:** Martin (maintained by the orchestrator)
**Classification:** Protected design material. Not for release to the Reverse-Engineering Effort (RVS).

Requirements use only the terms defined here (METHODOLOGY §8.4 rule 12), with the meaning given here. A term in *italics* inside a definition is itself defined in this glossary. "CV-nnn" refers to [CONVENTIONS.md](CONVENTIONS.md). Terms marked **TBR (C5)** are seed definitions that the autoflight mode logic (`specs/AF_MODE_LOGIC.md`, task C5) refines.

The mode names below (for example *Stationary*) are the names of functions in the design. The strings the crew sees on annunciations are not defined here. They are set by the annunciation requirements.

| Term | Definition | Ref. |
| --- | --- | --- |
| Active (mode) | State of a *mode* in which it is producing the references for the axes of its *mode group*. At most one mode per mode group is active at a time (D56). In requirements, "active" is used for this state; "engaged" is not used for modes. TBR (C5). | — |
| AER | Identifier of the Aeronef element in requirement IDs (`AER-…`). | METHODOLOGY 9.1 |
| Aeronef | The fictional six-degree-of-freedom flying vehicle that is the subject of the project, including its dynamics, effectors, fuel and mass properties, flight control, autoflight, flight control panel, navigation and operational data output. One of the three L1 elements, with the *TST* and the *RVS*. | — |
| Aeronef configuration | The *Aeronef* as verified: one *autoflight implementation* with one *flight-control-law design*, running on the vehicle model. There is one configuration for now, and it must pass every requirement (D42). | L0-SUC-020, D42 |
| Aeronef project | The project of interest at L0: the design of the *Aeronef*, the *TST* and the *RVS*. The subject of every L0 requirement; the Aeronef itself is a black box at L0 (D33). | L0, D33 |
| AI-assisted methods | The project's methods that use AI agents for system design, automated verification and evidence-based reverse engineering. Assessed in the *method assessment report*. | OBJECTIVES §1, L0-OBJ-210 |
| Air-relative velocity | Vehicle velocity minus the velocity of the air mass at the body origin. In version 1 the air mass moves with a uniform *wind* (D17). | CV-470 |
| Airborne | State of the *Aeronef* between the start of a run and *ground contact*. | L0-CON-310 |
| Airspeed | Magnitude of the *air-relative velocity*, in m/s. | CV-470 |
| Altitude | Vertical distance of the body origin (the CG) above the *datum plane*, positive up, in m (crew-facing: ft). Geometric, not pressure altitude. | CV-430 |
| Altitude Hold | Autoflight vertical *mode* that keeps the *altitude* at its *target*: the altitude captured from *Go to altitude* or *Vertical speed* mode, or the altitude when it was engaged (D56). | CV-430, D56 |
| Analysis | Verification method: calculation, model or comparison with an independent solution. | METHODOLOGY 9.3 |
| Annunciation | Information the Aeronef presents to the *crew* about its state, for example the *armed* and *active* modes and their *targets*. Annunciations are crew-facing; their values use crew-facing units. | CV-760 |
| Armed (mode) | State of a *mode* that the crew has selected but whose *capture* condition is not yet met. An armed mode does not produce references. It becomes *active* by *capture*. TBR (C5). | — |
| Assumption | Statement taken as true without proof, recorded in the L0 assumptions register with an owner, and confirmed, turned into a requirement or retired before L1 is baselined. | METHODOLOGY 4.4 |
| Attitude | Orientation of the *body frame* relative to the *local reference frame*, described by *Euler angles* or an attitude *quaternion*. Independent of the vehicle's motion on the Aeronef. | CV-210, CV-250, CV-550 |
| Autoflight | The Aeronef subsystem (AF) that, according to the *active modes* and their *targets*, produces the references for *flight control* and manages *mode* selection, *arming*, *capture*, transitions and *annunciation*. Inspired by airliner autopilot and flight-director concepts. Also "autoflight system". | — |
| Autoflight implementation | One implementation of the autoflight functions, replaceable without modifying the vehicle model. There is one (D24). | L0-CON-210 |
| Automated test procedure | A procedure that sets initial conditions, applies stimuli, records results and assesses the observed outcomes against the expected outcomes, without operator action. | L0-OBJ-080, L0-SUC-030 |
| Axis demand | A force along, or a moment about, one body axis that the regulation function of *flight control* asks the allocation function to produce. Six per *control frame*. | FUNCTIONAL_ANALYSIS F-AER-05, -06 |
| Axis reference | The value toward which *flight control* regulates one *degree of freedom*, produced by *autoflight*. Which quantity each reference is (velocity, position, rate, attitude) is set at L2 (C4, C5). The only data autoflight passes to flight control (D15). | FUNCTIONAL_ANALYSIS I-13; ICD-FC-AF |
| Baseline | Reviewed and approved version of an artifact, placed under configuration control and changed only by an approved change request. | METHODOLOGY 10.5 |
| Body frame | Frame B fixed to the vehicle: origin at the CG, x toward the nose, y to the right, z down through the cockpit floor. | CV-160, CV-170 |
| Body rates | Components (p, q, r) of the vehicle angular velocity along the body axes: roll rate, pitch rate and yaw rate, in rad/s. Not equal to the *Euler-angle* rates in general. | CV-280, CV-290 |
| Capture | Transition of an *armed* mode to *active* when its capture condition is met, for example *Altitude Hold* capturing the selected altitude from *Go to altitude*, or *Hover* engaging from *Go to hover*; for a mode with a capture phase, also the period during which the vehicle converges onto the *target* before holding it. TBR (C5). | — |
| Centre of gravity (CG) | Point about which the vehicle's weight acts. Fixed in the *body frame* in version 1, and the origin of the body frame. | CV-160 |
| Childless parent | Trace-check term (METHODOLOGY §10.4): a requirement with no child at the next level where one is expected. L0 requirements allocated only to the *TST* or the *RVS* are not childless parents until the plan covers those branches (D44). | L0-SUC-150, D44 |
| Climbing, descending | The vehicle is climbing when *vertical speed* > 0 and descending when vertical speed < 0. Properties of motion, not of *attitude*. | CV-570 |
| Command response | The time behaviour of an *effector output* after a change of its *effector command*, including its response time `[P-EF-010]`. | L0-CON-080; L1-AER-100, -710 |
| Configuration (run) | The items a run is started with besides its *initial condition* and *selection script*: the *vehicle parameter set*, the *flight-control-law design* and the *autoflight implementation*, each with an identifier and a version. Not to be confused with *Aeronef configuration* (D42), the one verified combination. | CONOPS §4.6; N-350 |
| Constraint | Requirement type that limits the design or the model, for example "no aerodynamic lift". | METHODOLOGY 4.4 |
| Consumption parameters | The translational `[P-FU-040]` and rotational `[P-FU-050]` parameters of the relationships that give the *fuel mass flow* from the control forces and control moments. Their form is set in MS-DYN (C2). | L0-CON-120; L1-AER-160, -170 |
| Control effectiveness | The control force and control moment, in the *body frame* and about the *centre of gravity*, that one *effector* produces per unit of its *effector command*. It carries the effector's point of application and moment arm. | L0-CON-080; CV-330 |
| Control force, control moment | A force or moment on the *Aeronef* other than gravity and aerodynamic drag. Only the *effectors* produce them. | L0-CON-060 |
| Control frame | One execution of the flight-control or autoflight functions. Its period is a parameter. | CV-830 |
| Control law | The rule by which the flight-control function turns references and vehicle state into *effector* commands. Defined at L2 (D33). | L0-CON-200 |
| Crash | *Ground contact* outside the *landing envelope*. It ends the run (D37). | L0-CON-290 |
| Crew | The person or simulated operator who selects modes and targets and reads annunciations. Never the subject of a requirement. | METHODOLOGY 8.1 |
| Crew interface | The data exchanged between the *crew* and the *Aeronef*: mode selections, *target* selections, *annunciations* and *indications*. Physical controls and *display formats* are not modelled (L0-CON-170). | L0-CON-170 |
| Crew selection | One data item of the *crew interface* by which the *crew* selects a *mode* or a *selected value*, with its *timestamp*. | L0-CON-170; CONOPS §4.3 |
| Crew station | The position of the *crew* in the *body frame*, in the cockpit toward the nose (CV-170). | L0-CON-150 |
| Crew-facing quantity | A quantity the *crew* selects or that is annunciated to the crew. It is stated in its *crew-facing unit*; every other quantity is in SI units. | L0-CON-260, L0-CON-270 |
| Crew-facing unit | Unit used for a value the crew selects or sees: ft, ft/min, kt, NM, deg (D7), lb for fuel (D9), and hours or minutes for durations (D34); the unit table is CV-740. Used only where CV-760 allows. | CV-740, CV-760 |
| Datum plane | The horizontal reference plane of the flat Aeronef world, `z_L = 0`, from which *altitude* is measured. It is also the ground: altitude zero is ground level, with no terrain (D8). | CV-110, CV-420 |
| Degree of freedom | One independent coordinate of rigid-body motion: translation along, or rotation about, one of three axes. The *Aeronef* has six. | L0-CON-010, -020, -030 |
| Demonstration | Verification method: operating the system to show a qualitative capability, without detailed measurement. | METHODOLOGY 9.3 |
| Derived requirement | Requirement that does not trace to a parent requirement but arises from a design decision. It is marked "Derived", cites its design decision (DD-nnn) and is reviewed at the parent level. | METHODOLOGY 12 |
| Design decision (DD) | Recorded choice behind one or more *derived requirements*, held in `registers/DECISIONS.md` with the alternatives considered and the rationale. | — |
| Deviation, error | Actual value minus *target* value, with angles differenced by `wrap180`. | CV-910, CV-930 |
| Direct manual flight control | A control by which the *crew* commands the effectors or the vehicle motion directly, such as a stick or yoke. Excluded: the crew acts only through the *flight control panel* (D33, L0-CON-180). | L0-CON-180 |
| Direction angle | Angle in the horizontal plane measured clockwise from true north, in [0, 2π) rad (crew-facing: [0°, 360°)). *Heading* and *track* are direction angles. | CV-520 |
| Disengagement | Transition of a *mode* out of the *active* or *armed* state, by crew action or automatically. TBR (C5). | — |
| Display format | The layout, graphics and symbology in which *crew-interface* data are shown. Not the value resolution or the rounding of a crew-interface data item, which are requirement matters (CV-780). | L0-CON-170; L1-AER-510 |
| Dry mass | *Vehicle mass* with no fuel, `[P-FU-030]`, in kg. | CV-340 |
| Effector | A fictional force or moment emitter that acts along a fixed direction in the *body frame* and produces a variable output on command, consuming fuel. "Emitter" is a synonym used in the concept documents; requirements use "effector". The set of effectors is the effector subsystem (EF). | CV-330 |
| Effector command | The value that *flight control* sends to one *effector* for a *control frame*. | CV-330 |
| Effector output | The force or moment one *effector* produces along its fixed direction at a *simulation step*. | CV-330 |
| Element | Major part of the system at L1: the *Aeronef*, the *TST* or the *RVS*. | METHODOLOGY 3 |
| Emitter | See *effector*. | — |
| Engaged (autoflight) | State of the *autoflight* system in which it provides the references to *flight control*. Used for the autoflight system as a whole, not for individual modes (see *active*). TBR (C5). | — |
| Engagement | Transition of the autoflight system to *engaged*, or of a mode to *active*. TBR (C5). | — |
| Euler angles | *Heading* (yaw angle) ψ, *pitch angle* θ and *roll angle* φ, applied in the yaw-pitch-roll (3-2-1) order from the vehicle-carried local frame to the body frame. | CV-210 to CV-230 |
| Evaluator | A project member on the *protected* side who assesses the *reconstructed model*; not a reverse-engineering agent. | L0-OBJ-170, L0-SUC-100 to -130 |
| Event record | A time-stamped record of a discrete event in the *operational data*: a *ground contact* classified as a *landing* or a *crash*, or a fuel alert. | CV-840 |
| Execution host | The computer whose CPU cores run the *simulation instances* of a *test campaign* (L0-ASM-130). | L0-CON-190 |
| Final test report | The report that records the result of each verification procedure performed against the requirements of each level, issued for the *requirements baseline*. Each element contributes its section (D28). | L0-SUC-170 |
| Flight control | The Aeronef subsystem (FC) that regulates each translational and rotational axis independently and allocates axis demands to the *effectors*. | — |
| Flight control panel | The panel the *crew* uses to select *modes* and *targets* (heading, horizontal speed, target altitude, vertical speed) and on which it reads the *annunciations* and indications. Its own L2 subsystem, FCP (D55). There is no stick or yoke. Content defined at L2 (#79). | L0-CON-170, L0-CON-180, D55 |
| Flight software | The Aeronef functions outside the *vehicle model* that run once per *control frame*: flight control, autoflight, the *flight control panel* and navigation. The *flight-control-law design* and the *autoflight implementation* are replaceable through the *configuration*. | FUNCTIONAL_ANALYSIS §5 |
| Flight-control-law design | One design of the *control laws* of the flight-control function, replaceable without modifying the vehicle model. There is one for now (D42). | L0-CON-200 |
| Force effector | Synonym of *effector*, used in the L0 requirements. | L0-CON-060 to -080, -300 |
| Fuel exhaustion | State in which the remaining fuel mass is zero. Nominal behaviour, not a failure. | — |
| Fuel mass flow | Mass of fuel consumed per unit of time, in kg/s, computed from the control forces and control moments through the *consumption parameters*. | CV-720; L1-AER-160 |
| Fuel state | The *remaining fuel mass* and whether it is below the low-fuel threshold `[P-FU-020]` or at *fuel exhaustion*. | CONOPS §4.5 |
| Gate | Review point between plan phases (G0 to G4) at which the project owner approves a baseline. | Plan §6 |
| Go to altitude | Autoflight vertical *mode* that climbs or descends toward the selected altitude at the *standard vertical speed*, or at the selected vertical speed if the crew sets one, and arms *Altitude Hold* (D56). | Plan D56 |
| Go to hover | Autoflight *mode* that governs both axes: from whatever the vehicle is flying, it brings the vehicle to zero velocity at the *hover height* and arms *Hover* (D56). | Plan D56 |
| Ground contact | Contact of the vehicle with the *datum plane*. Modelled as an ideal landing: within the *landing envelope* it is a *landing*, outside it a *crash*. There is no landing gear, bounce or friction model (D37). | L0-CON-290 |
| Gust | A change in time of the *wind* added to the steady wind, as a gust or a burst. Horizontal; its speed adds to the steady wind speed (D51). It builds up over at least `[P-SYS-570]`: there is no instantaneous step (D62). | L0-ASM-050, P-SYS-560, D62 |
| Heading | The direction in which the nose points: the *direction angle* of the horizontal projection of the body x axis; equal to the Euler yaw angle. Independent of *track* on the Aeronef. In rad (crew-facing: deg). | CV-530, CV-550 |
| Heading (mode) | Autoflight horizontal *mode* that turns the vehicle to the selected *heading* and moves it along that heading at the selected *horizontal speed*. With no horizontal speed, a heading change turns the vehicle in place about its vertical axis (D56). | Plan D56 |
| Heading rate | Rate of change of *heading*, dψ/dt, in rad/s. Not a *body rate* (CV-290). | CV-290 |
| Height | Vertical distance of the body origin above a stated reference other than the datum plane, positive up, in m. Always used with its reference. | CV-440 |
| Horizontal distance | Distance between the projections of two points on the datum plane, in m (crew-facing: NM). | CV-450 |
| Horizontal speed | Magnitude of the horizontal component of the vehicle velocity relative to the ground, in m/s (crew-facing: kt). Independent of attitude. Its selected value is flown by the *Heading* mode (D56). | CV-480 |
| Hover | Autoflight *mode* that governs both axes: it engages from *Go to hover* once the vehicle is stationary at the *hover height*, then holds that height and the position over the ground, compensating for *wind* (D56). | Plan D56 |
| Hover height | The height above the ground that *Go to hover* brings the vehicle to and *Hover* holds; a project constant `[P-AF-210]`. On the flat ground (D8) it is an altitude. | Plan D56 |
| ICD | Interface control document: data, units, rates and frames exchanged between two elements or subsystems. | METHODOLOGY 11.1 |
| Indication | A vehicle quantity shown to the *crew* in its *crew-facing unit*: *altitude*, *vertical speed*, *horizontal speed*, *heading*, *track* and *remaining fuel mass*. Distinct from an *annunciation*, which shows the autoflight state or an alert. | CONOPS §4.3; CV-760 |
| Initial condition | The state a run starts from: position, velocity, attitude, *body rates*, fuel mass, *mode state* and *targets*. Set by the TST (L1-AER-660). | CONOPS §4.6; N-310 |
| Inspection | Verification method: examination of an artifact, code or data against the requirement, without running it. | METHODOLOGY 9.3 |
| Landing | *Ground contact* within the *landing envelope*: a successful outcome, not a crash (D37). | L0-CON-290 |
| Landing envelope | The limits on the *vertical speed* magnitude (`[P-SYS-500]`) and the *horizontal speed* (`[P-SYS-510]`) at the ground-contact sample within which *ground contact* is a *landing*. There is no acceleration limit (D53). | L0-CON-290, D53 |
| Level attitude | *Attitude* with zero *pitch angle* and zero *roll angle*, at any *heading*. | CV-270 |
| Level file | The file `requirements/L<n>.md` that holds the requirements of one level, assembled from draft sections (plan §3, D2). | Plan §3 |
| Level flight | Motion with zero *vertical speed*. Unrelated to *level attitude*. | CV-570 |
| Local reference frame | Frame L fixed to the datum plane: x north, y east, z down (NED, D21), origin a fixed point on the datum plane. Treated as inertial. | CV-120 to CV-140 |
| Low-fuel alert | The *annunciation* given when the *remaining fuel mass* falls below the fraction `[P-FU-020]` of `[P-FU-010]`. Its label is set at L2. | CONOPS §4.5 |
| Major review finding | A review finding classed Major in the METHODOLOGY §13.4 record. | L0-SUC-010 |
| Manual trace register | The *protected* register tracing each operational manual section to the requirements it describes; the answer key for scoring the reconstruction (METHODOLOGY §11.2). | L0-SUC-130 |
| Mass properties | The *vehicle mass*, the *centre-of-gravity* position and the inertia tensor at a given fuel state. The body axes are principal axes, so the products of inertia are zero (D61). | CV-340, CV-350, D61 |
| Maximum vehicle mass | *Dry mass* plus the usable fuel mass at full capacity: `[P-FU-030]` + `[P-FU-010]`. | FUNCTIONAL_ANALYSIS §7 |
| Method assessment report | The report that assesses the AI-assisted methods used for system design, automated verification and evidence-based reverse engineering. Each element contributes its section and the owner audits it (D28). | L0-OBJ-210 |
| Mode | One autoflight function that, while *active*, sets the references for a defined set of axes from a *target*, for example *Altitude Hold* or *Heading* mode. The mode catalogue is decision D56. | Plan D56 |
| Mode catalogue | The list of autoflight *modes* fixed by plan decision D56, which replaced D3. Also called the autoflight mode catalogue. | Plan D56, L0-OBJ-030 |
| Mode group | Set of *modes* that act on the same axes and of which at most one is *active* at a time. Two groups, independent of each other: horizontal (*Stationary*, *Heading*) and vertical (*Altitude Hold*, *Go to altitude*, *Vertical speed* mode). *Go to hover* and *Hover* govern both groups while active (D56). | Plan D56 |
| Mode state | The *armed* and *active* modes of each *mode group*, and whether *autoflight* is *engaged*. A mode that arms, becomes active, leaves the armed state or is disengaged changes the mode state. TBR (C5). | D16, D56 |
| Model specification | The specification of the Aeronef dynamics model (MS-DYN, task C1): equations of motion, external effects, *effector*, fuel and mass models. | L0-OBJ-010, L0-CON-010 to -140 |
| Navigation | The Aeronef subsystem (NAV) that provides *position*, *altitude*, *heading*, *track*, *horizontal speed* and *vertical speed* to autoflight and to the *flight control panel*. | — |
| Operating volume | The region of nominal operation: *altitudes* from the minimum operating altitude `[P-SYS-210]` to the maximum operating altitude `[P-SYS-200]`, within a *horizontal distance* `[P-SYS-220]` of the local reference frame origin. | CONOPS §4.2 |
| Operational data | Signals the Aeronef outputs, at each *output sample*, describing its externally observable activity: *crew selections*, *targets*, *armed* and *active* modes, *annunciations*, control activity and *vehicle states*. Whether each signal is *releasable* or *protected* is decided with the RVS (#69, D44). | CV-830, CV-840 |
| Operational manuals | The Vehicle Operating Manual, the normal procedures and the quick reference checklists of METHODOLOGY §11.2, written for an operator after the *requirements baseline*. | L0-OBJ-150 |
| Orphan requirement | Trace-check term (METHODOLOGY §10.4): a requirement below L0 with no parent and no Derived flag. | L0-SUC-150 |
| Output limits | The smallest and largest *effector output* of one *effector*, including its maximum force magnitude (L0-CON-300). | L0-CON-080, L0-CON-300 |
| Output sample | One record of *operational data*. Its period is a parameter. | CV-830 |
| Parallel efficiency | Single-instance campaign duration divided by (parallel campaign duration × number of parallel instances). Dimensionless. | L0-SUC-060 (Draft) |
| Parameter | A named value used by requirements, the model or the design, held in `parameters/PARAMETERS.yaml` with an ID `P-<SUB>-<NNN>`, a unit, a value or TBD, a status and a source. Requirements cite parameters by ID instead of writing numbers. | CV-790 |
| Parameter database | The file `parameters/PARAMETERS.yaml`, which holds each *parameter* with its ID, unit, value or TBD, status and source. | CV-790; plan §3 |
| Pitch angle | Euler angle θ: rotation about the body y axis, positive nose up, in [−π/2, +π/2] rad. | CV-220, CV-230 |
| Position (vehicle position) | Position of the body origin (the CG) in the local reference frame, in m. *Horizontal position* is its north and east components. | CV-410 |
| Project owner | The person who decides open questions and approves each gate (Martin). | Plan §5 |
| Protected | Classification of information that must not reach the *RVS*: requirements, design artifacts (including this glossary and the conventions), source code, ground-truth test expectations, assessment answers and *operational data* signals classified protected. | REVERSE_ENGINEERING §2, §7 |
| Protected design baseline | The baselined requirements and design against which the *reconstructed model* is assessed. It is *protected*. | L0-OBJ-170 |
| Protected design material | The *protected* items withheld from the *RVS*, chosen by the owner when the reverse-engineering work starts (deletion of L0-CON-220 to -240, #69). | L0-CON-250, L0-SUC-140 (Draft) |
| Quaternion (attitude) | Unit quaternion (q0, q1, q2, q3), scalar first, that represents the attitude without the Euler-angle singularity. | CV-250 |
| Reconstructed model | The *RVS*'s inferred description of the Aeronef's functions, operating *modes*, mode transitions and control logic, each element citing the evidence it rests on. | L0-OBJ-160, -170, L0-SUC-100 to -130 |
| Reference mission | Scenario SC-110 of the ConOps: a fixed profile flown under autoflight from full fuel to *fuel exhaustion*, ending at *ground contact*. | CONOPS SC-110 |
| Reference position | The horizontal position over the ground that autoflight holds while *Stationary* or *Hover* is active. Whether it is the position at engagement or where the vehicle stops is set at L2 (#78). | D56, D60 |
| Relative track | wrap180(*track* − *heading*): the direction of horizontal motion relative to the nose. | CV-550 |
| Releasable | Classification of information that may be given to the *RVS*: operational manuals and procedures, the executable simulation as released, and *operational data* signals classified releasable. | REVERSE_ENGINEERING §3 |
| Released evidence | The material the owner gives to the *RVS* (*releasable* items). | L0-OBJ-160 |
| Remaining fuel mass | The usable fuel mass on board at a given time, in kg (crew-facing: lb). | CV-340 |
| Requirement | A single "shall" statement with its attributes (METHODOLOGY §9.2), stored as one record per the requirement template. | METHODOLOGY 8, 9 |
| Requirements baseline | The complete baselined Aeronef requirement set, tag `AER-REQ-baseline-1`, approved at Gate G4. | Plan §6 G4 |
| Roll angle | Euler angle φ: rotation about the body x axis, positive right side down, in (−π, +π] rad. "Bank angle" is not used. | CV-220, CV-230 |
| RVS | Reverse-Engineering Effort: the L1 element that reconstructs the Aeronef's functions and logic from *releasable* material only. | OBJECTIVES §4 |
| Selected value | A value the crew chooses for a *target*, in a crew-facing unit (for example a selected altitude in ft). It becomes the SI *target* by exact conversion. | CV-770 |
| Selection script | The *crew selections* of a run, each with the *simulation time* at which it applies; empty for an interactive run. | CONOPS §4.6 |
| Sensed acceleration | The acceleration the *crew* feels: the sum of the non-gravitational forces on the vehicle divided by its current mass (specific force), gravity included in the load felt. 1 g in a hover, 0 g in free fall. Limited to `[P-SYS-120]`, 3 g for now (D38). | L0-CON-310 |
| Shall, will, should | "Shall" states a verified requirement, "will" a fact or declaration of purpose, "should" a goal (not verified). | METHODOLOGY 8.2 |
| Simulation core | The part of the *TST* that executes the vehicle model and the Aeronef software, without any graphical display. | L0-CON-190 |
| Simulation instance | One isolated, independently started copy of the simulation, running one *test run* at a time. | L0-OBJ-090 (Draft) |
| Simulation step | The fixed time increment `Δt` by which the vehicle model advances; step k is at simulation time `k·Δt`. | CV-820 |
| Simulation time | Independent time variable of the vehicle model, in s, zero at the instant the initial conditions apply; independent of wall-clock time. | CV-810 |
| Slant range | Three-dimensional distance between two points, in m. | CV-450 |
| Standard atmosphere | A standard model of air density as a function of *altitude* only (D20, L0-ASM-060). MS-DYN names the model (C1). | D20 |
| Standard vertical speed | The vertical speed magnitude `[P-AF-220]` that *Go to altitude* uses until the crew selects another. | Plan D56 |
| Stationary | Autoflight horizontal *mode* that stops the horizontal motion and holds the horizontal position over the ground, compensating for *wind*; the vertical mode is independent of it (D56). | Plan D56 |
| Subsystem | Part of an element at L2. Aeronef subsystems: DYN (dynamics), FU (fuel and mass properties), EF (effectors), FC (flight control), AF (autoflight), FCP (flight control panel, D55), NAV (navigation), TM (operational data output). | Plan §3, D55 |
| Target | The SI reference value toward which a *mode* guides a quantity: either converted from a *selected value* or set by the autoflight system (for example the position held by *Stationary*). | CV-770 |
| TBD | To Be Determined: a value or item not yet known, recorded in the TBD/TBR register with an owner and a closure date. | METHODOLOGY 9.2 |
| TBR | To Be Resolved (also read "to be reviewed"): a value or statement that is stated provisionally and must be confirmed, recorded in the TBD/TBR register with an owner and a closure date. | METHODOLOGY 9.2 |
| Test | Verification method: operating the system under controlled conditions and measuring the result against the success criteria. | METHODOLOGY 9.3 |
| Test campaign | A set of *test runs* launched together as one batch. | L0-OBJ-130, L0-SUC-050 |
| Test category | One of: functional and logic tests, mode-transition tests, performance tests, statistical campaigns (OBJECTIVES §3). | L0-OBJ-120, L0-SUC-070 |
| Test run | One execution of one *automated test procedure*, or one interactive session, in one *simulation instance*. | L0-OBJ-120, L0-SUC-040 |
| Timestamp | The step index k and the simulation time `t_k` attached to an output sample, selection or event. The step index is authoritative. | CV-840 |
| Total speed | Magnitude of the vehicle velocity relative to the ground, in m/s. "Speed" alone is not used. | CV-460 |
| Track | The direction of horizontal motion: the *direction angle* of the horizontal velocity, ground-referenced. Independent of *heading* on the Aeronef. Undefined at zero horizontal speed. In rad (crew-facing: deg). | CV-540, CV-550 |
| TST | Simulation and Testing Platform: the L1 element that executes the Aeronef simulation, runs interactive and automated tests in parallel and reports results. | OBJECTIVES §3 |
| Validity range | The states in which a direction quantity is defined and used, bounded by the CV-580 thresholds `[P-NAV-010]` and `[P-NAV-030]`. | CV-580 |
| Vehicle acceleration | Time derivative of the vehicle velocity in the *local reference frame*, in m/s². Not the *sensed acceleration*, which excludes gravity. | CV-460 |
| Vehicle mass | *Dry mass* plus *remaining fuel mass*, in kg. | CV-340 |
| Vehicle model | The part of the Aeronef that reproduces its physics: the DYN, FU and EF subsystems and MS-DYN. It is unchanged when the *flight-control-law design* or the *autoflight implementation* is replaced. | L0-CON-200, -210; FUNCTIONAL_ANALYSIS §5 |
| Vehicle model file | A source or data file of the *vehicle model*; its checksum shows that a replacement did not modify the model. | L0-CON-200 |
| Vehicle parameter set | The values of the *vehicle model* parameters used in a run, identified by a version. | N-350 |
| Vehicle state | Position, velocity, attitude (quaternion, with *Euler angles* derived), *body rates* and *vehicle acceleration* of the vehicle at a *simulation step*. | CV-250, CV-410, CV-460 |
| Vehicle-carried local frame | Frame V with origin at the body origin and axes parallel to the local reference frame (north, east, down). Reference for the Euler angles. | CV-150 |
| Verification matrix | The table of each requirement with its verification method, procedure and last result (VCRM, `tools/vcrm.py`). | L0-SUC-020, -030 |
| Vertical speed | Rate of change of *altitude*, positive when climbing, in m/s (crew-facing: ft/min). Independent of attitude. | CV-490 |
| Vertical speed (mode) | Autoflight vertical *mode* that climbs or descends at the selected constant *vertical speed* toward the selected altitude, and arms *Altitude Hold* so that it levels off there (D56). | Plan D56 |
| Wind | Motion of the air mass relative to the *local reference frame*. In version 1 it is uniform (the same everywhere at a given time), horizontal, and set by the test environment for each run: a steady wind plus *gusts* (D17, D51). | L0-ASM-050, CV-470 |
| Wind envelope | The winds for which the Aeronef performance requirements apply, and the only winds the TST applies: a horizontal steady wind of speed at most `[P-SYS-430]` plus *gusts* of speed at most `[P-SYS-560]`, each building up over at least `[P-SYS-570]`. | L0-ASM-050, D51, D62 |
| Wind speed | Magnitude of the *wind* velocity, in m/s. | CV-470 |
| Withheld assessment scenario | A scenario defined by the *evaluators* and not shown to the *RVS*, used to test whether the *reconstructed model* predicts unseen behaviour. | L0-SUC-120 |
