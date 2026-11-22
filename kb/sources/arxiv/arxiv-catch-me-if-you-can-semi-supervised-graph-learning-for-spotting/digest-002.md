---
type: Source Digest
title: 'Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering - part 2 of 3 (pp. 6-10)'
description: 'Verified paraphrased digest, pp. 6-10: Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering > 4 EXPERIMENTS; Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering > 5 CONCLUSION AND OUTLOOK; Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering > ACKNOWLEDGMENT; and 1 more sections'
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
part: 2
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
digest_points: 67
---

# Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-10) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2 Experiment settings

- **descriptive / method**: The authors used the open source StellarGraph library to compute node embeddings, with BiasedRandomWalk and Word2Vec from the gensim library. (p. 6)[^original]  
  <sub>anchor: "We use open source StellarGraph17 library to compute node embeddings"</sub>
- **descriptive / method**: The DGT model was trained using its PyTorch implementation. (p. 6)[^original]  
  <sub>anchor: "The DGT model is trained based on its PyTorch implementation"</sub>
- **descriptive / method**: The RF and ERT classifiers are based on scikit-learn ensemble methods. (p. 6)[^original]  
  <sub>anchor: "The RF and ERT models are based on scikit-learn"</sub>
- **descriptive / method**: The GBT classifier was trained as an XGBoost implementation. (p. 6)[^original]  
  <sub>anchor: "As of GBT, we train its XGBoost implementation"</sub>
- **descriptive / method**: RDF2Vec was trained with a skip-gram model using a window size of 5, graph walk depth 5 and 500 walks per entity. (p. 6)[^original]  
  <sub>anchor: "While RDF2Vec was trained using a skip-gram model by setting a window size of 5"</sub>
- **descriptive / method**: To study the effect of embedding dimension, the dimension d was selected for each embedding model from 32, 64, 128, 256 and 300. (p. 6)[^original]  
  <sub>anchor: "for each embedding model, the value of"</sub>
- **descriptive / method**: For the DGT model, the number of layers L was selected from 1 to 5. (p. 6)[^original]  
  <sub>anchor: "As for the DGT model, number of layers"</sub>
- **descriptive / data or feature**: Footnote 16 lists max/min standard deviation and correlation coefficients of neighbour transactions with respect to number of inputs/outputs and transaction fee, among others. (p. 6)[^original]  
  <sub>anchor: "Max/min standard deviation and correlation coefficients of neighbour transactions"</sub>

## 4.3 Analysis of node classifications

- **descriptive / finding or result**: Table 1 reports for AMLSim the AUPR, F1-score and MCC of pipeline methods: Node2Vec with ERT 0.746, 0.753, 0.643; with RF 0.751, 0.760, 0.651; with XGBoost 0.806, 0.801, 0.752. (p. 6)[^original]  
  <sub>anchor: "TABLE 1: Pipeline methods on AMLSim"</sub>
- **descriptive / finding or result**: Table 1 reports for AMLSim: Attri2Vec with ERT 0.762, 0.783, 0.651; with RF 0.775, 0.782, 0.669; with XGBoost 0.815, 0.810, 0.7692 (value as printed). (p. 6)[^original]  
  <sub>anchor: "TABLE 1: Pipeline methods on AMLSim"</sub>
- **descriptive / finding or result**: Table 1 reports for AMLSim: GraphSAGE with ERT 0.786, 0.801, 0.679; with RF 0.802, 0.804, 0.675; with XGBoost 0.815, 0.816, 0.701. (p. 6)[^original]  
  <sub>anchor: "TABLE 1: Pipeline methods on AMLSim"</sub>
- **descriptive / finding or result**: Table 1 reports for AMLSim: DGT with ERT 0.797, 0.803, 0.671; with RF 0.813, 0.825, 0.693; with XGBoost 0.833, 0.832, 0.715. (p. 6)[^original]  
  <sub>anchor: "TABLE 1: Pipeline methods on AMLSim"</sub>

## 4.2 Experiment settings

