# Model Serving Architecture: Runtime Deployment, Hardware Allocation & MLOps Lifecycle

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Model_Serving_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Model Serving Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Serving Principles

The Model Serving Architecture bridges the gap between research training environments and reliable low-latency operational serving.

**Core Principles**:
1. **Separation of Model Lifecycle Tiers**: Explicitly decouples Research Models (exploratory scripts), Prototype Models (Phase 08 experimental candidates), and Production Serving Models.
2. **Right-Sized Hardware Provisioning**: Heavy GPU instances are reserved strictly for architectures that require them (LayoutLMv3, vLLM, TFT), while high-throughput tabular models (XGBoost, TreeSHAP, SBERT) execute on low-cost, CPU-optimized containers.
3. **Edge-First Client Execution**: Client-side execution via WebAssembly (`MediaPipe FaceMesh`) offloads vision processing entirely from central server clusters (`DD-005`).

---

## 2. Global Model Serving Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. TRAINING & EXPERIMENTAL ENVIRONMENT (Offline / Batch)               │
│ • PyTorch Lightning / XGBoost Training Pipeline                        │
│ • Datasets: DS-REAL-01, DS-BENCH-01, DS-CORPUS-01, DS-SYNTH-01        │
│ • Quantization & Optimization (ONNX FP16 / AWQ 4-Bit)                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Export Validated Artifacts
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. MODEL REGISTRY & ARTIFACT REPOSITORY (REG-MDL)                      │
│ • Semantic Versioning: `prie-xgb-v2.1.onnx`, `prie-tft-v1.0.pt`        │
│ • Signed Manifest: Hyperparameters, Training Hash, Brier Score, EXP ID│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Deploy Verified Artifacts
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. HETEROGENEOUS MODEL SERVING WORKERS (Layer 4)                       │
│                                                                        │
│ ┌──────────────────────────────────┐ ┌───────────────────────────────┐ │
│ │ CPU-OPTIMIZED WORKERS (Fast/Light│ │ GPU-ACCELERATED WORKERS       │ │
│ ├──────────────────────────────────┤ ├───────────────────────────────┤ │
│ │ • CMP-MDL-XGB: ONNX Runtime CPU  │ │ • CMP-MDL-DOC: LayoutLMv3 FP16│ │
│ │   (Latency < 5ms, Memory 25MB)   │ │   (HuggingFace, VRAM 2.5GB)   │ │
│ │ • CMP-MDL-SHP: TreeSHAP C++ Lib  │ │ • CMP-MDL-TFT: PyTorch TFT    │ │
│ │   (Latency < 15ms, Memory 40MB)  │ │   (Inference < 80ms, VRAM 2GB)│ │
│ │ • CMP-MDL-SEM: SBERT all-MiniLM  │ │ • CMP-MDL-LLM: vLLM Llama-3-8B│ │
│ │   (Latency < 20ms, Memory 120MB) │ │   (AWQ 4-Bit, VRAM 6.5GB)     │ │
│ │ • CMP-MDL-CF: DiCE Solver Worker │ │ • CMP-MDL-ASR: Whisper-Small  │ │
│ │   (Latency < 1500ms, Memory 80MB)│ │   (whisper.cpp, VRAM 1.5GB)   │ │
│ └──────────────────────────────────┘ └───────────────────────────────┘ │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Telemetry & Drift Signals
┌───────────────────────────────────▼────────────────────────────────────┐
│ 4. OBSERVABILITY & MODEL MONITORING PIPELINE                           │
│ • Latency Tracking & P99 SLA Enforcement                               │
│ • Population Stability Index (PSI) & Kolmogorov-Smirnov (KS) Drift     │
│ • Prediction Distribution & Calibration Divergence Alerts              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Subsystem Model Allocation & Hardware Quotas

| Model Worker | Underlying Model Architecture | Framework / Runtime | Target Hardware | Latency SLA (P95) | Memory Footprint |
|:---|:---|:---|:---|:---:|:---:|
| **`CMP-MDL-XGB`** | XGBoost GBDT (22 features) | ONNX Runtime (CPU) | 0.5 vCPU | $<5$ ms | $\sim 25$ MB |
| **`CMP-MDL-SHP`** | TreeSHAP exact attribution | C++ Extension | 0.5 vCPU | $<15$ ms | $\sim 40$ MB |
| **`CMP-MDL-SEM`** | Sentence-BERT (`all-MiniLM-L6-v2`)| PyTorch / ONNX | 1.0 vCPU | $<20$ ms | $\sim 120$ MB |
| **`CMP-MDL-CF`** | DiCE constraint optimizer | PyTorch (CPU) | 1.0 vCPU | $<1,500$ ms | $\sim 80$ MB |
| **`CMP-MDL-TFT`** | Temporal Fusion Transformer | PyTorch Lightning | 1x NVIDIA T4 / A10G | $<80$ ms | $\sim 2.0$ GB VRAM |
| **`CMP-MDL-DOC`** | LayoutLMv3 (Spatial OCR) | Transformers FP16 | 1x NVIDIA T4 / A10G | $<450$ ms | $\sim 2.5$ GB VRAM |
| **`CMP-MDL-ASR`** | Whisper ASR (Streaming) | whisper.cpp / PyTorch | 1x NVIDIA T4 / CPU | $<250$ ms / chunk| $\sim 1.5$ GB VRAM |
| **`CMP-MDL-LLM`** | Llama-3-8B-Instruct | vLLM Engine (AWQ 4-bit)| 1x NVIDIA A10G (24GB) | $<350$ ms TTFT | $\sim 6.5$ GB VRAM |
| **`Client Perceiver`**| MediaPipe FaceMesh (468 pts) | Browser WebAssembly | Client Device CPU/GPU| 30 FPS real-time | Zero Server VRAM |

---

## 4. Model Lifecycle & Version Governance

### 4.1 Tier Separation: Research vs Prototype vs Production
1. **Research Model (Phase 01–04)**:
   - Exploratory Jupyter notebooks and scripts used to analyze public datasets (`DS-BENCH-01`, `DS-BENCH-02`).
   - Purpose: Validating literature claims, inductive biases, and feature correlations.
   - Execution: Local researcher workstation; zero production network access.
2. **Prototype Model (Phase 08 Pre-Experiments)**:
   - Formally versioned candidates evaluated against experimental controls (`EXP-1` to `EXP-6`).
   - Purpose: Falsifying or validating Hypotheses **`H1`–`H6`**.
   - Execution: Isolated staging environment on stratified institutional cohorts.
3. **Production Model (Phase 07 Deployment)**:
   - Compiled, quantized, and hardened model binaries registered in `REG-MDL`.
   - Purpose: Serving live student placement preparation with deterministic SLAs.

### 4.2 Automated Drift Detection & Continuous Quality Monitoring
The model observability pipeline (`CMP-INF-OBS`) monitors live inference streams:
- **Concept Drift**: Evaluates the Kolmogorov-Smirnov ($KS$) two-sample test comparing live student feature distributions $\mathbf{x}_{\text{live}}$ against training baseline distributions $\mathbf{x}_{\text{train}}$.
- **Population Stability Index (PSI)**:
  $$\text{PSI} = \sum_{j=1}^B \big( \% \text{Actual}_j - \% \text{Expected}_j \big) \times \ln\left( \frac{\% \text{Actual}_j}{\% \text{Expected}_j} \right)$$
  - $\text{PSI} < 0.10$: Stable; no action.
  - $0.10 \le \text{PSI} \le 0.25$: Marginal shift; triggers advisor notification.
  - $\text{PSI} > 0.25$: Significant population drift (e.g., changes in university grading schema); triggers model retraining alert.
