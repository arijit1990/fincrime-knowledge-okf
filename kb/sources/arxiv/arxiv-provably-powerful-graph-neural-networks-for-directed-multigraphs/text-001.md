---
type: Source Text
title: Provably Powerful Graph Neural Networks for Directed Multigraphs - part 1 of 5 (pp. 1-5)
description: 'Verbatim extracted text, pp. 1-5: Provably Powerful Graph Neural Networks for Directed Multigraphs > Béni Egressy1* , Luc von Niederhäusern1 , Jovan Blanuša2 , Erik Altman3 , Roger Wattenhofer1 , Kubilay Atasu2; Provably Powerful Graph Neural Networks for Directed Multigraphs > 1 Introduction; Provably Powerful Graph Neural Networks for Directed Multigraphs > 2 Related Work; and 3 more sections'
resource: https://arxiv.org/abs/2306.11586
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-provably-powerful-graph-neural-networks-for-directed-multigraphs
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-06-20'
legal_status: unknown
part: 1
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T14:32:20Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T14:32:20Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.11586
  title: Provably Powerful Graph Neural Networks for Directed Multigraphs
  author: org:arxiv
  last_modified: '2023-06-20T00:00:00Z'
---

# Provably Powerful Graph Neural Networks for Directed Multigraphs

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2023-06-20), part 1 of 5, pp. 1-5. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Provably Powerful Graph Neural Networks for Directed Multigraphs


### Béni Egressy1* , Luc von Niederhäusern1 , Jovan Blanuša2 , Erik Altman3 , Roger Wattenhofer1 , Kubilay Atasu2


[p. 1]

1ETH Zurich, Zurich, Switzerland

2IBM Research Europe, Zurich, Switzerland

3IBM Watson Research, Yorktown Heights, NY, USA

begressy@ethz.ch, lucv@ethz.ch, jov@zurich.ibm.com, ealtman@us.ibm.com, wattenhofer@ethz.ch, kat@zurich.ibm.com

This paper analyses a set of simple adaptations that transform standard message-passing Graph Neural Networks (GNN) into provably powerful directed multigraph neural networks. The adaptations include multigraph port numbering, ego IDs, and reverse message passing. We prove that the combination of these theoretically enables the detection of any directed subgraph pattern. To validate the effectiveness of our proposed adaptations in practice, we conduct experiments on synthetic subgraph detection tasks, which demonstrate outstanding performance with almost perfect results.

#### Abstract


Moreover, we apply our proposed adaptations to two financial crime analysis tasks. We observe dramatic improvements in detecting money laundering transactions, improving the minority-class F1 score of a standard message-passing GNN by up to 30%, and closely matching or outperforming treebased and GNN baselines. Similarly impressive results are observed on a real-world phishing detection dataset, boosting three standard GNNs’ F1 scores by around 15% and outperforming all baselines. To appear as a conference paper at AAAI 2024.

Graph neural networks (GNNs) have become the go-to machine learning models for learning from relational data. GNNs are used in various fields, ranging from biology, physics, and chemistry to social networks, traffic, and weather forecasting (Bongini, Bianchini, and Scarselli 2021; Zhou et al. 2020; Derrow-Pinion et al. 2021; Shu, Wang, and Liu 2019; Wu et al. 2020; Keisler 2022; Zhang et al. 2019; Battaglia et al. 2016). More recently, there has been growing interest in using GNNs to identify financial crime (Cardoso, Saleiro, and Bizarro 2022; Kanezashi et al. 2022; Weber et al. 2019, 2018; Nicholls, Kuppa, and Le-Khac 2021).

### 1 Introduction


Our motivating task is to detect financial crimes manifesting as subgraph patterns in transaction networks. For example, see Fig. 1, which depicts established money laundering patterns, or see Fig. 4 in the appendix for an illustrative scenario. But note that similar patterns are relevant for graph tasks in many areas, ranging from chemistry to traffic forecasting. The task seems to lend itself nicely to the use of

> *This work was performed while Béni Egressy and Luc von Niederhäusern were at IBM Research Europe, Zurich, Switzerland. Copyright © 2024, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

GNNs. Unfortunately, current GNNs are ill-equipped to deal with financial transaction networks effectively.

