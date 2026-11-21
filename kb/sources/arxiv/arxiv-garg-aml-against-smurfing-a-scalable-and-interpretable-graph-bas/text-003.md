---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 3 of 10 (pp. 11-16)'
description: 'Verbatim extracted text, pp. 11-16: 4 Experimental Setup > 4.2 Model Specifications; 4 Experimental Setup > 4.3 Baselines; 4 Experimental Setup > 4.4 Evaluation; and 1 more sections'
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
part: 3
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 3 of 10, pp. 11-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 4 Experimental Setup


### 4.2 Model Specifications


[pp. 11-12]

Table 5: The summary of the two IBM datasets, representing the number of nodes, edges and the percentage of instances labelled as money laundering (ML).

|Dataset|# nodes|# edges|percentage ML|
|---|---|---|---|
|HI-Small|515,080|5,078,345|0_._1%|
|LI-Large|2,054,390|176,066,557|0_._06%|

Table 6: The distribution of the money laundering transaction patterns for the two IBM datasets.

|Type of pattern|HI-Small|LI-Large|
|---|---|---|
|Fan-out|342|1,985|
|Fan-in|318|1,935|
|Gather-scatter|716|3,857|
|Scatter-gather|626|3,694|
|Cycle|287|1,871|
|Random|191|1,458|
|Bipartite|263|1,807|
|Stack|466|2,854|
|Not classified|1,968|81,143|
|Total number of transactions|5,078,345|176,066,557|

Table 7: Percentage of instances labelled as 1 in the HI-Small dataset per cut-off.

|In percentage(%)|0|10|20|30|50|90|
|---|---|---|---|---|---|---|
|Is Laundering|1.234|0.445|0.175|0.103|0.020|0.013|
|Fan-out|0.070|0.029|0.013|0.009|0.002|0.001|
|Fan-in|0.066|0.022|0.006|0.005|0.002|0.001|
|Gather-scatter|0.133|0.056|0.018|0.014|0.003|0.001|
|Scatter-gather|0.072|0.036|0.023|0.010|0.003|0.000|
|Cycle|0.053|0.019|0.013|0.005|0.000|0.000|
|Random|0.041|0.015|0.007|0.002|0.000|0.000|
|Bipartite|0.095|0.030|0.007|0.004|0.001|0.001|
|Stack|0.129|0.044|0.021|0.011|0.001|0.001|

Table 8: Percentage of instances labelled as 1 in the LI-Large dataset per cut-off.

[pp. 12-13]

|In percentage(%)|0|10|20|30|50|90|
|---|---|---|---|---|---|---|
|Is Laundering|6.292|0.216|0.041|0.019|0.002|0.000|
|Fan-out|0.105|0.005|0.002|0.001|0.000|0.000|
|Fan-in|0.101|0.005|0.002|0.002|0.000|0.000|
|Gather-scatter|0.184|0.008|0.004|0.003|0.000|0.000|
|Scatter-gather|0.106|0.015|0.005|0.002|0.000|0.000|
|Cycle|0.085|0.009|0.002|0.001|0.000|0.000|
|Random|0.078|0.006|0.001|0.000|0.000|0.000|
|Bipartite|0.172|0.004|0.001|0.000|0.000|0.000|
|Stack|0.197|0.010|0.001|0.000|0.000|0.000|

Figure 5: The pipeline of the GARG-AML method.

Algorithm 1 GARG-AML Score Calculation Input : Network _G_ ( _V, E_ ) Output : GARG-AML propensity score(s) 1: Calculate communities using Louvain method (Blondel et al., 2008) 2: Remove inter-community edges 3: if Directed score then 4: for node _v ∈ V_ do 5: Extract second-order neighbourhood of _v_ 6: Distribute neighbours over level 0, 1 and 2 7: Define the adjacency matrix with levels 0, 1 and 2. 8: Define the nine blocks using Equation (13) 9: Calculate score via Equation (14) 10: end for 11: else 12: for node _v ∈ V_ do 13: Extract second-order neighbourhood of _v_ 14: Define the adjacency matrix using _v_ , _N_ 2( _v_ ) and _N_ 1( _v_ ) 15: Define the three blocks using Equations (2)–(4) 16: Calculate score via Equation (8) 17: end for 18: end if 19: return : scores

[p. 13]

