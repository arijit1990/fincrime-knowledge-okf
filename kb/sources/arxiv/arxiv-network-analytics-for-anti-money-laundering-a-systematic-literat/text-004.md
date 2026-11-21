---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 4 of 9 (pp. 15-19)
description: 'Verbatim extracted text, pp. 15-19: AUPRC'
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
part: 4
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2405.19383
  title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation
  author: org:arxiv
  last_modified: '2024-05-29T00:00:00Z'
---

# Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 4 of 9, pp. 15-19. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## AUPRC


[pp. 15-16] [ref: 3.3.4]

Statistical Evaluation [41], [137], [151], [78], [13], [152], [150]. Interpretation [33], [137], [13], [152]. Economical Evaluation [150]. Implementation [33], [88], [151], [78], [101],[152], [150].

Although detecting money laundering is in principle trying to find anomalous behaviour, very few studies deal with (unsupervised) anomaly detection [85, 108, 34], leaving possibilities for future work.

(Semi-)Supervised learning methods deal with different aspects of money laundering. Their strength lies in a combination of (1) the methods used and (2) tailoring the network to the problem at hand. The obtained network features are put into downstream classifier. To maintain interpretability, network metrics are recalculated for multiple networks, each representing a specific aspect of the data, to extract predictive features [41, 137]. Promising methods are based on deep learning [152], but these are mostly black boxes. Research on the interpretability of deep network representation methods is still scarce [74].

Table 10: Papers per fraud detection challenge, based on Bockel-Rickermann et al. [14].

Challenge Papers

Original

Automation [113], [23], [152]. Class Imbalance [137], [13]. Concept Drift [41], [13]. Data Availability [41], [22], [137], [87], [101], [150]. Feature Construction [101]. Noisy Data [113], [137], [87]. Stream Data [113], [88], [152]. Real-Time Execution [41]. Scalability [151], [101], [152]. Unlabelled Data [113], [137], [13], [152]. Verification Latency [150].

New

Bias in data [87], [150]. Generalisation [152]. Robustness [78]. Anonymity [88], [137], [13].

Visualisation of transaction networks is developed to support the experts in during investigations. This is either done by having a overview of the flow of money over different transactions [88, 22] or by finding specific relations among the persons involved [113, 29, 23]. Hence, these methods are mostly intended to be used after suspicion has been raised. None of them include an evaluation of the added value in money laundering detection.

3.3.4 Challenges.

Table 10 summarises the papers according to the challenges identified by Bockel-Rickermann et al. [14]. It only contains those challenges mentioned in the literature. The main challenge is data availability, followed by unlabelled data. Due to privacy issues, only a limited number of anonymised data is available. Additionally, since transaction data sets are often huge and resources are limited, it is hard to provide all instances with a label.

[pp. 16-17] [ref: 3.4]

Few papers mention feature construction, real-time execution, or verification latency as a challenge. Anti-money laundering is less reliant on execution time, since the investigation is done after the fact, based on a longer history of transactions [75].

We introduce four additional challenges observed in the anti-money laundering literature, supplementing Bockel- Rickermann et al. [14]. We view this as an extension of the framework since these challenges can be important to fraud research in general.

• Bias in data affects the performance of the model and manifests itself in different ways. First, there is bias in the missing values [87]. Second, detection bias [150] can be present in synthetic data when specific patterns are present that the model is trained to look for. • Generalisation is mainly used in two ways. One way refers to the ability for methods developed for anti-money laundering to be used for other fraud domains as well [152]. Another and important use of the term refers to the need for methods to generalise to unseen data [49], often referred to as inductive methods (compared to transductive ones). This is an important consideration when selecting network-based methods [56, 127, 128]. • Robustness of a method is important since money laundering can be seen as an adversarial attack [78], as perpetrators try to avoid detection by the methods. • Anonymity of the account data gives rise to two main challenges. First, the identity of the account holder is unknown in crypto data sets, which makes it almost impossible to know if different accounts - also called wallets - belong to the same person [137]. Second, financial institution possess customer data, but due to privacy reasons, researchers cannot publish these. Hence, published articles avoid using Personally Identifiable Information all together [13].

