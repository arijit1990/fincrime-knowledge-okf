---
type: Source Digest
title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics - part 1 of 2 (pp. 1-6)'
description: 'Verified paraphrased digest, pp. 1-6: Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > ABSTRACT; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > CCS CONCEPTS; and 11 more sections'
resource: https://arxiv.org/pdf/1908.02591
tags:
- academic_finding
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-anti-money-laundering-in-bitcoin-experimenting-with-graph-convol
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2019-07-31'
legal_status: unknown
part: 1
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:48:11Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:48:11Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:48:11Z'
sources:
- id: original
  resource: https://arxiv.org/pdf/1908.02591
  title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics'
  author: org:arxiv
  last_modified: '2019-07-31T00:00:00Z'
digest_points: 61
---

# Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / data or feature**: The authors contribute the Elliptic Data Set, a time series graph of over 200K Bitcoin transactions, about 234K directed payment flows and 166 node features, described as the largest labelled transaction data set publicly available in any cryptocurrency. (p. 1)[^original]  
  <sub>anchor: "We contribute the Elliptic Data Set, a time series graph of over 200K Bitcoin transactions (nodes)"</sub>
- **descriptive / finding or result**: Results of a binary illicit-transaction classification task show Random Forest performing best, and the authors suggest algorithmic work to combine Random Forest with graph methods. (p. 1)[^original]  
  <sub>anchor: "The results show the superiority of Random Forest (RF), but also invite algorithmic work to combine the respective powers of RF and graph methods."</sub>

## 1 TOWARD FINANCIAL INCLUSION

- **descriptive / context**: Restricted access to the financial system is partly an unintended consequence of stringent AML regulations, which disproportionately affect low-income people, immigrants and refugees. (p. 1)[^original]  
  <sub>anchor: "have a disproportionately negative effect on low-income people, immigrants, and refugees [16]"</sub>

## ABSTRACT

- **descriptive / data or feature**: The paper offers a simple visualization prototype that can navigate the transaction graph and show model performance on illicit activity over time. (p. 1)[^original]  
  <sub>anchor: "we offer a simple prototype capable of navigating the graph and observing model performance"</sub>

## 1 TOWARD FINANCIAL INCLUSION

- **descriptive / context**: AML policy imposes high fixed compliance costs on money service businesses and fear of penalties for noncompliance, making low-value customers seem not worth the risk. (p. 2)[^original]  
  <sub>anchor: "which enforces high fixed costs of compliance on money service businesses (MSBs)"</sub>
- **descriptive / context**: The paper reports about 1.7 billion adults are unbanked, and remittances to low- and middle-income countries reached a record $529 billion in 2018 versus $153 billion in global aid. (p. 2)[^original]  
  <sub>anchor: "Approximately 1.7 billion adults are unbanked [7]."</sub>
- **descriptive / context**: The average cost of sending $200 in remittances is stated as 7 percent, with some countries above 10 percent; the UN Sustainable Development Goal 10.7 targets 3 percent by 2030. (p. 2)[^original]  
  <sub>anchor: "The current average cost of sending $200 is an expensive 7 percent, with some countries suffering rates of over 10 percent."</sub>
- **descriptive / context**: The paper argues AML regulations cannot be dismissed as overburdensome, citing illicit industries such as drug cartels, human trafficking and terrorist organizations. (p. 2)[^original]  
  <sub>anchor: "And yet AML regulations cannot be summarily dismissed as over burdensome."</sub>
- **descriptive / case example**: The 1MDB money laundering scandal is described as robbing the Malaysian people of over $11 billion in taxpayer funds, with fines and indictments implicating Goldman Sachs among others. (p. 2)[^original]  
  <sub>anchor: "robbed the Malaysian people of over $11 billion in taxpayer funds earmarked for the nation’s development [22]"</sub>
- **descriptive / case example**: The Danske Bank scandal in Estonia is described as a hub for an estimated $200 billion in illicit money flows from Russia and Azerbaijan, causing billions in losses for Danske Bank and Deutsche Bank. (p. 2)[^original]  
  <sub>anchor: "served as a hub for an estimated $200 billion in illicit money flows from Russia and Azerbaijan"</sub>
- **descriptive / context**: The authors pose the question whether the right tools and open data can reconcile the need for safety with financial inclusion. (p. 2)[^original]  
  <sub>anchor: "with the right tools and open data, can we help reconcile the need for safety with the cause of financial inclusion?"</sub>

