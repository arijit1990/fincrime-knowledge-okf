---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 5 of 9 (pp. 19-25)
description: 'Verbatim extracted text, pp. 19-25: X; X; B; and 1 more sections'
resource: https://arxiv.org/abs/2405.19383
tags:
- academic_finding
- effectiveness
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-network-analytics-for-anti-money-laundering-a-systematic-literat
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-05-29'
legal_status: unknown
part: 5
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2405.19383
  title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation
  author: org:arxiv
  last_modified: '2024-05-29T00:00:00Z'
---

# Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 5 of 9, pp. 19-25. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## X


[p. 19]





h(l)

{h(l−1)

u , ∀u ∈Nv}

Nv = AGGREGATEl



h

i

h(l)

W (l) ·

h(l−1)

,

v = σ

v ∥h(l)

Nv

where ∥represents the concatenation operator.

The second extension is graph attention network (GAT) [132], which adds an attention mechanism. Our work uses the modified version of the attention mechanism, introduced to fix the static attention problem [16]:



i

W (l) h

h(l−1)

eij = aT LeakyReLU

v ∥h(l)

Nv

αij = softmaxj(eij)





h(l)

αijW (l)h(l−1)



i = σ

j .

j∈˜ Ni

As mentioned by Veliˇckovi´c et al. [132], having multiple mechanisms—also called heads—can improve stability. We follow Veliˇckovi´c et al. [132], where the intermediate steps concatenate the results over the heads, while the final layer averages the results.

The final method is the Graph Isomorphism Network (GIN) [144]. The authors used the Weisfeiler-Lehman graph isomorphism test to define the necessary conditions a GNN must satisfy to achieve maximal discriminative power. This discriminative power is denoted by how well the training data is fitted.

Using the universal approximation theorem [61, 60], GIN updates the representation using a multilayer percep- tron (MLP).







## X


h(l−1)

1 + ϵ(l) h(l−1)

h(l)

v = MLP(l)

v +





j

j∈Ni

Although this increases the risk of overfitting, the authors show that GIN has satisfactory generalisation capabilities. The main problem with other GNNs is that they tend to underfit the data [144]. Recent research showed GIN’s potential to outperform other GNN architectures [36, 123].

There are some key differences between the three categories presented in Table 11. The manual features need to be specifically defined, while representation learning tries to find meaningful embeddings automatically. Additionally, the manual features and the shallow representations are added to the intrinsic features, which are used in a down-stream classifier (as illustrated in Figure 5). The GNNs incorporate the intrinsic features and directly learn the embeddings on the classification task.

Different decoders are used for the final classification in the supervised setting. A neural network with two hidden layers, each of dimension ten is used for the manual features and shallow representation methods. For the graph neural networks, the GNN layers are followed by a single linear layer for making predictions.

For the unsupervised model, we apply isolation forest [80], as it achieves state-of-the-art performance for outlier/anomaly detection [122, 64]. This will be applied to the intrinsic and manual features, and the shallow representations, since it requires a tabular input. A larger experiment comparing unsupervised methods for network analytics is left for future work.

One of the objectives of this research is to provide the code for all methods in a clean and simple way and make these methods easily accessible to researchers and practitioners. The methods are implemented in Python. The manual

## B


[p. 20]

Network Embedding

ID F1 F2 . . . Fn A f11 f21 . . . fn1 B f12 f22 . . . fn2 ...

...

ID F1 F2 . . . Fn NF1 . . . NFm A f11 f21 . . . fn1 nf11 . . . nfm1 B f12 f22 . . . fn2 nf12 . . . nfm2 ...

...

... ... ...

... ... ... E f1k f2 . . . fnm

... ... ... E f1k f2 . . . fnm nf1k . . . nfmk

## D


[ref: 4.2]

Figure 5: For the feature engineering and shallow representation methods, the obtained network features/embedding is added to the intrinsic ones.

features are constructed using NetworkX [54] and NetworKit [7], and the representation learning is implemented in PyTorch Geometric [39]. The code is made available on GitHub2.

4.2 Data

The methods are compared on two data sets; the Elliptic [37, 134] and IBM money laundering [6, 36] data sets. These cover the two main lines of research in the literature. The Elliptic data set concerns real-world crypto-transactions, while the IBM data set deals with simulated transactions in fiat currencies.

4.2.1 Elliptic.

