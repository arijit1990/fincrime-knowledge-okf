---
type: Source Digest
title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models - part 1 of 4 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models; Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > Abstract; Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > 1 Introduction; and 2 more sections'
resource: https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
tags:
- academic_finding
- academic_paper
- datasets_benchmarks
- global_academic
- network_graph
status: stable
source_id: academic-publisher-realistic-synthetic-financial-transactions-for-anti
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-12-15'
legal_status: unknown
part: 1
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:02Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:02Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:02Z'
sources:
- id: original
  resource: https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
  title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models
  author: org:academic_publisher
  last_modified: '2023-12-15T00:00:00Z'
digest_points: 69
---

# Realistic Synthetic Financial Transactions for Anti-Money Laundering Models (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper cites a UN estimate that 2-5% of global GDP, or roughly $0.8-$2.0 trillion, is laundered globally each year. (p. 1)[^original]  
  <sub>anchor: "The UN estimates 2-5% of global GDP or $0.8 - $2.0 trillion dollars are laundered globally each year"</sub>
- **descriptive / context**: Real data to train machine learning models to detect laundering is generally unavailable, and previous synthetic generators had significant shortcomings. (p. 1)[^original]  
  <sub>anchor: "real data to train machine learning models to detect laundering is generally not available, and previous synthetic data generators have had significant shortcomings"</sub>
- **descriptive / context**: The paper contributes a synthetic financial transaction dataset generator and a set of synthetically generated AML datasets, calibrated to match real transactions as closely as possible and made public. (p. 1)[^original]  
  <sub>anchor: "this paper contributes a synthetic financial transaction dataset generator and a set of synthetically generated AML"</sub>
- **descriptive / finding or result**: The authors argue synthetic data can be better than real data for comparing models because its ground truth labels are complete, whereas many laundering transactions in real data are never detected. (p. 1)[^original]  
  <sub>anchor: "the ground truth labels are complete, whilst many laundering transactions in real data are never detected"</sub>

## 1 Introduction

- **descriptive / context**: Money laundering is the movement of illicit funds to conceal their origin and make them appear to come from legitimate sources; schemes often cross bank and national boundaries. (p. 1)[^original]  
  <sub>anchor: "Money laundering refers to the movement of illicit funds to conceal their origin and make them appear to come from legitimate sources"</sub>
- **descriptive / context**: The UN figure for global laundering is up to $2 trillion per year. (p. 1)[^original]  
  <sub>anchor: "the UN puts the global figure at up to $2 trillion per year [6] as noted in the abstract"</sub>
- **descriptive / context**: The CEO of Danske Bank resigned in 2019 after it was revealed that the Estonian branch alone may have laundered $230 billion. (p. 1)[^original]  
  <sub>anchor: "The CEO of Danske Bank resigned in 2019 after it was revealed that the Estonian branch alone may have laundered $230 billion"</sub>
- **descriptive / context**: Finextra estimates about $200 billion of laundering in 2017 solely in U.S. online sales. (p. 1)[^original]  
  <sub>anchor: "Finextra estimates that in 2017 there may have been $200 billion in laundering solely in U.S. online sales"</sub>
- **descriptive / definition**: Relational tables are the most common way of storing financial data, with each row a transaction moving assets from a source to a destination account, possibly at different banks, with amount, timestamp, currency and payment type recorded. (p. 2)[^original]  
  <sub>anchor: "Relational tables are the most common way of storing financial data"</sub>
- **descriptive / definition**: In a financial transaction graph, nodes typically represent accounts and directed edges represent transactions, so such graphs are directed multigraphs. (p. 2)[^original]  
  <sub>anchor: "the nodes typically represent accounts and the directed edges between the accounts represent financial transactions"</sub>
- **descriptive / typology or red flag**: A cycle, where money sent from one account returns to the same account, is described as a strong indicator of money laundering. (p. 2)[^original]  
  <sub>anchor: "the existence of such cycles is a strong indicator of money laundering"</sub>
- **descriptive / typology or red flag**: Cryptocurrency criminals use mixing and shuffling schemes, which can usually be expressed as subgraph structures such as scatter-gather and bipartite patterns. (p. 2)[^original]  
  <sub>anchor: "Such schemes can usually be expressed in terms of subgraph structures, such as scatter-gather and bipartite patterns"</sub>
- **descriptive / method**: Contribution one is a multi-agent synthetic transaction generator in which some agents are criminals with illicit income; it gives perfect information on which transactions are laundering and which patterns are used. (p. 2)[^original]  
  <sub>anchor: "builds a multi-agent virtual world in which some of the agents are criminals with illicit income to launder"</sub>
