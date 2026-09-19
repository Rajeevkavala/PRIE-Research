# PRIE Architecture: Recommendation Pipeline

## 1. Overview and Purpose
This document details the architectural pipeline diagram for the **PRIE Prescriptive Recommendation Engine (M07)**.

The engine solves the educational cold-start and curriculum sequencing challenges identified in `RG3` and formalized in `DD-004`. Instead of unconstrained collaborative filtering (which fails for new students or rare job profiles), PRIE deploys a **constrained topological $A^*$ search over a formal Computer Science Concept Directed Acyclic Graph (DAG)**. This diagram shows how diagnostic signals from M02 (Skill Gaps), M03 (Placement Predictions), and M04 (SHAP Attributions and DiCE Counterfactuals) are combined to compute the optimal remediation path respecting strict curricular prerequisites.

---

## 2. Mermaid Recommendation Pipeline Diagram

```mermaid
flowchart TD
    %% Styling
    classDef inputSource fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;
    classDef graphBase fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100;
    classDef algoAstar fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef priorityScorer fill:#ede7f6,stroke:#7b1fa2,stroke-width:2px,color:#4a148c;
    classDef outputMilestone fill:#fce4ec,stroke:#c2185b,stroke-width:3px,color:#880e4f;
    classDef downstream fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#263238;

    %% Ingress: Diagnostic Inputs
    subgraph INGRESS_DIAG ["Diagnostic & Profile Ingress"]
        IN_SPV["Current SPV Tensor<br/>$$\mathbf{v}_{s} \in \mathbb{R}^{22}$$ (M01)"]:::inputSource
        IN_TIER["Placement Tier & Probability<br/>$$P_{\text{placement}} = 0.54$$ (M03)"]:::inputSource
        IN_SHAP["TreeSHAP Feature Attributions<br/>(Identifies largest negative impacts)"]:::inputSource
        IN_DICE["DiCE Counterfactual Minimal Goals<br/>(e.g., $$F06 \ge 75$$, $$F04 \ge 150$$)"]:::inputSource
        IN_GAPS["M02 Skill Gap Vector<br/>$$\boldsymbol{\delta} = \mathbf{v}_{\text{target}} - \mathbf{v}_{s}$$"]:::inputSource
        IN_HIST["Historical Learning State<br/>(Mastered Concept Bitset $$\mathcal{M}_s$$)"]:::inputSource
    end

    %% Formal Knowledge Substrate
    subgraph KNOWLEDGE_DAG ["Curated Computer Science Concept DAG: G = (V, E)"]
        DAG_STORE["Hierarchical Concept Taxonomy<br/>- 450+ CS Concepts (DSA, OS, DBMS, Networks, Fullstack)<br/>- Directed Edges = Strict Prerequisite Dependency<br/>- Edge Weight = Estimated Cognitive Hours to Master"]:::graphBase
        DAG_FILTER["Topological Prerequisite Filter<br/>Rule: Node $$v$$ is unlockable iff $$\text{Parents}(v) \subseteq \mathcal{M}_s$$"]:::graphBase
    end

    %% Topological A* Search Algorithm (DD-004)
    subgraph ALGO_CORE ["Constrained Topological A* Traversal Engine"]
        HEURISTIC_EST["Heuristic Function: $$h(n)$$<br/>Estimated remaining distance from node $$n$$ to Target Job Profile Vector"]:::algoAstar
        COST_EVAL["Path Cost Function: $$g(n)$$<br/>Accumulated learning hours and cognitive load along DAG path"]:::algoAstar
        ASTAR_EVAL["Total Evaluation: $$f(n) = g(n) + h(n)$$<br/>Finds minimal-effort sequence closing critical gaps"]:::algoAstar
    end

    %% Priority Synthesis & Cold-Start Mitigation
    subgraph RANKING_TIER ["Prescriptive Priority Weighting"]
        WEIGHT_SYNTHESIS["Multi-Objective Priority Scoring<br/>$$\text{Priority}(c) = w_1 \cdot \text{Gap}(c) + w_2 \cdot |\text{SHAP}(c)| + w_3 \cdot \text{DiCE\_Urgency}(c)$$"]:::priorityScorer
        PREREQ_SAFETY["Strict Sequence Guard<br/>(Eliminates out-of-order learning frustrations)"]:::priorityScorer
    end

    %% Output Recommendation Milestones
    subgraph OUTPUT_REC ["Prescriptive Recommendations"]
        MILESTONE_LIST["<b>Ranked Learning Milestones</b><br/>1. Priority 1: Dynamic Programming Memoization (Prereq: Recursion [Met])<br/>2. Priority 2: Database Indexing & B-Trees (Prereq: Trees [Met])<br/>3. Priority 3: System Design Rate Limiting (Prereq: Redis [Unmet -> Auto-scheduled])"]:::outputMilestone
    end

    %% Downstream Hand-offs
    subgraph DOWNSTREAM_SERVICES ["Downstream Execution Engines"]
        M08_ROADMAP["M08: Learning Roadmap Engine<br/>(Compiles milestones into weekly sprints)"]:::downstream
        M09_RAG["M09: RAG Knowledge Retrieval<br/>(Fetches verified tutorials, code templates, videos)"]:::downstream
        M12_AQG["M12: Adaptive Question Generator<br/>(Generates diagnostic questions for next milestones)"]:::downstream
    end

    %% Ingress to Knowledge Filter
    IN_HIST --> DAG_FILTER
    DAG_STORE --> DAG_FILTER

    %% Filter to A* Engine
    DAG_FILTER --> COST_EVAL
    IN_GAPS --> HEURISTIC_EST
    IN_DICE --> HEURISTIC_EST

    COST_EVAL --> ASTAR_EVAL
    HEURISTIC_EST --> ASTAR_EVAL

    %% A* to Priority Synthesis
    ASTAR_EVAL --> WEIGHT_SYNTHESIS
    IN_SHAP --> WEIGHT_SYNTHESIS
    IN_TIER --> WEIGHT_SYNTHESIS

    WEIGHT_SYNTHESIS --> PREREQ_SAFETY
    PREREQ_SAFETY --> MILESTONE_LIST

    %% Output to Downstream Hand-offs
    MILESTONE_LIST --> M08_ROADMAP
    MILESTONE_LIST --> M09_RAG
    MILESTONE_LIST --> M12_AQG
```

---

## 3. Algorithmic Formulation and Constraints

### A. Mathematical Definition of the Search Optimization

$$\min_{\pi \in \Pi(\mathcal{G})} \sum_{c_i \in \pi} \text{Effort}(c_i) \quad \text{s.t.} \quad \forall c_i \in \pi, \, \text{Pre}(c_i) \subseteq \mathcal{M}_s \cup \{c_1, \dots, c_{i-1}\}$$

### B. Cold-Start Mitigation Guarantees
1. **Zero-Interaction Baseline**: When a student has zero platform history, the topological filter anchors recommendations strictly to foundational Tier-1 prerequisite nodes whose in-degree is zero.
2. **Deterministic Sequence Integrity**: Prevents common collaborative filtering failures where advanced topics (e.g., *Raft Consensus*) are recommended before foundational topics (*Socket Programming*).
3. **SHAP Alignment**: Maximizes ROI by prioritizing concepts that directly elevate the most damaging negative feature values in the student's SPV.
