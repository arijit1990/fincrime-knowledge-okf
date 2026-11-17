---
type: Source Text
title: 'The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset - part 1 of 2 (pp. 1-6)'
description: 'Verbatim extracted text, pp. 1-6: The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset; The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset > ABSTRACT; The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset > KEYWORDS; and 11 more sections'
resource: https://arxiv.org/abs/2404.19109
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-the-shape-of-money-laundering-subgraph-representation-learning-o
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-04-29'
legal_status: unknown
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2404.19109
  title: 'The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset'
  author: org:arxiv
  last_modified: '2024-04-29T00:00:00Z'
---

# The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2024-04-29), part 1 of 2, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset


[p. 1]

Claudio Bellei∗ Elliptic c.bellei@elliptic.co

Muhua Xu∗ MIT CSAIL MIT-IBM Watson AI Lab muhuaxu@mit.edu

Ross Phillips∗ Elliptic r.phillips@elliptic.co

Tom Robinson Elliptic tomrobinson@elliptic.co

Mark Weber MIT Media Lab mrweber@mit.edu

Tim Kaler MIT CSAIL MIT-IBM Watson AI Lab tfk@mit.edu

Charles E. Leiserson Arvind MIT CSAIL MIT CSAIL MIT-IBM Watson AI Lab MIT-IBM Watson AI Lab cel@mit.edu arvind@csail.mit.edu

Jie Chen IBM Research MIT-IBM Watson AI Lab chenjie@us.ibm.com

### ABSTRACT


Subgraph representation learning is a technique for analyzing local structures (or shapes) within complex networks. Enabled by recent developments in scalable Graph Neural Networks (GNNs), this approach encodes relational information at a subgroup level (multiple connected nodes) rather than at a node level of abstraction. We posit that certain domain applications, such as anti-money laundering (AML), are inherently subgraph problems and mainstream graph techniques have been operating at a suboptimal level of abstraction. This is due in part to the scarcity of annotated datasets of real-world size and complexity, as well as the lack of software tools for managing subgraph GNN workflows at scale. To enable work in fundamental algorithms as well as domain applications in AML and beyond, we introduce _Elliptic2_ , a large graph dataset containing 122K labeled subgraphs of Bitcoin clusters within a background graph consisting of 49M node clusters and 196M edge transactions. The dataset provides subgraphs known to be linked to illicit activity for learning the set of “shapes” that money laundering exhibits in cryptocurrency and accurately classifying new criminal activity. Along with the dataset we share our graph techniques, software tooling, promising early experimental results, and new domain insights already gleaned from this approach. Taken together, we find immediate practical value in this approach and the potential for a new standard in anti-money laundering and forensic analytics in cryptocurrencies and other financial networks.

- Security and privacy → Database activity monitoring ; •

- Computing methodologies → Machine learning ; • Applied computing → Network forensics .

### KEYWORDS


Artificial Intelligence, Machine Learning, Public Dataset, Graph Neural Networks, Subgraph Representation Learning, Financial Forensics, Cryptocurrency, Anti-Money Laundering

Claudio Bellei, Muhua Xu, Ross Phillips, Tom Robinson, Mark Weber, Tim Kaler, Charles E. Leiserson, Arvind, and Jie Chen. 2024. The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset. In _KDD MLF ’24: KDD Workshop on Machine Learning in Finance, August 26, 2024, Barcelona, Spain._ ACM, New York, NY, USA, 7 pages.

### 1 INTRODUCTION


[pp. 1-2]

Over the last few years, the development of graph neural networks (GNNs) has allowed the extension of deep learning methods to data that have an underlying non-Euclidian structure. GNNs offer a rich variety of models and architectures that enable the learning of meaningful representations for nodes, edges, and the entire graphs. These variants have found applications in diverse fields such as recommender systems, chemistry, traffic control, physics, and more [24]. However, when dealing with complex graph structures, it is often possible to identify subgraphs of particular interest. The recent emergence of subgraph representation learning has allowed the prediction of subgraph properties within the larger graph structure [2, 22]. By leveraging this approach, it is possible to gain valuable insights into the characteristics and behavior of these subgraphs within the broader background graph.

