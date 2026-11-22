---
type: Source Digest
title: 'BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis - part 1 of 3 (pp. 1-6)'
description: 'Verified paraphrased digest, pp. 1-6: BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > I. INTRODUCTION; BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis > II. RELATED WORK; and 6 more sections'
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
part: 1
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
digest_points: 108
---

# BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Cryptocurrencies are described as no longer only the preferred option for cybercriminal activity on darknets, because of growing mainstream adoption. (p. 1)[^original]  
  <sub>anchor: "Cryptocurrencies are no longer just the preferred option for cybercriminal activities on darknets"</sub>
- **descriptive / data or feature**: The authors build a dataset of Bitcoin transactions between 12 July 2019 and 26 May 2021, named BABD-13. (p. 1)[^original]  
  <sub>anchor: "we build a dataset comprising Bitcoin transactions between 12 July 2019 and 26 May 2021"</sub>
- **descriptive / data or feature**: BABD-13 contains 13 types of Bitcoin addresses, 5 categories of indicators with 148 features, and 544,462 labeled data, described as the largest labeled Bitcoin address behavior dataset publicly available to the authors' knowledge. (p. 1)[^original]  
  <sub>anchor: "contains 13 types of Bitcoin addresses, 5 categories of indicators with 148 features, and 544,462 labeled data"</sub>
- **descriptive / finding or result**: Five machine learning models (k-nearest neighbors, decision tree, random forest, multilayer perceptron and XGBoost) reach accuracy between 93.24% and 97.13% on the multi-classification task using the dataset. (p. 1)[^original]  
  <sub>anchor: "accuracy rates of these machine learning models for the multi-classification task"</sub>
- **descriptive / method**: The paper proposes a k-hop subgraph generation algorithm that extracts a k-hop subgraph from the entire Bitcoin transaction graph, built as a directed heterogeneous multigraph, starting from a specific address node such as a known transaction tied to a criminal investigation. (p. 1)[^original]  
  <sub>anchor: "the entire Bitcoin transaction graph constructed by the directed heterogeneous multigraph"</sub>
- **descriptive / finding or result**: The authors initially analyse behavior patterns of different Bitcoin address types using the extracted features and analyse the features and their relationships from the experiments. (p. 1)[^original]  
  <sub>anchor: "we initially analyze the behavior patterns of different types of Bitcoin addresses"</sub>

## I. INTRODUCTION

- **descriptive / context**: The global cryptocurrency market capitalisation is given as 1.77 trillion US dollars and Bitcoin's as 0.74 trillion US dollars, as of 27 February 2022. (p. 1)[^original]  
  <sub>anchor: "the global cryptocurrency market capital is $1.77 Trillion U.S. dollars"</sub>
- **descriptive / context**: Cryptocurrency transactions are described as easier to trace than fiat currency transactions, partly because of the transparency of the public ledger. (p. 1)[^original]  
  <sub>anchor: "one can more easily trace cryptocurrency transactions partly because of the transparency nature of the public ledger"</sub>
- **descriptive / limitation**: Existing transaction-tracing approaches face challenges and limitations ranging from accuracy to information loss and incompleteness, such as not considering internal relations and differences between classifications. (p. 1)[^original]  
  <sub>anchor: "There are, however, a number of challenges and limitations in existing approaches, ranging from accuracy to information loss"</sub>
- **descriptive / limitation**: The authors identify a lack of a comprehensive dataset that can serve as a baseline for the research community. (p. 1)[^original]  
  <sub>anchor: "the lack of a comprehensive dataset that can be used as a baseline for the research community"</sub>
- **descriptive / method**: The paper presents a general framework to build a Bitcoin transaction graph as a directed heterogeneous multigraph and to analyse address nodes from it. (p. 1)[^original]  
  <sub>anchor: "we present a general framework that can be used to build a Bitcoin transaction graph"</sub>
