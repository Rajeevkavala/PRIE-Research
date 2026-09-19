# PRIE Architecture: Learning Feedback Loop

## 1. Overview and Purpose
This document presents the detailed architectural diagram for the **PRIE Adaptive Learning Feedback Loop**.

A central limitation of existing placement prediction systems identified in `RG1` and `RG4` is their static, one-way nature: predictions are treated as immutable endpoints without continuous feedback. PRIE resolves this by establishing a **closed-loop continuous synchronization architecture** connecting student learning activity, behavioral telemetry (M10), SPV feature updates (M01), multi-stakeholder Digital Twin state synchronization (M11), and automated curricular adaptation (M07, M08).

---

## 2. Mermaid Learning Feedback Loop Diagram

```mermaid
flowchart TD
    %% Styling
    classDef actionTier fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;
    classDef telemetryTier fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100;
    classDef spvTier fill:#fce4ec,stroke:#c2185b,stroke-width:3px,color:#880e4f;
    classDef twinTier fill:#ede7f6,stroke:#7b1fa2,stroke-width:2px,color:#4a148c;
    classDef adaptTier fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef notifyTier fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#263238;

    %% 1. Student Interaction Events
    subgraph STAGE_ACTIONS ["1. Student Active Learning & Assessment Events"]
        EVT_CODE["Coding Problem Submission<br/>(Execution verdict, runtime, test passes)"]:::actionTier
        EVT_QUIZ["Adaptive AQG Assessment Item<br/>(Selected option, response latency, hints used)"]:::actionTier
        EVT_MOCK["AI Mock Interview Session<br/>(Acoustic fluency, speech rate, demeanor index)"]:::actionTier
        EVT_CLICK["LMS Telemetry Stream<br/>(Video pause/drop-off, reading time, login streak)"]:::actionTier
    end

    %% 2. Telemetry Ingestion & Aggregation
    subgraph STAGE_TELEMETRY ["2. M10: Behavioral Telemetry & Analytics Engine"]
        INGEST_QUEUE["Event Ingestion Buffer<br/>(Redis Stream / TimescaleDB Hypertable)"]:::telemetryTier
        FEATURE_AGGREGATOR["Behavioral Aggregator & Rollup Worker<br/>- Rolling 7-Day Study Hours Calculation<br/>- Login Frequency & Retest Persistence Metric<br/>- Hesitation & Drop-off Index Formulation"]:::telemetryTier
        EARLY_WARN["Weeks 3-4 Early Warning Trigger<br/>(Detects Disengagement Drop: Activity Decrease > 30%)"]:::telemetryTier
    end

    %% 3. SPV Mutation Engine
    subgraph STAGE_SPV ["3. M01: Invariant 22-Dimensional SPV Update"]
        SPV_MUTATOR["Profile Vector Synchronization Worker<br/>Atomically re-evaluates:<br/>- F04 (LeetCode count) & F06 (DSA Exam score)<br/>- F14-F17 (Mock score, WPM, fillers, confidence)<br/>- F18-F22 (Study hours, logins, persistence, roadmap %)"]:::spvTier
        SPV_LEDGER[("PostgreSQL SPV Ledger<br/>(Versioned Snapshot with Timestamp)")]:::spvTier
    end

    %% 4. Digital Twin Synchronization
    subgraph STAGE_TWIN ["4. M11: Digital Twin Multi-Stakeholder Sync"]
        TWIN_SYNC["Digital Twin Synchronization Engine<br/>- Computes Delta: Delta v_s = v_s(t) - v_s(t-1)<br/>- Recalculates Historical Trajectory & Velocity<br/>- Projects Future Placement Probability Horizon"]:::twinTier
        TWIN_STATE[("Digital Twin State Store<br/>(Real-Time Redis Cache + Historical PG)")]:::twinTier
    end

    %% 5. Adaptive Prescriptive Re-planning
    subgraph STAGE_ADAPT ["5. Closed-Loop Adaptation (M02, M07, M08)"]
        GAP_RECALC["M02: Skill Gap Vector Update<br/>(Removes mastered concepts, shrinks distance)"]:::adaptTier
        ASTAR_REPLAN["M07: A* DAG Dynamic Re-routing<br/>(Re-computes optimal path if student struggles or excels)"]:::adaptTier
        ROADMAP_REVISE["M08: Adaptive Roadmap Revision<br/>- Inserts prerequisite remedial nodes if failure rate > 40%<br/>- Accelerates sprint schedule if mastery threshold met"]:::adaptTier
    end

    %% 6. Multi-Stakeholder Notifications
    subgraph STAGE_NOTIFY ["6. Stakeholder Interventions & UI Updates"]
        UI_STUDENT["Student Dashboard UI<br/>(Roadmap dynamically updates, next task ready)"]:::notifyTier
        UI_FACULTY["Faculty / Mentor Portal<br/>(At-Risk early warning alert triggered)"]:::notifyTier
        UI_RECRUITER["Recruiter Talent Pool<br/>(Differential privacy aggregate readiness shifts)"]:::notifyTier
    end

    %% Connections: Events to Telemetry
    EVT_CODE --> INGEST_QUEUE
    EVT_QUIZ --> INGEST_QUEUE
    EVT_MOCK --> INGEST_QUEUE
    EVT_CLICK --> INGEST_QUEUE

    INGEST_QUEUE --> FEATURE_AGGREGATOR
    FEATURE_AGGREGATOR --> EARLY_WARN

    %% Telemetry to SPV
    FEATURE_AGGREGATOR --> SPV_MUTATOR
    EVT_CODE --> SPV_MUTATOR
    EVT_QUIZ --> SPV_MUTATOR
    EVT_MOCK --> SPV_MUTATOR

    SPV_MUTATOR --> SPV_LEDGER
    SPV_LEDGER --> TWIN_SYNC

    %% Twin Sync to State
    TWIN_SYNC --> TWIN_STATE

    %% State to Adaptation
    TWIN_STATE --> GAP_RECALC
    GAP_RECALC --> ASTAR_REPLAN
    ASTAR_REPLAN --> ROADMAP_REVISE

    %% Adaptation to Notifications & Loop Close
    ROADMAP_REVISE --> UI_STUDENT
    EARLY_WARN --> UI_FACULTY
    TWIN_SYNC --> UI_RECRUITER

    %% Closed loop arrow back to learning
    ROADMAP_REVISE -.->|"Delivers New Adaptive Tasks"| EVT_CODE
    ROADMAP_REVISE -.->|"Delivers New Adaptive Tasks"| EVT_QUIZ
```

---

## 3. Feedback Loop Invariants and Performance Gates

| Loop Component | Triggering Frequency | Execution SLA | Mutated State Entities |
| :--- | :--- | :--- | :--- |
| **Instant Score Updates** | Immediate upon test/code submit | $< 1.0\text{ s}$ | $F04, F06, F14$ raw scores in session cache |
| **Behavioral Rollup** | Hourly micro-batch | $< 15.0\text{ s}$ | $F18$ (Hours), $F19$ (Frequency), $F21$ (Hesitation) |
| **Twin Trajectory Sync** | Daily at 00:00 UTC (or post-session) | $< 2.0\text{ s}$ | Digital Twin historical velocity, 90-day projection |
| **Curricular Re-planning** | Upon milestone failure / completion | $< 500\text{ ms}$ | Weekly Roadmap task sequence, prerequisite injections |
| **Early Warning Escalation** | Continuous threshold check | $< 100\text{ ms}$ | Mentor notification queue (Weeks 3–4 dropout prevention) |
