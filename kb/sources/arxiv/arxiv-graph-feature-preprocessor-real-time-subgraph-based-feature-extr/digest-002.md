---
type: Source Digest
title: 'Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection - part 2 of 5 (pp. 3-6)'
description: 'Verified paraphrased digest, pp. 3-6: 2.2 Graph Pattern Mining; 2.3 Feature Encoding; 3 Experimental setup'
resource: https://arxiv.org/abs/2402.08593
tags:
- academic_finding
- data_features
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-graph-feature-preprocessor-real-time-subgraph-based-feature-extr
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-02-13'
legal_status: unknown
part: 2
parts_total: 5
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
  resource: https://arxiv.org/abs/2402.08593
  title: 'Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection'
  author: org:arxiv
  last_modified: '2024-02-13T00:00:00Z'
digest_points: 74
---

# Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 3-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 2.2 Graph Pattern Mining

- **descriptive / context**: The graph pattern mining component produces graph-based features for edges forwarded to the library through the transform function, and supports two types: graph-pattern-based features and vertex-statistics-based features. (p. 3)[^original]  
  <sub>anchor: "Two types of graph-based features are supported"</sub>
- **descriptive / definition**: The library extracts six graph patterns: fan-in, fan-out, scatter-gather, gather-scatter, simple cycle and temporal cycle. (p. 3)[^original]  
  <sub>anchor: "Our library extracts the following graph patterns: fan-in, fan-out, scatter-gather, gather-scatter, simple cycle, and temporal cycle."</sub>
- **descriptive / definition**: A fan-in or fan-out pattern is defined by a vertex and all of its incoming or outgoing edges, respectively. (p. 3)[^original]  
  <sub>anchor: "Fan-in and fan-out patterns refer to patterns defined by a vertex"</sub>
- **descriptive / definition**: A gather-scatter pattern combines the fan-in pattern of a vertex v with the fan-out pattern of the same vertex v. (p. 3)[^original]  
  <sub>anchor: "combines a fan-in pattern of the vertex"</sub>
- **descriptive / definition**: A scatter-gather pattern arises when the fan-out of vertex v and the fan-in of vertex u connect v and u respectively to the same set of intermediate vertices. (p. 3)[^original]  
  <sub>anchor: "to the same set of intermediate vertices [72]"</sub>
- **descriptive / definition**: A simple cycle is a path from a vertex back to itself without repeated vertices except for the first and last vertex. (p. 3)[^original]  
  <sub>anchor: "A simple cycle is a path from vertex"</sub>
- **descriptive / definition**: A temporal cycle is a simple cycle whose edges are ordered in time. (p. 3)[^original]  
  <sub>anchor: "Finally, a temporal cycle is a simple cycle with edges ordered in time."</sub>
- **descriptive / method**: To compute graph-pattern-based features in a streaming manner, the library enumerates new patterns formed after inserting the input batch of edges into the graph. (p. 4)[^original]  
  <sub>anchor: "enumerates new patterns that are formed after inserting the input batch of edges"</sub>
- **descriptive / definition**: A gather-scatter pattern is detected implicitly when the fan-in and fan-out of a vertex are each at least two. (p. 4)[^original]  
  <sub>anchor: "is detected implicitly if the fan-in and fan-out"</sub>
- **descriptive / method**: Simple and temporal cycles are enumerated in a streaming manner using fine-grained parallel algorithms introduced by Blanuša et al. [6, 7]. (p. 4)[^original]  
  <sub>anchor: "we use fine-grained parallel algorithms introduced in Blanuša et al."</sub>
- **descriptive / finding or result**: The fine-grained algorithms can process transactions in small batches with high throughput. (p. 4)[^original]  
  <sub>anchor: "The benefit of these algorithms is that they can process transactions in small batches with high throughput"</sub>
- **descriptive / finding or result**: Per the cited work, the coarse-grained parallel approach may give a suboptimal solution because of workload imbalance across threads. (p. 4)[^original]  
  <sub>anchor: "using the coarse-grained approach might result in a suboptimal solution"</sub>
- **descriptive / method**: Fine-grained algorithms run the recursive cycle search from a single edge using several threads, increasing parallelism. (p. 4)[^original]  
  <sub>anchor: "fine-grained enumeration algorithms are able to execute the recursive cycle search from a single edge"</sub>
