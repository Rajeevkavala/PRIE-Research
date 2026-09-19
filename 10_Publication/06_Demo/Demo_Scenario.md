# PRIE Demonstration Personas & Remediation Scenarios

**Document**: `10_Publication/06_Demo/Demo_Scenario.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

## Scenario A: At-Risk Candidate (Alex Chen - CS Senior)

### 1. Initial State Vector
* **Academic Profile**: CGPA = 7.4 / 10.0 ($F_{01} = 0.74$), CS Major ($F_{17} = 0.85$, locked).
* **Diagnostic Assessments**: DSA = 45% ($F_{03} = 0.45$), DBMS = 72% ($F_{04} = 0.72$), System Design = 40%.
* **Resume Status**: Multi-column technical PDF, 1 Project ($F_{10} = 1$), 0 Internships ($F_{11} = 0$). SBERT cosine similarity to SDE-1 JD = 0.76 ($F_{19} = 0.76$).
* **Interview Demeanor**: Acoustic jitter high, speech pause duration 2.8s ($F_{07} = 0.52, F_{08} = 0.55$).
* **Predicted Probability**: $P(\text{placed}) = 0.412$ (At-Risk classification).

### 2. Explainability Diagnostic (TreeSHAP)
* Primary negative attribution driver: `dsa_score` (-0.68 log-odds).
* Secondary negative driver: `mock_interview_score` (-0.34 log-odds).
* Tertiary negative driver: `consistency_score` (-0.22 log-odds).
* Demographic factor `branch_encoded` has 0.00 log-odds attribution.

### 3. Generated Actionable Recourse (DiCE)
* Intervention Target: Raise $P(\text{placed})$ to $\ge 0.75$ with $k \le 3$ feature shifts.
* **Milestone 1**: Raise `dsa_score` from $45\%$ to $70\%$ ($+25\%$).
* **Milestone 2**: Raise `mock_interview_score` from $5.2$ to $7.0$ ($+1.8$).
* **Milestone 3**: Increase weekly engagement `consistency_score` from $0.38$ to $0.65$ ($+0.27$).
* Immutable attributes ($F_{01}$ GPA, $F_{17}$ Department) are completely unchanged.

### 4. Closed-Loop Remediation Delivery
* Kahn topological sort on `cs_concept_dag.json` sequences learning modules over 4 weeks:
  - Week 1: Binary Trees, Heaps, and Priority Queues.
  - Week 2: Graph Representations, BFS & DFS Traversals.
  - Week 3: Dynamic Programming (Memoization, 1D/2D Arrays).
  - Week 4: Technical Interview Articulation Drills & Mock Behavioral Simulation.
* Result: Zero prerequisite precedence violations ($0.0\%$).

---

## Scenario B: Balanced High-Performer (Priya Sharma - IT Senior)

### 1. Initial State Vector
* **Academic Profile**: CGPA = 8.8 / 10.0 ($F_{01} = 0.88$), IT Major ($F_{17} = 0.85$, locked).
* **Diagnostic Assessments**: DSA = 84% ($F_{03} = 0.84$), DBMS = 88% ($F_{04} = 0.88$), Coding Score = 92% ($F_{06} = 0.92$).
* **Resume Status**: 4 Projects ($F_{10} = 4$), 1 Internship ($F_{11} = 1$), SBERT match = 0.89 ($F_{19} = 0.89$).
* **Interview Demeanor**: High composure, low filler word ratio ($F_{07} = 0.86, F_{08} = 0.88$).
* **Predicted Probability**: $P(\text{placed}) = 0.942$ (High-Confidence Ready).

### 2. Explainability Diagnostic & Role Elevation
* All features exhibit positive log-odds attributions.
* PRIE recommends targeted Tier-1 Product Giant benchmarks (Amazon, Google, Microsoft) and provides advanced distributed systems topics.
