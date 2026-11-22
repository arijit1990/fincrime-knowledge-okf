---
type: Source Digest
title: 'LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering - part 3 of 3 (pp. 5-9)'
description: 'Verified paraphrased digest, pp. 5-9: 4.2 Classification results; 4.3 Transaction visualization; 4.4 Customer visualization; and 3 more sections'
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
part: 3
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
digest_points: 43
---

# LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 5-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2.1 Hyperparameters.

- **descriptive / method**: Hyperparameters were selected with the Tree-structured Parzen Estimator algorithm, using validation loss as the success metric, with 20 different hyperparameter configurations trained for each model. (p. 5)[^original]  
  <sub>anchor: "Hyperparameters are selected through the Tree-structured Parzen Estimator (TPE) [1] algorithm using the validation loss as the metric of success"</sub>
- **descriptive / method**: The MLP baseline was set to 5 layers with dimensions 128, 64, 32, 16 and 1, with a dropout of 0.1. (p. 5)[^original]  
  <sub>anchor: "The hyperparameters were finally set as 5 layers with dimensions [128 _,_ 64 _,_ 32 _,_ 16 _,_ 1] and a dropout [21] of 0 _._ 1 for the MLP baseline"</sub>
- **descriptive / method**: The LightGBM baseline used a maximum of 400 leaves with a minimum of 150 samples per leaf. (p. 5)[^original]  
  <sub>anchor: "400 maximum leaves with 150 minimum samples per leaf for the LightGBM baseline"</sub>
- **descriptive / method**: The GAT variant has 3 layers with a hidden size of 32 and 4 attention heads. (p. 5)[^original]  
  <sub>anchor: "the _𝐺𝐴𝑇_ variant has 3 layers with a hidden size of 32 and 4 attention heads"</sub>
- **descriptive / method**: The GraphSAGE variant uses the mean aggregator with 3 layers of dimension 256 and a skip connection on the source node. (p. 5)[^original]  
  <sub>anchor: "we use the mean aggregator variant [5] with 3 layers with dimension of 256, together with a skip connection on the source node"</sub>
- **descriptive / method**: The GIN variant uses the GIN-0 form, with a simple 2-layer MLP per GNN layer. (p. 5)[^original]  
  <sub>anchor: "we use the GIN-0 variant [27] comprised of a simple 2-layer MLP per GNN layer"</sub>
- **descriptive / method**: The DGI baseline uses the GAT variant as its encoder. (p. 5)[^original]  
  <sub>anchor: "For the DGI baseline, we use the GAT variant described above as the encoder"</sub>
- **descriptive / method**: All neural network baselines apply the ReLU activation and batch normalization in every hidden layer. (p. 5)[^original]  
  <sub>anchor: "the ReLU activation function together with batch normalization [7] is applied in every hidden layer"</sub>
- **descriptive / method**: Training of the GNN-based models used the Adam optimizer with a learning rate of 0.001. (p. 5)[^original]  
  <sub>anchor: "For training, we use the Adam optimizer [10] with a learning rate of"</sub>
- **descriptive / method**: Early stopping with a patience threshold of 6 epochs was applied in all baselines, stopping training if validation loss does not improve for 6 epochs. (p. 6)[^original]  
  <sub>anchor: "early stopping is applied with a patience threshold of 6, i.e., we stop training if the validation loss does not improve after 6 epochs"</sub>

## 4.2 Classification results

- **descriptive / finding or result**: Table 1 reports ROC AUC and average precision on the test data; raw features are already informative, with competitive MLP and LightGBM results. (p. 6)[^original]  
  <sub>anchor: "We note that the raw features are already quite informative, as can be seen by the competitive results achieved with the MLP and LightGBM baselines"</sub>
- **descriptive / finding or result**: All graph-based baselines outperformed the non-graph baselines, showing the value of structural information from the graph. (p. 6)[^original]  
  <sub>anchor: "all graph-based baselines achieved superior performance, showcasing the importance of leveraging the structural information provided by the underlying graph"</sub>
- **descriptive / finding or result**: Jointly training encoder and decoder on link prediction gave better results than training the encoder with the DGI objective, with differences of 8.95 p.p. AUC and 11.86 p.p. AP compared with LaundroGraph GAT. (p. 6)[^original]  
  <sub>anchor: "resulting in a difference of 8 _._ 95 and 11 _._ 86 p.p. of AUC and AP, respectively, compared with LaundroGraph _𝐺𝐴𝑇_"</sub>
- **descriptive / finding or result**: The DGI objective still produced strong results, showing its ability to create informative node representations decoupled from any specific task. (p. 6)[^original]  
  <sub>anchor: "the strong results achieved by the DGI objective showcase the method’s ability to create informative node representations decoupled of any specific task"</sub>
