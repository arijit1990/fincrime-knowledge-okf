---
type: Source Digest
title: 'Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering - part 1 of 3 (pp. 1-6)'
description: 'Verified paraphrased digest, pp. 1-6: Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering; Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering > 1 INTRODUCTION; Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering > 2 RELATED WORKS; and 2 more sections'
resource: https://arxiv.org/abs/2302.11880
tags:
- academic_finding
- global_academic
- ml_statistics
- model_development
- network_graph
- preprint
status: stable
source_id: arxiv-catch-me-if-you-can-semi-supervised-graph-learning-for-spotting
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-02-23'
legal_status: unknown
part: 1
parts_total: 3
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
  resource: https://arxiv.org/abs/2302.11880
  title: 'Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering'
  author: org:arxiv
  last_modified: '2023-02-23T00:00:00Z'
digest_points: 66
---

# Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Money laundering is described as criminals using financial services to move large illegal sums to untraceable destinations and integrate them into legitimate systems; the paper proposes semi-supervised graph learning on financial transaction graphs to identify nodes involved in potential money laundering. (p. 1)[^original]  
  <sub>anchor: "Money laundering is the process where criminals use financial services to move massive amounts"</sub>
- **descriptive / limitation**: The authors state that only a tiny fraction of illicit activities is prevented despite AML efforts, and that existing detection approaches yield lower accuracy, making them less reliable. (p. 1)[^original]  
  <sub>anchor: "Despite tremendous efforts to AML only a tiny fraction of illicit activities is prevented."</sub>
- **descriptive / finding or result**: Experimental results suggest the approach can detect money laundering in both real and synthetic transaction graphs. (p. 1)[^original]  
  <sub>anchor: "Experimental results1 suggest that our approach can sport money laundering from real and synthetic transaction graphs."</sub>

## 1 INTRODUCTION

- **descriptive / context**: The paper cites an estimate that about 1.6 trillion USD, corresponding to 2.7% of global GDP, is laundered every year. (p. 1)[^original]  
  <sub>anchor: "It causes approximately 1.6 Trillion USD corresponding to 2.7% of the global GDP is laundered every year"</sub>
- **descriptive / definition**: Money laundering is described as comprising three primary steps: placement, layering and integration. (p. 1)[^original]  
  <sub>anchor: "generally, it is composed of three primary steps: _placement_ , _layering_ , and _integration_ ."</sub>
- **descriptive / definition**: Placement is introducing dirty money into existing financial systems. (p. 1)[^original]  
  <sub>anchor: "Placement is about introducing dirty money into existing financial systems."</sub>
- **descriptive / definition**: Layering is carrying out complex transactions to hide the source of the funds. (p. 1)[^original]  
  <sub>anchor: "Layering is the process of carrying out complex transactions to hide the source of the funds."</sub>
- **descriptive / definition**: Integration is withdrawing the proceeds from a destination bank account before using the funds for legitimate activities. (p. 1)[^original]  
  <sub>anchor: "The integration is about withdrawing the proceeds from a destination bank account before using the fund"</sub>
- **descriptive / definition**: AML is the task of preventing criminals from moving illicit funds through the financial system, and is often perceived through regulatory compliance, with the forensic burden falling mainly on financial institutions. (p. 1)[^original]  
  <sub>anchor: "AML is often perceived through regulatory compliance since the burden of forensic analysis falls primarily on financial institutions"</sub>
- **descriptive / context**: The AML process is described as typically a five-step process: compliance organization with formal AML training; KYC onboarding and profile maintenance; account activity oversight via transaction monitoring systems (TMS); manual review of flagged accounts and transactions; and filing SARs with corresponding restrictive action. (p. 1)[^original]  
  <sub>anchor: "These are typically carried out in a five-step process:"</sub>
- **descriptive / definition**: Transaction monitoring systems are predominantly rules-based thresholding protocols tuned for transaction volume and velocity, with tiered escalation procedures. (p. 1)[^original]  
  <sub>anchor: "Transaction monitoring systems are predominantly rules-based thresholding protocols tuned for the volume and velocity"</sub>
- **descriptive / typology or red flag**: The first laundering topology has one sender and one receiver with many intermediary accounts in a column; the sender divides funds among intermediaries, which resend them to the receiver. (p. 1)[^original]  
  <sub>anchor: "The first topology involves one sender account and one receiver account, and many intermediary accounts forming a column."</sub>
