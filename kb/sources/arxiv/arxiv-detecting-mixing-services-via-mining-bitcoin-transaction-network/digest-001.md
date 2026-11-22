---
type: Source Digest
title: Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs - part 1 of 3 (pp. 1-6)
description: 'Verified paraphrased digest, pp. 1-6: Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > I. INTRODUCTION; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > II. DATA COLLECTION; and 5 more sections'
resource: https://arxiv.org/abs/2001.05233
tags:
- academic_finding
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-detecting-mixing-services-via-mining-bitcoin-transaction-network
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-01-21'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2001.05233
  title: Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs
  author: org:arxiv
  last_modified: '2021-01-21T00:00:00Z'
digest_points: 108
---

# Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Bitcoin is described as the first decentralized peer-to-peer cryptocurrency allowing trading with pseudonymous addresses, and its P2P and pseudonymous nature makes transactions hard to track, enabling illegal activity. (p. 1)[^original]  
  <sub>anchor: "the P2P and pseudonymous nature of Bitcoin make transactions on this platform very difficult to track"</sub>
- **descriptive / method**: The paper provides a feature-based network analysis framework to identify statistical properties of mixing services at network, account and transaction levels. (p. 1)[^original]  
  <sub>anchor: "we provide a feature-based network analysis framework to identify statistical properties of mixing services from three levels"</sub>
- **descriptive / method**: The authors propose Attributed Temporal Heterogeneous motifs (ATH motifs) to characterise transaction patterns of different address types. (p. 1)[^original]  
  <sub>anchor: "we propose the concept of Attributed Temporal Heterogeneous motifs (ATH motifs)"</sub>
- **descriptive / method**: Imperfect labelling is handled by treating mixing detection as a Positive and Unlabeled (PU) learning problem and building a detection model on the features. (p. 1)[^original]  
  <sub>anchor: "we tackle the mixing detection task as a Positive and Unlabeled learning (PU learning) problem"</sub>

## I. INTRODUCTION

- **descriptive / context**: About 7,000 Bitcoins worth $40.7 million were reported stolen from Binance, and the stolen coins can be cashed out through exchanges. (p. 1)[^original]  
  <sub>anchor: "about 7,000 Bitcoins which worth $40.7 million were stolen from Binance recently"</sub>
- **descriptive / context**: Exchanges typically implement a Know-Your-Customer (KYC) process to verify user identities, which exposes thieves when stolen coins are cashed out through them. (p. 1)[^original]  
  <sub>anchor: "exchanges typically implement the Know-Your-Customer (KYC) process"</sub>
- **descriptive / case example**: Mixing services such as BitLaundry, Helix Light and Bitcoin Fog have been shown to be involved in laundering stolen Bitcoin and are significant tools for concealing illicit profits. (p. 1)[^original]  
  <sub>anchor: "mixing services such as BitLaundry, Helix Light, Bitcoin Fog, etc., have involved in this process of money laundering"</sub>
- **descriptive / context**: Bitcoin mixing services were originally designed to enhance transaction anonymity; in the illustrated example three users send 1 BTC each to a mixer, which randomly returns funds to new addresses, confusing the source-destination relationship. (p. 1)[^original]  
  <sub>anchor: "the relationships between sources and destinations are confused, thus increasing the difficulty of tracing the source of funds"</sub>
- **descriptive / context**: Because real identities behind addresses are only revealed through exchange interactions, the authors state it is unlikely KYC can be enforced for regulation of mixing, so identifying mixing services is of value for a healthier Bitcoin ecosystem. (p. 1)[^original]  
  <sub>anchor: "it is unlikely to enforce the KYC process for regulation"</sub>

## Abstract

- **descriptive / context**: The P2P and pseudonymous nature of Bitcoin makes transactions hard to track, which has triggered various illegal activities in the Bitcoin ecosystem. (p. 1)[^original]  
  <sub>anchor: "the P2P and pseudonymous nature of Bitcoin make transactions on this platform very difficult to track"</sub>

## I. INTRODUCTION

- **descriptive / context**: About 7,000 Bitcoins worth $40.7 million were reportedly stolen from Binance, one of the largest cryptocurrency exchanges. (p. 1)[^original]  
  <sub>anchor: "about 7,000 Bitcoins which worth $40.7 million were stolen from Binance recently"</sub>
