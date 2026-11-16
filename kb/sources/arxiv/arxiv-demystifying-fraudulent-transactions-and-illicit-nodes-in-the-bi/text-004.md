---
type: Source Text
title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics - part 4 of 4 (pp. 11-16)
description: 'Verbatim extracted text, pp. 11-16: Addresses per User: Max 14, 885 > REFERENCES; Addresses per User: Max 14, 885 > OUR BLOCKCHAIN TRANSACTION PARSER AND EXTRACTOR; Addresses per User: Max 14, 885 > OUR BLOCKCHAIN ADDRESS PARSER AND EXTRACTOR; and 6 more sections'
resource: https://arxiv.org/abs/2306.06108
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-demystifying-fraudulent-transactions-and-illicit-nodes-in-the-bi
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-05-25'
legal_status: unknown
part: 4
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:31:16Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:31:16Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.06108
  title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics
  author: org:arxiv
  last_modified: '2023-05-25T00:00:00Z'
---

# Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics

[previous part](text-003.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2023-05-25), part 4 of 4, pp. 11-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Addresses per User: Max 14, 885


### REFERENCES


[pp. 11-12]

Xiong. 2022. TTAGN: Temporal Transaction Aggregation Graph Network for Ethereum Phishing Scams Detection. In Proceedings of the ACM Web Conference 2022. 661–669. [22] Dan Lin, Jiajing Wu, Qi Yuan, and Zibin Zheng. 2020. Modeling and understanding

card fraud detection: Based on bagging ensemble classifier. Procedia computer science 48, 2015 (2015), 679–685. [45] Yuhang Zhang, Jun Wang, and Jie Luo. 2020. Heuristic-based address clustering

ethereum transaction records via a complex network approach. IEEE Transactions on Circuits and Systems II: Express Briefs 67, 11 (2020), 2737–2741. [23] Dan Lin, Jiajing Wu, Qi Yuan, and Zibin Zheng. 2020. T-edge: Temporal weighted

in bitcoin. IEEE Access 8 (2020), 210582–210591. [46] Jiajun Zhou, Chenkai Hu, Jianlei Chi, Jiajing Wu, Meng Shen, and Qi Xuan. 2022.

multidigraph embedding for ethereum transaction network analysis. Frontiers in Physics 8 (2020), 204. [24] Wai Weng Loa, Gayan K Kulatillekea, Mohanad Sarhana, Siamak Layeghya, and

Behavior-aware Account De-anonymization on Ethereum Interaction Graph. arXiv preprint arXiv:2203.09360 (2022). [47] Francesco Zola, Maria Eguimendia, Jan Lukas Bruse, and Raul Orduna Urrutia.

Marius Portmanna. 2022. Inspection-L: Self-Supervised GNN Node Embeddings for Money Laundering Detection in Bitcoin. (2022).

2019. Cascading machine learning to attack bitcoin anonymity. In 2019 IEEE International Conference on Blockchain (Blockchain). IEEE, 10–17.

Figure 13: Elliptic++ dataset collection pipeline using our blockchain parsers and extractors.

txs_features txs_edgelist

... txId1 txId2

PUBLIC DATASET txId Time step LF_1 AF_72

... ... ... ... ...

... ...

Elliptic

Dataset

...

272145560 296926618

272145560 24 -0.155493 1.521399

calculate TXS_in and TXS_out using edgelist

... ... ... ... ...

272145560 272145556

299475624 272145560

... ...

with txId

search edgelist

txId Time step LF_1 AF_72 TXS_in TXS_out BTC_out_total

...

### OUR BLOCKCHAIN TRANSACTION PARSER AND EXTRACTOR


[p. 12]

... ... ... ... ...

... ... ... ... ...

PUBLIC DATASET txId txHash

/btc/address/, /btc_in/, /btc_out/,

... ...

... ...

...

272145560 24 -0.155493 1.521399 1 2.77279994

Elliptic++ Transactions

Elliptic++

scrape blockchain with txHash

Dataset

Txs De-anonymized

Dataset

... ... ... ...

... ... ... ... ...

/address_in/, /address_out/, /btc_total/, /tx_fees/, /tx_size/

Dataset

272145560 56cba8aa85f90e1d8a703cc868dc79c11 3b289050da2958a64214e1efa5dd898 ... ...

grab all addresses

txId address

scrape blockchain

... ...

with address

272145560 39sfuA8pY4UfybgEZi7uvA13jkGzZpsg5K

