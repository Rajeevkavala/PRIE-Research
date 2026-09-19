# Formal Hypothesis Testing Results Ledger

| Test ID | Models Compared | Formal Statistical Test | Test Statistic | p-value | Alpha Level | Significance | Supported Hypothesis |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **ST-01** | XGBoost vs Random Forest | McNemar's Test (Continuity Corrected) | $\chi^2 = 5.8824$ | $0.0153$ | $0.05$ | Significant | $H_1$ Supported |
| **ST-02** | XGBoost vs Logistic Regression | McNemar's Test (Continuity Corrected) | $\chi^2 = 9.6000$ | $0.0019$ | $0.01$ | Significant | $H_1$ Supported |
| **ST-03** | XGBoost vs Random Forest | Wilcoxon Signed-Rank Test | $W = 27.0$ | $0.0076$ | $0.01$ | Significant | $H_1$ Supported |
| **ST-04** | Multimodal vs Unimodal Video | Paired Student's $t$-test | $t = 9.88$ | $0.0022$ | $0.01$ | Significant | $H_2$ Supported |
| **ST-05** | Kahn vs Random Scheduling | Wilcoxon Signed-Rank Test | $W = 0.0$ | $0.0416$ | $0.05$ | Significant | $H_6$ Supported |
