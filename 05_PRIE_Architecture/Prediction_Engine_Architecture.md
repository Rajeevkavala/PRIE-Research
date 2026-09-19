# Prediction Engine Architecture: Dual-Track Predictive Framework (M06)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Prediction_Engine_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Predictive Engine Architecture  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Problem Statement & Research Grounding

Traditional educational predictive modeling suffers from two fundamental limitations:
1. **Unimodal Feature Fragmentation (`RG1`)**: Prior systems rely exclusively on academic grades or flat-text resumes.
2. **Static Snapshot Blindness (`RG2`)**: 93% of existing placement literature evaluates candidate employability as a single, static point-in-time snapshot, completely failing to model student learning velocity, habit persistence, or early-warning intervention windows.

To solve both gaps simultaneously, PRIE establishes a **Dual-Track Predictive Architecture** (`DD-002`, `M06`):
- **Track 1 (Static Cross-Sectional)**: Extreme Gradient Boosting (XGBoost) for immediate screening and discrete tier classification based on the 22-dimensional Student Profile Vector (SPV).
- **Track 2 (Dynamic Longitudinal)**: Temporal Fusion Transformer (TFT) for multi-horizon progression forecasting across academic semesters (Sem 4 $\to$ Sem 7).

---

## 2. Dual-Track Architectural Topology

```
                         ┌────────────────────────────────────────────────────────┐
                         │       M01: Student Profile Vector Aggregator           │
                         └───────────────────────────┬────────────────────────────┘
                                                     │
                                    ┌────────────────┴────────────────┐
                                    │                                 │
                         (Current Snapshot SPV_t)          (Sequential SPV_1..T)
                                    │                                 │
                                    ▼                                 ▼
                     ┌─────────────────────────────┐   ┌─────────────────────────────┐
                     │ TRACK 1: CROSS-SECTIONAL    │   │ TRACK 2: DYNAMIC SEQUENCE   │
                     │ Extreme Gradient Boosting   │   │ Temporal Fusion Transformer │
                     │ (XGBoost GBDT)              │   │ (TFT with Self-Attention)   │
                     └──────────────┬──────────────┘   └──────────────┬──────────────┘
                                    │                                 │
                     ┌──────────────▼──────────────┐   ┌──────────────▼──────────────┐
                     │ • Readiness Probability     │   │ • Multi-Horizon Quantiles   │
                     │   P_ready in [0.0, 1.0]     │   │   (P10, P50, P90 at 6m/12m) │
                     │ • Discrete Readiness Tier   │   │ • Temporal Attention Weights│
                     │ • Handoff to TreeSHAP (M07) │   │ • Learning Velocity Vector  │
                     └──────────────┬──────────────┘   └──────────────┬──────────────┘
                                    │                                 │
                                    └────────────────┬────────────────┘
                                                     ▼
                                      [Prediction Bundle Interface]
                                                     │
                                      ├──► M07 (Prescriptive XAI Engine)
                                      ├──► M12 (Triangular Digital Twin Sync)
                                      └──► UI (Student / Faculty Dashboards)
```

---

## 3. Track 1: Static Cross-Sectional Prediction Pipeline (XGBoost)

### 3.1 Input Features & Preprocessing
- **Feature Vector**: Standardized 22-dimensional vector $\mathbf{x} = [f_1, f_2, \dots, f_{22}]^T \in \mathbb{R}^{22}$.
- **Preprocessing Pipeline**:
  - Missing values imputed using MICE/median imputation flags.
  - Continuous features normalized via Min-Max scaling.
  - Zero target label leakage: features measured strictly prior to placement drive commencement.
- **Inference Time Budget**: $<5$ms per profile on standard CPU.

### 3.2 Algorithmic Formulation & Regularization
XGBoost minimizes a regularized second-order Taylor approximation of the objective:
$$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \Omega(f_t)$$
where $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$, $h_i = \partial^2_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$, and the tree complexity penalty is:
$$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2 + \alpha \sum_{j=1}^T |w_j|$$
- **Hyperparameter Bounds**: Maximum tree depth $d \in [3, 6]$; learning rate $\eta \in [0.01, 0.1]$; subsample ratio $0.8$; colsample_bytree $0.8$.

### 3.3 Output Calibration & Tier Discretization
To ensure output probabilities represent true empirical frequencies:
- **Calibration Method**: Sigmoid Platt Scaling or Isotonic Regression calibrated on validation folds to minimize Brier Score:
  $$\text{Brier} = \frac{1}{N} \sum_{i=1}^N (P_{\text{calibrated}}(y_i=1 \mid \mathbf{x}_i) - y_i)^2$$
- **Readiness Tier Boundaries**:
  - **Tier 1: `Ready`** ($P_{\text{calibrated}} \ge 0.75$): Candidate exceeds standard enterprise corporate screening cutoffs.
  - **Tier 2: `Needs Remediation`** ($0.45 \le P_{\text{calibrated}} < 0.75$): Candidate exhibits competitive foundational skills but lacks specific technical depth or project quality.
  - **Tier 3: `At-Risk`** ($P_{\text{calibrated}} < 0.45$): Candidate exhibits severe academic, coding, or consistency deficits; triggers immediate faculty advisor escalation.

---

## 4. Track 2: Dynamic Longitudinal Sequence Forecasting Pipeline (TFT)

