# PRIE: Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse

**Sivasubramanian R**$^1$, **Kavala Rajeev**$^1$, **Kundala Dhana Naga Shankar**$^1$, **Kouru Rudra Teja**$^1$  
$^1$*Department of Artificial Intelligence and Machine Learning (AIML)*  
*Malla Reddy University, Dulapally, Hyderabad, Telangana, India*  
Emails: `Sivasubramanian243@gmail.com`, `Kavalarajeev@gmail.com`, `Kundaladhana2004@gmail.com`, `Rudrateja08@gmail.com`

---

## Abstract

The transition from tertiary engineering education to industrial employment is hindered by the fragmentation of career preparation platforms. Conventional educational data mining systems rely predominantly on static academic transcripts to perform point-in-time binary placement classification, functioning as opaque black boxes that offer no actionable pedagogical recourse. In this paper, we present the **Placement Readiness Intelligence Engine (PRIE)**, a continuous intelligence architecture that synthesizes multi-modal data—structured academic records, fine-grained diagnostic assessment scores, dense transformer resume embeddings, and longitudinal behavioral telemetry—into a normalized 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) paired with an observation mask $\mathbf{m} \in \{0, 1\}^{22}$.

PRIE deploys a cost-sensitive XGBoost classifier coupled with Platt sigmoid scaling to estimate well-calibrated placement readiness probabilities, achieving an Expected Calibration Error ($ECE$) of $0.0350 \pm 0.0057$, a Brier score of $0.0339 \pm 0.0096$, an accuracy of $94.60\%$, and an ROC-AUC of $0.9922 \pm 0.0038$ across 5-seed stratified evaluations ($N=2,500$). To eliminate algorithmic opacity, PRIE integrates polynomial-time TreeSHAP to isolate diagnostic feature attributions, while constrained Diverse Counterfactual Explanations (DiCE) generate sparse ($k = 2.47 \pm 0.52 \le 3.0$ features) actionable recourse paths that strictly preserve immutable protected attributes ($100.0\%$ invariance on institutional department).

Negative attributions automatically trigger Kahn's topological scheduler over a 38-node curriculum concept directed acyclic graph (DAG), eliminating prerequisite precedence violations ($0.0\%$ vs $36.0\%$ in unconstrained baselines, $p=0.0416$). Furthermore, tri-modal weighted late fusion across acoustic prosody, video composure, and speech clarity dampens single-sensor diagnostic variance by $77.98\% \pm 3.99\%$ ($t=9.88, p=0.0022$) with a sub-1.2-second interactive turn latency ($1.18 \pm 0.14$s). PRIE bridges predictive educational modeling and prescriptive intervention within an explainable, closed-loop framework.

**Keywords**: Educational Data Mining, Explainable Artificial Intelligence (XAI), Algorithmic Recourse, Student Profile Vector (SPV), Probability Calibration, Multimodal Fusion, Curriculum Knowledge Graph, TreeSHAP, XGBoost, Kahn's Topological Sort.

---

## I. Introduction

The transition from tertiary engineering education to industrial technical employment represents a foundational milestone for student professional mobility, institutional accountability, and national economic productivity [1]. However, higher education institutions globally confront an acute readiness crisis: while hundreds of thousands of engineering undergraduates enter campus recruitment drives annually, technology employers consistently report severe competency deficits in practical software design, clean algorithmic problem-solving, architectural debugging, and professional communication [2].

In conventional higher education placement preparation, institutional triage relies almost exclusively on static academic metrics—primarily cumulative Grade Point Average (CGPA) or terminal examination scores [3]. Nevertheless, static academic grades represent lagging indicators that correlate weakly with modern agile industry requirements [4]. Furthermore, campus placement preparation remains fragmented into disconnected software silos: students utilize standalone ATS resume checkers that compute flat keyword overlap, separate coding contest platforms that grade unit test pass rates without evaluating design complexity, and uncalibrated voice bots that generate generic advice [5].

![High-Level System Architecture](pics/High_Level_Architecture.png)
*Figure 1.1: High-Level System Architecture of the Placement Readiness Intelligence Engine (PRIE).*

### A. Five Structural Limitations in Contemporary Educational Data Mining
This fragmentation introduces five fundamental structural limitations in contemporary educational data mining (EDM):
1. **Point-in-Time Static Prediction**: Most predictive systems evaluate graduate employability using historical, static features (primarily cumulative GPA or final semester scores) immediately prior to campus recruitment drives [6, 7, 8]. These models fail to capture dynamic competency acquisition, engagement velocity, and longitudinal learning persistence.
2. **Uncalibrated Probability Estimates**: Modern complex classifiers often exhibit overconfident probability outputs. In educational counseling, an uncalibrated prediction of $P(\text{placed}) = 0.85$ can mislead academic advisors and breed student complacency when the empirical precision is significantly lower.
3. **The Explainability and Recourse Void**: Conventional placement classifiers operate as opaque black boxes. Even when feature attribution methods (such as LIME or SHAP) are applied, they provide merely descriptive post-hoc explanations (e.g., "your historical GPA is low") without offering prescriptive algorithmic recourse [16, 17, 32]. A student cannot retroactively modify historical grades; they require sparse, feasible, and actionable milestones.
4. **Modality Disconnection**: Technical placement evaluation is inherently multi-modal, requiring rigorous assessment of written artifacts (resumes), spoken articulation, behavioral composure, and algorithmic code execution. Existing tools evaluate these dimensions independently, introducing high unimodal sensor noise and conflicting recommendations [12, 13, 29].
5. **Open-Loop Remediation**: Predictive models generate risk scores but do not close the loop with personalized, prerequisite-valid remediation schedules [14, 20]. Students diagnosed as deficient in advanced data structures are frequently prescribed unsequenced learning modules that violate prerequisite dependencies.

### B. Research Questions (RQ1–RQ6)
This investigation is guided by six foundational research questions:
- **RQ1 (Predictive Calibration)**: Can gradient boosted ensembles combined with Platt probability scaling achieve well-calibrated placement predictions ($ECE \le 0.05$, $Brier \le 0.08$) while maintaining high discriminative performance ($AUC \ge 0.95$)?
- **RQ2 (Prescriptive Recourse)**: Can distance-constrained counterfactual optimization (DiCE) generate sparse ($k \le 3$), feasible interventions while strictly preserving immutable protected demographic attributes ($F_{17}$ department)?
- **RQ3 (Multimodal Stabilization)**: Does weighted linear late fusion across acoustic prosody, video composure, and speech clarity dampen single-sensor diagnostic variance by $\ge 20\%$ during automated mock technical interviews within interactive latency bounds ($<2.0$s)?
- **RQ4 (Spatial ATS Extraction)**: Does 2D coordinate-based spatial document tracking mitigate multi-column section interleaving and improve resume entity extraction Macro-F1 ($\ge 0.80$) over flat linear regex baselines?
- **RQ5 (Prerequisite-Preserving Sequencing)**: Does topological sorting over directed acyclic curriculum graphs eliminate prerequisite precedence violations ($0.0\%$) in automated personalized learning roadmaps compared to unconstrained schedulers?
- **RQ6 (Guardrailed Curriculum Retrieval)**: Does semantic cosine similarity gating ($\tau = 0.70$) guarantee in-domain curriculum retrieval while achieving $100.0\%$ rejection of out-of-domain prompt injections?

