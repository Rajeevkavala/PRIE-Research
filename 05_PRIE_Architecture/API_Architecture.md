# API Architecture: Logical Service Interfaces, Contracts & Protocols

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/API_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative API Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & API Design Principles

The API Architecture defines the logical communication contracts between external clients (Student, Faculty, Placement Cell interfaces) and internal PRIE intelligence microservices.

**Core Principles**:
1. **RESTful Semantics with Strict JSON Schema**: Standard OpenAPI 3.1 specification for transactional and request-response operations.
2. **Streaming Protocols for Low-Latency Perceptual Flows**: Full-duplex WebSockets (`WSS`) for chunked audio and real-time digital twin state synchronization.
3. **Zero-Trust Security & RBAC**: Every request is authenticated via cryptographically signed JWT tokens carrying Role-Based Access Control scopes (`student`, `faculty_mentor`, `placement_officer`, `recruiter`, `admin`).
4. **Differential Privacy Boundary**: All aggregate endpoints queried by corporate recruiters route through the Differential Privacy Proxy (`CMP-GW-PRIV`).
5. **Idempotency**: All state-mutating endpoints enforce idempotency via `Idempotency-Key` headers.

---

## 2. Global Service Endpoint Taxonomy

```
/api/v1/
├── auth/                    [Authentication & Session Token Management]
├── profile/                 [Student Profile Vector (SPV) Compilation & Read]
├── resume/                  [LayoutLMv3 Multi-Column Parsing & ATS Matching]
├── predict/                 [Dual-Track Placement Readiness Inference (M06)]
├── explain/                 [TreeSHAP Attribution & DiCE Prescriptive Recourse]
├── roadmap/                 [Topological Prerequisite Learning Pathways (M08)]
├── interview/               [Streaming Mock Interview & Ephemeral Sandbox]
├── assessment/              [Adaptive IRT Quizzing & Causal Concept AQG]
├── rag/                     [Two-Stage Curriculum RAG Assistant (M09)]
└── twin/                    [Triangular Digital Twin State Sync & Recruiter Analytics]
```

---

## 3. Logical Endpoint Specifications

---

### 3.1 Student Profile Vector (SPV) Interface (`M01`)

#### `GET /api/v1/profile/spv`
- **Purpose**: Retrieves the active, normalized 22-dimensional Student Profile Vector and confidence mask for the authenticated student.
- **Authorization**: `Bearer JWT` (Scopes: `student:read`, `faculty:read`).
- **Request Parameters**: None (Extracted from JWT subject).
- **Response Payload (200 OK)**:
  ```json
  {
    "student_id": "stu-104928",
    "timestamp": "2026-09-17T14:30:00Z",
    "version": 4,
    "features": {
      "F01_cgpa": 8.42,
      "F02_dsa_score": 78.5,
      "F03_dbms_score": 82.0,
      "F04_os_score": 68.0,
      "F05_cn_score": 74.0,
      "F06_programming_score": 88.0,
      "F07_aptitude_score": 72.0,
      "F08_soft_skills_score": 65.0,
      "F09_project_count": 3,
      "F10_project_quality_score": 75.0,
      "F11_has_internship": 1,
      "F12_certifications_count": 2,
      "F13_resume_ats_score": 84.5,
      "F14_cosine_similarity": 0.812,
      "F15_gap_score": 0.245,
      "F16_consistency_score": 0.782,
      "F17_branch_encoded": 0.85,
      "F18_target_role_encoded": 0.75,
      "F19_assessment_attempts": 28,
      "F20_behavior_score": 71.5,
      "F21_engagement_score": 0.820,
      "F22_roadmap_completion_rate": 0.650
    },
    "confidence_mask": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  }
  ```
- **Error Responses**: `401 Unauthorized`, `404 Not Found`.

---

### 3.2 Resume Intelligence & Multi-Column ATS Matcher (`M02`)

#### `POST /api/v1/resume/parse-and-match`
- **Purpose**: Uploads multi-column PDF resume, extracts structured entities using `LayoutLMv3`, and computes dense semantic alignment against target JD using `Sentence-BERT`.
- **Authorization**: `Bearer JWT` (Scope: `student:write`).
- **Request Type**: `multipart/form-data`.
- **Payload**:
  - `resume_file`: Binary PDF document (max 5MB).
  - `target_jd_id`: UUID of target corporate Job Description.