Therefore, we first partition the network into communities using the Louvain method (Blondel et al., 2008). This method consistently shows good performance for community detection, and scales well to large graphs (Lancichinetti and Fortunato, 2009; Yang et al., 2016). Communities are identified on the basis of the undirected version of the transaction network. Only intra-community edges are retained and edges between communities are discarded.

The Louvain method can produce overly large communities (Fortunato and Barth´elemy, 2007; Newman and Girvan, 2004). To mitigate this, we use the implementation from NetworkX (Hagberg et al., 2008), which includes a resolution parameter inspired by the improvements proposed by Traag et al. (2019). In our experiments, we set this hyperparameter to 10 to obtain smaller, more manageable communities. The choice of applying the Louvain method and the selection of the resolution parameter can break up the money laundering patterns if they span multiple communities. The sensitivity of GARG-AML to these choices is analysed in Section 5.3.

After pre-processing, we calculate the block densities as described above. We come to the final undirected and directed score via Equation (8) and Equation (14), respectively.

As a possible extension, we apply a decision tree and gradient boosting classifier that use features based on the GARGAML scores. A decision tree is a non-parametric model that performs greedy binary partitioning of the features on an impurity criterion. The resulting model can be seen as a collection of IF-ELSE rules. The gradient boosting classifier is an ensemble learning method that constructs an additive model in a forward stage-wise manner. It optimises a differentiable loss function by sequentially training ‘weak learners’ (shallow decision trees), where each subsequent tree is fit to the negative gradient of the loss function (the residuals) of the previous ensemble.

To capture the coordinated nature of smurfing, the base GARG-AML scores are supplemented with neighbourhood summary statistics (min, mean, max, and standard deviation of neighbour degrees and scores). This structural context helps the model differentiate between suspicious multi-mule topologies and benign linear chains by automatically filtering out these specific false positives. Applying this on the undirected and directed network results in four additional models.

The validation is set up in a transductive way. This is done since there is a large distributional shift over time for the IBM datasets. We use a 70-30 stratified train-test split for evaluation. For the GARG-AML scores, the split is performed on the resulting feature table, not the network itself. The split for GraphSAGE is done on the network itself.

[pp. 13-14]

For the decision tree, we use the Gini criterion and each leaf should contain at least ten samples. The gradient boosting classifier consists of 100 trees with a maximal depth of three and a learning rate of 0.1. Each leaf node should contain at least 10 observations.

We benchmark GARG-AML and its extension against established methods in smurfing detection, AutoAudit (Lee et al., 2020) and FlowScope (Li et al., 2020), with their default hyperparameters, except that FlowScope’s block size is capped at 10 accounts per mode, as in the reference tutorial (Table 9). Neither method outputs a score per account, so both need a small adaptation.

### 4.3 Baselines


[p. 14]

FlowScope returns _k_ = 3 dense flow blocks in the order in which they are found. To reflect the decreasing level of certainty, the accounts in the first block get score 1, those in the second2 3and those in the third1 3; all other accounts get score 0.

AutoAudit returns a reordering of the indices of the adjacency matrix: first the accounts of each detected smurfing pattern, in the order in which the patterns were found, then all remaining accounts. We use this reordering as a ranking: the account at position _j_ ( _j_ = 0 _, . . . , N −_ 1) among _N_ accounts gets score_N_ _N__−j_, so every account receives a distinct score. Only the head of the ordering comes from the detected patterns; the remaining accounts keep their index order, which depends on the arbitrary numbering of the nodes. To ensure robustness, we repeat the experiments three times with a random permutation of the node indices and report the average results.

In addition to AutoAudit and FlowScope, we test GARG-AML against GraphSAGE (Hamilton et al., 2017). GraphSAGE is a graph neural network (GNN) method that we include since GNNs have been shown to be capable deep learning methods for anti-money laundering (Altman et al., 2023; Egressy et al., 2024). A major drawback is that GNNs are black-box methods that do not allow for interpretable results. Compared to the other methods, GraphSAGE is also not specifically designed for smurfing detection. We include GraphSAGE in our comparison to have a better view of the interpretability-vs-performance trade-off. We use GraphSAGE as a supervised classifier, so enough labels and data are needed for training. Therefore, it is only included in the experiments on the IBM data.

We evaluate GraphSAGE under two feature configurations, both run on the full undirected transaction graph without Louvain pre-processing. In the topology configuration, each account is described only by its degree and log-degree. Since a two-layer GraphSAGE has the same two-hop receptive field as GARG-AML, this gives both methods the same structural information. The attributes configuration adds twelve per-account aggregates from the raw transactions: counts of sent and received transactions; the sum, mean, standard deviation and maximum of outgoing and incoming amounts; and the number of distinct currencies and counterparty banks.

