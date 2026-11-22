---
type: Source Digest
title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics - part 1 of 2 (pp. 1-6)'
description: 'Verified paraphrased digest, pp. 1-6: Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > ABSTRACT; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > CCS CONCEPTS; and 11 more sections'
resource: https://arxiv.org/abs/1908.02591
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-anti-money-laundering-in-bitcoin-experimenting-with-graph-convol-2
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
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1908.02591
  title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics'
  author: org:arxiv
  last_modified: '2019-07-31T00:00:00Z'
digest_points: 63
---

# Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / data or feature**: The authors contribute the Elliptic Data Set, a time series graph of over 200K Bitcoin transactions (nodes), 234K directed payment flows (edges) and 166 node features, including some based on non-public data, described as the largest labelled transaction data set publicly available in any cryptocurrency. (p. 1)[^original]  
  <sub>anchor: "We contribute the Elliptic Data Set, a time series graph of over 200K Bitcoin transactions (nodes), 234K directed payment flows (edges), and 166 node features"</sub>
- **descriptive / finding or result**: Results from a binary classification task predicting illicit transactions show the superiority of Random Forest, and invite algorithmic work combining Random Forest with graph methods. (p. 1)[^original]  
  <sub>anchor: "The results show the superiority of Random Forest (RF), but also invite algorithmic work to combine the respective powers of RF and graph methods."</sub>

## 1 TOWARD FINANCIAL INCLUSION

- **descriptive / context**: The paper states that approximately 1.7 billion adults are unbanked. (p. 1)[^original]  
  <sub>anchor: "Approximately 1.7 billion adults are unbanked [7]."</sub>
- **descriptive / context**: AML policy imposes high fixed compliance costs on money service businesses and fear of criminal and monetary penalties, making low-value customers seem not worth the risk. (p. 1)[^original]  
  <sub>anchor: "which enforces high fixed costs of compliance on money service businesses (MSBs) along with the fear of criminal and monetary penalties for noncompliance"</sub>
- **descriptive / context**: Restricted access to the financial system is, in part, an unintended consequence of increasingly stringent AML regulations, and higher relative costs of participation are also, in part, a function of AML policy. (p. 1)[^original]  
  <sub>anchor: "is, in part, an unintended consequence of increasingly stringent anti-money laundering (AML) regulations"</sub>
- **descriptive / context**: The paper says the AML rules, while essential for safeguarding the financial system, have a disproportionately negative effect on low-income people, immigrants and refugees. (p. 1)[^original]  
  <sub>anchor: "which, while essential for safeguarding the financial system, have a disproportionately negative effect on low-income people, immigrants, and refugees"</sub>

## ABSTRACT

- **descriptive / data or feature**: The paper offers a simple visualization prototype that can navigate the transaction graph and show model performance on illicit activity over time. (p. 1)[^original]  
  <sub>anchor: "we offer a simple prototype capable of navigating the graph and observing model performance on illicit activity over time"</sub>
- **descriptive / context**: The paper considers visualization for analysis and explainability, which it describes as difficult given the size and dynamism of real-world transaction graphs. (p. 1)[^original]  
  <sub>anchor: "we consider visualization for analysis and explainability, which is difficult given the size and dynamism"</sub>
- **descriptive / context**: The authors hope to invite feedback on their ongoing inquiry and to inspire others to work on this societally important challenge. (p. 1)[^original]  
  <sub>anchor: "invite feedback in support of our ongoing inquiry"</sub>

## 1 TOWARD FINANCIAL INCLUSION

- **descriptive / finding or result**: Global remittances to low- and middle-income countries reached a record high of $529 billion in 2018, far outpacing global aid of $153 billion. (p. 2)[^original]  
  <sub>anchor: "global remittances to low-andmiddle-income countries, which reached a record high $529 billion in 2018, far outpacing the global aid contribution of $153 billion"</sub>
- **descriptive / finding or result**: The current average cost of sending $200 is 7 percent, with some countries above 10 percent; UN Sustainable Development Goal 10.7 targets a reduction to 3 percent by 2030. (p. 2)[^original]  
  <sub>anchor: "The current average cost of sending $200 is an expensive 7 percent, with some countries suffering rates of over 10 percent."</sub>
- **descriptive / context**: The paper argues AML regulations cannot be dismissed as over-burdensome, given illicit industries such as drug cartels, human trafficking and terrorist organizations. (p. 2)[^original]  
  <sub>anchor: "And yet AML regulations cannot be summarily dismissed as over burdensome."</sub>
