# PRIE REST API REFERENCE (v1)
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Base URL**: `http://127.0.0.1:8000/api/v1`  
**Authentication**: Bearer JWT Token (`Authorization: Bearer <token>`)

---

## 1. Authentication (`/auth`)

### `POST /auth/register`
* **Description**: Register a new student account with academic profile baseline.
* **Request Body**:
  ```json
  {
    "email": "student@university.edu",
    "password": "SecurePassword123!",
    "full_name": "Ada Lovelace",
    "branch": "Computer Science",
    "semester": 7,
    "cgpa": 8.75,
    "target_role": "Software Development Engineer"
  }
  ```
* **Response `200 OK`**:
  ```json
  {
    "access_token": "<jwt_string>",
    "token_type": "bearer",
    "student_id": 1,
    "name": "Ada Lovelace",
    "is_admin": false
  }
  ```

### `POST /auth/login`
* **Description**: Authenticate with email and password to receive a JWT access token.
* **Request Body**:
  ```json
  {
    "email": "demo@prie.edu",
    "password": "demo_password"
  }
  ```
* **Response `200 OK`**: Returns token and user metadata.

---

## 2. Student Profile & SPV (`/profile`)

### `GET /profile/me`
* **Description**: Fetch authenticated student's profile and academic attributes.
* **Security**: Bearer Token required.
* **Response `200 OK`**: Returns student record, current SPV, and completion stats.

### `GET /profile/spv`
* **Description**: Retrieve student's canonical 22D Student Profile Vector, raw values, and observation mask.
* **Response `200 OK`**:
  ```json
  {
    "spv_vector": [0.85, 0.72, 0.65, ...],
    "spv_dict": { "cgpa": 0.85, "dsa_score": 0.72, ... },
    "raw_dict": { "cgpa": 8.5, "dsa_score": 72.0, ... },
    "observation_mask": [1, 1, 1, ...],
    "completeness_ratio": 1.0,
    "spv_version": "v1"
  }
  ```

### `PUT /profile/update`
* **Description**: Update mutable student attributes (target role, scores, projects).

---

## 3. Placement Readiness Prediction (`/predict`)

### `POST /predict/readiness`
* **Description**: Compute calibrated placement probability via Platt-calibrated XGBoost.
* **Request Body** (Optional custom SPV, otherwise uses authenticated student):
  ```json
  {
    "spv_vector": [0.85, 0.75, ...]
  }
  ```
* **Response `200 OK`**:
  ```json
  {
    "readiness_probability": 0.8452,
    "readiness_tier": "Placement Ready",
    "ci_lower": 0.8120,
    "ci_upper": 0.8784,
    "is_mock": false,
    "status": "REAL MODEL",
    "model_version": "v1.0.0-research",
    "shap_values": { "dsa_score": 0.142, "cgpa": 0.085, ... }
  }
  ```

---

## 4. Prescriptive Explainability & Recourse (`/explain`)

### `POST /explain/prescribe`
* **Description**: End-to-end explainability pipeline ($M_{01} \to M_{04} \to M_{06} \to M_{07}$).
* **Response `200 OK`**:
  ```json
  {
    "prediction": { "readiness_probability": 0.72, ... },
    "explanation": {
      "top_barriers": [ { "feature": "dsa_score", "shap_value": -0.12, ... } ],
      "top_strengths": [ { "feature": "cgpa", "shap_value": 0.15, ... } ]
    },
    "counterfactual": {
      "recourse_directives": [
        { "feature": "dsa_score", "required_delta": 0.15, "action_text": "..." }
      ],
      "feasibility_checks": { "immutable_features_unchanged": true }
    },
    "narrative": "Your current Placement Readiness Score is 72.0%..."
  }
  ```

---

## 5. Resume Intelligence & ATS (`/resume`)

### `POST /resume/upload-pdf`
* **Description**: Multipart upload of resume PDF for spatial tokenization and ATS scoring.
* **Form Data**: `file: <binary_pdf>`, `target_role: string`.
* **Response `200 OK`**:
  ```json
  {
    "resume_ats_score": 82.5,
    "cosine_similarity": 0.764,
    "ats_breakdown": {
      "keyword_coverage_score": 34.0,
      "section_completeness_score": 22.5,
      "impact_metrics_score": 14.0,
      "length_formatting_score": 12.0
    },
    "extracted_skills": ["Python", "Docker", "PostgreSQL", "Algorithms"],
    "missing_skills": ["Kubernetes", "Redis"],
    "tokens": [ { "text": "Education", "bbox": [50, 120, 140, 135] } ]
  }
  ```

