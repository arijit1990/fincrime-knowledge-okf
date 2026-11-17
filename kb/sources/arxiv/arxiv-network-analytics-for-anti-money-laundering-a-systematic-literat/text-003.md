---
type: Source Text
title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation - part 3 of 9 (pp. 9-15)
description: 'Verbatim extracted text, pp. 9-15: FPR; AUPRC'
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
part: 3
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2405.19383
  title: Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation
  author: org:arxiv
  last_modified: '2024-05-29T00:00:00Z'
---

# Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2024-05-29), part 3 of 9, pp. 9-15. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## FPR


[pp. 9-10]

The methods in the literature are supervised, unsupervised, semi-supervised and visualisations. The most popular method is unsupervised learning, followed by supervised learning and visualisations, as shown in Table 3. The popularity of unsupervised learning may be due to money laundering being very uncommon, resulting in highly skewed data sets with very few labelled observations [3]. Due to limited resources to investigate the massive amounts of transactions, most transactions are left unlabelled [129, 106]. In addition, criminals try to evade detection by continuously changing tactics [10, 106], making historically patterns less relevant for future predictions [15]. The performance of (supervised) models trained on historical data can therefore decrease over time [14].

Table 3 indicates that half of the papers rely on manual feature engineering. These manual features include classic network centrality measures (degree, betweenness etc.) and summary statistics of the transactions in the nodes’ ego-network. The second most popular method is clustering, which is used broadly in two ways. First, clustering for visualisations mitigates visual cluttering and allows the the selection detail shown. Second, clusters are used for feature engineering. Next to manual feature engineering and clustering, rule-based methods are still frequently used. This illustrates that the current literature heavily relies on expert knowledge. Hence, there is an opportunity to further develop data-driven machine learning methods in anti-money laundering.

The evolution of methods used over time, as presented in Figure 3, shows that the earliest research relied almost exclusively on rule-based systems and manual feature engineering. These remain popular approaches to this day. From 2018 onward, we see the application of deep learning methods based on shallow representations and graph neural networks. Especially the use of GNNs has seen a spike in 2022.

The downstream methods used for classification have also evolved. Popular methods are tree-based, clustering, anomaly detection and logistic regression. SVM-based methods were popular until 2019, while neural networks were only used in AML as of 2020. These are often recurrent neural networks to incorporate the temporal aspect [140, 149, 95, 79].

Key to these methods is how the authors define the network(s) used. The construction of multiple networks, e.g., same entities but using different relations, to capture richer data is present in 18 papers. Of these papers, five used the undirected network or the one with direction reversed in tandem with the original network. It allows for information propagate from, e.g., the transaction’s receiver back to the sender.

Modelling Method per Year (Detailed)

Rule-based

Manual features

Walk-based

Rule-based

Manual features

Walk-based

Shallow repr.

Deep repr.

Correlation-based

Shallow repr.

Deep repr.

Correlation-based

Tree-based

SVM-based

Neural Networks

Tree-based

SVM-based

Neural Networks

Anomaly detection

Clustering

Logistic regression

Anomaly detection

Clustering

Logistic regression

[p. 10] [ref: 3.2.2]

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

Year

Year

Year

Figure 3: The evolution of the model building blocks over the years. Since there are many modelling methods, the graphs are split.

3.2.2 Objectives.

Table 2 shows that the AML method’s objective is most often detecting suspicious clients, followed by detecting suspicious transactions, money flows and communities. Client classification combines client characteristics with payments made over a longer period. Since money laundering is done over a longer period, with the aim to make the individual transaction appear normal, models trained on a series of transactions, leveraging an individual’s behaviour, can obtain higher performance.

Figure A3 shows that methods for crypto-currency are most often introduced for suspicious transaction detection. Due to the pseudo-anonymity, it is much harder to know which wallets belong to what person [152, 145], making it less feasible to build profiles. Therefore, researchers in AML have also looked at de-anonymisation of the wallets [152, 145, 48]. They use network features to cluster wallets together to see if they belong to the same person or organization.

In recent years, more studies have been done on flow/chain detection, tracking payments over multiple steps/people. Although this requires more computing power, it more closely resembles reality [126, 75]. Hence, these methods are becoming more widely used.

3.2.3 Evaluation.

