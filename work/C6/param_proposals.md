# C6 — Parameter proposals (NAV)

Proposals for `parameters/PARAMETERS.yaml` from task C6 (NAV). The orchestrator merges them; C6 does not edit the database. The YAML block uses the database field layout. Existing IDs are reused for the two CV-580 validity thresholds (P-NAV-010, P-NAV-030). New P-NAV IDs start at 060: P-NAV-020, -040 and -050 were withdrawn with D56 and are never reused.

**P-NAV number blocks proposed.** 010–050 validity thresholds (020, 040, 050 withdrawn); 060–090 verification agreement tolerances; 100–990 free.

**Values.** Every value is a C6 proposal, TBR, for the owner to set or confirm at G2 (C6-Q02, C6-Q03). The agreement tolerances are verification tolerances, kept in the database like P-FU-060 and P-FU-090 because the success criteria cite them.

**TBD/TBR register.** TT-200 (P-NAV-010, P-NAV-030, TBD, G2 (C6)) becomes TBR with the values below. A new row is proposed for P-NAV-060 to -080: "NAV agreement tolerances 1e-6 m, 1e-9 m/s, 1e-9 rad", TBR, Martin, G2 (I1).

## 1. Changes to existing entries

| ID | Change | Reason |
| --- | --- | --- |
| P-NAV-010 | Value null → **0.514444** m/s (1 kt, rounded down from 1852/3600 so that a selected 1 kt is a valid track); TBD → TBR. Description: "Minimum horizontal speed for which track is valid; the track is valid at or above it (inclusive, CV-580)." | C6-Q02. One knot is the horizontal speed selection resolution [P-AF-030] and display resolution [P-TM-040]: the smallest non-zero speed Heading can fly has a valid track. It lies above the landing envelope horizontal speed [P-SYS-510] = 0.5 m/s, so the track is invalid on the ground, at each landing and in a hold (Stationary, Hover, Takeoff, Land settle below [P-AF-170] ≤ [P-SYS-510]). With an exact state the track direction is exact at any non-zero speed, so the threshold is a usefulness bound, not an accuracy bound. |
| P-NAV-030 | Value null → **1.396263** rad (80°); TBD → TBR. Description: "Maximum absolute pitch angle for which heading and roll angle are valid; valid at or below it (inclusive, CV-580)." | C6-Q03. At 80° the heading moves by tan 80° ≈ 5.7 times a small roll perturbation, the largest sensitivity at which a nose direction is still a usable indication; beyond, it grows without bound toward 90° (CV-260). Pitch is held within [P-AF-180] of zero in every mode (D57), so the threshold acts only in airborne test starts and after fuel exhaustion (tumbling). |

## 2. YAML block

```yaml
  # --- NAV (C6) ---
  - id: P-NAV-010
    name: Track validity speed
    description: Minimum horizontal speed for which the track is valid. The track is valid while the horizontal speed of the frame-start state is at least this value (inclusive, CV-580) and invalid below it; its value is zero while invalid (L2-AER-NAV-100, -110, -140).
    unit: m/s
    value: 0.514444
    tolerance: null
    note: 'C6. 1 kt = 1852/3600 m/s, rounded down to 6 decimals so that a selected 1 kt is a valid track. Equal to the horizontal speed selection resolution P-AF-030 and display resolution P-TM-040; above the landing envelope speed P-SYS-510, so the track is invalid on the ground and in a hold. Range - greater than zero.'
    status: TBR
    source: CV-540, CV-580; L2-AER-NAV-070, -100, -110, -330; C6 proposal (C6-Q02)
    owner: Martin
  - id: P-NAV-030
    name: Heading validity pitch limit
    description: Maximum magnitude of the pitch angle for which the heading and the roll angle are valid. The heading is valid while the magnitude of the pitch angle of the frame-start state is at most this value (inclusive, CV-580) and invalid above it (L2-AER-NAV-120, -130).
    unit: rad
    value: 1.396263
    tolerance: null
    note: 'C6. 80 deg. Heading sensitivity to a small roll perturbation is about tan(theta), 5.7 at 80 deg. Pitch is held within P-AF-180 of zero in every mode (D57); the limit acts in airborne test starts and after fuel exhaustion. Range - greater than zero, less than pi/2.'
    status: TBR
    source: CV-260, CV-580; L2-AER-NAV-060, -120, -130, -330; C6 proposal (C6-Q03)
    owner: Martin
  - id: P-NAV-060
    name: NAV length agreement tolerance
    description: Largest difference between a NAV length output (altitude, height above the ground, north or east component of the horizontal position) and its independent computation from the recorded frame-start state, in the NAV analyses and tests (AN-NAV-010, -020, -030; TP-NAV-330). Floating-point agreement only.
    unit: m
    value: 1.0e-6
    tolerance: null
    note: 'C6. Positions reach P-SYS-220 = 4.4e6 m, where double precision gives about 1e-9 m. A verification tolerance, kept in the database like P-FU-090 because the requirements cite it. Range - greater than zero.'
    status: TBR
    source: L2-AER-NAV-010, -020, -030, -330; C6 proposal
    owner: Martin
  - id: P-NAV-070
    name: NAV speed agreement tolerance
    description: Largest difference between a NAV speed output (horizontal speed, vertical speed) and its independent computation from the recorded frame-start state, in the NAV analyses (AN-NAV-040, -050). Floating-point agreement only.
    unit: m/s
    value: 1.0e-9
    tolerance: null
    note: 'C6. Speeds reach P-SYS-230 = 154 m/s (and the free-fall speed in the tumbling test), where double precision gives about 1e-13 m/s. A verification tolerance. Range - greater than zero.'
    status: TBR
    source: L2-AER-NAV-040, -050; C6 proposal
    owner: Martin
  - id: P-NAV-080
    name: NAV angle agreement tolerance
    description: Largest CV-930 difference between a NAV direction angle output (heading, track) and its independent computation from the recorded frame-start state, in the NAV analyses (AN-NAV-060, -070), where the quantity is valid. Floating-point agreement only.
    unit: rad
    value: 1.0e-9
    tolerance: null
    note: 'C6. Within the validity range (pitch magnitude at most P-NAV-030, horizontal speed at least P-NAV-010) the conditioning keeps the difference near 1e-15 rad. A verification tolerance. Range - greater than zero.'
    status: TBR
    source: L2-AER-NAV-060, -070; C6 proposal
    owner: Martin
```

## 3. Existing parameters the NAV records cite

| ID | Use in NAV | Owner |
| --- | --- | --- |
| P-DYN-020, P-DYN-030 | Body length and diameter in the height above the ground (CV-400, L2-AER-NAV-020, -330), taken from the run's vehicle parameter set | DYN (C1) |
| P-DYN-040 | Height above the ground at rest on the extended gear (verification of -020, -330) | DYN (C1) |
| P-AF-210, P-SYS-210 | Heights above the ground that autoflight and the envelope use (rationale of -020) | AF, SYS |
| P-AF-140, P-AF-160, P-AF-180, P-AF-200, P-AF-220, P-AF-240, P-AF-030 | Rationale only: how autoflight uses the quantities, and the value of P-NAV-010 | AF (C5) |
| P-SYS-230, P-SYS-510 | Rationale of -040 (ground speed, D72) and of P-NAV-010 | SYS |
| P-SYS-300, P-SYS-310, P-TM-010 | Frame and sample timing (-250, -300) | SYS, TM |

No crew-facing parameter is proposed: NAV is SI only (CV-760).
