# Recommendation Methodology: Topological A* Search over Concept DAGs, Prerequisite Safety & Ranking

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Recommendation_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Recommendation Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Resolving the Collaborative Filtering Cold-Start Collapse (`RG7`)

Traditional recommendation algorithms in educational technology rely on user-collaborative filtering (`Paper04`, `Paper13`, `Paper16`). When applied to new undergraduate students or evolving corporate job descriptions, these algorithms collapse due to extreme user-item matrix sparsity ($>99.2\%$). Furthermore, collaborative filtering frequently recommends advanced topics out of order (e.g., advising a student to study "Dynamic Programming" before mastering "Recursion"), inducing severe cognitive frustration.

PRIE formulates personalized career remediation as a **constrained topological $A^*$ shortest-path search across a formal Computer Science Concept Directed Acyclic Graph (DAG)** (`DD-008`, `M08`):

```
[Student Current SPV State] + [Target Role Profile] + [Skill Deficit Vector delta]
                                       │
                                       ▼
                     Topological Prerequisite Safety Filter
                     Rule: Concept v unlockable iff Parents(v) in Mastered(s)
                                       │
                                       ▼
                       Constrained A* Graph Traversal Engine
                         f(n) = g(n) [Cost] + h(n) [Heuristic]
                                       │
                                       ▼
                     Optimal Ordered Remediation Sequence
                     [Milestone 1] -> [Milestone 2] -> [Milestone 3]
```

---

## 2. Mathematical Formulation of the Concept DAG & A* Search

Let the Computer Science curriculum be represented as a formal DAG $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ where:
- Each vertex $v \in \mathcal{V}$ represents an atomic technical concept (e.g., `Binary Search`, `B-Trees`, `TCP Sockets`).
- Each directed edge $(u, v) \in \mathcal{E}$ indicates that concept $u$ is a mandatory prerequisite for concept $v$.
- Each node possesses an estimated cognitive mastery duration in hours $c(v) > 0$.

### 2.1 Prerequisite Safety Invariant
At any point in time, student $s$ possesses a mastered concept bitset $\mathcal{M}_s \subseteq \mathcal{V}$. A target skill $v_{\text{target}}$ cannot be scheduled until all prerequisite parents are satisfied:
$$\text{Unlockable}(v) \iff \forall u \in \text{Parents}(v), \; u \in \mathcal{M}_s$$

### 2.2 A* Evaluation Function
For any candidate concept node $n$:
$$f(n) = g(n) + h(n)$$
where:
- $g(n)$ is the accumulated cognitive learning cost along the traversal path from the student's current state:
  $$g(n) = \sum_{u \in \text{Path}(\mathbf{x}_s, n)} c(u)$$
- $h(n)$ is the admissible heuristic function estimating remaining Euclidean skill gap distance to the target corporate profile:
  $$h(n) = \|\mathbf{v}_{\text{target}} - \mathbf{v}_n\|_2 \times \min_{v \in \mathcal{V}} c(v)$$
Because $h(n)$ never overestimates the minimal remaining cognitive hours required to close the gap, the $A^*$ search is guaranteed to return the **theoretically optimal minimal-effort learning pathway**.

---

## 3. Measurable Recommendation Evaluation Metrics

In strict avoidance of subjective claims, recommendations are evaluated using objective metrics:
1. **Prerequisite Violation Rate ($\text{PVR}$)**: Proportion of recommended milestone sequences containing out-of-order dependencies (Target: $\text{PVR} = 0.0\%$).
2. **Path Cognitive Cost (PCC)**: Total estimated hours required to transition from unready state to ready threshold.
3. **Milestone Completion Velocity (MCV)**: Empirical days required by students to complete recommended remediation sprints.
