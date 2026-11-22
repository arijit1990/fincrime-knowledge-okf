---
type: Source Digest
title: Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions - part 1 of 3 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: 1 Introduction; 1 Introduction > 2 H. Tariq and M. Hassani; 2 Related Work; and 3 more sections'
resource: https://arxiv.org/abs/2309.13662
tags:
- academic_finding
- advanced_analytics
- global_academic
- network_graph
- preprint
- transaction_behaviour
status: stable
source_id: arxiv-topology-agnostic-detection-of-temporal-money-laundering-flows-i
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-09-24'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2309.13662
  title: Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions
  author: org:arxiv
  last_modified: '2023-09-24T00:00:00Z'
digest_points: 56
---

# Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Money launderers spread illicit funds across multiple accounts at different banks, layering them through mule accounts so the origin and flow are obscured and the money enters the financial system unnoticed. (p. 1)[^original]  
  <sub>anchor: "Money launderers exploit the weaknesses in detection systems by purposefully placing their ill-gotten money into multiple accounts, at different banks."</sub>
- **descriptive / limitation**: The paper states that path finding algorithms for tracking suspicious money flows usually struggle with scale and complexity, and existing community detection techniques fail to properly capture time-dependent relationships, especially on massive transaction graphs. (p. 1)[^original]  
  <sub>anchor: "Path finding algorithms that aim at tracking suspicious flows of money usually struggle with scale and complexity."</sub>
- **descriptive / context**: The authors propose a framework called FaSTM∀N, adapted to domain-specific constraints, to efficiently build a temporal graph of sequential transactions. (p. 1)[^original]  
  <sub>anchor: "We propose a framework (called FaSTM ∀ N ), adapted for domain-specific constraints, to efficiently construct a temporal graph of sequential transactions."</sub>
- **descriptive / method**: FaSTM∀N includes a weighting method using 2nd order graph representation to quantify the significance of edges, which allows complex queries to be distributed over smaller, densely connected networks of flows from which suspicious flow networks are identified. (p. 1)[^original]  
  <sub>anchor: "The framework includes a weighting method, using 2_nd_ order graph representation, to quantify the significance of the edges."</sub>
- **descriptive / finding or result**: On a dataset of over 1 billion transactions from multiple large European banks, the authors report clear superiority of FaSTM∀N in efficiency and usefulness against two state-of-the-art solutions. (p. 1)[^original]  
  <sub>anchor: "For a dataset of over 1 Billion transactions from _multiple_ large European banks, the results show a clear superiority of our framework both in efficiency and usefulness."</sub>

## 1 Introduction

- **descriptive / context**: UNODC estimates that between 2 and 5% of global GDP is laundered each year, which the paper converts to between EUR 715 billion and 1.87 trillion annually. (p. 1)[^original]  
  <sub>anchor: "The United Nations Office on Drugs and Crime (UNODC) estimates that between 2 and 5% of global GDP is laundered each year."</sub>
- **descriptive / context**: The authors state that financial systems have not been able to effectively monitor and detect money laundering networks, and some big banks have received huge fines from regulators. (p. 1)[^original]  
  <sub>anchor: "Financial systems have not been able to effectively monitor and detect these money laundering networks."</sub>
- **descriptive / limitation**: A major challenge is that banks see only their side of the money trail, whereas a launderer may move money via multiple banks. (p. 1)[^original]  
  <sub>anchor: "One of the major challenges banks face is that they only see their side of the money trail"</sub>
- **descriptive / limitation**: Most money laundering detection models were developed for single-bank transaction data, and banks are rarely interested in processing money trails with more than 2 hops. (p. 1)[^original]  
  <sub>anchor: "Most of the money laundering detection models have been developed keeping in mind single bank transaction data."</sub>
- **descriptive / case example**: Figure 1(a) shows a simple trail where money flows from a dispense account through two intermediate accounts to a sink account over 2 hops, invisible to the green bank. (p. 2)[^original]  
  <sub>anchor: "The money starts flowing from the dispense account (the left most); and ends up in the sink account"</sub>
- **descriptive / case example**: Figure 1(b) shows multiple dispense, intermediate and sink accounts, with the shortest distance between every dispense and sink account being 3. (p. 2)[^original]  
  <sub>anchor: "The shortest distance between every dispense and sink account is 3."</sub>
- **descriptive / case example**: In the complex flow of Figure 1(c), shortest paths between dispense and sink accounts have lengths 2, 3 and 4. (p. 2)[^original]  
  <sub>anchor: "The shortest paths are of lengths 2, 3, and 4."</sub>
