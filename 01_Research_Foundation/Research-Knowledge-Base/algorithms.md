# Algorithmic Foundations of the Reviewed Literature (Phase 01 Corpus)

This document provides a comprehensive, evidence-grounded taxonomy of all algorithms, machine learning models, deep neural architectures, natural language processing pipelines, and explainability frameworks identified across the **44 verified research papers** in the Phase 01 corpus.

> [!NOTE]
> In strict accordance with Phase 01 evidence protocols, all algorithmic descriptions, hyperparameters, and architectural frameworks documented herein are derived exclusively from the primary source PDF notes. No models or parameters have been inferred or synthesized from model memory.

---

## 1. Algorithmic Taxonomy Overview

Across the 44 reviewed papers, computational approaches cluster into nine distinct operational paradigms:

`mermaid
graph TD
    A[Phase 01 Algorithmic Landscape] --> B[Supervised Classifiers & Regressors]
    A --> C[Deep Learning & Sequential Models]
    A --> D[Large Language Models & GenAI]
    A --> E[NLP, Text Mining & Embeddings]
    A --> F[Retrieval-Augmented Generation RAG]
    A --> G[Multimodal Vision & Audio Processing]
    A --> H[Knowledge Graphs & Network Analytics]
    A --> I[Explainable AI XAI Frameworks]
    A --> J[Reinforcement Learning & Swarm Optimization]
`

---

## 2. Detailed Algorithm Inventory Across Reviewed Corpus

### 2.1. Supervised Machine Learning Classifiers & Ensembles

| Algorithm / Model | Papers Utilizing Model | Primary Function in Literature | Key Hyperparameters & Performance Reported |
|:---|:---|:---|:---|
| **Random Forest (RF)** | Paper 01, Paper 04, Paper 09, Paper 10, Paper 18, Paper 19, Paper 22, Paper 24, Paper 33, Paper 34, Paper 41, Paper 44 | Employability prediction, academic performance forecasting, baseline benchmarking | N_estimators=100-500, max_depth=10-20; Achieved 94.75% accuracy in Paper 22, 91.2% in Paper 01 |
| **XGBoost (Extreme Gradient Boosting)** | Paper 01, Paper 10, Paper 18, Paper 19, Paper 24, Paper 34, Paper 41, Paper 44 | Multi-stakeholder employability prediction, at-risk early warning | Learning_rate=0.01-0.1, max_depth=3-6; Achieved **94.5%** 3-class accuracy in Paper 41 (Babureddy 2026), 92.4% in Paper 10 |
| **Support Vector Machines (SVM / SVC)** | Paper 01, Paper 06, Paper 09, Paper 10, Paper 14, Paper 15, Paper 18, Paper 24, Paper 33, Paper 34 | Linear & non-linear classification, facial emotion recognition, text classification | Radial Basis Function (RBF) kernel, C=1.0-10.0, gamma=scale; 88.6% accuracy in Paper 09 |
| **LightGBM & CatBoost** | Paper 10, Paper 18, Paper 19, Paper 34 | High-dimensional student grade prediction | Gradient-based one-side sampling (GOSS), categorical feature handling; 92.8% in Paper 19 |
| **Logistic Regression (LR)** | Paper 06, Paper 09, Paper 10, Paper 18, Paper 24, Paper 33, Paper 44 | Baseline linear risk classification | L2 regularization (Ridge), C=1.0; 72.0% accuracy / 0.78 AUC in Paper 44 |
| **Decision Trees (CART / C4.5 / J48)** | Paper 06, Paper 08, Paper 09, Paper 10, Paper 24, Paper 31 | Rule extraction, baseline tree induction | Gini impurity / Information Gain entropy splits; 81.3% in Paper 09 |
| **K-Nearest Neighbors (KNN)** | Paper 06, Paper 09, Paper 10, Paper 18, Paper 24 | Instance-based collaborative filtering & placement classification | k=3 to k=11, Euclidean distance; 83.2% in Paper 09 |
| **Naive Bayes (Gaussian / Multinomial)** | Paper 06, Paper 09, Paper 10, Paper 24, Paper 36 | Probabilistic text classification & performance baseline | Laplace smoothing (alpha=1.0); 79.4% in Paper 09 |

