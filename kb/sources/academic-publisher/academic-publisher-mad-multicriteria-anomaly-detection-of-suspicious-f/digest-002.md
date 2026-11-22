---
type: Source Digest
title: 'MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions - part 2 of 4 (pp. 3-6)'
description: 'Verified paraphrased digest, pp. 3-6: 4.1 Dataset; 4.2 Focusing on interesting cases; 5 Methodology; and 2 more sections'
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
part: 2
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
digest_points: 45
---

# MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 3-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.1 Dataset

- **descriptive / data or feature**: The MAD dataset consists of anonymized transactions processed by Intesa Sanpaolo, covering eight months from November 2022 to June 2023. (p. 3)[^original]  
  <sub>anchor: "The dataset used for the development of MAD contains the anonymized transactions processed by Intesa Sanpaolo."</sub>
- **descriptive / data or feature**: Table 1 reports, for each month from Nov 2022 to Jun 2023, the total number of transactions and the number of unique accounts: Nov 2022 has 279,029,599 transactions and 14,503,838 accounts; Dec 2022 has 313,481,961 and 14,631,119; Jan 2023 has 277,222,213 and 14,894,278; Feb 2023 has 262,678,554 and 14,417,712; Mar 2023 has 300,891,611 and 15,461,731; Apr 2023 has 269,555,407 and 14,964,225; May 2023 has 310,595,368 and 14,652,299; Jun 2023 has 300,568,438 and 14,839,518. (p. 3)[^original]  
  <sub>anchor: "Cardinalities of the available datasets, separately for each month, in terms of number of transactions"</sub>
- **descriptive / context**: The dataset holds about 300 million transactions per month, performed by about 15 million accounts. (p. 3)[^original]  
  <sub>anchor: "We observe about 300 million transactions per month performed by about 15 million accounts."</sub>
- **descriptive / limitation**: For wire transfers (footnote 1), one party is guaranteed to be an account owned by a financial institution customer while the other account may be registered elsewhere, so a full characterization of those accounts may not be possible; since the paper focuses on cash transactions, this problem is ignored. (p. 3)[^original]  
  <sub>anchor: "for wire transfers, one of the parties is guaranteed to be an account owned by a financial institution customer"</sub>
- **descriptive / method**: The authors restrict the analysis to a well-defined slice of transactions: cash operations, which have no counterparty and therefore a homogeneous structure. (p. 3)[^original]  
  <sub>anchor: "The adoption of the cash perimeter provides a homogeneous structure in the transaction: no counterparty is involved in the operations."</sub>
- **descriptive / definition**: The set of accounts of interest A(1) is defined as all accounts that have at least one cash transaction. (p. 3)[^original]  
  <sub>anchor: "we establish the set of accounts of interest as"</sub>

## 4.2 Focusing on interesting cases

- **descriptive / context**: Limited-activity accounts are also harder to model because only limited information is available to describe their behaviour. (p. 4)[^original]  
  <sub>anchor: "accounts with limited activity are more difficult to model, as only limited information is available"</sub>
