---
type: Source Text
title: 'The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset - part 2 of 2 (pp. 6-7)'
description: 'Verbatim extracted text, pp. 6-7: The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset > 6 SUBGRAPH LEARNING AT SCALE; The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset > 6.1 SALIENT and SALIENT++; The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset > 6.2 Adapting node-classification GNNs to subgraph classification workloads; and 4 more sections'
resource: https://arxiv.org/abs/2404.19109
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-the-shape-of-money-laundering-subgraph-representation-learning-o
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-04-29'
legal_status: unknown
part: 2
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2404.19109
  title: 'The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset'
  author: org:arxiv
  last_modified: '2024-04-29T00:00:00Z'
---

# The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset

[previous part](text-001.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2024-04-29), part 2 of 2, pp. 6-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset


### 6 SUBGRAPH LEARNING AT SCALE


[p. 6]

The large size of _Elliptic2_ poses substantial challenges for training GNNs. It is imperative to build scalable training and inference systems that address the bottlenecks and workloads of subgraph representation learning. We use GLASS [22] as a motivating example, because it is a simple adaptation of node-classification GNNs while being provably expressive and empirically effective. Specifically, GLASS appends an extra, binary attribute to the feature vector, indicating whether a node belongs to the subgraphs of interest. The authors show that such a _0-1 labeling trick_ enables learning any function over subgraphs, provided that the backbone GNN is sufficiently expressive.

Subgraph methods like GLASS require some changes to those for node classification. Here, we introduce a scalable GNN training system, SALIENT [13], together with its improved successor SALIENT++ [12], which was designed for node classification workloads. Then, we discuss how systems like SALIENT/SALIENT++ can be adapted to address subgraph classification workloads.

### 6.1 SALIENT and SALIENT++


Large-scale, distributed training of GNNs is faced with two major bottlenecks: the cost of neighborhood sampling dominates that of model evaluation and the distributed storage of node features incurs heavy inter-machine communications.

Neighborhood sampling is a means to reduce the explosive size of the _𝑘_ -hop neighborhood of a minibatch of training nodes. This strategy reduces the computation and memory required in minibatch training. A commonly employed neighborhood sampling algorithm is called _nodewise sampling_ wherein the sampled _𝑘_ -hop neighborhood is computed by sampling up to _𝑓𝑘_ neighbors for each node in the ( _𝑘_ − 1)-hop neighborhood. Neighborhood sampling is performed in CPU memory, as a main computational component of the data loader; however, the CPU throughput is way below that of GPUs, which perform model evaluations based on the sampled neighbors.

To address the bottleneck of neighborhood sampling, SALIENT [13] implements the sampler in C++ by using the most efficient data structures, performs shared-memory parallel batch preparation by using C++ threads as opposed to PyTorch’s multi-processing, and pipelines the data transfers between GPUs and CPUs to maximize GPU utilization. These performance engineerings enable SALIENT to achieve a speedup of 3× over the standard GNN system implemented by using the popular PyTorch-Geometric library with a single GPU and a further 8× parallel speedup with 16 GPUs, on the

ogbn-papers100M dataset, one of the largest benchmarks for graph deep learning.

When node features are partitioned (such that each partition contains a subset of nodes) and stored in different machines, the communication of features across machines becomes another training bottleneck. Inter-machine communication occurs because the sampled _𝑘_ -hop neighborhood inevitably includes nodes outside a partition (i.e., those stored in another machine).

To reduce the communication volume, SALIENT++ [12] employs a static caching policy that caches the features of the frequently accessed out-of-partition nodes. This policy is based on a technique called _vertex-inclusion probability_ (VIP) analysis, which works in the following. Given a graph _𝐺_ = ( _𝑉, 𝐸_ ) and T ⊂ _𝑉_ of vertices in the training set, VIP analysis begins by estimating the probability that a given vertex will be present in a randomly selected minibatch of size _𝐵_ . The probability that any given vertex appears in such a minibatch is |T |/| _𝑉_ |. An iterative process is then performed to calculate the probability that a vertex will be sampled, using neighborhood sampling, in each layer of the GNN. This caching policy enables SALIENT++ to achieve a 12.7× speedup over another popular training system, DistDGL, on eight machines for the ogbn-papers100M benchmark.

### 6.2 Adapting node-classification GNNs to subgraph classification workloads


For subgraph methods such as GLASS, existing efficient training systems for node classification can be modified to handle subgraph classification workloads. We take SALIENT and SALIENT++ for example.

