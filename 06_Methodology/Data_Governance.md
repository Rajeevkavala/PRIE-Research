# Data Governance: Privacy Engineering, Ethical Compliance & Regulatory Architecture

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Data_Governance.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Data Governance Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Governance Scope & Regulatory Mandate

Higher education predictive systems handle highly sensitive student records, personal resumes, and behavioral telemetry. In accordance with the Protection of Personal Information Act (POPIA), Family Educational Rights and Privacy Act (FERPA), and IEEE ethically aligned design standards (`DD-011`, `RG8`), PRIE implements an institutional data governance protocol:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          DATA GOVERNANCE ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│  1. ZERO-TRUST ANONYMIZATION                                                    │
│     • Primary identifiers (Name, Roll No, Email) replaced with UUID v5          │
│     • Hash-based pseudonyms salted with institutional secret keys               │
│                                                                                 │
│  2. DIFFERENTIAL PRIVACY (DP) ENGINE                                            │
│     • Laplace noise mechanism applied to institutional cohort analytics         │
│     • Strict privacy budget constraint: Epsilon <= 1.0, Delta <= 1e-5           │
│                                                                                 │
│  3. ZERO RAW BIOMETRIC RETENTION                                                │
│     • Audio destroyed immediately post-transcription (in-memory buffer only)    │
│     • Video processed strictly in-browser via Wasm (zero video transmission)   │
│                                                                                 │
│  4. CRYPTOGRAPHIC ACCESS & RETENTION AUDITING                                   │
│     • Role-Based Access Control (RBAC) with cryptographic JWT verification      │
│     • Automated data sunsetting: telemetry purged 180 days post-graduation      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Identity De-Identification & Pseudonymization

To eliminate re-identification risks while maintaining longitudinal relational consistency across research datasets:
1. **Deterministic Salted Hashing**: Direct student identifiers (Roll Number, University Email, National ID) are irreversibly pseudonymized:
   $$	ext{Student\_UUID} = 	ext{HMAC-SHA256}(	ext{Raw\_Roll\_Number}, 	ext{Secret\_Institutional\_Salt})$$
2. **Resume Scrubbing**: During document parsing (`M02`), a dedicated pre-filter identifies and masks candidate phone numbers, personal email addresses, street addresses, and photo bounding boxes prior to semantic feature extraction.
3. **Lookup Table Isolation**: The de-identification lookup dictionary is stored on an air-gapped institutional server managed exclusively by the university registrar, completely segregated from the PRIE analytics datastore.

---

## 3. Mathematical Differential Privacy Framework (`DD-011`)

When corporate placement officers or academic deans query aggregate cohort analytics (e.g., departmental skill distributions, cohort placement probability curves), queries pass through the **PRIE Differential Privacy Proxy**:

$$\mathcal{M}(\mathbf{x}) = f(\mathbf{x}) + 	ext{Lap}\left(rac{\Delta f}{\epsilon}ight)$$
where:
- $f(\mathbf{x})$ is the true cohort statistical function (e.g., mean readiness score).
- $\Delta f$ is the global sensitivity of function $f$, defined as:
  $$\Delta f = \max_{\|\mathbf{x} - \mathbf{x}'\|_1 = 1} |f(\mathbf{x}) - f(\mathbf{x}')|$$
- $\epsilon \le 1.0$ is the strictly enforced privacy loss budget parameter.
- $\delta \le 10^{-5}$ represents the probability of privacy compromise.

This mathematical bound guarantees that the presence or absence of any individual student in the training cohort cannot be inferred from published placement statistics.

---

## 4. Role-Based Access Control (RBAC) & Stakeholder Boundaries

Data access permissions are strictly segregated across the three triangular stakeholder roles (`DD-010`):

| Data Class | Student Candidate | Faculty Mentor | Corporate Placement Cell |
| :--- | :---: | :---: | :---: |
| **Personal 22-Dim SPV** | Full Read | Full Read (Advisees only) | Differentially Private Aggregate |
| **Mock Interview Video Landmarks** | Full Read | Composite Score Only | Redacted (Behavior score only) |
| **Code Execution Sandboxes** | Full Read/Write | Read Test Logs | Pass Rate Only |
| **Detailed Resume Text** | Full Read/Write | Full Read | Anonymized Parsed Skills |
| **DiCE Counterfactual Remediation** | Personalized View | Mentorship Guide | Role Requirement Thresholds |
| **Cohort Placement Probability** | Restricted (Self) | Departmental View | Search & Filter Matrix |

---

## 5. Data Retention, Sunsetting & Student Rights

1. **Right to Forgotten / Data Deletion**: Students retain the autonomous right to request complete data deletion via the ScholarCamp user settings. Upon invocation, the student's SPV record, diagnostic histories, and resume embeddings are hard-deleted within 72 hours.
2. **Automatic Data Sunsetting**: All detailed behavioral telemetry (clickstream logs, interview landmark sequences) is scheduled for automated deletion 180 days after formal university graduation.
3. **Research Dataset Provenance**: All datasets used in experimental evaluations (`DS-BENCH-01`, `DS-BENCH-02`, `DS-CORPUS-01`, `DS-SYNTH-01`) are version-controlled using Git LFS and DVC (Data Version Control), with SHA-256 integrity hashes stored in `Dataset_Design.md`.
