---
type: Source Digest
title: Explainable Fraud Detection with GNNExplainer and Shapley Values - part 2 of 3 (pp. 17-26)
description: 'Verified paraphrased digest, pp. 17-26: 4. Research Method > 4.1. Datasets; 4. Research Method > 4.2. Data Analysis and Feature Engineering; 4. Research Method > 4.3. Graph Construction; and 3 more sections'
resource: https://arxiv.org/abs/2509.12262
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-explainable-fraud-detection-with-gnnexplainer-and-shapley-values
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-12-09'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2509.12262
  title: Explainable Fraud Detection with GNNExplainer and Shapley Values
  author: org:arxiv
  last_modified: '2025-12-09T00:00:00Z'
digest_points: 29
---

# Explainable Fraud Detection with GNNExplainer and Shapley Values (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 17-26) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.1. Datasets

- **descriptive / data or feature**: The synthetic payment data for fraud detection was obtained from J.P.Morgan and generated based on the multi-agent framework proposed by Borrajo et al. (2020). (p. 17)[^original]  
  <sub>anchor: "We obtain the synthetic payment data for fraud detection from J.P.Morgan. The dataset is generated based on the multi-agent framework proposed by Borrajo et al. (2020)."</sub>
- **descriptive / context**: The simulator used by planning agents has several parts, including an Execution module that generates a plan through a reasoning cycle of planning, executing actions and observing the resulting state; goal generation is also used to obtain new goals or state components. (p. 17)[^original]  
  <sub>anchor: "This module works by taking in information about the environment and using it to generate a plan through a reasoning cycle that involves Planning, executing actions, and observing the resulting state."</sub>

## 4.2. Data Analysis and Feature Engineering

- **descriptive / method**: Data analysis was carried out using the JMP Pro software application. (p. 18)[^original]  
  <sub>anchor: "Data analysis is carried out using JMP Pro (Jones and Sall, 2011) software application."</sub>
- **descriptive / data or feature**: The authors suspected that differences in transaction amount and timestamp between transactions of the same sender or receiver could be good features; these were labelled dAmount and dTime. Non-fraud transactions are labelled 0 and fraud transactions labelled 1. (p. 18)[^original]  
  <sub>anchor: "We suspect that the differences in transaction amount and timestamp between different transactions of the same sender or receiver could be good features to the machine learning model."</sub>

## 4.1. Datasets

- **descriptive / limitation**: The simulator can be used with different domains, but its goal reasoning capability requires generating behaviour for at least two types of agents within the same domain. (p. 18)[^original]  
  <sub>anchor: "Goal reasoning which requires generating behaviour for at least two types of agents within the same domain"</sub>
- **descriptive / limitation**: The exact details of behaviour patterns of agents in the J.P.Morgan dataset are not provided, so further data analysis is needed to identify fraudulent patterns. (p. 18)[^original]  
  <sub>anchor: "the exact details of behaviour patterns of agents in the dataset are not provided by J.P.Morgan"</sub>

## 4.2. Data Analysis and Feature Engineering

- **descriptive / finding or result**: Plots showed clear differences between fraud and non-fraud classes for dTime and dAmount: non-fraud accounts take more time between transactions while fraud accounts transact quickly, and amount differences are significant for fraud accounts but mostly stable for non-fraud accounts. (p. 19)[^original]  
  <sub>anchor: "Non-fraud accounts seem to take more time between transactions, while fraud accounts transact quite rapidly."</sub>
- **descriptive / finding or result**: The authors decided to add the dAmount and dTime features to the original dataset. (p. 19)[^original]  
  <sub>anchor: "We decide to add these 2 features to the original dataset."</sub>
- **descriptive / finding or result**: The Sector and Line of Business (Lob) fields were removed because they contain abstract values that might not aid explanation and their value distributions show little difference between fraud and non-fraud cases (Figures 10 and 11). (p. 20)[^original]  
  <sub>anchor: "there is not much difference of the value distribution of these field between fraud and non-fraud cases, so we remove them from the dataset."</sub>

## 4.3. Graph Construction