- **descriptive / data or feature**: Footnote 15 lists the timestep, numbers of inputs and outputs, transaction fee, output volume and aggregated figures (such as average BTC received or spent per input or output) as items in the footnote, without stating they are node features. (p. 6)[^original]  
  <sub>anchor: "Timestep, number of inputs/outputs, transaction fee, output volume and aggregated figures"</sub>
- **descriptive / method**: RDF2Vec was trained with a skip-gram model, a window size of 5, graph walks at depth 5 and 500 walks per entity. (p. 6)[^original]  
  <sub>anchor: "While RDF2Vec was trained using a skip-gram model by setting a window size of 5"</sub>

## 4.3 Analysis of node classifications

- **descriptive / finding or result**: Table 1 reports pipeline methods on AMLSim: with XGBoost, Node2Vec achieves AUPR 0.806, F1 0.801 and MCC 0.752, while DGT with XGBoost achieves AUPR 0.833, F1 0.832 and MCC 0.715 in the MCC column as printed. (p. 6)[^original]  
  <sub>anchor: "TABLE 1: Pipeline methods on AMLSim"</sub>

## 4.2 Experiment settings

- **descriptive / method**: The pipeline approach trains Node2vec, Attri2Vec, GraphSAGE and DGT embeddings first and then trains classifiers ERT, GBT and RF on them. (p. 7)[^original]  
  <sub>anchor: "Node2vec, Attri2Vec, GraphSAGE, and DGT models are first trained to generate node embeddings"</sub>
- **descriptive / method**: The end-to-end approach uses GCN with batched training, FastGCN which reduces training cost through neighbourhood sampling, and EvolveGCN which evolves GCN parameters to capture dynamism. (p. 7)[^original]  
  <sub>anchor: "we train GCN [4] with batched training, FastGCN [15] that reduces the training cost through neighbourhood sampling"</sub>
- **descriptive / method**: Both end-to-end models were configured with 128 hidden units and trained with AdaGrad using varying learning rates and batch sizes. (p. 7)[^original]  
  <sub>anchor: "Both models were configured to have 128 hidden units and trained with AdaGrad"</sub>
- **descriptive / method**: Because classes are imbalanced in both datasets, GCN, FastGCN and EvolveGCN were trained with a weighted cross-entropy loss giving more weight to the minority illicit (SARs) class. (p. 7)[^original]  
  <sub>anchor: "since classes are imbalanced in the case of both datasets"</sub>
- **descriptive / method**: In each experiment, 10 to 20% of the nodes are removed and the embedding models are trained on the reduced subgraph. (p. 7)[^original]  
  <sub>anchor: "we remove 10 to 20% of the nodes, followed by training the GE models on the reduced subgraph"</sub>
- **descriptive / method**: At inference, embeddings of the removed nodes are generated with the trained model and used to predict labels of the held-out nodes after they are re-inserted into the network. (p. 7)[^original]  
  <sub>anchor: "we generate the embeddings of the removed nodes using the trained GE model"</sub>
- **descriptive / method**: Hyperparameters were selected via random search and 5-fold cross-validation on 80% of the data used for training and validation. (p. 7)[^original]  
  <sub>anchor: "the best hyperparameters were produced via random search and 5-fold cross-validation"</sub>
- **descriptive / method**: Performance was measured with AUPR, MCC, AUC and F1-score. (p. 7)[^original]  
  <sub>anchor: "We used the area under the precision-recall curve (AUPR)"</sub>

## 4.3 Analysis of node classifications

- **descriptive / finding or result**: All classifiers performed worse when trained on embeddings from Node2Vec and Attri2Vec, according to the ROC curves. (p. 7)[^original]  
  <sub>anchor: "all the classifiers perform worse when trained on embeddings generated by the Node2Vec and Attri2Vec models"</sub>
- **descriptive / finding or result**: The performance of GraphSAGE+XGBoost is comparable to DGT+XGBoost. (p. 7)[^original]  
  <sub>anchor: "The performance of GraphSAGE+XGBoost is comparable to DGT+XGBoost."</sub>
- **descriptive / finding or result**: The end-to-end methods generally outperformed each pipeline method. (p. 7)[^original]  
  <sub>anchor: "the end-to-end methods outperformed each and every pipeline methods"</sub>
