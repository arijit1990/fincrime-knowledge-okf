---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 1 of 9 (pp. 1-6)
description: 'Verbatim extracted text, pp. 1-6: A PREPRINT; ABSTRACT; F1; and 1 more sections'
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
part: 1
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

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 1 of 9, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## A PREPRINT


[p. 1]

Bruno Deprez∗

Toon Vanderschueren

Bart Baesens

KU Leuven University of Antwerp - imec

KU Leuven University of Antwerp - imec

KU Leuven University of Southampton

Wouter Verbeke

Tim Verdonck University of Antwerp - imec

KU Leuven

KU Leuven

Money laundering presents a pervasive challenge, burdening society by financing illegal activities. The use of network information is increasingly being explored to effectively combat money laundering, given it involves connected parties. This led to a surge in research on network analytics for anti- money laundering (AML). The literature is, however, fragmented and a comprehensive overview of existing work is missing. This results in limited understanding of the methods to apply and their comparative detection power. This paper presents an extensive and unique literature review, based on 97 papers from Web of Science and Scopus, resulting in a taxonomy following a recently proposed fraud analytics framework. We conclude that most research relies on expert-based rules and manual features, while deep learning methods have been gaining traction. This paper also presents a comprehensive framework to evaluate and compare the performance of prominent methods in a standardized setup. We compare manual feature engineering, random walk-based, and deep learning methods on two publicly available data sets. We conclude that (1) network analytics increases the predictive power, but caution is needed when applying GNNs in the face of class imbalance and network topology, and that (2) care should be taken with synthetic data as this can give overly optimistic results. The open-source implementation facilitates researchers and practitioners to extend this work on proprietary data, promoting a standardized approach for the analysis and evaluation of network analytics for AML.

## ABSTRACT


[pp. 1-2]

Keywords Fraud Analytics · Anti-Money Laundering · Network Analytics · Literature Review

arXiv:2405.19383v4 [cs.SI] 22 Jul 2025

1 Introduction

Money laundering is the process of concealing illegally obtained funds by passing them through a complex sequence of transactions, so the money can be used to fund further criminal activities, e.g., drug trafficking, and terrorism [75]. The United Nations Office on Drugs and Crime [126] estimates that around 2% to 5% of global GDP is laundered worldwide, amounting yearly to USD 2 trillion.

In contrast to credit card fraud, money laundering occurs over a longer duration and requires analysis of multiple transactions for detection. It is actively concealed, since sustained laundering is needed to process continuous money streams. Credit card fraud, on the other hand, aims to get as much money out as fast as possible. Hence, the specific characteristics of money laundering merit dedicated research attention.

∗Correspondening author: bruno.deprez@kuleuven.be

Since this money needs to enter the financial system at some point [75], legislators have put stringent rules on financial institutions [15] for reporting suspicious transactions. Despite record fines and mounting pressure by regulators, money laundering represents a growing problem [135].

Money laundering typically involves three stages [126, 75]: placement, where illicit funds enter the financial system; layering, where transactions obscure their origin; and integration, where the funds re-enter the economy through seemingly legitimate means, completing the laundering process.

Anti-money laundering practices require constant monitoring of clients and transactions. These practices are, however, largely ineffective [35], with Europol estimating only 1.1% of criminal profits in the EU being confiscated [38].

Effective money laundering involves multiple parties, with individual transactions appearing normal [15]. Therefore, network analytics is essential [15, 10]. This need was already mentioned three decades ago by Senator et al. [113], where the authors used visualisations to support expert investing.

The increasing attention of the past years has resulted in a growing body of literature on network analytics for anti-money laundering, but simultaneously resulted in a lack of comprehensive overviews. Therefore, as a first step, this paper aims to supplement the literature by providing a comprehensive literature review of network analytics (NA) for anti-money laundering, covering 97 papers analysed according to multiple dimensions.

Due to the fragmented nature of the literature there is limited insight into which methods perform best. This fragmen- tation and lack of comparison is apparent in the fact that many of the introduced methods are not tested against any baselines. Furthermore, researchers are slow to adopt the latest network analytics methods and graph neural network in anti-money laundering. Therefore, the second goal of this work is to present a structured experimental set-up to evaluate the most prominent methods.

In summary, our main contributions are four-fold:

[pp. 2-3] [ref: 2.1]

• We provide an extensive and critical literature review on network analytics for anti-money laundering, to gain comprehensive and deep insights, and provide directions for future research.

• We benchmark a range of state-of-the-art network analytics methods for anti-money laundering, comparing the performance on two open-source data sets.

• We provide insights into the specific challenges of network methods based on the topology of the network and the data generating process.