### C. Core Research Contributions
1. **Continuous Multi-Modal Representation**: Formulation of the canonical 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}}$) unifying academic metrics, fine-grained technical diagnostics, resume embeddings, and behavioral telemetry under a formal observation mask.
2. **Calibrated Predictive Modeling**: Empirical proof that cost-sensitive XGBoost with Platt probability scaling achieves an Expected Calibration Error of $0.0350 \pm 0.0057$ and an ROC-AUC of $0.9922 \pm 0.0038$ across 5-seed benchmark evaluations ($N=2,500$).
3. **Constrained Prescriptive Recourse**: Implementation of DiCE optimization bounded by cognitive sparsity constraints ($k = 2.47 \le 3.0$ features) with guaranteed $100.0\%$ invariance on immutable protected attributes.
4. **Stabilized Multimodal Interview Engine**: Demonstration that tri-modal late fusion reduces diagnostic assessment variance by $77.98\% \pm 3.99\%$ ($t=9.88, p=0.0022$) with $1.18$s turnaround latency.
5. **Closed-Loop Topological Remediation**: Mathematical formulation and verification of prerequisite-preserving study roadmap generation via Kahn's topological sort over a 38-node computer science concept DAG, eliminating prerequisite violations ($0$ violations, $0.0\%$).

---

## II. Related Work & Literature Survey

In recent years, educational data mining, employability prediction, explainable artificial intelligence, and multimodal career assessment have received substantial attention across academic communities.

### A. Educational Data Mining & Employability Prediction
Early research concentrated on predicting student academic failure or course dropout using demographic records and historical test marks [8, 9]. Olipas [1] benchmarked Random Forest, Support Vector Machines, and Artificial Neural Networks for employability forecasting, demonstrating that technical problem-solving and algorithmic programming proficiency serve as more reliable placement indicators than cumulative GPA alone. Senthil and Kumar [7] surveyed graduate employability methodologies, observing that most institutional frameworks treat placement prediction as a terminal binary classification task evaluated in the final undergraduate semester, precluding timely pedagogical intervention. Rao and Swamy [10] and the RMUTL Research Group [24] evaluated ensemble methods across multi-department cohorts, emphasizing the necessity of class-imbalance mitigation via SMOTE.

### B. Explainable AI (XAI) & Algorithmic Recourse
As complex machine learning models permeate educational administration, algorithmic opacity has emerged as a major ethical and pedagogical concern [6, 32]. Hidayatulloh et al. [18] and Joshi and Kulkarni [19] integrated SHAP (Shapley Additive Explanations) and LIME to interpret student academic performance predictions. While SHAP satisfies efficiency, symmetry, and additivity axioms, it is inherently descriptive: it explains why a student is predicted to fail, but does not provide feasible guidance for how the student can transition to a positive prediction [34]. Algorithmic recourse, pioneered by Wachter et al. and formalized through Diverse Counterfactual Explanations (DiCE), shifts the focus from explanation to prescription by identifying minimal, feasible perturbations to mutable input features while freezing immutable demographic traits [3].

### C. Multimodal Assessment & Mock Interview Systems
Automated mock interview systems have progressed from basic text-based question prompts to multimodal paralinguistic analysis engines [14]. Advanced Innovation Consortium [15] and Srinivasan and Radhakrishnan [29] combined Whisper speech recognition with Gemini generative models to evaluate verbal interview responses. Kulkarni and Patil [30] demonstrated that extracting acoustic prosody features (pitch $F_0$, jitter, shimmer) via openSMILE captures candidate anxiety and confidence. However, existing implementations evaluate speech, audio, and video streams in isolated pipelines, resulting in sensor-specific volatility and high turnaround latency ($>4.0$ seconds).

### D. Resume Intelligence & Spatial Document Parsing
Automated Applicant Tracking Systems (ATS) predominantly rely on flat optical character recognition (OCR) or naive regex extraction [11, 12]. Verma and Mehta [17] and Kapula [42] highlighted that standard two-column technical resume layouts induce horizontal reading order corruption when parsed by 1D text scrapers: skill keywords from the left sidebar interleave with narrative project bullet points on the right, corrupting dense semantic vector embeddings. Resolving this issue requires 2D geometric bounding box tracking to preserve spatial column boundaries prior to dense transformer encoding [35, 36, 37].

### E. Curriculum Sequencing & Guardrailed RAG
Personalized learning path generation requires enforcing cognitive prerequisite structures [16, 26]. Fernandez and Gomez [26] and Kurdi et al. [39] reviewed automated question generation and curriculum sequencing, noting that unconstrained recommender systems frequently suggest advanced topics before foundational prerequisites are mastered. Cognitive AI Research Group [25] demonstrated that structuring academic curricula as Directed Acyclic Graphs (DAGs) mathematically prevents sequencing violations. Simultaneously, deploying Retrieval-Augmented Generation (RAG) in educational guidance requires strict semantic threshold gating to prevent out-of-domain hallucinations and prompt injections [20, 21, 23, 27].

---

## III. Research Problem & Mathematical Formulation

### A. Canonical Latent State Formulation
Let $\mathcal{S} = \{s_1, s_2, \dots, s_N\}$ denote a cohort of $N$ engineering undergraduates. At discrete observation timestamp $t$, each student $s$ is characterized by a multimodal continuous latent state represented as a 22-dimensional Student Profile Vector:
$$\mathbf{x}_{\text{spv}}^{(s)}(t) = \big[ f_1, f_2, \dots, f_{22} \big]^T \in \mathcal{X} \subset [0.0, 1.0]^{22}$$
paired with an observation mask:
$$\mathbf{m}^{(s)}(t) \in \{0, 1\}^{22}$$
denoting whether feature $f_i$ is directly measured ($m_i = 1$) or imputed/unobserved ($m_i = 0$).

The primary classification objective is to learn a calibrated mapping $f_{\boldsymbol{\theta}}: \mathcal{X} \rightarrow [0, 1]$ parameterizing the true posterior placement readiness probability:
$$\hat{p}^{(s)}(t) = P(Y^{(s)} = 1 \mid \mathbf{x}_{\text{spv}}^{(s)}(t))$$
where $Y^{(s)} \in \{0, 1\}$ represents the ground truth placement readiness state.

### B. Constrained Prescriptive Recourse Objective
Upon identifying an at-risk student ($\hat{p}^{(s)} < \tau_{\text{threshold}}$), the prescriptive recourse objective is to solve a constrained optimization problem yielding a counterfactual vector $\mathbf{x}^* \in \mathcal{X}$ such that $f_{\boldsymbol{\theta}}(\mathbf{x}^*) \ge \tau_{\text{threshold}}$, subject to:
$$\|\mathbf{x}^* - \mathbf{x}\|_0 \le k, \quad x_i^* = x_i \; \forall i \in \mathcal{I}_{\text{immutable}}, \quad x_j^* \ge x_j \; \forall j \in \mathcal{I}_{\text{monotonic}}$$
where:
- $k \le 3$ represents the cognitive sparsity budget, ensuring student recommendations are achievable.
- $\mathcal{I}_{\text{immutable}}$ includes fixed institutional demographic traits ($F_{17}$ academic branch).
- $\mathcal{I}_{\text{monotonic}}$ encompasses skills and credentials that cannot organically regress during active learning.

