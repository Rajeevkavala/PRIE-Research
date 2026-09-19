# Paper04 — Multimodal AI-Based Mock Interview System

## Paper metadata

| Field | Value |
|---|---|
| Title | Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation |
| Authors | Independent Consortium (as reported) |
| Year | 2025 |
| Journal | *International Journal of Scientific Research and Engineering Development (IJSRED)*, 8(6) |
| Publisher | IJSRED |
| DOI | Not reported; source plan maps it to [IJSRED PDF](https://ijsred.com/volume8/issue6/IJSRED-V8I6P92.pdf). |
| Domain | Multimodal AI; mock interviewing; speech emotion recognition; facial-expression analysis; NLP |

## Context, objectives, and questions

### Problem statement and motivation

Conventional interview preparation privileges technical answers but inadequately offers objective feedback on non-verbal communication, vocal delivery, tone, and anxiety-sensitive performance. Peer mentoring and static question banks do not scale or measure micro-level paralinguistic cues.

### Objectives extracted or inferred

1. Simulate domain-specific, dynamic interviews.
2. Assess visual, vocal, and linguistic aspects of a candidate response.
3. Provide holistic, data-driven feedback on technical and soft skills.
4. Improve confidence and interview success.

### Inferred questions

Can a live multimodal system assess facial, speech, and textual interview signals with useful accuracy? Does its feedback improve confidence and interview outcomes?

## Architecture and workflow

```text
Candidate / resume context
 → Gemini creates dynamic domain-specific questions
 → candidate video + speech response
 ├─ facial-expression CNN → facial signal
 ├─ speech-emotion / acoustic analysis → confidence, delivery signal
 └─ NLP sentiment + semantic relevance → content-quality signal
 → holistic real-time feedback and score
```

| Method category | Reported elements |
|---|---|
| Generative AI | Google Gemini for question generation |
| Vision | Deep-learning facial-expression CNNs |
| Audio | Speech Emotion Recognition; acoustic/prosodic measures such as pitch variation, speaking tempo, filler-word density described in source-plan context |
| NLP | Sentiment and semantic relevance analysis |
| Overall design | Quad-module architecture integrating video, audio-feature extraction, NLP, and real-time assessment |
| Resume awareness | Dynamic questions are described as domain-specific; source-plan context says resume-aware questioning is an intended ScholarCamp extension, not a verified feature of this paper |
| Preprocessing, fusion method, weights, tuning | Not reported |

## Dataset and setup

| Field | Value |
|---|---|
| Evaluation cohort | 150 job candidates in simulated interviews |
| Modalities | Video, audio, response text/NLP outputs |
| Ground-truth labels, demographics, consent process, split | Not reported |
| Hardware/software/frameworks/latency | Not reported; high computational demand and real-time video latency are identified as limitations |
| Missing-data / dropped-modality handling | Not reported |

## Evaluation and results

| Component / outcome | Reported result |
|---|---:|
| Facial module accuracy | **82%** |
| Speech module accuracy | **91%** |
| NLP module accuracy | **87%** |
| Self-reported candidate-confidence improvement | **34.2%** |
| Actual interview-success rate | **3.2× higher** among system users |

Definitions of accuracy, label sources, baselines/control design, confidence intervals, statistical significance, aggregate/fusion metric, fairness measures, false-positive/false-negative errors, and longitudinal retention are not reported.

## Strengths, limitations, and gaps

### Strengths

- Treats interview performance as multimodal rather than solely technical correctness.
- Uses dynamic questioning instead of a static question bank.
- Reports component-level accuracy and behavioral/outcome improvements.
- Directly targets anxiety, verbal communication, and non-verbal delivery.

### Explicit limitations

- High computation and latency for real-time video processing.
- Facial recognition may induce demographic algorithmic bias.

### Implied limitations

- Facial-expression proxies are culturally and individually variable; confidence cannot reliably be inferred from appearance alone.
- A 150-candidate live cohort may not establish generalizability across language, disability, job role, or culture.
- Self-reported confidence may not equal durable interview competence.
- Causal interpretation of 3.2× success requires a control, randomization, and confounder analysis not reported in the plan.

### Novel contribution reported

The plan credits the work with establishing the value of multimodal feedback loops for faster soft-skill development and lower interview anxiety.

### Future work reported

Develop lightweight, audio-first architectures to reduce latency and avoid visual demographic-bias pathways.

### Gap addressed / remaining gap

Addresses absence of objective feedback on verbal/non-verbal interview performance. It remains computationally heavy, susceptible to visual bias, and disconnected from end-to-end placement prediction, ATS evidence, and personalized learning remediation.

## ScholarCamp relevance and reusable design

- Prefer audio-first interaction: ASR transcript, semantic relevance, filler-word rate, pace, pause statistics, and prosody—subject to disability/accent-aware evaluation.
- Use a job-role and skill-rubric question blueprint; score answers against retrieved trusted rubrics, not latent affect alone.
- Retain a user-visible transcript, rubric evidence, and uncertainty; permit correction and opt-out of each modality.
- Feed only validated, stable signals into PRIE and conduct ablation/fairness tests before making readiness-impact claims.
- Evaluate an A/B or randomized study against static practice, with pre-registered outcomes and human-rater agreement.

## Important citations, keywords, reviewer notes

- [Primary paper PDF](https://ijsred.com/volume8/issue6/IJSRED-V8I6P92.pdf)
- [AI Mock Interview using Gemini AI and Whisper](https://www.ijert.org/ai-mock-interview-an-intelligent-voice-driven-interview-simulation-system-using-gemini-ai-and-whisper-ijertv15is031282)
- [PrepWise: ATS and real-time mock interviews](https://ijcrt.org/download.php?file=IJCRT2604367.pdf)

Keywords: mock interview; multimodal AI; speech emotion recognition; SER; facial-expression recognition; CNN; conversational AI; Google Gemini; interview simulation; acoustic features; prosody; pitch; speaking rate; filler words; speech transcription; NLP; sentiment analysis; semantic relevance; soft-skill assessment; confidence; algorithmic bias; real-time inference; audio-first design; fairness.

| IEEE reviewer criterion | Score / 10 | Assessment |
|---|---:|---|
| Novelty | 6 | Practical multimodal combination; novelty depends on fusion and validation specifics. |
| Technical depth | 6 | Covers vision, audio, and NLP; fusion details missing. |
| Research quality | 5 | Important human-centered problem; validity evidence is incomplete. |
| Experimental quality | 5 | Multiple numeric outcomes reported, but protocol/baselines are not available. |
| Writing quality | 5 | Secondary profile is readable; primary review required. |
| Reproducibility | 2 | No model setup, labels, split, rubric, or code details supplied. |
| Conference readiness | 4 | Needs ethics, demographic and accessibility analyses, human-rater validation, and controlled studies. |

## How can this paper improve ScholarCamp?

Adopt the paper’s holistic practice-feedback goal but avoid making facial emotion a core readiness signal. Deliver configurable audio/text-first mock interviews, use explicit role-specific rubrics, and offer students measurable revision tasks. Test whether repeat practice improves human-rated answer quality, not merely model-derived confidence scores.
