# Recommendation Engine Architecture: Topological Graph Traversal & Cold-Start Career Pathway Planning (M04 / M08)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Recommendation_Engine_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Recommendation Engine Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & The Cold-Start Collaborative Filtering Collapse

Recommendation engines in traditional educational and career advising systems predominantly attempt to adapt collaborative filtering algorithms (Matrix Factorization, User-User k-NN, Neural Collaborative Filtering).

As established in Phase 02 (`02_Cross_Analysis/Recommendation_Comparison.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG7`):
1. **Extreme Matrix Sparsity ($>99.2\%$)**: As demonstrated by **Paper16** (Tan et al. 2024), career transition matrices are catastrophically sparse. Junior college students have zero historical career milestones or transition records.
2. **Cold-Start Breakdown**: Collaborative filtering fails completely when recommending pathways to third-year students who have never participated in recruitment drives.
3. **Prerequisite Blindness**: Collaborative filtering recommends items based on statistical co-occurrence, frequently recommending advanced topics (e.g., "Advanced Transformers" or "Distributed Systems") to students who have not mastered basic linear algebra or socket programming.
4. **LLM Hallucination Vulnerability**: Unconstrained LLM prompting generates generic, un-sequenced, and ill-timed study plans that ignore prerequisite curriculum ordering.

PRIE solves this foundational challenge by architecting a **Topological Graph Traversal Recommendation Framework** (`DD-008`, `M08`), formulating career pathway generation as an $A^*$ shortest-path heuristic search across a verified Computer Science Concept Prerequisite Directed Acyclic Graph (DAG).

---

## 2. Recommendation Subsystem Topology

```
   ┌────────────────────────────────────────────────────────┐
   │ 1. MULTI-SOURCE RECOMMENDATION INPUTS                   │
   │ • SPV Feature Tensor x_spv (22 dimensions)             │
   │ • Predicted Readiness Probability P_ready & Tier (M06) │
   │ • Prescriptive Counterfactual Delta Targets x* (M07)   │
   │ • Missing Skill Deficit Vector from M04                │
   │ • Student Time Availability (Hours / Week)             │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │ 2. CS CONCEPT PREREQUISITE DIRECTED ACYCLIC GRAPH (DAG) │
   │ • Nodes V: Curricular & Industry Competencies          │
   │ • Edges E: Hard Prerequisite Dependencies (u -> v)     │
   │ • Edge Weights w(e): Estimated Learning Hours & Effort │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │ 3. TOPOLOGICAL A* SHORTEST-PATH TRAVERSAL ENGINE       │
   │ • Identifies Current Mastered Concept Subgraph V_init  │
   │ • Identifies Target Role Competency Set V_target       │
   │ • Computes Minimum-Effort Prerequisite-Compliant Path  │
   │ • Filters Illogical or Out-of-Order Learning Sequences │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │ 4. PERSONALIZED ROADMAP SYNTHESIS & RESOURCE MAPPING   │
   │ • Sequences Milestones into Weekly Sprint Containers   │
   │ • Attaches Verified Institutional Learning Resources   │
   │ • Calibrates Velocity against Telemetry Cadence (F16)  │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ├────────────────────────────┐
                               ▼                            ▼
                 [Active Student Roadmap UI]     [Digital Twin Sync (M12)]
                 (Interactive Milestone Cards)   (Faculty Advisor Visibility)
```

---

## 3. Mathematical Formulation of Topological Pathway Planning

### 3.1 The Concept Prerequisite Graph Model
Let the Computer Science knowledge domain be modeled as a weighted directed acyclic graph:
$$\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathcal{W})$$
where:
- $\mathcal{V} = \{v_1, v_2, \dots, v_n\}$ represents discrete technical concepts (e.g., Arrays, Binary Search Trees, Indexing, B-Trees, Dynamic Programming).
- $\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$ represents strict directed prerequisite dependencies: an edge $(u, v) \in \mathcal{E}$ asserts that concept $u$ must be mastered before concept $v$ can be comprehended.
- $\mathcal{W}: \mathcal{E} \to \mathbb{R}^+$ defines the cognitive effort or estimated study hours required to transition from $u$ to $v$.

### 3.2 The Candidate Learning State & Target Goal
For student $s$:
- **Mastered Set** $\mathcal{V}_{\text{mastered}}^{(s)} \subset \mathcal{V}$: Inferred from verified academic transcript marks (`F01`–`F05`), passed diagnostic assessments (`M03`), and verified coding sandbox submissions (`F06`).
- **Target Competency Set** $\mathcal{V}_{\text{target}} \subset \mathcal{V}$: Dictated by the target corporate role taxonomy (e.g., SDE-1 requirements: Object-Oriented Design, System Design, Graph Algorithms).
- **Skill Deficit Set**: $\mathcal{V}_{\text{deficit}} = \mathcal{V}_{\text{target}} \setminus \mathcal{V}_{\text{mastered}}^{(s)}$.