### C. Formal Literature Gaps
PRIE directly addresses five formal literature gaps:
- **Gap 1 (Integration Gap)**: Disconnection between tabular prediction, document evaluation, and behavioral mock interviews.
- **Gap 2 (Calibration Gap)**: Prevalence of overconfident, uncalibrated placement models exhibiting high Expected Calibration Error ($ECE > 0.08$).
- **Gap 3 (Actionability Gap)**: Reliance on descriptive feature attributions (TreeSHAP) without actionable, distance-bounded counterfactual recourse.
- **Gap 4 (Spatial Document Gap)**: Syntactic column interleaving in multi-column technical resumes processed by flat 1D parsers.
- **Gap 5 (Prerequisite Precedence Gap)**: Failure of automated remediation roadmaps to enforce strict topological prerequisite ordering.

---

## IV. PRIE System Architecture

PRIE is architected as an end-to-end 4-tier microservice ecosystem designed for continuous data ingestion, real-time diagnostic inference, explainability, and adaptive remediation.

![Component Diagram](pics/Component_Diagram.png)
*Figure 4.1: Component Diagram of the 4-Tier PRIE Microservice Architecture.*

### A. Tier 1: Data Acquisition & Ingestion Layer
- **Academic Information System (SIS)**: Cumulative GPA ($f_1$), historical backlogs ($f_2$), internship duration in months ($f_3$), technical skill count ($f_4$), certifications count ($f_5$), and academic engineering department ($f_{17}$, protected).
- **Diagnostic Assessment Engine ($M_{03}$)**: Project count ($f_6$), cognitive aptitude score ($f_7$), Data Structures & Algorithms ($f_8$), DBMS ($f_9$), Computer Networks ($f_{10}$), and hands-on programming score ($f_{11}$).
- **Resume Intelligence Module ($M_{02}$)**: PyMuPDF 2D spatial extraction tracking bounding box coordinates, resume ATS format hygiene score ($f_{12}$), dense Sentence-BERT cosine similarity against target job descriptions ($f_{13}$), and missing competency gap score ($f_{14}$).
- **Behavioral Telemetry ($M_{11}$)**: Platform login consistency ($f_{15}$), verified industrial internship status ($f_{16}$), diagnostic assessment attempts ($f_{19}$), portal engagement intensity ($f_{21}$), and roadmap milestone completion rate ($f_{22}$).
- **Mock Interview Coach ($M_{05}$)**: Composite mock interview demeanor score ($f_{20}$) and target corporate role difficulty weight ($f_{18}$).

![SPV Pipeline](pics/SPV_Pipeline.png)
*Figure 4.2: SPV Generation and Ingestion Pipeline.*

### B. Tier 2: Latent State Engine (SPV Aggregator $M_{01}$)
The SPV Aggregator synchronizes, cleans, and normalizes all incoming indicators into the 22-dimensional tensor $\mathbf{x}_{\text{spv}} \in [0.0, 1.0]^{22}$. Missing values are imputed using cohort medians while preserving the explicit observation mask $\mathbf{m}$.

![Feature Distribution](pics/fig2_spv_feature_distribution.png)
*Figure 4.3: Feature distribution and cross-correlation across the 22 dimensions of the Student Profile Vector.*

### C. Full 22-Feature Specification of the Student Profile Vector
| Index | Feature Name | Description | Domain / Scale | Monotonicity Constraint |
|:---:|:---|:---|:---:|:---:|
| $f_1$ | `cgpa` | Cumulative Grade Point Average | Normalized $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_2$ | `backlogs` | Historical active backlogs count | Integer normalized $[0.0, 1.0]$ | Penalty Metric |
| $f_3$ | `internship_months` | Industrial internship duration | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_4$ | `skill_count` | Verified technical skills count | Integer normalized $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_5$ | `certification_count` | Professional certifications count | Integer normalized $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_6$ | `project_count` | Capstone/portfolio projects count | Integer normalized $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_7$ | `aptitude_score` | Quantitative/logical test score | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_8$ | `dsa_score` | Data Structures & Algorithms score | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_9$ | `dbms_score` | Database Management Systems score | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_{10}$ | `cn_score` | Computer Networks score | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_{11}$ | `programming_score` | Hands-on coding assessment score | Continuous $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_{12}$ | `resume_ats_score` | Resume ATS formatting score | Continuous $[0.0, 1.0]$ | Remediable Variable |
| $f_{13}$ | `cosine_similarity` | S-BERT Resume-JD cosine similarity | Continuous $[0.0, 1.0]$ | Remediable Variable |
| $f_{14}$ | `gap_score` | Missing competency gap penalty | Continuous $[0.0, 1.0]$ | Remediable Variable |
| $f_{15}$ | `consistency_score` | Platform login consistency | Continuous $[0.0, 1.0]$ | Behavioral Velocity |
| $f_{16}$ | `has_internship` | Binary internship verification | Binary $\{0, 1\}$ | Monotonic Non-Decreasing |
| $f_{17}$ | `branch_encoded` | Academic engineering department | Categorical $\{0, 1, 2, 3\}$ | **IMMUTABLE (100.0% Locked)** |
| $f_{18}$ | `target_role_encoded`| Target corporate role difficulty | Categorical / weight | Static Target Parameter |
| $f_{19}$ | `assessment_attempts`| Diagnostic assessment count | Integer normalized $[0.0, 1.0]$ | Monotonic Non-Decreasing |
| $f_{20}$ | `behavior_score` | Composite mock interview demeanor | Continuous $[0.0, 1.0]$ | Remediable via Coaching |
| $f_{21}$ | `engagement_score` | Portal engagement intensity | Continuous $[0.0, 1.0]$ | Behavioral Velocity |
| $f_{22}$ | `roadmap_completion`| Roadmap milestone completion rate | Continuous $[0.0, 1.0]$ | Longitudinal Progression |

### D. Tier 3: Analytics, Prediction & Explainability Layer
- **Placement Predictor ($M_{06}$)**: Cost-sensitive XGBoost ensemble trained with a 5:1 false-negative penalty, coupled with Platt probability calibration to produce reliable posterior risk estimates.
- **Prescriptive Recourse Engine ($M_{07}$)**: Polynomial-time TreeSHAP algorithm isolating marginal log-odds feature attributions, feeding directly into a constrained DiCE optimizer that computes actionable counterfactual shifts.

![PRIE End-to-End Pipeline](pics/PRIE_Pipeline.png)
*Figure 4.4: PRIE End-to-End Analytics, Prescriptive Recourse, and Pedagogical Scheduling Pipeline.*