- **descriptive / definition**: Two thresholds are defined: a minimum of 3 operations performed (tau# = 3) and a minimum amount moved of 1,000 in absolute value (tau sigma = 1,000). (p. 4)[^original]  
  <sub>anchor: "For these reasons, we define two thresholds"</sub>
- **descriptive / definition**: Accounts with null or negative average account balance over the month are removed; these edge cases are less than 0.1% of accounts and otherwise produce artefacts in downstream normalization. (p. 4)[^original]  
  <sub>anchor: "These edge cases (less than 0.1% of the accounts) produce artefacts in the normalization steps downstream."</sub>
- **descriptive / definition**: The perimeter is restricted to accounts owned by natural persons (segment PERS), because other segments such as companies and institutions behave more variably and make unsupervised outlier detection noisier. (p. 4)[^original]  
  <sub>anchor: "other customer segments (e.g., companies, institutions) have a wider variety of behaviours"</sub>
- **descriptive / finding or result**: Table 2 shows, for May 2023 as an example, the account counts after each filter: original 14,652,299; cash perimeter 6,184,570 (42.2% of original); at least 3 transactions 2,900,805 (19.8% of original); total amount at least 1,000 1,399,255 (9.5%); positive balance 1,398,387; natural persons 995,907 (6.8% of original). (p. 4)[^original]  
  <sub>anchor: "the reduction in cardinality that occurs with each step of the definition of the perimeter"</sub>
- **descriptive / finding or result**: The final perimeter A(5) contains approximately one million accounts to analyse, and the reduction steps yield a more homogeneous setting in which anomalies can be better identified and later verified. (p. 4)[^original]  
  <sub>anchor: "Besides reducing the overall scale of the data, these reduction steps produce a more homogeneous setting"</sub>

## 5 Methodology

- **descriptive / method**: MAD is an unsupervised machine learning pipeline integrating feature engineering, anomaly detection algorithm selection and post-processing. (p. 4)[^original]  
  <sub>anchor: "We propose a machine learning pipeline for unsupervised anomaly detection, integrating the classic steps of feature engineering"</sub>
- **descriptive / method**: The pipeline aggregates data at account level, applies the perimeter filters, extracts domain-specific features, ranks outliers by anomaly level, and applies a post-processing step to refine results. (p. 4)[^original]  
  <sub>anchor: "We first aggregate data at the account level. Then, we apply the filters that define the perimeter of interest."</sub>

## 5.1 Feature Engineering

- **descriptive / method**: Features were designed with domain experts to describe account activity; all transactions in the period are grouped by account so that features capture overall behavioural patterns rather than individual transactions. (p. 4)[^original]  
  <sub>anchor: "We work closely with domain experts to design features that effectively describe account activity."</sub>
- **descriptive / method**: Monetary features are normalized either by the total amount moved by the account during the month (fraction of total flow) or by the account balance (fraction of potential movement capacity). (p. 4)[^original]  
  <sub>anchor: "we normalize the values by dividing either by the total amount moved by the account during the month"</sub>
- **descriptive / method**: The value distributions of each feature are summarized by their mean, median, standard deviation, minimum and maximum. (p. 4)[^original]  
  <sub>anchor: "We summarize the value distributions of features with their"</sub>

## 5.2 Anomaly Detection

- **descriptive / method**: Figure 1 shows the MAD architecture, which includes a validation framework that compares predictions with the available ground truth. (p. 4)[^original]  
  <sub>anchor: "including a validation framework to compare predictions with the available ground truth"</sub>

## 5.1 Feature Engineering

- **descriptive / data or feature**: Credit (C) and debit (D) transactions are computed separately to distinguish in- and out-flows, and total flow (all) combines both. (p. 5)[^original]  
  <sub>anchor: "allowing us to distinguish between in- and out-flows of money"</sub>
- **descriptive / method**: Envelope features quantify the ratio between an account's inflows and outflows, normalized to the [0,1] range with a sigmoid-based saturation function governed by minimum and maximum threshold ratios c1 and c2. (p. 5)[^original]  
  <sub>anchor: "a saturation function defined as follows:"</sub>
- **descriptive / data or feature**: Table 3 lists customer/account features: the account average monthly balance taken from the original dataset (one feature). (p. 5)[^original]  
  <sub>anchor: "Account average monthly balance, from the original dataset."</sub>
- **descriptive / data or feature**: Table 3 transaction features include counts of transactions (C, D, All), total amounts (unnormalized or normalized by account balance or month volume), total wire amount for the wire perimeter, and average, median, standard deviation, minimum and maximum amount per transaction. (p. 5)[^original]  
  <sub>anchor: "Total amount moved in transactions unnormalized or normalized by Account Balance or by Month Volume"</sub>
- **descriptive / data or feature**: Table 3 ratio features are Cash Ratio (total cash-in out of total cash-out), All Ratio (total incoming out of total outgoing across wire and cash), Cash-In Wire-Out Ratio (total cash-in out of total wire-out), and Wire-In Cash-Out Ratio (total wire-in out of total cash-out). (p. 5)[^original]  
  <sub>anchor: "Total Cash-In out of Total Cash-Out"</sub>
- **descriptive / data or feature**: Table 3 temporal features include the number of active days (C, D, All), the mean, median, standard deviation, minimum and maximum number of transactions on active days, and the timeslot 0/1 frequency. (p. 5)[^original]  
  <sub>anchor: "Number of days where the account has had some activity"</sub>
- **descriptive / data or feature**: The timeslot 0/1 feature is the fraction of transactions made in timeslot 0 (6 AM to 8 PM) or timeslot 1 (8 PM to 6 AM); the two fractions sum to 1. (p. 5)[^original]  
  <sub>anchor: "Fraction of transactions that have been made in either timeslot 0 (6 AM - 8 PM)"</sub>
- **descriptive / data or feature**: Sequential features include the fraction of times transaction type Y followed transaction type X (X, Y in C, D), and the median time elapsed between transactions of type X and the following transactions of type Y. (p. 5)[^original]  
  <sub>anchor: "Fraction of times transaction type Y followed transaction type X"</sub>
- **descriptive / data or feature**: Structuring features (C, D) are binary: 1 if the sum of transactions with amount below tau1 reaches at least tau2; the actual thresholds are omitted for safety reasons. A companion feature is the standard deviation of transactions below tau1. (p. 5)[^original]  
  <sub>anchor: "Binary features, 1 if the sum of the transactions with amount lower than"</sub>
- **descriptive / method**: Features spanning several orders of magnitude are transformed with a base-10 logarithm, f' = log10(f + 1), applied to all features except envelope, timeslot 0/1 frequency, number of active days and structuring features. (p. 5)[^original]  
  <sub>anchor: "After the computation, our dataset includes features spanning several orders of magnitude"</sub>
- **descriptive / data or feature**: Envelope features quantify the ratio between total incoming (credit, C) and total outgoing (debit, D) flows, within the same or across different perimeters, normalised to the 0-1 range with the saturation function. (p. 5)[^original]  
  <sub>anchor: "Ratio between Tot. incoming (C) and Tot. outgoing (D) within the same or across different perimeters"</sub>
- **descriptive / data or feature**: The Account Balance feature is the account's average monthly balance taken from the original dataset, and it counts as a single feature in Table 3. (p. 5)[^original]  
  <sub>anchor: "Account average monthly balance, from the original dataset."</sub>
- **descriptive / method**: Missing features are filled with zero to indicate absence (for example no debit transactions for total amount D). (p. 6)[^original]  
  <sub>anchor: "For missing features, we fill values with zero to indicate absence"</sub>
- **descriptive / method**: For standard deviation features, the value -1 is used instead, signalling out-of-distribution values. (p. 6)[^original]  
  <sub>anchor: "For the standard deviation, we use -1 instead, signalling out-of-distribution values."</sub>
- **descriptive / method**: All features are standardized by subtracting the mean and dividing by the standard deviation. (p. 6)[^original]  
  <sub>anchor: "we then standardize all features by subtracting the mean and dividing by the standard deviation."</sub>
- **descriptive / method**: To reduce multicollinearity, correlation-based feature selection removes features whose correlation exceeds a threshold theta; theta values from 0.1 to 1 were explored, with elbow points identified near 0.5 and 0.8, and these values plus theta = 1 (no reduction) are tested as hyperparameters. (p. 6)[^original]  
  <sub>anchor: "we identify elbow points near 0.5 and 0.8"</sub>
- **descriptive / method**: Principal Component Analysis (PCA) is also tested as an alternative dimensionality reduction method. (p. 6)[^original]  
  <sub>anchor: "Similarly, we test the usage of Principal Component Analysis (PCA) for dimensionality reduction."</sub>

## 5.2 Anomaly Detection

- **descriptive / method**: Because no prior knowledge of outliers is available, the authors select distance-based (Isolation Forest, One-class SVM), density-based (Local Outlier Factor) and reconstruction-based (Autoencoder) algorithms. (p. 6)[^original]  
  <sub>anchor: "where no prior knowledge about what defines or characterizes an outlier is available"</sub>
- **descriptive / method**: For the One-class SVM, given the large dataset, the Stochastic Gradient Descent linear solver is used with Nystroem kernel approximation to reduce computational complexity while preserving nonlinearity. (p. 6)[^original]  
  <sub>anchor: "the Stochastic Gradient Descent linear One-Class SVM solver"</sub>
- **descriptive / method**: For each algorithm a grid search over hyperparameters is performed to find the optimal configuration, validated on a partial ground truth. (p. 6)[^original]  
  <sub>anchor: "we perform a grid search (as detailed in Table 4) to identify the optimal configuration"</sub>
- **descriptive / data or feature**: Table 4 lists key hyperparameters: LOF (number of neighbors k, distance metric, correlation threshold, PCA); AE (number of layers, neurons per layer, batch size, epochs); IF (number of trees, subsample size, correlation threshold, PCA); OCS (nu, the fraction of training errors, tolerance, kernel type, correlation threshold, PCA). (p. 6)[^original]  
  <sub>anchor: "Key hyperparameters considered for the anomaly detection algorithms."</sub>
- **descriptive / method**: All algorithms produce an anomaly score per sample; accounts are ranked by score and the top-K most anomalous are retained for further analysis, yielding a ranked list ordered by anomaly score. (p. 6)[^original]  
  <sub>anchor: "The output of this step is a ranked list of accounts ordered by their anomaly score"</sub>
- **descriptive / context**: The top-K cut-off reflects the limited processing capacity of the competence centre. (p. 6)[^original]  
  <sub>anchor: "comes from the limited processing capacity of the competence centre"</sub>
- **descriptive / limitation**: Because the algorithms are unsupervised, the outliers are not biased toward illicit activity; many are accounts acting strangely but of no AML interest, mainly because they move very low volumes of money. (p. 6)[^original]  
  <sub>anchor: "many of the identified outliers are indeed accounts acting strangely, but not of interest to AML"</sub>
- **descriptive / method**: A post-processing filter keeps only anomalous accounts whose total moved amount exceeds a minimum threshold Tpost, reducing operator workload. (p. 6)[^original]  
  <sub>anchor: "we filter the ranking of anomalous accounts by selecting those with a total moved amount above a threshold"</sub>
- **descriptive / method**: The Tpost threshold is optimised together with the other pipeline hyperparameters. (p. 6)[^original]  
  <sub>anchor: "We optimise this threshold along with other pipeline hyperparameters."</sub>
- **expected / context**: Because of limited time for human operators, the authors state that prioritisation of accounts with high cash movements is needed. (p. 6)[^original]  
  <sub>anchor: "prioritization of accounts with high cash movements is needed"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions" (2025-06-07). https://dl.acm.org/doi/10.1145/3711896.3737244
