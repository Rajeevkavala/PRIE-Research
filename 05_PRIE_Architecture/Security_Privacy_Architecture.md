# Security & Privacy Architecture: Zero-Trust Governance & Differential Privacy (DD-011)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Security_Privacy_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Security & Privacy Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & Educational Privacy Imperative

Higher education career preparation platforms manage exceptionally sensitive candidate data:
- Academic transcripts and GPA histories.
- Personal resumes containing contact details, physical locations, and demographic signals.
- Facial and vocal paralinguistic biometrics during mock interview practice.

As established in Phase 02 (`02_Cross_Analysis/Limitation_Matrix.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG8`):
- **41 out of 44** reviewed systems operate without formal privacy architectures, storing plaintext student data in unencrypted databases.
- Storing video recordings of student mock interviews exposes institutions to severe candidate biometric liabilities under modern data privacy regulations (**Paper02**: Villegas-Chanaluisa et al. 2025).

PRIE enforces a **Zero-Trust Security & Differential Privacy Architecture** (`DD-011`), guaranteeing candidate confidentiality, secure code execution, and regulatory compliance.

> **Compliance Disclaimer**:
> This document specifies architectural and mathematical privacy controls. Final formal legal certification under specific regional statutes (e.g., GDPR, FERPA, POPIA, India DPDP Act 2023) *requires institutional legal and compliance verification prior to production rollout*.

---

## 2. Multi-Layered Security & Privacy Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. PERIMETER & IDENTITY BOUNDARY                                       │
│ • TLS 1.3 Transport Encryption & Strict HSTS                           │
│ • Asymmetric JWT Authentication with Ed25519 Cryptographic Signatures │
│ • Role-Based Access Control (RBAC): Student, Faculty, Recruiter, Admin │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Validated Request + Identity Context
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. BIOMETRIC & PERCEPTUAL ZERO-TRUST PRIVACY (DD-005, DD-011)          │
│ • Client Browser Wasm Perceiver: MediaPipe FaceMesh runs locally       │
│ • ZERO RAW VIDEO FRAMES TRANSMITTED TO CENTRAL SERVERS                 │
│ • In-Memory Audio Processing: Whisper audio chunks discarded post-turn │
│ • ZERO STORAGE OF RAW STUDENT AUDIO / VIDEO RECORDINGS                 │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Numeric Telemetry Only
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. CODE SANDBOX ISOLATION PERIMETER (DD-006)                           │
│ • Ephemeral Docker Micro-Containers with Linux cgroup isolation        │
│ • Disabled Networking (--net=none) & Non-Root Execution (--user)       │
│ • Read-Only Root Filesystem & Strict 5.0s Timeout Termination          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Execution Status Only
┌───────────────────────────────────▼────────────────────────────────────┐
│ 4. DIFFERENTIAL PRIVACY ANALYTICS PROXY (CMP-GW-PRIV)                  │
│ • Intercepts Recruiter / TPO Aggregate Cohort Queries                  │
│ • Enforces Privacy Budget Epsilon <= 1.0 (Laplace Mechanism)           │
│ • Prevents Membership Inference & Re-Identification Attacks            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Anonymized & Noised Outputs
┌───────────────────────────────────▼────────────────────────────────────┐
│ 5. DATA AT REST & CRYPTOGRAPHIC LEDGER                                 │
│ • Database Column-Level Encryption (AES-256-GCM) for PII               │
│ • Immutable, Append-Only Cryptographic Audit Log                       │
│ • Automated Data Retention & Erasure Protocols                         │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Mathematical Differential Privacy Framework (`DD-011`)

When corporate placement officers or external company recruiters query the PRIE ecosystem to inspect candidate readiness distributions (e.g., *"How many students have DSA > 80% and CGPA > 8.0?"*), the system must prevent **Membership Inference Attacks** where an adversary reconstructs an individual student's profile.

