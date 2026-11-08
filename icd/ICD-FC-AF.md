# ICD-FC-AF — Autoflight to flight control

**Status:** Draft, written at integration (I1, 2026-11-08) from the C4 and C5 proposals (`work/C4/interface_needs.md` §6, `work/C5/interface_needs.md` §2). Baselined with L2 at G2.
**Parties:** autoflight (AF) gives; flight control (FC) takes. TM observes the data and is not a party (L2-AER-TM-810).
**Decision:** DD-580 reconciles DD-290 (C4) and DD-360 (C5). The owner accepted both questions (C4-Q01, C4-Q02, C5-Q12, D76).
**Classification:** Protected design material (the interface exposes the split between guidance and regulation, D15).
**Related:** [GLOSSARY](../specs/GLOSSARY.md) *Axis reference*, [CONVENTIONS](../specs/CONVENTIONS.md), [AF_MODE_LOGIC](../specs/AF_MODE_LOGIC.md) §12, [FUNCTIONAL_ANALYSIS](../specs/FUNCTIONAL_ANALYSIS.md) I-13, L1-AER-370, -380, -410, -420.

## 1. Scope

This is the one interface between autoflight and flight control (L1-AER-420, D15). Any autoflight implementation pairs with any flight-control-law design through it. Nothing else crosses from AF to FC: no mode, target, selection, label or fuel information, and FC returns nothing to AF. FC reads the vehicle state and the mass properties directly from the vehicle model (ICD-VM-FS), and AF reads the navigation quantities from NAV (ICD-NAV-AF).

## 2. Conventions

| Item | Rule |
| --- | --- |
| Units | SI (CV-720); angles in rad. No crew unit crosses this interface (CV-760). |
| Frames | Axes of the translational references: north, east and vertical, those of the vehicle-carried local frame V (CV-150), which is parallel to the local frame L at all times. A velocity or an acceleration has the same components in V and in L. A reference **position** is absolute, in L (CV-410); a reference **altitude** is the altitude of the centre of gravity above the datum plane (CV-430). FC resolves the translational demands to the body axes by the attitude (DD-300). |
| Positive directions | North, east and up positive for position, velocity and acceleration (the vertical axis is up, CV-430, CV-490). Heading clockwise from true north (CV-510, CV-520, CV-530). |
| Rate of delivery | Once per control frame, at the start of the frame, after AF has executed and before FC executes (order FCP, NAV, AF, FC, DD-010). The values are those of the control frame that starts at the step with the timestamp (CV-840). |
| Absolute references | Every reference is absolute. FC latches nothing at an engagement or a mode change, because a latched state in FC would be mode information (L1-AER-420). |

## 3. Data items

At each control frame AF gives exactly one of two items: the **off value**, or the **six axis references**.

### 3.1 Axis reference (one per axis, six per frame)

An axis reference has four parts: a reference value, a reference rate, a reference acceleration and the regulated quantity.

| Axis | Reference value | Reference rate | Reference acceleration | Regulated quantity |
| --- | --- | --- | --- | --- |
| North | Position x_N in L (m) | Velocity v_N (m/s) | Acceleration a_N (m/s²) | `value` or `rate` |
| East | Position y_E in L (m) | Velocity v_E (m/s) | Acceleration a_E (m/s²) | `value` or `rate` |
| Vertical | Altitude h, CG altitude, positive up (m) | Vertical speed, positive up (m/s) | Vertical acceleration, positive up (m/s²) | `value` or `rate` |
| Heading | Heading ψ, [0, 2π) (rad) | Heading rate, the derivative of the heading reference (rad/s) | Heading acceleration (rad/s²) | `value` (always) |
| Pitch | Pitch angle (rad), zero | Zero (rad/s) | Zero (rad/s²) | `value` (always) |
| Roll | Roll angle (rad), zero | Zero (rad/s) | Zero (rad/s²) | `value` (always) |

Meaning of the regulated quantity (translational axes only; a rotational axis always regulates its angle):

| Value | FC regulates | The other parts |
| --- | --- | --- |
| `value` | The position or the altitude, to the reference value (a hold) | The reference rate and the reference acceleration are feed-forward |
| `rate` | The velocity or the vertical speed, to the reference rate (a motion at a rate, for example a climb at a selected vertical speed) | The reference acceleration is feed-forward; the reference value is carried but not regulated |

For the heading, at zero pitch and zero roll (D57) the heading rate equals the body rate about the vertical body axis, which is the rate FC regulates (L3-AER-FC-RO).

