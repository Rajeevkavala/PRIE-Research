# Methodology Traceability: Full N-Dimensional Research & Verification Matrix

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Methodology_Traceability.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative N-Dimensional Traceability Matrix  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Master N-Dimensional Traceability Chain

Every major methodological procedure in PRIE traces directly through the unbroken scientific spine:

$$\text{Research Question } (RQ) \longrightarrow \text{Hypothesis } (H) \longrightarrow \text{Objective } (RO) \longrightarrow \text{Gap } (RG) \longrightarrow \text{Module } (M) \longrightarrow \text{Method} \longrightarrow \text{Dataset} \longrightarrow \text{Model} \longrightarrow \text{Baseline} \longrightarrow \text{Experiment } (EXP) \longrightarrow \text{Metric} \longrightarrow \text{Statistical Test}$$

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                               MASTER RESEARCH TRACEABILITY MATRIX                                                               │
├─────┬────┬───┬────┬────┬──────────┬──────────────────────┬─────────────┬───────────┬──────────────┬──────────────┬────────────┬──────────────────┬──────────────┬─────┤
│ M_ID│ RQ │ H │ RO │ RG │ Module   │ Methodological Focus │ Dataset     │ Algorithm │ Baseline     │ Experiment   │ Primary Met│ Statistical Test │ Validation   │ Stat│
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-01│ RQ1│ H1│ RO1│ RG4│ M02 (ATS)│ 2D Spatial Layout    │ DS-CORPUS-01│ LayoutLMv3│ spaCy NER,   │ EXP-1        │ Boundary-F1│ Wilcoxon Signed- │ 5-Fold Group │ DEF │
│     │    │   │    │    │          │ Document Intelligence│             │           │ BERT Flat-Txt│              │ (Delta>=.15│ Rank Test        │ Split (Auth) │     │
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-02│ RQ2│ H2│ RO2│ RG5│ M05 (Int)│ Streaming Chunked STT│ DS-INTERVIEW│ Whisper + │ Cloud Batch  │ EXP-2        │ Turn Latency│ Paired t-test,   │ Blinded Recr.│ DEF │
│     │    │   │    │    │          │ + Wasm MediaPipe Face│ (Pilot N=150│ MediaPipe │ API Pipeline │              │ (<1.5s), r │ Pearson Correl. r│ Panel (N=3)  │     │
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-03│ RQ3│ H3│ RO3│ RG2│ M06 (Pred│ Longitudinal Sequence│ DS-BENCH-02,│ Temporal  │ Static       │ EXP-3        │ Quantile   │ Diebold-Mariano, │ 4-Window Roll│ DEF │
│     │    │   │    │    │ M11 (Tel)│ Multi-Horizon Forecas│ DS-SYNTH-01 │ Fusion Tr.│ XGBoost, LSTM│              │ Loss (q0.5)│ Wilcoxon Test    │ Origin Split │     │
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-04│ RQ4│ H4│ RO4│ RG3│ M07 (XAI)│ Distance-Constrained │ DS-SYNTH-01,│ DiCE ML + │ Descriptive  │ EXP-4        │ Likert     │ Paired t-test,   │ Double-blind │ DEF │
│     │    │   │    │    │          │ Prescriptive Recourse│ Student N=60│ TreeSHAP  │ TreeSHAP Only│              │ Actionable,│ Chi-Square Test  │ Crossover    │     │
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-05│ RQ5│ H5│ RO5│ RG6│ M10 (AQG)│ Causal Concept DAG-  │ DS-AQG-ITEM │ Causal CoT│ Zero-Shot    │ EXP-5        │ Item Discr.│ Independent      │ Pilot Exam   │ DEF │
│     │    │   │    │    │          │ Guided Distractor Gen│ (N = 500)   │ Prompting │ Llama-3-70B  │              │ DI, DPI    │ Student t-test   │ Cohort N=120 │     │
├─────┼────┼───┼────┼────┼──────────┼──────────────────────┼─────────────┼───────────┼──────────────┼──────────────┼────────────┼──────────────────┼──────────────┼─────┤
│ M-06│ RQ6│ H6│ RO6│ RG8│ M12 (Twin│ Closed-Loop Triang.  │ DS-REAL-01* │ Multi-Ag. │ Disconnected │ EXP-6        │ Placement  │ Two-Proportion   │ Longitudinal │ DEF*│
│     │    │   │    │    │          │ Digital Twin Platform│ (Proposed)  │ Sync + DP │ Point Tools  │              │ Uplift (%) │ Z-Test, Log-Rank │ Cohort Study │     │
└─────┴────┴───┴────┴────┴──────────┴──────────────────────┴─────────────┴───────────┴──────────────┴──────────────┴────────────┴──────────────────┴──────────────┴─────┤
│ *DS-REAL-01 Status: NOT YET AVAILABLE / DATA COLLECTION REQUIRED; Status DEF = Defined (Methodological Plan)                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