- **descriptive / data or feature**: BABD-13 is used as the baseline dataset to evaluate the five common machine learning models. (p. 1)[^original]  
  <sub>anchor: "We then use BABD-13 as the baseline dataset to evaluate common machine learning models"</sub>

## II. RELATED WORK

- **descriptive / finding or result**: Alqassem et al. studied, using Bitcoin transaction data from 2009 to 2014, how graph structural properties evolve over time, and found the Bitcoin transaction graph generally similar to typical social networks in structural index. (p. 1)[^original]  
  <sub>anchor: "They observed that the Bitcoin transaction graph is generally similar to typical social networks in the structural index"</sub>
- **descriptive / method**: Popuri and Gunes measured general characteristics of the Bitcoin network using complex network theory. (p. 1)[^original]  
  <sub>anchor: "measured the general characteristics of the Bitcoin network using the complex network theory"</sub>
- **descriptive / method**: Serena et al. treated the cryptocurrency transaction graph as a complex network and calculated simple indexes and their changes using degree distribution and aggregation clustering coefficient. (p. 1)[^original]  
  <sub>anchor: "using degree distribution and aggregation clustering coefficient, they calculated several simple indexes"</sub>
- **descriptive / finding or result**: Tao et al. (2021) reported non-rich club effect, small-world phenomenon and other typical characteristics in the Bitcoin transaction graph. (p. 1)[^original]  
  <sub>anchor: "the non-rich club effect, smallworld phenomenon, and other typical characteristics exist in the Bitcoin transaction graph"</sub>
- **descriptive / method**: Ranshous et al. used a directed hypergraph to analyse patterns of exchange addresses, proposed short thick bands to identify them, and applied basic machine learning to classify early exchange addresses. (p. 1)[^original]  
  <sub>anchor: "used the directed hypergraph to analyze the patterns associated with exchange addresses"</sub>
- **descriptive / method**: Romiti et al. selected three of the four biggest mining pools and used economic activity pattern-based methods to study relationships between miner-owned addresses and pools. (p. 1)[^original]  
  <sub>anchor: "selected three of four of the biggest pools to empirically investigate the relationships among them"</sub>
- **descriptive / context**: The excerpt says understanding the full Bitcoin transaction graph is important so that governments and regulators (taxation, law enforcement, financial intelligence units, AML/CTF regulators) can monitor and trace criminal proceeds. (p. 1)[^original]  
  <sub>anchor: "This reinforces the importance of understanding the full Bitcoin transaction graph so that governments and regulatory agencies"</sub>
- **descriptive / context**: The excerpt frames the question of distinguishing normal from suspicious cryptocurrency addresses and says such addresses generally include exchange-related and mining pool-related addresses. (p. 1)[^original]  
  <sub>anchor: "Such addresses generally include exchange-related addresses and mining pool-related addresses."</sub>
- **descriptive / finding or result**: Tovanich et al. studied pool hopping across 15 Bitcoin mining pools and concluded that pool fees and payout schemes are the two most important factors influencing miner-owned address behaviour. (p. 2)[^original]  
  <sub>anchor: "they determined those pool fees and payout schemes are the two most important factors"</sub>
- **descriptive / finding or result**: Liao et al. measured Bitcoin amounts in ransomware cases and the resulting financial loss. (p. 2)[^original]  
  <sub>anchor: "measured data such as Bitcoin amount in ransomware cases and the resulting financial loss"</sub>
- **descriptive / data or feature**: Conti et al. analysed the financial impact of ransomware, presented its timeline, and built a public dataset of ransomware-related Bitcoin addresses. (p. 2)[^original]  
  <sub>anchor: "They then built a public dataset of ransomwarerelated Bitcoin addresses"</sub>
- **descriptive / finding or result**: Paquet-Clouston et al. proposed a framework to identify and collect ransomware-related Bitcoin addresses and showed how the Bitcoin amount changed from 2013 to 2017. (p. 2)[^original]  
  <sub>anchor: "the change of the Bitcoin amount over time from 2013 to 2017"</sub>
