# Domain Shift & Population Discrepancy Analysis
1. **Public Benchmarks vs Proposed Target**:
   - `DS-BENCH-01` ($N=215$) reflects MBA/BBA business graduates rather than technical software engineers.
   - `DS-BENCH-02` (OULAD, $N=32,593$) reflects UK distance-learning adults, not full-time Indian engineering undergraduates.
2. **Transfer Limitations**:
   - Classifiers trained on distance-learning clickstreams cannot directly predict campus placement conversion without re-calibration.
   - PRIE uses `DS-BENCH-02` strictly for evaluating temporal sequence modeling architecture (TFT), not as final placement truth.
