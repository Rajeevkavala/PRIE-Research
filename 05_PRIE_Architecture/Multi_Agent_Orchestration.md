# Multi-Agent Orchestration Architecture: Specialized Agents, Delegation & Governance

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Multi_Agent_Orchestration.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Multi-Agent Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Philosophy & Anti-Proliferation Principle

PRIE explicitly rejects the uncritical adoption of multi-agent architectures simply because "multi-agent AI" is fashionable. In PRIE, an AI Agent is defined as:
> *An encapsulated autonomous software entity with a well-defined domain of responsibility, scoped tool permissions, state memory, and bounded decision authority.*

Agents are deployed **only** where distinct expertise, tool isolation, asynchronous delegation, or strict governance boundaries are scientifically and operationally required.

**The Golden Safety Invariant**:
> **No agent may autonomously alter authoritative student academic records or modify the 22-dimensional Student Profile Vector without passing through deterministic schema validation and immutable audit logging.**

---

## 2. Master Agent Inventory & Supervisory Hierarchy

PRIE organizes its multi-agent workforce under a **Supervisory Hierarchical Delegation Model**:

```
                       ┌────────────────────────────────────────────────────────┐
                       │               AGT-00: ORCHESTRATOR AGENT               │
                       │         (Supervisory Delegation & Task Router)         │
                       └───────────────────────────┬────────────────────────────┘
                                                   │
         ┌───────────────────┬─────────────────────┼─────────────────────┬───────────────────┐
         │                   │                     │                     │                   │
         ▼                   ▼                     ▼                     ▼                   ▼
┌─────────────────┐ ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐ ┌─────────────────┐
│ AGT-01: PROFILE │ │ AGT-02: RESUME  │   │ AGT-03: INTERV  │   │ AGT-04: PREDICT │ │ AGT-05: XAI     │
│ SPV Compiler    │ │ LayoutLM / SBERT│   │ Whisper / Wasm  │   │ Dual-Track ML   │ │ DiCE / TreeSHAP │
└─────────────────┘ └─────────────────┘   └─────────────────┘   └─────────────────┘ └─────────────────┘
         │                   │                     │                     │                   │
         └───────────────────┼─────────────────────┴─────────────────────┼───────────────────┘
                             │                                           │
                             ▼                                           ▼
                    ┌─────────────────┐                         ┌─────────────────┐
                    │ AGT-06: RECOM   │                         │ AGT-07: RAG     │
                    │ DAG Traversal   │                         │ ChromaDB / Triad│
                    └─────────────────┘                         └─────────────────┘
```

---

## 3. Detailed Agent Specifications

---

### AGT-00: Supervisory Orchestrator Agent
- **Agent ID**: `AGT-00`
- **Agent Name**: Supervisory Orchestrator Agent
- **Purpose**: Coordinates multi-agent workflows, dispatches tasks, manages user session context, and enforces global safety and rate-limiting policies.
- **Inputs**: User HTTP/WebSocket requests, inter-agent task completions, system alerts.
- **Outputs**: Delegated sub-tasks, aggregated user response payloads, system telemetry.
- **Tools**: Task Dispatcher, Agent Status Monitor, Audit Logger, Security Context Validator.
- **Memory**: Ephemeral session memory (Redis session cache, TTL 30 minutes).
- **Decision Authority**: High for workflow routing; **Zero authority to modify data models directly**.
- **Dependencies**: All specialized agents (`AGT-01` through `AGT-07`).
- **Failure Modes**: Sub-agent timeout $\to$ returns partial response with graceful degradation notice.
- **Human Oversight**: High; all critical institutional policy overrides require human admin sign-off.
- **Evaluation**: Task completion latency and workflow error rates.

---

### AGT-01: Student Profile Agent
- **Agent ID**: `AGT-01`
- **Agent Name**: Student Profile & Normalization Agent
- **Purpose**: Oversees data ingestion, missing-value imputation, normalization, and compilation of the authoritative 22-dimensional SPV tensor (`M01`).
- **Inputs**: Academic SIS grades, parsed resume metrics, diagnostic scores, interview telemetry.
- **Outputs**: Compiled, validated feature tensor $\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$.
- **Tools**: `MinMaxStandardizerTool`, `MICEImputerTool`, `VIFCollinearityTool`, `SPVDatabaseWriterTool`.
- **Memory**: Student historical profile cache.
- **Decision Authority**: Bounded; executes deterministic mathematical transformations.
- **Dependencies**: SIS API, PostgreSQL (`SPV-DB`).
- **Failure Modes**: Rejects malformed records; logs imputation confidence flags.
- **Human Oversight**: Faculty advisors can review and manually correct registrar discrepancies.
- **Evaluation**: Zero data leakage; mathematical invariance to normalization bounds.

