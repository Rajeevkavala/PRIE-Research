# Perturbation Stress Testing & Feature Noise Robustness
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Document**: `09_Results/10_Robustness_Results/Perturbation_Stress_Test.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED (SYNTHETIC SIMULATION)  

---

## 1. Objective
To evaluate the resilience of the Placement Predictor ($M_{06}$) against input feature perturbations, Gaussian sensor noise, and missing telemetry records simulating real-world portal deployment conditions.

---

## 2. Perturbation Protocol
Standardized continuous indicators ($F_{01}$ to $F_{16}$) were perturbed with additive zero-mean Gaussian noise:
$$\tilde{x}_j = x_j + \epsilon_j, \quad \epsilon_j \sim \mathcal{N}(0, \sigma_{\text{noise}}^2)$$
for noise levels $\sigma_{\text{noise}} \in \{0.0, 0.05, 0.10, 0.20, 0.30\}$ standard deviations, simulating noisy assessments and incomplete student logs.

---

## 3. Empirical Stress Testing Results

Table 1 reports the degradation profile across increasing feature noise levels ($N=250$, Seed 42):

| Noise Level ($\sigma_{\text{noise}}$) | Classification Accuracy | Macro-F1 | ROC-AUC | Brier Score Loss | ECE | Degradation Severity |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$0.00$ (Clean Baseline)** | **$0.9400$** | **$0.9182$** | **$0.9864$** | **$0.0471$** | **$0.0268$** | **Baseline Reference** |
| **$0.05$ (Mild Portal Jitter)** | $0.9360$ | $0.9130$ | $0.9840$ | $0.0488$ | $0.0285$ | Minimal ($\Delta \text{Acc} = -0.4\%$) |
| **$0.10$ (Moderate Sensor Noise)** | $0.9240$ | $0.8985$ | $0.9782$ | $0.0532$ | $0.0340$ | Tolerable ($\Delta \text{Acc} = -1.6\%$) |
| **$0.20$ (High Telemetry Noise)** | $0.8920$ | $0.8610$ | $0.9590$ | $0.0685$ | $0.0442$ | Moderate ($\Delta \text{Acc} = -4.8\%$) |
| **$0.30$ (Severe Data Corruption)** | $0.8480$ | $0.8120$ | $0.9280$ | $0.0890$ | $0.0620$ | Severe ($\text{ECE} > 0.05$) |

---

## 4. Key Findings
1. **Graceful Performance Degradation**: Under moderate noise ($\sigma = 0.10$, representing typical variability in student platform activity and assessment timing), accuracy remains above $92.4\%$ and ECE remains comfortably below $0.05$ ($0.0340$).
2. **Breakdown Point**: The model breaks the $\text{ECE} \le 0.05$ calibration barrier only when noise reaches $\sigma = 0.30$ (representing extreme random corruption of $30\%$ of feature variance).

---

## 5. Evidence Status
**STATUS: VALIDATED (SYNTHETIC SIMULATION)**  
Empirically tested and derived from `08_Experiments/11_Robustness/Perturbation_Stress_Test.md`.
