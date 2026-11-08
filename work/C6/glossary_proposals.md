# C6 — Glossary proposals (NAV)

Proposals for `specs/GLOSSARY.md` from task C6. New terms need no change request; changed definitions of Fixed terms do (D43): C6 proposes the refinements in §2 under **CR-C6-01** and **CR-C6-03** (`work/C6/issues.md`).

## 1. New terms

| Term | Definition | Source |
| --- | --- | --- |
| Navigation subsystem | The Aeronef subsystem NAV, part of the *flight software*. At each *control frame* it computes the *navigation quantities* from the *frame-start state* and gives them, with their *validity*, to autoflight, the *flight control panel* and the *operational data*. The subject of the NAV requirements. | Plan §3, §6 C6; FUNCTIONAL_ANALYSIS F-AER-09 |
| Frame-start state | The *vehicle state* of the first *simulation step* of a *control frame*, which the vehicle model gives to navigation and flight control at the start of that frame (L1-AER-440). | L1-AER-440; L2-AER-DYN-330 |
| Validity (of a navigation quantity) | A flag that goes with each *navigation quantity*: *valid* when the quantity is defined and usable at the *frame-start state*, *invalid* otherwise. The *track* and the *heading* are valid inside their *validity range* (CV-580); the other navigation quantities are valid at each control frame. | CV-580; L1-AER-890; L2-AER-NAV-100 to -150 |
| Tumbling test run | A NAV test run that starts airborne, well above the ground, with zero fuel, level attitude and a pitch rate, so that the vehicle falls while its pitch angle passes through its whole range. Used to exercise the heading validity. | L2-AER-NAV-020, -120, -130; D73 (B3-1) |

The last entry is a verification term; I1 may keep it in the verification plan instead of the glossary.

## 2. Refined definitions

| Term | Current | Proposed | CR |
| --- | --- | --- | --- |
| Navigation quantities | "The quantities the navigation subsystem computes from the *vehicle state* at each control frame: *altitude*, *height above the ground*, *horizontal speed*, *vertical speed*, *heading* and *track*, each with its validity (CV-580)." | "The quantities the *navigation subsystem* computes from the *frame-start state* at each control frame: *altitude*, *height above the ground*, *horizontal position*, *horizontal speed*, *vertical speed*, *heading* and *track*, each with its *validity* (CV-580). In SI." | CR-C6-01 |
| Navigation | "The Aeronef subsystem (NAV) that provides *position*, *altitude*, *height above the ground*, *heading*, *track*, *horizontal speed* and *vertical speed* to autoflight and to the *flight control panel*." | "The Aeronef subsystem (NAV) that computes the *navigation quantities* (*altitude*, *height above the ground*, *horizontal position*, *horizontal speed*, *vertical speed*, *heading* and *track*) from the *vehicle state*, with their *validity*, for autoflight, the *flight control panel* and the *operational data*. See *Navigation subsystem*." (The current text names "position"; the proposal names the horizontal position, since the altitude is the vertical one, CV-410.) | CR-C6-03 |
| Validity range | "The states in which a direction quantity is defined and used, bounded by the CV-580 thresholds `[P-NAV-010]` and `[P-NAV-030]`." | "The states in which a direction quantity is valid: for the *track*, a *horizontal speed* of at least `[P-NAV-010]`; for the *heading*, a pitch angle magnitude of at most `[P-NAV-030]` (CV-580, both inclusive)." | CR-C6-03 |
| Vehicle parameter set | "The values of the *vehicle model* parameters used in a run, identified by a version." | If C6-Q06 is answered as recommended: "The values of the *vehicle model* parameters and of the navigation parameters used in a run, identified by a version." | CR-C6-03 (conditional) |

## 3. Terms used and already defined

*Altitude*, *Height above the ground*, *Horizontal position* (under *Position*), *Horizontal speed*, *Vertical speed*, *Heading*, *Track*, *Direction angle*, *Control frame*, *Vehicle state*, *Vehicle-model boundary*, *Flight software*, *Indication*, *Reference position*, *Operational data*, *Output sample*, *Vehicle parameter set*. No airliner term of CV-960's excluded list is used.
