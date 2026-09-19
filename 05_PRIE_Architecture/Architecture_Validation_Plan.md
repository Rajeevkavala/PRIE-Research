# Architecture Validation Plan: Multi-Dimensional Verification & Experimental Alignment

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Architecture_Validation_Plan.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Architecture Validation Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Validation Governance & Scope

In accordance with Section 39 of the Master Directive, this document establishes the formal validation protocols required to verify the correctness, reliability, and scientific defensibility of the PRIE Architecture.

**Methodological Boundary**:
Phase 05 **defines the validation plan and test harness specifications**. It does **NOT execute empirical experiments**, train production models, or fabricate test results. Empirical execution is reserved for **Phase 08 (Experiments)** and **Phase 09 (Results)**.

---

## 2. Multi-Dimensional Architectural Verification Dimensions

PRIE's architectural integrity is validated across eleven (11) rigorous verification dimensions:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ARCHITECTURAL VALIDATION DIMENSIONS                  │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. Functional     │ 2. Data Flow      │ 3. Component & API             │
│    Correctness    │    & Latency SLAs │    Contracts                   │
├───────────────────┼───────────────────┼────────────────────────────────┤
│ 4. Model Serving  │ 5. Explainability │ 6. Multimodal Perceptual       │
│    Integration    │    Verification   │    Pipeline                    │
├───────────────────┼───────────────────┼────────────────────────────────┤
│ 7. Ephemeral      │ 8. Failure &      │ 9. Differential Privacy &      │
│    Sandbox Safety │    Degradation    │    Zero-Trust Security         │
├───────────────────┼───────────────────┼────────────────────────────────┤
│ 10. Scalability   │ 11. Epistemological Experimental Alignment         │
│     & Caching     │     (Direct Linkage to EXP-1 through EXP-6)        │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 3. Detailed Verification Protocols

### 3.1 Dimension 1: Functional & Schema Correctness
- **Target**: The 22-dimensional Student Profile Vector (`M01`).
- **Test Protocol**:
  - Instantiate synthetic test vectors with extreme edge-case values (e.g., all zeros, all maxima, NaN entries, missing subject marks).
  - Assert that `CMP-INT-SPV` outputs an array of length exactly 22 with all values clamped to $[0.0, 1.0]$.
  - Verify that the binary confidence mask correctly tracks imputed vs observed features.
- **Pass Criteria**: 100% schema compliance; zero unexpected exceptions.

### 3.2 Dimension 2: Data Flow & Latency Budget Verification
- **Target**: Pipeline SLAs across synchronous and conversational flows.
- **Test Protocol**:
  - Instrument end-to-end tracing using OpenTelemetry across simulated requests.
  - Measure Voice-to-Voice Turn-Taking Latency across 100 mock interview dialogue turns (`CMP-MDL-ASR` + `CMP-MDL-LLM` + TTS).
  - Measure static placement inference latency on CPU (`CMP-MDL-XGB`).
- **Pass Criteria**:
  - Voice-to-voice turn-taking latency $\le 1,500$ms (P95).
  - Static XGBoost inference $\le 5$ms (P99).
  - TreeSHAP local attribution $\le 20$ms (P95).

### 3.3 Dimension 3: Component & API Contract Integration
- **Target**: OpenAPI 3.1 and gRPC interface schemas.
- **Test Protocol**:
  - Execute automated contract testing (Schemathesis / Dredd) against all endpoints defined in `API_Architecture.md`.
  - Validate RFC 7807 Problem Details error formats for rejected payloads.
- **Pass Criteria**: 100% contract compliance; zero untyped JSON responses.

### 3.4 Dimension 4: Model Serving & Versioning Integration
- **Target**: Model Registry (`REG-MDL`) and execution containers.
- **Test Protocol**:
  - Deploy quantized ONNX XGBoost, PyTorch TFT, and LayoutLMv3 artifacts.
  - Test model hot-reloading: update model version in registry while under synthetic load and verify zero dropped requests.
- **Pass Criteria**: Seamless version cutover; zero dropped requests.

### 3.5 Dimension 5: Explainability & Prescriptive Feasibility Verification
- **Target**: Two-Tiered Explainability Engine (`M07`).
- **Test Protocol**:
  - Verify that TreeSHAP satisfies the Efficiency Property: $\sum \phi_i = f(\mathbf{x}) - \mathbb{E}[f(X)]$.
  - Execute DiCE optimization across 100 test candidate profiles.
  - **Hard Constraint Audit**: Assert that `F17: branch_encoded` is modified in 0% of generated counterfactuals.
  - Assert that `F01: cgpa` never decreases ($\Delta_{\text{cgpa}} \ge 0.0$).
- **Pass Criteria**: 100% adherence to feature mutability constraints; convergence within $<3,000$ms.

