---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 9 of 9 (pp. 39-45)
description: 'Verbatim extracted text, pp. 39-45: AP; TPR; AUROC'
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
part: 9
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:42:06Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:42:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2405.19383
  title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation
  author: org:arxiv
  last_modified: '2024-05-29T00:00:00Z'
---

# Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation

[previous part](text-008.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 9 of 9, pp. 39-45. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## AP


[pp. 39-41]

and Maosong Sun. Graph neural networks: A review of methods and applications. AI Open, 1:57–81, 2020. ISSN 2666-6510. doi:https://doi.org/10.1016/j.aiopen.2021.01.001. URL https://www.sciencedirect. com/science/article/pii/S2666651021000012. [154] Yadong Zhou, Ximi Wang, Junjie Zhang, Peng Zhang, Lili Liu, Huan Jin, and Hongbo Jin. Analyzing and detecting money-laundering accounts in online social networks. IEEE Network, 32(3):115–121, 2017. doi:10.1109/MNET.2017.1700213.

Data - Crypto

1.0

Proprietary Open-source Synthetic

0.8

0.6

0.4

0.2

0.0

0 1 Bitcoin/Crypto

Figure A1: The data for papers dealing with crypto currencies (1) and those that do not (0).

A Analysis of Categories between Crypto and Non-Crypto Papers

This part of the appendix gives the plots in which we compare the difference in nature of the crypto-literature compared non-crypto-related research.

Data without Crypto

Data Crypto

Proprietary Open-source Synthetic

Proprietary Open-source Synthetic

Year

Year

(a) The evolution of the data over the years for papers not covering crypto currencies.

(b) The evolution of the data over the years for papers cov- ering crypto currencies.

Figure A2: Evolution of the data.

Data

Non-Crypto Crypto

0.4

0.3

0.2

0.1

0.0

Client classification

Flow/Chain Detection

Community detection

Transaction classification

Figure A3: The distribution of the objective of the papers.

Data

0.5

Non-Crypto Crypto

0.4

0.3

0.2

0.1

0.0

## TPR


[pp. 41-42] [ref: 0.7]

Time

Recall

Precision

Accuracy

Figure A4: The distribution of the evaluation metrics used.

B The Top-Cited Papers

In this part of the appendix, we give the figures that summarise the top-cited papers.

0.7 Method Type

0.6

0.5

0.4

0.3

0.2

0.1

0.0

Mixed

Supervised

Visualisation

Unsupervised

Semi-Supervised

Figure B1: The methods for the top-cited papers.

Modelling Method

0.5

0.4

0.3

0.2

0.1

0.0

Clustering

Deep repr.

## AUROC


[pp. 42-44]

Tree-based

Rule-based

SVM-based

Walk-based

Shallow repr.

Manual features

Neural Networks

Correlation-based

Logistic regression

Anomaly detection

Figure B2: The modelling methods for the top-cited papers.

Metric

0.200

0.175

0.150

0.125

0.100

0.075

0.050

0.025

0.000

Time

Recall

Precision

Accuracy

Figure B3: The performance metrics for the top-cited papers.

Objective

0.4

0.3

0.2

0.1

0.0

Client classification

Flow/Chain Detection

Community detection

Transaction classification

Figure B4: The objective of the top-cited papers.

Data

0.6

0.5

0.4

0.3

0.2

0.1

0.0

Synthetic

Proprietary

Open-source

Figure B5: The nature of the data of the top-cited papers.

Table C1: Threshold-dependent metrics: Precision, recall and F1-score values for the top 0.1% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

Intrinsic features 0.5396 ± 0.3093 0.0204 ± 0.0302 0.0383 ± 0.0542 Egonet features 0.6833 ± 0.3187 0.0129 ± 0.0060 0.0253 ± 0.0118 DeepWalk 0.5333 ± 0.3148 0.0101 ± 0.0059 0.0198 ± 0.0117 Node2vec 0.5167 ± 0.3352 0.0097 ± 0.0063 0.0191 ± 0.0124 GCN 1.0000 ± 0.0000 0.0189 ± 0.0007 0.0371 ± 0.0014 GraphSAGE 0.9624 ± 0.0615 0.0300 ± 0.0071 0.0580 ± 0.0133 GAT 1.0000 ± 0.0000 0.0187 ± 0.0005 0.0367 ± 0.0010 GIN 0.8500 ± 0.2540 0.0191 ± 0.0093 0.0372 ± 0.0179

Table C2: Threshold-dependent metrics: Precision, recall and F1-score values for the top 0.1% scores over the different methods for the IBM-AML data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

[p. 44]

Intrinsic features 0.0050 ± 0.0087 0.0007 ± 0.0011 0.0012 ± 0.0019 Egonet features 0.0079 ± 0.0085 0.0011 ± 0.0012 0.0019 ± 0.0020 DeepWalk 0.0076 ± 0.0085 0.0011 ± 0.0013 0.0019 ± 0.0022 Node2vec 0.0035 ± 0.0058 0.0006 ± 0.0009 0.0010 ± 0.0016 GCN 0.0103 ± 0.0047 0.8815 ± 0.3117 0.0203 ± 0.0092 GraphSAGE 0.0057 ± 0.0062 0.4919 ± 0.5188 0.0112 ± 0.0123 GAT 0.0054 ± 0.0087 0.1798 ± 0.3688 0.0095 ± 0.0156 GIN 0.0044 ± 0.0080 0.0102 ± 0.0131 0.0016 ± 0.0015

C Results Threshold-Dependent Metrics

In this part of the appendix, we give the precision, recall and F1-scores for the models using different thresholds. The thresholds are set such that the observations with the top 0.1%, 10% and p% of scores are classified as money laundering, where p% is equal to the relative occurrence of the labels.

Table C3: Threshold-dependent metrics: Precision, recall and F1-score values for the top 10% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

[pp. 44-45]

Intrinsic features 0.3526 ± 0.0163 0.6204 ± 0.0287 0.4497 ± 0.0208 Egonet features 0.3559 ± 0.0101 0.6263 ± 0.0179 0.4539 ± 0.0129 DeepWalk 0.3517 ± 0.0050 0.6189 ± 0.0089 0.4485 ± 0.0064 Node2vec 0.3536 ± 0.0040 0.6222 ± 0.0071 0.4509 ± 0.0051 GCN 0.3471 ± 0.0272 0.5988 ± 0.0358 0.4393 ± 0.0306 GraphSAGE 0.3675 ± 0.0118 0.6395 ± 0.0207 0.4666 ± 0.0124 GAT 0.3661 ± 0.0247 0.6388 ± 0.0288 0.4653 ± 0.0270 GIN 0.3307 ± 0.0228 0.5889 ± 0.0407 0.4234 ± 0.0274

Table C4: Threshold-dependent metrics: Precision, recall and F1-score values for the top 10% scores over the different methods for the IBM-AML data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

[p. 45]

Intrinsic features 0.0148 ± 0.0006 0.1635 ± 0.0063 0.0272 ± 0.0011 Egonet features 0.0148 ± 0.0002 0.1626 ± 0.0026 0.0271 ± 0.0004 DeepWalk 0.0145 ± 0.0003 0.1602 ± 0.0033 0.0267 ± 0.0005 Node2vec 0.0148 ± 0.0006 0.1630 ± 0.0065 0.0271 ± 0.0011 GCN 0.0109 ± 0.0030 0.9814 ± 0.0374 0.0214 ± 0.0058 GraphSAGE 0.0121 ± 0.0026 0.9761 ± 0.0257 0.0238 ± 0.0051 GAT 0.0054 ± 0.0074 0.1993 ± 0.3722 0.0104 ± 0.0144 GIN 0.0081 ± 0.0077 0.0947 ± 0.0793 0.0149 ± 0.0141

Table C5: Threshold-dependent metrics: Precision, recall and F1-score values for the top p = 2% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

Intrinsic features 0.3244 ± 0.0143 0.6303 ± 0.0277 0.4283 ± 0.0188 Egonet features 0.3271 ± 0.0098 0.6357 ± 0.0190 0.4319 ± 0.0129 DeepWalk 0.3220 ± 0.0052 0.6258 ± 0.0102 0.4252 ± 0.0069 Node2vec 0.3241 ± 0.0046 0.6299 ± 0.0089 0.4280 ± 0.0060 GCN 0.3209 ± 0.0284 0.6230 ± 0.0371 0.4234 ± 0.0325 GraphSAGE 0.3343 ± 0.0130 0.6558 ± 0.0166 0.4427 ± 0.0121 GAT 0.3419 ± 0.0084 0.6613 ± 0.0212 0.4507 ± 0.0109 GIN 0.3034 ± 0.0169 0.5949 ± 0.0285 0.4018 ± 0.0205

Table C6: Threshold-dependent metrics: Precision, recall and F1-score values for the top p = 0.11% scores over the different methods for the Elliptic data set, based on the test set. The standard deviation is also reported.

Methods Precision Recall F1-score

Intrinsic features 0.0056 ± 0.0090 0.0008 ± 0.0012 0.0014 ± 0.0021 Egonet features 0.0085 ± 0.0077 0.0012 ± 0.0011 0.0021 ± 0.0019 DeepWalk 0.0080 ± 0.0076 0.0013 ± 0.0013 0.0023 ± 0.0021 Node2vec 0.0047 ± 0.0063 0.0008 ± 0.0010 0.0013 ± 0.0018 GCN 0.0103 ± 0.0046 0.8811 ± 0.3119 0.0203 ± 0.0089 GraphSAGE 0.0055 ± 0.0061 0.4907 ± 0.5175 0.0108 ± 0.0121 GAT 0.0047 ± 0.0078 0.1763 ± 0.3656 0.0085 ± 0.0146 GIN 0.0058 ± 0.0084 0.0091 ± 0.0116 0.0019 ± 0.0016


---

[previous part](text-008.md) | [source overview](overview.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
