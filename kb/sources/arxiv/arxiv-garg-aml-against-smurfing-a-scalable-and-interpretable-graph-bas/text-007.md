---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 7 of 10 (pp. 29-39)'
description: 'Verbatim extracted text, pp. 29-39: References; A Illustration GARG-AML; A Illustration GARG-AML > A.1 Undirected Calculations; and 4 more sections'
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
part: 7
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 7 of 10, pp. 29-39. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## References


[pp. 29-30]

- Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Claudio Bellei, Tom Robinson, and Charles E. Leiserson. Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics. arXiv preprint arXiv:1908.02591, 2019. URL `https://arxiv.org/abs/1908.02591` .

- Sarah N Welling. Smurfs, money laundering, and the federal criminal law: the crime of structuring transactions. _Fla. L. Rev._ , 41:287, 1989.

- Jiajing Wu, Jieli Liu, Weili Chen, Huawei Huang, Zibin Zheng, and Yan Zhang. Detecting mixing services via mining bitcoin transaction network with hybrid motifs. _IEEE Transactions on Systems, Man, and Cybernetics: Systems_ , 52 (4):2237–2249, 2021a. doi: 10.1109/TSMC.2021.3049278.

- Lei Wu, Yufeng Hu, Yajin Zhou, Haoyu Wang, Xiapu Luo, Zhi Wang, Fan Zhang, and Kui Ren. Towards understanding and demystifying Bitcoin mixing services. In _Proceedings of the Web Conference 2021_ , WWW ’21, pages 33–44, New York, NY, USA, 2021b. Association for Computing Machinery. ISBN 9781450383127. doi: 10.1145/3442381. 3449880.

- Jin Yang, XiaoJie Liu, Tao Li, Gang Liang, and SunJun Liu. Distributed agents model for intrusion detection based on ais. _Knowledge-Based Systems_ , 22(2):115–119, 2009. ISSN 0950-7051. doi: 10.1016/j.knosys.2008.07.005.

- Zhao Yang, Ren´e Algesheimer, and Claudio J. Tessone. A comparative analysis of community detection algorithms on artificial networks. _Scientific Reports_ , 6(1):30750, 2016. doi: 10.1038/srep30750.

- Maria Zhdanova, J¨urgen Repp, Roland Rieke, Chrystel Gaber, and Baptiste Hemery. No smurfs: Revealing fraud chains in mobile money transfers. In _2014 Ninth International Conference on Availability, Reliability and Security_ , pages 11–20. IEEE, 2014. doi: 10.1109/ARES.2014.10.

[pp. 30-31]

- Pengfei Zhu and Qinghua Hu. Rule extraction from support vector machines based on consistent region covering reduction. _Knowledge-Based Systems_ , 42:1–8, 2013. ISSN 0950-7051. doi: 10.1016/j.knosys.2012.12.003.

We demonstrate GARG-AML as described in Section 3. We start with a Watts-Strogatz network containing 20 nodes, each connecting to the next two nodes (initial degree equal to four), with rewiring probability 20%. We inject a smurfing pattern, where money originates at a new node (23) and gets transferred to an existing node (19) in the network using three mule accounts (20, 21, 22). The full network is visualised in Figure A.1.

## A Illustration GARG-AML


[p. 31]

We calculate the GARG-AML scores for two nodes as an illustration. We select node 23 because its second-order neighbourhood constitutes a pure smurfing pattern. We also select node 8 to show the impact of the neighbours’ interactions on the final score.

1422123 221 13 1119 020104 12185 317 16 915768

Figure A.1: The undirected network. Nodes 20 to 23 are part of the injected smurfing pattern. Node 19 is the destination node.

### A.1 Undirected Calculations


[pp. 31-33]

We start with the smurfing pattern using node 23. Its second-order neighbourhood is visualised in Figure A.2. The adjacency matrix, with the blocks, is as follows:

The elements that should be zero are indicated in red. Those elements that are certainly equal to one are indicated in green.

We take the upper-left block as block 1, the upper-right as block 2 (can also be the lower-left, since the matrix is symmetric), and the lower-right as block 3. Using Equations (5)–(10), this results in the following:

1422123 221 13 1119 020104 12185 317 16 915768

Figure A.2: Visualisation of the second-order neighbourhood of node 23 (presented in red). Nodes at distance one are presented in blue, nodes at distance two are presented in orange. All other nodes are given in grey.

1422123 221 13 1119 020104 12185 317 16 915768

Figure A.3: Visualisation of the second-order neighbourhood of node 8 (presented in red). Nodes at distance one are presented in blue, and nodes at distance two are presented in orange. All other nodes are given in grey.