- **descriptive / context**: Exchanges typically implement a KYC process; with it, the identity of thieves can be easily exposed via identity information held by exchanges. (p. 1)[^original]  
  <sub>anchor: "the identity of the thieves can be easily exposed via the identity information provided by the exchanges"</sub>
- **descriptive / context**: Stolen Bitcoins usually need to be laundered into clean Bitcoins before they can be cashed out. (p. 1)[^original]  
  <sub>anchor: "before being cashed out"</sub>
- **descriptive / context**: Mixing services such as BitLaundry, Helix Light and Bitcoin Fog have been shown to be involved in money laundering and can be significant tools for concealing illicit profits. (p. 1)[^original]  
  <sub>anchor: "mixing services such as BitLaundry, Helix Light, Bitcoin Fog, etc., have involved in this process of money laundering"</sub>
- **descriptive / context**: Bitcoin mixing services were originally designed to enhance transaction anonymity and make the sources of funds more untraceable. (p. 1)[^original]  
  <sub>anchor: "Bitcoin mixing services are originally designed to enhance the anonymity of transactions"</sub>
- **descriptive / case example**: Figure 1 illustrates three users each sending 1 BTC to three addresses of a mixing service, which returns the coins randomly to three new addresses, confusing the link between sources and destinations. (p. 1)[^original]  
  <sub>anchor: "Three users represented as A1, A2 and A3 send 1 Bitcoin (abbreviation BTC) to three addresses M 1, M 2 and M 3"</sub>
- **descriptive / context**: Prior work reports that mixing services and exchanges are two key components in laundering Bitcoins, with mixing services having a higher propensity to be used for laundering illicit money. (p. 2)[^original]  
  <sub>anchor: "mixing services and exchanges are two key components in laundering Bitcoins"</sub>
- **descriptive / context**: Prior work reverse-engineered the operation of several mixing services, and Prado-Romero et al. proposed mixing detection using community outlier detection. (p. 2)[^original]  
  <sub>anchor: "PradoRomero et al. proposed the problem of mixing detection and tackled this problem by exploiting the method of community outlier detection"</sub>
- **descriptive / limitation**: Bitcoin mixing detection is challenging due to incomplete label information: labelled mixing addresses are a small fraction of all addresses. (p. 2)[^original]  
  <sub>anchor: "Labeled addresses associated with mixing services occupy only a small fraction of all addresses"</sub>
- **descriptive / limitation**: Challenge of various obfuscation patterns: mixing services run by different third-party platforms have obfuscation patterns that vary considerably. (p. 2)[^original]  
  <sub>anchor: "their obfuscation patterns vary a lot from each other"</sub>
- **descriptive / method**: Two temporal directed transaction networks are constructed: a homogeneous Address-Address Interaction Network (AAIN) and a heterogeneous Transaction-Address Interaction Network (TAIN), with a two-stage strategy used to improve detection. (p. 2)[^original]  
  <sub>anchor: "we construct two kinds of temporal directed transaction networks including a homogeneous Address-Address Interaction Network (AAIN)"</sub>
- **descriptive / method**: The framework has four modules: data collection, network construction, feature extraction, and model training and application. (p. 2)[^original]  
  <sub>anchor: "the proposed mixing detection framework mainly contains four modules"</sub>
- **descriptive / finding or result**: The claimed contributions include being the first to apply network motifs to Bitcoin mixing detection, and showing temporal and ATH motifs are important; the model achieves a high true positive rate and a low false positive rate. (p. 2)[^original]  
  <sub>anchor: "The proposed model achieves a high true positive rate and a low false positive rate in Bitcoin mixing detection"</sub>

## II. DATA COLLECTION

- **descriptive / context**: WalletExplorer provides address labels by transacting with services and observing how Bitcoin flows merge, but its name database has not been updated since 2016 and so does not include newly emerging services. (p. 2)[^original]  
  <sub>anchor: "the name database of WalletExplorer no longer updated since 2016"</sub>

## I. INTRODUCTION

- **descriptive / context**: Because real identities behind Bitcoin addresses are rarely learned, the authors state it is unlikely KYC can be enforced for regulation of mixing. (p. 2)[^original]  
  <sub>anchor: "it is unlikely to enforce the KYC process for regulation"</sub>