- **Response Payload (202 Accepted)**:
  ```json
  {
    "job_id": "job-parse-99120",
    "status": "PROCESSING",
    "estimated_latency_ms": 1200,
    "websocket_channel": "wss://prie.internal/v1/jobs/job-parse-99120"
  }
  ```
- **Async Completed Payload (via WebSocket or GET polling)**:
  ```json
  {
    "status": "COMPLETED",
    "f13_resume_ats_score": 86.0,
    "f14_cosine_similarity": 0.845,
    "extracted_entities": {
      "education": [{"degree": "B.Tech Computer Science", "institution": "State University", "gpa": "8.4"}],
      "skills": ["Python", "FastAPI", "Docker", "PostgreSQL", "React"],
      "projects": [{"title": "Distributed Task Queue", "tech": ["Redis", "Python", "Celery"]}]
    },
    "layout_diagnostics": {
      "multi_column_detected": true,
      "bounding_box_coherence": 0.94,
      "scrambled_blocks_detected": 0
    }
  }
  ```

---

### 3.3 Placement Readiness Prediction Engine (`M06`)

#### `POST /api/v1/predict/readiness`
- **Purpose**: Evaluates candidate readiness using dual-track XGBoost (cross-sectional tier) and Temporal Fusion Transformer (longitudinal forecast).
- **Authorization**: `Bearer JWT` (Scope: `student:read`, `faculty:read`).
- **Request Body**:
  ```json
  {
    "student_id": "stu-104928",
    "include_longitudinal_forecast": true
  }
  ```
- **Response Payload (200 OK)**:
  ```json
  {
    "student_id": "stu-104928",
    "track1_static": {
      "readiness_probability": 0.52,
      "readiness_tier": "Needs Remediation",
      "model_version": "prie-xgb-static-v2.1",
      "brier_calibration_score": 0.082
    },
    "track2_longitudinal": {
      "horizon_6_month": {
        "p10": 0.44,
        "p50": 0.62,
        "p90": 0.78
      },
      "horizon_12_month": {
        "p10": 0.51,
        "p50": 0.74,
        "p90": 0.88
      },
      "temporal_attention_peak": "Semester_5_Week_4"
    }
  }
  ```

---

### 3.4 Prescriptive Explainability & Counterfactual Recourse (`M07`)

#### `POST /api/v1/explain/prescribe`
- **Purpose**: Computes local TreeSHAP attribution and solves DiCE constraint-optimized counterfactuals to generate actionable remediation targets.
- **Authorization**: `Bearer JWT` (Scope: `student:read`).
- **Request Body**:
  ```json
  {
    "student_id": "stu-104928",
    "target_probability": 0.75,
    "max_counterfactual_actions": 3
  }
  ```
- **Response Payload (200 OK)**:
  ```json
  {
    "descriptive_shap": [
      {"feature": "F02_dsa_score", "attribution_phi": -0.22, "meaning": "DSA score below target threshold"},
      {"feature": "F11_has_internship", "attribution_phi": -0.18, "meaning": "Absence of industrial internship"},
      {"feature": "F06_programming_score", "attribution_phi": +0.14, "meaning": "Strong coding test pass rate"}
    ],
    "prescriptive_counterfactual_recourse": {
      "target_probability": 0.76,
      "proximity_L1": 0.12,
      "sparsity_L0": 2,
      "actionable_deltas": [
        {
          "feature": "F02_dsa_score",
          "current_value": 78.5,
          "target_value": 90.0,
          "directive": "Elevate DSA score by +11.5 points via Trees and Graphs sprint."
        },
        {
          "feature": "F10_project_quality_score",
          "current_value": 75.0,
          "target_value": 90.0,
          "directive": "Deploy existing full-stack project to cloud with automated CI/CD pipeline."
        }
      ],
      "immutable_features_locked": ["F17_branch_encoded", "F01_cgpa"]
    }
  }
  ```

---

### 3.5 Multimodal Mock Interview Streaming Interface (`M05`)

