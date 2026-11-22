---
type: Source Digest
title: Towards Improved Illicit Node Detection with Positive-Unlabelled Learning - part 1 of 2 (pp. 1-5)
description: 'Verified paraphrased digest, pp. 1-5: Towards Improved Illicit Node Detection with Positive-Unlabelled Learning; Towards Improved Illicit Node Detection with Positive-Unlabelled Learning > I. INTRODUCTION; Towards Improved Illicit Node Detection with Positive-Unlabelled Learning > II. RELATED WORK; and 7 more sections'
resource: https://arxiv.org/abs/2303.02462
tags:
- academic_finding
- global_academic
- ml_statistics
- model_development
- network_graph
- preprint
status: stable
source_id: arxiv-towards-improved-illicit-node-detection-with-positive-unlabelled
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-04-03'
legal_status: unknown
part: 1
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2303.02462
  title: Towards Improved Illicit Node Detection with Positive-Unlabelled Learning
  author: org:arxiv
  last_modified: '2023-04-03T00:00:00Z'
digest_points: 48
---

# Towards Improved Illicit Node Detection with Positive-Unlabelled Learning (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-5) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Detecting illicit nodes on blockchain networks is described as valuable for strengthening future regulation; recent ML methods use transaction datasets with a small positive-labelled portion and the rest unlabelled (PU). (p. 1)[^original]  
  <sub>anchor: "Detecting illicit nodes on blockchain networks is a valuable task for strengthening future regulation."</sub>
- **descriptive / finding or result**: The paper argues that the label mechanism assumption for hidden positive labels, and its effect on evaluation metrics, is worth considering. (p. 1)[^original]  
  <sub>anchor: "we discuss that the label mechanism assumption for the hidden positive labels, and its effect on the evaluation metrics is worth considering"</sub>
- **descriptive / finding or result**: PU classifiers handling potential hidden positive labels are reported to can achieve improved performance compared with regular machine learning models. (p. 1)[^original]  
  <sub>anchor: "PU classifiers dealing with potential hidden positive labels can have improved performance compared to regular machine learning models."</sub>
- **descriptive / method**: PU classifiers are tested with a list of graph representation learning methods that yield different feature distributions for the same data, to obtain more reliable results. (p. 1)[^original]  
  <sub>anchor: "We test the PU classifiers with a list of graph representation learning methods for obtaining different feature distributions for the same data"</sub>

## I. INTRODUCTION

- **descriptive / context**: Blockchain systems are described as operating in a temporarily unregulated environment with varied abnormal usages and security concerns, including traditionally defined illicit activities such as phishing scams, Ponzi schemes and money laundering. (p. 1)[^original]  
  <sub>anchor: "Such decentralized systems, however, are in the current stage of a temporarily unregulated environment [2], [3]"</sub>
- **descriptive / context**: Mixing services, whose mixer nodes obscure the trace of transfers, are cited as activities without a clear definition of lawfulness; the US Treasury declared Tornado Cash a sanctioned entity. (p. 1)[^original]  
  <sub>anchor: "US Department of the Treasury declared Tornado Cash as a sanctioned entity [5], [6]."</sub>
- **descriptive / method**: Existing illicit node detection methods use topological graph features with tree-based models, clustering, and logistic regression, or node embeddings from graph representation learning for node classification. (p. 1)[^original]  
  <sub>anchor: "The methods include using topological graph features as the input to machine learning models such as tree-based models [7], clustering [8], [9], logistic regression [10]"</sub>
- **descriptive / finding or result**: Prior work has seldom discussed label assumptions or evaluation methods for blockchain datasets with very few positive labels and many unlabelled samples. (p. 1)[^original]  
  <sub>anchor: "little has been discussed about label assumptions or the evaluation methods for the blockchain datasets with illicit node labels"</sub>
- **descriptive / typology or red flag**: Some earlier phishing-node studies use binary labels assuming unlabelled nodes are normal; this is described as practicable if the majority of nodes are not illicit. (p. 1)[^original]  
  <sub>anchor: "The assumption is practicable if the majority of nodes are not illicit."</sub>
- **descriptive / limitation**: Standard metrics such as precision and F1 score cannot be precisely calculated without fully labelled data. (p. 1)[^original]  
  <sub>anchor: "standard classification metrics such as precision and F1 score cannot be precisely calculated without fully labeled data."</sub>