- **descriptive / finding or result**: EvolveGCN outperforms all pipeline methods that use tree-ensemble classifiers, which the authors take to indicate the effectiveness of end-to-end methods. (p. 7)[^original]  
  <sub>anchor: "EvolveGCN outperforms all the pipeline methods with tree-ensemble classifiers"</sub>
- **descriptive / finding or result**: EvolveGCN consistently outperforms Skip-GCN and FastGCN, although the improvement is not very substantial on either dataset. (p. 7)[^original]  
  <sub>anchor: "EvolveGCN consistently outperforms both Skip-GCN and FastGCN, although the improvement is not very substantial for both datasets"</sub>
- **descriptive / finding or result**: Table 3 reports for Elliptic: DGT with ERT AUPR 0.885, F1 0.854, MCC 0.726; with RF 0.907, 0.897, 0.753; with XGBoost 0.918, 0.915, 0.792. (p. 7)[^original]  
  <sub>anchor: "TABLE 3: Pipeline methods on Elliptic"</sub>
- **descriptive / finding or result**: Table 3 reports for Elliptic: GraphSAGE with ERT 0.874, 0.865, 0.743; with RF 0.891, 0.882, 0.778; with XGBoost 0.912, 0.905, 0.782. (p. 7)[^original]  
  <sub>anchor: "TABLE 3: Pipeline methods on Elliptic"</sub>
- **descriptive / finding or result**: Table 3 reports for Elliptic: Attri2Vec with ERT 0.815, 0.824, 0.653; with RF 0.821, 0.832, 0.665; with XGBoost 0.902, 0.894, 0.673. (p. 7)[^original]  
  <sub>anchor: "TABLE 3: Pipeline methods on Elliptic"</sub>
- **descriptive / finding or result**: Table 3 reports for Elliptic: Node2Vec with ERT 0.792, 0.805, 0.617; with RF 0.806, 0.817, 0.622; with XGBoost 0.885, 0.874, 0.662. (p. 7)[^original]  
  <sub>anchor: "TABLE 3: Pipeline methods on Elliptic"</sub>

## 4.4 Effects of temporal information

- **descriptive / finding or result**: On AMLSim, XGBoost mostly benefited from the temporal information captured by the DGT embedding model, and this pipeline outperformed other pipeline methods. (p. 7)[^original]  
  <sub>anchor: "the XGBoost model mostly benefited from the temporal information captured by the DGT embedding model"</sub>
- **descriptive / finding or result**: On the Elliptic dataset, DGT+XGBoost outperformed GraphSAGE+XGBoost. (p. 7)[^original]  
  <sub>anchor: "This is also the case for the Elliptic dataset, where same method outperformed GraphSAGE+XGboost"</sub>
- **descriptive / context**: The authors suggest the dynamic models are more effective, possibly because input features are already informative and GNNs or transformers extract more abstract features that distinguish licit and illicit nodes. (p. 7)[^original]  
  <sub>anchor: "A potential reason could be that the input features are already quite informative"</sub>

## 4.5 Effects of nodes embeddings + feature space

- **descriptive / context**: A cited recent approach reported that aggregated information may lead to higher F1 scores for anomaly-detection-like tasks, which motivated the authors to extend the feature space with node embeddings. (p. 7)[^original]  
  <sub>anchor: "A recent approach [29] showed that aggregated information may lead higher F1 scores for anomaly detection like tasks"</sub>
- **descriptive / finding or result**: Combining node embeddings with features slightly improves node classification accuracy, making pipeline results somewhat comparable to end-to-end methods. (p. 7)[^original]  
  <sub>anchor: "the node classification accuracy is slightly improves, by taking the global graph structure"</sub>
- **descriptive / finding or result**: The micro averages for all pipeline approaches are higher than 0.93. (p. 7)[^original]  
  <sub>anchor: "The micro averages for all pipeline approach is higher than 0.93."</sub>
- **descriptive / limitation**: Micro averages are not very informative for highly imbalanced datasets, so the authors plotted minority-class F1 scores for both datasets. (p. 7)[^original]  
  <sub>anchor: "However, they are not very informative for highly imbalanced datasets."</sub>

## 5 CONCLUSION AND OUTLOOK

