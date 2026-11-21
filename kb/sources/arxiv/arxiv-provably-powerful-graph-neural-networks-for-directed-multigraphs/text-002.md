---
type: Source Text
title: Provably Powerful Graph Neural Networks for Directed Multigraphs - part 2 of 5 (pp. 5-8)
description: 'Verbatim extracted text, pp. 5-8: Provably Powerful Graph Neural Networks for Directed Multigraphs > 6 Experimental Setup; Provably Powerful Graph Neural Networks for Directed Multigraphs > 7 Results; Provably Powerful Graph Neural Networks for Directed Multigraphs > 8 Conclusion; and 1 more sections'
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
part: 2
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.11586
  title: Provably Powerful Graph Neural Networks for Directed Multigraphs
  author: org:arxiv
  last_modified: '2023-06-20T00:00:00Z'
---

# Provably Powerful Graph Neural Networks for Directed Multigraphs

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2023-06-20), part 2 of 5, pp. 5-8. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Provably Powerful Graph Neural Networks for Directed Multigraphs


### 6 Experimental Setup


[pp. 5-6]

Base GNNs and Baselines. GIN with edge features (Hu et al. 2019) is used as the main GNN base model with our adaptations added on top. GAT (Veliˇckovi´c et al. 2017) and PNA (Velickovic et al. 2019) are also used as base models, and we refer to their adapted versions as Multi-GAT and Multi-PNA, respectively. All three are also considered baselines. Additionally, GIN with ego IDs can be considered an ID-GNN (You et al. 2021) baseline, and GIN with port numbering can be considered a CPNGNN (Sato, Yamada, and Kashima 2019) baseline. Since AML is an edge classification problem, we also include a baseline using edge updates (Battaglia et al. 2018), denoted GIN+EU. This approach is similar to replacing edges with nodes and running a GNN on said _line graph_ , which recently achieved state-of-the-art (SOTA) results in self-supervised money laundering detection (Cardoso, Saleiro, and Bizarro 2022). We also include R-GCN (Schlichtkrull et al. 2018) as a baseline. We do not focus on including a more expansive range of GNN baselines, for the simple reason that without (the proposed) adaptations, they are not equipped to deal with directed multigraphs. However, some additional results with “more expressive” GNNs can be found in Appendix H.1. As far as we are aware, there are no other GNNs that one could expect to achieve SOTA results on directed multigraphs.

We include a baseline representing the parallel line of work in financial crime detection that uses pre-calculated graphbased features (GFs) and tree-based classifiers to classify nodes or edges individually. We train XGBoost (Chen and Guestrin 2016) and LightGBM (Ke et al. 2017) models on the individual edges (or nodes) using the original raw features combined with additional graph-based features. This approach has produced SOTA results in financial applications (Weber et al. 2019; Lo, Layeghy, and Portmann 2022).

Given the size of the AML and ETH datasets, we use neighborhood sampling (Hamilton, Ying, and Leskovec 2017) for all GNN-based models. Further details of the experimental setup for the different datasets can be found in Appendix F.

Scoring. Since we have very imbalanced datasets, accuracy and other popular metrics are not suitable. Instead, we use the minority class F1 score. This aligns well with what banks and regulators use in real-world scenarios.

### 7 Results


#### 7.1 Synthetic Pattern Detection Results


[p. 6]

The synthetic pattern detection results can be seen in Table 1. The degree-out results reveal that the standard messagepassing GNNs are unable to solve the degree-out task, achieving F1 scores below 44%. However, all the GNNs that are equipped with reverse MP score above 98%, thus supporting Proposition 4.1. The next column shows that port numbering is the critical adaptation for solving fan-in, though the F1 score is quite high even for the baseline GIN. On the other hand, for the fan-out task, the combination of reverse MP and port numbering is needed to score above 99%. Again, these results support Propositions 4.2 and 4.3. The ablation study of cumulative adaptations on top of GIN also supports Corollary 4.4.1: The combination of reverse MP, port numbering, and ego IDs, scores high on all of the subtasks, with only 6-cycle detection coming in below 90%. We see similar results when using other base GNN models, with Multi-PNA achieving the best overall results. Moreover, on the more complex tasks — directed cycle, scatter-gather, and biclique detection — the combination of the three is what leads to the first significant improvement in F1 scores. In the most extreme case, scatter-gather detection, the minority class F1 score jumps from 67 _._ 84% with only reverse MP and port numbers to 97 _._ 42% when ego IDs are added. No adaptation alone comes close to this score, so it is clear that the combination is needed. Similar jumps can be seen for directed 4-, 5-, and 6-cycle, and biclique detection. Increasing the dataset size and restricting the task to only the “complex” subtasks further increases the scores, with 6-cycle detection also reaching above 97%. More details can be found in Appendix H.2. Additional ablations can also be found in the appendix. In particular, we rerun the experiments using random unique node IDs as input features and see that node IDs are unable to replace port numbers and ego IDs in practice.