- **descriptive / data or feature**: Bartoletti et al. collected Ponzi scheme addresses from Bitcoin forums and proposed 11 features for Bitcoin address classification. (p. 2)[^original]  
  <sub>anchor: "proposed 11 features for Bitcoin address classification"</sub>
- **descriptive / finding or result**: Vasek and Moore found, in Ponzi scheme data from a Bitcoin forum, that cybercriminals interacted more frequently with victims and posted more comments in the thread. (p. 2)[^original]  
  <sub>anchor: "observed that cybercriminals interacted more frequently with the victims and posted more comments in the thread"</sub>
- **descriptive / finding or result**: Toyoda et al. studied high yield investment programs (a kind of Ponzi scheme), applied supervised learning to classify HYIP addresses, and reported an accuracy rate of 93.75%. (p. 2)[^original]  
  <sub>anchor: "The accuracy rate of their approach is as high as 93.75%"</sub>
- **descriptive / limitation**: Most existing approaches use a simplified Bitcoin transaction graph (such as an undirected simple graph) rather than its original structure, which may cause information loss. (p. 2)[^original]  
  <sub>anchor: "most existing approaches prefer to utilize the simplified Bitcoin transaction graph"</sub>
- **descriptive / limitation**: The authors state that the address types in most existing works are inaccurate and/or incomplete; for instance, at most 7 address types were analysed together in one recent work. (p. 2)[^original]  
  <sub>anchor: "at most 7 types of addresses were analyzed together in recent works"</sub>
- **descriptive / limitation**: Indicators in existing approaches are described as generally not systematic or comprehensive, and the graph construction is not publicly clear, making those approaches hard to replicate. (p. 2)[^original]  
  <sub>anchor: "these approaches are hard to replicate since it is not clear (publicly) how the Bitcoin transaction graph(s) is/are built"</sub>

## III. BACKGROUND MATERIALS / A. Bitcoin Graph Structure

- **descriptive / context**: The Bitcoin transaction graph is essentially a kind of unspent transaction output (UTXO) model. (p. 2)[^original]  
  <sub>anchor: "Bitcoin transaction graph is essentially a kind of unspent transaction output (UTXO) model"</sub>
- **descriptive / limitation**: The authors argue that simplifying the Bitcoin transaction graph, as in many existing approaches, leads to information loss in graph analysis. (p. 3)[^original]  
  <sub>anchor: "the above and similar approaches to simplify the Bitcoin transaction graph will lead to information loss"</sub>
- **descriptive / method**: The paper proposes an improved directed heterogeneous multigraph structure based on Maesa et al., with characteristics of both address nodes and transaction nodes, to preserve analysis accuracy. (p. 3)[^original]  
  <sub>anchor: "we proposed an improved directed heterogeneous multigraph Bitcoin structure based on the structure proposed by Maesa et al."</sub>

## III. BACKGROUND MATERIALS / B. Behavior Classification and Definition

- **descriptive / context**: Classifying and defining typical Bitcoin address behaviours exactly is described as significant for improving classification and understanding address behaviour patterns. (p. 3)[^original]  
  <sub>anchor: "It is significant to classify and define typical behaviors of Bitcoin addresses exactly"</sub>
- **descriptive / definition**: The paper studies 13 mainstream illicit and licit Bitcoin address types. (p. 3)[^original]  
  <sub>anchor: "We will study and analyze the mainstream 13 types of illicit and licit Bitcoin addresses in this paper"</sub>
- **descriptive / definition**: Blackmail addresses: cryptocurrency blackmail has three typical categories (ransomware, sextortion and scam) that threaten or deceive victims into paying cryptocurrency to specific addresses. (p. 3)[^original]  
  <sub>anchor: "Cryptocurrency blackmail has three typical categories that are ransomware, sextortion, and scam"</sub>
