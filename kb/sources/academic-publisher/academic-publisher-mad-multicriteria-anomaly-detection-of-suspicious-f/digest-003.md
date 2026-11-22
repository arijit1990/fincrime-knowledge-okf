---
type: Source Digest
title: 'MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions - part 3 of 4 (pp. 6-9)'
description: 'Verified paraphrased digest, pp. 6-9: 6 Experimental results; 6.1 Experimental setup; 6.2 Results; and 1 more sections'
resource: https://dl.acm.org/doi/10.1145/3711896.3737244
tags:
- academic_finding
- academic_paper
- alerts_triage
- global_academic
- ml_statistics
- model_development
- transaction_behaviour
status: stable
source_id: academic-publisher-mad-multicriteria-anomaly-detection-of-suspicious-f
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2025-06-07'
legal_status: unknown
part: 3
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:02Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:02Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:02Z'
sources:
- id: original
  resource: https://dl.acm.org/doi/10.1145/3711896.3737244
  title: 'MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions'
  author: org:academic_publisher
  last_modified: '2025-06-07T00:00:00Z'
digest_points: 38
---

# MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 6 Experimental results

- **descriptive / context**: The section reports the main experimental results for MAD, but the configurations of hyperparameters identified as best performing cannot be disclosed. Source code and anonymised data are available for research purposes upon request. (p. 6)[^original]  
  <sub>anchor: "we cannot disclose the configurations of hyperparameters that have been identified as the best performing"</sub>
- **descriptive / context**: The validation data spans 8 months. (p. 6)[^original]  
  <sub>anchor: "the data used for the validation spans across 8 months"</sub>

## 6.1 Experimental setup

- **descriptive / context**: A complete ground truth of all illicit activity is infeasible, since it would require perfect human evaluation of billions of transactions, so only a subset of the ground truth is known. (p. 6)[^original]  
  <sub>anchor: "only a subset of the full ground truth is known"</sub>
- **descriptive / definition**: The known ground truth consists of SARs filed by Intesa Sanpaolo on cash-related activities during the period of interest; the ground truth is limited to non-archived SARs, since the FIU archives most SARs as not considered interesting. (p. 6)[^original]  
  <sub>anchor: "we limit the ground truth to the non-archived SARs"</sub>
- **descriptive / definition**: Operators of the competence centre assign a risk score to each SAR, and SARs scored as high risk form a subset; detecting these is a high priority. (p. 6)[^original]  
  <sub>anchor: "This score allows us to identify the SAR subset as _high risk_ ones"</sub>
- **descriptive / context**: Two sources generate the SARs: TradTxM, a rule-based commercial system used by the bank (name changed to avoid disclosure), and Branches, suspicious situations flagged by branch managers. (p. 6)[^original]  
  <sub>anchor: "Two sources of detections generate those SARs: TradTxM and Branches"</sub>
- **descriptive / typology or red flag**: TradTxM encodes suspicious scenarios as rules with accumulators and thresholds, each checking a single criterion, making it a single-criterion anomaly detection system. (p. 6)[^original]  
  <sub>anchor: "Each rule involves the check of a single criterion, i.e. in a single-criterion anomaly detection system"</sub>
- **descriptive / finding or result**: TradTxM triggered about 3,000 alarms per month (18,000 over 6 months), of which only 58 were SARs within the perimeter of interest, and only 4 of those were high risk; the authors describe the system as very prone to false positives. (p. 6)[^original]  
  <sub>anchor: "TradTxM triggered about 3,000 alarms per month (18,000 in 6 months)"</sub>
- **descriptive / method**: Because SARs often span multiple months, the validation ground truth covers the entire 8-month period rather than per month; MAD is run every month and results are aggregated over the 8 months. (p. 6)[^original]  
  <sub>anchor: "Consequently, the validation ground truth spans the entire 8-month period"</sub>
- **descriptive / finding or result**: Branches filed 7,164 SARs over the 6 months of interest, most of which were not detected by TradTxM. (p. 6)[^original]  
  <sub>anchor: "Branches filed a total of 7,164 SARs in the 6 months of interest"</sub>
- **descriptive / finding or result**: The excerpt gives 698 high-risk Branches SARs, placed in parentheses after the statement that most Branches SARs were not detected by TradTxM; the excerpt does not clearly state whether this is a subset of the 7,164. (p. 6)[^original]  
  <sub>anchor: "most of which have not been detected by TradTxM (698 _high risk_ ones)"</sub>
