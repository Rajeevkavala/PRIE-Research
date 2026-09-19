# Research vs Engineering Evidence Ledger
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  

In strict compliance with Phase 08 Section 56, engineering software checks are separated from empirical research findings:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      ENGINEERING VALIDATION vs EMPIRICAL RESEARCH EVIDENCE                       │
├──────────────────────────────────────┬───────────────────────────────────────────────────────────┤
│ Engineering Validation Check         │ Empirical Research Evidence                               │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ FastAPI returns HTTP 200 on /health  │ Platt-calibrated XGBoost achieves Brier score 0.0339      │
│ SQLite connects to prie_v1.db        │ Late Multimodal Fusion reduces diagnostic variance by 78% │
│ Pytest 70/70 passing                 │ DiCE achieves 100% invariance on F17 with sparsity k <= 3 │
│ Docker container compiles C++ in 3.5s│ Kahn's DAG sort achieves 0 prerequisite sequencing errors │
│ ChromaDB indexes 10 semantic chunks  │ SBERT/BM25 hybrid RRF yields 100% in-domain precision     │
└──────────────────────────────────────┴───────────────────────────────────────────────────────────┘
```