- **descriptive / definition**: Cyber-security service addresses belong to providers of payment gateways, proxy or VPN services and other cybersecurity services that accept only cryptocurrency as payment to improve service security. (p. 3)[^original]  
  <sub>anchor: "providers only accept cryptocurrency as payment in order to improve the security of their services"</sub>
- **descriptive / definition**: Darknet market addresses belong to markets on the darknet where illegal goods and services are bought and sold anonymously, with traders exchanging through cryptocurrencies to enhance anonymity. (p. 3)[^original]  
  <sub>anchor: "traders are oriented to exchange through cryptocurrencies"</sub>
- **descriptive / definition**: Centralized exchange addresses belong to exchanges that earn fees as intermediaries, run know-your-customer policies, allow trading of crypto pairs and swaps between cryptocurrency and fiat. (p. 3)[^original]  
  <sub>anchor: "earn fees by acting as trustworthy intermediaries among their customers"</sub>
- **descriptive / definition**: P2P financial infrastructure service addresses belong to peer-to-peer financial activity conducted only in cryptocurrency, such as bond markets and P2P lending platforms. (p. 3)[^original]  
  <sub>anchor: "Examples are bond markets and P2P lending platforms"</sub>
- **descriptive / definition**: P2P financial service addresses belong to applications that reward users in cryptocurrency for contributions to missions helpful to organisers, including faucets, video sharing and affiliate marketers. (p. 3)[^original]  
  <sub>anchor: "P2P financial applications use cryptocurrency as a reward according to users’ contributions"</sub>
- **descriptive / definition**: Gambling addresses belong to casino-style games such as blackjack and roulette in which only cryptocurrencies can be used as wagers. (p. 3)[^original]  
  <sub>anchor: "playing casino games, such as blackjack and roulette, in which only cryptocurrencies can be utilized as wagers"</sub>
- **descriptive / definition**: Government criminal blacklist addresses include cryptocurrency addresses highly suspected or confirmed to be involved in criminal activity, according to different countries' laws. (p. 3)[^original]  
  <sub>anchor: "includes cryptocurrency addresses highly suspected or confirmed involved in criminal activities"</sub>
- **descriptive / definition**: Money laundering is the movement of dirty cryptocurrency from illegal sources to normal addresses through complicated, hard-to-trace methods, generally in three stages: placement, laundering and integration. (p. 3)[^original]  
  <sub>anchor: "Generally, money laundering includes the following three stages that are placement, laundering, and integration"</sub>

## III. BACKGROUND MATERIALS / B. Statistical Indicator

- **descriptive / definition**: Pure Amount Indicator (PAI) relates to the token amount attributes of address nodes in the Bitcoin transaction graph. (p. 3)[^original]  
  <sub>anchor: "is related to the token amount attributes of _Ads_ nodes"</sub>
- **descriptive / definition**: Pure Time Indicator (PTI) covers time-related attributes of address nodes. (p. 3)[^original]  
  <sub>anchor: "is time-related attributes of _Ads_ nodes"</sub>
- **descriptive / definition**: Combination Indicator (CI) consists of combinations of features drawn from PAI, PDI and PTI. (p. 3)[^original]  
  <sub>anchor: "is the combinations of the features from"</sub>
- **descriptive / data or feature**: The excerpt notes that the token amount in the tables is the original Bitcoin transaction data, i.e. BTC, and that the basic unit is the solar day of 24 hours. (p. 3)[^original]  
  <sub>anchor: "the basic unit mentioned in the above tables is the solar day of 24 hours"</sub>

## III. BACKGROUND MATERIALS / B. Behavior Classification and Definition

- **descriptive / definition**: Ponzi scheme addresses belong to schemes where the initiator pays high interest in cryptocurrency to earlier investors using money from new investors, so investors believe profits are easily earned in a short time. (p. 4)[^original]  
  <sub>anchor: "the initiator of the Ponzi scheme will pay high interests by cryptocurrency to the former investors"</sub>