• We implement the methods in a uniform manner and facilitate replication of the presented results by pro- viding public access to the code at https://github.com/B-Deprez/AML_Network, aiming to promote a standardized approach towards the analysis and adoption of NA for AML and to encourage further research.

This paper is structured as follows. We present the methodology for the literature review in Section 2, with Section 3 presenting the results and analysis. Section 4 describes the the empirical evaluation, with the results presented in Section 5. Overall conclusions and directions for future work are presented in Section 6.

2 Literature Review

The first part of this work covers the current literature. A summary is given according to multiple categories. Additional analyses are provided for the top-cited papers. The aim is to provide answers to the following research questions:

• What are the most prominent learning methods in the literature and how have these evolved over time?

• How are methods evaluated, using what data sets and evaluation metrics?

• What is the setting, objectives and challenges discussed in the top-cited papers?

2.1 Methodology

We conducted the literature search using the queries “graph analy*” AND “money launder*” and “network analy*” AND “money launder*” on WoS and Scopus, chosen for their high completeness and research credibility [96, 14]. The

search is limited to English-language papers published before 2023, excluded recent publications to ensure adequate time for community evaluation.

The selection process included a title and abstract scan, followed by a full-text review. Papers were excluded if they focused on legal aspects or lacked substantial application of network analytics to anti-money laundering (AML). The

final set of papers is classified according to seven criteria as summarised in Table 1: publication data, method type, modelling approach, evaluation metrics, main objectives, data type, and network characteristics.

Our review provides both a broad analysis of trends across all selected papers and an in-depth focus on top-cited works (top 10% annually and overall, per Google Scholar). This dual approach highlights general trends and the state-of-the-art (SOTA) in the field. Finally, we examine relevant review papers to contextualize our findings and demonstrate how our work extends existing literature.

Table 1: The (sub-)categories with explanation for the classification of the literature. Category Sub-Category Definition

Publication Data

[pp. 3-4] [ref: 2.2]

Title The full title of the paper Journal/Conference Where the paper is published Year The year of publication Review Paper Indicating if it is a review paper Bitcoin/Crypto Indicating if it deals with crypto currency

Method Type

Supervised Application of supervised method Unsupervised Application of unsupervised method Semi-Supervised Application of semi-supervised method Mixed Methods presented across different learning methods Visualisation Application of visualisation method

Modelling Method

Rule-based Application of specific rules or cut-offs Manual features Network features having a exact definition Walk-based Network analysis based on (random) walks Shallow representation Embeddings typically through matrix factorization or random walks, without employing deep neural networks Deep representation Embeddings based on deep neural networks, e.g., GNNs Correlation-based Analysis of correlation of network features with target Logistic regression Application of logistic regression Tree-based Application of tree-based methods SVM-based Application of support vector machines Neural networks Learning using neural networks Anomaly detection Application of anomaly or outlier detection Clustering Features based on community detection or clustering of features

Evaluation Metric

Accuracy Accuracy Precision The precision Recall The recall F1 The F1 or micro-F1 score TPR The true positive rate FPR The false positive rate AUC-ROC The area under the ROC curve AUC-PR The area under the precision-recall curve Time The execution time

Objective

Client classification Detection of suspicious entities Transaction classification Detection of suspicious transactions Community detection Detection of suspicious groups of clients Flow/Chain detection Detection of suspicious combination of transactions

Data

Proprietary Usage of confidential data Open-source Usage of freely available data Synthetic Usage of synthetically generated data

Network Multiple Usage of multiple networks Inverse/undirected Additional use of network with directions removed or reverted

Systematic Review NA Methods

Web of Science Scopus

Query Search

Query Search

Wider Search

(141)

(198)

Title & Abstract Scan

Title & Abstract Scan

(84)

(103)

Full Text Scan

(97)

Top Cited

State-of-the-Art

(20)

(Section 4.1)

Experimental Evaluation (Section 4)

Figure 1: The search and filtering method with the number of remaining papers between brackets.

2.2 Results

Figure 1 summarizes the initial search results. After filtering and removing duplicates, 97 papers remained, of which 11 were review papers. Classification based on Table 1 is detailed in Table 2 and Table 3, with review papers excluded from category-specific analysis due to their broader scope.

Table 2: Literature classification. Classification of the papers according to different categories: publication data, learning method, evaluation metric, objective, and data.

Publication Data Evaluation Metric Objective Data Network

## F1


[p. 4]

Flow/Chain Detection

Inverse/undirected network

Recall

Year

Precision

Time

Synthetic

Transaction Classification

Open-Source

Multiple networks

Reference