Table 2 shows that research mostly relies on the recall, F1-score, precision and time. Figure 4 illustrates that training/prediction time was a popular method in earlier studies, but relatively few papers use time in more recent work, which might be a consequence of increased computing power. Additionally, the popularity of the precision, recall and F1-score is a recent and increasing trend in the literature.

We remark two surprising results. First, only one paper used the area under the precision-recall curve (AUC-PR). Due to the high label imbalanced, this metric is shown to be more appropriate than the area under the ROC curve (AUC- ROC) [26, 102]. Therefore, we would expect it to be more widely used. Second, some papers solely reported accuracy [31, 141, 48, 143]. Given the high class imbalance, accuracy fails in providing an appropriate performance assessment.

[pp. 10-11] [ref: 3.2.4]

3.2.4 Data.

Table 2 shows that most studies use open-source data, with proprietary data used in almost 50% of the papers. Only a minority of papers report their findings using synthetic data. There is, however, a major difference between crypto- and other research. Figure A1 shows that crypto-research is almost exclusively done on open-source data. This results from

Evaluation Metrics per Year (Detailed)

Accuracy

Precision

Recall

Accuracy

Precision

Recall

7.5

5.0

2.5

0.0

7.5

5.0

2.5

0.0

Time

Time

## AUPRC


[p. 11]

7.5

5.0

2.5

0.0

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

1995 2007 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

Year

Year

Year

Figure 4: The evolution of the evaluation metrics over the years. Since there are many metrics, the graphs are split.

the blockchain’s freely accessible distributed ledger [134]. On the other hand, classic transaction data cannot be shared, due to privacy reasons, resulting in half the data sets being proprietary.

Following this last remark, one would expect to have (almost) no research done on open-source data sets for fiat currencies. Figure A1 shows that almost 30% of non-crypto related papers use open-source data. These papers can be categorised in four groups:

• Methods that are evaluated on non-financial network data, whether or not next to proprietary/synthetic money laundering data: Zhou et al. [151], Ovelgönne et al. [101], Micale et al. [92], Prado-Romero and Gago-Alonso [108] • Methods evaluated on government data, assumed or stated to be open-source: Didimo et al. [29], Imanpour et al. [62], Velasco et al. [131], Bahulkar et al. [11], Malm and Bichler [87] • Methods constructed to analyse leaked documents/scandals, e.g., the Panama papers: Joaristi et al. [68, 69], Magalingam et al. [84], Adriaens et al. [1], Winiecki et al. [136], Helmy et al. [59], Cheong and Si [23] • Other: Nandhini and Das [97], Bhalerao et al. [13], Ça˘glayan and Bahtiyar [17]

For the Other category, we have the following. Nandhini and Das [97] say that the data is publicly available, without giving any more information. Bhalerao et al. [13] scraped their data from Hack Forums. Finally, Ça˘glayan and Bahtiyar [17] use a Kaggle data set based on synthetic data. We categorise it as open-source, since it is made publicly available.

[pp. 11-12] [ref: 3.3]

Table 5 summarises the open-source data sets. The most widely used are almost all crypto-currency data sets. Raw Bitcoin data is used by ten papers. This raw data is often enhanced using data from other platforms. One such platform is WalletExplorer, which is used by three papers. It is less relevant today, since the data has not been maintained since 2016. Another recent data set on Bitcoin is the Elliptic data sets [37, 134]. Although only published in 2019, it has already been used in six experiments. After Bitcoin, Ethereum seems to be the second most popular crytpo-currency in AML.

The most used data set for fiat currency is the Czech Financial Data set (CFD). This data set does not provide any labels. Papers using it introduce additional, synthetic money laundering patterns to test their methods [78, 133]. This is not ideal, as this hinders comparison across research and can introduce detection bias.

As mentioned above, AML methods are also being evaluated on leaked data like the ICIJ Offshore Leaks Database (including, e.g., the Panama-papers) and the Enron data set.

3.3 Top Cited Papers

A final step in our discussion is an in-depth analysis of the top-cited papers. These papers are well received by the scientific community and are likely of high quality. We select the 10% most cited papers per year, extended with the 10% most cited papers overall (see Section 2.1). This results in 20 papers as listed in Table 6. The analysis is done in

Table 5: The open-source data sets used in the different papers. Data Set Number References

Raw bitcon 10 [88], [137], [105], [138], [125], [110], [145], [121],

