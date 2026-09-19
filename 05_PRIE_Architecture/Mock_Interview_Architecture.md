# Mock Interview Architecture: Sub-1.5s Streaming Speech, Client Wasm Vision & Ephemeral Sandboxing (M05)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Mock_Interview_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Mock Interview Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & Conversational Bottlenecks

In automated technical interview coaching, existing prototypes suffer from two debilitating failures identified in Phase 02 (`02_Cross_Analysis/Interview_Comparison.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG5`):
1. **Compounding Latency Bottlenecks**: As documented by **Paper03** (Joshi et al. 2025) and **Paper29** (Srinivasan & Radhakrishnan 2025), sequential cloud API piping (Audio Upload $\to$ Cloud Whisper $\to$ GPT-4 $\to$ Cloud TTS) incurs turn-taking delays of **2.8 to 4.2 seconds**. This breaks conversational cadence, creates awkward silences, and induces severe candidate anxiety.
2. **Absent Objective Code Sandboxing**: Automated mock interview tools evaluate coding ability via superficial text regexes or unisolated server `exec()` calls, creating massive host security vulnerabilities while failing to validate actual test-case coverage (**Paper28**).
3. **Biometric Privacy Liabilities**: Streaming raw candidate video to centralized servers exposes student facial biometrics to severe regulatory and data breach risks under POPIA and FERPA (**Paper02**).

PRIE overcomes these limitations through a **Low-Latency Streaming Speech, Client-Side Wasm Vision, and Ephemeral Docker Sandbox Architecture** (`DD-005`, `DD-006`, `M05`).

---

## 2. Mock Interview Subsystem Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. CLIENT BROWSER PERCEPTION LAYER (WebAssembly & Audio Worklet)       │
│ • Local Webcam Stream -> MediaPipe FaceMesh compiled to Wasm (30 FPS)  │
│ • Extracts 468 3D Landmarks Locally: Gaze Stability, Blink Rate, Tilt │
│ • Audio Worklet: Captures Microphone Audio in 250ms Opus Chunks        │
│ • ZERO RAW VIDEO FRAMES TRANSMITTED TO SERVER (DD-005, DD-011)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ WebSocket (WSS) Audio Chunks & Telemetry
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. STREAMING SPEECH & DIALOGUE BACKEND (Sub-1.5s Voice Pipeline)       │
│ • Chunked Whisper ASR with Silero VAD (Voice Activity Detection)       │
│ • Generates Real-Time Transcript with Word Timestamps                  │
│ • Dispatches Context to Local Quantized Llama-3-8B-Instruct (via vLLM) │
│ • Streams Synthesized Response via Fast Lightweight Local TTS Engine   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
┌───────────────────────────────────────┐   ┌────────────────────────────┐
│ 3. LIVE CODE EXECUTION SANDBOX        │   │ 4. MULTIMODAL EVALUATOR    │
│ • Ephemeral Docker Micro-Containers   │   │ • Acoustic: Pause Ratio,   │
│ • Strict Limits: 128MB RAM, 0.5 CPU   │   │   Filler Disfluency Count  │
│ • Disabled Networking (--net=none)    │   │ • Semantic: Technical Depth│
│ • 5.0s Timeout Termination (DD-006)   │   │ • Visual: Composure Index  │
└───────────────────┬───────────────────┘   └─────────────┬──────────────┘
                    │                                     │
                    └───────────────────┬─────────────────┘
                                        ▼
                   ┌─────────────────────────────────────────┐
                   │ Subsystem Outputs to PRIE Ecosystem     │
                   │ • F06: programming_score (Unit Tests)   │
                   │ • F08: soft_skills_score (Communication)│
                   │ • F20: behavior_score (Composure Index) │
                   │ • Actionable Feedback to M12 & Student  │
                   └─────────────────────────────────────────┘
```

---

## 3. Sub-1.5s Voice-to-Voice Latency Budget

To achieve natural conversational turn-taking, the voice interaction loop is engineered to strictly satisfy the sub-1.5s latency budget:

```
[Candidate Stops Speaking]
       │
       ├─► 1. Silero Voice Activity Detection (VAD) Confirms End-of-Turn:  ~150 ms
       ├─► 2. Final Chunk Whisper ASR Transcription (whisper.cpp):        ~250 ms
       ├─► 3. Prompt Construction & vLLM First Token Generation (TTFT):   ~320 ms
       ├─► 4. Local FastTTS Audio Synthesis of First Sentence:            ~280 ms
       └─► 5. Audio Buffer Streaming to Browser & Playback Start:          ~120 ms
──────────────────────────────────────────────────────────────────────────────────
TOTAL VOICE-TO-VOICE TURN-TAKING LATENCY:                                  ~1,120 ms
                                                         (Well within < 1,500 ms SLA)
