---
type: Source Text
title: 'GuiltyWalker: Distance to illicit nodes in the Bitcoin network - part 2 of 2 (pp. 3-5)'
description: 'Verbatim extracted text, pp. 3-5: 4 RESULTS; 5 RELATED WORK; REFERENCES; and 1 more sections'
resource: https://arxiv.org/abs/2102.05373
tags:
- academic_finding
- data_features
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-guiltywalker-distance-to-illicit-nodes-in-the-bitcoin-network
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-10-02'
legal_status: unknown
part: 2
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2102.05373
  title: 'GuiltyWalker: Distance to illicit nodes in the Bitcoin network'
  author: org:arxiv
  last_modified: '2021-10-02T00:00:00Z'
---

# GuiltyWalker: Distance to illicit nodes in the Bitcoin network

[previous part](text-001.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2021-10-02), part 2 of 2, pp. 3-5. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 4 RESULTS


[pp. 3-4]

|||Illicit||MicroAVG|
|---|---|---|---|---|
|Method|Precision|Recall|F1|F1|
|AF|0.91|0.72|0.80|0.977|
|GWF|0.93|0.11|0.20|0.942|
|AF + GWF|0.93|0.76|0.84|0.981|
|AF + GWF*|0.97|0.77|0.85|0.983|

Table 1 shows the testing results in terms of precision, recall and F1-score concerning the illicit class. For the sake of completeness, we also show the micro-averaged F1 score.

An important thing to note from Table 1 is that the GuiltyWalker features alone are not informative enough. The F1-score value obtained using only these features is very low (0.20). We can also observe higher precision, recall, and F1-score when using GuiltyWalker’s additional features, suggesting the importance of the graph structure. Using GuiltyWalker features, we improved precision, recall, and F1-score by 2 percentage points (pp), 4pp, and 4pp, respectively.

In order to understand the importance of each one of the features created, we performed feature importance, using the method described in the previous section. We kept only the most important

Catarina Oliveira, João Torres, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro Bizarro

Figure 2: ROC curve associated with AF + GWF* and AF models. Random baseline represented in red.

features to train together with the original ones. Results show that by filtering GuiltyWalker features and keeping only the most important ones ( _hit_ , _std_ , _illicit_ , _max_ and _mean_ ), the performance of the model slightly improves (we improved F1-score by 1pp, comparing with the model AF+GWF).

To give additional insights about the performance of the new model AF + GWF* compared against the original model, we plot the ROC curve of both models.

Note that the ROC curve shows the trade-off between sensitivity/ recall and specificity. Moreover, the area under the curve (AUC) can be seen as a measure of separability. In other words, it represents how much a model is capable of distinguishing between classes. Therefore, from the observation of Figure 2, we can infer that both models are quite good at predicting illicit nodes as illicit and licit ones as licit. However, AF + GWF* is slightly better (improves AUC value by 1pp). In particular, for very low false positive rates, our method seems to be significantly better.

[p. 4]

In a real scenario, we would be more interested in low falsepositive regions of the ROC-curve since raising too many alerts is not practical. With this in mind, we compare the recall at specific low false positive rates, namely 1%, 5% and 10%, and AF+GWF* shows considerable gains when compared against AF: recall@1% increases from 73% to 78% (5pp), recall@5% increases from 75% to 80% (5pp), and recall@10% increases from 76% to 82% (6pp). Therefore, while the gain of using GuiltyWalker’s features is only 1pp in the full region, in the region of interest the gain is considerably higher.

As noted by Weber et al. [16], a sudden dark market shutdown occurring at time step 43 extremely affects the model performance. In particular, the random forest model trained on the 166 features, from that time step forward, cannot achieve an Illicit F1-score value above 0.25. The introduction of the new set of features extracted from GuiltyWalker improves F1 results in the entire test set (i.e., time steps 35-49). However, this improvement is more notorious after this dark market shutdown (from time step 43 to 49). In fact, from time step 43 to time step 49, we observe, on average, a F1 score improvement of about 10pp and 16pp with AF + GWF and AF + GWF* models, respectively. Note that for time steps 48 and 49, both of these models still perform poorly.

