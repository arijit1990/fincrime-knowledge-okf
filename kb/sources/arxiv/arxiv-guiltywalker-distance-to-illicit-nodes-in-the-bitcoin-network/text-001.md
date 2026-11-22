---
type: Source Text
title: 'GuiltyWalker: Distance to illicit nodes in the Bitcoin network - part 1 of 2 (pp. 1-3)'
description: 'Verbatim extracted text, pp. 1-3: ABSTRACT; CCS CONCEPTS; 1 INTRODUCTION; and 5 more sections'
resource: https://arxiv.org/abs/2102.05373
tags:
- academic_finding
- data_features
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-guiltywalker-distance-to-illicit-nodes-in-the-bitcoin-network
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-10-02'
legal_status: unknown
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2102.05373
  title: 'GuiltyWalker: Distance to illicit nodes in the Bitcoin network'
  author: org:arxiv
  last_modified: '2021-10-02T00:00:00Z'
---

# GuiltyWalker: Distance to illicit nodes in the Bitcoin network

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2021-10-02), part 1 of 2, pp. 1-3. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Catarina Oliveira João Torres Maria Inês Silva catarina.a.oliveira@tecnico.ulisboa.pt joao.m.f.torres@tecnico.ulisboa.pt maria.silva@feedzai.com Instituto Superior Técnico Instituto Superior Técnico Feedzai Portugal Portugal Portugal David Aparício João Tiago Ascensão Pedro Bizarro david.aparicio@feedzai.com joao.ascensao@feedzai.com pedro.bizarro@feedzai.com Feedzai Feedzai Feedzai Portugal Portugal Portugal

## ABSTRACT


Money laundering is a global phenomenon with wide-reaching social and economic consequences. Cryptocurrencies are particularly susceptible due to the lack of control by authorities and their anonymity. Thus, it is important to develop new techniques to detect and prevent illicit cryptocurrency transactions. In our work, we propose new features based on the structure of the graph and past labels to boost the performance of machine learning methods to detect money laundering. Our method, GuiltyWalker, performs random walks on the bitcoin transaction graph and computes features based on the distance to illicit transactions. We combine these new features with features proposed by Weber et al. [16] and observe an improvement of about 5pp regarding illicit classification. Namely, we observe that our proposed features are particularly helpful during a black market shutdown, where the algorithm by Weber et al. [16] was low performing.

## CCS CONCEPTS


• Computing methodologies → Supervised learning by classification .

cryptocurrency, anti-money laundering, supervised learning, transaction graph, random walker

Catarina Oliveira, João Torres, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro Bizarro. 2021. GuiltyWalker: Distance to illicit nodes in the Bitcoin network. In _Workshop on Machine Learning in Finance (KDD ’21), August, 2021, Singapore._ ACM, New York, NY, USA, 5 pages.

Money laundering is a serious financial crime that consists of the illegal process of obtaining money from criminal activities, such as drug or human trafficking, and making it appear legitimate. Cryptocurrencies, such as Bitcoin [7], are particularly susceptible to

## 1 INTRODUCTION


Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _KDD ’21, August 14–18, 2021, Singapore_

© 2021 Association for Computing Machinery.

money laundering schemes due to their pseudo-anonymity and the relative lack of control by authorities. Preventing money laundering is an international effort and Anti-Money Laundering (AML) laws have been trying to cope with the new threats posed by criminals using cryptocurrencies [8, 15].

In 2019, Weber et al. [16] released the Elliptic data set. It contains anonymized labeled Bitcoin transactions and enables researchers to study illicit behaviour in cryptocurrencies. The data set consists of a time-series graph with 200K labeled bitcoin transaction nodes and tabular data with 166 anonymized features describing each transaction. Weber et al. [16] assesses the performance of several supervised learning algorithms on the task of detecting nodes associated with illicit activities.

To improve existing supervised learning results found in the literature, we propose a new set of features that leverage the structure of the network and the existence of hubs or pockets of illicit transactions. We extract these new features with _GuiltyWalker_ . This random walker traverses a given network starting from a seed node and computes features related to the distance of the seed node to other nodes known to be illicit.

GuiltyWalker consists of two main components:

- Random walker : Given a transaction graph, a set of seed nodes, and the number of desired random walks for each of the seeds, GuiltyWalker samples random walks for each seed node. Due to the temporal nature of the graph, the walker only travels to past nodes (i.e., transactions) and stops at the first illicit node found or when there are no more valid nodes to visit.

- Feature extractor : Given a set of random walks for each of the seeds, GuiltyWalker computes aggregated features that summarize these walks, e.g., the average number of steps needed to reach one illicit node or the total number of different illicit nodes found.

[pp. 1-2]

