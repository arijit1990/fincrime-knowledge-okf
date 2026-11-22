---
type: Source Digest
title: 'TeMP-TraG: Edge-based Temporal Message Passing in Transaction Graphs - part 1 of 2 (pp. 1-10)'
description: 'Verified paraphrased digest, pp. 1-10: 1 Introduction; 2 Related Work; 2 Related Work > 2.1 Graph-Based AML and Financial Fraud Detection; and 8 more sections'
resource: https://arxiv.org/abs/2503.16901
tags:
- academic_finding
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-temp-trag-edge-based-temporal-message-passing-in-transaction-gra
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-03-21'
legal_status: unknown
part: 1
parts_total: 2
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
  resource: https://arxiv.org/abs/2503.16901
  title: 'TeMP-TraG: Edge-based Temporal Message Passing in Transaction Graphs'
  author: org:arxiv
  last_modified: '2025-03-21T00:00:00Z'
digest_points: 51
---

# TeMP-TraG: Edge-based Temporal Message Passing in Transaction Graphs (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-10) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / finding or result**: TeMP-TraG is proposed as a graph neural network mechanism that incorporates temporal dynamics into message passing and prioritises more recent transactions when aggregating node messages; the authors report it improves four state-of-the-art GNNs by 6.19% on average. (p. 1)[^original]  
  <sub>anchor: "TeMP-TraG improves four state-of-the-art graph neural networks by 6 _._ 19% on average"</sub>
- **descriptive / context**: Transaction graphs representing financial and trade transactions between entities such as bank accounts and companies can reveal patterns indicative of money laundering and fraud, but detection requires methods handling rich edge features, multigraph structures and temporal dynamics. (p. 1)[^original]  
  <sub>anchor: "effective detection of such cases requires node and edge classification methods capable of addressing the unique challenges"</sub>

## 1 Introduction

- **descriptive / context**: Money laundering facilitates crimes such as fraud, terrorism financing and corruption, creating a need for solutions that analyse financial transaction graphs and identify involved actors. (p. 1)[^original]  
  <sub>anchor: "Money laundering poses a serious threat to global financial systems, facilitating crimes like fraud, terrorism financing, and corruption."</sub>
- **descriptive / context**: GNNs are described as well-suited to transaction graph analysis through node and edge classification. (p. 2)[^original]  
  <sub>anchor: "Graph Neural Networks (GNNs) are well-suited for this task [13] through node and edge classification."</sub>
- **descriptive / limitation**: State-of-the-art GNNs mainly use node features in message passing and often disregard edge features, which are critical in transaction graphs. (p. 2)[^original]  
  <sub>anchor: "State-of-the-art GNNs primarily focus on node features during message passing while often disregarding essential edge features"</sub>
- **descriptive / limitation**: GNNs typically struggle to model multigraph structures, where multiple transactions exist between the same two nodes. (p. 2)[^original]  
  <sub>anchor: "GNNs typically struggle to effectively model multigraph structures, where multiple edges exist between two nodes"</sub>
- **descriptive / limitation**: Temporal dynamics, i.e. prioritising edges by occurrence time, are crucial for detecting illicit activity but are often overlooked in prior research. (p. 2)[^original]  
  <sub>anchor: "involve prioritising edges based on their occurrence time, play a crucial role in detecting illicit activities but are often overlooked"</sub>
- **descriptive / limitation**: EGAT merges edge features with node features, which dilutes edge-specific information such as relationship types and directional properties. (p. 2)[^original]  
  <sub>anchor: "this approach dilutes edge-specific information, such as relationship types and directional properties"</sub>
- **descriptive / limitation**: Sotiropoulos et al. aggregate multiple edges into a single edge using statistical summaries, potentially overlooking structural details such as an unusually high number of transactions between two nodes. (p. 2)[^original]  
  <sub>anchor: "aggregate multiple edges into a single edge using statistical summaries"</sub>
- **descriptive / limitation**: T-EGAT and TeMP split the graph into multiple subgraphs by time interval, making it difficult to capture meaningful relational patterns over time. (p. 2)[^original]  
  <sub>anchor: "split the given graph into multiple subgraphs based on time intervals"</sub>