- **descriptive / case example**: The 1MDB scandal reportedly robbed the Malaysian people of over $11 billion in taxpayer funds, with mega-fines and criminal indictments for Goldman Sachs among others implicated. (p. 2)[^original]  
  <sub>anchor: "robbed the Malaysian people of over $11 billion in taxpayer funds earmarked for the nation’s development [22]"</sub>
- **descriptive / case example**: The Danske Bank scandal in Estonia reportedly served as a hub for an estimated $200 billion in illicit money flows from Russia and Azerbaijan, causing billions of dollars in losses for Danske Bank and Deutsche Bank. (p. 2)[^original]  
  <sub>anchor: "served as a hub for an estimated $200 billion in illicit money flows from Russia and Azerbaijan"</sub>
- **descriptive / context**: The paper poses the research question of whether the right tools and open data can reconcile the need for safety with financial inclusion. (p. 2)[^original]  
  <sub>anchor: "with the right tools and open data, can we help reconcile the need for safety with the cause of financial inclusion?"</sub>

## 1.1 AML in a cryptocurrency world

- **descriptive / context**: Cryptocurrency spurred startups aiming at low-cost peer-to-peer cross-border transfers, many targeting remittances and financial inclusion, while Bitcoin's pseudonymity was exploited by criminals for ransomware and dark marketplaces. (p. 2)[^original]  
  <sub>anchor: "Many criminals used Bitcoin’s pseudonymity to hide in plain sight, conducting ransomware attacks and operating dark marketplaces"</sub>
- **mandatory / requirement**: Under the FinCEN guidance, the risk assessments must inform management of customer relationships, including implementing controls commensurate with risk, so MSBs must act against suspicious accounts (e.g. freezing or closing them), not only report them. (p. 2)[^original]  
  <sub>anchor: "The assessments must inform the management of customer relationships, including the implementation of controls commensurate with risk"</sub>
- **descriptive / definition**: The FinCEN guidance defines a well-developed risk assessment as one that assists MSBs in identifying and providing a comprehensive analysis of their individual risk profile. (p. 2)[^original]  
  <sub>anchor: "The guidance defines a “well-developed risk assessment” as “assisting MSBs in identifying and providing a comprehensive analysis of their individual risk profile.”"</sub>
- **mandatory / requirement**: The guidance requires MSBs, under the Know Your Customer requirements of the BSA, to know enough about their customers to determine the risk level they represent. (p. 2)[^original]  
  <sub>anchor: "the guidance requires MSBs to “know enough about their customers to be able to determine the risk level they represent to the institution.”"</sub>
- **descriptive / context**: In practice an implicit but effectively enforced requirement is to know the customer's customer; in traditional finance this is done by phone calls between MSBs, whereas Bitcoin's full transaction graph is publicly available though pseudonymous and unlabelled. (p. 2)[^original]  
  <sub>anchor: "In the fragmented data ecosystem of traditional finance, this aspect of compliance is often executed by phone calls between MSBs."</sub>
- **descriptive / context**: Cryptocurrency intelligence companies have emerged to offer AML solutions for the crypto domain, where public data is an advantage for investigators while pseudonymity benefits criminals. (p. 2)[^original]  
  <sub>anchor: "Whereas the pseudonymity of Bitcoin is an advantage for criminals, the public availability of data is a key advantage for investigators."</sub>

## 2 THE ELLIPTIC DATA SET

- **descriptive / definition**: The Elliptic Data Set is a graph of Bitcoin transactions with handcrafted features, mapping transactions to real entities in licit categories (exchanges, wallet providers, miners, licit services) versus illicit ones (scams, malware, terrorist organizations, ransomware, Ponzi schemes). (p. 2)[^original]  
  <sub>anchor: "The Elliptic Data Set maps Bitcoin transactions to real entities belonging to _licit_ categories"</sub>
- **descriptive / definition**: In the data set a graph is constructed where nodes are transactions and edges represent the flow of Bitcoin from one transaction to the next; a transaction is deemed licit or illicit according to the category of the entity controlling the private keys of its input addresses. (p. 2)[^original]  
  <sub>anchor: "the nodes represent transactions and the edges represent the flow of Bitcoin currency (BTC) going from one transaction to the next one"</sub>
- **descriptive / data or feature**: All features in the Elliptic Data Set are constructed using only publicly available information. (p. 2)[^original]  
  <sub>anchor: "Importantly, all features are constructed using only publicly available information."</sub>

## 2.1.1 Nodes and Edges

