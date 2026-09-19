# Paper 25 — Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning

## 1. Bibliographic Information

- **Paper ID**: Paper25
- **Full Title**: Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning
- **Authors**: Nichoas X. Wang (Stellar Learning Technologies, San Jose, USA), Neel V. Parpia (Stellar Learning Technologies), Aaryan D. Parikh (Stellar Learning Technologies), and Aggelos K. Katsaggelos (Northwestern University, Evanston, USA)
- **Year**: August 2025
- **Venue**: IEEE International Conference on Multimedia Information Processing and Retrieval (IEEE MIPR 2025)
- **DOI**: IEEE MIPR 2025 conference proceedings (not explicitly printed on the header; published by IEEE)
- **PDF filename**: `Paper25_cognitive2026automatic.pdf` (Note: filename reflects legacy bibtex tag `cognitive2026automatic`; authentic PDF confirms authors Nicholas X. Wang et al., IEEE MIPR 2025)
- **PDF path**: `Papers/PDFs/Paper25_cognitive2026automatic.pdf`
- **Page count**: 5 pages (pp. 1–5)

---

## 2. Research Problem

Automatic question generation (AQG) is vital for personalized and adaptive learning in STEM education. However, its effectiveness is severely constrained by large language model (LLM) hallucinations, where models produce factually incorrect, ambiguous, or pedagogically inconsistent questions that mislead learners, reinforce misconceptions, and undermine instructional trust.

### Source Evidence
- **Page**: PDF p. 1
- **Section**: Section I — Introduction

---

## 3. Research Objectives

The authors explicitly define their objective:
1. To propose a novel framework combining causal-graph-guided Chain-of-Thought (CoT) reasoning with a multi-agent LLM architecture to enable reliable, pedagogically sound automatic question generation.
2. To structure concept dependencies explicitly to minimize hallucinations and scaffold learning from basic recall to complex problem-solving.
3. To deploy and empirically validate the framework in a live educational platform (Stellar) across multiple STEM and humanities courses.

### Source Evidence
- **Page**: PDF p. 1
- **Section**: Abstract & Section I — Introduction

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an architectural design and empirical validation framework rather than numbered formal research questions).

---

## 5. Dataset

The system was evaluated through deployment and benchmarking:
- **Deployment Platform**: Stellar (public online intuitive learning platform launched in November 2024, `https://stellarlearning.app`).
- **Scale / Cohort**: Supported over 5,000 students across more than 40 courses (STEM and humanities); approximately 20% of users engage for over an hour on a near-daily basis.
- **Experimental Test Set**: Curated question evaluation benchmark comparing generated questions against baseline platforms across AP exam and textbook-level domains (Physics/Mechanics, Macroeconomics, Electricity & Magnetism).
- **Subjective Study Cohort**: $N = 25$ human subjects evaluating question quality across STEM and humanities subjects.
- **Data Availability**: Stellar platform is deployed publicly; internal proprietary multi-agent prompt pipelines.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section IV — Experimental Results & Section V — Conclusion

---

## 6. Features

The framework operates on structured concept graphs and reasoning paths:

### Academic / Knowledge Representation
- **Concept Dependency Nodes**: Key domain principles, laws, definitions, and equations (e.g., Newton's Second Law, Force, Acceleration, Velocity, Kinetic Energy).
- **Causal Links / Directed Edges**: Directional dependencies representing logical progression, prerequisite relationships, or cause-and-effect mechanisms.
- **Traversal Subgraphs**: Path length, depth, and branching complexity used to scale question difficulty.

### Reasoning / CoT Features
- **Step-by-Step Explanation Chains**: Intermediate logical derivations linking prerequisite nodes to the target outcome.
- **Dual Validation Signals**: Validity score of causal graph path and semantic/pedagogical correctness score of generated questions.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section II — Causal Graph for Intuitive Learning & Section III — Causal Graph Guided Chain-of-Thought Reasoning

---

## 7. Data Preprocessing

The authors implement graph-based knowledge structuring and traversal transformations:
- **Graph Construction**: Domain knowledge mapped into directed causal dependency graphs (concept nodes and causal edges).
- **Traversal Operationalization**:
  - *Forward traversal*: Propagates consequences from foundational principles (e.g., "What follows from this principle?").
  - *Backward traversal*: Traces prerequisites from outcomes (e.g., "What must be true for this result to occur?").
  - *Branching*: Explores multiple conditional dependencies (e.g., "Which conditions affect this outcome?").
  - *Misconception injection*: Introduces deliberate counterfactual/erroneous links to test error diagnosis.
- **Difficulty Scaling**: Subgraph expansion adjusting the number of interconnected concept nodes.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section II & Section III

---

## 8. Algorithms and Models

The framework employs a coordinated multi-agent Large Language Model (LLM) architecture with dual validation:
1. **Causal Graph Pathfinder Agent**: Converts an input question or topic into a corresponding path within the domain causal graph.
2. **Causal Graph Path Expansion Agent**: Derives new conceptual paths in the causal graph based on existing question paths from training/domain data.
3. **Causal Graph Path Validation Agent**: Evaluates whether a proposed conceptual path is logically and domain-valid prior to generation.
4. **CoT-Based Question Generation Agent**: Generates questions, answer keys, and explanations using the expanded path, domain context, and step-by-step CoT reasoning prompts.
5. **Question Validation Agent**: Assesses generated questions for factual correctness, pedagogical alignment, clarity, and absence of hallucinations.
6. **Question Output Agent**: Formats and delivers the validated question, hints, and progressive scaffolding to the learner.

### Source Evidence
- **Page**: PDF p. 3
- **Section**: Section III, Figure 3

---

## 9. Architecture

The system architecture is explicitly presented in **Figure 3**:
- **Input Layer**: Learner input / course syllabus topic / seed question.
- **Graph Traversal Layer**: Pathfinder Agent $\rightarrow$ Path Expansion Agent $\rightarrow$ Path Validation Agent (loops if invalid).
- **Generation & Validation Layer**: CoT Question Generation Agent $\rightarrow$ Question Validation Agent (loops if invalid).
- **Output Layer**: Question Output Agent delivering scaffolded interactive questions to the user interface.
- **Dual Validation Loop**: The separation of path validation and output question validation prevents hallucinated relationships from propagating into prompts.

### Source Evidence
- **Page**: PDF p. 3
- **Figure**: Figure 3 ("The implementation of causal graph-guided chain-of-thought framework with a coordinated system of LLM agents")

---

## 10. Methodology

1. **Causal Graph Modeling**: Domain experts and curriculum structures establish concept dependency graphs across target subjects.
2. **Target Path Selection**: Given a learning objective or prerequisite deficiency, the system identifies relevant nodes and traverses paths via forward, backward, or branching patterns.
3. **Multi-Agent Generation Pipeline**:
   - The pathfinder and expansion agents formulate a reasoning trajectory.
   - The path validator verifies logical soundness against graph constraints.
   - The CoT generation agent synthesizes the question and stepped solution.
   - The question validator screens for pedagogical consistency and hallucinations.
4. **Comparative Empirical Benchmarking**: Automated evaluation across readability, conceptual depth, and solution complexity against ChatGPT and Knowt.
5. **Human Subject Evaluation**: User trial with 25 participants rating educational utility, clarity, and scaffolding.

### Source Evidence
- **Page**: PDF pp. 2–5
- **Section**: Sections II, III, and IV

---

## 11. Experimental Setup

- **Platform Under Test**: Stellar (`https://stellarlearning.app`).
- **Baseline Systems**:
  - ChatGPT (OpenAI GPT-based conversational generation) [Ref 6].
  - Knowt (commercial online learning and flashcard/quiz generation platform) [Ref 17].
- **Objective Evaluation Metrics**:
  - *Flesch-Kincaid Grade Level*: Readability metric estimating U.S. school grade level.
  - *Key Points*: Count of domain-specific terms and learning objectives covered per question.
  - *Solution Quality*: Count of logical steps required in a complete, scaffolded solution.
- **Composite Scoring**: Weighted objective metric: overall score $= 0.3 \times \text{Flesch-Kincaid} + 0.3 \times \text{Key Points} + 0.4 \times \text{Solution Quality}$.
- **Subjective User Study**: 25 human subjects across STEM and humanities courses.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section IV — Experimental Results

---

## 12. Evaluation Metrics

1. **Flesch-Kincaid Grade Level**: Sentence length and word complexity assessment of question text.
2. **Key Points Coverage**: Domain terminology and curriculum objective density.
3. **Solution Quality / Reasoning Steps**: Count of explicit logical steps required for solution.
4. **Composite Quality Score**: Weighted objective function $(0.3, 0.3, 0.4)$.
5. **Subjective User Rating**: 5-point Likert scale (1 to 5 stars) from $N=25$ users.
6. **User Preference Percentage**: Proportion of users reporting superior utility over baseline tools.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section IV

---

## 13. Results

### Objective Benchmark Results (Figure 4 & Figure 5)
- **Overall Quality Outperformance**: Stellar consistently outperformed both ChatGPT and Knowt across all evaluated metrics.
- **Relative Improvement**: Stellar's overall weighted score exceeded commercial benchmark Knowt by up to **70%** (PDF p. 4, Section IV).
- **Key Points Dominance**: Stellar showed its most pronounced advantage in the *Key Points* category due to causal graph-based comprehensive knowledge connections.
- **Solution Quality**: Superior logical progression and step count driven by causal CoT guidance.

### Subjective User Study Results ($N=25$, Figure 7)
- **5 Stars**: 17 users (68.0%)
- **4 Stars**: 5 users (20.0%)
- **3 Stars**: 2 users (8.0%)
- **2 Stars**: 1 user (4.0%)
- **1 Star**: 0 users (0.0%)
- **Positive Utility**: Over **90%** of participants reported that Stellar's generated questions were "far more useful than those from other products" (PDF p. 5).

### Source Evidence
- **Page**: PDF pp. 4–5
- **Figures / Tables**: Figure 4, Figure 5, Figure 7, Section IV text

---

## 14. Baselines

1. **ChatGPT** (OpenAI conversational LLM question generation baseline).
2. **Knowt** (Commercial educational flashcard and AI quiz generation platform).

### Source Evidence
- **Page**: PDF p. 4
- **Section**: Section IV

---

## 15. Ablation Study

- *Not formally reported as an isolated component-removal table.* The paper contrasts the integrated multi-agent causal CoT system directly against standard unconstrained LLM generation (ChatGPT) and commercial template-based generation (Knowt).

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section IV

---

## 16. Explainability

- **Explicit Causal Explainability**: Unlike black-box question generation, the causal graph provides explicit visual and structural interpretability:
  - Prerequisite and dependency chains are transparent to instructors and learners.
  - Student errors and misconceptions are traced directly back to specific failed nodes or links in the graph.
  - Step-by-step CoT reasoning paths expose the exact logical sequence connecting concepts.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section II (Bullet 4: "Targeted error diagnosis") & Section III

---

## 17. Main Findings

1. Grounding LLM question generation in causal concept dependency graphs substantially reduces hallucinations by constraining generation to verified paths.
2. Causal-graph-guided Chain-of-Thought (CoT) reasoning yields higher conceptual depth (*Key Points*) and richer solution trajectories than unconstrained LLM prompting, beating commercial baselines by up to 70%.
3. Dual validation (path validation followed by output question validation) ensures that pedagogical structure and linguistic clarity are both satisfied.
4. Over 90% of user study participants favored the scaffolded, step-by-step questions over conventional AI flashcards/quizzes.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Sections IV & V

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Occasional Difficulty Mismatch**: A minority of lower user ratings stemmed from occasional mismatches between question difficulty and student readiness.
2. **Redundancy in Wording**: Some generated questions exhibited repetitive phrasing or wording patterns.
3. **Graph Construction Overhead**: Requires initial domain modeling of concept dependencies to build the causal graph.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The objective metrics (Key Points, Solution Quality) rely in part on automated or heuristic scoring whose exact programmatic formulas are partially summarized in the text. The subjective evaluation cohort ($N=25$) is relatively modest, though supported by 5,000 live platform users.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section IV (Subjective Test discussion)

---

## 19. Future Work

Explicitly proposed by the authors:
1. Extending causal graph generation across more diverse higher-education and specialized domains.
2. Refining dynamic difficulty calibration to prevent the occasional difficulty mismatches observed in user feedback.
3. Incorporating more granular student error telemetry directly into real-time causal graph traversal updates.

### Source Evidence
- **Page**: PDF p. 5
- **Section**: Section V — Conclusion

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides direct architectural foundation for PRIE's **Adaptive Question Generation (AQG)** and **Mock Interview Assessment** modules:
1. **Curriculum Prerequisite Modeling**: PRIE's placement readiness engine requires testing candidates across CS fundamentals (e.g., Data Structures $\rightarrow$ Algorithms $\rightarrow$ System Design). Stellar's causal graph path traversal provides an exact blueprint for generating scaffolded coding and conceptual questions.
2. **Hallucination Mitigation in Technical Assessment**: Unconstrained LLM mock interviewers frequently hallucinate technical syntax or pedagogical requirements. PRIE can implement Stellar's dual-agent validation (Causal Graph Path Validator + Question Output Validator) to guarantee factual alignment.
3. **Targeted Diagnostic Remediation**: Tracing candidate mock interview mistakes to specific graph nodes enables PRIE to recommend precise learning interventions rather than generic feedback.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **Primary Objective** | "combines causal-graph-guided Chain-of-Thought (CoT) reasoning with a multi-agent LLM framework for automatic question generation." | PDF p. 1, Section I | Direct statement |
| **Causal Traversal Modes** | Forward traversal, backward traversal, branching, and misconception injection. | PDF p. 2, Section II | Methodology |
| **Multi-Agent Roles** | Six specialized agents: Pathfinder, Expansion, Path Validation, CoT Generation, Question Validation, Output Agent. | PDF p. 3, Section III & Figure 3 | Architecture / Figure |
| **Deployed Platform Scale** | Deployed in Stellar platform; >5,000 students across >40 courses; ~20% daily active >1 hr. | PDF pp. 4–5, Sections IV & V | Experimental context |
| **Objective Outperformance** | Stellar's composite quality score exceeds Knowt by up to 70%, outperforming ChatGPT and Knowt. | PDF p. 4, Section IV & Figure 4 | Experimental result |
| **User Study Ratings** | 17/25 5-star, 5/25 4-star, 2/25 3-star, 1/25 2-star; >90% find questions far more useful. | PDF pp. 4–5, Section IV & Figure 7 | Experimental result |
| **Stated Limitations** | "occasional question difficulty mismatches or redundancy in wording." | PDF p. 5, Section IV | Author limitation |

---

## 22. Verification Checklist

- [x] PDF read (`Paper25_cognitive2026automatic.pdf`, 5 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected
- [x] Dataset verified (Stellar platform, 5,000 users, 25-user subjective study)
- [x] Features verified (Causal concept nodes, dependency edges, CoT paths)
- [x] Algorithms verified (6 multi-agent LLM roles, dual validation loops)
- [x] Architecture inspected (Figure 3 multi-agent pipeline)
- [x] Experiments inspected (Readability, Key Points, Solution Quality vs ChatGPT & Knowt)
- [x] Results verified (+70% over Knowt, 68% 5-star rating, >90% positive utility)
- [x] Limitations verified (Difficulty mismatch, wording redundancy)
- [x] Future work verified (Dynamic difficulty tuning, multi-domain graph expansion)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact multi-agent architecture from Figure 3, objective benchmark gains of +70% from Figure 4, and user study distribution from Figure 7 verified directly from source text).