- **descriptive / context**: The authors aim to detect addresses belonging to mixing services by mining transaction records, so that users involved in criminal activity can be traced. (p. 2)[^original]  
  <sub>anchor: "To this end, in this paper, we focus on detecting addresses belonging to mixing services via mining the transaction records"</sub>
- **descriptive / context**: Mixing services and exchanges are reported as two key components in laundering Bitcoins, and mixing services have a higher propensity to be used in laundering illicit money. (p. 2)[^original]  
  <sub>anchor: "mixing services have a higher propensity to be used in laundering illicit money"</sub>
- **descriptive / context**: Prior work reverse-engineered the operation of several mixing services, and Prado-Romero et al. proposed mixing detection using community outlier detection. (p. 2)[^original]  
  <sub>anchor: "PradoRomero et al. proposed the problem of mixing detection and tackled this problem by exploiting the method of community outlier detection"</sub>
- **descriptive / limitation**: Incomplete label information is a challenge: labeled mixing addresses form only a small fraction of all addresses, and the identities of most others are unknown. (p. 2)[^original]  
  <sub>anchor: "Labeled addresses associated with mixing services occupy only a small fraction of all addresses"</sub>
- **descriptive / limitation**: Some mixing services use hubs to combine transactions or split large amounts into smaller ones, making mixing processes and involved addresses harder to identify. (p. 2)[^original]  
  <sub>anchor: "Some mixing services use hubs to combine multiple transactions or split a large amount of money into multiple smaller transactions"</sub>
- **descriptive / limitation**: Obfuscation patterns vary widely because mixing services are provided by different third-party platforms. (p. 2)[^original]  
  <sub>anchor: "Mixing services are provided by different third-party platforms, and their obfuscation patterns vary a lot from each other"</sub>
- **descriptive / method**: The authors treat mixing detection as a Positive and Unlabeled (PU) learning problem to cope with incomplete labels, and adopt a two-stage strategy. (p. 2)[^original]  
  <sub>anchor: "we tackle the task of Bitcoin mixing detection as a Positive and Unlabeled learning (PU learning) problem"</sub>
- **descriptive / method**: Two temporal directed transaction networks are built: a homogeneous Address-Address Interaction Network (AAIN) and a heterogeneous Transaction-Address Interaction Network (TAIN). (p. 2)[^original]  
  <sub>anchor: "we construct two kinds of temporal directed transaction networks including a homogeneous Address-Address Interaction Network (AAIN)"</sub>
- **descriptive / method**: The proposed framework has four modules: data collection, network construction, feature extraction, and model training and application. (p. 2)[^original]  
  <sub>anchor: "the proposed mixing detection framework mainly contains four modules"</sub>
- **descriptive / method**: In the model training and application module, the model predicts unlabeled addresses and finally outputs the detected mixing addresses. (p. 2)[^original]  
  <sub>anchor: "makes prediction for the unlabeled addresses and finally outputs the detected mixing addresses"</sub>
- **descriptive / finding or result**: The proposed model is reported to achieve a high true positive rate and a low false positive rate in mixing detection. (p. 2)[^original]  
  <sub>anchor: "The proposed model achieves a high true positive rate and a low false positive rate"</sub>

## II. DATA COLLECTION

- **descriptive / context**: WalletExplorer is a block explorer that provides label information for addresses by making transactions with services and observing how Bitcoin flows merge. (p. 2)[^original]  
  <sub>anchor: "WalletExplorer is a smart Bitcoin block explorer providing label information of addresses by making transactions with some services"</sub>
- **descriptive / limitation**: The WalletExplorer name database has not been updated since 2016, so it does not include newly emerging services. (p. 2)[^original]  
  <sub>anchor: "the name database of WalletExplorer no longer updated since 2016"</sub>
- **descriptive / data or feature**: Three snapshots of Bitcoin transaction data were extracted between November 2014 and January 2016. (p. 2)[^original]  
  <sub>anchor: "we extract three snapshots of Bitcoin transaction data between November 2014 and January 2016"</sub>
- **descriptive / data or feature**: Each snapshot contains 1,500,000 transaction records, and labeled mixing addresses were crawled from WalletExplorer. (p. 2)[^original]  
  <sub>anchor: "Each snapshot contains 1,500,000 transaction records. And we crawl"</sub>
- **descriptive / method**: Figure 3 defines a 3-node, 3-edge δ-temporal motif where the constrained time window δ is set to 15 seconds. (p. 2)[^original]  
  <sub>anchor: "the constrained time window δ is set as 15s"</sub>
