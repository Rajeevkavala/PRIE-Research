# Synthetic Data Methodology: Gaussian Copula Generation, Marginal Matching & Simulation Limits

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Synthetic_Data_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Synthetic Data Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Scientific Justification & Mandatory Epistemological Limit

In strict compliance with the Phase 06 Master Execution Directives and `DD-012`:

> [!CAUTION]
> **MANDATORY SCIENTIFIC RULE: SYNTHETIC DATA IS NOT EMPIRICAL PROOF**  
> Synthetic data (`DS-SYNTH-01`) is engineered exclusively for **computational stress-testing**, **pipeline throughput profiling**, **XAI convergence auditing**, and **pre-deployment baseline calibration**.  
> **Under no circumstances shall synthetic data be presented as real-world empirical evidence of student capability, nor shall external validity or clinical predictive superiority be claimed based on synthetic cohorts alone.**

Synthetic cohorts are scientifically necessary prior to Phase 08 for three reasons:
1. **Pre-Deployment Stress-Testing**: Validating that all 12 modules (`M01`–`M12`) handle multimodal inputs at scale without schema exceptions or deadlocks.
2. **Algorithmic Convergence Auditing**: Verifying that DiCE counterfactual optimization and TreeSHAP explainer kernels converge reliably within bounded latency constraints.
3. **Class Imbalance Simulation**: Evaluating how predictive models behave under simulated corporate selection ratios (e.g., highly selective 15% placement cutoffs).

---

## 2. Gaussian Copula Generation Mechanics

To avoid simplistic, independent random variable generation (which destroys realistic inter-skill correlations), `DS-SYNTH-01` is generated using **Gaussian Copulas** parameterized by empirical educational literature distributions (`DD-012`):

### 2.1 Mathematical Formulation
By Sklar's Theorem, any multivariate cumulative distribution function $F(x_1, \dots, x_d)$ can be expressed in terms of its marginal distributions $F_i(x_i)$ and a copula $C$:
$$F(x_1, x_2, \dots, x_{22}) = C\Big( F_1(x_1), F_2(x_2), \dots, F_{22}(x_{22}) \Big)$$

For the Gaussian copula:
$$C_{\mathbf{R}}^{	ext{Gauss}}(u_1, \dots, u_{22}) = \Phi_{\mathbf{R}}\Big( \Phi^{-1}(u_1), \Phi^{-1}(u_2), \dots, \Phi^{-1}(u_{22}) \Big)$$
where:
- $\Phi^{-1}$ is the inverse cumulative distribution function of a standard univariate normal distribution.
- $\Phi_{\mathbf{R}}$ is the joint cumulative distribution function of a multivariate normal distribution with mean vector $\mathbf{0}$ and correlation matrix $\mathbf{R} \in \mathbb{R}^{22 	imes 22}$.

---

## 3. Preserved Empirical Correlation Matrix ($\mathbf{R}$)

The correlation matrix $\mathbf{R}$ enforces documented academic relationships recovered from the Phase 01 corpus:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                SYNTHETIC SPV CORRELATION STRUCTURE (SAMPLE ROWS)                 │
├──────────────────┬───────┬───────────┬────────────┬────────────┬────────────────┤
│ Feature Pair     │ CGPA  │ DSA Score │ Proj Qual  │ Gap Score  │ Placement Prob │
├──────────────────┼───────┼───────────┼────────────┼────────────┼────────────────┤
│ F01 (CGPA)       │  1.00 │   +0.68   │   +0.42    │   -0.58    │     +0.72      │
│ F02 (DSA Score)  │ +0.68 │    1.00   │   +0.61    │   -0.74    │     +0.81      │
│ F10 (Proj Qual)  │ +0.42 │   +0.61   │    1.00    │   -0.63    │     +0.65      │
│ F15 (Gap Score)  │ -0.58 │   -0.74   │   -0.63    │    1.00    │     -0.79      │
│ F16 (Consistency)│ +0.38 │   +0.52   │   +0.48    │   -0.55    │     +0.58      │
└──────────────────┴───────┴───────────┴────────────┴────────────┴────────────────┘
```

---

## 4. Marginal Distribution Parameterization

Continuous and discrete features are fitted to established parametric distributions:
1. **Academic Features (`F01` to `F07`)**: Truncated Normal distributions $\mathcal{TN}(\mu, \sigma^2, a, b)$ fitted to historical engineering exam percentiles (e.g., $	ext{CGPA} \sim \mathcal{TN}(7.2, 1.1^2, 4.0, 10.0)$).
2. **Project & Certification Counts (`F09`, `F12`)**: Poisson distributions $	ext{Pois}(\lambda)$ modeling discrete counts ($\lambda_{	ext{proj}} = 2.4, \lambda_{	ext{cert}} = 1.2$).
3. **Binary Indicators (`F11`)**: Bernoulli distributions $	ext{Bern}(p)$ where $p = 0.38$ reflects historical corporate internship participation rates.
4. **Behavioral Telemetry (`F16`, `F21`)**: Beta distributions $	ext{Beta}(lpha, eta)$ bounded strictly in $[0.0, 1.0]$.

---

## 5. Noise Injection & Controlled Missingness

To simulate realistic institutional data messiness:
1. **Gaussian Noise**: Additive zero-mean Gaussian noise $\epsilon \sim \mathcal{N}(0, 0.05^2)$ is added to continuous scores.
2. **Missing Completely at Random (MCAR)**: An 8% missingness mask is injected into secondary features (`F12` Certifications, `F20` Behavior Score) to evaluate MICE imputation robustness.
3. **Reproducibility Guarantee**: The generation script uses a fixed global seed (`RNG_SEED = 42`) and is serialized in `06_Methodology/Synthetic_Data_Methodology.md` for deterministic re-generation.
