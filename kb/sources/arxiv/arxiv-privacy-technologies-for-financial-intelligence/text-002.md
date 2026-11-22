---
type: Source Text
title: Privacy Technologies for Financial Intelligence - part 2 of 4 (pp. 16-29)
description: 'Verbatim extracted text, pp. 16-29: Privacy Technologies for Financial Intelligence > 4. Privacy-Preserving Information Sharing; Privacy Technologies for Financial Intelligence > _4.1. Suspicious Persons List_; Privacy Technologies for Financial Intelligence > _4.2. Transaction Flow Tracing and Typology Matching_; and 2 more sections'
resource: https://arxiv.org/abs/2408.09935
tags:
- academic_finding
- global_academic
- preprint
- privacy_data_protection
- public_private_partnership
status: stable
source_id: arxiv-privacy-technologies-for-financial-intelligence
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-08-19'
legal_status: unknown
part: 2
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T14:32:20Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T14:32:20Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2408.09935
  title: Privacy Technologies for Financial Intelligence
  author: org:arxiv
  last_modified: '2024-08-19T00:00:00Z'
---

# Privacy Technologies for Financial Intelligence

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2024-08-19), part 2 of 4, pp. 16-29. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Privacy Technologies for Financial Intelligence


### 4. Privacy-Preserving Information Sharing


[p. 16]

In this section, we revisit the three computational problems listed at the end of § 2 and further contextualise them using real-world financial intelligence scenarios wherein information-sharing between different parties is crucial to support effective detection of financial crimes. In each scenario, we discuss the privacy risks during multiparty collaborations and examine the feasibility of applying various privacy-preserving techniques to address these privacy risks.

It is important to recognise that each scenario may entail varying levels of privacy risks. These risks depend on the degree of trust among different parties. The level of trust is basically inversely proportional to the risks of sharing information that have to be shouldered by the collaborating parties, which is in turn a function of the prevailing government legislation (or lack thereof) and applicable penalties in the event of a privacy breach.

The parties involved in conducting financial intelligence analysis today may include both public sectors (domestic or international) and private sectors. Generally speaking, information-sharing between different domestic public sectors involves a high level of trust. In contrast, information sharing between public and private sectors, or among private sectors, often entails a low level of trust. This lack of trust may stem from various factors, including the absence of clear legislation and threats of business competition. For instance, financial institutions tend to refrain from sharing customer transaction data among themselves, despite the potential benefits such informationsharing could offer in enhancing their anti-money laundering controls. Privacy technologies provide the greatest value in low-trust settings that exist either because the parties involved cannot trust each other or a third party for commercial/legal reasons, or when there is ambiguity on whether a publicgood sharing of information crosses the threshold into unacceptable privacy intrusion.

### _4.1. Suspicious Persons List_


[pp. 17-18]

_Problem statement._ Suppose an FIU possesses a moderate-sized list of suspicious individuals (or, more generally, commercial entities) obtained, say, from its own investigations and law-enforcement agencies and the FIU wishes to acquire additional information about those suspicious individuals, including where they conduct their financial activities and whether they are known to other FIUs. This can be done if the FIU can safely distribute the Suspicious Person List (SPL) to other FIUs and financial institutions to verify the association of individuals on the list with specific financial entities before engaging in further targeted information exchanges with those financial entities.

_Privacy risks._ If the SPL is shared with the financial institution in a manner that allows for the identification of individuals on the list, there arise the following privacy concerns, especially in the low-trust public-to-private information-sharing setting.

- (Accidental Tip-off) The financial institution may inadvertently disclose the FIU’s suspicions to an existing customer, prompting the customer to take additional measures to conceal their activities.

- (Debanking and Displacement) The financial institution may deliberately cease its banking relationship with a suspicious individual before conclusive evidence can be gathered to substantiate or refute the individual’s suspected wrongdoing. This action may be deemed discriminatory if the financial institution’s decision to terminate services is also influenced by personal factors such as the individual’s nationality, race, or name. Further, suspected individuals that are debanked will also move on to other parts of the financial system, including the shadow financial system, and the FIU will lose sight of them.

