---
type: Source Digest
title: 'BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis - part 2 of 3 (pp. 6-11)'
description: 'Verified paraphrased digest, pp. 6-11: BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _C. Local Structural Indicator_; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _B. Experiment Process_; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > _C. Result and Analysis_; and 3 more sections'
resource: https://arxiv.org/abs/2204.05746
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-babd-a-bitcoin-address-behavior-dataset-for-pattern-analysis
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-12-28'
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
  resource: https://arxiv.org/abs/2204.05746
  title: 'BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis'
  author: org:arxiv
  last_modified: '2023-12-28T00:00:00Z'
digest_points: 70
---

# BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-11) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## C. Local Structural Indicator

- **descriptive / data or feature**: The PAI+PTI group of context indicators includes, for each address, the average, minimum/maximum and standard deviation of input/output token amounts and of their ratios and changes across basic units of the active period. (p. 6)[^original]  
  <sub>anchor: "The average input/output token amount of an address in each basic unit of the active period"</sub>
- **descriptive / data or feature**: The PDI+PTI group of context indicators covers in-degree and out-degree per basic unit of the active period, including their averages, minimum/maximum, ratios across in, out and all degrees, and changes in ratios, each with statistical summaries. (p. 6)[^original]  
  <sub>anchor: "The average in-degree/out-degree of an address in each basic unit of the active period"</sub>
- **descriptive / data or feature**: Fig. 2 shows the k-hop subgraph Gk with maximum k = 4 generated with different maximum numbers of nodes, ranging from 500 nodes to 20000 nodes across panels (a) to (h). (p. 7)[^original]  
  <sub>anchor: "Fig. 2. _Gk_ with maximum _k_ = 4 and different maximum number of nodes"</sub>
- **descriptive / data or feature**: The maximum value of the degree distribution is used as a feature of the local structural indicator (LSI). (p. 7)[^original]  
  <sub>anchor: "the maximum value of degree distribution as the feature of _LSI_ ."</sub>
- **descriptive / definition**: Degree correlation (S3) measures how nodes with large degree relate to nodes with small degree in Gk; the paper uses the simplified Pearson degree correlation proposed by Newman, computed over edges using the degrees of the two connected nodes and the total number of edges E. (p. 7)[^original]  
  <sub>anchor: "simplified Pearson degree correlation proposed by Newman [33] is selected to measure _Gk_ :"</sub>
- **descriptive / definition**: Betweenness (S4) reflects the impact of a node in Gk, based on the number of shortest paths between two other nodes that pass through that node. (p. 7)[^original]  
  <sub>anchor: "is the betweenness that reflects the impact of the node in _Gk_ [32]:"</sub>
- **descriptive / definition**: Average path (S5) is the average distance between any two nodes in Gk. (p. 7)[^original]  
  <sub>anchor: "GPk_istheaveragedistancebetween any two nodes in _Gk_ :"</sub>
- **descriptive / definition**: Diameter (S6) is the longest distance between any two nodes in Gk. (p. 7)[^original]  
  <sub>anchor: "Diameter (S6). _G__len_ _k_ is the longest distance between any two nodes in _Gk_ ."</sub>
- **descriptive / definition**: Closeness centrality (S7) measures how close a node is to all other nodes in Gk, indicating how efficiently it can spread information, using the minimum distances from the node to the others and the total number of nodes n. (p. 7)[^original]  
  <sub>anchor: "which can provide the efficiency of spreading information of a node [34]:"</sub>
- **descriptive / definition**: PageRank (S8) gives the PageRank value of a node in Gk as an evaluation of its influence, using a damping factor alpha, the in-neighbours of the node and the out-degree of each in-neighbour. (p. 7)[^original]  
  <sub>anchor: "which evaluates the influence of the node [35]:"</sub>
- **descriptive / definition**: Density (S9) measures the density of Gk according to edge connectivity, using the total number of edges E. (p. 8)[^original]  
  <sub>anchor: "G__ds_ _k_isthedensityof_Gk_thatmeasuresthe density according to the edge connectivity [36]:"</sub>