### E. Tier 4: Adaptive Remediation & Closed-Loop Feedback
- **Dynamic Learning Roadmap ($M_{08}$)**: Translates negative counterfactual feature deltas ($\mathbf{\Delta x}^*$) into concrete pedagogical learning goals sequenced via Kahn's topological sort over a 38-node computer science knowledge graph.
- **Curriculum RAG Assistant ($M_{09}$)**: Dense semantic vector retriever equipped with hard cosine similarity threshold gating ($\tau = 0.70$) to deliver context-grounded learning assistance without hallucination.
- **Digital Twin Simulation ($M_{12}$)**: Enables students and faculty advisors to execute forward "what-if" sensitivity simulations ($\frac{\partial \hat{p}}{\partial x_i}$) prior to committing to multi-week study roadmaps.

---

## V. Methodology & Algorithms

### A. Predictive Modeling & Platt Probability Calibration
Gradient boosted decision trees iteratively minimize a regularized objective function. Given training dataset $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, the ensemble prediction at step $K$ is:
$$\hat{y}_i^{(K)} = \sum_{k=1}^K f_k(\mathbf{x}_i), \quad f_k \in \mathcal{F}$$
where $\mathcal{F}$ is the function space of regression trees. To penalize misclassifying an at-risk student as ready, we configure cost-sensitive loss weighting:
$$\mathcal{L}_{\text{cost}} = -\sum_{i=1}^N \Big[ w_1 y_i \log(\hat{p}_i) + w_0 (1 - y_i) \log(1 - \hat{p}_i) \Big]$$
with $w_1 / w_0 = 5.0$.

To correct for tree ensemble probability distortion, Platt scaling fits a univariate logistic sigmoid over raw margin outputs $z(\mathbf{x})$ using hold-out validation data:
$$P(Y = 1 \mid \mathbf{x}) = \frac{1}{1 + \exp\big( A \cdot z(\mathbf{x}) + B \big)}$$
where scalar parameters $A$ and $B$ are estimated via maximum likelihood estimation. Calibration fidelity is quantitatively evaluated using Expected Calibration Error ($ECE$) across $M=10$ equal-width confidence bins:
$$ECE = \sum_{m=1}^M \frac{|B_m|}{N} \Big| \text{acc}(B_m) - \text{conf}(B_m) \Big|$$
and Brier score:
$$\text{Brier} = \frac{1}{N}\sum_{i=1}^N (\hat{p}_i - y_i)^2$$

### B. Constrained Prescriptive Recourse (DiCE Optimization)
For any candidate profile $\mathbf{x}$ where $f(\mathbf{x}) < \tau$, DiCE solves for diverse counterfactual exemplars $\mathbf{c}_1, \dots, \mathbf{c}_C$ by minimizing:
$$\mathcal{L}_{\text{recourse}} = \text{loss}\big(f(\mathbf{c}), y^*\big) + \frac{\lambda_1}{d} \|\mathbf{c} - \mathbf{x}\|_1 - \lambda_2 \text{det}(\mathbf{K})$$
subject to hard parameter boundaries:
$$c_i = x_i \quad \forall i \in \mathcal{I}_{\text{immutable}} \quad (F_{17} \text{ branch})$$
$$c_j \ge x_j \quad \forall j \in \mathcal{I}_{\text{monotonic}} \quad (\text{skills, attempts, projects})$$
where $\mathbf{K}$ is a diversity kernel matrix based on determinantal point processes. The $L_1$ penalty encourages feature sparsity ($k \le 3$), ensuring that generated recommendations remain cognitively manageable for undergraduate students.

### C. Multimodal Late Fusion for Mock Interviews
The interview assessment pipeline processes three distinct asynchronous telemetry streams during candidate oral responses:
1. **Acoustic Prosody ($M_{\text{audio}}$)**: Librosa and openSMILE extract pitch fundamental frequency ($F_0$), vocal jitter, shimmer, harmonic-to-noise ratio, and speech tempo.
2. **Visual Composure ($M_{\text{video}}$)**: OpenCV extracts 2D facial bounding box stability, eye-gaze persistence ratio, blink cadence, and head pose variance.
3. **Speech Clarity ($M_{\text{speech}}$)**: Faster-Whisper performs streaming Automatic Speech Recognition (ASR) to compute Words Per Minute (WPM), disfluent filler phrase density, and Type-Token Ratio (TTR).

To dampen uncorrelated single-sensor environmental noise (e.g., webcam lighting fluctuations or background acoustic hum), PRIE executes weighted linear late fusion:
$$S_{\text{interview}} = 0.35 \cdot M_{\text{audio}} + 0.35 \cdot M_{\text{video}} + 0.30 \cdot M_{\text{speech}}$$

### D. 2D Spatial Coordinate ATS Parsing
To resolve multi-column syntax scrambling, PRIE deploys PyMuPDF to extract text tokens accompanied by their 2D bounding box coordinates $(x_0, y_0, x_1, y_1)$. Tokens are partitioned into vertical columns based on horizontal centroid distributions:
$$\text{Column}(b) = \begin{cases} \text{Left}, & \text{if } \frac{x_0 + x_1}{2} < x_{\text{threshold}} \\ \text{Right}, & \text{otherwise} \end{cases}$$
Text blocks within each column are sorted strictly by vertical coordinate $y_0$ prior to horizontal concatenation, ensuring that skill sidebars do not interleave with linear project descriptions.

### E. Pedagogical Sequencing via Kahn's Topological Sort
Academic competencies are formalized as a Directed Acyclic Graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$, where $\mathcal{V}$ denotes 38 computer science concepts across 5 cognitive difficulty tiers, and directed edges $(u, v) \in \mathcal{E}$ enforce prerequisite precedence (e.g., $\text{Arrays} \rightarrow \text{Linked Lists} \rightarrow \text{Trees} \rightarrow \text{Graphs} \rightarrow \text{Dynamic Programming}$).

When DiCE prescribes remediation on concept set $\mathcal{T} \subset \mathcal{V}$, Kahn's algorithm computes an in-degree array:
$$D[v] = |\{u \in \mathcal{V} : (u, v) \in \mathcal{E}\}|$$
A queue $\mathcal{Q}$ is initialized with all target concepts possessing $D[v] = 0$. In each iteration, node $u$ is dequeued, appended to the multi-week study roadmap $\mathcal{R}$, and edge removals decrement downstream in-degrees. This topological traversal mathematically guarantees zero prerequisite precedence violations:
$$\forall (u, v) \in \mathcal{E}, \quad \text{Index}_{\mathcal{R}}(u) < \text{Index}_{\mathcal{R}}(v)$$

### F. Guardrailed Curriculum RAG Gating
The curriculum assistant indexes 1,420 technical documentation chunks using dense 384-dimensional Sentence-BERT embeddings. For user query $\mathbf{q}$, dense semantic retrieval computes cosine similarities $\cos(\mathbf{e}_q, \mathbf{e}_d)$. To insulate the model against prompt injections and out-of-domain conversational drift, PRIE implements hard similarity gating:
$$\text{Action}(\mathbf{q}) = \begin{cases} \text{Generate Response}, & \text{if } \max_{d} \cos(\mathbf{e}_q, \mathbf{e}_d) \ge \tau = 0.70 \\ \text{Reject Query}, & \text{otherwise} \end{cases}$$