## 1.1 AML in a cryptocurrency world

- **descriptive / context**: Cryptocurrency startups emerged to offer low-cost peer-to-peer transfers, many targeting remittances and financial inclusion, competing with legacy banks and MSBs. (p. 2)[^original]  
  <sub>anchor: "They focused on enabling low-cost, peer-to-peer transfers of cash within and across borders"</sub>
- **descriptive / context**: Bitcoin's pseudonymity was exploited by criminals for ransomware attacks and dark marketplaces trading illegal goods and services. (p. 2)[^original]  
  <sub>anchor: "conducting ransomware attacks and operating dark marketplaces for the exchange of illegal goods and services."</sub>
- **mandatory / requirement**: Under the FinCEN guidance, risk assessments based on customer composition, geographies served and products offered must inform customer relationship management and controls commensurate with risk; MSBs must not only report suspicious accounts but also act against them, e.g. freezing or closing them. (p. 2)[^original]  
  <sub>anchor: "The assessments must inform the management of customer relationships, including the implementation of controls commensurate with risk"</sub>
- **descriptive / definition**: The FinCEN guidance defines a well-developed risk assessment as one that provides a comprehensive analysis of an MSB's individual risk profile. (p. 2)[^original]  
  <sub>anchor: "The guidance defines a “well-developed risk assessment” as “assisting MSBs in identifying and providing a comprehensive analysis of their individual risk profile.”"</sub>
- **mandatory / requirement**: The FinCEN guidance requires MSBs to know enough about their customers to determine the risk level they represent, reinforcing the BSA Know Your Customer requirements. (p. 2)[^original]  
  <sub>anchor: "the guidance requires MSBs to “know enough about their customers to be able to determine the risk level they represent to the institution.”"</sub>
- **descriptive / context**: In practice an implicit but effectively enforced requirement extends know-your-customer to the customer's customer, usually handled by phone calls between MSBs in traditional finance. (p. 2)[^original]  
  <sub>anchor: "to not only know your customer, but to know your _customer’s_ customer."</sub>
- **descriptive / context**: Bitcoin's full transaction graph is publicly available, though pseudonymous and unlabelled, and cryptocurrency intelligence companies have emerged to offer AML solutions. (p. 2)[^original]  
  <sub>anchor: "the full graph transaction network data is publicly available, albeit in pseudonymous and unlabelled form."</sub>

## 2 THE ELLIPTIC DATA SET

- **descriptive / definition**: Transactions are labelled licit or illicit by the category of the entity initiating them; licit categories include exchanges, wallet providers, miners and licit services, while illicit ones include scams, malware, terrorist organizations, ransomware and Ponzi schemes. (p. 2)[^original]  
  <sub>anchor: "exchanges, wallet providers, miners, licit services, etc.) versus _illicit_ ones (scams, malware, terrorist organizations, ransomware, Ponzi schemes, etc.)"</sub>
- **descriptive / definition**: The graph has nodes as transactions and edges as flows of bitcoin from one transaction to the next; a transaction is licit or illicit according to the category of the entity controlling the input addresses' private keys. (p. 2)[^original]  
  <sub>anchor: "the entity controlling the private keys associated with the input addresses of a specific transaction"</sub>
- **descriptive / data or feature**: All Elliptic Data Set features are constructed using only publicly available information. (p. 2)[^original]  
  <sub>anchor: "Importantly, all features are constructed using only publicly available information."</sub>

## 2.1.1 Nodes and Edges

- **descriptive / data or feature**: The data set has 203,769 node transactions and 234,355 directed payment flow edges; the full Bitcoin network is approximately 438M nodes and 1.1B edges as of writing. (p. 2)[^original]  
  <sub>anchor: "There are 203,769 node transactions and 234,355 directed edge payments flows."</sub>

## 2.1.2 Features

- **descriptive / limitation**: Footnote 1 notes that, for simplicity, the labelling argument ignores mixer transactions whose inputs are controlled by multiple entities. (p. 2)[^original]  
  <sub>anchor: "this argument ignores mixer transactions where the inputs are controlled by multiple entities"</sub>

## 2.1.1 Nodes and Edges