- **descriptive / data or feature**: Bitcoin Fog is one of the earliest mixing services and can be accessed only via Tor; each withdrawal is split into a random number of transactions. (p. 2)[^original]  
  <sub>anchor: "each withdrawal will be split into a random number of transactions spreading out randomly over a specific time period"</sub>
- **descriptive / data or feature**: Three snapshots of Bitcoin transaction data were extracted between November 2014 and January 2016 with a six-month sampling interval, each containing 1,500,000 transaction records, labelled as the 2014, 2015 and 2016 datasets. (p. 3)[^original]  
  <sub>anchor: "Each snapshot contains 1,500,000 transaction records"</sub>
- **descriptive / data or feature**: Labelled mixing addresses were crawled from WalletExplorer and mainly belong to Bitcoin Fog, BitLaunder and Helix. (p. 3)[^original]  
  <sub>anchor: "The labeled addresses obtained from WalletExplorer are mainly belonging to three mixing services as follows"</sub>
- **descriptive / context**: Bitcoin Fog is described as one of the earliest mixing services, accessible only via Tor, splitting each withdrawal into a random number of transactions spread over a time period. (p. 3)[^original]  
  <sub>anchor: "each withdrawal will be split into a random number of transactions spreading out randomly over a specific time period"</sub>
- **descriptive / context**: BitLaunder was reported by Balthasar and Hernandez-Castro as one of the weakest mixers tested, and its detailed information is no longer available. (p. 3)[^original]  
  <sub>anchor: "it has been reported as one of the weakest mixers of all tested in the analysis conducted by Balthasar and HernandezCastro"</sub>
- **descriptive / context**: Helix, offline since 2017, offered a standard version requiring wallet registration and a light version letting Bitcoins be withdrawn to up to five addresses. (p. 3)[^original]  
  <sub>anchor: "While for the light version, the Bitcoins could be withdrawn to up to five addresses"</sub>
- **descriptive / data or feature**: Table I reports, for the 2014, 2015 and 2016 datasets, the start time, unlabelled address counts and labelled address counts for BitcoinFog, BitLaunder and HelixMixer; for example 2014 has 2,507,872 unlabelled addresses and 6,088 Bitcoin Fog addresses. (p. 3)[^original]  
  <sub>anchor: "Table I shows the statistics of these three datasets"</sub>
- **descriptive / finding or result**: Labelled addresses account on average for about 0.19% of all addresses in the transaction data. (p. 3)[^original]  
  <sub>anchor: "the labeled addresses only account for about 0.19% of all addresses appearing in the transaction data"</sub>

## III. NETWORK CONSTRUCTION AND MOTIF DEFINITION

- **descriptive / method**: Bitcoin transaction records are abstracted as a complex network where nodes are addresses and edges are transactions between addresses; the AAIN models address interactions. (p. 3)[^original]  
  <sub>anchor: "each node refers to a Bitcoin address and each edge represents a transaction process between"</sub>
- **descriptive / context**: The TAIN is a heterogeneous network representing transaction amounts, in which nodes can be either a transaction or an address, so it shows more clearly how much an address sent or received. (p. 3)[^original]  
  <sub>anchor: "From TAIN, we can clearly find how much an address has sent to or received from a transaction"</sub>

## III. A. AAIN and Temporal Motifs

- **descriptive / definition**: Definition 1: an AAIN is a temporal directed multigraph whose edges are tuples (u, v, tx, t) recording source address, destination address, transaction and time. (p. 3)[^original]  
  <sub>anchor: "each edge e ∈ E standing for a transaction is defined as a tuple (u, v, tx, t)"</sub>

## II. DATA COLLECTION

- **descriptive / data or feature**: BitLaunder claimed to be the best Bitcoin laundering service, but was reported as one of the weakest mixers tested in an analysis by Balthasar and Hernandez-Castro; its details are no longer available. (p. 3)[^original]  
  <sub>anchor: "it has been reported as one of the weakest mixers of all tested"</sub>
- **descriptive / data or feature**: Helix, offline since 2017, offered a standard version and a light version. (p. 3)[^original]  
  <sub>anchor: "Helix (has been offline since 20173 ) offered two version of mixing services"</sub>