#### 7.2 AML Results


The results for the AML datasets can be seen in Table 2. For AML Small HI, we see that our adaptations boost the minority class F1 score of GIN from 28 _._ 7% to 57 _._ 2%, a gain

of almost 30%. The largest improvements are brought by reverse MP and port numbering, taking the F1 score from 28 _._ 7% to 56 _._ 9%, whilst ego IDs do not make much difference here. The results for the other AML datasets show a similar trend with overall gains of 14 _._ 2%, 14 _._ 0%, and 10 _._ 7% for GIN, again with diminishing returns as more adaptations are added. The two rows corresponding to port numbering — _GIN+Ports_ and _+Ports_ — indicate clear gains from using port numbering, both when used alone and on top of reverse MP. The support for ego IDs is less clear, with clear gains when used as an individual adaptation but no significant gains when added on top of reverse MP and port numbering. Note that only two GNN layers were used, so this conclusion could change as more layers are added and longer cycles can also be detected. The full set of adaptations was tested with three other base models, GIN+EU (GIN with edge updates), PNA, and PNA+EU. In each case, and across almost all AML datasets, we see clear gains from using the adaptations. These gains underline the effectiveness and versatility of the approach. We further note that Multi-PNA+EU outperforms all of the baselines on all of the AML datasets. This is particularly impressive when compared with the treebased methods using graph-based features (XGBoost+GFs and LightGBM+GFs) since the hand-crafted features align perfectly with the illicit money laundering patterns used by the simulator. Moreover, these tree-based methods have been SOTA in previous financial applications (Weber et al. 2019; Lo, Layeghy, and Portmann 2022).

Recall scores for individual money laundering patterns can be found in Appendix I. It is worth noting that the majority of the illicit transactions that belong to money laundering patterns are identified, and the overall dataset scores are greatly influenced by the proportion of lone (not belonging to a money laundering pattern) illicit transactions in the datasets. Lone illicit transactions are very difficult to identify.

For training times and inference throughput rates of models based on GIN, please see Table 5 in the appendix. Notably, with all the adaptations, the inference rate of Multi-GIN still surpasses 18k transactions per second on a single GPU.

#### 7.3 ETH Results


Finally, we test our adaptations on a real-world financial crime dataset — Ethereum phishing account classification. The results are provided in Table 2. Similar to the AML datasets, we see a consistent improvement in final scores as we add the adaptations. In total, the minority class F1 score jumps from 26 _._ 9% without adaptations to 42 _._ 9% with reverse MP, port numbering, and ego IDs. Again, the largest single improvement is due to the reverse MP. In this case, Multi-GIN does not outperform all of the baselines, but the adaptations also significantly boost PNA performance, and Multi-PNA and Multi-PNA+EU beat all the baselines by more than 12%.

This work has investigated a series of straightforward adaptations capable of transforming conventional message-passing GNNs into provably powerful directed multigraph learners. Our contributions to the field of graph neural networks are

### 8 Conclusion


[p. 7]