- (Need to Know) The FIU can inadvertently disclose the identities of suspicious entities who are not customers of a financial institution, and that would be an unacceptable violation of those individual’s privacy and the need-to-know principle.

_Proposed solution._ The problem described above of identifying common individuals between the SPL and each participating financial institution’s customer database can be formulated as a private set intersection (PSI) problem.

The goal of PSI is to identify the common elements that appear in the parties’ sets and nothing else.

We now describe a simple semi-honest PSI protocol from [21] that utilises polynomial evaluation and homomorphic encryption to ensure the protection of unmatched individuals in the SPL. For detailed security and efficiency analyses, readers are encouraged to refer to [21]. For simplicity, it is assumed that each individual can be uniquely identified by an identification (ID) number, which can be derived from a national ID (in some countries) or a combination of personal information. Here are the steps of the protocol.

1. Assuming the FIU’s list of suspicious individuals is _S_ = _{s_ 1 _, . . . , sn}_ , the FIU first defines the polynomial

[pp. 18-19]

whose roots are exactly the elements in the set _S_ . The question of whether an arbitrary _s__′_ is in _S_ can be checked by evaluating _f_ ( _s__′_ ).

2. The FIU uses polynomial interpolation to find the coefficient representation of _f_ ( _x_ )

which is uniquely defined according to the Fundamental Theorem of Algebra. The FIU then encrypts the coefficients of _f_ ( _x_ ) using HE and sends the encrypted coefficients and the public key to the other parties:

3. Upon receiving the encrypted _f_ , each financial institution evaluates the encrypted polynomial Enc( _f_ ) at each element _d ∈ D_ in its customer database, then multiplies the evaluation result by a random integer _r_ and adds it to _d_ . The property of HE guarantees that the result of these operations is equivalent to the following

The above formula ensures that if _d_ is a positive match then FIU is able to identify it from the output, and if _d_ is not a positive match then FIU learns nothing about _d_ from the output.

4. Once the matching outputs are shared, FIU decrypts the outputs and finds those elements that also appear in its suspicious person list.

By executing this PSI protocol, the FIU and financial institutions collaborate in a confidential manner, enabling the FIU to identify individuals who appear on both the FIU’s SPL and the databases of participating financial institutions. This facilitates the FIU in requesting additional information from appropriate financial institutions to conduct further investigations. Simultaneously, individuals listed on the SPL but absent from a financial institution’s database remain undisclosed to that institution. Similarly, individuals present in a financial institution’s database but not flagged on the SPL remain confidential to the FIU.

_Industrial grade solutions._ The FIU.net operated jointly by FIUs in the European Union has offered privacy-preserving sharing of suspicious entities for over a decade now, using the Ma3tch algorithm [22]. A recent legal review of FIU.net can be found in [23]. In Australia, the Australian Financial Crime Exchange ( `http://afcx.com.au` ) is a platform for financial institutions to share lists of entities of interest, from a financial crime and cyber crime perspective, with each other and, selectively, with the Australian Taxation Office.

There are now many fast PSI algorithms that can operate at large scale, including [24, 25, 26]. A key issue with PSI is that an adversary can use repeated PSI computations to completely recover an organisation’s entire dataset. Proposals like [27] seek to address this issue by introducing DP protection into PSI computations.

### _4.2. Transaction Flow Tracing and Typology Matching_


[pp. 19-20]

_Problem statement._ A key problem in financial crime investigation is tracing the entire digital footprint of “dirty money” within the financial system, allowing investigators to clearly track the movement of funds across different financial institutions, how they are processed and transferred and, crucially, their ultimate usage or destination. We call this problem transaction-flow tracing.

A key task in financial intelligence supported by transaction-flow tracing is the identification of accounts that match certain money-laundering or terrorism-financing (ML/TF) typologies. The NDIS fraud described in [28] serves as an example. Australia’s National Disability Insurance Scheme (NDIS) provides financial support to eligible participants to improve their

quality of life. However, continuous fraudulent activities against the NDIS scheme have resulted in several billions of dollars in losses from its intended use [29]. These fraudulent transactions share common patterns, crossing multiple organisations and eventually being transferred overseas. No single institution in the financial system would have all the data required to identify accounts and entities that exhibit such behaviour. We will show in this section how privacy technologies can help tackle this broad class of problems.

