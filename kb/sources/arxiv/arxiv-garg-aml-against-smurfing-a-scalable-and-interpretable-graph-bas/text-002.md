---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 2 of 10 (pp. 5-11)'
description: 'Verbatim extracted text, pp. 5-11: 3 GARG-AML; 3 GARG-AML > 3.1 Preliminaries and Notation; 3 GARG-AML > 3.2 Undirected Network; and 6 more sections'
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
part: 2
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 2 of 10, pp. 5-11. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 3 GARG-AML


[p. 5]

GARG-AML provides each individual node with a score expressing how likely it is that this entity is involved in a smurfing scheme. This is done by analysing the second-order neighbourhood of the nodes. We start by formally defining some crucial concepts. Afterwards, we introduce two versions for GARG-AML, one for undirected and one for directed networks. The full GARG-AML method is given in Algorithm 1.

The process of money laundering is traditionally divided into three stages (Levi and Reuter, 2006; United Nations Office on Drugs and Crime, 2011). During placement, illicit funds enter the financial system, often in jurisdictions where regulatory checks are lighter. During layering, transactions mix illegally and legitimately obtained money, obscuring their origin. During integration, funds are used to make seemingly legitimate purchases, after which the money is effectively laundered.

### 3.1 Preliminaries and Notation


During the placement and layering stage, money mules are often used (Raza et al., 2020). These can either be people actively recruited from outside the organisation (Esoimeme, 2020; Leukfeldt and Jansen, 2015) or unaware victims whose bank accounts have been hacked (Raza et al., 2020). Their accounts are used to receive money from criminal activity and to quickly transfer it to the criminal organisation’s account. The use of accounts in the name of outsiders circumvents strict KYC rules and puts distance between the criminal activity and the criminals’ accounts (Esoimeme, 2020).

One subcategory of money mules is smurfs (Starnini et al., 2021; Zhdanova et al., 2014). Smurfs are used to break up large transactions and funnel the money through many accounts in smaller instances. This helps the criminals to avoid business rules that are often only monitoring transactions per counterparty (e.g., between person A and B, and A and C, separately, but not aggregated among A,B and C).

A network _G_ ( _V, E_ ) is defined by a set of nodes, _V_ = _{v_ 1 _, . . . , vk}_ , and edges, _E ⊂ V × V_ . We represent the network using the adjacency matrix _A_ . The elements of _A_ indicate whether pairs of nodes are connected via an edge. Mathematically, it is defined as:

_Nk_ ( _v_ ) represents the set of nodes that are at distance exactly _k_ from node _v_ , with _N_ 0( _v_ ) = _{v}_ . GARG-AML relies on the second-order neighbourhood of node _v_ . This is the sub-graph consisting of all nodes at a distance of at most two from _v_ , capturing both direct counterparties ( _N_ 1( _v_ )) and the ‘counterparties of counterparties’ ( _N_ 2( _v_ )).

Suppose that _| N_ 1( _v_ ) _|_ = _n_ and _| N_ 2( _v_ ) _|_ = _m −_ 1; then, the adjacency matrix of the second-order neighbourhood of _v_ is of size ( _m_ + _n_ ) _×_ ( _m_ + _n_ ).

The _k_ th-order neighbourhood of node _v_ is the sub-network _G_ ( _V__′_ _, E__′_ ) where _V__′_ =� _Nl_ ( _v_ ) and _E__′_ = _{_ ( _u, w_ ) _| l≤k_

_u, w ∈ V__′_ _∧_ ( _u, w_ ) _∈ E}_ . Hence, it is the sub-network that represents all nodes at distance at most _k_ and all the interactions among these nodes.

### 3.2 Undirected Network


[pp. 5-6]

We introduce GARG-AML using an example based on the smurfing pattern illustrated in Figure 2. We will consider only the scatter-gather pattern, as this is most widely recognised as smurfing. The methodology is the same for gatherscatter patterns.

In this example, node _A_ is given a score. The adjacency matrix of its second-order neighbourhood, given in Equation (1), is constructed by arranging the nodes in a specific order: node _A_ is placed first, followed by the second-order neighbour _E_ , and then its first-order neighbours _B, C_ and _D_ . This ordering results in an adjacency matrix that is divided into four distinct blocks. The diagonal blocks contain only zeros, whereas the off-diagonal blocks contain ones.

Figure 2: Pure smurfing pattern. _A_ is the node that is scored. The first-order neighbours ( _B, C, D_ ) are shown in purple, the second-order neighbour ( _E_ ) is shown in green.