|Model|deg-in|deg-out|fan-in|fan-out|C2|C3|C4|C5|C6|S-G|B-C|
|---|---|---|---|---|---|---|---|---|---|---|---|
|GIN (Xu et al. 2018; Hu et al. 2019)|99.77|43.58|95.57|35.91|34.67|58.00|50.80|43.12|48.59|69.31|63.12|
|GAT (Veliˇckovi´c et al. 2017)|10.33|10.53|9.69|0.00|0.00|0.00|25.86|0.00|0.00|0.00|0.00|
|PNA (Velickovic et al. 2019)|99.63|43.02|95.00|38.93|25.77|54.75|51.92|48.79|48.40|65.88|65.51|
|GIN+EU (Battaglia et al. 2018)|99.30|42.74|95.70|39.13|32.58|55.91|54.65|47.62|49.68|68.54|64.64|
|GIN+EgoIDs (You et al. 2021)|99.78|51.48|95.06|49.24|98.13|97.97|53.12|44.37|45.42|66.44|63.90|
|GIN+Ports (Sato, Yamada, and Kashima 2019)|99.47|45.00|99.59|41.51|27.79|56.11|42.68|41.11|44.99|67.99|65.76|
|GIN+ReverseMP (Jaume et al. 2019)|98.87|99.08|94.99|95.25|35.96|63.85|69.09|67.44|71.23|65.83|66.18|
|+Ports|98.41|98.35|98.51|99.16|39.15|63.58|69.00|70.35|75.04|67.84|65.78|
|+EgoIDs (Multi-GIN)|99.48|99.09|99.62|99.32|98.97|98.73|97.46|91.60|84.23|97.42|94.33|
|Multi-GAT|98.68|98.36|99.28|99.33|98.61|98.93|98.90|95.82|91.81|96.66|86.92|
|Multi-PNA|99.64|99.25|99.53|99.41|99.71|99.54|99.49|97.46|88.75|99.07|96.77|
|Multi-GIN+EU|99.55|99.53|99.76|99.77|99.37|99.71|98.73|95.73|88.38|98.81|97.82|

Table 1: Minority class F1 scores (%) for the synthetic subgraph detection tasks. First from the top are the standard MPNN baselines; then the results with each adaptation added separately on top of GIN; followed by GIN with the adaptations added cumulatively; and finally, results for the other GNN baselines with the three adaptations (Multi-GNNs). The C _k_ abbreviations stand for directed _k_ -cycle detection, S-G stands for scatter-gather and B-C stands for biclique detection. We report minority class F1 scores averaged over five runs. We omit standard deviations in favor of readability.

|Model|AML Small HI|AML Small LI|AML Medium HI|AML Medium LI|ETH|
|---|---|---|---|---|---|
|LightGBM+GFs (Altman et al. 2023)|62_._86_±_0_._25|20_._83_±_1_._50|59_._48_±_0_._15|20_._85_±_0_._38|53_._20_±_0_._60|
|XGBoost+GFs (Altman et al. 2023)|63_._23_±_0_._17|27_._30_±_0_._33|65_._70_±_0_._26|28_._16_±_0_._14|49_._40_±_0_._54|
|GIN (Xu et al. 2018; Hu et al. 2019)|28_._70_±_1_._13|7_._90_±_2_._78|42_._20_±_0_._44|3_._86_±_3_._62|26_._92_±_7_._52|
|PNA (Velickovic et al. 2019)|56_._77_±_2_._41|14_._85_±_1_._46|59_._71_±_1_._91|27_._73_±_1_._65|51_._49_±_4_._26|
|GIN+EU (Battaglia et al. 2018)|47_._73_±_7_._86|20_._62_±_2_._41|49_._26_±_4_._02|6_._19_±_8_._32|33_._92_±_7_._34|
|R-GCN (Schlichtkrull et al. 2018)|41_._78_±_0_._48|7_._43_±_0_._38|OOM|OOM|OOM|
|GIN+EgoIDs (You et al. 2021)|39_._65_±_4_._73|14_._98_±_2_._66|45_._26_±_2_._16|11_._17_±_6_._41|26_._01_±_2_._27|
|GIN+Ports (Sato, Yamada, and Kashima 2019)|54_._85_±_0_._89|21_._41_±_2_._40|54_._22_±_1_._94|10_._51_±_12_._82|32_._96_±_0_._25|
|GIN+ReverseMP (Jaume et al. 2019)|46_._79_±_4_._97|15_._98_±_4_._39|51_._93_±_2_._90|14_._00_±_9_._34|36_._86_±_8_._12|
|+Ports|56_._85_±_2_._64|23_._80_±_4_._07|57_._15_±_0_._76|11_._39_±_8_._36|42_._51_±_7_._16|
|+EgoIDs (Multi-GIN)|57_._15_±_4_._99|22_._12_±_2_._88|56_._23_±_1_._51|14_._55_±_2_._91|42_._86_±_2_._53|
|Multi-GIN+EU|64_._79_±_1_._22|26_._88_±_6_._63|58_._92_±_1_._83|16_._30_±_4_._73|48_._37_±_6_._62|
|Multi-PNA|64_._59_±_3_._60|30_._65_±_2_._00|65_._67_±_2_._66|33_._23_±_1_._31|65_._28_±_2_._89|
|Multi-PNA+EU|68_._16_±_2_._65|33_._07_±_2_._63|66_._48_±_1_._63|36_._07_±_1_._17|66_._58_±_1_._60|

