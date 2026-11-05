## CON — Constraints (L0-CON)

### L0-CON-010

```req
ID:            L0-CON-010
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall model the Aeronef as a rigid body with six degrees of
  freedom.
Rationale:     The concept fixes six degrees of freedom: translation along three axes and rotation
  about three axes (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §2, §7). A rigid body keeps
  the dynamics simple and fully understood; structural flexibility and fuel slosh are
  excluded by L0-ASM-080. Children must show (D41): (Inspection) the model
  specification states rigid-body equations of motion in six degrees of freedom and no
  structural or internal degrees of freedom.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-020

```req
ID:            L0-CON-020
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall give the Aeronef independent control authority in each of
  its six degrees of freedom.
Rationale:     This is the defining property of the vehicle: translation does not require the
  vehicle to turn or tilt, and attitude can be controlled independently of translation
  (AIRCRAFT_CHARACTERISTICS §2, §7). It is why heading and track are independent on the
  Aeronef; pitch and roll stay level (D10), and the attitude behaviour of each mode is
  defined at L2 (D33). Children must show (D41): (Analysis) the force effector set can
  produce a pure force along each body axis and a pure moment about each body axis,
  each with the other five force and moment components equal to zero.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §2, §7; OBJECTIVES.md §2
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-030

```req
ID:            L0-CON-030
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude from the Aeronef model any coupling by which motion
  along one degree of freedom induces an acceleration along another degree of freedom
  in the body frame.
Rationale:     The initial design avoids coupling between axes (OBJECTIVES §2), and the concept
  excludes aerodynamic coupling (AIRCRAFT_CHARACTERISTICS §2). The scope of the
  constraint is the owner's definition D18, which is wider than aerodynamic coupling.
  G0 owner review (2026-10-25): accepted with the owner's definition (D18): a motion
  along one degree of freedom does not induce an acceleration on another axis, seen
  from the body frame. This is unlike winged aircraft, where roll and yaw are coupled.
  How the rigid-body kinematic and gyroscopic terms are treated is decided in the model
  specification (#81, deferred to L2). Children must show (D41): (Inspection) the model
  specification defines no term by which motion along one degree of freedom produces a
  force, moment or acceleration along another degree of freedom in the body frame,
  other than the rigid-body kinematic terms decided under #81.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       Treatment of rigid-body kinematic terms (#81, deferred to L2), Martin, closes at G2
  (C1)
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-040

```req
ID:            L0-CON-040
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude aerodynamic lift from the Aeronef model.
Rationale:     The Aeronef is not a conventional aircraft; lift would couple attitude and
  translation and defeat the independent control of L0-CON-020
  (AIRCRAFT_CHARACTERISTICS §1, §7; METHODOLOGY §4.3 example). Children must show
  (D41): (Inspection) the model specification defines no aerodynamic lift force.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §1, §7; METHODOLOGY.md §4.3
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-050

```req
ID:            L0-CON-050
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude aerodynamic control surfaces from the Aeronef.
Rationale:     Motion is generated by fictional force effectors rather than aerodynamic control
  surfaces (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §2, §7). Children must show (D41):
  (Inspection) the Aeronef requirements and the model specification define no
  aerodynamic control surface.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-060

```req
ID:            L0-CON-060
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall generate each control force and control moment on the
  Aeronef with fictional force effectors.
Rationale:     Instead of engines, wings or control surfaces, the Aeronef uses fictional
  gravity-like force emitters (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §3). A control
  force or moment (glossary) is any force or moment other than gravity and aerodynamic
  drag. Children must show (D41): (Inspection) the model specification identifies the
  force effectors as the only source of force and moment other than gravity and
  aerodynamic drag.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §3, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-070

```req
ID:            L0-CON-070
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall fix the direction of action of each force effector relative
  to the Aeronef body.
Rationale:     AIRCRAFT_CHARACTERISTICS §3 states that each emitter acts in a fixed direction. This
  record reads 'fixed' as fixed in the body frame (no gimballing), which is the reading
  under which the effector set provides authority along and about body axes. The layout
  of the effectors is a design decision, not an L0 constraint. G0 owner review
  (2026-10-25): accepted (D19). Nothing swivels, so there must be enough effectors to
  give control in all six degrees of freedom (L0-CON-020). The TBR is closed. Children
  must show (D41): (Inspection) the effector requirements and the model specification
  define a constant body-frame direction of action for each force effector.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-080

```req
ID:            L0-CON-080
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude the physical mechanism of force generation from the
  force effector model.