- **descriptive / definition**: Mining pool addresses belong to groups of miners pooling computational resources to improve the chance of finding a new block; the majority of coinbase-related addresses in Bitcoin belong to mining pools. (p. 4)[^original]  
  <sub>anchor: "the majority of addresses related to coinbase transactions in Bitcoin belong to mining pools"</sub>
- **descriptive / definition**: Tumbler addresses belong to services that prevent tracing of cryptocurrency flows by combining multiple inputs over a long period and sending outputs to destinations at random times. (p. 4)[^original]  
  <sub>anchor: "send different inputs to their planned destinations at random times"</sub>
- **descriptive / definition**: Individual wallet addresses are wallets owned by ordinary people who use cryptocurrency as a payment method in daily life. (p. 4)[^original]  
  <sub>anchor: "Individual wallets stand for the wallets owned by ordinary people who use cryptocurrency"</sub>

## III. BACKGROUND MATERIALS / C. Data Collection

- **descriptive / method**: The Bitcoin ledger was collected through a public API. (p. 4)[^original]  
  <sub>anchor: "We collect the Bitcoin ledger using the public API"</sub>
- **descriptive / data or feature**: The ledger data covers 100,001 blocks with block heights from 585,000 to 685,000, corresponding to 12 July 2019 to 26 May 2021. (p. 4)[^original]  
  <sub>anchor: "based on 100,001 blocks data, where the block height is from 585,000 to 685,000"</sub>
- **descriptive / data or feature**: The built transaction graph contains 516,167,131 address and transaction nodes and 713,703,239 relationship edges. (p. 4)[^original]  
  <sub>anchor: "including 516,167,131 address and transaction nodes and 713,703,239 relationship edges"</sub>
- **descriptive / limitation**: Because of device performance limits only 100,001 blocks were used, although the approach can in principle build transaction graphs of any size. (p. 4)[^original]  
  <sub>anchor: "Due to our device performance limitations, we only use 100,001 blocks to build the bitcoin transaction graph"</sub>
- **descriptive / definition**: Labelled addresses are split into strong addresses (strongly confirmed label) and weak addresses (weaker confirmed label, e.g. reported addresses). (p. 4)[^original]  
  <sub>anchor: "the address with the week confirmed label (e.g. the reported address)"</sub>
- **descriptive / data or feature**: Some weak addresses were gathered from a number of social accounts on Twitter. (p. 4)[^original]  
  <sub>anchor: "and a number of social accounts on Twitter7"</sub>

## IV. FRAMEWORK

- **descriptive / method**: The authors propose their own framework for extracting and analysing Bitcoin address behaviours from the directed heterogeneous multigraph, based on indicators from several earlier works. (p. 4)[^original]  
  <sub>anchor: "we proposed our own framework for extracting and analyzing Bitcoin address behaviors from the Bitcoin transaction graph"</sub>

## IV. FRAMEWORK / B. Statistical Indicator

- **descriptive / method**: The framework has two parts: statistical indicators (SI) and local structural indicators (LSI). (p. 4)[^original]  
  <sub>anchor: "The proposed framework consists of two parts that are the"</sub>
- **descriptive / method**: The statistical indicator is divided into four types: Pure Amount Indicator, Pure Degree Indicator, Pure Time Indicator and Combination Indicator. (p. 4)[^original]  
  <sub>anchor: "in our proposed scheme is divided into four concrete indicator types"</sub>
- **descriptive / data or feature**: The Pure Amount Indicator relates to token amount attributes of address nodes in the transaction graph. (p. 4)[^original]  
  <sub>anchor: "is related to the token amount attributes of"</sub>
- **descriptive / data or feature**: The Combination Indicator combines features from the amount, degree and time indicators. (p. 4)[^original]  
  <sub>anchor: "is the combinations of the features from"</sub>
- **descriptive / data or feature**: Table II lists basic statistical indicators including PDIa1, the in-degree, out-degree and in-degree plus out-degree of an address node. (p. 4)[^original]  
  <sub>anchor: "The in-degree/out-degree/in-degree and out-degree of an address"</sub>
