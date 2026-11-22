---
type: Source Digest
title: Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs - part 3 of 3 (pp. 9-12)
description: 'Verified paraphrased digest, pp. 9-12: Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > D. Parameter Sensitivity Analysis; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > E. Discussion; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > VII. RELATED WORK; and 1 more sections'
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
part: 3
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
digest_points: 34
---

# Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 9-12) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## D. Parameter Sensitivity Analysis

- **descriptive / finding or result**: The metrics of the model are generally stable across different settings of parameter δ in the testing domain, indicating the model steadily obtains relatively good results. (p. 9)[^original]  
  <sub>anchor: "the curves of the metrics are generally stable, which illustrates that our model can steadily obtain"</sub>
- **descriptive / finding or result**: Table VII reports TPR and FPR of the model under different voting probability thresholds ε; a lower ε gives a higher TPR, while FPR becomes lower with a larger ε. (p. 9)[^original]  
  <sub>anchor: "We can observe that the lower ε is, the higher TPR is."</sub>
- **permissive / recommendation**: In practical applications, an appropriate voting threshold can be chosen according to whether the user prioritises a higher TPR or a lower FPR. (p. 9)[^original]  
  <sub>anchor: "we can choose an appropriate threshold according to our specific requirement of pursuing a higher TPR"</sub>

## E. Discussion

- **descriptive / context**: The SegWit soft-fork accepted in August 2017 addresses transaction malleability by redesigning the transaction structure and segregating witness data, so witness modifications do not change the transaction hash. (p. 10)[^original]  
  <sub>anchor: "The SegWit soft-fork accepted in August, 2017 is a solution for the transaction malleability problem"</sub>
- **descriptive / context**: SegWit can reduce transaction size and increase the number of transactions contained in a block. (p. 10)[^original]  
  <sub>anchor: "the use of SegWit can reduce the size of a transaction and increase the number of transactions contained in a block"</sub>
- **descriptive / context**: The Lightning Network is an off-chain scalability solution in which two users open a channel by locking Bitcoins in a 2-of-2 multi-signature address via an on-chain transaction, transact off-chain, and close the channel by broadcasting a commitment transaction. (p. 10)[^original]  
  <sub>anchor: "LN is an offchain solution to improve the scalability of Bitcoin. For two Bitcoin users, they can open"</sub>
- **descriptive / limitation**: WalletExplorer does not include new services emerging after 2016, so experiments used three snapshots from 2014-2016. (p. 10)[^original]  
  <sub>anchor: "Since WalletExplorer does not include the new emerging services after 2016, we have conducted experiments with three snapshots"</sub>
- **descriptive / data or feature**: A 2020 dataset was built from 1,500,000 consecutive Bitcoin transactions since Mar. 25, 2020, containing 89 labelled Bitcoin Fog addresses and 1,654,175 unlabelled addresses after filtering. (p. 10)[^original]  
  <sub>anchor: "we collect 1,500,000 consecutive transactions on Bitcoin since Mar. 25, 2020"</sub>
- **descriptive / finding or result**: On the 2020 dataset the model still performs best in terms of G-mean, but its TPR and FPR are slightly worse than the best method. (p. 10)[^original]  
  <sub>anchor: "our model still performs best in terms of G-mean. Yet its performance in terms TPR and FPR is slightly worse"</sub>
- **descriptive / limitation**: Possible reasons for weaker TPR/FPR on the 2020 dataset are the small number of labels and the introduction of new techniques such as LN. (p. 10)[^original]  
  <sub>anchor: "One is the small amount of labels in the 2020 dataset, the other one is the introduction of some new techniques like LN."</sub>
- **permissive / recommendation**: The most direct way to improve detection on current transactions is to collect more labels from mixing services and analyse them to better capture their features; link prediction to enrich links of native SegWit addresses is another feasible option for identifying ownership. (p. 10)[^original]  
  <sub>anchor: "the most direct method is to collect more labels via using some mixing services"</sub>

## VII. RELATED WORK

- **descriptive / context**: Prior blockchain research has mined transaction network properties, clustered addresses by ownership, and discovered scams, attacks and dark market trading. (p. 10)[^original]  
  <sub>anchor: "to mine some network properties for transaction networks [24]–[26], to cluster addresses sharing the same ownership"</sub>
- **descriptive / finding or result**: Chen et al. performed graph analysis and abnormal contract detection on Ethereum using money flow, smart contract creation and invocation graphs. (p. 10)[^original]  
  <sub>anchor: "Chen et al. conducted a graph analysis and abnormal contract detection on Ethereum"</sub>
- **descriptive / finding or result**: Tam et al. proposed a GCN-based embedding method to identify illicit accounts in e-payment networks including Ethereum. (p. 10)[^original]  
  <sub>anchor: "Tam et al. proposed a Graph Convolution Network (GCN)-based embedding method to identify illicit accounts"</sub>
- **descriptive / finding or result**: Abnormal transaction patterns for Bitcoin market manipulation were mined using singular value decomposition metrics on base networks. (p. 10)[^original]  
  <sub>anchor: "typical abnormal transaction patterns for Bitcoin market manipulation were mined by inspecting the base networks"</sub>
- **descriptive / finding or result**: Möser et al. examined the operation models of three mixing services and attempted to trace anonymous transactions. (p. 10)[^original]  
  <sub>anchor: "provided an inquiry into the operation models of three mixing services"</sub>
