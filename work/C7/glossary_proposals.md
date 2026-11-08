# C7 — Glossary proposals (TM)

Proposals for `specs/GLOSSARY.md` from task C7. New terms need no change request. Changed definitions of Fixed terms do (D43): C7 proposes **CR-C7-03** for the refinements in §2 (`work/C7/issues.md`).

## 1. New terms

| Term | Definition | Source |
| --- | --- | --- |
| Operational data output | The Aeronef subsystem TM. It records, with their *timestamps*, the *signals* that the other subsystems give it, and gives the *operational data* to the TST. It observes and feeds nothing back to the *vehicle model* or the *flight software*. The subject of the TM requirements. | Plan §3, §6 C7; FUNCTIONAL_ANALYSIS F-AER-11, §5.2 |
| Signal | One named data item of the *operational data*, defined in ICD-AER-TST with its unit or its set of values, and readable without any other signal (L2-AER-TM-020). Each signal is classified *releasable* or *protected* with the RVS (#69, D44). | L1-AER-630, -640; L2-AER-TM-020 |
| Sample step | A *simulation step* at which an *output sample* is taken: step zero and each step whose *simulation time* is a whole multiple of `[P-TM-010]`. Each sample step is the first step of a *control frame* (L2-AER-TM-150). | L2-AER-TM-140, -150; CV-830 |
| Crew selection record | The record of the *operational data* that TM outputs for each *crew selection* the *flight control panel* receives. It holds the selection as received, with its *selected value* in its crew-facing unit, the *timestamp* of the selection, and the SI *target* that the panel passes to autoflight from it, or the indication that the panel passes none. Distinct from the *crew selection*, the data item of the *crew interface*. | L1-AER-590, -610; L2-AER-TM-110, -200, -210 |
| Configuration record | The record of the *operational data* that TM outputs once per run, before the first *output sample*. It holds the identifier and version of the *vehicle parameter set*, the *flight-control-law design* and the *autoflight implementation* of the run's *configuration*. | L1-AER-650; L2-AER-TM-700 |

## 2. Refined definitions (CR-C7-03)

| Term | Current | Proposed | Reason |
| --- | --- | --- | --- |
| Operational data | "Signals the Aeronef outputs, at each *output sample*, describing its externally observable activity: *crew selections*, *targets*, *armed* and *active* modes, *annunciations*, control activity and *vehicle states*. Whether each signal is *releasable* or *protected* is decided with the RVS (#69, D44)." | "The records the Aeronef outputs to the TST during a run, describing its externally observable activity: the *output samples*, the *crew selection records*, the *event records* and the *configuration record*. Together they relate the crew selections and their *targets*, the *armed* and *active* modes, the *annunciations* and *indications*, the control activity and the *vehicle states* in time. Whether each *signal* is *releasable* or *protected* is decided with the RVS (#69, D44)." | Crew selection records and event records are not at an output sample (L1-AER-590, L2-AER-TM-010); the indications follow CR-C7-01. |
| Event record | "A time-stamped record of a discrete event in the *operational data*: a *ground contact* classified as a *landing* or a *crash*, or a fuel alert." | "A time-stamped record in the *operational data* of a *ground contact* classified as a *landing* or a *crash*, at its *contact step*, with the speeds by which it was classified and the state reported for that step (L2-AER-TM-600, -610). The fuel alerts are *annunciations*, recorded in the *output samples*." | L1-AER-640 lists only landing and crash events (closed list); C7-Q06; DD-490. |
| Output sample | "One record of *operational data*. Its period is a parameter." | "One record of *operational data*, taken at a *sample step* every `[P-TM-010]`. It holds, for each sampled *signal*, the value its source gives for that step, or, for a *flight software* signal, for the *control frame* that contains that step (L2-AER-TM-130)." | The instant a sample stands for (DD-470) and the sample grid (L2-AER-TM-140). |