Firstly, financial transaction networks are, in fact, directed multigraphs, i.e., edges (or transactions) have a direction, and there can be multiple edges between two nodes (or accounts). Secondly, most GNNs cannot detect some subgraph patterns, such as cycles (Chen et al. 2020, 2019b). There have been many efforts to overcome this limitation (You et al. 2021; Huang et al. 2022; Papp and Wattenhofer 2022; Zhang and Li 2021; Loukas 2019; Sato, Yamada, and Kashima 2019), all focusing on simple (undirected) graphs. But even on simple graphs, the problem is far from solved. Until very recently, for example, there was no linear-time permutation-equivariant GNN that could count 6-cycles with theoretical guarantees (Huang et al. 2022).

This paper addresses both of these issues. To our knowledge, this is the first GNN architecture designed specifically for directed multigraphs. Secondly, we first prove that the proposed architecture can theoretically detect any subgraph pattern in directed multigraphs and then empirically confirm that our proposed architecture can detect the patterns illustrated in Fig. 1. Our proposed architecture is based on a set of simple adaptations that can transform any standard GNN architecture into a directed multigraph GNN. The adaptations are reverse message passing (Jaume et al. 2019), port numbering (Sato, Yamada, and Kashima 2019), and ego IDs (You et al. 2021). Although these individual building blocks are present in existing literature, the theoretical and empirical power of combining them has not been explored. In this work, we fill this gap: We combine them, adapt them to directed multigraphs, and showcase the theoretical and empirical advantages of using them in unison.

[pp. 1-2]

Our contributions. (1) We propose a set of simple and intuitive adaptations that can transform message-passing GNNs into provably powerful directed multigraph neural networks. (2) We prove that suitably powerful GNNs equipped with ego IDs, port numbering, and reverse message passing can identify any directed subgraph pattern. (3) The theory is tested on synthetic graphs, confirming that GNNs using these adaptations can detect a variety of subgraph patterns, including directed cycles up to length six, scatter-gather patterns, and directed bicliques, setting them apart from previous GNN architectures. (4) The improvements translate to significant gains on two financial datasets. The adaptations boost GNN

(a) Degree-in = 4 (b) Degree-out = 4 (c) Directed Biclique (d) Scatter-Gather(e) Fan-in = 3 (f) Fan-out = 2 (g) Directed Cycle (5) (h) Gather-Scatter

Figure 1: Money Laundering Patterns. The gray fill indicates the nodes to be detected by the synthetic pattern detection tasks. The exact degree/fan pattern sizes here are for illustrative purposes only.

performance dramatically on money laundering and phishing datasets, matching or surpassing state-of-the-art financial crime detection models on both simulated and real data.

### 2 Related Work


[p. 2]

Xu et al. (2018) showed that standard MPNNs are at most as powerful as the Weisfeiler-Lehman (WL) isomorphism test, and provided a GNN architecture, GIN, that theoretically matches the power of the WL test. Although the WL test can asymptotically almost surely differentiate any two non-isomorphic graphs (Babai, Erdos, and Selkow 1980), standard MPNNs cannot — in certain graphs — detect simple substructures like cycles (Chen et al. 2020, 2019b). This motivated researchers to go beyond standard MPNNs.

One direction considers emulating the more powerful k- WL isomorphism test, by conducting message passing between k-tuples or using a tensor-based model (Maron et al. 2019; Morris et al. 2019). Unfortunately, these models have high complexity and are impractical for most applications. Another line of work uses pre-calculated features to augment the GNN. These works explore adding subgraph counts (Bouritsas et al. 2022; Barceló et al. 2021), positional node embeddings (Egressy and Wattenhofer 2022; Dwivedi et al. 2021), random IDs (Abboud et al. 2020; Sato, Yamada, and Kashima 2021), and node IDs (Loukas 2019).

A recent class of expressive GNNs called Subgraph GNNs, model graphs as collections of subgraphs (Frasca et al. 2022; Zhao et al. 2021). Papp et al. (2021) drop random nodes from the input and run the GNN multiple times, gathering more information with each run. Zhang and Li (2021) instead extract subgraphs around each node and run the GNN on these. Also falling into this category is ID-GNN, which uses ego IDs (You et al. 2021), whereby each node is sampled with its neighborhood and given an identifier to differentiate it from the neighbors. Although the authors claim that IDGNNs can count cycles, the proof turns out to be incorrect. In fact, Huang et al. (2022) show that the whole family of Subgraph GNNs cannot count cycles of length greater than 4, and propose I2 -GNNs that can count cycles up to length 6.

