---
type: Source Text
title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification - part 1 of 4 (pp. 1-4)'
description: 'Verbatim extracted text, pp. 1-4: Abstract; 1 Introduction; 2 Related Work; and 6 more sections'
resource: https://arxiv.org/abs/2607.17586
tags:
- academic_finding
- data_features
- explainability
- global_academic
- model_development
- preprint
status: stable
source_id: arxiv-detection-attribution-narration-an-end-to-end-pipeline-for-expla
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-07-20'
legal_status: unknown
part: 1
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2607.17586
  title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification'
  author: org:arxiv
  last_modified: '2026-07-20T00:00:00Z'
---

# Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2026-07-20), part 1 of 4, pp. 1-4. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Yuge Zhang Yuanxing Zhang Yichao Jin Khairul Amsyar Mohd yugezhang@ocbc.com yuanxingzhang@ocbc.com jinyichao@ocbc.com Razis OCBC, Singapore OCBC, Singapore OCBC, Singapore khairulmohdrazis@ocbc.com OCBC, Singapore

Nicholas Qi An Choo Kai Yin Anders Wong nicholaschoo3@ocbc.com anderswong@ocbc.com OCBC, Singapore OCBC, Singapore

Wee Keong Dennis Lee dennislee@ocbc.com OCBC, Singapore

## Abstract


Money mule accounts are critical facilitators of financial fraud, yet detecting them at scale remains challenging due to the heterogeneous nature of transactional and behavioural data. We present an end-to-end pipeline for customer-level mule detection comprising three stages: (1) a LightGBM classifier trained on 280 engineered features spanning transaction patterns, account demographics, network topology, and temporal behaviour; (2) a TreeSHAP attribution layer that decomposes each prediction into feature contributions; and (3) a large language model (LLM) module that converts SHAP attributions into analyst-facing natural-language narratives. We evaluate across three open-weight LLM families and assess explanation quality through analyst feedback. In a live production deployment, the system achieves a yield rate of 89%, up from 61% under the incumbent rule-based system, with monthly alert volume expanding from 211 to 302, reflecting broader true-positive coverage rather than increased noise. This corresponds to a 60% incremental adverse detection beyond existing review workflows, substantially outperforming the rule-based approach. Qualitative feedback from analysts indicates that LLM-generated narratives reduce cognitive load during alert triage. We further discuss implications of deploying LLM-augmented explainability in regulated financial environments.

## 1 Introduction


Money mules, which are usually individual bank accounts involved in laundering the proceeds of fraud, represent one of the most prevalent drivers in the financial crime ecosystem. Mule accounts receive illicit funds from victims and rapidly disperse them onward, often across jurisdictions, making recovery difficult and enabling

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _KDD’26 - MLF workshop, Jeju, Korea_

© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.

Xinyan Tang Kenneth Zhu Ke tangxy@ocbc.com kennethzhu@ocbc.com OCBC, Singapore OCBC, Singapore

Jingyuan Zhao jingyuanzhao@ocbc.com OCBC, Singapore

downstream criminal activity at scale [12]. Despite increasing regulatory scrutiny, detection remains difficult because mule accounts often mimic legitimate customer behaviour during onboarding and early account activity, revealing anomalous patterns only when examined across multiple feature dimensions simultaneously.

A further operational challenge is that detection alone is insufficient. In practice, every flagged customer must be reviewed by a human analyst before action can be taken. Therefore, the usefulness of a detection system depends not only on its precision and recall, but also on how quickly and confidently analysts can triage the alerts it produces. This _explainability_ requirement is often underweighted in the academic literature, but is critical in production.

The incumbent approach in most financial institutions relies on deterministic threshold-based rules (e.g., more than _𝑁_ transactions to new payees within _𝑇_ days). While interpretable, these approaches suffer from a well-documented precision-recall tradeoff. Tightening rules reduces false positives but allows sophisticated mules to evade detection, while loosening them overwhelms analyst queues with false alerts. The rigidity of static rules also means that they cannot adapt to the evolving mule typologies without costly, repeated manual recalibration.