- **descriptive / data or feature**: Contribution two is a set of realistic, standardized AML datasets covering a range of sizes and difficulties, all made publicly available. (p. 2)[^original]  
  <sub>anchor: "The datasets cover a range of sizes and difficulties and are all made publicly available"</sub>
- **descriptive / method**: Contribution three is initial experiments with Graph Neural Networks and Gradient Boosted Trees providing baselines; the GNN code is open source and GBT results are reproducible with public tools. (p. 2)[^original]  
  <sub>anchor: "Importantly, our GNN code is open source. In addition, our GBT results can be reproduced using publicly available tools"</sub>

## 2 Related Work

- **descriptive / context**: Legal, privacy and competition concerns mean real financial transaction data is generally not available, and even anonymized data lacks ground truth labels. (p. 2)[^original]  
  <sub>anchor: "legal, privacy, and competition concerns mean that real financial transaction data is not generally available"</sub>

## 1 Introduction

- **descriptive / limitation**: Real data is often unavailable for legal and privacy reasons, and its labeling is inherently poor because much laundering goes undetected, according to the cited sources. (p. 2)[^original]  
  <sub>anchor: "Even if real data were available, its labeling is inherently poor, as most laundering often goes undetected"</sub>
- **descriptive / context**: The paper lists as a contribution observations on how its data release is ethically sound and supports the fight against money laundering and other financial crime. (p. 2)[^original]  
  <sub>anchor: "Observations in Section 7 about how our data release is ethically sound"</sub>

## 2 Related Work

- **descriptive / finding or result**: Starnini et al. report six months of data from a major Italian bank with 180M transactions, looking only for two laundering patterns, with no guarantee all instances are detected; the data was not available to other investigators. (p. 3)[^original]  
  <sub>anchor: "which reports 6 months of data from a major Italian bank with 180M transactions"</sub>
- **descriptive / context**: Harris et al. received 2,827 transaction history summaries for 4,469 customers of Scotia Bank in Canada to assess which customers pose a high laundering risk. (p. 3)[^original]  
  <sub>anchor: "received 2,827 transaction history summaries for 4,469 customers of Scotia Bank in Canada"</sub>
- **descriptive / limitation**: Existing AML synthetic data efforts suffer from one or more shortcomings: generators needing access to real data to mimic, lacking authoritative laundering labels, or lacking important attributes of real data. (p. 3)[^original]  
  <sub>anchor: "existing AML efforts suffer from one or more of the following shortcomings"</sub>
- **descriptive / context**: Previous synthetic AML efforts are agent-based; modelling fidelity and scale matter because illicit transactions are a tiny minority class. (p. 3)[^original]  
  <sub>anchor: "For activities like money laundering, with only a tiny fraction of illicit transactions"</sub>
- **descriptive / finding or result**: Table 1 compares MLDP, AMLsim and the paper's AMLworld: MLDP has 2,340 transactions and laundering rate 3/5; AMLsim has 1.32 M transactions and rate 1/762; AMLworld has 180 M transactions and rates 1/807 and 1/1,750. (p. 3)[^original]  
  <sub>anchor: "Table 1 outlines key aspects of money laundering data"</sub>
- **descriptive / context**: The authors state that higher transaction counts and lower laundering rates are generally more realistic; the MLDP scenario with 2,340 transactions and a 60% laundering rate is described as tiny and unrealistic. (p. 3)[^original]  
  <sub>anchor: "The 2,340 transactions and 60% laundering rate for _MLDP_ suggest a tiny, unrealistic scenario"</sub>
- **descriptive / context**: GNNs are models designed for graph-structured relational data and have been used for financial crime detection, including money laundering, phishing on Ethereum and fraudulent transaction detection. (p. 3)[^original]  
  <sub>anchor: "GNNs [65, 59, 14, 30, 23, 15, 35, 62] are powerful machine learning models specifically designed for relational data (graphs)"</sub>
- **descriptive / method**: Graph Substructure Network uses pre-calculated subgraph pattern counts to improve GNN expressivity. (p. 3)[^original]  
  <sub>anchor: "takes advantage of pre-calculated subgraph pattern counts to improve the expressivity of GNNs"</sub>

## 3 Synthetic Datasets

- **descriptive / context**: Abundant labeled data exists for images, speech, NLP and recommendation, but little or no financial transaction data is broadly available due to privacy, law and competitive advantage. (p. 3)[^original]  
  <sub>anchor: "little or no financial transaction data is broadly available"</sub>

