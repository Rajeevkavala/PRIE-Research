# Architecture Assumptions: Formal Architectural Assumptions & Risk Ledger

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Architecture_Assumptions.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Assumptions Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Governance & Epistemological Taxonomy

In accordance with Section 37 of the Master Directive, every architectural assumption underlying PRIE is explicitly cataloged, analyzed for operational risk, and linked to a formal validation methodology.

**Assumption Status Taxonomy**:
- **`ESTABLISHED`**: Supported by verified literature consensus and empirical data across the 44-paper corpus.
- **`PROPOSED`**: Formulated as an architectural hypothesis; designated for testing in Phase 08.
- **`UNVERIFIED`**: Plausible operational assumption requiring empirical institutional calibration.
- **`INVALIDATED`**: Proved false or structurally flawed; rejected from system architecture.

---

## 2. Master Architecture Assumptions Ledger

---

### ASM-01: Standardized Curricular Grade Normalizability
- **Assumption ID**: `ASM-01`
- **Statement**: Academic grades and CGPA scales across disparate university departments and grading systems can be mapped to a standardized continuous domain $[0.0, 1.0]$ without destroying relative candidate ranking fidelity.
- **Reason**: Placement drives apply standardized percentage or CGPA eligibility cutoffs across varied college cohorts.
- **Evidence Base**: **Paper01**, **Paper06**, **Paper22**; standard practice across 34 of 44 reviewed papers.
- **Risk**: Grading inflation variance between autonomous colleges and state universities may introduce non-linear domain shifts.
- **Impact**: High (Affects `F01: cgpa` weighting in Track 1 XGBoost).
- **Validation Method**: Distributional Kolmogorov-Smirnov ($KS$) tests across cross-institutional grading transcripts in Phase 08.
- **Status**: `ESTABLISHED`.

---

### ASM-02: Spatial Layout Disambiguation via Bounding Box Coordinates
- **Assumption ID**: `ASM-02`
- **Statement**: 2D spatial layout coordinates ($[x_0, y_0, x_1, y_1]$) and visual document patches provide sufficient geometric context for LayoutLMv3 to separate adjacent parallel columns without reading-order corruption.
- **Reason**: Multi-column text interleaving is fundamentally a spatial geometry problem.
- **Evidence Base**: **Paper17** (Verma & Mehta 2026), **Paper42** (Davenport 2025: extraction F1 boosted from 0.68 to 0.92).
- **Risk**: Resumes with non-standard graphic elements, rotated text, or watermarks may distort bounding box normalization.
- **Impact**: High (Directly impacts ATS parsing accuracy in `M02`).
- **Validation Method**: Entity Extraction Boundary-F1 benchmark across 200 real student resumes (`EXP-1`).
- **Status**: `ESTABLISHED`.

---

### ASM-03: Client Browser WebAssembly Capability for Real-Time Vision
- **Assumption ID**: `ASM-03`
- **Statement**: Contemporary student personal computers and laptop web browsers (Chrome, Firefox, Edge) possess sufficient CPU/GPU acceleration to execute MediaPipe FaceMesh compiled to WebAssembly at 30 FPS without thermal throttling or UI freezing.
- **Reason**: Necessary to achieve zero-trust candidate privacy and eliminate expensive central server video streaming (`DD-005`, `DD-011`).
- **Evidence Base**: **Paper15** (Inamdar et al. 2025: client-side landmark tracking sustained 30 FPS on entry-level hardware).
- **Risk**: Low-end netbooks or legacy mobile browsers may drop frames or experience JavaScript thread blocking.
- **Impact**: Medium (Affects `F20: behavior_score` data completeness).
- **Validation Method**: Client hardware profiling across 50 heterogeneous student devices during pre-experimental interviews (`EXP-2`).
- **Status**: `PROPOSED`.

---

### ASM-04: Sub-1.5s Voice Turnaround Cadence Satisfies Conversational Realism
- **Assumption ID**: `ASM-04`
- **Statement**: Achieving a voice-to-voice turn-taking latency below $1,500$ms is sufficient to eliminate candidate conversational anxiety and sustain natural dialogue cadence in technical mock interviews.
- **Reason**: Sequential cloud API pipelines fail because delays exceed 2.8–4.2s (**Paper03**, **Paper29**).
- **Evidence Base**: Human-computer interaction conversational speech literature; **Paper03**, **Paper29**.
- **Risk**: Network packet jitter on consumer Wi-Fi connections may introduce latency spikes beyond the local processing budget.
- **Impact**: High (Affects candidate engagement and interview realism in `M05`).
- **Validation Method**: Latency profiling and candidate usability Likert instruments in Phase 08 (`EXP-2`).
- **Status**: `PROPOSED`.

---

