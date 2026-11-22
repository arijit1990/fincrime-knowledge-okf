---
type: Source Digest
title: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation - part 1 of 4 (pp. 1-5)
description: 'Verified paraphrased digest, pp. 1-5: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation; Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation > ABSTRACT; Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation > 1 INTRODUCTION; and 6 more sections'
resource: https://arxiv.org/abs/2310.04546
tags:
- academic_finding
- global_academic
- ml_statistics
- preprint
- privacy_data_protection
status: stable
source_id: arxiv-privacy-preserving-financial-anomaly-detection-via-federated-lea
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-06-10'
legal_status: unknown
part: 1
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2310.04546
  title: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation
  author: org:arxiv
  last_modified: '2023-06-10T00:00:00Z'
digest_points: 48
---

# Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-5) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Financial institutions use machine-learning models trained on customer data to combat fraud and financial crime, but sharing that data across institutions is constrained by consent and privacy laws such as GDPR and CCPA, making joint training of accurate anomaly detection models difficult. (p. 1)[^original]  
  <sub>anchor: "may prohibit FIs from sharing clients’ sensitive data (e.g., personally identifiable information) in certain geographies"</sub>

## 1 INTRODUCTION

- **descriptive / context**: Identifying financial transactions linked to illicit activity such as fraud, drug trafficking or terrorism is important for law enforcement and payment networks such as SWIFT. (p. 1)[^original]  
  <sub>anchor: "Identifying financial transactions associated with illicit activities (e.g., fraud, drug trafficking or terrorism) is important for law enforcement authorities"</sub>
- **descriptive / context**: Compliance with local and cross-border privacy laws is a key design consideration, so no single entity would have plaintext access to financial data across institutions or jurisdictions. (p. 1)[^original]  
  <sub>anchor: "no single entity would have plaintext access to financial data across different institutions and/or jurisdictions"</sub>
- **descriptive / method**: The paper describes a privacy-preserving framework combining federated learning, efficient multi-party computation and noisy aggregates inspired by differential privacy, allowing FIs to jointly train accurate anomaly detection models. (p. 1)[^original]  
  <sub>anchor: "The framework combines the concept of federated learning with efficient multi-party computation and noisy aggregates inspired by differential privacy"</sub>
- **descriptive / context**: The framework was submitted as a winning entry to the financial crime detection track of the US/UK Privacy-Enhancing Technologies (PETs) Challenge. (p. 1)[^original]  
  <sub>anchor: "The presented framework was submitted as a winning entry to the financial crime detection track of the US/UK Privacy-Enhancing Technologies (PETs) Challenge."</sub>
- **descriptive / data or feature**: Experiments used the synthetic transaction data of the PETs challenge: 7 million transactions for training and 700 thousand for inference. (p. 1)[^original]  
  <sub>anchor: "7 million transactions for training and 700 thousand transactions for inference"</sub>
- **descriptive / finding or result**: Using additional customer data via the proposed privacy-preserving approach improved the model's Area Under the Precision–Recall Curve from 0.6 to 0.7. (p. 1)[^original]  
  <sub>anchor: "results in improvement of our anomaly detection model’s Area Under the Precision–Recall"</sub>
- **descriptive / context**: MPC and federated learning are presented as privacy-enhancing technologies that can potentially offer solutions; in MPC, private data is securely distributed among computing nodes. (p. 1)[^original]  
  <sub>anchor: "In MPC, the private data is securely distributed among a group of computing nodes."</sub>
- **descriptive / limitation**: Using federated learning as a black-box solution may not be viable for privacy-preserving financial anomaly detection, partly because solutions without strong privacy protection can leak local data information through gradient updates, enabling membership inference attacks. (p. 2)[^original]  
  <sub>anchor: "can leak information about local data sets to the other involved parties, e.g., via their local gradient updates"</sub>
- **descriptive / limitation**: Data schemas across FI parties may be heterogeneous rather than homogeneous as in standard horizontal FL; such a setting with heterogeneous schemas or sub-models is referred to as vertical FL. (p. 2)[^original]  
  <sub>anchor: "Such a setting, where the machine-learning model embraces sub-models or heterogeneous data schemas from different clients is referred to as _vertical_ FL."</sub>

## 1.1 Problem Statement