_Privacy risks._ This scenario exemplifies a case of government-to-private and private-to-private information sharing, which are generally low-trust settings. Complex ML/TF typologies can usually be described as a graph pattern, where nodes correspond to accounts/entities and edges correspond to transactions between those nodes and there can be non-trivial conditions attached to the nodes and edges. To enable the identification of entities that match a complex ML/TF typology that span the financial system, we would need accounts and transaction data from multiple financial institutions to be matched at scale before a filtering or sub-graph matching operation is performed. This is obviously highly intrusive to entities who are not involved in financial crimes, so we need a way of performing the large-scale data-matching and graph pattern searching in a privacy-preserving manner.

_Proposed solution._ The FinTracer algorithm described in [28] is a computationally efficient way to conduct breadth-first search on large distributed graphs in homomorphically-encrypted space. The algorithm enables Financial Intelligence Units to start with some known suspicious entities and then work with law-enforcement agencies and financial institutions to find the entire footprints of those entities across the financial system

1. without having to disclose the actual identities of the suspicious entities to financial institutions, thus avoiding the risk of accidentally tipping off the entities; and

2. without having to compromise the privacy of unrelated entities even though their data need to be processed.

The key insight behind the FinTracer algorithm is that large distributed graphs can be represented as sparse matrices and the breadth-first search algorithm can be expressed as a sequence of matrix multiplication operations [30]. The FinTracer algorithm can be used as a foundational routine to detect a wide range of financial crime typologies (i.e. graph patterns). Its

[pp. 21-22]

B CA Db1 c1a1 d1b2 c2a2 d2b3 c3a3 d3b4 c4a4 d4c5b5

Figure 5: A simplified transaction network to demonstrate FinTracer. Accounts with crossorganisation transactions are linked by directed edges. There are four financial institutions A, B, C and D, each having a number of accounts. The account _a_ 1 in A directly received NDIS payment.

adoption can thus meaningfully advance the state-of-the-art in financial intelligence agency’s ability to detect complex financial crimes that span multiple organisations in a privacy-preserving manner at scale.

To see how this works, suppose AUSTRAC is interested in identifying the accounts (from multiple financial institutions) that transferred NDIS funds overseas. These accounts either received funds directly from NDIS or indirectly via a limited number of cross-institution transactions. The FinTracer tag _t≤_ is implemented to keep track of accounts with at most _k_ cross-institution transactions. These tags are homomorphically encrypted to securely follow NDIS funds in the entire transaction network. The key components of the FinTracer process are the ElGamal encryption scheme [31] over the additive Curve25519 for its performance efficiency [32], and the aggregations of the tag values across financial institutions over multiple iterations of the breadth-first search algorithm.

Figure 5 is a simplified example of the NDIS fraud scenario. In this example, there are four financial institutions. The only account that directly received suspicious NDIS funds is a1 in institution A. All institutions are only aware of the source and destination accounts that are involved in the transactions they process. In its simplest form (Algorithms 1 and 2 [28]), the FinTracer protocol does the following steps:

- Initialisation: Each financial institution sets the initial FinTracer tag of each of its customer account _x_ to either Enc(1) or Enc(0), depending on whether _x_ receive NDIS funds directly. In the example above,

- _t≤_ ( _a_ 1) = Enc(1) and _t≤_ ( _{b_ 1 _, b_ 2 _, c_ 1 _, c_ 2 _, d_ 1 _}_ ) = Enc(0) (the set notation denotes that the tag is set for element in the set).

- The other accounts do not have cross-institution transactions, hence are out of considerations by the protocol.

- Iteration 1: In the first iteration, the initialised tags are passed to the neighbouring institutions following the transaction flow. The receiving institutions then aggregate the tags with the received tags. In the example, the shared partial mappings are

[p. 22]

- A _→_ B: _PB__A_((_a_1_, b_1)) = Enc(1)_, P_ _B__A_((_a_1_, b_2)) = Enc(1).

- B _→_ C: _PC__B_((_b_1_, c_1)) = Enc(0)_, P_ _C__B_((_b_2_, c_2)) = Enc(0).

