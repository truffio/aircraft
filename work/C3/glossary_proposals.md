# C3 — Glossary proposals (EF)

Proposals for `specs/GLOSSARY.md` from task C3. New terms need no change request; changed definitions of Fixed terms do (D43): C3 proposes **CR-C3-03** for the refinements in §2 (`work/C3/issues.md`).

## 1. New terms

| Term | Definition | Source |
| --- | --- | --- |
| Effector subsystem | The Aeronef subsystem EF, part of the *vehicle model*: the set of *effectors*. At each *simulation step* it turns the *effector commands* into *effector outputs* and sums them into the *control force* and *control moment*. Specified by the *effector model* of MS-DYN. The subject of the EF requirements. | Plan §3, §6 C3; FUNCTIONAL_ANALYSIS F-AER-01 |
| Effector activation state | The state, *on* or *off*, of the *effector subsystem* that the *flight software* sets with the *effector commands*. While it is off, each *effector output* is zero, so no fuel is used. Off before the first effector commands of a run. | D69; DD-C3-04; L2-AER-EF-210 |
| Point of application | The fixed body-frame position, measured from the *centre of gravity*, through which an *effector* acts. With the *direction of action* it gives the *control effectiveness*. | L1-AER-100; DD-C3-01 |
| Direction of action | The fixed unit vector in the *body frame* along which an *effector* acts; a positive output acts along it. | CV-330; L1-AER-090 |
| Clipped command | An *effector command* brought within the *output limits* of its effector: the command itself when it lies within them, otherwise the limit it exceeds. | MS-DYN effector model; L2-AER-EF-110, -340 |
| Authority box | The set of *control force* and *control moment* combinations whose force components along the body x and y axes are within `[P-SYS-410]`, whose body z component lies from minus `[P-SYS-400]` to `[P-SYS-410]`, and whose moment about each body axis is within `[P-SYS-420]`. The *effector subsystem* can produce each of them together. | L2-AER-EF-330; DD-C3-03 |
| Achievable set | The set of *control force* and *control moment* combinations that the *effector subsystem* can produce with each *effector output* within its *output limits*, while fuel is available and the effectors are on. | MS-DYN effector model |

## 2. Refined definitions (CR-C3-03)

| Term | Current | Proposed |
| --- | --- | --- |
| Effector | "A fictional force or moment emitter that acts along a fixed direction in the *body frame* …" | "A fictional force emitter that acts along a fixed *direction of action* through a fixed *point of application* in the *body frame* and produces a variable output on command, consuming fuel (DD-C3-01). …" (rest unchanged). Reason: every effector is a force effector (L0-CON-060, -300); its moment comes from its moment arm. |
| Effector command | "The value that *flight control* sends to one *effector* for a *control frame*." | "The force, in N along its *direction of action*, that *flight control* asks of one *effector* for a *control frame*. The effector commands of a frame are one per effector plus the *effector activation state*." |
| Effector output | "The force or moment one *effector* produces along its fixed direction at a *simulation step*." | "The force, in N along its *direction of action*, that one *effector* produces at a *simulation step*, held over that step. It follows the *clipped command* through the *command response*, and is zero while fuel is not available or the effectors are off." |
| Control effectiveness | "… that one *effector* produces per unit of its *effector command*. …" | "… that one *effector* produces per newton of its *effector output*: the *direction of action* for the force and the cross product of the *point of application* with it for the moment. …" Reason: command and output differ during the response; the effectiveness is per unit output. |
| Command response | "The time behaviour of an *effector output* after a change of its *effector command*, including its response time `[P-EF-010]`." | "The time behaviour of an *effector output* after a change of its *effector command*: a first-order lag of time constant `[P-EF-020]` on the *clipped command* (DD-C3-02), which must reach the command within `[P-EF-010]`, to the band `[P-EF-030]`." |
| Output limits | "The smallest and largest *effector output* of one *effector*, including its maximum force magnitude (L0-CON-300)." | "The smallest output `[P-EF-130]` and the largest output `[P-EF-120]` of one *effector*; the largest is its maximum force magnitude (L0-CON-300). Zero lies within them." |
| Fuel availability | "… While fuel is not available, the effectors produce no output. …" | unchanged; add "(L2-AER-EF-200)". |
