# Student Profile Vector (SPV) Methodology: Mathematical Construction, Imputation & Tensor Lifecycle

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Student_Profile_Vector_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative SPV Construction Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Mathematical Tensor Representation

The **Student Profile Vector (SPV)** is the central representational construct of the PRIE architecture (`DD-001`, `M01`). It provides a normalized, continuous-categorical numerical encoding of candidate employability.

Formally, at discrete timestamp $t$, student $s$ is represented as:
$$\mathbf{x}_{	ext{spv}}^{(s)}(t) = ig[ f_1, f_2, \dots, f_{22} ig]^T \in [0.0, 1.0]^{22}$$

To account for incomplete data across academic semesters without corrupting downstream estimators, every SPV tensor is paired with an invariant binary observation mask:
$$\mathbf{m}^{(s)}(t) \in \{0, 1\}^{22}, \quad m_i = egin{cases} 1 & 	ext{if } f_i 	ext{ is directly measured from telemetry} \ 0 & 	ext{if } f_i 	ext{ is unobserved and imputed} \end{cases}$$

---

## 2. Exhaustive 22-Dimensional SPV Specification Matrix

The ordering, bounds, types, and imputation rules for all 22 invariant features are defined below:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                          INVARIANT 22-DIMENSIONAL SPV TENSOR SCHEMA                         │
├─────┬──────────────────────────┬──────────────┬───────────────┬─────────────┬───────────────┤
│ ID  │ Feature Name             │ Native Type  │ Scaled Domain │ Imputation  │ Modality      │
├─────┼──────────────────────────┼──────────────┼───────────────┼─────────────┼───────────────┤
│ F01 │ cgpa                     │ Float [0, 10]│ [0.0, 1.0]    │ None (Mand) │ SIS Tabular   │
│ F02 │ dsa_score                │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Diagnostic M03│
│ F03 │ dbms_score               │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Diagnostic M03│
│ F04 │ os_score                 │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Diagnostic M03│
│ F05 │ cn_score                 │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Diagnostic M03│
│ F06 │ programming_score        │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Sandbox M05   │
│ F07 │ aptitude_score           │ Float [0,100]│ [0.0, 1.0]    │ MICE        │ Diagnostic M03│
│ F08 │ soft_skills_score        │ Float [0,100]│ [0.0, 1.0]    │ Median      │ Diagnostic M03│
│ F09 │ project_count            │ Integer [0,20│ Scaled [0, 1] │ Zero (0)    │ Resume M02    │
│ F10 │ project_quality_score    │ Float [0,100]│ [0.0, 1.0]    │ Zero (0)    │ Resume M02    │
│ F11 │ has_internship           │ Binary {0, 1}│ {0.0, 1.0}    │ Zero (0)    │ Resume M02    │
│ F12 │ certifications_count     │ Integer [0,15│ Scaled [0, 1] │ Zero (0)    │ Resume M02    │
│ F13 │ resume_ats_score         │ Float [0,100]│ [0.0, 1.0]    │ Default 0.5 │ ATS Parser M02│
│ F14 │ cosine_similarity        │ Float [0, 1] │ [0.0, 1.0]    │ Default 0.0 │ S-BERT M02    │
│ F15 │ gap_score                │ Float [0, 1] │ [0.0, 1.0]    │ Default 1.0 │ Gap Engine M04│
│ F16 │ consistency_score        │ Float [0, 1] │ [0.0, 1.0]    │ Default 0.5 │ Telemetry M11 │
│ F17 │ branch_encoded           │ Categorical  │ Target [0, 1] │ None (Mand) │ SIS Tabular   │
│ F18 │ target_role_encoded      │ Float [0, 1] │ [0.0, 1.0]    │ Default 0.5 │ Student Target│
│ F19 │ assessment_attempts      │ Integer [0,99│ Scaled [0, 1] │ Zero (0)    │ Telemetry M11 │
│ F20 │ behavior_score           │ Float [0,100]│ [0.0, 1.0]    │ Median      │ Interview M05 │
│ F21 │ engagement_score         │ Float [0, 1] │ [0.0, 1.0]    │ Default 0.5 │ Telemetry M11 │
│ F22 │ roadmap_completion_rate  │ Float [0, 1] │ [0.0, 1.0]    │ Zero (0)    │ Roadmap M08   │
└─────┴──────────────────────────┴──────────────┴───────────────┴─────────────┴───────────────┘
```

---

## 3. SPV Construction Pipeline

The end-to-end mathematical construction of $\mathbf{x}_{	ext{spv}}$ proceeds through six sequential steps:

1. **Data Ingress & Sanitization**: Raw values are ingested from SIS, ATS, Interview, and LMS logs. Extreme outliers outside theoretical physical limits are clipped.
2. **Missing Feature Detection**: The observation mask is initialized:
   $$m_i = egin{cases} 1 & 	ext{if } f_i 	ext{ is present in telemetry} \ 0 & 	ext{if } f_i 	ext{ is missing/unobserved} \end{cases}$$
3. **MICE Imputation for Unobserved Features**: Missing diagnostic competencies (`F02`–`F07`) are imputed using the pre-fitted MICE pipeline.
4. **Target Encoding for Categorical Attributes**: Departmental specialization (`branch_encoded`: `F17`) is encoded using smoothed empirical out-of-fold target encoding:
   $$	ilde{f}_{17} = rac{n_{	ext{branch}} \cdot ar{y}_{	ext{branch}} + m \cdot ar{y}_{	ext{global}}}{n_{	ext{branch}} + m}$$
   where $m = 10$ is the Bayesian smoothing parameter.
5. **Continuous Normalization**: All features are bounded within $[0.0, 1.0]$ via fitted Min-Max scalers.
6. **Temporal Decay Weighting**: For features dependent on student practice (`dsa_score`, `programming_score`), observations older than 90 days undergo exponential temporal decay:
   $$f_i(t) = f_i(t_0) \cdot \exp\Big( -\gamma (t - t_0) \Big) + f_{	ext{baseline}} \cdot \Big( 1 - \exp(-\gamma(t - t_0)) \Big)$$
   where $\gamma = 0.005$ per day.