- **descriptive / typology or red flag**: The second laundering topology has one sender, one receiver and a row of intermediary accounts that pass the entire amount along the row to the receiver. (p. 1)[^original]  
  <sub>anchor: "The second topology consists of one sender and one receiver and a row of intermediary accounts."</sub>
- **descriptive / definition**: A transaction graph represents an account as a vertex and a transaction as an edge; a group of accounts can be a vertex (e.g., under a holding company), with an edge representing aggregate transaction volume over a period; a node may be a single account or a set of associated accounts. (p. 1)[^original]  
  <sub>anchor: "A money transfer or transaction graph can be constructed such that a single account is represented as a vertex"</sub>
- **descriptive / context**: Criminals involved in money laundering often hide the original sources of illegal money by using funds in casinos or real estate purchases, or by overvaluing legitimate invoices. (p. 1)[^original]  
  <sub>anchor: "often hide the original sources of illegal money by using the funds in casinos or real estate purchases"</sub>
- **descriptive / context**: AML is often perceived through regulatory compliance, because the burden of forensic analysis falls primarily on financial institutions that are responsible for complying with KYC standards, transaction monitoring, restricting suspect accounts and filing SARs. (p. 1)[^original]  
  <sub>anchor: "the burden of forensic analysis falls primarily on financial institutions that are responsible to comply"</sub>
- **descriptive / context**: The source describes a typical five-step AML process, beginning with introducing a compliance organization within the company including formal AML training for employees. (p. 1)[^original]  
  <sub>anchor: "introducing a compliance organization within the company including formal AML training for employees"</sub>
- **descriptive / context**: The five-step AML process continues with KYC onboarding and profile maintenance, transaction monitoring systems (TMS), manual review of flagged accounts and transactions, and filing SARs with corresponding restrictive action against suspect accounts. (p. 1)[^original]  
  <sub>anchor: "emphasising and execution of KYC onboarding and profile maintenance procedures"</sub>
- **descriptive / context**: Existing methods prevent only a tiny fraction of illicit activities despite tremendous AML efforts, and penalties for failed AML compliance are severe. (p. 1)[^original]  
  <sub>anchor: "while penalties for failed AML compliance are severe"</sub>
- **descriptive / context**: The source states that money laundering usually involves high-volume flows of funds through chains of bank accounts. (p. 1)[^original]  
  <sub>anchor: "Money laundering usually involves high-volume flows of funds through chains of bank accounts"</sub>
- **descriptive / limitation**: Identifying money launderers in massive graphs is challenging because billions of edges between millions of nodes require scalable methods, and criminals mask transactions with layering or multi-hop transactions. (p. 2)[^original]  
  <sub>anchor: "making the identification of money laundering extremely difficult and computationally complex problem."</sub>
- **descriptive / context**: The authors note that the importance of identifying such activities accurately and reliably is stressed for any country or financial organization. (p. 2)[^original]  
  <sub>anchor: "Therefore, it is of uttermost importance for any country or financial organization to identify such activities"</sub>
- **descriptive / context**: Recent non-graph models mostly benefit from features generated by graph-based models such as GNNs; the authors combine graph analytics with tree-based ensemble models in semi-supervised settings to model spatial and temporal information. (p. 2)[^original]  
  <sub>anchor: "thereby modelling both spatial and temporal information in a large-scale graph, in semi-supervised learning settings"</sub>

## 2 RELATED WORKS

- **descriptive / context**: Rule-based classification was the earliest AML approach; the paper notes rule-based algorithms are easy for fraudsters to evade. (p. 2)[^original]  
  <sub>anchor: "However, rule-based algorithms are easy to be evaded by fraudsters [6]."</sub>
- **descriptive / context**: Related work includes an ontology-based expert system for detecting suspicious transactions, fuzzy matching for subgraphs, radial basis function neural networks, and clustering-based grouping of transactions. (p. 2)[^original]  
  <sub>anchor: "Rajput et al. [7] developed an ontology-based expert system to detect suspicious transactions."</sub>
- **descriptive / context**: Methods used for detecting money laundering from transfer graphs include logistic regression, support vector machines, random forest, multilayer perceptron and GNNs. (p. 2)[^original]  
  <sub>anchor: "starting from simple logistic regression (LR), support vector machines (SVM) [9], random forest (RF)"</sub>
