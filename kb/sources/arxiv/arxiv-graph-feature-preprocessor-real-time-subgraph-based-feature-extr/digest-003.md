---
type: Source Digest
title: 'Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection - part 3 of 5 (pp. 6-8)'
description: 'Verified paraphrased digest, pp. 6-8: 4 Results; 5 Related Work'
resource: https://arxiv.org/abs/2402.08593
tags:
- academic_finding
- data_features
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-graph-feature-preprocessor-real-time-subgraph-based-feature-extr
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-02-13'
legal_status: unknown
part: 3
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:34Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:34Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:34Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2402.08593
  title: 'Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection'
  author: org:arxiv
  last_modified: '2024-02-13T00:00:00Z'
digest_points: 44
---

# Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-8) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4 Results

- **descriptive / method**: The paper evaluates the accuracy of its graph ML pipeline and other baselines trained on the datasets in Table 1, using minority-class F1 score as the accuracy measure, averaged across five runs with standard deviation reported. (p. 6)[^original]  
  <sub>anchor: "As a measure of accuracy, we use the minority-class F1 score. The F1 scores reported are averaged across five different runs."</sub>
- **descriptive / method**: The graph ML pipeline using LightGBM and XGBoost is referred to as GFP+LightGBM and GFP+XGBoost respectively. (p. 6)[^original]  
  <sub>anchor: "We refer to our graph ML pipeline that uses LightGBM and XGBoost as GFP+LightGBM and GFP+XGBoost, respectively."</sub>
- **descriptive / context**: The graph ML pipeline requires transactions to arrive in batches; for the AML datasets batch sizes of 128 and 2048 are used, and for the ETH Phishing dataset batch sizes of 128 and infinity. (p. 6)[^original]  
  <sub>anchor: "Our graph ML pipeline requires transactions to arrive in batches. For the AML datasets, the graph ML pipeline uses batch sizes of 128 and 2048."</sub>
- **descriptive / context**: A batch size of infinity makes all test-set transactions available to GFP in a single batch, which is essentially an offline solution that can give better accuracy because future transactions are visible during feature extraction. (p. 6)[^original]  
  <sub>anchor: "Using a batch size of ∞ essentially corresponds to an offline solution and, in principle, can lead to better accuracy because"</sub>
- **descriptive / context**: If real-time processing is required by an application, the batch size has to be constrained. (p. 6)[^original]  
  <sub>anchor: "However, if real-time processing capability is required by an application, the batch size will have to be constrained."</sub>
- **descriptive / context**: GNN baselines require the entire dataset to be in memory, making them effectively offline solutions with batch size infinity. (p. 6)[^original]  
  <sub>anchor: "Note that GNN baselines require the entire dataset to be available in memory, making it effectively an offline solution with batch size ∞."</sub>
- **descriptive / finding or result**: Table 4 reports minority-class F1 scores (%) for money laundering detection on AML datasets and phishing detection on ETH Phishing. GIN gets 28.70 on AML HI Small, 42.30 on AML HI Medium, NA on AML HI Large, 7.90 on AML LI Small, 3.86 on AML LI Medium, NA on AML LI Large, and 26.92 on ETH Phishing at batch infinity. (p. 7)[^original]  
  <sub>anchor: "GIN [35]|∞|28.70 ± 1.13|42.30 ± 0.44|NA|7.90 ± 2.78|3.86 ± 3.62|NA|∞|26.92 ± 7.52|"</sub>
- **descriptive / finding or result**: Table 4 reports GIN+EU scores of 47.73 (AML HI Small), 49.26 (AML HI Medium), 20.62 (AML LI Small), 6.19 (AML LI Medium) and 33.92 on ETH Phishing, with AML HI Large and AML LI Large not available. (p. 7)[^original]  
  <sub>anchor: "GIN+EU [4, 12]|∞|47.73 ± 7.86|49.26 ± 4.02|NA|20.62 ± 2.41|6.19 ± 8.32|NA|∞|33.92 ± 7.34|"</sub>
