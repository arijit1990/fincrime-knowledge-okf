---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 6 of 9 (pp. 25-31)
description: 'Verbatim extracted text, pp. 25-31: D; AUC; AP'
resource: https://arxiv.org/abs/2405.19383
tags:
- academic_finding
- effectiveness
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-network-analytics-for-anti-money-laundering-a-systematic-literat
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-05-29'
legal_status: unknown
part: 6
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2405.19383
  title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation
  author: org:arxiv
  last_modified: '2024-05-29T00:00:00Z'
---

# Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 6 of 9, pp. 25-31. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## D


[p. 25] [ref: 5.2]

The results on the IBM data set in Table 15 show a different picture. Only the egonet features improve performance. The threshold-dependent metrics show a similar picture.

One explanation for the poor performance of GNNs might be related to the network structure (Section 4.2), with very short average paths and many high-degree nodes. This results in strong over-smoothing [77], resulting in very similar embeddings for the different nodes with insufficient discriminatory power.

Moreover, a deeper analysis reveals that the training loss, when training on the train and validation set, is highly unstable. Depending on the epoch and specific weight initialization, the results vary widely, with the models sometimes just predicting the majority class. For this specific data set, GNNs seem to face instability due to the extreme class imbalance.

The supervised learning experiments on both data sets demonstrate that the network structure provides additional insights for anti-money laundering. The observed performance improvements are limited, but even a small relative increase in performance has material implications for the business. The efficiency of AML practices increases significantly since investigators have more high quality predictions, and spend less time on the investigation of false positives.

However, depending on the network topology and the extent of the class imbalance, GNNs might be too unstable. Additional experiments are needed to quantify the sensitivity of GNNs to the imbalance, but this is outside the scope of this research.

5.2 Unsupervised Learning

The results of the unsupervised methods using isolation forests are given in Tables 18. None of the results on the Elliptic data set are particularly good, with AUC-ROC values below 0.5. For completeness, we also include the threshold-dependent metric in Table 19, where most models fail to detect any money laundering cases.

These results are in line with a previous study performed by Lorenz et al. [83] who tested anomaly detection methods on the Elliptic data set. The authors did not include any additional network analytics methods and only reported the F1 score. However, they found that across the methods, the anomaly detection results were much worse than for supervised learning, with reported F1-scores for the isolation forest equal to 0.

We perform additional analyses on these results. Figure 8 shows the anomaly scores for the intrinsic features for the Elliptic data set. Here, a very negative score signifies anomalies. All money laundering cases have scores near zero, within the bulk of the distribution, indicating that the isolation forest does not recognize these cases as anomalies.

Conversely, the results for IBM-AML are more in line with expectations. Network information captured by DeepWalk, results in the best performing model here. Comparing these results to those in Table 15, we see that DeepWalk even outperforms the supervised learning methods in terms of AUC-PR.

[pp. 25-26] [ref: 0.7]

The most plausible explanation in our opinion lies in the assumptions underlying isolation forest and the data generating process. Two specific assumptions by Liu et al. [80]:

• Anomalies yield fewer partitions since anomalies occupy regions with lower density;

• Instances with distinct attributes are separated earlier in the tree, contributing to shorter paths.

Therefore, the nature of the data sets explains the difference in performance. The Elliptic data set is a real-life data set, containing criminals that actively attempt to cover their tracks [10]. They try to mimic the ‘average behaviour’, but no real transaction/person is average on all attributes. This is why it seems that classifying the least suspicious

Histogram of Anomaly Scores by True Label

Legit Money Laundering

Count (log scale)

0.7 0.6 0.5 0.4 Anomaly Score

Figure 8: The anomaly scores for the legitimate and money laundering cases. More negative is more anomalous.

Table 18: Threshold-independent metrics: AUC-ROC and AUC-PR values over the different methods for the two data set, based on the test set. The standard deviation is also reported.

Unsupervised Elliptic IBM-AML Methods AUC-ROC AUC-PR AUC-ROC AUC-PR

Intrinsic features 0.134 ± 0.007 0.058 ± 0.001 0.710 ± 0.015 0.017 ± 0.003 Egonet features 0.217 ± 0.010 0.013 ± 0.000 0.700 ± 0.033 0.011 ± 0.005 DeepWalk 0.182 ± 0.008 0.056 ± 0.001 0.744 ± 0.023 0.024 ± 0.008 Node2vec 0.190 ± 0.008 0.056 ± 0.0005 0.632 ± 0.031 0.005 ± 0.001