---

### AGT-02: Resume Intelligence Agent
- **Agent ID**: `AGT-02`
- **Agent Name**: Resume Document Intelligence Agent
- **Purpose**: Manages multi-column PDF resume parsing, bounding box extraction, entity classification (`LayoutLMv3`), and semantic JD alignment (`Sentence-BERT`) (`M02`).
- **Inputs**: Raw resume binary (PDF/DOCX), target Job Description text.
- **Outputs**: Extracted entity spans, `F13: resume_ats_score`, `F14: cosine_similarity`.
- **Tools**: `PyMuPDFParserTool`, `LayoutLMv3InferenceTool`, `SBERTVectorizerTool`, `PIIRedactorTool`.
- **Memory**: Stateless (processes document in-memory; persists only extracted vectors).
- **Decision Authority**: Autonomous for entity tagging; cannot alter candidate profile without user confirmation.
- **Dependencies**: LayoutLMv3 worker, Sentence-BERT worker, ChromaDB.
- **Failure Modes**: Low-quality scan $\to$ falls back to Tesseract OCR and flags warning.
- **Human Oversight**: Candidate can review and edit extracted entities before saving to SPV.
- **Evaluation**: Boundary-Token F1 across multi-column templates (`EXP-1`).

---

### AGT-03: Multimodal Interview Coach Agent
- **Agent ID**: `AGT-03`
- **Agent Name**: Multimodal Interview Coach Agent
- **Purpose**: Conducts real-time conversational technical interviews, manages audio chunking, generates context-aware follow-up questions, monitors paralinguistics, and validates code submissions in Docker sandboxes (`M05`).
- **Inputs**: Streaming audio chunks, client Wasm visual telemetry scalars, candidate code.
- **Outputs**: Synthesized audio responses, code execution reports, `F06`, `F08`, `F20` scores.
- **Tools**: `WhisperStreamingTool`, `vLLMDialogueTool`, `FastTTSVoiceTool`, `DockerSandboxRunnerTool`.
- **Memory**: Multi-turn dialogue context window (active interview session only).
- **Decision Authority**: Autonomous dialogue turn management; sandboxed execution authority.
- **Dependencies**: Whisper ASR, vLLM, Docker daemon.
- **Failure Modes**: Network jitter $\to$ requests phrase repeat; code sandbox timeout $\to$ terminates container.
- **Human Oversight**: Recruiter panels review recorded scores for calibration (`EXP-2`).
- **Evaluation**: Voice-to-voice turn-taking latency $<1.5$s; Pearson $r \ge 0.70$ with human recruiters.

---

### AGT-04: Placement Prediction Agent
- **Agent ID**: `AGT-04`
- **Agent Name**: Placement Prediction Agent
- **Purpose**: Executes dual-track placement readiness prediction (XGBoost cross-sectional tiering and TFT longitudinal sequence forecasting) (`M06`).
- **Inputs**: Current SPV tensor $\mathbf{x}_{\text{spv}}$, historical semester sequence $\mathbf{x}_{1..T}$.
- **Outputs**: $P_{\text{ready}}$, Readiness Tier (`Ready`, `Needs Remediation`, `At-Risk`), quantile forecasts ($q_{0.1}, q_{0.5}, q_{0.9}$).
- **Tools**: `ONNXXGBoostRunnerTool`, `TFTPyTorchRunnerTool`, `PlattCalibratorTool`.
- **Memory**: Model registry cache.
- **Decision Authority**: Autonomous scoring; zero policy-setting authority.
- **Dependencies**: Model execution workers (`CMP-MDL-XGB`, `CMP-MDL-TFT`).
- **Failure Modes**: Sequence data missing $\to$ falls back to Track 1 static XGBoost model.
- **Human Oversight**: Predictions are advisory; human placement officers make final corporate shortlists.
- **Evaluation**: Macro-$F_1$, ROC-AUC, Brier score, multi-horizon Quantile Loss (`EXP-3`).

---

