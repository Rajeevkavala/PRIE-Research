# PRIE REPRODUCIBILITY & RESEARCH INTEGRITY CHARTER
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Epistemological Basis**: Phases 01–06 Methodology Specifications

---

## 1. Reproducibility Foundations

To ensure that independent academic researchers can reproduce all empirical claims, experiments, and benchmark evaluations, PRIE enforces the following foundational standards:

### A. Deterministic Seed Control
* All pseudorandom generators (NumPy `np.random.seed`, Python `random.seed`, Scikit-learn `random_state`, XGBoost `random_state`, PyTorch `torch.manual_seed`) are parameterized from a central configuration.
* Default baseline experimental runs use `SEED = 42`.
* Every experiment records the active seed in its `run_metadata.json`.

### B. Prevention of Data Leakage
1. **Preprocessing Leakage**: All standard scalers (`StandardScaler`), normalizers, and categorical encoders are fitted **strictly on training splits** ($X_{\text{train}}$) and only applied as transformations to validation, calibration, and test splits ($X_{\text{val}}, X_{\text{cal}}, X_{\text{test}}$).
2. **Resampling Leakage**: When synthetic oversampling (SMOTE) is applied to mitigate minority class imbalance, it is executed **exclusively within training folds**. Test and calibration sets maintain their natural empirical class distribution.
3. **Temporal & Group Leakage**: Student assessment records are grouped by unique student identifiers (`student_id`) using `GroupKFold` or chronological splits to prevent candidate identity leakage across cross-validation folds.

---

## 2. Zero-Fabrication Research Guarantee

1. **No Fabricated Benchmarks**: Benchmark datasets (`DS-BENCH-01`, `DS-BENCH-02`, `DS-REAL-01`) that are not locally present on a deployment machine are explicitly flagged as `DATASET NOT AVAILABLE`. The system never generates synthetic data and claims it to be empirical student observations.
2. **No Fabricated Model Accuracies**: Modules without completed model training (such as the LayoutLMv3 spatial token classifier) explicitly display `MODEL NOT TRAINED` and utilize rule-based research ablations rather than mocking artificial evaluation scores.
3. **No Fabricated User Outcomes**: The Digital Twin ($M_{12}$) and Prescriptive Counterfactual Recourse ($M_{07}$) engines explicitly state that their outputs are mathematical model simulations ($\mathbf{x} + \Delta \mathbf{x} \mapsto \hat{y}$), not guarantees of corporate hiring decisions.

---

## 3. Environment & Hardware Prerequisites

* **Operating System**: Windows 11 / Linux (Ubuntu 22.04+) / macOS
* **Python Runtime**: Python 3.10.x (Tested on Python 3.10.6 64-bit)
* **Core Scientific Libraries**:
  - `numpy >= 1.24.0`
  - `pandas >= 2.0.0`
  - `scipy >= 1.10.0`
  - `scikit-learn >= 1.3.0`
  - `xgboost >= 3.0.0`
  - `shap >= 0.45.0`
  - `optuna >= 3.6.0`
  - `dice-ml >= 0.11.0`
* **Signal & Multimodal Processing**:
  - `librosa >= 0.10.0`
  - `soundfile >= 0.12.0`
  - `opencv-python >= 4.9.0`
  - `faster-whisper >= 1.0.0`
* **Document & Spatial Extraction**:
  - `PyMuPDF (fitz) >= 1.23.0`
* **Backend & API Layer**:
  - `fastapi >= 0.110.0`
  - `uvicorn >= 0.28.0`
  - `pydantic >= 2.6.0`
  - `python-jose[cryptography] >= 3.3.0`
  - `passlib[bcrypt] >= 1.7.4`
* **Testing Framework**:
  - `pytest >= 8.0.0`
  - `httpx >= 0.27.0`
