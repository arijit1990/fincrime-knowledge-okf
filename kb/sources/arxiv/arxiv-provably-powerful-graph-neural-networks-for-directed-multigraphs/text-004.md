---
type: Source Text
title: Provably Powerful Graph Neural Networks for Directed Multigraphs - part 4 of 5 (pp. 12-16)
description: 'Verbatim extracted text, pp. 12-16: Provably Powerful Graph Neural Networks for Directed Multigraphs > D Synthetic Pattern Detection Datasets; Provably Powerful Graph Neural Networks for Directed Multigraphs > E AML and ETH Datasets; Provably Powerful Graph Neural Networks for Directed Multigraphs > F Experimental Details; and 2 more sections'
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
part: 4
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.11586
  title: Provably Powerful Graph Neural Networks for Directed Multigraphs
  author: org:arxiv
  last_modified: '2023-06-20T00:00:00Z'
---

# Provably Powerful Graph Neural Networks for Directed Multigraphs

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (arXiv, 2023-06-20), part 4 of 5, pp. 12-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Provably Powerful Graph Neural Networks for Directed Multigraphs


### D Synthetic Pattern Detection Datasets


#### D.1 Random Circulant Graphs


[p. 12]

This model is similar to the Watts–Strogatz small-world model (Watts and Strogatz 1998), where nodes are also arranged in a ring, each node is connected to its k nearest neighbors, and edges are randomly rewired with a chosen

Algorithm 2: Random Circulant Graph Generator

Parameters : Number of nodes _n_ , average degree _d_ , locality radius _r_ .

Output : A graph _G_ = ( _V, E_ ).

- 1: _Nedges ←⌊__nd_ 2_⌋_ 2: _⃗u ←_ ( _ui | i_ = 1 _, . . . , Nedges_ ) _∼_ iid unif( _{_ 1 _, . . . , n}_ ) _▷_ Sample tail nodes

- 3: _⃗v ←_ ( _vi | i_ = 1 _, . . . , Nedges_ ) _∼N_ iid ( _ui, r_ ) _▷_ Sample head nodes

- 4: _⃗v ←_ ( _⌊vi_ +1 2_⌋| i_= 1_, . . . , Nedges_) _▷_ Round head nodes to nearest integer

- 5: _V_ ( _G_ ) = _{_ 1 _, . . . , n}_ 6: _E_ ( _G_ ) = _{_ ( _ui, vi_ ) _| i_ = 1 _, . . . , Nedges}_

probability. However, standard Watts–Strogatz implementations produce undirected graphs and do not allow for multiple edges between a pair of vertices. In particular, a randomly oriented Watts-Strogatz graph — a directed graph created by generating an undirected Watts-Strogatz graph, and then choosing an arbitrary direction for each edge independently and uniformly at random — doesn’t allow for testing the detection of directed cycles of length 2 and fan patterns (without parallel edges fan patterns are identical to degree patterns).

#### D.2 Pattern Detection Tasks


The synthetic pattern detection dataset includes the following (sub-)tasks:

- Degree-in (-out): Degree -in and -out of a node is the number of incoming and outgoing transactions respectively. Note that multiple transactions can come from the same node, and these are counted separately.

- Fan-in (-out): Fan -in and -out of a node is the number of unique incoming and outgoing neighbors, respectively. Neighbors with multiple edges are counted only once, but a node can contribute to both the fan-in and fan-out counts, as it can be both an incoming and outgoing neighbor.

- Cycle (k): A node receives a positive label if it is part of a directed cycle of length _k_ . We only consider directed cycle patterns and omit the word “directed”.

- Scatter-Gather: A node receives a positive label if it is the _sink_ node of a scatter-gather pattern with at least 2 _intermediate_ nodes. A scatter-gather pattern consists of a _source_ node, _intermediate_ nodes, and a _sink_ node. Given a _sink_ node _v_ , a node _u_ is considered a _source_ node if there is a directed path of length 2 from _u_ to _v_ . A node _wi_ is considered an _intermediate_ node if there is a directed path of length 2 from _u_ to _v_ through _wi_ , i.e., if both ( _u, wi_ ) and ( _wi, v_ ) are in _E_ ( _G_ ). Note that a scattergather pattern with a single intermediate node is simply a directed path of length 2. This does not capture the pattern we are interested in, so we require at least 2 intermediate nodes.

- Gather-Scatter: We do not explicitly include this pattern as a subtask since it is a combination of fan-in and fan-out.

[p. 13]