- **descriptive / data or feature**: The data set has 203,769 node transactions and 234,355 directed edge payment flows; the full Bitcoin network is said to have approximately 438M nodes and 1.1B edges. (p. 2)[^original]  
  <sub>anchor: "There are 203,769 node transactions and 234,355 directed edge payments flows."</sub>
- **descriptive / data or feature**: Of the nodes, two percent (4,545) are labelled class1 (illicit), twenty-one percent (42,019) are labelled class2 (licit), and the remainder are unlabelled for licit versus illicit status. (p. 3)[^original]  
  <sub>anchor: "In the Elliptic Data Set, two percent (4,545) are labelled _class1 (illicit)_ . Twenty-one percent (42,019) are labelled _class2 (licit)_ ."</sub>

## 2.1.2 Features

- **descriptive / data or feature**: Each node has 166 features: the first 94 are local information about the transaction (time step, inputs/outputs, fee, output volume, average BTC and transaction counts), and the remaining 72 are aggregated features over one-hop neighbour transactions (maximum, minimum, standard deviation and correlation coefficients). (p. 3)[^original]  
  <sub>anchor: "The first 94 features represent _local information_ about the transaction"</sub>
- **descriptive / limitation**: A footnote notes the labelling argument ignores mixer transactions where inputs are controlled by multiple entities. (p. 3)[^original]  
  <sub>anchor: "Note that for simplicity, this argument ignores mixer transactions where the inputs are controlled by multiple entities."</sub>

## 2.1.3 Temporal Information

- **descriptive / data or feature**: Nodes carry a timestamp estimating confirmation time; there are 49 distinct time steps spaced about two weeks apart, each a single connected component with no edges between time steps, and 1,000 to 8,000 nodes per step. (p. 3)[^original]  
  <sub>anchor: "There are 49 distinct time steps, evenly spaced with an interval of about two weeks."</sub>

## 2.2 Notes on Feature Construction

- **descriptive / context**: Building features requires access to the complete blockchain, about 200GB of compressed data and around 400 million addressed transactions, to observe full transaction history; Elliptic uses an all-in-memory graph engine for feature computation. (p. 3)[^original]  
  <sub>anchor: "Though not all transactions are included in the subset used in this study, it is still necessary to access the complete blockchain"</sub>

## 2.1.2 Features

- **descriptive / context**: The licit/illicit labelling is informed by heuristic reasoning; for example, many inputs and address reuse are associated with higher address clustering, making entities that forgo anonymity-preserving measures more likely licit, while illicit activity may favour fewer inputs. (p. 3)[^original]  
  <sub>anchor: "It follows that entities eschewing anonymity-preserving measures for large volumes of user requests are likely to be licit"</sub>

## 2.2 Notes on Feature Construction

- **descriptive / limitation**: The authors note that the simple statistical aggregation used for the 72 neighbourhood features is sub-optimal because it loses a significant amount of information about neighbour heterogeneity. (p. 3)[^original]  
  <sub>anchor: "In general, this solution is sub-optimal because it carries a significant loss of information."</sub>
- **descriptive / context**: AML analytics is described as an anomaly detection challenge of classifying a small number of illicit transactions in massive data sets, with industry-standard false positive rates of upwards of 90%. (p. 3)[^original]  
  <sub>anchor: "Industry standard high false positive rates of upwards of 90% inhibit this effort."</sub>
- **descriptive / expectation**: The aim is to reduce false positive rates without increasing false negative rates, including more innocent people without letting more criminals through; Logistic Regression and Random Forest are benchmark methods. (p. 3)[^original]  
  <sub>anchor: "We want to reduce false positive rates without increasing false negative rates"</sub>

## 3 TASK AND METHODS

- **descriptive / definition**: The task is transaction screening: each unlabelled Bitcoin transaction is to be classified as illicit or licit to assess risk of transactions to and from wallets. (p. 3)[^original]  
  <sub>anchor: "each unlabelled Bitcoin transaction is to be classified illicit or licit"</sub>
- **descriptive / method**: Benchmark methods use the first 94 local features for supervised binary classification: Logistic Regression, Multilayer Perceptron and Random Forest; these do not use graph information. (p. 3)[^original]  
  <sub>anchor: "Such techniques include Logistic Regression [1], Multilayer Perceptron (MLP) (ibid), and Random Forest [2]."</sub>

## 2.1.3 Temporal Information.

- **descriptive / limitation**: The second challenge is the heterogeneity in the number of neighbours a transaction can have, which the paper says arises from the graph structure of the data. (p. 3)[^original]  
  <sub>anchor: "the heterogeneity in the number of neighbors a transaction can have"</sub>