address class TXS_input Addr_interactions_median

...

272145560 1MLvzsdbo2N12ANUcGTXkMCQ1GZbLTvkTL

### OUR BLOCKCHAIN ADDRESS PARSER AND EXTRACTOR


...

... ... ... ...

... ...

Elliptic++

...

39sfuA8pY4UfybgEZi 7uvA13jkGzZpsg5K 1 420 1

Actors Dataset

...

1MLvzsdbo2N12ANUcG TXkMCQ1GZbLTvkTL 1 1 1

/btc_sent/, /btc_received/, /tx_fees/, /tx_fees_share/, /txs_total/, /blocks_txs/, / blocks_input/, /blocks_output/,

...

... ... ... ...

/blocks_first/, /lifetime/, /blocks_last/, /blocks_first_sent/, /blocks_first_receive/

A APPENDIX A.1 Dataset Collection

above, a major technical challenge was the resource demand. The collection, cleaning, parsing, and labeling of the dataset were com- putation and storage intensive. We leveraged the High Performance Computing (HPC) Clusters at the Georgia Institute of Technology (the PACE clusters4), taking several weeks to complete the extrac- tion of all accounts and their features present in the Elliptic++ dataset.

A.2 Fraud Detection Evaluation Metrics

The Bitcoin blockchain contains a huge number of transactions since its inception. Given that our goal of data collection is for fraud detection on the Bitcoin network, we use the 203k transactions col- lected in the Elliptic dataset as the seeds of our crawling module for two reasons. First, the Elliptic dataset is the largest labelled Bitcoin transaction data publicly available. Second, the Elliptic dataset only contains transactions in the Bitcoin network labeled as licit, illicit, and unknown. To enable detection of both fraudulent transactions and illicit accounts, we need to collect all accounts involved in the Elliptic transaction dataset. The data acquisition pipeline for the Elliptic++ dataset is shown in Figure 13 and is described as follows.

The accuracy of the models is verified using five metrics: Precision, Recall, F1 Score, Micro-Avg F1 Score, and Matthews Correlation Coefficient. The explanations have the following components: true positive (TP), false positive (FP), false negative (FN), and true nega- tive (TN).

(1) Precision - the fraction of positive points that were correctly

classified. It is calculated by:

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= 𝑇𝑃 𝑇𝑃+ 𝐹𝑃

First, we design and implement a blockchain parser which takes de-anonymized transactions as input, scrapes the public Blockchain, and augments additional features to the transactions. The aug- mented features include information regarding the transaction in- cluding number of incoming/outgoing edges, number of input/output addresses, amount of incoming/outgoing BTC, and much more

[pp. 12-13]

(2) Recall - the fraction of actual positive points that were cor-

rectly classified. It is calculated by:

Next, the output from the blockchain transactions parser is fed into our extractor that parses the addresses involved in the transac- tions and scrapes the public Blockchain to gather the corresponding address-related features. These features include transaction and time related information.

𝑅𝑒𝑐𝑎𝑙𝑙= 𝑇𝑃 𝑇𝑃+ 𝐹𝑁

(3) F1 Score - the harmonic mean of precision and recall. It is

calculated by:

𝐹1 = 2 · 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛· 𝑟𝑒𝑐𝑎𝑙𝑙

We define the transaction data structure (see Table 1) and account data structure (see Table 4) such that the parsers and extractors will organize, clean, and store the data based on these structures. Fur- thermore, we collect those account features that are needed in the construction of the four types of graph representations: (a) Money Flow Transaction Graph, (b) Actor Interaction Graph, (c) Address- Transaction Graph, and (d) User Entity Graph. These graphs enable

𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙

mining and visualizations of account and transaction connections for anomaly detection.

4www.pace.gatech.edu

In addition, to identify and define the important features for all accounts involved in the Elliptic transaction dataset, as outlined

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

Figure 14: Distribution of transactions in time steps 14 (left) and 32 (right).

Figure 15: Distribution of wallet addresses in time steps 14 (left) and 32 (right).

Figure 16: Distribution of transactions and wallet addresses in time steps 14 (left) and 32 (right).

(4) Micro-Avg F1 Score - similar to F1 Score, but using the total

number of TP, FP, and FN instead of individually for each class. It is calculated by:

Interaction Graph, and the Address-Transaction Graph respectively. Specifically, they show a comparison between distributions in time step 14, which produce more sparse graphs, and time step 32, which produce more dense graphs. The grey area is due to the density of the edges.

