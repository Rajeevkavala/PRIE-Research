# Threats to Validity Methodology: Four-Quadrant Analysis, Mitigations & Residual Risks

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Threats_to_Validity_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Validity Evaluation  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Four-Quadrant Validity Governance

Following established empirical software engineering guidelines (Wohlin et al.), PRIE evaluates research validity across four classical dimensions:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        FOUR-QUADRANT VALIDITY MATRIX                            │
├───────────────────────────────────────┬─────────────────────────────────────────┤
│ 1. CONSTRUCT VALIDITY                 │ 2. INTERNAL VALIDITY                    │
│ • Are we truly measuring readiness?   │ • Are observed gains caused by PRIE     │
│ • Mitigation: Anchored to verified    │   rather than confounding noise?        │
│   literature psychometrics & JDs      │ • Mitigation: Strict test isolation,    │
│                                       │   ablation studies & cross-validation   │
├───────────────────────────────────────┼─────────────────────────────────────────┤
│ 3. EXTERNAL VALIDITY                  │ 4. STATISTICAL CONCLUSION VALIDITY      │
│ • Do findings generalize across       │ • Are statistical conclusions sound?    │
│   different universities & cohorts?   │ • Mitigation: Non-parametric tests,     │
│ • Mitigation: Multi-dataset benchmarks│   power analysis & Bonferroni-Holm      │
└───────────────────────────────────────┴─────────────────────────────────────────┘
```

---

## 2. Detailed Threat Mitigations & Residual Risk Matrix

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   DETAILED THREAT MITIGATION MATRIX                                     │
├────┬─────────────────────┬────────────────────────────────┬────────────────────────┬────────────────────┤
│ ID │ Validity Threat     │ Impact on Research Findings    │ Methodological Mitig.  │ Residual Risk      │
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T1 │ Data Leakage        │ Artificially inflated accuracy │ Strict test set        │ Minimal: sealed    │
│    │ across Splits       │ masking true generalization    │ freezing & in-fold pre-│ encrypted test set │
│    │                     │ failure in real students       │ processing (MICE/SMOTE)│                    │
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T2 │ Synthetic Copula    │ Over-optimistic convergence on │ Synthetic data strictly│ Low: real cohort   │
│    │ Distribution Gap    │ simulated data (DS-SYNTH-01)   │ restricted to stress-  │ required for final │
│    │                     │ not matching human reality     │ testing (DD-012)       │ claims (DS-REAL-01)│
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T3 │ Non-Standard Resume │ Tesseract OCR failure on       │ Image deskewing,       │ Low: manual review │
│    │ OCR Artifacts       │ artistic graphical resumes     │ LayoutLMv3 spatial     │ fallback for < 3%  │
│    │                     │ causing skill omissions        │ bounding boxes (M02)   │ corrupted PDFs     │
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T4 │ Conversational Turn │ Audio latency spikes exceeding │ Streaming Whisper STT, │ Moderate: low-end  │
│    │ Latency Spikes      │ 1.5s on weak client hardware   │ client Wasm MediaPipe, │ hardware requires  │
│    │                     │ breaking interview cadence     │ local quantized LLM    │ local WebAssembly  │
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T5 │ LLM Hallucination   │ Inaccurate curriculum advice or│ Two-stage RAG with     │ Minimal: runtime   │
│    │ in Career Guidance  │ misleading conceptual answers  │ runtime RAG Triad      │ triad guard blocks │
│    │                     │ damaging student learning      │ verification (M09)     │ ungrounded claims  │
├────┼─────────────────────┼────────────────────────────────┼────────────────────────┼────────────────────┤
│ T6 │ Historical Label    │ Model learns past corporate    │ Exclusion of protected │ Moderate: hiring   │
│    │ Selection Bias      │ hiring biases against specific │ demographics; fairness │ market shifts are  │
│    │                     │ student subgroups              │ parity audits (DIR)    │ extrinsic to model │
└────┴─────────────────────┴────────────────────────────────┴────────────────────────┴────────────────────┘
```