- **descriptive / finding or result**: Weber et al. stressed the importance of AML regulation and contributed the Elliptic dataset for illicit activity detection in Bitcoin. (p. 10)[^original]  
  <sub>anchor: "contributed the Elliptic dataset for illicit activity detection in Bitcoin"</sub>
- **descriptive / finding or result**: Ranshous et al. introduced motifs in directed hypergraphs and recognised specific laundering patterns for Bitcoin exchanges. (p. 10)[^original]  
  <sub>anchor: "introduced the idea of motifs in directed hypergraphs"</sub>
- **descriptive / context**: Bitconeview is a visualisation tool that shows how and when an address mixes its money. (p. 10)[^original]  
  <sub>anchor: "was proposed to visualize how and when an address mixes its money"</sub>
- **descriptive / case example**: The cryptocurrency exchange ShapeShift was reported to be involved in money laundering by moving Bitcoins to privacy-enhancing cryptocurrencies such as Zcash and Monero. (p. 10)[^original]  
  <sub>anchor: "a cryptocurrency exchange platform called ShapeShift4 was reported to be involved in money laundering"</sub>
- **descriptive / limitation**: Prior tools do not focus on identifying addresses enrolled in mixing; a community outlier detection approach to Bitcoin mixing detection lacks generalisation across mixing services and uses only topology information. (p. 10)[^original]  
  <sub>anchor: "this work is in lack of generalization for different mixing services and it only utilizes the topology information"</sub>
- **descriptive / method**: The paper proposes multi-level features to discover transaction patterns of mixing services, inspired by a Ponzi scheme detection study on Ethereum, to enhance generalisation. (p. 10)[^original]  
  <sub>anchor: "we propose features from multi-level, trying to discover the transaction patterns of mixing services"</sub>
- **descriptive / context**: Network motifs are defined as recurrent subgraph patterns of complex networks and play an important role in characterising mixing service behaviour. (p. 10)[^original]  
  <sub>anchor: "the network motifs we used, which are defined as the recurrent subgraph patterns of complex networks"</sub>

## E. Discussion

- **descriptive / context**: Unlike traditional Bitcoin transactions, Lightning Network usage results in only two transaction records per channel, one for opening and one for closing. (p. 10)[^original]  
  <sub>anchor: "the use of LN only results in two transaction records each time for the opening and closing of a channel"</sub>
- **descriptive / context**: Almost all Lightning Network transactions are based on 2-of-2 multi-signature addresses in witness scripts after SegWit activation, and these are native SegWit addresses starting with "bc". (p. 10)[^original]  
  <sub>anchor: "almost all the LN transactions are based on 2-of-2 multi-signature addresses in witness scripts after the activation of SegWit"</sub>

## VII. RELATED WORK

- **descriptive / context**: Temporal motifs combined with time information have been proposed for dynamic homogeneous networks and extended to heterogeneous information networks. (p. 11)[^original]  
  <sub>anchor: "network motifs combined with temporal information were proposed to characterize dynamic homogeneous network"</sub>
- **descriptive / limitation**: Most network mining studies fail to consider rich network attribute information when characterising interaction patterns with motifs. (p. 11)[^original]  
  <sub>anchor: "most of these network mining studies fail to consider the rich information of network attributes"</sub>

## VIII. CONCLUSION AND FUTURE WORK

- **descriptive / method**: The study builds two temporal directed graphs from Bitcoin records: a homogeneous Address-Address Interaction Network (AAIN) and a heterogeneous Transaction-Address Interaction Network (TAIN). (p. 11)[^original]  
  <sub>anchor: "we employed the Bitcoin transaction records to build two temporal directed graphs"</sub>
- **descriptive / method**: The authors propose ATH motifs for TAIN to integrate edge attribute information with higher-order structures, and use temporal motifs in AAIN and ATH motifs in TAIN as hybrid key features. (p. 11)[^original]  
  <sub>anchor: "For TAIN, we proposed a novel concept of ATH motifs to integrate edge attribute information"</sub>
- **descriptive / method**: A PU learning based detection model is built on the designed features to handle extreme label imbalance in mixing detection. (p. 11)[^original]  
  <sub>anchor: "we built a PU learning based detection model to handle the issue of extremely label imbalance"</sub>
- **descriptive / finding or result**: Extensive experiments on three real Bitcoin datasets demonstrated the effectiveness of the detection model. (p. 11)[^original]  
  <sub>anchor: "Extensive experimental results on three real Bitcoin datasets demonstrated the effectiveness of our detection model."</sub>
- **descriptive / limitation**: Mixing providers may update mechanisms to remove the typical behaviours, for example by injecting extra Bitcoins that sit in addresses or by randomising arrival-departure intervals to avoid the motifs. (p. 11)[^original]  
  <sub>anchor: "the mixing service providers may update their mechanisms to eliminate these typical behaviors"</sub>
- **descriptive / limitation**: Because the data is mostly unlabelled and the model relies on prior information, unknown complex mixing strategies may exist and may go undetected. (p. 11)[^original]  
  <sub>anchor: "Since the available data is intrinsically mostly unlabeled and our detection model is based on the prior information"</sub>
- **descriptive / recommendation**: Future work will seek more adaptive strategies against updated privacy-enhancing techniques, such as applying link prediction to enrich money flow information. (p. 11)[^original]  
  <sub>anchor: "we will look for more adaptive strategies to defense these updated privacy-enhancing techniques"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: Jiajing Wu, Jieli Liu, Weili Chen, Huawei Huang, Zibin Zheng, Yan Zhang, "Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs" (2021-01-21). https://arxiv.org/abs/2001.05233