The second-order neighbourhood of node 8 is shown in Figure A.3. We observe an interaction between neighbours at distance one and two, something we do not have for a pure smurfing pattern. These are reflected in the adjacency matrix in Equation (17). The first row contains the node to be scored, node 8. The following rows represent the nodes at distance two, i.e., 3, 4, 5, 10, 11 and 15. The final rows represent the nodes at distance one, i.e., 6, 7 and 9.

1422123 221 13 1119 020104 12185 317 16 915768

Figure A.4: The directed network. Nodes 20 to 23 are part of the injected smurfing pattern, and with node 19 the destination node.

[pp. 33-34]

This results in the following scores:

The directed network is illustrated in Figure A.4. We calculate the scores for node 23 and 8.

The directed second-order neighbourhood for node 23 is shown in Figure A.5, and the corresponding adjacency matrix is provided in Equation (19). Note that we now have a different ordering of the nodes, using level 0 (node 23), level 1 (nodes 20, 21, 22) and level 2 (node 19), resulting in nine blocks.

1422123 221 13 1119 020104 12185 317 16 915768

### A.2 Directed Calculations


[pp. 34-35]

Figure A.5: Visualisation of the second-order neighbourhood of node 23 (presented in red). Nodes at distance one are presented in blue, and nodes at distance two are presented in orange. All other nodes are given in grey.

The density of the nine blocks is calculated for the final score. We use the matrix representation of Equation (13) to represent the densities. This results in:

The score for node 23 is calculated as

We do the same for node 8. Here, level 0 consists of nodes 8 and 15, level 1 consists of nodes 6, 7 and 9, and level 2 consists of nodes 3, 4, 5, 10 and 11. Contrary to the second-order neighbourhood of node 23, we see in Figure A.6 that money flows in multiple directions, with nodes sending and receiving money to and from nodes across levels. This indicates that node 8 is not part of a smurfing scheme. The corresponding adjacency matrix is given in Equation (23).

1422123 221 13 1119 020104 12185 317 16 915768

Figure A.6: Visualisation of the second-order neighbourhood of node 8 (presented in red). Nodes at distance one are presented in blue, and nodes at distance two are presented in orange. All other nodes are given in grey.

Figure A.7: A pure directed smurfing pattern.

We can, indeed, see that the score for node 8 is below 0. Hence, we have no suspicion that this node is part of a smurfing scheme.

### A.3 Limitations for Intermediate Accounts


[pp. 35-37]

Section 5.2 illustrated the consistent underperformance of the directed scores. We return to the original example from Section 3.3, and include it again in Figure A.7.

We illustrate the calculations from the perspective of node _B_ . Equation (11) tells us that both nodes _C_ and _D_ are put at level 0. Nodes _A_ and _E_ are first-order neighbours, so they are put at level 1. Without looking at the adjacency matrix, the main problem is already apparent. There are no nodes at level 2, meaning that their scores are defaulted to 0.

We obtain the following adjacency and density matrix, which ultimately results in a score equal to 0 (weighted mean) or 0.18 (regular mean):

Hence, even with a perfect smurfing pattern, the intermediate accounts receive a low score. As these form the majority of nodes involved in smurfing, this skews the results. More research is needed to obtain more meaningful results from this particular representation.

Pattern: laundering Pattern: new_mules1.00.80.60.40.20.0AUC-ROC AUC-PR AUC-ROC AUC-PRPerformance Metric Performance MetricPattern: separate Pattern: existing_mules1.00.80.60.40.20.0AUC-ROC AUC-PR AUC-ROC AUC-PRPerformance Metric Performance MetricMethodFlowScope GARG-AML Undirected GARG-AML Undir. Tree GARG-AML Dir. TreeAutoAudit GARG-AML Directed GARG-AML Undir. Boost GARG-AML Dir. BoostPerformancePerformance

Figure B.1: AUC-ROC and AUC-PR values of the compared methods across all synthetic datasets, split by money laundering pattern.

## B Results Synthetic Data


[pp. 37-38]

The results are presented according to the injected patterns. These are provided in Figure B.1, with their corresponding ranks presented in Figure B.2.

Figure B.1 shows the distribution of AUC-ROC and AUC-PR values across the datasets. The AUC-PR values are more spread out than the AUC-ROC values. For a model with random label predictions, the AUC-ROC is always 0.5, regardless of the label distribution, whereas the AUC-PR equals the proportion of positive labels, which leads to the high variance.

Figure B.1 indicates that, on average, the undirected GARG-AML scores show competitive performance. This performance is boosted when combining the GARG-AML scores with the tree-based learners. In comparison, the performance of AutoAudit is less stable. Here, we set all the AUC-ROC and AUC-PR values to 0 when the method runs out of time or out of memory to allow for a full comparison of the ranks.

Figure B.2 shows the boxplots of the ranks of the methods (rank 1 means best scoring model, and rank 8 worst). We can see more clearly that models combining the tree-based learners with the scores and summary statistics of the node’s neighbours score better than the other methods, even when just applying a simple decision tree.