### `POST /resume/analyze-text`
* **Description**: Analyze raw resume text without PDF file upload.

---

## 6. Multimodal Mock Interview Coach (`/interview`)

### `POST /interview/analyze-media`
* **Description**: Multipart upload of recorded interview video/audio webm file.
* **Response `200 OK`**:
  ```json
  {
    "composite_score": 81.4,
    "f20_behavior_score": 0.814,
    "audio_metrics": { "pitch_mean": 145.2, "jitter": 0.011, "tempo": 124.0 },
    "video_metrics": { "gaze_persistence": 0.86, "face_presence_ratio": 0.98 },
    "speech_metrics": { "words_per_minute": 138, "filler_density": 0.018, "type_token_ratio": 0.68 },
    "transcript": "In distributed systems, we leverage Raft consensus..."
  }
  ```

### `POST /interview/analyze-text`
* **Description**: Analyze transcript text for speaking pace and lexical diversity.

---

## 7. Adaptive Assessment & Mastery (`/assessment`)

### `GET /assessment/topics`
* **Description**: Fetch available CS assessment domains (DSA, DBMS, OS, CN, Programming).

### `POST /assessment/next-item/{topic}`
* **Description**: Serve the next item calibrated to student's current proficiency level.

### `POST /assessment/submit`
* **Description**: Record student answer and update mastery score.

---

## 8. Dynamic Learning Roadmap (`/roadmap`)

### `GET /roadmap/active`
* **Description**: Fetch active student roadmap structured into Kahn DAG topological weekly milestones.

### `POST /roadmap/generate`
* **Description**: Generate a personalized curriculum roadmap targeting identified skill gaps.

### `POST /roadmap/complete/{week}`
* **Description**: Mark weekly milestone tasks completed and recalculate velocity.

---

## 9. Placement Curriculum RAG Assistant (`/rag`)

### `POST /rag/query`
* **Description**: Query curriculum corpus with dense retrieval and grounding validation.
* **Request Body**: `{ "query": "Explain deadlock detection algorithm", "top_k": 3 }`
* **Response `200 OK`**:
  ```json
  {
    "answer": "Deadlock detection involves resource allocation graph analysis...",
    "grounded": true,
    "citations": [ { "source": "Operating Systems Concepts", "section": "Deadlocks" } ]
  }
  ```

---

## 10. Bloom's Taxonomy Question Generation (`/aqg`)

### `POST /aqg/generate`
* **Description**: Generate or retrieve assessment items matching specific Bloom cognitive levels.
* **Request Body**:
  ```json
  {
    "topic": "DSA",
    "bloom_level": "Analyze",
    "difficulty": "Medium",
    "count": 2
  }
  ```

---

## 11. Company Readiness Matcher (`/company`)

### `GET /company/benchmarks`
* **Description**: List enterprise company benchmark profiles (Google, Amazon, TCS, etc.).

### `POST /company/match`
* **Description**: Evaluate student SPV against all benchmarks for compatibility and eligibility.

---

## 12. Digital Twin What-If Simulation (`/twin`)

### `POST /twin/what-if`
* **Description**: Simulate forward student placement readiness response under feature perturbation.
* **Request Body**:
  ```json
  {
    "feature_deltas": { "dsa_score": 0.15, "project_quality_score": 0.10 }
  }
  ```
* **Response `200 OK`**:
  ```json
  {
    "baseline_probability": 0.684,
    "perturbed_probability": 0.815,
    "delta_probability": 0.131,
    "feasibility_checks": { "immutable_features_unchanged": true }
  }
  ```

### `POST /twin/sensitivity`
* **Description**: Compute numerical partial derivatives $\frac{\partial P}{\partial x_i}$ across actionable dimensions.

---

## 13. Experiments Framework (`/experiments`)

### `GET /experiments/`
* **Description**: List all 6 experimental pathways (`EXP-1` to `EXP-6`) and execution statuses.

### `GET /experiments/{exp_id}`
* **Description**: Fetch detailed results, metrics, statistical tests, and LaTeX paper tables.