- **descriptive / method**: The study used SARs annotations from alerts as ground truth labels. (p. 7)[^original]  
  <sub>anchor: "We use SARs annotations from alerts as the ground truths."</sub>

## 4.3 Analysis of node classifications

- **descriptive / context**: Figures 4 and 5 plot sensitivity versus specificity for the pipeline and end-to-end methods on AMLSim and Elliptic. (p. 7)[^original]  
  <sub>anchor: "Fig. 4: Sensitivity vs. specificity for AMLSim dataset"</sub>

## 4.5 Effects of nodes embeddings + feature space

- **descriptive / context**: Figure 6 shows the effects of combining node embeddings with features. (p. 7)[^original]  
  <sub>anchor: "Fig. 6: Effects of combining node embeddings with features"</sub>

## 4.3 Analysis of node classifications

- **descriptive / finding or result**: Table 2 reports end-to-end results on AMLSim: Skip-GCN has AUPR 0.834 (0.792), F1 0.915 (0.875) and MCC 0.881 (0.763); FastGCN 0.841 (0.804), 0.927 (0.890) and 0.903 (0.781); EvolveGCN 0.869 (0.813), 0.934 (0.902) and 0.891 (0.773). (p. 7)[^original]  
  <sub>anchor: "Skip-GCN|0.834(0.792)|0.915(0.875)|0.881(0.763)|"</sub>
- **descriptive / finding or result**: The authors report that the DGT+XGBoost combination outperformed the other combinations in the pipeline comparison, covering both datasets. (p. 7)[^original]  
  <sub>anchor: "the _DGT+XGBoost_ combination outperformed all other combinations, covering both datasets"</sub>
- **descriptive / finding or result**: The authors observe that the end-to-end methods outperformed each and every pipeline method, with EvolveGCN outperforming all pipeline methods using tree-ensemble classifiers. (p. 7)[^original]  
  <sub>anchor: "the end-to-end methods outperformed each and every pipeline methods"</sub>
- **descriptive / finding or result**: EvolveGCN consistently outperforms both Skip-GCN and FastGCN, although the improvement is not very substantial for both datasets. (p. 7)[^original]  
  <sub>anchor: "EvolveGCN consistently outperforms both Skip-GCN and FastGCN"</sub>
- **descriptive / finding or result**: Table 4 reports end-to-end results on Elliptic: Skip-GCN has AUPR 0.928 (0.793), F1 0.916 (0.873) and MCC 0.854 (0.763); FastGCN 0.933 (0.805), 0.925 (0.881) and 0.875 (0.781); EvolveGCN 0.941 (0.813), 0.934 (0.891) and 0.891 (0.773). (p. 7)[^original]  
  <sub>anchor: "Skip-GCN|0.928(0.793)|0.916(0.873)|0.854(0.763)|"</sub>

## 5 CONCLUSION AND OUTLOOK

- **descriptive / method**: RF, GBT and ERT classifiers were trained on the embeddings to predict the suspiciousness of a target node via direct or indirect connections to known suspicious nodes. (p. 8)[^original]  
  <sub>anchor: "we trained RF, GBT, and ERT classifiers to predict the suspiciousness of a given target node"</sub>
- **descriptive / context**: The authors critically reviewed existing AML methods and outlined their potential limitations. (p. 8)[^original]  
  <sub>anchor: "we critically reviewed existing AML methods and outlined their potential limitations"</sub>
- **descriptive / context**: Cryptocurrencies pose great challenges to AML and make detection harder across cryptocurrency types. (p. 8)[^original]  
  <sub>anchor: "Cryptocurrencies not only impose great challenges to AML but also increase difficulty across cryptocurrency types."</sub>
- **descriptive / limitation**: Deep models may lack robustness under adversarial attacks, so AML detection mechanisms are not immune to attacks. (p. 8)[^original]  
  <sub>anchor: "while deep models may lack robustness under adversarial attacks"</sub>
- **descriptive / context**: Transactional datasets can be private, containing sensitive personal information and data of high monetary value, so privacy attacks could be very costly. (p. 8)[^original]  
  <sub>anchor: "the transactional dataset contains sensitive personal information and data with a high monetary value"</sub>
