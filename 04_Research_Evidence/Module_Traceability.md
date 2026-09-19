# Module Traceability Matrix: PRIE Architectural Subsystems to Research Evidence

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Module_Traceability.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Architectural Mapping Matrix  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Subsystem Inventory

The Placement Readiness Intelligence Engine (PRIE) is structured into twelve (12) cohesive, interoperable functional modules (`M01` through `M12`). Each module directly corresponds to a specific dimension of the core research problem formulated in Phase 03: resolving the fragmentation of graduate placement systems across isolated, static, unexplainable, and non-actionable point solutions.

```
       ┌────────────────────────────────────────────────────────┐
       │         M12: Closed-Loop Digital Twin Orchestrator      │
       └───────────────────────────┬────────────────────────────┘
                                   │
      ┌────────────────────────────┼────────────────────────────┐
      ▼                            ▼                            ▼
┌──────────────┐          ┌──────────────────┐          ┌──────────────┐
│  PERCEPTION  │          │    REASONING     │          │ ACTIONABLE   │
│              │          │                  │          │ REMEDIATION  │
│ M01: SPV     │          │ M04: Gap Engine  │          │ M07: XAI     │
│ M02: ATS     │─────────►│ M06: Predictor   │─────────►│ M08: Roadmap │
│ M03: Quiz    │          │ M11: Telemetry   │          │ M09: RAG     │
│ M05: Interview          │                  │          │ M10: AQG     │
└──────────────┘          └──────────────────┘          └──────────────┘
```

---

## 2. Master Module Traceability Matrix

The table below establishes the complete deductive chain from primary literature to PRIE's 12 subsystems:

| Module ID & Name | Core Research Problem Addressed | Phase 03 Objective | Phase 03 RQ & Hypothesis | Supporting Literature (P01–P44) | Phase 02 Cross-Analysis Finding | Core Architectural Design Rationale | Evidentiary Strength | Key Evaluation Requirement |
|:---|:---|:---:|:---:|:---|:---|:---|:---:|:---|
| **M01: Student Profile Vector (SPV) Aggregator** | Siloed student data; lack of unified multi-modal candidate representation. | **PRO**, **RO1** | **RQ1**, **H1** | **Paper01**, **Paper04**, **Paper06**, **Paper08**, **Paper10**, **Paper22**, **Paper24** | `Feature_Comparison.md`: Unifying academic, technical, and behavioral signals improves placement prediction $F_1$ by $>14\%$. | Harmonizes 22 heterogeneous dimensions (academic, coding, ATS, behavior, telemetry) into a normalized feature tensor. | `STRONG` (Direct Literature Consensus) | Dimensionality reduction and ablation analysis of individual feature clusters. |
| **M02: Resume Intelligence & Multi-Column ATS Matcher** | Spatial layout destruction in multi-column resumes; brittle keyword matching. | **RO1** | **RQ1**, **H1** | **Paper11**, **Paper12**, **Paper13**, **Paper17**, **Paper35**, **Paper36**, **Paper37**, **Paper42** | `ATS_Comparison.md`: 64% of resumes fail traditional parsers due to multi-column text interleaving. | LayoutLMv3 spatial bounding box parsing combined with Sentence-BERT dense semantic matching against target JDs. | `STRONG` (Direct Literature & Benchmark) | Boundary Token F1 and Entity Extraction Accuracy on single vs multi-column resumes. |
| **M03: Adaptive Assessment & Diagnostic Quizzing** | Static, uncalibrated diagnostic quizzes that fail to pinpoint exact conceptual voids. | **RO5** | **RQ5**, **H5** | **Paper02**, **Paper04**, **Paper05**, **Paper25**, **Paper26**, **Paper39** | `Future_Work_Matrix.md`: Traditional diagnostic tests lack cognitive depth and prerequisite dependency tracking. | Serves dynamically calibrated assessments targeting specific prerequisite concepts in the CS curriculum. | `MODERATE` (Concept Validated; AQG Proposed) | Item Discrimination Index ($DI$), Item Difficulty ($p$-value), and student mastery slope. |
| **M04: Skill Gap Analysis & Distance Engine** | Vague, qualitative feedback on candidate shortcomings without mathematical distance metrics. | **RO4** | **RQ4**, **H4** | **Paper04**, **Paper13**, **Paper16**, **Paper35**, **Paper41** | `Limitation_Matrix.md`: Prior systems list missing skills alphabetically without weighting role criticality. | Formulates skill deficit as a weighted Euclidean/cosine distance vector against target corporate role taxonomies. | `STRONG` (Grounded in Vector Analytics) | Correlation between computed skill gap distance and candidate technical interview failure rate. |
| **M05: Multimodal Mock Interview Coach** | Excessive conversational latency ($>2.8$s); lack of objective code execution in interview practice. | **RO2** | **RQ2**, **H2** | **Paper03**, **Paper14**, **Paper15**, **Paper27**, **Paper28**, **Paper29**, **Paper30**, **Paper38** | `Interview_Comparison.md`: Sequential API piping creates unnatural conversational hesitation; client video leaks privacy. | Streaming Whisper ASR + local quantized LLM for sub-1.5s voice dialogue; client-side MediaPipe Wasm; Dockerized code sandbox. | `STRONG` (Perception Validated; Architecture Proposed) | Turn-taking latency ($<1.5$s); Pearson correlation ($r \ge 0.70$) with human recruiter panel. |
| **M06: Placement Readiness Prediction Engine** | Binary, opaque placement predictions uncoupled from longitudinal learning trajectories. | **PRO**, **RO3** | **RQ3**, **H3** | **Paper01**, **Paper04**, **Paper06**, **Paper09**, **Paper18**, **Paper22**, **Paper44** | `Algorithm_Comparison.md`: Tree ensembles (XGBoost) dominate static tabular data; TFT dominates temporal sequences. | Dual-track architecture: XGBoost for static cross-sectional classification; Temporal Fusion Transformer for multi-semester trajectory forecasting. | `VERY STRONG` (Direct Literature Consensus) | Accuracy, Macro-$F_1$, ROC-AUC on static cohorts; Multi-horizon Quantile Loss on temporal sequences. |
| **M07: Prescriptive Explainability & Counterfactual Engine** | Descriptive XAI (SHAP) explains historical failure but provides zero actionable remediation. | **RO4** | **RQ4**, **H4** | **Paper02**, **Paper18**, **Paper19**, **Paper22**, **Paper32**, **Paper34** | `XAI_Comparison.md`: The "Descriptive-to-Prescriptive Chasm" leaves students without actionable recourse. | Generates dual-tier explanations: TreeSHAP for global/local attribution; DiCE constraint optimization for actionable counterfactual paths. | `STRONG` (SHAP Established; DiCE Prescriptive Innovation) | Actionability Score ($\ge 80\%$), Counterfactual Proximity ($L_1$), Sparsity ($L_0$), and Student Adherence. |
| **M08: Dynamic Personalized Roadmap Generator** | Rigid, static study plans that ignore prerequisite dependencies and individual velocity. | **RO4**, **RO6** | **RQ4**, **H4** | **Paper13**, **Paper16**, **Paper41**, **Paper44** | `Recommendation_Comparison.md`: Pure collaborative filtering collapses; requires prerequisite graph traversal. | Computes optimal topological path across curriculum concept DAG to bridge diagnosed skill gaps with minimum effort. | `MODERATE` (Graph Traversal Grounded) | Milestone completion rate and pre/post diagnostic score uplift. |
| **M09: Retrieval-Augmented Generation (RAG) Assistant** | Domain hallucination and unverified curriculum advice in generative student guidance. | **RO5**, **RO6** | **RQ6** | **Paper20**, **Paper21**, **Paper23**, **Paper27**, **Paper40** | `RAG_Comparison.md`: Unconstrained LLMs hallucinate syllabus facts; RAG Triad required for factual verification. | ChromaDB vector store grounded on verified college syllabi and placement archives; Cross-Encoder reranking; TruLens Triad verification. | `STRONG` (Established Educational Architecture) | Context Relevance ($\ge 0.85$), Groundedness ($\ge 0.90$), Answer Relevance ($\ge 0.88$). |
| **M10: Causal Concept-Guided Question Generation (AQG)** | Trivial, uncalibrated distractors in automated multiple-choice question generation. | **RO5** | **RQ5**, **H5** | **Paper25**, **Paper26**, **Paper39** | `Future_Work_Matrix.md`: 78% of LLM-generated MCQs suffer from non-functional distractors that test superficial recall. | Causal DAG-guided Chain-of-Thought prompting ensures distractors reflect verified student misconception pathways. | `STRONG` (Direct Evidence from Paper25) | Distractor Plausibility Index ($DPI \ge 0.70$) and Psychometric Item Discrimination ($DI \ge 0.35$). |
| **M11: Behavioral Telemetry & Longitudinal Analytics** | Inability to track student persistence, habit decay, or optimal early intervention windows. | **RO3**, **RO6** | **RQ3**, **H3** | **Paper02**, **Paper05**, **Paper33**, **Paper44** | `Learning_Analytics_Comparison.md`: Weeks 3–4 represent the critical early-intervention window before drop-out becomes irreversible. | Tracks continuous interaction cadence (login entropy, attempt frequency, session duration) to feed temporal TFT predictors. | `STRONG` (Direct Literature Consensus) | Early risk detection sensitivity ($>85\%$) at Week 4 of preparation cycle. |
| **M12: Triangular Digital Twin & Closed-Loop Orchestrator** | Disconnected stakeholders; faculty and recruiters lack visibility into student preparation state. | **RO6** | **RQ6**, **H6** | **Paper02**, **Paper41**, **Paper44** | `Architecture_Comparison.md`: Open-loop systems fail because recommendations are never dynamically re-ingested into models. | Synchronizes student real-time readiness state across Student, Faculty Advisor, and Corporate Placement Cell dashboards under strict privacy. | `STRONG` (Direct Evidence from Paper41) | Longitudinal skill mastery uplift and overall institutional campus placement conversion rate. |

