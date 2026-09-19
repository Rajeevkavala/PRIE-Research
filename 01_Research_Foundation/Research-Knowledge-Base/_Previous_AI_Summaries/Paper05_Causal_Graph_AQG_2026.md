# Paper05 — Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning

## Paper metadata

| Field | Value |
|---|---|
| Title | Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning |
| Authors | Independent Researchers (as reported) |
| Year | 2026 |
| Venue / publisher | arXiv preprint / arXiv |
| DOI | Not reported; [source PDF](https://arxiv.org/pdf/2601.06098) |
| Citation supplied by plan | [Anonymous]. (2026). *Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning*. arXiv preprint. |
| Domain | Automatic question generation; RAG; LLMs; knowledge graphs; adaptive learning |

## Context, objectives, and research questions

### Problem statement

LLM-generated educational questions can hallucinate, be factually wrong, violate curriculum constraints, or fail pedagogical alignment. Such content can reinforce misconceptions and reduce learner trust.

### Objectives extracted or inferred

1. Generate factually grounded, curriculum-aligned questions.
2. Represent concept dependencies using a causal graph.
3. Use specialized agents for pathfinding, reasoning, validation, and generation.
4. Support scaffolded, multi-step questions and prerequisite-aware sequencing.
5. Reduce hallucination and drift relative to unconstrained generation.

### Inferred research questions

Can causal-graph-guided CoT plus multi-agent generation improve factuality and learning-objective alignment? Can graph dependencies create scaffolded, prerequisite-aware questions?

## Architecture and technical workflow

```text
Verified STEM curricula, textbooks, university materials
 → embed/index trusted content in a vector database (RAG corpus)
 → construct causal concept-dependency graph
 → pathfinding agent identifies prerequisite / target path
 → reasoning agent uses graph-guided CoT
 → generation agent drafts question
 → validation agent checks grounding, logic, and learning objective
 → Bloom-aligned, scaffolded question and rationale
```

| Component | Reported contribution |
|---|---|
| Knowledge source | Domain-specific STEM curricula, textbooks, verified university lecture materials |
| Retrieval / grounding | RAG pipeline; source-plan describes vector embeddings/vector database concept |
| Structure | Causal graph mapping strict concept dependencies |
| LLM workflow | Multi-agent roles: pathfinding, reasoning, validation, generation |
| Reasoning | Chain-of-Thought guided by the causal graph |
| Algorithms | Graph traversal; RAG; multi-agent LLM architecture |
| Pedagogy | Bloom’s Taxonomy alignment; scaffolded multi-step questions; prerequisite concept mastery |
| Model family/name, prompts, retrieval configuration, graph-building algorithm, hyperparameters | Not reported |

## Dataset and experimental record

| Field | Value |
|---|---|
| Source materials | STEM curricula, textbook data, verified university lecture materials |
| Size / disciplines / annotations / question count | Not reported |
| Labels | No formal labels reported; targets include factuality, curriculum alignment, and cognitive objectives |
| Train/test split, contamination controls, missing values | Not reported |
| Hardware, model/API versions, frameworks, cost/latency | Not reported |

## Evaluation and results

### Reported findings

- The architecture **significantly reduces hallucination rates** (no numeric rate supplied).
- It generates scaffolded, multi-step questions aligned with cognitive objectives and Bloom’s Taxonomy.

### Metrics not reported

No numerical hallucination rate, question-validity rate, human-expert agreement, retrieval recall, answer correctness, difficulty calibration, discrimination index, latency, cost, safety failure rate, or baseline comparison is supplied by the plan. These are required for a reproducible empirical claim.

## Strengths, limitations, gaps, and future work

### Strengths

- Grounds generation in verified sources rather than unconstrained LLM memory.
- Encodes prerequisite dependencies explicitly instead of only using semantic similarity.
- Separates generation from validation in a multi-agent workflow.
- Targets pedagogical sequencing, not merely grammatical question generation.

### Explicit limitation

The causal graph and vector embeddings require intensive upfront manual or semi-automated construction.

### Implied limitations

- “Causal” graph edges must be validated: a concept dependency graph is not automatically a causal model.
- Multi-agent pipelines increase latency, cost, and failure surfaces.
- RAG cannot guarantee factuality when retrieval is incomplete or validation is weak.
- Quality claims need blind expert review and learner-outcome studies, not only model self-validation.

### Novel contribution reported

The paper proposes a mathematically structured, causal-graph-guided multi-agent CoT approach for reliable automated-question generation and learning-objective alignment.

### Future work reported

Automatically extract causal knowledge graphs from unstructured video lectures and academic papers.

### Gap addressed / remaining gap

It addresses hallucination and curriculum misalignment in AQG. It does not yet demonstrate low-cost deployment, automatic graph induction, learner-effectiveness outcomes, or an integrated placement-readiness loop.

## ScholarCamp relevance and implementation ideas

- Make a skills ontology from verified course outcomes, job-role competencies, and prerequisite relationships; distinguish source-supported links from inferred links.
- When PRIE/SHAP identifies an actionable gap, retrieve approved content and generate only to a declared Bloom level and difficulty target.
- Store question provenance: retrieved chunks, graph path, model/version, validator verdict, rubric, and human-review state.
- Create a failure-safe: if retrieval evidence is insufficient, ask/route rather than generate a claimed answer.
- Evaluate against static authored questions, plain RAG, and ungrounded LLM generation with blinded faculty ratings and learning-gain measures.

## Important citations, keywords, and reviewer notes

- [Primary arXiv PDF](https://arxiv.org/pdf/2601.06098)
- [RAG Chatbots for Education: survey](https://www.researchgate.net/publication/390700272_Retrieval-Augmented_Generation_RAG_Chatbots_for_Education_A_Survey_of_Applications)
- [RAG-Based AI Chatbot for Student and Institutional Assistance](https://www.ijraset.com/research-paper/rag-based-ai-chatbot-for-student-and-institutional-assistance)

Keywords: automatic question generation; AQG; retrieval-augmented generation; RAG; large language model; multi-agent system; chain-of-thought; causal graph; concept dependency graph; graph traversal; vector database; embeddings; grounded generation; hallucination mitigation; Bloom’s Taxonomy; adaptive learning; prerequisite mastery; curriculum alignment; intelligent tutoring; knowledge graph; validation agent; educational NLP.

| IEEE reviewer criterion | Score / 10 | Assessment |
|---|---:|---|
| Novelty | 7 | Explicit causal-graph-guided multi-agent AQG is a potentially differentiated formulation. |
| Technical depth | 7 | Graph, retrieval, reasoning, validation, and pedagogy are coherently linked. |
| Research quality | 5 | Claims are promising but numerical evidence is unavailable in the source plan. |
| Experimental quality | 3 | No detailed dataset, baselines, or metrics reported. |
| Writing quality | 6 | Conceptual profile is clear; preprint should be scrutinized directly. |
| Reproducibility | 2 | Model, corpus, graph, prompts, and implementation are unspecified. |
| Conference readiness | 5 | Needs expert/human studies, robust benchmarks, ablations, and open artefacts. |

## How can this paper improve ScholarCamp?

Use its causal-graph/RAG principle to make ScholarCamp’s quiz and tutor outputs traceable rather than merely fluent. Build a curated career-skill graph first, generate questions only from retrieved evidence, validate them against a job-specific rubric, and use student performance to update—not blindly overwrite—the estimated skill state.