There has been much less work on GNNs for directed graphs. Zhang et al. (2021) propose a spectral network for

directed graphs, but it is difficult to analyze the power of this network or apply it to larger datasets. Similar approaches can be found in (Tong et al. 2020) and (Ma et al. 2019). Jaume et al. (2019) extend message passing to aggregate incoming and outgoing neighbors separately, rather than naively treating the graph as undirected. Directed multigraphs have not specifically been considered.

GNNs have been used for various financial applications (Li et al. 2021; Feng et al. 2019; Chen, Wei, and Huang 2018; Zhang et al. 2019; Li et al. 2019; Xu et al. 2021; Yang et al. 2021). Closest to our work, GNNs have been used for fraud detection. Liang et al. (2019) and Rao et al. (2021) work on bipartite customer-product graphs to uncover insurance and credit card fraud, respectively. Liu et al. (2018) use heterogeneous GNNs to detect malicious accounts in the device-activity bipartite graph of an online payment platform. Weber et al. (2019) were the first to apply standard GNNs for anti-money laundering (AML), and more recently Cardoso, Saleiro, and Bizarro (2022) proposed representing the transaction network as a bipartite account-transaction graph and showed promising results in the semi-supervised AML setting. However, it is not clear how these approaches help with detecting typical fraud patterns.

### 3 Background


#### 3.1 Graphs and Financial Transaction Graphs


[pp. 2-3]

We consider directed multigraphs, _G_ , where the nodes _v ∈ V_ ( _G_ ) represent accounts, and the directed edges _e_ = ( _u, v_ ) _∈ E_ ( _G_ ) represent transactions from _u_ to _v_ . Each node _u_ (optionally) has a set of account features _h_(0) ( _u_ ); this could include the account number, bank ID, and account balance. Each transaction _e_ = ( _u, v_ ) has a set of associated transaction features _h_(0) ( _u,v_ );thisincludestheamount,cur- rency, and timestamp of the transaction. The incoming and outgoing neighbors of _u_ are denoted by _Nin_ ( _u_ ) and _Nout_ ( _u_ ) respectively. Multiple transactions between the same two accounts are possible, making _G_ a multigraph. In node (or edge) prediction tasks, each node (or edge) will have a binary label indicating whether the account (or transaction) is illicit. Financial Crime Patterns. Fig. 1 shows a selection of

subgraph patterns indicative of money laundering (Granados and Vargas 2022; He et al. 2021; Suzumura 2022; Weber et al. 2018; Starnini et al. 2021). Unfortunately, these are rather generic patterns, which also appear extensively amongst perfectly innocent transactions. As a result, detecting financial crime relies not just on detecting individual patterns, but also on learning relevant combinations. This makes neural networks promising candidates for the task. However, standard message-passing GNNs typically fail to detect the depicted patterns, except for degree-in. In the next section, we describe architectural adaptations, which enable GNNs to detect each one of these patterns.

Subgraph Detection. Given a subgraph pattern _H_ , we define subgraph detection for nodes as deciding for each node in a graph whether it is part of a subgraph that is isomorphic to _H_ ; i.e., given a node _v ∈ V_ ( _G_ ), deciding whether there exists a graph _G__′_ , with _E_ ( _G__′_ ) _⊆ E_ ( _G_ ) and _V_ ( _G__′_ ) _⊆ V_ ( _G_ ), such that _v ∈ V_ ( _G__′_ ) and _G__′∼_ = _H_ .

#### 3.2 Message Passing Neural Networks


[p. 3]

Message-passing GNNs, commonly referred to as Message Passing Neural Networks (MPNNs), form the most prominent family of GNNs. They include GCN (Kipf and Welling 2016), GIN (Xu et al. 2018), GAT (Veliˇckovi´c et al. 2017), GraphSAGE (Hamilton, Ying, and Leskovec 2017), and many more architectures. They work in three steps: (1) Each node sends a message with its current state _h_ ( _v_ ) to its neighbors, (2) Each node aggregates all the messages it receives from its neighbors in the embedding _a_ ( _v_ ), and (3) Each node updates its state based on _h_ ( _v_ ) and _a_ ( _v_ ) to produce a new state. These 3 steps constitute a layer of the GNN, and they can be repeated to gather information from further and further reaches of the graph. More formally:

where _{{.}}_ denotes a multiset, and AGGREGATE is a permutation-invariant function. We will shorten AGGREGATE to AGG, and for readability, we will use _{.}_ rather than _{{.}}_ to indicate multisets.

In the case of directed graphs, we need to distinguish between the incoming and outgoing neighbors of node _u_ . In a standard MPNN, the messages are passed along the directed edges in the direction indicated. As such, the aggregation step only considers messages from incoming neighbors:

where we aggregate over the incoming neighbors, _Nin_ ( _v_ ).

The edges of an input graph may also have input features. We denote the input features of directed edge _e_ = ( _u, v_ ) by _h_(0) (( _u, v_ )). When using edge features during the message passing, the aggregation step becomes:

In the remainder, we omit edge features from formulas when unnecessary in favor of brevity.

a cb d

Figure 2: Nodes ( _a_ and _b_ ) with different out-degrees are not distinguishable by a standard MPNN with directed message passing. Note that naive bidirectional message passing, on the other hand, is unable to distinguish nodes _a_ and _d_ .

### 4 Methods


In this section, we introduce simple adaptations for standard MPNNs (Message Passing Neural Networks) to enable the detection of the fraud patterns in Fig. 1. We consider the adaptations in increasing order of complexity in terms of the patterns they help to detect. We provide theory results to motivate the adaptations and include corresponding experiments on the synthetic subgraph detection dataset in Section 7.1 to support the theory empirically.

When using a standard MPNN with directed edges, a node does not receive any messages from outgoing neighbors (unless they happen to also be incoming neighbors), and so is unable to count its outgoing edges. For example, a standard MPNN is unable to distinguish nodes _a_ and _b_ in Fig. 2. Further, note that naive bidirectional message passing, where edges are treated as undirected and messages travel in both directions, does not solve the problem, because a node then can not distinguish incoming and outgoing edges. So this would fail to distinguish nodes _a_ and _d_ in the same figure.

#### 4.1 Reverse Message Passing


To overcome this issue, we need to indicate the direction of the edges in some way. We propose using a separate message-passing layer for the incoming and outgoing edges respectively, i.e., adding _reverse message passing_ . Note that this is akin to using a relational GNN with two edge types (Schlichtkrull et al. 2018). More formally, the aggregation and update mechanisms become:

where _ain_ is now an aggregation of incoming neighbors and _aout_ of outgoing neighbors. We now prove that messagepassing GNNs with reverse MP can solve degree-out.

Proposition 4.1. _An MPNN with sum aggregation and reverse MP can solve degree-out._

The proof of Proposition 4.1 can be found in Appendix B. In Section 7.1, we use a synthetic pattern detection task to confirm that the theory translates into practice.

#### 4.2 Directed Multigraph Port Numbering


[pp. 3-4]

People often make multiple transactions to the same account. In transaction networks, these are represented as parallel

(1,1) (1,1)(2,1)(2,1)(2,1) (3,1)

Figure 3: Nodes (in gray) with different fan-ins that are not distinguishable by a standard MPNN. The edge labels indicate incoming and outgoing port numbers, respectively.

edges. To detect fan-in (or fan-out) patterns, a model has to distinguish between edges from the same neighbor and edges from different neighbors. Using unique account numbers (or in general node IDs) would naturally allow for this. However, using account numbers does not generalize well. During training, a model can memorize fraudulent account numbers without learning to identify fraudulent patterns, but this will not generalize to unseen accounts.

Instead, we adapt port numbering (Sato, Yamada, and Kashima 2019) to directed multigraphs. Port numbering assigns local IDs to each neighbor at a node. This allows a node to identify messages coming from the same neighbor in consecutive message-passing rounds. To adapt port numbering to directed multigraphs, we assign each directed edge an incoming and an outgoing port number, and edges coming from (or going to) the same node, receive the same incoming (or outgoing) port number. Unlike Sato, Yamada, and Kashima (2019), who attach only the local port numbers at a node to received messages, we attach the port numbers in both directions, i.e., a node sees both the port number it has assigned to a neighbor and the port number that the neighbor has assigned to it. This turns out to be crucial for our expressivity arguments.