- **descriptive / data or feature**: Table II includes the life period of an address (PTIa1) and the active period of an address (PTIa2) among its time indicators. (p. 4)[^original]  
  <sub>anchor: "The active period of an address"</sub>
- **descriptive / definition**: Token amount in the statistical indicators is the original Bitcoin transaction data, i.e. BTC. (p. 4)[^original]  
  <sub>anchor: "the token amount in the above tables is the original data of the Bitcoin transactions, i.e., BTC"</sub>
- **descriptive / definition**: The basic unit used in the tables is the solar day of 24 hours. (p. 4)[^original]  
  <sub>anchor: "the basic unit mentioned in the above tables is the solar day of 24 hours"</sub>
- **descriptive / method**: For address-node features the authors also compute simplified features by recomputing them after merging duplicate directed edges, added as new features. (p. 4)[^original]  
  <sub>anchor: "we recompute the same features after combining the same directed edges in the Bitcoin transaction graph"</sub>

## IV. FRAMEWORK / C. Local Structural Indicator

- **descriptive / context**: The authors assume that the characteristics of a subgraph of addresses close to an address reflect information about that address. (p. 4)[^original]  
  <sub>anchor: "considering the characteristics of a subgraph composed of addresses that are close to an address can reflect some information about that address"</sub>
- **descriptive / method**: The proposed Algorithm 1 generates a k-hop subgraph for each labelled address node by treating the graph as undirected and traversing edges breadth-first from a given address, keeping the real edge directions. (p. 4)[^original]  
  <sub>anchor: "traverse each edge in breadth-first order starting from a given address"</sub>

## III. BACKGROUND MATERIALS / C. Data Collection

- **descriptive / data or feature**: Table I gives labelled counts split into strong and weak addresses. Blackmail has 8,686 addresses (8 strong, 8,678 weak). Cyber-Security Service has 91,617, Darknet Market 13,861 and Centralized Exchange 300,000, all strong. (p. 4)[^original]  
  <sub>anchor: "Blackmail|8,686 (8 / 8,678)|"</sub>
- **descriptive / data or feature**: Table I lists P2P Financial Infrastructure Service with 180, P2P Financial Service with 9,309, Gambling with 105,257, Government Criminal Blacklist with 27 and Money Laundering with 16 addresses, all of them strong. (p. 4)[^original]  
  <sub>anchor: "Gambling|105,257 (105,257 / 0)|"</sub>
- **descriptive / data or feature**: Table I lists Ponzi Scheme with 15 addresses (8 strong, 7 weak), Mining Pool with 1,580 (all strong), Tumbler with 12,412 (10,817 strong, 1,595 weak) and Individual Wallet with 1,502 (52 strong, 1,450 weak). (p. 4)[^original]  
  <sub>anchor: "Tumbler|12,412 (10,817 / 1,595)|Individual Wallet|1,502 (52 / 1,450)|"</sub>
- **descriptive / finding or result**: In total, the labelled dataset contains 544,462 addresses, of which 532,732 are strong and 11,730 are weak. (p. 4)[^original]  
  <sub>anchor: "_Total Number_|544,462 (532,732 / 11,730)|"</sub>
- **descriptive / definition**: A strong address (SA) is one with a strongly confirmed label. A weak address (WA) is one with a weakly confirmed label, such as a reported address; the excerpt writes this as 'week confirmed label'. (p. 4)[^original]  
  <sub>anchor: "the address with the week confirmed label (e.g. the reported address)"</sub>
- **descriptive / data or feature**: Strong addresses were mainly collected from a public dataset and government blacklists, with further strong data taken from high-influence papers. Weak addresses came from a public reported-address dataset and Twitter accounts. (p. 4)[^original]  
  <sub>anchor: "_SA_ s mainly collected from the public dataset"</sub>

## IV. FRAMEWORK / C. Local Structural Indicator

