# Aeronef Project — Aircraft Characteristics

**Status:** Initial concept summary
**Date:** 2026-10-24

## 1. General Concept

The Aeronef is a fictitious flying vehicle created as a deliberately simplified platform for studying flight-control laws, autoflight functions, simulation, automated testing, and reverse engineering. It is not intended to reproduce a conventional airplane or its aerodynamic systems.

The first version will use a simple, elongated "Tic Tac" shape. The precise exterior shape is not operationally important, except insofar as it affects mass properties and moments of inertia. The craft has a designated forward direction, a nose, and a cockpit with windows, establishing a consistent orientation for piloting and navigation.

## 2. Motion and Physics

The vehicle has six degrees of freedom (6-DOF):

- Translational motion along three axes.
- Rotational motion about three axes.

The propulsion/control concept permits independent commands in these six degrees of freedom. Translation does not require the vehicle to turn or tilt, and attitude can be controlled independently of the translational motion. The initial model deliberately excludes aerodynamic control surfaces and aerodynamic coupling between the axes.

The external physical effects to be modeled are:

- Gravity.
- Air resistance (drag).

The precise equations, axis conventions, drag model, and physical limits have not yet been defined.

## 3. Force-Generating Effectors

Instead of conventional engines, wings, or control surfaces, the vehicle uses fictional gravity-like force emitters (effectors). Each emitter acts in a fixed direction; the collective set of effectors provides control authority for translation and rotation along/about all three axes. The emitters generate variable force or rotational effect under command.

No physical explanation of the emitter technology or its energy-conversion mechanism is required. The effectors will ultimately be characterized by control effectiveness, limits, and fuel-consumption parameters, to be defined later.

## 4. Mass, Inertia, and Fuel

The vehicle carries a finite quantity of fictional, very high-energy-density fuel. Fuel is consumed to generate the forces and rotational effects commanded from the effectors. Fuel consumption will be represented with configurable parameters, including consumption rates associated with linear and rotational actuation.

As fuel is consumed, the total vehicle mass decreases. For the initial approximation, the center of gravity is assumed fixed and the mass distribution is simplified. A suitable set of moments of inertia will be assigned based on the craft's basic geometry and simplifying assumptions. These choices must remain compatible with a meaningful rotational dynamics model; their exact formulation is still open.

The electrical power system and electrical consumption are outside the initial modeling scope.

## 5. Flight Controls

Flight-control functions will command the effectors and regulate motion independently for each of the three translational and three rotational axes. Multiple control-law designs are expected to be developed and compared.

The detailed axis controllers, control allocation, handling qualities, limits, and manual interfaces remain to be designed.

## 6. Autoflight

Autoflight is the primary operating method in the initial development, because direct manual control of a fully independent 6-DOF vehicle is expected to be difficult.

The autoflight system will take inspiration from the modes and operational concepts used in commercial airliners, while adapting them to the Aeronef's unconventional flight capabilities and simplified physics. The modes, transitions, guidance functions, and operating procedures will be defined later.

Manual control may be introduced subsequently, but autoflight development will come first.

## 7. Initial Modeling Boundaries

**Included in the initial aircraft concept:**

- A simple, oriented vehicle geometry with nose and cockpit.
- Six-degree-of-freedom rigid-body motion.
- Gravity and aerodynamic drag.
- Independent translational and rotational control capability.
- Fictional fixed-direction force effectors.
- Finite fuel supply, fuel consumption, and decreasing vehicle mass.
- Simplified center-of-gravity and inertia assumptions.
- Flight-control laws and airliner-inspired autoflight functions.

**Excluded or deferred:**

- Conventional aerodynamic lift and control surfaces.
- Realistic propulsion/force-emitter physics.
- Detailed aircraft electrical systems and other ancillary systems.
- Detailed pilot controls and displays.
- Precise physical parameters, actuator layouts, control laws, and autoflight mode definitions.

---

*This document describes the preliminary vehicle concept, not a finalized set of engineering requirements.*