The Elliptic data set [37, 134] contains Bitcoin transactions for 49 time steps, each being around two weeks long. The network has 203 769 nodes and 234 355 edges. The nodes correspond to transactions, and an edge represents that the output of one transaction is the input of the next. Additionally, the data set contains 166 pre-calculated features. These are split into 94 transaction-specific, i.e., local features and 72 aggregated features, summarizing the local features of a node’s neighbours.

All features are numerical and have already been standardised. The local features will be used for all methods. Aggregated features are not included for the GNNs, since these methods aggregate the neighbourhood information, including the node features. This was also addressed by Weber et al. [134], stating that graph neural networks are better to address the heterogeneity of the neighbourhoods than the aggregated features.

Around 33% of transactions are labelled, 4 545 of which as illicit and 42 019 as licit. Hence, the classification problem is imbalanced with 2% of all nodes labelled illicit. We note that an illicit label does not automatically mean that the transaction is used to launder money. However, criminals will try to obscure the source of these illicit funds, so we believe that it is still informative. Section 3.2 also illustrated that this data set is widely used in AML research.

We use the Elliptic data set included in the Pytorch Geometric library [25, 39]. We split the periods into a train (period 1-30), validation (period 31-40) and test set (period 41-49). Only nodes having a label are used for performance evaluation. Transactions with label 2 (unknown) are included for the construction of the network, but they do not contribute to training or loss calculation [70, 147, 134].

4.2.2 IBM Money Laundering.

[pp. 20-21]

The second data set is the HI-Small data set, taken from Kaggle, consisting of simulated transactions in a virtual world between individuals, companies and banks [6, 36]. A fraction of these transactions are labelled as money laundering. Given that the labels are at transaction level, the network is constructed with the transactions as nodes. Edges are added from transaction vi to vj if the receiver of transaction vi is the sender of transaction vj, transaction vj happened before vi, and the difference in time is smaller than ∆t, i.e., ∆t ≥tj −ti ≥0. This is inspired by the work by Tariq and Hassani [120], and allows to capture the money flow. We take a 60-20-20 train-validation-test split based on transaction time.

2https://github.com/B-Deprez/AML_Network

Table 12: Network features for the Elliptic and IBM-AML data set. Network Nodes Edges Percentage Fraud Avg. Degree Avg. Path Length Clustering

Elliptic 203,769 234,355 2% 2.3 15.96 0.0117 IBM-AML 500,000 1,278,952 0.27% 5.1 3.78 0.0000

Since this results in a massive data set and hyperparameter tuning for DeepWalk and node2vec would take too long, we only take the last 500 000 transactions, and set ∆t to four hours. This results in a network with 500 000 nodes and 1 278 952 edges. Just 1356 transactions, i.e., 0.27%, are labelled as money laundering.

Each transaction has a couple of features, of which we use the following: ‘Amount Received’, ‘Receiving Currency’, ‘Amount Paid’, ‘Payment Currency’, ‘Payment Format’. Next to that, we extract the day of the week, hour and minute

out of a transaction’s date stamp. The categorical features, i.e., ‘Receiving Currency’, ‘Payment Currency’, ‘Payment Format’, are transformed using one-hot-encoding. In the remainder of this paper, we denote this data set as IBM-AML.

An analysis of the topology of both networks is given in Table 12, based on well-known network features. IBM-AML seems to be much more connected, compared to the Elliptic data set, having higher average degree and lower average path length. This is corroborated by the degree distribution and the distributions of the closeness centrality, in Figure 6 and Figure 7, respectively. The Elliptic data set more closely presents a scale-free distribution, while the IBM-AML data set deviates from this with fewer nodes with low degree and more nodes with higher degree (hubs). The hubs resulted in a much lower average path length, and higher closeness centrality values.

Degree distribution

[pp. 21-22] [ref: 0.0]

Elliptic IBM-AML

10 5

10 4

10 3

Frequency (log)

10 2

10 1

10 0

10 0 10 1 10 2 10 3

Degree (log)

Figure 6: Comparison of the degree distributions of the Elliptic and IBM-AML data sets.

Closeness distribution

Elliptic IBM-AML

Frequency

0.0 0.2 0.4 0.6 0.8 1.0 Closeness Centrality

Figure 7: Comparison of the distributions of the closeness centrality of the Elliptic and IBM-AML data sets.

4.3 Hyperparameter Tuning

