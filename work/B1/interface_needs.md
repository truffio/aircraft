# B1 — Interface needs

What the L1 architecture (`specs/FUNCTIONAL_ANALYSIS.md` §3, §5) needs from the ICDs (task I1) and from the L2 agents (C1 to C7). Interface IDs I-nn refer to FUNCTIONAL_ANALYSIS §3.2.

## 1. ICDs

| ID | ICD | Need | Driven by |
| --- | --- | --- | --- |
| IN-B1-01 | **New: vehicle-model boundary** (proposed `icd/ICD-VM-FS.md`, or a section of ICD-AER-TST; I1 decides) | The only data between the vehicle model (DYN, FU, EF) and the flight software (FC, AF, NAV, TM): effector commands in; vehicle state, vehicle mass and fuel state out (I-05, I-06, I-09, I-10, I-12). Units SI, frames per CONVENTIONS, quaternion attitude (CV-250). | L1-AER-430, -440 |
| IN-B1-02 | ICD-AER-TST | Configuration in (vehicle parameter set, flight-control-law design, autoflight implementation, each with identifier and version); initial condition in (position, velocity, attitude, body rates, fuel mass, mode state, targets, VOR stations); simulation step command and wind velocity in; crew selections in, time-stamped; operational data out at `[P-TM-010]`; annunciations and indications out in crew-facing units (CV-760 group 4, with the SI value alongside); landing and crash events out; configuration identity out. Fix whether an input timestamped k first affects step k or k + 1 (CV-840). | L1-AER-480, -490, -550, -590 to -670 |
| IN-B1-03 | ICD-FC-AF | Six axis references (one per degree of freedom) and mode status; the same interface for every control-law design and autoflight implementation (D15). Which quantity each reference is (velocity, position, rate, attitude) is a joint C4/C5 decision. | L1-AER-370, -420 |
| IN-B1-04 | ICD-NAV-AF | Navigation quantities of L1-AER-530 and -540 with their validity flags (CV-580 thresholds); the selected VOR station and selected course from AF to NAV. | L1-AER-530, -540 |
| IN-B1-05 | All ICDs | Every signal carries its unit and frame; every record carries the CV-840 timestamp. | L1-AER-590, -730, -740 |
| IN-B1-06 | Evidence package (#73, deferred) | None now. Whether each operational data signal is releasable or protected is decided with the RVS (#69, G0-F22). L1-AER-630 carries the TBD. | L1-AER-630 |
| IN-B1-07 | ICD-AER-TST, MS-DYN | Is the uniform wind horizontal only, or may it have a vertical component? The upward authority budget (FUNCTIONAL_ANALYSIS §7.1) assumes horizontal wind. **Answered (D51, #99):** horizontal only; steady wind plus gusts, given by the TST with each step; record it and the gust shape in MS-DYN and the ICD. | L1-AER-120, -130; L0-ASM-050 |

## 2. To the L2 agents

| To | Need from L1 | L1 records |
| --- | --- | --- |
| C1 — DYN, MS-DYN | Rigid-body 6-DOF equations; the exclusion of coupling except the kinematic terms decided under #81; gravity `[P-DYN-010]` (standard gravity proposed); drag on the air-relative velocity with standard-atmosphere density; the closed list of forces; nose on +x_B; crew station `[P-DYN-400]`; sensed acceleration at the centre of gravity as an output (D45); ground contact classified against the landing envelope; one step per TST command; state at frame start, exact. | L1-AER-010 to -070, -240 to -290, -440, -640, -670, -720 |
| C2 — FU | Initial fuel from the initial condition, at most `[P-FU-010]`; translational and rotational consumption with configurable parameters `[P-FU-040]`, `[P-FU-050]` and the form stated in MS-DYN; vehicle mass = dry mass + remaining fuel; the fuel integral within `[P-FU-060]`; fixed CG; inertia at each fuel state; zero fuel → zero output (with EF); hover endurance budget (FUNCTIONAL_ANALYSIS §7.3); fuel indication and the two alerts (with TM). | L1-AER-100, -150 to -230, -290, -360, -560 to -580 |
| C3 — EF | Control forces and moments only from effectors; constant body-frame directions; parameters limited to five kinds; per-effector maximum force; pure forces `[P-SYS-400]`, `[P-SYS-410]` and moments `[P-SYS-420]` with the other components at zero; zero output at fuel exhaustion; command response time `[P-EF-010]`. The layout stays a design decision. | L1-AER-020, -040, -080 to -140, -200, -380, -710 |
| C4 — FC | Six-axis regulation from separate references; cross-axis tolerances `[P-SYS-540]`, `[P-SYS-550]`; level pitch and roll within `[P-AF-180]` under autoflight (with AF); crew limit at the centre of gravity, enforced as a force limit at the current mass; transient allowance `[P-FC-020]`; position share `[P-FC-010]`; control-law design from the configuration; control-loop latency. | L1-AER-110 to -140, -290, -300, -370 to -440, -460, -680, -710 |
| C5 — AF | Guidance through the catalogue modes; manoeuvre acceleration limit `[P-AF-200]` (D16); position guidance share `[P-AF-160]`; annunciation within `[P-SYS-470]` (AF share `[P-AF-060]`); crew selections as data, in crew-facing units; initial mode state; the envelope records; Q5 proposal (issues §4) as input to AF_MODE_LOGIC; the FCP question (#80.3, #79). | L1-AER-290, -300, -310 to -360, -390, -410, -420, -450 to -480, -500, -660, -680 |
| C6 — NAV | Altitude, horizontal speed, vertical speed, heading, track, flight path angle at each control frame; VOR radial, sense, course deviation and distance within `[P-NAV-050]`; stations from the TST; validity per CV-580. | L1-AER-340, -440, -450, -530 to -550, -640, -680 |
| C7 — TM | Annunciations and indications as crew-interface data, in crew-facing units; timestamps; output every `[P-TM-010]`; the four content records (crew inputs, mode states, control activity, vehicle responses); configuration identity; landing and crash events; fuel indication and alerts (with FU). Releasable/protected classification is deferred (#69). | L1-AER-260, -270, -470, -490, -500, -560 to -650 |
| All | Determinism: identical inputs on one host give identical operational data. | L1-AER-690 |

## 3. Needed by B1 from others

| From | Need | Why |
| --- | --- | --- |
| Project owner | Answers to B1-Q01 to B1-Q10 and the Q5 decision (#6) | `work/B1/issues.md` |
| I1 | Closure of the budgets in FUNCTIONAL_ANALYSIS §7 once the L2 values exist | METHODOLOGY §7 rule 4 |
| C1, C2 | Maximum vehicle mass and inertia, to compute `[P-SYS-400]` to `[P-SYS-420]` | L1-AER-120 to -140 |