- **descriptive / finding or result**: Only few approaches (MEGAGNN and Multi-GNN) tackle more than one of the three challenges, and no existing approach addresses all three simultaneously. (p. 2)[^original]  
  <sub>anchor: "no existing approach simultaneously addresses all three of them"</sub>
- **descriptive / context**: Figure 1 contrasts traditional message passing, which aggregates neighbour messages regardless of time, with TeMP-TraG's temporal message passing that weights edges by temporal proximity. (p. 2)[^original]  
  <sub>anchor: "showing that edges are weighted based on temporal proximity"</sub>
- **descriptive / context**: TeMP-TraG is applied on top of existing GNNs such as MEGA-GNN and Multi-GNN, retaining their edge-feature and multigraph capabilities while adding temporal message passing. (p. 2)[^original]  
  <sub>anchor: "TeMP-TraG is applied on top of existing graph neural networks such as MEGA-GNN and Multi-GNN"</sub>
- **descriptive / context**: A burst of transactions in a short period may signal an attempt to rapidly move funds and evade detection, whereas evenly spaced transactions may reflect routine business activity. (p. 3)[^original]  
  <sub>anchor: "a burst of transactions within a short period may signal an attempt to rapidly move funds"</sub>
- **descriptive / finding or result**: Experiments on two financial transaction graph datasets show TeMP-TraG improves four state-of-the-art GNNs by 6.19% on average. (p. 3)[^original]  
  <sub>anchor: "Experimental results on two financial transaction graph datasets show that TeMP-TraG improves four"</sub>

## 2 Related Work

- **descriptive / context**: Traditional AML approaches relied on human judgement and expert knowledge and were often rule-based; they struggled to adapt to dynamic transaction graphs, and recent work uses machine learning and neural networks. (p. 3)[^original]  
  <sub>anchor: "Traditional approaches [10,15,21,22] primarily relied on human judgements and expert knowledge"</sub>

## 2.1 Graph-Based AML and Financial Fraud Detection

- **descriptive / context**: Goecks et al. apply GNNs for link prediction and edge classification in temporal transaction graphs with LightGBM for node classification but do not explicitly integrate temporal dependencies into message passing. (p. 4)[^original]  
  <sub>anchor: "does not explicitly integrate temporal dependencies into message passing"</sub>
- **descriptive / limitation**: Wan et al. combine GCNs with RNNs to capture sequential transaction patterns but lack fine-grained control in dynamic networks. (p. 4)[^original]  
  <sub>anchor: "lacking fine-grained control in dynamic networks"</sub>
- **descriptive / limitation**: Karim et al. use semi-supervised graph learning with topological features for binary AML classification but focus on node-level properties without refining transaction-level representations. (p. 4)[^original]  
  <sub>anchor: "their model primarily focuses on node-level properties without explicitly refining transaction-level representations"</sub>

## 2.2 GNNs for Multigraphs and Edge-Based Learning

- **descriptive / context**: GIN was proved highly expressive and PNA embeds subgraph structure around a node into patch representations; both incorporate edge features into message passing. (p. 4)[^original]  
  <sub>anchor: "which was proved to be a highly expressive GNN architecture"</sub>
- **descriptive / limitation**: EGAT and ADAMM do not fully exploit valuable graph structures due to their aggregations, although they are effective for multigraphs. (p. 4)[^original]  
  <sub>anchor: "EGAT and ADAMM do not fully exploit valuable graph structures due to their aggregations"</sub>
- **descriptive / context**: Multi-GNN incorporates ego IDs, bidirectional edges and port numbering, while MEGA-GNN introduces artificial edges for bidirectional information exchange. (p. 4)[^original]  
  <sub>anchor: "Multi-GNN [9] incorporates ego IDs, bidirectional edges, and port numbering"</sub>
- **descriptive / limitation**: Multigraph-specific models such as Multi-GNN and MEGA-GNN are not time-aware and fall short in capturing temporal patterns. (p. 4)[^original]  
  <sub>anchor: "they are not time-aware and fall short in capturing temporal patterns"</sub>
- **descriptive / limitation**: NNConv and MGCN were developed for molecular graph classification and typically assume undirected graphs and predefined edge types, making them less suitable for transaction graphs. (p. 4)[^original]  
  <sub>anchor: "these models typically assume undirected graphs and predefined edge types"</sub>

## 2.3 Temporal GNNs and Time-Aware Learning