- **descriptive / finding or result**: Even when the input batch contains a single transaction, the library can parallelise the search for cycles. (p. 4)[^original]  
  <sub>anchor: "even if the input batch contains one transaction, our library would be able to parallelise the search for cycles"</sub>
- **descriptive / method**: The scatter-gather algorithm processes each edge of the batch by searching for all scatter-gather patterns that include that edge, in two phases. (p. 4)[^original]  
  <sub>anchor: "The first and second phase of this algorithm search for scatter-gather patterns"</sub>
- **descriptive / method**: In the first phase, the outgoing neighbours of u and v are determined, and for each outgoing neighbour w of v the incoming neighbours of w are searched. (p. 4)[^original]  
  <sub>anchor: "we first determine the outgoing neighbours of"</sub>
- **descriptive / method**: The algorithm intersects the outgoing neighbours of u with the incoming neighbours of w to find the intermediate vertices of a scatter-gather pattern. (p. 4)[^original]  
  <sub>anchor: "we perform a set intersection between"</sub>
- **descriptive / method**: The second phase of the scatter-gather algorithm is analogous to the first and its description is omitted for brevity. (p. 4)[^original]  
  <sub>anchor: "is analogous to the first phase, and we omit its description for brevity"</sub>
- **permissive / method**: Pattern search time can be reduced by imposing time-window constraints, with a window parameter specified for each graph pattern. (p. 4)[^original]  
  <sub>anchor: "Apart from parallelisation, another method to reduce the time required to find graph patterns is to impose time-window constraints"</sub>
- **descriptive / definition**: Under a time window, the library searches only for patterns whose edges have timestamps at or after t_now minus the window parameter, where t_now is the largest timestamp in the in-memory graph. (p. 4)[^original]  
  <sub>anchor: "searches only for patterns whose edges have timestamps greater than or equal to"</sub>
- **permissive / method**: The search for simple cycles can be constrained by limiting their maximal length. (p. 4)[^original]  
  <sub>anchor: "the search for simple cycles can be constrained by limiting their maximal length"</sub>
- **descriptive / method**: The library maintains second, third and fourth central moments for each vertex and each basic feature used for account statistics. (p. 4)[^original]  
  <sub>anchor: "our library maintains second, third, and fourth central moments for each vertex"</sub>
- **descriptive / method**: After inserting or removing an edge, the central moments of its two endpoints are updated incrementally, and these are used to compute sum, mean, variance, skew and kurtosis. (p. 4)[^original]  
  <sub>anchor: "used to compute the following statistical features: sum, mean, variance, skew, and kurtosis"</sub>
- **descriptive / method**: The scatter-gather algorithm can be parallelised in a fine-grained manner by parallelising its loops. (p. 5)[^original]  
  <sub>anchor: "this algorithm can be parallelised in a fine-grained manner by parallelising its loops"</sub>
- **descriptive / definition**: The library supports eight statistical properties for vertex-statistics-based features: sum, mean, minimum, maximum, median, variance, skew and kurtosis. (p. 5)[^original]  
  <sub>anchor: "The statistical properties currently supported by our library are: sum, mean, minimum, maximum, median, variance, skew, and kurtosis"</sub>
- **descriptive / data or feature**: Vertex statistics are computed over the outgoing and incoming edges of a vertex using a selected basic feature, which extends the feature space significantly when combined. (p. 5)[^original]  
  <sub>anchor: "Combining different statistical feature types with different user-specified basic features in this way extends the feature space significantly"</sub>
- **descriptive / data or feature**: Using Amount as the basic feature, the statistical features include the average and total amount an account received or sent. (p. 5)[^original]  
  <sub>anchor: "the statistical features include the average and total amount of money an account received or sent"</sub>
- **descriptive / finding or result**: Each of sum, mean, variance, skew and kurtosis can be computed in O(1) time. (p. 5)[^original]  
  <sub>anchor: "the computation of each aforementioned statistical feature can be performed in"</sub>

## 2.3 Feature Encoding

- **descriptive / data or feature**: Each row of the output feature table holds the feature vector of a single transaction, combining basic, graph-pattern-based and source and destination account features. (p. 5)[^original]  
  <sub>anchor: "Each row of the output feature table stores the feature vector of a single transaction"</sub>
