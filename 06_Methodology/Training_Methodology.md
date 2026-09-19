# Training Methodology: Convergence Criteria, Checkpointing & Serialization Protocols

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Training_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Training Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. End-to-End Training Lifecycle

The model training pipeline transitions systematically across six stages, ensuring reproducibility, artifact provenance, and leak-free convergence:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MODEL TRAINING LIFECYCLE                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│  STAGE 1: HARDWARE PROVISIONING & DETERMINISTIC SEEDING                         │
│  • Hardware environment locked (1x NVIDIA RTX 4090 / 24GB VRAM)                 │
│  • Deterministic random seeds enforced (Python=42, NumPy=42, Torch=42, XGB=42)  │
│                                                                                 │
│  STAGE 2: TRAINING DATA INGRESS & IN-FOLD PREPROCESSING                         │
│  • Ingestion of 80% Training partition                                         │
│  • In-fold fitting of MICE Imputer, RobustScaler, and SMOTE                     │
│                                                                                 │
│  STAGE 3: ITERATIVE GRADIENT OPTIMIZATION & EARLY STOPPING                      │
│  • XGBoost: Max 1000 rounds with early stopping patience = 30 rounds            │
│  • TFT: AdamW optimizer, cosine annealing learning schedule, patience = 15     │
│                                                                                 │
│  STAGE 4: CHECKPOINTING & METRIC LOGGING                                        │
│  • Epoch-by-epoch loss tracking logged to MLflow                                │
│  • State dict checkpoints saved upon validation PR-AUC improvement              │
│                                                                                 │
│  STAGE 5: PROBABILITY CALIBRATION & FREEZING                                    │
│  • In-fold Isotonic Regression fitted on validation predictions                 │
│                                                                                 │
│  STAGE 6: STANDARDIZED SERIALIZATION & REGISTRATION                             │
│  • Model artifacts serialized to ONNX / TorchScript with SHA-256 signatures     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Early Stopping & Convergence Criteria

To prevent overfitting on limited student cohorts:
- **XGBoost Early Stopping**: Monitored on inner validation fold `logloss`. If validation loss does not improve for 30 consecutive trees, boosting terminates.
- **TFT Early Stopping**: Monitored on validation `QuantileLoss`. If validation loss fails to decrease by at least $\Delta = 10^{-4}$ for 15 consecutive epochs, training terminates.
- **Gradient Clipping**: For neural sequence models (TFT, LSTM), gradient norms are clipped to $\|\mathbf{g}\|_2 \le 0.5$ to prevent gradient explosion during multi-horizon backpropagation.

---

## 3. Artifact Serialization & Model Governance

1. **ONNX Export**: All trained models are exported to Open Neural Network Exchange (ONNX) format with fixed dynamic batch dimension axes, enabling high-performance, language-agnostic inference across Python and Go runtimes.
2. **Cryptographic Manifest**: Every saved model artifact is registered with an immutable JSON provenance manifest containing:
   - Git commit hash of the training repository.
   - DVC dataset hash and version tag.
   - Full hyperparameter configuration dictionary.
   - SHA-256 cryptographic checksum of the `.onnx` model weights.
