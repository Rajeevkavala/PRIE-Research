# RQ to Experiment Mapping: Operational Research Pathways & Decision Rules

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/RQ_to_Experiment_Mapping.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative RQ-to-Experiment Mapping  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Operational Research Question Pathways

Every research question formulated in Phase 03 (`03_Research_Problem/Research_Questions.md`) is linked to a concrete experimental protocol:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    RESEARCH QUESTION TO EXPERIMENT MAPPING                                             │
├──────┬────────────────────────────────────────┬─────────────┬──────────────┬────────────────────┬──────────────────────┤
│ RQ   │ Core Scientific Inquiry                │ Linked Hyp. │ Experiment   │ Primary Metric     │ Decision Criterion   │
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ1  │ Can 2D spatial layout intelligence     │ H1          │ EXP-1        │ Entity Boundary-F1 │ Delta F1 >= +0.15 on │
│      │ resolve multi-column ATS destruction?  │             │              │ on multi-column    │ multi-column, p<0.01 │
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ2  │ Can streaming pipelines achieve        │ H2          │ EXP-2        │ Voice Turn Latency │ Latency < 1.500 ms,  │
│      │ sub-1.5s latency with high panel r?    │             │              │ & Recruiter r      │ r >= 0.70, p < 0.001 │
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ3  │ Does longitudinal sequence modeling    │ H3          │ EXP-3        │ Quantile Loss      │ Quantile loss delta  │
│      │ outperform static cross-sectional ML?  │             │              │ (q0.1, q0.5, q0.9) │ >= 12% reduction     │
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ4  │ Does prescriptive counterfactual       │ H4          │ EXP-4        │ Likert Usability   │ Actionability +40%,  │
│      │ recourse elevate student actionability?│             │              │ & 30-Day Complete  │ p < 0.001            │
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ5  │ Do causal concept DAGs eliminate       │ H5          │ EXP-5        │ Item Discrimination│ DI >= 0.35,          │
│      │ trivial non-functional distractors?    │             │              │ DI & Distractor DPI│ DPI >= 0.70, p < 0.01│
├──────┼────────────────────────────────────────┼─────────────┼──────────────┼────────────────────┼──────────────────────┤
│ RQ6  │ Does closed-loop digital twin platform │ H6          │ EXP-6        │ Campus Placement   │ Institutional uplift │
│      │ yield measurable placement conversion? │             │              │ Conversion Rate    │ Delta >= +15%, p<0.05│
└──────┴────────────────────────────────────────┴─────────────┴──────────────┴────────────────────┴──────────────────────┘
```