Figure 3: Illicit F1-score obtained with Random Forest, for the standard 166 features and the new GuiltyWalker features before and after feature selection.

As we can see in Figure 3, both AF + GWF and AF + GWF* models are able to reliably capture new illicit transactions after the dark market shutdown, in comparison with the original model. To understand the additional information those models are capturing, we compute the confusion matrices of the models AF, AF+GWF and AF+GWF*. We obtain 784, 828 and 831 true positives (referred to as TP), respectively. We also determine the new TP found and the ones lost, using AF + GWF and AF + GWF* models, in comparison to the ones found training RF with the original set of features. By doing so, we can verify that with the new sets of features, AF+GWF and AF+GWF*, we found 48 and 50 new TP and lost 4 and 3 TP that the original model could find, respectively.

Concerning the AF + GWF* model, we observe that, for almost all new TP found, the features extracted from GuiltyWalker ( _max_ , _mean_ , _std_ , _illicit_ and _hit_ ) have positive values. Only 2 of the 50 elements have -1 values regarding _max_ , _mean_ , _std_ and _illicit_ and 0 with respect to _hit_ . Recall that these values indicate that the associated transaction nodes have no possible paths to known illicit nodes.

This interesting fact lets us infer that the new set of features adds some new information based on the graph’s structure, which allows the model to make better predictions. However, we have to notice that the fact that a given node has a path to an illicit transaction does not necessarily imply that it is also illicit and vice-versa. This information alone is not enough to make good predictions concerning the labels of the transaction nodes, as we verified from the results obtained for the GWF model. Nonetheless, it provides extra information to complement the original features in a way that boosts performance of the overall model.

## 5 RELATED WORK


[pp. 4-5]

Besides the work of Weber et al. [16], which was the baseline for our study, more recently, Lorenz et al. [6] proposed active learning techniques to study the minimum number of labels necessary to achieve high detection of illicit activity in cryptocurrencies and tested them also on the Elliptic data set. Thus, even though using a different approach to the same problem, the authors did not aim to achieve better results than the baseline. Moreover, Alarab et al.

[1] proposed an ensemble learning method, using a combination of the given supervised learning models, and applied it on the Elliptic data set, improving the baseline results. Although they improved upon existing results, our results, using the new set of features, are better. While Alarab et al. [1] achieves higher precision than us (97.38% versus 96.5%), we achieve higher recall (76.7% versus 72.2%), higher F1-score (85.47% versus 82.92%), and higher accuracy (98.3% versus 98.06%).

As far as we know, previous work on the application of graphrelated features and, in particular, random walks, in a supervised learning setting are scarce. Hu et al. [5] worked with Bitcoin transaction graphs and used various graph characteristics to differentiate money laundering transactions from regular transactions. They actually found that the main difference between them lies in their output values and neighbourhood information. The authors also evaluated a set of classifiers based on different types of extracted features, namely immediate neighbours, curated features, deepwalk embeddings [11], and node2vec embeddings [3] to classify money laundering and regular transactions. This approach differs from ours as we are not trying to embed the graph or a particular node’s neighbourhood but instead to describe distances to a specific target (i.e., malicious activity). Nonetheless, the descriptive power of random walks in networks is still recognized. Smriti Bhagat and Muthukrishnan [14] studied methods based on the iterative application of traditional classifiers using graph information as features, and methods that propagate the existing labels via random walks. Moreover, concerning the application of random walks in the context of classification problems, Samer Hassan and Banea [12] proposed a new approach for estimating term weights in a document based on a random walk model. They showed that the new random walk based approach outperforms the traditional term frequency approach of feature weighting. Therefore, with this work, we extend the existing knowledge regarding random walks to improve classifiers’ performance in graph datasets.

illicit transactions that were not captured by the model from Weber et al. [16].

## REFERENCES


[p. 5]

- [1] Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. 2020. Comparative analysis using supervised learning methods for anti-money laundering in bitcoin. In _Proceedings of the 2020 5th International Conference on Machine Learning Technologies_ . 11–17.