Critically, these rule-based systems usually operate on individual features in isolation. Money mule behaviour, however, is inherently multi-dimensional, where no single indicator is sufficiently diagnostic. Instead, it relies heavily on the _combination_ of subtle anomalies across transaction velocity, network structure, temporal patterns, and account demographics. This distinctive signature cannot be easily captured by deterministic rules.

This paper presents an end-to-end pipeline that addresses both detection and explainability challenges. Our contributions include

[pp. 1-2]

- High-dimensional ML classifier: A LightGBM model [7] trained using 280 engineered features for customer-level mule detection, with calibration analysis demonstrating reliable probability estimates across score ranges.

- LLM-augmented explainability: A pipeline that feeds SHAP [9] attributions into large language models to generate natural-language narratives. We assess output quality through analyst feedback.

Y. Zhang, Y. Zhang, Y. Jin, K. Razis, N. Choo, K. Wong, X. Tang, K. Zhu, W. Lee, and J. Zhao

- Live production validation: Deployment in an AML (AntiMoney Laundering) production environment achieves a yield rate of 89%, up from 61% under the incumbent rule-based system. Monthly alert volume expanded from 211 to 302, reflecting broader true-positive coverage rather than increased noise. This corresponds to 60% incremental adverse detection beyond existing review workflows, with qualitative analyst feedback indicating reduced cognitive load during triage compared to raw SHAP visualizations.

- Operational insights: Practical lessons on integrating ML and LLM components into analyst workflows within regulated financial environments, including guardrails against LLM hallucination and considerations for model governance.

## 2 Related Work


[p. 2]

Our work sits at the intersection of three research streams, including machine learning for financial crime detection, post-hoc explainability for high-stakes models, and the emerging use of LLMs to translate quantitative explanations into natural language. We review each in turn, highlighting the gap our pipeline addresses.

Machine learning has been applied to fraud and AML detection for more than two decades [12], yet work targeting money mule accounts specifically remains limited. Most published approaches frame the problem at the transaction level and rely on graphbased methods. Savage et al. [13] used supervised learning in small networks grouped by transactional interactions. More recently, Jambhrunkar et al. [6] proposed MuleTrack, a Markov-chain-based framework for detecting mule accounts in India’s UPI (Unified Payments Interface) system. Huang et al. [5] presented the MuleTrace algorithm to locate mule nodes within transaction graphs by tracking entire laundering chains.

## 2.1 Machine Learning for AML Detection


While graph-based methods are well-suited to network-level detection, they require access to full transaction graphs, which is often infeasible in siloed institutional environments. In contrast, our approach operates on _tabular features engineered at the customer level_ , requiring only data available within a single institution. Gradient boosting methods, particularly LightGBM [7], have demonstrated strong performance on tabular financial data. Taha and Malebary [14] showed that an optimised LightGBM achieves state-of-the-art results on credit card fraud detection. Xu et al. [16] proposed deep boosting decision trees that embed neural networks into gradient boosting while preserving interpretability. To date, gradient boosting approaches remain the dominant approach in deployed AML systems, yet published work rarely reports production deployment metrics such as analyst yield rate and increased coverage of real-world cases.

## 2.2 Explainability in High-Stakes ML


In regulated financial environments, model transparency is both an operational necessity and a compliance requirement. Regulators, including the United States (US) government [11] and European Union (EU) [4], increasingly mandate financial institutions to demonstrate how model output informs decisions. SHAP (SHapley Additive exPlanations) [9] had become the de facto standard for

local feature attribution, due to its game-theoretic foundations and the efficiency of the TreeSHAP algorithm [8] for tree-based models.

