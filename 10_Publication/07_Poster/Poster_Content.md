# Academic Conference Poster Verbatim Content

**Document**: `10_Publication/07_Poster/Poster_Content.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

## Panel 1: The Problem — Educational Technology Fragmentation
* **The Transition Disconnect**: Over 1.5 million engineering students graduate annually, yet corporate recruiters report severe deficits in practical coding, articulation, and problem-solving.
* **Flaws of Point-in-Time Classifiers**: Traditional educational data mining relies on static CGPA in final semesters, acting as opaque black boxes providing binary labels without actionable remediation.
* **The PRIE Solution**: Continuous intelligence unifying multi-modal data streams into a normalized 22-D Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) paired with an observation mask $\mathbf{m} \in \{0, 1\}^{22}$.

---

## Panel 2: System Architecture & Latent State Modeling
* **4-Tier Ecosystem**:
  1. *Data Acquisition*: SIS transcripts, diagnostic quizzes, resume PDFs, mock interview audio/video, and portal telemetry.
  2. *Latent State Engine*: Continuous SPV synchronization and normalization.
  3. *Analytics & XAI*: Cost-sensitive XGBoost with Platt probability calibration; polynomial-time TreeSHAP feature attributions.
  4. *Adaptive Remediation*: DiCE constrained recourse, Kahn topological DAG scheduling, and guardrailed curriculum RAG.

---

## Panel 3: Methodology & Algorithmic Formulations
* **Platt Probability Calibration**: Fits logistic sigmoid $P(Y=1 \mid \mathbf{x}) = \frac{1}{1 + \exp(A \cdot f(\mathbf{x}) + B)}$, contracting Expected Calibration Error ($ECE$) to $0.0350 \pm 0.0057$ and Brier score to $0.0339 \le 0.08$.
* **Constrained Prescriptive Recourse (DiCE)**:
  $$\min_{\mathbf{c}} \text{loss}(f(\mathbf{c}), y^*) + \frac{\lambda_1}{d}\|\mathbf{c} - \mathbf{x}\|_1 - \lambda_2 \text{det}(\mathbf{K})$$
  $$\text{s.t.} \quad c_{17} = x_{17} \quad (\text{Strict immutable lock on academic department})$$
* **Multimodal Late Fusion**:
  $$S_{\text{interview}} = 0.40 \cdot \text{Audio} + 0.35 \cdot \text{Video} + 0.25 \cdot \text{Speech}$$
  Dampens diagnostic variance by $77.98\% \pm 3.99\%$ ($p=0.0022$).
* **Topological Prerequisite Sequencing**: Kahn's sort on 38-node CS concept DAG eliminates sequencing errors ($0$ violations, $0.0\%$).

---

## Panel 4: Empirical Results & Validated Evidence
* **Classification Benchmark ($N=2,500$, 5 Seeds)**:
  - Accuracy: $94.6\%$ (Test fold Seed 42) / $95.20 \pm 0.0117$
  - Macro-F1: $0.9390 \pm 0.0187$
  - ROC-AUC: $0.9922 \pm 0.0038$
  - McNemar's Test vs Random Forest: $\chi^2 = 5.8824, p = 0.0153$.
* **Recourse Quality ($N=30$ at-risk profiles)**:
  - Sparsity: $k = 2.47 \pm 0.52 \le 3.0$ features ($t = -5.84, p < 0.0001$).
  - $F_{17}$ Lock Preservation: $100.0\%$ (0 demographic drift).
* **Spatial ATS Extraction**: Macro-F1 $= 0.8421$ ($+0.1564$ over 1D regex); section scramble drops from $78.4\%$ to $4.2\%$.
* **Guardrailed RAG**: $100.0\%$ in-domain precision, $100.0\%$ OOD prompt injection rejection ($\tau = 0.70$).

---

## Panel 5: Discussion, Epistemic Limits & Future Directions
* **Actionable Guidance**: TreeSHAP + DiCE shifts educational AI from punitive assessment to student empowerment.
* **Controlled Benchmark Boundary**: Predictive and multimodal evaluations reflect synthetic benchmarks (`DS-SYNTH-01`, `DS-INTERVIEW-SIM`). Longitudinal placement rate uplift ($\ge 15\%$) and human recruiter correlation ($r \ge 0.82$) are designated as `DATA COLLECTION REQUIRED` for live institutional trials.
* **Future Work**: Multi-campus prospective deployment under IRB oversight, vision-language model scaling (LayoutLMv3), and federated cross-campus model learning.