Given these insights, we define the general GARG-AML method, starting with the adjacency matrix. The first row of the adjacency matrix, which corresponds to entries ( _A_ 1 _,j_ ), represents the connections of node _v_ under consideration. The next _m −_ 1 rows, i.e., ( _Ai,j_ ) for 2 _≤ i ≤ m_ , represent the connections of nodes at distance two from _v_ . The final _n_ rows, i.e., ( _Ai,j_ ) for _m_ + 1 _≤ i ≤ m_ + _n_ , represent the connections of nodes at distance one.

Enforcing this node ordering—the target node, second-order neighbours, and first-order neighbours—for the adjacency matrix ensures that the diagonal blocks remain sparse (low density), and the off-diagonal blocks have a high density in case of pure smurfing patterns. The exact order of nodes within each group is not important. Any permutation within the first-order neighbours, such as _C, B, D_ , is equally valid.

We consider three blocks of the adjacency matrix for score calculation: the upper-left, upper-right, and lower-right blocks. These are defined as follows:

Our method uses the density, i.e., the relative number of non-zero elements in each block. GARG-AML measures the similarity between an observed pattern and the pure smurfing template by analysing the expected density and actual density (or sparsity) of each block. This results in a single quantitative score expressing similarity to the pure smurfing pattern.

[pp. 6-7]

Several structural properties of the adjacency matrix are taken into account for more rigorous density calculations. First, self-loops are excluded; thus, diagonal elements are always zero. Furthermore, in block1 (upper-left block), the first row and column can never contain ones, as a ‘1’ would indicate a direct connection between a node and its neighbours at distance two, a contradiction. This upper-left block serves as a check that the nodes at distance two do not make transactions to each other. Similarly, for block2 (upper-right block), all the elements in the first row must be ones since these represent connections between the node under investigation and its first-order neighbours.

We consider only the _free_ entries, i.e., those that are not certain upfront, for density calculations. We define the block size as the number of free elements. This is reflected in the numerator (number of non-zero elements) and denominator (block size).

Smurfing is likely to be present when the density of block2 (upper-right block) is high, while block1 (upper-left block) and block3 (lower-right) exhibit low densities. Therefore, the final GARG-AML score is calculated as:

Figure 3: The directed version of the smurfing pattern example, extended with an additional sending node (A’) and receiving node (E’). Nodes at level 0 are put in blue, at level 1 in purple and at level 2 in green.

where _li_ is a weight given to each term in the score calculation. If _li_ = 1, the score is the average of score1 and score3. We take a weighted average using the block sizes:

When there is only one destination account, there is only one node at distance two (as in Figure 2). This results in _l_ 1 being 0. Then, the calculations simplify to scoretotal = score2 _−_ score3, and we only analyse whether all money ends up at the destination node (high score2) and none of the intermediary accounts interact with each other (low score3).

The final score in Equation (8) ranges from _−_ 1 to 1. Second-order neighbourhoods resembling a smurfing pattern result in a score close to 1. Additional examples are provided in A.1 as illustration.

### 3.3 Directed Network


[pp. 7-8]

A defining trait of smurfing is the uni-directional flow of funds. Money moves from one account to others with minimal/no return flow (Starnini et al., 2021; Lee et al., 2020; Li et al., 2020; Shadrooh and Nørv˚ag, 2024), forming _pure smurfing_ patterns (see Figure 3). To capture this behaviour, we extend GARG-AML to directed networks.

We start with an example. In the directed network of Figure 3 node _A_ only sends funds to the smurfs, while node _E_ only receives from them. This leads to a non-symmetric adjacency matrix, requiring the analysis of nine matrix blocks instead of three (see Equation (12)). To ensure consistency in block-wise density calculations, especially with multiple senders or receivers, nodes at distance two are classified as senders (level 0) and receivers (level 2).

We define two types of second-order neighbourhoods in network _G_ ( _V, E_ ). The _strong_ second-order neighbourhood, denoted _N_ 2_s_(_v_),considersnodesreachablefrom_v_viaadirectedpathoflengthtwo.The_weak_second-orderneigh- bourhood, _N_ 2_w_(_v_), is based on the undirected network.In both, only nodes at exact distance two are included.

A node _w_ is assigned to level 0 if

To account for reverse flow patterns, we repeat this selection on the reversed network. This means that a node _w_ at distance two of node _v_ is put at level 0 if there is no directed path of length two from _v_ to _w_ nor from _w_ to _v_ . The other second-order neighbours are put at level 2.