The hyperparameters are tuned to maximises the AUC-PR on the validation set. However, it is not feasible to tune these using a grid search. As the methods often have many hyperparameters, the number of combinations increases

Table 13: The overview of the hyperparameter values for the supervised learning models. The tuned hyperparameter value is added between parentheses next to the name of the model.

Hyperparameter Tuning Range Model (hyperparameter value Elliptic | IBM )

[2, 10] ∩N DeepWalkS (2 | 2), node2vecS (5 | 9)

α: random jump parameter [0.1, 0.9] PageRankS (0.593 | 0.646) Number of walks per node [1, 3] ∩N DeepWalkS (2 | 2), node2vecS (1 | 3) Walk length [3, 10] ∩N DeepWalkS (3 | 7), node2vecS (9 | 9) Word2vec context window size

[2, 64] ∩N DeepWalkS (5 | 52), node2vecS (47 | 9)

Latent/Embedding dimension

Latent/Embedding dimension

[p. 22]

[32, 128] ∩N GCN (108 | 97), GraphSAGE (48 | 53), GAT (99 | 51), GIN (74 | 47) p: return parameter [0.5, 2] node2vecS (1.17 | 0.537) q: in-out parameter [0.5, 2] node2vecS (1.60 | 1.394) Number of negative samples [1, 5] ∩N DeepWalkS (1 | 1), node2vecS (1 | 4) GNN hidden dimensions [64, 256] ∩N GCN (NA | 88), GraphSAGE (NA | 175), GAT (NA | NA), GIN (NA | NA) GNN layers [1, 3] ∩N GCN (1 | 2), GraphSAGE (1 | 2), GAT (1 | 1), GIN (1 | 1) Learning rate [0.01, 0.1] IFS (0.0163 | 0.0770), ManualS (0.0166 | 0.0401), DeepWalkS (0.0554 | 0.0526), node2vecS (0.0159 | 0.0708), GCN (0.0225 | 0.0514), GraphSAGE (0.0248 | 0.0660), GAT (0.0421 | 0.0313), GIN (0.0345 | 0.0166) Aggregator {min, mean, max} GraphSAGE (mean | max) Number of attention heads [1, 5]∩N | [1, 2]∩N GAT (4 | 2) Dropout rate [0, 0.5] GCN (0.288 | 0.163), GraphSAGE (0.350 | 0.244), GAT (0.186 | 0.188), GIN (0.271 | 0.273) Number of layers decoder [1, 3] ∩N IFS (1 | 2), ManualS (1 | 2) Hidden dimension decoder [5, 20] ∩N IFS (5 | 14), ManualS (6 | 17) Number of epochs decoder [5, 500] ∩N IFS (497 | 450 ) Number of epochs decoder [5, 100] ∩N ManualS (64 | 59), DeepWalkS (80 | 75), node2vecS (93 | 75) Number of epochs [5, 500] ∩N | [5, 100] ∩N

[pp. 22-23]

DeepWalkS (176 | 75), node2vecS (222 | 84), GCN (483 | 325), GraphSAGE (498 | 399), GAT (280 | 341), GIN (218 | 89)

exponentially. Additionally, transaction networks are very large, which results in a relative long training time for each individual combination of hyperparameters. Therefore, we tune the hyperparameters efficiently via Optuna [2], whereby we give a range of possible values to select from. We use optuna’s default TPESampler sampler.

The ranges are summarised in Table 13 and 14, for supervised and unsupervised learning, respectively. We add superscript S and U to indicate that tuning is done for supervised and unsupervised learning, respectively. A model only based on the intrinsic features (IF) is included. The number of trials is set to 50 for DeepWalk and node2vec, and 100 for the GNNs.

Since the IBM data set is much larger, scalability in both time and memory are very important. Especially DeepWalk and node2vec take much time to run. The higher average degree also makes transition probability calculations more expensive. That is why the number of epochs for calculating the embedding are capped at 100. The attention mechanism of GAT is conditional on the query node, meaning that attention is learned for each node pair. To be able to train the model in memory, we limit the attention head to a maximum of two.

All decoders used for classification have a fixed architecture (Section 4.1). For the GNNs, the training of the decoder weights happens simultaneously with the other weights during training. For the manual and shallow representation features, the decoder/classifier needs to be trained afterwards. The only hyperparameter tuned is the number of epochs.

The tuned hyperparameters are presented in parentheses in Table 13 and Table 14.

