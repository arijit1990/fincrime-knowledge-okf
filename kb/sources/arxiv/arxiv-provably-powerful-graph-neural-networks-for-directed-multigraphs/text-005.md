---
type: Source Text
title: Provably Powerful Graph Neural Networks for Directed Multigraphs - part 5 of 5 (pp. 17-18)
description: 'Verbatim extracted text, pp. 17-18: Provably Powerful Graph Neural Networks for Directed Multigraphs > H Additional Subgraph Detection Results H.1 Additional GNN Baselines; Provably Powerful Graph Neural Networks for Directed Multigraphs > I Detailed AML Results'
resource: https://arxiv.org/abs/2306.11586
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-provably-powerful-graph-neural-networks-for-directed-multigraphs
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-06-20'
legal_status: unknown
part: 5
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.11586
  title: Provably Powerful Graph Neural Networks for Directed Multigraphs
  author: org:arxiv
  last_modified: '2023-06-20T00:00:00Z'
---

# Provably Powerful Graph Neural Networks for Directed Multigraphs

[previous part](text-004.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2023-06-20), part 5 of 5, pp. 17-18. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Provably Powerful Graph Neural Networks for Directed Multigraphs


### H Additional Subgraph Detection Results H.1 Additional GNN Baselines


#### H.2 Complex Patterns and Dataset Size


[p. 17]

|Model|Fan-in|Fan-out|Cycle|S-G|G-S|B-C|none|
|---|---|---|---|---|---|---|---|
|GIN (Xu et al. 2018; Hu et al. 2019)|40.65|64.89|44.44|51.46|47.24|34.85|4.31|
|GIN+ReverseMP (Jaume et al. 2019)|58.54|80.92|40.40|72.80|68.50|36.36|2.43|
|+Ports|67.48|91.60|48.48|82.85|84.51|51.52|1.08|
|+EgoIDs (Multi-GIN)|87.80|80.15|50.51|89.96|86.35|51.52|1.89|
|Multi-GIN+EU|88.62|95.42|57.58|88.28|94.49|57.58|1.35|
|Multi-PNA|85.37|93.13|61.62|93.72|92.65|54.55|0.54|

Table 13: Recall scores by money laundering pattern on AML Small HI dataset, where ground truth pattern labels are available. S-G stands for Scatter-Gather, G-S stands for Gather-Scatter, B-C stands for Bipartite, and none indicated illicit transactions that are not part of any standard money laundering pattern. The ground truth money laundering patterns are of varying sizes.

|Model|Fan-in|Fan-out|Cycle|S-G|G-S|B-C|none|
|---|---|---|---|---|---|---|---|
|GIN (Xu et al. 2018; Hu et al. 2019)|0.00|60.87|11.90|20.34|41.43|2.38|1.45|
|GIN+ReverseMP (Jaume et al. 2019)|14.29|36.96|26.19|37.29|34.29|28.57|5.58|
|+Ports|35.71|76.09|42.86|54.24|54.29|42.86|3.31|
|+EgoIDs (Multi-GIN)|42.86|56.52|28.57|45.76|51.43|40.48|0.83|
|Multi-GIN+EU|42.86|84.78|40.48|52.54|70.00|35.71|0.83|
|Multi-PNA|71.43|95.65|33.33|71.19|94.29|64.29|0.62|

Table 14: Recall scores by money laundering pattern on AML Small LI dataset, where ground truth pattern labels are available.

were not solved almost perfectly, namely C4, C5, C6, ScatterGather, and Biclique detection. Dataset sizes of 1024 up to 16384 are used, increasing by a factor of 2. All other graph generator settings are kept constant. In particular, we use the same average degree and average radius.

The results can be seen in Fig. 9, and specific values can be found in Table 9. One can see that increasing the training dataset size gradually increases the scores on all the complex tasks, with even 6-cycle detection reaching above 97% minority class F1 score. The starred results also show that restricting to a smaller set of tasks significantly improves performance.

For cycles, we further extended these experiments to cycles of length 10 and training datasets with 65536 nodes. These results can be seen in Table 10 and show similar trends with all cycle sizes reaching above 98% minority class F1 score with the largest training dataset.

#### H.3 Subgraph Detection with Unique Node IDs


We include additional subgraph detection results below. Firstly, we rerun the subgraph detection experiments with all GIN-based models with the addition of random unique node IDs as part of the input. The results can be seen in Table 12. This experiment shows that theoretical expressiveness does not always translate into better results in practice. Comparing the first row of the table with the first row of Table 1 reveals that random node IDs, although universal, are not effective for subgraph detection. The rest of the table shows the effect of adding adaptations. The trends are the same, and the results are similar to Table 1, but most of the scores are actually slightly lower with the node IDs. Note in particular that both port numbers and ego IDs (in addition to reverse message passing) are still needed to attain high scores for the complex

patterns. This highlights that although node IDs could easily provide either of these features, the neural network is not able to extract and use this information effectively. The results indicate that the adaptations offer the right inductive biases for the task.

#### H.4 Subgraph Detection with the Collapsed Multigraph


Secondly, we explore whether the directed multigraph input can be collapsed into a directed graph with weighted edges, where the edge weights indicate the number of parallel edges in the original multigraph. We rerun the subgraph detection experiments with all GIN-based models. The results of the collapsed multigraph experiments can be found in Table 11. The results are very similar to using the But importantly, note that port numbers are no longer needed to solve the tasks. For example, fan-in can now be solved perfectly without ports, and port numbers do not increase any of the scores significantly, whether added on top of GIN or GIN with reverse message passing. This is not surprising as all of these tasks can be solved easily on a weighted directed graph (given reverse message passing and ego IDs as needed). Indeed, collapsing the parallel edges of a multigraph in this way could be a valid option for some multigraph tasks. However, as soon as edges have non-additive features that are important for the task, this might no longer be an option. It might not be possible to summarize the features of parallel edges without losing valuable information.

### I Detailed AML Results


[pp. 17-18]

Ground truth money laundering pattern labels are available for a portion of the fraudulent transactions in the AML datasets. The remaining illicit transactions (without pattern

labels) do not belong to specific money laundering patterns; we might therefore expect worse recall scores for these transactions. Using these pattern labels, we calculate recall scores for each pattern type individually and present these results in Table 13 for AML Small HI and in Table 14 for AML Small LI.

From the tables, we can see that our models identify most of the laundering patterns leading to very high individual recall scores, though the cycle and bipartite recall scores could be further improved. This is likely due to the fact that our best-performing GNN models used only two message passing layers, making it impossible to detect longer cycles. Increasing the number of layers can increase the overall F1 scores, but also comes at a significant cost in terms of the runtime.

We can also immediately notice that the recall scores for illicit transactions that do not belong to any specific money laundering pattern (none) are close to 0%. This probably explains the low aggregate minority class F1 scores for Small LI (Table 2) where 71% of the laundering transactions are not part of laundering patterns. The equivalent value for Small HI is only 38%. These insights reveal just how effective the proposed approach is in detecting money laundering patterns.


---

[previous part](text-004.md) | [source overview](overview.md)

[^original]: arXiv, "Provably Powerful Graph Neural Networks for Directed Multigraphs" (2023-06-20). https://arxiv.org/abs/2306.11586