Rationale:     No physical explanation of the emitter technology or its energy conversion is
  required; effectors are characterised by control effectiveness, limits and fuel
  consumption (AIRCRAFT_CHARACTERISTICS §3, §7). Children must show (D41): (Inspection)
  the effector model is defined only through control effectiveness, limits, command
  response and fuel consumption parameters.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §3, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-090

```req
ID:            L0-CON-090
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall limit the external effects on the Aeronef model to gravity,
  aerodynamic drag on the air-relative velocity and ground contact.
Rationale:     The concept lists gravity and air resistance as the only external effects to be
  modelled (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §2, §7). The gravity and drag
  models are defined in the model specification. G0 owner review (2026-10-25): accepted
  with wind and ground contact. Drag acts on the velocity relative to the air, which
  includes the wind (L0-ASM-050, D17). Ground contact is the ideal landing of
  L0-CON-290 (D37). Children must show (D41): (Inspection) the model specification
  defines gravity and aerodynamic drag on the vehicle velocity relative to the air
  mass, including wind, as the only external forces and moments, and ground contact
  (L0-CON-290) as the only other external effect.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §2, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-100

```req
ID:            L0-CON-100
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall supply the force effectors from a finite onboard quantity
  of fictional fuel.
Rationale:     A finite supply of fictional high-energy-density fuel powers the emitters (OBJECTIVES
  §2; AIRCRAFT_CHARACTERISTICS §4). The finite supply bounds every mission; reaching
  fuel exhaustion is nominal behaviour in this cycle, not a failure. Children must show
  (D41): (Inspection) the Aeronef requirements define an initial fuel quantity as a
  parameter and make the output of each force effector depend on the availability of
  fuel.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §4, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-110

```req
ID:            L0-CON-110
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall decrease the mass of the Aeronef by the mass of the fuel
  consumed.
Rationale:     Fuel consumption affects vehicle mass (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §4).
  The way consumed fuel leaves the vehicle is covered by L0-ASM-090. Children must show
  (D41): (Analysis) over a simulated run, the vehicle mass equals the initial mass
  minus the time integral of the fuel flow, compared with an independent computation
  (METHODOLOGY §10.3).
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §4, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-120

```req
ID:            L0-CON-120
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall define the fuel consumption relationships for translational
  actuation and for rotational actuation as configurable parameters.
Rationale:     OBJECTIVES §2 and AIRCRAFT_CHARACTERISTICS §4 call for configurable consumption
  relationships for linear and rotational actuation. Configurable parameters let
  consumption be tuned and varied in campaigns without a software change. Children must
  show (D41): (Demonstration) the parameter database holds the translational and
  rotational consumption parameters, and a change of their values takes effect in a run
  without modification of the software.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §4
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-130

```req
ID:            L0-CON-130
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall treat the centre of gravity of the Aeronef as fixed in the
  body frame.
Rationale:     The centre of gravity is initially treated as fixed, including while fuel is consumed
  (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §4; METHODOLOGY §4.3 example). A fixed
  centre of gravity keeps the effector moment arms constant. Children must show (D41):
  (Inspection) the model specification defines the centre of gravity as a constant
  position in the body frame for each fuel state.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §4, §7; METHODOLOGY.md §4.3
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-140

```req
ID:            L0-CON-140
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall compute the moments of inertia of the Aeronef from a
  simplified mass distribution over an elongated body shape.
Rationale:     The exterior shape matters only through its mass properties (AIRCRAFT_CHARACTERISTICS
  §1). The first version is a simple elongated shape, provisionally resembling a Tic
  Tac; the inertias must still support a meaningful rotational dynamics model
  (AIRCRAFT_CHARACTERISTICS §4). Whether inertia varies with fuel state is left to the
  fuel and mass-properties requirements. Children must show (D41): (Inspection) the
  model specification derives each moment of inertia from a stated elongated body shape
  and a stated simplified mass distribution.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §1, §4, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       Elongated body shape provisional, TBR, Martin, 2026-11-30
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-150

