---
type: Source Digest
title: 'BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis - part 3 of 3 (pp. 11-14)'
description: 'Verified paraphrased digest, pp. 11-14: BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _F. Feature Analysis_; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _A. Preliminary Analysis_; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _B. Dataset Improvement_; and 3 more sections'
resource: https://arxiv.org/abs/2204.05746
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-babd-a-bitcoin-address-behavior-dataset-for-pattern-analysis
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-12-28'
legal_status: unknown
part: 3
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2204.05746
  title: 'BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis'
  author: org:arxiv
  last_modified: '2023-12-28T00:00:00Z'
digest_points: 21
---

# BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 11-14) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## F. Feature Analysis

- **descriptive / finding or result**: Table VII reports KNN, RF and XGB accuracy, precision, recall and F1-score with SI+LSI features versus the new selected features: KNN 0.9324 vs 0.9444 accuracy, RF 0.9598 vs 0.9635, XGB 0.9671 vs 0.9713 (new features give higher scores for every classifier). (p. 11)[^original]  
  <sub>anchor: "KNNnew|0.9444|0.9409|0.9444|0.9424|"</sub>
- **descriptive / finding or result**: For Fig. 4(b), the feature's data distributions are similar with one peak that is not apparent, and types 2, 5, 6, 8 and 9 are almost the same; the authors think this explains why the feature ranks low in feature importance. (p. 11)[^original]  
  <sub>anchor: "For Fig. 4(b), the data distributions are similar and have one peak that is not apparent."</sub>
- **descriptive / finding or result**: For Fig. 4(c), types 1, 3, 10 and 11 look similar, while type 8 has the most distinct distribution. (p. 11)[^original]  
  <sub>anchor: "In Fig. 4(c), we can observe that there are several types that are similar."</sub>
- **descriptive / finding or result**: For Fig. 4(d), types 7 and 8 are unique; types 0 and 1 are similar, types 1, 3, 6 and 11 are similar, and types 2, 4, 5, 8 and 10 are similar, which the authors suggest explains why this feature is not in the top 10 influential features. (p. 11)[^original]  
  <sub>anchor: "For Fig. 4(d), the data distribution of types 7 and 8 are unique to other types."</sub>
- **descriptive / finding or result**: For Fig. 4(e), all types have clearly different distribution shapes, so this feature can easily distinguish address types; differences appear in number of peaks, peak location, shape and symmetry. (p. 11)[^original]  
  <sub>anchor: "In Fig. 4(e) data distributions of all types have obvious different shapes"</sub>
- **descriptive / finding or result**: The authors selected S2-3, a feature highly correlated with S2-2, to compare distributions; most same-type features have similar shapes, with partial similarity for types 0, 1 and 12, which the authors say explains the high S2-2/S2-3 correlation in the heatmap. (p. 12)[^original]  
  <sub>anchor: "There are some with partially similar shapes, such as types 0, 1, and 12."</sub>
- **descriptive / context**: The authors list open questions for future work: how to use feature value distributions to extract novel meaningful features, and whether an address can carry more than one label because of overlapping feature distributions across address types. (p. 12)[^original]  
  <sub>anchor: "And is it possible for an address to have more than one label due to there being overlapping"</sub>

## A. Preliminary Analysis

- **descriptive / finding or result**: Table VIII gives PDIa1-3 average, maximum, minimum and median: darknet market average 2.1, max 14, min 1, median 2; money laundering average 2, max 4, min 1, median 2; Ponzi average 606.4, max 3,939, min 2, median 74. (p. 12)[^original]  
  <sub>anchor: "|Darknet Market|2.1|14|1|2|"</sub>
- **descriptive / finding or result**: The Ponzi median is higher than the other types because Ponzi schemes need many people to keep paying an address to sustain the fraud. (p. 12)[^original]  
  <sub>anchor: "The median of PDIa1-3 of Ponzi is higher than others because Ponzi needs a lot of people"</sub>
