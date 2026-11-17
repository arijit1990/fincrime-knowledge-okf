---
type: Source Text
title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics - part 1 of 4 (pp. 1-5)
description: 'Verbatim extracted text, pp. 1-5: ABSTRACT; CCS CONCEPTS; KEYWORDS; and 1 more sections'
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
part: 1
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.06108
  title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics
  author: org:arxiv
  last_modified: '2023-05-25T00:00:00Z'
---

# Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2023-05-25), part 1 of 4, pp. 1-5. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Demystifying Fraudulent Transactions and Illicit Nodes

in the Bitcoin Network for Financial Forensics

Youssef Elmougy Georgia Institute of Technology

Ling Liu Georgia Institute of Technology

Atlanta, GA 30332, USA

Atlanta, GA 30332, USA

ACM Reference Format: Youssef Elmougy and Ling Liu. 2023. Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics. In Proceed- ings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’23), August 6–10, 2023, Long Beach, CA, USA. ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3580305.3599803 1 INTRODUCTION

## ABSTRACT


The emergence of cryptocurrency, initiated by Bitcoin [29], has kindled an adoption of a new exchange system in which finan- cial transactions can be completed without an intermediary. This popularity has been perceived as a catalyst for the integration of cryptocurrencies into the payment systems of traditional financial institutions, enabling processing of exchanges between fiat money and cryptocurrency. To allow for immense volumes of such ex- changes, financial institutions must provide rigid security against high risk transactions from fraudulent activities and assure com- pliance with anti-money laundering (AML) regulations. Although machine learning (ML) models have become a popular tool for anomaly detection and risk assessment of cryptocurrency transac- tions in recent years, we argue that fraud detection models trained for financial forensics should revolve around two goals: (i) priori- tizing higher recall with a (reasonable) trade-off on precision, since the penalty of classifying an illicit transaction/account as licit far outweighs that of the reverse, and (ii) allowing explainability (and derivation of proof) on the risk of transactions/accounts.

Blockchain provides the unique and accountable channel for finan- cial forensics by mining its open and immutable transaction data. A recent surge has been witnessed by training machine learning models with cryptocurrency transaction data for anomaly detec- tion, such as money laundering and other fraudulent activities. This paper presents a holistic applied data science approach to fraud detection in the Bitcoin network with two original contri- butions. First, we contribute the Elliptic++ dataset, which extends the Elliptic transaction dataset to include over 822𝑘Bitcoin wal- let addresses (nodes), each with 56 features, and 1.27𝑀temporal interactions. This enables both the detection of fraudulent trans- actions and the detection of illicit addresses (actors) in the Bitcoin network by leveraging four types of graph data: (i) the transaction- to-transaction graph, representing the money flow in the Bitcoin network, (ii) the address-to-address interaction graph, capturing the types of transaction flows between Bitcoin addresses, (iii) the address-transaction graph, representing the bi-directional money flow between addresses and transactions (BTC flow from input address to one or more transactions and BTC flow from a trans- action to one or more output addresses), and (iv) the user entity graph, capturing clusters of Bitcoin addresses representing unique Bitcoin users. Second, we perform fraud detection tasks on all four graphs by using diverse machine learning algorithms. We show that adding enhanced features from the address-to-address and the address-transaction graphs not only assists in effectively detecting both illicit transactions and illicit addresses, but also assists in gain- ing in-depth understanding of the root cause of money laundering vulnerabilities in cryptocurrency transactions and the strategies for fraud detection and prevention. The Elliptic++ dataset is released at https://www.github.com/git-disl/EllipticPlusPlus.

## CCS CONCEPTS


arXiv:2306.06108v1 [cs.CR] 25 May 2023

• Security and privacy →Intrusion/anomaly detection and malware mitigation; • Applied computing →Network foren- sics; • Computing methodologies →Machine learning.

Bitcoin [29] is the most widely used cryptocurrency. Analyz- ing its blockchain will provide a basis of reference. The Elliptic dataset [40] is the largest labelled Bitcoin transaction data publicly available. The dataset consists of over 203𝑘transactions labelled illicit, licit, and unknown. It provides a good entry into fraudulent transaction analysis. However, the Elliptic dataset [40] consists of only Bitcoin transactions, without features of the addresses in- volved and the different interactions between pairs of addresses. Hence, the forensic analysis using the Elliptic dataset suffers from a prominent downfall: when a model predicts an illicit transaction, the addresses responsible cannot be clearly identified since a trans- action may be associated with several input and output addresses.

