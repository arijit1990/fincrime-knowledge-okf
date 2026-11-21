---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 5 of 10 (pp. 21-25)'
description: 'Verbatim extracted text, pp. 21-25: 5 Results and Discussion > 5.2.2 IBM Data; 5 Results and Discussion > 5.3 Sensitivity to the Pre-processing Step'
resource: https://arxiv.org/abs/2506.04292
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-garg-aml-against-smurfing-a-scalable-and-interpretable-graph-bas
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-04-06'
legal_status: unknown
part: 5
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 5 of 10, pp. 21-25. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 5 Results and Discussion


### 5.2.2 IBM Data


[p. 21]

|ore rows, Precision and F1 use the rulelt excluding GraphSAGE is underlined.|.9AUC-PRP@10000.0000.0000.0030.0000.0050.0000.0680.0020.0040.0000.0000.0000.0030.0000.0050.0000.0170.000––––––––––––––––––––––––––––––––––––|
|---|---|
|ML scresu|ut-off 0AUC-ROC50.091.383.859.964.850.074.192.579.5––––––––––––––––––|
|RG-Ae best|CF10.0000.0000.0000.0000.0000.0000.0000.0000.000––––––––––––––––––|
|GAold; th|Preci-sion0.0000.0000.0000.0000.0000.0000.0000.0000.000––––––––––––––––––|
|he twos in b|P@10000.0000.0000.0000.0020.0000.0000.0010.0000.0090.0000.0000.0000.0000.0000.0000.0000.0000.0010.0000.0000.000––––––|
|For tumn i|.5AUC-PR0.0020.0030.0040.0120.0030.0020.0050.0211.5830.0000.0010.0010.0000.0010.0000.0010.0050.0980.0000.0000.000––––––|
|taset.er col|ut-off 0AUC-ROC50.068.068.451.359.350.069.185.796.050.059.060.850.039.550.067.196.899.850.041.640.8––––––|
|rge dasult p|CF10.0000.0000.0000.0000.0000.0000.0000.0000.0010.0000.0000.0000.0000.0000.0000.0000.0000.0020.0000.0000.000––––––|
|LI-Labest re|Preci-sion0.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0010.0000.0000.000––––––|
|r the The|P@10000.0030.0090.0070.0250.0240.0380.0260.0270.4800.0010.0000.0000.0000.0020.0020.0000.0050.0870.0000.0000.0000.0050.0010.0030.0020.0000.190|
|offs foa cut.|.1AUC-PR0.2160.2550.2080.3610.8600.4240.9890.63018.3280.0080.0090.0100.0080.0130.0110.0210.10916.3850.0150.0180.0180.0220.0450.0220.0460.12232.092|
|d cut-end on|ut-off 0AUC-ROC50.055.147.255.480.755.381.876.996.950.059.560.949.960.250.665.187.798.650.058.859.649.865.351.071.389.799.6|
|rns ant dep|CF10.0000.0060.0050.0000.0000.0010.0000.0080.0360.0000.0000.0000.0000.0000.0000.0000.0010.0120.0000.0000.0000.0000.0030.0000.0010.0010.030|
|h pattedo no|Preci-sion0.0000.0030.0030.0000.0000.1000.0000.0040.0180.0000.0000.0000.0000.0000.0000.0000.0000.0060.0000.0000.0000.0000.0020.0000.0000.0000.015|
|Table 13: Performance comparison across grapscore_>_0_._5; AUC-ROC, AUC-PR and P@1000|Model_Is Laundering_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)_Gather-scatter_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)_Scatter-gather_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)|

[p. 22]

Critical difference diagram for average rank according to the AUC-ROCPattern: laundering3 4 5 6 7GARG-AML Undir. Boost (2.41) (7.03) AutoAuditGARG-AML Undir. Tree (2.62) (6.86) FlowScopeGARG-AML Dir. Boost (2.91) (6.19) GARG-AML DirectedGARG-AML Dir. Tree (3.09) (4.89) GARG-AML UndirectedPattern: separate3 4 5 6GARG-AML Undir. Tree (2.45) (6.67) FlowScopeGARG-AML Undir. Boost (2.52) (6.21) GARG-AML DirectedGARG-AML Dir. Boost (3.64) (5.76) AutoAuditGARG-AML Dir. Tree (3.73) (5.02) GARG-AML UndirectedPattern: new_mules3 4 5 6 7GARG-AML Undir. Tree (2.55) (7.62) AutoAuditGARG-AML Dir. Tree (2.60) (6.56) FlowScopeGARG-AML Dir. Boost (2.72) (6.36) GARG-AML DirectedGARG-AML Undir. Boost (2.72) (4.87) GARG-AML UndirectedPattern: existing_mules3 4 5 6GARG-AML Undir. Tree (2.88) (6.77) AutoAuditGARG-AML Undir. Boost (3.14) (6.15) GARG-AML UndirectedGARG-AML Dir. Tree (3.73) (4.98) GARG-AML DirectedGARG-AML Dir. Boost (3.84) (4.50) FlowScope