- **descriptive / finding or result**: The LaundroGraph GAT variant achieved the overall best results, which the authors attribute to the extra expressiveness of attention mechanisms. (p. 6)[^original]  
  <sub>anchor: "The GAT variant of the proposed model (LaundroGraph _𝐺𝐴𝑇_ ) achieves the overall best results, as the additional expressiveness provided by the attention mechanisms seems to be beneficial"</sub>
- **descriptive / finding or result**: The GraphSAGE variant achieved the worst results of the three convolutional variants; the authors hypothesise this is due to lower expressiveness and dependence on the graph's homophilous nature. (p. 6)[^original]  
  <sub>anchor: "which we hypothesize to be due to the lack of expressiveness compared to the remaining three variants, and the dependence on the underlying homophilous nature of the graph"</sub>
- **descriptive / finding or result**: At very low FPRs, all graph-based variants trained on link prediction achieved recall above 80%, whereas MLP and DGI achieved 40% or below and LightGBM about 60%. (p. 6)[^original]  
  <sub>anchor: "all graph-based variants trained directly on the link prediction task already achieve a recall of _>_ 80%"</sub>
- **descriptive / finding or result**: As FPR increases, the DGI baseline approaches the other graph-based baselines, while MLP and LightGBM remain consistently inferior. (p. 6)[^original]  
  <sub>anchor: "As the FPR increases, the DGI baseline approaches the performance of the remaining graph-based baselines"</sub>

## 4.3 Transaction visualization

- **descriptive / method**: UMAP embeddings were plotted for transactions of 5 randomly sampled customers with more than 10 transactions, with outgoing and incoming transactions marked differently and coloured by customer or anomaly score. (p. 6)[^original]  
  <sub>anchor: "Figure 3 shows a plot of the UMAP [18] embeddings for the transactions of 5 different and randomly sampled customers with more than 10 transactions"</sub>

## 4.2.1 Hyperparameters.

- **descriptive / method**: The MLP baseline used a learning rate of 0.01 and the LightGBM baseline's learning rate is separately stated as 0.01. (p. 6)[^original]  
  <sub>anchor: "The learning rate for the LightGBM baseline is also set as 0 _._ 01."</sub>

## 4.2 Classification results

- **descriptive / finding or result**: The ROC curves show the trade-off between recall and specificity, and the AUC is described as a measure of separability, i.e. how well a model distinguishes between classes. (p. 6)[^original]  
  <sub>anchor: "as a measure of separability, representing how much a model is capable of distinguishing between classes"</sub>

## 4.3 Transaction visualization

- **descriptive / finding or result**: Transactions cluster naturally by customer, with multiple activity clusters per customer and some separability between customers. (p. 7)[^original]  
  <sub>anchor: "transactions are naturally clustered according to their customer, and that there are multiple clusters of activity for each customer"</sub>
- **expected / finding or result**: The authors state it is expected for a customer to have several activity clusters reflecting different counterpart types, with intracluster variability reflecting transaction properties. (p. 7)[^original]  
  <sub>anchor: "It is expected for a customer to have several clusters of activity representing the different types of counterparts interacted with"</sub>
- **descriptive / case example**: The purple customer's cluster represents several counterparts with very similar behaviour, almost all of which only received transactions from that customer in the training period. (p. 7)[^original]  
  <sub>anchor: "almost all counterparts only received transactions from the purple customer during the training period"</sub>
- **descriptive / finding or result**: Transactions farther from their non-anomalous clusters generally have higher anomaly scores, as seen with an anomalous cluster and scattered incoming orange-customer transactions. (p. 7)[^original]  
  <sub>anchor: "transactions farther away from their respective non-anomalous clusters (i.e., the "expected" behavior) usually have a higher anomaly score"</sub>
- **descriptive / context**: Aggregating a reviewed customer's transactions by meaningful categories is a key AML investigation component; on-demand cluster aggregation in latent space goes beyond simple aggregation schemes. (p. 7)[^original]  
  <sub>anchor: "aggregating the transactions for a customer under review according to meaningful categories is a key component of the AML investigation process"</sub>

## 4.4 Customer visualization

- **descriptive / method**: Customer UMAP embeddings for 6 customers over 3 snapshots of a rolling window were plotted with pairwise cosine similarity heatmaps; each snapshot covers 6 months of transactions, sliding 1 month forward. (p. 7)[^original]  
  <sub>anchor: "Each snapshot describes a graph comprised of 6 months worth of transactions, with each subsequent snapshot sliding the window 1 month into the future"</sub>
- **descriptive / method**: Customers were sampled half from those with a cosine similarity below 0.8 for at least one value and half from the remaining customers, and only customers with new activity were considered. (p. 7)[^original]  
  <sub>anchor: "we sample half of the customers from the pool of customers with one value of cosine similarity below 0 _._ 8"</sub>

## 4.3 Transaction visualization