```req
ID:            L0-CON-150
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall give the Aeronef a designated forward direction marked by
  its nose.
Rationale:     The craft has a nose, and a cockpit with windows, that establish a consistent
  orientation for piloting and navigation (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §1).
  The forward direction is the basis for the body axes and for heading, which is
  distinct from track on this vehicle. Children must show (D41): (Inspection) the
  conventions define the forward body axis through the nose, and the crew station is at
  a stated position in the body frame.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §1, §7
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-160

```req
ID:            L0-CON-160
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude electrical power generation, distribution and
  consumption from the Aeronef model.
Rationale:     The electrical power system and electrical consumption are outside the initial
  modelling scope (AIRCRAFT_CHARACTERISTICS §4, §7). The force effectors draw only on
  fuel (L0-CON-100). Children must show (D41): (Inspection) the Aeronef requirements
  and the model specification define no electrical power generation, distribution or
  consumption.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §4, §7; METHODOLOGY.md §1
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-170

```req
ID:            L0-CON-170
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall represent the crew interface of the Aeronef as data
  exchanged with the Aeronef, without a model of physical cockpit controls or display formats.
Rationale:     Detailed pilot controls and displays are excluded (AIRCRAFT_CHARACTERISTICS §7). The
  crew still selects modes and targets and receives annunciations; these are data items
  exchanged with the Aeronef, which also lets test procedures act as the crew
  (L0-ASM-120). G0 owner review (2026-10-25): accepted for now. For manual testing, the
  owner will fly the craft through a flight control panel. The panel is defined in the
  detailed design and in the requirements of the craft and its subsystems (#79, #80.3).
  A graphical interface for it belongs to the TST and does not change the data boundary
  set here. Children must show (D41): (Inspection) the Aeronef requirements define each
  crew selection and each annunciation as a data item, and define no physical control
  device or display format.
Parent(s):     —
Source:        AIRCRAFT_CHARACTERISTICS.md §5, §7
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-180

```req
ID:            L0-CON-180
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall exclude direct manual flight controls from the Aeronef.
Rationale:     Autoflight is the primary operating method and manual control may be introduced later
  (OBJECTIVES §2; AIRCRAFT_CHARACTERISTICS §6). The plan records manual control with
  the EARS 'Where' pattern and does not develop it in this cycle
  (AIRCRAFT_REQUIREMENTS_PLAN §1). G0 owner review (2026-10-25): manual control with a
  stick or yoke is not in scope. The crew's manual inputs are made through the flight
  control panel, which is as manual as flying the Aeronef gets; the system generates
  the effector forces from those inputs. A direct manual flight control is a control,
  such as a stick or a yoke, with which the pilot commands the effectors without the
  autoflight system. Children must show (D41): (Inspection) no Aeronef requirement
  defines a direct manual flight control; each crew input is made through the flight
  control panel.
Parent(s):     —
Source:        OBJECTIVES.md §2; AIRCRAFT_CHARACTERISTICS.md §6; AIRCRAFT_REQUIREMENTS_PLAN.md §1
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-190

```req
ID:            L0-CON-190
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall make the simulation core executable without a graphical
  display.
Rationale:     A graphical interface is optional; the core simulator must work without graphics so
  that large automated campaigns run efficiently (OBJECTIVES §3; TESTING_ENVIRONMENT
  §2). G0 owner review (2026-10-25): accepted for batch runs and automated testing.
  Manual testing needs a graphical user interface, which may be minimal; it may be
  needed from the start, so that the owner can try the craft before automated runs.
  This is an TST capability (L0-OBJ-070); the headless core required here is unchanged.
  Children must show (D41): (Demonstration) an automated test campaign runs to
  completion on an execution host with no graphical display attached. No Aeronef
  function may need a display (CR-B1-02, D50); the TST children come when the plan is
  extended to that branch (D44).
Parent(s):     —
Source:        OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §2
Allocated to:  TST, AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       4
```