- – C _→_ D: _PD__C_((_c_1_, d_1)) = Enc(0)_, P_ _D__C_((_c_2_, d_1)) = Enc(0).

- After receiving these partial mappings, the aggregated tags are – _t≤_ ( _{a_ 1 _, b_ 1 _, b_ 2 _}_ ) = Enc(1) and _t≤_ ( _{c_ 1 _, c_ 2 _, d_ 1 _}_ ) = Enc(0)

- since _t≤_ ( _b_ 1) = _t≤_ ( _b_ 1) + _PB__A_((_a_1_, b_1))=Enc(0) + Enc(1)=Enc(1)and similarly for _t≤_ ( _b_ 2). The tag values of _c_ 1, _c_ 2, _d_ 1 remain Enc(0) since the initial and received tags are Enc(0).

- Iteration 2: The partial mappings are updated by institution B yielding – A _→_ B: _PB__A_((_a_1_, b_1)) = Enc(1)_, P_ _B__A_((_a_1_, b_2)) = Enc(1). – B _→_ C: _PC__B_((_b_1_, c_1)) = Enc(1)_, P_ _C__B_((_b_2_, c_2)) = Enc(1). – C _→_ D: _PD__C_((_c_1_, d_1)) = Enc(0)_, P_ _D__C_((_c_2_, d_1)) = Enc(0).

After receiving these partial mappings, the aggregated tags are

- _t≤_ ( _a_ 1) = Enc(1), _t≤_ ( _{b_ 1 _, b_ 2 _}_ ) = Enc(2), _t≤_ ( _{c_ 1 _, c_ 2 _}_ ) = Enc(1), _t≤_ ( _d_ 1) = Enc(0).

[pp. 22-23]

- Iteration 3: The partial mappings are updated by B and C yielding – A _→_ B: _PB__A_((_a_1_, b_1)) = Enc(1)_, P_ _B__A_((_a_1_, b_2)) = Enc(1). – B _→_ C: _PC__B_((_b_1_, c_1)) = Enc(2)_, P_ _C__B_((_b_2_, c_2)) = Enc(2). – C _→_ D: _PD__C_((_c_1_, d_1)) = Enc(1)_, P_ _D__C_((_c_2_, d_1)) = Enc(1).

After receiving these partial mappings, the aggregated tags are

- _t≤_ ( _a_ 1) = Enc(1), _t≤_ ( _{b_ 1 _, b_ 2 _}_ ) = Enc(3), _t≤_ ( _{c_ 1 _, c_ 2 _}_ ) = Enc(3), _t≤_ ( _d_ 1) = Enc(2).

The FinTracer tags are now sent to the FIU and decrypted. Only those accounts with a non-zero tag have received money that can be traced either directly or indirectly to suspicious NDIS payment.

_Finding key players in transaction networks._ Once the small number of accounts and entities that matched a certain ML/TF typology is detected using a technology like FinTracer, an FIU like AUSTRAC has the legal power to request much more comprehensive information about those accounts and entities from financial institutions because the request for information or notice to produce information is now targeted and backed by genuine grounds for suspicion. (The remaining small-scale privacy concerns can mostly be addressed using differentially private graph search algorithms like [33].) With such a dataset, it then makes sense to calculate connected components and risk metrics like PageRank scores and betweenness centrality scores, some of which have been shown to be useful features to enhance the accuracy or confidence of machine learning or rule-based financial intelligence classification models [34, 35, 36].

[p. 23]

_Industrial grade solutions._ An open-source, scalable implementation of FinTracer can be found at `http://github.com/AUSTRAC` . The implementation includes a C/Cuda library for additive HE with ElGamal over the Ed25519 elliptic curve. A number of algorithms for different graph operations are included in `http://github.com/AUSTRAC/ftillite/Documentation/ Purgles` . The extension of FinTracer, which allows only linear operations because of the use of additive HE, to non-linear set and graph operations to allow the detection of more-or-less arbitrarily complex criminal typologies is described in [37]. Note that differential privacy noise is added in several steps in these algorithms to avoid variations of database-reconstruction attacks [38, 39].