## KEYWORDS


[pp. 1-2]

Blockchain, Anomaly Detection, Financial Forensics

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. KDD ’23, August 6–10, 2023, Long Beach, CA, USA © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0103-0/23/08...$15.00 https://doi.org/10.1145/3580305.3599803

The first contribution of this paper is the Elliptic++ dataset, which extends the Elliptic dataset to include all the Bitcoin wallet addresses (actors) and their temporal interactions associated to the transac- tions in the Elliptic dataset. Hence, forensics performed using the Elliptic++ dataset can identify fraudulent transactions and dishon- est actors in the Bitcoin network and will also allow explainability as to why a wallet address associated with a transaction is illusive and dishonest. The construction of the Elliptic++ dataset contributes a novel way in collecting and visualizing Blockchain data, using wallet addresses as the center of a risk detection model. We collect Blockchain data associated with the Elliptic dataset (transactions). We first augment each transaction in the transactions dataset with

To the best of our knowledge, our Elliptic++ dataset is the largest public Bitcoin account dataset with 822, 942 addresses.

17 additional features, then we crawl the Blockchain to create the Elliptic++ dataset, consisting of the feature-enhanced transactions dataset and the actors (wallet addresses) dataset. The actors dataset includes over 822𝑘labelled wallet addresses, each described with 56 features, and over 1.27𝑀temporal occurrences (interactions) across the same time steps (as those recorded in the Elliptic dataset). With our Elliptic++ dataset, one can perform anomaly detection of fraudulent activities, such as illicit transactions and fraudulent actors. We also include four types of graphs: the Money Flow Trans- action Graph, the Actor Interaction Graph, the Address-Transaction Graph, and the User Entity Graph. These graphs contribute to both mining and visualization of the connections of transactions and the interactions among wallet addresses through their transactions.

[p. 2]

Existing works on Ethereum account profiling and phishing account detection exclusively focus on graph representation learn- ing methods [36, 37]. For Ethereum account profiling, [35] and [46] applied either Graph Convolution Network (GCN) [18] or a hierarchical graph attention encoder (HGATE) to infer the iden- tity of Ethereum accounts based on learning latent features using node-embedding and subgraph-embeddings. TTAGNN [21] gen- erate node embedding by combining LSTM encoder and Graph Attention Network (GAT) [39]. For detecting phishing accounts, Trans2Vec [42] and its variants [22, 23] utilize a graph based ran- dom walk algorithm on transaction time and amount information. The cascade method [13] leverages statistical feature extraction and a lightGBM-based ensemble algorithm. It is worth to note that given the difference in fundamental settings (UTXO and account models), it is not straightforward to apply the existing graph representa- tion learning models developed for profiling Ethereum accounts to profiling Bitcoin accounts on the Bitcoin network.

The second contribution of the paper is performing fraud detec- tion using the Elliptic++ dataset and the four graph representations by combining diverse ML algorithms and feature optimizations. We observe that Random Forest (RF) with feature refinement offers the best-performing model: on the transactions dataset, it achieves 98.6% precision and 72.7% recall compared to 97.5% precision and 71.9% recall when using RF without feature refinement; on the actors dataset, RF with feature refinement achieves 92.1% preci- sion and 80.2% recall, compared to 91.1% precision and 78.9% recall when using RF without feature refinement. Furthermore, the fraud detection using the Elliptic++ dataset allows for in-depth under- standing of the root cause of fraudulent activities in cryptocurrency transactions through semantic and statistical explainability, shining light on the strategies for fraud detection and prevention.

Compared to the literature, this paper presents novel contribu- tions from two perspectives. First, it describes and makes publicly available a labelled dataset with Bitcoin blockchain transactions and wallet addresses. The main benefit of this dataset is that it allows more accurate fraud detection models and algorithms to be developed. Second, it uses the dataset to showcase the detection of illicit blockchain transactions, illicit actors, and the risks of de- anonymizing users based on address clustering. For this, it utilizes a number of baseline machine learning models.

## 3 THE ELLIPTIC++ DATASET


The Elliptic++ dataset consists of 203𝑘Bitcoin transactions and 822𝑘 wallet addresses. It leverages elements from the Elliptic dataset1 [40], a published dataset deanonymizing 99.5% of Elliptic transaction data2, and the Bitcoin addresses dataset obtained by using our Bit- coin Blockchain3 scraping pipeline. A detailed description of the data collection pipeline is included in the Appendix. 3.1 Transactions Dataset