- **descriptive / finding or result**: Table 4 reports PNA scores of 56.77 (AML HI Small), 59.71 (AML HI Medium), 16.45 (AML LI Small), 27.73 (AML LI Medium) and 51.49 on ETH Phishing, with Large variants not available. (p. 7)[^original]  
  <sub>anchor: "PNA[22]|∞|56.77 ± 2.41|59.71 ± 1.91|NA|16.45 ± 1.46|27.73 ± 1.65|NA|∞|51.49 ± 4.29|"</sub>
- **descriptive / finding or result**: LightGBM alone scores 21.30 (AML HI Small), 18.60 (AML HI Medium), 24.50 (AML HI Large), 2.05 (AML LI Small), 3.3 (AML LI Medium), 4.04 (AML LI Large) and 13.74 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "LightGBM [43]|—|21.30 ± 0.30|18.60 ± 0.10|24.50 ± 0.20|2.05 ± 0.81|3.3 ± 0.48|4.04 ± 0.16|—|13.74 ± 0.54|"</sub>
- **descriptive / finding or result**: GFP+LightGBM with batch 128 scores 62.86 (AML HI Small), 59.48 (AML HI Medium), 58.03 (AML HI Large), 20.83 (AML LI Small), 24.74 (AML LI Medium), 23.67 (AML LI Large) and 40.17 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "GFP+LightGBM|128|62.86 ± 0.25|59.48 ± 0.15|58.03 ± 0.19|20.83 ± 1.50|24.74 ± 0.46|23.67 ± 0.11|128|40.17 ± 0.22|"</sub>
- **descriptive / finding or result**: GFP+LightGBM with batch 2048 scores 60.52 (AML HI Small), 56.12 (AML HI Medium), 54.76 (AML HI Large), 17.99 (AML LI Small), 21.06 (AML LI Medium), 22.65 (AML LI Large) and 51.00 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "GFP+LightGBM|2048|60.52 ± 0.59|56.12 ± 0.37|54.76 ± 0.08|17.99 ± 0.60|21.06 ± 0.08|22.65 ± 0.59|∞|51.00 ± 1.01|"</sub>
- **descriptive / finding or result**: XGBoost alone scores 19.75 (AML HI Small), 20.10 (AML HI Medium), 10.61 (AML HI Large), 0.21 (AML LI Small), 0.40 (AML LI Medium), 0.00 (AML LI Large) and 15.52 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "XGBoost [16]|—|19.75 ± 0.89|20.10 ± 0.22|10.61 ± 6.73|0.21 ± 0.22|0.40 ± 0.14|0.00 ± 0.00|—|15.52 ± 0.15|"</sub>
- **descriptive / finding or result**: GFP+XGBoost with batch 128 scores 63.23 (AML HI Small), 65.69 (AML HI Medium), 42.68 (AML HI Large), 27.28 (AML LI Small), 31.03 (AML LI Medium), 24.23 (AML LI Large) and 37.01 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "GFP+XGBoost|128|63.23 ± 0.17|65.69 ± 0.26|42.68 ± 12.93|27.28 ± 0.69|31.03 ± 0.22|24.23 ± 0.12|128|37.01 ± 2.45|"</sub>
- **descriptive / finding or result**: GFP+XGBoost with batch 2048 scores 64.77 (AML HI Small), 59.19 (AML HI Medium), 56.88 (AML HI Large), 28.25 (AML LI Small), 21.36 (AML LI Medium), 22.64 (AML LI Large) and 49.40 on ETH Phishing. (p. 7)[^original]  
  <sub>anchor: "GFP+XGBoost|2048|64.77 ± 0.47|59.19 ± 0.29|56.88 ± 0.21|28.25 ± 0.80|21.36 ± 0.90|22.64 ± 0.15|∞|49.40 ± 0.54|"</sub>