Figure 8: Critical difference plots of the average ranks according to the AUC-ROC across patterns.

For the lower cut-off values, we see a significant improvement of AUC-PR across the tree-based models. This results from the models being able to better capture the interaction among a node’s GARG-AML score and those of its neighbours. This reduces the false positives compared to the base score, resulting in a much higher AUC-PR. Therefore, on lower cut-offs, we conclude that the tree-based methods are better suited for smurfing detection.

For the highest cut-offs, the base undirected GARG-AML score reaches an AUC-ROC above 80% for the full ‘Is Laundering’ label and for several patterns. In these cases, only clients are labelled that have 90% or more of their transactions involved in money laundering. Therefore, these patterns closely resemble pure smurfing, making them easily recognisable by GARG-AML.

The tree-based models, on the other hand, seem to perform poorly at these highest cut-offs. The class imbalance (see also Table 7 and Table 8) is too extreme in these cases, resulting in the model’s inability to train properly. This is most apparent on the LI-Large data at cut-off 0.9, where only the ‘Is Laundering’ label has any positives (very few; see Table 8) and the tree-based models reach an AUC-ROC of only 50–74%. In this extreme case, the base undirected GARG-AML score (AUC-ROC 91 _._ 3%) is on par with GraphSAGE using topology only (92 _._ 5%) and above GraphSAGE with attributes (79 _._ 5%). The undirected tree-based model has the highest AUC-PR and P@1000 (0 _._ 068% and 0 _._ 002, versus 0 _._ 017% and 0 _._ 000 for GraphSAGE with attributes), even though its AUC-ROC is low. Since these values rest on very few positive accounts, they should be read as indicative only. We therefore conclude that GARG-AML remains competitive with GraphSAGE when labels are extremely scarce, not that it outperforms it.

A general trend observed across the experiments is the counter-intuitive underperformance of the directed version of GARG-AML. It seems that the definition of the score in Equation (14) misses an important part of smurfs. The final score works well from the point of view of the sender, but is less suited when looking at the intermediate smurfing accounts. We give more details on the inherent shortcoming of the directed GARG-AML score in A.3. Solving this, however, would result in the definition of a collection of rules trying to cover each case individually. Future work should build upon the idea of the nine blocks, and combine these with more advanced methods to come to meaningful results.

[p. 23]

Critical difference diagram for average rank according to the AUC-PRPattern: laundering2 3 4 5 6 7GARG-AML Undir. Boost (2.11) (6.82) FlowScopeGARG-AML Undir. Tree (2.57) (6.79) AutoAuditGARG-AML Dir. Boost (2.85) (6.31) GARG-AML DirectedGARG-AML Dir. Tree (3.48) (5.07) GARG-AML UndirectedPattern: separate3 4 5 6GARG-AML Undir. Boost (2.53) (6.62) FlowScopeGARG-AML Undir. Tree (2.65) (6.47) GARG-AML DirectedGARG-AML Dir. Boost (3.29) (5.52) AutoAuditGARG-AML Dir. Tree (3.51) (5.41) GARG-AML UndirectedPattern: new_mules3 4 5 6 7GARG-AML Undir. Boost (2.41) (7.64) AutoAuditGARG-AML Dir. Boost (2.43) (7.11) FlowScopeGARG-AML Undir. Tree (2.52) (5.86) GARG-AML DirectedGARG-AML Dir. Tree (2.80) (5.23) GARG-AML UndirectedPattern: existing_mules3 4 5 6 7GARG-AML Undir. Boost (2.90) (7.05) AutoAuditGARG-AML Undir. Tree (2.95) (6.05) GARG-AML UndirectedGARG-AML Dir. Boost (3.24) (5.21) GARG-AML DirectedGARG-AML Dir. Tree (3.90) (4.70) FlowScope

Figure 9: Critical difference plots of the average ranks according to the AUC-PR across patterns.

### 5.3 Sensitivity to the Pre-processing Step


[pp. 23-24]

The main pre-processing step of GARG-AML involves applying clustering via the Louvain method and removing inter-community edges. This might remove certain money laundering transactions if these are between nodes in different communities. We analyse different resolution parameters and include an evaluation where hubs are removed instead. Removal of hubs can be interpreted as a bank removing the largest clients (often big utility/insurance/retail companies), assuming that money laundering will most likely not go through these firms. Our analysis covers the impact on community size (for the Louvain method only), edges removed, calculation time and predictive performance when the resolution parameter is varied, and when the pre-processing step is skipped altogether.

Table 14 shows that each method removes some money laundering transactions. The hub removal removes around 10% of all money laundering transactions, but these are almost exclusively among the ‘Not Classified’ laundering transactions. The Louvain method, on the other hand, affects around one in three laundering transactions and this across most patterns. Only for the scatter-gather pattern, our main pattern of interest, do most transactions stay in the network.