- **descriptive / method**: MAD ranks the top K most anomalous accounts each month; the 8-month prediction set is the union of the monthly top-K sets, so an account is predicted positive if flagged in at least one month. (p. 7)[^original]  
  <sub>anchor: "an account is considered as _predicted positive_ if it has been predicted as anomalous for at least one of the 8 months"</sub>
- **descriptive / method**: An account is a true positive if MAD flags it and it belongs to at least one SAR in the period; an SAR counts as detected if MAD flags at least one of its accounts. (p. 7)[^original]  
  <sub>anchor: "We consider an account as a _true positive_ if it is predicted as anomalous by MAD"</sub>
- **descriptive / limitation**: The authors state that the account-level aggregation does not constitute a limitation, since human operators can uncover the rest of the activity after an initial account-based detection. (p. 7)[^original]  
  <sub>anchor: "These assumptions do not constitute a limitation: human operators can unravel the rest of the activity"</sub>
- **descriptive / definition**: Detecting SARs also identified by TradTxM is called non-regression, and any additional detection is a progression; progressions are evaluated using Branches data and manual examination of cases not in the ground truth. (p. 7)[^original]  
  <sub>anchor: "We refer to the capability of MAD to detect SARs also identified by TradTxM as _non-regression_"</sub>
- **descriptive / method**: Evaluation uses the total number of undetected SARs and the total money involved in them for SAR-level results, and precision, recall and F1 score for accounts. (p. 7)[^original]  
  <sub>anchor: "we consider as the two metrics of interest the total number of _undetected_ SARs"</sub>
- **descriptive / method**: Branches SARs are not comparable to the TxM systems because branches use much more information than MAD and TradTxM. (p. 7)[^original]  
  <sub>anchor: "the branches operate using much more information than those used by MAD and TradTxM"</sub>

## 6.2 Results

- **descriptive / finding or result**: Results are reported at K = 550, the average monthly number of detections by TradTxM, which is a reasonable number for manual processing by the competence centre. (p. 7)[^original]  
  <sub>anchor: "This value of _𝐾_ is the average number of monthly detections reported by TradTxM"</sub>
- **descriptive / finding or result**: Local Outlier Factor achieves the best results across almost all metrics; the Autoencoder is comparable, while Isolation Forest and One-class SVM perform worst; TradTxM has 0 undetected TradTxM SARs by definition but performs poorly on other metrics. (p. 7)[^original]  
  <sub>anchor: "Local Outlier Factor achieves the best results across almost all metrics"</sub>
- **descriptive / finding or result**: No algorithm achieves full non-regression, but LOF and AE each miss only 1 of 4 high-risk TradTxM SARs. (p. 7)[^original]  
  <sub>anchor: "both LOF and AE only miss 1 out of 4 high risk SARs"</sub>
- **descriptive / finding or result**: MAD improves on TradTxM for Branches SARs: TradTxM detected none of them, while MAD identifies 200+ cases with a total volume of 150M euros. (p. 7)[^original]  
  <sub>anchor: "MAD instead identifies 200+ cases, for a total volume of 150M €"</sub>
- **descriptive / finding or result**: Across values of K, LOF gives the most satisfactory results; the Autoencoder detects a similar number of TradTxM SARs, but LOF detections involve SARs with larger money volumes. (p. 7)[^original]  
  <sub>anchor: "the gap between the _amount_ curves highlights how the LOF’s detections identifies SARs with larger volumes of money involved"</sub>
- **descriptive / finding or result**: As K increases, precision decreases and recall increases; MAD generally outperforms TradTxM even at lower K, and the F1 score rises sharply at low K before plateauing for larger K. (p. 7)[^original]  
  <sub>anchor: "precision decreases as _𝐾_ increases (the model is less certain about anomalies further down the ranking)"</sub>
- **descriptive / data or feature**: Figure 2 plots the number and amount of undetected SARs for TradTxM and Branches as a function of K (0 to 1000) for the four algorithms. (p. 8)[^original]  
  <sub>anchor: "Number of undetected SARs and their amount, for TradTxM and Branches, as a function of"</sub>
- **descriptive / finding or result**: Figure 3 shows precision, recall and F1 score for the four algorithms and TradTxM as a function of K; the gray line marks the K = 550 operating point. (p. 8)[^original]  
  <sub>anchor: "Figure 3 reports the performance of the four models and TradTxM"</sub>
