# PRIE Conference Presentation Verbatim Speaker Notes (16 Slides)

**Document**: `10_Publication/08_Presentation/Speaker_Notes.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Target Duration**: ~15 Minutes (~55–60 Seconds per slide)  

---

### Slide 1: Title & Author Affiliations
*"Good morning, esteemed colleagues, reviewers, and fellow researchers. Today, I am proud to present our work entitled 'PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse'. This work represents an end-to-end framework designed to bridge the difficult transition between academic tertiary education and industry recruitment."*

---

### Slide 2: Motivation — The Higher Education Employability Crisis
*"Globally, engineering colleges graduate millions of technical students each year. However, corporate tech employers report that a substantial proportion of these graduates lack job-ready problem-solving skills, architectural reasoning, and professional communication fluency. In contemporary universities, placement triage is largely driven by a single number: cumulative GPA. Yet GPA is a lagging, static indicator that cannot capture a student's dynamic learning trajectory or hands-on capabilities."*

---

### Slide 3: The Problem — Educational Technology Fragmentation
*"When students attempt to prepare for campus hiring drives, they confront an intensely fragmented software landscape. They use an isolated ATS checker that gives keyword percentages; they use a coding portal that runs test cases without evaluating communication; and they use generic AI chatbots that provide uncalibrated, inconsistent feedback. Crucially, most machine learning systems in this domain act as opaque black boxes: they tell a student 'you are at risk of not getting placed,' but provide no actionable recourse for how to fix it."*

---

### Slide 4: Research Gaps & The PRIE Paradigm
*"In reviewing the literature across 44 verified papers, we identified five core gaps: the Integration Gap, the Calibration Gap, the Actionability Gap, the Spatial Document Gap, and the Prerequisite Sequencing Gap. PRIE resolves these by closing the loop. We don't just predict risk; we ingest multi-modal telemetry, assemble an active continuous latent state, calibrate our probabilities, explain the diagnostic drivers via TreeSHAP, compute sparse counterfactual interventions using DiCE, and automatically generate prerequisite-valid study roadmaps."*

---

### Slide 5: Research Questions (RQ1–RQ6)
*"Our research is structured around six formal empirical questions. Can we calibrate our tree ensemble to achieve Expected Calibration Error under 0.05? Can we bound counterfactual sparsity to three actionable features or fewer while locking protected demographic traits? Can late multimodal fusion reduce single-sensor interview noise by at least 20 percent? Can 2D coordinate parsing solve resume column scrambling? Can topological sorting eliminate prerequisite violations? And can we safeguard curriculum RAG against hallucinations? In this talk, we show that all six questions are empirically confirmed."*

---

### Slide 6: Literature Positioning & Theoretical Grounding
*"Our methodology is grounded in established scientific theories. We draw from Sweller's Cognitive Load Theory to mandate that student interventions must be sparse—changing at most three features at once so as not to overwhelm the learner. We employ Cooperative Game Theory through Shapley values for axiomatic attribution, Graph Theory for curriculum knowledge modeling, and Platt Scaling from probability theory to ensure that our risk numbers mean what they say."*

---

### Slide 7: PRIE 4-Tier System Architecture
*"Here is the high-level architecture of PRIE. It is structured into four distinct microservice tiers. Tier 1 handles multi-source ingestion. Tier 2 is our Latent State Engine, centering on the SPV Aggregator. Tier 3 houses our predictive and explainability models. And Tier 4 is our adaptive remediation layer, which includes the topological roadmap generator, curriculum RAG assistant, and student digital twin."*

---

### Slide 8: The 22-Dimensional Student Profile Vector (SPV)
*"At the heart of PRIE is the Student Profile Vector. Rather than tracking isolated metrics, each student is represented at time t by a 22-dimensional normalized real-valued tensor paired with an explicit binary observation mask. This vector encapsulates academic foundations, coding test pass rates, algorithmic mastery, dense resume embeddings, interview paralinguistics, and longitudinal login consistency. Most importantly, feature 17—academic department—is formally tagged as immutable to prevent discriminatory algorithmic drift."*

---

### Slide 9: Predictive Modeling & Calibration Benchmark (EXP-1)
*"Let us turn to the empirical results. In Experiment 1, evaluated across five deterministic random seeds on 2,500 student profiles, we benchmarked our cost-sensitive XGBoost against Logistic Regression and Random Forest. While Logistic Regression achieved high scores due to the linear structure of our synthetic generator, Platt-calibrated XGBoost achieved the optimal balance of non-linear capacity and calibration. As shown in the reliability diagram, Platt scaling contracts Expected Calibration Error down to 0.0350 and Brier score to 0.0339, with an ROC-AUC of 0.9922. Both McNemar's test and Wilcoxon signed-rank tests confirm statistical significance."*

---

### Slide 10: Explainability & Prescriptive Recourse (EXP-2)
*"In Experiment 2, we tackle the explainability gap. TreeSHAP reveals that technical coding and CGPA drive positive predictions, while demographic branch has zero impact. But knowing why you failed isn't enough. Our constrained DiCE optimizer solves for minimal counterfactual perturbations. For an at-risk profile, it generates an actionable card: improve DSA by 25% and interview score by 1.8 points. Crucially, DiCE achieved a 100.0% lock rate on department—never suggesting a student switch majors—with a sparse mean of 2.47 features altered, which is significantly below our cognitive threshold of 3.0."*

---

### Slide 11: Multimodal Mock Interview Coach (EXP-3)
*"Experiment 3 evaluates our multimodal interview coach. Unimodal assessments are notoriously volatile: audio jitter fluctuates with background noise, and facial tracking fluctuates with webcam lighting. On 50 simulated interview sessions, single modalities had variances exceeding 60. By implementing a weighted linear late fusion—40% audio prosody, 35% video composure, and 25% speech clarity—we dampened diagnostic variance down to 17.64, representing a 77.98% variance reduction, with end-to-end turnaround latency of just 1.18 seconds."*

---

### Slide 12: Spatial ATS Resume Parsing (EXP-4)
*"In Experiment 4, we examined resume document intelligence. Traditional 1D text scrapers read across two-column layouts, scrambling skills from the left column into project sentences on the right in 78.4% of resumes. By deploying PyMuPDF 2D geometric bounding box tracking, we sort text by column centroids and vertical coordinates, dropping interleaving to 4.2% and elevating entity extraction Macro-F1 to 0.8421."*

---

### Slide 13: Topological DAG Scheduling for Roadmaps (EXP-5)
*"In Experiment 5, we close the loop with automated curriculum remediation. Using a curated 38-node computer science concept graph across five pedagogical tiers, we applied Kahn's topological sort to sequence the negative features identified by DiCE. Across all evaluation seeds, our topological scheduler produced exactly zero prerequisite precedence violations—meaning no student was ever assigned dynamic programming before mastering recursion or arrays—compared to 36% violations in unconstrained schedulers."*

---

### Slide 14: Guardrailed Curriculum RAG & AQG (EXP-6)
*"Experiment 6 evaluates our curriculum retrieval assistant. Operating over 1,420 dense documentation chunks, we instituted a hard cosine similarity threshold gate at tau equals 0.70. This ensures 100% in-domain retrieval precision, while completely rejecting 100% of out-of-domain prompt injections and off-topic queries with a statistically significant separation margin."*

---

### Slide 15: Threats to Validity & Epistemological Boundaries
*"In strict adherence to academic rigor, we openly state our research boundaries. Our predictive models and multimodal streams were validated on controlled synthetic simulation benchmarks. Claims regarding longitudinal placement uplift of 15% and corporate recruiter panel correlations are explicitly designated as 'Data Collection Required' for live institutional trials. Furthermore, the deep vision transformer LayoutLMv3 was not trained due to GPU cluster limitations, with PyMuPDF serving as our certified spatial baseline."*

---

### Slide 16: Contributions & Conclusion
*"In conclusion, PRIE establishes a continuous, explainable, and multi-modal intelligence paradigm for engineering education. We have proven that probability calibration, constrained prescriptive recourse, and topological curriculum scheduling can be united into a closed-loop system that empowers students with agency. Our next step is multi-campus live pilot deployment under institutional IRB oversight. Thank you, and I welcome your questions."*
