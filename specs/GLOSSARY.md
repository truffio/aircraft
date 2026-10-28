# Aeronef — Glossary

**Status:** Fixed at Gate G0 (D43), 2026-10-27. Extended at later gates from agents' `glossary_proposals.md`; changes to a fixed definition go through a change request.
**Date:** 2026-10-27
**Owner:** Martin (maintained by the orchestrator)
**Classification:** Protected design material. Not for release to the Reverse-Engineering Effort (REE).

Requirements use only the terms defined here (METHODOLOGY §8.4 rule 12), with the meaning given here. A term in *italics* inside a definition is itself defined in this glossary. "CV-nnn" refers to [CONVENTIONS.md](CONVENTIONS.md). Terms marked **TBR (C5)** are seed definitions that the autoflight mode logic (`specs/AF_MODE_LOGIC.md`, task C5) refines.

The mode names below (for example *Position Hold*) are the names of functions in the design. The strings the crew sees on annunciations are not defined here. They are set by the annunciation requirements.

| Term | Definition | Ref. |
| --- | --- | --- |
| Active (mode) | State of a *mode* in which it is producing the references for the axes of its *mode group*. At most one mode per mode group is active at a time (TBR, #6, deferred to L2). In requirements, "active" is used for this state; "engaged" is not used for modes. TBR (C5). | — |
| AER | Identifier of the Aeronef element in requirement IDs (`AER-…`). | METHODOLOGY 9.1 |
| Aeronef | The fictional six-degree-of-freedom flying vehicle that is the subject of the project, including its dynamics, effectors, fuel and mass properties, flight control, autoflight, navigation and operational data output. One of the three L1 elements, with the *STP* and the *REE*. | — |
| Aeronef configuration | The *Aeronef* as verified: one *autoflight implementation* with one *flight-control-law design*, running on the vehicle model. There is one configuration for now, and it must pass every requirement (D42). | L0-SUC-020, D42 |
| Aeronef project | The project of interest at L0: the design of the *Aeronef*, the *STP* and the *REE*. The subject of every L0 requirement; the Aeronef itself is a black box at L0 (D33). | L0, D33 |
| Air-relative velocity | Vehicle velocity minus the velocity of the air mass at the body origin. In version 1 the air mass moves with a uniform *wind* (D17). | CV-470 |
| Airborne | State of the *Aeronef* between the start of a run and *ground contact*. | L0-CON-310 |
| Airspeed | Magnitude of the *air-relative velocity*, in m/s. | CV-470 |
| Altitude | Vertical distance of the body origin (the CG) above the *datum plane*, positive up, in m (crew-facing: ft). Geometric, not pressure altitude. | CV-430 |
| Altitude capture | Autoflight function that, from an *armed* state during a climb or descent, takes over the vertical axis when its capture condition is met and brings the vehicle onto the *target* altitude, then hands over to *Altitude Hold*. TBR (C5). | — |
| Altitude Hold | Autoflight *mode* of the vertical *mode group* that keeps the *altitude* at its *target*. | CV-430 |
| Analysis | Verification method: calculation, model or comparison with an independent solution. | METHODOLOGY 9.3 |
| Annunciation | Information the Aeronef presents to the *crew* about its state, for example the *armed* and *active* modes and their *targets*. Annunciations are crew-facing; their values use crew-facing units. | CV-760 |
| Armed (mode) | State of a *mode* that the crew has selected but whose *capture* condition is not yet met. An armed mode does not produce references. It becomes *active* by *capture*. TBR (C5). | — |
| Assumption | Statement taken as true without proof, recorded in the L0 assumptions register with an owner, and confirmed, turned into a requirement or retired before L1 is baselined. | METHODOLOGY 4.4 |
| Attitude | Orientation of the *body frame* relative to the *local reference frame*, described by *Euler angles* or an attitude *quaternion*. Independent of the vehicle's motion on the Aeronef. | CV-210, CV-250, CV-550 |
| Autoflight | The Aeronef subsystem (AF) that, according to the *active modes* and their *targets*, produces the references for *flight control* and manages *mode* selection, *arming*, *capture*, transitions and *annunciation*. Inspired by airliner autopilot and flight-director concepts. Also "autoflight system". | — |
| Autoflight implementation | One implementation of the autoflight functions, replaceable without modifying the vehicle model. There is one (D24). | L0-CON-210 |
| Automated test procedure | A procedure that sets initial conditions, applies stimuli, records results and assesses the observed outcomes against the expected outcomes, without operator action. | L0-OBJ-080, L0-SUC-030 |
| Baseline | Reviewed and approved version of an artifact, placed under configuration control and changed only by an approved change request. | METHODOLOGY 10.5 |
| Body frame | Frame B fixed to the vehicle: origin at the CG, x toward the nose, y to the right, z down through the cockpit floor. | CV-160, CV-170 |
| Body rates | Components (p, q, r) of the vehicle angular velocity along the body axes: roll rate, pitch rate and yaw rate, in rad/s. Not equal to the *Euler-angle* rates in general. | CV-280, CV-290 |
| Capture | Transition of an *armed* mode to *active* when its capture condition is met, and, for modes with a capture phase (for example *altitude capture*, VOR radial capture), the period during which the vehicle converges from its previous path onto the *target* before holding it. TBR (C5). | — |
| Centre of gravity (CG) | Point about which the vehicle's weight acts. Fixed in the *body frame* in version 1, and the origin of the body frame. | CV-160 |
| Childless parent | Trace-check term (METHODOLOGY §10.4): a requirement with no child at the next level where one is expected. L0 requirements allocated only to the *STP* or the *REE* are not childless parents until the plan covers those branches (D44). | L0-SUC-150, D44 |
| Climbing, descending | The vehicle is climbing when *vertical speed* > 0 and descending when vertical speed < 0. Properties of motion, not of *attitude*. | CV-570 |
| Constraint | Requirement type that limits the design or the model, for example "no aerodynamic lift". | METHODOLOGY 4.4 |
| Control force, control moment | A force or moment on the *Aeronef* other than gravity and aerodynamic drag. Only the *effectors* produce them. | L0-CON-060 |
| Control frame | One execution of the flight-control or autoflight functions. Its period is a parameter. | CV-830 |
| Control law | The rule by which the flight-control function turns references and vehicle state into *effector* commands. Defined at L2 (D33). | L0-CON-200 |
| Course deviation | Signed angle between the *selected course* line and the line from the *VOR station* to the vehicle, positive when the vehicle is to the right of the course looking along the course direction, in rad (crew-facing: deg). | CV-650 |
| Crash | *Ground contact* outside the *landing envelope*. It ends the run (D37). | L0-CON-290 |
| Crew | The person or simulated operator who selects modes and targets and reads annunciations. Never the subject of a requirement. | METHODOLOGY 8.1 |
| Crew interface | The data exchanged between the *crew* and the *Aeronef*: mode selections, *target* selections and *annunciations*. Physical controls and display formats are not modelled (L0-CON-170). | L0-CON-170 |
| Crew station | The position of the *crew* in the *body frame*, in the cockpit toward the nose (CV-170). | L0-CON-150 |
| Crew-facing quantity | A quantity the *crew* selects or that is annunciated to the crew. It is stated in its *crew-facing unit*; every other quantity is in SI units. | L0-CON-260, L0-CON-270 |
| Crew-facing unit | Unit used for a value the crew selects or sees: ft, ft/min, kt, NM, deg (D7), lb for fuel (D9), and hours or minutes for durations (D34); the unit table is CV-740. Used only where CV-760 allows. | CV-740, CV-760 |
| Cross-track deviation | Signed horizontal distance from the vehicle to the *selected course* line through the *VOR station*, positive to the right of the course, in m. | CV-660 |
| Datum plane | The horizontal reference plane of the flat Aeronef world, `z_L = 0`, from which *altitude* is measured. It is also the ground: altitude zero is ground level, with no terrain (D8). | CV-110, CV-420 |
| Degree of freedom | One independent coordinate of rigid-body motion: translation along, or rotation about, one of three axes. The *Aeronef* has six. | L0-CON-010, -020, -030 |
| Demonstration | Verification method: operating the system to show a qualitative capability, without detailed measurement. | METHODOLOGY 9.3 |
| Derived requirement | Requirement that does not trace to a parent requirement but arises from a design decision. It is marked "Derived", cites its design decision (DD-nnn) and is reviewed at the parent level. | METHODOLOGY 12 |
| Design decision (DD) | Recorded choice behind one or more *derived requirements*, held in `registers/DECISIONS.md` with the alternatives considered and the rationale. | — |
| Deviation, error | Actual value minus *target* value, with angles differenced by `wrap180`. | CV-910, CV-930 |
| Direct manual flight control | A control by which the *crew* commands the effectors or the vehicle motion directly, such as a stick or yoke. Excluded: the crew acts only through the *flight control panel* (D33, L0-CON-180). | L0-CON-180 |
| Direction angle | Angle in the horizontal plane measured clockwise from true north, in [0, 2π) rad (crew-facing: [0°, 360°)). *Heading*, *track*, *radial* and *selected course* are direction angles. | CV-520 |
| Disengagement | Transition of a *mode* out of the *active* or *armed* state, by crew action or automatically. TBR (C5). | — |
| Effector | A fictional force or moment emitter that acts along a fixed direction in the *body frame* and produces a variable output on command, consuming fuel. "Emitter" is a synonym used in the concept documents; requirements use "effector". The set of effectors is the effector subsystem (EF). | CV-330 |
| Element | Major part of the system at L1: the *Aeronef*, the *STP* or the *REE*. | METHODOLOGY 3 |
| Emitter | See *effector*. | — |
| Engaged (autoflight) | State of the *autoflight* system in which it provides the references to *flight control*. Used for the autoflight system as a whole, not for individual modes (see *active*). TBR (C5). | — |
| Engagement | Transition of the autoflight system to *engaged*, or of a mode to *active*. TBR (C5). | — |
| Euler angles | *Heading* (yaw angle) ψ, *pitch angle* θ and *roll angle* φ, applied in the yaw-pitch-roll (3-2-1) order from the vehicle-carried local frame to the body frame. | CV-210 to CV-230 |
| Evaluator | A project member on the *protected* side who assesses the *reconstructed model*; not a reverse-engineering agent. | L0-OBJ-170, L0-SUC-100 to -130 |
| Execution host | The computer whose CPU cores run the *simulation instances* of a *test campaign* (L0-ASM-130). | L0-CON-190 |
| Flight control | The Aeronef subsystem (FC) that regulates each translational and rotational axis independently and allocates axis demands to the *effectors*. | — |
| Flight control panel | The panel the *crew* uses to select *modes* and *targets* and to control the *autoflight* system. The crew's manual inputs go through it; there is no stick or yoke. Defined at lower levels (#79). | L0-CON-170, L0-CON-180 |
| Flight path angle | Angle between the vehicle velocity and the horizontal plane, positive when climbing, in rad (crew-facing: deg). Independent of the *pitch angle* on the Aeronef. | CV-560 |
| Flight-control-law design | One design of the *control laws* of the flight-control function, replaceable without modifying the vehicle model. There is one for now (D42). | L0-CON-200 |
| Force effector | Synonym of *effector*, used in the L0 requirements. | L0-CON-060 to -080, -300 |
| Fuel exhaustion | State in which the remaining fuel mass is zero. Nominal behaviour, not a failure. | — |
| Gate | Review point between plan phases (G0 to G4) at which the project owner approves a baseline. | Plan §6 |
| Ground contact | Contact of the vehicle with the *datum plane*. Modelled as an ideal landing: within the *landing envelope* it is a *landing*, outside it a *crash*. There is no landing gear, bounce or friction model (D37). | L0-CON-290 |
| Heading | The direction in which the nose points: the *direction angle* of the horizontal projection of the body x axis; equal to the Euler yaw angle. Independent of *track* on the Aeronef. In rad (crew-facing: deg). | CV-530, CV-550 |
| Heading Hold | Autoflight *mode* that keeps the *heading* at its *target*. It constrains where the nose points, not the direction of motion. | CV-530 |
| Height | Vertical distance of the body origin above a stated reference other than the datum plane, positive up, in m. Always used with its reference. | CV-440 |
| Horizontal distance | Distance between the projections of two points on the datum plane, in m (crew-facing: NM). | CV-450 |
| Horizontal speed | Magnitude of the horizontal component of the vehicle velocity relative to the ground, in m/s (crew-facing: kt). Independent of attitude. Also the name of the speed *mode* that keeps horizontal speed at its *target*. | CV-480 |
| Hover at altitude | Autoflight vertical *mode* (D11). When it engages, the vehicle descends from its current *altitude* to the hover altitude set on the *flight control panel*, then holds position as in *Position Hold*. The reference position and the deceleration are TBR (#78). | Plan D11 |
| ICD | Interface control document: data, units, rates and frames exchanged between two elements or subsystems. | METHODOLOGY 11.1 |
| Inspection | Verification method: examination of an artifact, code or data against the requirement, without running it. | METHODOLOGY 9.3 |
| Landing | *Ground contact* within the *landing envelope*: a successful outcome, not a crash (D37). | L0-CON-290 |
| Landing envelope | The limits on velocity and acceleration at *ground contact* within which contact is a *landing*. Parameters, set at a lower level. | L0-CON-290 |
| Level attitude | *Attitude* with zero *pitch angle* and zero *roll angle*, at any *heading*. | CV-270 |
| Level flight | Motion with zero *vertical speed*. Unrelated to *level attitude*. | CV-570 |
| Local reference frame | Frame L fixed to the datum plane: x north, y east, z down (NED, D21), origin a fixed point on the datum plane. Treated as inertial. | CV-120 to CV-140 |
| Major review finding | A review finding classed Major in the METHODOLOGY §13.4 record. | L0-SUC-010 |
| Manual trace register | The *protected* register tracing each operational manual section to the requirements it describes; the answer key for scoring the reconstruction (METHODOLOGY §11.2). | L0-SUC-130 |
| Method assessment report | The report that assesses the AI-assisted methods used for system design, automated verification and evidence-based reverse engineering. Each element contributes its section and the owner audits it (D28). | L0-OBJ-210 |
| Mode | One autoflight function that, while *active*, sets the references for a defined set of axes from a *target*, for example *Altitude Hold* or *Track Hold*. The mode catalogue is decision D3. | Plan D3 |
| Mode catalogue | The baselined list of autoflight *modes*, initially plan decision D3. Also called the autoflight mode catalogue. | Plan D3, L0-OBJ-030 |
| Mode group | Set of *modes* that act on the same axes and of which at most one is *active* at a time. Groups: vertical, lateral and speed. *Position Hold* is a lateral mode and *Hover at altitude* a vertical mode (D11). Which modes can be combined is designed at L2 (#6, D13). | — |
| Model specification | The specification of the Aeronef dynamics model (MS-DYN, task C1): equations of motion, external effects, *effector*, fuel and mass models. | L0-OBJ-010, L0-CON-010 to -140 |
| Navigation | The Aeronef subsystem (NAV) that provides *position*, *altitude*, *heading*, *track*, *horizontal speed*, *vertical speed*, *flight path angle* and the simulated VOR quantities to autoflight. | — |
| Operational data | Signals the Aeronef outputs, at each output sample, describing its externally observable activity: crew selections, *targets*, *armed* and *active* modes, *annunciations*, control activity and vehicle states. Each signal is classified *releasable* or *protected*. | CV-830, CV-840 |
| Orphan requirement | Trace-check term (METHODOLOGY §10.4): a requirement below L0 with no parent and no Derived flag. | L0-SUC-150 |
| Output sample | One record of *operational data*. Its period is a parameter. | CV-830 |
| Parallel efficiency | Single-instance campaign duration divided by (parallel campaign duration × number of parallel instances). Dimensionless. | L0-SUC-060 (Draft) |
| Parameter | A named value used by requirements, the model or the design, held in `parameters/PARAMETERS.yaml` with an ID `P-<SUB>-<NNN>`, a unit, a value or TBD, a status and a source. Requirements cite parameters by ID instead of writing numbers. | CV-790 |
| Pitch angle | Euler angle θ: rotation about the body y axis, positive nose up, in [−π/2, +π/2] rad. | CV-220, CV-230 |
| Position (vehicle position) | Position of the body origin (the CG) in the local reference frame, in m. *Horizontal position* is its north and east components. | CV-410 |
| Position Hold | Autoflight lateral *mode* (D11) in which the vehicle stops moving on all axes (zero velocity, zero acceleration) and holds its position at any *altitude*, compensating for *wind*. Whether the reference position is the position at engagement or where the vehicle stops is TBR (#78). | Plan D11 |
| Project owner | The person who decides open questions and approves each gate (Martin). | Plan §5 |
| Protected | Classification of information that must not reach the *REE*: requirements, design artifacts (including this glossary and the conventions), source code, ground-truth test expectations, assessment answers and *operational data* signals classified protected. | REVERSE_ENGINEERING §2, §7 |
| Protected design baseline | The baselined requirements and design against which the *reconstructed model* is assessed. It is *protected*. | L0-OBJ-170 |
| Protected design material | The *protected* items withheld from the *REE*, chosen by the owner when the reverse-engineering work starts (deletion of L0-CON-220 to -240, #69). | L0-CON-250, L0-SUC-140 (Draft) |
| Quaternion (attitude) | Unit quaternion (q0, q1, q2, q3), scalar first, that represents the attitude without the Euler-angle singularity. | CV-250 |
| Radial | The *direction angle* of the horizontal line from a *VOR station* to the vehicle (the bearing from the station); also the half-line of positions with that bearing. Referenced to true north (D12). | CV-620 |
| Reception range | Distance from a *VOR station* within which its signal is received. A parameter. Ideal VOR (D12). | CV-670 |
| Reconstructed model | The *REE*'s inferred description of the Aeronef's functions, operating *modes*, mode transitions and control logic, each element citing the evidence it rests on. | L0-OBJ-160, -170, L0-SUC-100 to -130 |
| REE | Reverse-Engineering Effort: the L1 element that reconstructs the Aeronef's functions and logic from *releasable* material only. | OBJECTIVES §4 |
| Relative track | wrap180(*track* − *heading*): the direction of horizontal motion relative to the nose. | CV-550 |
| Releasable | Classification of information that may be given to the *REE*: operational manuals and procedures, the executable simulation as released, and *operational data* signals classified releasable. | REVERSE_ENGINEERING §3 |
| Released evidence | The material the owner gives to the *REE* (*releasable* items). | L0-OBJ-160 |
| Requirement | A single "shall" statement with its attributes (METHODOLOGY §9.2), stored as one record per the requirement template. | METHODOLOGY 8, 9 |
| Roll angle | Euler angle φ: rotation about the body x axis, positive right side down, in (−π, +π] rad. "Bank angle" is not used. | CV-220, CV-230 |
| Selected course | The *direction angle* of the path along a radial line through a *VOR station* that the vehicle is to follow, flown outbound on radial C or inbound on its reciprocal. The crew selects a course and flies it TO or FROM the station (D14). | CV-630 |
| Selected value | A value the crew chooses for a *target*, in a crew-facing unit (for example a selected altitude in ft). It becomes the SI *target* by exact conversion. | CV-770 |
| Sensed acceleration | The acceleration the *crew* feels: the sum of the non-gravitational forces on the vehicle divided by its current mass (specific force), gravity included in the load felt. 1 g in a hover, 0 g in free fall. Limited to `[P-SYS-120]`, 3 g for now (D38). | L0-CON-310 |
| Shall, will, should | "Shall" states a verified requirement, "will" a fact or declaration of purpose, "should" a goal (not verified). | METHODOLOGY 8.2 |
| Simulation core | The part of the *STP* that executes the vehicle model and the Aeronef software, without any graphical display. | L0-CON-190 |
| Simulation instance | One isolated, independently started copy of the simulation, running one *test run* at a time. | L0-OBJ-090 (Draft) |
| Simulation step | The fixed time increment `Δt` by which the vehicle model advances; step k is at simulation time `k·Δt`. | CV-820 |
| Simulation time | Independent time variable of the vehicle model, in s, zero at the instant the initial conditions apply; independent of wall-clock time. | CV-810 |
| Slant range | Three-dimensional distance between two points, in m. | CV-450 |
| STP | Simulation and Testing Platform: the L1 element that executes the Aeronef simulation, runs interactive and automated tests in parallel and reports results. | OBJECTIVES §3 |
| Subsystem | Part of an element at L2. Aeronef subsystems: DYN (dynamics), FU (fuel and mass properties), EF (effectors), FC (flight control), AF (autoflight), NAV (navigation), TM (operational data output). | Plan §3 |
| Target | The SI reference value toward which a *mode* guides a quantity: either converted from a *selected value* or set by the autoflight system (for example the position at *Position Hold* engagement). | CV-770 |
| TBD | To Be Determined: a value or item not yet known, recorded in the TBD/TBR register with an owner and a closure date. | METHODOLOGY 9.2 |
| TBR | To Be Resolved (also read "to be reviewed"): a value or statement that is stated provisionally and must be confirmed, recorded in the TBD/TBR register with an owner and a closure date. | METHODOLOGY 9.2 |
| Test | Verification method: operating the system under controlled conditions and measuring the result against the success criteria. | METHODOLOGY 9.3 |
| Test campaign | A set of *test runs* launched together as one batch. | L0-OBJ-130, L0-SUC-050 |
| Test category | One of: functional and logic tests, mode-transition tests, performance tests, statistical campaigns (OBJECTIVES §3). | L0-OBJ-120, L0-SUC-070 |
| Test run | One execution of one *automated test procedure*, or one interactive session, in one *simulation instance*. | L0-OBJ-120, L0-SUC-040 |
| Timestamp | The step index k and the simulation time `t_k` attached to an output sample, selection or event. The step index is authoritative. | CV-840 |
| TO/FROM sense | FROM when the vehicle is beyond the *VOR station* in the direction of the *selected course* (radial within 90° of the course), TO when it is before the station. | CV-640 |
| Total speed | Magnitude of the vehicle velocity relative to the ground, in m/s. "Speed" alone is not used. | CV-460 |
| Track | The direction of horizontal motion: the *direction angle* of the horizontal velocity, ground-referenced. Independent of *heading* on the Aeronef. Undefined at zero horizontal speed. In rad (crew-facing: deg). | CV-540, CV-550 |
| Track Hold | Autoflight *mode* that keeps the *track* at its *target*. It constrains the direction of motion, not where the nose points. | CV-540 |
| Vehicle-carried local frame | Frame V with origin at the body origin and axes parallel to the local reference frame (north, east, down). Reference for the Euler angles. | CV-150 |
| Verification matrix | The table of each requirement with its verification method, procedure and last result (VCRM, `tools/vcrm.py`). | L0-SUC-020, -030 |
| Vertical speed | Rate of change of *altitude*, positive when climbing, in m/s (crew-facing: ft/min). Independent of attitude. | CV-490 |
| VOR | VHF omnidirectional range: in the Aeronef world, a simulated navigation function that gives the vehicle's *radial* from a *VOR station*, its *TO/FROM sense* and its *course deviation* relative to a *selected course*. Version 1: ideal signal within the *reception range*, no noise, no magnetic variation. (D12) | CV-6xx |
| VOR radial tracking | Autoflight lateral *mode* that, after *arming*, intercepts and *captures* the *selected course* of a *VOR station* and then keeps the *course deviation* at zero. TBR (C5). | CV-650 |
| VOR station | Fixed point in the local reference frame, with an identifier, from which radials are defined. | CV-610 |
| Wind | Motion of the air mass relative to the *local reference frame*. In version 1 it is uniform, the same everywhere, and set by the test environment for each run (D17). | L0-ASM-050, CV-470 |
| Withheld assessment scenario | A scenario defined by the *evaluators* and not shown to the *REE*, used to test whether the *reconstructed model* predicts unseen behaviour. | L0-SUC-120 |