3.4 Further Considerations

Based on the observations made above, we give an intermediate conclusion and perspective on future work. The methods in the literature still rely heavily on expert-based methods, i.e., manual feature engineering and rule-based

systems, but deep learning methods are gaining traction. A more detailed analysis of these methods is needed to evaluate their performance properly, especially given that the current literature barely applies threshold-independent metrics meant for highly skewed data, like the AUC-PR. Moreover, the top-cited papers barely compare their methods to other baselines. This detailed analysis is the topic for the second part of this paper.

Different gaps in the literature exist. A first gap was also identified by Kute et al. [74], namely the lack of interpretation tools. Future work should interpretation methods to try and explain the output of graph neural networks.

[p. 17] [ref: 4.1]

A second gap concerns the under-representation of classic unsupervised methods [21, 3]. Future work should analyse the effectiveness of unsupervised learning in networks to find anomalous behaviour. This can be beneficial since many clients and transactions are effectively unlabelled, and the modi operandi for money laundering keep evolving. The second part of this paper will introduce a first way of applying such unsupervised learning methods, but a more extensive study is needed.

A third is that most research studies static networks. Some research is being done to incorporate the time-dynamic nature of transaction networks using recurrent neural networks, but we believe that much more can still be done.

A fourth gap is related to the inherent incompleteness of labels in AML. As criminals try to cover their tracks and financial institutions have only limited resources [129, 106], it is a given that there are still many money laundering cases that stay unnoticed. These transactions are seen as having label 0 when training the models, resulting in a positive and unlabelled (PU) problem. Specific PU-learning methods for networks should be applied when training a model.

A fifth gap is related to the limited resources as well. Since not all clients and transactions can be investigated, the predictions should take this into account. One way of dealing with this is learning-to-rank [28, 130], which has already been shown to be effective in fraud detection. The main benefit is that the goals is to correctly rank the most suspicious clients, while less importance is given to have a correct ranking for less suspicious clients. Although this is highly relevant, it has not yet been applied to the AML literature using network analytics.

4 Experimental Set-Up

To the best of our knowledge, a benchmark study comparing the state-of-the-art network learning methods for anti- money laundering is still missing. This section describes the experimental framework to fill this gap, including model specification (Section 4.1), data (Section 4.2), hyperparameter tuning (Section 4.3) and performance metrics (Section 4.4). The focus is on supervised learning, but unsupervised learning is also explored. Given challenges in open-source data availability, we present results on two data sets and provide code to facilitate reproducible experiments. We hope this framework will support and expand future research, and allows uniform publishing and comparing of results on proprietary data without the need to disclose sensitive information.

4.1 Model Specification

To set up the experimental evaluation, we start from the wider literature on network representation. Extensive overviews are given by Cai et al. [18], Hamilton et al. [56] and Goyal and Ferrara [50]. A sub-branch of representation learning applies deep learning methods [153, 139]. Based on these papers, we select the methods that are most prominently used.

[pp. 17-18]

We refined the selection by considering that, for AML, transaction data contains networks with millions of nodes and edges, making scalability an important selection criterion. Table 11 provides an overview of the methods selected. They are grouped into three categories [18, 56, 50]: manual feature engineering, shallow representation learning and deep representation learning. These methods will be tested against a baseline model that only includes the intrinsic features, denoted by IF.

Manual feature engineering includes both local and global metrics. The first is the density of the ego-network. A node’s ego-network consists of the node, its direct neighbours and all connections between the neighbours. The density is the relative number of connections in this ego-network compared to the theoretical maximum. Summary statistics, i.e., minimum, mean and maximum values, of the density of the node’s neighbours are also included.

A second type consists of centrality metrics, quantifying the global position of the node in the network [98]. The most popular centrality metrics are the betweenness, closeness and eigenvector centrality. The betweenness quantifies the number of shortest paths between any two nodes in the network passing through that node. The closeness, being the inverse of the average distance, measures how close a node is to all other nodes. The eigenvector centrality is high for nodes that are connected to important nodes in the network. The importance of the node itself is quantified using the PageRank [103].