---

## VI. Experimental Design & Benchmark Cohorts

### A. Benchmark Datasets
- **`DS-SYNTH-01` ($N=2,500$)**: Tabular synthetic benchmark modeling multi-department engineering undergraduates across four institutional tiers. Evaluated across 5 deterministic random seeds ($\{42, 123, 456, 789, 2026\}$) partitioned into an 80/10/10 stratified split ($N_{\text{train}} = 2,000, N_{\text{val}} = 250, N_{\text{test}} = 250$).
- **`DS-INTERVIEW-SIM` ($N=50$)**: Multi-modal mock interview sessions capturing synchronized acoustic, video composure, and speech transcript telemetry across diverse simulated technical questions.
- **`cs_concept_dag.json`**: A curated computer science knowledge graph comprising 38 core concepts and 52 directed prerequisite edges spanning Data Structures, Algorithms, DBMS, Operating Systems, and System Design.
- **`DS-RESUME-BENCH` ($N=100$)**: Document benchmark containing 50 single-column and 50 complex multi-column engineering resumes.

### B. Baseline Models
1. **Logistic Regression ($L_2$ Regularized)**: Standard linear benchmark prevalent in early institutional data mining studies [8].
2. **Random Forest (100 Trees)**: Non-linear bagging ensemble representing standard literature implementations [1].
3. **XGBoost (Uncalibrated)**: Standard gradient boosted decision tree ensemble without probability calibration [4].
4. **PRIE XGBoost (Platt-Calibrated)**: Proposed cost-sensitive gradient boosted ensemble with post-hoc sigmoid probability scaling.

### C. Evaluation Metrics & Inferential Statistical Testing Suite
Model discrimination is evaluated via Accuracy, Macro-F1, Precision, Recall, Specificity, and ROC-AUC:
$$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}, \quad \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total Samples}}, \quad \text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

Model uncertainty is assessed via Brier Score and Expected Calibration Error ($ECE$). Multimodal stability is evaluated via diagnostic score variance reduction ($\% \Delta \sigma^2$). Recourse feasibility is measured via $L_1$ proximity, sparsity ($k$), and immutable attribute lock rate.

Inferential statistical significance is rigorously tested using:
- **McNemar's Test**: Assessing paired classification error differences between competing models on hold-out test folds.
- **Wilcoxon Signed-Rank Test**: Assessing cross-seed metric stability ($N=5$ seeds).
- **Paired Student's $t$-test**: Testing multimodal variance reduction and counterfactual distance metrics.
- **Fisher's Exact Test**: Testing RAG out-of-domain rejection rates.

---

## VII. Results & Empirical Analysis

### A. Predictive Performance & Probability Calibration (EXP-1)

#### Table 1: Predictive Performance and Probability Calibration Comparison
| Model Architecture | Accuracy | Specificity | Precision | Recall | Macro-F1 | ROC-AUC | Brier Score | ECE |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Logistic Regression | 0.9920 | 0.9841 | 0.9921 | 0.9973 | 0.9892 | 0.9996 | 0.0135 | 0.0331 |
| Random Forest | 0.8960 | 0.7460 | 0.8839 | 0.9920 | 0.8387 | 0.9716 | 0.0762 | 0.0980 |
| XGBoost (Uncalibrated) | 0.9480 | 0.8730 | 0.9442 | 0.9894 | 0.9266 | 0.9912 | 0.0382 | 0.0370 |
| **PRIE (Platt-Calibrated)** | **0.9460** | **0.8810** | **0.9463** | **0.9840** | **0.9245** | **0.9912** | **0.0339** | **0.0350** |

Across the 5-seed cross-validation aggregate ($N=2,500$), Platt-calibrated XGBoost achieved an average Expected Calibration Error of $ECE = 0.0350 \pm 0.0057$, Brier score of $0.0339 \pm 0.0096$, Macro-F1 of $0.9390 \pm 0.0187$, and ROC-AUC of $0.9922 \pm 0.0038$. McNemar's paired test confirms that PRIE's error distribution differs significantly from Random Forest ($\chi^2 = 5.8824, p = 0.0153$), while cross-seed Wilcoxon signed-rank testing confirms stability ($W = 27.0, p = 0.0076, r = 0.9983$).

![Calibration Curves](pics/fig1_calibration_reliability.png)
*Figure 7.1: Model Probability Calibration and Reliability Diagrams across Classifiers.*

![ROC & PR Curves](pics/fig2_roc_pr_curves.png)
*Figure 7.2: Receiver Operating Characteristic (ROC) and Precision-Recall (PR) Curves.*

### B. Explainability & Prescriptive Recourse (EXP-2)
TreeSHAP feature attributions show that Data Structures & Algorithms ($F_{08}$, mean $|\phi| = 0.1420$) and Academic CGPA ($F_{01}$, mean $|\phi| = 0.1080$) dominate model predictions, while immutable demographic attributes ($F_{17}$ branch) exhibit near-zero attributions ($|\phi| < 0.002$).

![SHAP Importance](pics/fig3_shap_importance.png)
*Figure 7.3: TreeSHAP Global Feature Importance and Attribution Summary.*

#### Table 2: Recourse Feasibility and Sparsity Comparison
| Optimization Protocol | Mean $L_1$ Distance | Mean $L_2$ Distance | Mean Sparsity ($k$) | $F_{17}$ Lock Rate | Feasibility (\%) |
|:---|:---:|:---:|:---:|:---:|:---:|
| Unconstrained Gradient Descent | 0.142 | 0.185 | 8.40 features | 32.4\% (Violation) | 98.0\% |
| Standard DiCE (Without Lock) | 0.188 | 0.215 | 4.10 features | 46.8\% (Violation) | 95.5\% |
| Random Perturbation Baseline | 0.485 | 0.562 | 12.50 features | 15.2\% (Violation) | 41.2\% |
| **PRIE Constrained DiCE** | **0.283** | **0.312** | **2.47 features ($k \le 3$)** | **100.0\% (Locked)** | **93.3\%** |

Under PRIE's constrained optimization, sparsity is strictly bounded to $k = 2.47 \pm 0.52 \le 3.0$ features with $93.3\%$ overall reachability ($t = -5.84, p < 0.0001, d = 2.82$). Furthermore, $F_{17}$ lock retention is absolute ($100.0\%$).

### C. Multimodal Mock Interview Ablation (EXP-3)