## V. EXPERIMENTS

- **descriptive / method**: The framework is implemented mainly with graph-tool, while networkx is used to test and verify methods on small graphs. (p. 8)[^original]  
  <sub>anchor: "We mainly utilize _graph-tool_ [37] to implement the framework proposed above."</sub>
- **descriptive / data or feature**: Table IV lists the computer configuration: Intel Xeon Silver 4210R 2.40 GHz CPU, 320 GB RAM, Ubuntu 21.04, Python 3.9.5 and graph-tool 2.42. (p. 8)[^original]  
  <sub>anchor: "Intel Xeon Silver 4210R 2.40 GHz"</sub>
- **descriptive / method**: The authors use scikit-learn and xgboost to implement five common machine learning models (KNN, decision tree, random forest, MLP and XGBoost) to test BABD-13. (p. 8)[^original]  
  <sub>anchor: "We choose _k_ -nearest neighbors (KNN) algorithm, decision tree"</sub>

## B. Experiment Process

- **descriptive / method**: The experiment has three phases: construction of a directed heterogeneous multigraph transaction graph from the Bitcoin ledger JSON files, feature extraction, and address category modelling. (p. 8)[^original]  
  <sub>anchor: "our following experiment consists of three phases - transaction graph construction, features extraction, and address category modeling"</sub>
- **descriptive / method**: Coinbase transactions are added to the graph using a different method from normal transactions. (p. 8)[^original]  
  <sub>anchor: "coinbase transactions are different from normal transactions, thus, we add them to the graph in different methods respectively."</sub>
- **descriptive / method**: Missing values in the feature CSV file are filled with zero, based on the authors' understanding of the proposed features. (p. 8)[^original]  
  <sub>anchor: "we use the zero value to fill all the missing values in the raw CSV file"</sub>
- **descriptive / method**: The data is split 8:2 into training and testing sets, and min-max normalization is applied. (p. 8)[^original]  
  <sub>anchor: "We perform an 8:2 split of the training set and testing set on the BABD-13"</sub>
- **descriptive / data or feature**: BABD-13 is divided into SI features (132 features) and LSI features (16 features). (p. 8)[^original]  
  <sub>anchor: "It is noted that we divide the BABD-13 into two parts that are _SI_ with 132 features and _LSI_ with 16 features."</sub>
- **descriptive / method**: The task is a multiclass classification on BABD-13, and the number of samples per class is quite imbalanced. (p. 8)[^original]  
  <sub>anchor: "The task for these models is a multiclass classification on BABD-13 and the number of samples for each class is quite imbalanced."</sub>
- **descriptive / method**: The KNN model uses 4 neighbours, a kd-tree algorithm and distance weighting. (p. 8)[^original]  
  <sub>anchor: "KNN , built by function _KNeighborsClassifier_ () from _scikit-learn_ with parameters _n neighbors=4_"</sub>
- **descriptive / method**: The decision tree model uses entropy as the criterion and the best splitter. (p. 8)[^original]  
  <sub>anchor: "DT , built by function _DecisionTreeClassifier_ () from _scikit-learn_ with parameters _criterion=‘entropy’_"</sub>

## V. EXPERIMENTS

- **descriptive / method**: Algorithm 1 generates the k-hop subgraph Gk for a Bitcoin address, taking the transaction graph, a dictionary and the address as input and returning the subgraph. (p. 8)[^original]  
  <sub>anchor: "Output: the _k_ -hop subgraph _Gk_"</sub>

## B. Experiment Process

- **descriptive / data or feature**: The experiment uses 132 SI features and 16 LSI features, which together form 148 features on BABD-13. (p. 8)[^original]  
  <sub>anchor: "we divide the BABD-13 into two parts that are _SI_ with 132 features and _LSI_ with 16 features"</sub>

## V. EXPERIMENTS

- **descriptive / method**: Table IV gives the computer configuration used, including an Intel Xeon Silver 4210R CPU, 320 GB RAM, Ubuntu 21.04, Python 3.9.5 and graph-tool 2.42. (p. 8)[^original]  
  <sub>anchor: "Intel Xeon Silver 4210R 2.40 GHz"</sub>

