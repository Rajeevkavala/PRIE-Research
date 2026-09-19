# Paper 11 — Web Scraping for Job Listings Using Python and BeautifulSoup

## 1. Bibliographic Information

- **Paper ID**: Paper11
- **Full Title**: Web Scraping for Job Listings Using Python and BeautifulSoup
- **Authors**: Dr Reeta Mishra (IILM University, Knowledge Park II, Greater Noida, Uttar Pradesh, India)
- **Year**: 2025 (Submission: 22-08-2025, Acceptance: 26-08-2025, Publication: 01-09-2025)
- **Venue**: Scientific Journal of Artificial Intelligence and Blockchain Technologies (SJAIBT), Vol. 2, Issue 3, pp. 63–70
- **ISSN**: 3049-4389
- **DOI**: 10.63345/sjaibt.v2.i3.308
- **PDF filename**: `Paper11_consortium2025resume.pdf`
- **PDF path**: `Papers/PDFs/Paper11_consortium2025resume.pdf`
- **Page count**: 8 pages (pp. 63–70)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper11_consortium2025resume.bib`) listed a synthetic title ("Resume Parser and Auto-Formatter Using NLP") and synthetic author ("Academic Engineering Consortium"). Inspection of the actual PDF confirms the true paper is Dr Reeta Mishra's 2025 empirical study on web scraping job listings using Python and BeautifulSoup.

---

## 2. Research Problem

The paper addresses the challenge of acquiring, structuring, and analyzing massive daily volumes of online job listings across global and specialized recruitment portals. Manual data collection methods (such as manually copying postings into spreadsheets) are labor-intensive, slow, inconsistent, and highly error-prone (exhibiting high error margins), which restricts large-scale, real-time labor market analysis and workforce trend forecasting in rapidly changing employment environments.

### Source Evidence
- **PDF Page**: Page 1 (p. 63), Abstract & Page 2 (p. 64), Section "INTRODUCTION".

---

## 3. Research Objectives

1. Develop an automated, scalable, and reproducible workflow using Python and BeautifulSoup to extract online job postings.
2. Formulate a structured extraction pipeline spanning HTTP requests, DOM navigation, text cleaning, and tabular CSV data export.
3. Conduct a controlled statistical benchmark comparing manual data collection against automated web scraping in terms of extraction speed, accuracy, and error rates.
4. Address legal and ethical considerations in automated labor market scraping (e.g., `robots.txt` compliance, rate limiting).

### Source Evidence
- **PDF Page**: Page 1 (p. 63), Abstract; Page 3 (p. 65), Section "INTRODUCTION".

---

## 4. Research Questions

Not explicitly reported by the author in question format. The study is formulated around empirical validation objectives and efficiency benchmarking.

---

## 5. Dataset

- **Dataset Name**: Online Job Listings Extraction Benchmark
- **Dataset Source**: Public online job listing portal (reputable job board selected for structured HTML and public accessibility)
- **Institution**: IILM University, Greater Noida, India
- **Collection Period**: August 2025
- **Dataset Size**: 500 job postings
- **Number of Samples**: 500 listings
- **Target Fields**: Job title, company name, location, salary range, posting date
- **Data Type**: Semi-structured HTML web pages
- **Real / Synthetic**: Real-world job postings
- **Public / Private**: Publicly accessible web portal without authentication barriers
- **Train / Test Split**: N/A (Comparative data extraction benchmark, not supervised classification)

### Source Evidence
- **PDF Page**: Page 4 (p. 66), Section "STATISTICAL ANALYSIS" & Page 5 (p. 67), Section "METHODOLOGY — Data Source Selection".

---

## 6. Features

The extracted data entities from the target DOM tree include:

### Resume / Job Market Entities
- **Job Title**: Text extracted from header elements (`<h2>`, `job-card` title)
- **Company Name**: Text extracted from company division containers (`<div class="company">`)
- **Location**: Geographic placement or remote status (`<div class="location">`)
- **Salary Information**: Offered compensation or hourly rate (where reported)
- **Posting Date**: Date of publication on the job portal
- **Job Description / Requirements**: Skill prerequisites and role summaries

### Source Evidence
- **PDF Page**: Page 6 (p. 68), Section "METHODOLOGY — Workflow Steps" and code snippet; Page 7 (p. 69), Section "RESULTS".

---

## 7. Data Preprocessing

The author implements a four-step pipeline:
1. **HTTP Request Fetching**: Sending GET requests using Python `requests` with standard user-agent configurations.
2. **HTML Parsing & DOM Navigation**: Parsing raw HTML response strings into DOM tree nodes using `BeautifulSoup(response.text, 'html.parser')`.
3. **Data Cleaning & Normalization**:
   - Stripping surrounding whitespace (`.strip()`).
   - Removal of non-standard characters and unescaped HTML entities.
   - Filtering incomplete HTML tags and empty field containers.
4. **Structured Tabular Formatting**: Exporting parsed arrays into a pandas DataFrame (`pd.DataFrame`) and serializing to CSV format (`job_listings.csv`).

### Source Evidence
- **PDF Page**: Page 6 (p. 68), Section "METHODOLOGY — Workflow Steps", Steps 1–4.

---

## 8. Algorithms and Models

- **HTML Parsing Engine**: BeautifulSoup4 (`bs4`) with standard Python HTML parser.
- **HTTP Transport Layer**: Python `Requests` library.
- **Data Structuring / Transformation**: Pandas DataFrame processing.
- **Pagination Handler**: Iterative loop structure (`for page in range(1, 6):`) parameterizing URL query strings (`?page={page}`).

### Source Evidence
- **PDF Page**: Pages 5–7 (pp. 67–69), Section "METHODOLOGY — Tools and Libraries" and Python code block.

---

## 9. Architecture

The paper depicts a multi-stage web scraping architecture:
- **Target Web Layer**: Online Recruitment Portals / Job Boards.
- **Acquisition Engine**: Python Request Client fetching HTML documents.
- **Parsing & Extraction Engine**: BeautifulSoup DOM parser traversing CSS classes and tag identifiers.
- **Transformation Pipeline**: Data cleaning, text sanitization, and structured mapping.
- **Storage & Analytics Layer**: Pandas DataFrame export to CSV for labor market intelligence and recruitment analytics.

### Source Evidence
- **PDF Page**: Page 2 (p. 64), Figure 1 ("Web Scraping"); Page 6 (p. 68), Section "Workflow Steps".

---

## 10. Methodology

1. **Target Selection**: Selection of an open recruitment portal with high update frequency and clear HTML tags.
2. **Scraper Implementation**: Writing modular Python functions to request, parse, clean, and store 500 job postings.
3. **Manual Baseline Execution**: Human operator manually recording identical fields for 500 postings into spreadsheets.
4. **Benchmarking Comparison**: Measuring total elapsed time (minutes), data accuracy (percentage of perfectly matched fields), and error margin (percentage of corrupted or omitted fields).
5. **Statistical Verification**: Calculating speed improvement ratios and error margin differences.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 66–68), Sections "STATISTICAL ANALYSIS" and "METHODOLOGY".

---

## 11. Experimental Setup

- **Hardware**: Standard workstation (not further detailed).
- **Software**: Python 3.10.
- **Key Libraries**: `beautifulsoup4`, `requests`, `pandas`.
- **Target Sample Size**: 500 job postings.
- **Comparative Baseline**: Manual copy-paste entry by human evaluators.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 66–68).

---

## 12. Evaluation Metrics

- **Extraction Time**: Total duration in minutes required to collect 500 complete listings.
- **Extraction Accuracy (%)**: Percentage of collected listings matching true web page content without missing or distorted tokens.
- **Error Margin (%)**: Percentage of erroneous, incomplete, or misplaced data points.
- **Speed Improvement Ratio**: Percentage reduction in data collection time.

### Source Evidence
- **PDF Page**: Page 4 (p. 66), Section "STATISTICAL ANALYSIS" table and Page 5 (p. 67), interpretation.

---

## 13. Results

### Comparative Statistical Analysis Table (PDF p. 4, p. 66)

| Method | Total Listings Collected | Time Taken (minutes) | Accuracy (%) | Error Margin (%) |
|:---|:---:|:---:|:---:|:---:|
| **Manual Collection** | 500 | 250 | 94.2% | 5.8% |
| **Automated Scraping (BeautifulSoup)** | 500 | 16 | 98.3% | 1.7% |

### Key Experimental Findings
- **Speed Gain**: Time reduced from 250 minutes to 16 minutes—a **93.6% reduction** in data collection time (processing over 15 times faster).
- **Accuracy Improvement**: Accuracy improved by **4.1 percentage points** (from 94.2% to 98.3%).
- **Error Reduction**: Error margin decreased from 5.8% to **1.7%** (below 2%).

### Source Evidence
- **PDF Page**: Page 4 (p. 66), "STATISTICAL ANALYSIS" table; Page 5 (p. 67), Figure 3 and Interpretation text.

---

## 14. Baselines

- **Manual Data Collection**: Human operator locating job postings on the portal and copying title, company, location, and salary fields into spreadsheet software.

### Source Evidence
- **PDF Page**: Page 4 (p. 66), Section "STATISTICAL ANALYSIS".

---

## 15. Ablation Study

Not reported. (The study focuses on comparing automated scraping against manual collection rather than component-wise scraper ablation).

---

## 16. Explainability

Not applicable. (The extraction engine is deterministic rule-based DOM parsing rather than a black-box machine learning model).

---

## 17. Main Findings

1. Python with BeautifulSoup provides a reliable, cost-effective automation pipeline for job listing acquisition, cutting collection duration by over 93%.
2. Automated DOM extraction reduces human transcription errors, maintaining error margins below 2% compared to nearly 6% for human operators.
3. Incomplete HTML tags and dynamic page changes represent the primary source of missing data during scraping.
4. Structured CSV outputs enable downstream analytical workflows, such as skill demand analysis and salary range modeling.

### Source Evidence
- **PDF Page**: Page 1 (p. 63), Abstract; Page 5 (p. 67), interpretation; Page 7 (p. 69), Section "RESULTS" and "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Author
- **Static DOM Limitation**: Dependent on static HTML structure; sites heavily reliant on dynamic JavaScript rendering or CAPTCHA require additional headless browser tooling.
- **Incomplete HTML Tags**: Missing data occurred when target postings had missing or malformed tags.
- **Ethical and Legal Constraints**: Scraping must strictly adhere to website terms of service and robots.txt directives to avoid server overloading and legal infringement.

### 18.2 Research Interpretation
- The sample size of 500 postings from a single portal is relatively modest for large-scale labor market economics.
- The paper does not evaluate dynamic single-page applications (SPAs) built with React or Angular where `requests` alone cannot render content without tools like Selenium or Playwright.

---

## 19. Future Work

Explicitly proposed by author:
1. Multi-board scraping integration across diverse national and international job platforms.
2. Real-time labor market analytics dashboards.
3. Integration with Natural Language Processing (NLP) techniques to classify job descriptions and extract fine-grained technical skills.
4. Coupling scraped historical data with predictive machine learning models for workforce demand and salary forecasting.

### Source Evidence
- **PDF Page**: Page 8 (p. 70), Section "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original author.*

- **Relevant Module**: **PRIE ATS & Labor Market Alignment Engine (Module 04)**.
- **Methodological Value**: Validates the automated acquisition pipeline for live job postings, ensuring ScholarCamp's skill ontology reflects current employer demand rather than static, outdated syllabi.
- **Architecture Connection**: Provides the scraping foundation for feeding real-time job specifications into PRIE's skill gap analyzer and resume matcher.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Scraping reduces data collection time by 93.6% | 16 min (scraper) vs 250 min (manual) | PDF p. 4, Table & p. 5, text | Experimental result |
| Scraping error margin is 1.7% vs 5.8% manual | Accuracy 98.3% vs 94.2% | PDF p. 4, Table & p. 5, text | Experimental result |
| Python 3.10 and BeautifulSoup4 workflow | Code listing and tool descriptions | PDF pp. 5–7, Section METHODOLOGY | Methodology |
| Ethical and legal compliance requirement | Discussion on terms of service and robots.txt | PDF p. 3 & p. 8 | Author discussion |
| Integration with NLP for skill extraction | Author's proposed future research directions | PDF p. 8, Section CONCLUSION | Future work |

---

## 22. Verification Checklist

- [x] PDF read
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected
- [x] Dataset verified
- [x] Features verified
- [x] Algorithms verified
- [x] Architecture inspected
- [x] Experiments inspected
- [x] Results verified
- [x] Limitations verified
- [x] Future work verified
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read, exact experimental numbers verified, discrepancy from legacy BibTeX documented).