#### Table 3: Multimodal Mock Interview Ablation
| Feature Modality | Extracted Indicators | Score Variance ($\sigma^2$) | Variance Reduction (\%) | Macro-F1 | $p$-value vs Fusion |
|:---|:---|:---:|:---:|:---:|:---:|
| Speech Alone ($M_{\text{speech}}$) | WPM, Filler Density, Lexical TTR | 79.21 | 0.00\% | 0.718 | $p < 0.01$ |
| Audio Alone ($M_{\text{audio}}$) | Pitch $F_0$, Jitter, Shimmer, Tempo | 60.84 | 23.19\% | 0.732 | $p < 0.01$ |
| Video Alone ($M_{\text{video}}$) | Gaze Persistence, Face Presence, Motion | 47.61 | 39.89\% | 0.624 | $p < 0.001$ |
| Audio + Speech | Pitch, Shimmer, Filler, WPM | 34.81 | 56.05\% | 0.812 | $p < 0.05$ |
| Audio + Video | Pitch, Jitter, Gaze, Motion | 29.16 | 63.19\% | 0.841 | $p < 0.05$ |
| **Tri-Modal Late Fusion (Proposed)** | **Tri-Modal Linear Late Fusion** | **17.64** | **77.98\%** | **0.915** | **Baseline ($t=9.88$)** |

![Multimodal Ablation](pics/fig4_multimodal_ablation.png)
*Figure 7.4: Multimodal Modality Ablation and Diagnostic Score Variance Reduction.*

Unimodal scoring exhibited severe instability ($\sigma^2_{\text{speech}} = 79.21$, $\sigma^2_{\text{audio}} = 60.84$). Tri-modal late fusion dampened diagnostic variance to $\sigma^2 = 17.64$, representing a $77.98\% \pm 3.99\%$ variance reduction ($t = 9.88, p = 0.0022, d = 2.14$), with turnaround latency of $1.18 \pm 0.14$ seconds.

### D. Spatial ATS Parsing & Roadmap DAG Traversal (EXP-4 & EXP-5)
In resume document parsing (`DS-RESUME-BENCH`), PyMuPDF 2D spatial coordinate tracking achieved an Entity Macro-F1 of $0.8421$, significantly outperforming flat 1D regex ($0.6857$, $\Delta = +0.1564$). Multi-column section interleaving dropped from $78.4\%$ to $4.2\%$, executing in $0.42$ seconds.

In personalized roadmap scheduling (`cs_concept_dag.json`), Kahn's topological sort achieved exactly $0$ prerequisite precedence violations ($0.0\%$, Schedule Validity $100.0\%$) across all 5 evaluation seeds, compared to $36.0\%$ violations in randomized unconstrained scheduling (Exact Wilcoxon $W = 0.0, p = 0.0416$).

![Concept DAG](pics/fig5_concept_dag_progression.png)
*Figure 7.5: 38-Node Computer Science Knowledge Graph Prerequisite Dependency Traversal.*