Techniques described in this section can also be extended to provide more general SQL-like queries on encrypted data, using ideas described in CryptDB [40, 41]. In this area, Enveil and Duality provide industry-grade solutions with their products, Enveil ZeroReveal Search and Duality Query Engine. Such solutions allow organisations to run SQL-like queries on decentralised databases, ensuring data remains within the owner’s environment and supporting compliance with data sovereignty laws. Additionally, these secure systems encrypt both query content and results, keeping them private and visible only to the querier.

### _4.3. Collaborative Model Learning_


[pp. 24-25]

_Problem statement._ The use of supervised learning and anomaly detection algorithms to learn financial crime models from data has long been a topic of interest within financial intelligence [35, 36], but the practical utility of such approaches has been hampered by a lack of quality labelled data in the case of supervised learning algorithms, and high false positive rates in the case of anomaly detection algorithms.

Recent advances in privacy-preserving FL have the potential to alleviate some of these issues by allowing different business units within a financial institution and even multiple financial institutions to jointly learn models from their collective data. In this section, we describe some of the key ideas behind some exploratory work in this area.

_Privacy risks._ To enable FL, we would need accounts and transaction data from multiple financial institutions to be matched, often probabilistically, at scale before a machine learning algorithm can be run. In the case of supervised learning, the participating parties would also need to share, as labelled data, entities that are either known or suspected to be engaging in financial crime. This is obviously highly intrusive to entities who are not involved in financial crimes, and also causes the kind of tipping-off issues discussed in Section 4.1 for those (suspected to be) involved in financial crimes. All these imply that we need scalable and secure ways to perform large-scale probabilistic data matching and model learning in a privacy-preserving manner. The publication and reuse of machine learning models by multiple organisations also open the door to attacks like membership inference that need to be managed [42].

_Proposed solutions._ As discussed, the first step in FL is privacy-preserving data matching. Unlike transaction flow tracing, where the source and target of each transaction are uniquely identifiable for exact matching, there can be inconsistencies in how different financial institutions collect and store individual information, such as names, addresses, driver’s licences, business names, and other details. Consequently, data matching and entity resolution in federated learning - both within and across financial institutions - are often performed probabilistically. A comprehensive description of key privacypreserving data matching/record linkage algorithms, including those that are built on Bloom Filters can be found in [12].

Figure 6: Federated learning setup for privacy-preserving risk modelling using linear regression

We now describe a simplified example of federated learning to illustrate its applicability in financial intelligence. The task is to learn a linear regression risk model using probabilistically matched data from multiple participating parties, while preserving privacy in a distributed manner. The target of the regression is the individual risk score, and the features for the regression are derived from all the data held by the REs. The setup is shown in Figure 6 for three parties.

[pp. 25-27]

More formally, given a training set _{_ ( _x_ _l, yl_ ) _}l_ =1 _,...,m_ that includes _m_ individuals, where the feature set _x_ _l_ = _x_(1) _l ∪· · ·∪_ _x_( _l__p_) is the union of the features from all parties, the task is to fit a linear regression model _Y_ = _Xw_ + _ϵ_ that predicts the target variable _Y_ as accurate as possible.

The regression training is performed using gradient descent. The weight vector _w_ is initially assigned random values and then updated using the gradient of the loss function with respect to each weight element _wj_ as follows, until convergence.

The algorithm converges to the optimal solution because the least-squares loss function is convex and the learning rate _α_ controls the convergence rate. Below are the steps for the privacy-preserving distributed version of the algorithm that uses an additive HE system.

1. The FIU generates a public-private key pair ( _pk_ , _sk_ ) and shares the public key _pk_ with the REs.

2. Each RE initialises its portion of the weight coefficients _w_(_i_) randomly and computes a partial prediction for each individual

...

where _x_( _l__i_) is the feature set of individual _l_ held by the _i__th_ RE.

3. Each RE homomorphically encrypts its partial prediction element-wise and participates in a round robin communication to aggregate a complete prediction for each individual. The resulting encrypted prediction is then sent to the FIU for subsequent computation.

4. The FIU decrypts the complete prediction and computes the difference from the actual values

and then sends the unencrypted _E_ back to the REs.

