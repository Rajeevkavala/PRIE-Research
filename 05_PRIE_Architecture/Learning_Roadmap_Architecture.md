# Learning Roadmap Architecture: Adaptive Milestone Sequencing & Dynamic Remediation (M08)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Learning_Roadmap_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Learning Roadmap Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Mission & Remediation Principles

The Dynamic Personalized Roadmap Generator (`M08`) transforms the mathematical outputs of the Skill Gap Engine (`M04`), Prescriptive Counterfactual Engine (`M07`), and Topological Graph Search (`M08`) into an actionable, cognitive-load-balanced, and verifiable learning journey for the candidate.

Traditional study roadmaps in educational technology suffer from three fatal flaws:
1. **Static Inflexibility**: Study plans are static PDF checklists that fail to adapt when a student struggles with a concept or masters a topic early.
2. **Prerequisite Ignorance**: Roadmaps list topics alphabetically or by arbitrary popularity rather than enforcing strict cognitive prerequisite dependencies.
3. **Absence of Objective Verification Gates**: Students self-report completion without rigorous diagnostic verification, leading to false confidence.

PRIE enforces the **Triad of Roadmap Integrity**:
$$\text{Topological Sequencing (DD-008)} + \text{Telemetry-Calibrated Velocity (M11)} + \text{Sandbox Verification Gates (DD-006)}$$

---

## 2. Roadmap Subsystem Topology & Data Lifecycle

```
[Prescriptive Delta Targets (M07)] + [Topological DAG Path (M08)]
                               │
                               ▼
┌────────────────────────────────────────────────────────┐
│ 1. MILESTONE SYNTHESIS & SPRINT PACKAGING ENGINE       │
│ • Groups Topological Nodes into 1-Week or 2-Week Sprints│
│ • Allocates Cognitive Budget (Hours/Week vs Student Cap│
│ • Attaches Verified Institutional Syllabi & Coding Labs │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. SPRINT EXECUTION & FORMATIVE PRACTICE LAYER         │
│ • Milestone 1: Conceptual Study Units & RAG Notes (M09)│
│ • Milestone 2: Formative Diagnostic Quizzes (M03, M10) │
│ • Milestone 3: Practical Code Sandbox Assignments (M05)│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. GATEKEEPER OBJECTIVE VERIFICATION ENGINE            │
│ • Evaluates Test Pass Rate (Unit Tests >= 80%)         │
│ • Evaluates Psychometric Mastery (Rasch Theta >= Threshold│
│ • Decision: PASS (Advance) vs FAIL (Remediate)         │
└──────────────────────────┬─────────────────────────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      [GATEWAY: PASS]             [GATEWAY: FAIL]
             │                           │
  Advance to Next Milestone     Trigger Dynamic Re-Planning:
  Update F22: completion_rate   Insert Targeted Prerequisite
  Notify Digital Twin (M12)     Recalculate Remaining Timeline
```

---

## 3. Detailed Roadmap Data Structure & Schema

The roadmap is structured as a hierarchical JSON container:

```json
{
  "roadmap_id": "rdm-77a1b2-2026",
  "student_id": "stu-104928",
  "target_role": "SDE-1",
  "target_deadline": "2026-11-30",
  "status": "ACTIVE",
  "weekly_time_budget_hours": 12.0,
  "overall_progress_ratio": 0.45,
  "sprints": [
    {
      "sprint_number": 1,
      "sprint_title": "Core Algorithmic Foundations: BSTs & Heaps",
      "status": "COMPLETED",
      "milestones": [
        {
          "milestone_id": "ms-01",
          "concept_node": "CS.DSA.TREES.BST",
          "estimated_hours": 4.0,
          "learning_resources": [
            {"title": "Binary Search Trees & Balancing", "type": "CURRICULUM_RAG_NOTE", "ref": "doc-syll-cs301"},
            {"title": "LeetCode 98: Validate BST", "type": "CODING_SANDBOX_LAB", "sandbox_id": "lab-dsa-98"}
          ],
          "verification_criteria": {
            "quiz_accuracy_threshold": 0.80,
            "unit_test_coverage_threshold": 1.00
          },
          "verification_result": {
            "status": "VERIFIED",
            "score": 0.92,
            "timestamp": "2026-09-12T14:30:00Z"
          }
        }
      ]
    },
    {
      "sprint_number": 2,
      "sprint_title": "Database Transactions & Indexing Optimizations",
      "status": "IN_PROGRESS",
      "milestones": [
        {
          "milestone_id": "ms-02",
          "concept_node": "CS.DBMS.INDEXING.BTREE",
          "estimated_hours": 5.0,
          "verification_criteria": {
            "quiz_accuracy_threshold": 0.80,
            "sandbox_query_latency_ms": 50.0
          },
          "verification_result": {
            "status": "PENDING"
          }
        }
      ]
    }
  ]
}
```

---

## 4. Adaptive Re-Planning & Dynamic Velocity Calibration

### 4.1 Trigger Conditions for Roadmap Adaptation
A roadmap recalculation is automatically triggered under any of the following events:
1. **Verification Gate Failure**: Candidate fails a milestone diagnostic assessment twice consecutively ($<70\%$ accuracy).
2. **Severe Temporal Drift**: Candidate falls more than 10 calendar days behind target milestone schedule.
3. **Target Career Track Shift**: Student changes target corporate role preference (e.g., switches from SDE-1 to Cloud DevOps).
4. **Sudden Mastery Leap**: Candidate completes an advanced external certification or passes an advanced milestone with $100\%$ score, unlocking downstream topics.

### 4.2 Dynamic Re-Planning Algorithm [PROPOSED ARCHITECTURE]
When adaptation is triggered:
1. The engine locks completed historical milestones $\mathcal{M}_{\text{done}}$.
2. Re-queries the Concept DAG starting from the failed or advanced concept node.
3. If remediation is required, it inserts a micro-sprint containing the missing prerequisite sub-concepts.
4. Smooths the remaining schedule using the candidate's active `F16: consistency_score` to prevent schedule compression that induces burnout.

---

## 5. Architectural Verification & Governance

- **Verification Gate Policy**: No milestone can be marked "Complete" purely through self-reported checkmarks. Every technical milestone requires:
  - Minimum 80% score on the associated Causal Concept AQG quiz (`M10`).
  - Successful unit test pass in the Docker code sandbox (`M05`).
- **Traceability to SPV**: Verified milestone completions increment `F22: roadmap_completion_rate` in real time, which feeds back into `M06` and `M12`.
- **Status Classification**:
  - Topological milestone sequencing: `ESTABLISHED BY RESEARCH` (**Paper13**, **Paper16**, **Paper41**).
  - Dynamic automated re-planning with velocity adaptation: `PROPOSED ARCHITECTURE` (Designated for empirical validation in Phase 08).
