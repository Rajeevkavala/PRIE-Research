# Architecture Constraints: Scientific, Computational, Latency & Regulatory Boundaries

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Architecture_Constraints.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Architecture Constraints Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Governance & Constraint Classification

The Architecture Constraints define the non-negotiable boundaries within which PRIE must be architected, implemented, and validated. These constraints are categorized into six orthogonal domains:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ARCHITECTURAL CONSTRAINTS                       │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. RESEARCH &     │ 2. DATASET &      │ 3. COMPUTATIONAL &             │
│    EPISTEMOLOGICAL│    EVIDENTIARY    │    INFRASTRUCTURE              │
├───────────────────┼───────────────────┼────────────────────────────────┤
│ 4. LATENCY &      │ 5. PRIVACY &      │ 6. REPRODUCIBILITY &           │
│    PERFORMANCE    │    REGULATORY     │    METHODOLOGICAL              │
└───────────────────┴───────────────────┴────────────────────────────────┘
```

---

## 2. Exhaustive Constraint Specifications

### 2.1 Domain 1: Research & Epistemological Constraints
- **C-RES-01 (Strict SPV Dimensionality Invariance)**: The baseline Student Profile Vector must contain **exactly 22 features** (`F01` through `F22`). No dimension may be silently added or omitted. Any proposed future feature must be labeled `PROPOSED — NOT PART OF BASELINE SPV`.
- **C-RES-02 (Subsystem Invariance)**: All twelve functional modules (`M01` through `M12`) established in Phase 04 must be accounted for without arbitrary re-naming or consolidation.
- **C-RES-03 (Source Hierarchy Precedence)**: The epistemological hierarchy (Level 1 Primary Literature $\to$ Level 2 Notes $\to$ Level 3 Cross-Analysis $\to$ Level 4 Problem Formulation $\to$ Level 5 Evidence $\to$ Level 6 Implementation) is absolute. Existing codebase implementation (Level 6) **cannot override** validated research decisions.
- **C-RES-04 (The Non-Fabrication Rule)**: Under no circumstances may citations, benchmark accuracies, $p$-values, or institutional study results be fabricated. If a parameter or metric is unverified, it must be explicitly labeled `VALIDATION REQUIRED` or `PROPOSED`.

---

### 2.2 Domain 2: Dataset & Evidentiary Constraints
- **C-DAT-01 (Public Benchmark Segregation)**:
  - Public benchmark datasets (`DS-BENCH-01`: Kaggle Campus Placement, $N=215$; `DS-BENCH-02`: OULAD, $N=32,593$) may be used strictly for baseline model calibration and hyperparameter search.
- **C-DAT-02 (Synthetic Data Disclosure)**:
  - Synthetic student cohorts (`DS-SYNTH-01`, $N=2,500$) generated via Gaussian Copulas and SMOTE (`DD-012`) must be **explicitly labeled as synthetic in all documentation and evaluation reports**. They may never be presented as empirical proof of real-world efficacy.
- **C-DAT-03 (Institutional Data Staging)**:
  - The prospective institutional cohort (`DS-REAL-01`, target $N \ge 1,000$) is recognized as **"Proposed — Not Yet Collected"**. Architecture must not assume historical multi-year records are available without formal registrar ingestion.

---

### 2.3 Domain 3: Computational & Hardware Constraints
- **C-CMP-01 (On-Premise Privacy Isolation)**:
  - All core machine learning models processing student transcripts, resumes, and code (`LayoutLMv3`, `Sentence-BERT`, `XGBoost`, `TreeSHAP`, `Llama-3-8B`) must be executable **on local on-premise infrastructure**. Transmitting confidential student data to commercial closed APIs (e.g., OpenAI API, Anthropic API) is strictly prohibited.
- **C-CMP-02 (Docker Sandbox Hardware Caps)**:
  - Every ephemeral code execution container (`DD-006`) is subject to hard cgroup constraints:
    - Maximum Memory: $128$ MB.
    - Maximum CPU: $0.5$ cores.
    - Maximum Processes: $64$ PIDs.
    - Networking: Disabled (`--net=none`).
    - Root Filesystem: Read-only.
    - Execution Timeout: $5.0$ seconds (enforced by host SIGKILL).
- **C-CMP-03 (Client-Side Video Offloading)**:
  - Computer vision facial landmark tracking (`MediaPipe FaceMesh`) must run exclusively client-side in the browser via WebAssembly (`DD-005`). Server infrastructure is forbidden from ingesting raw video streams.

---

### 2.4 Domain 4: Latency & Real-Time Performance Constraints
- **C-LAT-01 (Voice Turn-Taking SLA)**:
  - In multimodal mock technical interviews (`M05`), total voice-to-voice turn-taking latency (from the moment student speech ceases to the first synthesized audio playback) must be **strictly bounded to $<1,500$ milliseconds** (`DD-005`).
- **C-LAT-02 (Static Tabular Scoring SLA)**:
  - Static cross-sectional placement readiness scoring (`XGBoost` via ONNX Runtime) must complete in **$<5$ milliseconds** per profile.
- **C-LAT-03 (TreeSHAP Local Attribution SLA)**:
  - Exact cooperative game-theoretic feature attribution must execute in **$<20$ milliseconds** per student profile.
- **C-LAT-04 (DiCE Counterfactual Optimization Timeout)**:
  - Prescriptive counterfactual search must converge within **$<3,000$ milliseconds**. If convergence is not achieved, the engine must gracefully fall back to pre-computed archetype counterfactuals.

---

### 2.5 Domain 5: Privacy, Security & Regulatory Constraints
- **C-PRV-01 (Zero Raw Media Retention)**:
  - Raw audio and video recordings of candidate mock interviews must **never be permanently persisted to storage media** (`DD-005`, `DD-011`). Audio buffers in server RAM must be cleared immediately post-transcription.
- **C-PRV-02 (Differential Privacy Budget Enforcement)**:
  - All analytical cohort queries surfaced to corporate recruiters and public placement dashboards must pass through the Laplace Mechanism with a privacy budget parameter:
    $$\epsilon \le 1.0$$
- **C-PRV-03 (Immutable Feature Locking in Recourse)**:
  - In prescriptive explainability (`M07`), immutable demographic features (`F17: branch_encoded`) must be mathematically locked. Recommendations suggesting changes to immutable attributes are strictly prohibited.
- **C-PRV-04 (Regulatory Disclaimer)**:
  - All architecture specifications and interfaces must include explicit notices that live deployment requires formal institutional compliance verification under POPIA, FERPA, and regional educational privacy laws.

---

### 2.6 Domain 6: Reproducibility & Methodological Constraints
- **C-REP-01 (Deterministic Pseudo-Random Initialization)**:
  - All stochastic training, sampling, cross-validation splits, and copula generation must initialize with fixed random seeds:
    $$\text{seed} = 42$$
- **C-REP-02 (Falsifiable Pre-Experimental Alignment)**:
  - Architecture decisions must map one-to-one to the pre-experimental designs established in Phase 04 (`EXP-1` through `EXP-6`). The architecture must support empirical refutation of Hypotheses **`H1`–`H6`** in Phase 08.
- **C-REP-03 (Temporal Look-Ahead Leakage Guard)**:
  - Telemetry features (`consistency_score`, `assessment_attempts`, `roadmap_completion_rate`) evaluated in historical training folds must be computed strictly prior to the simulated prediction timestamp, preventing look-ahead bias.