- **descriptive / data or feature**: In the Helix standard version, users registered a wallet and the Bitcoins sent to it were automatically mixed and then sent to a defined address. (p. 3)[^original]  
  <sub>anchor: "the Bitcoins sent to the wallet would be automatically mixed and finally sent to a defined address"</sub>
- **descriptive / data or feature**: In the Helix light version, Bitcoins could be withdrawn to up to five addresses. (p. 3)[^original]  
  <sub>anchor: "While for the light version, the Bitcoins could be withdrawn to up to five addresses."</sub>
- **descriptive / finding or result**: Labeled addresses account on average for about 0.19% of all addresses appearing in the transaction data. (p. 3)[^original]  
  <sub>anchor: "On the average, the labeled addresses only account for about 0.19% of all addresses appearing in the transaction data"</sub>
- **descriptive / data or feature**: Table I reports for the 2014, 2015 and 2016 datasets the counts of unlabeled addresses and of labeled addresses for Bitcoin Fog, BitLaunder and Helix Mixer, with about 2.5 million unlabeled addresses per dataset. (p. 3)[^original]  
  <sub>anchor: "Table I shows the statistics of these three datasets."</sub>
- **descriptive / data or feature**: Labeled addresses for Bitcoin Fog, BitLaunder and Helix Mixer were crawled from WalletExplorer and used as the labeled addresses. (p. 3)[^original]  
  <sub>anchor: "Addresses of three mixing services including Bitcoin Fog, BitLaunder and Helix Mixer crawled from WalletExplorer are as our labeled addresses."</sub>

## III. A. AAIN and Temporal Motifs

- **descriptive / definition**: Temporal motifs are recurring interconnection patterns occurring in temporal networks. (p. 3)[^original]  
  <sub>anchor: "Temporal motifs are defined as recurring interconnection patterns occurring in temporal networks"</sub>

## III. B. TAIN and ATH Motifs

- **descriptive / method**: In the Figure 4 example, the first bit of the edge vector is 0 if the amount of tx1 is higher than tx2, and 1 otherwise. (p. 3)[^original]  
  <sub>anchor: "the first bit of ΓV is set as 0 if the amount of tx1 is higher than tx2"</sub>

## III. A. AAIN and Temporal Motifs

- **descriptive / definition**: Definition 2: a k-node, l-edge, δ-temporal motif instance has its l edges occurring in non-decreasing time order within a time window δ, i.e. the last edge time minus the first is at most δ. (p. 4)[^original]  
  <sub>anchor: "satisfies t1 ⩽ t2 ⩽ ... ⩽ tl and tl − t1 ⩽ δ"</sub>
- **descriptive / context**: Temporal motifs preserve the time-ordered sequence of contacts within a time window, unlike static network motifs. (p. 4)[^original]  
  <sub>anchor: "Different from static network motifs, temporal motifs well preserve the time-ordered sequence of contacts"</sub>
- **descriptive / definition**: Figure 3 illustrates a 3-node, 3-edge δ-temporal motif with instances, where patterns that violate edge order or the time window do not count as instances. (p. 4)[^original]  
  <sub>anchor: "their edge order or occurring time window does not satisfy the condition"</sub>

## III. B. TAIN and ATH Motifs

- **descriptive / definition**: Definition 3: a TAIN is an attributed temporal heterogeneous network with node types address and transaction, edge types transaction-address and address-transaction, and attributes for transaction amount and time. (p. 4)[^original]  
  <sub>anchor: "A transaction-address edge (u, txin, a, t1) denotes that an input transaction txin happens at time t1"</sub>
- **descriptive / definition**: Definition 4: ATH motifs are local recurring subgraphs of attributed temporal heterogeneous networks, requiring more than one node type or more than one edge type, with an edge attribute vector and a time window constraint. (p. 4)[^original]  
  <sub>anchor: "also satisfying node types |{ϕV (v)|v ∈ VAT H }| > 1 or edge types |{ϕE(e)|e ∈ EAT H }| > 1"</sub>

## IV. FEATURE-BASED ANALYSIS

- **descriptive / context**: Addresses associated with mixing services are expected to have features different from normal addresses due to the mixing function; features are extracted at three levels. (p. 4)[^original]  
  <sub>anchor: "addresses associated with mixing services may have several unique features different from normal addresses"</sub>

## IV. A. Network Features