### 4.1 Input Sequence Structure
- **Entity Identification**: Student ID ($s$).
- **Static Metadata (Time-Invariant)**: `branch_encoded` (`F17`), baseline entrance percentile, institutional tier.
- **Observed Time-Varying Inputs (Historical)**: Sequence of semester vectors $\mathbf{x}_t$ for $t \in \{1, 2, \dots, T\}$ (Semesters 4, 5, 6), containing weekly quiz attempts (`F19`), consistency scores (`F16`), coding sandbox milestones (`F06`), and longitudinal engagement (`F21`).
- **Known Future Inputs**: Target corporate drive deadline, semester calendar milestones.

### 4.2 Architectural Sub-Components of TFT
1. **Variable Selection Networks (VSN)**: At each time step $t$, VSN applies Gated Residual Networks (GRNs) to dynamically filter irrelevant historical noise and assign instance-specific feature importance weights.
2. **LSTM Sequence Encoder-Decoder**: Generates context vectors capturing sequential state transitions between semesters.
3. **Multi-Head Temporal Self-Attention**: Captures long-range dependencies across the multi-year preparation cycle:
   $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$
   Multi-head attention weights $\alpha_{t, \tau}$ explicitly expose *which past semester or intervention event* exerted the strongest influence on the projected placement outcome.
4. **Quantile Forecasting Head**: Simultaneously outputs 10th, 50th, and 90th percentiles ($\hat{y}_t(q_{0.1}), \hat{y}_t(q_{0.5}), \hat{y}_t(q_{0.9})$) across multi-horizon forecasts (12-month and 6-month horizons), providing intrinsic uncertainty intervals for academic advising.

---

## 5. Candidate Model Portfolio & Scientific Controls

In strict accordance with the **Tripartite Standard** (`Model_Selection_Justification.md`), PRIE maintains explicit baselines and avoids premature claims of model superiority:

| Model Architecture | Role in PRIE | Literature Grounding | Engineering Rationale | Experimental Validation Plan |
|:---|:---|:---|:---|:---|
| **XGBoost (Selected)** | Primary Track 1 Static Classifier | **P01, P04, P06, P18, P22** | Sub-5ms CPU inference, native TreeSHAP integration | 5x2 cross-validation on institutional cohort ($N \ge 2,000$) |
| **Temporal Fusion Transformer (Selected)**| Primary Track 2 Sequence Forecaster| **P02, P44** | Multi-horizon quantile forecasting, temporal attention maps| Quantile loss reduction $\ge 12\%$ vs LSTM at 6-month horizon |
| **Random Forest (Baseline)** | Static Ensemble Baseline | **P01, P06, P22** | Non-linear baseline resistant to overfitting | Benchmark control for Track 1 |
| **Logistic Regression ElasticNet (Control)**| Linear Baseline | **P01, P24** | Provable global optimum; verifies non-linear necessity | Control to establish whether tree ensembles provide statistically significant uplift ($p < 0.05$) |
| **LSTM with Attention (Baseline)** | Deep Recurrent Baseline | **P33, P44** | Standard established EDM sequence architecture | Benchmark control for Track 2 temporal attention |

**Anti-Hallucination Guard**: No model is declared superior prior to executing the Phase 08 pre-experimental protocol (`EXP-3`).

---

## 6. Model Serving, Versioning & Handoff Interfaces

### 6.1 Model Serving Architecture
- **Track 1 (XGBoost)**: Compiled into optimized ONNX computational graphs and served via ONNX Runtime inside lightweight CPU container workers (`CMP-MDL-XGB`).
- **Track 2 (TFT)**: Served via PyTorch Lightning / TorchScript inference service with optional GPU acceleration (`CMP-MDL-TFT`).

### 6.2 Model Registry & Provenance Schema
Every deployed model artifact in `REG-MDL` is cataloged with an immutable manifest:
```json
{
  "model_id": "prie-xgb-static-v2.1",
  "architecture": "XGBoost",
  "training_corpus": "DS-REAL-01 + DS-BENCH-01",
  "sample_size_n": 2215,
  "features_dimension": 22,
  "brier_score": 0.082,
  "validation_protocol": "EXP-3",
  "date_registered": "2026-09-17"
}
```

### 6.3 Explainability Handoff Contract
Upon generating prediction bundle $\mathcal{P} = \{P_{\text{ready}}, \text{Tier}, \hat{y}(q_{0.1..0.9})\}$, the engine immediately passes $\{\mathbf{x}_{\text{spv}}, \mathcal{P}\}$ to Module `M07`:
- For Tier 1 (`Ready`): Dispatch to `M07` for TreeSHAP positive factor reinforcement.
- For Tier 2 & 3 (`Needs Remediation`, `At-Risk`): Dispatch to `M07` for DiCE prescriptive counterfactual optimization and to `M12` for advisor alert dispatch.

---

## 7. Architectural Validation Plan Linkage

The prediction engine is directly tied to **`EXP-3`** defined in `Experimental_Decisions.md`:
- **Hypothesis H3**: Deep longitudinal sequence models (TFT) utilizing continuous telemetry achieve superior placement readiness prediction accuracy (Quantile Loss reduction $\ge 12\%$, $p < 0.01$) over static tabular models at 12-month and 6-month prediction horizons.
- **Statistical Falsification Test**: Diebold-Mariano test for predictive accuracy of time-series forecasts against static lagged XGBoost and standard LSTM baselines.