---

### 2.2. Deep Learning & Sequential Neural Architectures

| Architecture | Papers Utilizing Architecture | Operational Role & Mechanism | Key Findings & Evidence Location |
|:---|:---|:---|:---|
| **Temporal Fusion Transformer (TFT)** | Paper 44 (Azeez 2026) | Multi-horizon sequential behavior forecasting from longitudinal LMS clickstreams | Integrates Variable Selection Networks (VSN), LSTM encoder-decoder, and multi-head self-attention; Achieved **0.96 AUC** and **89.5% accuracy** at Week 6 (Paper 44, PDF p. 7) |
| **Long Short-Term Memory (LSTM / BiLSTM)** | Paper 01, Paper 15, Paper 18, Paper 25, Paper 33, Paper 39, Paper 44 | Sequential student clickstream modeling, audio prosody time-series, text encoding | Outperformed static ML on temporal sequences (0.90 AUC in Paper 44; 87.4% accuracy in Paper 01) |
| **Convolutional Neural Networks (CNNs / ResNet / VGG)** | Paper 01, Paper 14, Paper 15, Paper 28 | Computer vision for facial expression recognition, emotion detection in mock interviews | ResNet-50 and custom 2D-CNNs extracting 7 basic facial emotion classes (Happy, Neutral, Confused, etc.) (Paper 15, PDF p. 4) |
| **Multi-Layer Perceptron (MLP / ANN)** | Paper 01, Paper 09, Paper 10, Paper 18, Paper 24, Paper 33 | Non-linear dense feature combination | 2-4 hidden layers with ReLU activations and Dropout (0.2-0.5); 89.1% in Paper 01 |

---

### 2.3. Large Language Models (LLMs) & Generative AI

| Model / Gateway | Papers Utilizing Model | Prompting & Orchestration Strategy | Task Executed |
|:---|:---|:---|:---|
| **GPT-4 / GPT-4o** | Paper 03, Paper 20, Paper 21, Paper 23, Paper 27, Paper 40 | Few-shot prompting, system-role steering, conversational agent orchestration | Dynamic follow-up interview question generation (Paper 27), multi-source RAG synthesis (Paper 40) |
| **GPT-3.5-Turbo** | Paper 03, Paper 14, Paper 20, Paper 21, Paper 23 | Cost-efficient zero-shot and few-shot API prompting | Placement Q&A simulation, resume-to-JD gap analysis |
| **OpenRouter LLM API Gateway** | Paper 38 (Kulkarni 2026) | Modular API routing across multiple foundation models | Dynamic question generation and rubric scoring (Paper 38, PDF p. 1) |
| **LLaMA-2 / LLaMA-3 (Open Weights)** | Paper 20, Paper 26, Paper 40 | Parameter-efficient fine-tuning (PEFT/LoRA) and on-premises deployment | Institutional RAG chatbots, MCQ distractor generation (Paper 26) |
| **BART & T5 (Seq2Seq Transformers)** | Paper 25, Paper 26, Paper 39 | Fine-tuned conditional sequence generation | Question generation from passage contexts and causal reasoning graphs (Paper 25, 26) |

---

### 2.4. Natural Language Processing & Vector Embedding Models

| Technique / Library | Papers Utilizing Technique | Function in System Pipeline |
|:---|:---|:---|
| **Sentence-BERT (SBERT / all-MiniLM-L6-v2)** | Paper 12, Paper 17, Paper 28, Paper 35, Paper 40, Paper 43 | Generating dense 384d/768d semantic embeddings for resume matching, job description alignment, and library catalog search |
| **KeyBERT** | Paper 43 (Rajeevan 2026) | Unsupervised keyword and technical concept extraction from unstructured text |
| **TF-IDF & Cosine Similarity** | Paper 11, Paper 12, Paper 17, Paper 36, Paper 37, Paper 43 | Lexical baseline matching between candidate resumes and vacancy descriptions |
| **spaCy & NLTK (NER / POS)** | Paper 11, Paper 12, Paper 17, Paper 28, Paper 36, Paper 37, Paper 42 | Tokenization, lemmatization, Part-of-Speech tagging, and Named Entity Recognition (extracting candidate skills, colleges, degrees) |
| **Wav2Vec 2.0 & Whisper ASR** | Paper 15, Paper 28, Paper 29, Paper 30 | Automatic speech-to-text transcription and vocal acoustic feature extraction in mock interviews |
| **MediaPipe Face Mesh & Pose** | Paper 15, Paper 28, Paper 29 | Real-time tracking of eye contact, head movement, facial landmarks, and posture |

