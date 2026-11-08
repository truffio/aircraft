# C7 — Issues, owner questions, change requests and design decisions (TM)

Task C7 (plan §6, Phase 3): the TM section of L2 (`work/C7/L2_TM.md`), the operational data output. Written at branch c1_c2, commit 55c6c29 (D1–D74). Questions are at L2 level: the operational data output. Local IDs C7-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 TM records | 31: Functional 20, Interface 5, Constraint 5, Performance 1 |
| Verification methods | Test 26, Inspection 3, Demonstration 2 |
| L1 parents covered | 10 of 10 L1 records allocated to TM (L1-AER-260, -270, -590 to -650, -690) |
| Derived records | 3: L2-AER-TM-020 (DD-C7-04), -150 (DD-C7-02), -610 (DD-C7-03) |
| Design decisions proposed | 5 (§4): DD-C7-01 to -05; two are choices inside non-derived records |
| L3 records | None: each TM record is a leaf; the next layer is the record format and encoding, which ICD-AER-TST and the design fix (D4) |
| Parameters | None new; P-TM-010 description refined (`param_proposals.md`) |
| Owner questions | 7 (§2) |
| Change requests | 4 (§3): L1-AER-620 (targets, indications), L1-AER-630 (landing gear command), glossary, FUNCTIONAL_ANALYSIS §7.5 and CV-830 (editorial) |
| Signal classification | Proposed per signal (§2, C7-Q01), not settled: 22 signal groups, of which 14 releasable (S-02 only if its identifiers are opaque), 6 protected, 1 split (S-16) and 1 protected unless the manual states the value (S-18a) |
| Lint | 0 errors, 12 COMPOUND warnings (judged in §6) |

**What the section does.** TM is an observer that records, at each output sample `[P-TM-010]`, the signals its sources define, and records crew selections, ground-contact events and the run's configuration as records of their own. It computes nothing new, feeds nothing back, and does not filter for release. The releasable/protected question (#69) is left to the owner with the RVS (D44). TM's share is that each signal can be released or withheld on its own (L2-AER-TM-020).

## 2. Questions for the project owner

Each question has a recommended answer. The records are written for the recommended answer; where another answer changes a record, the question says which.

### C7-Q01 — Releasable or protected: principle and per-signal proposal (#69)