---

## 3. Subsystem Inter-Module Dependency & Data Flow

To ensure scientific reproducibility and robust engineering, inter-module data contracts are formally specified:

```
[Candidate PDF Resume] ──► M02 (ATS Engine) ──────────┐
                                                      │ (F13, F14)
[Transcripts & Marks]  ──► M01 (SPV Aggregator) ◄─────┴── [F01–F12, F17, F18]
                                │
                                ▼
                       [22-Dimensional SPV]
                                │
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
     M04 (Skill Gap)     M06 (Predictor)     M11 (Telemetry)
            │                   │                   │
            ▼                   ▼                   ▼
     [Missing Skills]    [Readiness Tier]    [Consistency F16]
            │                   │                   │
            └───────────┬───────┴───────────────────┘
                        ▼
                M07 (XAI Engine)
                 /            \
       (TreeSHAP)              (DiCE Counterfactual)
           │                           │
     [Descriptive]               [Prescriptive]
           │                           │
           ▼                           ▼
     Student Dashboard         M08 (Roadmap Generator)
                                       │
                                       ▼
                              M03 / M10 (Assessment)
                                       │
                                       ▼
                              M05 (Mock Interview)
                                       │
                                       ▼
                              M12 (Digital Twin Sync)
```

---

## 4. Module Scientific Integrity Certification

- **Zero Fictional Modules**: All 12 modules correspond strictly to functional components designed to resolve Phase 03 validated research gaps (`RG1`–`RG8`).
- **Traceability Continuity**: Every module links unbrokenly from:
  $$\text{Corpus Literature (P01–P44)} \longrightarrow \text{Phase 02 Cross-Finding} \longrightarrow \text{Phase 03 Objective/RQ} \longrightarrow \text{PRIE Module} \longrightarrow \text{Evaluation Protocol}$$
- **Epistemological Discipline**: Distinctly differentiates between established algorithmic components (e.g., TreeSHAP in M07, XGBoost in M06) and novel architectural integrations (e.g., Causal DAG AQG in M10, DiCE Prescriptive Recourse in M07).
