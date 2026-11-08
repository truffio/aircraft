# C7 — Parameter proposals (TM)

Proposals for `parameters/PARAMETERS.yaml` from task C7 (TM). The orchestrator merges them; C7 does not edit the database.

**No new parameter.** The TM records need no value of their own: TM records the signals its sources define, and the only TM quantity is the output sample period [P-TM-010]. The records also cite P-SYS-300, -310, -450, -470, -500, -510, P-DYN-010, -050 and P-TM-020 to -050, all existing, in their success criteria or rationale. With L2-AER-TM-320 and -330, P-TM-020 to -050 are no longer reported as PARAM-UNUSED.

**P-TM number blocks proposed.** 010 output sampling; 020–050 display resolutions (owned by FCP, D55; the IDs keep their TM prefix because CV-780 cites them); 060, 070 withdrawn (D56), never reused; 080–990 free.

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-TM-010 | Description: "Period of one operational data record" → "Period of the output samples of the operational data. An integer multiple of P-SYS-310 (L2-AER-TM-150), so of P-SYS-300; one output sample at step 0 and one at each step whose simulation time is a whole multiple of P-TM-010 (L2-AER-TM-140)." Value unchanged (0.02 s), status unchanged (TBR). Note added. Source extended. | DD-480; C7-Q03 recommends that P-TM-010 equal P-SYS-310, so that its value follows P-SYS-310. |
| P-TM-020 to P-TM-050 | Source: add "L2-AER-TM-320, -330". No other change. | Cited by the TM records of the targets and the indications (CR-C7-01). |

**TBD/TBR register.** TT-590 (the L1-AER-600 field, "P-TM-010 value TBR … G2 (C7)"): C7 proposes no value of its own. P-TM-010 is defined as equal to P-SYS-310 (C7-Q03), so TT-590 merges into TT-070 (the timing budget, G2 (I1)). The L1-AER-600 field keeps its text until the next change of that record. No new TT row is needed for parameters. The TM records also open these items: the classification (TT-600, existing), the ICDs (TT-680, existing), DD-470 to -05 (proposed, G2) and CR-C7-01 to -04 (proposed, G2). The orchestrator decides whether DDs and CRs get TT rows.

## 2. YAML block

```yaml
  # --- TM (C7: description, note and source refined; value and status unchanged) ---
  - id: P-TM-010
    name: Output sample period
    description: Period of the output samples of the operational data. An integer multiple of P-SYS-310 (L2-AER-TM-150), so of P-SYS-300; one output sample at step 0 and one at each simulation step whose simulation time is a whole multiple of P-TM-010 (L2-AER-TM-140). Each output sample is then taken at the first step of a control frame.
    unit: s
    value: 0.02
    tolerance: null
    note: 'C7 (C7-Q03, DD-480). Equal to P-SYS-310, so that each control frame is recorded; the value follows P-SYS-310. A period equal to P-SYS-300 would put half the samples in mid-frame and is not allowed by L2-AER-TM-150. The per-step data that analyses need come from the TST recording of the vehicle-model interfaces, not from the operational data. FCP share of P-SYS-470 (FUNCTIONAL_ANALYSIS §7.5).'
    status: TBR
    source: CV-830; L1-AER-470, -600; L2-AER-TM-140, -150; DD-480; B1 proposal (equal to P-SYS-310); C7 proposal
    owner: Martin
```

For P-TM-020 to P-TM-050, only the `source` field changes: append `; L2-AER-TM-320, -330`.