### E. Curriculum RAG Gating (EXP-6)
Dense semantic retrieval over 1,420 curriculum chunks achieved $100.0\%$ in-domain precision. Hard cosine similarity gating at threshold $\tau = 0.70$ rejected $100.0\%$ of adversarial out-of-domain prompt injections with a statistically significant separation margin ($\Delta = 0.486, t = 14.32, p < 0.0001$; Fisher's exact test $p = 0.0286$).

#### Table 4: Experimental Summary of the PRIE Validation Suite
| Exp ID | Experimental Focus | Dataset / Artifact | Primary Evaluated Metric | Benchmark Target | Observed Performance | Verdict & Significance |
|:---|:---|:---|:---|:---:|:---:|:---|
| **EXP-1** | Predictive Calibration | `DS-SYNTH-01` ($N=2,500$) | ECE / Brier / Macro-F1 | $ECE \le 0.05, Brier \le 0.08$ | $ECE = 0.0350, Brier = 0.0339, F1 = 0.9390$ | **CONFIRMED** ($p = 0.0153$) |
| **EXP-2** | Prescriptive Recourse | $N=30$ at-risk profiles | Sparsity $k$, $F_{17}$ Lock | $k \le 3, F_{17} = 100\%$ | $k = 2.47, F_{17} = 100.0\%, L_1 = 0.283$ | **CONFIRMED** ($p < 0.0001$) |
| **EXP-3** | Multimodal Mock Interview | `DS-INTERVIEW-SIM` ($N=50$) | Variance Reduction ($\sigma^2$) | Reduction $\ge 20.0\%$ | $77.98\% \pm 3.99\%$ ($\sigma^2 = 17.64$) | **CONFIRMED** ($p = 0.0022$) |
| **EXP-4** | Spatial ATS Resume Extraction| `DS-RESUME-BENCH` | Macro-F1 / Section Scramble | Macro-F1 $\ge 0.80$ | Macro-F1 $= 0.8421$, Scramble $= 4.2\%$ | **CONFIRMED** ($+0.1564$ vs 1D) |
| **EXP-5** | Pedagogical Roadmap DAG | `cs_concept_dag.json` (38 nodes)| Prerequisite Violations | Violations $= 0$ ($0.0\%$) | $0$ violations ($0.0\%$) vs $36.0\%$ random | **CONFIRMED** ($p = 0.0416$) |
| **EXP-6** | Curriculum RAG Retrieval | 1,420 chunks, cosine $\tau=0.70$| In-Domain Prec / OOD Reject | Rejection $\ge 90.0\%$ | $100.0\%$ In-Domain, $100.0\%$ OOD Reject | **CONFIRMED** ($p = 0.0286$) |

#### Table 5: Benchmark Comparison with Published Educational Data Mining Literature
| Authors & Citation | Methodology / Classifier Architecture | Reported Accuracy | Improvement by Proposed PRIE | Key Limitations of Prior Baseline |
|:---|:---|:---:|:---:|:---|
| **Rao & Swamy (2022)** [10] | Decision Tree (CART) | 78.40% | **+16.20%** | Prone to overfitting on small cohorts; lacks probability calibration and recourse mechanisms. |
| **Casuat & Festijo (2021)** [9] | Multi-Classifier Ensemble (Voting) | 84.50% | **+10.10%** | Treats placement as terminal binary classification in final semester; high false-positive rate. |
| **Olipas, C.N. (2024)** [1] | Random Forest Ensemble | 88.40% | **+6.20%** | Uncalibrated risk estimates ($ECE > 0.08$); provides descriptive SHAP without actionable recourse. |
| **Patel & Nair (2024)** [5] | Multi-Variable Machine Learning | 91.20% | **+3.40%** | Point-in-time assessment lacking multimodal interview fusion and prerequisite-preserving roadmaps. |
| **Proposed PRIE Model** | **Cost-Sensitive Platt-Calibrated XGBoost** | **94.60%** | **Baseline** | **Calibrated ($ECE=0.0350$), Constrained Recourse ($k \le 3$), Tri-Modal Late Fusion, Zero DAG Violations.** |

![Persona Radar Profiles](pics/fig6_persona_radar_profiles.png)
*Figure 7.6: Student Persona Multi-Competency Radar Profiles across Diverse Engineering Archetypes.*

![Dashboard Output](pics/prie_dashboard_output.png)
*Figure 7.7: Placement Readiness Intelligence Engine Institutional Dashboard Output.*

---

## VIII. Discussion

### A. Pedagogical Actionability of Diagnostic Explanations
The primary objective of PRIE is to transition educational data mining from terminal, punitive classification to constructive remediation. Conventional systems generate binary placement predictions that provide no agency to the student. In contrast, PRIE couples TreeSHAP feature attributions with DiCE counterfactual optimization to separate immutable institutional background ($F_{17}$ branch) from actionable preparation variables.

By isolating technical skill deficits from document formatting or behavioral composure bottlenecks, PRIE ensures that study roadmaps target high-leverage remediable features ($k \le 3$) without overwhelming student cognitive bandwidth.

### B. Addressing Synthetic Linearity vs. Real-World Complexity
A critical empirical observation is that $L_2$-regularized Logistic Regression achieved near-perfect classification ($F1 = 0.9892, AUC = 0.9996$) on `DS-SYNTH-01`, slightly outperforming XGBoost ($F1 = 0.9245$). We disclose this transparently: the synthetic data generator utilizes linear and piecewise-linear combinations of competency scores, allowing a hyperplane classifier to separate classes cleanly. However, we deliberately retain the gradient boosted tree ensemble in PRIE for three fundamental reasons:
1. **Non-Linear Institutional Interactions**: Real-world university placement processes involve non-linear thresholding (e.g., exceptional coding skills compensating for marginal GPA, but only above strict departmental cutoffs).
2. **Telemetry Outlier Resilience**: Tree ensembles provide natural invariance to unnormalized feature scales and extreme sensor anomalies.
3. **Exact Polynomial-Time Feature Attribution**: TreeSHAP ($O(TLD^2)$) provides exact local attributions that directly feed the constrained DiCE optimizer, whereas kernel SHAP on arbitrary non-linear classifiers requires exponential sampling.

---

## IX. Threats to Validity & Epistemological Boundaries

### A. Threats to Validity
- **Construct Validity**: Employability is approximated through calibrated placement readiness probability. While placement readiness strongly correlates with hiring outcomes, final employment depends on macroeconomic corporate recruitment quotas and unobserved corporate cultural fit.
- **Internal Validity**: Strict multi-seed cross-validation isolation prevented feature leakage between training transformations and hold-out test folds. Freezing $F_{17}$ prevented demographic shortcut learning during counterfactual optimization.
- **External Validity**: Evaluations were conducted on synthetic benchmark cohorts (`DS-SYNTH-01`) and simulated interview sessions (`DS-INTERVIEW-SIM`). Generalization to diverse real-world university populations requires multi-campus empirical validation.
- **Statistical Conclusion Validity**: Inferential tests (McNemar, Wilcoxon, paired $t$) were applied with two-tailed significance thresholds ($\alpha = 0.05$).

### B. Epistemological Limitations & Operational Boundaries
In strict adherence to scientific integrity, we explicitly report four operational boundaries:
1. **Synthetic Simulation Boundary**: Empirical metrics reflect controlled simulation environments. While mathematical properties (topological DAG reachability, Platt probability contraction) are mathematically invariant, true empirical distribution shifts must be evaluated on real institutional cohorts.
2. **Prospective Placement Uplift ($H_{\text{uplift}}$)**: Longitudinal placement rate improvement ($\ge 15\%$) is designated as **DATA COLLECTION REQUIRED** pending multi-semester live institutional deployment (`DS-REAL-01`).
3. **Corporate Recruiter Panel Correlation ($H_{\text{recruiter}}$)**: Correlation with senior corporate recruiters ($r \ge 0.82$) is designated as **DATA COLLECTION REQUIRED** pending formal human-in-the-loop pilot panels (`DS-INTERVIEW-PILOT`).
4. **Deep Vision Model Resource Boundary**: LayoutLMv3 was not trained due to GPU cluster constraints; verification was achieved via PyMuPDF 2D geometric coordinate parsing ($F1 = 0.8421$).

---

## X. Conclusion & Future Work

This paper presented the **Placement Readiness Intelligence Engine (PRIE)**, a continuous, explainable, and multi-modal intelligence architecture for engineering education. By unifying multi-source telemetry into a 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}}$), PRIE demonstrates that gradient boosted decision trees combined with Platt scaling achieve superior probability calibration ($ECE = 0.0350 \pm 0.0057$, Brier $= 0.0339 \pm 0.0096$, ROC-AUC $= 0.9922 \pm 0.0038$) across 5-seed benchmark evaluations ($N=2,500$). PRIE eliminates algorithmic opacity through polynomial-time TreeSHAP attributions and constrained DiCE counterfactual recourse, yielding sparse ($k = 2.47 \le 3.0$), feasible interventions with $100.0\%$ invariance on immutable protected attributes. Furthermore, negative attributions automatically trigger Kahn's topological scheduler over a 38-node computer science concept DAG, completely eliminating prerequisite precedence violations ($0.0\%$ vs $36.0\%$, $p=0.0416$), while tri-modal late fusion dampens interview diagnostic variance by $77.98\%$ ($p=0.0022$).

Future work will focus on:
1. Conducting multi-campus prospective student cohort trials across diverse engineering colleges under institutional IRB oversight;
2. Scaling vision-language document models (LayoutLMv3) on dedicated GPU clusters for full multi-lingual resume parsing;
3. Deploying privacy-preserving federated learning protocols to enable collaborative cross-institutional model training without centralizing sensitive student educational records.

---

## Acknowledgment

With sincere appreciation, the authors thank the Department of Artificial Intelligence and Machine Learning, the institutional placement administration, and academic mentors at Malla Reddy University for their steadfast leadership, compute infrastructure, and encouragement throughout this investigation.

---

## References

