# Future Work Matrix & Cross-Corpus Research Trajectories

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/Future_Work_Matrix.md`  
**Status**: Authoritative Future Work Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. Future Research Trajectories & Thematic Clusters

A comprehensive synthesis of author-proposed future work across the 44 verified primary papers reveals clear methodological convergence. Rather than diverging randomly, author recommendations cluster into seven (7) strategic research trajectories:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           FUTURE WORK THEMATIC CLUSTERS                          │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Thematic Cluster              │ Core Research Focus & Objectives                 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Multimodal Real-Time Fusion│ Unifying speech prosody (openSMILE), facial gaze │
│                               │ (MediaPipe), and live code execution (Docker).   │
│ 2. Dynamic RL Interventions   │ Transitioning from passive dashboard alerts to   │
│                               │ autonomous reinforcement-learned student nudges. │
│ 3. Prescriptive Counterfactual│ Generating actionable, feasible "what-if" study  │
│    Recourse Dashboards        │ and skill roadmaps for students and job seekers. │
│ 4. Live Market Skill Grounding│ Synchronizing university curricula and ATS with  │
│                               │ real-time hiring trends from live job portals.   │
│ 5. Cognitive Taxonomy AQG     │ Scaffolding automated question generation to     │
│                               │ evaluate higher-order Bloom's analysis skills.   │
│ 6. Privacy & Federated Twin   │ Decentralized, privacy-preserving multi-agent    │
│                               │ placement twins complying with POPIA / GDPR.     │
│ 7. Cognitive Layout IDP       │ Layout-invariant, vision-language resume parsing │
│                               │ for complex multi-column and graphical CVs.      │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master Cross-Corpus Future Work Matrix (All 44 Papers)

The matrix below compiles the explicit future-work proposals articulated by the original authors across all 44 papers, assessing implementation feasibility and direct relevance to the ScholarCamp / PRIE ecosystem:

| Paper ID | Primary Authors & Year | Tier A: Explicit Author-Stated Future Work (`[AUTHOR-STATED FUTURE WORK]`) | Thematic Cluster | Feasibility | PRIE Ecosystem Relevance |
|:---|:---|:---|:---|:---:|:---|
| **P01** | Sravan et al. (2025) | Expand sample size to multi-institutional cohorts; integrate coding metrics | Cluster 4 (Market/Coding)| High | Ingest competitive coding metrics (LeetCode, GitHub) |
| **P02** | Villegas-Chanaluisa (2025)| Implement dynamic counterfactual explanations in student-facing dashboards | Cluster 3 (Prescriptive XAI)| High | Deploy DiCE counterfactuals in student UI (P19) |
| **P03** | Joshi et al. (2025) | Deploy local LLMs for sub-second latency and cross-cultural gesture tracking | Cluster 1 (Multimodal Fusion)| Medium | Integrate WebRTC streaming and faster-whisper |
| **P04** | Kazi et al. (2025) | Incorporate adaptive generative quizzing to remediate identified resume gaps| Cluster 5 (Cognitive AQG)| High | Link ATS skill gaps directly to AQG quiz generator |
| **P05** | Bopape et al. (2025) | Design reinforcement learning policies to trigger automated nudge messages | Cluster 2 (Dynamic RL) | Medium | Deploy Proximal Policy Optimization (PPO) agent |
| **P06** | Pujari et al. (2025) | Connect model with live job board APIs (LinkedIn/Naukri) for dynamic weights | Cluster 4 (Market Grounding)| High | Implement live job description scrapers and embeddings |
| **P07** | Yadav et al. (2025) | Implement SHAP and LIME to provide actionable diagnostic feedback to students| Cluster 3 (Prescriptive XAI)| High | Deploy TreeSHAP and diagnostic advisor cards |
| **P08** | Anoop et al. (2025) | Distill deep temporal sequence attention weights into interpretable rules | Cluster 3 (Prescriptive XAI)| Medium | Use Temporal Fusion Transformer attention weights |
| **P09** | Thippanna et al. (2025)| Automate Abstract Syntax Tree (AST) code analysis for project scoring | Cluster 1 (Multimodal Fusion)| High | Integrate AST parser into Docker interview sandbox |
| **P10** | Rajesh et al. (2025) | Formulate continuous-time Markov decision processes for retention updates | Cluster 2 (Dynamic RL) | Medium | Multi-horizon weekly time-series forecasting |
| **P11** | Mishra (2025) | Replace lexical TF-IDF with dense semantic sentence transformer embeddings | Cluster 7 (Layout IDP) | High | Deploy Sentence-BERT dual-encoders (all-MiniLM) |
| **P12** | Kashif & Kumar (2024)| Deploy layout-aware vision-language document processing (LayoutLM) | Cluster 7 (Layout IDP) | High | Implement LayoutLMv3 spatial parsing pipeline |
| **P13** | Ashrafi et al. (2023)| Deploy localized open-weights LLMs fine-tuned on university curricula | Cluster 6 (Privacy/Local LLM)| High | Deploy 4-bit LLaMA-3-8B local RAG assistant |
| **P14** | Koli et al. (2025) | Integrate end-to-end multimodal fusion combining spoken text with non-verbal | Cluster 1 (Multimodal Fusion)| High | Combine MediaPipe vision with Whisper speech text |
| **P15** | Inamdar et al. (2025)| Unify multi-modal pipeline into end-to-end transformer for real-time scoring | Cluster 1 (Multimodal Fusion)| Medium | Deploy WebRTC streaming audio/vision pipeline |
| **P16** | Senthil et al. (2025)| Hybridize Ant Colony Optimization with real-time job market skill trends | Cluster 4 (Market Grounding)| Medium | Update course graph weights via live industry data |
| **P17** | Solanki et al. (2026)| Incorporate OCR layout parsing and candidate explanation reports | Cluster 7 (Layout IDP) | High | Generate ATS gap visualizer reports for students |
| **P18** | Sharma et al. (2025) | Generate actionable counterfactual recourses with minimal intervention cost| Cluster 3 (Prescriptive XAI)| High | Implement DiCE counterfactual optimization |
| **P19** | Kumar et al. (2025) | Enforce student cognitive load constraints during counterfactual generation | Cluster 3 (Prescriptive XAI)| High | Bound weekly study hour suggestions to $\le 15$ hrs |
| **P20** | Swacha & Gracel (2025)| Establish standardized benchmark suites for educational RAG evaluation | Cluster 6 (Privacy/RAG) | High | Enforce automated RAG Triad logging protocol |
| **P21** | Nisanth et al. (2025)| Explore hybrid long-context retrieval and hierarchical summary caching | Cluster 6 (Privacy/RAG) | High | Implement hierarchical syllabus chunk caching |
| **P22** | Ganesan et al. (2025)| Pair predictive models with conversational interview practice bots | Cluster 1 (Multimodal Fusion)| High | Link placement predictor directly to mock interview |
| **P23** | Venkatesh et al. (2025)| Deploy speculative decoding and query caching to reduce cloud API latency | Cluster 6 (Privacy/RAG) | High | Cache frequent student queries in Redis vector store |
| **P24** | Balasubramanian (2025)| Design targeted English communication and technical micro-modules | Cluster 4 (Market/Remediation)| High | Embed communication fluency drills into interview bot |
| **P25** | Wang et al. (2025) | Distill causal CoT prompting pipeline into fine-tuned 7B parameter model | Cluster 5 (Cognitive AQG)| High | Fine-tune local LLaMA-3 model for fast MCQ generation |
| **P26** | Awalurahman (2025) | Develop prompting frameworks specifically targeting Bloom's Analysis levels| Cluster 5 (Cognitive AQG)| High | Enforce Bloom's Taxonomy Level 4/5 prompt templates |
| **P27** | Zhang et al. (2025) | Transition from WoZ to fully autonomous LLM agents with empathetic tone | Cluster 1 (Multimodal Fusion)| High | Prompt Gemini 1.5 Flash with empathetic coaching persona |
| **P28** | Vachkal et al. (2026)| Deploy edge-device execution and speculative response streaming | Cluster 1 (Multimodal Fusion)| High | Stream Claude/Gemini tokens during code execution |
| **P29** | Wahid et al. (2026) | Integrate curriculum knowledge graph to bound LLM question generation | Cluster 1 (Multimodal Fusion)| High | Ground interview questions in Neo4j competency graph |
| **P30** | Verma et al. (2025) | Add WebAssembly-powered on-device computer vision for posture tracking | Cluster 1 (Multimodal Fusion)| High | Run MediaPipe FaceMesh via client-side WebAssembly |
| **P31** | Jia et al. (2022) | Develop online adaptive feature selection algorithms for streaming clickstreams| Cluster 2 (Dynamic RL) | Medium | Implement streaming feature selection pipelines |
| **P32** | Talmoudi & Choukir (2026)| Conduct human-in-the-loop studies measuring XAI impact on student grades | Cluster 3 (Prescriptive XAI)| High | Measure student placement offer uplift post-XAI |
| **P33** | Al-Shabandar (2019) | Combine clickstream logs with natural language processing of forum posts | Cluster 2 (Dynamic RL) | Medium | Ingest forum text embeddings into TFT temporal model |
| **P34** | Babu (2025) | Develop lightweight glass-box models for easier faculty deployment | Cluster 3 (Prescriptive XAI)| High | Deploy Explainable Boosting Machines (EBM) |
| **P35** | Gugnani & Misra (2020)| Utilize transformer-based contrastive learning representations (SimCSE) | Cluster 7 (Layout IDP) | High | Upgrade Doc2Vec to Sentence-Transformers |
| **P36** | Suryawanshi (2025) | Upgrade to dense sentence transformers and automated course suggestions | Cluster 7 (Layout IDP) | High | Link resume parser directly to course recommender |
| **P37** | JayaPriya et al. (2025)| Migrate to fine-tuned BERT bi-encoders and incorporate ATS format checks | Cluster 7 (Layout IDP) | High | Implement ATS formatting validation rules |
| **P38** | Kulkarni et al. (2026)| Conduct rigorous validation with corporate recruiters and speech prosody | Cluster 1 (Multimodal Fusion)| High | Benchmark PrepWise modules against enterprise panels |
| **P39** | Dousary et al. (2025)| Incorporate adversarial discriminator LLM to audit distractor exclusivity | Cluster 5 (Cognitive AQG)| High | Deploy dual-agent generator-verifier loop (P25) |
| **P40** | Murti et al. (2025) | Link RAG assistant interaction logs directly to end-of-semester exam grades | Cluster 6 (Privacy/RAG) | High | Correlate RAG usage hours with semester GPA uplift |
| **P41** | Babureddy & Mathew (2026)| Implement decentralized privacy-preserving federated learning across colleges| Cluster 6 (Privacy/Federated)| Medium | Design federated digital twin model updates |
| **P42** | Kapula (2025) | Model quantization and distillation into lightweight ONNX runtimes | Cluster 7 (Layout IDP) | High | Quantize LayoutLMv3 to ONNX for CPU deployment |
| **P43** | Rajeevan & Mini Devi (2026)| Incorporate syllabus-driven semantic seeding for first-year students | Cluster 4 (Market Grounding)| High | Map course enrollment codes directly into graph |
| **P44** | Azeez & Sajjad (2026)| Implement off-policy batch RL validation and teacher oversight dashboards | Cluster 2 (Dynamic RL) | High | Add advisor approval gate before RL nudge dispatch |

---

## 3. Emerging Candidate Research Directions for Phase 03

Synthesizing author-proposed future work across the 44 papers reveals four (4) transformative candidate research opportunities:

1. `[CANDIDATE RESEARCH OPPORTUNITY]` **The Unified Closed-Loop Placement Digital Twin**: Integrating ATS parsing (P12, P17, P42), real-time multimodal interview coaching (P28, P29), adaptive cognitive quizzing (P25, P39), and predictive employability modeling (P09, P22) into a synchronized multi-agent digital twin (P41).
2. `[CANDIDATE RESEARCH OPPORTUNITY]` **Prescriptive Counterfactual Career Remediation**: Moving beyond descriptive feature importance (TreeSHAP) by operationalizing constrained DiCE counterfactuals (P19) that tell students the exact minimal changes in study hours, coding challenges, and mock interviews required to achieve placement readiness.
3. `[CANDIDATE RESEARCH OPPORTUNITY]` **Multi-Horizon Dynamic Learning Analytics with RL Nudges**: Coupling Temporal Fusion Transformers (P44) for multi-horizon semester risk forecasting with safety-constrained Proximal Policy Optimization (PPO) reinforcement learning agents to automatically trigger tailored remedial interventions.
4. `[CANDIDATE RESEARCH OPPORTUNITY]` **Layout-Invariant ATS with Cognitive Distractor Verification**: Unifying LayoutLMv3 spatial document vision (P42) with dual-encoder semantic ranking (P17) and causal concept dependency graphs (P25) to automatically extract resume deficits and generate targeted, pedagogically verified assessment questions.

---

## 4. ScholarCamp / PRIE Architectural Implementation Roadmap

ScholarCamp / PRIE synthesizes these future-work trajectories into four operational development phases:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             PRIE ROADMAP SYNTHESIS                               │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Phase / Milestone        │ Targeted Future-Work Trajectories                     │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Milestone 1: Document &  │ Implement LayoutLMv3 (P42) + SBERT-BM25 hybrid (P17); │
│ Knowledge Intelligence   │ Construct Neo4j Competency & Prerequisite Graph (P13).│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Milestone 2: Conversational│ Deploy WebRTC streaming gateway with Gemini 1.5 Flash │
│ & Coding Sandbox         │ and openSMILE (P29); Integrate Docker sandbox (P28).  │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Milestone 3: Predictive  │ Train CatBoost employability model (P22) & Temporal   │
│ & Explainable Core       │ Fusion Transformer (P44); Deploy DiCE counterfactuals.│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Milestone 4: Closed-Loop │ Synchronize all modules via Triangular Digital Twin   │
│ Placement Digital Twin   │ (P41) with PPO reinforcement learning nudges (P44).   │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