transactions as money launderers, we would achieve an AUC-ROC around 80%. Hence, transactions that appear ‘too normal’ are actually most suspicious. In contrast, the IBM-AML data set is synthetic, with fraudulent patterns and behaviours deliberately introduced. It is likely that camouflage behaviour is not present in this data set.

These insight highlights the importance of knowing the exact assumptions underlying the data sets used. Synthetic data sets might give overly optimistic results, since complex behaviour inherent to the problem at hand are not captured.

5.3 Ablation Study

[pp. 26-27]

To better understand the effect of the network structure on the predictive power of the models, we analyse the performance of the different models without intrinsic features. For the models, we take the hyperparameters as determines in Table 13 and Table 14. The GNNs require feature values, so we give each node a dummy feature with value 1 [128]. Additionally, for the Elliptic data set, we have no control on the summary features, so we discard these as well, although they represent some network structure.

Table 19: Threshold-dependent metrics: Precision, recall and F1-score values for the top 1% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Elliptic Unsupervised Methods Precision Recall F1-score

Intrinsic features 0.000 ± 0.000 0.000 ± 0.000 0.000 ± 0.000 Egonet features 0.000 ± 0.000 0.000 ± 0.000 0.000 ± 0.000 DeepWalk 0.005 ± 0.005 0.001 ± 0.001 0.001 ± 0.001 Node2vec 0.003 ± 0.004 0.000 ± 0.000 0.001 ± 0.001

Table 20: Threshold-dependent metrics: Precision, recall and F1-score values for the top 1% scores over the different methods for the IBM-AML data set, based on the test set. The standard deviation is also reported.

IBM-AML Unupervised Methods Precision Recall F1-score

Intrinsic features 0.042 ± 0.005 0.156 ± 0.020 0.067 ± 0.008 Egonet features 0.027 ± 0.013 0.098 ± 0.048 0.042 ± 0.021 DeepWalk 0.055 ± 0.009 0.204 ± 0.034 0.087 ± 0.015 Node2vec 0.007 ± 0.002 0.025 ± 0.008 0.010 ± 0.003

Table 21: Threshold-independent metrics: AUC-ROC and AUC-PR values over the different methods for the two data sets, based on the test set. The standard deviation is also reported.

Supervised Elliptic IBM-AML Methods AUC-ROC AUC-PR AUC-ROC AUC-PR

[p. 27]

Egonet features 0.5172 ± 0.0607 0.0630 ± 0.0122 0.4758 ± 0.0187 0.0088 ± 0.0003 DeepWalk 0.5125 ± 0.0184 0.0597 ± 0.0021 0.5019 ± 0.0143 0.0092 ± 0.0004 Node2vec 0.4454 ± 0.0118 0.0511 ± 0.0021 0.4931 ± 0.0095 0.0091 ± 0.0003 GCN 0.5655 ± 0.0139 0.0696 ± 0.0039 0.4985 ± 0.0183 0.0092 ± 0.0007 GraphSAGE 0.5000 ± 0.0000 0.0565 ± 0.0025 0.5050 ± 0.0081 0.0093 ± 0.0003 GAT 0.5002 ± 0.0032 0.0566 ± 0.0018 0.5014 ± 0.0035 0.0091 ± 0.0002 GIN 0.6177 ± 0.0110 0.0739 ± 0.0049 0.5061 ± 0.0035 0.0092 ± 0.0003

The results for supervised learning are given in Table 21. The AUC values indicate that most methods based purely on the network structure are close to random.

One notable exception is GIN, which is specifically designed to better distinguish certain graph structures [144]. Graph structure is the only information available in this part of the experiments. The results for GIN indicate that there are some structural difference in the network for fraudulent and non-fraudulent nodes in the Elliptic data set. These structural difference are complex, since they are not picked up by the egonet features or the random-walk-based ones.

The other GNN architectures struggle, since they rely heavily on the node features. Especially GAT—which performed well with features—leverages node features for the attention calculations.

