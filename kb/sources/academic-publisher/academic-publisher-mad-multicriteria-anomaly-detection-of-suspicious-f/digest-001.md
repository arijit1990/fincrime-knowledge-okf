---
type: Source Digest
title: 'MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions - part 1 of 4 (pp. 1-3)'
description: 'Verified paraphrased digest, pp. 1-3: Abstract > ACM Reference Format:; 1 Introduction; CCS Concepts; and 4 more sections'
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
part: 1
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
digest_points: 36
---

# MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-3) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / finding or result**: The MAD study reports a real-world deployment at Intesa Sanpaolo using unsupervised anomaly detection on more than 2 billion anonymized bank transactions registered over 8 months. (p. 1)[^original]  
  <sub>anchor: "Using more than 2 billion anonymized bank transactions that Intesa Sanpaolo, a primary Italian financial institution, registered over 8 months"</sub>
- **descriptive / finding or result**: The authors report that the pipeline increased precision and recall by a factor of 6 in detecting high-risk cases. (p. 1)[^original]  
  <sub>anchor: "Besides increasing both precision and recall by a factor of 6 in the detection of high-risk cases"</sub>
- **descriptive / finding or result**: The pipeline raised more than 200 additional alerts over the 8-month period that branch managers had identified manually but the rule-based system missed. (p. 1)[^original]  
  <sub>anchor: "our pipeline raises 200+ additional alerts during the 8-month period, manually identified by branch managers, but missed by the rulebased system"</sub>
- **descriptive / finding or result**: A manual inspection of 100 new unseen cases revealed 28 significant previously unreported cases. (p. 1)[^original]  
  <sub>anchor: "a manual inspection of 100 new unseen cases revealed 28 significant previously unreported cases"</sub>
- **descriptive / context**: The pipeline is now fully deployed in Intesa Sanpaolo's Transaction Monitoring system. (p. 1)[^original]  
  <sub>anchor: "The pipeline, now fully deployed in Intesa Sanpaolo’s Transaction Monitoring system"</sub>

## 1 Introduction

- **descriptive / context**: Financial Intelligence Units worldwide require financial institutions to report activities considered suspect, and institutions rely on Transaction Monitoring systems that process hundreds of millions of transactions. (p. 1)[^original]  
  <sub>anchor: "Financial Intelligence Units (FIU) worldwide require financial institutions to report activities that are considered as suspect"</sub>
- **descriptive / context**: Transaction monitoring is typically run every month because alarms do not need to be raised in real time, unlike for credit card transactions. (p. 1)[^original]  
  <sub>anchor: "This process is typically run every month, as alarms do not need to be raised in real-time"</sub>
- **descriptive / context**: Rule-based TxM systems detected simple money laundering and sanctions circumvention cases, but individuals and organisations can easily bypass these simplistic rules. (p. 1)[^original]  
  <sub>anchor: "However, individuals and organizations can easily bypass these often simplistic rules"</sub>
- **descriptive / context**: The paper claims to be the first detailed account of the full end-to-end process of an ML pipeline deployed with results in a real scenario. (p. 1)[^original]  
  <sub>anchor: "to the best of our knowledge we are the first to provide a detailed account of the full end-to-end process"</sub>
- **descriptive / method**: MAD is an unsupervised anomaly detection approach that compares multiple algorithms and adds a post-processing step to enhance detection of suspicious cash-based activity. (p. 2)[^original]  
  <sub>anchor: "We compare and test multiple algorithms, and integrate a post-processing step to enhance the detection of suspicious activity considering cash-based transactions"</sub>
- **descriptive / finding or result**: Experts validated MAD against the current rule-based system and manually detected fraud cases; MAD identified all high-risk cases the rule-based system detected while reducing the overall number of alarms. (p. 2)[^original]  
  <sub>anchor: "MAD successfully identified all high-risk cases detected by the rule-based system, while reducing the overall number of alarms"</sub>
- **descriptive / finding or result**: In a manual review of a sample of flagged accounts, 25-30% corresponded to never-reported but suspicious accounts. (p. 2)[^original]  
  <sub>anchor: "A manual review of a sample of flagged accounts reveals that 25-30% of them correspond to never-reported but suspicious accounts"</sub>
- **descriptive / context**: The paper outlines its structure: background, related work, problem definition and dataset, methodology, experiments, deployment, and lessons learned. (p. 2)[^original]  
  <sub>anchor: "Section 2 provides the necessary background on TxM and financial regulations"</sub>

## 2 Background

- **descriptive / definition**: A customer is the entity interacting with a financial institution, which can be a physical person or a legal entity; an account is identified by an accountID such as an ABA routing number or IBAN. (p. 2)[^original]  
  <sub>anchor: "A customer of a financial institution is defined as the entity that interacts with a financial institution"</sub>
- **descriptive / definition**: Financial Intelligence Units are government agencies that collect and investigate suspicious or unusual financial activity and act as intermediaries between institutions and law enforcement. (p. 2)[^original]  
  <sub>anchor: "FIUs act as an intermediary between financial institutions and law enforcement agencies"</sub>
- **mandatory / requirement**: Financial institutions such as banks, credit unions and insurance companies are required to report suspicious activities to FIUs through a Suspicious Activity Report (SAR). (p. 2)[^original]  
  <sub>anchor: "Financial institutions, such as banks, credit unions, insurance companies, etc., are required to report suspicious activities to FIUs"</sub>
- **descriptive / method**: Transaction Monitoring typically starts with an automated, often rule-based, first step, followed by investigation by human operators in a two-level competence centre (L1 and L2). (p. 2)[^original]  
  <sub>anchor: "Because of these volumes, the first step of TxM is typically automated, often with rule-based detection systems"</sub>
