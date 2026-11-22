---
type: Source Digest
title: Detecting money laundering transactions with machine learning - part 1 of 1 (p. 1)
description: 'Verified paraphrased digest, p. 1: Abstract'
resource: https://doi.org/10.1108/jmlc-07-2019-0055
tags:
- academic_finding
- academic_paper
- global_academic
- ml_statistics
- model_development
status: stable
source_id: academic-publisher-detecting-money-laundering-transactions-with-machin
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2020-01-04'
legal_status: unknown
part: 1
parts_total: 1
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:32Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:32Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:32Z'
sources:
- id: original
  resource: https://doi.org/10.1108/jmlc-07-2019-0055
  title: Detecting money laundering transactions with machine learning
  author: org:academic_publisher
  last_modified: '2020-01-04T00:00:00Z'
digest_points: 9
---

# Detecting money laundering transactions with machine learning (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper aims to develop, describe and validate a machine learning model that prioritises which financial transactions should be manually investigated for potential money laundering. (p. 1)[^original]  
  <sub>anchor: "develop, describe and validate a machine learning model for prioritising which financial transactions should be manually investigated"</sub>
- **descriptive / data or feature**: The model is applied to a large data set from Norway's largest bank, DNB. (p. 1)[^original]  
  <sub>anchor: "The model is applied to a large data set from Norway’s largest bank, DNB."</sub>
- **descriptive / method**: The approach is a supervised machine learning model trained on three types of historic data: normal legal transactions, transactions flagged as suspicious by the bank's internal alert system, and potential money laundering cases reported to the authorities. (p. 1)[^original]  
  <sub>anchor: "A supervised machine learning model is trained by using three types of historic data"</sub>
- **descriptive / method**: The model predicts the probability that a new transaction should be reported, using inputs such as background information about the sender or receiver, their earlier behaviour and their transaction history. (p. 1)[^original]  
  <sub>anchor: "The model is trained to predict the probability that a new transaction should be reported"</sub>
- **descriptive / finding or result**: The paper finds that the common practice of not using non-reported alerts (transactions investigated but not reported) in training can lead to sub-optimal results. (p. 1)[^original]  
  <sub>anchor: "the common approach of not using non-reported alerts (i.e. transactions that are investigated but not reported)"</sub>
- **descriptive / finding or result**: The paper finds that using normal (un-investigated) transactions in training can likewise lead to sub-optimal results. (p. 1)[^original]  
  <sub>anchor: "The same applies to the use of normal (un-investigated) transactions."</sub>
- **descriptive / finding or result**: The developed method outperforms the bank's current approach on a fair measure of performance. (p. 1)[^original]  
  <sub>anchor: "Our developed method outperforms the bank’s current approach in terms of a fair measure of performance."</sub>
- **descriptive / context**: The authors claim the study is one of very few published AML models for suspicious transactions applied to a realistically sized data set. (p. 1)[^original]  
  <sub>anchor: "This research study is one of very few published anti-money laundering (AML) models"</sub>
- **descriptive / method**: The paper presents a new performance measure specifically tailored to compare the proposed method with the bank's existing AML system. (p. 1)[^original]  
  <sub>anchor: "The paper also presents a new performance measure specifically tailored to compare the proposed method to the bank’s existing AML system."</sub>

---

[source overview](overview.md)

[^original]: Martin Jullum, Anders Løland, Ragnar Bang Huseby, Geir Ånonsen, Johannes Pippidis Lorentzen, "Detecting money laundering transactions with machine learning" (2020-01-04). https://doi.org/10.1108/jmlc-07-2019-0055