- **descriptive / context**: Soltani et al. proposed a structural similarity-based algorithm that finds pairs of transactions with common attributes and behaviours. (p. 2)[^original]  
  <sub>anchor: "This structural similarity-based approach finds pairs of transactions with common attributes and behaviours"</sub>
- **descriptive / limitation**: Approaches that do not perform flow tracking yield lower detection accuracy and cannot provide theoretical guarantees; cross-node flow matters for accuracy and robustness against camouflage. (p. 2)[^original]  
  <sub>anchor: "Methods that do not perform flow tracking, yield lower detection accuracy and hence cannot provide theoretical guarantees"</sub>
- **descriptive / limitation**: Real-world data is often unlabeled or has noisy or sparse labels, while supervised detection algorithms suffer from highly skewed labels and limited adaptability. (p. 2)[^original]  
  <sub>anchor: "real-world data is typically either unlabeled, or has noisy, or sparse labels"</sub>
- **descriptive / definition**: A knowledge graph has entities as nodes and binary relations as edges, formalised as G = {E, R, T}, a labelled directed multigraph of entities, relations and triples (h, r, t). (p. 2)[^original]  
  <sub>anchor: "where nodes represent entities and edges represent binary relations between those entities [13]."</sub>
- **descriptive / context**: Approaches employing structural and behavioural dynamics of dense subgraph detection do not take into account high-volume flows of funds through chains of bank accounts. (p. 2)[^original]  
  <sub>anchor: "some approaches employ structural and behavioural dynamics of dense subgraph detection thereby not taking into consideration"</sub>
- **descriptive / context**: In particular, FlowScope is a flow-based approach for detecting money laundering behaviour, detecting chains of transactions. (p. 2)[^original]  
  <sub>anchor: "In particular, FlowScope [6] is a flow-based approach for detecting money laundering behaviour"</sub>
- **descriptive / method**: Some approaches model transactions as multipartite graphs to detect the complete flow of money from source to destination, in an unsupervised manner based on graphs. (p. 2)[^original]  
  <sub>anchor: "in an unsupervised manner based on graphs"</sub>
- **descriptive / context**: GNN architectures such as GCN, GraphSAGE and FastGCN are noted for efficiency and scalability in graph-based representation learning. (p. 3)[^original]  
  <sub>anchor: "In particular, GNN architectures such as graph convolutional networks (GCN) [4], GraphSAGE [14], and FastGCN [15] have emerged"</sub>
- **descriptive / definition**: A graph embedding model consists of three steps: representing entities and relations, defining a scoring function, and learning entity and relation representations. (p. 3)[^original]  
  <sub>anchor: "A GE model consists of three steps: representing entities and relations, defining a scoring function, and learning entity and relation representation"</sub>
- **descriptive / definition**: Translation-based embeddings (TransD, TransE) treat relations as translations from head to tail entity, but are limited in modelling symmetric, transitive and one-to-many style relations. (p. 3)[^original]  
  <sub>anchor: "However, most translation-based embeddings are limited in their capacity to model complex and diverse objects"</sub>
- **descriptive / definition**: GraphSAGE is an inductive embedding technique that can embed unseen nodes without retraining by sampling and aggregating attributes from each node's local neighbourhood. (p. 3)[^original]  
  <sub>anchor: "Being an inductive embedding technique, GraphSAGE allows extracting embeddings of unseen nodes, without the need to re-training."</sub>
- **descriptive / finding or result**: The cited work reports FastGCN outperformed GCN and GraphSAGE on benchmark datasets by as much as two orders of magnitude without sacrificing accuracy. (p. 3)[^original]  
  <sub>anchor: "FastGCN outperformed GCN and GraphSAGE in various benchmark datasets by as much as two orders of magnitude"</sub>
- **descriptive / finding or result**: Weber et al. trained GCN and FastGCN on a synthetic graph of 1 million nodes and 9 million edges; RF was the best classifier, outperforming GCN, which significantly outperformed LR. (p. 3)[^original]  
  <sub>anchor: "Weber et al. [27] trained GCN and FastGCN models on a large synthetic graph of 1 million nodes and 9 million edges."</sub>
- **descriptive / finding or result**: On the Elliptic Bitcoin transaction graph, a two-layer GCN outperformed linear models such as LR, was comparable to MLP, and underperformed RF. (p. 3)[^original]  
  <sub>anchor: "shows that the GCN model outperforms linear models like LR, comparable to MLP, but underperforms in comparison with RF."</sub>