- **descriptive / definition**: Network motifs are small subgraph patterns occurring with significantly higher frequency than in randomised networks; significance is measured by a z-score comparing real and random-network frequencies. (p. 4)[^original]  
  <sub>anchor: "Network motifs are small subgraph patterns in a network that occurring with significantly higher frequency than those in randomized networks"</sub>
- **descriptive / requirement**: A pattern is usually regarded as a statistically significant motif if its z-score exceeds 2.0, citing reference [14]. (p. 4)[^original]  
  <sub>anchor: "A pattern is usually regarded as a statistically significant motif if its z-score > 2.0 [14]"</sub>
- **descriptive / method**: Six simplest two-edge transaction patterns in AAIN are considered, describing how an address interacts with other addresses within a δ duration; a1 is receive-then-send and a2 the opposite order. (p. 4)[^original]  
  <sub>anchor: "pattern a1 represents that an address first receives money from a neighbor and then transfers money to another neighbor"</sub>
- **descriptive / method**: In TAIN, transactions of an address within a δ window are abstracted as all-in, all-out, and in-and-out structures; the in-and-out structure is further divided into four patterns, giving six candidate ATH patterns. (p. 4)[^original]  
  <sub>anchor: "the in and out structure can be further divided into four patterns, and all these six patterns"</sub>

## III. B. TAIN and ATH Motifs

- **descriptive / definition**: A transaction-address edge denotes that an input transaction happens at a given time and transfers a number of Bitcoins into an address. (p. 4)[^original]  
  <sub>anchor: "A transaction-address edge (u, txin, a, t1) denotes that an input transaction txin happens at time t1"</sub>
- **descriptive / case example**: Figure 4(c) shows an ATH motif instance where money is received first and less is sent out later. (p. 4)[^original]  
  <sub>anchor: "the instance in Fig. 4(c) represents the transaction pattern of receiving money first and sending out less money later"</sub>
- **descriptive / case example**: Figure 4(d) shows an ATH motif instance where money is sent out first and less is received later, giving a negative balance. (p. 4)[^original]  
  <sub>anchor: "the instance in Fig. 4(d) stands for sending money out firstly and receiving less money later"</sub>

## IV. A. Network Features

- **descriptive / method**: A network motif is a small subgraph pattern occurring with significantly higher frequency than in randomized networks, measured by a z-score. (p. 4)[^original]  
  <sub>anchor: "Network motifs are small subgraph patterns in a network that occurring with significantly higher frequency than those in randomized networks"</sub>
- **descriptive / method**: Six two-edge transaction patterns in AAIN are considered, and in TAIN three topological structures are abstracted: all in, all out, and in and out. (p. 4)[^original]  
  <sub>anchor: "We consider six simplest transaction patterns (Fig. 5(a)) with two edges in AAIN"</sub>
- **descriptive / data or feature**: Table II reports the average fraction of δ-temporal motifs a1 to a6 for labeled and unlabeled addresses with δ = 3 hours. (p. 4)[^original]  
  <sub>anchor: "TABLE II AVERAGE FRACTION OF δ-TEMPORAL MOTIFS (δ = 3 HOURS)."</sub>
- **descriptive / data or feature**: Table III reports the average fraction of δ-ATH motifs b2, b4, b5 and b6 for labeled and unlabeled addresses with δ = 3 hours. (p. 4)[^original]  
  <sub>anchor: "TABLE III AVERAGE FRACTION OF δ-ATH MOTIFS (δ = 3 HOURS)."</sub>
- **descriptive / method**: Z-scores are computed using 100 random networks per real network, generated by the configuration model preserving degree sequence, with attribute information rearranged. (p. 5)[^original]  
  <sub>anchor: "these random networks are generalized by the configuration model [15] with a rearrangement of the attribute information"</sub>
- **descriptive / finding or result**: Temporal motifs a1-a6 and ATH motifs b2 and b4-b6 are reported as statistically significant motifs in the Bitcoin transaction network, and are used as hybrid motif features. (p. 5)[^original]  
  <sub>anchor: "Pattern a1-a6 and pattern b2, b4b6 are statistically significant motifs in the Bitcoin transaction network"</sub>
- **descriptive / data or feature**: Feature NF1-NF6 is the occurrence frequency proportion of each temporal motif among all considered temporal motifs in the first-order AAIN for each address. (p. 5)[^original]  
  <sub>anchor: "The occurring frequency proportion of each temporal motif in all considered temporal motifs in the firstorder AAIN for each address"</sub>