Accuracy

Client Classification

Bitcoin/Crypto

Community Detection

Proprietary

Review Paper

Total 11 26 9 15 18 17 4 5 10 1 11 37 27 13 16 32 40 11 5 18

## FPR


Dre˙zewski et al. [33] 2015 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Ngai et al. [99] 2011 ✓ ✗ Malm and Bichler [87] 2013 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Fronzetti Colladon and Remondi [41] 2017 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ Zhou et al. [151] 2017 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✗ ✗ Didimo et al. [29] 2011 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ McGinn et al. [88] 2016 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Senator et al. [113] 1995 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ Wu et al. [137] 2021 ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ Gao and Ye [42] 2007 ✓ ✗ Joaristi et al. [68] 2018 ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✓ Irwin and Turner [63] 2018 ✓ ✓ Michalak and Korczak [93] 2011 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Wu et al. [138] 2021 ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Li et al. [78] 2020 ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✓ ✗ ✓ ✗ ✗ Phetsouvanh et al. [105] 2018 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✓ ✗ ✓ ✓ Continued on next page

[p. 5]

Table 2 (continued)

Publication Data Evaluation Metric Objective Data Network

Flow/Chain Detection

Inverse/undirected network

Recall

Time

Year

Precision

Community Detection

Reference

Bitcoin/Crypto

Accuracy

Client Classification

Open-Source

Synthetic

Multiple networks

Transaction Classification

Proprietary

Review Paper

Zhou et al. [154] 2017 ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Didimo et al. [31] 2019 ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Joaristi et al. [69] 2019 ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✓ Camino et al. [19] 2017 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ Velasco et al. [131] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Nandhini and Das [97] 2016 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Zhdanova et al. [150] 2014 ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ Imanpour et al. [62] 2019 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Turner et al. [124] 2019 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ Ovelgönne et al. [101] 2012 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Magalingam et al. [84] 2015 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✓ ✓ Helmy et al. [59] 2016 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Xueshuo et al. [145] 2021 ✗ ✓ ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ Plaksiy et al. [107] 2018 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ Garcia-Bedoya et al. [44] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✓ ✓ ✗ ✗ ✗ ✗ Mehmet and Wijesekera [90] 2013 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ Xia et al. [140] 2021 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✗ ✗ ✗ Kute et al. [74] 2021 ✓ ✗ Mahootiha et al. [86] 2021 ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ Shaikh et al. [115] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✗ Turner et al. [125] 2020 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ Ricci [110] 2020 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Bahulkar et al. [11] 2018 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ Chmielewski and Stkapor [24] 2017 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Zhou et al. [152] 2022 ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ Gasanova et al. [46] 2018 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ Magomedov et al. [85] 2018 ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ Tharani et al. [121] 2021 ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✓ ✗ ✗ ✓ Jin and Qu [67] 2018 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ Mehmet et al. [91] 2014 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ Xiao et al. [141] 2018 ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ Mohan et al. [95] 2022 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Alarab et al. [4] 2020 ✓ ✓ Shen et al. [116] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✓ Prado-Romero and Gago-Alonso [108] 2017 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Zhang et al. [149] 2021 ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ Garcia-Bernardo et al. [45] 2022 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ He et al. [58] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ Micale et al. [92] 2019 ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✗ ✗ Bhalerao et al. [13] 2019 ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ Omar et al. [100] 2014 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Winiecki et al. [136] 2020 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✓ Starnini et al. [118] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ Hamid [55] 2017 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ Gulino et al. [53] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Adriaens et al. [1] 2019 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ Chang et al. [22] 2007 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Kurshan and Shen [73] 2020 ✓ ✗ Jin et al. [65] 2022 ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✓ Bellomarini et al. [12] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ Sousa Lima et al. [117] 2022 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ Ça˘glayan and Bahtiyar [17] 2022 ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Jin et al. [66] 2022 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Kurniawan et al. [72] 2015 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Sun et al. [119] 2022 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Gerbrands et al. [47] 2022 ✓ ✗ Dumitrescu et al. [34] 2022 ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Yu et al. [148] 2022 ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ García and Mateos [43] 2021 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✓ Wang et al. [133] 2022 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ Gong et al. [48] 2022 ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ Li et al. [79] 2022 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Li et al. [76] 2022 ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✗ Continued on next page

[p. 6]

Table 2 (continued)

Publication Data Evaluation Metric Objective Data Network

Flow/Chain Detection

Inverse/undirected network

Recall

Time

Year

Precision

Community Detection

Reference

Bitcoin/Crypto

Accuracy

Client Classification

Open-Source

Synthetic

Multiple networks

Transaction Classification

Proprietary

Review Paper


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