- **descriptive / requirement**: The text states AML requires time-aware methodologies that preserve structural information, and that GNNs need time-aware node and edge embedding mechanisms capturing the impact of past transactions. (p. 5)[^original]  
  <sub>anchor: "AML requires methodologies that are time-aware while preserving structural information of transaction graphs"</sub>
- **descriptive / context**: Wu et al. combine GNNs with Gated Recurrent Units for temporal node embeddings but do not apply time-aware message passing; Li et al. combine multi-hop message passing with personalised PageRank. (p. 5)[^original]  
  <sub>anchor: "Wu et al. [31] combine GNNs with Gated Recurrent Units to generate temporal node embeddings"</sub>
- **descriptive / limitation**: Existing time-aware methods typically consider all neighbours equally in message passing, although transactions in close temporal proximity should have stronger influence on embeddings. (p. 5)[^original]  
  <sub>anchor: "they typically consider all neighbours of a node equally in message passing"</sub>

## 3 Problem Statement

- **descriptive / definition**: A transaction graph is defined as a tuple of nodes, edges, node features, edge features and timestamps, where nodes represent entities such as companies, individuals or bank accounts. (p. 5)[^original]  
  <sub>anchor: "each representing an entity (e.g., a company, an individual or a bank account)"</sub>

## 2.3 Temporal GNNs and Time-Aware Learning

- **descriptive / limitation**: Temporal-graph approaches that split the transaction graph into multiple graphs valid at different periods capture time-dependent relationships only to some extent, according to the authors. (p. 5)[^original]  
  <sub>anchor: "While these approaches capture time-dependent relationships to some extent"</sub>
- **descriptive / context**: Tariq et al. transform the transaction graph into a temporal graph of sequential transactions rather than splitting it into snapshots. (p. 5)[^original]  
  <sub>anchor: "Tariq et al. [25] instead transform the transaction graph into a temporal graph of sequential transactions"</sub>
- **descriptive / method**: T-EGAT performs message passing over temporal graphs by applying attention-based learning across time steps. (p. 5)[^original]  
  <sub>anchor: "T-EGAT [28] performs message passing over these temporal graphs by applying attention-based learning across time steps"</sub>
- **descriptive / limitation**: The authors note that existing temporal methods typically weight all neighbours of a node equally during message passing. (p. 5)[^original]  
  <sub>anchor: "they typically consider all neighbours of a node equally in message passing"</sub>
- **descriptive / method**: The proposed work introduces a time-based weighting mechanism during message passing so that recent interactions have greater influence on embeddings. (p. 5)[^original]  
  <sub>anchor: "introducing a time-based weighting mechanism during message passing, ensuring that recent interactions have a greater influence"</sub>

## 3 Problem Statement

- **descriptive / definition**: Each edge (i, j, k) denotes a transaction between nodes i and j, where k indexes the k-th edge between the same pair, since multiple edges can exist between the same nodes. (p. 6)[^original]  
  <sub>anchor: "as multiple edges can exist between the same pair of nodes, reflecting multiple transactions"</sub>
- **descriptive / definition**: Node feature matrix X has one dx-dimensional row per node, such as creation date or category; edge feature matrix Z has one dz-dimensional row per edge, such as amount, currency or type; T holds an timestamp per edge. (p. 6)[^original]  
  <sub>anchor: "contains a dz-dimensional feature vector (such as amount, currency or type)"</sub>
- **descriptive / definition**: The neighbour set of node i contains all nodes joined to i by an edge in either direction. (p. 6)[^original]  
  <sub>anchor: "N ( i ) = _{j ∈V |_ ( i, j, k ) _∈E ∨_ ( _j, i, k_ ) _∈E}_"</sub>
- **descriptive / definition**: Node classification learns a function predicting a label for each node, e.g. classifying entities as licit or illicit; edge classification is analogous, e.g. classifying transactions as illicit or licit. (p. 6)[^original]  
  <sub>anchor: "for example aiming at classifying entities in a transaction graph as licit or illicit"</sub>

## 4 Approach

- **descriptive / method**: TeMP-TraG pipeline: graph sampling to handle millions of nodes and edges, embedding via multigraph temporal message passing, then an MLP predicts labels for nodes or edges. (p. 6)[^original]  
  <sub>anchor: "we first perform graph sampling to deal with the millions of nodes and edges"</sub>