- **descriptive / data or feature**: Features NF7-NF10 give the frequency proportion of an address being part of each ATH motif among all considered ATH motifs; NF11 and NF12 are in-degree and out-degree in AAIN. (p. 5)[^original]  
  <sub>anchor: "The frequency proportion of an address being a part of each ATH motif in all considered ATH motifs"</sub>
- **descriptive / data or feature**: Features NF13-NF17 are degree-based ratios and counts in AAIN: in-to-out degree ratio, unique successor and predecessor counts, and in-degree to unique successor ratio and out-degree to unique predecessor ratio. (p. 5)[^original]  
  <sub>anchor: "NF17: Ratio of the out-degree to the number of unique predecessor addresses in AAIN"</sub>
- **descriptive / finding or result**: Finding 1: the a1 pattern fraction is much higher than a2, and b4 far exceeds b5 and b6; this difference is more significant for labelled addresses, so mixing services favour receiving money first and sending later with balance not less than 0. (p. 5)[^original]  
  <sub>anchor: "mixing services are more in line with the transaction pattern of receiving money firstly and sending money out latter"</sub>
- **descriptive / finding or result**: Finding 2: a5 and a6 results suggest non-mixing entities may reuse addresses in a short time, a situation seldom seen for mixing services; NF16 and NF17 indicate the same. (p. 5)[^original]  
  <sub>anchor: "non-mixing service entity may reuse some addresses in a short time while this situation seldom happens for mixing services"</sub>
- **descriptive / finding or result**: Finding 3: the a3 pattern arises from change addresses; mixing services prefer dispersing tainted Bitcoins to others, a common mixing strategy, with NF11-NF13 supporting this. (p. 5)[^original]  
  <sub>anchor: "mixing services prefer dispersing the tainted Bitcoins to others, which is a usually adopted strategy for Bitcoin mixing"</sub>
- **descriptive / context**: Some analytic companies apply taint analysis to predict risk scores for addresses and blacklist high-risk tainted coin holders to avoid buying tainted coins. (p. 5)[^original]  
  <sub>anchor: "which can predict a risk score for addresses and blacklist the high-risk tainted coin possessors"</sub>

## IV. B. Account Features

- **descriptive / data or feature**: Account features describe the state and activeness of an address; exchanges usually have higher trade frequency than ordinary users. (p. 5)[^original]  
  <sub>anchor: "addresses belonging to Bitcoin exchanges usually have a higher trade frequency for a great many of businesses"</sub>
- **descriptive / data or feature**: Account features AF1 and AF2 are the number of input and output transactions in the snapshot; AF3 is their ratio. (p. 5)[^original]  
  <sub>anchor: "AF3: Number ratio of the input transactions to the output transactions"</sub>
- **descriptive / data or feature**: Account features AF4 and AF5 are total input and output amounts in the snapshot, and AF6 is the amount ratio of total input to total output. (p. 5)[^original]  
  <sub>anchor: "AF4: Total amount of input transactions in the snapshot"</sub>
- **descriptive / data or feature**: Table II gives average fractions of temporal motifs a1-a6 for labelled and unlabelled addresses with a 3-hour window, e.g. a1 0.2552 for labelled versus 0.2320 for unlabelled. (p. 5)[^original]  
  <sub>anchor: "Labeled address|0.2552|0.0051|0.5902|0.1465|0.0000|0.0030"</sub>

## IV. A. Network Features

- **descriptive / data or feature**: Table III gives average fractions of ATH motifs b2, b4, b5, b6 for labelled and unlabelled addresses with a 3-hour window, e.g. b2 0.4957 for labelled versus 0.6557 for unlabelled. (p. 5)[^original]  
  <sub>anchor: "Labeled address|0.4957|0.4916|0.0057|0.0069"</sub>
- **descriptive / method**: The ATH mapped vector for all-out patterns is given as [1, 1]. (p. 5)[^original]  
  <sub>anchor: "Contrarily, ΓΩ of all out patterns are given as [1, 1]."</sub>
- **descriptive / method**: The z-score of candidate patterns is calculated against 100 random networks for each real network. (p. 5)[^original]  
  <sub>anchor: "The z-score value of these patterns (Fig. 5) are calculated with 100 random networks for each real network"</sub>