### ASM-05: Concept DAG Faithfulness to Real-World Prerequisite Dependencies
- **Assumption ID**: `ASM-05`
- **Statement**: Computer Science curricula and industry engineering skill requirements can be accurately modeled as a Directed Acyclic Graph (DAG) whose topological traversal guarantees pedagogical soundness.
- **Reason**: Prerequisite chains in computer science (e.g., Programming $\to$ Data Structures $\to$ Algorithms $\to$ System Design) exhibit strong natural hierarchy.
- **Evidence Base**: **Paper13** (Zhang 2023), **Paper16** (Tan 2024), **Paper39** (Kurdi 2020), **Paper43** (Rajeevan 2026).
- **Risk**: Emerging interdisciplinary tracks (e.g., MLOps, Prompt Engineering) may blur strict prerequisite edges.
- **Impact**: High (Governs roadmap generation in `M08` and AQG distractor mapping in `M10`).
- **Validation Method**: Expert curriculum review and cycle-detection validation scripts.
- **Status**: `ESTABLISHED`.

---

### ASM-06: Actionable Counterfactuals Yield Higher Adherence than Descriptive SHAP
- **Assumption ID**: `ASM-06`
- **Statement**: Presenting students with distance-constrained, feasible counterfactual steps (DiCE) produces measurably higher study plan adherence and milestone completion than presenting descriptive SHAP feature importance charts.
- **Reason**: Descriptive attribution informs students what is wrong without prescribing what to do (`RG3`).
- **Evidence Base**: **Paper18** (Hidayatulloh 2026), **Paper19** (Joshi & Khan 2025).
- **Risk**: Students may perceive multiple recommended changes as overwhelming if sparsity ($L_0$) is not strictly constrained.
- **Impact**: Very High (Core hypothesis **`H4`** of the PRIE research ecosystem).
- **Validation Method**: Randomized controlled trial with 60 students over a 30-day intervention sprint (`EXP-4`).
- **Status**: `PROPOSED` (Hypothesis to be tested in Phase 08).

---

### ASM-07: Early Disengagement Telemetry Predicts Final Unreadiness
- **Assumption ID**: `ASM-07`
- **Statement**: A persistent decline in interaction cadence (`F16`) and weekly engagement (`F21`) during Weeks 3–4 of an academic preparation cycle strongly correlates with final campus recruitment failure, providing a viable early-intervention window.
- **Reason**: Regularity of deliberate practice reflects self-regulated learning and persistent motivation.
- **Evidence Base**: **Paper02** (Van Wyk 2025), **Paper05** (Chen 2024), **Paper33** (Al-Shabandar 2019/2025), **Paper44** (Azeez 2026).
- **Risk**: External unmodeled events (e.g., student illness or university semester exams) can cause transient engagement drops without indicating unreadiness.
- **Impact**: Medium (Triggers faculty advisor escalation in `M12`).
- **Validation Method**: Longitudinal time-series correlation analysis and early-warning sensitivity benchmarking (`EXP-3`).
- **Status**: `ESTABLISHED`.

---

### ASM-08: Differential Privacy Noise Preserves Corporate Recruiter Utility
- **Assumption ID**: `ASM-08`
- **Statement**: Applying Laplace noise with privacy budget $\epsilon \le 1.0$ to aggregate cohort queries preserves sufficient analytical utility for corporate recruiters to identify eligible talent pools while mathematically preventing individual re-identification.
- **Reason**: Large corporate campus drives evaluate macro-cohort distributions rather than single-candidate micro-counts.
- **Evidence Base**: **Paper02** (POPIA compliance framework), **Paper41**; standard differential privacy literature.
- **Risk**: On very small specialized batches ($N < 15$), Laplace noise may distort percentage thresholds noticeably.
- **Impact**: Medium (Affects recruiter search results on small cohorts).
- **Validation Method**: Utility-loss benchmarking comparing noisy vs true cohort counts across 100 simulated recruiter queries.
- **Status**: `PROPOSED`.

---

## 3. Assumptions Summary & Audit Status

| Assumption ID | Core Domain | Risk Level | Impact | Validation Protocol | Status |
|:---:|:---|:---:|:---:|:---|:---:|
| **ASM-01** | Academic Grading Normalization | Medium | High | Two-sample KS test | `ESTABLISHED` |
| **ASM-02** | 2D Spatial Layout Parsing | Medium | High | Benchmark on 200 resumes (`EXP-1`) | `ESTABLISHED` |
| **ASM-03** | Client Browser Wasm Execution | Medium | Medium | Hardware profiling across 50 devices | `PROPOSED` |
| **ASM-04** | Sub-1.5s Conversational Cadence | Low | High | Latency measurement & panel study (`EXP-2`) | `PROPOSED` |
| **ASM-05** | CS Concept DAG Hierarchy | Low | High | Cycle-breaking and curriculum audit | `ESTABLISHED` |
| **ASM-06** | Counterfactual Adherence Uplift | Medium | Very High | Randomized controlled trial (`EXP-4`) | `PROPOSED` |
| **ASM-07** | Week 3–4 Early Intervention | Low | High | Longitudinal sensitivity audit (`EXP-3`) | `ESTABLISHED` |
| **ASM-08** | Differential Privacy Utility | Low | Medium | Analytical utility-loss evaluation | `PROPOSED` |

**Scientific Discipline Certified**: Zero assumptions are treated as self-evident facts. Every assumption is equipped with a concrete validation protocol in Phase 08.
