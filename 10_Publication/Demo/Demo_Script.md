# PRIE Interactive Research Demo Script

1. **Step 1: Student Onboarding**
   - Ingest candidate profile (CGPA: 7.8, Branch: Computer Science).
   - Upload sample technical resume.
2. **Step 2: Vector Assembly**
   - Demonstrate real-time assembly of the 22-D Student Profile Vector.
3. **Step 3: Prediction & TreeSHAP Waterfall**
   - Execute XGBoost prediction: $P(\text{placed}) = 0.68$, Composite PRS = 71.4.
   - Render interactive SHAP waterfall plot isolating top negative driver (`dsa_score` = 45%).
4. **Step 4: Closed-Loop Remediation**
   - System automatically generates a 4-week prerequisite-aware study roadmap targeting Trees, Heaps, and Dynamic Programming.
5. **Step 5: Voice Mock Interview**
   - Candidate completes 3-question voice interview; Whisper ASR transcribes and computes cadence and semantic relevance.