### AGT-05: Prescriptive Explainability Agent
- **Agent ID**: `AGT-05`
- **Agent Name**: Prescriptive Explainability Agent
- **Purpose**: Generates descriptive feature attributions (TreeSHAP) and executes constraint-optimized counterfactual searches (DiCE) to produce actionable remediation targets (`M07`).
- **Inputs**: Student SPV, XGBoost model artifact, mutability constraints.
- **Outputs**: SHAP local attribution bars ($\phi_i$), counterfactual delta vector $\mathbf{x}^*$.
- **Tools**: `TreeSHAPCalculatorTool`, `DiCEOptimizerTool`, `ConceptPrerequisiteValidatorTool`.
- **Memory**: Pre-computed archetype counterfactual lookup cache.
- **Decision Authority**: Bounded by mathematical optimization constraints and immutable demographic locks.
- **Dependencies**: TreeSHAP, DiCE solver, CS Concept DAG.
- **Failure Modes**: DiCE timeout $>3.0$s $\to$ serves pre-computed cohort archetype counterfactual.
- **Human Oversight**: Faculty mentors can inspect and adjust counterfactual recommendations.
- **Evaluation**: Actionability score $\ge 80\%$, Proximity $L_1$, Sparsity $L_0$ (`EXP-4`).

---

### AGT-06: Recommendation & Roadmap Agent
- **Agent ID**: `AGT-06`
- **Agent Name**: Recommendation & Roadmap Agent
- **Purpose**: Performs topological shortest-path graph search ($A^*$) across the Computer Science Concept DAG to sequence prescribed counterfactual deltas into structured learning sprints (`M08`).
- **Inputs**: Prescriptive delta targets, diagnosed skill gaps, student weekly time availability.
- **Outputs**: Structured weekly learning roadmap with verification criteria.
- **Tools**: `AStarDAGSearchTool`, `PrerequisiteTopologicalSorterTool`, `RoadmapJSONBuilderTool`.
- **Memory**: Active student roadmap progress state.
- **Decision Authority**: Autonomous sequencing; subject to prerequisite DAG constraints.
- **Dependencies**: CS Concept DAG store, `M04`, `M07`.
- **Failure Modes**: Graph cycle detected $\to$ invokes cycle breaker; unreachable goal $\to$ adjusts target deadline.
- **Human Oversight**: Students can adjust weekly hour allocations; advisors can verify sprint milestones.
- **Evaluation**: Catalog Coverage $\ge 90\%$, Milestone completion uplift $\ge 35\%$.

---

### AGT-07: Curriculum RAG & Verification Agent
- **Agent ID**: `AGT-07`
- **Agent Name**: Curriculum RAG & Verification Agent
- **Purpose**: Retrieves institutional syllabus documents and answers student technical questions, guarded by automated runtime RAG Triad verification (`M09`).
- **Inputs**: Student natural language query.
- **Outputs**: Grounded response with citations, RAG Triad verification scores.
- **Tools**: `ChromaDBDenseRetrieverTool`, `CrossEncoderRerankerTool`, `RAGTriadVerifierTool`, `LocalLLMCallerTool`.
- **Memory**: Conversational context buffer (rolling 5 turns).
- **Decision Authority**: Bounded; automatically discards responses with Groundedness $<0.90$.
- **Dependencies**: ChromaDB, Cross-Encoder, local vLLM.
- **Failure Modes**: Zero relevant context $\to$ outputs explicit syllabus boundary fallback.
- **Human Oversight**: Faculty can audit retrieval logs and update vector collections.
- **Evaluation**: RAG Triad benchmark ($\text{CR} \ge 0.85, \text{GR} \ge 0.90, \text{AR} \ge 0.88$).

---

## 4. Agent Governance & Safety Boundaries

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENT SAFETY BOUNDARIES                         │
├───────────────────┬────────────────────────────────────────────────────┤
│ AUTHORITY LEVEL   │ PERMITTED ACTIONS & RESTRICTIONS                   │
├───────────────────┼────────────────────────────────────────────────────┤
│ Read-Only Agents  │ AGT-04 (Predict), AGT-05 (XAI), AGT-07 (RAG).      │
│                   │ Strictly cannot mutate persistent database states. │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sandboxed Agents  │ AGT-03 (Interview). Code execution restricted to   │
│                   │ ephemeral Docker containers with disabled network. │
├───────────────────┼────────────────────────────────────────────────────┤
│ State-Mutating    │ AGT-01 (Profile) & AGT-06 (Roadmap). Can only write│
│ Agents            │ to SPV/Roadmap stores after passing Pydantic schema│
│                   │ validation and triggering immutable audit logs.    │
├───────────────────┼────────────────────────────────────────────────────┤
│ Privacy Boundary  │ No agent has authority to bypass the Differential  │
│                   │ Privacy Proxy (CMP-GW-PRIV) for recruiter views.   │
└───────────────────┴────────────────────────────────────────────────────┘
```

**Architectural Integrity Certified**: Every agent has an explicit, non-overlapping mandate derived directly from the M01–M12 module architecture, with strict governance preventing autonomous state corruption.