- **descriptive / finding or result**: Money laundering addresses show low transaction frequency per address, since launderers must hide the movement of Bitcoin flows; darknet market transactions are few due to high threshold, high risk and high cost. (p. 12)[^original]  
  <sub>anchor: "while the frequency of money laundering is quite low for a single address"</sub>

## B. Dataset Improvement

- **descriptive / finding or result**: PDI-related features perform poorly in the classification task, and the information they provide is limited because their final status is not the most important feature of Bitcoin address transactions and they cover only the first layer. (p. 12)[^original]  
  <sub>anchor: "We can see from 4(b) that the effect of _PDI_ related features is bad"</sub>
- **descriptive / limitation**: The key open issue for this growth-pattern approach is how to choose the time interval and how to construct suitable subgraphs. (p. 12)[^original]  
  <sub>anchor: "The key issue of this study is how to choose the time interval and how to construct suitable subgraphs."</sub>

## VII. CONCLUSION AND FUTURE WORK

- **descriptive / method**: The paper proposes a framework for Bitcoin address behaviour pattern analysis on a directed heterogeneous multigraph Bitcoin transaction graph, built from the BABD-13 dataset. (p. 12)[^original]  
  <sub>anchor: "we proposed a framework for Bitcoin address behavior pattern analysis"</sub>
- **descriptive / method**: The authors propose a method to generate k-hop subgraphs for an address node from the whole transaction graph in order to extract LSI features. (p. 12)[^original]  
  <sub>anchor: "We also proposed a novel approach to generate _k_ -hop subgraph for an address node"</sub>
- **descriptive / finding or result**: Five common machine learning models evaluated on BABD-13 achieved accuracy between 93.24% and 97.13%. (p. 12)[^original]  
  <sub>anchor: "We then used BABD-13 to evaluate 5 common machine learning models and achieved an accuracy rate of between 93.24% and 97.13%."</sub>

## A. Preliminary Analysis

- **descriptive / method**: The authors use PDI to show how the features and the address-type definitions are applied to analyse behaviour patterns. They choose darknet market, money laundering and Ponzi addresses, with their total degrees (PDIa1-3), as examples. (p. 12)[^original]  
  <sub>anchor: "We choose darknet market, money laundering, and Ponzi with their total degrees"</sub>

## B. Dataset Improvement

- **descriptive / context**: The authors state that they consider it possible to analyse regular growth patterns of Bitcoin addresses within the same time interval and extract information from them as new features that could be added to PDI. (p. 12)[^original]  
  <sub>anchor: "we consider that it is possible to analyze the regular pattern of the growth"</sub>

## VII. CONCLUSION AND FUTURE WORK

- **permissive / recommendation**: The authors note that, if better performance is wanted, BABD-13 can also be simplified. (p. 12)[^original]  
  <sub>anchor: "If we wish to achieve better performance, we can also simplify BABD-13."</sub>
- **descriptive / context**: Future work includes further study of BABD-13 to find more features and characteristics and to mine patterns of different Bitcoin address types. (p. 13)[^original]  
  <sub>anchor: "First, BABD-13 can be studied further in order to help us determine other useful features"</sub>
- **descriptive / context**: The authors plan to extend the framework from address behaviour analysis to Bitcoin transaction mode analysis and combine the two frameworks. (p. 13)[^original]  
  <sub>anchor: "we are also exploring how we can extend our proposed framework from Bitcoin address behavioral analysis"</sub>
- **descriptive / method**: The authors consider designing a method to identify entities from the directed heterogeneous multigraph transaction graph to distinguish and analyse different entities. (p. 13)[^original]  
  <sub>anchor: "we also consider designing a method to identify entities"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: Yuexin Xiang, Yuchen Lei, Bao Fu Ding, Tiantian Li, Qingqing Yang, Wenmao Liu et al., "BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis" (2023-12-28). https://arxiv.org/abs/2204.05746