- **descriptive / method**: The paper combines PU learning studies for illicit node classification, examining the SCAR assumption, quantifying metric gaps on an engineered Ethereum PU dataset, and comparing PU classifiers and graph embedding methods on two real-world datasets. (p. 1)[^original]  
  <sub>anchor: "In this work, we combine existing studies of PU learning on illicit node classification."</sub>
- **descriptive / finding or result**: The results indicate PU classifiers improve on baselines, and PU learning helps where hidden positive nodes are likely, a common situation in blockchain transaction data. (p. 1)[^original]  
  <sub>anchor: "The result evidence that PU learning help in learning the data with possible hidden positive nodes"</sub>

## II. RELATED WORK

- **descriptive / context**: Related work covers node classification in blockchain transaction networks for phishing and scam nodes, mixing service nodes, and user deanonymizing; a few works apply PU learning. (p. 1)[^original]  
  <sub>anchor: "Among the node classification approaches on blockchain transaction data, a few works apply PU learning models [10], [19]."</sub>
- **descriptive / case example**: Wu et al. use the two-step spy method to select reliable negatives from unlabelled data for detecting mixer nodes in Bitcoin networks. (p. 2)[^original]  
  <sub>anchor: "Wu et al. [10] use the two-step spy method to select some reliable negative instances from the unlabeled data"</sub>
- **descriptive / finding or result**: Saunders et al. argue that the label mechanism assumption is essential for obtaining convincing results on PU datasets. (p. 2)[^original]  
  <sub>anchor: "argue that the label mechanism assumption is essential for obtaining convincing results for the PU datasets."</sub>

## III. POSITIVE AND UNLABELED (PU) LEARNING

- **descriptive / context**: The major challenge for ML on blockchain transaction networks is lack of labelled data; unlabelled addresses may be negative or hidden positive, and labels come from explorers and analytics platforms such as Etherscan and may be added later from public submissions. (p. 2)[^original]  
  <sub>anchor: "unlabeled addresses can be negative or actually hidden positive"</sub>
- **descriptive / definition**: In a PU dataset for binary illicit detection, positives are labelled +1 and unlabelled nodes are labelled -1 or 0, so no negative examples are labelled. (p. 2)[^original]  
  <sub>anchor: "a PU dataset has limited number of positive nodes labeled as +1 and unlabeled nodes labeled -1 or 0"</sub>
- **mandatory / requirement**: To reduce a PU task to standard binary classification the data must satisfy the SCAR assumption, under which the labelled set is selected independently of its attributes; otherwise standard classification metrics cannot be estimated. (p. 2)[^original]  
  <sub>anchor: "the data must be under Selected Completely At Random (SCAR) assumption [23]"</sub>

## III-A. Selected Completely At Random (SCAR) Assumption

- **descriptive / definition**: Under SCAR, predicting Pr(y=1|x) differs from predicting Pr(s=1|x) only by a constant, so both classifiers rank instances the same way and recall can be estimated. (p. 2)[^original]  
  <sub>anchor: "predicting _Pr_ ( _y_ = 1 _|x_ ) is different from predicting _Pr_ ( _s_ = 1 _|x_ ) by a constant under SCAR assumption"</sub>

## III-B. Evaluation metrics

- **descriptive / finding or result**: Under SCAR, recall can be estimated from PU data, but precision cannot be calculated because false positives cannot be correctly estimated. (p. 2)[^original]  
  <sub>anchor: "the recall r = Pr (ˆ y = 1 |y = 1) can be estimated from PU data"</sub>
- **descriptive / definition**: Since precision cannot be estimated from PU data, F1 cannot be defined; the alternative PUF1 = r^2 / Pr(ŷ=1) is proposed in prior work and penalises a large share of positive predictions while rewarding high recall. (p. 2)[^original]  
  <sub>anchor: "PUF1 = _r_2 _/Pr_ (ˆ _y_ = 1) is proposed and suggested in [24], [25]"</sub>

## III-C. Evaluation Metrics on Engineered PU Data

- **descriptive / data or feature**: The engineered PU dataset is derived from an Ethereum transaction dataset with 1165 labelled illicit nodes among 2.9 million nodes. (p. 2)[^original]  
  <sub>anchor: "which has _1165_ labeled illicit nodes in _2.9_ million nodes."</sub>
- **descriptive / method**: Experiments randomly pick 1165 unlabelled nodes as negatives, extract first-order neighbours of positive and negative nodes and their edges to form subnetworks, repeated ten times, averaging about 30,000 nodes and 263,000 edges per subnetwork. (p. 2)[^original]  
  <sub>anchor: "the average number of nodes of the subnetworks is _30,000_ nodes and _263,000_ edges."</sub>

