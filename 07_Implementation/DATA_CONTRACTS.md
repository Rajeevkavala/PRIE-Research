# PRIE DATA CONTRACTS & SPV CANONICAL SPECIFICATION
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Epistemological Basis**: Phases 04 (`Feature_Traceability.md`) & 05 (`Student_Profile_Vector_Architecture.md`)  
**Schema Version**: `SPV_VERSION = "v1"`  
**Tensor Dimension**: $\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$

---

## 1. Authoritative Student Profile Vector (SPV) Contract

The canonical Student Profile Vector $\mathbf{x}_{\text{spv}}$ is a 22-dimensional real-valued feature vector representing a student's holistic multi-dimensional placement readiness. Every downstream module ($M_{04}, M_{06}, M_{07}, M_{08}, M_{11}, M_{12}$) must consume this vector in this exact order.

### Feature Definition Table ($F_{01}$ through $F_{22}$)

| ID | Feature Name | Dimension Domain | Raw Range | Normalized Range | Actionability | Epistemological Source |
|:---|:---|:---|:---|:---|:---|:---|
| **$F_{01}$** | `cgpa` | Academic Performance | $[0.0, 10.0]$ | $[0.0, 1.0]$ | Low (Cumulative) | Official Academic Transcript |
| **$F_{02}$** | `dsa_score` | Core Technical Mastery | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Adaptive Cognitive Quiz |
| **$F_{03}$** | `dbms_score` | Core Technical Mastery | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Adaptive Cognitive Quiz |
| **$F_{04}$** | `os_score` | Core Technical Mastery | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Adaptive Cognitive Quiz |
| **$F_{05}$** | `cn_score` | Core Technical Mastery | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Adaptive Cognitive Quiz |
| **$F_{06}$** | `programming_score` | Programming Proficiency | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Code Tracing Assessment |
| **$F_{07}$** | `aptitude_score` | Cognitive / Quantitative | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{03}$ Quantitative Assessment |
| **$F_{08}$** | `soft_skills_score` | Communication & Demeanor | $[0.0, 100.0]$ | $[0.0, 1.0]$ | Medium | Module $M_{05}$ Behavioral Mock Interview |
| **$F_{09}$** | `project_count` | Practical Experience | $[0, 20]$ | $[0.0, 1.0]$ | High (Monotonic $\uparrow$) | Resume Extraction ($M_{02}$) / Profile |
| **$F_{10}$** | `project_quality_score` | Architecture & Code Depth | $[0.0, 10.0]$ | $[0.0, 1.0]$ | High | Portfolio Audit ($M_{02}$) |
| **$F_{11}$** | `has_internship` | Industry Exposure | $\{0, 1\}$ | $[0.0, 1.0]$ | Medium (Monotonic $\uparrow$) | Verified Experience Records |
| **$F_{12}$** | `certifications_count` | External Validation | $[0, 15]$ | $[0.0, 1.0]$ | High (Monotonic $\uparrow$) | Verified Credential Records |
| **$F_{13}$** | `resume_ats_score` | Resume Syntactic Quality | $[0.0, 100.0]$ | $[0.0, 1.0]$ | High | Module $M_{02}$ Multi-Dimensional ATS |
| **$F_{14}$** | `cosine_similarity` | Resume–JD Semantic Alignment | $[0.0, 1.0]$ | $[0.0, 1.0]$ | High | Module $M_{02}$ SBERT Dense Embedding Match |
| **$F_{15}$** | `gap_score` | Total Competency Deficit | $[0.0, 1.0]$ | $[0.0, 1.0]$ | Computed State | Module $M_{04}$ Skill Gap Engine |
| **$F_{16}$** | `consistency_score` | Habitual Learning Velocity | $[0.0, 1.0]$ | $[0.0, 1.0]$ | High | Telemetry / Activity Streak Tracker |
| **$F_{17}$** | `branch_encoded` | Academic Department | $\{0, 1, 2, 3, 4\}$ | $[0.0, 1.0]$ | **IMMUTABLE** | Institutional Registrar (Locked) |
| **$F_{18}$** | `target_role_encoded` | Target Career Complexity | $\{0, 1, 2, 3, 4\}$ | $[0.0, 1.0]$ | Medium | Student Goal Configuration |
| **$F_{19}$** | `assessment_attempts` | Practice Volume & Grit | $[0, 100]$ | $[0.0, 1.0]$ | High (Monotonic $\uparrow$) | Quiz Session Database Logs |
| **$F_{20}$** | `behavior_score` | Interview Composure | $[0.0, 1.0]$ | $[0.0, 1.0]$ | Medium | Module $M_{05}$ Multimodal Late Fusion |
| **$F_{21}$** | `engagement_score` | Platform Task Completion | $[0.0, 1.0]$ | $[0.0, 1.0]$ | High | Weekly LMS Action Logs |
| **$F_{22}$** | `roadmap_completion_rate`| Curriculum Progress | $[0.0, 1.0]$ | $[0.0, 1.0]$ | High (Monotonic $\uparrow$) | Module $M_{08}$ Kahn DAG Milestones |