[p. 13]

𝑀𝑖𝑐𝑟𝑜𝐴𝑣𝑔𝐹1 = 𝑇𝑃

A.4 Bitcoin Address Clustering

(5) Matthews Correlation Coefficient (MCC) - measures the qual-

ity of binary classifications, taking into account the differ- ence between predicted values and actual values. It ranges from [−1, +1] with the extreme values −1 and +1 in cases of perfect misclassification and perfect classification respec- tively. It is calculated by:

The Bitcoin address clustering process discussed in this study is referred to as the multiple input addresses heuristic. This heuristic takes advantage of the fact that in order to transact correctly, a user must provide the signatures corresponding to the private keys and the public key wallet addresses for all the input addresses, thus, a user must have access over all private keys. Hence, allowing for the assumption that all input addresses of a transaction can be attributed to the same user. This is demonstrated in Figure 18, where the input addresses addr1, addr2, addr3, and addr4 are grouped into User 𝑈1, while input addresses addr5 and addr6 are grouped into User 𝑈2. Figure 17 shows the address clustering process using the four steps discussed in Section 3.3.4, producing a user graph on the right.

### (𝑇𝑃+ 𝐹𝑃) · (𝑇𝑃+ 𝐹𝑁) · (𝑇𝑁+ 𝐹𝑃) · (𝑇𝑁+ 𝐹𝑁)


[pp. 13-14]

A.3 Graph Visualization

Figures 14, 15, and 16 show the distributions of transactions and/or wallet addresses for the Money Flow Transaction Graph, the Actor

Figure 17: Clustering Bitcoin addresses: (a) collect the set of input addresses for each transaction in the address-transaction graph; (b) group transactions with ≥1 common element in each set into unique users; (c) highlight transactions within each user in the original graph; and (d) convert highlighted address-transaction graph into a user graph, with edges across users if a path existed between groups of transactions in the original graph.

tx 4

tx 1

tx 2

### USER 1


[p. 14]

addr 7

addr 1

addr 2 addr 3

tx 5

addr 4 tx 3

b

addr 9

addr 1

tx 7

tx 8

tx 6

addr 2

addr 14

addr 1

addr 1

a

addr 5

addr 3

addr 6

tx 1 tx 2

addr 4

addr 2

addr 8

addr 5

addr 3

c

addr 10 addr 7

addr 1

addr 6

addr 9

tx 3 tx 4

tx 5

tx 1 tx 2

addr 4

addr 11

addr 8

### USER 5


[pp. 14-15]

addr 12

tx 6

addr 10 addr 7

addr 1

tx 7 tx 8

addr 9

d

addr 13 addr 14 addr 15

tx 3 tx 4

tx 5

addr 11

addr 12

tx 6

tx 7 tx 8

addr 13 addr 14 addr 15

A.5 Statistical Analysis of the Dataset

Figure 18: Bitcoin address clustering based on multiple input addresses heuristic in an address-transaction graph.

Figure 19 shows illicit actors that exist in only 1 time step (14, 007 total illicit actors). Aside from providing information about the timeline of the illicit actors, it displays the distribution of the illicit actors among the dataset for these types of actors. For example, in time step 6 there are 8 illicit actors, in time step 14 there are 74 illicit actors, and in time step 32 there are 759 illicit actors.

Figure 20 is an extension of the dataset feature analysis and feature refinement by displaying the top 2 and bottom 2 of each feature class in (a) the transactions dataset (left: local features, right: aggregate features), and (b) the actors dataset (left: transactions fea- tures, right: time features). This further solidifies the explainability behind the risk of transactions and actors through the visual (and numerical) distinction among the illicit and licit classes. In all green highlighted figures, one can clearly classify between both classes. Though, this is unlike the red highlighted figures where there is no characteristic trend among both classes.

A.6 Data Distribution

Tables 12 and 13 show the numerical distribution within each class by time step for the transactions and actors datasets respectively.

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

Figure 19: Number of transactions for illicit actors appearing in only 1 time step. Each point is a unique illicit actor. Y-axes are in log scale.

#Transactions #Actors

Number of Illicit Actors

Number of Transactions

1 5 10 15 20 25 30 35 40 45 49

Time Step

Figure 20: Trend comparison for features in the transactions dataset (left) and actors dataset (right). Green highlight shows good correlation (top 2 rows), while red highlight shows unclear correlation (bottom 2 rows).