Table 14: The overview of the hyperparameter values for the unsupervised learning models. The tuned hyperparameter value is added between parentheses next to the name of the model.

Hyperparameter Tuning Range Model (hyperparameter value Elliptic | IBM )

[2, 10] ∩N DeepWalkU (4 | 6), node2vecU (2 | 4)

α: random jump parameter [0.1, 0.9] PageRankU (0.187 | 0.117) Number of walks per node [1, 3] ∩N DeepWalkU (3 | 2), node2vecU (3 | 2) Walk length [3, 10] ∩N DeepWalkU (6 | 7), node2vecU (4 | 6) Word2vec context window size

[2, 64] ∩N DeepWalkU (64 | 6), node2vecU (63 | 47)

[p. 23] [ref: 4.4]

Latent/embedding dimension

DeepWalkU (17 | 46), node2vecU (59 | 50)

p: return parameter [0.5, 2] node2vecU (0.78 | 1.52) q: in-out parameter [0.5, 2] node2vecU (1.58 | 1.60) Number of negative samples [1, 5] ∩N DeepWalkU (4 | 5), node2vecU (4 | 1) Learning rate [0.01, 0.1] DeepWalkU (0.0948 | 0.0541), node2vecU (0.0414 | 0.062) Number of epochs [5, 500] ∩N | [5, 100] ∩N

Number of estimators [50, 200] ∩N IFU (60 | 119), ManualU (70 | 66), DeepWalkU (69 | 169), node2vecU (60 | 100) Max. number of samples [0.1, 1] IFU (0.484 | 0.111), ManualU (0.333 | 0.559), DeepWalkU (0.533 | 0.386), node2vecU (0.824 | 0.354) Max. number of features (%)

{10 ∗n | n ∈N10} IFU (0.1 | 0.9), ManualU (0.8 | 0.3), DeepWalkU (0.8 | 0.2), node2vecU (0.8 | 0.4) Bootstrap {True, False} IFU (True | False), ManualU (True | True), DeepWalkU (True | False), node2vecU (True | True)

4.4 Performance Metrics

We tackle money laundering as a binary classification problem. We adopt the most popular performance metrics from the literature, namely the precision, recall and F1-score (Section 3.2). These require a classification threshold. Since investigation resources are limited [129], the thresholds will be set relatively high, e.g., by classifying the top 0.1%, 1% or 10% of scores as money laundering. This is supplemented by a threshold equal to the relative prevalence of money laundering in the data sets.

[pp. 23-24] [ref: 5.1]

The selection of these thresholds is ad-hoc, and can influence the conclusions. Therefore, we also include threshold- independent metrics. The most popular one for binary classification is the area under the ROC curve (AUC-ROC). The ROC curve plots the true positive rate against the false positive rate. However, in highly imbalanced data sets with many negative samples, the false positive rate can appear low even when the absolute number of false positives is high, making it less sensitive to performance issues in detecting the minority class [26, 111]. The area under the precision-recall curve (AUC-PR) is better suited to compare these models [26, 102, 111]. This also adds to the literature, since we showed in Section 3.2 that few papers base their conclusions on the AUC-PR.

To test model stability, the models are trained 10 times on a randomised version of the training set. The manual network features and shallow representation embeddings result in classic tabular features (cf. Figure 5). For these, we apply a bootstrap method, where a new train set is constructed of the same size as the original, where the observations are sampled with replacement. The deep representation methods apply train masks. We initialise new train masks by randomly selecting half the train masks from the original ones.

5 Results and Discussion

5.1 Supervised Learning

The results for the threshold-independent metrics, i.e., AUC-ROC and AUC-PR, on the test set are shown in Table 15, including the standard deviation calculated as described in Section 4.4. Additionally, the threshold-dependent results, i.e., precision, recall and F1-score, are given in Table 16 and Table 17 for the top-1% results. To analyse the sensitivity to the threshold, we report the results on the other three thresholds in Appendix C.

Table 15: Threshold-independent metrics: AUC-ROC and AUC-PR values over the different methods for the two data sets, based on the test set. The standard deviation is also reported.

Supervised Elliptic IBM-AML Methods AUC-ROC AUC-PR AUC-ROC AUC-PR

[p. 24]

