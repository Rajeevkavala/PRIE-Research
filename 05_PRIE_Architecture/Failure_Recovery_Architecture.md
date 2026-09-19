# Failure & Recovery Architecture: Fault Tolerance, Fallback Modes & Graceful Degradation

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Failure_Recovery_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Failure & Recovery Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Resilience Principles

The Failure & Recovery Architecture defines how PRIE detects, isolates, and recovers from runtime faults across all layers.

**Core Resilience Principles**:
1. **Graceful Degradation over Hard Failure**: When an advanced machine learning component (e.g., LayoutLMv3 or TFT) experiences a fault, the system must degrade to a simpler, verified fallback (e.g., linear OCR or static XGBoost) rather than returning a blank screen or crashing.
2. **Circuit Breaking & Timeout Bounding**: External service integrations and heavy optimization solvers enforce strict timeout deadlines to prevent thread exhaustion.
3. **Data Protection Integrity**: A failure in perception or analytical pipelines must never corrupt persistent student records in `SPV-DB`.
4. **Transparent User Advisories**: The user interface clearly communicates when a fallback model is being served, preserving scientific and operational transparency.

---

## 2. Failure Recovery Matrix across Critical Subsystems

| # | Failure Scenario | Detection Mechanism | Immediate Fallback Action | Graceful Degradation Behavior | User-Visible Behavior | Recovery Procedure |
|:---:|:---|:---|:---|:---|:---|:---|
| **1** | **XGBoost Inference Worker Down** (`CMP-MDL-XGB`) | Container health check failure; gRPC timeout $>50$ms. | Route SPV tensor to embedded in-process Random Forest baseline model (`DD-002`). | Non-linear ensemble score served with baseline accuracy ($\approx 88\%$). | Score presented with subtitle: *"Calculated using baseline ensemble."* | Automated container restart via Docker/K8s liveness probe. |
| **2** | **Temporal Fusion Transformer (TFT) Sequence Failure** | PyTorch worker OOM or missing multi-semester history. | Fallback to Track 1 static XGBoost model with lagged delta features. | Omit multi-horizon quantile forecast; serve static readiness probability. | Longitudinal chart replaced with static tier card and message: *"Historical sequence unavailable."* | Log sequence gap; re-queue historical ingestion worker. |
| **3** | **Local LLM Inference Crash** (vLLM Llama-3-8B) | HTTP 500 from vLLM endpoint; heartbeat timeout $>1.0$s. | Circuit breaker trips; reroute prompt to cloud frontier fallback API (Gemini 1.5 Flash). | Conversational interview continues; turnaround latency increases from $1.1$s to $2.2$s. | Negligible UI disruption; slightly longer conversational turn latency. | Watchdog restarts vLLM process; reload model weights into VRAM. |
| **4** | **ChromaDB Vector Store Unavailable** | Connection refused on port 8000; query timeout $>200$ms. | Fallback to local in-memory SQLite keyword / BM25 inverted index for curriculum and JDs. | Semantic synonym matching disabled; uses exact lexical keyword matching. | Search results tagged: *"Lexical match active; semantic search temporarily offline."* | Reconnect to ChromaDB container; trigger HNSW index integrity check. |
| **5** | **LayoutLMv3 GPU OOM / Parsing Crash** | CUDA Out-of-Memory exception; token parsing error. | Divert resume binary to CPU-based Tesseract OCR + SpaCy NER pipeline. | Flat text parsing executed; 2D spatial layout bounding boxes unavailable. | Resume parsed; warning displayed: *"Multi-column formatting disabled; verify extracted skills."* | Reset GPU memory buffer; re-size maximum page rendering resolution. |
| **6** | **Streaming Audio / Whisper Failure** | WebSocket frame drops; audio decoder exception. | Switch interview session to text-based technical chat mode. | Verbal interview disabled; candidate types answers in real-time chat window. | UI displays alert: *"Microphone connection interrupted; continuing in text-chat mode."* | Re-initialize audio worklet and WebSocket handshake. |
| **7** | **Client Wasm MediaPipe Crash** | Browser JavaScript exception; Wasm execution halted. | Disable non-verbal visual telemetry; continue interview purely via audio speech stream. | `F20: behavior_score` set to neutral cohort median ($0.65$); paralinguistic analysis omitted. | Video canvas shows neutral placeholder: *"Video tracking paused; audio interview active."* | Reload client Wasm module on next interview question turn. |
| **8** | **Docker Code Sandbox Timeout / Infinite Loop** | Container execution watchdog exceeds 5.0 seconds (`DD-006`). | Host daemon issues `SIGKILL` to container; cleanup temporary volume mount. | Mark code submission as "Execution Timeout (Infinite Loop / Time Limit Exceeded)". | Student sees code editor error: *"Execution terminated: Time Limit Exceeded (>5.0s)."* | Ephemeral container pruned automatically; fresh sandbox spawned for next run. |
| **9** | **DiCE Prescriptive Solver Timeout** | Gradient optimization fails to converge within 3.0 seconds. | Abort optimization loop; retrieve nearest pre-computed **Cohort Archetype Counterfactual**. | Serves generalized standard remediation roadmap based on candidate's skill deficit cluster. | Roadmap displays: *"Standard Remediation Roadmap (Personalized optimization timed out)."* | Log non-converging feature sub-space for algorithmic hyperparameter tuning. |
| **10**| **External SIS Registrar API Failure** | Connection timeout $>5.0$s during student onboarding sync. | Read cached academic profile from local `SPV-DB`; lock semester GPA update. | Student accesses platform using existing transcript data; fresh sync deferred. | Advisor dashboard shows notification: *"SIS synchronization delayed; showing cached records."* | Exponential backoff retry worker polls SIS API every 15 minutes until restored. |

---

## 3. Circuit Breaker & Health Check Specifications

All internal microservice communication through the API Gateway (`CMP-GW-ROUT`) is guarded by **Hystrix-pattern Circuit Breakers**:

```
           ┌────────────────────────┐
           │     CLOSED STATE       │◄────────────────────────┐
           │ (Normal Service Flow)  │                         │
           └───────────┬────────────┘                         │
                       │ Failure Rate > 20%                   │ 5 Consecutive
                       │ or Timeout > 500ms                   │ Successful Probes
                       ▼                                      │
           ┌────────────────────────┐                         │
           │       OPEN STATE       │                         │
           │ (Direct to Fallback)   │                         │
           └───────────┬────────────┘                         │
                       │ Sleep Window (30s) Expired           │
                       ▼                                      │
           ┌────────────────────────┐                         │
           │    HALF-OPEN STATE     │─────────────────────────┘
           │ (Probe Single Request) │
           └────────────────────────┘
```

- **Thresholds**: If any machine learning worker exhibits a $>20\%$ failure rate over a rolling 60-second window, the circuit breaker opens, immediately routing all subsequent requests to the lightweight baseline model without waiting for timeouts.
- **Health Check Endpoints**: Every worker exposes `GET /health/liveness` and `GET /health/readiness` queried every 10 seconds by the orchestration daemon.