## B. Experiment Process

- **descriptive / method**: Models are trained on an 8:2 split of training and testing data, with min-max normalisation applied to the split data, and the zero value is used to fill missing values. (p. 8)[^original]  
  <sub>anchor: "We perform an 8:2 split of the training set and testing set on the BABD-13"</sub>
- **descriptive / method**: The random forest model uses 200 estimators. (p. 9)[^original]  
  <sub>anchor: "RF , built by function _RandomForestClassifier_ () with parameter _n estimators=200_ ."</sub>
- **descriptive / method**: The MLP model uses the adam solver, 1000 maximum iterations and three hidden layers of 100 units each. (p. 9)[^original]  
  <sub>anchor: "hidden layer sizes=(100, 100, 100)_ ."</sub>
- **descriptive / method**: The XGB model uses the multi:softmax objective with 13 classes, mlogloss evaluation, and a learning rate of 0.5. (p. 9)[^original]  
  <sub>anchor: "XGB by function _XGBClassifier_ () from _xgboost_ with parameters _objective=‘multi:softmax’_"</sub>
- **descriptive / method**: A random state of 9 is set for every method and model where it exists, to ease reproduction. (p. 9)[^original]  
  <sub>anchor: "we set parameter _random_ _state=9_ for every method and model if it exists"</sub>

## C. Result and Analysis

- **descriptive / finding or result**: With SI+LSI features, the five models reach accuracy of at least 93.24% and at most 96.71%, with precision, recall and F1-score in comparable ranges. (p. 9)[^original]  
  <sub>anchor: "The results of ( _SI+LSI_ ) witness that the accuracy rate, precision, recall, and f1-score can reach at least 93.24%"</sub>
- **descriptive / data or feature**: Table V reports accuracy, weighted precision, recall and F1-score for KNN, DT, RF, MLP and XGB on SI, LSI and SI+LSI features, with XGB on SI+LSI being the best row at accuracy 0.9671, precision 0.9646, recall 0.9671 and F1-score 0.9657. (p. 9)[^original]  
  <sub>anchor: "XGB_SI_+_LSI_|0.9671|0.9646|0.9671|0.9657|"</sub>
- **descriptive / finding or result**: Table V gives KNN on SI as accuracy 0.6862, precision 0.6667, recall 0.6862 and F1 0.6749; on LSI as 0.9418, 0.9381, 0.9418 and 0.9397; and on SI+LSI as 0.9324, 0.9280, 0.9324 and 0.9297. (p. 9)[^original]  
  <sub>anchor: "KNN_SI_|0.6862|0.6667|0.6862|0.6749|"</sub>
- **descriptive / finding or result**: Table V gives DT on SI as accuracy 0.7061, on LSI as 0.9376 and on SI+LSI as 0.9444 (precision 0.9447, recall 0.9444, F1 0.9446). (p. 9)[^original]  
  <sub>anchor: "DT_SI_+_LSI_|0.9444|0.9447|0.9444|0.9446|"</sub>
- **descriptive / finding or result**: Table V gives RF on SI as accuracy 0.7566, on LSI as 0.9565 and on SI+LSI as 0.9598 (F1 0.9577). (p. 9)[^original]  
  <sub>anchor: "RF_SI_+_LSI_|0.9598|0.9564|0.9598|0.9577|"</sub>
- **descriptive / finding or result**: Table V gives MLP on SI as accuracy 0.7366, on LSI as 0.9331 and on SI+LSI as 0.9406 (F1 0.9385). (p. 9)[^original]  
  <sub>anchor: "MLP_SI_+_LSI_|0.9406|0.9376|0.9406|0.9385|"</sub>
- **descriptive / finding or result**: Table V gives XGB on SI as accuracy 0.7825, and on LSI as accuracy 0.9604 with F1 0.9590. (p. 9)[^original]  
  <sub>anchor: "XGB_LSI_|0.9604|0.9579|0.9604|0.9590|"</sub>