For the IBM data set, the differences are less pronounced that for the Elliptic data set. The network structure alone might not be enough to uncover money laundering. The data generation process of this synthetic data set creates a direct correlation between the money laundering pattern and feature values. Therefore, these feature values are more important than the network structure.

[pp. 27-28] [ref: 5.4]

The results for the isolation forest in Table 22 show an improvement for the Elliptic data set, compared to the isolation forest with intrinsic features. Here, however, the models mostly make random predictions. When including the features, a better distinction can be made between money and non-money laundering. As mentioned before, the features of the money laundering transactions are so average (not anomalous according to the isolation forest) that they become suspicious again. The inverse predictions were in that case very good predictors. When only considering the network structure, it is harder to find meaningful anomalies. Hence, a higher AUC in this case points to a less useful model, as the model is as good as random.

The results on the IBM data set are in line with what we have seen before. The model makes almost random predictions, with deepwalk giving the best AUC-ROC and AUC-PR values.

This ablation study showed that it seems that network structure alone is not enough to come to a performant AML model. There is an important interplay between the network and the node features, pointing to a need to combine the two. Additionally, it highlighted the strong dependence of GNNs on these node features—except for the GIN in some cases—and on the data generation process. The explicit correlation between the money laundering cases and feature values for the IBM data set resulted in sub-optimal results when only considering the network structure.

5.4 Model Stability

As a final analysis, we look at the range of the results to assess model stability. Figure 9 present the box plots of the results for the models on the ten different training sets.

Table 22: Threshold-independent metrics: AUC-ROC and AUC-PR values over the different methods for the two data sets, based on the test set. The standard deviation is also reported.

Supervised Elliptic IBM-AML Methods AUC-ROC AUC-PR AUC-ROC AUC-PR

Egonet features 0.5254 ± 0.0120 0.0226 ± 0.0008 0.4737 ± 0.0057 0.0027 ± 0.0000 DeepWalk 0.4337 ± 0.0064 0.0834 ± 0.0013 0.5380 ± 0.0081 0.0031 ± 0.0001 Node2vec 0.4231 ± 0.0050 0.0815 ± 0.0010 0.4910 ± 0.0092 0.0026 ± 0.0001

AUC-ROC for elliptic dataset

AUC-ROC for ibm dataset

0.875

0.7

0.6

0.850

## AUC


[p. 28]

0.5

0.825

0.4

0.800

0.3

0.775

gin

gin

gat

gat

gcn

gcn

sage

sage

intrinsic

intrinsic

deepwalk

deepwalk

positional

positional

node2vec

node2vec

Method

Method

AUC-PR for elliptic dataset

AUC-PR for ibm dataset

0.7

0.020

0.6

0.015

0.5

0.010

0.4

0.005

gin

gin

gat

gat

gcn

gcn

sage

sage

intrinsic

intrinsic

deepwalk

deepwalk

positional

positional

node2vec

## AP


[pp. 28-29] [ref: 6.1]

node2vec

Method

Method

Figure 9: Box plots of the AUC-ROC and AUC-PR for the ten different training sets.

The results are quite stable on the Elliptic data set, although the AUC-ROC shows a bit more variability for the GNNs. The values on the IBM data set show strong instability for all GNNs, while the other models are relatively stable. The GNNs are probably less stable on the IBM data set due to the larger class imbalance.

6 Conclusion

6.1 Literature Review

This paper present a literature review on network analytics for anti-money laundering. The 97 selected papers were processed in two steps to achieve (1) a comprehensive understanding of the broader literature and (2) detailed insight into research that has been well received by the community. The comprehensive analysis classified all papers according to seven categories, each having different sub-characteristics. The detailed analysis was performed on the 10% most-cited papers in scope, which were further categorized using the framework recently proposed by Bockel-Rickermann et al. [14]. Information was given on the different processing steps taken, the challenges faced or addressed in the papers, the experiments performed, and the definition of nodes and edges in the networks.

A large part of the literature concerns methods that rely heavily on expert-knowledge by applying manual feature engineering and rule-based methods. Most of these are based on basic network centrality metrics.

The analysis and comparison of the models is mostly done using threshold-dependent metric, most notably accuracy, precision and recall. Given the class imbalance, we strongly advise against the use of accuracy as an evaluation metric

for AML models. Instead, the AML research should adopt the threshold-independent AUC-PR as a standard evaluation metric, as this is well suited for model comparison in the presence of high class imbalance.