- **descriptive / method**: Random networks preserve the degree sequence and attribute distribution of the real network via the configuration model with attribute rearrangement. (p. 5)[^original]  
  <sub>anchor: "these random networks are generalized by the configuration model [15] with a rearrangement of the attribute information"</sub>
- **descriptive / finding or result**: Temporal motifs a1-a6 and ATH motifs b2 and b4-b6 are reported as statistically significant motifs in the Bitcoin transaction network. (p. 5)[^original]  
  <sub>anchor: "We then make use of these hybrid motifs, including temporal motifs a1-a6 and ATH motifs b2, b4-b6"</sub>
- **descriptive / data or feature**: Features NF1-NF6 are the occurrence frequency proportion of each temporal motif among all considered temporal motifs in the first-order AAIN for each address. (p. 5)[^original]  
  <sub>anchor: "NF1-NF6: The occurring frequency proportion of each temporal motif in all considered temporal motifs in the firstorder AAIN for each address."</sub>
- **descriptive / data or feature**: Features NF7-NF10 are the frequency proportion of an address being part of each ATH motif among all considered ATH motifs. (p. 5)[^original]  
  <sub>anchor: "The frequency proportion of an address being a part of each ATH motif in all considered ATH motifs"</sub>
- **descriptive / data or feature**: Features NF11 and NF12 are the in-degree and out-degree values in AAIN, and NF13 is the ratio of in-degree to out-degree. (p. 5)[^original]  
  <sub>anchor: "NF11: Value of in-degree in AAIN. NF12: Value of out-degree in AAIN."</sub>
- **descriptive / finding or result**: Finding 1: mixing services follow the pattern of receiving money first and sending it out later with a balance not less than 0, more markedly for labeled addresses. (p. 5)[^original]  
  <sub>anchor: "In other words, mixing services are more in line with the transaction pattern of receiving money firstly"</sub>
- **descriptive / finding or result**: Finding 2: non-mixing entities may reuse addresses in a short time, a situation that seldom happens for mixing services. (p. 5)[^original]  
  <sub>anchor: "non-mixing service entity may reuse some addresses in a short time"</sub>
- **descriptive / finding or result**: Finding 3: mixing services prefer dispersing tainted Bitcoins to others, a commonly adopted strategy for Bitcoin mixing. (p. 5)[^original]  
  <sub>anchor: "mixing services prefer dispersing the tainted Bitcoins to others, which is a usually adopted strategy for Bitcoin mixing"</sub>
- **descriptive / finding or result**: The prevalence of the a3 pattern is attributed to change addresses generated to receive change. (p. 5)[^original]  
  <sub>anchor: "The prevalence of a3 pattern is due to the change addresses generated to receive the change"</sub>
- **descriptive / context**: Taint analysis companies predict risk scores for addresses and blacklist high-risk tainted coin possessors to avoid buying tainted coins. (p. 5)[^original]  
  <sub>anchor: "which can predict a risk score for addresses and blacklist the high-risk tainted coin possessors"</sub>

## IV. B. Account Features

- **descriptive / context**: Addresses belonging to Bitcoin exchanges usually have a higher trade frequency than ordinary users, which account features are meant to capture. (p. 5)[^original]  
  <sub>anchor: "addresses belonging to Bitcoin exchanges usually have a higher trade frequency for a great many of businesses"</sub>
- **descriptive / data or feature**: AF1 is the number of input transactions in the snapshot. (p. 5)[^original]  
  <sub>anchor: "AF1: Number of input transactions in the snapshot."</sub>
- **descriptive / data or feature**: AF2 is the number of output transactions in the snapshot, AF3 the ratio of input to output transaction numbers, and AF4 to AF6 are the corresponding amount totals and ratio. (p. 5)[^original]  
  <sub>anchor: "AF2: Number of output transactions in the snapshot."</sub>
- **descriptive / finding or result**: Table IV reports statistics of the account features AF1-AF6 and the features NF11-NF17. (p. 5)[^original]  
  <sub>anchor: "STATISTICS OF FEATURES (EXCEPT MOTIF FEATURES)."</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Jiajing Wu, Jieli Liu, Weili Chen, Huawei Huang, Zibin Zheng, Yan Zhang, "Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs" (2021-01-21). https://arxiv.org/abs/2001.05233