First, the neighborhood sampling code in SALIENT can be adapted to operate on subgraphs with only minor modifications to the composition of minibatches. A minibatch of subgraphs can be represented as a list of nodes combined with metadata indicating the ranges in the list that correspond to distinct subgraphs. A minibatch can be constructed during training by shuffling the subgraphs in the training set and then forming a minibatch of the selected subgraphs’ contained nodes. With these adaptations, the existing fast sampling code in SALIENT can be used to address the computational bottlenecks of neighborhood sampling in subgraph classification.

Second, the VIP analysis technique used by SALIENT++ can be adapted to handle subgraph workloads in a fairly straightforward manner as well. Conceptually, one can reduce the problem to that of computing an optimal static caching policy for a node classification workload with an augmented graph and sampling scheme. The augmented graph _𝐺_′ contains all of the nodes and edges of _𝐺_ , but additionally contains one extra node per subgraph which is connected to all nodes in _𝐺_ contained in that subgraph by directed edges. The augmented sampling scheme includes one extra layer that samples all neighbors of the “subgraph nodes.” VIP analysis may now be performed on _𝐺_′ by treating the set of added “subgraph nodes” as the training set of a node classification workload. In practice, there is no need to actually materialize _𝐺_′ as the original graph _𝐺_ combined with a list of subgraphs in _𝐺_ is sufficient to perform the required update.

### 7 SUMMARY


[p. 7]

We have contributed a second large, labeled cryptocurrency transaction data set, _Elliptic2_ , five years after _Elliptic1_ was published. _Elliptic2_ is more than two orders of magnitude larger than _Elliptic1_ and it supports a different machine-learning task – subgraph classification – for AML. It offers research opportunities in not only financial forensics but also machine learning, particularly, subgraph representation learning. We demonstrated its utility through training subgraph-based predictive models and discovered an effective one: GLASS.

The model produced very promising results, identifying illicit activity based on on-chain patterns, which were previously only identifiable through off-chain information, once funds entered a regulated exchange service. This opens the way to using the output of these models as an effective compliance tool.

The model also successfully directed us towards previously unknown illicit cryptocurrency wallets, based on the subgraphs - i.e. based on the way funds from these wallets were being laundered. This could be utilised by blockchain analytics companies, law enforcement investigators and financial regulators to identify cryptocurrency wallets involved in illicit activity.

While the model applied here has demonstrated promising results, future studies can improve the prediction performance by using a scalable training system that incorporates node/edge features into the model under a computational budget. The inclusion of more features could enable discovery of more sophisticated and previously undocumented money laundering strategies, leading to the more accurate identification of financial crime.

### 8 DATA AND CODE


The _Elliptic2_ dataset can be accessed through http://elliptic.co/ elliptic2. The accompanying code used for experimentation is located at https://github.com/MITIBMxGraph/Elliptic2.

This work was funded by Elliptic and the MIT-IBM Watson AI Lab, a joint research initiative between the Massachusetts Institute of Technology and IBM Research. Data and domain expertise were provided by Elliptic.

- [8] Europol. 2023. Bitzlato: senior management arrested. https://www.europol. europa.eu/media-press/newsroom/news/bitzlato-senior-management-arrested.

### ACKNOWLEDGMENTS


- [9] Martin Harrigan and Christoph Fretter. 2016. The unreasonable effectiveness of address clustering. In _2016 Intl IEEE Conferences on Ubiquitous Intelligence & Computing, Advanced and Trusted Computing, Scalable Computing and Communications, Cloud and Big Data Computing, Internet of People, and Smart World Congress_ . IEEE, 368–373.

- [10] Weihua Hu, Matthias Fey, Hongyu Ren, Maho Nakata, Yuxiao Dong, and Jure Leskovec. 2021. OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs. In _NeurIPS Datasets and Benchmarks Track_ .

- [11] Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. 2020. Open Graph Benchmark: Datasets for Machine Learning on Graphs. Preprint arXiv:2005.00687.

- [12] Tim Kaler, Alexandros Iliopoulos, Philip Murzynowski, Tao Schardl, Charles E Leiserson, and Jie Chen. 2023. Communication-Efficient Graph Neural Networks with Probabilistic Neighborhood Expansion Analysis and Caching. _Proceedings of Machine Learning and Systems_ 5 (2023).