In our experiments on the Elliptic data set, we observe that adding the features computed by GuiltyWalker improves the performance of machine learning methods; namely, we achieve a 5pp increased performance in F1-score, when compared against machine learning methods that use only the original anonymized features from Weber et al. [16]. Furthermore, the gains in performance are more pronounced during a black market shutdown, where the original performance by Weber et al. [16] dropped significantly.

This paper is organized as follows. Section 2 details the implementation of GuiltyWalker and how we generate new features from

Catarina Oliveira, João Torres, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro Bizarro

its output to enrich the data and convey additional information to supervised learning methods. Section 3 describes the experimental setup, and Section 4 the results consequently obtained. Section 5 presents the related work. Finally, we set out the main conclusions in Section 6.

## 2 GUILTYWALKER


[p. 2]

GuiltyWalker consists of a random walker that traverses a given transaction network from a seed node and extracts features based on the distance of that node to known illicit nodes. It includes two main components – a random walker and a feature extractor, explained in the following subsections.

The random walker receives as input the original transaction graph _𝐺_ , a list of seed nodes, _𝑆_ ⊂ _𝑉_ ( _𝐺_ ), and the number of _successful_ random walks desired, _𝑘_ . Successful random walks are explained later in this section. GuiltyWalker’s output for each seed node _𝑠_ ∈ _𝑆_ is the list of sampled random walks X_𝑠_ = { _𝑋_ 1_𝑠,𝑋_ 2_𝑠, ...,𝑋_ _𝑘__𝑠_}. A random walk _𝑋𝑖__𝑠_consists of a sequence of nodes

## 2.1 Random Walker


number of unsuccessful walks made from each node, which may be informative.

It is important to note that some nodes in a transaction graph might have no paths to any illicit node. Thus, it is impossible to obtain successful random walks (as per our definition) for those nodes. To avoid this problem, GuiltyWalker first determines which nodes actually can reach an illicit node. To do that, we first invert the direction of the graph. Then, we use the descendants algorithm for directed acyclic graphs from NetworkX [4] [9]. It returns all nodes reachable from a source node _𝑠_ in the graph _𝐺_ . Afterwards, we inspect if at least one of them is illicit. This procedure is made for all nodes in the transaction graph, and only those that can reach an illicit node are given as input for the random walker.

## 2.2 Features Computation


The second component of GuiltyWalker receives the list of random walks from each seed node and returns a data frame of features corresponding to each transaction, summarizing the random walks. In particular, GuiltyWalker obtains the following features:

- Minimum size of the random walks (min);

- Maximum size of the random walks (max);

- Mean size of the random walks (mean);

- Standard deviation of the random walks sizes (std);

such that _𝑥_ 1 = _𝑠_ . Due to the temporal nature of the transaction graph, the random walker can only walk backward in time. That is, it is only valid to go from node _𝑥𝑛_ to node _𝑥𝑚_ if _𝑥𝑚_ represents a transaction older than _𝑥𝑛_ . This transaction network is represented as a directed graph connecting older nodes to newer nodes by an outgoing edge. Then, to address the former condition, during the random walk process, GuiltyWalker chooses a node uniformly at random from the incoming neighbors of the current node. When GuiltyWalker is in a given state of a random walk _𝑋𝑖__𝑠_=(_𝑠,𝑥_2_, ...,𝑥𝑛_), the process stops and returns _𝑋𝑖__𝑠_as the final random walk if at least one of the following criteria is met:

- _𝑥𝑛_ is a known illicit node/transaction.

- The set of eligible nodes to pick from is empty. This scenario happens when a given node has no incoming neighbors and, consequently, the random walker has no possible moves.

Otherwise, GuiltyWalker randomly picks the next node to add to _𝑋𝑖__𝑠_, and the process continues.

Note that since the edges only connect older transactions to newer transactions, there is always an end node in any random walk. In other words, the properties of our transaction graph guarantee that GuiltyWalker will not be stuck in an endless loop.

The number of _successful_ random walks, given by the user as input, intends to set the desired number of random walks ending in an illicit node from each seed node _𝑠_ ∈ _𝑆_ . However, as discussed before, the random walker may find a node with no incoming neighbors. In this case, a random walker finishes traversing the graph without reaching an illicit node. To ensure the number of desired successful random walks, GuiltyWalker performs as many random walks as needed, and only those are used for feature extraction. As we mention in Section 2.2, one of the features extracted from GuiltyWalker is the fraction of _successful_ random walks from the total number of random walks needed to perform to ensure the number of successful ones. This is a way of also considering the

- Median size of the random walks (median);

- First quartile of the random walks sizes (q25);

- Third quartile of the random walks sizes (q75);

- Fraction of _successful_ random walks from all the random walks performed by Random Walker (hit rate);