- **descriptive / definition**: In the heterogeneous graph G, each node has a type from the set Transaction, Account, User and Country. (p. 20)[^original]  
  <sub>anchor: "each node 𝑣∈𝑉 has a type 𝑁𝑜𝑑𝑒𝑇𝑦𝑝𝑒(𝑣) ∈𝐴 where 𝐴≔ {𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛, 𝐴𝑐𝑐𝑜𝑢𝑛𝑡, 𝑈𝑠𝑒𝑟, 𝐶𝑜𝑢𝑛𝑡𝑟𝑦}."</sub>
- **descriptive / data or feature**: Initial features of Transaction nodes are USD Amount, dAmount and dTime; node and edge type features are one-hot encoded before entering the heterogeneous convolution layer. (p. 20)[^original]  
  <sub>anchor: "their initial features are 𝐹𝑒𝑎𝑡𝑢𝑟𝑒𝑠(𝑣) ≔{𝑈𝑆𝐷 𝐴𝑚𝑜𝑢𝑛𝑡, 𝑑𝐴𝑚𝑜𝑢𝑛𝑡, 𝑑𝑇𝑖𝑚𝑒}. Node and edge type features are onehot encoded"</sub>
- **descriptive / method**: An Account node is created for each unique value of Sender_Account and Bene_Account, and a Transaction node is created per Transaction_Id; edges run from each transaction node to the non-transaction nodes in the same row. (p. 20)[^original]  
  <sub>anchor: "an _Account_ node is created for each unique value of _Sender_Account_ and _Bene_Account_ in the dataset, and a _Transaction_ node is created according to the _Transaction_Id_ field."</sub>
- **descriptive / method**: The graph was constructed from the J.P.Morgan tabular dataset using a Neo4j database. (p. 21)[^original]  
  <sub>anchor: "We construct the graph based on the tabular dataset from J.P.Morgan using Neo4j database."</sub>

## 4.4. Baseline Models

- **descriptive / method**: GEM and GAT were chosen as baseline models because they are similar to the proposed model while having simpler architectures. (p. 21)[^original]  
  <sub>anchor: "GEM (Liu et al, 2018) and GAT (Veličković et al, 2017) are chosen as baseline models due to them being similar to the proposed model while having simpler architecture."</sub>

## 4.3. Graph Construction

- **descriptive / data or feature**: Edge types Executed_In, Sent_To and Sent_By, and Transferred_By and Received_By are mapped to the node types they connect: Executed_In links Transaction to Country, Sent_To and Sent_By link Transaction to Account, and Transferred_By and Received_By link Transaction to Users. (p. 21)[^original]  
  <sub>anchor: "Regarding edge types, we have the following mappings between edge types and involved node types:"</sub>

## 4.4. Baseline Models

- **descriptive / limitation**: GAT does not account for node type and edge type features in its attention calculation, so it is expected to perform worse than the proposed model on heterogeneous graphs; it computes attention for each node sequentially, whereas the proposed model uses multi-headed Transformer attention. The authors nonetheless consider GAT a possibly good baseline for fraud detection. (p. 22)[^original]  
  <sub>anchor: "Nevertheless, GAT could still be a good baseline model for the task of fraud detection."</sub>
- **descriptive / limitation**: GEM targets heterogeneous graphs, but its node embedding contains no type features, so it cannot learn interactions between type relations; it was still chosen because it was tested on Alipay datasets and used in Alipay's payment system to detect fraud. (p. 22)[^original]  
  <sub>anchor: "while it targets heterogeneous graph inputs, its node embedding does not contain type features, and thus it cannot learn interaction between type relations."</sub>

## 4.5. Proposed Model

- **descriptive / method**: The proposed model is the xFraud detector from section 3.1.3 with modifications to its heterogeneous convolution layer. (p. 22)[^original]  
  <sub>anchor: "We utilize the xFraud detector model presented in section 3.1.3 with some modifications to its heterogeneous convolution layer."</sub>
- **descriptive / method**: Node type and edge type embeddings and source and target attention weight matrices are initialised with zero weights, while key, query and value weight matrices are initialised using the Xavier method. (p. 22)[^original]  
  <sub>anchor: "we initialize the node type embeddings 𝑁𝑜𝑑𝑒𝑇𝑦𝑝𝑒𝐸𝑚𝑏(𝑣) and edge type embeddings 𝐸𝑑𝑔𝑒𝑇𝑦𝑝𝑒𝐸𝑚𝑏(𝑒) with zero weights"</sub>