- **descriptive / finding or result**: LSI features perform much better than SI features; the average accuracy of the five models is 94.58% on LSI and 73.36% on SI. (p. 9)[^original]  
  <sub>anchor: "The average accuracy rates of these 5 models are 94.58% and 73.36% respectively on _LSI_ and _SI_ ."</sub>
- **descriptive / finding or result**: On KNN, accuracy improves by 25.56% when using LSI instead of SI, the largest increase among the models; on XGB the accuracy improves by at least 17.79%. (p. 9)[^original]  
  <sub>anchor: "on KNN, the accuracy rate improves by 25.56% after using _LSI_ instead of _SI_"</sub>
- **descriptive / finding or result**: Combining SI and LSI increases all metrics for all models except KNN, although the improvement is not significant; the authors take this as evidence that SI contains valuable features. (p. 9)[^original]  
  <sub>anchor: "it proves that there are valuable features in _SI_ and we will further analyze them in the next section."</sub>
- **descriptive / finding or result**: XGB gives the best results, above 96.46% on all metrics, and RF follows with results above 95.64%. (p. 9)[^original]  
  <sub>anchor: "XGB displays the best results that are all higher than 96.46% on all evaluation metrics"</sub>
- **descriptive / finding or result**: The metrics of DT and MLP are close, differing by fewer than 0.71%; MLP and KNN differ by 0.82% to 0.96%. MLP on SI alone reaches accuracy 73.66%, close to RF. (p. 9)[^original]  
  <sub>anchor: "the accuracy rate is 73.66% and is close to RF."</sub>
- **descriptive / finding or result**: The stated effect order of the five models on BABD-13 is XGB > RF > DT ≈ MLP > KNN. (p. 9)[^original]  
  <sub>anchor: "the effect order of these 5 models on BABD-13 is XGB _>_ RF _>_ DT _≈_ MLP _>_ KNN on BABD-13"</sub>
- **descriptive / finding or result**: The authors analysed relationships among the 148 features with a heatmap and conclude the five models perform well on BABD-13, which they consider meaningful for studying behavioural patterns, while some specific features need further consideration. (p. 9)[^original]  
  <sub>anchor: "it proves that BABD-13 is meaningful and helpful for further studying the behavioral patterns"</sub>

## D. Feature Selection

- **descriptive / method**: Feature importance is measured with scikit-learn's SelectKBest function and with the feature_importances attribute of specific models. (p. 9)[^original]  
  <sub>anchor: "We utilize two methods to measure the importance of each feature in BABD-13"</sub>

## B. Experiment Process

- **descriptive / method**: Five models are tested on BABD-13: KNN, decision tree, random forest, MLP and XGBoost, with stated scikit-learn and xgboost parameters, such as n_neighbors=4 for KNN and n_estimators=200 for random forest. (p. 9)[^original]  
  <sub>anchor: "KNN , built by function _KNeighborsClassifier_ () from _scikit-learn_"</sub>

## C. Result and Analysis

- **descriptive / finding or result**: With SI+LSI features, accuracy, precision, recall and F1-score reach at least 93.24%, 92.80%, 93.24% and 92.97%, and at most 96.71%, 96.46%, 96.71% and 96.57%. (p. 9)[^original]  
  <sub>anchor: "the accuracy rate, precision, recall, and f1-score can reach at least 93.24%"</sub>
- **descriptive / finding or result**: LSI features perform much better than SI features; average accuracy across the five models is 94.58% on LSI and 73.36% on SI. (p. 9)[^original]  
  <sub>anchor: "The average accuracy rates of these 5 models are 94.58% and 73.36% respectively"</sub>
- **descriptive / finding or result**: Accuracy on KNN improves by 25.56% when LSI is used instead of SI, the largest increase among the models, and at least 17.79% on XGB. (p. 9)[^original]  
  <sub>anchor: "on KNN, the accuracy rate improves by 25.56% after using _LSI_ instead of _SI_"</sub>