[109], [146] Elliptic Data set 6 [5], [140], [95], [119], [76], [79] Ethereum XBlock.pro 4 [121], [152], [65], [66] ICIJ Offshore Leaks Database 4 [69], [44], [68], [136] WalletExplorer 3 [137], [125], [145] Czech Financial Data set (CFD) 2 [78], [133] Enron Data set 2 [84], [1] RenRenDai 1 [141] Bloxy 1 [66] iCOV 1 [47] Secret Presidential Funds scandal 1 [23] Tencent QQ 1 [154] Caviar data set 1 [11] BitcoinTalk 1 [138] Ripple Network 1 [19] 2015 Ashley Madison extortion scam 1 [105] FinCEN 1 [29] BlockCypher 1 [109]

[pp. 12-13] [ref: 3.3.1]

three stages to gain deeper insights. First, we revisit the categories as presented in Table 1. Second, we analyse the task-level objectives by discussing the data and methods present in these literature. Third, the papers are classified according to the processing steps and challenges, as introduced by Bockel-Rickermann et al. [14].

3.3.1 General Classification.

Five out of 11 review papers are selected. This is to be expected, since review papers have a higher likelihood of being cited [32]. Plots summarising the classification according to Table 1 are given in Appendix B. Similar results are observed for the top-cited papers as for the literature as a whole; unsupervised learning is by far the most applied method, and research relies heavily on manual and rule-based features. Only time and threshold-dependent metrics were used for evaluation. This indicates that threshold-independent metrics are not mainstream when comparing AML models using networks analytics. We observe that, compared to the wider literature, flow/chain detection methods are better cited as well as studies using open-source data. As mentioned before, flow detection better captures the intricate patterns used in money laundering. The use of open-source data makes comparison with and replication of the studies possible, fostering research adoption.

Additionally, five papers deal with crypto-related money laundering, indicating a strong research interest. On the one hand, crypto currencies are widely used by criminals because of the absence of regulation [40] and the anonymity it provides [63, 134]. On the other hand, a full history of ownership is available on the blockchain for each coin, facilitating the discovery of transaction patterns in payment networks [63, 134].

3.3.2 Task-Level Objectives.

Table 7 summarises the data set used with information therein, the model proposed by the authors to capture a certain money laundering phenomenon, and the baselines to which the proposed model is compared. Additionally, Table 8 summarises the network properties of these papers.

We again see a strong reliance on basic centrality measures for anti-money laundering. A couple of papers apply very basic analysis. Fronzetti Colladon and Remondi [41] and Malm and Bichler [87] purely consider correlations to extract conclusions for their AML features.

Next to the typical objectives of money laundering detection, some research illustrates how network analytics can be used to support investigators to find novel leads and other people involved in previously-reported cases.

Table 7 points to limitations in the literature. Many of the proposed methods are only tested on proprietary data, limiting the reproducibility of their results. The performance is often illustrated using case studies, without the inclusion of other baselines. This shows that there is a lack of a consensus on baselines and state-of-the-art methods in the field.

Table 6: Summary of the top-cited papers, with indication of whether it is a review and/or crypto-related.

Reference Title Year Citations Review Crypto

[p. 13]

2011 1307 ✓

Ngai et al. [99] The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature

Fronzetti Colladon and

2017 200

Remondi [41]

Using social network analysis to prevent money laun- dering

2007 171

Chang et al. [22] WireVis: Visualization of Categorical, Time-Varying Data From Financial Transactions

1995 152

Senator et al. [113] Financial Crimes Enforcement Network AI System (FAIS) Identifying Potential Money Laundering from Reports of Large Cash Transactions

2015 141

Dre˙zewski et al. [33] The application of social network analysis algorithms in a system supporting money laundering detection

2007 106 ✓

McGinn et al. [88] Visualizing Dynamic Bitcoin Transaction Patterns 2016 122 ✓ Gao and Ye [42] A framework for data mining-based anti-money laun- dering research

2021 94 ✓

Wu et al. [137] Detecting Mixing Services via Mining Bitcoin Trans- action Network With Hybrid Motifs

2013 66

Malm and Bichler [87] Using friends for money: the positional importance of money-launderers in organized crime

2017 63

Zhou et al. [151] A Local Algorithm for Structure-Preserving Graph Cut

2020 54

Li et al. [78] FlowScope: Spotting Money Laundering Based on Graphs