- **descriptive / data or feature**: Of the nodes, two percent (4,545) are labelled class1 (illicit), twenty-one percent (42,019) are labelled class2 (licit), and the remainder are unlabelled for licit versus illicit. (p. 3)[^original]  
  <sub>anchor: "In the Elliptic Data Set, two percent (4,545) are labelled _class1 (illicit)_ ."</sub>

## 2.1.2 Features

- **descriptive / data or feature**: Each node has 166 features: the first 94 are local transaction information (time step, inputs/outputs, fee, volume and averages), and the remaining 72 are aggregated one-hop neighbour features (maximum, minimum, standard deviation and correlation coefficients). (p. 3)[^original]  
  <sub>anchor: "The first 94 features represent _local information_ about the transaction"</sub>

## 2.1.3 Temporal Information

- **descriptive / data or feature**: Nodes have timestamps estimating confirmation time; there are 49 distinct time steps spaced about two weeks apart, with no edges between time steps. (p. 3)[^original]  
  <sub>anchor: "There are 49 distinct time steps, evenly spaced with an interval of about two weeks."</sub>
- **descriptive / data or feature**: Each time step contains a single connected component of transactions confirmed within less than three hours of each other, and node counts per step range from 1,000 to 8,000. (p. 3)[^original]  
  <sub>anchor: "The number of nodes for each time step is reasonably uniform over time (ranging from 1,000 to 8,000 nodes)."</sub>

## 2.1.2 Features

- **descriptive / limitation**: Aggregating neighbour features with simple statistics is described as sub-optimal because it loses significant information about heterogeneous neighbourhoods. (p. 3)[^original]  
  <sub>anchor: "In general, this solution is sub-optimal because it carries a significant loss of information."</sub>

## 2.1.3 Temporal Information

- **descriptive / context**: Licit/illicit labelling is informed by heuristic reasoning; reuse of addresses and many inputs are associated with higher address clustering and reduced anonymity, so high-volume services like exchanges are likely licit, while illicit activity tends to use fewer inputs. (p. 3)[^original]  
  <sub>anchor: "In contrast, illicit activity may tend to favor transactions with a lower number of inputs"</sub>

## 2.2 Notes on Feature Construction

- **descriptive / context**: Building features is challenging because the Bitcoin blockchain is about 200GB compressed with about 400 million transactions, requiring access to the complete history; Elliptic uses an all-in-memory graph engine. (p. 3)[^original]  
  <sub>anchor: "Though not all transactions are included in the subset used in this study, it is still necessary to access the complete blockchain"</sub>
- **descriptive / context**: AML analytics is described as anomaly detection of a few illicit transactions in massive data sets, with industry standard false positive rates of upwards of 90%. (p. 3)[^original]  
  <sub>anchor: "Industry standard high false positive rates of upwards of 90% inhibit this effort."</sub>
- **descriptive / expectation**: The authors aim to reduce false positive rates without increasing false negative rates, including more innocent people without allowing more criminals. (p. 3)[^original]  
  <sub>anchor: "We want to reduce false positive rates without increasing false negative rates"</sub>

## 3 TASK AND METHODS

- **descriptive / definition**: The task is transaction screening: each unlabelled Bitcoin transaction is to be classified as illicit or licit to assess risk. (p. 3)[^original]  
  <sub>anchor: "each unlabelled Bitcoin transaction is to be classified illicit or licit."</sub>
- **descriptive / method**: Benchmark methods use the first 94 local features for supervised binary classification: Logistic Regression, Multilayer Perceptron and Random Forest; these methods do not use graph information. (p. 4)[^original]  
  <sub>anchor: "Such techniques include Logistic Regression [1], Multilayer Perceptron (MLP) (ibid), and Random Forest [2]."</sub>
- **descriptive / context**: Random Forest and Logistic Regression are popular for AML, used together with Random Forest for accuracy and Logistic Regression for explainability. (p. 4)[^original]  
  <sub>anchor: "Random Forest for accuracy and Logistic Regression for explainability."</sub>

## 3.1 Benchmark Methods

- **descriptive / finding or result**: Adding the 72 neighbourhood features improves performance, showing graph structure carries information for binary classification, but purely feature-based methods are difficult to extend beyond the immediate neighbourhood. (p. 4)[^original]  
  <sub>anchor: "it is challenging to extend the purely feature-based method beyond the immediate neighbourhood."</sub>