- **descriptive / finding or result**: Combining SI and LSI increases all metrics to some extent for all models except KNN; the authors say SI features are valuable even though the gain is not significant. (p. 9)[^original]  
  <sub>anchor: "it proves that there are valuable features in _SI_ and we will further analyze them"</sub>
- **descriptive / finding or result**: XGB gives the best results, above 96.46% on all metrics, with RF next at above 95.64%; the model effect order is XGB > RF > DT ≈ MLP > KNN. (p. 9)[^original]  
  <sub>anchor: "XGB displays the best results that are all higher than 96.46% on all evaluation metrics"</sub>
- **descriptive / finding or result**: Using only SI, MLP reaches 73.66% accuracy, close to RF's performance in that setting. (p. 9)[^original]  
  <sub>anchor: "the accuracy rate is 73.66% and is close to RF"</sub>

## D. Feature Selection

- **descriptive / method**: Feature importance is measured two ways: scikit-learn's SelectKBest for general single-feature selection and the feature_importances attribute for a specific model. (p. 9)[^original]  
  <sub>anchor: "one is the function _SelectKBest_ () from _scikit-learn_"</sub>
- **descriptive / finding or result**: The top 10 features listed are: maximum out-degree in Gk (S2-2); standard deviation of in- and out-degree in Gk (S1-6); standard deviation of in-degree in Gk (S1-2); degree correlation of Gk (S3); RAain3min (PAIa21-1); ATImin (PTIa41-2); longest distance between any two nodes in Gk (S6); closeness centrality (S5 as labelled in the text); delta RAin2max (CI3a32-2); and density of Gk (S7). (p. 10)[^original]  
  <sub>anchor: "The degree correlation of _Gk_ (S3)."</sub>
- **descriptive / finding or result**: The top-ranked feature per indicator type is: PAI, RAain3min (PAIa21-1); PDI, out-degree of an address (PDIa1-2); PTI, ATImin (PTIa41-2); CI, delta RAin2max (CI3a32-2); and LSI, maximum out-degree in Gk (S2-2). (p. 10)[^original]  
  <sub>anchor: "_PDI_ : The out-degree of an address (PDIa1-2)."</sub>

## E. Model Improvement by Selected Features

- **descriptive / finding or result**: Re-selecting SI features raises KNN accuracy by 1.20%, and RF and XGB accuracy by 0.37% and 0.42%; XGB reaches a new highest accuracy of 97.13% with the selected features. (p. 10)[^original]  
  <sub>anchor: "the accuracy rate increases by 1.20% on KNN which is obvious."</sub>
- **descriptive / finding or result**: The authors conclude that the SI+LSI combination can be re-selected within SI to improve performance across different models, but the effect of a feature can differ between models and would require testing many combinations, which is left to future work. (p. 10)[^original]  
  <sub>anchor: "The experimental results prove that the current feature combination, i.e., _SI+LSI_ can be re-selected in _SI_"</sub>

## F. Feature Analysis

- **descriptive / finding or result**: For the top feature of the PAI type, the data distributions of all address types show two peaks, are symmetric with different shapes, and have symmetry axes around 0.5. (p. 10)[^original]  
  <sub>anchor: "the data distributions of all types of addresses on this feature are symmetric with different shapes"</sub>

## D. Feature Selection

- **descriptive / finding or result**: The top-ranked features include the maximum out-degree in Gk (S2-2), the standard deviation of in-degree and out-degree in Gk (S1-6), and the degree correlation of Gk (S3). (p. 10)[^original]  
  <sub>anchor: "The maximum out-degree in _Gk_ (S2-2)."</sub>
- **descriptive / finding or result**: The top feature of each indicator type is PAI: RAa_in_3 min (PAIa21-1); PDI: out-degree of an address (PDIa1-2); PTI: PTIa41-2; CI: CI3a32-2; LSI: maximum out-degree in Gk (S2-2). (p. 10)[^original]  
  <sub>anchor: "_PDI_ : The out-degree of an address (PDIa1-2)."</sub>