- **descriptive / definition**: Account features consist of vertex-statistics-based features and single-hop fan-in and fan-out pattern features, which count the accounts connected to the account in those patterns. (p. 5)[^original]  
  <sub>anchor: "The account features consist of vertex-statistics-based features and features based on fan-in and fan-out patterns"</sub>
- **descriptive / data or feature**: Graph-pattern-based transaction features use multi-hop subgraph patterns: scatter-gather, hop-constrained simple cycles and temporal cycles, reporting counts per transaction by pattern size. (p. 5)[^original]  
  <sub>anchor: "Graph-pattern-based transaction features are computed using multi-hop subgraph patterns"</sub>
- **descriptive / case example**: In the Figure 6 example, the first transaction participates in 4 scatter-gather patterns with 3 intermediate vertices and in 2 temporal cycles with 30 or more edges. (p. 5)[^original]  
  <sub>anchor: "the first transaction participates in 4 scatter-gather patterns with 3 intermediate vertices"</sub>
- **descriptive / finding or result**: Computing multi-hop patterns as transaction features, rather than account features, provides more compact feature vectors. (p. 5)[^original]  
  <sub>anchor: "computing them as transaction features provides more compact feature vectors"</sub>

## 3 Experimental setup

- **descriptive / data or feature**: The AML datasets are publicly available synthetic datasets produced by the AMLworld generator, with transactions labelled licit or illicit, in high illicit rate (AML HI) and low illicit rate (AML LI) variants. (p. 5)[^original]  
  <sub>anchor: "The AML datasets are publicly available synthetic AML datasets produced by the"</sub>
- **descriptive / data or feature**: Table 1 reports for the ETH Phishing dataset 2.9 M nodes, 13 M edges, 0.278% illicit rate and a 1261-day time span. (p. 5)[^original]  
  <sub>anchor: "Table 1 presents the datasets used in the evaluation"</sub>
- **descriptive / data or feature**: The ETH Phishing dataset is a real-world Ethereum dataset, with 1,165 accounts labelled as phishing. (p. 5)[^original]  
  <sub>anchor: "we use the ETH Phishing dataset, which is a real-world Ethereum dataset"</sub>
- **descriptive / method**: For ETH Phishing, a transaction is labelled phishing if its destination account is labelled phishing. (p. 5)[^original]  
  <sub>anchor: "we label a transaction of this dataset as phishing if its destination account is labelled as phishing"</sub>
- **descriptive / finding or result**: As a result of this labelling, 0.278% of Ethereum transactions are labelled phishing. (p. 5)[^original]  
  <sub>anchor: "of Ethereum transactions are labelled as phishing"</sub>
- **descriptive / data or feature**: Table 2 gives successive halving configurations for LightGBM and XGBoost tuning: x0 is 1000 for AML Small, 100 for AML Medium, 16 for AML Large and 100 for ETH; eta is 2 throughout; r0 is 0.1, 0.2, 0.2 and 0.1 respectively. (p. 5)[^original]  
  <sub>anchor: "Successive halving configurations used for hyperparameter tuning of both LightGBM and XGBoost models"</sub>
- **descriptive / data or feature**: Table 3 gives the LightGBM parameter ranges (num_round 10 to 1000, num_leaves 1 to 16384, learning_rate 10 to the power -2.5 to -1, lambda_l2 10 to the power -2 to 2, scale_pos_weight 1 to 10, lambda_l1 10 to the power 0.01 to 0.5) and XGBoost ranges (num_round 10 to 1000, max_depth 1 to 15, learning_rate 10 to the power -2.5 to -1, lambda 10 to the power -2 to 2, scale_pos_weight 1 to 10, colsample_bytree 0.5 to 1.0, subsample 0.5 to 1.0), with early stopping after 20 rounds. (p. 5)[^original]  
  <sub>anchor: "Model parameter ranges used at tuning time"</sub>
- **descriptive / context**: The baselines are LightGBM version 3.1.1 and XGBoost version 1.7.5, widely used machine learning models for tabular data. (p. 5)[^original]  
  <sub>anchor: "We use LightGBM (version 3.1.1) [43] and XGBoost (version 1.7.5) [16]"</sub>