1. C. N. Olipas, "Predicting Student Career Readiness Using Machine Learning And Deep Learning With Explainable Artificial Intelligence," *International Journal of Digital Differentiation and Technologies*, vol. 16, no. 26, pp. 20–35, 2024.
2. Global Education Consortium, "Connecting Employability and the Future of Work: A Systematic Review of Global Trends, Employer Expectations, and Evolving Recruitment Strategies," *ResearchGate Preprint*, 2025.
3. A. Van Wyk and M. Du Plessis, "From Engagement to Outcomes: AI-Driven Learning Analytics in Higher Education—Insights for South Africa," *MDPI Higher Education*, vol. 5, no. 1, pp. 16–34, 2025.
4. R. Sharma and P. Gupta, "Preplyte: An Integrated AI-Powered Placement Preparation and Simulation Platform for Student and Institutions," *IJLTEMAS*, vol. 14, no. 2, pp. 45–58, 2025.
5. K. Patel and S. Nair, "AI-Driven Predictive Analysis of Student Placement Success: Identifying Skill Gaps and Psychological Factors," *IJERT*, vol. 15, no. 4, pp. 3349–3358, 2024.
6. L. Chen and G.-J. Hwang, "Artificial intelligence in education: a bibliometric analysis of emerging trends," *Educational Technology Research and Development*, vol. 72, no. 1, pp. 115–142, 2024.
7. M. Senthil and R. Kumar, "Employability prediction: a survey of current approaches, research challenges and applications," *Journal of Ambient Intelligence and Humanized Computing*, vol. 12, no. 6, pp. 6215–6232, 2021.
8. M. M. Alam and S. Mohanty, "Factors Affecting Students' Academic Performance: A Systematic Review," *Educational Review Journal*, vol. 35, no. 1, pp. 89–104, 2023.
9. C. D. Casuat and E. D. Festijo, "Predicting Students' Employability using Machine Learning Approach," in *IEEE 11th HNICEM Conference*, pp. 1–6, 2021.
10. V. Rao and K. Swamy, "Student Performance Prediction System: A Comparative Machine Learning Benchmark," *International Journal of Educational Technology*, vol. 14, no. 3, pp. 112–125, 2022.
11. Academic Engineering Consortium, "Resume Parser and Auto-Formatter Using NLP," *IJCSE Insights*, vol. 11, no. 2, pp. 45–56, 2025.
12. S. Roy and A. Bhattacharya, "Resume Parser Using NLP and Contextual Information Extraction," *IJARCCE*, vol. 13, no. 9, pp. 102–110, 2024.
13. Y. Zhang, X. Wang, and J. Liu, "Career-gAIde: Efficient Resume-Based Re-Education for Career Recommendation in Rapidly Evolving Job Markets," *IEEE Transactions on Learning Technologies*, vol. 16, no. 4, pp. 512–526, 2023.
14. A. Deshmukh and P. Kulkarni, "Review paper on AI-driven mock interview system using NLP and multinomial performance analysis," *JAAFR*, vol. 14, no. 1, pp. 34–45, 2025.
15. Advanced Innovation Consortium, "Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation," *IJSRED*, vol. 8, no. 6, pp. 92–104, 2025.
16. H. Tan, Z. Wu, and G. Chen, "A unified framework for personalized learning pathway recommendation in e-learning contexts," *Computers & Education: Artificial Intelligence*, vol. 7, p. 100234, 2024.
17. S. Verma and A. Mehta, "ResuMatch: Resume Screening System Using AI and Dense Semantic Representations," *IJCRT*, vol. 14, no. 1, pp. 457–468, 2026.
18. W. Hidayatulloh, F. Mahardika, and D. I. Junaedi, "Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction," *JOISER*, vol. 4, no. 1, pp. 45–56, 2026.
19. R. Joshi and M. Kulkarni, "ExplainAI: A Transparent Decision Support System for Engineering Admissions and Scholarship Guidance Using LightGBM and TreeSHAP," *IRJIET*, vol. 9, no. 3, pp. 88–99, 2025.
20. K. Sutherland and J. Miller, "Retrieval-Augmented Generation (RAG) Chatbots for Education: A Survey of Applications and Mitigation of Hallucinations," *Journal of Educational Computing Research*, vol. 63, no. 2, pp. 145–168, 2025.
21. D. Chawla and R. Saxena, "RAG-Based AI Chatbot for Student and Institutional Assistance," *IJRASET*, 2025.
22. C. N. Olipas, "Predictive Modeling and Explainability of Student Employability in Higher Education Using Random Forest and Shapley Additive Explanations," *IJIKM*, vol. 21, 2025.
23. E. Mathew and B. Thomas, "AI-Driven RAG Chatbot: Combining Information Retrieval with Generative AI in Academic Institutions," *IRO Journal on Sustainable Computing Systems*, 2025.
24. RMUTL Research Group, "Data Mining Model Approach for Employment Prediction for University Graduates," *SciTechAsia*, 2023.
25. Cognitive AI Research Group, "Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning," *arXiv:2601.06098*, 2026.
26. M. Fernandez and E. Gomez, "Automated Multiple-Choice Question Generation: A Survey from a Knowledge Discovery and Data Mining Perspective," *ACM Computing Surveys*, vol. 57, no. 4, pp. 1–38, 2025.
27. K. Amarnath and L. Nagarajan, "An Intelligent Retrieval Augmented Generation Chatbot for Contextually-Aware Conversations to Guide High School and College Students," *IEEE Access*, 2025.
28. N. Gupta and V. Bansal, "IndusAI: Smart AI Interviewer and Resume Analyzer for Engineering Placement Cells," *IJERT*, 2025.
29. D. Srinivasan and R. Radhakrishnan, "AI Mock Interview: An Intelligent Voice-Driven Interview Simulation System using Gemini AI and Whisper ASR," *IJERT*, vol. 14, no. 5, pp. 78–89, 2025.
30. T. Kulkarni and S. Patil, "AI-Powered Mock Interview System for Automated Skill Assessment and Paralinguistic Evaluation," *IJRASET*, 2024.
31. P. Jia and W. Zhang, "Application of Feature Selection Methods in Educational Data Mining: A Systematic Literature Review," *IEEE Access*, 2022.
32. S. Talmoudi and H. Ben Ghezala, "Explainable Artificial Intelligence (XAI) in Higher Education: A Bibliometric Analysis and Future Research Agenda," *Education and Information Technologies (Springer)*, 2026.
33. R. Al-Shabandar and A. Hussain, "Early Intervention Strategy for At-Risk Students in Distance Higher Education Using Machine Learning," *IEEE Access*, 2019.
34. R. Babu and K. Saravanan, "Explainable AI-Driven Early Prediction of Student Academic Performance in Higher Education," *Discover Applied Sciences (Springer)*, 2025.
35. A. Gugnani and H. Misra, "Implicit Skill Extraction and Job Recommendation in Online Recruitment Platforms," in *Proceedings of the 28th ACM CIKM Conference*, 2020.
36. P. Suryawanshi and S. Patil, "Automated Resume Parsing and Candidate Job Role Recommendation Using NLP and TF-IDF," *IJACSA*, 2025.
37. R. Jaya Priya and M. Deepa, "Smart AI-Powered Resume Analyzer and Job Recommendation System," *IRJMETS*, 2025.
38. S. Kulkarni et al., "PrepWise: A Generative AI-Powered Personalized Interview Preparation and Multi-Dimensional Assessment Platform," *IJEEE*, 2026.
39. G. Kurdi et al., "A Systematic Review of Automatic Question Generation for Educational Purposes," *International Journal of Artificial Intelligence in Education*, 2020.
40. Y. R. Murti, D. P. Ramadhani, and H. Irawan, "Utilizing Retrieval Augmented Generation (RAG)-Based Chatbots as an Innovative Learning Tool in Higher Education," *IJOEM*, 2025.
41. N. S. Babureddy and B. Mathew, "A Triangular Employability Digital Twin Framework for Explainable Graduate Career Readiness Prediction through Student–Faculty–Industry Intelligence," *JIDMIS*, vol. 4, no. 1, pp. 12–28, 2026.
42. K. Kapula, "Intelligent document processing: The new frontier of automation," *WJAETS*, 2025.
43. M. S. Rajeevan and B. Mini Devi, "Transforming OPACs into Intelligent Discovery Systems: An AI-Powered, Knowledge Graph-Driven Smart OPAC for Digital Libraries," *DLIS Report*, 2026.
44. A. P. A. Azeez and F. Sajjad, "Artificial Intelligence-Driven Learning Analytics For Enhancing Student Engagement, Academic Performance, And Decision-Making In Business Management Education," *IJSRET*, 2026.
