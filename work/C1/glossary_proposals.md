# C1 — Glossary proposals (DYN)

New terms used by the DYN requirements and MS-DYN, and changes to fixed terms. New terms need no change request; a change to a fixed definition goes through one (glossary header). Same table layout as `specs/GLOSSARY.md`.

## 1. New terms

| Term | Definition | Ref. |
| --- | --- | --- |
| Accuracy horizon | The simulation time `[P-DYN-270]` over which the credibility-check tolerances of the *dynamics model* apply; at least the longest run. | MS-DYN §10.3, §11 |
| Body shape | The exterior shape of the *Aeronef* from which the *mass properties* are derived: a *capsule* in version 1 (provisional, L0-CON-140). | MS-DYN §2.1; L1-AER-220 |
| Capsule | A circular cylinder closed at each end by a hemisphere of the cylinder's radius. Its overall length is `[P-DYN-020]` and its diameter `[P-DYN-030]`. | MS-DYN §2.1 |
| Contact step | The first *simulation step* at which the propagated *altitude* is at most zero. *Ground contact* is detected and classified at this step; it is the "contact sample" of L1-AER-280 and of the *landing envelope*. | MS-DYN §9; L1-AER-280; CV-940 |
| Credibility check | A comparison of the simulated motion with an independent solution (a closed form or a conservation law) computed outside the model, with a stated configuration and tolerance. MS-DYN lists checks C-1 to C-8 (NASA-STD-7009B). | METHODOLOGY §10.3; MS-DYN §11 |
| Drag area | The product of the drag coefficient and the reference area, `[P-DYN-100]`, in m², that scales the drag force. | MS-DYN §5.5 |
| Drag force | The aerodynamic force on the vehicle computed by the drag model of MS-DYN from the *air-relative velocity* and the air density at the vehicle *altitude*. It acts at the *centre of gravity*. The only aerodynamic force (L1-AER-030). | MS-DYN §5.5; L1-AER-070 |
| Dynamics model | The Aeronef subsystem DYN, part of the *vehicle model*: it propagates the six-degree-of-freedom rigid-body motion under gravity, drag and the control forces and moments, computes the *sensed acceleration*, and detects and classifies *ground contact*. Specified by MS-DYN. The subject of the DYN requirements. | FUNCTIONAL_ANALYSIS §6.1 |
| Free fall | Motion with zero *control force* and zero *control moment*, for example after *fuel exhaustion*. "Free fall in the *vacuum-equivalent configuration*" is free fall with no drag. | MS-DYN §11; N-290 |
| Gravity force | The force of gravity on the vehicle: the *vehicle mass* times `[P-DYN-010]`, along the positive z axis of the *local reference frame*, at the *centre of gravity*. | MS-DYN §5.2; L1-AER-060 |
| Gust event | One gust or burst of the *wind model*: a one-minus-cosine rise of at least `[P-SYS-570]` to an amplitude of at most `[P-SYS-560]` along a fixed horizontal direction, a hold, and a one-minus-cosine decay of at least `[P-SYS-570]`. | MS-DYN §5.4; D51, D62 |
| Gyroscopic term | The rigid-body term `ω × (J·ω)` of the rotational equation. Zero while pitch and roll are held at zero (D57). | MS-DYN §4.3, §4.5 (K-1); #81 |
| Kinematic terms list | The list in MS-DYN §4.5 of the rigid-body kinematic terms the *dynamics model* retains (L1-AER-020 exception). | MS-DYN §4.5; #81 |
| Nose | The end of the *body shape* on the positive body x axis; it marks the designated forward direction. | CV-170; MS-DYN §2.2 |
| Principal moments of inertia | The three moments of inertia `I_xx`, `I_yy`, `I_zz` about the body axes, which are principal axes (D61). | CV-350; D61 |
| Rotation-during-translation term | The rigid-body term `ω × v` that appears when the translational equation is written in body axes. Whether the model retains it is owner question #81.1. | MS-DYN §4.2, §4.5 (K-2) |
| Step command | The TST's command to advance the *vehicle model* by one *simulation step*, carrying the *wind velocity* for that step. | L1-AER-670; I-25 |
| Terminal vertical speed | The *vertical speed* magnitude at which the *drag force* balances the *gravity force* in a vertical *free fall* with drag, at the local air density; MS-DYN check C-2 gives it with a correction for the density gradient. | MS-DYN §11 (C-2) |
| Total force, total moment | The sum of the forces on the vehicle (*gravity force*, *drag force*, *control force*) and the sum of the moments about the *centre of gravity* (the *control moment* only). | MS-DYN §5.1; L1-AER-050 |
| Vacuum-equivalent configuration | A *vehicle parameter set* with a zero *drag area*, so that no drag acts; used by the *credibility checks*. | MS-DYN §5.5, §11; L1-AER-060 |
| Wind velocity | The velocity of the air mass relative to the *local reference frame*, uniform and horizontal: the steady wind plus the *gust events* (MS-DYN wind model). | CV-470; MS-DYN §5.4 |