[pp. 14-15]

Table 9: Hyperparameters of the baseline models. _Default_ : the value of the reference implementation (spartan2 for FlowScope; the authors’ AA-Smurf code for AutoAudit, where these constants are hard-coded and the method is presented as parameter-free; PyTorch Geometric and PyTorch for GraphSAGE). _Set_ : fixed by us before any experiment. No hyperparameter search was run for any model, so no value was selected on, or tuned against, a test fold.

|Hyperparameter|Value|Origin|
|---|---|---|
|FlowScope(Li et al.,2020)|||
|Number of blocks_k_|3|default|
|Penalty weight_α_(_λ_in the paper)|4|default|
|Search strategy|fast greedy decreasing (`level`= 0)|default|
|Maximum block size|10 accounts per mode (source, middle, target)|set_a_|
|Flow graph|3-partite, with the directed transaction graph as both hops|set|
|Edge weight|amount received (IBM); 1 (synthetic)|set|
|Account score|1, 23, 13 for blocks 1–3; 0 otherwise|set|
|Alert rule (precision, F1)|score_>_0_._5, i.e. blocks 1 and 2|set|
|Repetitions|1 (the algorithm is deterministic)|–|
|AutoAudit(AA-Smurf) (Lee et al.,|2020)||
|Min. intermediaries per pair|3 (candidate source–target pairs need at least 3 two-hop paths)|default|
|Solution reported|last one whose code length is at least 10% above the minimum|default|
|Maximum iterations|none (until no candidate pattern lowers the code length)|default|
|Adjacency matrix|binary, directed, dense_|V | × |V |_|default|
|Node-index permutations|3 (seeds 0, 1, 2); metrics averaged over them|set|
|Account score|(_N −j_)_/N_ for the account at position_j_ of the returned ordering of_N_accounts|set|
|Alert rule (precision, F1)|score_>_0_._5, i.e. the top half of the ordering|set|
|GraphSAGE(Hamilton et al.,201|7)||
|Architecture|2`SAGEConv`layers (receptive field: the second-order neighbourhood), 64hidden units, ReLU, dropout 0.2 after the first layer; one logit per account|set|

_Continued on next page_

_Table 9 (continued)_

[p. 15]

|Hyperparameter|Value|Origin|
|---|---|---|
|Aggregator|mean, with root weight, no output normalisation|default|
|Optimiser|Adam, learning rate10_−_3|set|
|Weight decay|0|default|
|Loss|binary cross-entropy, positive-class weight_n_neg_/n_pos of the training split|set|
|Mini-batches|neighbour sampling with fan-out (25, 10); 1,024 seed accounts per batch|set|
|Training length|at most 50 epochs; early stopping on validation AUC-PR with patience 5,best epoch restored|set|
|Validation split|stratified 10% of the training fold_b_|set|
|Input graph|undirected, unweighted, parallel transactions merged, self-loops removed,no Louvain filtering|set|
|Node features|_topology_: degree, log-degree (2);_attributes_: also sent and received counts,sum/mean/std/max of outgoing and incoming amounts, distinct currenciesand counterparty banks (14);log(1 +_x_)on counts and amounts, thenstandardised|set|
|Inference|full graph (HI-Small); sampled, fan-out (25, 10), batches of 4,096(LI-Large)|set|
|Alert rule (precision, F1)|predicted probability_>_0_._5|set|
|Random seed|1997|set|

> _a_ spartan2’s default imposes no size limit; 10 per mode is the setting of the spartan2 FlowScope tutorial.

> _b_ A training fold with fewer than 10 positives gets no validation split and trains for the full 50 epochs (64 of 460 fits on HI-Small, 30 of 220 on LI-Large).

### 4.4 Evaluation


Two aspects are critical for business adoption. A model must (1) catch launderers with few false positives (model performance), and (2) process millions of daily transactions quickly (scalability). Accordingly, the evaluation of the methods focuses on these two dimensions.

The performance is evaluated using precision, precision at K (P@K), F1-score, the area under the receiver operating characteristic curve (AUC-ROC) and the area under the precision-recall curve (AUC-PR), also called average precision.

