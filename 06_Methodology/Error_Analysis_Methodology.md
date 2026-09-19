# Error Analysis Methodology: Failure Taxonomies, Residual Diagnostics & Qualitative Audits

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Error_Analysis_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Error Analysis Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Structured Failure Taxonomy

To move beyond aggregate summary metrics, all test-set prediction errors are decomposed into five standardized failure classes:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           SYSTEM ERROR TAXONOMY                                 │
├────┬─────────────────────┬──────────────────────────────────────────────────────┤
│ ID │ Error Category      │ Manifestation & Real-World Impact                    │
├────┼─────────────────────┼──────────────────────────────────────────────────────┤
│ E1 │ False Positive (FP) │ Candidate predicted Ready (Tier 1) but fails actual  │
│    │                     │ corporate interviews (Severe: damages trust).        │
├────┼─────────────────────┼──────────────────────────────────────────────────────┤
│ E2 │ False Negative (FN) │ Candidate predicted Unready (Tier 3) but successfully│
│    │                     │ secures corporate offer (Generates student anxiety). │
├────┼─────────────────────┼──────────────────────────────────────────────────────┤
│ E3 │ OCR / Layout Fault  │ Resume bounding box scrambling or non-standard font  │
│    │                     │ rendering causing missed technical skill entities.   │
├────┼─────────────────────┼──────────────────────────────────────────────────────┤
│ E4 │ Cold-Start Mismatch │ Student with zero platform interaction history       │
│    │                     │ receiving sub-optimal concept roadmap allocations.   │
├────┼─────────────────────┼──────────────────────────────────────────────────────┤
│ E5 │ Acoustic Disfluency │ Heavy regional accent or low-SNR microphone stream   │
│    │                     │ inducing Whisper word error spikes (WER > 25%).      │
└────┴─────────────────────┴──────────────────────────────────────────────────────┘
```

---

## 2. Systematic Error Sampling & Qualitative Audit Protocol

For each test set evaluation cycle:
1. **Stratified Error Extraction**: All misclassified instances ($y \neq \hat{y}$) are extracted from the test split.
2. **Confidence Margin Sorting**: Errors are sorted by prediction margin $|P - 0.50|$; borderline errors ($0.45 \le P \le 0.55$) are separated from high-confidence blunders ($P > 0.85$ or $P < 0.15$).
3. **Independent Double-Audit**: Two domain experts independently inspect the candidate's raw resume, coding logs, and transcript to identify root causes:
   - Was the ground-truth placement label unrepresentative (e.g., candidate rejected due to hiring freeze rather than lack of competence)?
   - Was a critical feature missing in telemetry?
   - Did the model over-index on historical CGPA while ignoring elite competitive programming ratings?