- **descriptive / limitation**: The paper says that building the 72 aggregated features by naively taking statistical aggregates of neighbour features is generally sub-optimal because it loses significant information. (p. 3)[^original]  
  <sub>anchor: "In general, this solution is sub-optimal because it carries a significant loss of information"</sub>

## 3 TASK AND METHODS

- **descriptive / context**: Random Forest is popular for accuracy and Logistic Regression for explainability, and the two are often used together in AML. (p. 4)[^original]  
  <sub>anchor: "Random Forest for accuracy and Logistic Regression for explainability."</sub>

## 3.1 Benchmark Methods

- **descriptive / finding or result**: Adding the 72 neighbourhood features to local features improves performance, showing graph structure carries information for the binary classification problem, but purely feature-based methods are hard to extend beyond the immediate neighbourhood. (p. 4)[^original]  
  <sub>anchor: "While this approach shows the graph structure carries in the binary classification problem"</sub>

## 3.2 Graph Convolutional Networks (GCN)

- **descriptive / method**: A GCN consists of multiple layers of graph convolution, similar to a perceptron but with a neighbourhood aggregation step motivated by spectral convolution. (p. 4)[^original]  
  <sub>anchor: "A GCN consists of multiple layers of graph convolution, which is similar to a perceptron but additionally uses a neighborhood aggregation step motivated by spectral convolution."</sub>
- **descriptive / method**: The initial embedding matrix is the node features, and in node classification the output layer is a softmax producing prediction probabilities; the activation is typically ReLU for all but the output layer. (p. 4)[^original]  
  <sub>anchor: "The initial embedding matrix comes from the node features; i.e., _H_(0) = _X_ ."</sub>
- **descriptive / method**: The Skip-GCN variant adds a skip connection between the first intermediate embedding and the input node features; when its weights are zero it reduces to Logistic Regression, so it should be at least as powerful as Logistic Regression. (p. 4)[^original]  
  <sub>anchor: "Hence, Skip-GCN should be at least as powerful as Logistic Regression."</sub>

## 3.3 Temporal Modeling

- **descriptive / context**: Financial data are temporal and a model designed to capture system dynamics may generalise better to subsequent time steps and forecast further ahead. (p. 4)[^original]  
  <sub>anchor: "A prediction model will be more useful if it is designed in a manner to capture the dynamism."</sub>
- **descriptive / method**: EvolveGCN extends GCN by computing a separate GCN for each time step, connected through a recurrent neural network that treats GCN weights as system state and is updated using the top-k influential node embeddings. (p. 4)[^original]  
  <sub>anchor: "These GCNs are then connected through a recurrent neural network (RNN) to capture the system dynamics."</sub>

## 4 EXPERIMENTS

- **descriptive / method**: A 70:30 temporal split is used: the first 34 time steps for training and the last 15 for testing, with GCN trained in an inductive setting, chosen because the temporal split reflects the nature of the task. (p. 4)[^original]  
  <sub>anchor: "We performed a 70:30 temporal split of training and test data, respectively. That is, the first 34 time steps are used for training the model and the last 15 for test."</sub>
- **descriptive / method**: Logistic Regression uses scikit-learn default parameters; Random Forest uses scikit-learn with 50 estimators and 50 max features; the MLP is implemented in PyTorch with one hidden layer of 50 neurons, trained for 200 epochs with the Adam optimizer and learning rate 0.001. (p. 4)[^original]  
  <sub>anchor: "Our MLP had one hidden layer of 50 neurons and was trained for 200 epochs by using the _Adam_ optimizer and a learning rate of 0.001."</sub>
- **descriptive / method**: Models were evaluated on all 166 features (AF) and on the 94 local features (LF). (p. 4)[^original]  
  <sub>anchor: "We evaluated these models by using all the 166 features (referred to as _AF_ ), as well as only the local ones"</sub>
- **descriptive / method**: The GCN was trained for 1000 epochs with Adam at learning rate 0.001, using a 2-layer GCN and node embeddings of size 100 after hyper-parameter tuning. (p. 5)[^original]  
  <sub>anchor: "We trained the GCN model for 1000 epochs using the _Adam_ optimizer with a learning"</sub>
- **descriptive / method**: Because classes are imbalanced, the GCN used a weighted cross entropy loss giving more importance to illicit samples, with a 0.3/0.7 ratio for licit and illicit classes after tuning. (p. 5)[^original]  
  <sub>anchor: "Hence, we trained the GCN model using a weighted cross entropy loss to provide higher importance to the illicit samples."</sub>
