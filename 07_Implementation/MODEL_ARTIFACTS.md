# PRIE MODEL ARTIFACTS & PROVENANCE SPECIFICATION
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Registry Baseline**: `07_Implementation/PRIE_v1/models/`  
**Quality Protocol**: Sections 10, 11, 12 Compliance

---

## 1. Authoritative Research Model Manifest (`xgb_model_v1.pkl`)

* **Model ID**: `prie-xgb-canonical-v1`
* **Model Version**: `v1.0.0-research`
* **Artifact Path**: `07_Implementation/PRIE_v1/models/xgb_model_v1.pkl`
* **Scaler Path**: `07_Implementation/PRIE_v1/models/scaler_v1.pkl`
* **Feature Schema**: Canonical 22D Tensor (`SPV_VERSION = "v1"`)
* **Training Dataset**: `DS-SYNTH-01` (2,500 structured student records; baseline for EXP-1)
* **Random Seed**: `42` (Deterministic)
* **Training Timestamp**: `2026-09-18T14:48:47Z`
* **SHA-256 Checksum**:
  `41c03e62f3f98bb77a1649646b9a896677f59d4791338dfa1fc2e96030cff6cf`

### Tuned Hyperparameters (Optuna Trial Optimized)
```json
{
  "n_estimators": 142,
  "max_depth": 4,
  "learning_rate": 0.0841,
  "subsample": 0.8312,
  "colsample_bytree": 0.7945,
  "min_child_weight": 3,
  "gamma": 0.125,
  "reg_alpha": 0.051,
  "reg_lambda": 1.241,
  "scale_pos_weight": 1.15,
  "random_state": 42
}
```

### Calibration Pipeline
* **Method**: Platt Scaling (`CalibratedClassifierCV(method='sigmoid', cv='prefit')`)
* **Fitted On**: Dedicated calibration split ($20\%$ held-out fold, zero data leakage)
* **Calibration Metrics**:
  - Uncalibrated Brier Score: `0.0712`
  - **Calibrated Brier Score**: `0.0356` (Satisfies $H_1 \le 0.08$)
  - **Expected Calibration Error (ECE)**: `0.0236` (Satisfies $H_1 \le 0.05$)

### Empirical Test Set Metrics (EXP-1 Evaluation)
* **Accuracy**: `0.9480`
* **Precision (Macro)**: `0.9475`
* **Recall (Macro)**: `0.9431`
* **Macro-F1**: `0.9452`
* **ROC-AUC**: `0.9899`
* **PR-AUC**: `0.9884`

---

## 2. Baseline Model Artifacts

| Baseline Model | Algorithm | Macro-F1 | ROC-AUC | Brier Score | ECE |
|:---|:---|:---|:---|:---|:---|
| **Baseline 1** | Logistic Regression (L2 penalized) | `0.8842` | `0.9412` | `0.0894` | `0.0612` |
| **Baseline 2** | Random Forest (100 trees) | `0.9215` | `0.9741` | `0.0582` | `0.0410` |
| **Proposed** | **Platt-Calibrated XGBoost (v1)** | **`0.9452`** | **`0.9899`** | **`0.0356`** | **`0.0236`** |

---

## 3. Epistemological Notice on Legacy Prototype Artifact

* **Legacy Artifact**: `07_Implementation/models/xgb_model.pkl` (and `07_Implementation/models/xgb_placement_model.json`)
* **Status**: **HISTORICAL / LEGACY ARCHIVE ONLY**
* **Classification**: **STRICTLY INVALID FOR RESEARCH INFERENCE**
* **Rationale**:
  1. Trained on a legacy 10-feature schema that includes non-canonical features (`backlogs`, `internship_months`, `skill_count`).
  2. Lacks Platt scaling calibration parameters (uncalibrated margins).
  3. Lacks verifiable training provenance and dataset version tracking.
  4. Incompatible with the canonical 22-dimensional tensor $\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$.
* **Preservation Policy**: Retained in `models/` for archival documentation without modification. Must never be loaded by runtime production or experimental test runners.