However, a persistent gap exists between what these methods produce, mainly numeric feature-contribution vectors, and what operational analysts need to act on. Waterfall plots and beeswarm diagrams require statistical literacy to interpret and slow down alert triage, particularly when analysts must process hundreds of alerts per day. This _last-mile explainability gap_ is the primary motivation for our LLM interpretation module.

## 2.3 LLMs as Explanation Narrators


The use of LLMs to convert quantitative AI model outputs into natural language is a rapidly growing research direction. Martens et al. [10] demonstrated that LLM-generated narratives from SHAP values are found convincing by over 90% of surveyed non-experts and help users more accurately summarize AI decisions compared to raw SHAP plots alone. Zytek et al. [19] developed Explingo, a dual-LLM system comprising a narrator that generates explanation narratives and an automated grader that evaluates them on accuracy, completeness, and fluency. Bello et al. [2] presented a three-level framework for LLM-enhanced explainable AI, including a case study that translates SHAP values from a loan-denial model into conversational narratives. Zeng [18] further explores using LLMs to enhance the interpretability of SHAP values specifically, demonstrating that model-generated narratives can surface feature interactions that raw attribution plots obscure.

These works established the feasibility of LLM-based XAI narration. However, evaluation to date has focused on narrative quality metrics rather than downstream operational impact, and deployment constraints such as on-premise hosting for data residency have not been highlighted. Our work extends this direction with production-validated evidence from a live AML setting using selfhosted open-weight models.

## 3.1 System Overview


The pipeline executes three modules sequentially for each customer: (1) feature engineering and classification, (2) SHAP attribution, and (3) LLM interpretation. This is followed by a domain expert workflow for alert triage. Figure 1 presents the end-to-end architecture. First, raw data from multiple source systems are transformed into a tabular feature matrix at the customer level and scored by a LightGBM classifier. The model outputs are then decomposed via TreeSHAP into per-feature contributions and narrated by self-hosted open-weight LLM models into a domain-expert-facing explanation. Alerts are ranked by predicted probability and surfaced to human analysts together with the generated narrative. A feedback loop from confirmed dispositions back into the watchlist and label pipeline to support periodic model retraining.

## 3.2 Data and Feature Engineering


[pp. 2-3]

Data sources. The model ingests data from multiple internal systems, including core banking transactions, customer onboarding records, device and channel metadata, and internal/external watchlist and sanctions feeds.

Figure 1: End-to-end system architecture for LLM-augmented money mule detection. The pipeline flows from raw data sources (left) through feature engineering (280 features), LightGBM classification with TreeSHAP attribution, LLM-based narrative generation, and into the domain expert workflow. Dashed line indicates the feedback loop for model retraining.

The training dataset includes 2,176 customer-level records across 2,115 unique customers.

Labels are derived from two primary sources of ground truth. The first consists of customers subject to Seizure Orders (SOs) filed by police officers under the Criminal Procedure Code (CPC), wherein affected customers are assigned a positive label, reflecting a legal determination that the funds are suspected proceeds of criminal activity. The second source comprises analyst-confirmed money mule cases, where customers have been reviewed and adjudicated by financial crime investigators. Customers confirmed as mules are labeled positive; those cleared are labeled negative.

In total, 1,680 customers (77.2%) are labeled as mules (positive class) and 496 (22.8%) as non-mules (negative class), yielding a positive-to-negative ratio of approximately 3.4:1. This distribution does not reflect the true population prevalence of money mule activity. To better approximate the real-world class distribution, additional negative samples are drawn from the unlabeled population and incorporated into the training set, reducing the positive-tonegative ratio to 1:5.

Feature taxonomy. Over 280 features are engineered at the customer level and organized into five overlapping feature groups, as summarized in Table 1.

All features are computed over multiple time windows (e.g., 7, 30, 90, 180 days) to capture both short-term bursts and longer-term behavioural drift.

Features are constructed by aggregating raw transactional and relational data at the customer level across multiple lookback windows of 7, 30, 90, and 180 days. For each window, aggregation functions including count, sum, min, max, and standard deviation

