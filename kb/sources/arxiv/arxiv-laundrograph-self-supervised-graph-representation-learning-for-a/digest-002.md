---
type: Source Digest
title: 'LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering - part 2 of 3 (pp. 3-5)'
description: 'Verified paraphrased digest, pp. 3-5: 3.2 Self-Supervised anomaly detection; 4 EXPERIMENTS; 4.1 Experimental setup'
resource: https://arxiv.org/abs/2210.14360
tags:
- academic_finding
- alerts_triage
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-laundrograph-self-supervised-graph-representation-learning-for-a
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-10-25'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2210.14360
  title: 'LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2022-10-25T00:00:00Z'
digest_points: 34
---

# LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 3-5) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.2 Self-Supervised anomaly detection

- **descriptive / definition**: The LaundroGraph encoder takes customer and transaction node features and the adjacency matrix and produces embeddings for each customer node and each transaction node, while the decoder takes a customer-transaction embedding pair and outputs the likelihood that the transaction exists for that customer. (p. 3)[^original]  
  <sub>anchor: "The decoder receives a pair of customer-transaction embeddings (zc, zt), and outputs the likelihood of that transaction existing for that customer."</sub>
- **descriptive / method**: The encoder is built from several graph convolutional layers that repeatedly pass messages along a node's local neighbourhood and aggregate them with the source node's own information, so each node's representation reflects its surrounding context. (p. 3)[^original]  
  <sub>anchor: "These operators compute representations by repeatedly sending messages along the edges of a node's local neighbourhood"</sub>
- **descriptive / context**: The authors state that contextual representation from message passing is crucial in AML scenarios. (p. 3)[^original]  
  <sub>anchor: "a property that is crucial in AML scenarios"</sub>
- **descriptive / definition**: The receptive field of each node is determined by the number of GNN layers; more layers allow neighbours further away to affect the central node. (p. 3)[^original]  
  <sub>anchor: "The receptive field of each node is defined by the number of layers of the GNN."</sub>
- **descriptive / method**: The experiments use the graph attention convolution operator (GAT), with separate learnable parameters for each node and edge type because the graph is bipartite. (p. 3)[^original]  
  <sub>anchor: "we use the graph attention convolution operator (GAT) [22]"</sub>
- **descriptive / context**: The authors hypothesise that attention is beneficial when the transaction to classify resembles an existing interaction, as it can assign that interaction a higher attention coefficient. (p. 3)[^original]  
  <sub>anchor: "We hypothesize that the additional expressiveness provided by the attention mechanisms is beneficial in this scenario"</sub>

## 3.2.2 Model overview

- **descriptive / method**: Because the graph is bipartite, a node's neighbours are always of the opposite type (customer nodes connect to transaction nodes and vice versa), and each node type and edge type uses its own set of learnable parameters. (p. 3)[^original]  
  <sub>anchor: "Note that since we have a bipartite graph, nodes _𝑖_ and _𝑗_ will be of different types"</sub>
- **descriptive / method**: In the GAT formulation, the neighbourhood N(i) is the set of neighbours of node i, the symbol for concatenation is used, and the outputs of K attention heads are concatenated over K heads, with alpha(i,j) an attention coefficient between nodes i and j. (p. 3)[^original]  
  <sub>anchor: "In the previous equations, _𝑁_ ( _𝑖_ ) denotes neighbors of node _𝑖_ , ∥ denotes concatenation, with"</sub>
- **descriptive / method**: The authors hypothesise that the extra expressiveness of the attention mechanism helps here, especially when the transaction to classify resembles an existing interaction, since the model can then assign that interaction a higher attention coefficient. (p. 3)[^original]  
  <sub>anchor: "We hypothesize that the additional expressiveness provided by the attention mechanisms is beneficial in this scenario"</sub>

## 3.2 Self-Supervised anomaly detection

- **descriptive / method**: The decoder is a simple feed-forward network; the anomaly score is defined as one minus the predicted edge likelihood, and a single decoder predicts both incoming and outgoing transactions. (p. 4)[^original]  
  <sub>anchor: "Note that we consider a single decoder that predicts both incoming and outgoing transactions."</sub>

## 3.2.3 Training objective

- **descriptive / method**: Because labels are unavailable, the model uses self-supervision: it predicts whether an edge exists between customer and transaction nodes, in a manner similar to graph autoencoders. (p. 4)[^original]  
  <sub>anchor: "Since labels are not available, we resort to self-supervision."</sub>
- **descriptive / method**: Positive examples are existing customer-transaction edges, and negative examples are non-edges created by randomly sampling customer and transaction nodes; the edges in the direction being predicted are severed before prediction. (p. 4)[^original]  
  <sub>anchor: "negative examples are obtained through the sampling function _𝑆_ in Algorithm 1, which randomly samples customer and transaction nodes to create non-edges"</sub>
- **descriptive / method**: The encoder and decoder are trained jointly using a standard binary cross-entropy loss over one positive example and M sampled negative examples. (p. 4)[^original]  
  <sub>anchor: "the encoder and decoder are jointly trained through a standard binary cross-entropy (BCE)"</sub>
- **descriptive / limitation**: The authors identify exploring alternatives to uniform negative sampling as an important direction of future work. (p. 4)[^original]  
  <sub>anchor: "An important direction of future work would be exploring alternatives to uniform negative sampling"</sub>