∗These authors contributed equally to this research.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

Interesting subgraphs can be found in financial graphs such as blockchain-based cryptocurrencies. Since their inception with Bitcoin [16], one of the primary features of cryptocurrency is the immutable and transparent record of all transactions ever logged

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.

on the network, while maintaining pseudonymity for users. Combining this public information with knowledge about the presence of licit and illicit services on the network, cryptocurrency intelligence companies have emerged to provide Anti-Money-Laundering (AML) solutions tailored to the cryptocurrency domain. Whereas the pseudonymity of Bitcoin is an advantage for criminals, the public availability of data is a key advantage for those within law enforcement agencies and financial institutions looking to identify and investigate financial crime.

The dataset here presented identifies subgraphs of interest within the AML lens of a cryptocurrency intelligence company: some subgraphs carry anomalous signatures of money laundering activity, while others (the vast majority) appear to be transferring flows of bitcoins among licit services. The challenge is being able to make predictions on subgraphs that have not yet been labeled, and potentially will never be labeled using standard methodologies, to allow AML solutions to make predictions even in the presence of unknowns by making exclusive use of public blockchain data.

### 2 A MASSIVE DATASET FOR SUBGRAPHS


[p. 2]

Available real-world datasets for subgraph representation learning include _PPI-BP_ , _HPO-METAB_ , _HPO-NEURO_ , and _EM-USER_ . Detailed properties for each can be found in [2, Appendix B]. The largest background graphs among these datasets constitute 100K nodes and 5M edges, with the number of subgraphs varying between 324 and 4,000 and with nodes per subgraph ranging between 10 and 155. To our knowledge, these are the largest subgraph datasets available, but they are not so large indeed. This limits scientific advancement in this field because resolving scalability constraints and other challenges common to massive network structures are indeed central to the promise of GNNs in many practical settings.

To enable research on subgraph learning on a much larger scale, we present _Elliptic2_ , a fully connected network of Bitcoin addresses and transactions between them comprising a background graph almost three orders of magnitude larger than any available real-world dataset that we know of . Within this background graph are many small subgraphs labeled as suspicious or licit, the task at hand being the binary classification of suspicious subgraphs. The release of this dataset follows our publication of a standard graph dataset in 2019, which contained Bitcoin transactions and focused on node classification. Both datasets enable the advancement of research in scalable Graph Neural Networks and their applications for anti-money laundering in cryptocurrency.

### 2.1 Retrospect on _Elliptic1_


In 2019, we published a labeled graph dataset of Bitcoin transactions named _The Elliptic Data Set_ (hereafter referred to as _Elliptic1_ ) on Kaggle [21] with an accompanying paper [23] demonstrating through experimental results on how GNNs can be used to extract hidden relational information that can be fed to classification models for significant performance boosts. The dataset comprised 204K node transactions with 166 features and 234K directed edge payment flows. Approximately 2% of the node transactions were labeled as illicit and 21% labeled as licit. The task presented was a binary node classification task, predicting whether a node transaction was broadcasted to the Bitcoin network by a licit or illicit

entity. As of this publication, the dataset has been viewed more than 100K times and downloaded almost 10K times, with the paper receiving approximately 400 citations. Traction in both the machine learning and AML communities motivated us to publish an even larger dataset we call _Elliptic2_ with a modified structure and the addition of subgraph labels to enable subgraph classification as a potentially powerful new tool for AML professionals. While our own novel methods on this new dataset are forthcoming, we offer this dataset to the community now in the interest of scientific advancement and the public good.

### 2.2 Introducing _Elliptic2_


[pp. 2-3]

Our task with _Elliptic2_ is to combat financial crime by identifying whether a specific flow of bitcoins may be linked to money laundering activity, specifically the attempt to convert the profits gained from illegal actions into fiat currency or other cryptocurrencies through a legitimate service. For the discussion that follows, some useful definitions are needed.

_Definition 2.1._ A _cluster_ is a set of Bitcoin addresses thought to be controlled by a single person or organization.