- **descriptive / method**: The heterogeneous convolution layer aggregates neighbourhood messages by simple averaging followed by a non-linear activation, weighted by attention; multi-head query, key and value vectors are built for each target node, with the first layer using transaction features and node type embedding. (p. 23)[^original]  
  <sub>anchor: "The _Aggregate_ function carries out a simple averaging followed by a non-linear activation to aggregate neighbourhood message by the attention weight."</sub>
- **descriptive / method**: Attention is computed per head, combined across h heads by vector concatenation, normalised by softmax over the target node's neighbours, and messages are passed between consecutive layers. (p. 24)[^original]  
  <sub>anchor: "Where 𝑁(𝑣𝑡) is the neighbours of the target node, ℎ is the number of attention heads, and || is vector concatenation operator."</sub>
- **descriptive / finding or result**: The authors state the xFraud detector is very similar to HGT but differs in attention and message passing because it avoids aggregating over different node types with different weight matrices, which they report gives better detector performance on their synthetic dataset. (p. 24)[^original]  
  <sub>anchor: "This gives us better performance in the detector on our synthetic dataset."</sub>

## 4.5. Composite Explainer

- **descriptive / method**: The proposed composite explainer has three components: a GNNExplainer graph, node feature importance, and edge missingness importance. (p. 25)[^original]  
  <sub>anchor: "We propose a composite explainer consisting of 3 components 1) a GNNExplainer graph,"</sub>
- **descriptive / method**: GNNExplainer takes the trained xFraud detector, the node to explain and its relevant input subgraph, and produces edge and feature weights used to extract the most important edges and nodes for the explanation subgraph. (p. 25)[^original]  
  <sub>anchor: "GNNExplainer takes in the trained xFraud detector model, the node to explain 𝑣 and the input subgraph relevant to the node 𝑣, and produces edge and feature weights"</sub>
- **descriptive / data or feature**: To keep explanation subgraphs concise, the maximum subgraph depth is 6 and the maximum width at each level is 16, giving a maximum of 96 nodes, consistent with the detector input for each node. (p. 25)[^original]  
  <sub>anchor: "the maximum depth for a subgraph is 6, and the maximum width at each level is 16, making the maximum number of nodes in a graph 96."</sub>

## 4.5.1. GNNExplainer

- **descriptive / context**: The authors state it is challenging to determine the directional influence of selected nodes and features on predictions using mutual information (MI), so they proposed an algorithm approximating Shapley values for edge missingness and node feature contribution, implementing Strumbelj and Kononenko (2014) with Monte-Carlo sampling. (p. 25)[^original]  
  <sub>anchor: "it is challenging to determine the directional influence of selected nodes and features on the model's prediction using MI."</sub>

## 4.5.2. Node Feature Shapley Values

- **descriptive / finding or result**: The sign of a node feature Shapley value indicates whether the feature has a negative or positive correlation with the final prediction, helping match visualisations with known fraud patterns, such as whether a low transaction amount is associated with fraud prediction. (p. 26)[^original]  
  <sub>anchor: "The resulted Shapley value can tell us whether the node feature has a negative or positive correlation with the final prediction."</sub>

## 4.5.3. Edge Missingness Shapley Values

- **descriptive / method**: Edge missingness Shapley values are approximated over M iterations by sampling coalitions of edges (1 present, 0 absent) with the edge of interest absent in one and present in the other, computing the prediction difference and averaging over iterations. (p. 26)[^original]  
  <sub>anchor: "Sample coalitions 𝑧𝑘′ ∈{0,1}𝑀and 𝑧𝑘 ∈{0,1}𝑀 (1 = edge present in coalition, 0 = edge absent)"</sub>
- **descriptive / finding or result**: An edge missingness Shapley value shows whether the prediction would change if the edge were removed; a highly negative value means removing the edge flips the prediction to the other class, indicating the edge carries most of the message passing behind the node's prediction. (p. 26)[^original]  
  <sub>anchor: "a highly negative Shapley value for an edge means that removing the edge from the subgraph will change the prediction to the other class"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Explainable Fraud Detection with GNNExplainer and Shapley Values" (2025-12-09). https://arxiv.org/abs/2509.12262