- **descriptive / finding or result**: The cited work reports that including non-local information about neighbours of a centre node always improves each model's performance. (p. 3)[^original]  
  <sub>anchor: "the inclusion of non-local information – specifically information about the neighbours of a centre node always improves the performance"</sub>
- **descriptive / definition**: EvolveGCN couples spatial and temporal information by evolving the GCN parameters along the time axis with a recurrent neural network. (p. 3)[^original]  
  <sub>anchor: "EvolveGCN evolves along the temporal axis, where a recurrent neural network (RNN) is used for evolving the GCN model’s parameters."</sub>
- **descriptive / definition**: Dynamic graph transformer (DGT) has a transformer module using attention to capture cross-domain knowledge and a pooling module, with the final attention layer producing node embeddings. (p. 3)[^original]  
  <sub>anchor: "The transformer module captures the cross-domain knowledge by the attention mechanism"</sub>

## 3 METHODS

- **descriptive / method**: The authors use pipeline and end-to-end approaches: in the pipeline, an embedding model generates node embeddings that train ERT, GBT and RF classifiers; in the end-to-end setting, classification is done without separate classifiers. (p. 3)[^original]  
  <sub>anchor: "For the former, an embedding model is first trained to generate node embeddings that are used to train the ERT, GBT, and RF classifiers."</sub>
- **descriptive / definition**: The transaction graph G=(V,E) has nodes for accounts and edges for transfers; V is partitioned into inner bank accounts W and outer accounts X (net money in) and Y (net money out), with edge amounts e_ij. (p. 3)[^original]  
  <sub>anchor: "where _W_ is the inner accounts of the bank, and _X_ and _Y_ are sets of outer accounts."</sub>

## 3.1 Problem formulation

- **descriptive / method**: In the semi-supervised setting, the embedding of nodes is followed by training a binary classifier to predict suspiciousness of a target node, using connections to known suspicious nodes, with annotations from alerts. (p. 3)[^original]  
  <sub>anchor: "the task in a semi-supervised learning setting is embedding the nodes into a lower dimensional vector space"</sub>
- **descriptive / method**: To simulate semi-supervision, a certain percentage of nodes, with their edges, is removed and a GE model is trained on the reduced subgraph; embeddings of removed nodes are then generated and used to predict their labels after re-insertion. (p. 4)[^original]  
  <sub>anchor: "we remove a certain per cent of the nodes (including edges from these nodes to any other nodes in the network)"</sub>

## 3.2 Generating directed graphs

- **descriptive / method**: A directed transactional graph is generated in five steps: load transactions, alerts and party datasets; define utility functions for preprocessing and encoding categorical features; generate nodes and edges; form the directed graph; annotate nodes with alerts or additional features. (p. 4)[^original]  
  <sub>anchor: "We generate a directed transactional graph in five steps:"</sub>

## 3.3 Graph embeddings

- **descriptive / method**: Unsupervised graph representation methods Word2vec, Node2vec, Attri2Vec, GraphSAGE and DGT are used to generate node embeddings, since ML classifiers expect fixed-length vectors. (p. 4)[^original]  
  <sub>anchor: "we employ different unsupervised graph representation learning techniques to generate node embeddings"</sub>
- **descriptive / method**: Word2vec and Node2vec generate a corpus via uniform random walks from each entity, then learn node embeddings with the skip-gram model using negative sampling. (p. 4)[^original]  
  <sub>anchor: "a corpus of text _C_ is generated by performing uniform random walks starting from each entity in the graph"</sub>
- **descriptive / method**: Attri2Vec learns node representations by linear or non-linear mapping of node content attributes, predicting context nodes from random-walk pairs with a three-layer neural network. (p. 5)[^original]  
  <sub>anchor: "Attri2Vec learns the representation _⃗vi_ for the target node _vi_ by using it to predict the existence of context node"</sub>
- **descriptive / method**: GraphSAGE learns a binary classifier distinguishing positive node pairs co-occurring in random walks from randomly selected negative pairs. (p. 5)[^original]  
  <sub>anchor: "GraphSAGE learns a binary classifier that predicts whether arbitrary node pairs are likely to co-occur in a random walk"</sub>
- **descriptive / method**: The authors hypothesise that anti-money laundering could benefit from DGT, which couples spatial and temporal information, since the earlier models consider only spatial/structural information. (p. 5)[^original]  
  <sub>anchor: "with the hypothesis that the anti-money laundering could be benefited from it since DGT is able to couple both"</sub>
