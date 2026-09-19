# Reproducibility Methodology: Environment Specifications, Dependency Lockfiles & Artifact Tracking

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Reproducibility.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Reproducibility Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Five Pillars of Scientific Reproducibility

To ensure any independent research group can replicate PRIE's experimental results with identical outputs, reproducibility is guaranteed across five operational tiers:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          REPRODUCIBILITY ARCHITECTURE                           │
├───────────────────┬─────────────────────────────────────────────────────────────┤
│ Dimension         │ Technical Realization & Verification Mechanism              │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ 1. Code Base      │ Git repository versioning with immutable semantic commit    │
│                   │ hashes; complete separation of library code and experiments │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ 2. Datasets       │ Data Version Control (DVC) paired with SHA-256 integrity    │
│                   │ manifests for raw and preprocessed splits                   │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ 3. Environment    │ Containerized Docker images with pinned multi-stage builds; │
│                   │ lockfiles for Python (uv.lock / poetry.lock)                │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ 4. Determinism    │ Global pseudo-random number generator (RNG) seeding         │
│                   │ enforced across Python, NumPy, PyTorch, and XGBoost         │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ 5. Artifacts      │ Trained model checkpoints serialized to standardized ONNX   │
│                   │ format accompanied by JSON configuration manifests          │
└───────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 2. Pinned Hardware & Software Specifications

### 2.1 Hardware Reference Baseline
- **Compute Server**: 1x AMD EPYC 7763 (64 cores, 128 threads @ 2.45 GHz).
- **GPU Accelerator**: 1x NVIDIA RTX 4090 (24 GB GDDR6X VRAM, CUDA Compute Capability 8.9).
- **System Memory**: 128 GB DDR4-3200 ECC Registered RAM.
- **Storage Subsystem**: 2 TB NVMe PCIe 4.0 SSD (Read: 7,000 MB/s, Write: 5,000 MB/s).

### 2.2 Software Environment Baseline
- **Operating System**: Ubuntu 22.04.4 LTS (Linux Kernel 5.15.0-105-generic).
- **CUDA Toolkit Version**: CUDA 12.1 with cuDNN 8.9.2.
- **Python Runtime**: CPython 3.10.14.
- **Core Library Lockfile**:
  - `torch==2.3.0+cu121`
  - `xgboost==2.0.3`
  - `lightgbm==4.3.0`
  - `pytorch-forecasting==1.0.0`
  - `transformers==4.40.2`
  - `shap==0.45.1`
  - `dice-ml==0.11`
  - `optuna==3.6.1`
  - `chromadb==0.5.0`
  - `sentence-transformers==2.7.0`