- **descriptive / context**: The setting has a central hub S routing transactions between Financial Institutions ('Banks'); SWIFT is given as an example of such a central hub. (p. 2)[^original]  
  <sub>anchor: "SWIFT [4], which provides the services and framework for executing cross-border payments between Banks worldwide, is a central hub in this architecture."</sub>
- **descriptive / context**: Hub S learns many transaction details, including sender and receiver banks, account numbers, names, addresses, currencies and amounts; a centralised model trained on this data could achieve decent accuracy. (p. 2)[^original]  
  <sub>anchor: "In a naive approach, a centralized machine learning model could be trained using the above data with decent accuracy."</sub>

## 1.2 Our Approach

- **descriptive / method**: The approach uses secure multi-party computation, restricting transaction sensitivity and applying noise to hinder inference attacks and provide differential privacy, so the hub can train a model with banks while keeping bank data private. (p. 2)[^original]  
  <sub>anchor: "Our solution enables the hub to collaboratively train a highly accurate anomaly detection model with multiple Banks"</sub>
- **descriptive / data or feature**: The PETs synthetic dataset comprises 7 million training transactions, 700 thousand inference transactions and 530 thousand bank accounts. (p. 2)[^original]  
  <sub>anchor: "consisting of 7 million transactions for training and 700 thousand transactions for inference, as well as 530 thousand bank accounts"</sub>
- **descriptive / data or feature**: Banks hold account fields (name, account number, address, ZIP code) shared with S, plus a private 'Flag' field indicating potential issues or special features of the account, which cannot be shared with S. (p. 2)[^original]  
  <sub>anchor: "This Flag essentially resembles the private information held by the Banks and cannot be shared with S."</sub>
- **descriptive / finding or result**: S alone could train a transaction classifier; adding the banks' Flag privately has potential to improve accuracy, observed as AUPRC rising from 0.6 to 0.7 on the PETs dataset. (p. 2)[^original]  
  <sub>anchor: "we observe an improvement on the model’s Area Under the Precision–Recall Curve from 0 _._ 6 to 0 _._ 7.1"</sub>
- **descriptive / method**: In training, S computes two model updates per transaction, assuming the receiving account flag is normal or abnormal; the hub, receiving bank and an aggregator run an MPC protocol to select the update matching the flag obliviously. (p. 2)[^original]  
  <sub>anchor: "The hub S, the receiving bank, and a third party called the _aggregator_ then participate in a _secure multi-party computation (MPC)_ protocol"</sub>
- **descriptive / method**: The sending bank does not take part in the MPC protocol, on the assumption that a sending bank would not approve an outgoing transaction from an abnormal account; this is said to be in line with the dataset. (p. 2)[^original]  
  <sub>anchor: "Note that the sending Bank does not participate in the MPC protocol, as we assume that a sending Bank would not approve an outgoing transcation from an "abnormal" account"</sub>
- **descriptive / method**: The aggregator adds noise to the aggregated update before it is sent to S, to hide individual transaction contributions; the noise magnitude is a hyperparameter depending on batch size, clipping bound and desired privacy level. (p. 2)[^original]  
  <sub>anchor: "The magnitude of the noise is a hyperparameter that depends on the batch size, the clipping bound, and the desired level of privacy."</sub>
- **descriptive / method**: Only S learns the final noised update, and neither the aggregator nor the bank gains insight into S's transaction data; S then applies the update to its local model. (p. 2)[^original]  
  <sub>anchor: "Our approach guarantees that only S learns this final update, and neither the aggregator nor the bank can gain insight into S’s transaction data."</sub>
- **descriptive / method**: In inference, S runs each transaction through the model twice (flag normal or abnormal) and then uses a secure two-party computation with the receiver bank, without the aggregator, to learn whether the transaction is anomalous. (p. 2)[^original]  
  <sub>anchor: "S and the receiver bank engage in a secure two-party computation protocol without involving the aggregator."</sub>
- **descriptive / limitation**: If the two labels computed by S differ, interacting with the receiver bank leaks information about the flag to S; this inherent leakage is discussed in Section 3. (p. 2)[^original]  
  <sub>anchor: "If the two labels computed by S differ, then interacting with the receiver bank leaks information about the flag to S."</sub>