Since the introduction of the Elliptic dataset in 2019 by Weber et al. [40], there have been numerous efforts on data labelling and anomaly detection using ML models. Lorenz et al. [25] assumed minimal access to labels, and proposes an active learning solution by leveraging a smaller subset of the available labels. Oliveira et al. [30] proposed GuiltyWalker, a detection method that computes new fea- tures based on the structure of a transaction-to-transction graph and the distance to known illicit transactions. Alarab et al. [3] pre- sented a comparative analysis of the Elliptic dataset using different supervised learning methods. Loa et al. [24] proposed Inspection-L, a graph neural network framework for anomaly detection, and similarly, Alarab et al. [2] proposed a graph-based LSTM with a graph convolutional network to detect illicit transactions.

The transactions dataset consists of a time-series graph with 49 dis- tinct time steps, 203, 769 transactions (nodes), and 234, 355 directed edges representing the payment flows. Each transaction node is la- belled as illicit, licit, or unknown; with 2% (4, 545) labelled as class-1 (illicit), 21% (42, 019) as class-2 (licit), and the remaining transactions are unknown with regard to licit/illicit, hence labelled as class-3. Three csv files are used, as shown in Table 1. Each transaction node has an entry in txs_features.csv, with numerical data for 183 transaction features, and an entry in txs_classes.csv, repre- senting its class label (1: illicit, 2: licit, 3: unknown). Each edge has an entry in txs_edgelist.csv (indexed by two transaction IDs), representing money flow from one transaction to another. Among the 183 node features, 166 features are inherited from the Elliptic dataset, i.e., the time step, 93 local features, representing local infor- mation about the transaction, and 72 aggregate features, obtained by

1www.kaggle.com/datasets/ellipticco/elliptic-data-set 2www.kaggle.com/datasets/alexbenzik/deanonymized-995-pct-of-elliptic- transactions 3www.blockchain.com

[pp. 2-3]

More generally, there is increasing interest in AML in the con- text of financial transactions and cryptocurrency networks, such as Bitcoin or Ethereum. Combinatorial optimization methods for identifying transactions from graphs, including statistical devia- tion and dense subgraph discovery methods, have been explored in [11, 38]. The lack of labelled data and the imbalanced data are two major challenges for fraud detection when using supervised learn- ing [6, 17, 28] or unsupervised learning [14, 27, 28, 31, 32]. Some efforts have also focused on de-anonymizing mixed transactions by Bitcoin-dedicated graph-based approaches [7, 8, 19, 41]. Regarding Bitcoin account profiling, Michalski et al. [33] built a small dataset of 9, 000 addresses and applied supervised learning to characterize nodes in the Blockchain as miner or exchange, indicating the need of countermeasures for preserving the desired level of anonymity.

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

Table 1: Data structure for an example transaction node in the transactions dataset: (1) features, row of all 183 feature values for txId, (2) edgelist, all incoming and outgoing edges involving txId, and (3) classes, the class label for txId.

txs_features.csv

txId Time step LF_1 · · · LF_93 AF_1 · · · AF_72 TXS_in · · · BTC_out_total

272145560 24 -0.155493 · · · 1.135279 -0.159681 · · · 1.521399 1 · · · 2.77279994

txs_edgelist.csv txs_classes.csv

txId1 txId2 txId class

272145560 296926618 272145560 1

272145560 272145556

299475624 272145560

Table 2: Transactions dataset augmented features.

Table 3: Actors (wallet addresses) dataset features.

Feature Description

Feature Description

𝐵𝑇𝐶𝑖𝑛 Total BTC incoming

Transaction related:

𝐵𝑇𝐶𝑜𝑢𝑡 Total BTC outgoing

𝐵𝑇𝐶𝑡𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑒𝑑 Total BTC transacted (sent+received)

𝐵𝑇𝐶𝑠𝑒𝑛𝑡 Total BTC sent

each has 5 values: total, min, max, mean, median

[p. 3]

𝐵𝑇𝐶𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑑 Total BTC received

𝑇𝑥𝑠𝑖𝑛 Number of incoming transactions

𝐹𝑒𝑒𝑠 Total fees in BTC

𝑇𝑥𝑠𝑜𝑢𝑡 Number of outgoing transactions

𝐹𝑒𝑒𝑠𝑠ℎ𝑎𝑟𝑒 Total fees as share of BTC transacted

𝐴𝑑𝑑𝑟𝑖𝑛 Number of input addresses

Time related:

𝐴𝑑𝑑𝑟𝑜𝑢𝑡 Number of output addresses

