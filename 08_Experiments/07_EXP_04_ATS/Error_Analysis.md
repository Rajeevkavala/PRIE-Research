# EXP-04 Resume Extraction Failure Mode Analysis
1. **Horizontal Interleaving**: Linear parsers concatenate left-column "Skills" with right-column "Project Description" text.
2. **Bounding Box Mitigation**: PyMuPDF column boundary sorting clusters text blocks by horizontal $x$-intervals before vertical $y$-ordering, eliminating cross-column interleaving.