5. Each RE then updates its portion of the weight vector _w_(_i_) independently using Equation (2)

where _j_ ranges over the variables held by the RE.

6. Repeat steps 2 to 5 until the model has converged.

Throughout the entire computation, the FIU only sees the predicted values from the REs, from which it cannot recover the data held by the REs. Conversely, the REs only see the encrypted partial predictions from each

other and the gradients from the FIU, from which they cannot recover the data held by the FIU or other REs.

[pp. 27-28]

In the remainder of this subsection, we provide a survey of some innovative use of FL that holds promise for financial intelligence. In the work of [43], we see a reasonably compelling demonstration of how FL can significantly enhance the detection capabilities of financial crime models. Through a series of case studies and rigorous experimental evaluations, this research highlights the dual achievement of improved detection performance and robust data privacy.

Building upon this foundation, [44] introduces a novel approach that advances secure and collaborative model training across multiple financial institutions. By integrating HE with FL, this approach achieves secure model aggregation and parameter updates. The experimental results and evaluations presented reveal the approach’s effectiveness in preserving data privacy and security, thus fostering a collaborative environment for financial data analysis across institutions.

Further extending this narrative, [45] presents an end-to-end scheme designed for linear classifiers, employing additive HE to counter semi-honest adversaries in vertical FL scenarios. This research delves into the impact of entity resolution on learning performance, utilising a Taylor approximation for the loss and gradient functions. The application of Paillier additive HE within this context enables privacy-preserving computations, showcasing an innovative method for handling sensitive data securely.

Additionally, [46] proposes a FL scheme tailored for fraud detection. In this scheme, individual financial organisations enhance their model parameters with DP noise before transmitting them to a central server. This strategy effectively diminishes the server’s ability to recover private information, advancing the cause of privacy in fraud detection efforts.

The above FL techniques collectively offer a glimpse into the forefront of financial intelligence. Their contributions highlight ongoing advancements and set the stage for future innovations in the field.

_Industrial grade solutions._ There are several industrial-grade solutions like [47, 7] for conducting probabilistic matching of databases with millions to billions of entities and these can be used in conjunction with techniques like Bloom filters and HE to produce somewhat scalable privacy-preserving prob-

abilistic data-matching algorithms. Privitar SecureLink7 offers a solution for securely joining data from various contributors without revealing sensitive identifiers or directly linking data across organisations.

While federated learning is now a mature technology, progress in using federated learning at the industrial scale for financial intelligence applications is still somewhat hampered by general lack of labelled data to support the acquisition of robust and trusted machine-learning models with low falsepositive rates. Having said that, several case studies and investigations have validated and implemented privacy-preserving solutions for specific scenarios. In particular, industrial solutions developed by Enveil, Duality, and Inpher have scaled effectively to address real-world challenges, with some initiatives leading to collaborations with other organisations to create domain specific products. The details are described in Section 5.

### 5. Real-World Case Studies


[pp. 28-29]

In this section, we describe several case studies that have been trialled and, in some cases, deployed in real-world applications. The presentation provides an update on some key projects first listed in [4] and includes more recent additional work; the emphasis is on the business problem, participating financial institutions, and achieved business outcomes (when that is available.) The case studies vary in scope and complexity, with some focusing on a singular use case while others cover all the three major use cases described in Section 4. It is important to note that in the practical context, AML/CTF use cases can be affected by a large number of factors, including computational cost, operational cost, technical complexity, efficiency, data availability, quality and interoperability. These case studies are summarised in Table 1.

_Enveil ZeroReveal Inter-Bank Private Collaboration [4]._ This is an initiative, started in 2019, by the UK Financial Conduct Authority (FCA) Global AML and Financial Crime TechSprint and Enveil to develop a system that could enable data and knowledge sharing between stakeholders to identify and prevent money flows within and between criminal networks. This initiative was supported by several private UK banks including EY, BAE Systems, Refinitiv, HSBC, Barclays and ING. Their proposed system used homomorphic

> 7SecureLink website

Table 1: Overview of several case studies by different jurisdictions.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Privacy Technologies for Financial Intelligence" (2024-08-19). https://arxiv.org/abs/2408.09935