- **descriptive / definition**: The three commonly known phases of money laundering are placement, layering and integration; placement injects ill-gotten money into the financial system unnoticed, layering obscures the trail by moving money among accomplices, and integration withdraws money from seemingly legitimate accounts under a false pretext. (p. 2)[^original]  
  <sub>anchor: "Placement is when a criminal injects their ill-gotten money in the financial system, a bank for instance, without raising any suspicion."</sub>
- **descriptive / definition**: Typologies are the different ways a criminal can place, layer and integrate money; the paper uses topology to mean graph topology, distinct from typology. (p. 2)[^original]  
  <sub>anchor: "The different ways a criminal can place, layer, and integrate money are called typologies."</sub>
- **descriptive / typology or red flag**: Smurfing (structuring) is a typology in which a criminal deposits a large amount of cash through several smaller deposits in multiple mule accounts. (p. 2)[^original]  
  <sub>anchor: "Smurfing (or structuring) [1] is one such typology, where a criminal deposits a large chunk of cash using (several) smaller deposits in multiple mule [38] accounts."</sub>
- **descriptive / data or feature**: In Fig. 1, a dotted orange outline on a node marks a dispense account, and a dotted red outline marks a sink account. (p. 2)[^original]  
  <sub>anchor: "The dotted orange outline on a node represents a dispense account"</sub>
- **descriptive / context**: Most modelling focuses on known unknown cases and is designed for single-bank data, and AML experts find it difficult to keep up with new typologies. (p. 3)[^original]  
  <sub>anchor: "It is difficult for the Anti Money Laundering (AML) experts and modelers to keep up."</sub>
- **descriptive / context**: Transaction Monitoring Netherlands (TMNL) is an initiative in which 5 major Dutch banks collaboratively monitor payment transactions for signs of money laundering and terrorism financing. (p. 3)[^original]  
  <sub>anchor: "Transaction Monitoring Netherlands (TMNL) [34] is an initiative where 5 major Dutch banks have joined forces."</sub>
- **descriptive / context**: Other similar initiatives exist elsewhere in the world. (p. 3)[^original]  
  <sub>anchor: "Recently, there have been other similar initiatives [39] [35] [36] throughout the world."</sub>
- **descriptive / requirement**: The paper identifies two needs: dealing with money flows longer than 2 hops in a scalable way, and capturing complex types of flows such as the one in Figure 1(c). (p. 3)[^original]  
  <sub>anchor: "This creates the necessity of 1) dealing with longer (than 2 hops) money flows in a scalable way."</sub>
- **descriptive / finding or result**: The authors claim FaSTM∀N can find unknown cases by discovering new typologies. (p. 3)[^original]  
  <sub>anchor: "With FaSTM ∀ N we are able to find the unknown unknown cases by discovering new typologies."</sub>
- **descriptive / finding or result**: Key contribution one: a scalable method to save and retrieve all possible money flows as a temporal graph; the paper notes adding the time dimension could explode space complexity, and FaSTM∀N generates the temporal graph in a distributed manner and can instantly jump to a point in time. (p. 3)[^original]  
  <sub>anchor: "We show that adding the time dimension to the transaction graph could explode the space complexity."</sub>
- **descriptive / finding or result**: Key contribution two: a novel weighting method using higher-order graph representation to quantify temporal relationships of sequential transactions, which removes insignificant edges and enables efficient complex queries. (p. 3)[^original]  
  <sub>anchor: "A novel weighting method that uses higher-order graph representation to quantify temporal relationships of sequential transactions."</sub>
- **descriptive / finding or result**: Key contribution three: topology-agnostic detection of significant money flows; FaSTM∀N is parameter-free regarding the number of dispense, intermediate and sink accounts, varying path lengths and number of hops. (p. 3)[^original]  
  <sub>anchor: "FaSTM ∀ N is parameterfree when it comes to defining the topological properties like number of dispense, intermediate, and sink accounts"</sub>
- **descriptive / typology or red flag**: Examples of AML risks listed include high cash volume, transactions from or to high-risk countries (for instance as labelled by FATF), and unusual turnover volume for an industry. (p. 3)[^original]  
  <sub>anchor: "High cash volume; transactions from or to high-risk countries (for instance, labelled by the Financial Action Task Force [33])"</sub>

## 2 Related Work

- **descriptive / context**: The authors distinguish money laundering detection from fraud detection and say their research focuses strictly on detecting money laundering networks. (p. 3)[^original]  
  <sub>anchor: "the focus of our research is strictly on detecting networks of money laundering."</sub>