We analyse the difference in AUC-ROC and AUC-PR across these configurations. Given that the value of the AUC-PR depends on the prevalence of the labels (a random model has AUC-PR equal to the relative number of positive labels), we divide the AUC-PR by the label prevalence to have a fair comparison. Otherwise, removing nodes would change the AUC-PR values even if the model performance stays stable.

The effect on performance is given in Figure 10 for the HI-Small dataset. The patterns are different for low cut-off and high cut-off levels. Therefore, the results show that there is no single strategy best for all situations.

At lower cut-off levels, i.e., a small portion of a node’s transactions involved in money laundering leads to a money laundering label, the performance is in general higher in networks where clustering is applied. At cut-off 0, higher resolution (smaller communities) is correlated with higher performance. In this case, even a single transaction results in the node being labelled. The other transactions seem to be adding noise to the data. So, removing these and only keeping those within a small, close-knit community seems to result in much clearer laundering patterns.

Table 14: Percentage of each pattern’s edges discarded by the pre-processing on HI-Small; _n_ is the pattern’s edge count. Hub removal deletes the _k_ highest-degree accounts and runs no community detection; _r_ is the Louvain resolution, _†_ the setting used in the main experiments. Pattern rows over-count 87 edges belonging to attempts of two types.

[p. 24]

|||Hu(|b remotop_k_)|val|L|ouvain|resolu|tion (_r_|)|
|---|---|---|---|---|---|---|---|---|---|
|Pattern|_n_|5|10|100|1|5|10_†_|20|50|
|_GARG-AML targets_||||||||||
|Gather-scatter|661|0.0|0.0|0.0|49.2|58.7|57.0|58.4|60.7|
|Scatter-gather|601|0.0|0.0|0.0|22.5|9.7|4.3|1.7|0.7|
|_Other injected patte_|_rns_|||||||||
|Fan-out|331|0.0|0.0|0.0|45.3|48.9|48.3|50.8|48.3|
|Fan-in|309|0.0|0.0|0.0|47.9|55.0|55.0|57.9|59.2|
|Cycle|265|0.0|0.0|0.8|36.2|39.6|35.1|27.9|29.4|
|Bipartite|252|0.0|0.0|0.0|29.0|32.9|32.5|30.6|29.0|
|Stack|446|0.0|0.0|0.0|35.2|42.2|37.2|37.0|37.0|
|Random|181|0.0|0.0|0.0|38.7|44.2|33.7|36.5|37.0|
|Not Classified|1,930|23.6|28.9|32.5|4.6|19.9|24.4|29.4|34.9|
|All flagged edges|4,889|9.3|11.4|12.9|25.4|33.1|32.8|34.6|36.9|
|All graph edges|644,246|4.5|5.5|7.1|6.0|19.6|22.8|28.6|31.6|

[pp. 24-25]

Undirected Directedcut-off 0 cut-off 0.1 cut-off 0.5 cut-off 0.96,357 positives 2,294 positives 104 positives 69 positives0.80.60.41.0 1.42.001.75 30.9 1.21.5020.8 1.0 1.251.00 1none 1 5 10† 20 50 5 10 100 none 1 5 10† 20 50 5 10 100 none 1 5 10† 20 50 5 10 100 none 1 5 10† 20 50 5 10 100Louvain r top-k hubs Louvain r top-k hubs Louvain r top-k hubs Louvain r top-k hubscomputation time per setting (the same at every cut-off; one run each)3,8863,1313,0762,4651,000 597472 437 462560442 380 325 191 173120100 1569476none 1 5 10† 20 50 5 10 100Louvain r top-k hubsLouvain resolution r (none = no reduction; † published) · number of hubs removed k, no LouvainAUC-ROCAUC-PR / prevalencestage-1 runtime (s)

Figure 10: Sensitivity of the GARG-AML score on HI-Small to the pre-processing: AUC-ROC (top) and AUC-PR relative to prevalence (middle) at four label cut-offs, and stage-1 runtime in seconds (bottom; one run per setting, independent of the cut-off). Undirected in blue, directed in orange. “none” is no Louvain reduction, numbers are Louvain resolutions († published, _r_ = 10); right of the dashed line, the top- _k_ hubs are removed instead. No model is fitted. Dotted lines mark a random ranking.

Figure 11: Smurfing over multiple banks. The (i)-icon indicates that the main (blue) bank has all client information about the corresponding account. The dotted lines indicate that the bank is unaware of these transactions/accounts.

[p. 25]

At higher cut-off levels, the best models are those based on the full network or the networks where only a few hubs have been deleted. Labels are only assigned if most of the transactions are involved in money laundering. Removing transactions across communities gets rid of important information in these cases.

The main trade-off to be made is that lower resolution limits, i.e., larger communities, or fewer deleted hubs come at the cost of longer calculation times. We see that removing hubs is the most effective in reducing calculation time, even though the number of removed edges is limited. Increasing the resolution limits, on the other hand, reduces the calculation time dramatically at first, but these improvements flatten out past a resolution limit of 10.


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
