# Mock Interview Systems Comparison & Multimodal Synthesis

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/Interview_Comparison.md`  
**Status**: Authoritative Interview Systems Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. The Automated Interview Assessment Landscape

Automated mock interview systems simulate technical and behavioral employment evaluations, providing candidates with objective feedback on communication, coding proficiency, emotional composure, and subject-matter expertise. Across the 44 verified papers, eight (8) primary studies investigate mock interview automation:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         MOCK INTERVIEW RESEARCH DOMAINS                          │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Focus Area                    │ Representative Studies & Systems                 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Non-Verbal Video Tracking  │ P14 (Koli et al., 2025), P15 (Inamdar et al., 2025)│
│                               │ MediaPipe FaceMesh, eye gaze, VGG-16 facial AUs. │
│ 2. Acoustic Prosody & Speech  │ P03 (Joshi et al., 2025), P29 (Wahid et al., 2026)│
│                               │ openSMILE toolkit, pitch F0, jitter, shimmer.    │
│ 3. Human-Agent Psychometrics  │ P27 (Zhang et al., 2025 Wizard-of-Oz Study)      │
│                               │ Anxiety delta, pupil dilation, Galvanic Skin.    │
│ 4. Enterprise Technical Voice │ P28 (Vachkal et al., 2026 IndusAI)               │
│    & Code Execution           │ Whisper-v3, Claude-3-Sonnet, Docker sandbox.     │
│ 5. Real-Time WebRTC Streaming │ P29 (Wahid et al., 2026)                         │
│                               │ Gemini 1.5 Flash, WebRTC streaming, <1.2s lag.   │
│ 6. Full-Stack Web Portals     │ P30 (Verma et al., 2025), P38 (Kulkarni et al., 2026)│
│                               │ MERN stack, Web Speech API, PrepWise portal.     │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master Mock Interview Cross-System Benchmark Matrix

The table below provides a comprehensive architectural and empirical comparison across all eight mock interview systems in the corpus:

| Paper ID & System | Modalities Evaluated | Speech-to-Text (ASR) Engine | Video & Facial Feature Extractor | Audio Prosody Toolkit | Dialogue & Feedback Engine | Live Code Sandbox | Human Expert Score Correlation | End-to-End System Latency |
|:---|:---|:---|:---|:---|:---|:---:|:---|:---|
| **P03** (Joshi et al., 2025) | Audio, Facial, Text | OpenAI Whisper | MediaPipe FaceMesh (468 landmarks) | openSMILE (eGeMAPS) | RoBERTa + Gemini-Pro | No | Intent Acc: 86.4%, Emotion: 82.1% | ~2.8s |
| **P14** (Koli et al., 2025) | Video, Audio | Wav2Vec 2.0 | MediaPipe Gaze + Head Pose | Custom Python RMS | Rule-based scoring | No | Non-verbal confidence: r = 0.78 | ~1.5s |
| **P15** (Inamdar et al., 2025)| Video, Audio, Text | SpeechRecognition (Google) | VGG-16 CNN (Emotion AU12/AU04)| Speech Jitter / Shimmer | TextBlob Sentiment | No | Panel correlation: rho = 0.82 | >15.0s (Batch post-processing)|
| **P27** (Zhang et al., 2025) | Audio, Text, GSR | Whisper ASR | Pupil Dilation Tracker | Pitch / Pause extraction | Wizard-of-Oz (Human-in-Loop)| No | Anxiety reduction: -31% (p<0.01) | Real-time (Human operator) |
| **P28** (Vachkal et al., 2026)| Voice, Code, Text | **OpenAI Whisper-v3** | None (Voice + Code only) | Librosa Speech Rate | **Claude-3-Sonnet** | **Yes (Docker Sandbox)**| Code eval: 88.5%, Soft skill: r=0.84 | ~3.5s–5.0s (Compile + LLM) |
| **P29** (Wahid et al., 2026) | Audio, Voice, Text | Whisper-v3 | None (Pure Voice/Prosody) | **openSMILE (Real-Time)** | **Google Gemini 1.5 Flash** | No | Prosody Acc: 90.1%, Fluency: r=0.87 | **<1.2s (WebRTC Streaming)**|
| **P30** (Verma et al., 2025) | Audio, Text | Web Speech API | None | Speech-to-Text latency | OpenAI GPT-3.5 API | No | Usability SUS: 82.4/100, Comp: 85.6%| ~2.2s |
| **P38** (Kulkarni et al., 2026)| Audio, Text, Quiz | Web Speech API | None | Simple duration logging | Basic BERT similarity | No | Preparedness gain: +28% (Self-report)| ~1.8s |

---

## 3. Critical Methodological Findings & Engineering Bottlenecks

### 3.1 The Conversational Latency Bottleneck
- `[CROSS-PAPER OBSERVATION]` Natural human conversational dialogue requires conversational turn latency of under **1.2 to 1.5 seconds**. When latency exceeds 2.5 seconds, candidate cognitive flow is disrupted, inducing unnatural speech pauses and elevated anxiety.
- `[AUTHOR-STATED LIMITATION]` Multi-stage architectures that asynchronously cascade separate models (e.g., Inamdar et al., P15: video frame extraction $\rightarrow$ VGG-16 $\rightarrow$ Google ASR $\rightarrow$ TextBlob) suffer catastrophic latency exceeding **15 seconds per response**, completely prohibiting real-time interactive dialogue.
- `[AUTHOR-STATED FACT]` Wahid et al. (P29) overcame this barrier by establishing a direct **WebRTC audio streaming channel connected to Gemini 1.5 Flash**, streaming raw PCM audio chunks concurrently to a local **openSMILE prosody engine** and the cloud LLM, achieving an end-to-end turnaround latency of **under 1.2 seconds**.

### 3.2 The Technical vs Behavioral Disconnection
- `[CROSS-PAPER OBSERVATION]` 7 out of 8 interview systems (87.5%) focus exclusively on non-verbal behavioral presentation (eye contact, pitch jitter, smile frequency) or general HR interview questions. They provide zero mechanism to evaluate software programming, algorithmic problem-solving, or mathematical correctness.
- `[AUTHOR-STATED FACT]` Vachkal et al. (P28, IndusAI) demonstrated the feasibility of technical mock interviews by executing candidate code inside an isolated **Docker container sandbox**, running unit tests and parsing Abstract Syntax Trees (ASTs) alongside a Claude-3 conversational interviewer. However, P28 omitted computer vision tracking entirely.

### 3.3 The Anxiety Remediation Paradox (Zhang et al., 2025)
- `[AUTHOR-STATED FACT]` Zhang et al. (P27) proved through physiological Galvanic Skin Response (GSR) tracking that student interview anxiety decreases by **31% across 3 iterative practice sessions**, provided the automated agent employs an empathetic, conversational coaching persona rather than an intimidating, cold evaluative tone.

---

## 4. ScholarCamp / PRIE Unified Mock Interview Architecture

ScholarCamp / PRIE bridges the gap between behavioral coaching and technical code evaluation by engineering a unified multimodal interview agent:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         PRIE MULTIMODAL INTERVIEW ENGINE                         │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Module                   │ Implementation Technology & Literature Grounding      │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 1. Real-Time Vision      │ MediaPipe FaceMesh WebAssembly (P03, P14): Tracking   │
│                          │ eye gaze, blink rate, and AU12 smile ratio at 60 FPS. │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 2. Acoustic Prosody      │ openSMILE real-time C++ stream (P29): Extracting      │
│                          │ pitch (F0), jitter, speaking pace, and hesitation lag.│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 3. Conversational Core   │ Gemini 1.5 Flash via WebRTC (P29) for adaptive,       │
│                          │ empathetic behavioral and technical questioning.      │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 4. Live Coding Sandbox   │ Docker container sandbox (P28) running AST analysis,  │
│                          │ test cases, and algorithmic complexity checks.        │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 5. ATS Resume Grounding  │ Dynamically tailoring interview questions to candidate│
│                          │ resume skills and identified skill deficits (P12, P17)│
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