A _licit_ cluster is owned by a “licit” entity (exchange, wallet provider, miner, licit service, etc.). An _illicit_ cluster is owned by an “illicit” entity (dark market, scam, hack, etc.). Clusters that are neither licit nor illicit are deemed _unknown_ (e.g., unlabeled clusters).

A _suspicious_ path is a path that connects an illicit cluster to a licit cluster. An _illicit_ path is a path that connects an illicit cluster to an illicit cluster. A path that is neither licit nor suspicious nor illicit is considered _neutral_ .

_2.2.1 Assumptions._ The definitions above rest on the following assumption: a path on the blockchain connecting an illicit cluster to a licit cluster without a change of ownership of the funds likely represents the activity of money laundering by a criminal person or organization. The idea is that criminals who intend to deposit their funds at a legitimate service will try to evade detection on the blockchain, creating a distinct subgraph with associated “shape” and features that a machine learning model should be able to identify.

Figure 1: Illustrative example of the dataset, with its background graph and annotated subgraphs. Each node represents a Bitcoin cluster, a collection of Bitcoin addresses controlled by the same entity, and each edge representing a transaction between them.

_2.2.2 Graph construction._ Figure 1 shows the components of the dataset, with each node in the graph representing a Bitcoin cluster, and edges representing transactions between them. Clustering

|# Nodes|# Edges|# Subgraphs|# Node features|# Edge features|# Classes|
|---|---|---|---|---|---|
|49,299,864|196,215,60|6121,810|43|95|2|
|Class|# Subgraphs|Average # Nodes|Median # Nodes|Min # Nodes|Max # Nodes|
|Licit|119,047|3.65|3|2|296|
|Suspicious|2,763|3.79|3|2|30|

Table 1: Dataset properties for the background graph (top) and for the licit and suspicious subgraphs (bottom).

[p. 3]

addresses is done applying well known [3, 9, 14, 15, 18, 20] as well as proprietary heuristics, human analysis and domain expertise. While annotating the subgraphs, for intellectual property reasons only a subset of Elliptic’s cluster labels were used.

The dataset is built following the steps provided below.

- (1) Define the time window, the maximum number of hops to be traversed, and an early stopping condition when a change of ownership is likely to happen (e.g., when an unknown cluster with high activity is found during traversal).

- (2) Within the time window, determine the largest connected component (background graph).

- (3) For each labeled node in the background graph, obtain its outgoing transactions, providing a starting point for graph traversal.

- (4) Traverse the graph until one of the following conditions is true: I. a labeled node found; II. the length traversed is larger than the maximum number of hops allowed; III. the early stopping condition is satisfied.

- (5) For each path found at the previous step, define it as “suspicious” if illicit → licit, “licit” if licit → licit, “illicit” if illicit → illicit, or “neutral” if illicit/licit → unknown.

- (6) Using the above paths, run connected components to keep only subgraphs that can be labeled, i.e., those that only have logically consistent paths (licit + neutral or suspicious + illicit + neutral).

- (7) Annotate subgraphs for the final output, keeping only _unknown_ nodes that are part of either licit (licit subgraphs) or suspicious (suspicious subgraphs) paths.

The time window was chosen to be 1 year of blockchain data, and the maximum number of hops was 6 for computational reasons. The transactions at step (3) were capped to a maximum for each cluster, to help balance the dataset for different actors with varying blockchain activity.

_2.2.3 Overview of Elliptic2._ An overview of some of the properties of the dataset can be found in Table 1. The dataset is made of a background graph of 49M clusters and 196M edges. A subset of the background graph consists of labeled (licit/suspicious) subgraphs, as shown in Figure 1. Note that the only labels present in the dataset are those associated with these subgraphs, and that the vast majority of the nodes in the graph do not belong to labeled subgraphs. Only about 2% of the subgraphs are labeled “suspicious” with the remainder being labeled “licit”, thus introducing the challenge of a significant class imbalance. On average, the size of the subgraphs

