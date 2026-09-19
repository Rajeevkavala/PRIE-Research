# Prediction Methodology: Target Operationalization, Dual-Track Forecasting & Tier Classification

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Prediction_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Prediction Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Precise Operationalization of Placement Readiness

In prior literature (`Paper01`, `Paper06`, `Paper10`), the term "placement readiness" was frequently used as a vague colloquialism without formal operational definitions. PRIE resolves this ambiguity through a rigorous two-tier mathematical formulation:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      PREDICTION OPERATIONALIZATION TOPOLOGY                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  1. CONTINUOUS READINESS PROBABILITY                                            │
│     • Calibrated probability P_placement in [0.0, 1.0]                          │
│     • Estimated via Dual-Track Estimators (XGBoost + TFT)                       │
│                                                                                 │
│  2. CATEGORICAL READINESS TIERS (DECISION THRESHOLDS)                           │
│     • Tier 1: "Placement Ready" (P_placement >= 0.75)                          │
│     • Tier 2: "Remediating / Moderately Ready" (0.50 <= P_placement < 0.75)    │
│     • Tier 3: "At-Risk / Substantial Deficit" (P_placement < 0.50)             │
│                                                                                 │
│  3. ROLE-SPECIFIC COMPENSATION TIERS (AUXILIARY TARGET)                         │
│     • Core / Super Dream: Top 10% compensation cutoff                           │
│     • Product / Dream: 60th–90th percentile compensation                        │
│     • Mass / Standard: Base corporate threshold                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. End-to-End Prediction Pipeline Architecture

The prediction pipeline ingests the invariant 22-dimensional SPV tensor and dispatches predictions through calibrated inference engines (`M06`):

```
[Normalized 22-Dim SPV Tensor x_spv] + [Observation Mask m]
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. MODEL ROUTING & FEATURE DISPATCH                         │
│    • Static Tabular Path: x_spv -> XGBoost Classifier       │
│    • Temporal Sequence Path: [x_spv(t)] -> TFT Forecaster   │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. RAW LOGIT INFERENCE & ENSEMBLE SCORING                   │
│    • XGBoost margin: z_static = sum(w_j * f_t(x))           │
│    • TFT Multi-Horizon Quantiles: q_0.1, q_0.5, q_0.9       │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. PROBABILITY CALIBRATION (ISOTONIC / PLATT)               │
│    • P_placement = Calibrator(z_static) in [0.0, 1.0]       │
│    • Verification: Brier Score <= 0.12, ECE <= 0.05         │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. READINESS TIER ASSIGNMENT & DISPATCH                     │
│    • Ready (Tier 1) -> Dispatch to Corporate Shortlist (M12)│
│    • Remediating (Tier 2) -> Trigger DiCE Recourse (M07)   │
│    • At-Risk (Tier 3) -> Trigger Week 3-4 Early Alert (M11) │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Dual-Track Inference Mechanics

### Track 1: Static Cross-Sectional Prediction (XGBoost)
Provides immediate point-in-time assessment when a student updates their resume or completes a diagnostic test:
$$z_{	ext{static}} = \sum_{m=1}^M f_m(\mathbf{x}_{	ext{spv}}), \quad \hat{P}_{	ext{raw}} = \sigma(z_{	ext{static}})$$
$$\hat{P}_{	ext{placement}} = 	ext{IsotonicCalibrator}(\hat{P}_{	ext{raw}})$$

### Track 2: Dynamic Multi-Horizon Forecasting (TFT)
Provides forward-looking trajectory curves across future semesters using historical multi-week interaction sequences:
$$\mathbf{y}_{t+	au}(q) = 	ext{TFT}\Big( [\mathbf{x}_{	ext{spv}}(t-W), \dots, \mathbf{x}_{	ext{spv}}(t)], \mathbf{c}_{	ext{static}} \Big), \quad q \in \{0.1, 0.5, 0.9\}$$
where $	au = +6$ months and $+12$ months represent upcoming campus placement drive windows.

---

## 4. Decision Threshold Calibration

Decision thresholds are calibrated on the inner validation fold using a Cost-Utility Matrix that heavily penalizes false positives (declaring an unready student as ready, which leads to corporate interview rejection):
$$	ext{Threshold}^* = rg\max_{	heta \in [0, 1]} \Big( 	ext{Benefit}_{	ext{TP}} \cdot 	ext{TP}(	heta) - 	ext{Cost}_{	ext{FP}} \cdot 	ext{FP}(	heta) - 	ext{Cost}_{	ext{FN}} \cdot 	ext{FN}(	heta) \Big)$$
where $	ext{Cost}_{	ext{FP}} = 3 	imes 	ext{Cost}_{	ext{FN}}$.