## 4.1 Overview

- **descriptive / method**: Sampling uses GraphSAGE two-hop neighbourhood sampling, where each node selects a fixed number of direct neighbours and their neighbours. (p. 6)[^original]  
  <sub>anchor: "We employ the GraphSAGE [14] sampling method for efficient learning on large-scale graphs"</sub>
- **descriptive / method**: The embedding function learns latent node and edge representations by aggregating node and multi-edge information via multigraph temporal message passing; a classification function then maps representations to labels. (p. 7)[^original]  
  <sub>anchor: "we apply multigraph temporal message passing"</sub>

## 4.2 Multigraph Message Passing

- **descriptive / method**: Multigraph message passing extends standard single-graph message passing and follows a strategy inspired by MEGA-GNN, adding edge timestamp aggregation alongside edge feature aggregation. (p. 7)[^original]  
  <sub>anchor: "TeMP-TraG employs a MGMP strategy inspired by MEGA-GNN [3]"</sub>
- **descriptive / method**: Multiple edges between two nodes are aggregated into a single representative timestamp using a permutation-invariant function such as max, and into a single edge feature vector. (p. 8)[^original]  
  <sub>anchor: "leveraging a permutation-invariant function (e.g., max) and aggregates edge features into a single representative feature vector"</sub>
- **descriptive / method**: At each layer, parallel edges between i and j are merged with a mean operation over the K edges between them. (p. 8)[^original]  
  <sub>anchor: "we merge multiple edges with a mean operation"</sub>
- **descriptive / method**: Standard message passing then runs: an aggregation function collects neighbour features and connecting edges into a node message, and an update function refreshes node embeddings; edge embeddings are then updated from neighbour node embeddings. (p. 8)[^original]  
  <sub>anchor: "each node i collects features from its neighbours and the connecting edges from the previous layer"</sub>

## 4.3 Temporal Message Passing

- **descriptive / method**: Temporal message passing assigns higher importance to more recent neighbours, unlike traditional message passing where all neighbours contribute equally. (p. 9)[^original]  
  <sub>anchor: "our approach assigns higher importance to more recent neighbours"</sub>
- **descriptive / method**: The time-based weight alpha for a node pair is computed in two steps: first the timestamp of the most recent transaction between the two nodes is selected by max-pooling, then weights are obtained by applying a softmax over transaction timestamps. (p. 10)[^original]  
  <sub>anchor: "The timestamp of the most recent transaction between two nodes is selected by applying a max-pooling operation"</sub>
- **descriptive / method**: A configuration without edge-feature aggregation is proposed for the single-graph setting, enabling extension of SGMP-based GNNs such as Multi-GNN. (p. 10)[^original]  
  <sub>anchor: "TeMP-TraG without Aggregation We further propose a configuration of TeMP-TraG"</sub>
- **descriptive / finding or result**: The authors assume multigraph message passing is especially effective where many edges exist between the same nodes, while single-graph message passing may be more effective in sparser graphs. (p. 10)[^original]  
  <sub>anchor: "MGPM is specifically effective in multigraphs with many edges between the same nodes while SGMP could be more effective in sparser graphs"</sub>

## 4.4 Training

- **descriptive / method**: TeMP-TraG is trained with cross-entropy loss plus L2 regularisation to mitigate overfitting, using the Adam optimiser with early stopping and selecting the model with the highest validation F1-score. (p. 10)[^original]  
  <sub>anchor: "We use the Adam optimizer with early stopping to prevent overfitting, selecting the best model based on the highest validation F1-score"</sub>

## 4.3 Temporal Message Passing

- **descriptive / method**: The node aggregation function in multigraph message passing is modified by incorporating a time-based weighting term. (p. 10)[^original]  
  <sub>anchor: "by incorporating a time-based weighting term"</sub>
- **descriptive / method**: The time-based weighting parameter for a node pair is computed in two steps, first selecting the most recent transaction timestamp via max-pooling and then normalising timestamps with a softmax. (p. 10)[^original]  
  <sub>anchor: "The timestamp of the most recent transaction between two nodes is selected by applying a max-pooling operation"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "TeMP-TraG: Edge-based Temporal Message Passing in Transaction Graphs" (2025-03-21). https://arxiv.org/abs/2503.16901