- **descriptive / method**: In production, negative examples are not used; each incoming transaction is treated as a positive example, its edge is severed, the transaction embedding is computed, and the decoder with the customer embedding (the customer's expected behaviour) yields the anomaly score. (p. 4)[^original]  
  <sub>anchor: "During production, all transactions entering the system are positive examples for which we already know the entities involved."</sub>

## 4.1.1 Dataset

- **descriptive / data or feature**: The dataset is a real-world banking dataset of approximately one year of bank transfers, with the identity undisclosed for privacy reasons; six months of data are used to build the graph. (p. 4)[^original]  
  <sub>anchor: "The dataset consists of approximately one year of bank transfers, and we use 6 months of data to create the graph."</sub>
- **descriptive / data or feature**: Customer profiles are calculated from all transactions prior to the start of the training snapshot, while transaction features describe the transaction itself and mirror a typical rule-based system used by financial institutions. (p. 4)[^original]  
  <sub>anchor: "The features reflect information that is used in a typical rule-based system deployed by financial institutions."</sub>
- **descriptive / data or feature**: There are 66 customer features, including daily, weekly and monthly aggregates of past behaviour, plus attributes such as country, risk rating and max/min amounts. (p. 4)[^original]  
  <sub>anchor: "In total, there are 66 customer features,"</sub>
- **descriptive / data or feature**: Transaction nodes have 12 features describing the interaction, such as amount, countries of the banks involved and time-stamp information. (p. 5)[^original]  
  <sub>anchor: "The transaction nodes contain 12 features reflecting the properties of that interaction"</sub>
- **descriptive / data or feature**: The resulting graph has 3.2M customer nodes and 17.7M transaction nodes, with average in/out node degree of 5.23/4.94 for customer nodes, and 17.1M incoming and 16.2M outgoing edges. (p. 5)[^original]  
  <sub>anchor: "The resulting graph contains 3 _._ 2M customer nodes and 17 _._ 7M transaction nodes"</sub>
- **descriptive / method**: During training, 30% of edges are reserved for supervision and 20% for validation, with the remaining edges used for message passing. (p. 5)[^original]  
  <sub>anchor: "we reserve 30% of the edges for supervision and 20% for validation"</sub>
- **descriptive / method**: The following month of transactions is the test data, evaluated on a subset of 100K customers with around 514K transactions. (p. 5)[^original]  
  <sub>anchor: "The following month of transactions is used as test data, and we report the results on a subset of 100 _𝐾_ customers"</sub>
- **descriptive / method**: Each edge is paired with one randomly sampled non-edge as a negative example (M = 1), and neighbourhood sampling with 32 neighbours per direction at each layer is used to fit the graph in GPU memory. (p. 5)[^original]  
  <sub>anchor: "sampling 32 neighbors in each direction at each layer"</sub>
- **descriptive / method**: The validation set is used to tune hyperparameters with early stopping. (p. 5)[^original]  
  <sub>anchor: "The validation set is used to tune model hyperparameters with the early stopping procedure."</sub>

## 4.1.2 Baselines

- **descriptive / method**: Baselines are an MLP and LightGBM using the same raw features but no structural graph information, predicting edge existence from source customer, destination customer and transaction features. (p. 5)[^original]  
  <sub>anchor: "these baselines are tasked with predicting the existence of an edge"</sub>
- **descriptive / finding or result**: The authors note LightGBM is consistently the best algorithm in this use case of fraud or money-laundering detection with tabular data. (p. 5)[^original]  
  <sub>anchor: "Note that the LightGBM is consistently the best algorithm in this use case"</sub>
- **descriptive / method**: Baseline datasets have equal numbers of positive and negative samples, created by appending random source-customer, destination-customer and transaction negatives to all positive transactions. (p. 5)[^original]  
  <sub>anchor: "we create a dataset with the same number of positive and negative samples"</sub>
- **descriptive / method**: Deep Graph Infomax (DGI) is another baseline, trained to maximise mutual information between nodes and the graph, using random node re-shuffling as corruption; it is extended naively by applying the objective independently to each node type. (p. 5)[^original]  
  <sub>anchor: "we naively extend it to our scenario by independently applying the DGI objective for each node type"</sub>
- **descriptive / method**: For DGI, the decoder is trained on the link prediction task with the same architecture, and at inference customer embeddings are those derived during training; updating them after each new transaction is left as future work. (p. 5)[^original]  
  <sub>anchor: "we leave this as future work"</sub>
- **descriptive / method**: Architecture variants replace GAT with the GraphSAGE operator or the GIN operator. (p. 5)[^original]  
  <sub>anchor: "replacing the GAT [22] operator with two other popular convolutional operators"</sub>

## 4.2 Results

- **descriptive / finding or result**: Table 1 reports test ROC AUC and average precision: MLP 77.26 AUC and 82.45 AP; LightGBM 82.58 AUC and 89.02 AP; DGI 85.87 AUC and 84.06 AP. (p. 5)[^original]  
  <sub>anchor: "|MLP|77_._26|82_._45|"</sub>
- **descriptive / finding or result**: Table 1 reports LaundroGraph with SAGE at 89.97 AUC and 93.17 AP, with GIN at 90.24 AUC and 93.82 AP, and with GAT at 94.83 AUC and 95.22 AP, with GAT the best-performing variant. (p. 5)[^original]  
  <sub>anchor: "|LaundroGraph_𝐺𝐴𝑇_|94_._83|95_._22|"</sub>
- **descriptive / finding or result**: Table 1 caption states these are ROC AUC and average precision results on test data for all methods, with best values shown in bold. (p. 5)[^original]  
  <sub>anchor: "ROC AUC and average precision (AP) results on the test data for all methods under consideration."</sub>
- **descriptive / data or feature**: Figure 2 shows ROC curves and corresponding AUCs for all models considered. (p. 5)[^original]  
  <sub>anchor: "ROC curves and corresponding AUCs for all models considered."</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering" (2022-10-25). https://arxiv.org/abs/2210.14360