## III-B. Evaluation metrics

- **descriptive / limitation**: Some earlier works treat the unlabelled data as negative without stating negative-label assumptions, so their reported precision, recall and F1-score rest on that assumption. (p. 2)[^original]  
  <sub>anchor: "The presented evaluation results of precision, recall, and F1-score is based on assuming the unlabeled is negative."</sub>
- **descriptive / limitation**: Without noting that the results are an estimation based on the SCAR assumption, similar future works on positive-unlabelled blockchain data could raise concerns. (p. 2)[^original]  
  <sub>anchor: "without noting that the results are an estimation based on the SCAR assumption could raise the concern"</sub>

## III-C. Evaluation Metrics on Engineered PU Data

- **descriptive / method**: Data were split 80% training and 20% testing after some positive nodes were relabelled as negatives; node2vec embeddings were used with logistic regression and SVM classifiers. (p. 3)[^original]  
  <sub>anchor: "the data was split into 80% for training and 20% for testing."</sub>
- **descriptive / finding or result**: Hidden positives counted as false positives lower the estimated precision because the detected share of labelled positives is used as an estimate for the whole positive set. (p. 3)[^original]  
  <sub>anchor: "some positives labeled as negative (unlabeled) are correctly predicted but counted as false positives, therefore the precision decreases."</sub>
- **descriptive / finding or result**: Even the genuine collected labels form a PU dataset with missing hidden positives, so precision and F1 may be underestimated, but comparisons between PU models are still considered fair. (p. 3)[^original]  
  <sub>anchor: "even though the precision and F1 may be underestimated due to hidden positive labels, the comparison between PU models is still fair."</sub>

## IV. NODE EMBEDDINGS AND PU LEARNING MODELS

- **descriptive / data or feature**: Two real-world datasets are used: the Ethereum dataset with 1165 illicit nodes in 2.9 million nodes, and the Elliptic Bitcoin dataset with 4545 illicit nodes in 203,000 nodes. (p. 3)[^original]  
  <sub>anchor: "a Bitcoin transaction dataset (Elliptic dataset) with _4545_ illicit nodes labeled in _203,000_ nodes of Bitcoin networks [16]."</sub>
- **descriptive / method**: Graph representation algorithms map nodes into low-dimensional embedding vectors that reduce storage and computation; all methods use an output dimension of 64. (p. 3)[^original]  
  <sub>anchor: "with an output dimension of 64 for all the methods."</sub>

## IV-A. Node Embedding

- **descriptive / method**: Node2vec is a random-walk method preserving neighbour relations; p=1 and q=1 are used to avoid biasing movement, with walk length 5 following reference [14]. (p. 3)[^original]  
  <sub>anchor: "We use _p=1, q=1_ to not add bias moving forward or return from the current node."</sub>
- **descriptive / method**: Poincaré embedding learns node representations in a hyperbolic Poincaré space via Riemannian optimisation to capture hierarchy, with high-hierarchy nodes being those connected to many others, such as whale nodes. (p. 3)[^original]  
  <sub>anchor: "learns node embedding in a hyperbolic Poincar´e space which can better capture the hierarchy information of nodes."</sub>
- **descriptive / method**: Role2vec is a random-walk structural embedding method with walk length 5, treating addresses with similar motif structure as more similar regardless of distance. (p. 3)[^original]  
  <sub>anchor: "Role2vec [29] is a random-walk-based structural node embedding method (with walk length l = 5)."</sub>

## III-C. Evaluation Metrics on Engineered PU Data

- **descriptive / finding or result**: In illicit node detection, labelled positives are fewer than reality and the unlabelled class makes true positives underestimated and false positives overestimated. (p. 3)[^original]  
  <sub>anchor: "the labeled positives are smaller than the reality and the other class being unlabeled makes the true positives underestimated"</sub>
- **permissive / recommendation**: Where the cost of a false negative is higher than that of a false positive, recall can be treated as the more important metric to maximise. (p. 3)[^original]  
  <sub>anchor: "we can treat recall as a more important metric to maximize. However, we must ensure that the positive predictions"</sub>

## IV. NODE EMBEDDINGS AND PU LEARNING MODELS

