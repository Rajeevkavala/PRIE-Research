# ScholarCamp / PRIE Interactive Research Demonstration Script

**System**: Placement Readiness Intelligence Engine (PRIE)  
**Document**: `10_Publication/06_Demo/Demo_Script.md`  
**Purpose**: Live step-by-step conference demonstration protocol  
**Target Duration**: 8–10 Minutes  
**Target Audience**: Academic Reviewers, Conference Attendees, Industry Liaisons  

---

## Stage 1: Student Onboarding & 22D Profile Vector Assembly (Minutes 00:00 – 02:00)
* **Objective**: Demonstrate ingestion of heterogeneous multi-modal telemetry into the canonical 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) with active observation mask.
* **Demonstrator Actions**:
  1. Open the PRIE Web Studio (`http://localhost:8000`).
  2. Select Candidate Persona: **Candidate A (Alex Chen - 3rd Year Computer Science)**.
  3. Load SIS records: CGPA = 7.4/10.0 ($F_{01} = 0.74$), Department = Computer Science ($F_{17} = 0.85$), Backlogs = 0 ($F_{02} = 0.0$).
  4. Upload candidate two-column resume (`alex_chen_resume.pdf`).
  5. Trigger spatial 2D ATS parsing via PyMuPDF. Show how column bounding boxes separate sidebar skills (Python, Java, Docker) from project narrative text, yielding parseability score $F_{20} = 0.84$ and job semantic cosine similarity $F_{19} = 0.76$ against SDE-1 description.
  6. Display the assembled 22-dimensional tensor in the live UI inspector.

---

## Stage 2: Predictive Inference & Platt Calibration (Minutes 02:00 – 04:00)
* **Objective**: Show how PRIE computes calibrated posterior placement probabilities rather than overconfident uncalibrated scores.
* **Demonstrator Actions**:
  1. Click **"Run Readiness Inference"**.
  2. Predictor ($M_{06}$) executes cost-sensitive XGBoost.
  3. Raw uncalibrated margin score: $f(\mathbf{x}) = -0.42$ (Uncalibrated $P = 0.397$).
  4. Platt scaling transform: $P(Y=1 \mid \mathbf{x}) = \frac{1}{1 + \exp(A \cdot f(\mathbf{x}) + B)} = 0.412$.
  5. The UI displays the diagnostic classification: **"At-Risk of Unsuccessful Placement ($P_{\text{calibrated}} = 41.2\%$)"**.
  6. Highlight the confidence interval and Brier calibration reliability indicator ($ECE \le 0.035$).

---

## Stage 3: Explainability via TreeSHAP Waterfall (Minutes 04:00 – 05:30)
* **Objective**: Transition from opaque prediction to transparent axiomatic attribution.
* **Demonstrator Actions**:
  1. Click **"Inspect Diagnostic Attribution"**.
  2. TreeSHAP module ($M_{07}$) renders an interactive waterfall plot:
     - Base Value ($\mathbb{E}[f(x)]$): $+0.58$ log-odds.
     - Negative attribution driver 1: `dsa_score` ($F_{03} = 0.45$) $\rightarrow -0.68$ log-odds impact.
     - Negative attribution driver 2: `mock_interview_score` ($F_{07} = 0.52$) $\rightarrow -0.34$ log-odds impact.
     - Negative attribution driver 3: `consistency_score` ($F_{13} = 0.38$) $\rightarrow -0.22$ log-odds impact.
     - Neutral/Protected attribute: `branch_encoded` ($F_{17}$) $\rightarrow 0.00$ log-odds impact.
  3. Emphasize to the audience: *``The system does not penalize the student for their demographic branch, but pinpoints specific mutable technical and behavioral skill gaps.''''*

---

## Stage 4: Prescriptive Recourse via Constrained DiCE (Minutes 05:30 – 07:00)
* **Objective**: Show how PRIE generates bounded, feasible counterfactual recommendations ($k \le 3$).
* **Demonstrator Actions**:
  1. Click **"Generate Actionable Recourse"**.
  2. DiCE solves the distance-constrained optimization problem with $F_{17}$ locked.
  3. System renders an interactive **Actionable Recourse Card**:
     - *``To flip predicted readiness from 41.2% to 76.5% (+35.3%), achieve the following 3 bounded milestones:''*
       1. $\Delta F_{03}$ (`dsa_score`): $45\% \rightarrow 70\%$ ($+25\%$)
       2. $\Delta F_{07}$ (`mock_interview_score`): $5.2 \rightarrow 7.0$ ($+1.8$)
       3. $\Delta F_{13}$ (`consistency_score`): $0.38 \rightarrow 0.65$ ($+0.27$)
  4. Note that $F_{01}$ (CGPA) and $F_{17}$ (Branch) remain untouched, respecting cognitive feasibility.

---

## Stage 5: Closed-Loop Topological Roadmap & Voice Interview (Minutes 07:00 – 09:30)
* **Objective**: Demonstrate closed-loop remediation via DAG scheduling and multimodal interview coaching.
* **Demonstrator Actions**:
  1. Click **"Synthesize Personalized Roadmap"**.
  2. Kahn's topological scheduler executes over `cs_concept_dag.json`.
  3. UI displays a 4-Week prerequisite-valid progression:
     - *Week 1*: Binary Search Trees & Hash Maps (Prerequisites satisfied).
     - *Week 2*: Heaps & Priority Queues.
     - *Week 3*: Graph Traversals (BFS/DFS).
     - *Week 4*: Dynamic Programming & Memoization.
     - Precedence violations: **0 violations (100% valid)**.
  4. Launch **Multimodal Voice Mock Interview**:
     - Candidate completes a 60-second technical question (*``Explain how you detect cycles in a directed graph''*).
     - Faster-Whisper transcribes speech; Librosa extracts pitch $F_0$; OpenCV evaluates gaze stability.
     - Weighted late fusion ($0.40 \cdot \text{Audio} + 0.35 \cdot \text{Video} + 0.25 \cdot \text{Speech}$) delivers composite feedback in $1.18$ seconds, updating $F_{07}$ in real time.