- **descriptive / method**: Algorithm 1 uses two thresholds: a maximum value of k and a maximum number of address and transaction nodes, to keep subgraphs from becoming too large. (p. 5)[^original]  
  <sub>anchor: "we set two thresholds for the proposed algorithm"</sub>
- **descriptive / method**: In the implementation the maximum sum of address and transaction nodes is set to 3,000. (p. 5)[^original]  
  <sub>anchor: "we choose 3,000 as the maximum number of the sum of"</sub>
- **descriptive / method**: The maximum value of k is set to 4. (p. 5)[^original]  
  <sub>anchor: "= 4 as the maximum value"</sub>
- **descriptive / finding or result**: Figures 2(a) to 2(c) contain less structural information than the other subgraphs, while Figures 2(g) and 2(h) contain so much information similar to the whole graph that distinctive information is hard to extract. (p. 5)[^original]  
  <sub>anchor: "contain less structural information than other 5 figures"</sub>
- **descriptive / finding or result**: Figures 2(g) and 2(h) contain too much information similar to the entire transaction graph to yield distinctive information. (p. 5)[^original]  
  <sub>anchor: "have too much information that is similar to the entire transaction graph"</sub>
- **descriptive / finding or result**: Among Figures 2(d) to 2(f) the structures are almost identical, so the authors chose Figure 2(d), with 3,000 nodes, for efficiency. (p. 5)[^original]  
  <sub>anchor: "their structural are almost identical, thus, we choose Fig. 2(d)"</sub>
- **descriptive / finding or result**: Similar conclusions were found for many other address nodes across different Bitcoin address types. (p. 5)[^original]  
  <sub>anchor: "we find similar conclusions in many other address nodes in different types of Bitcoin addresses"</sub>
- **descriptive / limitation**: The chosen hyperparameters are described as a balance between the device's performance limit and the usefulness of the local indicators. (p. 5)[^original]  
  <sub>anchor: "this set of hyperparameters achieves a balance between our device’s performance limit"</sub>
- **descriptive / method**: The average degree feature (S1) is computed from the average degree of nodes in the subgraph, and the authors compute average values and standard deviations of in-degree, out-degree and in-degree plus out-degree as LSI features. (p. 5)[^original]  
  <sub>anchor: "we calculate the average values and standard deviations of in-degree/outdegree/in-degree and out-degree"</sub>
- **descriptive / definition**: The degree distribution feature (S2) is the proportion of nodes with a given degree in the subgraph, computed for in-degree, out-degree and total degree. (p. 5)[^original]  
  <sub>anchor: "that means the proportion of the node with the"</sub>
- **descriptive / method**: For the degree distribution feature the degree is divided into three types: in-degree, out-degree, and in-degree plus out-degree. (p. 5)[^original]  
  <sub>anchor: "the degree here can be divided into three types"</sub>

## III. BACKGROUND MATERIALS / B. Statistical Indicator

- **descriptive / definition**: Pure Degree Indicator (PDI) covers the degree-related attributes of address nodes in the Bitcoin transaction graph. (p. 5)[^original]  
  <sub>anchor: "includes the degreerelated attributes of _Ads_ nodes in the Bitcoin transaction graph"</sub>
- **descriptive / data or feature**: Table II feature PAIa1 is the input or output token amount of an address node. (p. 5)[^original]  
  <sub>anchor: "The input/output token amount of an address node"</sub>
- **descriptive / data or feature**: Table II feature PAIa11 is the total input or output token amount of an address node. (p. 5)[^original]  
  <sub>anchor: "The total input/output token amount of an address node"</sub>
- **descriptive / data or feature**: Table II feature PAIa14 is the minimum or maximum input or output token amount of an address node. (p. 5)[^original]  
  <sub>anchor: "The minimum/maximum input/output token amount of an address node"</sub>
- **descriptive / data or feature**: Table II feature PAIa17 is the standard deviation of all input, output and combined token amounts of an address node. (p. 5)[^original]  
  <sub>anchor: "The standard deviation of all input/output/input and output token amounts of an address node"</sub>