𝐵𝑙𝑜𝑐𝑘𝑠𝑡𝑥𝑠 Number of blocks between transactions

𝐵𝑇𝐶𝑡𝑜𝑡𝑎𝑙 Total BTC transacted

𝐹𝑒𝑒𝑠 Total fees in BTC

𝐵𝑙𝑜𝑐𝑘𝑠𝑖𝑛𝑝𝑢𝑡 Number of blocks between being an in- put address

𝑆𝑖𝑧𝑒 Total transaction size

single value

𝐵𝑙𝑜𝑐𝑘𝑠𝑜𝑢𝑡𝑝𝑢𝑡 Number of blocks between being an out- put address

Figure 1: Number of transactions by time step.

𝐴𝑑𝑑𝑟𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑠 Number of interactions among addresses

each has 5 values: total, min, max, mean, median

𝐶𝑙𝑎𝑠𝑠 class label: {illicit, licit, unknown}

Total Transactions Unknown Illicit Licit

Transaction related:

𝑇𝑥𝑠𝑡𝑜𝑡𝑎𝑙 Total number of blockchain transactions

Number of Transactions

𝑇𝑥𝑠𝑖𝑛𝑝𝑢𝑡 Total number of dataset transactions as input address

𝑇𝑥𝑠𝑜𝑢𝑡𝑝𝑢𝑡 Total number of dataset transactions as output address

1 5 10 15 20 25 30 35 40 45 49

Time related:

Time Step

[pp. 3-4] [ref: 3.2]

𝑇𝑖𝑚𝑒𝑠𝑡𝑒𝑝𝑠 Number of time steps transacting in

𝐿𝑖𝑓𝑒𝑡𝑖𝑚𝑒 Lifetime in blocks

𝐵𝑙𝑜𝑐𝑘𝑓𝑖𝑟𝑠𝑡 Block height first transacted in

𝐵𝑙𝑜𝑐𝑘𝑙𝑎𝑠𝑡 Block height last transacted in

𝐵𝑙𝑜𝑐𝑘𝑓𝑖𝑟𝑠𝑡𝑠𝑒𝑛𝑡 Block height first sent in

aggregating transaction information one-hop forward/backward. The remaining 17 node features are gathered by our Elliptic++ data collection pipeline (with the exception of the 0.5% of transactions that were not deanonymized) as augmented features and are shown in Table 2. Figure 1 shows the distribution of transactions across the three classes in each of the 49 time steps.

𝐵𝑙𝑜𝑐𝑘𝑓𝑖𝑟𝑠𝑡𝑟𝑒𝑐𝑒𝑖𝑣𝑒 Block height first received in

3.2 Actors (Wallet Addresses) Dataset

𝑅𝑒𝑝𝑒𝑎𝑡𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑠 Number of addresses transacted with multiple times

single value

The actors (wallet addresses) dataset is a graph network of 822, 942 wallet addresses, each with 56 features as shown in Table 3. Five csv files are used, as shown in Table 4. Each address has an en- try in wallets_features.csv, with numerical data for the time

Table 4: Data structure for an example address in the actors dataset: (1) features, row of 56 feature values for address, (2) classes, the class label for address, (3) AddrAddr, all edges involving address in the actor interaction graph, (4) AddrTx, all edges as involving address as the input address in the address-transaction graph, and similarly (5) TxAddr, as the output address.

wallets_features.csv

address time step txs_input · · · lifetime_blocks · · · Addr_interactions_median

39sfuA8pY4UfybgEZi7uvA13jkGzZpsg5K 23 420 · · · 18145 · · · 1

AddrAddr_edgelist.csv wallets_classes.csv

[p. 4] [ref: 3.3]

input_address output_address address class

39sfuA8pY4UfybgEZi7uvA13jkGzZpsg5K 1ML...kTL 39sf...sg5K 1

AddrTx_edgelist.csv TxAddr_edgelist.csv

input_address txId txId output_address

39sfuA8pY4UfybgEZi7uvA13jkGzZpsg5K 272145560 322554634 39sfuA8pY4UfybgEZi7uvA13jkGzZpsg5K

Figure 2: Number of wallet addresses by time step.

3.3 Graph Visualization

Total Wallets Unknown Illicit Licit

In this section, we provide a detailed explanation with visualization of the Elliptic++ dataset using four types of graphs: Money Flow Transaction Graph, Actor Interaction Graph, Address-Transaction Graph, and User Entity Graph. Each graph has its own unique importance.

Number of Addresses

1 5 10 15 20 25 30 35 40 45 49