- **descriptive / context**: The approach generalises to heterogeneous settings where clients train models incrementally and send updates; privacy holds if the aggregation step can be computed securely (e.g., via MPC or homomorphic encryption). (p. 2)[^original]  
  <sub>anchor: "The privacy properties hold when the aggregation step, including but not limited to model selection, vector concatenation and weighted sum, can be efficiently computed securely"</sub>
- **descriptive / context**: The protocol also generalises to sharing data with differing magnitudes (e.g., risk scores) rather than a single bit, and to fully malicious banks and aggregators at an efficiency cost. (p. 2)[^original]  
  <sub>anchor: "our approach also generalizes to incorporate fully malicious banks and aggregators albeit with an impact to efficiency."</sub>

## 1.3 Related Work

- **descriptive / context**: Related work covers FL research on heterogeneity, security, privacy, fairness and communication, starting from McMahan et al.; SecureBoost addressed vertically partitioned data, and other works studied leakage attacks and inference prevention. (p. 2)[^original]  
  <sub>anchor: "Since the seminal work from McMahan et al. [27], there has been widespread interest"</sub>
- **descriptive / limitation**: A prior graph-plus-federated-learning framework for suspicious payment patterns across institutions did not consider heterogeneous data sharing, which is the common scenario in the authors' setting. (p. 2)[^original]  
  <sub>anchor: "However, this framework did not consider heterogeneous data sharing between institutions, which is the common scenario in our setting."</sub>

## 1.2 Our Approach

- **descriptive / method**: In the training phase, the aggregator adds noise to the aggregated update before the final noised update is sent to S. (p. 2)[^original]  
  <sub>anchor: "the aggregator adds noise to the aggregated update"</sub>
- **descriptive / method**: In the inference phase, S and the receiver bank run a secure two-party computation without involving the aggregator. S learns whether the transaction is anomalous without learning additional information about the recipient account's flag. (p. 2)[^original]  
  <sub>anchor: "S and the receiver bank engage in a secure two-party computation protocol without involving the aggregator"</sub>
- **descriptive / finding or result**: The result of the inference protocol is that S learns whether a transaction is anomalous or not. (p. 2)[^original]  
  <sub>anchor: "The result of this protocol is that S learns if that transaction is anomalous or not"</sub>

## 2 PRELIMINARIES

- **descriptive / definition**: In 1-out-of-2 oblivious transfer, the sender holds two values and the receiver learns exactly one of them while the sender learns nothing; this generalises to 1-out-of-n OT. (p. 3)[^original]  
  <sub>anchor: "At the end of the protocol, the receiver learns exactly one of the sender values while the sender learns nothing."</sub>
- **descriptive / definition**: A zero-knowledge proof lets a prover convince a verifier that a property of a private witness holds for a public instance, without the verifier learning more. (p. 3)[^original]  
  <sub>anchor: "to convince a verifier _𝑉_ that some property of _𝑤_ is true i.e. _𝑅_ ( _𝑥,𝑤_ ) = 1, without _𝑉_ learning anything more."</sub>
- **descriptive / definition**: Definition 1 states a zero-knowledge proof for an NP relation must satisfy completeness, soundness (false statements accepted with negligible probability against any malicious unbounded prover) and zero knowledge (simulatable views for malicious PPT verifiers). (p. 3)[^original]  
  <sub>anchor: "Soundness: _For every malicious and computationally unbounded 𝑃_∗ _, there is a negligible function"</sub>
- **descriptive / context**: In server-client federated learning, the server broadcasts the global model, clients return gradient updates from private data, and the server aggregates them into a new global model. (p. 3)[^original]  
  <sub>anchor: "In each training step, the server broadcasts the current global model to all clients."</sub>
- **descriptive / context**: Recent FL work addresses heterogeneous clients with different input features, privacy leakage in server aggregation, and secure aggregation and differentially private mechanisms to enhance privacy. (p. 3)[^original]  
  <sub>anchor: "Secure aggregation [9, 20] and differentially-private mechanisms [17, 37] are subsequently introduced in the FL framework"</sub>

## 3 THREAT MODEL

- **expected / requirement**: The primary goal is for S to decide with high accuracy whether a transaction is anomalous while protecting against private data leakage; S should be the only entity that learns the model's prediction. (p. 3)[^original]  
  <sub>anchor: "In addition, S should be the only entity which learns the model’s prediction."</sub>