Table 2: Minority class F1 scores (%) for the AML and ETH tasks. HI indicates a higher illicit ratio and LI indicates a lower illicit ratio. The models are organized as in Table 1. “OOM” indicates that the model ran out of GPU memory.

threefold. Firstly, our theoretical analysis addresses a notable gap in the existing literature about the power of combining different GNN adaptations/augmentations. Specifically, we prove that ego IDs combined with port numbering and reverse message passing enable a suitably powerful message-passing GNN, such as GIN, to compute unique node IDs and therefore detect any directed subgraph patterns. Secondly, our theoretical findings are validated empirically with a range of synthetic subgraph detection tasks. The practical results closely mirror the theoretical expectations, confirming that the combination of all three adaptations is needed to detect the more complex subgraphs. Lastly, we show how our adaptations can be applied to two important financial crime problems: detecting money laundering transactions and phishing accounts. GNNs enhanced with our proposed adaptations achieve impressive results in both tasks, either matching or surpassing relevant baselines. Reverse message passing and port numbering again prove crucial in reaching the highest scores, however, we find that ego IDs do not provide much

#### additional benefit for these datasets.


Although this work has focused on financial crime applications, the theory and practical results have a broader relevance. Immediate future work could involve exploring applications of our methods to other directed multigraph problems. An initial exploration can be found in the appendix, showing promising results on three real-world datasets. However, further experiments are needed to confirm general applicability in various domains. Additionally, future work could explore the relationship between the computational complexity of different subgraph detection problems and GNN performance.

The support of the Swiss National Science Foundation (project numbers: 172610 and 212158) for this work is gratefully acknowledged.

### References


[p. 8]

Abboud, R.; Ceylan, I. I.; Grohe, M.; and Lukasiewicz, T. 2020. The surprising power of graph neural networks with random node initialization. _arXiv preprint arXiv:2010.01179_ .

Altman, E.; Blanuša, J.; Von Niederhäusern, L.; Egressy, B.; Anghel, A.; and Atasu, K. 2023. Realistic Synthetic Financial Transactions for Anti-Money Laundering Models. In _Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track_ .

Babai, L.; Erdos, P.; and Selkow, S. M. 1980. Random graph isomorphism. _SIaM Journal on computing_ , 9(3): 628–635. Barceló, P.; Geerts, F.; Reutter, J.; and Ryschkov, M. 2021. Graph neural networks with local graph parameters. _Advances in Neural Information Processing Systems_ , 34: 25280–25293.

Battaglia, P.; Pascanu, R.; Lai, M.; Jimenez Rezende, D.; et al. 2016. Interaction networks for learning about objects, relations and physics. _Advances in neural information processing systems_ , 29. Battaglia, P. W.; Hamrick, J. B.; Bapst, V.; Sanchez-Gonzalez, A.; Zambaldi, V.; Malinowski, M.; Tacchetti, A.; Raposo, D.; Santoro, A.; Faulkner, R.; et al. 2018. Relational inductive biases, deep learning, and graph networks. _arXiv preprint arXiv:1806.01261_ .

Blanusa, J.; Ienne, P.; and Atasu, K. 2022. Scalable Fine-Grained Parallel Cycle Enumeration Algorithms. In _Proceedings of the 34th ACM Symposium on Parallelism in Algorithms and Architectures_ , 247–258.

Blanuša, J.; Atasu, K.; and Ienne, P. 2023. Fast Parallel Algorithms for Enumeration of Simple, Temporal, and Hop-Constrained Cycles. ArXiv:2301.01068 [cs].

Bongini, P.; Bianchini, M.; and Scarselli, F. 2021. Molecular generative graph neural networks for drug discovery. _Neurocomputing_ , 450: 242–252.