- **descriptive / context**: The authors are not interested in detecting cycles in the transaction graph, because launderers use accounts across banks and geographies so deposits and withdrawals do not mimic a cyclic pattern. (p. 4)[^original]  
  <sub>anchor: "We are also not interested in detecting cycles [20] [32] in our transaction graph."</sub>
- **descriptive / context**: Mapping a UBO (Ultimate Beneficial Owner) to relevant bank accounts remains a big challenge for banks. (p. 4)[^original]  
  <sub>anchor: "Mapping a UBO (or Ultimate Beneficial Owner) [43] to the relevant bank accounts remains a big challenge for the banks [41]."</sub>
- **descriptive / context**: The authors consider methods for detecting structural anomalies in transaction graphs complementary to their framework and say they should not be compared against it. (p. 4)[^original]  
  <sub>anchor: "We believe that such methods are complementary to our framework and as such should not be compared against."</sub>
- **descriptive / context**: Graph node identifier choices include IBAN, parent entity or UBO; edge granularity, weight, direction and attributes are non-trivial design decisions. (p. 4)[^original]  
  <sub>anchor: "Decisions like, selection of node identifier (IBAN [40], parent entity, or UBO [43]); edge granularity"</sub>
- **descriptive / context**: The Louvain algorithm is described as one of the most popular modularity-based community detection methods; the Leiden algorithm, a more advanced version, is used in the authors' framework. (p. 4)[^original]  
  <sub>anchor: "The so called Louvain algorithm [4] is one of the most popular modularity-based [3] community detection methods."</sub>
- **descriptive / context**: The paper reports that Dunbar's number of 150 is relevant in contexts other than social sciences, and notes community size matters for AML because anomalous communities must be analysed by experts. (p. 4)[^original]  
  <sub>anchor: "They show that the Dunbar’s number [2] of 150 is relevant in contexts other than social sciences."</sub>
- **descriptive / limitation**: A big community size can make it humanly impossible for AML experts to analyse anomalous communities. (p. 4)[^original]  
  <sub>anchor: "A big community size, in some cases, makes it humanly impossible to analyze."</sub>
- **descriptive / finding or result**: Community detection methods tend to find communities with dense intra-connections and light inter-connections, which for transaction data yields communities with short paths, usually of 1 or 2 hops. (p. 5)[^original]  
  <sub>anchor: "For a transaction dataset, this would result in communities with short paths. In most cases, paths of 1 or 2 hops are observed."</sub>
- **descriptive / context**: Banks face strict scrutiny from data and financial regulators, so AML models must be free of biases such as geographic and demographic biases, which limits the data points usable. (p. 5)[^original]  
  <sub>anchor: "the AML models have to be void of any kind of biases. This limits the number of data points that can be used in AML models."</sub>
- **descriptive / typology or red flag**: Guilt by association (association fallacy) is a bias risk AML modelers must be aware of. (p. 5)[^original]  
  <sub>anchor: "Guilt by association (or association fallacy) is one such risk that the AML modelers have to be aware of."</sub>
- **descriptive / context**: Detecting dense money flows differs from community detection because a flow has temporal order, and a dependent flow of transactions is more interesting for AML than immediate interactions. (p. 5)[^original]  
  <sub>anchor: "A flow, by definition, has a temporal order."</sub>
- **descriptive / limitation**: Motif queries in temporal graphs are bounded and deterministic, whereas the authors' goal is to capture networks with any possible composition. (p. 5)[^original]  
  <sub>anchor: "Motif queries are bounded and deterministic, whereas our goal is to capture networks with any possible composition."</sub>
- **descriptive / context**: The two baseline methods evaluated are FlowScope and the Database Joins method (DBJ); a major shortcoming of FlowScope is that its design is strictly relevant for a single bank dataset. (p. 5)[^original]  
  <sub>anchor: "A major shortcoming of FlowScope is that its design is strictly relevant for a single bank dataset"</sub>
- **descriptive / definition**: Dynamic grouping in the comparison means explicitly defining how detected paths are grouped as flows, with DBJ defining this by the type 1 and type 2 motif types in its paper. (p. 5)[^original]  
  <sub>anchor: "by dynamic grouping we mean that with DBJ you have to explicitly define how you want to group the detected paths as flows."</sub>
- **descriptive / typology or red flag**: Motivation 1 is few but repeated interactions with the accomplices. (p. 5)[^original]  
  <sub>anchor: "Motivation 1 : Few (but repeated) interactions with the accomplices,"</sub>
- **descriptive / typology or red flag**: Motivation 2 is complicating the money trail by making several hops. (p. 5)[^original]  
  <sub>anchor: "Motivation 2 : Complicating the money trail by making several hops,"</sub>