---

### 2.5. Explainable AI (XAI) Methods

| XAI Algorithm | Papers Utilizing XAI | Interpretability Modality & Insights Provided |
|:---|:---|:---|
| **TreeSHAP** | Paper 01, Paper 18, Paper 19, Paper 22, Paper 32, Paper 34, Paper 41, Paper 44 | Exact game-theoretic Shapley values providing global feature attribution ranking and local decision force plots; identified Hiring Readiness (0.40) and CGPA (0.31) in Paper 41 |
| **KernelSHAP** | Paper 01, Paper 18, Paper 19, Paper 44 | Model-agnostic feature attribution for neural and black-box ensembles |
| **LIME (Local Interpretable Model-agnostic Explanations)** | Paper 01, Paper 18, Paper 19, Paper 32, Paper 34 | Sparse linear surrogate approximations explaining individual student predictions |
| **Permutation Feature Importance (PFI)** | Paper 10, Paper 18, Paper 31 | Quantifying degradation in validation score upon random feature shuffling |
| **Attention Weight Visualization** | Paper 25, Paper 44 | Inspecting temporal attention heatmaps across semester weeks |

---

### 2.6. Knowledge Graphs & Graph Analytics

| Method / Library | Papers Utilizing Method | Graph Structure & Analytical Insights |
|:---|:---|:---|
| **Heterogeneous Knowledge Graphs** | Paper 41 (Babureddy 2026), Paper 43 (Rajeevan 2026) | Modeling multi-relational entities (Students, Faculty Mentors, Industry Roles, Skills, Academic Metrics) across 1,150 nodes and 2,908 edges |
| **Greedy Modularity Community Detection** | Paper 41 (Babureddy 2026) | Clustering multi-stakeholder graph into **12 distinct cohesive communities** with modularity score **Q = 0.4442** |
| **Network Centrality (Degree, Betweenness)** | Paper 41, Paper 43 | Identifying key hub concepts, prerequisite skills, and academic bridging courses |

---

### 2.7. Reinforcement Learning & Optimization

| Algorithm | Papers Utilizing Algorithm | Application in Reviewed Literature |
|:---|:---|:---|
| **Proximal Policy Optimization (PPO)** | Paper 44 (Azeez 2026) | Policy gradient RL agent recommending personalized weekly interventions to at-risk students, reducing course failures by 41.2% in an RCT |
| **Particle Swarm Optimization (PSO)** | Paper 31 (Jia 2022) | Swarm intelligence metaheuristic for high-dimensional feature selection in educational data mining |

---

## 3. Systematic Summary on Algorithmic Coverage for PRIE

1. **Predominance of Tree Ensembles for Tabular Placement Modeling**: XGBoost and Random Forest consistently achieve the highest accuracy and stability across educational tabular datasets (94.5% to 94.75%).
2. **Emergence of Temporal Attention for Behavioral Sequences**: While standard LSTMs improve over static models, Temporal Fusion Transformers (TFT) with multi-head self-attention represent the state-of-the-art for longitudinal telemetry.
3. **The Necessity of Hybrid Explainability**: TreeSHAP serves as the gold standard for global institutional dashboards, while LIME and individual force plots provide student-facing actionability.
4. **Graph and RAG Synergy**: Combining dense vector embeddings (SBERT) with structured Knowledge Graphs provides the highest precision and lowest hallucination rate in academic and career discovery.