For the extended network in Figure 3, node _A__′_ is put at the same level as node _A_ and node _E__′_ at the same level as node _E_ . The resulting adjacency matrix is then

Structural constraints of the adjacency matrix are considered when calculating block-wise densities. For the upperleft block, score00, the first row and column are excluded since all other level-0 nodes are nodes at distance two. Additionally, diagonal elements are excluded for score00, score11 and score22, as self-loops are not present.

Adjustments are also made to score20 and score02, which represent connections between the node and its second-order neighbours. The first row of block02 (from the node to its second-order neighbours) and first column of block20 (from the second-order neighbours to the node) are always zero.

[p. 8]

No adjustments are applied to the remaining blocks, as the directionality among level-1 and level-2 nodes does not impose clear structural constraints.

We take the sizes to be _| N_ 1( _v_ ) _|_ = _n_ , _| N_ 2_s_(_v_)_|_=_m_,and_|N_ 2_w_(_v_)_\N_ 2_s_(_v_)_|_=_l−_1,resultingin_l_nodesat level 0, _n_ nodes at level 1, and _m_ nodes at level 2. The adjacency matrix is partitioned into nine blocks, as shown in Equation (13), with block labels using zero-based indexing to reflect node levels 0, 1, and 2.

where

The final score takes the weighted average of the two blocks expected to have high density, according to the smurfing pattern in Equation (12), and subtracts the weighted average of the remaining blocks, which are expected to be sparse. The final GARG-AML score is between _−_ 1 and 1, to have consistent comparison and interpretation across datasets.

Additional examples are provided in A.2 as illustration.

The GARG-AML scores offer three key advantages. First, scores near 1 offer a transparent signal for automated detection and human investigation by reflecting structural smurfing resemblances. Second, the resulting scores and densities can be easily incorporated into existing business rules or machine learning workflows. Third, each score is computed independently using a node’s second-order neighbourhood, allowing for efficient parallel computation and low memory usage, even on large transaction networks.

### 3.4 Integration in Existing Detection Systems


This section illustrates how GARG-AML can easily be integrated in existing detection methods.

Rule-based systems can integrate new scenarios based on the GARG-AML score and its interaction with other features. The rules remain highly interpretable, given that the GARG-AML scores are within a fixed range, with higher scores indicating that the network resembles smurfing. More complex scenarios can be constructed using the individual densities and sizes of the blocks. These are obtained during the intermediary calculations, so these do not increase calculation costs.

Detection models based on machine learning can also be extended. The scores or densities can be interpreted as additional client features. The existing pipelines can be kept to retrain the models.

## 4 Experimental Setup


### 4.1 Data


[pp. 8-9]

Due to the high sensitivity of financial transaction and fraud data, which precludes the use of proprietary banking datasets, we evaluate the detection power of GARG-AML using a two-tiered approach. First, we utilise self-generated

Table 3: Overview of the parameters used to construct the synthetic data.

|Parameter|Values|Barab´asi-Albert|Erd˝os-R´enyi|Watts-Strogatz|
|---|---|---|---|---|
|Number of initial nodes|_{_100; 10,000; 100,000_}_|✓|✓|✓|
|Number of edges|_{_1; 2; 5_}_|✓|✗|✓|
|Edge (rewiring) probability|_{_0.001; 0.01_}_|✗|✓|✓|
|Number of smurfing patterns|_{_3; 5_}_|✓|✓|✓|
|Total number of combinations||18|12|36|

Figure 4: A random network with the three methods of smurfing pattern injection. Solid lines indicate nodes and edges of the original network. Dashed lines indicate injected nodes and edges.

networks created through various simulation methods to maintain full control over network size, topology, and the specific smurfing patterns present, allowing us to illustrate the model’s scalability and its performance against diverse camouflaging tactics. Second, we test the framework on realistic open-source datasets that mimic real-life transaction flows, including millions of transactions with a realistically low ratio of confirmed money laundering cases. This establishes a robust evaluation procedure while ensuring all experiments remain fully reproducible.

### 4.1.1 Synthetic Data


[pp. 9-10]

We generate synthetic networks of varying sizes using three generation methods, i.e., Barab´asi-Albert (Barab´asi and Albert, 1999), Erd˝os-R´enyi (Erd˝os and R´enyi, 1959) and Watts-Strogatz (Watts and Strogatz, 1998). By generating networks with varying properties, we evaluated GARG-AML across a spectrum of topologies.

