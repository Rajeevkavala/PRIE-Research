# Randomness and Seeds Methodology: Stochastic Controls & Non-Deterministic Boundaries

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Randomness_and_Seeds.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Stochastic Control Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Inventory of Stochastic Pipeline Stages

To guarantee full replicability, all sources of pseudo-randomness across the PRIE pipeline are formally cataloged and bound to deterministic seeds:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          STOCHASTIC STAGES INVENTORY                            │
├────┬─────────────────────┬──────────────────────┬───────────────────────────────┤
│ ID │ Pipeline Stage      │ Stochastic Library   │ Global Seed Parameter         │
├────┼─────────────────────┼──────────────────────┼───────────────────────────────┤
│ S1 │ Synthetic SPV Gen   │ NumPy / SciPy        │ RNG_SEED = 42                 │
│ S2 │ Dataset Partition   │ Scikit-Learn         │ random_state = 42             │
│ S3 │ In-Fold SMOTE       │ Imbalanced-Learn     │ random_state = 42             │
│ S4 │ XGBoost Boosting    │ XGBoost Native       │ seed = 42                     │
│ S5 │ Neural Training     │ PyTorch / PyTorch-LC │ torch.manual_seed(42)         │
│ S6 │ Optuna TPE Search   │ Optuna Sampler       │ seed = 42                     │
│ S7 │ DiCE Optimization   │ DiCE ML Surrogates   │ random_state = 42             │
└────┴─────────────────────┴──────────────────────┴───────────────────────────────┘
```

---

## 2. Master Deterministic Initialization Script

Every execution worker executes the following initialization hook prior to importing analytical modules:
```python
import os
import random
import numpy as np
import torch

def set_global_deterministic_seed(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
```

---

## 3. Irreducible Sources of Non-Determinism

> [!NOTE]
> **SCIENTIFIC HONESTY: IRREDUCIBLE VARIABILITY BOUNDARIES**  
> While pseudo-random seeds eliminate algorithm-level variance, modern GPU architectures and cloud LLMs introduce two minor irreducible sources of non-determinism:
> 1. **GPU Atomic Operations**: CUDA parallel reduction operations (e.g., `torch.bmm`, sparse gradient scatter) can introduce floating-point rounding variations at the order of $10^{-7}$.
> 2. **External Cloud LLM Endpoints**: External commercial APIs (e.g., GPT-4o) do not guarantee bitwise reproducible token generation even with `temperature = 0.0`. For this reason, all core benchmark evaluations in PRIE run strictly on **local quantized models** (`Llama-3-8B` via vLLM) with greedy decoding (`temperature = 0.0`, `top_p = 1.0`).