### L0-CON-200

```req
ID:            L0-CON-200
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall make each flight-control-law design replaceable without
  modification of the vehicle model.
Rationale:     Control-law designers need to swap controllers without touching the vehicle model
  (METHODOLOGY §4.1), and the vehicle, control laws and autoflight logic need clear
  boundaries (TESTING_ENVIRONMENT §2; D15). One set of control laws is developed for
  now (D42); keeping the laws replaceable lets more designs be added later without
  touching the vehicle model. Children must show (D41): (Demonstration) a test variant
  of the flight-control-law design is substituted through configuration, and the
  vehicle model files are unchanged, as shown by their checksums.
Parent(s):     —
Source:        TESTING_ENVIRONMENT.md §2, §7; METHODOLOGY.md §4.1
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-210

```req
ID:            L0-CON-210
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall make each autoflight implementation replaceable without
  modification of the vehicle model.
Rationale:     Same reason as L0-CON-200 for autoflight versions (OBJECTIVES §2; TESTING_ENVIRONMENT
  §2, §7). Modes and controllers are decoupled, so any autoflight implementation pairs
  with any control law (D15). There is one autoflight implementation (D24). Children
  must show (D41): (Demonstration) a test variant of the autoflight implementation is
  substituted through configuration, and the vehicle model files are unchanged, as
  shown by their checksums.
Parent(s):     —
Source:        OBJECTIVES.md §2; TESTING_ENVIRONMENT.md §2, §7
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-220

```req
ID:            L0-CON-220
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall withhold the protected design material from the
  reverse-engineering effort.
Rationale:     G0 owner review (2026-10-25): deleted. The owner will select the documents given to
  the reverse-engineering functions when that part of the project starts; the system
  itself does not have to protect anything, so this constraint is irrelevant here. The
  reverse-engineering objective (L0-OBJ-160) stays. Original rationale: Separation
  between the original design and the material available to the reverse-engineering
  agents is essential to the experiment (OBJECTIVES §4; REVERSE_ENGINEERING §2, §7).
  Protected design material (glossary) is a closed set: requirements, design
  specifications, the model specification, the parameter database, the interface
  control documents, implementation and source code, ground-truth test expectations,
  assessment answers and the manual trace register.
Parent(s):     —
Source:        OBJECTIVES.md §4; REVERSE_ENGINEERING.md §2, §7
Allocated to:  RVS, AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: the release record of each evidence package lists
  no item of protected design material, and L0-SUC-140 is met.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-CON-230

```req
ID:            L0-CON-230
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall limit the released evidence to operational manuals and
  procedures, black-box access to the executable simulation and released operational data.
Rationale:     G0 owner review (2026-10-25): deleted. The owner will select the documents given to
  the reverse-engineering functions when that part of the project starts; the system
  itself does not have to protect anything, so this constraint is irrelevant here. The
  reverse-engineering objective (L0-OBJ-160) stays. Original rationale:
  REVERSE_ENGINEERING §3 defines the three kinds of information available to the
  agents: human-oriented operational documents, observable behaviour in simulation, and
  recorded operational data. Black-box access (glossary) means running and stimulating
  the simulation through its operator interface without access to source code or
  internal state. The exact items released are fixed in the reverse-engineering effort
  requirements (METHODOLOGY §11.2, rule 4).
Parent(s):     —
Source:        OBJECTIVES.md §4; REVERSE_ENGINEERING.md §3; METHODOLOGY.md §11.2
Allocated to:  RVS, AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each item in the release record of each evidence
  package belongs to one of the three permitted kinds.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-CON-240

```req
ID:            L0-CON-240
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall restrict the content of each released evidence item to
  externally observable behaviour and operator actions.
Rationale:     G0 owner review (2026-10-25): deleted. The owner will select the documents given to
  the reverse-engineering functions when that part of the project starts; the system
  itself does not have to protect anything, so this constraint is irrelevant here. The
  reverse-engineering objective (L0-OBJ-160) stays. Original rationale: Manuals must
  describe observable behaviour and operator actions without pasting requirement text
  (METHODOLOGY §11.2, rule 1), and operational data must not inadvertently expose
  protected requirements or implementation details (REVERSE_ENGINEERING §3C, §7). This
  is why each operational data signal is classified releasable or protected.
Parent(s):     —
Source:        REVERSE_ENGINEERING.md §3, §7; METHODOLOGY.md §11.2
Allocated to:  AER, TST, RVS
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: a review of each released evidence item against
  the protected design material, recorded before release, finds no requirement text and no signal
  classified protected.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Deleted
Version:       2
```