---

## 2. Invariance & Recourse Restrictions

### A. Immutable Feature Lock ($F_{17}$)
* Feature $F_{17}$ (`branch_encoded`) represents a student's enrolled academic branch (e.g., Computer Science, Information Technology, Electronics, Mechanical, Civil).
* **Ethical and Pragmatic Hard Constraint**: Prescriptive counterfactual recourse ($M_{07}$ DiCE) and What-if simulation ($M_{12}$ Digital Twin) **MUST NEVER** prescribe altering $F_{17}$ (e.g., recommending a Mechanical Engineering student change their branch in their final year).
* **Enforcement**: Any perturbation vector $\Delta \mathbf{x}$ where $\Delta x_{17} \neq 0$ triggers an immediate `ImmutableFeaturePerturbationError` or is projected to $0$.

### B. Monotonic Non-Decreasing Constraints
The following cumulative features represent accumulated life experience and can never decrease during counterfactual recourse:
* $F_{09}$ (`project_count`)
* $F_{11}$ (`has_internship`)
* $F_{12}$ (`certifications_count`)
* $F_{19}$ (`assessment_attempts`)
* $F_{22}$ (`roadmap_completion_rate`)

### C. Normalization Bounds
Every normalized feature value $x_i$ must satisfy:
$$0.0 \le x_i \le 1.0 \quad \forall i \in \{1, \dots, 22\}$$
Any vector containing values outside this range, or containing `NaN`, `+Inf`, or `-Inf`, is rejected immediately with a `SPVValidationError`.

---

## 3. Strict Rejection of Legacy Prototype Schemas

The legacy prototype codebase (`07_Implementation/src/`) defined an ad-hoc 10-feature schema that included ungrounded features:
* ❌ `backlogs` (Replaced by transcript GPA & verified eligibility filters)
* ❌ `internship_months` (Replaced by canonical binary indicator $F_{11}$ `has_internship`)
* ❌ `skill_count` (Replaced by fine-grained technical scores $F_{02}$–$F_{06}$ and ATS coverage $F_{13}$)

**Validator Enforcement**:
If an incoming request or dictionary contains `backlogs`, `internship_months`, or `skill_count`, `validate_spv_dict()` raises an immediate `ValueError: Legacy feature detected`.

---

## 4. Observation Mask ($\mathbf{m} \in \{0, 1\}^{22}$)

In real-world institutional settings, a student may be missing certain empirical observations (e.g., before taking an interview or before uploading a resume).
* For each feature $i$, $m_i = 1$ if empirically observed, and $m_i = 0$ if imputed or pending.
* **Completeness Ratio**:
  $$C = \frac{1}{22}\sum_{i=1}^{22} m_i$$
* If $C < 0.60$, the system issues a warning and restricts high-confidence placement certifications until foundational assessments are completed.