- **descriptive / method**: Graph Convolutional Networks consist of multiple graph convolution layers, similar to a perceptron with an added neighbourhood aggregation step motivated by spectral convolution. (p. 4)[^original]  
  <sub>anchor: "A GCN consists of multiple layers of graph convolution, which is similar to a perceptron"</sub>

## 3.2 Graph Convolutional Networks (GCN)

- **descriptive / method**: Each GCN layer takes the adjacency matrix and node embeddings, applies a weight matrix and an activation (typically ReLU except at the output layer), starting from the node features; the output layer is a softmax giving prediction probabilities. (p. 4)[^original]  
  <sub>anchor: "and _σ_ is the activation function (typically ReLU) for all but the output layer."</sub>
- **descriptive / method**: The Skip-GCN variant adds a skip connection from the input node features to an intermediate embedding; when its weights are zero it reduces to Logistic Regression, so it should be at least as powerful as Logistic Regression. (p. 4)[^original]  
  <sub>anchor: "When _W_(0) and _W_(1) are zero, Skip-GCN is equivalent to Logistic Regression."</sub>

## 3.3 Temporal Modeling

- **descriptive / method**: EvolveGCN computes a separate GCN for each time step, with the GCNs connected through a recurrent neural network to capture system dynamics so future models evolve from past ones. (p. 4)[^original]  
  <sub>anchor: "These GCNs are then connected through a recurrent neural network (RNN) to capture the system dynamics."</sub>
- **descriptive / method**: In EvolveGCN the GCN weights are the system state, updated by a GRU-type RNN using the current graph information, represented by embeddings of the top-k influential nodes. (p. 4)[^original]  
  <sub>anchor: "in EvolveGCN, it is represented by the embeddings of the top- _k_ influential nodes in the graph."</sub>

## 4 EXPERIMENTS

- **descriptive / method**: The data is split 70:30 temporally: the first 34 time steps are used for training and the last 15 for testing; GCN is trained in an inductive setting. (p. 4)[^original]  
  <sub>anchor: "That is, the first 34 time steps are used for training the model and the last 15 for test."</sub>
- **descriptive / method**: Baselines: Logistic Regression with scikit-learn defaults, Random Forest with 50 estimators and 50 max features, and an MLP with one hidden layer of 50 neurons trained 200 epochs with Adam at learning rate 0.001. (p. 4)[^original]  
  <sub>anchor: "Our MLP had one hidden layer of 50 neurons and was trained for 200 epochs by using the _Adam_ optimizer and a learning rate of 0.001."</sub>
- **descriptive / method**: Models were evaluated with all 166 features (AF) and with only the 94 local features (LF). (p. 4)[^original]  
  <sub>anchor: "We evaluated these models by using all the 166 features (referred to as _AF_ ), as well as only the local ones"</sub>
- **descriptive / method**: The GCN was a 2-layer model trained for 1000 epochs with Adam at learning rate 0.001, with node embedding size set to 100 after hyperparameter tuning. (p. 5)[^original]  
  <sub>anchor: "In our experiment we used a 2-layer GCN and, after hyper-parameter tuning, we set the size of the node embeddings to be 100."</sub>
- **descriptive / method**: Because classes are imbalanced, GCN was trained with a weighted cross entropy loss giving more importance to illicit samples, using a 0.3/0.7 licit/illicit ratio chosen after tuning. (p. 5)[^original]  
  <sub>anchor: "After hyperparameter tuning, we opted for a 0.3/0.7 ratio for the licit and illicit classes."</sub>
- **descriptive / finding or result**: Table 1 results for illicit class: Random Forest with all features reaches precision 0.956, recall 0.670, F1 0.788 and micro-averaged F1 0.977; Random Forest with all features plus node embeddings reaches F1 0.796, the best F1 in the table. (p. 5)[^original]  
  <sub>anchor: "RandomForest_AF_|0.956|0.670|0.788|0.977|"</sub>
- **descriptive / finding or result**: Table 1 Logistic Regression rows: with all features precision 0.404, recall 0.593, F1 0.481 (micro F1 0.931); with all features plus node embeddings F1 0.533; with local features F1 0.457; with local features plus node embeddings F1 0.543. (p. 5)[^original]  
  <sub>anchor: "Logistic Regr_AF_|0.404|0.593|0.481|0.931|"</sub>
