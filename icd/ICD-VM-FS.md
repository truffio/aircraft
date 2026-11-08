# ICD-VM-FS — Vehicle model to flight software

**Status:** Draft, written at integration (I1, 2026-11-08) from the interface needs of B1, C1 to C6. Baselined with L2 at G2.
**Home decision:** The vehicle-model boundary has its own interface control document (DD-570; IN-B1-01, TT-720). It is not a section of ICD-AER-TST, which keeps to the interface with the test environment.
**Parties:** the vehicle model (DYN, FU, EF) on one side; the flight software (FC, AF, FCP, NAV) on the other. TM observes the boundary and is not a party (L2-AER-TM-810). The TST drives the vehicle model per simulation step through ICD-AER-TST and does not use this interface.
**Classification:** Protected design material.
**Related:** [CONVENTIONS](../specs/CONVENTIONS.md), [MS-DYN](../specs/MS-DYN.md), [FUNCTIONAL_ANALYSIS](../specs/FUNCTIONAL_ANALYSIS.md) §5, L1-AER-430, -440, L0-CON-200, -210.

## 1. Scope

L1-AER-430 fixes the data between the vehicle model and the flight software to a closed list. A fixed boundary is what lets a control law and an autoflight implementation be replaced without modifying the vehicle model. **The list is closed:** into the vehicle model, the effector commands (with the effector activation state) and the landing gear command; out of it, the vehicle state, the gear state, the mass properties and the fuel state. Every other data item of the vehicle model (the control force and moment, the ground reaction, the drag, the mass-properties step values that DYN uses) is internal to the vehicle model and is defined in MS-DYN.

## 2. Conventions