are applied to capture transaction frequency, volume, and dispersion. The diversity of counterparties and channels is measured using cardinality counts across unique recipients, senders, countries, and transaction channels. Two types of derived ratio features are computed, including credit-to-debit ratios for both transaction count and transaction value within each look-back window, as well as short-to-long-term velocity ratios that contrast 7-day activity with a 180-day baseline to identify sudden increases in transactional behaviour.

[p. 3]

Missing values in numeric features are imputed with zero, which is semantically appropriate as the absence of a transaction record implies zero activity. Categorical features retain missing values and are handled natively by the model. To prevent division-by-zero artefacts in ratio features, zero denominators are substituted with a missing indicator prior to computation.

No explicit post-engineering feature selection procedure, such as recursive feature elimination or correlation-based filtering, was applied. The full set of 280 engineered features was presented to the model, with implicit feature selection performed by the gradientboosted tree algorithm through its split-gain optimisation criterion.

## 3.3 LightGBM Classifier


[pp. 3-4]

We use LightGBM [7] for binary classification at the customer level, predicting the probability that a customer is operating as a money mule. LightGBM is chosen for its efficiency on high-dimensional tabular data, native categorical feature handling, and strong empirical performance in deployed financial systems.

Class imbalance. Although money mule accounts are rare in the real-world population, we apply negative sampling during training

Y. Zhang, Y. Zhang, Y. Jin, K. Razis, N. Choo, K. Wong, X. Tang, K. Zhu, W. Lee, and J. Zhao

Table 1: Summary of Feature Groups

|FeatureGroup|Count |Representative Examples|
|---|---|---|
|Transactionpatterns|263|Transaction count and amount for all(debit and credit), debit, and credittransactions; credit-to-debit ratios; pass-through frequency and amount; equiva-lent statistics for STR (Suspicious Trans-action Report)-linked counterparties andhigh/medium-risk geographies|
|Account|15|Customer tenure, age, country of domicile,|
|demo-graphics||number of active accounts, recency of ac-count opening/closing, number of policeorders received, and recency of last policeorder|
|Network/graph|47|Number and types of C2C relationships,number of connected customers with STRfilings, transaction value linked to net-work STRs|
|Temporal|37|Short-term to long-term velocity ratios|
|behaviour||comparing 7-day activity against 180-daybaseline for all (debit and credit), debit,credit, and STR-linked transactions, cap-turing sudden spikes in activity|
|Device/session/|16|Number of distinct transaction channelsused across multiple lookback windows,|
|channel||including channel diversity for high-riskgeography transactions and STR-linkedentities|

_Note:_ Feature counts sum to more than the total of 280 as certain features span multiple groups.

to construct a dataset with a positive-to-negative ratio of 1:5. This introduces an engineered class imbalance in the training set. To address this, we use the scale_pos_weight parameter, set to the ratio of negative to positive samples in the training data, which up-weights the loss contribution of positive examples.

Hyperparameter tuning. We perform grid search over the following hyperparameter space, selecting the configuration that maximises AUC-PR on the validation set as shown in table 2.

[p. 4]

Temporal train/test split. To prevent data leakage and simulate realistic deployment conditions, we split the data temporally. In particular, the model is trained on customers observed before a cutoff date and evaluated on customers appearing after that date.

Calibration. Since the predicted probability directly determines alert ranking and analyst workload, well-calibrated scores are essential. We assess calibration using reliability diagrams and the Expected Calibration Error (ECE), and apply Platt scaling where necessary. Platt scaling fits a logistic regression on a held-out validation set to map raw LightGBM scores to better-aligned probabilities, ensuring that a predicted score of 0.8 more faithfully reflects an 80% empirical likelihood of money mule behaviour rather than being an arbitrary model output.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification" (2026-07-20). https://arxiv.org/abs/2607.17586