## 2 Related Work

- **descriptive / finding or result**: The paper describes the 2,340 transactions and 60% laundering rate of MLDP as suggesting a tiny, unrealistic scenario. (p. 3)[^original]  
  <sub>anchor: "The 2,340 transactions and 60% laundering rate for _MLDP_ suggest a tiny, unrealistic scenario"</sub>
- **descriptive / finding or result**: The paper states that AMLworld's capabilities are significantly more advanced than those of its predecessors, making for more robust data sets. (p. 3)[^original]  
  <sub>anchor: "the capabilities of _AMLworld_ are significantly more advanced than those of its predecessors, making for more robust data sets"</sub>

## 3.1 Motivation for Synthetic Data

- **descriptive / limitation**: Individual banks see only their own transactions, not those at the other institutions with which their customers transact. (p. 4)[^original]  
  <sub>anchor: "Individual banks see only their own transactions – not the transactions at the multitude of other institutions"</sub>
- **descriptive / limitation**: Real ground truth labels are usually incomplete, so many AML models mislabel laundering transactions as false negatives. (p. 4)[^original]  
  <sub>anchor: "Ground truth labels are usually incomplete, with many instances of laundering being missed"</sub>
- **descriptive / limitation**: Identifying complex laundering patterns in real data requires additional work, if it is possible at all for individual banks. (p. 4)[^original]  
  <sub>anchor: "Identifying complex money laundering patterns in real data requires additional work"</sub>
- **descriptive / method**: Conclusive ground truth in synthetic data enables precise model comparison, and multiple banks allow measuring performance gains from federated learning; a single bank can be simulated by filtering. (p. 4)[^original]  
  <sub>anchor: "The conclusive ground truth labels in synthetic data enable the precise comparison of different models"</sub>

## 3.2 AML patterns

- **descriptive / definition**: Suzumura and Kanezashi's AMLSim generator introduced a set of 8 money laundering patterns, which AMLworld also generates. (p. 4)[^original]  
  <sub>anchor: "introduced a set of 8 patterns2 often used in money laundering"</sub>
- **descriptive / definition**: A fan-out pattern is a vertex whose outgoing edges connect it to at least k ≥ 2 different vertices. (p. 4)[^original]  
  <sub>anchor: "a fan-out pattern of vertex _v_ , shown in Figure 2a, is defined by the outgoing edges of _v_ connecting _v_ to at least _k ≥_ 2 different vertices"</sub>
- **descriptive / definition**: A fan-in pattern is a vertex connected to at least k ≥ 2 different vertices via incoming edges. (p. 4)[^original]  
  <sub>anchor: "for a _fan-in_ pattern, shown in Figure 2b, _v_ is connected to _k ≥_ 2 different vertices via incoming edges"</sub>
- **descriptive / definition**: A gather-scatter pattern combines a fan-in and a fan-out pattern of the same vertex. (p. 4)[^original]  
  <sub>anchor: "A _gather-scatter_ pattern combines a fan-in pattern with a fan-out pattern of the same vertex"</sub>
- **descriptive / definition**: A scatter-gather pattern is formed when a fan-out from one vertex and a fan-in to another connect both to the same set of intermediate vertices; Figure 2d shows four intermediate vertices. (p. 4)[^original]  
  <sub>anchor: "form a _scatter-gather_ pattern if the fan-out and the fan-in patterns connect vertices _v_ and _u_ , respectively, to the same set of intermediate vertices"</sub>
- **descriptive / definition**: A simple cycle is a sequence of edges starting and ending at the same vertex that visits other vertices at most once. (p. 5)[^original]  
  <sub>anchor: "A _simple cycle_ pattern, shown in Figure 2e, is a sequence of edges that starts and ends with the same vertex and visits other vertices at most once"</sub>
- **descriptive / typology or red flag**: In Figure 1, node A launders money through nodes C and D in a cycle. (p. 5)[^original]  
  <sub>anchor: "Figure 1 shows a cycle in the financial transaction graph, in which node A launders money through nodes C and D"</sub>
- **descriptive / definition**: A random pattern resembles a cycle except that funds are not returned to their original account, so it can be viewed as a random walk among accounts owned or controlled, e.g. through shell companies. (p. 5)[^original]  
  <sub>anchor: "random can be viewed as a random walk among accounts owned or controlled (e.g. through shell companies)"</sub>