Time Step

• The Money Flow Transaction Graph shows BTC flow from one transaction to the next, allowing exploration of the spa- tial and temporal patterns surrounding a given transaction. • The Actor Interaction Graph shows the pairwise inter- actions among input and output addresses of transactions, showing the density of the k-hop neighborhoods of wallet addresses. • The Address-Transaction Graph is a heterogenous graph showing flow of BTC across transactions and addresses, al- lowing an evaluation of purposes of a transaction and the relationships among addresses of the same transaction. • The User Entity Graph is an address cluster graph that allows for potential linking of addresses controlled by a specific user, which further de-anonymizes their identity and purpose.

[ref: 3.3.1]

step and 56 address features listed in Table 3 for each transaction it was involved in, and an entry in wallets_classes.csv, rep- resenting its class label (1: illicit, 2: licit, 3: unknown). A wallet address is labelled illicit if it has at least 1 edge with an illicit trans- action, otherwise it is labelled licit if the ratio of its total unknown transactions (edges) to its total licit transactions (edges) is > 3.7 or unknown if ≤3.7. The ratio "3.7" is calculated using the total ratio of unknown transactions to licit transactions in the transac- tions dataset. We also create AddrAddr_edgelist.csv to record the pairwise interactions of input and output addresses through Bitcoin transactions. Each entry represents the input address and output address relationship of one transaction. If there are multiple transactions between a pair of addresses, then there are multiple en- tries in this table. Additionally, we create AddrTx_edgelist.csv, where each entry represents the relationship between an input address and a transaction, and TxAddr_edgelist.csv, with each entry representing a directed connection between a transaction and an output address. With these data structures, the Elliptic++ dataset can be used to build the address-to-address graph (Section 3.3.2), and the address-transaction graph (Section 3.3.3), in addition to the transaction-to-transaction money flow graph (Section 3.3.1).

3.3.1 Money Flow Transaction Graph. This is a directed graph where nodes represent transactions and edges represent directed BTC flows from one transaction to the next. Figure 3 visualizes the distribution of all transactions in time step 32. We choose three transactions (one per class) representing the unknown (yellow), illicit (blue), and licit (red) classes, and display sub-graphs of their four-hop neighbourhoods as shown in the left, middle, and right of Figure 3. All neighbour nodes are shown, though for visual clarity, some edges are abbreviated with dotted arrows signifying that a particular node has two (or more) outgoing edges of the same pattern as the graph is traversed further. This displays the potential utility of exploring the spatial and temporal patterns surrounding a given transaction.

[pp. 4-5]

The distribution of address classes are 2% (14, 266) class-1 (illicit), 31% (251, 088) class-2 (licit), and the remaining are unknown (class- 3). When populated using temporal information provided by the time steps in the transactions dataset, we obtain 1, 268, 260 wallet address occurrences across all time steps, including 2% (28, 601) illicit addresses, 27% (338, 871) licit addresses, and 71% (900, 788) unknown addresses, as shown in Figure 2.

It is important to note that some time steps produce sparse transaction graphs, e.g. time step 14, while others produce dense transaction graphs, e.g. time step 32. We provide a comparison in the Appendix (see Figure 14). This difference in graph density drastically affects the node neighborhood patterns, with some time steps creating shallow, wide money flow transaction graphs, while

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

Figure 5: An address-transaction graph for selected nodes in time step 32 featuring Illicit Actor 13 at the root.

Figure 3: Money flow transaction graphs for selected un- known (left), illicit (middle), and licit (right) transactions in time step 32 (top shows distribution of TS 32 transactions).

txId: 355111463

money flow

≥2 nodes with

addr: 39sfuA8pY4UfybgEZ i7uvA13jkGzZpsg5K

txId: 355006712

same hops

txId: 355007070

licit

… …

txId: 355128718

txId: 355163541

unknown

… … txId: 215596974 …

Actors:

Transactions:

illicit licit unknown

illicit licit unknown

illicit

… txId: 355110111

information regarding the purposes of a transaction and the rela- tionships among addresses connected by the same transaction. We provide a visual comparison of the distributions of all transactions and addresses at both time steps in the Appendix (see Figure 16).

other time steps creating deep, narrow money flow transaction graphs. Moreover, although there are only 2% illicit transactions within the dataset, they are evidently spread out across each time step and hence the ML model trained for anomaly detection over the earlier sequence of time steps can be leveraged to perform forensics on the later part of the sequence of time steps.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics" (2023-05-25). https://arxiv.org/abs/2306.06108