Each method has specific parameters that we vary to obtain a range of networks to test our method. We summarise these in Table 3. The first parameter is the size of the network, which is subsequently set to 100, 10,000 and 100,000.

The definitions of the other parameters differ depending on the method. For Barab´asi-Albert, _the number of edges_ represents the number of nodes to which each new node connects, resulting in a large difference in degree across the nodes. For Watts-Strogatz, on the other hand, this is half the initial degree that all the nodes have before some of the edges are rewired.

For the Erd˝os-R´enyi method, _the edge (rewiring) probability_ is the probability of having an edge between any two nodes. The Watts-Strogatz method starts with a fixed number of nodes, and uses this parameter to express the probability that an edge changes its end node (rewiring).

Smurfing patterns are injected after network generation. The three types of smurfing patterns (visualised in Figure 4) considered in the experiment are:

1. Separate: The smurfing patterns are not connected to the rest of the network;

2. External smurfs: Mules are added between two existing entities in the network;

3. Internal smurfs: Existing nodes in the network are assigned the roles of sender, receiver and mule, and corresponding transactions are added.

In our experiments, each of the smurfing patterns is included either three or five times; see Table 3. The number of smurfs in each pattern is randomly chosen between two and ten. This allows for both smaller and larger smurfing patterns. A summary of all synthetic datasets is presented in Table 4.

Since we have information on which nodes are involved in which pattern, we not only test the methods for money laundering detection in general; we analyse the performance on the different patterns separately, representing increasing levels of obfuscation.

### 4.1.2 Open-Source Data


[p. 10]

As post-hoc injection of specific patterns may lead to detection bias (Deprez et al., 2026) and altered topology (Egressy et al., 2024), we also include data without this injection. We use the HI-Small and LI-Large datasets, made publicly available by Altman et al. (2023) and Egressy et al. (2024), representing a relatively small dataset with high money laundering activity and a large dataset with low money laundering activity, respectively. Table 5 summarises the number of nodes, edges and the percentage of cases labelled as money laundering. Especially LI-Large closely resembles real-world transaction networks.

These two datasets are generated using the same simulator (Altman et al., 2023; Egressy et al., 2024). It models financial transactions in a virtual world involving individuals, companies, and banks. A subset of these transactions is labelled as money laundering. The data contains detailed labels, categorising transaction streams into eight distinct types: fan-out, fan-in, gather-scatter, scatter-gather, simple cycle, random, bipartite, and stack. The distribution of labelled patterns is shown in Table 6.

It is worth noting that some transactions are labelled as money laundering but do not match any of the eight defined structural patterns. These are grouped under the category “not classified”, indicating that they are suspicious but not attributable to a specific laundering archetype.

The original labels in these datasets are provided at the edge level, while GARG-AML produces features at the node level. To bridge this gap, we aggregate labels by computing the ratio of labelled laundering transactions to the total number of transactions per client. This ratio is interpreted as a propensity score for money laundering.

A node is labelled as a money launderer if the proportion of its laundering-labelled transactions exceeds a certain cut-off. Depending on the cut-off ratio we set, the number of labels and with that the available information will change drastically. This ultimately has an effect on the learning capabilities of the models. We vary these across the full range, to see the effect on the models and to analyse which models perform best under what circumstances. We compare each node’s propensity score against a set of predefined cut-offs: 0%, 10% _,_ 20% _,_ 30% _,_ 50% and 90%. The resulting label distributions are presented in Table 7 and Table 8, for the HI-Small and LI-Large datasets, respectively.

A smaller cut-off means that only a small portion of a node’s transactions should be illicit to label the node as laundering money, with 0% implying that already one transaction is enough. A large cut-off means that most of the transactions should be illicit before the node is labelled as laundering money. The lower cut-offs represent ideal scenarios where almost every illicit transaction is caught. Higher cut-offs mimic reality, where it is often the case that laundering only becomes apparent when many transactions have been made, and where it is easier to detect if limited obfuscation via other transactions is present.

In many cases, fewer than 0 _._ 1% of accounts are assigned a positive label, highlighting the extreme class imbalance and difficulty of the classification task. Additionally, accounts with more than 90% of laundering-labelled transactions are extremely rare, which reflects the realistic behaviour of laundering entities mixing illicit flows with legitimate transactions to obfuscate detection.

### 4.2 Model Specifications


[pp. 10-11]