**Question.** The classification of each operational data signal is decided with the RVS (#69, D44; TT-600). Can the owner accept a working principle and a per-signal proposal now, so that ICD-AER-TST can carry a proposed class from I1, with the decision itself still taken when the plan covers the RVS?

**Proposed principle.**

- **Releasable:** what the crew enters and sees (the crew interface), the motion and physical outcomes that an outside observer of the vehicle could record, and the opaque identity of the configuration. This matches REVERSE_ENGINEERING §3: observable behaviour (§3B) and the externally observable activity, states, commands and outputs of the vehicle (§3C).
- **Protected:** signals internal to the design (those that cross an internal interface: ICD-FC-AF, the FC-internal axis demands, the commands across the vehicle-model boundary), the design's own names and state variables, and values that give a design parameter directly when no operator document states it. Releasing these would expose the requirements or implementation, which REVERSE_ENGINEERING §3C and §7 forbid. Inferring them from releasable data is the reverse-engineering exercise itself, and is not a leak.

**Proposed classification.**

| ID | Signal | TM record | Source | Proposed | Reason |
| --- | --- | --- | --- | --- | --- |
| S-01 | Timestamps (step index, simulation time) | -100, -110, -120 | TM | Releasable | The common time base the RVS needs (N-390). It shows only the step and sample periods, which the data show anyway. |
| S-02 | Configuration record (identifiers, versions) | -700 | Run set-up | Releasable, if opaque | It lets the RVS tell its runs apart. Identifiers must not describe the design (for example a control-law type in a name); that rule goes in ICD-AER-TST (I1). |
| S-03 | Crew selection as received | -200 | FCP | Releasable | The RVS's own input (N-400). |
| S-04 | SI target passed to autoflight, or none | -210 | FCP | Releasable | The conversion uses public exact factors (CV-750). "None" shows only that the panel did not pass the selection, which the annunciations also show. |
| S-05 | Mode state | -300 | AF | **Protected** | It carries the design's mode names (glossary note on mode names) and may hold states that are not annunciated. It is the mode logic's own state variable, which is what the RVS is to infer (L0-SUC-100, -110). The annunciations (S-06) carry the same state as the crew sees it. Alternative: releasable if coded with the crew labels, in which case it repeats S-06. |
| S-06 | Annunciations presented | -310 | FCP | Releasable | What the crew sees: the main evidence of mode behaviour (N-210, N-380). |
| S-07 | Targets of the armed and active modes, SI | -320 | AF | **Protected** | They are internal guidance references. The captured altitude, the held position and the instant of capture are exactly what the RVS should infer. The selected targets are in S-06 in crew units already. |
| S-08 | Indications presented | -330 | FCP | Releasable | What the crew sees. |
| S-09 | Axis references | -400 | FC (from AF) | **Protected** | The split between guidance and regulation is design (ICD-FC-AF, D15). With S-10, the references give the structure and gains of the control law directly. |
| S-10 | Axis demands | -410 | FC | **Protected** | Internal to FC (I-11); they give the regulation law directly. |
| S-11 | Effector commands, activation state | -420 | FC | **Protected** | The output of the allocation. With S-12 they give the allocation rule and the command response model (DD-160). The off state on the ground shows in S-12 and S-13 (zero). |
| S-12 | Effector outputs | -430 | EF | Releasable | The physical actuator activity, the counterpart of the control-surface positions that a flight data recorder holds. They give the RVS the control activity that L0-OBJ-140 and REVERSE_ENGINEERING §3C intend it to have. They show the number of effectors, which is observing the vehicle, not reading its design. Alternative: protected, with the resultant control force and moment released instead (a new signal, needing a CR on L1-AER-630). |
| S-13 | Fuel mass flow | -440 | FU | Releasable | A quantity recorders normally hold (fuel flow); it can be derived from S-18b anyway. |
| S-14 | Landing gear command | -450 | AF | **Protected** | An internal command across the vehicle-model boundary. Its effect shows in the gear position (S-19) and its annunciation. |
| S-15 | Vehicle state | -500 | DYN | Releasable | Observable motion (REVERSE_ENGINEERING §3B). |
| S-16 | Navigation quantities: values / validity | -510 | NAV | **Split:** values releasable, validity protected | The values are motion. The validity flags expose the NAV thresholds (P-NAV-010, -030; CV-580), whose effect the crew sees in the indications (S-08). |
| S-17 | Sensed acceleration | -520 | DYN | Releasable | What the crew feels; recorders hold accelerations. |
| S-18a | Vehicle mass | -530 | FU | **Protected, unless** the operating manual states the empty mass | With S-18b it gives the dry mass [P-FU-030], a design parameter. If the manual states it, as aircraft manuals state the empty weight, release it. |
| S-18b | Remaining fuel mass | -530 | FU | Releasable | Indicated to the crew, in lb. |
| S-19 | Gear state | -540 | DYN | Releasable | The gear position is annunciated, and "on the ground" is the counterpart of a weight-on-gear signal. |
| S-20 | Event: classification, timestamp | -600, -120 | DYN | Releasable | The outcome of a contact is visible. |
| S-21 | Event: classification speeds, reported state | -610 | DYN | Releasable | Motion values at the contact. Finding the envelope limits from many contacts is reverse engineering, not a leak. |

**Recommended answer:** accept the principle and the table as the **working proposal**. I1 enters it in ICD-AER-TST as a "proposed class" column. TT-600 stays open, and the classification is decided when the plan is extended to the RVS (D44). Nothing in the requirements depends on it: L2-AER-TM-020 makes any classification applicable. Keep the two conditional items (S-12 and S-18a) open for the owner, because they depend on what the operating manuals will say.

**Affects.** ICD-AER-TST (I1); TT-600; L1-AER-630 TBD field; the TM records' TBD/TBR fields; the RVS branch.

### C7-Q02 — Who applies the classification

**Question.** When the RVS receives data, who removes the protected signals: the TST, when it assembles the release, or the Aeronef, through a "release" signal set chosen by the configuration?

| | Option A — outside the Aeronef (recommended) | Option B — a release mode in TM |
| --- | --- | --- |
| How | TM always outputs the full set. The TST, or the owner's release step, copies only the releasable signals into the released package (CONOPS SC-240: "an executable TST configuration that outputs releasable data only"). | A configuration item selects the full or the release signal set; TM omits the protected signals in release mode. |
| Basis | L0-CON-220 was deleted at G0: the system itself protects nothing, and the owner chooses what is released. | Would bring back an Aeronef protection function that the owner removed. |
| Effect on requirements | None: L2-AER-TM-020 (each signal separable) is enough. | L1-AER-630 and -640 ("at each output sample") would not hold in release mode, so a CR is needed. A second code path would have to be shown to behave identically (SC-240, L2-AER-TM-810). |

**Recommended answer: A**, with two additions for the RVS branch: (1) ICD-AER-TST, a protected document, records the decided class of each signal; (2) the released package includes a **releasable data dictionary** that names and describes each released signal in operator terms and crew-facing units where the crew sees them (N-380). It is written from ICD-AER-TST but is not ICD-AER-TST, because the ICD is protected design material. That dictionary is an operational-documentation deliverable (L1-AER-840 family) or an RVS-branch item (D44).

**Affects.** L2-AER-TM-020 (kept under A; under B replaced by a release-mode record and CRs on L1-AER-630, -640); IN-C7-43.

### C7-Q03 — Output sample period [P-TM-010]

**Question.** L1-AER-600 leaves [P-TM-010] TBR (TT-590, closes at G2 with C7); FUNCTIONAL_ANALYSIS §7.5 proposes it equal to the control frame period. What should it be?

| | Option S1 — equal to [P-SYS-310], 0.02 s (recommended) | Option S2 — equal to [P-SYS-300], 0.01 s | Option S3 — a multiple of the frame, for example 0.1 s |
| --- | --- | --- | --- |
| What is seen | Every control frame: each mode change, each new command, each target at the frame where it happens | Every step, including the effector lag inside a frame | Mode states that last less than one sample can be missed |
| L2-AER-TM-150 (multiple of the frame) | Holds | Fails: half the samples fall in mid-frame; -150 would be deleted | Holds |
| Annunciation latency budget | FCP share [P-TM-010] = 0.02 s of [P-SYS-470] = 0.5 s (FA §7.5) | Same, smaller | 0.1 s of 0.5 s |
| Volume | About 100 values per sample: about 1.4 million samples, of the order of 1 GB uncompressed, for an 8 h run | Twice S1 | One fifth of S1 |
| Analyses that need each step | Use the TST per-step recording (IN-C1-26, IN-C2-30, IN-C3-31) | Still need it for the vehicle-model inputs of the previous step | Same as S1 |

**Recommended answer: S1.** [P-TM-010] is defined as equal to [P-SYS-310]; its value follows [P-SYS-310] and stays TBR until [P-SYS-310] is set at I1 (TT-070). TT-590 merges into TT-070. The per-step needs of the analyses stay with the TST recording, which is not operational data.

**Affects.** P-TM-010 (`param_proposals.md`); L2-AER-TM-140, -150, -300; TT-590, TT-070.

### C7-Q04 — Targets of the active and armed modes, and the indications (CR-C7-01)

**Question.** L1-AER-620 records the armed and active modes and the annunciations. It records neither the SI targets that the modes fly nor the indications. Should both be added?

- **Targets.** The tests of captures and holds need the target in SI: the captured altitude, the position held by Stationary and Hover (L1-AER-460's reference position) and the heading held. The annunciations show the selected targets only, in crew units at display resolution, and a target that autoflight sets is not a crew selection, so L1-AER-610 does not record it either. Without it the TST would have to assess against its own guess of the capture instant, which depends on the design.
- **Indications.** CONOPS §4.6 lists the annunciations *and indications* in the operational data, and FUNCTIONAL_ANALYSIS I-38 carries the presentation to TM, but L1-AER-620 does not. The SI quantities are already in L1-AER-640. The indications add what the crew actually saw (rounding, behaviour while a quantity is not valid).

**Recommended answer: yes to both (CR-C7-01).** L2-AER-TM-320 and -330 are written for it. An acceptable alternative for the indications alone: the TST records the crew interface output (I-42) itself. Then CR-C7-01 drops "and indications" and L2-AER-TM-330 is deleted. The targets part stays in either case.

**Affects.** L1-AER-620 v2; L2-AER-TM-320, -330; C5 (AF gives the targets, IN-C7-30), C8 (IN-C7-11).

### C7-Q05 — Landing gear command in the operational data (CR-C7-02)

**Question.** The children of L1-AER-910 must show that "after each change of the gear command in flight" the gear is in transit and then in the commanded position within [P-DYN-050]. The operational data hold the gear state but not the command, and the per-step recording IN-C1-26 does not list the command either. Should the landing gear command be added to L1-AER-630 (control activity), with AF added to that record's allocation?

**Recommended answer: yes (CR-C7-02).** The command is the cause and the gear state the effect: without it the test infers the command instant from the mode state, which depends on the design. AF already gives TM its outputs (FUNCTIONAL_ANALYSIS I-34). Alternative: add the command to the TST per-step recording only (IN-C7-03) and leave L1-AER-630 unchanged; then L2-AER-TM-450 is deleted. IN-C7-03 is recommended in either case.

**Affects.** L1-AER-630 v2 (statement, allocation); FUNCTIONAL_ANALYSIS §6.2 (AF count 25 → 26) and §3.3; L2-AER-TM-450; C5 (IN-C7-30).

### C7-Q06 — Fuel alerts: annunciations, not event records (CR-C7-03)

**Question.** The glossary *Event record* includes "a fuel alert", and IN-C2-33 left it to TM. L1-AER-640 lists only the landing and crash events (closed list). Should the low-fuel alert and fuel exhaustion also be event records?

**Recommended answer: no.** They are annunciations (LOW FUEL, FUEL EXHAUSTED), recorded at each output sample (L2-AER-TM-310), and the latency [P-SYS-470] is measured on samples (CV-860). The step-exact FU tests use the per-step recording (IN-C2-30). A fuel-alert event would duplicate the annunciation with no L1 parent. CR-C7-03 removes "or a fuel alert" from the glossary *Event record*. Alternative: event records at the step at which FU sets each indication; this needs a derived TM record, a new FU output to TM, and a CR adding them to L1-AER-640.

**Affects.** GLOSSARY *Event record* (CR-C7-03); L2-AER-TM-600, -310; IN-C2-33 answer.

### C7-Q07 — The contact values in the event record (DD-C7-03)

**Question.** The contact step usually falls between two output samples, and a crash ends the run, often before the next sample. A landing reports the rest state at the contact step (zero velocity, L2-AER-DYN-560), so even a sample at that step would not show the speeds by which the contact was classified. Should each event record carry the classification speeds (vertical and horizontal speed of the propagated state) and the vehicle state and gear state reported for the contact step?

| | Option E1 — values in the event record (recommended) | Option E2 — an extra output sample at each contact step | Option E3 — nothing; the TST per-step recording only |
| --- | --- | --- | --- |
| L1-AER-600 | Unchanged | The spacing "every [P-TM-010]" breaks; CR needed | Unchanged |
| Classification speeds | In the record | Not shown for a landing (rest state) | In the TST recording only |
| RVS (no per-step recording) | Sees each contact with its speeds | Sees the state, not the speeds of a landing | Sees a crash without its speed |
| DYN change | Gives the two speeds with the event (IN-C7-01) | None | None |

**Recommended answer: E1** (L2-AER-TM-610, Derived, DD-C7-03). If C1 does not add the speeds to the event output, -610 keeps only the reported state and gear state.

**Affects.** L2-AER-TM-610; L2-AER-DYN-530 content (IN-C7-01); DD-C7-03.

## 3. Change requests

| ID | Against | Requested change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-C7-01 | L1-AER-620 (Statement, Rationale, children must show); FUNCTIONAL_ANALYSIS §6.2 row text | Statement: "The Aeronef shall record in its operational data, at each output sample, the armed and active autoflight modes, their targets, and the annunciations and indications presented to the crew." Add to the children-must-show: "(Test) the target of each armed and active mode is present in SI at each output sample, and the annunciations and indications recorded equal the crew interface output of the same sample." Rationale: cite CONOPS §4.6 and FA I-38 for the indications, and L1-AER-460 and the capture tests for the targets. Allocation unchanged (TM, AF, FCP). Version 1 → 2. | The TST needs the SI targets that the modes fly; the indications are in CONOPS §4.6 and FA I-38 but not in L1 (C7-Q04). | Proposed |
| CR-C7-02 | L1-AER-630 (Statement, Allocated to); FUNCTIONAL_ANALYSIS §6.2 (row and counts), §3.3 (AF → TM cell) | Statement: "… the axis references, the axis demands, the effector commands, the landing gear command, the effector outputs and the fuel mass flow." Allocated to: TM, FC, EF, FU → TM, FC, EF, FU, AF. Rationale: the gear command is the cause of the gear state that L1-AER-910's children assess; it crosses the vehicle-model boundary (L1-AER-430). Version 1 → 2. FA §6.2: tick AF in the row; AF count 25 → 26. FA §3.3: AF → TM "× modes, targets, gear command". | L1-AER-910 cannot be shown from the operational data without the command (C7-Q05). | Proposed |
| CR-C7-03 | GLOSSARY *Operational data*, *Event record*, *Output sample* (Fixed, D43) | As in `work/C7/glossary_proposals.md` §2. | *Operational data* says "at each output sample" for every signal, but crew selection and event records are separate record kinds (L1-AER-590). *Event record* includes fuel alerts, which L1-AER-640 does not (C7-Q06). *Output sample* needs the sample step and the instant its values stand for (L2-AER-TM-130). | Proposed |
| CR-C7-04 | FUNCTIONAL_ANALYSIS §7.5 (P-TM-010 row); CONVENTIONS CV-830 last sentence (editorial) | FA §7.5: "Integer multiple of [P-SYS-300]; proposed equal to [P-SYS-310] so each frame is recorded" → "Integer multiple of [P-SYS-310], so of [P-SYS-300], with the first output sample at step 0 (L2-AER-TM-140, -150; DD-C7-02); equal to [P-SYS-310] (C7-Q03)". CV-830: "Whether these periods equal the simulation step or are integer multiples of it is an ICD-AER-TST matter." → "Their relation to the simulation step is set by L1-AER-680 (control frame) and L2-AER-TM-150 (output sample)." | The requirements now fix what CV-830 left to the ICD. | Proposed (editorial) |

No L1 record allocated to TM is unsatisfiable: no corrective CR is needed for the ten parents. L1-AER-600's rationale ("an integer multiple of the simulation step … proposed equal to the control frame period") is consistent with L2-AER-TM-150 and needs no change.

## 4. Design decisions proposed

Local IDs; I1 registers them in `registers/DECISIONS.md` (next free numbers after DD-200 and the pending C1 proposals).

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-C7-01 | An output sample of step k holds, for each signal, the value that its source gives for step k (vehicle state with the MS-DYN §3.4 accelerations; effector outputs, fuel mass flow and masses of step k, held over the step from t_k to t_(k+1)), and, for a flight software signal, the value of the control frame that contains step k. No interpolation, filtering or re-sampling. | The latest value available when TM runs (depends on execution order); the effector outputs and flow of the step that ends at t_k (what produced the state); interpolation to t_k. | One definition per signal, taken from its source (MS-DYN §3.4, §10.2, DD-080, DD-100); deterministic (L1-AER-690); with DD-C7-02 a sample holds the state, the decisions computed from it and the response over the next step on one record. | — (choice inside L2-AER-TM-130) |
| DD-C7-02 | [P-TM-010] is an integer multiple of [P-SYS-310], with the first output sample at step 0, so each sample step is the first step of a control frame. Proposed equal. | An integer multiple of [P-SYS-300] only (L1-AER-600 as written); an independent period. | A sample in mid-frame would hold flight software values computed from an earlier state, and record mode changes with a varying offset. | L2-AER-TM-150 |
| DD-C7-03 | Each event record carries the vertical and horizontal speed of the propagated state by which the contact was classified, and the vehicle state and gear state reported for the contact step. | An extra output sample at the contact step; nothing beyond classification and timestamp (TST per-step recording only). | The contact step is usually between samples, and a crash ends the run; a landing reports zero velocity at the contact step; L1-AER-600's spacing is kept (C7-Q07). | L2-AER-TM-610 |
| DD-C7-04 | Each signal is a separate, named data item of ICD-AER-TST, readable without any other signal of its record; a release of the operational data is a subset of the signals, assembled outside the Aeronef. | A release mode in TM selected by the configuration (C7-Q02 B); packed or encoded records that need the full set to decode. | L0-CON-220 deleted (the system protects nothing); any classification of #69 can then be applied without changing the Aeronef, and the released Aeronef behaves as the protected one (SC-240). | L2-AER-TM-020 |
| DD-C7-05 | The crew selection record holds the SI target that the flight control panel passes to autoflight, or "none"; TM does not recompute the conversion. | TM converts the selected value itself; record only the selections that the panel passes. | What crosses ICD-FCP is what autoflight flies; a recomputation could differ from it (range, resolution) and hide a panel defect; an ignored selection is behaviour too. | — (choice inside L2-AER-TM-210) |

## 5. Other findings and notes for I1

1. **Conflicts found and their disposition.** (a) Glossary *Event record* includes fuel alerts, L1-AER-640 does not: CR-C7-03, C7-Q06. (b) Glossary *Operational data* says every signal is at an output sample: CR-C7-03. (c) CONOPS §4.6 lists the indications in the operational data, L1-AER-620 does not: CR-C7-01. (d) CV-830 leaves the period relations to the ICD: CR-C7-04. (e) L1-AER-910's evidence needs the gear command, which neither the operational data nor IN-C1-26 holds: CR-C7-02, IN-C7-03. (f) L1-AER-280's contact tests need the propagated speeds, but a landing reports the rest state: IN-C7-01, DD-C7-03.
2. **Last sample of a run.** A sample of step k is complete once the TST commands the step from k (the effector outputs and flow of step k, and the accelerations of step 0, IN-C1-38). When a crash ends the run at a contact step, the operational data end with the event record (and its contact values) and the last complete sample before it. ICD-AER-TST states this (IN-C7-42).
3. **TM is not the per-step recording.** IN-C1-26, IN-C2-30 and IN-C3-31 ask the TST for per-step records of the vehicle-model interfaces. They are not operational data and TM does not provide them. The TM tests also need a recording of the flight software interfaces of the same kind (IN-C7-40). Both are TST items for when the plan covers the TST (D44).
4. **Data volume.** About 100 values per sample at S1 (C7-Q03): an 8 h reference mission gives about 1.4 million samples, of the order of 1 GB uncompressed. No long hover run is required (D72, D74).
5. **The effectors-off state** is visible in the effector commands (activation state) and outputs; no new signal is needed (B3 impact list, C7).
6. **Run start.** The first output sample (step zero) reports the initial condition (L1-AER-660, -950 children); the configuration record precedes it (L2-AER-TM-700).
7. **L1-AER-610 and -620 are shared with AF and FCP.** Their AF and FCP children (C5, C8) give TM the selections, targets, mode state and annunciations (IN-C7-10, -11, -30); TM's children record them.

## 6. Self-check (METHODOLOGY 13.1, 13.2)

**13.1, each record:**

- [x] One "shall", one subject (the operational data output), one thought. The 12 COMPOUND warnings are judged as follows. -010: a closed list of the record kinds. -030: one property over the pair of replaceable designs. -130: one rule with its two source kinds (vehicle model per step, flight software per frame). -140: one sample grid, step zero and its multiples. -210: the two outcomes of one item (a target or none). -320: one set (armed and active modes). -530: a pair of FU outputs of the same step. -600: the value set of the classification. -610: a closed list of contact values. -700: a closed list of three identities. -800: a closed list of inputs. -810: one prohibition with two receivers. None is a tree of cases (D30).
- [x] The subject is the element at this level, never a person.
- [x] EARS pattern: ubiquitous (-010 to -150, -210 to -540, -610, -800, -810), event-driven (-200, -600, -700). Conditions are explicit: the sample step, the control frame, the contact step, the start of the run.
- [x] Every quantity is a parameter ID or a unit named in the success criteria; there is no number in a statement (lint).
- [x] No vague terms, escape clauses, open lists or absolutes (lint).
- [x] Solution-free: the record format, encoding and transport are left to ICD-AER-TST and the design. The sampling rule and separability are justified as DD-C7-01 to -04.
- [x] Terms are in the glossary or proposed (`glossary_proposals.md`: *Operational data output*, *Crew selection record*, *Configuration record*, *Signal*, *Sample step*). Axes and units follow CONVENTIONS (CV-310, CV-320, CV-720, CV-740, CV-760 group 4).
- [x] Rationale, parent (or Derived with a DD) and source are on each record, with a sufficiency argument for each parent.
- [x] Verification method, procedure ID and success criteria are on each record.
- [x] Criticality is "Not assessed"; each TBD/TBR item has an owner and a closure.

**13.2, the set:**

- [x] Each of the 10 L1 parents is covered, with a sufficiency argument (coverage table at the head of the section).
- [x] No duplicates or conflicts inside TM. The source-side records (L2-AER-DYN-350, -530, FU-250, -260, EF-410) say what each source gives; the TM records say what TM records. Each pair is consistent: same signal, same step, same unit.
- [x] Types considered: functional, performance, interface, constraint. Model fidelity does not apply (TM computes no physics). Documentation is not needed (ICD-AER-TST is I1's). Failure handling is deferred (tailoring).
- [n/a] Hazard rows and fault injection: deferred (tailoring).
- [x] Interfaces: each TM input has a source record (DYN, FU, EF) or a need on the source agent (FC, AF, FCP, NAV: `interface_needs.md`); the output is ICD-AER-TST (IN-C7-41).
- [x] Three Derived records (-020, -150, -610), for review at the parent level, with DD proposals.
- [x] Trace checks: expected results below.
- [n/a] Manual sections: none yet. The releasable data dictionary (C7-Q02) is a future documentation item.

## 7. Check results (scratch copy outside the worktree, the draft assembled into L2)

| Check | Result | Meaning |
| --- | --- | --- |
| `lint.py --file work/C7/L2_TM.md` | 0 errors, 12 warnings (COMPOUND) | Judged in §6 |
| `trace_check.py` (draft assembled) | 20 errors: 17 CHILDLESS, 3 DERIVED | CHILDLESS: L1 records allocated only to FC, AF, FCP and NAV (C4, C5, C6, C8 pending); none of the ten TM parents is childless. DERIVED: DD-C7-02, -03, -04 are not yet in the register; they clear when I1 registers them. |
| `param_check.py` (draft assembled) | 0 errors, 15 warnings | Pre-existing PARAM-UNUSED on AF, NAV parameters and P-SYS-290. P-TM-020 to -050 are no longer unused: L2-AER-TM-320 and -330 cite them. |

The scratch assembly also rewrote the DYN, FU and EF sections, but the differences are line endings only (CRLF in `requirements/L2.md`, LF in the drafts).