- **descriptive / context**: The threat model assumes a single global adversary that may passively corrupt a subset of the parties, such as S, the aggregator and the banks, with restrictions on which parties can be corrupted together. (p. 3)[^original]  
  <sub>anchor: "We assume a single global adversary that is allowed to passively corrupt a subset of the parties"</sub>
- **descriptive / context**: Network-level observers are assumed to face secure channels and can learn at most unavoidable metadata, such as which bank is contacted at a time for a transaction; they see strictly less than the aggregator in training, so network-level adversaries are not the focus. (p. 4)[^original]  
  <sub>anchor: "Such an adversary can see strictly less than the aggregator during the training phase, hence we do not focus on tackling network level adversary."</sub>
- **descriptive / requirement**: All parties (S, aggregator and banks) are assumed honest-but-curious: they may try to learn sensitive information but otherwise follow the protocol; the architecture prevents banks from learning data from S beyond queried accounts. (p. 4)[^original]  
  <sub>anchor: "Our architecture strictly prevents banks from learning any data from S, besides the accounts that are queried."</sub>
- **descriptive / limitation**: Leakage of the banks' flags to S is minimal and bounded by an inherent leakage; for example, if S finds no anomaly but the federated label is 1, S may attribute this to the receiving account flag. (p. 4)[^original]  
  <sub>anchor: "if S based on its local information does not find an anomaly, but the model predicted label is 1, then S may attribute this to the receiving account flag."</sub>
- **descriptive / context**: Because an abnormal account is assumed unable to send funds (its bank freezes it), a transaction in the dataset implies the sending account has flag 0, and a bank learns the account queried in training and inference. (p. 4)[^original]  
  <sub>anchor: "a transaction being present in the data set implies that the sending account has flag 0"</sub>

## 4 TECHNICAL APPROACH

- **descriptive / method**: Setup assumes a public key infrastructure: all parties know each other's public keys; S encrypts account identifiers for banks with their keys and banks and S encrypt other information with S's key. (p. 4)[^original]  
  <sub>anchor: "S uses the public keys of banks to encrypt account identifiers for them"</sub>
- **descriptive / method**: In training, S randomly samples a batch of k transactions (k is a hyperparameter) and inputs each through its model twice, with the secret input set to normal and abnormal, producing updates u0(s) and u1(s). (p. 4)[^original]  
  <sub>anchor: "For each batch, S randomly samples a batch _𝐾_ of _𝑘_ transactions ( _𝑘_ being a hyperparameter)"</sub>
- **descriptive / method**: S sends the receiving account identifier to the receiving bank, and S, the aggregator and that bank run an MPC using secret sharing and oblivious transfer so that S and the aggregator obtain secret shares of the selected update without either learning its plaintext value. (p. 4)[^original]  
  <sub>anchor: "S, the aggregator and _𝐵𝑟_ ( _𝑠_ ) engages in a secure multiparty computation"</sub>
- **descriptive / method**: The selected update is computed as a linear combination of the two updates weighted by the bit b, using a single multiplication on shared or encrypted data, then converted to shares between S and the aggregator. (p. 4)[^original]  
  <sub>anchor: "using a single multiplication on the shared or encrypted data and then converted to shares between S and the aggregator"</sub>

## 3 THREAT MODEL

- **descriptive / context**: MPC is a main technique used to ensure that the private data of honest parties is not revealed to other parties. (p. 4)[^original]  
  <sub>anchor: "MPC is one of the main techniques leveraged by our approach to ensure that private data of honest parties"</sub>
- **descriptive / context**: The core privacy goal is that private data held by one party should not be leaked to a different party. (p. 4)[^original]  
  <sub>anchor: "The core privacy goal is that any private data held by some party should not be leaked"</sub>
- **descriptive / method**: Figure 3 describes the training phase: the aggregator adds noise to the transaction batch updates, and the parties reveal the aggregated, noised update to S via MPC. This is repeated for all transaction batches. (p. 5)[^original]  
  <sub>anchor: "This process is repeated for all transaction batches."</sub>
- **descriptive / limitation**: The inherent privacy leakage would be less deterministic when data sharing involves more than a single bit, such as risk scores. (p. 5)[^original]  
  <sub>anchor: "this inherent privacy leakage would not be as deterministic in more complex data sharing"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation" (2023-06-10). https://arxiv.org/abs/2310.04546
