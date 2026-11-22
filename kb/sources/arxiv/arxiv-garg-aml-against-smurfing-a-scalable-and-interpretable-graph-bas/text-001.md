---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 1 of 10 (pp. 1-4)'
description: 'Verbatim extracted text, pp. 1-4: ABSTRACT; 1 Introduction; 2 Related Work'
resource: https://arxiv.org/abs/2506.04292
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-garg-aml-against-smurfing-a-scalable-and-interpretable-graph-bas
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-04-06'
legal_status: unknown
part: 1
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 1 of 10, pp. 1-4. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Bruno Deprez_∗_ Bart Baesens Tim Verdonck Wouter Verbeke KU Leuven KU Leuven University of Antwerp - imec KU Leuven University of Antwerp - imec University of Southampton KU Leuven

Money laundering, a global problem estimated to account for 2%-5% of the global GDP, required regulators to enforce stringent rules on financial institutions to combat it. One prominent laundering method, called smurfing, relies on breaking up transactions into smaller amounts to evade detection. Given the complexity of laundering schemes, involving numerous transactions across multiple parties, network analytics is an important tool for anti-money laundering. However, recent advances in network analytics have leaned heavily on black-box network embedding methods, limiting their utility in businesses. To address the specific nature of smurfing and banks’ operational requirements, this paper introduces GARG-AML, a novel graph-based method that quantifies smurfing risk through a single interpretable metric derived from the structure of the second-order transaction network. Unlike traditional methods, GARG-AML provides a balance between computational efficiency and transparency, enabling integration into existing AML workflows. We demonstrate the scalability of GARG-AML on large random networks, and its performance on two open-source money laundering datasets. Our results highlight the potential of GARG-AML to enhance smurfing detection and support investigative decision-making.

## ABSTRACT


_Keywords_ Fraud Analytics _·_ Anti-Money Laundering _·_ Network Analytics _·_ Smurfing _·_ Microstructuring

Criminals launder an estimated USD 2 trillion, up to 5% of global GDP, a year to disguise their illicit profits and fund future crimes (United Nations Office on Drugs and Crime, 2011). To mitigate this, regulators have mandated that financial institutions serve as the primary front in anti-money laundering (AML) efforts (FATF, 2012-2023; Levi and Reuter, 2006).

## 1 Introduction


[pp. 1-2]

Financial institutions have put in place AML detection and reporting processes. This often starts with alert generation. Alert generation is an automatic process for spotting unusual behaviour, and results in many false positives. Manual investigation filters out legitimate transactions, based on both internal (e.g., transactions and client records) and external data (e.g., public domain information searches on company structure). The remaining alerts are further investigated to build cases, which contain multiple alerts. Expert investigators decide if a suspicious activity report (SAR) is filed to the regulator (Halford et al., 2025; Jullum et al., 2020; FATF, 2012-2023; Levi and Reuter, 2006).

A large portion of generated alerts comes from business rules flagging large transaction amounts in accordance with regulation (Welling, 1989; Bolton and Hand, 2002; Senator et al., 1995; Oztas et al., 2024; Jullum et al., 2020). These rules also consider aggregation attempts, where criminals make many transactions each staying under the reporting threshold, but where the aggregated amount passes a certain threshold. However, the efficacy of these rules is often compromised by the sheer volume and complexity of global transaction data.

> _∗_ Corresponding author: `bruno.deprez@kuleuven.be`

A popular method to circumvent these business rules is _smurfing_ (Madinger, 2012; Welling, 1989; Starnini et al., 2021; Zhdanova et al., 2014). Criminals split transactions into smaller amounts and transfer them through money mules, called smurfs, to dodge the rules. Smurfing makes AML harder since (1) the chain between the criminal activity and the criminals’ bank accounts is interrupted, and (2) smaller transactions through distinct accounts seem less suspicious.

Banks monitor millions of transactions and require multiple departments to report suspicious activity. To be useful, any new tool must meet at least these two criteria:

- The method must process large volumes of transactions in a memory and time-efficient manner;

- The predictions must be interpretable for smooth integration in SAR filing.

Despite these business requirements, the current network-based AML literature focuses on black box graph neural networks (GNNs) (Deprez et al., 2026). Consequently, many institutions rely on business rules and manual feature engineering based on expert knowledge.

[p. 2]

To address the specific nature of smurfing and the operational requirements, we introduce G raph- A ided R isk G rading for A nti- M oney L aundering (GARG-AML), a novel method that grades clients based on their second-order neighbourhood in the transaction network. GARG-AML quantifies how closely an account’s network structure resembles known smurfing patterns.

Moreover, we present an extension using tree-based learners to increase smurf detection power. This shows the versatility and power of our method, without compromising on the business need of speed and simplicity.

