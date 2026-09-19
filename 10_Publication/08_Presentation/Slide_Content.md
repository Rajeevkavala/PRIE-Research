# PRIE Conference Presentation Slide Content (16 Slides)

**Document**: `10_Publication/08_Presentation/Slide_Content.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

### Slide 1: Title & Author Affiliations
* **Title**: PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse
* **Authors**: Anonymous Authors
* **Affiliation**: Department of Computer Science and Engineering, Affiliated Engineering Institution
* **Conference**: IEEE / ACM Academic Dissemination Track

---

### Slide 2: Motivation — The Higher Education Employability Crisis
* **The Global Dilemma**: Rapid expansion of engineering graduates vs corporate reports of critical skill deficits.
* **The Traditional Academic Metric**: Over-reliance on cumulative GPA (CGPA) as the sole predictor of job readiness.
* **The Reality**: Placement readiness requires multi-faceted competencies—algorithmic coding, system architecture, verbal communication, and resume alignment.

---

### Slide 3: The Problem — Educational Technology Fragmentation
* **Siloed Solutions**:
  - *Isolated Resume Parsers*: Provide flat keyword scores without evaluating coding fluency.
  - *Coding Portals*: Measure unit test passes without assessing interpersonal interview articulation.
  - *Mock Interview Bots*: Suffer from high single-sensor variance ($>60$) and uncalibrated feedback.
  - *Black-Box ML*: Generates terminal failure predictions without explaining how to improve.
* **The Need**: A continuous, closed-loop intelligence engine uniting diagnosis, explanation, and remediation.

---

### Slide 4: Research Gaps & The PRIE Paradigm
* **The 5 Literature Gaps**:
  1. *Integration Gap*: Disconnected single-task architectures.
  2. *Calibration Gap*: Overconfident probability outputs ($ECE > 0.08$).
  3. *Actionability Gap*: Descriptive SHAP values without prescriptive recourse.
  4. *Spatial Document Gap*: Text interleaving in multi-column resumes.
  5. *Prerequisite Gap*: Automated study roadmaps violating cognitive prerequisites.
* **The PRIE Closed-Loop Loop**: Ingestion $\rightarrow$ Latent State $\rightarrow$ Calibrated Prediction $\rightarrow$ Explainability $\rightarrow$ Prescriptive Recourse $\rightarrow$ Topological Roadmap.

---

### Slide 5: Research Questions (RQ1–RQ6)
* **RQ1 (Calibration)**: Can Platt scaling achieve $ECE \le 0.05$ and $Brier \le 0.08$ on placement prediction?
* **RQ2 (Recourse)**: Can DiCE generate sparse ($k \le 3$) interventions with $100\%$ immutable attribute locking?
* **RQ3 (Multimodal)**: Can tri-modal late fusion reduce interview variance by $\ge 20\%$ within $<2.0$s?
* **RQ4 (Spatial ATS)**: Can 2D coordinate parsing achieve Macro-F1 $\ge 0.80$ on multi-column resumes?
* **RQ5 (Sequencing)**: Can topological DAG sorting eliminate prerequisite precedence violations ($0.0\%$)?
* **RQ6 (Guardrail)**: Can cosine similarity gating ($\tau = 0.70$) eliminate out-of-domain hallucinations?

---

### Slide 6: Literature Positioning & Theoretical Grounding
* **Corpus Foundation**: 44 verified primary research papers spanning 2019–2026.
* **Theoretical Frameworks**:
  - *Cognitive Load Theory*: Justifying sparse, bounded interventions ($k \le 3$).
  - *Cooperative Game Theory*: Shapley Additive Explanations (TreeSHAP).
  - *Graph Theory*: Directed Acyclic Graphs (DAGs) for curriculum knowledge representation.
  - *Probability Theory*: Platt sigmoid scaling for empirical risk calibration.

---

### Slide 7: PRIE 4-Tier System Architecture
* **Tier 1 (Data Acquisition)**: SIS records, diagnostic assessments, resume PDFs, interview telemetry.
* **Tier 2 (Latent State Engine)**: SPV Aggregator normalizing inputs into $\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$.
* **Tier 3 (Analytics & XAI)**: Cost-sensitive XGBoost with Platt scaling; TreeSHAP feature attributions.
* **Tier 4 (Adaptive Remediation)**: Constrained DiCE recourse, Kahn DAG scheduler, guardrailed RAG assistant.

---

### Slide 8: The 22-Dimensional Student Profile Vector (SPV)
* **Mathematical Tensor**: $\mathbf{x}_{\text{spv}} \in [0.0, 1.0]^{22}$ paired with observation mask $\mathbf{m} \in \{0, 1\}^{22}$.
* **Core Indicator Groups**:
  - *Academic Core*: CGPA ($F_{01}$), Backlogs ($F_{02}$), Core CS ($F_{03}$–$F_{05}$).
  - *Practical Engineering*: Hands-on Coding ($F_{06}$), Projects ($F_{10}$), Internships ($F_{11}$).
  - *Document & Behavioral*: Resume ATS ($F_{20}$), SBERT Match ($F_{19}$), Mock Interview ($F_{07}$), Demeanor ($F_{08}$).
  - *Longitudinal Telemetry*: Consistency ($F_{13}$), Attempts ($F_{14}$), Engagement ($F_{15}$).
  - *Protected/Immutable*: Academic Branch ($F_{17}$ - strictly locked).

---

### Slide 9: Predictive Modeling & Calibration Benchmark (EXP-1)
* **Multi-Baseline Comparison ($N=2,500$, 5 Seeds)**:
  - *Logistic Regression*: High synthetic accuracy ($99.2\%$) due to generator linearity.
  - *Random Forest*: Accuracy $89.6\%$, Macro-F1 $0.8387$, $ECE = 0.0980$ (Uncalibrated).
  - *PRIE Calibrated XGBoost*: Accuracy $94.6\%$ (Seed 42) / $95.20 \pm 0.0117$, Macro-F1 $0.9390 \pm 0.0187$, ROC-AUC $0.9922 \pm 0.0038$.
  - *Calibration*: Platt scaling contracts ECE to $0.0350 \pm 0.0057$ and Brier to $0.0339 \pm 0.0096$ (Target: $ECE \le 0.05, Brier \le 0.08$).
  - *Statistical Significance*: McNemar vs RF ($\chi^2 = 5.88, p = 0.0153$); Wilcoxon ($W = 27.0, p = 0.0076$).

---

### Slide 10: Explainability & Prescriptive Recourse (EXP-2)
* **TreeSHAP Attributions**:
  - Coding proficiency ($F_{06}$) and CGPA ($F_{01}$) dominate positive predictions.
  - Protected attribute $F_{17}$ (Branch) exhibits near-zero attribution ($|\phi| < 0.002$).
* **Constrained DiCE Counterfactual Recourse ($N=30$ at-risk profiles)**:
  - Mean Sparsity: $k = 2.47 \pm 0.52 \le 3.0$ features ($t = -5.84, p < 0.0001$).
  - Immutable Feature Lock ($F_{17}$): **100.0% Preserved** (vs $32.4\%$ in unconstrained GD).
  - Reachability: $93.3\%$ feasible counterfactual conversion.

---

### Slide 11: Multimodal Mock Interview Coach (EXP-3)
* **Modality Ablation ($N=50$ simulated sessions)**:
  - Unimodal Speech: $\sigma^2 = 79.21$, Macro-F1 $= 0.718$.
  - Unimodal Acoustic: $\sigma^2 = 60.84$, Macro-F1 $= 0.732$.
  - Unimodal Video: $\sigma^2 = 47.61$, Macro-F1 $= 0.624$.
* **Tri-Modal Late Fusion**:
  - Formula: $0.40 \cdot \text{Audio} + 0.35 \cdot \text{Video} + 0.25 \cdot \text{Speech}$.
  - Variance Dampening: $\sigma^2 = 17.64$ ($\mathbf{77.98\% \pm 3.99\%}$ reduction, $t = 9.88, p = 0.0022$).
  - Interactive Latency: $1.18 \pm 0.14$ seconds end-to-end.

---

### Slide 12: Spatial ATS Resume Parsing (EXP-4)
* **The 1D Problem**: Scrapes left sidebar skills into right column project descriptions, scrambling text order in $78.4\%$ of multi-column resumes.
* **The 2D Solution**: PyMuPDF coordinate-based geometric sorting tracks horizontal column boundaries and sorts blocks by vertical coordinate $y_0$.
* **Empirical Validation**:
  - Entity Extraction Macro-F1: Elevates from $0.6857$ to **$0.8421$** ($\Delta = +0.1564$).
  - Column Interleaving: Drops from $78.4\%$ to **$4.2\%$**.
  - Execution Latency: $0.42$ seconds.

---

### Slide 13: Topological DAG Scheduling for Roadmaps (EXP-5)
* **Pedagogical Knowledge Graph**: 38 concepts, 52 directed prerequisite edges across 5 cognitive difficulty tiers (`cs_concept_dag.json`).
* **Kahn's Topological Sort**: Automatically translates negative DiCE feature shifts into multi-week sequenced milestones.
* **Empirical Validation**:
  - Prerequisite Precedence Violations: **0 violations (0.0%)** across all 5 evaluation seeds.
  - Unconstrained Scheduling Baseline: Produced **$36.0\%$ violations** ($p = 0.0416$).
  - Schedule Validity: **100.0%**.

---

### Slide 14: Guardrailed Curriculum RAG & AQG (EXP-6)
* **Curriculum Vector Bank**: 1,420 technical documentation chunks indexed via Sentence-BERT (384d).
* **Hard Cosine Similarity Gating ($\tau = 0.70$)**:
  - In-Domain Retrieval Precision: **100.0%**.
  - Out-of-Domain Rejection Rate: **100.0%** (blocks prompt injections, adversarial off-topic queries).
  - Separation Margin: $\Delta = 0.486$ ($t = 14.32, p < 0.0001$; Fisher's exact $p = 0.0286$).

---

### Slide 15: Threats to Validity & Epistemological Boundaries
* **Four Validity Dimensions**: Construct, Internal (zero data leakage), External, Statistical Conclusion.
* **Explicit Scientific Disclosures**:
  1. *Synthetic Data Boundary*: Evaluations performed on calibrated simulation benchmarks (`DS-SYNTH-01`, `DS-INTERVIEW-SIM`).
  2. *Prospective Cohort Trials*: Longitudinal placement rate uplift ($\ge 15\%$) and human recruiter correlation ($r \ge 0.82$) are designated as `DATA COLLECTION REQUIRED` for live institutional trials.
  3. *Resource Boundary*: LayoutLMv3 deep model categorized as `MODEL NOT TRAINED` due to GPU cluster limits; PyMuPDF verified as spatial baseline.

---

### Slide 16: Contributions & Conclusion
* **Summary of Contributions**:
  - Formal continuous 22-D Student Profile Vector ($\mathbf{x}_{\text{spv}}$) with observation mask.
  - Platt-calibrated XGBoost achieving $ECE = 0.0350$ and $AUC = 0.9922$.
  - Constrained DiCE recourse ($k = 2.47 \le 3.0$) with $100.0\%$ immutable attribute lock.
  - Tri-modal late fusion reducing interview assessment variance by $77.98\%$ ($p=0.0022$).
  - Kahn DAG scheduling mathematically eliminating prerequisite violations ($0.0\%$).
* **Future Directions**: Multi-campus prospective deployment under IRB oversight, vision-language model scaling, and federated privacy-preserving model training.