|Subtask|Threshold|Positive Ratio|Dataset|# nodes|# edges|Illicit Ratio|
|---|---|---|---|---|---|---|
|Degree-in|>3|0.352|AML Small HI|0.5M|5M|0.07%|
|Degree-out|>3|0.349|AML Small LI|0.7M|7M|0.05%|
|Fan-in|>3|0.324|AML Medium HI|2.1M|32M|0.11%|
|Fan-out|>3|0.323|AML Medium LI|2.0M|31M|0.05%|
|Cycle (2)Cycle (3)|--|0.1910.344|ETH|2.9M|13M|0.04%|
|Cycle (4)Cycle (5)Cycle (6)|---|0.5270.6770.779|Table 4: AML and ETillicit ratio and LI indic|H task statiates a low|stics. HI iner illicit ra|dicates a higtio.|
|Scatter-Gather|-|0.321|||||
|Biclique|-|0.318|||||

Table 4: AML and ETH task statistics. HI indicates a higher illicit ratio and LI indicates a lower illicit ratio.

test indices to transactions after _t_ 2. However, the validation and test set transactions need access to the previous transactions to identify patterns. So we construct train, validation, and test graphs. This corresponds to considering the financial transaction graph as a dynamic graph and taking three snapshots at times _t_ 1, _t_ 2, and _t_ 3 = _tmax_ . The train graph contains only the training transactions (and corresponding nodes). The validation graph contains the training and validation transactions, but only the validation indices are used for evaluation. The test graph contains all the transactions, but only the test indices are used for evaluation. This is the most likely scenario faced by banks and financial authorities who want to classify new batches of transactions.

Table 3: Synthetic pattern detection task statistics

- Biclique: A biclique (or complete bipartite graph) is a bipartite graph, where every node of the first set is connected to every node of the second set. We consider a special case of the directed biclique, where every node in the first set has at least one outgoing edge to every node in the second set. We call the nodes in the first set _source_ nodes, and the nodes in the second set _sink_ nodes. The task is to identify all nodes that are the sink nodes of some directed _K_ 2 _,_ 2 biclique with (at least) 2 source nodes and (at least) 2 sink nodes.

#### E.2 ETH Dataset


All the (sub-)tasks are combined in one overall task, i.e., the output of the models is a vector, where each element of the vector corresponds to one of the subtasks.

The Kaggle dataset was constructed by starting from 1165 reported phishing nodes and crawling the whole Ethereum transaction network via breadth-first search. The dataset originally comes with four edge features: transaction time, transaction amount, source node address, and destination node address. Each node has one feature, the account address. As this information is minimal, we enhance the dataset with additional transaction features taken directly from the blockchain using Ethereum ETL (Medvedev 2022). We add nonce, block number, gas, and gas price. These are cryptocurrency terms for the number of transactions made by the sender prior to the given transaction; the block containing this transaction; and the transaction fees the sender provided for the transaction to go through. Table 4 shows the number of nodes (accounts) and edges (transactions) and the illicit ratio. Unlike AML, this is a node classification task, where the goal is to classify nodes as phishing accounts.

We implement pattern detection algorithms to find the desired patterns and generate binary node labels. The parameters are adjusted to achieve relatively balanced labels, but since a perfect split (for all subtasks) is not guaranteed, we rely on minority class F1 scores rather than accuracy to measure the performance of our models. All subtasks in the final dataset have at least 19% and at most 68% positive labels.

Thresholds are used in some cases to produce binary labels. For example, for the degree-in task, nodes with an in-degree greater than 3 receive the label 1, while low in-degree nodes receive the label 0. For degree-in/-out and fan-in/-out the threshold is 3. For degree-in-time-span and maximum-degreein the thresholds are 1 and 4 respectively. Examples of the patterns are provided in Fig. 1.

We use _n_ = 8192 nodes, average degree _d_ = 6, and radius _r_ = 11 _._ 1 to generate our pattern detection data. To avoid any information leakage between train, validation, and test sets, we generate an independent random circulant graph _Gn,d,r_ for each dataset. Table 3 shows the thresholds and distribution of labels for each subtask.

Unlike the AML use case, we do not know a priori what subgraph patterns to look for to identify phishing nodes. To this end, we defined _fraudulent clusters_ and visualized these to give an indication of the patterns our model might need to detect. The clusters were constructed by starting from the 1165 reported phishing nodes, adding their 1-hop neighborhoods, and then joining any clusters sharing a common node. Fig. 8 shows an example of one of these fraudulent clusters.

### E AML and ETH Datasets


#### E.1 AML Data Split


[pp. 13-14]

Similar to AML, we use a temporal train-validation-test split, but this time we split the nodes. We order the nodes by the first transaction they are involved in (either as sender or receiver) before splitting. Again this gives us threshold times _t_ 1 and _t_ 2, and we use these times to create our train, validation, and test graphs. See the AML dataset split for