- **descriptive / method**: L1 discards clearly irrelevant detections and passes interesting cases to L2, which investigates further and decides between false positive and SAR submission. (p. 2)[^original]  
  <sub>anchor: "L1 performs an initial analysis to discard clearly irrelevant detections"</sub>
- **descriptive / definition**: The FIU generally gives only archived or non-archived status for a SAR; for this work non-archived SARs are treated as true positives. (p. 2)[^original]  
  <sub>anchor: "For the purposes of this work, we consider non-archived SARs as _true positives_"</sub>

## 3 Related Works

- **descriptive / context**: Supervised learning studies use decision trees, Random Forest, SVMs, feedforward networks, LSTM, GRU, Transformers and Graph Neural Networks, but annotation effort limits training set size and generalisability. (p. 2)[^original]  
  <sub>anchor: "However, the intensive effort required for dataset annotation lays the limitation, often leading to small training sets"</sub>
- **descriptive / limitation**: Supervised and labelled-data approaches struggle to keep pace with rapidly evolving laundering techniques and can become reactive rather than proactive. (p. 2)[^original]  
  <sub>anchor: "often leaves these models struggling to keep pace"</sub>
- **descriptive / method**: Unsupervised AML work uses anomaly detection algorithms such as Isolation Forest, One-Class SVM and Local Outlier Factor, and cluster analysis. (p. 2)[^original]  
  <sub>anchor: "Algorithms like Isolation Forest, One-Class SVM, and Local Outlier Factors [3, 7, 10, 17] detect samples deviating"</sub>
- **descriptive / limitation**: Anomalous is not necessarily suspicious, so the false positive rate of anomaly detection can be high. (p. 2)[^original]  
  <sub>anchor: "what is anomalous is not necessarily suspicious/fraudulent, so the false positive rate can be high"</sub>

## 2 Background

- **expected / requirement**: SARs need to contain information on both the parties involved (subjects) and the financial operations characterising the suspicious activity (objects). (p. 2)[^original]  
  <sub>anchor: "These SARs need to contain both information on who performed the suspicious activity"</sub>

## 3 Related Works

- **descriptive / context**: Semi-supervised works combine limited labelled data with unlabelled transactions, for example self-supervised GCN embeddings, Snorkel-based label expansion and isolation-forest-ranked manual annotation. (p. 3)[^original]  
  <sub>anchor: "Usman et al. [23] use a self-supervised GCN [13] to generate user embeddings"</sub>
- **descriptive / limitation**: Many prior studies use datasets of some thousands of transactions or accounts, orders of magnitude smaller than the millions of accounts in this study. (p. 3)[^original]  
  <sub>anchor: "Many studies work with datasets containing some thousands of transactions/account [1, 12, 26]"</sub>
- **descriptive / limitation**: Some prior work oversimplifies the task through artificially balanced datasets, down-sampling of legitimate transactions, or identifying SARs from alerts only. (p. 3)[^original]  
  <sub>anchor: "the oversimplification of the anomaly detection task through artificially balanced datasets or inflated anomaly rates"</sub>
- **descriptive / finding or result**: Reference [7] uses a more realistic setup where anomalies represent 0.01% of total transactions. (p. 3)[^original]  
  <sub>anchor: "[7] provides a more realistic setup by working with datasets where anomalies represent 0.01% of the total transactions"</sub>
- **descriptive / context**: The present work addresses both scale and extreme imbalance, with millions of accounts and anomalies at 0.01% of transactions. (p. 3)[^original]  
  <sub>anchor: "We focus on datasets with millions of accounts and anomalies comprising only 0.01% of the transactions"</sub>
- **descriptive / context**: No previous work was found reporting experience in a production system; this paper reports deployment in Intesa Sanpaolo's production TxM. (p. 3)[^original]  
  <sub>anchor: "to the best of our knowledge, no previous work reports the experience in the production system"</sub>

## 4 Problem definition

- **descriptive / definition**: Customers and accounts are linked by ownership functions; a customer may own several accounts and an account may be jointly held, with a primary owner identified. (p. 3)[^original]  
  <sub>anchor: "customers can own multiple accounts, and an account can be jointly held by multiple customers"</sub>
- **descriptive / definition**: Each account has a balance, and each customer is assigned a segment (e.g. natural person, legal entity, institution) determined during Know Your Customer due diligence. (p. 3)[^original]  
  <sub>anchor: "Each customer is associated with a _customer segment_ , as determined during the _Know Your Customer_ (KYC) due diligence phase"</sub>
- **descriptive / data or feature**: CASH transactions (withdrawals and deposits) are modelled as a 4-tuple of account, amount (positive for deposits), date and time. (p. 3)[^original]  
  <sub>anchor: "A CASH transaction can be fully described as a 4-tuple"</sub>
- **descriptive / data or feature**: WIRE transactions involve two parties, originator and beneficiary, and are modelled as a 5-tuple with amount positive when the account is the beneficiary. (p. 3)[^original]  
  <sub>anchor: "the transaction can be represented as a 5-tuple"</sub>
- **descriptive / method**: TxM is performed over batches spanning a time window (e.g. monthly), and the goal is to produce a set of subjects of interest that call for competence-centre evaluation and may become SARs. (p. 3)[^original]  
  <sub>anchor: "TxM is generally performed over batches of data that span a specific time span"</sub>
- **descriptive / limitation**: Using FIU outcomes as ground truth is problematic: the FIU often gives no feedback, relies on information not available to institutions, and investigates only reported cases so false negatives are ignored. (p. 3)[^original]  
  <sub>anchor: "Second, the FIU investigates only reported cases, with the risk that false negatives are ignored"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions" (2025-06-07). https://dl.acm.org/doi/10.1145/3711896.3737244