- **descriptive / definition**: A bipartite pattern moves funds from a set of input accounts to a set of output accounts; a stack pattern extends it by adding an additional bipartite layer. (p. 5)[^original]  
  <sub>anchor: "A _bipartite_ pattern in Figure 2g moves funds from a set of input accounts to a set of output accounts"</sub>
- **descriptive / typology or red flag**: In all laundering patterns the laundering entity owns or controls all accounts used, e.g. shell companies that appear to own an account; accurate Ultimate Beneficial Owner designations are difficult to enforce or detect. (p. 5)[^original]  
  <sub>anchor: "accurate UBO designations can be difficult to enforce or detect"</sub>

## 3.3 What is new in our AMLworld generator?

- **descriptive / method**: AMLworld models the full money laundering cycle of placement, layering and integration, whereas AMLSim models only layering. (p. 5)[^original]  
  <sub>anchor: "AMLworld models the entire money laundering cycle [19]"</sub>
- **descriptive / typology or red flag**: Placement in AMLworld can come from nine criminal sources: extortion, loan sharking, gambling, prostitution, kidnapping, robbery, embezzlement, drugs and smuggling. (p. 5)[^original]  
  <sub>anchor: "Placement in _AMLworld_ can come from 9 sources of criminal activity: extortion, loan sharking, gambling, prostitution, kidnapping, robbery, embezzlement, drugs, and smuggling"</sub>
- **descriptive / method**: AMLworld tags illicit funds from their origin through all transactions used to launder them, and laundering is not limited to specific patterns. (p. 5)[^original]  
  <sub>anchor: "To support this detailed laundering model _AMLworld_ tags illicit funds from their origin"</sub>

## 3.4 The Virtual World Model

- **descriptive / method**: AMLworld is a multi-agent virtual world of banks, individuals and companies that buy items and make bank transfers for supplies, salaries and pensions; bad actors include those smuggling and laundering. (p. 6)[^original]  
  <sub>anchor: "At its foundation _AMLworld_ builds a multi-agent virtual world of banks, individuals, and companies"</sub>
- **descriptive / method**: Some laundering transfers occur naturally, e.g. a criminal boss pays employees or buys supplies as part of normal activity. (p. 6)[^original]  
  <sub>anchor: "a criminal boss launders money by paying employees, buying supplies, etc"</sub>
- **descriptive / data or feature**: AMLworld has been used to generate billions of transactions in dollars, euros, yuan, yen, bitcoin and other currencies. (p. 6)[^original]  
  <sub>anchor: "has been used to generate billions of transactions in a variety of currencies including dollars, euros, yuan, yen, bitcoin"</sub>
- **descriptive / method**: All agent actions are governed by statistical distributions and no seed of real transactions is used; the data is described as synthetic and based on real statistics rather than anonymized real individuals. (p. 6)[^original]  
  <sub>anchor: "Likewise, our model uses no seed of real transactions from which to expand. Everything is synthetic"</sub>
- **descriptive / method**: The entity graph is a variant of Circular Flow graphs used to measure GDP, where each person or company owns one or more bank accounts and edges reflect financial flows. (p. 6)[^original]  
  <sub>anchor: "The entity graph in Figure 5 is essentially a variant of the _Circular Flow_ graphs used to measure GDP"</sub>
- **descriptive / method**: Transactions are generated at appropriate frequencies; salaries are typically paid weekly, biweekly or monthly, and interest is almost always paid monthly. (p. 6)[^original]  
  <sub>anchor: "salaries are typically paid weekly, biweekly, or monthly (as noted in Figure 4). Interest is almost always paid monthly"</sub>
- **descriptive / method**: Because the generator knows the source of all funds, it knows which transfers are laundering. (p. 6)[^original]  
  <sub>anchor: "Since the generator knows the source of all funds, it knows which transfers are laundering"</sub>
- **descriptive / context**: Multiple entity types exist, including individuals, corporations, partnerships and sole proprietors; banks are a special entity type where most transactions occur. (p. 6)[^original]  
  <sub>anchor: "There are multiple types of entities in the model, including individuals, corporations, partnerships, and sole proprietors"</sub>
- **descriptive / typology or red flag**: Holding multiple accounts across banks can serve legitimate saving and spending but can also facilitate obfuscating fund sources during laundering. (p. 7)[^original]  
  <sub>anchor: "This spreading can further legitimate pursuits such as saving and spending, but can also facilitate illegal activity"</sub>
- **descriptive / typology or red flag**: Cross-linked company ownership and individual ownership represent legitimate complexity and allow layers of shell companies, whose accounts may sit at arbitrary banks, through which bad actors can launder funds. (p. 7)[^original]  
  <sub>anchor: "it allows layers of shell companies to be created through"</sub>
