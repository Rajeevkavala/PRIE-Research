# Learning Roadmap Methodology: Dynamic Sprint Compilation, Velocity Calibration & Re-Planning

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Learning_Roadmap_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Roadmap Compilation Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Algorithmic vs Heuristic vs LLM Decomposition

To avoid uncontrolled LLM hallucinations in student career advice, the learning roadmap engine (`M08`) enforces a strict functional division of labor:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       ROADMAP FUNCTIONAL SEPARATION                             │
├────────────────────┬────────────────────┬───────────────────────────────────────┤
│ Roadmap Function   │ Execution Engine   │ Governing Principle                   │
├────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Concept Sequencing │ Deterministic A*   │ Topological graph traversal on        │
│                    │ Graph Engine       │ verified CS Concept DAG               │
├────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Weekly Allocation  │ Linear Programming │ Knapsack load optimization bounded    │
│ & Pace Limits      │ Solver (PuLP)      │ by student historical weekly hours    │
├────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Contextual Tips &  │ Grounded LLM       │ Retrieval-Augmented generation bound  │
│ Sprint Summaries   │ Prompting (Llama-3)│ to verified curriculum chunks         │
├────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Re-planning Trigger│ Rule-based Event   │ Automated re-routing upon failed quiz │
│                    │ State Machine      │ or milestone deadline breach          │
└────────────────────┴────────────────────┴───────────────────────────────────────┘
```

---

## 2. Dynamic Sprint Compilation & Cognitive Load Balancing

The optimal concept sequence from the $A^*$ search is compiled into actionable 7-day learning sprints:
1. **Weekly Cognitive Capacity Constraint**: Each student possesses an estimated weekly study budget $B_w \in [5, 20]$ hours calibrated by their historical platform login consistency (`F16`).
2. **Knapsack Sprint Allocation**: Concepts are allocated to Sprint $k$ subject to:
   $$\sum_{v \in \text{Sprint}_k} c(v) \le B_w \times \eta_{\text{velocity}}$$
   where $\eta_{\text{velocity}}$ is the student's empirical learning velocity ratio (actual hours taken / estimated hours).
3. **Formative Checkpoints**: Every sprint culminates in an automated coding sandbox problem or diagnostic quiz (`M03`, `M10`) verifying mastery before the next sprint unlocks.

---

## 3. Dynamic Re-Planning & Closed-Loop Adaptation

If a student fails a milestone checkpoint (Diagnostic Score $< 60\%$ or delay $> 10$ days):
1. The Concept State Machine transitions the failed concept back from `In-Progress` to `Unmastered`.
2. The $A^*$ engine re-runs from the updated state bitset $\mathcal{M}_s$, automatically inserting targeted prerequisite reinforcement modules into the next weekly sprint.