Our analysis of the literature identified six critical gaps that future research must address:

1. Benchmark: There is a lack of comparison of novel methods with other models in the literature. This shows that there is a need for a unified approach to perform test including standard open-source data sets on which to test as well as a consensus on which methods can be seen as baseline models and which as state-of-the-art.

2. Interpretability: Few studies have explored tools to explain the outputs of graph neural networks (GNNs), which is essential for regulatory and operational transparency.

3. Unsupervised Methods: Limited exploration of classic unsupervised methods restricts their potential to detect anomalies, a key requirement as money laundering tactics evolve.

4. Dynamic Network Analysis: Most approaches rely on static networks, with insufficient research into dynamic methods that could better capture the temporal nature of transactions.

[p. 29] [ref: 6.2]

5. Fraud Specific Methods: The inherent incompleteness of AML labels, due to undetected cases and resource constraints, highlights the need for specialized PU-learning techniques, while limited resources necessitate actionable, prioritized predictions, which could be achieved through learning-to-rank methods.

6. Adoption State-of-the-Art: AML is often done using basic network metrics, while new developments in the field are adopted slowly. There is a need for standardising the use of heterogeneous and dynamic networks in AML. Future work should study how this can be achieved by comparing the latest state-of-the-art in continual graph learning, graph contrastive learning, heterogeneous and temporal GNNs, and graph transformers for AML, to name a few.

6.2 Experimental Evaluation

To extend upon the existing body of knowledge and to partially address the gaps in the literature, we implemented an extensive experimental evaluation covering manual feature engineering, shallow and deep representation learning, both in a supervised and unsupervised setting. We can that network features bring additional predictive power to AML models, when combined with the node features. However, the GNNs struggled when faced with extreme class imbalance and with a network with many hubs.

The observed performance improvements were limited, but even a small relative increase in performance has material implications for the business. The efficiency of AML practices increases significantly since investigators have more high quality predictions, and spend less time on the investigation of false positives.

In the unsupervised learning experiments, we employed isolation forests and observed notable differences between the real-world Elliptic data set and the synthetic IBM-AML data set. Although on synthetic data, the methods performed well, the observations from the Elliptic data seemed to exhibit strong camouflaging tactics. The anomaly scores of the latter were so low that investigating the least suspicious transactions for money laundering became the better strategy. We conclude from this that care should be taken when testing methods on synthetic data, since it can give overly optimistic results.

Our experiments on unsupervised learning are, however, limited. We only applied an isolation forest, which is a global anomaly detection method. Future work should focus on extending this to a larger benchmark, in line with the work of Lorenz et al. [83], to analyse if the same conclusions hold for other global and local anomaly detection methods.

The additional ablation study highlighted the need to incorporate both the network and feature information. When excluding the node features, the model predictions are as good as random. While this approach is common in the literature, we recommend against relying solely on the network structure.

6.3 Limitations

There are limitations to our work that should be addressed in future research.

[pp. 29-30]

First, conclusions are drawn based on only two data sets. To generalise our conclusions, additional tests need to be performed on a broader range of data sets. This can be done by including more open-source data sets when these become available, and rely on practitioners to use our code to test the methods on their proprietary data and publish the results.

Second, the decoders were always based on neural networks. The application and impact analysis of applying different machine learning methods as down-stream classifiers is another interesting area of study to extend the experiments presented here.

Third, the hyperparameter tuning process was limited. While Optuna provided an efficient method for hyperparameter search, the 50 to 100 tuning rounds used in this study may be insufficient. The choices in this paper were made to keep everything tractable and feasible given the limited resources available. Future work could expand the parameter ranges and number of tuning rounds.

Acknowledgments

This work was supported by the Research Foundation – Flanders (FWO research project 1SHEN24N) and by the BNP Paribas Fortis Chair in Fraud Analytics. The resources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government.

References

[1] Florian Adriaens, Cigdem Aslay, Tijl De Bie, Aristides Gionis, and Jefrey Lijffijt. Discovering interesting cycles

in directed graphs. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management, pages 1191–1200, 2019.

[2] Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama. Optuna: A next-generation

hyperparameter optimization framework. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2019.