- **descriptive / method**: For temporal relations, nodes involved in a transfer at time t are linked to their earlier-timestamp transactions, and attention layers aggregate node encodings into node embeddings. (p. 5)[^original]  
  <sub>anchor: "Attention layers are utilized to exchange the information of different nodes"</sub>

## 3.4 Training of classifiers

- **descriptive / method**: Decision trees and ensembles RF, extremely randomized trees (ERT) and gradient-boosted trees (GBT) are trained on learned embeddings; DTs split data on feature thresholds until subsets contain one class. (p. 5)[^original]  
  <sub>anchor: "We train decision trees (DTs) and their ensemble models such as RF, extremely randomized trees (ERT), and gradientboosted trees (GBT) on learned embeddings."</sub>
- **descriptive / method**: For graph-based node classification, the authors follow EvolveGCN and FastGCN training procedures and set the last graph convolution activation to sigmoid so the output is a probability vector over two classes. (p. 5)[^original]  
  <sub>anchor: "the activation function of the last graph convolution layer is set to sigmoid so that _h__u_ _t_is a probability vector over two probable classes."</sub>

## 4 EXPERIMENTS

- **descriptive / context**: Experiments use two datasets: AMLSim, a multi-agent simulation platform for AML where a few agents conduct nefarious activity modelled on real-world patterns, and the Elliptic dataset. (p. 5)[^original]  
  <sub>anchor: "We tested approach on two datasets: _AMLSim_ and _Elliptic dataset_ ."</sub>

## 4.1 Datasets

- **descriptive / data or feature**: The AMLSim data comprises Accounts, Alerts (transactions triggering an AML alert) and Transactions (all transactions with sender and receiver accounts). (p. 5)[^original]  
  <sub>anchor: "Alerts : contains the list of transactions that triggered an alert according to AML guidelines."</sub>
- **descriptive / data or feature**: AMLSim nodes are accounts with account number, type, owner name and creation date/time, designated with cash in, cash out, debit, payment, transfer or deposit activities, and are of organization or individual type; edges carry transaction ID, amount and timestamp. (p. 5)[^original]  
  <sub>anchor: "Each node in the graph represents an account with attributes such as account number, account type, owner name"</sub>
- **descriptive / limitation**: The AMLSim data is sparsely labelled with flagged transactions and SARs. (p. 5)[^original]  
  <sub>anchor: "The data is sparsely labelled with flagged transactions12 and SARs13 ."</sub>
- **descriptive / data or feature**: The Elliptic dataset is an anonymised graph of Bitcoin transactions with handcrafted features built only from publicly available information. (p. 5)[^original]  
  <sub>anchor: "The Elliptic dataset14 is a graph network of Bitcoin transactions with handcrafted features."</sub>
- **descriptive / definition**: In Elliptic, licit entities include exchanges, wallet providers, miners and licit services; illicit entities include scams, malware, terrorist organisations, ransomware and Ponzi schemes. (p. 6)[^original]  
  <sub>anchor: "Licit : Exchanges, wallet providers, miners, licit services."</sub>
- **descriptive / data or feature**: The Elliptic graph has 203,769 node transactions and 234,355 directed edge payments; 2% are illicit, 21% licit and 77% unknown. (p. 6)[^original]  
  <sub>anchor: "The graph contains 203,769 node transactions and 234,355 directed edge payments flow out of which 2% are illicit, 21% are licit."</sub>
- **descriptive / data or feature**: Elliptic has 49 distinct time steps, evenly spaced at 2-week intervals, representing the estimated confirmation time of each transaction. (p. 6)[^original]  
  <sub>anchor: "There are 49 distinct timesteps evenly spaced with an interval of 2 weeks."</sub>
- **descriptive / data or feature**: Each Elliptic node has 166 features; the first 94 represent local information. (p. 6)[^original]  
  <sub>anchor: "the first 94 features represent local information"</sub>
- **descriptive / data or feature**: The remaining 72 Elliptic node features are aggregated from transaction information one-hop backwards and forwards from the centre node. (p. 6)[^original]  
  <sub>anchor: "The remaining 72 features represent aggregated features that are obtained using transaction information one-hop backwards/forwards"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering" (2023-02-23). https://arxiv.org/abs/2302.11880
