---
type: Source Digest
title: 'FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive Financial Fraud Detection - part 1 of 1 (p. 1)'
description: 'Verified paraphrased digest, p. 1: Abstract'
resource: https://doi.org/10.1109/ojcs.2025.3543450
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
- model_monitoring
status: stable
source_id: academic-publisher-fraudgnn-rl-a-graph-neural-network-with-reinforceme
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2025-01-01'
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
  resource: https://doi.org/10.1109/ojcs.2025.3543450
  title: 'FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive Financial Fraud Detection'
  author: org:academic_publisher
  last_modified: '2025-01-01T00:00:00Z'
digest_points: 10
---

# FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive Financial Fraud Detection (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Traditional fraud detection methods struggle to keep pace with increasingly complex and interconnected financial systems and sophisticated fraudulent activity. (p. 1)[^original]  
  <sub>anchor: "traditional fraud detection methods struggle to keep pace with sophisticated fraudulent activities"</sub>
- **descriptive / method**: The article introduces FraudGNN-RL, a framework combining Graph Neural Networks (GNNs) with Reinforcement Learning (RL) for adaptive and context-aware financial fraud detection. (p. 1)[^original]  
  <sub>anchor: "combines Graph Neural Networks (GNNs) with Reinforcement Learning (RL) for adaptive and context-aware financial fraud detection"</sub>
- **descriptive / data or feature**: The approach models financial transactions as a dynamic graph in which entities such as users and merchants are nodes and transactions form edges. (p. 1)[^original]  
  <sub>anchor: "models financial transactions as a dynamic graph, where entities (e.g., users, merchants) are nodes and transactions form edges"</sub>
- **descriptive / method**: The authors propose a novel GNN architecture called Temporal-Spatial-Semantic Graph Convolution (TSSGC), intended to capture temporal patterns, spatial relationships and semantic information in transaction data simultaneously. (p. 1)[^original]  
  <sub>anchor: "We propose a novel GNN architecture, Temporal-Spatial-Semantic Graph Convolution (TSSGC)"</sub>
- **descriptive / method**: The RL component is implemented as a Deep Q-Network (DQN) that dynamically adjusts the fraud detection threshold and feature importance, aiming to adapt to evolving fraud patterns and minimise detection costs. (p. 1)[^original]  
  <sub>anchor: "implemented as a Deep Q-Network (DQN), dynamically adjusts the fraud detection threshold and feature importance"</sub>
- **descriptive / method**: A Federated Learning scheme is introduced to allow collaborative model training across multiple financial institutions while preserving data privacy. (p. 1)[^original]  
  <sub>anchor: "We further introduce a Federated Learning scheme to enable collaborative model training across multiple financial institutions"</sub>
- **descriptive / finding or result**: On a large-scale, real-world financial dataset, FraudGNN-RL reportedly outperforms state-of-the-art baselines, achieving a 97.3% F1-score. (p. 1)[^original]  
  <sub>anchor: "demonstrate that FraudGNN-RL outperforms state-of-the-art baselines, achieving a 97.3% F1-score"</sub>
- **descriptive / finding or result**: Compared with the best-performing baseline, FraudGNN-RL reportedly reduces false positives by 31%. (p. 1)[^original]  
  <sub>anchor: "reducing false positives by 31% compared to the best-performing baseline"</sub>
- **descriptive / finding or result**: The framework reportedly shows resilience to concept drift and adversarial attacks, maintaining high performance over extended periods. (p. 1)[^original]  
  <sub>anchor: "Our framework also shows remarkable resilience to concept drift and adversarial attacks, maintaining high performance over extended periods"</sub>
- **descriptive / finding or result**: The authors conclude that FraudGNN-RL offers a robust, adaptive and privacy-preserving solution for financial fraud detection. (p. 1)[^original]  
  <sub>anchor: "offers a robust, adaptive, and privacy-preserving solution for financial fraud detection in the era of Big Data"</sub>

---

[source overview](overview.md)

[^original]: Yiwen Cui, Xu Han, Jiaying Chen, Xinguang Zhang, Jingyun Yang, Xuguang Zhang, "FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive Financial Fraud Detection" (2025-01-01). https://doi.org/10.1109/ojcs.2025.3543450