- **descriptive / method**: The graph is arbitrary and not bipartite between merchants and consumers, unlike some credit card transaction modelling. (p. 7)[^original]  
  <sub>anchor: "the graph is not bipartite between merchants and consumers as can be the case in modeling credit card transactions"</sub>
- **descriptive / method**: The simulator parameterizes population and transaction information for tuning, modelling behaviour changes, and updating to match real behaviour; feedback loops enforce consistency, e.g. adjusting parameters if too many transactions per person per month occur. (p. 7)[^original]  
  <sub>anchor: "if results show too many transactions per person per month, then parameters may be adjusted"</sub>
- **descriptive / method**: Some events take precedence, e.g. avoiding a negative bank balance generally outranks earning a higher interest rate; parameters are not independent so iteration is needed. (p. 7)[^original]  
  <sub>anchor: "moving money to avoid a negative bank account balance takes precedence in most cases over moving money to get a higher interest rate"</sub>
- **descriptive / method**: Synthetic data supports what-if scenarios, such as more laundering or changes to banking laws, which real data cannot offer. (p. 7)[^original]  
  <sub>anchor: "what if there were more laundering, or what if there were changes to banking laws"</sub>
- **descriptive / method**: The laundering tag is transitive: if A pays B $100 in illicit funds, and B and C pass on parts, those later amounts are also laundering; the tag propagates through co-mingled funds. (p. 7)[^original]  
  <sub>anchor: "the laundering tag on financial transfers is transitive in _AMLworld_"</sub>
- **descriptive / finding or result**: The authors state AMLworld's complete labeling of laundering is nearly impossible to achieve with real-world data. (p. 7)[^original]  
  <sub>anchor: "AMLworld’s complete labeling of laundering is nearly impossible with real-world data"</sub>

## 3.5 Public Availability of Synthetic Data

- **descriptive / data or feature**: Several synthetic AML datasets are on Kaggle, divided into HI and LI groups with higher and lower illicit ratios, each split into small, medium and large sizes; large datasets have 175M-180M transactions. (p. 7)[^original]  
  <sub>anchor: "Both HI and LI are further divided into _small_ , _medium_ , and _large_ datasets, with _large_ having 175 _M −_ 180 _M_ transactions"</sub>
- **descriptive / finding or result**: The LI-Large dataset has 176M transactions spanning a little over three months; the other five datasets are said to share similar characteristics apart from size and laundering rates. (p. 7)[^original]  
  <sub>anchor: "LI - _Large_ has 176M transactions spanning a little over 3 months"</sub>
- **descriptive / finding or result**: In LI-Large, 1 in 1,750 transactions is laundering. (p. 7)[^original]  
  <sub>anchor: "Overall 1 in 1,750 transactions is laundering in LI _-Large_"</sub>
- **descriptive / finding or result**: Starnini et al.'s real data (180M transactions over six months from an Italian bank) contains 855 laundering motifs, each with less than 20 nodes, equating to roughly 1 laundering transaction per 21,000. (p. 7)[^original]  
  <sub>anchor: "They find 855 laundering _motifs_ (equivalent to our _Gather-Scatter_ and _Scatter-Gather_ patterns)"</sub>
- **descriptive / finding or result**: LI-Large contains 8,212 combined Gather-Scatter and Scatter-Gather transactions, giving about 1 laundering transaction per 21,440 transactions from these patterns, very similar to the real-data figure. (p. 7)[^original]  
  <sub>anchor: "LI _-Large_ has 8,212 combined _Gather-Scatter_ and _Scatter-Gather_ transactions"</sub>
- **descriptive / finding or result**: The distribution of transaction formats such as ACH, wire and cheque in LI-Large is shown in Table 5, and the numbers correspond roughly with Federal Reserve statistics. (p. 7)[^original]  
  <sub>anchor: "Table 5 shows the distribution of transaction formats like ACH, wire, and cheque"</sub>
- **descriptive / context**: The AMLworld datasets are divided into HI and LI groups with higher and lower illicit ratios respectively, and each group is further divided into small, medium and large datasets, with large having 175M to 180M transactions; Table 4 in the Appendix gives details. (p. 7)[^original]  
  <sub>anchor: "Data is divided into two high-level groups: HI and LI , with higher and lower illicit ratios"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "Realistic Synthetic Financial Transactions for Anti-Money Laundering Models" (2023-12-15). https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
