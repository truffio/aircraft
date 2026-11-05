# A3 — Interface needs

CONVENTIONS.md and GLOSSARY.md provide definitions to every subsystem. This file lists what the conventions expect each downstream artifact to carry, and what A3 needs from others.

## Provided by A3 (to be adopted downstream)

| To | Need | Conventions |
| --- | --- | --- |
| MS-DYN (C1) | Use frames L, V and B, NED and FRD, the flat non-rotating world, uniform gravity along `+z_L`, the quaternion convention, the inertia-tensor sign and the air-relative velocity for drag | CV-110 to CV-190, CV-250, CV-350, CV-470 |
| FU (C2) | Mass properties about the CG in body axes; fuel quantity as mass in kg; product-of-inertia sign | CV-340, CV-350 |
| EF (C3) | Effector direction vectors in B; positive output along `+d_i`; force and moment components and signs | CV-310 to CV-330 |
| FC (C4) | Body force, moment and rate signs; Euler-rate versus body-rate distinction; attitude independent of motion | CV-280, CV-290, CV-310, CV-320, CV-970 |
| AF (C5, Phase 4) | Definitions of altitude, vertical speed, horizontal speed, heading, track, flight path angle, course deviation; error sign; angle differencing; bound inclusivity; response-time measurement; crew-unit rule and exact conversion of selections | CV-4xx, CV-5xx, CV-6xx, CV-760, CV-770, CV-860, CV-910 to CV-940 |
| NAV (C6) | Computation definitions for all navigation quantities and VOR geometry; validity conditions and their parameters | CV-4xx, CV-5xx, CV-6xx, CV-580 |
| TM (C7) | Timestamps (step index authoritative); SI signals; optional crew-unit copies of selected or shown values with explicit units; display resolution parameters | CV-760, CV-780, CV-840 |
| ICD-AER-TST (I1) | State vector in SI: position in L, velocity in V (NED) and B, attitude quaternion with derived Euler angles, body rates; step index and simulation time on every sample; latency convention (input at step k affects state at k or k+1) to be fixed there | CV-250, CV-410, CV-460, CV-280, CV-840 |
| TST (out of scope, via ICD) | Any graphics or user-interface frame (for example y-up) is converted at the TST side of the boundary; the Aeronef side stays NED | §0 Scope, §2.1 |
| Parameter database (B2) | A field marking crew-facing parameters and their crew unit, if G0-10 is adopted | CV-790 |
| L0 assumptions register (A1) | Assumptions to record: still air (no wind), flat world, perfect state knowledge already planned | CV-110, CV-470 |

## Needed by A3

| From | Need | Why |
| --- | --- | --- |
| A2 (ConOps) | Whether scenarios start airborne or on a surface, and whether any scenario needs a ground | Decides whether CV-420 needs a ground surface (issue A3-Q06) |
| C5 (AF mode logic) | Final definitions of armed, active, engaged, capture, disengagement | Glossary entries marked TBR (C5) |
| C6 (NAV) | VOR reception-range geometry (horizontal or slant), TO/FROM ambiguity band, overhead behaviour | CV-640, CV-670 |
| Project owner | Answers to Q2–Q5 and to A3-Q01 to A3-Q14 | TBR items in CONVENTIONS and GLOSSARY |