#### `WSS /v1/interview/stream`
- **Purpose**: Real-time bidirectional streaming audio, dialogue generation, and telemetry uplink.
- **Protocol**: Secure WebSocket (`WSS`).
- **Client Uplink Messages**:
  - `type: "audio_chunk"`: Base64-encoded 250ms Opus audio frame.
  - `type: "telemetry_scalar"`: Client Wasm MediaPipe non-verbal metrics (`{blink_rate, gaze_stability, pause_ratio}`).
  - `type: "code_submission"`: Source code string and target language (`python`, `java`).
- **Server Downlink Messages**:
  - `type: "transcript_turn"`: Real-time Whisper transcript of candidate utterance.
  - `type: "interviewer_speech"`: Streaming audio buffer of synthesized interviewer question.
  - `type: "sandbox_result"`: Docker container unit test execution report.

---

### 3.6 Curriculum RAG Assistant Interface (`M09`)

#### `POST /api/v1/rag/query`
- **Purpose**: Natural language question answering grounded in verified institutional syllabi and corporate drive policies.
- **Authorization**: `Bearer JWT` (Scope: `student:read`).
- **Request Body**:
  ```json
  {
    "query": "What are the essential requirements for operating systems concurrency?",
    "target_subject": "Operating Systems"
  }
  ```
- **Response Payload (200 OK)**:
  ```json
  {
    "answer": "Operating systems concurrency requires managing mutual exclusion, deadlock avoidance, and synchronization primitives (mutexes, semaphores, and condition variables)...",
    "citations": [
      {"document": "OS_Syllabus_2026.pdf", "section": "Module 3: Concurrency & Semaphores", "page": 14}
    ],
    "rag_triad_verification": {
      "context_relevance": 0.92,
      "groundedness": 0.96,
      "answer_relevance": 0.94,
      "triad_verdict": "PASS"
    }
  }
  ```

---

### 3.7 Triangular Digital Twin & Recruiter Analytics (`M12`)

#### `GET /api/v1/twin/recruiter/cohort-distribution`
- **Purpose**: Provides aggregate institutional cohort statistics to corporate recruiters, protected by Differential Privacy (`DD-011`).
- **Authorization**: `Bearer JWT` (Scope: `recruiter:read`).
- **Request Parameters**: `?role=SDE-1&branch=CS`.
- **Response Payload (200 OK)**:
  ```json
  {
    "role": "SDE-1",
    "eligible_candidates_count": 142,
    "mean_readiness_score": 0.74,
    "privacy_guarantee": {
      "mechanism": "Laplace_Mechanism",
      "epsilon_applied": 0.85,
      "delta": 0.0,
      "dp_compliant": true
    },
    "distribution_percentiles": {
      "p25": 0.65,
      "p50": 0.76,
      "p75": 0.88
    }
  }
  ```

---

## 4. API Error Handling & Status Codes

All PRIE API responses adhere to standard RFC 7807 Problem Details:

```json
{
  "type": "https://prie.internal/errors/constraint-violation",
  "title": "Immutable Feature Modification Rejected",
  "status": 400,
  "detail": "Feature F17_branch_encoded is strictly immutable under DiCE optimization rules.",
  "instance": "/api/v1/explain/prescribe",
  "timestamp": "2026-09-17T14:35:00Z"
}
```

| HTTP Status | Meaning | Typical Trigger |
|:---|:---|:---|
| **200 OK** | Successful Request | Synchronous inference, profile retrieval. |
| **202 Accepted** | Background Task Queued | Heavy resume parsing (`LayoutLMv3`), counterfactual search. |
| **400 Bad Request** | Schema / Constraint Error | Malformed feature tensor, immutable feature violation. |
| **401 Unauthorized**| Missing / Expired JWT | Invalid signature or expired auth token. |
| **403 Forbidden** | RBAC Scope Violation | Student attempting to query faculty advisee roster. |
| **422 Unprocessable**| Semantic Validation Error| Corrupted PDF binary or un-executable code syntax. |
| **429 Too Many Req** | Rate Limit Exhausted | Exceeding token bucket limits on ML inference endpoints. |
| **503 Service Unavail**| Model Worker Down | Worker GPU OOM; triggers automated fallback degradation. |