- [13] Tim Kaler, Nickolas Stathas, Anne Ouyang, Alexandros-Stavros Iliopoulos, Tao Schardl, Charles E Leiserson, and Jie Chen. 2022. Accelerating training and inference of graph neural networks with fast sampling and pipelining. _Proceedings of Machine Learning and Systems_ 4 (2022), 172–189.

- [14] Sarah Meiklejohn, Marjori Pomarole, Grant Jordan, Kirill Levchenko, Damon McCoy, Geoffrey M Voelker, and Stefan Savage. 2013. A fistful of bitcoins: characterizing payments among men with no names. In _Proceedings of the 2013 conference on Internet measurement conference_ . 127–140.

- [15] Malte Möser and Arvind Narayanan. 2022. Resurrecting Address Clustering in Bitcoin. In _Financial Cryptography and Data Security - 26th International Conference, FC 2022, Revised Selected Papers_ . Springer Science and Business Media Deutschland GmbH, 386–403. https://doi.org/10.1007/978-3-031-18283-9_19

- [16] Satoshi Nakamoto. 2008. Bitcoin: A peer-to-peer electronic cash system. (2008).

- [17] United States of America v. Virtual Currency Accounts. 2020. AFFIDAVIT IN SUPPORT OF ISSUANCE OF WARRANT OF ARREST IN REM. https://assetforfeiturelaw.us/wp-content/uploads/2020/08/113-VirtualCurrency-Accounts-Affidavit.pdf.

- [18] Fergal Reid and Martin Harrigan. 2013. An analysis of anonymity in the bitcoin system. In _Security and privacy in social networks_ . Springer, 197–223.

- [19] Elliptic Typologies Report. 2023. https://www.elliptic.co/resources/elliptictypologies-report-2023.

- [20] Dorit Ron and Adi Shamir. 2013. Quantitative analysis of the full bitcoin transaction graph. In _International Conference on Financial Cryptography and Data Security_ . Springer, 6–24.

- [21] Elliptic Data Set. 2019. https://www.kaggle.com/ellipticco/elliptic-data-set.

- [22] Xiyuan Wang and Muhan Zhang. 2022. GLASS: GNN with Labeling Tricks for Subgraph Representation Learning. In _International Conference on Learning Representations_ .

- [23] Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Claudio Bellei, Tom Robinson, and Charles E. Leiserson. 2019. Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics. arXiv:1908.02591 [cs.SI]

- [24] Jie Zhou, Ganqu Cui, Shengding Hu, Zhengyan Zhang, Cheng Yang, Zhiyuan Liu, Lifeng Wang, Changcheng Li, and Maosong Sun. 2021. Graph Neural Networks: A Review of Methods and Applications. arXiv:1812.08434 [cs.LG]

### REFERENCES


- [1] Bijaya Adhikari, Yao Zhang, and Naren Ramakrishnan. 2018. Sub2Vec: Feature Learning for Subgraphs. In _PAKDD_ .

- [2] Emily Alsentzer, Samuel G Finlayson, Michelle M Li, and Marinka Zitnik. 2020. Subgraph Neural Networks. _Proceedings of Neural Information Processing Systems, NeurIPS_ (2020).

- [3] Elli Androulaki, Ghassan O Karame, Marc Roeschlin, Tobias Scherer, and Srdjan Capkun. 2013. Evaluating user privacy in bitcoin. In _International Conference on Financial Cryptography and Data Security_ . Springer, 34–51.

- [4] Vijay Prakash Dwivedi and Xavier Bresson. 2021. A Generalization of Transformer Networks to Graphs. In _AAAI Workshop on Deep Learning on Graphs: Methods and Applications_ .

- [5] Vijay Prakash Dwivedi, Chaitanya K. Joshi, Anh Tuan Luu, Thomas Laurent, Yoshua Bengio, and Xavier Bresson. 2020. Benchmarking Graph Neural Networks. Preprint arXiv:2003.00982.

- [6] Vijay Prakash Dwivedi, Ladislav Rampášek, Mikhail Galkin, Ali Parviz, Guy Wolf, Anh Tuan Luu, and Dominique Beaini. 2022. Long Range Graph Benchmark. In _NeurIPS Track on Datasets and Benchmarks_ .

- [7] Elliptic. 2023. Five ways coin swap services facilitate money laundering and sanctions evasion. https://www.elliptic.co/blog/five-ways-coin-swap-servicesfacilitate-money-laundering-and-sanctions-evasion.


---

[previous part](text-001.md) | [source overview](overview.md)

[^original]: arXiv, "The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset" (2024-04-29). https://arxiv.org/abs/2404.19109