- **descriptive / data or feature**: Bagging SVM (BAG) learns and aggregates multiple biased SVM classifiers trained on the positive samples and a subset of the negative samples. (p. 3)[^original]  
  <sub>anchor: "which learns and aggregates multiple biased SVM classifiers trained on the positive samples and a subset of the negative samples"</sub>
- **descriptive / method**: Elkanoto-SVM (EL) trains a classifier to predict the probability that a sample is labelled, and uses it to estimate the probability that a sample is positive. (p. 3)[^original]  
  <sub>anchor: "Elkanoto (EL)-SVM [23] (which trains a classifier to predict _P_ ( _s_ = 1 _|x_ )"</sub>
- **descriptive / method**: Unbiased PU learning (UPU) treats unlabelled data as downweighted negative examples and uses a double hinge loss to remove the bias between positive and unlabelled data. (p. 3)[^original]  
  <sub>anchor: "where unlabeled data is used as downweighted negative examples by using a double hinge loss"</sub>

## IV-A. Node Embedding

- **descriptive / method**: MNMF is a matrix-factorisation method learning a cluster membership distribution so embeddings preserve both node and community structure. (p. 4)[^original]  
  <sub>anchor: "learns a cluster membership distribution over nodes such that a node’s embedding preserves both itself and community structures."</sub>
- **descriptive / method**: Baselines are Logistic Regression, Random Forest and SVM; PU models examined are bagging SVM (BAG), Elkan-Noto SVM (EL) and Unbiased PU learning (UPU) using a double hinge loss. (p. 4)[^original]  
  <sub>anchor: "We use Logistic Regression (LR), Random Forest (RF), and Support Vector Machine (SVM) as the baselines."</sub>
- **descriptive / method**: Experiments use the same ten subgraph construction as before and report mean results across them. (p. 4)[^original]  
  <sub>anchor: "We perform the same ten subgraphs construction as mentioned in section III-C and report the mean evaluation results."</sub>
- **descriptive / data or feature**: Table I reports precision, recall, F1 and PUF1 for LR, RF, SVM, BA, EL, UPU across node2vec, Poincaré, Role2vec, MNMF and two combined embeddings on the Ethereum dataset; the values are partly garbled in extraction and are not restated here. (p. 4)[^original]  
  <sub>anchor: "TABLE I: Evaluation results on list of ML models and graph embeddings on Ethereum dataset"</sub>
- **descriptive / data or feature**: Table II reports the same metrics for the Bitcoin dataset across the same embedding methods and classifiers; values are partly garbled in extraction and are not restated here. (p. 4)[^original]  
  <sub>anchor: "TABLE II: Evaluation results on list of ML models and graph embeddings on Bitcoin dataset"</sub>
- **descriptive / finding or result**: BA and EL PU models perform better than baselines for most embedding methods in terms of F1 or PUF1 on both datasets. (p. 4)[^original]  
  <sub>anchor: "the PU learning models BA and EL perform better than the baselines for the majority of embedding methods"</sub>
- **descriptive / finding or result**: Combining node2vec and Poincaré embeddings gives an F1 of 0.946 on the Ethereum data, the same as combining node2vec with structural feature engineering from reference [14]. (p. 4)[^original]  
  <sub>anchor: "end up with a performance of 0.946 in terms of F1 as the same performance as combining node2vec with feature engineering"</sub>
- **descriptive / finding or result**: On the Bitcoin dataset, BA and EL PU models also improve performance, suggesting detection benefits from PU models placed after graph representation learning. (p. 4)[^original]  
  <sub>anchor: "we can also observe an improved performance using BA and EL PU models"</sub>

## V. CONCLUSION

- **descriptive / finding or result**: The paper discusses the PU data problem in blockchain cryptocurrency transactions, label mechanism assumptions and proper evaluation, and reports better performance from combining PU learning with graph representation learning on two real-world datasets. (p. 4)[^original]  
  <sub>anchor: "Moreover, we demonstrated the better performance of combining PU learning models into illicit node detection"</sub>

## IV. NODE EMBEDDINGS AND PU LEARNING MODELS

- **descriptive / data or feature**: Poincaré embedding is a hierarchical representation method based on Riemannian optimisation in hyperbolic space, and higher-hierarchy nodes lie closer to the coordinate origin. (p. 4)[^original]  
  <sub>anchor: "The higher the hierarchy, the closer the node is to the coordinate origin."</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Towards Improved Illicit Node Detection with Positive-Unlabelled Learning" (2023-04-03). https://arxiv.org/abs/2303.02462