Figure 2: Construction of the dataset requires labeling paths first and then labeling subgraphs. In the example above, there are 3 licit paths (I. 13 → 14 → 15 → 19; II. 16 → 17 → 15 → 19; III. 23 → 22 → 24), 1 illicit path (1 → 7 → 4 → 5 → 6), 3 suspicious paths (I. 1 → 7 → 8 → 9 → 12; II. 1 → 7 → 8 → 10 → 11 → 12; III. 20 → 21 → 22 → 24), and 1 neutral path (1 → 2 → 3). The result is one licit subgraph and one suspicious subgraph (note that the subgraph 21,22 is unlabeled as it is made of both a suspicious and a licit path).

Figure 3: Example of a size-3 suspicious subgraph, connecting the profits of a scam to two exchanges (Note: the label categories are not available in the dataset).

is small but the tail of the distribution is significant. An example of a size-3 suspicious subgraph is presented in Figure 3.

Each node in the background graph has 43 features, and each edge 95 features. The node features include, among others, the node size (number of addresses) and number of transactions. Both are examples of features that can vary by several orders of magnitude (from 1 to millions). The edge features include the transaction volume, fee, timestamp. To protect the intellectual property of Elliptic, most features were categorized into bins. The number of bins used varied between features. This process converted continuous numerical features into ordinal ones.

### 3.1 The anti-money laundering perspective


[p. 4]

The setup of _Elliptic2_ is tailored to the regulatory compliance constraints that companies interacting with cryptocurrency must adhere to. As in the traditional AML setting, companies receiving funds are usually required to make a determination regarding the legitimacy of said funds with regard to potential connections to suspicious activities or organizations. For this purpose, the task proposed with _Elliptic2_ is a binary classification with the objective of determining whether a subgraph is suspicious or not. The transparency of Bitcoin is helpful in that it allows for open, privacypreserving forensic analysis of observable patterns (such as subgraph shapes) on the public blockchain. Utilizing advanced machine learning techniques to reduce label dependence, the promise of accurate anti-money laundering in cryptocurrency at scale seems directionally attainable. Although some “typologies” of money laundering in cryptocurrency have been identified that can help tackle this problem [19], a general solution to it is still difficult to achieve, for example in “low profile” cases where timeliness is important (such as when scammers try to quickly cash out the proceeds of their crime).

### 3.2 The AI perspective


The _Elliptic2_ dataset is a timely contribution to the AI community, as graph representation learning research gained explosive traction over the years and demands real-life, large-scale, and challenging datasets to benchmark methods and models, typically GNNs and emergingly graph transformers [4]. Example benchmark contributions include Benchmarking GNNs [5], which offers an extensible framework for reproducible benchmarking; and the Long Range Graph Benchmark [6], which designs graph datasets that can test a model’s capability in reasoning over long-range interactions of nodes. These contributions generally do not involve massive graphs, for which the Open Graph Benchmark [11] is an alternative example, composed of several largest graphs widely used today. These graphs include ogbn-papers100M and MAG240M [10], which support not only the development of machine learning models but also the research on system design.

_Elliptic2_ is a similarly large-scale dataset that can be used to benchmark the scalability of graph models and the efficiency of training systems. It represents a real-life use case in the financial domain—cryptocurrency—for which there are rarely public datasets available for benchmarking.

Besides the large scale and the unique domain, more importantly, _Elliptic2_ supports the research of an emerging topic: subgraph representation learning. Traditionally, graph benchmark datasets are used to perform node-level tasks (classification and regression), graph-level tasks (similar), and edge-level tasks (link prediction). Instead, _Elliptic2_ can be used to perform subgraph-level tasks. Subgraph classification is mathematically defined in the following.

_Definition 3.1._ Given a graph _𝐺_ , let _𝑆__𝐺_ denote a subgraph of it and use ⊂ to denote the subgraph relation; i.e., _𝑆__𝐺_ ⊂ _𝐺_ . Let Label be the label space, Train be the set of training indices, and Test be the set of test indices. Then, the problem of _subgraph classification_ is that given a collection of labeled training subgraphs {( _𝑆𝑖__𝐺,𝑦𝑖_)|

_𝑆𝑖__𝐺_ ⊂ _𝐺, 𝑦𝑖_ ∈ Label _, 𝑖_ ∈ Train}, predict the labels of the subgraphs from the test set { _𝑆__𝐺_ _𝑗_|_𝑆𝐺_ _𝑗_⊂_𝐺,𝑗_∈Test}. Note that each subgraph may be disconnected and different subgraphs may overlap.