- **descriptive / finding or result**: Figure 8 shows the throughput (transactions per second) of the graph ML pipeline and GNN baselines; GFP+LightGBM and GFP+XGBoost were run on IBM Cloud Cascade Lake Xeon with 64 threads and GNNs on an NVIDIA Tesla V100 GPU, and the pipeline has higher throughput than GNN baselines at batch size 2048. (p. 7)[^original]  
  <sub>anchor: "We observe that our graph ML pipeline is able to achieve higher throughput than GNN baselines when it receives transactions in batches of 2048."</sub>
- **descriptive / finding or result**: Without graph-based features, the best F1 scores of LightGBM and XGBoost are 24.5% on AML HI datasets and 4.04% on AML LI datasets. (p. 7)[^original]  
  <sub>anchor: "Without our graph-based features, the maximum F1 score that LightGBM and XGBoost achieve is 24 _._ 5% for the AML HI datasets and 4 _._ 04% for the AML LI datasets."</sub>
- **descriptive / context**: The low baseline accuracy is attributed to highly imbalanced AML labels, with illicit transactions at most 0.13% of all transactions. (p. 7)[^original]  
  <sub>anchor: "the number of illicit transactions in these datasets is at most 0 _._ 13% of the total number of transactions (see Table 1)."</sub>
- **descriptive / finding or result**: The graph ML pipeline with graph-based features achieves up to 46% higher F1 scores than models using only basic features. (p. 7)[^original]  
  <sub>anchor: "achieves up to a 46% higher F1 scores than the models that use only basic features."</sub>
- **descriptive / finding or result**: GFP+XGBoost consistently achieves higher F1 scores than GNN baselines; compared with PNA, the best GNN baseline, it achieves up to 8% higher F1 for AML HI and up to 11.8% higher F1 for AML LI datasets. (p. 7)[^original]  
  <sub>anchor: "Compared to PNA, the GNN baseline with the highest accuracy, our graph ML pipeline with XGBoost achieves up to an 8% higher F1 score for AML HI datasets and up to an 11 _._ 8% higher F1 score for LI datasets."</sub>
- **descriptive / finding or result**: Table 5 ablation: adding fan-in and fan-out graph features improves minority-class F1 by more than 30% over basic transaction features only. (p. 7)[^original]  
  <sub>anchor: "We observe that including graph features based on fan-in and fan-out patterns already improves the minority class F1 score by more than 30%"</sub>
- **descriptive / finding or result**: Adding multi-hop pattern features (simple cycles, temporal cycles and scatter-gather patterns) further improves F1 by up to 4%. (p. 8)[^original]  
  <sub>anchor: "Including multi-hop graph pattern features, i.e., features based on cycles and scatter-gather patterns, further improves the F1 score by up to 4%."</sub>
- **descriptive / finding or result**: Adding vertex-statistics-based features lets the pipeline exceed the PNA baseline accuracy, and the authors conclude that each type of graph-based feature contributes to overall accuracy. (p. 8)[^original]  
  <sub>anchor: "Thus, each type of graph-based feature contributes to the overall accuracy of our graph ML pipeline."</sub>
- **descriptive / finding or result**: Table 5 ablation rows for AML HI Small: basic features 21.30 (LightGBM) and 19.75 (XGBoost) at both batch sizes; plus fan-in/fan-out 50.85 and 49.73 (LightGBM, batch 128 and 2048) and 56.88 and 59.71 (XGBoost); plus multi-hop 54.66 and 55.54 (LightGBM) and 58.60 and 61.01 (XGBoost); plus vertex-statistic 62.86 and 60.52 (LightGBM) and 63.23 and 64.77 (XGBoost). (p. 8)[^original]  
  <sub>anchor: "|+ fan-in/fan-out features|50.85 ± 0.83|49.73 ± 1.20|56.88 ± 0.66|59.71 ± 0.07|46.71 ± 0.17|50.59 ± 0.36|53.00 ± 0.08|55.25 ± 0.19|35.92 ± 1.96|40.46 ± 0.94|"</sub>