### 3.2 Off value

A single item, `off`, that replaces the six axis references. It means that autoflight is not engaged. It carries no mode information. While FC receives it, FC sets the effector activation state off and each effector command to zero (L2-AER-FC-190); FC sets the activation state on in the control frame that carries axis references again (L2-AER-FC-200).

## 4. Rules on the content (obligations of AF)

| ID | Rule | Reason | Records |
| --- | --- | --- | --- |
| R-01 | The three parts of a reference are consistent: the rate is the derivative of the value, and the acceleration is the derivative of the rate. | The feed-forward tracks a shaped reference without lag (DD-290); the tracking tolerances assume it. | L2-AER-FC-140 |
| R-02 | The magnitude of the reference acceleration vector (a_N, a_E, vertical) is at most [P-AF-200]; the vertical speed reference changes at most at [P-AF-230]; the heading rate reference is at most [P-SYS-270] and at most [P-AF-200] over the horizontal speed reference. | The budgets [P-AF-200] + [P-FC-020] ≤ [P-SYS-440] and the turn at speed (D72). | L2-AER-AF-420, -430, -440; L2-AER-FC-140 |
| R-03 | A reference steps only at a mode change, at a new selection, or at the first frame after the off value. At a change of the regulated quantity of an axis, the new reference value is where the vehicle will be (no step beyond the tracking tolerance). A velocity vector that turns with the heading (Heading mode) is expressed by a reference acceleration of the speed times the heading rate. | Premise of the settling times [P-FC-060] and [P-FC-090] and of the reference step of L3-AER-FC. | L2-AER-FC-100, -110, -140 |
| R-04 | **Takeoff.** In the engagement frame the off value is replaced by axis references: the horizontal reference position is exactly the position on the ground, the vertical axis regulates the rate at the climb speed [P-AF-240], the heading is the present heading, pitch and roll are zero. | L1-AER-960: no guidance share of the position error at liftoff; FC switches the effectors on in that frame. | L2-AER-FC-200, -220; L2-AER-AF-660 |
| R-05 | **Land.** In the Hover that precedes Land the vertical reference rate is zero; in Land the vertical axis regulates the rate at minus [P-AF-240] (a negative reference rate) from the frame in which the gear is commanded extended, and AF gives the off value in the control frame whose gear state shows the vehicle on the ground. | FC keeps the upward force below the weight while the gear is extended and the vertical reference rate is negative (L2-AER-FC-210), so that a contact is not followed by a liftoff. | L2-AER-FC-190, -210; L2-AER-AF-670 |
| R-06 | **Start of a run.** A run that starts on the ground carries the off value in its first control frame. A test run that starts airborne carries axis references from step zero. | #60; L1-AER-950. | L2-AER-FC-190, -200 |
| R-07 | After fuel exhaustion AF gives the off value (DD-400). FC does nothing else: the commands keep going and the effectors give zero (D68). | L2-AER-AF-860. | L2-AER-AF-860 |

## 5. Rules on FC (obligations of FC)

| ID | Rule | Records |
| --- | --- | --- |
| R-11 | FC regulates each axis separately, to the reference value or the reference rate as the regulated quantity says, with the reference rate and the reference acceleration as feed-forward. FC regulates the position and the altitude only where the regulated quantity is `value`. | L2-AER-FC-010, -020, -100, -110 |
| R-12 | FC takes no other data item from AF and gives nothing to AF. | L2-AER-FC-020, L2-AER-AF-030 |
| R-13 | FC sets the effector activation state from the off value alone. | DD-340; L2-AER-FC-190, -200 |

## 6. Recording and test

TM records the axis references as FC received them, the off value included, as signal S-09 of ICD-AER-TST (class: protected, proposed). A test autoflight variant, selected through the configuration, may send scripted axis references and the off value through this interface in place of the mode logic; it is the open-loop source of the FC tests and the demonstration variant of L1-AER-410 (IN-C4-30).

## 7. Traceability

| Interface | FUNCTIONAL_ANALYSIS I-13 |
| --- | --- |
| FC side | L2-AER-FC-020, -190, -200, -210; L3-AER-FC (introduction) |
| AF side | L2-AER-AF-030, -090, -410, -420 to -440 |
| L1 | L1-AER-370, -380, -410, -420, -930 |
| Decisions | DD-290, DD-300, DD-340, DD-360, DD-580 |