- **descriptive / finding or result**: Table 1 Random Forest with local features reaches precision 0.803, recall 0.611, F1 0.694 (micro F1 0.966); with local features plus node embeddings F1 0.759. (p. 5)[^original]  
  <sub>anchor: "RandomForest_LF_|0.803|0.611|0.694|0.966|"</sub>
- **descriptive / finding or result**: Table 1 MLP rows: MLP with all features F1 0.653; with all features plus node embeddings F1 0.689; with local features F1 0.649; with local features plus node embeddings F1 0.6258 (micro F1 0.986, precision and recall as printed in the table). (p. 5)[^original]  
  <sub>anchor: "MLP_LF_+_N E_|0.6819|0.5782|0.6258|0.986|"</sub>
- **descriptive / finding or result**: Table 1 GCN reaches precision 0.812, recall 0.512 and F1 0.628 (micro F1 0.961); Skip-GCN reaches precision 0.812, recall 0.623 and F1 0.705 (micro F1 0.966). (p. 5)[^original]  
  <sub>anchor: "GCN|0.812|0.512|0.628|0.961|"</sub>
- **descriptive / finding or result**: GCN and Skip-GCN outperform Logistic Regression, indicating the usefulness of graph-based methods, but with these features Random Forest achieves the best F1 score. (p. 5)[^original]  
  <sub>anchor: "Note that GCN and the variant Skip-GCN outperform Logistic Regression"</sub>
- **descriptive / finding or result**: For all three models, using aggregated features (AF) rather than only local features (LF) led to higher accuracy, indicating the importance of graph structure. (p. 5)[^original]  
  <sub>anchor: "For all the three evaluated models, the aggregated information led to higher accuracy"</sub>
- **descriptive / finding or result**: Concatenating GCN node embeddings with original features improved model accuracy for both full and local feature sets. (p. 5)[^original]  
  <sub>anchor: "Results show that with the enhanced feature set the accuracy of the model improves"</sub>
- **descriptive / finding or result**: Table 2: EvolveGCN illicit precision 0.850, recall 0.624, F1 0.720 versus GCN 0.812, 0.623, 0.705; micro-averaged F1 0.968 versus 0.966. EvolveGCN consistently outperforms GCN, though the improvement is not substantial. (p. 5)[^original]  
  <sub>anchor: "EvolveGCN consistently outperforms GCN, although the improvement is not substantial for this data set."</sub>
- **descriptive / limitation**: Alternative forms of system input to drive the recurrent GRU update are suggested as a direction for further investigation. (p. 5)[^original]  
  <sub>anchor: "One avenue of further investigation is the use of alternative forms of system input to drive the recurrent update inside GRU."</sub>
- **descriptive / case example**: A dark market shutdown at time step 43 causes all methods to perform poorly after the shutdown, including a Random Forest retrained after every test time step. (p. 5)[^original]  
  <sub>anchor: "this event causes all methods to perform poorly after the shutdown."</sub>
- **descriptive / limitation**: Robustness to emerging events such as the dark market shutdown is identified as a major challenge; even retrained Random Forest cannot reliably capture new illicit transactions afterwards. (p. 5)[^original]  
  <sub>anchor: "The robustness of methods to such events emerges as a major challenge to address."</sub>

## 5 DISCUSSION

- **descriptive / finding or result**: Random Forest significantly outperforms Logistic Regression and also outperforms GCN, even though GCN uses graph structure; GCN uses Logistic Regression as its final output layer and can be considered a nontrivial generalisation of it. (p. 6)[^original]  
  <sub>anchor: "We have seen Random Forest significantly outperforms Logistic Regression; in fact, it also outperforms GCN"</sub>
- **descriptive / finding or result**: Simply augmenting node features with GCN embeddings before Random Forest helps only marginally according to prior experimentation. (p. 6)[^original]  
  <sub>anchor: "This idea helps only marginally according to prior experimentation."</sub>
- **descriptive / method**: A proposed approach parameterises each decision tree node with a feedforward neural network and, as a future idea, replaces the GCN logistic output layer with this differentiable tree to enable end-to-end training. (p. 6)[^original]  
  <sub>anchor: "One possible approach is to replace the Logistic Regression output layer in GCN by this differentiable version of the decision tree"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Weber, Mark, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Bellei, Claudio, Robinson, Tom et al., "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics" (2019-07-31). https://arxiv.org/pdf/1908.02591