| Item | Rule |
| --- | --- |
| Units, frames | SI (CV-720); frames, axes and signs as CONVENTIONS defines them (CV-120 to CV-350). Attitude is a unit quaternion (CV-250) with the Euler angles derived by CV-260. No crew unit crosses. |
| Rate | The vehicle model produces its outputs at every simulation step (`[P-SYS-300]`). The flight software reads them once per control frame (`[P-SYS-310]`), the values of the **frame-start step**, the first simulation step of the frame (L2-AER-DYN-330, L2-AER-FC-040). The effector commands of a control frame are used by EF at every simulation step of that frame (L2-AER-EF-150). |
| Perfect knowledge | The vehicle state is exact: no sensor model, no noise (L1-AER-440, #83). A sensor model would be a later extension at this boundary. |
| Timestamp | Step index and simulation time (CV-840). |

## 3. Into the vehicle model

### 3.1 Effector commands (I-12), FC to EF

| Item | Content | Unit and rule | Records |
| --- | --- | --- | --- |
| Effector command | One per effector: the force asked of the effector along its direction of action. A positive command acts along the effector's direction (CV-330) | N; the number, order and sign are those of the vehicle parameter set (P-EF-100 to -130) | L2-AER-EF-400; L2-AER-FC-060, -070 |
| Effector activation state | `on` or `off` for the effector set. While `off`, each effector output is zero and no fuel is used; `off` before the first commands of a run (DD-180, DD-340) | — | L2-AER-EF-210; L2-AER-FC-190, -200 |

The commands are held for the control frame. FC never commands outside the output limits (L2-AER-FC-160), and the authority box (L2-AER-EF-330, DD-170) is guaranteed together. After fuel exhaustion EF gives zero whatever the commands are (D68).

### 3.2 Landing gear command (I-43), AF to DYN

| Item | Content | Rule | Records |
| --- | --- | --- | --- |
| Landing gear command | `extend` or `retract` | One per control frame, held between changes; the first command equals the initial gear position. AF commands retraction only airborne at the hover height, and extension at the activation of Land and throughout the on-ground state (DD-410). A retraction commanded on the ground takes effect at the first airborne step (DD-220) | L2-AER-DYN-270, -280; L2-AER-AF-700 to -740 |

## 4. Out of the vehicle model

### 4.1 Vehicle state (I-09, I-10), DYN to NAV and FC

| Item | Unit | Frame / convention |
| --- | --- | --- |
| Position: north, east, altitude | m | Local frame L (CV-410); altitude of the CG above the datum plane, positive up (CV-430) |
| Velocity: north, east, down components | m/s | Frame V, parallel to L (CV-150, CV-460) |
| Attitude: unit quaternion; Euler angles (yaw, pitch, roll) derived by CV-260 | 1; rad | Body frame B relative to V (CV-250) |
| Body rates: p, q, r | rad/s | Body frame B (CV-280) |
| Vehicle acceleration | m/s² | Frame V; evaluated at the end of the step that produced the state, for step 0 with the inputs of the first step (DD-080, DD-250) |

The sensed acceleration is **not** part of the vehicle state and does not cross this boundary (IN-C1-35). The state at the contact step of a landing is the rest state; of a crash, the propagated state raised onto the datum plane (DD-240). Records: L2-AER-DYN-320, -330, -340; L2-AER-FC-030, -040; L2-AER-NAV-200.

### 4.2 Gear state (I-45), DYN to AF and FC

| Item | Values | Rule |
| --- | --- | --- |
| Gear position | `extended`, `retracted`, `in transit` | Of the frame-start step. AF uses it to end Land and to extend and retract; FC uses only `extended`, for the descent cap (L2-AER-FC-210, CR-C4-02) |
| On the ground | true / false | True from the contact step of a landing (the step in which the vehicle comes to rest) |

NAV and FCP take no gear state. The panel gets the gear position through AF (ICD-FCP §5). Records: L2-AER-DYN-290, -320, -340; L2-AER-FC-030, -210; L2-AER-AF-060, -270, -710.

### 4.3 Mass properties (I-05), FU to FC

| Item | Unit | Rule |
| --- | --- | --- |
| Vehicle mass | kg | The same mass that FU gives DYN for the same step (L2-AER-FU-140) |
| Centre-of-gravity position | m, body axes | The zero vector at every fuel state (the body origin, L2-AER-FU-150). FC does not use it |
| Principal moments of inertia | kg·m² | Three values about the body axes; the products of inertia are zero (D61). They fall linearly with the fuel (DD-120) |

FC reads the mass and the three moments of the frame-start step and holds no estimate of them (L3-AER-FC-TR-090, -RO-060). The glossary *Mass properties* is this item.

### 4.4 Fuel state (I-06), FU to AF and FCP

| Item | Unit and values | Records |
| --- | --- | --- |
| Remaining fuel mass | kg | L2-AER-FU-210 |
| Low-fuel indication | true while the remaining fuel mass is below the fraction `[P-FU-020]` of `[P-FU-010]` | L2-AER-FU-220 |
| Fuel-exhaustion indication | true at fuel exhaustion | L2-AER-FU-230 |

One fuel-state item serves both recipients (L2-AER-FU-240). AF uses only the fuel-exhaustion indication (DD-400, TR-01 of AF_MODE_LOGIC); the panel uses all three (ICD-FCP §6). FC takes no fuel state.

## 5. What does not cross

| Item | Where it goes |
| --- | --- |
| Control force and moment, ground reaction, drag, wind | Internal to the vehicle model (MS-DYN) |
| Sensed acceleration, effector outputs, fuel mass flow, vehicle mass, remaining fuel mass per step | The vehicle model to TM only (ICD-AER-TST §6, signals S-12, S-13, S-17, S-18) |
| Any mode, target, selection, axis reference | Not across this boundary (ICD-FC-AF, ICD-FCP) |
| Navigation quantities | Computed by NAV from the vehicle state (ICD-NAV-AF); not part of the boundary |

## 6. Traceability

| Vehicle model side | L2-AER-DYN-270, -280, -290, -320, -330, -340; L2-AER-FU-130, -140, -150, -210 to -240; L2-AER-EF-150, -400 |
| --- | --- |
| Flight software side | L2-AER-FC-030, -040, -070, -190 to -210; L2-AER-AF-060; L2-AER-NAV-200; L2-AER-FCP-070 |
| L1 | L1-AER-430, -440, -910 |
| Decisions | DD-080, DD-120, DD-170, DD-180, DD-220, DD-240, DD-250, DD-340, DD-400, DD-410, DD-570 |