- **descriptive / context**: The LightGBM and XGBoost baselines are trained only on basic features, without features from the Graph Feature Preprocessor. (p. 5)[^original]  
  <sub>anchor: "trained exclusively using basic features, without incorporating features generated by our Graph Feature Preprocessor"</sub>
- **descriptive / method**: Baseline hyperparameters are tuned with a successive halving approach. (p. 5)[^original]  
  <sub>anchor: "we employ a successive halving model tuning approach [40]"</sub>
- **descriptive / context**: Additional GNN baselines are Graph Isomorphism Network (GIN), GIN with edge updates (GIN+EU) and Principal Neighbourhood Aggregation (PNA). (p. 5)[^original]  
  <sub>anchor: "As additional baselines, we use the following graph neural networks"</sub>
- **descriptive / context**: The GIN+EU baseline is similar to LaundroGraph, a GNN designed specifically for anti-money laundering. (p. 5)[^original]  
  <sub>anchor: "GIN+EU baseline is similar to LaundroGraph [12]"</sub>
- **descriptive / finding or result**: The accuracy results for the GNN baselines on the AML datasets are taken from Altman et al. (p. 5)[^original]  
  <sub>anchor: "The accuracy results for these GNNs on the AML datasets are obtained from Altman et al. [1]"</sub>
- **descriptive / method**: All baselines and the proposed pipeline are trained without source and destination account IDs, to prevent models memorising account IDs to identify laundering transactions. (p. 5)[^original]  
  <sub>anchor: "This prevents the models from identifying money laundering transactions based on the memorisation of account IDs"</sub>
- **descriptive / method**: For AML datasets, GFP uses a six-hour time window for scatter-gather patterns and a one-day window for the other graph-based features. (p. 5)[^original]  
  <sub>anchor: "using a time window of six hours for scatter-gather patterns and a time window of one day"</sub>
- **descriptive / method**: For AML datasets, a cycle-length constraint of 10 is specified for simple cycle enumeration. (p. 5)[^original]  
  <sub>anchor: "We specify a cycle-length constraint of 10 for simple cycle enumeration"</sub>
- **descriptive / method**: For AML datasets, vertex-statistics-based features are generated from the Amount and Timestamp fields of the basic transaction features. (p. 5)[^original]  
  <sub>anchor: "fields of the basic transaction features to generate the vertex-statistics-based features"</sub>
- **descriptive / method**: For ETH Phishing, feature extraction uses a 20-day time window for all graph-based features. (p. 5)[^original]  
  <sub>anchor: "Feature extraction from the ETH Phishing dataset is performed using a 20-day time window"</sub>
- **descriptive / method**: For ETH Phishing, temporal cycle generation is disabled and simple cycle enumeration uses a hop constraint of 5. (p. 5)[^original]  
  <sub>anchor: "we disable the generation of temporal cycles and specify a hop constraint of 5"</sub>
- **descriptive / method**: For ETH Phishing, account statistics are generated from the Amount, Timestamp and Block Nr. fields of the basic transaction features. (p. 5)[^original]  
  <sub>anchor: "fields of the basic transaction features to generate the account statistics"</sub>
- **descriptive / limitation**: The GFP parameters were chosen after careful exploration aimed at the best trade-off between GFP throughput and the accuracy of the scoring ML models. (p. 5)[^original]  
  <sub>anchor: "We selected these parameters after some careful exploration aimed at finding the best trade-offs"</sub>

## 2.2 Graph Pattern Mining

- **descriptive / finding or result**: Minimum, maximum and median statistics are computed by iterating through a vertex's incident edges, taking O(Δ) time per statistic, where Δ is the maximum degree of a vertex in the graph. (p. 5)[^original]  
  <sub>anchor: "are simply computed by iterating through the incident edges of a vertex"</sub>

## 3 Experimental setup

- **descriptive / data or feature**: Table 1 lists each dataset with its number of nodes, number of edges, illicit rate and time span, covering the AML HI and AML LI Small, Medium and Large variants and the ETH Phishing dataset. (p. 5)[^original]  
  <sub>anchor: "Table 1 presents the datasets used in the evaluation"</sub>
- **descriptive / data or feature**: The ETH Phishing dataset is a real-world Ethereum dataset, and Table 1 gives it about 2.9 M nodes, 13 M edges, a 0.278% illicit rate and a 1261-day time span. (p. 5)[^original]  
  <sub>anchor: "the ETH Phishing dataset, which is a real-world Ethereum dataset"</sub>