We use a 60-20-20 temporal train-validation-test split, i.e., we split the transaction indices after ordering them by their timestamps. The data split is defined by two timestamps _t_ 1 and _t_ 2. Train indices correspond to transactions before time _t_ 1, validation indices to transactions between times _t_ 1 and _t_ 2, and

Figure 8: One of the fraudulent clusters identified in the ETH phishing dataset. The patterns that might help identify a fraudulent node are mostly 1-hop, namely in-degree, outdegree, fan-in, fan-out patterns, and 2-cycles.

more details. This time we use a 65-15-20 split because the illicit accounts are skewed towards the end of the dataset, with few illicit accounts in the first half of the data.

### F Experimental Details


#### F.1 Hyperparameter Tuning and Scoring


[p. 14]

We used random sampling to identify a good range of hyperparameters. A second round of random sampling was conducted with this narrower range to pick our final set of hyperparameters. We varied the following hyperparameters: the number of GNN layers, hidden embedding size, learning rate, dropout, and minority class weight (for the weighted loss function). The number of random samples ranged between 10 to 50, depending on the training time of the model on a particular dataset.

To get our final results, we use the hyperparameters with the best validation score to train five models initialized with five different random seeds. The results of the five runs are then averaged and the standard deviation is calculated to give the reported scores.

#### F.2 LightGBM with Graph-based Features


We include a LightGBM baseline using pre-calculated graph features to classify nodes or edges individually. Calculating complex subgraph features naively can be prohibitively expensive, therefore we rely on efficient implementations (Blanuša, Atasu, and Ienne 2023; Blanusa, Ienne, and Atasu 2022; Altman et al. 2023) to enumerate subgraph patterns.

We use these graph-mining algorithms to enumerate the suspicious patterns introduced in Fig. 1. We enumerate on a fine-grained level, counting patterns of different sizes separately. For the edge classification tasks (AML) we count patterns that an edge is contained in and add these counts as additional edge features. We do the same with nodes for the node classification task (ETH).

We train a LightGBM (Ke et al. 2017) model on the individual edges (or nodes) with the full set of features (original raw features and additional graph-based features). The pattern enumeration can be restricted to a certain time range; we

|Model|TTT (s)|TPS (inference)|
|---|---|---|
|GIN|1876|53130|
|Individual Adaptations|||
|GIN+Ports|2007|58663|
|GIN+EgoIDs|1873|58533|
|GIN+ReverseMP|12510|21067|
|Cumulative Adaptations|||
|GIN+ReverseMP+Ports|13051|18763|
|+EgoIDs|12958|18700|

Table 5: Total training times (TTT) and Transaction per Second (TPS) for all GIN-based models on the AML Small HI dataset. The TPS values were measured in evaluation mode.

optimize the range (as a hyperparameter) for each dataset to get the best performance.

#### F.3 Synthetic Pattern Detection Experiments


Unlike the much larger AML and ETH datasets, we do not have to subsample the neighborhood. Instead, we use the whole 3-hop neighborhood in our model to ensure that all of the patterns can be found. Moreover, we used six GNN layers to ensure that 6-cycles can also be detected.

Since this is an edge classification dataset, all GNNs use a final edge readout layer that takes the edge embedding and the corresponding endpoint node embeddings as its input. We use neighborhood sampling, sampling 100 one- and two-hop neighbors respectively. We remove node IDs from edge and node features to avoid, as far as possible, overfitting to the fraudulent node IDs. Since we know what financial crime patterns were used for generating this dataset, we use the graph mining library to enumerate exactly these suspicious patterns for each transaction: degree-in/-out, fan-in/-out, directed cycle, undirected cycle, and scatter-gather patterns of different sizes. We leave out bicliques, as these are not currently included in the library. For the low IR dataset, we took the hyperparameters from the corresponding high IR dataset and only optimized the minority class weight. We found that this has to be optimized to account for the greater class imbalance.

#### F.5 AML Runtimes


[pp. 14-15]

Table 5 shows the runtime cost of adding the adaptations to GIN when running on the AML Small HI dataset. The size of the GNN models was kept the same: 2 GNN layers and a hidden size of 64. All models were run on an Nvidia GeForce RTX 3090 GPU.

Since this is a node classification dataset, all GNNs use a final node readout layer that takes only the corresponding node embedding as its input. We use neighborhood sampling, sampling 1000 one- and two-hop neighbors respectively.

