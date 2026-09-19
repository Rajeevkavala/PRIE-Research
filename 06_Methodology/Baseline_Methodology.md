# Baseline Methodology: State-of-the-Art Literature Baselines & Empirical Benchmarks

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Baseline_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Baseline Methodology  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Principles of Fair Baseline Selection

In educational data mining research, algorithms are frequently compared against artificially crippled "strawman" baselines. In PRIE, baselines are selected strictly according to four rigorous criteria:

1. **Literature Prominence**: Baselines represent the dominant methods reported across the 44-paper Phase 01 corpus (`Paper01`, `Paper06`, `Paper11`, `Paper14`, `Paper22`).
2. **Identical Preprocessing**: All baselines receive identical training data splits, scaling transformations, and missing-value treatments.
3. **Hyperparameter Parity**: Baselines undergo equivalent Optuna Bayesian tuning rather than defaulting to out-of-the-box library defaults.
4. **Subsystem-Specific Alignment**: Baselines are established independently for each functional modality.

---

## 2. Authoritative Baseline Inventory by Subsystem

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      MASTER BASELINE SPECIFICATIONS                                     │
├──────┬──────────────────────┬────────────────────────────┬────────────────────────┬─────────────────────┤
│ Exp  │ PRIE Model           │ Literature Baseline Model  │ Reference Citation     │ Baseline Rationale  │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-1│ LayoutLMv3 Spatial   │ BL1.1: spaCy Transformer   │ Mishra 2025 (P11)      │ Industry standard   │
│      │ ATS Parser           │ BL1.2: BERT-base NER       │ Verma 2026 (P17)       │ Flat text benchmark │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-2│ Streaming Local STT  │ BL2.1: Sequential Cloud API│ Deshmukh 2025 (P14)    │ Commercial pattern  │
│      │ Voice Pipeline       │ BL2.2: Text-Only Chatbot   │ Inamdar 2025 (P15)     │ Conversational base │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-3│ Temporal Fusion      │ BL3.1: Static XGBoost      │ Olipas 2024 (P01)      │ Tabular baseline    │
│      │ Transformer (TFT)    │ BL3.2: Standard LSTM       │ Chen 2024 (P05)        │ Recurrent baseline  │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-4│ DiCE Prescriptive    │ BL4.1: Raw Probability     │ Senthil 2021 (P06)     │ Zero explainability │
│      │ Recourse             │ BL4.2: TreeSHAP Waterfall  │ Talmoudi 2026 (P32)    │ Descriptive base    │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-5│ Causal Concept DAG   │ BL5.1: Zero-Shot Llama-3   │ Wang 2026 (P25)        │ Unconstrained LLM   │
│      │ Guided AQG           │ BL5.2: Few-Shot GPT-4o     │ Fernandez 2025 (P26)   │ Frontier model base │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ EXP-6│ Triangular Digital   │ BL6.1: Historical Control  │ Institutional Data     │ Unassisted baseline │
│      │ Twin Synchronization │ BL6.2: Uncoordinated Tools │ Consortium 2026 (P41)  │ Disconnected tools  │
└──────┴──────────────────────┴────────────────────────────┴────────────────────────┴─────────────────────┘
```