## E. Model Improvement by Selected Features

- **descriptive / finding or result**: Re-selecting SI features raises KNN accuracy by 1.20%, RF and XGB accuracy by 0.37% and 0.42%, and XGB reaches a new highest accuracy of 97.13%. (p. 10)[^original]  
  <sub>anchor: "the accuracy rate increases by 1.20% on KNN which is obvious"</sub>
- **descriptive / limitation**: The same feature may have a positive or negative effect depending on the model, so testing many feature combinations is costly; the effect on different models is left to future work. (p. 10)[^original]  
  <sub>anchor: "the same feature might have an unequal influence (positive or negative)"</sub>

## F. Feature Analysis

- **descriptive / finding or result**: In Fig. 4(a) the data distributions of all address types have two peaks and are symmetric with different shapes around an axis near 0.5. (p. 10)[^original]  
  <sub>anchor: "the symmetry axes are around 0.5."</sub>

## COMPARISON WITH OTHER SCHEMES

- **descriptive / finding or result**: Table VI compares BABD with other schemes: BABD covers Jul. 12, 2019 to May 26, 2021, a graph of 516,167,131 nodes and 713,703,239 edges, sample size 544,462, 148 features, 13 types, methods DT, KNN, MLP, RF and XGB, best accuracy 97.1%, and year 2022. (p. 11)[^original]  
  <sub>anchor: "Jul. 12, 2019_∼_May 26, 2021"</sub>
- **descriptive / finding or result**: Table VI lists scheme [13] as a transaction-node study with a graph of 203,769 nodes and 234,355 edges, sample size 46,564, 166 features, 2 types, GCN, LR, MLP and RF methods, and best precision 97.1%, recall 66.80% and F1 98.6%, from 2019. (p. 11)[^original]  
  <sub>anchor: "Precision: 97.1%Recall: 66.80%F1-score: 98.6%"</sub>
- **descriptive / finding or result**: Table VI lists scheme [11] with sample size 1,234,047, 92 features, 2 types, ANN, RF, SVM and XGB methods, and best precision 93.5%, recall 85.4% and F1 88.1%, from 2020. (p. 11)[^original]  
  <sub>anchor: "Precision: 93.5%Recall: 85.4%F1-score: 88.1%"</sub>
- **descriptive / finding or result**: Table VI lists scheme [8] with time range Sep. 29, 2011 to Apr. 22, 2015, sample size 972,866, AdaBoost, LR, MLP, RF and SVM methods, best precision 99.7%, recall 99.7% and F1 99.7%, from 2017. (p. 11)[^original]  
  <sub>anchor: "Precision: 99.7%Recall: 99.7%F1-score: 99.7%"</sub>
- **descriptive / finding or result**: Table VI lists scheme [41] with time range May 2, 2018 to May 3, 2018, sample size 8,808, 149 features, 6 types, DT, ET, NN, RF and SVM methods, best F1 96.0%, from 2020. (p. 11)[^original]  
  <sub>anchor: "F1-score: 96.0%"</sub>
- **descriptive / finding or result**: Table VI lists scheme [25] with time range Jan. 3, 2009 to Jun. 30, 2018, sample size 26,313, 64 features, 7 types, AdaBoost, LightGB, LR, MLP, NN, RF, SVM and XGB methods, best F1 87.0%, from 2019. (p. 11)[^original]  
  <sub>anchor: "F1-score: 87.0%"</sub>

## F. Feature Analysis

- **descriptive / finding or result**: Table VI compares BABD with other schemes; BABD covers 544,462 samples and 148 features across 13 types, reporting best accuracy of 97.1%, precision 96.9%, recall 97.1% and F1 97.0%. (p. 11)[^original]  
  <sub>anchor: "Accuracy: 97.1%Precision: 96.9%Recall: 97.1%F1-score: 97.0%"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Yuexin Xiang, Yuchen Lei, Bao Fu Ding, Tiantian Li, Qingqing Yang, Wenmao Liu et al., "BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis" (2023-12-28). https://arxiv.org/abs/2204.05746