Subgraph classification is relatively less studied, compared with node/graph classification. A straightforward approach is to apply a graph model (e.g., GNN), obtain node representations, perform pooling (e.g., averaging) over the subgraph nodes, and apply a prediction head to predict the subgraph label. While being a common baseline, this approach is outperformed by several recently proposed methods [1, 2, 22]. _Elliptic2_ is a useful testbed for new methods regarding performance and scalability benchmarking.

### 4 RESULTS


We experimented with three subgraph classification methods on _Elliptic2_ : a conventional GNN trained with the subgraphs as independent graphs (named GNN-Seg), Sub2Vec [1], and GLASS [22]. Sub2Vec uses random walk samples within the subgraphs to build subgraph embeddings. Both GNN-Seg and Sub2Vec neglect the background graph, which may provide important information complementing the subgraphs themselves (e.g., the edges crossing a subgraph and the background graph), while GLASS makes use of it.

The GNN architecture of GLASS employs basic message-passing layers, supplemented with additional linear layers for node labeling, and is configured to have two layers. Hyperparameters mostly follow the default configuration provided by the authors of GLASS, with a slight tuning of the batch size (4000) and the learning rate (0.001) to improve training speed and quality.

We performed a random 80:10:10 split for training, validation, and testing, respectively. The experiments were conducted on a Linux server with 160 CPU cores and 1.2TB of RAM. We did not use GPUs, because the dataset was too large for the GPU memory to host all graph and intermediate data. For the same reason, we did not use the node/edge features. See Section 6 for a discussion on how one can perform training and inference for datasets of such a large size, by incorporating neighborhood sampling and using a scalable training sytem.

|||Train|||Test||
|---|---|---|---|---|---|---|
|Method|f1|pr_auc|roc_auc|f1|pr_auc|roc_auc|
|GNN-Seg|0.397|0.024|0.538|0.398|0.026|0.537|
|Sub2Vec|0.964|0.145|0.706|0.944|0.022|0.496|
|GLASS|0.937|0.224|0.915|0.933|0.208|0.889|

Table 2: Performance of different subgraph classification methods on _Elliptic2_ .

Table 2 compares the performance of the three methods under three evaluation metrics: micro-averaged F1, PR-AUC, and ROCAUC. We see that GLASS significantly outperforms the other two approaches under the PR-AUC and ROC-AUC metrics, while being competitive on F1. Because of the high imbalance of the labels, the AUC metrics reflect a more fluid choice of the labeling threshold; thus, a higher performance on these metrics translates to a stronger

[p. 5]

benefit when coroborating the ranked predictions by hand. We see that GLASS is able to reliably predict suspicious subgraphs, yielding consistent performance on both training and test sets. This notable gain demonstrates not only the feasibility of obtaining insights from the dataset but also the importance of using the background graph for model training.

||PP|PN|
|---|---|---|
|AP|245|46|
|AN|765|11125|

Table 3: Confusion matrix obtained by the GLASS method. Positive is the suspicious class.

To provide a more comprehensive picture of the predictability of GLASS in the context of class imbalance, we show the confusion matrix in Table 3. At least one in four predicted suspicious subgraphs is truly suspicious, and 85% of the suspicious subgraphs are correctly detected, indicating that GLASS maintains reasonable false positive and false negative rates.

In terms of computation, Sub2Vec has a lengthy pre-processing stage that takes around seven hours to finish but requires very little time for model training, whereas GNN-Seg and GLASS require heavy computation in the training of the GNN model. Overall, all methods were able to converge in several days of training with an inference time that was less than 8 hours.

### 5 CORROBORATING THE TRAINED MODEL


Based on the results in the preceding section, we predicted suspiciousness of additional, unlabeled subgraphs by using the trained GLASS model.