## 2. Changes to fixed terms (change request needed)

| Term | Current definition (short) | Proposed change | Reason |
| --- | --- | --- | --- |
| Standard atmosphere | "A standard model of air density as a function of altitude only (D20, L0-ASM-060). MS-DYN names the model (C1)." | Replace the last sentence by: "The model is the U.S. Standard Atmosphere, 1976 (identical to the ICAO Standard Atmosphere up to 32 km), from altitude zero to 47 000 m, with the geopotential altitude taken equal to the altitude (MS-DYN §5.3)." | MS-DYN now names it. |
| Vehicle state | "Position, velocity, attitude (quaternion, with Euler angles derived), body rates and vehicle acceleration of the vehicle at a simulation step." | Add: "The vehicle acceleration of step k is evaluated at the end of the step that produced the state (for step 0, with the inputs of the first step), as MS-DYN §3.3 states. The sensed acceleration is not part of the vehicle state." | An acceleration depends on the inputs, which change at step boundaries; the definition must say which value is meant (DD-080). FUNCTIONAL_ANALYSIS I-07 lists the sensed acceleration inside the state; L1-AER-640 lists it separately. |
| Landing envelope | "...at the ground-contact sample..." | "...at the *contact step*..." | One term for one instant; the contact step need not be an output sample. |
| Sensed acceleration | "...the sum of the non-gravitational forces on the vehicle divided by its current mass (specific force), gravity included in the load felt..." | Add: "Evaluated at the *centre of gravity* (D45) as the *control force* plus the *drag force*, divided by the *vehicle mass* (MS-DYN §8)." Consider dropping "gravity included in the load felt", which reads as if gravity were added. | Makes the definition the formula the model computes. |

## 3. Rework for G2 and D69 (version 2, 2026-11-06)

B3 (approved, D73; CR-B3-37) already changes *Accuracy horizon*, *Airborne*, *Contact step*, *Crash*, *Dynamics model*, *Ground contact*, *Landing*, *Sensed acceleration*, *Total force, total moment* and others, and adds *Gear state*, *Ground reaction*, *Height above the ground*, *Landing gear*, *Liftoff*, *On the ground*. The DYN records use those. New terms used by the reworked DYN records and MS-DYN:

| Term | Definition | Ref. |
| --- | --- | --- |
| Integrated state | The thirteen quantities the *dynamics model* integrates: the position and the velocity of the *centre of gravity* in the *local reference frame*, the attitude quaternion and the *body rates*. The *vehicle state* is the integrated state plus the quantities derived from it (G2-F15). | MS-DYN §3.1; L2-AER-DYN-020 |
| Gravity-free check configuration | A *vehicle parameter set* with `[P-DYN-010]` set to zero, used only by the torque-free rotation and rotation-during-translation *credibility checks*, so that no fall and no *ground contact* ends them before the *accuracy horizon* (D72). | MS-DYN §5.2, §11 |
| Lowest point of the vehicle | The point of the vehicle nearest the *datum plane*: the lowest contact point of the *landing gear* when it is at or below the lowest point of the *body shape*, otherwise the lowest point of the body shape (CV-400). *Ground contact* is detected at it. | MS-DYN §2.6; L2-AER-DYN-500 |
| Rest state | The *integrated state* of the *Aeronef* *on the ground*: the *centre of gravity* at the altitude `[P-DYN-030]/2 + [P-DYN-040]` over a fixed horizontal position, zero velocity, *level attitude* at a fixed *heading*, and zero *body rates*, with the *landing gear* extended. | MS-DYN §9.6; L1-AER-920 |
| Liftoff step | The last *simulation step* *on the ground*: the step at which the upward component of the *control force* first exceeds the vehicle mass times `[P-DYN-010]`. The next step is *airborne*. Refines *Liftoff* (B3). | MS-DYN §9.6; L2-AER-DYN-590 |

**Superseded in §1:** *Contact step* and *Total force, total moment* (merged earlier) are now as revised by CR-B3-37. The §1 entry *Rotation-during-translation term* still says "Whether the model retains it is owner question #81.1"; proposed: "The model retains it (D64)."