The full GARG-AML calculation pipeline consists of multiple stages, beginning with pre-processing steps that prepare the network data for analysis, followed by the computation of the GARG-AML scores. We introduce a possible extension that applies tree-based methods, since these have been shown to have strong performance for AML (Jullum et al., 2020; Ramadhan, 2024; Halford et al., 2025; Lokanan, 2025). This extension illustrates the versatility of GARGAML. An overview of the complete pipeline is shown in Figure 5 and summarised in Algorithm 1.

Transaction networks often exhibit a scale-free structure (Starnini et al., 2021), which is characterised by a majority of nodes having only a few connections, while a few nodes, called hubs, have a disproportionately high number of connections. As a result, second-order neighbourhoods that contain such hubs encompass an unmanageable number of nodes for score computation.

Table 4: Summary of the numbers of nodes and edges and money laundering percentages for the synthetic datasets according to the network generation parameters. _m_ is the number of edges and _p_ the edge (rewiring) probability (see Table 3).

[p. 11]

||||3 smi|urfing patte|i rns|5 smi|urfing patter|i ns|
|---|---|---|---|---|---|---|---|---|
||||||Labels|||Labels|
|Generator|_m_|_p_|Nodes|Edges|(%)|Nodes|Edges|(%)|
|_100 initial nodes_|||||||||
|Barab´asi-Albert|1|–|145|199|46.90|180|291|70.00|
|Barab´asi-Albert|2|–|155|345|60.00|179|385|69.83|
|Barab´asi-Albert|5|–|141|582|50.35|175|678|74.29|
|Erd˝os-R´enyi|–|0.001|151|122|52.32|182|196|70.33|
|Erd˝os-R´enyi|–|0.01|153|155|60.78|163|161|65.03|
|Watts-Strogatz|1|0.001|144|204|48.61|176|271|65.91|
|Watts-Strogatz|1|0.01|146|216|52.05|152|248|69.74|
|Watts-Strogatz|2|0.001|131|268|40.46|171|376|70.18|
|Watts-Strogatz|2|0.01|146|316|52.74|180|380|67.22|
|Watts-Strogatz|5|0.001|151|618|52.32|171|669|69.01|
|Watts-Strogatz|5|0.01|145|616|53.10|165|655|66.67|
|_10,000 initial nod_|_es_||||||||
|Barab´asi-Albert|1|–|10,037|10,101|0.69|10,059|10,171|1.15|
|Barab´asi-Albert|2|–|10,042|20,105|0.72|10,081|20,215|1.38|
|Barab´asi-Albert|5|–|10,043|50,103|0.77|10,072|50,167|1.20|
|Erd˝os-R´enyi|–|0.001|10,044|5,101|0.71|10,079|5,263|1.40|
|Erd˝os-R´enyi|–|0.01|10,050|50,388|0.79|10,067|49,998|1.08|
|Watts-Strogatz|1|0.001|10,054|10,132|0.84|10,081|10,168|1.13|
|Watts-Strogatz|1|0.01|10,052|10,134|0.85|10,070|10,182|1.20|
|Watts-Strogatz|2|0.001|10,038|20,104|0.70|10,075|20,180|1.19|
|Watts-Strogatz|2|0.01|10,046|20,134|0.85|10,071|20,190|1.24|
|Watts-Strogatz|5|0.001|10,039|50,090|0.63|10,081|50,196|1.27|
|Watts-Strogatz|5|0.01|10,040|50,108|0.72|10,060|50,148|1.03|
|_100,000 initial no_|_des_||||||||
|Barab´asi-Albert|1|–|100,044|100,099|0.07|100,063|100,167|0.11|
|Barab´asi-Albert|2|–|100,038|200,095|0.07|100,069|200,175|0.12|
|Barab´asi-Albert|5|–|100,043|500,093|0.07|100,065|500,159|0.12|
|Erd˝os-R´enyi|–|0.001|100,033|498,969|0.06|100,087|501,039|0.14|
|Erd˝os-R´enyi|–|0.01|100,044|4,998,019|0.07|100,076|4,997,365|0.13|
|Watts-Strogatz|1|0.001|100,050|100,124|0.08|100,061|100,166|0.11|
|Watts-Strogatz|1|0.01|100,045|100,096|0.07|100,058|100,134|0.10|
|Watts-Strogatz|2|0.001|100,044|200,114|0.07|100,065|200,154|0.11|
|Watts-Strogatz|2|0.01|100,041|200,116|0.08|100,059|200,154|0.11|
|Watts-Strogatz|5|0.001|100,042|500,114|0.07|100,074|500,176|0.12|
|Watts-Strogatz|5|0.01|100,045|500,116|0.08|100,068|500,166|0.11|


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
