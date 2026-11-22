---
type: Source Digest
title: Bitcoin Money Laundering Detection via Subgraph Contrastive Learning - part 1 of 1 (p. 1)
description: 'Verified paraphrased digest, p. 1: Abstract'
resource: https://doi.org/10.3390/e26030211
tags:
- academic_finding
- academic_paper
- global_academic
- ml_statistics
- virtual_assets
status: stable
source_id: academic-publisher-bitcoin-money-laundering-detection-via-subgraph-con
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2024-02-28'
legal_status: unknown
part: 1
parts_total: 1
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
  resource: https://doi.org/10.3390/e26030211
  title: Bitcoin Money Laundering Detection via Subgraph Contrastive Learning
  author: org:academic_publisher
  last_modified: '2024-02-28T00:00:00Z'
digest_points: 8
---

# Bitcoin Money Laundering Detection via Subgraph Contrastive Learning (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The abstract notes that cryptocurrency money laundering has grown in severity and that graph neural networks have produced promising results for cryptocurrency fraud detection. (p. 1)[^original]  
  <sub>anchor: "The rapid development of cryptocurrencies has led to an increasing severity of money laundering activities."</sub>
- **descriptive / limitation**: The authors state that many existing methods mainly perform node classification, detecting individual illicit transactions, rather than uncovering behavioral pattern differences among money laundering groups. (p. 1)[^original]  
  <sub>anchor: "many existing methods predominantly focus on node classification, i.e., detecting individual illicit transactions"</sub>
- **descriptive / context**: The authors characterise Bitcoin money laundering as organized, heterogeneous and noisy, and aim to address the challenges this presents. (p. 1)[^original]  
  <sub>anchor: "we tackle the challenges presented by the organized, heterogeneous, and noisy nature of Bitcoin money laundering"</sub>
- **descriptive / method**: The paper proposes Bit-CHetG, a subgraph-based contrastive learning algorithm for heterogeneous graphs, to perform money laundering group detection. (p. 1)[^original]  
  <sub>anchor: "We propose a novel subgraph-based contrastive learning algorithm for heterogeneous graphs, named Bit-CHetG"</sub>
- **descriptive / method**: Bit-CHetG uses predefined metapaths to build homogeneous subgraphs of wallet addresses and transaction records from the address-transaction heterogeneous graph. (p. 1)[^original]  
  <sub>anchor: "we employ predefined metapaths to construct the homogeneous subgraphs of wallet addresses and transaction records"</sub>
- **descriptive / method**: Bit-CHetG applies graph neural networks separately to extract topological embeddings of transaction subgraphs and associated address representations of transaction nodes. (p. 1)[^original]  
  <sub>anchor: "we utilize graph neural networks to separately extract the topological embedding representations of transaction subgraphs"</sub>
- **descriptive / method**: Supervised contrastive learning is used to reduce the effect of noise by pulling together transaction subgraphs of the same class and pushing apart subgraphs of different classes. (p. 1)[^original]  
  <sub>anchor: "supervised contrastive learning is introduced to reduce the effect of noise, which pulls together the transaction subgraphs"</sub>
- **descriptive / finding or result**: The authors report that their proposed Bit-CHetG improves the Micro F1 Score by at least 5% compared with other methods, in experiments on two real-world datasets with homogeneous and heterogeneous graphs. (p. 1)[^original]  
  <sub>anchor: "the Micro F1 Score of our proposed Bit-CHetG is improved by at least 5% compared to others"</sub>

---

[source overview](overview.md)

[^original]: Shiyu Ouyang, Qianlan Bai, Hui Feng, Bo Hu, "Bitcoin Money Laundering Detection via Subgraph Contrastive Learning" (2024-02-28). https://doi.org/10.3390/e26030211
