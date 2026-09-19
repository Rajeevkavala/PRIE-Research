# Ablation Study Methodology: Systematic Component Dissection & Contribution Isolation

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Ablation_Study_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Ablation Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Scientific Justification & Ablation Philosophy

To establish that PRIE's performance gains originate from genuine methodological innovations rather than incidental hyperparameter tuning, systematic ablation experiments isolate the independent contribution of each core component:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        MASTER ABLATION STUDY PROTOCOL                           │
├───────┬──────────────────────┬──────────────────────────┬───────────────────────┤
│ Exp   │ Subsystem Tested     │ Ablated Component Variant│ Research Question     │
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-1 │ ATS Document Parser  │ Strip 2D Bounding Boxes  │ Is spatial layout     │
│       │                      │ (Pure text LayoutLMv3)   │ essential for parsing?│
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-2 │ Sequence Forecaster  │ Strip Longitudinal Rec.  │ Does multi-week log   │
│       │                      │ (Evaluate static snapshot│ outperform snapshot?  │
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-3 │ Recourse Engine      │ Disable Mutability Lock  │ Do unlocked features  │
│       │                      │ (Allow unconstrained CF) │ produce absurd advice?│
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-4 │ Recommendation DAG   │ Replace A* DAG with      │ Does graph topology   │
│       │                      │ Collaborative Filtering  │ prevent out-of-order? │
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-5 │ Automated Question Gen│ Remove Causal Misconcep.│ Do casual distractors │
│       │                      │ (Zero-shot unconstrained)│ improve discrimination│
├───────┼──────────────────────┼──────────────────────────┼───────────────────────┤
│ ABL-6 │ Curriculum RAG       │ Remove Cross-Encoder     │ Does two-stage rerank │
│       │                      │ (Single dense retrieval) │ improve groundedness? │
└───────┴──────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 2. Experimental Ablation Protocols

### ABL-1: Spatial Coordinate Contribution in LayoutLMv3
- **Full Model**: LayoutLMv3 with $[x_0, y_0, x_1, y_1]$ 2D bounding boxes and image patches.
- **Ablated Variant**: LayoutLMv3 with all 2D coordinates clamped to $(0, 0, 0, 0)$ and visual patches masked.
- **Hypothesized Delta**: Significant drop in multi-column Entity Boundary-F1 ($\Delta F_1 \ge 0.15$).

### ABL-2: Longitudinal Telemetry in TFT Forecasting
- **Full Model**: TFT multi-horizon forecaster operating on 16-week longitudinal sequence tensors.
- **Ablated Variant**: XGBoost operating on final cumulative feature snapshot at identical prediction horizon.
- **Hypothesized Delta**: Quantile loss reduction degradation ($\ge 12\%$).

### ABL-3: Feature Mutability & Directional Constraints in DiCE
- **Full Model**: DiCE with immutable feature locking (`CGPA`, `Branch`, `Gender`) and monotonic directional constraints.
- **Ablated Variant**: Standard unconstrained DiCE search allowing all features to vary bidirectionally.
- **Hypothesized Delta**: Unconstrained DiCE generates faster mathematical convergence but yields clinically absurd student recommendations (e.g., "reduce CGPA to 7.0" or "change engineering department").