[3] Leman Akoglu, Hanghang Tong, and Danai Koutra. Graph based anomaly detection and description: a survey. Data Mining and Knowledge Discovery, 29(3):626–688, 2015. doi:10.1007/s10618-014-0365-y. URL https://doi.org/10.1007/s10618-014-0365-y.

[4] Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. Comparative analysis using supervised learning

[p. 30]

methods for anti-money laundering in bitcoin. In Proceedings of the 2020 5th International Conference on Machine Learning Technologies, ICMLT ’20, page 11–17, Beijing, China, 2020. Association for Computing Machinery. ISBN 9781450377645. doi:10.1145/3409073.3409078. URL https://doi.org/10.1145/ 3409073.3409078.

[5] Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. Competence of graph convolutional networks

for anti-money laundering in bitcoin blockchain. In Proceedings of the 2020 5th International Conference on Machine Learning Technologies, ICMLT ’20, page 23–27, Beijing, China, 2020. Association for Computing Machinery. ISBN 9781450377645. doi:10.1145/3409073.3409080. URL https://doi.org/10.1145/ 3409073.3409080.

[6] Erik Altman, Jovan Blanuša, Luc von Niederhäusern, Beni Egressy, Andreea Anghel, and Ku- bilay Atasu. Realistic synthetic financial transactions for anti-money laundering models. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Ad- vances in Neural Information Processing Systems, volume 36, pages 29851–29874. Curran As- sociates, Inc., 2023. URL https://proceedings.neurips.cc/paper_files/paper/2023/file/ 5f38404edff6f3f642d6fa5892479c42-Paper-Datasets_and_Benchmarks.pdf.

[7] Eugenio Angriman, Alexander van der Grinten, Michael Hamann, Henning Meyerhenke, and Manuel Pen-

schuck. Algorithms for Large-Scale Network Analysis and the NetworKit Toolkit, pages 3–20. Springer Nature Switzerland, Cham, 2022. ISBN 978-3-031-21534-6. doi:10.1007/978-3-031-21534-6_1. URL https://doi.org/10.1007/978-3-031-21534-6_1.

[8] Henrique S Assumpção, Fabrício Souza, Leandro Lacerda Campos, Vinícius T de Castro Pires, Paulo M Laurentys

[pp. 30-31]

de Almeida, and Fabricio Murai. Delator: Money laundering detection via multi-task learning on large transaction graphs. In 2022 IEEE International Conference on Big Data (Big Data), pages 709–714. IEEE, 2022. doi:10.1109/BigData55660.2022.10021010.

[9] LAa Badalov, SDa Belov, and ISa Kadochnikov. Checking foreign counterparty companies using big data. In

CEUR Workshop Proceedings, volume 2267, pages 523–527, 2018.

[10] Bart Baesens, Veronique Van Vlasselaer, and Wouter Verbeke. Fraud analytics using descriptive, predictive, and

social network techniques: a guide to data science for fraud detection. John Wiley & Sons, Inc, 2015. ISBN 9781119133124. doi:10.1002/9781119146841.

[11] Ashwin Bahulkar, N Orkun Baycik, Thomas Sharkey, Yeming Shen, Boleslaw Szymanski, and William Wallace.

Integrative analytics for detecting and disrupting transnational interdependent criminal smuggling, money, and money-laundering networks. In 2018 IEEE International Symposium on Technologies for Homeland Security (HST), pages 1–6. IEEE, 2018. doi:10.1109/THS.2018.8574121.

[12] Luigi Bellomarini, Davide Magnanimi, Markus Nissl, and Emanuel Sallinger. Neither in the programs nor

in the data: Mining the hidden financial knowledge with knowledge graphs and reasoning. In Mining Data for Financial Applications: 5th ECML PKDD Workshop, MIDAS 2020, Ghent, Belgium, September 18, 2020, Revised Selected Papers 5, pages 119–134. Springer, 2021.

[13] Rasika Bhalerao, Maxwell Aliapoulios, Ilia Shumailov, Sadia Afroz, and Damon McCoy. Mapping the under-

ground: Supervised discovery of cybercrime supply chains. In 2019 APWG Symposium on Electronic Crime Research (eCrime), pages 1–16. IEEE, 2019. doi:10.1109/eCrime47957.2019.9037582.

[14] Christopher Bockel-Rickermann, Tim Verdonck, and Wouter Verbeke. Fraud analytics: A decade of research:


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