2018 47 ✓ ✓

Irwin and Turner [63] Illicit Bitcoin transactions: challenges in getting to the who, what, when and where

2018 38 ✓

Phetsouvanh et al. [105] EGRET: Extortion Graph Exploration Techniques in the Bitcoin Network

2021 38 ✓

Kute et al. [74] Deep Learning and Explainable Artificial Intelligence Techniques Applied for Detecting Money Launder- ing–A Critical Review

2014 32

Zhdanova et al. [150] No Smurfs: Revealing Fraud Chains in Mobile Money Transfers

2019 24

Bhalerao et al. [13] Mapping the underground: Supervised discovery of cybercrime supply chains

2010 12

Ovelgönne et al. [101] Covertness Centrality in Networks 2012 20 Cheong and Si [23] Event-based approach to money laundering data anal- ysis and visualization

2022 11 ✓

Gerbrands et al. [47] The effect of anti-money laundering policies: an em- pirical network analysis

2022 7 ✓

Zhou et al. [152] Behavior-Aware Account De-Anonymization on Ethereum Interaction Graph

The above observations motivate the construction of the experimental set-up of Section 4. Our aim is to come to a common framework to test methods for network analytics in a uniform way.

[pp. 13-14] [ref: 3.3.3]

In addition to the objectives of the studies, Table 8 presents the network construction in these papers. It indicates that most of the papers use homogeneous networks with transactions forming the edges between accounts. Only a few use heterogeneous networks, either by having both accounts and transactions as nodes, or having nodes that represent different characteristics or feature values.

3.3.3 Processing steps.

Next, the papers are classified according to the framework presented by Bockel-Rickermann et al. [14]. Table 9 summarises the papers over the processing steps. The most prevalent pre-processing steps are feature engineering and exploration. Feature engineering is done to define different risk profiles or to enhance GNN models. This is either based on neighbourhood and centrality metrics [41, 33, 101] or on the aggregation of local (node-specific) information [152, 150]. For exploration, some research is done on how to construct meaningful visualisations [22, 88], while other papers rely on clustering the nodes as additional support for their findings [87, 41].

Table 7: Summary of the objective of the paper, where the paper uses [Data set] with [information] to introduce a [model] capturing [phenomenon] and is compared to [baselines].

Paper Data set Information Model Phenomenon Baselines

Smurfing -

Fronzetti Colladon and Remondi [41]

Correlation of centrality metrics with label

Italian factoring data Transaction invoices, economic sector, geographical area

Suspicious behaviour -

Chang et al. [22] Proprietary bank data set Transactions, accounts, keywords, personal information

Visualisation of keywords-accounts, account using transactions, and evolution transactions of (groups of) accounts

Graphical user interface identifying high-value leads -

People, accounts, businesses, locations and transactions

Senator et al. [113] Reports of large cash transactions according to Bank Secrecy Act

-

Dre˙zewski et al. [33] Proprietary bank statements, national court register

Connections Rule-based role definition via centrality metrics

Roles in criminal organisations

-

McGinn et al. [88] Bitcoin Transactions, wallets Visualisation Unexpected high-frequency transaction patterns

Mixing -

Wu et al. [137] Bitcoin Transactions and wallets Account, transaction and network feature extraction + z-score based on hybrid motives + logistic regression

-

Role of money-launderers in illicit markets

Correlation of betweenness and eigen-vector centrality with known roles

Malm and Bichler [87] Police intelligence reports Person under investigation in the report and relations, demographic characteristics of each person, nature of illicit drug trade involvement, and the types of relationships that existed among individuals

HOSPLOC (local graph clustering)

Synthetic identities and money laundering

Zhou et al. [151] Proprietary bank data set Bank accounts, names, emails, addresses, and phone number

[p. 14]

Local clustering (Nibble, NPR, LS-OSC), global (NMF, TSC) Li et al. [78] Proprietary and Czech Financial Data set

SpokEn, D-Cube, Fraudar, HoloScope, RRCF

Anomalous money flow indicative for money laundering

Bank accounts, transactions FlowScope (objective maximisation to find fast money flow through bank in multi-partite network)

-

Phetsouvanh et al. [105] Bitcoin blockchain and Ashley Madison blackmail

Transactions and wallets Average length and confluence analysis

Suspicious bitcoin flow and discover other wallets owned by suspected perpetrators