(a) Comparison of local features (left) and aggregate

(b) Comparison of transaction features (left) and

features (right) in the transactions dataset.

time features (right) in the actors dataset.

0.5

2 Local Feature 53

Aggregate Feature 70

### ADDRINTERACTION {TOTAL}


[p. 15]

1.2x107 FeesSHARE {TOTAL}

0.4

1.5

1x107

0.3

8x106

0.2

6x106

0.1

0.5

4x106

2x106

-0.1

-0.5

-0.2

2 Local Feature 55

Aggregate Feature 39

BlockFIRST SENT

1x1010 BTCRECEIVED {MAX}

0.8

1.5

8x109

0.6

6x109

0.4

Values

Values

0.5

4x109

0.2

2x109

-0.5

-0.2

160000 FeesSHARE {MEAN}

### 1.6 ADDRINTERACTION {MIN}


[ref: 1.7]

Aggregate Feature 41

0.4

20 Local Feature 70

1.5

1.4

0.2

1.3

1.2

-0.2

1.1

-0.4

-0.6

0.9

FeesSHARE {MEDIAN}

140000 Unknown

1.7 Unknown

Local Feature 15

0.4 Aggregate Feature 42

1.6

0.5 Unknown

Illicit

Illicit

0.4

1.5

Illicit

Licit

Licit

0.2

Licit

1.4

0.3

1.3

0.2

1.2

-0.2

0.1

### ADDRINTERACTION {MEDIAN}


[pp. 15-16]

1.1

-0.4

0.9

-0.6

-0.1

1 5 10 15 20 25 30 35 40 45 49 Time Step

1 5 10 15 20 25 30 35 40 45 49 Time Step

1 5 10 15 20 25 30 35 40 45 49 Time Step

1 5 10 15 20 25 30 35 40 45 49 Time Step

Table 12: Numerical distribution of the number of transactions of each class by time step. First two tables are for the training set and the third table is for the testing set.

Time step 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

Unknown 5733 3427 5342 4253 4921 3843 4845 3292 4218 5755 3600 1541 3719 1605 3021 2445 2574

Illicit 17 18 11 30 8 5 102 67 248 18 131 16 291 43 147 128 99

Licit 2130 1099 1268 1410 1874 480 1101 1098 530 954 565 490 518 374 471 402 712

Time step 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34

Unknown 1587 2761 3391 2896 4131 2978 3466 1720 2006 883 1369 3101 1959 2106 3202 2710 1971

Illicit 52 80 260 100 158 53 137 118 96 24 85 329 83 106 342 23 37

Licit 337 665 640 541 1605 1134 989 476 421 182 199 845 441 604 981 418 478

Time step 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49

Unknown 4166 4685 2808 2135 1577 3270 4210 4986 3693 3384 4377 2807 4275 2483 1978

Illicit 182 33 40 111 81 112 116 239 24 24 5 2 22 36 56

[p. 16]

Licit 1159 1675 458 645 1102 1099 1016 1915 1346 1567 1216 710 824 435 420

Table 13: Numerical distribution of the number of wallet addresses of each class by time step. First two tables are for the training set and the third table is for the testing set.

Time step 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

Unknown 26465 15878 26213 31035 24621 17029 23357 17631 23819 38271 18250 10343 26813 5912 11500 9064 17066

Illicit 96 99 58 266 54 17 463 267 960 120 494 77 918 156 447 427 321

Licit 24547 16292 4835 8647 10465 1957 7902 16229 3894 8454 10576 2875 3288 1941 6671 2315 4039

Time step 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34

Unknown 6413 11633 32483 21725 28827 14101 19396 12231 16434 9130 6489 17180 8882 13328 15679 10109 9914

Illicit 189 320 950 1256 1491 734 1083 2243 1334 89 219 979 287 312 1730 561 908

Licit 1643 3220 6315 16576 9693 7301 3518 8314 2360 1000 920 3811 2931 5119 4873 7675 5546

Time step 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49

Unknown 23898 34887 16578 16820 9679 23564 22123 31496 24953 16255 22201 17719 19726 13638 10030

Illicit 943 1226 804 400 282 801 454 967 156 497 42 626 256 433 789

Licit 6229 11130 3455 4039 4881 10233 7033 11142 7302 10631 11057 4723 8106 8783 4385


---

[previous part](text-003.md) | [source overview](overview.md)

[^original]: arXiv, "Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics" (2023-05-25). https://arxiv.org/abs/2306.06108
