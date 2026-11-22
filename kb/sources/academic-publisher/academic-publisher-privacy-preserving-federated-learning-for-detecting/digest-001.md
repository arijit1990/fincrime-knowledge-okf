---
type: Source Digest
title: Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks - part 1 of 1 (p. 1)
description: 'Verified paraphrased digest, p. 1: Abstract'
resource: https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article
tags:
- academic_finding
- academic_paper
- global_academic
- ml_statistics
- privacy_data_protection
status: stable
source_id: academic-publisher-privacy-preserving-federated-learning-for-detecting
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-01-01'
legal_status: unknown
part: 1
parts_total: 1
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:33Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:33Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:33Z'
sources:
- id: original
  resource: https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article
  title: Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks
  author: org:academic_publisher
  last_modified: '2022-01-01T00:00:00Z'
digest_points: 10
---

# Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Financial crimes such as fraudulent financial transactions, money laundering, illegal money transfers and bank transfer scams are the target of AI-based detection systems, particularly deep learning ones, which the authors say have been considered. (p. 1)[^original]  
  <sub>anchor: "several attempts have been considered to employ artificial intelligence (AI)-based FFT detection systems"</sub>
- **descriptive / context**: The authors state that, to their knowledge, no federated learning system using real transaction data among financial institutions had been implemented before this work. (p. 1)[^original]  
  <sub>anchor: "no federated learning systems using real transaction data among financial institutions have been implemented so far"</sub>
- **descriptive / limitation**: One obstacle identified is that a single financial institution, such as a local bank, may find it difficult to assemble enough transaction data for training, and a small dataset does not promise high detection accuracy. (p. 1)[^original]  
  <sub>anchor: "it is difficult to prepare sufficient amount of transaction data for training by one financial institution"</sub>
- **descriptive / limitation**: A second obstacle is that transaction data contains personal information, which the Japanese Act on the Protection of Personal Information restricts from being provided to third parties. (p. 1)[^original]  
  <sub>anchor: "it is restricted by Act on the Protection of Personal Information in Japan to provide the transaction data to a third party"</sub>
- **descriptive / context**: The paper reports demonstration experiments of privacy-preserving federated learning involving five Japanese banks: Chiba Bank, MUFG Bank, Chugoku Bank, Sumitomo Mitsui Trust Bank and Iyo Bank. (p. 1)[^original]  
  <sub>anchor: "privacy-preserving federated learning with five banks in Japan: the Chiba Bank, Ltd., MUFG Bank, Ltd."</sub>
- **descriptive / method**: The authors propose a privacy-preserving federated learning protocol, called Deepprotect, as the underlying cryptographic tool for detecting fraudulent financial transactions. (p. 1)[^original]  
  <sub>anchor: "we proposed a privacy-preserving federated learning protocol which we call Deepprotect, for detecting fraudulent financial transactions"</sub>
- **descriptive / method**: Deepprotect lets parties run stochastic gradient descent using a set of techniques for privacy-preserving deep learning, which the authors cite as IEEE TIFS 2018 and 2019 work. (p. 1)[^original]  
  <sub>anchor: "Deepprotect allows parties to execute the stochastic gradient descent algorithm using a set of techniques"</sub>
- **descriptive / method**: In the demonstration experiments the authors built machine learning models for two kinds of fraud: fraudulent transactions in customers' or victims' accounts, and criminals' bank accounts. (p. 1)[^original]  
  <sub>anchor: "we built machine learning models for detecting two types of financial frauds"</sub>
- **descriptive / finding or result**: The federated learning system detected fraudulent transactions that a model built on a single bank's dataset could not detect. (p. 1)[^original]  
  <sub>anchor: "our federated learning system detected FFTs that could not be detected by the model built using the dataset from a single bank"</sub>
- **descriptive / finding or result**: The federated learning system detected criminals' bank accounts before the bank actually froze them. (p. 1)[^original]  
  <sub>anchor: "detected criminals' bank accounts before the bank actually froze them"</sub>

---

[source overview](overview.md)

[^original]: Sachiko Kanamori, Taeko Abe, Takuma Ito, Keita Emura, Lihua Wang, Shuntaro Yamamoto et al., "Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks" (2022-01-01). https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article