- **permissive / typology or red flag**: An attacker could apply reconstruction techniques to recover original inputs from shared embeddings or link them back to a natural person. (p. 9)[^original]  
  <sub>anchor: "to original input or link back to a natural person"</sub>
- **descriptive / typology or red flag**: Membership inference attacks can disclose whether a particular training record was used to train a deployed model. (p. 9)[^original]  
  <sub>anchor: "membership inference attacks [37] can be introduced in order to disclose whether a particular training record was used"</sub>
- **descriptive / method**: Future work will apply realistic attacks on AML detection algorithms and explore defence strategies, with differential privacy noted as one popular defence. (p. 9)[^original]  
  <sub>anchor: "we will also explore defence strategies to mitigate these attacks"</sub>
- **descriptive / limitation**: The main results rely on graphs that are fully available, such as public blockchain transaction graphs. (p. 9)[^original]  
  <sub>anchor: "Our main results learn from graphs which are totally available"</sub>
- **descriptive / typology or red flag**: In classical banking, money launderers may split laundered amounts into intermediates across different banks while not disclosing private transactions, so they go undetected. (p. 9)[^original]  
  <sub>anchor: "money-launderers take advantage of banks by not disclosing private transactions to split the laundered amounts"</sub>
- **descriptive / limitation**: In a prior functional encryption scheme, the size of embedding vectors used for similarity scores grows linearly with the number of existing bank accounts, which would be huge in practice. (p. 9)[^original]  
  <sub>anchor: "size of embedding vectors on which the similarity scores are calculated are linear w.r.t number of existing bank accounts"</sub>
- **descriptive / finding or result**: The authors argue that graph embedding techniques could drastically reduce these embedding sizes. (p. 9)[^original]  
  <sub>anchor: "Using graph embedding techniques the way we have in previous sections could drastically improve these sizes."</sub>
- **descriptive / context**: A challenge for banks is that each bank knows only the subgraph of transactions to and from the accounts it controls, so it must embed its nodes with that limited view. (p. 9)[^original]  
  <sub>anchor: "knowing only the subgraph of the transactions made to and from the accounts they control"</sub>
- **descriptive / method**: The proposed embedding depends only on each node's first neighbours, which fits the case of intermediate nodes split across banks with the same direct neighbours. (p. 9)[^original]  
  <sub>anchor: "we will perform an embedding depending only on"</sub>
- **descriptive / method**: Step 1 of the fast random projection variant gives each node and its direct neighbours an initial random embedding derived from a public hash function with a public seed. (p. 9)[^original]  
  <sub>anchor: "gets an initial random embedding vector value"</sub>
- **descriptive / method**: Step 2 sets each new embedding as the sum of neighbour embeddings weighted by transaction amounts, with the weight set to 0 when nodes are not connected. (p. 9)[^original]  
  <sub>anchor: "setting that weight to 0 when the nodes are not connected"</sub>
- **descriptive / method**: Step 3 normalises the vectors from the previous step to unit Euclidean norm to give the incoming or outgoing transaction embedding. (p. 9)[^original]  
  <sub>anchor: "The vectors for the previous step are then normalized"</sub>
- **descriptive / method**: Similarity between nodes from two banks is computed as the product of inner products of their incoming and outgoing transaction embeddings. (p. 9)[^original]  
  <sub>anchor: "We then apply the inner-products and similarity calculations similar to literature"</sub>
- **expected / recommendation**: Nodes with high similarity values should be labelled as suspicious accounts that may belong to the same money-laundering network, since they share most of their transaction neighbours. (p. 9)[^original]  
  <sub>anchor: "deem that nodes with high similarity values should be labeled as suspicious accounts"</sub>
- **permissive / typology or red flag**: Footnote 20 gives examples of how an adversary could fool the system, such as adding noise or minor perturbations in the embedding space. (p. 9)[^original]  
  <sub>anchor: "e.g., by adding noise or minor perturbations in the embedding space"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Catch Me If You Can: Semi-supervised Graph Learning for Spotting Money Laundering" (2023-02-23). https://arxiv.org/abs/2302.11880