Intrinsic features 0.8607 ± 0.0079 0.5730 ± 0.0958 0.7560 ± 0.0075 0.0186 ± 0.0008 Egonet features 0.8648 ± 0.0090 0.5956 ± 0.0328 0.7579 ± 0.0033 0.0187 ± 0.0004 DeepWalk 0.8483 ± 0.0083 0.5823 ± 0.0265 0.7558 ± 0.0033 0.0185 ± 0.0004 Node2vec 0.8497 ± 0.0044 0.5938 ± 0.0251 0.7551 ± 0.0031 0.0184 ± 0.0004 GCN 0.8465 ± 0.0110 0.5948 ± 0.0164 0.5657 ± 0.0904 0.0113 ± 0.0029 GraphSAGE 0.8712 ± 0.0122 0.6392 ± 0.0336 0.6068 ± 0.0793 0.0120 ± 0.0028 GAT 0.8579 ± 0.0161 0.6376 ± 0.0270 0.4203 ± 0.1889 0.0103 ± 0.0041 GIN 0.8213 ± 0.0203 0.5079 ± 0.0593 0.5028 ± 0.2533 0.0119 ± 0.0065

Table 16: Threshold-dependent metrics: Precision, recall and F1-score values for the top 1% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Elliptic Supervised Methods Precision Recall F1-score

Intrinsic features 0.8570 ± 0.2706 0.1840 ± 0.1173 0.2932 ± 0.1451 Egonet features 0.9339 ± 0.0463 0.1645 ± 0.0082 0.2797 ± 0.0139 DeepWalk 0.9116 ± 0.0464 0.1881 ± 0.0895 0.3049 ± 0.1054 Node2vec 0.9321 ± 0.0465 0.1642 ± 0.0082 0.2791 ± 0.0139 GCN 0.9911 ± 0.0094 0.1728 ± 0.0047 0.2942 ± 0.0070 GraphSAGE 0.9822 ± 0.0188 0.1721 ± 0.0077 0.2929 ± 0.0113 GAT 0.9964 ± 0.0075 0.1753 ± 0.0067 0.2981 ± 0.0099 GIN 0.9286 ± 0.0709 0.1633 ± 0.0129 0.2777 ± 0.0214

Table 17: Threshold-dependent metrics: Precision, recall and F1-score values for the top 1% scores over the different methods for the IBM-AML data set, based on the test set. The standard deviation is also reported.

IBM-AML Supervised Methods Precision Recall F1-score

[pp. 24-25]

Intrinsic features 0.0190 ± 0.0040 0.0210 ± 0.0044 0.0200 ± 0.0042 Egonet features 0.0192 ± 0.0034 0.0213 ± 0.0038 0.0202 ± 0.0036 DeepWalk 0.0174 ± 0.0053 0.0193 ± 0.0059 0.0183 ± 0.0056 Node2vec 0.0181 ± 0.0047 0.0200 ± 0.0052 0.0190 ± 0.0049 GCN 0.0100 ± 0.0045 0.8807 ± 0.3119 0.0197 ± 0.0089 GraphSAGE 0.0119 ± 0.0027 0.9742 ± 0.0298 0.0236 ± 0.0052 GAT 0.0065 ± 0.0070 0.1805 ± 0.3695 0.0104 ± 0.0139 GIN 0.0085 ± 0.0087 0.0166 ± 0.0087 0.0092 ± 0.0089

For both data sets, the models with intrinsic features give already good result. Adding egonet features is beneficial for both data sets. We do, however, see a drop in performance for DeepWalk and node2vec. It is possible that some of the feature values, i.e., the coordinates in the latent space, are correlated or noisy. Neural networks, used here as the decoder for classification, are known to suffer under correlated and noisy features [51]. GIN also performs poorly on both data sets. One explanation is that the neural network in the aggregation step is not optimal, and should be tuned further. Another explanation is that the inclusion of neural network aggregation makes GIN more sensitive to the high class imbalance. Hence, GIN seems less suited for anti-money laundering. It should be noted that good performance is observed for the precision indicating that GIN reduces false positives in the top-percentiles of predictions.

When looking at the Elliptic data set, we see that also the GNNs appear to underperform, except for GraphSAGE. Additionally, GAT has good AUC-PR performance. We see in Tables 16, C1, C3 and C5 that for the top percentages the GNNs have remarkably higher precision, but lower recall. Although fewer cases are detected, those with highest predicted money laundering propensity contain far fewer false positives. This is highly important when adopting these models in practice.


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