The precision expresses the relative proportion of predicted cases (positive) that are actually positive (true positive); TPP.Financialinstitutionshavelimitedresourcestoinvestigatethegeneratedalerts.Onlyasmallportionofalerts can be investigated. The P@K is the relative number of true positives in the top _K_ predictions, and hence expresses the quality of the most suspicious cases. For the synthetic datasets, we set _K_ = 10. For the IBM datasets, we set _K_ = 1000, given that these are much larger datasets with many more labels. If precision or precision@K is high, investigators have a good indication that the generated alerts are also high quality, containing limited false positives. The F1-score is the harmonic mean of the precision and recall of the model. It strikes a balance between limiting false positives (high precision) and detecting all fraudulent cases (high recall).

These metrics require binary predictions, so their values depend on a chosen classification threshold. In our evaluation, an account is flagged when its score exceeds 0 _._ 5. For the GARG-AML scores, which range from _−_ 1 to 1, this is the raw score. For the tree-based extensions and GraphSAGE, it is the predicted probability of laundering. For FlowScope, it means the first two blocks, and for AutoAudit the top half of the ordering.

Both AUC metrics, on the other hand, compare models across classification thresholds. The AUC-ROC quantifies the model’s ability to discriminate between classes by plotting the true positive rate against the false positive rate. While it is a widely used metric for binary classification, it may not be sufficient for anti-money laundering (AML) datasets, which are often highly imbalanced, typically with fewer than 0 _._ 1% observations flagged as laundering money.

The AUC-PR is more indicative of performance under extreme class imbalance, where the positive class (smurfing) is rare (Davis and Goadrich, 2006; Ozenne et al., 2015). It plots precision against recall. The AUC-PR measures the model’s ability to identify positive examples correctly while minimising false positives across all possible threshold values. The AUC-PR specifically focuses on the model’s precision in identifying the positive class at various recall thresholds.

[pp. 15-16]

Scalability is assessed in terms of calculation time. The theoretical time complexity for the baseline models is _O_ ( _k | E |_ log ( _| V |_ )) for FlowScope (Li et al., 2020) and _O_ � _| V | · | E |_ + _| V |_2� for AutoAudit (Lee et al., 2020).

For GARG-AML, the main calculations are the selection of the second-order neighbourhood and the assignment of the neighbours to the levels. Assuming that we are working in sparse graphs, both steps have complexity _O_ ( _| V |_ ). This brings us to a total worst case time complexity of _O_ � _n_2� . Hence, theoretically, GARG-AML scales as AutoAudit, while FlowScope is much faster. However, we can speed up the calculations by running them in parallel. In addition, second-order neighbours are generally much smaller than _n_ , meaning that those steps can run very quickly. In addition to runtime, memory usage is a key factor. We report any instances where methods fail due to memory limitations.

All the experiments were conducted on the Flemish Supercomputer (VSC) with an Intel Xeon Platinum 8360Y CPU and 200 GB of memory, with GraphSAGE trained on an NVIDIA A100 SXM4 GPU. Each experiment was constrained to a time budget of 16 hours, the maximum on the VSC.

### 4.5 Statistical Test


[p. 16]

To test whether the observed differences in performance are not due to random chance, we determine for each model its rank compared to the other models based on the AUC-ROC and the AUC-PR. The best-performing method receives rank 1, the second-best method receives rank 2, and so on.

The statistical significance of the difference in ranks is evaluated using the Friedman test (Friedman, 1937, 1940) and the post hoc Nemenyi test (Nemenyi, 1963), as described by Demˇsar (2006). It compares the performance of _k_ methods across _N_ datasets. If we take _ri__j_to be the rank of method_j_on dataset_i_, the average performance across all datasets is equal to _Rj_ = _N_1 � _i__r_ _i__j_.

The null hypothesis of the Friedman test is that the average ranks _Rj_ are equal, and the Friedman statistic is equal to

The Friedman statistic follows a _χ_2 _k−_ 1distribution under this null hypothesis.

Rejecting the null hypothesis indicates that significant differences are present among the methods. In that case, we proceed with the post hoc Nemenyi test. It indicates that the performances of two methods are significantly different at level _α_ if their respective average ranks differ by at least the critical difference (CD):

where critical levels _qα_ are provided by Demˇsar (2006).

Our experiments compare the ranks of the _k_ = 8 methods across the _N_ = 66 synthetic datasets at a significance level of _α_ = 0 _._ 05. We visualise the results using CD diagrams (Demˇsar, 2006) for the AUC-ROC and AUC-PR.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