- **descriptive / typology or red flag**: Motivation 3 is convoluting the trail by having more interactions among the accomplices. (p. 5)[^original]  
  <sub>anchor: "Motivation 3 : Convoluting it further by having more interactions among the accomplices"</sub>
- **descriptive / typology or red flag**: Motivation 4 is breaking down big transactions into many small transactions. (p. 5)[^original]  
  <sub>anchor: "Motivation 4 : Breaking down big transactions into many small transactions."</sub>
- **descriptive / finding or result**: The authors argue that the designs of FlowScope and DBJ do not take into account all of these motivations, while FaSTM∀N addresses them by making as few assumptions as possible. (p. 5)[^original]  
  <sub>anchor: "We argue that the designs for FlowScope and DBJ, do not take into account _all of these_ motivations."</sub>

## 3 Preliminaries

- **descriptive / definition**: Communities of flows, a novel concept claimed by the authors, are closely related and interdependent sequences of transactions detected by FaSTM∀N. (p. 5)[^original]  
  <sub>anchor: "Detecting _communities of flows_ is, to the best of our knowledge, a novel approach that we are proposing in this paper."</sub>

## 2 Related Work

- **descriptive / context**: Table 1 summarises the key differences between DBJ, FlowScope and the proposed framework, covering dynamic grouping, parameter-free number of hops, complex flows and suitability for multi-bank data. (p. 5)[^original]  
  <sub>anchor: "Table 1 summarizes the key differences for the 3 methods."</sub>

## 3.1 Temporal and Higher Order Graphs

- **descriptive / context**: Dynamic graphs are mostly series of static snapshots at different moments in time, and time can be modelled as layers in a multiplex graph. (p. 6)[^original]  
  <sub>anchor: "The dynamic graphs mentioned in [12] are (mostly) series of static snapshots of graphs,"</sub>
- **descriptive / method**: The authors are mostly interested in temporal graphs where paths can only be traversed in chronological order, since in most money laundering typologies money is only pushed forward after it has been received. (p. 6)[^original]  
  <sub>anchor: "We are mostly interested in temporal graphs where the paths can only be traversed in a chronological order."</sub>
- **descriptive / method**: FaSTM∀N builds a static time-dependent graph by creating copies of nodes, aiming to invalidate cyclic paths that do not respect temporal order. (p. 6)[^original]  
  <sub>anchor: "Therefore, for FaSTM ∀ N , we build a static time-dependent graph by creating copies of nodes"</sub>
- **descriptive / finding or result**: Once chronological order is respected, the apparent cyclic behaviour of a flow disappears; the authors note the number of nodes and edges could explode in this representation, which Section 4 addresses using AML knowledge. (p. 6)[^original]  
  <sub>anchor: "It can be observed that the number of nodes and edges could potentially explode with this type of representation."</sub>
- **descriptive / method**: Edge weights are calculated using higher-order graph representations based on the principles in reference [18]; a 2nd order representation records a transaction from A to B followed by one from B to C, incorporating a short memory of sequential transactions. (p. 6)[^original]  
  <sub>anchor: "On the right hand side we have the 2_nd_ order representation, a transaction from A to B is followed by a transaction from B to C."</sub>
- **descriptive / limitation**: The experiments do not consider higher than 2nd order or multi-order representations, which the authors leave to future research. (p. 6)[^original]  
  <sub>anchor: "For our experiments, we did not consider higher (than 2_nd_ ) order"</sub>

## 3.2 Dataset

- **descriptive / data or feature**: The dataset contains around 1.1 billion transactions from 5 large Dutch banks and cannot be revealed in detail because of its sensitive nature. (p. 6)[^original]  
  <sub>anchor: "Our dataset includes around 1.1 billion transactions from 5 large Dutch banks."</sub>

## 3.1 Temporal and Higher Order Graphs

- **descriptive / method**: In the second-order representation, the more dominant or frequent a memory is, the stronger the interdependence of the sequential transactions becomes. (p. 6)[^original]  
  <sub>anchor: "the more dominant (or frequent) a memory is; the stronger"</sub>

## 3.2 Dataset

- **descriptive / data or feature**: Input records have an id for each transaction, a transaction timestamp in Unix time, and source and target account identifiers for sender and receiver, plus an amount; these are the bare minimum data points needed to run FaSTM∀N. (p. 7)[^original]  
  <sub>anchor: "These are the bare minimum data points required to run `FaSTM` _∀_ `N` ."</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions" (2023-09-24). https://arxiv.org/abs/2309.13662