### L0-CON-250

```req
ID:            L0-CON-250
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall perform the reverse-engineering effort with agents that
  have had no access to the protected design material.
Rationale:     The reconstruction must be made by independent agents (OBJECTIVES §4;
  REVERSE_ENGINEERING §1, §7). An AI agent that authored or reviewed the design carries
  that knowledge in its context, so withholding the material is not enough on its own.
  G0 owner review (2026-10-25): deferred. Nothing is implemented for reverse
  engineering now; this is revisited once the other elements of the project are done
  (#69). Stays Draft. Children must show (D41): (Inspection) the session record of each
  reverse-engineering agent shows a context limited to the released evidence from the
  start of the session. Allocated only to RVS: its children come when the plan is
  extended to that branch (D44).
Parent(s):     —
Source:        OBJECTIVES.md §4; REVERSE_ENGINEERING.md §1, §7
Allocated to:  RVS
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       3
```

### L0-CON-260

```req
ID:            L0-CON-260
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall state each quantity that is not a crew-facing quantity in
  SI units.
Rationale:     Requirements, models and the parameter database use SI units (METHODOLOGY §8.4, rule
  12; plan decision D7). A crew-facing quantity (glossary) is one the crew selects or
  that is annunciated to the crew; those follow L0-CON-270. Children must show (D41):
  (Inspection) each parameter in the parameter database that is not a crew-facing
  quantity has an SI unit, and each quantity in a requirement statement that is not
  crew-facing is expressed in an SI unit.
Parent(s):     —
Source:        METHODOLOGY.md §8.4; AIRCRAFT_REQUIREMENTS_PLAN.md §9 D7
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-270

```req
ID:            L0-CON-270
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall state each crew-facing quantity in the crew-facing unit
  that the conventions document assigns to its quantity.
Rationale:     The units are those of plan decision D7, which adopts North American aviation units
  for everything the crew selects or sees, to keep the operating concept airliner-like.
  The unit table and the conversions to SI are fixed in the conventions document
  (CV-740, CV-750), so the statement points to it instead of repeating it. G0 owner
  review (2026-10-25): accepted. Time is in whatever unit makes sense: vertical rates
  in ft/min, flight duration in hours or minutes (D34). Children must show (D41):
  (Inspection) each crew selection and each annunciated quantity uses the unit the
  conventions unit table (CV-740) assigns to it, including lb for fuel (D9) and hours
  or minutes for durations (D34), and the conventions give its conversion to SI.
Parent(s):     —
Source:        AIRCRAFT_REQUIREMENTS_PLAN.md §9 D7
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       4
```

### L0-CON-280

```req
ID:            L0-CON-280
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall define the reference frames, axes and sign conventions of
  the Aeronef consistently with AIAA R-004-1992 practice.
Rationale:     Axis and sign conventions must be fixed before any dynamics requirement is written,
  and every axis must follow the coordinate-system standard (METHODOLOGY §2; §8.4, rule
  12). The conventions document applies the standard and records the choices it leaves
  open. G0 owner review (2026-10-25): accepted. No copy of R-004 is held; the
  conventions were checked against public sources (D36). Children must show (D41):
  (Inspection) the conventions document defines each reference frame, axis and sign
  convention used by the Aeronef, states that it is consistent with R-004 practice as
  checked against the public sources of D36, and identifies each documented departure.
Parent(s):     —
Source:        METHODOLOGY.md §2, §8.4; AIRCRAFT_REQUIREMENTS_PLAN.md §6 (A3)
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Baselined
Version:       3
```

### L0-CON-290

```req
ID:            L0-CON-290
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall model ground contact of the Aeronef as a landing within the
  landing envelope and as a crash outside it.