- **descriptive / method**: In training, transactions are ordered by ascending timestamp and split into train, validation and test sets, with the train set holding the lowest timestamps. (p. 6)[^original]  
  <sub>anchor: "ordered in ascending order of their timestamps and are split into train, validation, and test sets"</sub>
- **descriptive / method**: The split places the transactions with the lowest timestamps in the train set and the highest in the test set. (p. 6)[^original]  
  <sub>anchor: "the transactions from the train set have the lowest timestamps"</sub>
- **descriptive / method**: To prevent information leakage, the training set is processed by GFP before the validation set. (p. 6)[^original]  
  <sub>anchor: "the training set is processed before the validation set"</sub>
- **descriptive / method**: Graph-based features for training transactions are computed on a graph built only from training transactions, so no validation information is used. (p. 6)[^original]  
  <sub>anchor: "graph-based features for the transactions of the train set are computed on the graph created using only those transactions"</sub>
- **descriptive / method**: The enriched train and validation sets are used to train the gradient boosting models. (p. 6)[^original]  
  <sub>anchor: "the train and validation sets with enriched features are then used to train the gradient boosting models"</sub>
- **descriptive / method**: Successive halving starts by randomly sampling x0 parameter combinations using a fraction r0 of the train set. (p. 6)[^original]  
  <sub>anchor: "This approach starts by randomly sampling"</sub>
- **descriptive / method**: At each round the best configurations are kept and the training fraction is multiplied by eta, continuing until the evaluation fraction reaches 1. (p. 6)[^original]  
  <sub>anchor: "This process continues until the fraction of the training set used for evaluation reaches 1"</sub>
- **descriptive / method**: At inference, the trained model is loaded and GFP is initialised with past financial transactions to create the initial in-memory graph. (p. 6)[^original]  
  <sub>anchor: "we initialise GFP by loading past financial transactions"</sub>
- **descriptive / method**: At inference, test transactions are grouped into batches and forwarded to GFP, which updates the dynamic graph and enriches the transactions with graph features. (p. 6)[^original]  
  <sub>anchor: "the transactions from the test set are grouped into batches and forwarded to GFP"</sub>
- **descriptive / method**: Enriched test transactions are sent to the pre-trained model to detect transactions associated with financial crime. (p. 6)[^original]  
  <sub>anchor: "the enriched test transactions are sent to the pre-trained machine learning model"</sub>
- **descriptive / method**: For AML datasets, 60% of transactions with the smallest timestamps form the training set. (p. 6)[^original]  
  <sub>anchor: "60% of transactions with the smallest timestamps is selected as a training set"</sub>
- **descriptive / method**: For AML datasets, the next 20% of transactions by smallest timestamp, excluding training transactions, form the validation set, and the rest form the test set. (p. 6)[^original]  
  <sub>anchor: "the next 20% transactions with the smallest timestamps excluding the ones from the training set"</sub>
- **descriptive / method**: For the ETH dataset, an account's timestamp is defined as the minimum timestamp among the transactions involving that account. (p. 6)[^original]  
  <sub>anchor: "we define the timestamp of an account as the minimum timestamp among the transactions that involve this account"</sub>
- **descriptive / method**: For the ETH dataset, 65% of accounts with the smallest timestamps exist only in the training set. (p. 6)[^original]  
  <sub>anchor: "65% of the accounts with the smallest timestamp exist only in the training set"</sub>
- **descriptive / method**: For the ETH dataset, the next 15% of accounts exist only in the validation set, and the rest are in the test set. (p. 6)[^original]  
  <sub>anchor: "the next 15% of the accounts exist only in the validation dataset"</sub>
- **descriptive / method**: The train and validation sets tune the models via successive halving, while the test set is used for final evaluation. (p. 6)[^original]  
  <sub>anchor: "the test set is used for the final evaluation of the model"</sub>
- **descriptive / finding or result**: The authors state that splitting the datasets in this way prevents data leakage in their experiments. (p. 6)[^original]  
  <sub>anchor: "Splitting the datasets in the aforementioned way prevents data leakage in our experiments"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection" (2024-02-13). https://arxiv.org/abs/2402.08593