### 3.1 The Laplace Mechanism Formulation
PRIE implements $\epsilon$-Differential Privacy via the **Laplace Mechanism**:
$$\mathcal{M}(D) = f(D) + \text{Lap}\left( \frac{\Delta f}{\epsilon} \right)$$
where:
- $f(D)$ is the true aggregate analytical query on dataset $D$ (e.g., candidate count or mean score).
- $\Delta f$ is the $L_1$ global sensitivity of the query function:
  $$\Delta f = \max_{D, D': \|D - D'\|_1 = 1} \|f(D) - f(D')\|_1$$
  For count queries, $\Delta f = 1.0$; for mean scores bounded in $[0, 1]$, $\Delta f = \frac{1}{N}$.
- $\epsilon$ is the privacy budget parameter, strictly configured to:
  $$\epsilon \le 1.0$$
- $\text{Lap}(b)$ draws random noise from the zero-mean Laplace distribution with scale $b = \frac{\Delta f}{\epsilon}$:
  $$p(z) = \frac{1}{2b} \exp\left( -\frac{|z|}{b} \right)$$

### 3.2 Privacy Budget Accounting & Composition
- The privacy proxy (`CMP-GW-PRIV`) tracks cumulative $\epsilon$-consumption across each institutional cohort using the **Advanced Composition Theorem**:
  $$\epsilon_{\text{total}} = \sum_{k=1}^m \epsilon_k$$
- If cumulative queries against a specific small candidate pool ($N < 20$) exhaust $\epsilon_{\text{total}} > 1.0$, further granular filtering is blocked to prevent reconstruction attacks.

---

## 4. Biometric & Interview Privacy Standards (`DD-005`)

To protect student biometric identity during mock technical interviews:
1. **Zero Video Uplink**: Video streams from the webcam are piped directly into an in-browser HTML5 `<canvas>` element. The JavaScript WebAssembly wrapper executes `MediaPipe FaceMesh` locally. The raw video buffer is immediately garbage collected.
2. **Ephemeral Audio Buffers**: Candidate audio streamed over WebSocket is held in an encrypted, volatile in-memory ring buffer strictly for the duration of the transcription turn. Once Whisper produces the text transcript, the audio buffer is zeroed out (`memset`).
3. **No Biometric Identification**: PRIE stores only derived behavioral indices (`speech_pause_ratio`, `filler_frequency`, `gaze_stability_index`). At no point does the system store facial feature vectors, voice embeddings, or biometric templates.

---

## 5. Sandboxed Code Execution Security (`DD-006`)

To prevent candidate code submissions from compromising the server infrastructure:
- Every code execution request provisions an ephemeral, isolated Docker container:
  ```bash
  docker run --rm \
    --net=none \
    --memory=128m \
    --cpus=0.5 \
    --pids-limit=64 \
    --read-only \
    --tmpfs /tmp:rw,noexec,nosuid,size=16m \
    --user=sandboxuser \
    --volume /tmp/code_run_8812:/workspace:ro \
    prie-sandbox-runner:latest pytest /tests/test_suite.py
  ```
- **Host Protection Guarantees**:
  - Zero outbound/inbound network connectivity (`--net=none`).
  - Read-only root filesystem prevents writing malicious binaries to the host.
  - Process limits (`--pids-limit=64`) prevent fork bomb Denial-of-Service attacks.
  - Memory caps (128MB) prevent out-of-memory host crashes.
  - 5.0-second SIGKILL watchdog automatically terminates infinite loops.

---

## 6. Access Control & Encryption Standards

| Data Domain | At-Rest Protection | In-Transit Protection | Access Control Scopes |
|:---|:---|:---|:---|
| **Student Credentials & Auth** | Argon2id Password Hashing | TLS 1.3 (ChaCha20 / AES-GCM) | System Authenticator Only |
| **Academic Records (SIS)** | AES-256-GCM Column Encryption| Internal TLS Mutual Auth | `student:read`, `faculty:read` |
| **Resume Documents (PDFs)** | AES-256 Envelope Encryption | TLS 1.3 HTTPS Upload | `student:owner`, `ats:worker` |
| **SPV Feature Vectors** | TimescaleDB Column Encryption | Internal gRPC TLS | `prie:internal:engine` |
| **Recruiter Analytics** | Noisy Aggregate Views | TLS 1.3 REST API | `recruiter:read` (Guarded by DP) |
| **Audit Logs** | SHA-256 Hash Chaining | TLS 1.3 Append-Only | `admin:audit:read` |