Rationale:     G0 owner review (2026-10-25), decision D37: landing has to be modelled. Contact with
  the ground within a landing envelope of velocity and acceleration is a successful
  landing; contact outside it is a crash. There is no landing gear, bounce or friction
  model (L0-ASM-110). The envelope limits are parameters set at a lower level. Children
  must show (D41): (Inspection) the model specification defines ground contact at
  altitude zero, a landing envelope of velocity and acceleration limits, and the
  landing and crash outcomes.
Parent(s):     —
Source:        Owner review at G0, 2026-10-25 (D8, D37)
Allocated to:  AER, TST
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       Landing envelope limits TBD (lower level), Martin, closes at G2
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-300

```req
ID:            L0-CON-300
Level:         L0
Type:          Constraint
Statement:     The Aeronef project shall limit the force of each force effector to a maximum
  magnitude.
Rationale:     G0 owner review (2026-10-25): each effector has a maximum force. How the controls
  manoeuvre when an effector is at its limit is a detailed-design matter. The
  per-effector maxima are effector parameters, set at a lower level. Children must show
  (D41): (Inspection) the effector requirements define a maximum force magnitude for
  each force effector as a parameter; (Test) no automated test run produces an effector
  force above it.
Parent(s):     —
Source:        Owner review at G0, 2026-10-25
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    —
TBD/TBR:       Per-effector maximum force values TBD (EF level), Martin, closes at G2 (C3)
Owner:         Martin
Status:        Baselined
Version:       2
```

### L0-CON-310

```req
ID:            L0-CON-310
Level:         L0
Type:          Constraint
Statement:     While the Aeronef is airborne, the Aeronef project shall limit the magnitude of the
  acceleration sensed by the crew to [P-SYS-120].
Rationale:     G0 owner review (2026-10-25): the crew must be protected from excessive g load. The
  limiting factor is the acceleration the crew senses and experiences, not the force
  itself (D38, #87). The sensed acceleration is the specific force: the sum of the
  non-gravitational forces on the Aeronef divided by its current mass. Because the mass
  falls as fuel is consumed (L0-CON-110, L0-ASM-090), the allowed resultant effector
  force falls with it, and the force has to be compensated for the fuel used. The limit
  applies to the whole project and lives in the system constants. How the controls
  handle it when an effector is at its own limit (L0-CON-300) and a manoeuvre is needed
  is a detailed-design matter. The owner set the limit at plus or minus 3 g for now
  (2026-10-25): a sensed-acceleration magnitude of at most 3 g in any direction, with g
  the standard gravity 9.806 65 m/s² (P-SYS-120 = 29.419 95 m/s²). Owner precision
  (2026-10-25): the limit is on the total load the crew feels, gravity included. The 1
  g needed to hold the Aeronef up against gravity counts toward the 3 g: hovering is 1
  g, and free fall is 0 g. The limit applies while the Aeronef is airborne: the ideal
  landing has no contact dynamics (L0-CON-290), so the landing envelope's own
  acceleration limit covers ground contact. Where on the Aeronef the crew acceleration
  is evaluated (centre of gravity or crew station) is set at a lower level. The g of
  the limit is standard gravity whatever value the model gravity P-DYN-010 takes, so
  the hover figure of 1 g is exact only if P-DYN-010 equals standard gravity. Children
  must show (D41): (Test) in every automated test run, at every fuel state, while the
  Aeronef is airborne, the magnitude of the sensed acceleration (specific force) does
  not exceed [P-SYS-120]; the acceleration limit of the landing envelope (L0-CON-290)
  does not exceed [P-SYS-120].
Parent(s):     —
Source:        Owner review at G0, 2026-10-25
Allocated to:  AER
Criticality:   Not assessed
Verification:  Inspection — TBD; success criteria: each child requirement has passed its
  verification and the decomposition has been reviewed (D41).
Parameters:    P-SYS-120
TBD/TBR:       P-SYS-120 = 29.419 95 m/s² (3 g) TBR (owner, 'for now'), Martin, closes at G1
Owner:         Martin
Status:        Baselined
Version:       4
```