MetricAUC-ROC AUC-PRPattern: laundering Pattern: separate8642Pattern: new_mules Pattern: existing_mules8642FlowScope AutoAuditGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. Boost FlowScope AutoAuditGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostRankRank

Figure B.2: Ranks of the AUC-ROC and AUC-PR values of the compared methods across all synthetic datasets, split by money laundering pattern, where rank 1 indicates the best performance and rank 8 indicates the worst performance.

## C Results IBM Data


[p. 38]

In this part of the appendix, we provide the full results on the IBM datasets. These include all patterns defined by Altman et al. (2023). The binary labels are defined using the cut-off values 0, 0.1, 0.2, 0.3, 0.5 and 0.9. The results on the HI-Small and LI-Large datasets are provided in Figure C.1 and Figure C.2, respectively. Overall, GraphSAGE trained with node attributes performs best across both datasets, with the exceptions discussed below. Cells marked n/a indicate that no results are available for that model.

Figure C.1 shows that, on HI-Small, GraphSAGE with attributes has the highest AUC-ROC for almost all patterns and cut-offs for which the supervised models could be trained. Among the GARG-AML variants, the boosted extensions improve clearly on the base scores at the lower cut-offs (e.g., AUC-ROC of 80 _._ 0% and 77 _._ 2% versus 61 _._ 2% for the full ‘Is Laundering’ label at cut-off 0.1), and the tree-based extensions give a large gain in AUC-PR. For scatter-gather, the pattern GARG-AML is designed for, the tree-based extensions reach an AUC-PR that is on par with or higher than that of GraphSAGE with attributes at most cut-offs (e.g., 32 _._ 4% versus 26 _._ 5% at cut-off 0.1 and 11 _._ 4% versus 2 _._ 9% at cut-off 0.5), although their AUC-ROC remains lower. At the highest cut-offs, few positive labels remain, the supervised models often cannot be trained, and the base undirected score is the best GARG-AML variant (e.g., an AUC-ROC of 86 _._ 0% for scatter-gather at cut-off 0.9). For the non-smurfing patterns, GraphSAGE clearly outperforms the GARG-AML variants in most cases (e.g., fan-in at cut-off 0.1: AUC-ROC of 97 _._ 5% versus 64 _._ 6% for the base undirected score).

On LI-Large (Figure C.2), results for the supervised models are not available at cut-offs 0.2 and 0.3, nor for patterns with too few positives at cut-offs 0.5 and 0.9. Where they can be compared, GraphSAGE with attributes has by far the highest AUC-ROC (87–99% at cut-offs 0 and 0.1) and AUC-PR. The boosted GARG-AML extensions improve the AUC-ROC over the base scores (e.g., 80 _._ 7% versus 55 _._ 1% for ‘Is Laundering’ at cut-off 0.1), but their AUC-PR at cut-off 0.1 remains below 1%. The only setting in which the unsupervised scores are competitive with GraphSAGE is ‘Is Laundering’ at cut-off 0.9: the base undirected score has an AUC-ROC of 91 _._ 3%, similar to GraphSAGE using topology only (92 _._ 5%) and higher than GraphSAGE with attributes (79 _._ 5%). This label has very few positives (Table 8), so the corresponding AUC-PR and P@1000 values should be interpreted with care.

[p. 39]

Models - HI-SmallFlowScope GARG-AML Undirected GARG-AML Directed GARG-AML Undir. Tree GARG-AML Undir. Boost GARG-AML Dir. Tree GARG-AML Dir. Boost GraphSAGE (topology) GraphSAGE (+ attributes)1.00.80.60.40.20.0 50.0% 0.095% 51.0% Pattern: BIPARTITE 0.094%40.5%0.073%59.2% 1.400% 70.8%0.257% 48.2%0.903% | Cutoff: 0.071.5%0.330% 78.2% 0.480%93.2%3.557% 0.030.020.010.00 1.00.80.60.40.20.0 50.0%0.030%64.2%Pattern: BIPARTITE 0.041%47.1%0.029%60.9%0.046%65.8%0.054%48.3%0|. Cutoff: 0.1032% 60.0% 0.045%74.1%0.076% 95.3%4.636% 0.050.040.030.020.010.00 0.80.60.40.20.0 50.0%0.007%67.5%Pattern: BIPARTITE 0.012%32.7%0.005%60.2%0.011%61.6%0.011%47.1%0.007%| Cutoff: 0.264.6%0.018%69.3%0.011% 81.9%0.577% 0.0060.0040.0020.000 0.80.60.40.20.0 50.0%0.004%71.0%Pattern: BIPARTITE 0.010%33.4%0.004% 61.6% 0.006% 62.3% 0.007%47.2%0.004%| Cutoff: 0.3 63.1% 0.015%65.8%0.010%80.4%0.367% 0.0040.0030.0020.0010.000 0.50.40.30.20.10.0 50.0% 0.001% 36.8%Pattern:

BIPARTITE 0.001%7.2% 0.000% n/a n/a n/a n/a n/a|n/a Cutoff: 0.5n/a n/a n/a n/a n/a n/a1e 6 6420 0.50.40.30.20.10.0 50.0% 0.001% 36.8%Pattern: BIPARTITE 0.001%7.2% 0.000% n/a n/a n/a n/a n/a|n/a Cutoff: 0.9n/a n/a n/a n/a n/a n/a1e 6 64201.00.80.60.40.20.0 50.0%0.053%45.1%0.046%Pattern: CYCLE 38.6% 0.039% 60.4% 0.494% 78.6% 0.261%52.8%| Cutoff: 0.00.416%71.5%0.246%85.1%0.240% 96.7%4.722% 0.050.040.030.020.010.00 1.00.80.60.40.20.0 50.0% 0.019%53.9%0.020%Pattern: CYCLE 39.6%0.014%60.1%0.054%72.7%0.044% 49.7% | Cutoff: 0.10.019%69.3%0.076%82.0%0.055% 96.7%7.258% 0.060.040.020.00 1.00.80.60.40.20.0 50.0%0.013% 58.4% 0.015%Pattern: CYCLE 40.4%0.010%62.7%0.153% 59.0% 0.020%49.7%| Cutoff: 0.20.013%71.1%0.036%85.0%0.049% 99.1%4.917% 0.050.040.030.020.010.00 1.00.80.60.40.20.0 50.0% 0.005%61.9%0Pattern: CYCLE .006%43.9%0.004%62.3%0.047% 68.4% 0.015% 50.0% | Cutoff:

0.30.005% 56.3% 0.007% 85.6% 0.028% 95.0%1.074% 0.0100.0080.0060.0040.0020.000 0.60.40.20.0 50.0% 0.000%58.4%0.000% Pattern: CYCLE 45.9%0.000% n/a n/a n/a n/a | Cutoff: 0.5n/a n/a n/a n/a n/a n/a n/a n/a1e 6 43210 0.60.40.20.0 50.0% 0.000%58.4%0.000% Pattern: CYCLE 45.9%0.000% n/a n/a n/a n/a | Cutoff: 0.9n/a n/a n/a n/a n/a n/a n/a n/a1e 6 432101.00.80.60.40.20.0 50.0% 0.066%54.3%0.068%Pattern: FAN-IN 48.0%0.060% 55.8% 0.515% 68.1% 0.239% 58.2% | Cutoff: 0.02.229%71.8%0.423% 86.7% 0.506% 97.7%27.186% 0.250.200.150.100.050.00 1.00.80.60.40.20.0 50.0%0.022% 64.6% 0.030%Pattern: FAN-IN 61.0%0.031%68.5%0.959% 78.0% 0.579%67.8%| Cutoff: 0.11.360%74.6%0.710%90.5%0.600% 97.5%21.869% 0.200.150.100.050.00 1.00.80.60.40.20.0 50.0% 0.006% 51.1% 0.007%Pattern: FAN-IN 49.9% 0.007% 52.6% 0.014%74.6%0.039% 51.4% | Cutoff:

0.20.158%67.2%0.037%83.6%0.156%93.2%17.112% 0.150.100.050.00 1.00.80.60.40.20.0 50.0%0.005%49.7%0.005%Pattern: FAN-IN 47.8%0.006%54.4%0.015%71.9%0.024%53.6%| Cutoff: 0.30.351%70.2%0.094%84.4%0.100%92.4%15.399% 0.150.100.050.00 0.80.60.40.20.0 50.0%0.002% 40.6% 0.002%Pattern: FAN-IN 35.3% 0.002%49.7%0.002%47.4%0.003%50.0%| Cutoff: 0.50.002%49.7%0.007%89.4%0.130%85.3%21.478% 0.200.150.100.050.00 0.60.40.20.0 50.0% 0.001% 63.8% 0.001% Pattern: FAN-IN 61.6%0.001% n/a n/a n/a n/a | Cutoff: 0.9n/a n/a n/a n/a n/a n/a n/a n/a1e 5 1.00.80.60.40.20.01.00.80.60.40.20.0 50.0%0.070%54.4%Pattern: FAN-OUT 0.074%32.8%0.047% 61.3% 1.450%74.5%1.334%59.2%| Cutoff: 0.02.331%72.8%0.699% 84.1% 0.366% 98.0%22.471% 0.200.150.100.050.00 1.00.80.60.40.20.0 50.0%0.029%64.9%Pattern: FAN-OUT 0.043%30.2%0.019%68.1%0.264% 77.7% 0.256%66.2%| Cutoff:


---

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
