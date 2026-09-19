# Real Data Methodology: Institutional Cohort Acquisition, Onboarding & Ethical Readiness

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Real_Data_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Real Data Acquisition Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Authoritative Acquisition Status

> [!IMPORTANT]
> **CURRENT STATUS: NOT YET AVAILABLE / DATA COLLECTION REQUIRED**  
> In strict compliance with Phase 06 directives, real-world institutional student data (`DS-REAL-01`) has **not** been collected, simulated, or prematurely claimed as existing.  
> This document defines the **operational onboarding protocol** required to collect, validate, and govern real student cohorts during Phase 07 implementation and Phase 08 experimental execution.

---

## 2. Institutional Study Population & Eligibility Criteria

The target cohort for future empirical evaluation (`DS-REAL-01`) comprises undergraduate engineering students preparing for campus corporate placement drives:

### 2.1 Inclusion Criteria
1. **Academic Enrollment**: Active enrollment in an accredited 4-year undergraduate engineering degree program (B.Tech / B.E.).
2. **Academic Specialization**: Enrolled in Computer Science & Engineering (CSE), Information Technology (IT), or Electronics & Communication Engineering (ECE).
3. **Academic Standing**: Completed at least four (4) academic semesters (entry into Semester 5 / Year 3), ensuring sufficient academic transcript history.
4. **Institutional Consent**: Formally signed electronic informed consent agreeing to anonymized telemetry collection for research purposes.

### 2.2 Exclusion Criteria
1. Formal academic suspension, voluntary medical leave of absence, or discontinuation.
2. Transfer students with fewer than two semesters of accredited institutional grade history.
3. Candidates opting out of automated career coaching telemetry.

---

## 3. Four-Stage Institutional Onboarding Protocol

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    INSTITUTIONAL ONBOARDING WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│  STAGE 1: INSTITUTIONAL ETHICS REVIEW & GOVERNANCE APPROVAL                     │
│  • Institutional Review Board (IRB) / Ethics Committee application submission   │
│  • Institutional Data Protection Officer (DPO) sign-off on POPIA/FERPA compliance│
│                                                                                 │
│  STAGE 2: STUDENT CONSENT & AUTONOMOUS ONBOARDING                               │
│  • Granular multi-tier consent modal presented upon initial ScholarCamp login   │
│  • Explicit opt-in for: (a) SIS Sync, (b) Resume Parsing, (c) Interview Wasm   │
│                                                                                 │
│  STAGE 3: MULTIMODAL INGRESS & SECURE BASELINE COMPILATION                      │
│  • Automated API handshake with university SIS registrar database               │
│  • Initial baseline diagnostic test (M03) and resume upload (M02)              │
│  • Initial invariant 22-dimensional SPV tensor generated                        │
│                                                                                 │
│  STAGE 4: LONGITUDINAL MONITORING & VERIFIED OUTCOME AUDITING                   │
│  • Continuous interaction logging across pre-placement semesters                │
│  • Placement Cell audits verified campus hiring offers (Placed / Unplaced)      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Ground-Truth Placement Label Operationalization

To eliminate ambiguity in target classification, the final placement outcome label ($y$) is operationalized strictly through official university placement cell records:

$$y = egin{cases} 
1 & 	ext{if candidate receives a verified, written corporate technical job offer through campus drives} \ 
0 & 	ext{if candidate completes all recruitment drives without receiving a verified corporate offer} 
\end{cases}$$

### Continuous Auxiliary Target Variables:
1. **Placement Offer Compensation Tier**: Normalized salary tier:
   - Tier 1 (Core / Super Dream): Top 10% compensation bracket.
   - Tier 2 (Dream / High Growth): 60th–90th percentile compensation.
   - Tier 3 (Standard Mass Recruitment): Base threshold compensation.
2. **Time to Placement**: Days elapsed from official campus recruitment season opening to confirmed offer acceptance.

---

## 5. Mitigation of Institutional & Demographic Selection Bias

To prevent algorithms from reinforcing historical institutional biases:
1. **Departmental Balance**: Sampling stratified across CSE, IT, and non-circuit branches to avoid overfitting to computer science curricula.
2. **Gender Parity Audits**: Telemetry monitored to ensure male-to-female representation reflects institutional enrolment without systematic exclusion.
3. **Socioeconomic Feature Isolation**: Family income, regional origin, and residential categories are strictly excluded from the SPV feature set, preventing proxy bias encoding.