- **descriptive / finding or result**: Table 5 ablation rows for AML HI Medium: basic features 18.60 (LightGBM) and 20.10 (XGBoost); plus fan-in/fan-out 46.71 and 50.59 (LightGBM, batch 128 and 2048) and 53.00 and 55.25 (XGBoost); plus multi-hop 47.47 and 51.40 (LightGBM) and 55.42 and 55.92 (XGBoost); plus vertex-statistic 59.48 and 56.12 (LightGBM) and 65.70 and 59.19 (XGBoost). (p. 8)[^original]  
  <sub>anchor: "|+ multi-hop pattern features|54.66 ± 0.39|55.54 ± 0.55|58.60 ± 0.15|61.01 ± 0.24|47.47 ± 0.21|51.40 ± 0.15|55.42 ± 0.23|55.92 ± 0.26|39.46 ± 0.27|42.76 ± 0.48|"</sub>
- **descriptive / finding or result**: Table 5 ETH Phishing ablation: basic features 13.74 (LightGBM) and 15.52 (XGBoost); plus fan-in/fan-out 35.92 and 40.46; plus multi-hop 39.46 and 42.76; plus vertex-statistic 51.00 and 49.40. (p. 8)[^original]  
  <sub>anchor: "|+ vertex-statistic-based features|62.86 ± 0.25|60.52 ± 0.59|63.23 ± 0.17|64.77 ± 0.47|59.48 ± 0.15|56.12 ± 0.37|65.70 ± 0.26|59.19 ± 0.29|51.00 ± 1.01|49.40 ± 0.54|"</sub>
- **descriptive / finding or result**: Figure 9 shows the pipeline's streaming scatter-gather algorithm scales almost linearly with software threads when batch size is infinity; the speedup is relative to single-threaded execution. (p. 8)[^original]  
  <sub>anchor: "This figure also shows that our streaming scatter-gather algorithm, introduced in Section 2.2, scales almost linearly with the number of software threads when batch size is infinity."</sub>
- **descriptive / finding or result**: Average latency of processing batches of AML transactions is 30 ms for batch size 128 and 148 ms for batch size 2048, which the authors say makes GFP suitable for real-time processing. (p. 8)[^original]  
  <sub>anchor: "the average latency of processing batches of 128 and 2048 transactions from the AML dataset is 30 ms and 148 ms, respectively."</sub>
- **descriptive / finding or result**: Explainability: using the SHAP library, feature importance can be obtained for the gradient-boosting model's illicit flags; the two most important features in Figure 10 are the number of two-hop temporal cycles and the sum of money the target account received. (p. 8)[^original]  
  <sub>anchor: "the two most important features used for flagging a transaction as illicit in Figure 10 are the number of two-hop temporal cycles"</sub>
- **descriptive / context**: The authors state that explaining decisions is critical for trust in a fraud detection system because analysts can verify the system's decisions. (p. 8)[^original]  
  <sub>anchor: "Explaining the decision is critical for increasing trust in a fraud detection system because it allows analysts to verify the decisions of the system as needed."</sub>
- **descriptive / finding or result**: On the ETH Phishing dataset with batch size 128, graph-based features improve F1 by more than 20% for both LightGBM and XGBoost. (p. 8)[^original]  
  <sub>anchor: "When using a batch size of 128, our graph-based features enable F1-score improvements exceeding 20% for both LightGBM and XGBoost."</sub>
- **descriptive / finding or result**: Setting batch size to infinity raises GFP+LightGBM's ETH Phishing F1 to 51%, outperforming GIN+EU by 10% and achieving competitive accuracy with PNA. (p. 8)[^original]  
  <sub>anchor: "In that case, LightGBM with our graph-based features outperforms the GIN+EU baseline by 10% and achieves competitive accuracy with PNA."</sub>
- **descriptive / limitation**: Increasing batch size from 128 to infinity effectively makes the pipeline an offline solution; the optimal GFP configuration depends on application requirements and may require trading performance for accuracy. (p. 8)[^original]  
  <sub>anchor: "However, increasing the batch size from 128 to ∞ effectively makes our graph ML pipeline an offline solution."</sub>