Port numbers have been shown to increase the expressivity of GNNs on simple graphs, but message-passing GNNs with port numbers alone cannot even detect 3-cycles in some cases (Garg, Jegelka, and Jaakkola 2020).

In general, the assignment of port numbers around a node is arbitrary. A node with _d_ incoming neighbors can assign incoming port numbers in _d_ ! ways. To break this symmetry in our datasets, we use the transaction timestamps to order the incoming (or outgoing) neighbors. In the case of parallel edges, we use the earliest timestamp to decide the order of the neighbors. Since timestamps carry meaning in financial crime detection, the choice of ordering is motivated; indeed two identical subgraph patterns with different timestamps can have different meanings.

[p. 4]

Computing the port numbers in this way can be a timeintensive step, with runtime complexity dominated by sorting all edges by their timestamps: _O_ ( _m_ log _m_ ), where _m_ = _|E_ ( _G_ ) _|_ . However, port numbers can be calculated in advance, so training and inference times are unaffected. Each edge receives an incoming and an outgoing port number as additional edge features. Fig. 3 shows an example of graphs with port numbers. We now prove that GNNs using port numbers can correctly identify fan-in and fan-out patterns.

Note that the following proof, and later proofs using port numbers, do not rely on the timestamps for correctness. How-

ever, if timestamps that uniquely identify the ports are available, then permutation invariance/equivariance of the GNN will be preserved.

Proposition 4.2. _An MPNN with max aggregation and multigraph port numbering can solve fan-in._

A proof is provided in Appendix B. Adding reverse MP, one can argue similarly that fan-out can also be solved. Both propositions are confirmed empirically in Section 7.1.

Proposition 4.3. _An MPNN with max aggregation, multigraph port numbering, and reverse MP can solve fan-out._

#### 4.3 Ego IDs


[pp. 4-5]

Although reverse MP and multigraph port numbering help with detecting some of the suspicious patterns in Fig. 1, they are not sufficient to detect directed cycles, scatter-gather patterns, and directed bicliques. You et al. (2021) introduced ego IDs specifically to help detect cycles in graphs. The idea is that by “marking” a “center” node with a distinct (binary) feature, this node can recognize when a sequence of messages cycles back around to it, thereby detecting cycles that it is part of. However, it turns out that the proof of Proposition 2 in the paper is incorrect, and ego IDs alone do not enable cycle detection. We give a counterexample in Fig. 6 in the appendix. Indeed, Huang et al. (2022) also note that the proof “confuses walks with paths”.

We see this reflected in the individual results in Table 1. Although ego IDs offer a boost in detecting short cycles, they do not help the baseline (GIN) in detecting longer cycles. This can also be explained theoretically: Assuming a graph has no loops (edges from a node to itself), walks of length two and three that return to the start node are also cycles since there is no possibility to repeat intermediate nodes. Therefore Proposition 2 from You et al. (2021) applies in these cases and it is not surprising that GIN+EgoIDs can achieve impressive F1 scores for 2- and 3-cycle detection.

However, in combination with reverse MP and port numbering, ego IDs can detect cycles, scatter-gather patterns, and bipartite subgraphs, completing the list of suspicious patterns. In fact, it can be shown that a suitably powerful standard MPNN with these adaptations can distinguish any two non-isomorphic (sub-)graphs, and given a _consistent_ use of port-numbering they will not mistakenly distinguish any two isomorphic (sub-)graphs. GNNs fulfilling these two properties are often referred to as _universal_ . The crux of the proof is showing how the ego ID, port numbers, and reverse MP can be used to assign unique IDs to each node in the graph. Given unique node IDs, sufficiently powerful standard MPNNs are known to be universal (Loukas 2019; Abboud et al. 2020).

Theorem 4.4. _Ego IDs combined with port numbering and reverse MP can be used to assign unique node IDs in connected directed multigraphs._

The idea of the proof is to show how a GNN can replicate a labeling algorithm that assigns unique IDs to each node in an ego node’s neighborhood. The labeling algorithm as well as the full proof are provided in Appendix B. The universality of the adaptations follows from this theorem.