Table 11: The methods used to generate network features for the experimental evaluation. Category Features Definition

Manual feature engineering

Density Baesens et al. [10]: Number of edges in the egonet relative to the maximal number possible. Centrality measures Closeness, betweenness and eigenvector centrality. PageRank Page et al. [103]: Score indicating the importance of a node.

Shallow representation learning DeepWalk Perozzi et al. [104]: Random walk through the network. Embedding via word2vec. Node2vec Grover and Leskovec [52]: Truncated random walks (breadth-first vs. depth-first). Embedding via word2vec.

Deep representation learning

GCN Kipf and Welling [70]: Graph convolutional network GraphSAGE Hamilton et al. [56]: Aggregation based on fixed-size sample of neighbours GAT Veliˇckovi´c et al. [132]: Graph attention network GIN Xu et al. [144]: Graph isomorphism network

Next to the manual feature engineering, automatic network features are constructed using network embedding meth- ods [56, 50, 18]. Although there are many different methods to construct a network embedding [18], we use those based on deep learning, called network representation learning [127, 129].

[p. 18]

Shallow network representation learning can be viewed as an “embedding lookup” [56, 129]. We apply methods based on random walks. DeepWalk [104] was the first method to try to give nodes that are close in the network, i.e., that co-occur on short random walks, a similar embedding. Each random walk is seen as a sentence of words. The nodes are embedded into a Euclidean latent space using NLP methods, often skip-gram [94].

Node2vec [52] extends DeepWalk by introducing two hyperparameters, p and q. The method samples each node according to the following unnormalized transition probability, α, at node v, when coming from node t:

  

,

α(ci+1 = x | ci = v, ci−1 = t) =

 

1 p if dtx = 0 1 if dtx = 1 1 q if dtx = 2

where dtx denotes the distance between node t and x. These probabilities are defined a link exists between v and x. Otherwise, it is set to 0.

The main drawbacks of shallow representation learning methods are that (1) they are transductive, so need full retraining when a new node is added to the network, and (2) retraining on the same network results in a different embedding. This second point can be understood intuitively by viewing two embeddings of the same network, with one being a rotation of the other. Both are equally good, but a downstream classifier trained on one cannot be used to make predictions on the other, as the coordinates of the nodes are different.

In the experiments below, we construct the embedding on all nodes in the training and validation set, while only training on the labels from the training set. Afterwards, the embedding is constructed for the full network, and we train a new classifier using the labels of the train and validation set.

This mimics the applications of these methods in reality, since a bank will have the full transaction network up to the current time, with some historical labels. Based on this, they need to determine which accounts to investigate next for money laundering.

Deep network representation learning adapts deep learning methods to be directly applicable on networks. We apply different graph neural network (GNN) architectures.

The most popular methods for node embedding calculation are graph convolutional networks (GCNs), based on convolutional neural networks [70]. It relies on neighbourhood aggregation to update the embedding as follows:



H(l+1) = σ

˜D−1/2 ˜A ˜D−1/2H(l)W (l)

,

j ˜Aij, and W (l) the learnable weights in layer l. The node embedding for the

[pp. 18-19]

with H(l) the embedding at step l, σ a non-linear (activation) function, ˜A = A + I the adjacency matrix with self-loops added, the diagonal matrix ˜Dii = P

individual node is updated via





h(l+1)

W (l)h(l)

.

i = σ

j

1 p

deg(i)deg(j)

j∈˜ Ni

Neighbourhood aggregation has seen multiple extensions, two of which this paper will evaluate. The first is Graph- SAGE [56], which samples a fixed number of neighbours for each node, to make the calculations scalable to large graphs. The representations of the sampled neighbours are aggregated, with the authors proposing the mean, LSTM and pooling aggregators [56]. Then, the aggregated neighbourhood representation is concatenated with the node’s representation. Finally, the representation is updated using the weights and activation function. For a given node v, this is calculated as:


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