- **descriptive / case example**: For the green customer, one outgoing transaction lay apart from the main cluster; the authors note that one might expect it to be anomalous, but the training-period history of frequent similar interactions between the two entities matters. (p. 7)[^original]  
  <sub>anchor: "At first glance, we may expect this transaction to be anomalous, however, we reiterate the importance of the history observed during the training period"</sub>

## 4.4 Customer visualization

- **descriptive / data or feature**: Figure 4 shows UMAP embeddings for 6 customers across 3 snapshots, with each customer providing 3 points, one per snapshot (18 points in total), connected by a dashed line of the same colour. (p. 7)[^original]  
  <sub>anchor: "each customer providing 3 points, one for each snapshot (18 points in total)"</sub>
- **descriptive / finding or result**: Stable customers show very high cosine similarity across snapshots, with subgraphs that remain largely similar, while divergent customers show shifts in embedding space. (p. 8)[^original]  
  <sub>anchor: "For the customers with stable behavior (i.e., customers with very high cosine similarity values)"</sub>
- **descriptive / finding or result**: A common cause of representation divergence is a new type (incoming or outgoing) of transaction performed for the first time, as with the orange customer. (p. 8)[^original]  
  <sub>anchor: "a common reason for divergence of representations is due to a new type (i.e., incoming or outgoing) of transaction being performed for the first time"</sub>
- **descriptive / finding or result**: Another cause of divergence is changes in counterparts and their neighbourhood structure, since messages carry information about the sender's neighbourhood, so a customer can diverge even with unchanged transaction counts. (p. 8)[^original]  
  <sub>anchor: "a customer can obtain different representations if the received messages describe very different neighborhoods"</sub>
- **descriptive / finding or result**: The effect of neighbourhood changes is diminished for high centrality nodes, so customers with more known behaviour have more stable representations. (p. 8)[^original]  
  <sub>anchor: "This is alleviated for high centrality nodes, as the contribution of each message on the final representation is diminished"</sub>
- **descriptive / method**: The customer representations used are from the last (third) layer of LaundroGraph GAT; using earlier layers prioritises different information, with more volatile representations at shallower depth. (p. 8)[^original]  
  <sub>anchor: "By using the representations at different depths of the network, different information can be prioritized"</sub>
- **descriptive / finding or result**: Layer one reflects only the source customer's transactions, layer two also considers counterparts, and three layers let the counterparts' transactions affect the source representation, giving more stable representations. (p. 8)[^original]  
  <sub>anchor: "Using the representations provided by the second layer additionally considers the counterparts interacted with"</sub>
- **descriptive / limitation**: If a counterpart's behaviour changes drastically, the source embedding reflects it, giving an illusion of behaviour divergence, as with the blue customer. (p. 8)[^original]  
  <sub>anchor: "giving an illusion of behavior divergence, as exemplified through the blue customer"</sub>

## 5 CONCLUSION

- **descriptive / finding or result**: LaundroGraph is a fully self-supervised approach using a novel customer-transaction bipartite graph with GNNs to produce representations used to score transaction anomalies. (p. 8)[^original]  
  <sub>anchor: "By leveraging a novel customer-transaction bipartite graph through GNNs, we are able to obtain representations that characterize each entity"</sub>
- **descriptive / finding or result**: The best method achieved an AUC of about 95% and AP of about 96%, improvements of 12.2 and 6.2 p.p. over the best non-graph baseline respectively. (p. 8)[^original]  
  <sub>anchor: "the best method achieving an AUC of ∼ 95% and AP of ∼ 96%, an improvement of 12 _._ 2 and 6 _._ 2 p.p. over the best non-graph baseline"</sub>
- **descriptive / finding or result**: For edge prediction, jointly training encoder and decoder achieved superior results compared with pre-training the encoder on a separate self-supervised objective. (p. 8)[^original]  
  <sub>anchor: "jointly training the encoder and decoder achieves superior results compared to pre-training the encoder on a separate self-supervised objective"</sub>

## 4.4 Customer visualization

- **permissive / method**: Divergence information can be shown to the analyst to accelerate customer contextualisation; if a customer with past false positives does not diverge from those periods, the current assessment is then expected to be a false positive too, giving a prior before any transaction is investigated. (p. 8)[^original]  
  <sub>anchor: "then it is expected that the current assessment will also be a false positive, introducing a prior on the analyst"</sub>

## 5 CONCLUSION

- **recommended / recommendation**: Future work can consider incorporating additional node types such as merchants and card transactions. (p. 9)[^original]  
  <sub>anchor: "A number of directions can be considered for future work, such as incorporating additional information in the form of different types of nodes"</sub>
- **descriptive / recommendation**: A sequential model connecting graph snapshots over time is proposed as an interesting future direction to exploit the temporal component and capture evolving customer behaviour. (p. 9)[^original]  
  <sub>anchor: "A particularly interesting direction of research would be to further exploit the temporal component present in the data through a sequential model"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: arXiv, "LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering" (2022-10-25). https://arxiv.org/abs/2210.14360
