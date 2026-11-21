---
type: Source Digest
title: 'Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems - part 1 of 1 (p. 1)'
description: 'Verified paraphrased digest, p. 1: Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems > Focus; Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems > Contribution; Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems > Abstract'
resource: https://www.bis.org/publications/working-paper-1188-finding-needle-haystack-machine-learning-framework-anomaly-detection-payment-systems
tags:
- academic_paper
- alerts_triage
- international_standard
- intl
- ml_statistics
- transaction_behaviour
status: stable
source_id: bis-bcbs-finding-a-needle-in-a-haystack-a-machine-learning-framework-f
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: academic_paper
normative_force: international_standard
publication_date: '2024-05-15'
legal_status: current
part: 1
parts_total: 1
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T17:26:07Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T17:26:07Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T17:26:07Z'
sources:
- id: original
  resource: https://www.bis.org/publications/working-paper-1188-finding-needle-haystack-machine-learning-framework-anomaly-detection-payment-systems
  title: 'Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems'
  author: org:bis_bcbs
  last_modified: '2024-05-15T00:00:00Z'
digest_points: 13
---

# Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Focus

- **descriptive / context**: High-value payment systems (HVPS) are described as a central piece of a country's financial infrastructure. The paper proposes a novel machine learning framework for real-time transaction monitoring in these systems. (p. 1)[^original]  
  <sub>anchor: "We propose a novel machine learning framework for real-time transaction monitoring in these systems."</sub>
- **descriptive / context**: Because of the substantial volume of high-value payments settled each day and the scarcity of actual anomalous transactions, detecting anomalies in HVPS is likened to finding a needle in a haystack. (p. 1)[^original]  
  <sub>anchor: "the scarcity of actual anomalous transactions"</sub>
- **descriptive / method**: The framework is tested using artificially manipulated transactions and payments data from the Canadian high-value payment system. (p. 1)[^original]  
  <sub>anchor: "We test this framework using artificially manipulated transactions and payments data from the Canadian high-value payment system."</sub>

## Contribution

- **descriptive / finding or result**: The key strength of the framework is that it can identify anomalies in high-frequency payments data, particularly when anomalies are unknown a priori. Its strength derives from the layered approach, and it can be used for different applications in finance. (p. 1)[^original]  
  <sub>anchor: "particularly when anomalies are unknown a priori"</sub>
- **descriptive / finding or result**: The machine learning algorithm in the first layer achieves a detection rate of 93%, described as a significant improvement over commonly used econometric models. (p. 1)[^original]  
  <sub>anchor: "achieves a detection rate of 93%, which is a significant improvement over commonly used econometric models"</sub>
- **descriptive / finding or result**: The algorithm in the second layer marks the artificially manipulated transactions as nearly twice as suspicious as the original transactions. Scenario analyses are said to demonstrate that the framework is flexible enough to be applied to different payment system designs. (p. 1)[^original]  
  <sub>anchor: "marks the artificially manipulated transactions as nearly twice as suspicious as the original transactions"</sub>

## Abstract

- **descriptive / method**: In the first layer a supervised ML algorithm identifies and separates 'typical' payments from 'unusual' payments; in the second layer only the 'unusual' payments are run through an unsupervised ML algorithm for anomaly detection. (p. 1)[^original]  
  <sub>anchor: "a supervised ML algorithm is used to identify and separate 'typical' payments from 'unusual' payments"</sub>
- **descriptive / finding or result**: The abstract reports that the first-layer ML algorithm achieves a 93% detection rate, a significant improvement over commonly-used econometric models, and that the second-layer algorithm marks the artificially manipulated transactions as nearly twice as suspicious as the original transactions, which the authors say proves its effectiveness. (p. 1)[^original]  
  <sub>anchor: "marking a significant improvement over commonly-used econometric models"</sub>

## Focus

- **descriptive / method**: In the proposed two-layer framework for monitoring high-value payment systems, the first layer is a supervised machine learning algorithm that sorts 'typical' payments from 'unusual' ones. (p. 1)[^original]  
  <sub>anchor: "First, a supervised machine learning algorithm identifies and separates"</sub>
- **descriptive / method**: In the second layer, solely the payments judged unusual by the first layer are passed to an unsupervised machine learning algorithm whose job is to find anomalies. (p. 1)[^original]  
  <sub>anchor: "Second, only the unusual payments are run through an unsupervised machine learning algorithm to detect anomalies"</sub>

## Contribution

- **permissive / context**: Operators and overseers of payment systems may apply the framework to spot cyber attacks or operational outages whose going unnoticed could have serious consequences for the financial system. (p. 1)[^original]  
  <sub>anchor: "Payment system operators and overseers may use it to detect cyber attacks or operational outages that, if left undetected"</sub>
- **permissive / context**: The framework could further be applied to pick up early signs of financial stress at individual financial institutions, or to screen transactions as part of countering money laundering and terrorist financing. (p. 1)[^original]  
  <sub>anchor: "The framework could also be used to detect early signs of financial stress at individual financial institutions"</sub>

## Abstract

- **permissive / context**: The abstract says system operators and overseers can use the framework to find anomalous transactions that, were they caused by a cyber attack or operational outage and went undetected, might seriously affect the HVPS, its participants and the wider financial system. (p. 1)[^original]  
  <sub>anchor: "This framework can be used by system operators and overseers to detect anomalous transactions"</sub>

---

[source overview](overview.md)

[^original]: Bank for International Settlements / Basel Committee, "Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems" (2024-05-15). https://www.bis.org/publications/working-paper-1188-finding-needle-haystack-machine-learning-framework-anomaly-detection-payment-systems
