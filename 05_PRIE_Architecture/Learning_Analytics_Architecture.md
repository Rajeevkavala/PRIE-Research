# Learning Analytics Architecture: Behavioral Telemetry & Longitudinal Modeling (M11)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Learning_Analytics_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Learning Analytics Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & Longitudinal Early Intervention

In traditional educational data mining, candidate modeling fails due to **Static Snapshot Blindness (`RG2`)**. As synthesized in Phase 02 (`02_Cross_Analysis/Learning_Analytics_Comparison.md`):
- **Literature Finding**: **Paper02** (Van Wyk & Du Plessis 2025) and **Paper05** (Chen et al. 2024) established that the **critical early-intervention window** in academic preparation occurs during **Weeks 3–4**. 
- If student disengagement is not detected and addressed within this window, academic unreadiness and placement failure rates increase by over $70\%$.
- Static placement models evaluating students only in final semesters miss this window entirely.

Module `M11` establishes a continuous, asynchronous **Behavioral Telemetry & Longitudinal Analytics Architecture** designed to capture student habit persistence, learning velocity, and disengagement markers to feed the temporal prediction track (`M06`) and digital twin (`M12`).

---

## 2. Learning Analytics Subsystem Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. RAW INTERACTION EVENT STREAM                                        │
│ • Client Session Events: Login, Page View, Resource Download           │
│ • Practice Events: Quiz Start, Question Answered, Hint Requested       │
│ • Sandbox Events: Code Run, Unit Test Execution, Debugging Cycles      │
│ • Interview Events: Turn Turnaround Latency, Audio Duration            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Non-Blocking Redis Event Bus
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. TIME-SERIES INGESTION & EVENT STORE (TimescaleDB)                   │
│ • Partitioned Hyper-Tables for Millisecond-Precision Logging           │
│ • Event Deduplication & Idempotent Sequencing                          │
│ • PII Anonymization & Device Metadata Stripping                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Rolling Window Aggregation
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. DERIVED FEATURE EXTRACTION ENGINE (M11)                             │
│ • Habit Persistence & Cadence -> F16: consistency_score                │
│ • Cumulative Practice Volume  -> F19: assessment_attempts              │
│ • Multidimensional Intensity  -> F21: engagement_score                 │
│ • Early-Warning Anomaly Detection (14-Day Velocity Decay)              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
┌───────────────────────────────────────┐   ┌────────────────────────────┐
│ 4. SPV TENSOR UPDATE HANDOFF          │   │ 5. EARLY-WARNING ALERTS    │
│ • Dispatches F16, F19, F21 to M01     │   │ • Triggers M12 Digital Twin│
│ • Triggers Temporal Fusion Transformer│   │ • Surfaces At-Risk Flag on │
│   Sequence Retraining in M06          │   │   Faculty Mentor Dashboard │
└───────────────────────────────────────┘   └────────────────────────────┘
```

---

## 3. Strict Epistemological Separation: Events vs Features vs Predictions

To prevent circular reasoning, telemetry data is categorized into four distinct layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DATA ABSTRACTION HIERARCHY                      │
├────────────────────────────────────────────────────────────────────────┤
│ LEVEL 1: RAW INTERACTION EVENTS                                        │
│ • Unprocessed factual event stream:                                    │
│   {"event_id": "ev-892", "type": "quiz_submit", "duration_sec": 412}  │
├────────────────────────────────────────────────────────────────────────┤
│ LEVEL 2: DERIVED LONGITUDINAL FEATURES                                 │
│ • Mathematically transformed aggregated metrics (SPV components):      │
│   - F16: consistency_score (EMA over 6 weeks)                          │
│   - F19: assessment_attempts (Monotonic count)                         │
│   - F21: engagement_score (Percentile ranking)                         │
├────────────────────────────────────────────────────────────────────────┤
│ LEVEL 3: MODEL PREDICTIONS                                             │
│ • Statistical inferences generated by machine learning models (M06):   │
│   - Placement Probability P_ready, Readiness Tier, TFT Quantiles       │
├────────────────────────────────────────────────────────────────────────┤
│ LEVEL 4: ACTIONABLE RECOMMENDATIONS                                    │
│ • Prescriptive interventions derived from predictions (M07, M08):      │
│   - DiCE counterfactuals, prerequisite DAG roadmaps                    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Mathematical Feature Derivations

### 4.1 Feature F16: `consistency_score` (Longitudinal Habit Persistence)
Calculated using an Exponential Moving Average (EMA) of active weekly practice sessions over the preceding 6-week window:
$$\text{EMA}_t = \alpha \cdot \text{ActiveRatio}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}$$
where $\alpha = 0.3$ and $\text{ActiveRatio}_t = \frac{\text{Days with practice in week } t}{7.0}$.
- **Decay Penalty**: If zero events are recorded in week $t$, $\text{ActiveRatio}_t = 0.0$, applying an exponential decay that reflects habit erosion.

### 4.2 Feature F21: `engagement_score` (Interaction Intensity)
A multi-factor composite normalized against the active institutional cohort distribution:
$$F_{21} = 0.4 \cdot \tilde{T}_{\text{session}} + 0.3 \cdot \tilde{A}_{\text{quiz}} + 0.3 \cdot \tilde{C}_{\text{code}}$$
where $\tilde{T}$, $\tilde{A}$, and $\tilde{C}$ represent cohort-percentile normalized metrics for weekly active session duration, quiz items answered, and code test runs executed.

---

## 5. Early-Warning Disengagement Detection (Week 3–4)

`M11` executes continuous anomaly detection across student cohorts:
- **Trigger Rule**: If $\Delta F_{21} = F_{21}(t) - F_{21}(t-14\text{ days}) < -0.30$ and $F_{16} < 0.40$:
  - Mark candidate as **`Early-Warning At-Risk`**.
  - Dispatch urgent alert to Faculty Advisor via `M12` (`DD-010`).
  - Target: $>85\%$ sensitivity in detecting potential placement dropouts before Semester 6 ends.