### 3.6 Dimension 6: Multimodal Perceptual Integration
- **Target**: Document parsing (`M02`) and interview perception (`M05`).
- **Test Protocol**:
  - Feed synthetic multi-column PDF resumes into LayoutLMv3 worker; verify 2D bounding boxes prevent text interleaving.
  - Test client-side Wasm MediaPipe pipeline: verify that zero raw video frames transmit over the WebSocket connection.
- **Pass Criteria**: Zero video frames in server network capture; valid extracted scalar telemetry stream.

### 3.7 Dimension 7: Ephemeral Docker Sandbox Security
- **Target**: Code execution container manager (`CMP-INF-BOX`).
- **Test Protocol**:
  - Execute simulated adversarial code payloads (fork bombs, socket connection attempts, disk writes, infinite loops).
  - Verify that `--net=none` prevents external socket connections.
  - Verify that 5.0-second watchdog issues SIGKILL to infinite loops.
- **Pass Criteria**: Zero host system compromise; 100% clean container termination.

### 3.8 Dimension 8: Failure Handling & Graceful Degradation
- **Target**: The 10 failure modes defined in `Failure_Recovery_Architecture.md`.
- **Test Protocol**:
  - Chaos Engineering: Inject simulated faults (kill vLLM process, disconnect ChromaDB, trigger GPU OOM in LayoutLMv3).
  - Verify that circuit breakers trip and fallback models (CPU Tesseract, cloud SLM, Random Forest) engage cleanly.
- **Pass Criteria**: Zero uncaught 500 exceptions; transparent fallback advisories delivered to client.

### 3.9 Dimension 9: Differential Privacy & Zero-Trust Security
- **Target**: Differential Privacy Proxy (`CMP-GW-PRIV`).
- **Test Protocol**:
  - Execute 500 automated aggregate queries against simulated candidate databases.
  - Verify Laplace noise injection conforms to $\epsilon \le 1.0$.
  - Conduct simulated Membership Inference Attack: verify that individual student membership cannot be determined with probability greater than random baseline $+ \epsilon$.
- **Pass Criteria**: Privacy budget $\epsilon_{\text{total}} \le 1.0$ strictly enforced; attack success bounded.

### 3.10 Dimension 10: Scalability & Caching Efficiency
- **Target**: Redis caching and asynchronous queue offloading.
- **Test Protocol**:
  - Simulate 500 concurrent student profile view requests using Locust.
  - Measure Redis cache hit ratio for pre-computed SPV vectors and concept DAG traversals.
- **Pass Criteria**: Cache hit ratio $\ge 85\%$; P95 response time under load $\le 150$ms.

---

## 4. Master Linkage to Phase 08 Pre-Experiments (EXP-1 to EXP-6)

The architectural validation plan interfaces directly with the six pre-experimental protocols codified in Phase 04:

```
┌────────────────────────────────────────────────────────────────────────┐
│           PRE-EXPERIMENTAL ALIGNMENT MATRIX (PHASE 05 -> PHASE 08)     │
├─────────┬──────────────┬──────────────┬────────────────────────────────┤
│ EXP ID  │ TARGET RQ/H  │ PRIE MODULE  │ ARCHITECTURAL VERIFICATION HOOK│
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-1   │ RQ1 / H1     │ M02 (ATS)    │ LayoutLMv3 2D Spatial OCR vs   │
│         │              │              │ Flat-Text Tesseract + SpaCy    │
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-2   │ RQ2 / H2     │ M05 (Mock)   │ Sub-1.5s Streaming Whisper vs  │
│         │              │              │ Cloud Sequential API Pipeline  │
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-3   │ RQ3 / H3     │ M06 (Predict)│ Longitudinal TFT Sequence vs   │
│         │              │              │ Static Tabular XGBoost / LSTM  │
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-4   │ RQ4 / H4     │ M07 (XAI)    │ Prescriptive DiCE Counterfact  │
│         │              │              │ vs Descriptive TreeSHAP Only   │
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-5   │ RQ5 / H5     │ M10 (AQG)    │ Causal Concept DAG CoT AQG vs  │
│         │              │              │ Unconstrained LLM Prompting    │
├─────────┼──────────────┼──────────────┼────────────────────────────────┤
│ EXP-6   │ RQ6 / H6     │ M12 (Twin)   │ Closed-Loop Triangular Twin vs │
│         │              │              │ Disconnected Status Quo Tools  │
└─────────┴──────────────┴──────────────┴────────────────────────────────┘
```

**Verification Guarantee**: By architecting explicit measurement hooks, model registries, and baseline controls into every subsystem, PRIE ensures that Phase 08 experiments can be executed rigorously, reproducibly, and without redesigning the system.