A cryptocurrency exchange was asked to validate the model predictions using their own off-chain insights. Specifically, 52 subgraphs deemed suspicious and which ended with deposit transactions to the exchange were chosen, since the exchange would hold information on the account holders that received these deposits. These deposit transactions were shared with the exchange. On review, the exchange found that 14 of the 52 accounts receiving these deposits were potentially involved in illicit activity, based on their own offchain insights, obtained through customer due diligence and other off-chain information. Notably, of these 14 accounts, 8 had been definitively associated with ‘money laundering’ or ‘fraud’. Despite the exchange having no positive indications that the remaining 38 accounts were involved in illicit activity, this does not exclude the possibility that they were.

### 5.1 Insights from a cryptocurrency exchange service


According to the exchange, less than 0.1% of customer accounts have been associated with money laundering or fraud, whereas at least 26.9% of the accounts highlighted by the model predictions were found to have such an association. This suggests that the empirical precision of our model significantly surpasses that of a naïve random model.

Another approach to verifying the model predictions is to prove that the unlabeled nodes that fund subgraphs predicted as suspicious are in fact illicit entities. To that end, investigations were undertaken to identify the origin of funds flowing into subgraphs deemed suspicious, i.e. to identify the entity controlling the node preceding the subgraph. These investigations utilised open source research and other standard identification techniques and resulted in the identification of a number of nodes. For example:

### 5.2 Identifying the source of funds in suspicious subgraphs


- (1) At least sixty subgraphs deemed suspicious received their funds from a node identified to be a cryptocurrency mixer. Mixers provide obfuscation services and are heavily-used by those laundering proceeds of illicit activity.

- (2) Two suspicious subgraphs received their funds from a Panamabased ponzi scheme.

- (3) At least one hundred suspicious subgraphs received their funds from a node identified to be a bot that enables anonymous cryptocurrency trading on a messaging platform. It is functionally similar to a service offered by the cryptocurrency exchange Bitzlato, which was shut down after almost half of its transactions were linked to criminal activities [8].

- (4) At least twenty suspicious subgraphs received funds from a node believed to be an invite-only Russian darknet market.

These results suggest an application of the model output beyond identification of suspicious transactions, i.e. the identification of suspicious nodes. The model has been shown here to be beneficial in directing manual investigations towards nodes most likely to be illicit, based on the subgraphs originating from them.

### 5.3 Identification of known cryptocurrency laundering patterns


[pp. 5-6]

Further validation of the model results can be obtained by examining the suspicious subgraphs for known cryptocurrency laundering transaction patterns.

Many of the suspicious subgraphs were found to contain what are known as “peeling chains”. This refers to a transaction pattern created when a cryptocurrency user sends or “peels” cryptocurrency to a destination address, while the remainder is sent to another address under the user’s control. This happens repeatedly to form a peeling chain. The pattern can have legitimate financial privacy purposes, for example to avoid address reuse, which can enable a user’s transactions to be easily linked together. However the pattern can also be indicative of money laundering, as described in various criminal cases [17], especially where the “peeled” cryptocurrency is repeatedly sent to an exchange service. In traditional finance this is known as “smurfing”, where large amounts of cash are structured into multiple small transactions, to keep them under regulatory reporting limits and avoid detection. Given the model was using node degree, it is understandable that peeling chains are a pattern visible to it, as a peeling chain is likely to result in a chain of nodes all with matching node degree.

Aside from peeling chains, many of the suspicious subgraphs contain apparent “nested services” in the vicinity of the final deposits into cryptocurrency exchanges. Nested services are businesses that

move funds through accounts at larger cryptocurrency exchanges, sometimes without the awareness or approval of the exchange. A nested service might receive a deposit from one of their customers into a cryptocurrency address, and then forward the funds to their deposit address at an exchange. Nested services are known to frequently have less stringent customer due diligence checks than the cryptocurrency exchanges they utilise, or sometimes have no such anti-money laundering checks at all, resulting in their misuse for cryptocurrency laundering [7] - potentially causing them to feature in subgraphs deemed by the model as suspicious.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset" (2024-04-29). https://arxiv.org/abs/2404.19109