- [2] Claudio Bellei. 2019. The Elliptic Data Set: opening up machine learning on the blockchain. https://medium.com/elliptic/the-elliptic-data-set-opening-upmachine-learning-on-the-blockchain-e0a343d99a1

- [3] Aditya Grover and Jure Leskovec. 2016. node2vec: Scalable feature learning for networks. In _Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining_ . 855–864.

- [4] Aric A. Hagberg, Daniel A. Schult, and Pieter J. Swart. 2008. Exploring Network Structure, Dynamics, and Function using NetworkX. In _Proceedings of the 7th Python in Science Conference_ , Gaël Varoquaux, Travis Vaught, and Jarrod Millman (Eds.). Pasadena, CA USA, 11 – 15.

- [5] Yining Hu, Suranga Seneviratne, Kanchana Thilakarathna, Kensuke Fukuda, and A. Seneviratne. 2019. Characterizing and Detecting Money Laundering Activities on the Bitcoin Network. _ArXiv_ abs/1912.12060 (2019).

- [6] Joana Lorenz, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro Bizarro. 2020. Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity. In _arXiv 2005.14635_ .

- [7] Satoshi Nakamoto and A Bitcoin. 2008. A peer-to-peer electronic cash system. _Bitcoin_ 4 (2008). https://bitcoin.org/bitcoin.pdf

- [8] Financial Crimes Enforcement Network. 2019. Application of FinCEN’s Regulations to Certain Business Models Involving Convertible Virtual Currencies. https://www.fincen.gov/resources/statutes-regulations/guidance/ application-fincens-regulations-certain-business-models

- [9] NetworkX. [n.d.]. _networkx.algorithms.dag.descendants_ . https: //networkx.org/documentation/stable/reference/algorithms/generated/ networkx.algorithms.dag.descendants.html

- [10] Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, et al. 2011. Scikit-learn: Machine learning in Python. _the Journal of machine Learning research_ 12 (2011), 2825–2830.

- [11] Bryan Perozzi, Rami Al-Rfou, and Steven Skiena. 2014. Deepwalk: Online learning of social representations. In _Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining_ . 701–710.

- [12] Rada Mihalcea Samer Hassan and Carmen Banea. 2006. Random Walk Term Weighting for improved Text Classification. In _International Journal of Semantic Computing_ . 421–439.

- [13] scikit learn. [n.d.]. _Permutation feature importance_ . https://scikit-learn.org/ stable/modules/permutation_importance.html

- [14] Graham Cormode Smriti Bhagat and S. Muthukrishnan. 2011. Node Classification in Social Networks. In _Social Network Data Analytics_ . 115–148.

## 6 CONCLUSION


In this study, we set out to improve the performance of supervised models in an anti-money laundering classification task. Given a transaction network, we propose a method called GuiltyWalker that extracts information from the structure of the network and the existence of past labels to create new features for a supervised model. It consists of a random walker that traverses the transaction network starting from a seed node and a feature extractor that computes features related to the distance of the seed node to other nodes known to be illicit.

- [15] European Union. 2018. Directive (EU) 2018/843 of the European Parliament and of the Council of 30 May 2018 amending Directive (EU) 2015/849 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing, and amending Directives 2009/138/EC and 2013/36/EU.

- [16] Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Claudio Bellei, Tom Robinson, and Charles E. Leiserson. 2019. Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics. arXiv:1908.02591 [cs.SI]

We test our method on a public dataset of Bitcoin transactions published by Weber et al. [16]. Using a supervised setting similar to the original authors as our baseline, we showed that by training the same classifier considering the original 166 features and the new ones extracted from GuiltyWalker, we could obtain better results. In particular, by filtering the features extracted from GuiltyWalker and considering only the most important ones, the results were even better. The performance differences were more notorious for time steps associated with a black market shutdown, where the baseline model performed poorly. Moreover, we observed that the models that considered GuiltyWalker features could reliably capture new


---

[previous part](text-001.md) | [source overview](overview.md)

[^original]: arXiv, "GuiltyWalker: Distance to illicit nodes in the Bitcoin network" (2021-10-02). https://arxiv.org/abs/2102.05373