### 3.3 The Prerequisite-Constrained Shortest-Path Optimization
The recommendation problem is formulated as finding an ordered sequence of learning nodes $\pi^* = \langle v_{(1)}, v_{(2)}, \dots, v_{(k)} \rangle$ that resolves $\mathcal{V}_{\text{deficit}}$ while minimizing total cognitive effort:
$$\pi^* = \arg\min_{\pi} \sum_{i=1}^{k} \text{Effort}\big(v_{(i)}\big)$$
subject to the strict **Topological Prerequisite Constraint**:
$$\forall v_{(j)} \in \pi, \quad \text{Parents}(v_{(j)}) \subseteq \mathcal{V}_{\text{mastered}}^{(s)} \cup \{ v_{(1)}, \dots, v_{(j-1)} \}$$
This constraint guarantees that no student is ever assigned an advanced milestone without first having been assigned its unfulfilled prerequisite dependencies.

---

## 4. Cold-Start Resilience & Dynamic Adaptation

### 4.1 Cold-Start Mitigation Mechanism
- Because graph traversal operates on the **structural geometry of the curriculum ontology** rather than historical user co-occurrence matrices:
  - It functions flawlessly for newly onboarded students with **zero historical platform usage** (`DD-008`).
  - The initial state $\mathcal{V}_{\text{mastered}}$ is populated immediately from the student's initial academic transcript grades and onboarding diagnostic test.
  - Catalog Coverage is mathematically guaranteed at $\ge 90\%$, eliminating the rich-get-richer popularity bias of collaborative filtering.

### 4.2 Dynamic Velocity Adaptation Loop
As the candidate interacts with practice assessments (`M03`) and coding sandboxes (`M05`):
1. If the student fails a diagnostic test on node $v$, PRIE dynamically inserts a remedial prerequisite node $u \in \text{Parents}(v)$ into the active sprint.
2. If the student demonstrates rapid mastery ($p > 0.85$ on advanced questions), PRIE applies topological shortcuts to compress the roadmap duration.
3. Roadmap velocity is dynamically calibrated using `F16: consistency_score` to prevent setting unrealistic deadlines.

---

## 5. Candidate Recommendation Architectures & Controls

In strict accordance with the Tripartite Standard (`Model_Selection_Justification.md`):

| Recommender Architecture | Role in PRIE | Literature Grounding | Engineering Rationale | Experimental Validation Target |
|:---|:---|:---|:---|:---|
| **Topological DAG Traversal ($A^*$)** [Selected] | Primary Career Pathway Engine | **Paper13, Paper16, Paper35, Paper41** | Mathematically guarantees prerequisite compliance; 100% cold-start resilient | Catalog Coverage $\ge 90\%$, Milestone completion uplift $\ge 35\%$ |
| **Collaborative Filtering (Matrix Factorization)** [Baseline] | Traditional Recommender Baseline | **Paper16** | Standard status-quo industry recommendation baseline | Control to verify collaborative filtering collapse ($>99\%$ sparsity) |
| **Unconstrained LLM Prompting** [Baseline] | Generative Baseline | **Paper20, Paper26** | Direct zero-shot LLM study plan prompting | Control to demonstrate hallucinated prerequisite violations |
| **Static Rule Grid** [Baseline] | Curriculum Table Baseline | **Paper04** | Fixed semester-wise syllabus advisory | Control to prove personalized dynamic adaptation necessity |

**Anti-Hallucination Guard**: PRIE explicitly rejects unsupported claims that "AI magically knows what a student needs." All recommendations are deterministic functions of the student's diagnosed skill deficit vector, target role requirements, and formal concept graph dependencies.

---

## 6. Downstream Architectural Linkage

The recommendation engine outputs directly feed:
- **`M08` (Personalized Roadmap Generator)**: Formats the topological node sequence into structured weekly milestone containers with estimated completion dates.
- **`M09` (Curriculum RAG Assistant)**: Retrieves verified lecture notes, textbook chapters, and coding problem links mapped to each active node.
- **`M10` (Causal Concept AQG Engine)**: Generates targeted formative quizzes calibrated to the specific prerequisite concept nodes currently scheduled for remediation.