The performance is evaluated against state-of-the-art smurfing detection methods using both synthetic data and two open-source network datasets. These datasets, which include millions of clients and transactions, closely resemble real-world financial networks. As a result, our experiments assess both detection power and computational efficiency.

The main contributions of this work are as follows:

- We introduce a novel smurfing detection method that is scalable to large transaction networks, interpretable and easily integrated into existing models;

- We evaluate our method on multiple datasets that are uniquely suited for assessing the effectiveness of our approach;

- We compare the current state-of-the-art in smurfing detection methods, and we analyse the scalability of these methods to very large transaction datasets, where the original papers only tested their methods on substantially smaller datasets.

The remainder of this work is organised as follows. Related work on anti-money laundering and smurfing is discussed in Section 2. The methodology behind GARG-AML is described in Section 3. Section 4 outlines the experimental evaluation, with results presented in Section 5. We discuss the main data and methodological limitations in Section 6. Section 7 concludes this work.

The full implementation of the experiments is made available on GitHub2 . The GARG-AML implementation is also published as the open-source Python package `garg-aml-smurfing` , available via PyPI3 , fostering the adoption of our method by researchers and practitioners.

## 2 Related Work


[pp. 2-3]

According to Routine Activity Theory (RAT), criminal acts occur when three elements converge: a motivated offender, a suitable target, and the absence of a capable guardian. In the context of money laundering, all three are present (Cohen and Felson, 1979):

- Motivated Offenders: Criminal organisations seeking to integrate “dirty” money into the legitimate economy without triggering regulatory alarms.

- Suitable Targets: Financial institutions, whose systemic gaps or high transaction volumes can be exploited to hide illicit flows.

> 2 `https://github.com/B-Deprez/GARG-AML`

> 3 `https://pypi.org/project/garg-aml-smurfing/`

Figure 1: The two smurfing patterns; as scatter-gather (left) and gather-scatter (right).

- Capable Guardians: The AML systems and human investigators tasked with identifying and reporting suspicious activity.

Current technological “guardians” largely rely on IF-THEN business rules that monitor individual transactions or aggregate amounts over time (Bolton and Hand, 2002; Leonard, 1995; S´anchez et al., 2009; Welling, 1989; Cardoso et al., 2022; Deprez et al., 2026). While transparent, these rules are often ineffective as they are easily circumvented once the underlying logic is exposed, reducing their utility as capable guardians (Zhu and Hu, 2013; Van Belle et al., 2023). Additionally, the volume and complexity of monitored transactions often compromise the effectiveness of these guardians (Mat Isa et al., 2025; Lokanan, 2025). As a result, machine learning has emerged as a preferred approach, offering scalability and the ability to detect complex laundering patterns (Chen et al., 2018; Jullum et al., 2020; Ramadhan, 2024).

Network analytics has emerged as a critical tool for AML, shifting the focus from individual transactions to the structural interactions between entities (Deprez et al., 2026). Current literature can be categorised into three primary research streams: manual feature engineering, deep learning architectures, and pattern-specific detection frameworks.

Early research emphasised the use of centrality measures for profile definition. Dre˙zewski et al. (2015) used centrality measures to define nine roles in criminal networks. Fronzetti Colladon and Remondi (2017) used similar metrics across industries and analysed the correlation with the target label to demonstrate the added value of network analytics for AML. Wu et al. (2021a) defined temporal motives tailored to money laundering and mixing detection in the Bitcoin network.

[pp. 3-4]

Deep learning has been studied extensively through GNNs (Lo et al., 2023; Alarab et al., 2020; Weber et al., 2019; Deprez et al., 2026). These methods capture the complex geometry of suspicious money laundering activities in financial networks by learning network topology while also incorporating node features. A drawback is that GNNs are not interpretable (Kute et al., 2021), which limits their use by investigators.

Smurfing, also called microstructuring, has long been a popular laundering method (Welling, 1989; Senator et al., 1995). Welling (1989) sees it as a consequence of the Bank Secrecy Act in the USA, which required reporting of transactions above $10,000. Similar monetary-based systems are still in place that require immediate investigation of transactions that surpass a given amount (Senator et al., 1995; Oztas et al., 2024; Bolton and Hand, 2002).

Although many money laundering methods and patterns exist (Suzumura and Kanezashi, 2021), two types of patterns are typical for smurfing (Starnini et al., 2021; Altman et al., 2023): (1) scatter-gather and (2) gather-scatter. Both patterns are visualised in Figure 1. With scatter-gather, money is sent to its destination account via money mules. Gather-scatter, on the other hand, consists of collecting money from multiple accounts into one (or a few) account(s) and sending it to many destination accounts. Gather-scatter is a popular money laundering method for cryptocurrencies (Wu et al., 2021b).