Bouritsas, G.; Frasca, F.; Zafeiriou, S. P.; and Bronstein, M. 2022. Improving graph neural network expressivity via subgraph isomorphism counting. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ .

Cardoso, M.; Saleiro, P.; and Bizarro, P. 2022. LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering. In _Proceedings of the Third ACM International Conference on AI in Finance_ , 130–138.

Chen, L.; Peng, J.; Liu, Y.; Li, J.; Xie, F.; and Zheng, Z. 2019a. XBLOCK Blockchain Datasets: InPlusLab Ethereum Phishing Detection Datasets. http://xblock.pro/ethereum/.

Chen, T.; and Guestrin, C. 2016. Xgboost: A scalable tree boosting system. In _Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining_ , 785–794.

Chen, Y.; Wei, Z.; and Huang, X. 2018. Incorporating corporation relationship via graph convolutional neural networks for stock price prediction. In _Proceedings of the 27th ACM International Conference on Information and Knowledge Management_ , 1655–1658.

Chen, Z.; Chen, L.; Villar, S.; and Bruna, J. 2020. Can graph neural networks count substructures? _Advances in neural information processing systems_ , 33: 10383–10395.

Chen, Z.; Villar, S.; Chen, L.; and Bruna, J. 2019b. On the equivalence between graph isomorphism testing and function approximation with gnns. _Advances in neural information processing systems_ , 32.

Derrow-Pinion, A.; She, J.; Wong, D.; Lange, O.; Hester, T.; Perez, L.; Nunkesser, M.; Lee, S.; Guo, X.; Wiltshire, B.; et al. 2021. Eta prediction with graph neural networks in google maps. In _Proceedings of the 30th ACM International Conference on Information & Knowledge Management_ , 3767–3776.

Dwivedi, V. P.; Luu, A. T.; Laurent, T.; Bengio, Y.; and Bresson, X. 2021. Graph neural networks with learnable structural and positional representations. _arXiv preprint arXiv:2110.07875_ .

Egressy, B.; and Wattenhofer, R. 2022. Graph Neural Networks with Precomputed Node Features. _arXiv preprint arXiv:2206.00637_ . Feng, F.; He, X.; Wang, X.; Luo, C.; Liu, Y.; and Chua, T.-S. 2019. Temporal relational ranking for stock prediction. _ACM Transactions on Information Systems (TOIS)_ , 37(2): 1–30.

Frasca, F.; Bevilacqua, B.; Bronstein, M. M.; and Maron, H. 2022. Understanding and extending subgraph gnns by rethinking their symmetries. _arXiv preprint arXiv:2206.11140_ .

Garg, V.; Jegelka, S.; and Jaakkola, T. 2020. Generalization and representational limits of graph neural networks. In _International Conference on Machine Learning_ , 3419–3430. PMLR.

Granados, O. M.; and Vargas, A. 2022. The geometry of suspicious money laundering activities in financial networks. _EPJ Data Science_ , 11(1): 6.

Hamilton, W.; Ying, Z.; and Leskovec, J. 2017. Inductive representation learning on large graphs. _Advances in neural information processing systems_ , 30.

He, J.; Tian, J.; Wu, Y.; Cia, X.; Zhang, K.; Guo, M.; Zheng, H.; Wu, J.; and Ji, Y. 2021. An efficient solution to detect common topologies in money launderings based on coupling and connection. _IEEE Intelligent Systems_ , 36(1): 64–74.

Hornik, K.; Stinchcombe, M.; and White, H. 1989. Multilayer feedforward networks are universal approximators. _Neural networks_ , 2(5): 359–366.

Hu, W.; Fey, M.; Zitnik, M.; Dong, Y.; Ren, H.; Liu, B.; Catasta, M.; and Leskovec, J. 2020. Open graph benchmark: Datasets for machine learning on graphs. _Advances in neural information processing systems_ , 33: 22118–22133.

Hu, W.; Liu, B.; Gomes, J.; Zitnik, M.; Liang, P.; Pande, V.; and Leskovec, J. 2019. Strategies for pre-training graph neural networks. _arXiv preprint arXiv:1905.12265_ .


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Provably Powerful Graph Neural Networks for Directed Multigraphs" (2023-06-20). https://arxiv.org/abs/2306.11586