- Number of distinct illicit nodes in the random walks (illicit).

We also add information about the transaction nodes with no possible paths to fraudulent nodes to the data frame of features, with all features set accordingly (see Section 3.2), due to the lack of information regarding the distance to an illicit node.

## 3.1 Elliptic Data Set


[pp. 2-3]

In this work, we use the Elliptic Data Set, a graph network of Bitcoin transactions2 . Elliptic, a company focused on combating financial crime in cryptocurrencies, released this data set.

The data set includes 203,769 node transactions and 234,355 directed edges, representing the flow of Bitcoin currency (BTC) going from one transaction to the next. Each transaction can be categorized into three classes: "licit", "illicit" or "unknown", based on the category of the entity that created it. Licit categories include exchanges, wallet providers, miners, and financial service providers. Illicit categories include scams, malware, terrorist organizations, and Ponzi schemes. From the total number of transactions, 21% (42,019) are labeled as licit, 2% (4,545) as illicit, and the remaining 77% (157,205) are unknown.

Besides the graph structure, the data set has 166 anonymized features associated with each transaction. The first 94 relate to information about the transaction itself, such as the time step, number of inputs/outputs, and transaction fee. The remaining features relate to aggregated information about the direct neighbors of the

> 2Available at https://www.kaggle.com/ellipticco/elliptic-data-set

transaction, giving the maximum, minimum, standard deviation, and correlation coefficients of each transaction.

Besides, a time step from 1 to 49 is associated with each node. It represents an estimate of when the Bitcoin network confirmed the transaction. The time steps are evenly spaced with an interval of about two weeks and each one contains a single connected component of transactions that appeared on the blockchain within less than three hours between each other. Therefore, it can be considered that this data set includes 49 directed acyclic graphs associated with different sequential moments in time. Figure 1 provides an idea of the structure of this data set.

## 3.2 Methodology


[p. 3]

This section gives an overview of the models used in our experiments and discusses our experimental setup. Following Weber et al. [16], we perform a 70/30 temporal split of training and test data, respectively, for all experiments. Therefore, the train set includes all labeled samples up to the 34th time step, and the test set includes all labeled samples from the last 15 time steps, up to the 49th .

We use random forest for licit versus illicit prediction. First, we train the model on the train set using all 166 features and evaluate it on the entire test set. We use the scikit-learn [10] implementation of random forest, with 50 estimators, corresponding to the number of trees in the forest, and 50 max features, defined as the maximum number of features each tree can have. By doing so, we mimic the method in Weber et al. [16] enabling a fair comparison of the results. We also set the random state to 0 for the purpose of results reproducibility.

Then, we train a random forest model (using the same parameters as before) using (i) only the new set of features obtained by GuiltyWalker and (ii) both the features obtained by GuiltyWalker and the original 166 features. We extract the GuiltyWalker features after performing 100 _successful_ random walks. Missing values for the transaction nodes that cannot reach an illicit node are filled with -1 values, except feature _hit_ , which is filled with 0 values, as it represents the fraction of random walks ending in a fraudulent node. We see that the utilization of some of these alternative sets of features improves performance in Section 4.

To further improve the results, we filter the set of features obtained by GuiltyWalker to keep just the most important ones. This method characterizes every single feature’s importance as the decrease in the performance score after randomly shuffling its position in the set, and is called Permutation feature importance [13]. After applying this method and assessing every feature’s importance, the new features kept for further classification purposes are _hit_ , _std_ , _illicit_ , _max_ and _mean_ . We also analyse the model’s performance with these features together with the 166 original ones in Section 4.

Similarly to Weber et al. [16], we evaluate the random forest classifier’s performance with each set of features using the F1-score for the illicit class, hereafter referred to as illicit F1-score. This score is the weighted average of precision and recall. Moreover, it is suitable for imbalanced tasks, which is the case of our dataset (91% of licit nodes and 9% of illicit ones). We also use the ROC curve (and AUC value) and precision and recall measures to evaluate the models’ performance.

Figure 1: Structure of the data set (taken from [2])

In this section, we present the results obtained by using the standard model, random forest, with the 166 baseline features (referred to as AF), as well as only the new features extracted from GuiltyWalker (referred to as GWF) and the former ones together with the latter (referred to as AF+GWF). Furthermore, we show the results obtained using the 166 features in conjunction with the new ones obtained after performing feature reduction (referred to as AF+GWF*).

Table 1: Illicit classification results using random forest, for different features. _AF_ refers to the original all features, _GWF_ refers features extracted from the GuiltyWalker, and, _GWF*_ refers to GuiltyWalker features after feature selection.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "GuiltyWalker: Distance to illicit nodes in the Bitcoin network" (2021-10-02). https://arxiv.org/abs/2102.05373