Smurfing makes use of smurfs, who function as money mules. Smurfs are recruited from outside the criminal organisation for a short period of time. Criminals lure the young or financially vulnerable with promises of quick cash, using them to open accounts in the victim’s name to funnel illicit funds through (Esoimeme, 2020; Leukfeldt and Jansen, 2015; Bekkers et al., 2025).

The evolution of laundering techniques like smurfing is best explained by Rational Choice Theory (McCarthy and Chaudhary, 2014). Offenders seek to maximise reward while minimising the risk of detection. By splitting large, reportable sums into smaller transactions funnelled through smurfs, criminals exploit the ‘blind spots’ of rule-based systems. This tactic interrupts the visible chain of funds, making illicit flows appear indistinguishable from legitimate retail banking activity.

Table 1: Summary of key aspects of the methodology in the literature.

[p. 4]

|Paper|Pattern|Client Scoring|Parallel Calculation|All Nodes|Code|Scalable|
|---|---|---|---|---|---|---|
|Zhdanova et al.(2014)|Scatter-gather|✓|✓|✓|||
|Li et al.(2020)|Scatter-gather|||✓|✓|✓|
|Lee et al.(2020)|Scatter-gather|✓|||✓||
|Starnini et al.(2021)|Scatter-gather & gather-scatter||✓|||✓|
|Shadrooh and Nørv˚ag(2024)|Scatter-gather|✓||||✓|
|Prado-Romero et al.(2018)|Gather-scatter|✓|✓|✓|||
|Wu et al.(2021a)|Gather-scatter|||||✓|
|This work|Scatter-gather & gather-scatter|✓|✓|✓|✓|✓|

Table 2: Summary of key aspects of the experimental set-ups in the literature.

|Paper|Dataset|Size Dataset (nodes)|Metrics|
|---|---|---|---|
|Zhdanova et al.(2014)|Simulated|10,000|Precision, recall|
|Li et al.(2020)|Proprietary & Czech Financial|6,130,000 & 11,374|F1, Time|
|Lee et al.(2020)|Czech Financial & Enron|11,374 & 16,771|Accuracy|
|Starnini et al.(2021)|Proprietary|18,000,000 (reduced to 21,000)|Time|
|Shadrooh and Nørv˚ag(2024)|Czech Financial & Enron &Darpa|11,374 & 16,771 & 371,000|Time, Precision, Recall, F1|
|Prado-Romero et al.(2018)|Bitcoin|942,204|Recall|
|Wu et al.(2021a)|WalletExplorer|_±_2_,_500_,_000|TPR, FPR, geometric mean|
|This work|Simulated & IBM AML|100 & 10,000 & 100,000 &515,080 & 2,054,390|Time, AUC-ROC, AUC-PR,Precision, F1, Precision@K,Rank|

There is a rich collection of research specifically on smurfing detection. PSA@R (Zhdanova et al., 2014) detects smurfing in mobile money networks. It uses different underlying workflow models. Transaction streams that differ from the process model are flagged as anomalous. FlowScope (Li et al., 2020) identifies anomalous sub-graphs by calculating the net inflow and outflow at intermediate middlemen who ideally retain zero balance. AutoAudit (Lee et al., 2020) utilises adjacency matrix reordering to expose high-density blocks that signify coordinated smurfing. Starnini et al. (2021) and SMoTeF (Shadrooh and Nørv˚ag, 2024) incorporate temporal constraints, pruning data to focus on motifs that emerge within specific time windows. FaSTM _∀_ N (Tariq and Hassani, 2025) tries to find anomalous money flows, or sub-graphs, from a temporal representation of sequential transactions.

Closely related to smurfing is mixing, which is a money laundering method that is used for cryptocurrencies (Liu et al., 2021). Coins are transferred to the same entity and are redistributed afterward, resulting in a gather-scatter pattern.

Prado-Romero et al. (2018) introduce an anomaly score for mixing detection by identifying mixing services that act as bridges between unrelated user communities. Wu et al. (2021a) applies positive and unlabelled (PU)-learning using predefined temporal motifs. These are extracted from two networks, one with just accounts as nodes and the other with accounts and transactions as nodes.

The methodologies and experimental setups of these existing works are summarised and juxtaposed against GARGAML in Table 1 and Table 2, respectively. Methods for anti-money laundering on fiat currency consider scatter-gather patterns, while research on crypto-currency is mostly concerned with gather-scatter.

The evaluation in most papers is done on relatively small datasets. The Czech dataset (Data World, 1999) is used most. It is a small network containing approximately 11,000 nodes and 273,000 edges. This dataset is unlabelled, so the authors of each paper inject synthetic patterns. Evaluation and comparison is often limited to threshold-dependent metrics like precision, recall and F1. GARG-AML addresses these limitations by providing an interpretable, parallelisable scoring framework evaluated on massive, realistic transaction networks using threshold-independent metrics.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
