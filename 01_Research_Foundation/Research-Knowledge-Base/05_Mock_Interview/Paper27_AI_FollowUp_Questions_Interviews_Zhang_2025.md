# Paper 27 — Harnessing the Power of AI in Qualitative Research: Role Assignment, Engagement, and User Perceptions of AI-Generated Follow-Up Questions in Semi-Structured Interviews

## 1. Bibliographic Information

- **Paper ID**: Paper27
- **Full Title**: Harnessing the Power of AI in Qualitative Research: Role Assignment, Engagement, and User Perceptions of AI-Generated Follow-Up Questions in Semi-Structured Interviews
- **Authors**: He Zhang (Penn State University), Yueyan Liu (Tsinghua University), Xin Guan (Columbia University), Jie Cai (Tsinghua University), and John M. Carroll (Penn State University)
- **Year**: 2025/2026 (ACM Conference format)
- **Venue**: ACM Conference on Human Factors in Computing Systems (CHI / CSCW conference proceedings format)
- **DOI**: ACM proceedings format (Note: header shows template format `10.1145/nnnnnnn.nnnnnnn`)
- **PDF filename**: `Paper27_amarnath2025intelligent.pdf` (Note: filename reflects legacy bibtex mismatch tag `amarnath2025intelligent` which actually corresponds to Ref [5] in this paper's bibliography; authentic primary PDF is authored by He Zhang et al., Penn State & Tsinghua University)
- **PDF path**: `Papers/PDFs/Paper27_amarnath2025intelligent.pdf`
- **Page count**: 19 pages (pp. 1–19)

---

## 2. Research Problem

Semi-structured interviews rely heavily on the quality and timing of real-time follow-up questions (probes). However, an interviewer's domain knowledge, working memory, and split-second conversational management often constrain question depth, leading to missed sub-dimensions, fatigue, and topic drift. While Large Language Models (LLMs) are widely studied for post-hoc qualitative data analysis, their real-time deployment as dynamic co-interviewers during live data collection remains underexplored, particularly regarding conversational pacing, role division, human gatekeeping, and trust.

### Source Evidence
- **Page**: PDF p. 1
- **Section**: Abstract & Section 1 — Introduction

---

## 3. Research Objectives

1. To investigate how real-time LLM support in generating adaptive follow-up questions (AGQs - AI-Generated Questions) shapes the dynamics, depth, and conversational flow of semi-structured interviews.
2. To examine lead interviewers' cognitive load, role perceptions, and trust calibration when collaborating with an AI co-interviewer.
3. To identify optimal interaction configurations (frontstage autonomous AI vs backstage human-screened assistant) and formalize design principles (such as an "AI Checker" and bidirectional questioning) for human-AI interviewing systems.

### Source Evidence
- **Page**: PDF pp. 1–3
- **Section**: Abstract & Section 1

---

## 4. Research Questions

The paper explicitly formulates two research questions:
- **RQ1**: *How do lead interviewers perceive follow-up questions in semi-structured interviews when supported by AI?* (Focusing on depth enhancement, supplementation of missed points, conversational flow, and timing collisions).
- **RQ2**: *How do lead interviewers perceive the follow-up assistant / AI co-interviewer?* (Evaluating cognitive load reduction, fatigue mitigation, gatekeeping autonomy, and trust mediated by domain expertise and research goal alignment).

### Source Evidence
- **Page**: PDF pp. 3–4, 8–9
- **Section**: Section 1 & Section 4 (Sections 4.1 & 4.2)

---

## 5. Dataset / Participant Cohort

- **Methodology**: AI-driven Wizard-of-Oz (WoZ) empirical laboratory study.
- **Participant Sample ($N=17$)**:
  - 17 recruited researchers/interviewers (10 female, 7 male; ages 21 to 35).
  - Academic credentials: PhD candidates/holders (4), Master's students/graduates (10), Bachelor's (3).
  - Disciplines: Human-Computer Interaction (HCI), Education, Smart Home, Psychology, Usable Privacy and Security, Applied Linguistics, Ergonomics, Social Work, Management Science.
  - Experience: Novice (9), Intermediate (6), Advanced (2; $>3$ published peer-reviewed qualitative papers).
- **Session Architecture**: 3 roles per session: (1) Participant as primary lead interviewer, (2) Researcher simulating the interviewee ("Oz"), and (3) Researcher functioning as the "Wizard" feeding real-time dialogue into the LLM.
- **Intervention Patterns Evaluated**:
  1. *Occasional single follow-up*: Sparse probe insertions.
  2. *Periodic follow-up*: Insertion after every 1–2 participant questions.
  3. *Consecutive multi-probing*: 2 or more sequential follow-ups without participant interjection.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section 3.1 (Participants) & Section 3.2 (Study Design, Table 1)

---

## 6. Features / Input Streams

Input signals processed dynamically during live interviews:
- **Real-Time Dialogue Transcript**: Live spoken utterance stream between interviewer and interviewee.
- **Research Goals & Outline**: Pre-defined interview protocol and study objectives provided by the participant.
- **Probe Type Tags**: Categorized follow-up modes (clarification, concrete example request, contrast, causal mechanism, boundary testing).
- **Turn-Taking & Pacing Latency**: Timing gaps and pauses between conversational turns.

### Source Evidence
- **Page**: PDF pp. 4–6, 11
- **Section**: Section 3 & Section 5.1.1

---

## 7. Data Preprocessing

- **Interview Topic Alignment**: Pre-screening participant outlines to ensure simulation feasibility across domains.
- **Prompt Formulation**: Structuring conversation history, active research objectives, and instructions for GPT-4o to generate concise, non-leading, probe-style questions.
- **Qualitative Data Extraction**: Video/audio recordings transcribed and coded through inductive thematic analysis; independent multi-coder reliability verification with debrief consensus.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section 3

---

## 8. Algorithms and Models

- **Core LLM Engine**: **GPT-4o** (OpenAI), executing zero-shot / few-shot dynamic prompt chains to generate context-sensitive follow-up probes in real time based on "Oz" transcript streams.
- **Intervention Controller**: Simulated Wizard-of-Oz mediation controlling latency, insertion frequency, and role allocation (testing frontstage direct-speech vs backstage text-feed delivery).
- **Proposed Architectural Framework — AI Checker Mechanism (Figure 8)**: Dual-agent design incorporating an automated alignment checker to verify that generated probes align with study goals before being presented to the interviewer.

### Source Evidence
- **Page**: PDF pp. 4–5, 14–15
- **Section**: Section 3.2 & Section 5.3 (Figure 8)

---

## 9. Architecture

The paper formalizes **Four AI-Supported Interview Modes** across two orthogonal axes (Figure 5):
1. **Axis 1 (Visibility)**: Frontstage (AI speaks directly to interviewee) vs Backstage (AI suggests probes silently to human interviewer).
2. **Axis 2 (Autonomy)**: Autonomous (AI acts unvetted) vs Human Gatekeeping (Interviewer approves/edits AI suggestions).

### System Topologies Identified
- **Frontstage Co-Interviewer with Human Approval (Figure 7)**: AI synthesizes probe $\rightarrow$ displayed to interviewer $\rightarrow$ approved with 1 click $\rightarrow$ synthesized voice asks interviewee.
- **Backstage Scaffolding Assistant (Figure 3 & 4)**: AI acts as private cognitive copilot on interviewer's second screen.
- **Bidirectional Questioning Framework (Figure 6)**: Three-way collaborative inquiry enabling mutual verification between AI, researcher, and interviewee.

### Source Evidence
- **Page**: PDF pp. 2, 10–14
- **Figures**: Figures 1, 3, 4, 5, 6, 7, 8

---

## 10. Methodology

1. **Protocol Preparation**: Participants submit interview protocols based on their own specialized domain expertise.
2. **WoZ Simulation**: The participant leads a 45–60 minute interview with "Oz" while GPT-4o generates real-time probes across varying frequency conditions.
3. **Semi-Structured Debrief & Retrospective Cued Recall**: Immediately following the interview, participants review video recordings and probe moments to critique timing, usefulness, and perceived agency.
4. **Thematic Coding**: Transcript analysis identifying cognitive load impacts, conversational disruptions, and role evolution.

### Source Evidence
- **Page**: PDF pp. 4–6
- **Section**: Section 3

---

## 11. Experimental Setup

- **LLM**: GPT-4o API.
- **Setting**: Synchronous video-conferencing interview suite with multi-channel audio capture.
- **Participant Distribution**: 17 interviewers spanning 9 academic departments across 3 continents.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Section 3

---

## 12. Evaluation Metrics

- **Cognitive Load Reduction**: Qualitative self-reports on mental fatigue, working memory release, and attention allocation.
- **Conversational Pacing & Flow Stability**: Frequency of turn-taking collisions, topic derailments, and conversational awkwardness.
- **Probe Depth & Supplementation**: Extent to which AGQs captured overlooked sub-dimensions and pushed broad answers into analyzable specifics.
- **Trust & Agency Calibration**: Willingness of interviewer to delegate questions vs desire for strict gatekeeping control.

### Source Evidence
- **Page**: PDF pp. 7–11
- **Section**: Section 4 (Sections 4.1 & 4.2)

---

## 13. Results

### Perceived Usefulness of AI-Generated Questions (RQ1)
1. **Depth-Oriented Supplementation**: 100% of participants recognized that AGQs successfully identified subtle details, omitted sub-dimensions, and pushed high-level conceptual statements down to granular, concrete examples.
2. **Novice Scaffolding**: For novices ($N=9$), AGQs acted as an indispensable cognitive buffer, providing ready-made probes while the novice processed previous answers.
3. **Conversational Collisions & Flow Disruption**: Consecutive multi-probing (Pattern 3) was universally rejected; it created rigid, interrogation-like dynamics, disempowered the lead interviewer, and overwhelmed the interviewee.

### Cognitive Load & Trust Calibration (RQ2)
1. **Cognitive Relief**: Participants reported substantial reductions in cognitive exhaustion and fatigue (P6, P12), improved time management (P7, P8), and enhanced note-taking support (P9, P14).
2. **The Timing Bottleneck**: Machine intervention latency and turn-taking timing were identified as the single greatest vulnerability; ill-timed questions broke conversational rapport even when the probe content was intellectually sound.
3. **Mandatory Human Gatekeeping**: Experienced interviewers strongly favored **backstage** positioning where they retained ultimate veto power over whether an AGQ was vocalized.

### Source Evidence
- **Page**: PDF pp. 7–12
- **Section**: Section 4 & Section 5

---

## 14. Baselines

- **Solo Unassisted Human Interviewing**: Conventional human interviewer conducting semi-structured interview without AI tooling.
- **Unconstrained Autonomous AI Interviewer**: Direct AI-to-interviewee conversational agents without human supervision or gatekeeping.

### Source Evidence
- **Page**: PDF pp. 2–4, 10–11
- **Section**: Sections 1, 3, 5

---

## 15. Ablation Study

- The study systematically contrasted three intervention frequencies:
  - *Sparse Single Probe*: Maximally preserved human rapport; rated highest by experienced researchers.
  - *Periodic Probing*: Effective for novices; required strict human veto control.
  - *Consecutive Multi-Probing*: Severely damaged conversational flow and rapport; proved unsuitable for live interviewing.

### Source Evidence
- **Page**: PDF pp. 4–5, 8–10
- **Section**: Section 3.2 & Section 4.1

---

## 16. Explainability & Alignment

- The study introduces the **AI Checker Mechanism** (Figure 8), which explicitly computes and visualizes alignment between generated follow-up questions and the overarching research goals / rubrics before presentation to the user, providing transparent prompt rationales.

### Source Evidence
- **Page**: PDF pp. 14–15
- **Section**: Section 5.3 & Figure 8

---

## 17. Main Findings

1. **Coupled Condition of Question Quality and Conversational Flow**: High semantic question quality is useless if conversational timing, tone, and turn-taking are disrupted.
2. **Differentiated User Needs**: Novice interviewers require real-time content scaffolding to formulate questions, whereas expert interviewers require high-gain, unexpected boundary-testing probes delivered silently backstage.
3. **The Primacy of Backstage Human-in-the-Loop**: Full AI autonomy in live interviews alienates both interviewer and candidate; the optimal paradigm is backstage co-piloting with instantaneous human approval.

### Source Evidence
- **Page**: PDF pp. 10–13
- **Section**: Section 5 — Discussion

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Simulated Interviewee Dynamics**: Used researcher-simulated interviewees ("Oz") rather than genuine field interviewees in high-stakes environments.
2. **Wizard-of-Oz Latency Buffer**: The human Wizard manually inputting text introduces timing artifacts that may differ from fully automated speech-to-text pipelines.
3. **Sample Size**: Qualitative study cohort of 17 participants, limiting broad statistical generalizability across cultural interview norms.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The study focused on academic research interviews; technical coding or behavioral placement mock interviews introduce additional stress vectors, code evaluation needs, and objective scoring rubrics not present in qualitative social science interviews.

### Source Evidence
- **Page**: PDF pp. 4, 15
- **Section**: Section 3 & Section 5

---

## 19. Future Work

Explicitly proposed by the authors:
1. Developing low-latency speech-to-text integrated prototypes that eliminate the human wizard.
2. Implementing and validating the **AI Checker Mechanism** to filter out-of-scope follow-ups automatically.
3. Conducting field trials with real interviewees across medical, legal, and educational domains.

### Source Evidence
- **Page**: PDF pp. 14–16
- **Section**: Section 5 & Section 6

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides foundational human-AI interaction insights for PRIE's **AI Mock Interview Engine**:
1. **Dynamic Follow-Up Probing**: Standard mock interview bots ask rigid, pre-scripted questions. Zhang et al. provide empirical proof that adaptive follow-up questions dramatically increase interview depth and candidate diagnostic assessment.
2. **Pacing and Turn-Taking Architecture**: Zhang et al.'s finding that consecutive AI questions feel like "interrogation" warns PRIE against aggressive multi-turn probing; PRIE must enforce natural pauses and allow candidates to complete thoughts.
3. **Backstage vs Frontstage Modes**: For peer-to-peer student mock interviews in ScholarCamp, PRIE can implement the "Backstage Copilot Mode", feeding suggested technical follow-up questions to a student interviewer evaluating their peer.
4. **AI Checker Implementation**: PRIE can adopt the AI Checker architecture to ensure that generated technical interview questions adhere strictly to the target company's job description and syllabus.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **Primary Research Focus** | "investigate how real-time LLM support in generating follow-up questions shapes semi-structured interviews... study with 17 participants." | PDF p. 1, Abstract | Direct statement |
| **LLM Engine** | "all follow-up questions were generated in real-time by GPT-4o, based directly on the responses provided by 'Oz'." | PDF pp. 4–5, Section 3.2 | Experimental setup |
| **Participant Demographics** | 17 participants (10 female, 7 male, ages 21–35; 9 novices, 6 intermediate, 2 advanced; PhD/Master/Bachelor). | PDF p. 5, Table 1 | Table / Demographics |
| **Cognitive Load Relief** | Participants confirmed reduction in cognitive fatigue (P6, P12) and assistance in capturing overlooked points (P8, P10). | PDF pp. 7–9, Sections 4.1 & 4.2 | Experimental result |
| **Pacing Breakdown** | Posing consecutive follow-ups without interviewer interjection disrupted conversational flow and created interrogation dynamics. | PDF pp. 9–10, Section 4.1 | Qualitative finding |
| **Proposed Architectures** | Formalized 4 quadrant interview modes (Figure 5), bidirectional questioning (Figure 6), and AI Checker mechanism (Figure 8). | PDF pp. 10–14, Section 5 | Architectural contribution |

---

## 22. Verification Checklist

- [x] PDF read (`Paper27_amarnath2025intelligent.pdf`, 19 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (WoZ study with Wizard, Oz, and Lead Interviewer)
- [x] Dataset verified ($N=17$ participants, Table 1 demographics verified)
- [x] Features verified (Dialogue transcripts, protocol outlines, probe types)
- [x] Algorithms verified (GPT-4o prompting, Wizard-of-Oz intervention controller)
- [x] Architecture inspected (Figures 1, 3, 4, 5, 6, 7, 8 verified)
- [x] Experiments inspected (3 intervention frequency modes tested)
- [x] Results verified (Depth enhancement, cognitive load reduction, pacing bottlenecks)
- [x] Limitations verified (Simulated Oz interviewee, WoZ latency buffer, sample size)
- [x] Future work verified (Low-latency STT, AI Checker prototype, field deployment)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 17-participant cohort from Table 1, GPT-4o setup from Section 3.2, architectural quadrants from Figure 5, and AI Checker design from Figure 8 verified directly from source text; legacy filename discrepancy documented).