- **descriptive / finding or result**: Manual inspection by Intesa Sanpaolo domain experts was limited to LOF and AE, the top 50 accounts not in the ground truth for each algorithm, to check for previously unknown suspicious activity. (p. 8)[^original]  
  <sub>anchor: "LOF and AE results have been considered, given their promising results"</sub>
- **descriptive / finding or result**: Of the top 50 LOF accounts not in the ground truth, 13 (26%) were considered worth further inspection; for AE, 15 of 50 (30%). (p. 8)[^original]  
  <sub>anchor: "For LOF, 13 out of the 50 accounts (26%) have been considered worth of further inspection"</sub>
- **descriptive / finding or result**: Applying the authors' prior estimate that about 5.7% of cases considered interesting become non-archived SARs, LOF and AE have estimated precisions of 1.5% and 1.7% on previously unknown cases. (p. 8)[^original]  
  <sub>anchor: "By applying this 5.7% factor, LOF and AE have a 1.5% and 1.7% precision respectively"</sub>
- **descriptive / finding or result**: The remaining flagged accounts (37 for LOF and 35 for AE) were judged by domain experts to be genuine outlier behaviour not related to money laundering, such as multiple personal and commercial activities, large gifts (e.g. weddings), or potential off-the-books payments. (p. 8)[^original]  
  <sub>anchor: "The remaining false positives (37 and 35 accounts respectively) were considered by the domain experts as actual outlier behaviors"</sub>

## 7 Deployment

- **descriptive / context**: MAD was deployed in November 2024 on an on-premise node within Intesa Sanpaolo's cluster. (p. 8)[^original]  
  <sub>anchor: "MAD has been deployed in November 2024 on an on-premise node within Intesa Sanpaolo’s cluster"</sub>
- **descriptive / data or feature**: The node has 112 cores (Intel Xeon Gold 6330N, 2.20GHz), 2.5 TB memory, 30 TB storage and one NVIDIA A100 GPU; MAD is allotted 8 cores and 40 GB memory. (p. 8)[^original]  
  <sub>anchor: "The resources dedicated to MAD are 8 cores and 40 GB of memory"</sub>
- **descriptive / method**: MAD is implemented in Python 3.11 using FastAPI for the API, BigQuery for data access, and scikit-learn plus PyTorch for the pipeline. (p. 8)[^original]  
  <sub>anchor: "The solution has been implemented in Python (3.11), using FastAPI for the definition of API"</sub>
- **descriptive / finding or result**: From November 2024 to February 2025 the full pipeline took on average 8.7 hours to process an average of 329M monthly transactions. (p. 9)[^original]  
  <sub>anchor: "the average execution time for the entire pipeline has been, on average, of 8.7 hours"</sub>
- **descriptive / finding or result**: LOF was the best performer throughout validation; 50 LOF-identified anomalies are sent monthly to the competence centre, totalling 200 detections, of which 68 had been processed at least by first level (L1). (p. 9)[^original]  
  <sub>anchor: "a subset of 50 anomalies identified by LOF are being sent to the competence centre on a monthly basis, for a total of 200 detections"</sub>
- **descriptive / finding or result**: At L1, MAD promoted 36 of 68 detections (52.9%) versus a 12.8% TradTxM promotion rate; 4 of those 36 belong to already reported SARs. (p. 9)[^original]  
  <sub>anchor: "L1 has promoted 36 out of the 68 detections (52.9%), whereas TradTxM only achieves a promotion rate of 12.8%"</sub>
- **descriptive / finding or result**: At L2, 23 of the remaining detections were processed and 9 promoted (39.1%), versus 9.4% for TradTxM. (p. 9)[^original]  
  <sub>anchor: "L2 has processed 23 of the remaining detections, promoting 9 of them, for a promotion rate of 39.1%"</sub>
- **descriptive / finding or result**: Combining L1 and L2, MAD's overall promotion rate is 20.7%, about an order of magnitude above TradTxM's approximately 1.2%; the authors note these are based on a small set and will change, but indicate meaningful improvement. (p. 9)[^original]  
  <sub>anchor: "By combining the L1 and L2 promotion rates, MAD has an overall rate of 20.7%"</sub>
- **descriptive / expectation**: The goal for the coming months, at time of writing, is to transition from TradTxM to MAD as the main cash transaction monitoring system at Intesa Sanpaolo. (p. 9)[^original]  
  <sub>anchor: "The goal for the upcoming months (at the time of writing) is to transition from TradTxM to MAD"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Academic publisher / repository, "MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions" (2025-06-07). https://dl.acm.org/doi/10.1145/3711896.3737244