- **descriptive / data or feature**: Table II feature PAIa21 is the minimum or maximum input or output value of the RAa ratio feature. (p. 5)[^original]  
  <sub>anchor: "The minimum/maximum input/output value of _RAa__in/out_3"</sub>
- **descriptive / data or feature**: Table II feature PAIa22 is the standard deviation of all input and output values of the RAa ratio feature. (p. 5)[^original]  
  <sub>anchor: "The standard deviation of all input/output values of"</sub>
- **descriptive / data or feature**: Table II feature PDIa1 gives the in-degree, out-degree and in-degree plus out-degree of an address. (p. 5)[^original]  
  <sub>anchor: "The in-degree/out-degree/in-degree and out-degree of an address"</sub>
- **descriptive / data or feature**: Table II feature PDIa11 is a ratio of in-degree to total degree and out-degree to total degree. (p. 5)[^original]  
  <sub>anchor: "The ratio of_A__in__d__A__all__d_and _Aout__d__A__all__d_"</sub>
- **descriptive / data or feature**: Table II feature PDIa12 is the ratio of in-degree to out-degree of an address. (p. 5)[^original]  
  <sub>anchor: "The ratio of_A__in__d__A__out__d_"</sub>
- **descriptive / data or feature**: Table II feature PDIa13 is the difference between in-degree and out-degree of an address. (p. 5)[^original]  
  <sub>anchor: "The difference of _A__in__d __−Aout__d_"</sub>
- **descriptive / data or feature**: Table II feature PTIa1 is the life period of an address. (p. 5)[^original]  
  <sub>anchor: "The life period of an address"</sub>
- **descriptive / data or feature**: Table II feature PTIa2 is the active period of an address. (p. 5)[^original]  
  <sub>anchor: "The active period of an address"</sub>
- **descriptive / data or feature**: Table II feature PTIa3 is the number of active times of an address in each basic unit of the active period. (p. 5)[^original]  
  <sub>anchor: "The number of active times of an address in each basic unit of the active period"</sub>
- **descriptive / data or feature**: Table II feature PTIa31 is the minimum, maximum or average of the active-times feature. (p. 5)[^original]  
  <sub>anchor: "The minimum/maximum/average active times of _A__v__n_"</sub>
- **descriptive / data or feature**: Table II feature PTIa32 is the difference between the maximum and minimum active times. (p. 5)[^original]  
  <sub>anchor: "The difference of _A__v__nmax __−Av__nmin_"</sub>
- **descriptive / data or feature**: Table II feature PTIa33 is the standard deviation of the active-times feature. (p. 5)[^original]  
  <sub>anchor: "The standard deviation of _A__v__n_"</sub>
- **descriptive / data or feature**: Table II feature PTIa4 is the time interval between transactions of an address, in chronological order. (p. 5)[^original]  
  <sub>anchor: "The time interval of transactions of an address (chronological order)"</sub>
- **descriptive / data or feature**: Table II features PTIa41 to PTIa43 are the minimum, maximum or average time interval, the difference between maximum and minimum intervals, and the standard deviation of intervals. (p. 5)[^original]  
  <sub>anchor: "The minimum/maximum/average time interval of _A__ti_"</sub>
- **descriptive / data or feature**: Table II feature PTIa42 is the difference between the maximum and minimum time intervals of an address. (p. 5)[^original]  
  <sub>anchor: "The difference of _A__ti__max __−Ati__min_"</sub>
- **descriptive / data or feature**: Table II feature PTIa43 is the standard deviation of the time interval of transactions of an address. (p. 5)[^original]  
  <sub>anchor: "The standard deviation of time interval of _A__ti_"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Yuexin Xiang, Yuchen Lei, Bao Fu Ding, Tiantian Li, Qingqing Yang, Wenmao Liu et al., "BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis" (2023-12-28). https://arxiv.org/abs/2204.05746