Corollary 4.4.1. _GIN with ego IDs, port numbering, and reverse MP can theoretically detect any directed subgraph pattern._

[p. 5]

The proof follows from Theorem 4.4 above and Corollary 3.1 from Loukas (2019). Similar statements can be made for simple undirected graphs. One can remove the reverse MP from the assumptions since this is only needed to make the proof work with directed edges.

Theorem 4.5. _Ego IDs and port numbering can be used to assign unique node IDs in connected undirected graphs._

Corollary 4.5.1. _GIN with ego IDs and port numbering can theoretically detect any subgraph in undirected graphs._

The ablation study in Table 1 of Section 7.1 again supports the theoretical analysis. The combination of the three adaptations achieves impressive scores for all subgraph patterns.

Note that passing the port numbers of both incident nodes of an edge is crucial for inferring unique node IDs. Fig. 5 in the appendix illustrates this with a simple example. In particular, port numbering, as introduced by Sato, Yamada, and Kashima (2019), is not sufficient.

#### 4.4 Complexity & Runtime


We propose a set of adaptations, so the final model complexity will depend on the choice of base GNN. We describe the additional runtime costs incurred by the adaptations in Appendix C. All in all, the adaptations add a constant factor to the runtime complexity in addition to a one-off precomputation cost of _O_ ( _m_ log( _m_ )). The empirical runtimes on AML Small HI using GIN can be seen in Appendix F.5.

datasets generates a financial transaction network by modeling agents (banks, companies, and individuals) in a virtual world. The generator uses well-established laundering patterns to add realistic money laundering (illicit) transactions. We use two small and two medium-sized datasets, one of each with a higher illicit ratio (HI) and with a lower illicit ratio (LI). The dataset sizes and illicit ratios are provided in Table 4 in the appendix. We use a 60-20-20 temporal train-validation-test split, i.e., we split the transactions after ordering them by their timestamps. Details can be found in Appendix E.

Ethereum Phishing Detection (ETH). Since banks do not release their data, we turn to cryptocurrencies for a real-world dataset. We use an Ethereum transaction network published on Kaggle (Chen et al. 2019a), where some nodes are labeled as phishing accounts. We use a temporal train-validation-test split, but this time splitting the nodes. We use a 65-15-20 split because the illicit accounts are skewed towards the end of the dataset. More details and dataset statistics can be found in Appendix E.

Real-World Directed Graph Datasets. The theory results and the subgraph detection tasks demonstrate the general purpose potential of the architectural adaptations. However, testing our model on real-world benchmark datasets is important to further support these claims. For lack of established directed multi-graph benchmarks, we have taken three directed graph datasets, Chameleon, Squirrel (Pei et al. 2020), and Arxiv-Year (Hu et al. 2020), and compare our approach with the state-of-the-art model for these benchmarks (Rusch et al. 2022). As these datasets are not the focus of this paper, we leave the experimental details and results to the appendix; please see Appendix G.

### 5 Datasets


Synthetic Pattern Detection Tasks. The AML subgraph patterns seen in Fig. 1 are used to create a controllable testbed of synthetic pattern detection tasks. The key design principle is to ensure that the desired subgraph patterns appear randomly, rather than being inserted post hoc into a graph. The problem with inserting patterns is that it skews the random distribution, and simple indicators (such as the degrees of nodes) can be enough to solve the task approximately. For example, consider the extreme case of generating a random _k_ -regular graph and then inserting a pattern. Nodes belonging to the pattern could be identified by checking whether their degree exceeds _k_ . Additionally, if only inserted patterns are labeled, then randomly occurring patterns will be overlooked.

To ensure that the desired subgraph patterns appear randomly, we introduce the _random circulant graph_ generator. Details of the generator and pseudocode can be found in Appendix D.1. The pattern detection tasks include degree-in/out (number of in/out edges), fan-in/out (number of unique in/out neighbors), scatter-gather, directed biclique, and directed cycles of length up to six. Detailed descriptions can be found in Appendix D.2.

Anti-Money Laundering (AML). Given the strict privacy regulations around financial data, real-world datasets are not readily available. Instead, we use simulated money laundering data (Altman et al. 2023). The simulator behind these


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Provably Powerful Graph Neural Networks for Directed Multigraphs" (2023-06-20). https://arxiv.org/abs/2306.11586