|Dataset|# nodes|# edges|# node feats|# classes|
|---|---|---|---|---|
|Chamaleon|2,277|36K|2,325|5|
|Squirrel|5,201|217K|2,089|5|
|Arxiv-Year|169K|1.17M|128|40|

#### F.6 ETH Experiments


[p. 15]

Table 6: Real-World dataset statistics.

|Model|Squirrel|Chameleon|Arxiv-Year|
|---|---|---|---|
|Grad. Gating (SOTA)|64_._26_±_ 2_._38|71_._40_±_2_._38|63_._30_±_1_._84|
|GIN (GCN_∗_)|35_._94_±_2_._01_∗_|51_._29_±_0_._63|50_._15_±_0_._26|
|+ReverseMP|59_._84_±_2_._08_∗_|66_._36_±_1_._23|63_._31_±_0_._45|
|+Ports|59_._33_±_2_._40_∗_|73_._46_±_0_._97|68_._12_±_ 0_._51|
|+EgoIDs|58_._41_±_2_._49_∗_|73_._73_±_ 1_._03|68_._04_±_0_._60|

Table 7: Comparison with state-of-the-art (Rusch et al. 2022) results on three real-world directed graph datasets.

For the LightGBM baseline, we use the graph mining library to enumerate the same graph-based patterns as for AML, but this time for nodes. Additionally, we calculate basic node statistics (such as averages, maximums, and variances) of the transaction amounts and the time between transactions to improve the baseline further. The statistical features give a significant boost to the minority class F1 scores, from 27 _._ 1% with only raw and graph-based features to above 50% with the additional statistical features.

|Model|C4|C5|C6|S-G|B-C|
|---|---|---|---|---|---|
|DropGIN|16.92|26.02|45.17|48.87|51.59|
|R-GCN|65.57|64.35|71.27|59.23|55.61|
|PPGN|57.93|48.74|41.15|54.23|54.98|
|Multi-DropGIN|99.09|97.08|94.93|96.98|94.27|
|Multi-R-GCN|85.20|74.08|74.30|82.37|67.16|
|Multi-PPGN_∗_|98.11|92.49|86.69|68.74|62.78|
|Multi-PNA|99.49|97.46|88.75|99.07|96.77|

Table 8: Additional subgraph detection results (F1 scores). Multi-PNA is included for comparison._∗_ No port numbers.

Figure 9: Performance of Multi-GIN on the “complex” subtasks as training dataset size is increased.

### G Additional Real-World Benchmarks


The theory results and the subgraph detection tasks demonstrate the general purpose potential of the architectural adaptations. Indeed, many of the subgraph patterns we consider could also be relevant to other areas. However, testing our model on real-world benchmark datasets is crucial to support these claims. Therefore we have taken three real-world directed graph datasets and compared our approach with the state-of-the-art (SOTA) model for these 3 benchmarks (Rusch et al. 2022). A summary of the dataset statistics can be seen in Table 6.

We report results for GIN with various adaptations. The models are set up as in our previous experiments. We use the Adam optimizer and train the model for 2000 epochs, using early stopping on the validation accuracy with a patience of 400. We do a single run of random sampling to optimize the hyperparameters within a predefined range. We sample 20 different sets of hyperparameters, and take choose the best performing model. We use the standard data splits for the datasets: For Chameleon and Squirrel we use the fixed GEOM-GCN splits (Pei et al. 2020), and for Arxiv-Year we use the splits provided by Lim et al. (2021). We report the mean and standard deviation of the test accuracy, calculated over 10 different data splits. The results can be seen in Table 7. We outperform SOTA in 2 out of the 3 benchmarks. On one dataset in particular the gain is almost 6 percentage points.

### H Additional Subgraph Detection Results H.1 Additional GNN Baselines


There are many “expressive” GNN architectures that have been developed for simple (no loops or parallel edges), undirected graphs with subgraph detection in mind. For example, PPGN (Maron et al. 2019) and DropGIN (Papp et al. 2021) to name a few. However, as we argue in Section 6 _Base GNNs and Baselines_ , none of these has been developed for directed multigraphs, and their ability to detect subgraphs unfortunately does not translate into this setting. For instance, since none of these models consider the direction of edges, they cannot distinguish between incoming and outgoing neighbors. Some of these architectures could be adapted to the setting, and in some cases, our proposed adaptations offer a possible approach to do so. To support our argument, we have added more baselines for the subgraph detection experiments, please see Table 8 for the results. When possible, we also include adapted versions based on our proposed adaptations. The architectures are indeed unable to perform well without adaptation.

#### H.2 Complex Patterns and Dataset Size


[pp. 15-16]