- **descriptive / context**: The optimal configuration of GFP depends on the requirements of the end application and might require trading off performance for accuracy. (p. 8)[^original]  
  <sub>anchor: "In general, the optimal configuration of GFP depends on the requirements of the end application and might require trading off performance for accuracy."</sub>

## 5 Related Work

- **descriptive / context**: Graph machine learning is applied to financial transaction network analysis, fraud detection, drug discovery, molecular property prediction, genomics, recommender systems, social network analysis and knowledge graph relation prediction. (p. 8)[^original]  
  <sub>anchor: "Graph machine learning has applications in many different fields, including financial transaction network analysis"</sub>
- **descriptive / context**: Fraud detection systems TitAnt and Eddin et al. are graph machine learning systems that extract features from transaction graphs via node embeddings or random walks, which feed machine learning models predicting whether a transaction is fraudulent. (p. 8)[^original]  
  <sub>anchor: "Fraud detection systems TitAnt [11] and Eddin et al. [24] are graph machine learning systems that extract features from transaction graphs"</sub>
- **descriptive / context**: Cardoso et al. and Weber et al. apply GNNs to anti-money laundering; Kanezashi et al. apply GNNs to phishing detection on Ethereum; Rao et al. use a GNN to detect fraudulent transactions. (p. 8)[^original]  
  <sub>anchor: "Cardoso et al. [12] and Weber et al. [80] apply GNN to the anti-money laundering problem"</sub>
- **descriptive / context**: Graph Substructure Network by Bouritsas et al. uses pre-calculated subgraph pattern counts to improve GNN expressivity; GNNs could also count subgraph patterns, which could enable detecting financial crime patterns. (p. 8)[^original]  
  <sub>anchor: "Graph Substructure Network, proposed by Bouritsas et al. [8], takes advantage of pre-calculated subgraph pattern counts"</sub>
- **descriptive / limitation**: In contrast to the authors' work, GNNs cannot straightforwardly operate in a streaming manner and require the entire dataset at testing time. (p. 8)[^original]  
  <sub>anchor: "In contrast to our work, GNNs cannot straightforwardly operate in a streaming manner and require the entire dataset to be available at the time of testing."</sub>
- **descriptive / context**: Dynamic graph management is often required for real-time processing of financial transactions; STINGER, GraphTinker and Sortledton are dynamic graph structures supporting edge insertion and removal. (p. 8)[^original]  
  <sub>anchor: "Dynamic graph management is often required for real-time processing of financial transactions."</sub>
- **descriptive / limitation**: STINGER and GraphTinker cannot be directly used for financial transaction graphs because they do not support multiple edges with the same source and destination vertices. (p. 8)[^original]  
  <sub>anchor: "However, STINGER and GraphTinker cannot be directly used for representing financial transaction graphs because they do not support the maintenance of multiple edges"</sub>
- **descriptive / context**: Bing's distributed in-memory graph database A1 uses high-speed Remote Direct Memory Access to maintain an evolving graph with billions of vertices and edges. (p. 8)[^original]  
  <sub>anchor: "Bing’s distributed in-memory graph database A1 [10] leverages high-speed Remote Direct Memory Access"</sub>
- **descriptive / context**: LinkedIn's in-memory graph database enables low-latency reads and writes and supports N-ary relationships. (p. 8)[^original]  
  <sub>anchor: "Linkedin’s in-memory graph database [13] enables low latency read and write operations to the graph"</sub>
- **descriptive / context**: The authors' dynamic graph data structure does not need N-ary relationship support, so it can be implemented more simply. (p. 8)[^original]  
  <sub>anchor: "Our dynamic graph data structure does not require support for N-ary relationships, and thus can be implemented in a simpler manner."</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: arXiv, "Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection" (2024-02-13). https://arxiv.org/abs/2402.08593