Smurfing PART, C4.5, Random Forest

Zhdanova et al. [150] Synthetic MMT data Transaction between phones PSA@R (event-driven process analysis)

-

Bhalerao et al. [13] Forum threads (English and Russian)

Money laundering and other fraudulent behaviour

Users, Posts and replies Automatic classification using XGBoost, LogReg, SVM ans FastText. Construction supply chain based on interaction graph. Visualisation via alluvial plots

Network Covertness centrality Hiding behaviour -

Ovelgönne et al. [101] Youtube and Universitat Rovira I Virgili data sets

-

Cheong and Si [23] Criminal relations database Transactions and relationships

Find additional suspects in money laundering cases

Rule-based degree of suspicion and visualisation of relations

Interactions over time -

Gerbrands et al. [47] iCOV Transactions, family and professional relations of people investigated

Clustering (Louvain and temporal) + node level centralities

Account identification (phishing, exchange etc.)

Zhou et al. [152] Ethereum (Eth-ICO, Eth-Mining, Eth-Exchange, Eth-Pish&Hack)

Transactions and wallets Pipeline based on sampling, Hierarchical Graph ATtention Encoder and sub-graph contrastive learning

Manual, Deepwalk, node2vec, trans2vec, graph2vec + LR, RF, LGBM, and GCN, GAT, GIN, I2BGNN-A, I2BGNN-T

Most papers apply unsupervised learning in their processing step. This involves detection of suspicious transaction flows [151, 78, 105]. Another important part is the use of centrality metrics to define specific roles for entities in the network [33, 87, 101]. Finally, some methods create heuristics to define outlying behaviour [113, 22, 23, 150].

For the post-processing step, most research covers statistical evaluation, implementation and interpretation. Statistical evaluation is used to obtain a quantitative evaluation of the performance. Implementation consists of analysing the efficiency of the methods. It deals solely with computation time and scalability. For interpretation, researchers use specific interpretable features.

[pp. 14-15]

More detailed trends in the literature are discussed below according to three main categories, that mainly follow the processing steps; unsupervised learning, (semi-)supervised learning and visualisation methods.

Unsupervised learning is divided into two main streams. The first assigns and identifies specific roles of actors in criminal networks, based on police reports of criminal cases [87, 33]. The second covers methods to track money flows through the network [151, 78, 105]. It is important to integrate these transaction chains, since money laundering is a process involving multiple steps and actors [75]. Next to these two main streams, the remaining paper [101] introduces a new covertness measure.

Table 8: Summary of the construction of the network. Paper Nodes Edges

Factoring companies

Fronzetti Colladon and Remondi [41]

Economic sector geographical data transaction amount tacit link (same owners/resources) Chang et al. [22] People Transactions

Senator et al. [113] Accounts People, businesses, accounts and location Connections

Dre˙zewski et al. [33] People (via court register) Transactions (via bank statements) McGinn et al. [88] Transactions, inputs and outputs Input/output part of same transaction, inputs that belong to the same address

Wu et al. [137] Address Address and transactions

Link bank account to other items

Transactions If they are related Malm and Bichler [87] People (from police reports) Co-appearance in the report (family, client-lawyer etc.) Zhou et al. [151] All items of interest (bank account, name, email, address, phone number)

Li et al. [78] Bank accounts Transfers Phetsouvanh et al. [105] Bitcoin wallet address Transactions Ovelgönne et al. [101] - - Cheong and Si [23] People Relations Zhou et al. [152] Accounts Transactions Zhdanova et al. [150] mWallets Transactions

Table 9: Papers per method cluster, based on Bockel-Rickermann et al. [14]. Process Step Sub-Steps References

Pre-processing

Sampling [41]. Exploration [41],[22],[88], [87]. Missing Value Treatment [41]. Outlier Detection and Treatment - Categorization, standardization & segmentation [33], [13]. Feature Engineering [41], [33], [101],[152], [150]. Variable Selection -

Unsupervised Learning [22], [113], [33], [87], [151], [78], [105],

Processing

[101], [23],[150]. Supervised Learning [41], [13]. Semi-Supervised Learning [137]. Hybrid Learning [152].

Post-processing


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Network Analytics for Anti-Money Laundering -- A Systematic Literature Review and Experimental Evaluation" (2024-05-29). https://arxiv.org/abs/2405.19383