```

**Optimization Principles**:
- **Chunked Audio Streaming**: Audio is streamed continuously in 250ms chunks; transcription occurs incrementally in a circular ring buffer rather than waiting for the entire utterance to finish.
- **Speculative Streaming**: TTS generation starts on the first generated sentence boundary (`.` or `?`) rather than waiting for full LLM completion.

---

## 4. Client-Side Vision & Zero-Trust Biometric Privacy

In strict compliance with **`DD-005`** and **`DD-011`**:
- The candidate's video stream is **never transmitted over the network**.
- `MediaPipe FaceMesh` executes locally within the candidate's browser via Google Chrome / Firefox WebAssembly (Wasm) runtime, leveraging local GPU/CPU hardware acceleration at 30 frames per second.
- **Computed Telemetry Scalars**: The client script extracts and transmits only five scalar numbers per interview turn:
  1. `gaze_stability_index`: Standard deviation of iris center coordinates relative to screen bounding box.
  2. `blink_rate_cpm`: Blinks per minute detected via eye aspect ratio (EAR).
  3. `head_pose_yaw_pitch_variance`: Degree of head movement/nodding stability.
  4. `speech_pause_ratio`: Proportion of turn duration spent in pauses $>1.2$s.
  5. `filler_word_frequency`: Count of verbal disfluencies ("um", "uh", "like", "you know") per 100 spoken words.
- These scalars are synthesized into `F20: behavior_score` and `F08: soft_skills_score`.

---

## 5. Ephemeral Docker Sandbox Execution Architecture

To evaluate practical programming competency objectively during technical interview coding rounds (`DD-006`):
- **Container Provisioning**: Upon question presentation, PRIE pre-warms a pool of isolated Linux micro-containers based on alpine-python / alpine-java images.
- **Hard Resource Quotas**:
  ```bash
  docker run --rm \
    --net=none \
    --memory=128m \
    --cpus=0.5 \
    --pids-limit=64 \
    --read-only \
    --user=sandboxuser \
    --volume /tmp/candidate_code:/code:ro \
    prie-sandbox-runner:latest pytest /tests/test_suite.py
  ```
- **Execution Safeguards**:
  - `--net=none`: Completely disables network interfaces, preventing malicious code from establishing socket connections or downloading malware.
  - Non-root execution: Prevents privilege escalation attacks on the host server.
  - Read-only root filesystem: Prevents disk tampering or persistent state pollution.
  - Strict 5.0-second timeout: Automatically kills infinite loops or fork bombs.
- **Outputs**: Generates unit test pass count, memory consumption, execution time, and stdout/stderr traces feeding `F06: programming_score`.

---

## 6. Candidate Model Portfolio & Scientific Controls

| Model Component | Role in Interview | Literature Grounding | Engineering Rationale | Experimental Validation Target |
|:---|:---|:---|:---|:---|
| **Whisper ASR (Streaming)** | Speech-to-Text Transcription | **Paper29** ($\text{WER} = 6.2\%$) | Superior accuracy across accented Indian student speech | Word Error Rate $\le 8.0\%$ across noisy backgrounds |
| **MediaPipe FaceMesh (Wasm)** | Non-Verbal Composure | **Paper15, Paper30** | Zero server GPU compute; absolute biometric privacy | Pearson $r \ge 0.70$ with panel ratings (`EXP-2`) |
| **Quantized Llama-3-8B / vLLM** | Conversational Questioner | **Paper03, Paper27** | First-token latency $<350$ms; local on-premise execution | Technical question relevance $\ge 90\%$ |
| **Sequential Cloud API (Baseline)**| Cloud API Baseline | **Paper03** | Standard status-quo pipeline (OpenAI API + ElevenLabs) | Benchmark control to prove sub-1.5s latency uplift |
| **Human Expert Recruiter Panel**| Golden Evaluation Standard | **Paper14, Paper38** | Blinded evaluation by 5 enterprise technical recruiters | Golden standard for calibrating PRIE composite score |

---

## 7. Experimental Validation Plan Linkage

The interview architecture is directly evaluated under **`EXP-2`** (`Experimental_Decisions.md`):
- **Hypothesis H2**: A streaming chunked conversational pipeline achieves sub-1.5s voice-to-voice turn-taking latency while maintaining a high positive Pearson correlation ($r \ge 0.70, p < 0.001$) with blinded human recruiter interview panel ratings.
- **Experimental Protocol**: 50 live mock technical interview sessions with graduating engineering seniors; measure end-to-end turn-taking latency and inter-rater reliability with a panel of 5 senior technical recruiters across technical accuracy, communication clarity, and behavioral composure.