Additional experiments were carried out to measure the influence of dataset size on the subgraph detection tasks. We restrict these experiments to the GIN model with all the adaptations. We also restrict to the more “complex” tasks that

|No. Training Nodes|C4|C5|C6|S-G|B-C|
|---|---|---|---|---|---|
|1024|65.22_±_3.34|61.38_±_7.25|59.97_±_7.30|65.12_±_2.83|60.11_±_2.86|
|2048|78.06_±_6.19|72.44_±_4.48|70.19_±_2.49|75.82_±_4.77|67.82_±_1.53|
|4096|95.85_±_0.86|92.06_±_1.81|76.57_±_0.96|92.90_±_1.29|89.64_±_1.74|
|8192_∗_|97.46_±_0.43|91.60_±_1.50|84.23_±_1.12|97.42_±_0.85|94.33_±_0.95|
|8192|99.46_±_0.05|97.92_±_0.26|93.72_±_0.75|98.77_±_0.18|97.75_±_0.21|
|16384|99.72_±_0.06|98.66_±_0.15|97.24_±_0.19|99.61_±_0.08|99.53_±_0.07|

Table 9: Minority class F1 scores for the “complex” subgraph detection tasks with different dataset sizes. Multi-GIN is used in all experiments. The_∗_ indicates that these results are copied from Table 1, where all subgraph tasks were learned at once. All other experiments were restricted to the subtasks shown.

[p. 16]

|No. Training Nodes|C2|C3|C4|C5|C6|C7|C8|C9|C10|
|---|---|---|---|---|---|---|---|---|---|
|2048|97.53|89.72|84.71|80.60|75.48|81.34|91.51|93.57|93.39|
|4096|99.51|96.49|95.23|89.75|85.71|85.85|90.69|94.52|96.09|
|8192|99.83|99.78|99.13|97.17|93.58|89.93|91.87|94.92|96.64|
|16384|99.96|99.95|99.75|99.01|97.46|95.89|95.15|96.45|97.64|
|32768|99.99|100.00|99.93|99.62|98.76|97.98|97.93|98.10|98.30|
|65536|100.00|100.00|99.96|99.80|99.36|98.89|98.73|98.86|98.83|

Table 10: Minority class F1 scores for detecting cycles of increasing lengths with different training dataset sizes. Multi-GIN is used in all experiments.

|Model|deg-in|deg-out|fan-in|fan-out|C2|C3|C4|C5|C6|S-G|B-C|
|---|---|---|---|---|---|---|---|---|---|---|---|
|GIN|99.63|45.70|99.49|42.15|35.48|57.04|51.07|45.66|48.32|69.38|63.85|
|GIN+EgoIDs|99.90|51.51|99.64|49.92|98.89|93.71|57.89|49.08|49.78|67.27|62.88|
|GIN+Ports|99.84|42.33|99.51|38.61|33.72|55.77|55.43|47.25|46.79|68.89|65.68|
|GIN+ReverseMP|98.64|98.73|97.74|98.83|40.09|61.10|72.34|70.27|74.55|66.44|66.26|
|+Ports|99.03|99.44|99.35|99.37|43.15|63.15|68.20|68.29|73.67|68.02|66.87|
|+EgoIDs (Multi-GIN)|99.68|99.71|99.76|99.52|99.02|99.13|97.93|93.88|82.83|99.47|98.81|

Table 11: Subgraph detection results with parallel edges combined into single weighted edges.

|Model|deg-in|deg-out|fan-in|fan-out|C2|C3|C4|C5|C6|S-G|B-C|
|---|---|---|---|---|---|---|---|---|---|---|---|
|GIN|99.91|44.68|95.26|40.72|25.05|55.30|46.73|43.61|47.32|65.97|63.58|
|GIN+EgoIDs|99.82|52.56|95.67|49.78|98.67|95.78|54.56|45.95|48.01|69.00|64.93|
|GIN+Ports|98.88|44.49|99.16|40.71|27.84|55.73|48.03|43.30|47.78|66.46|63.04|
|GIN+ReverseMP|98.58|99.24|93.19|94.23|38.18|62.62|69.74|69.08|74.07|65.83|63.67|
|+Ports|98.36|98.31|99.01|99.37|37.13|61.88|72.12|71.04|76.47|65.00|66.89|
|+EgoIDs (Multi-GIN)|99.31|99.05|99.36|99.37|98.28|97.97|95.92|87.82|78.15|96.83|91.26|

Table 12: Subgraph detection results using random unique integer node IDs.


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: arXiv, "Provably Powerful Graph Neural Networks for Directed Multigraphs" (2023-06-20). https://arxiv.org/abs/2306.11586