- **descriptive / finding or result**: Table 1 illicit results: Logistic Regression AF precision 0.404, recall 0.593, F1 0.481; LR AF+NE 0.537, 0.528, 0.533; LR LF 0.348, 0.668, 0.457; LR LF+NE 0.518, 0.571, 0.543. (p. 5)[^original]  
  <sub>anchor: "Logistic Regr_AF_|0.404|0.593|0.481|0.931|"</sub>
- **descriptive / finding or result**: Table 1 illicit results for Random Forest: AF precision 0.956, recall 0.670, F1 0.788; AF+NE 0.971, 0.675, 0.796; LF 0.803, 0.611, 0.694; LF+NE 0.878, 0.668, 0.759. (p. 5)[^original]  
  <sub>anchor: "RandomForest_AF_|0.956|0.670|0.788|0.977|"</sub>
- **descriptive / finding or result**: Table 1 illicit results for MLP: AF precision 0.694, recall 0.617, F1 0.653; AF+NE 0.780, 0.617, 0.689; LF 0.637, 0.662, 0.649; LF+NE 0.6819, 0.5782, 0.6258. (p. 5)[^original]  
  <sub>anchor: "MLP_AF_|0.694|0.617|0.653|0.962|"</sub>
- **descriptive / finding or result**: Table 1 illicit results: GCN precision 0.812, recall 0.512, F1 0.628; Skip-GCN precision 0.812, recall 0.623, F1 0.705, micro-averaged F1 0.966. (p. 5)[^original]  
  <sub>anchor: "|GCN|0.812|0.512|0.628|0.961|"</sub>
- **descriptive / finding or result**: GCN and Skip-GCN outperform Logistic Regression, indicating the usefulness of graph-based methods, but with these informative features Random Forest achieves the best F1 score. (p. 5)[^original]  
  <sub>anchor: "Note that GCN and the variant Skip-GCN outperform Logistic Regression"</sub>
- **descriptive / finding or result**: For all three evaluated models, using aggregated features (AF) rather than only local features (LF) led to higher accuracy, indicating the importance of graph structure. (p. 5)[^original]  
  <sub>anchor: "For all the three evaluated models, the aggregated information led to higher accuracy"</sub>
- **descriptive / method**: An enhanced feature set concatenates GCN node embeddings with the original features; this improves accuracy for both full and local feature sets. (p. 5)[^original]  
  <sub>anchor: "In this setting, we concatenated the node embeddings obtained from GCN with the original features _X_ ."</sub>
- **descriptive / finding or result**: Table 2: EvolveGCN consistently outperforms the non-temporal GCN, with illicit F1 0.720 versus 0.705 and micro-averaged F1 0.968 versus 0.966, though the improvement is not substantial for this data set. (p. 5)[^original]  
  <sub>anchor: "EvolveGCN consistently outperforms GCN, although the improvement is not substantial for this data set."</sub>
- **descriptive / limitation**: Future work may explore alternative forms of system input to drive the recurrent GRU update in EvolveGCN. (p. 5)[^original]  
  <sub>anchor: "One avenue of further investigation is the use of alternative forms of system input to drive the recurrent update inside GRU."</sub>
- **descriptive / case example**: A dark market shutdown at time step 43 causes all methods to perform poorly afterwards; even a Random Forest retrained after every test step cannot reliably capture new illicit transactions, making robustness to emerging events a major challenge. (p. 5)[^original]  
  <sub>anchor: "this event causes all methods to perform poorly after the shutdown."</sub>

## 5 DISCUSSION

- **descriptive / finding or result**: Random Forest significantly outperforms Logistic Regression and also outperforms GCN, even though GCN uses graph structure; GCN uses Logistic Regression as its final output layer and can be seen as a nontrivial generalisation of Logistic Regression. (p. 6)[^original]  
  <sub>anchor: "We have seen Random Forest significantly outperforms Logistic Regression; in fact, it also outperforms GCN"</sub>
- **descriptive / finding or result**: Augmenting node features with GCN embeddings before running Random Forest helps only marginally according to prior experimentation. (p. 6)[^original]  
  <sub>anchor: "This idea helps only marginally according to prior experimentation."</sub>
- **descriptive / method**: Another proposal parameterises each node in decision trees with a feedforward neural network, combining Random Forest with neural networks but not suggesting how graph information is incorporated; a possible approach replaces GCN's logistic output layer with this differentiable tree for end-to-end training, left for future investigation. (p. 6)[^original]  
  <sub>anchor: "One possible approach is to replace the Logistic Regression output layer in GCN by this differentiable version of the decision tree"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics" (2019-07-31). https://arxiv.org/abs/1908.02591
