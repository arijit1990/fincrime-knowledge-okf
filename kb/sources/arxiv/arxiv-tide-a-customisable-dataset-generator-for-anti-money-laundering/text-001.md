---
type: Source Text
title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research - part 1 of 5 (pp. 1-9)'
description: Verbatim extracted text, pp. 1-9
resource: https://arxiv.org/abs/2603.01863
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-tide-a-customisable-dataset-generator-for-anti-money-laundering
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-02-03'
legal_status: unknown
part: 1
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.01863
  title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research'
  author: org:arxiv
  last_modified: '2026-02-03T00:00:00Z'
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2026-02-03), part 1 of 5, pp. 1-9. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1] [ref: 1.1]

MONTIJN VAN DEN BEUKEL, University of Amsterdam, The Netherlands JOŽE M. ROŽANEC, Jožef Stefan Institute, Slovenia ANA-LUCIA VARBANESCU, University of Amsterdam/University of Twente, The Netherlands

The lack of accessible transactional data significantly hinders machine learning research for Anti-Money Laundering (AML). Privacy

and legal concerns prevent the sharing of real financial data, while existing synthetic generators focus on simplistic structural patterns

and neglect the temporal dynamics (timing and frequency) that characterise sophisticated laundering schemes.

We present Tide, an open-source synthetic dataset generator that produces graph-based financial networks incorporating money

laundering patterns defined by both structural and temporal characteristics. Tide enables reproducible, customisable dataset generation

tailored to specific research needs. We release two reference datasets with varying illicit ratios (LI: 0.10%, HI: 0.19%), alongside the

implementation of state-of-the-art detection models.

Evaluation across these datasets reveals condition-dependent model rankings: LightGBM achieves the highest PR-AUC (78.05) in

the low illicit ratio condition, while XGBoost performs best (85.12) at higher fraud prevalence. These divergent rankings demonstrate

that the reference datasets can meaningfully differentiate model capabilities across operational conditions.

Tide provides the research community with a configurable benchmark that exposes meaningful performance variation across

model architectures, advancing the development of robust AML detection methods.

Additional Key Words and Phrases: Anti-money laundering, synthetic data generation, graph neural networks, financial fraud detection,

temporal patterns, dataset benchmarking

1 Introduction

Money laundering enables criminals to disguise illegal funds by routing them through complex transactions to integrate

them into the legitimate financial system. These funds often fuel other illicit activities, including drug distribution,

bribery, corruption, and terrorism [22]. An estimated 2–5% of global GDP is laundered annually, amounting to $800

billion to $2 trillion, though the clandestine nature of these operations makes precise measurement difficult [34]. The

fight against money laundering imposes a significant financial burden: in the United States alone, financial crime

compliance costs exceeded $59 billion in 2023 [16], with anti-money laundering (AML) efforts accounting for $4.8 billion

to $8 billion annually, yet yielding fewer than 700 convictions [11]. The challenge of detecting illicit schemes buried

within vast amounts of legitimate financial traffic remains substantial, as most money laundering goes undetected and

regulatory definitions of suspicious activity remain poorly defined [2, 9].

1.1 Machine Learning for Fraud Detection

Financial transactions naturally form complex networks in which entities are connected by monetary flows; thus, they

can be represented as directed graphs. This graph-based representation has proven valuable for money laundering

arXiv:2603.01863v1 [cs.LG] 2 Mar 2026

[pp. 1-2] [ref: 1.2]

detection, as illicit activities often manifest as distinctive network patterns, such as fan-in, fan-out, scatter-gather, and

cyclic structures, that are difficult to detect when analysing transactions in isolation [6, 28].

While traditional machine learning approaches such as Support Vector Machines, Random Forests, and Neural

Networks have been applied to financial fraud detection [31], these methods typically operate on tabular transaction

Corresponding author: Jože M. Rožanec: joze.rozanec@ijs.si. Authors’ Contact Information: Montijn van den Beukel, montijnvandenbeukel@gmail.com, University of Amsterdam, Amsterdam, The Netherlands; Jože M. Rožanec, joze.rozanec@ijs.si, Jožef Stefan Institute, Ljubljana, Slovenia; Ana-Lucia Varbanescu, a.l.varbanescu@utwente.nl, University of Amsterdam/University of Twente, Amsterdam, The Netherlands.

features without explicitly modelling relational structure among entities. Graph Neural Networks (GNNs) address this

limitation by learning directly from network topology alongside transaction attributes, and have shown promising

results for anti-money laundering and related financial crime detection tasks [13, 26]. Yet regardless of the approach

chosen, developing robust detection models remains difficult due to challenges that extend beyond model architecture.

1.2 Current Limitations and Challenges

These challenges are primarily rooted in data access and availability. First, legal, privacy, and competition concerns

prevent financial institutions from sharing real transaction data [6], limiting access to high-quality training datasets.

Second, studies presenting classification models suffer from poor reproducibility due to a lack of accessible datasets;

researchers cannot replicate experiments, validate claims, or benchmark new methods against existing work. While

synthetic datasets offer a promising solution by providing shareable alternatives that represent real-world characteristics,

existing generators have significant limitations. They often ignore the temporal dimensions of laundering patterns,

focusing solely on structural relationships [29]. Furthermore, they lack fine-grained customisability for adjusting entity

attributes and pattern parameters, and implement only basic structural patterns while omitting more sophisticated

real-world schemes [7].

1.3 Contributions

To address these limitations, we present Tide, a customisable synthetic data generator that produces reproducible

datasets modelling both the structural and temporal aspects of money laundering patterns. At the broadest level,

Tide addresses the shortage of accessible data that has limited progress in money laundering detection research.

Our contributions are fourfold: (1) we introduce the Tide generator, which advances synthetic data generation by

incorporating temporal dynamics alongside structural relationships, offering extensive customisability for graph

parameters and pattern characteristics; (2) we release reference datasets to facilitate immediate reproducibility and allow

researchers to benchmark detection methods against consistent data; (3) we provide implementations of state-of-the-art

[pp. 2-3] [ref: 1.4]

detection models, serving both to validate the synthetic data and to establish robust baselines for future AML research;

and (4) we perform a comprehensive performance analysis of the generator, demonstrating its scalability and efficiency

in generating large-scale networks.

1.4 Paper Organization

The remainder of this paper is structured as follows. Section 2 reviews related work on fraud characterization, existing

dataset generators, and money laundering detection models. Section 3 presents our research methodology, including

pattern identification, and our graph modelling approach. Section 4 describes Tide’s implementation in detail, including

our reference dataset. Section 5 presents our evaluation results, demonstrating both structural validity and machine

learning model performance on the generated datasets. Finally, Section 6 summarises our contributions, discusses

limitations, and outlines future work.

2 Related work

While the financial burden of AML compliance is immense, the operational failure of legacy systems stems primarily

from their reliance on deterministic logic. Historically, institutions relied on Transaction Monitoring Systems (TMS)

defined by static rules and thresholds. These systems are inherently reactive, flagging activities only when they

deviate from prescribed norms, such as transfers exceeding a fixed value or interactions with high-risk jurisdictions.

Consequently, they generate false positive rates often exceeding 95%, overwhelming analysts and diluting the focus

required to identify genuine financial crime [27].

Machine learning methods aim to provide more precise identification by moving beyond static thresholds to learn

adaptive decision boundaries. Among them, unsupervised methods address legacy limitations by modelling normal

behaviour and identifying anomalies. Clustering algorithms like DBSCAN group entities with similar transaction

profiles, flagging outliers for investigation [14, 41]. However, validation remains challenging without ground truth

labels, and traditional approaches often analyse transactions in isolation rather than capturing coordinated network

activities.

2.1 Money Laundering Detection Models

2.1.1 Traditional Machine Learning Methods. To overcome the rigidity of rule-based systems, machine learning

approaches have been widely adopted for financial fraud detection. A systematic review by Soria et al. [31] examined

models including Support Vector Machines (SVMs), Random Forests, k-Nearest Neighbours, and Artificial Neural

Networks, finding that SVMs achieved the highest reported accuracy among traditional approaches. Gradient Boosted

Trees, particularly XGBoost, have become an industry standard for tabular financial data due to their ability to learn

non-linear patterns, handle extreme class imbalance, and provide interpretable baselines for benchmarking [20].

However, these methods suffer from a fundamental limitation: they treat transactions as independent, isolated events.

They cannot inherently capture the relational dependencies—such as circular flows or long chains of intermediaries—that

characterise sophisticated money laundering schemes, often requiring extensive feature engineering to approximate

network structure.

2.1.2 Graph Representation Learning. Graph-based supervised learning has emerged as a promising approach for

financial fraud detection, with growing adoption in recent years [13, 26]. By representing financial systems as directed

[pp. 3-4] [ref: 2.1.3]

graphs, with entities as nodes and transactions as edges, these methods can model complex, high-dimensional relational

patterns that traditional approaches cannot capture [18]. Graph Neural Networks (GNNs), including Graph Convolutional

Networks (GCNs) [5], Graph Attention Networks (GATs) [36], and Graph Isomorphism Networks (GINs) [38], learn from

both node features and network structure through neighbourhood aggregation, enabling the detection of sophisticated

patterns such as circular fund flows [13].

However, standard GNNs operate under the assumption of homophily, the principle that connected nodes share

similar labels. Financial fraud networks, conversely, are typically heterophilic: illicit actors strategically connect with

legitimate accounts to camouflage their activities [42]. In such settings, standard aggregation mechanisms smooth out

the distinct features of fraud nodes by mixing them with the dominant benign signals from their neighbours, often

degrading detection performance [42]. While recent architectures like CPGNN attempt to model this heterophily by

learning a compatibility matrix [42], they require dense, representative training data to learn these complex class

correlations.

Furthermore, the representational power of these models is strictly limited by the topological complexity of available

training data. Without datasets that exhibit both the intricate structural-temporal dependencies and the heterophilic

nature of real-world laundering, GNNs cannot be trained or benchmarked robustly.

2.1.3 Class Imbalance in Fraud Detection. A defining characteristic of financial fraud datasets is extreme class imbalance,

in which legitimate transactions substantially outnumber fraudulent ones [24]. This imbalance poses significant

challenges for classification algorithms: due to the dominance of the benign class, optimisation steps tend to correctly

classify the majority while ignoring the minority, causing fraudulent transactions to go undetected [24]. In graph-based

settings, this problem is further compounded during message passing, where the influence exerted by the vast majority

of benign neighbours overwhelms the signal from fraudulent connections, and gradient updates become dominated by

the majority class [43]. Consequently, the model’s ability to learn discriminative patterns for identifying illicit edges is

compromised. While prior work has attempted to mitigate this through techniques such as oversampling (e.g., SMOTE)

or cost-sensitive learning, these approaches often yield increased false positive rates without substantially improving

fraud detection [24], underscoring the need for benchmarks that simulate realistic fraud patterns at scale.

2.2 Fraud Characterization and Pattern Requirements

Money laundering typically follows a three-stage process: placement (introducing illicit funds into the financial system),

layering (obscuring the origin through complex transactions), and integration (re-entering funds into the legitimate

economy) [30]. However, detecting sophisticated schemes requires analyzing the interdependence between structural

characteristics (network topology) and temporal characteristics (timing and frequency) [33]. Existing literature has

identified specific typologies that exhibit these features. We categorize these patterns below to establish the functional

requirements for our generator.

[pp. 4-5] [ref: 2.2.1]

2.2.1 Temporal Dynamics. Certain patterns are defined primarily by transaction timing rather than unique topological

structures. High-Frequency Transactions involve sudden bursts of activity or rapid flow-through that deviate from an

entity’s established history, often involving cash structuring below reporting thresholds [1, 23]. Similarly, synchronised

transactions imply collusion, where seemingly unrelated entities transact (e.g., cash deposits) at nearly the same time to

coordinate a larger transfer [29]. Periodic Transactions attempt to mimic legitimate salary or bill payments but lack a

clear economic purpose for the involved entities [1].

2.2.2 Network Topology Structures. Graph-based detection often seeks specific subgraph patterns. Star Topologies

feature a central node (mule or shell company) interacting with multiple outer nodes, characterized by high in-

degree or out-degree centrality [18]. Cliques represent fully connected subgraphs; 𝑘-cliques (where 𝑘≥4) with

bimodal edge curvature distributions are strong indicators of coordinated rings rather than random chance [17]. Front

Businesses introduce dense connectivity among business accounts, whereby cash deposits are immediately converted

into international transfers [19].

2.2.3 Transaction Chains. Sophisticated layering involves extended transaction chains. U-Turn Transactions create

international loops in which funds leave and return to the originator’s jurisdiction, obscuring the trail [30]. Low-Degree

Path Hopping and Parallel Structures (or Smurfing) involve splitting funds across long chains of intermediaries or

parallel paths to dilute the value of individual transactions before consolidation [18].

2.3 Synthetic Data Generation Methodologies

The legal and privacy barriers surrounding real financial data have necessitated a reliance on synthetic generation

within the Anti-Money Laundering (AML) research community [6, 21]. To contextualize our contribution, we draw on

recent systematic reviews that survey the landscape of synthetic financial data. In an analysis of 72 studies published

since 2018, Meldrum et al. [25] identify a heavy concentration of research on stock market time-series, with transaction

data appearing in only a small fraction of works. This scarcity is corroborated by Motie and Raahemi [26], whose

systematic review of Graph Neural Networks (GNNs) for fraud detection highlights the limited availability of diverse

graph datasets across financial domains and identifies the study of dynamic graphs as a critical research gap. Similarly, a

2025 review by Wilson and Azmani [37] confirms that, although Generative Adversarial Networks (GANs) have become

widely adopted for financial data generation, significant challenges persist, including mode collapse, training instability,

and difficulty capturing competitive market dynamics such as strategic interactions between market participants.

Current approaches can be broadly categorized into two paradigms: Process-Driven (Agent-Based) methods, which

simulate economic behavior from the bottom up, and Data-Driven (Generative) methods, which learn statistical

distributions from seed data.

[p. 5] [ref: 2.3.1]

2.3.1 Process-Driven Approaches (Agent-Based Modeling). Process-driven methods circumvent the need for sensitive

training data by relying on predefined logic and typologies. AMLSim [32] remains among the most widely used

generators for this approach. While it successfully generates valid graph structures with injected patterns, it focuses

primarily on the layering stage and lacks the mechanisms to inject the precise temporal signatures required to benchmark

modern Temporal Graph Networks (TGNs).

AMLWorld [6] improves upon this by employing a “Virtual World” model, where agent actions are governed by

strict, calibrated schedules (e.g., weekly salaries, monthly interest payments) rather than simple stochastic interactions,

thereby capturing temporal regularity in both legitimate and illicit flows. However, unlike AMLSim, AMLWorld is

distributed primarily as a static benchmark dataset rather than an accessible generation tool. This creates a barrier for

researchers who require custom scenarios, as they are restricted to the fixed set of laundering patterns (e.g., fan-in,

scatter-gather) pre-baked into the released data, with no mechanism to programmatically inject novel or evolving

typologies.

The importance of such structural flexibility is underscored by Singh and Best [30], who demonstrate that money

laundering manifests as distinct topological “fingerprints”: specific subgraph patterns that investigators must isolate

from background noise. This observation highlights a critical limitation in current simulation tools: to effectively train

and benchmark detection systems, a generator must be able to explicitly and deterministically inject known topological

patterns, rather than relying on stochastic agents to produce them by chance.

2.3.2 Data-Driven Approaches (Generative AI & Statistical). Data-driven methods attempt to clone the statistical

properties of real datasets. As highlighted by recent surveys, GANs are widely adopted for generative techniques in

finance [37]. Architectures such as CTGAN [40] have shown success in reproducing tabular and time-series distributions.

However, as Wilson and Azmani [37] note, these models struggle with topological integrity in the graph domain and

remain prone to mode collapse when generating diverse transaction patterns. They typically treat transactions as

independent tabular rows, failing to preserve the complex degree distributions of financial networks.

A notable exception to GAN based approaches is SynthAML [21], which employs a statistical approach that uses

Gaussian copulas trained on real banking data. While SynthAML achieves high distributional fidelity to its source,

it inherently suffers from low customizability: it is constrained to the specific view of the single institution used for

training (seed data) and cannot simulate the complex, cross-border flows essential to international AML research.

2.3.3 The Gap: Interdependence of Structure and Time. A synthesis of these reviews reveals a clear dichotomy. Process-

driven tools are structurally valid but operationally limited: either by the rigidity of the codebase (AMLSim) or the

[pp. 5-6] [ref: 3.1]

unavailability of the generator itself (AMLWorld). Conversely, data-driven tools (GANs) offer statistical realism but

suffer from mode collapse and a lack of control over specific typological injections [37].

Table 1. Comparison of synthetic financial transaction generators. Unlike predecessors that offer either fixed patterns (AMLSim) or statistical approximations (SynthAML), Tide provides a dual capability: it is preloaded with a library of complex, well-researched typologies (e.g., U-Turns, Smurfing) while simultaneously allowing the programmatic injection of novel, user-defined patterns.

Feature AMLSim [32] AMLWorld [6] SynthAML [21] Tide (Ours)

Core Approach Agent-Based Virtual World Agents Statistical (Copulas) Pattern Injection

Executable Generator ✓ ✗ ✗ ✓

Pre-loaded Pattern Library ✓1 ✓1 ✗ ✓2

Custom Pattern Injection ✗ ✗ ✗ ✓

Precise Temporal Control ✗ ✗ ✗ ✓

Zero-Shot (No Real Data) ✓ ✓ ✗ ✓

1 Basic Library: Limited to standard, structural-only shapes. 2 Complex Library: Includes advanced spatio-temporal schemes derived from literature.

Motie and Raahemi [26] conclude that tackling the dynamic, time-evolving nature of fraud graphs is a critical future

direction for the field. Tide addresses this gap by providing an open, executable framework that enables the explicit

injection of patterns defined by both network topologies and precise temporal constraints, thereby bridging the divide

between structural validity and temporal complexity. Consequently, it achieves this by providing a library of complex

typologies found in the literature [1, 3, 7, 18, 19] while supporting the fully custom injection of user-defined constraints.

3 Research Methodology

3.1 Overview

When performing this research, we adopted an iterative, feedback-driven development lifecycle. As illustrated in

Figure 1, the process consisted of four phases structured around an optimization loop:

(1) Typological Abstraction: We created injection rules by abstracting structural and temporal constraints from

regulatory literature and AML case studies.

(2) Generative Framework Design: These rules were formalized into the Tide generator, which injected specific

fraud topologies into a background of statistically calibrated legitimate activity.

(3) Optimization Loop: This phase constituted the core refinement cycle. We generated provisional datasets and

subject them to a diverse committee of baseline detection models. We utilize the Youden Index [15] (𝐽) to

determine the decision threshold for each classifier, ensuring that performance is benchmarked at the point

that maximizes the separation between legitimate and illicit distributions.

(4) Calibration & Refinement: Based on the detection feedback, we adjusted the generator’s difficulty parameters

while strictly enforcing statistical invariants. The Area Under the Precision-Recall Curve (PR-AUC) served

[pp. 6-7] [ref: 3.2]

as our primary difficulty gauge, as it is robust to the extreme class imbalance inherent in financial fraud. If

patterns were detected with trivial ease (e.g., PR-AUC > 0.90), we could introduce higher temporal variance

or topological camouflage; if they were undetectable (approaching the random baseline), we could relax the

constraints. This cycle was repeated until the datasets exhibited realistic detection complexity that challenges

classifiers while remaining solvable.

Once the generator is calibrated, we proceed to the final comparative benchmarking (Section 5.2.3), where the tool is

evaluated against state-of-the-art baselines.

1. Pattern Research (Typology Abstraction)

2. Generator Design (Graph Modelling)

Calibrate parameters

Final Benchmarking

4. Adversarial Evaluation (ML Detection Tests)

3. Synthetic Generation (Data Production)

(Paper Results)

Fig. 1. The iterative research methodology. The process employs an adversarial feedback loop where generator parameters (Phase 2) are recalibrated based on the performance of detection models (Phase 4).

3.2 Data Modelling and Typology Formalization

To ensure the generated datasets accurately reflect the complexity of financial crime, we first established a robust data

model. We represented the financial domain as a heterogeneous, directed graph comprising multiple entities. Following

this modelling phase, we conducted a review of regulatory reports [1, 7] and academic literature [3, 17, 23, 29, 30] to

identify recurring laundering typologies.

We then mapped these qualitative descriptions into executable constraints. To guarantee the topological integrity of

the identified schemes, we generate the fraud schemes in isolation. In this hierarchical process, distinct laundering

patterns are instantiated first to strictly enforce their structural and temporal requirements. Subsequently, a background

generation process simulates general financial traffic, enveloping the fraudulent entities in noise. To formalize these

descriptions, we represent each money-laundering pattern as a tuple 𝑃= (𝑆,𝑇):

• The Structural Component (𝑆) defines the criteria for selecting the entities that will participate in the pattern

instance. It acts as a query to find nodes with specific attributes from the pre-computed clusters.

• The Temporal Component (𝑇) defines the sequence of transactions between the selected entities, including

their timing, amounts, and other edge attributes.

3.3 Validation Framework and Iteration

We define a two-stage validation process to assess the quality and utility of the generated datasets.

Structural Validation. This phase verifies that the generated graph topology and transaction patterns strictly adhere

to their formal definitions and user configurations. It confirms that the selected entities satisfy pattern-specific criteria

and that transaction sequences comply with the defined temporal constraints.

Machine Learning Model Performance Evaluation. This phase assesses the dataset’s practical utility by training a

selection of detection models on the generated data. The objective is twofold: to ensure that embedded patterns are

[pp. 7-9] [ref: 3.4]

realistic enough to be detectable yet subtle enough to pose a non-trivial challenge for money laundering detection.

Additionally, this process established a feedback loop in which early experimental results guided refinements to the

generation logic to enhance data realism.

3.4 Performance Assessment Metrics

To evaluate machine learning model performance on the generated datasets, we employ standard binary classification

metrics that facilitate direct comparison with established benchmarks, specifically AMLWorld [6], while including

supplementary measures for robustness. To ensure reported metrics reflect each model’s maximum potential effectiveness

rather than an arbitrary probability cut-off, we determine classification thresholds using Youden’s 𝐽statistic (Equation 1),

which identifies the point that maximizes separation between the legitimate and illicit class distributions. This threshold-

selection approach makes performance metrics invariant to class prevalence, providing a fair comparison across datasets

with varying imbalance ratios.

𝐽= Sensitivity + Specificity −1 = Recall + (1 −FPR) −1 (1)

The following metrics are reported:

• F1-Score (at Youden Index): The harmonic mean of precision and recall, adopted as the primary metric to align

with AMLWorld benchmarks.

• Precision (at Youden Index): The proportion of flagged transactions that are truly illicit, reflecting investigative

efficiency. High precision minimizes false positives, reducing the operational burden of reviewing legitimate

transactions.

• Recall (at Youden Index): The proportion of illicit transactions successfully identified, capturing detection

coverage. High recall ensures fewer illicit flows escape detection.

• PR-AUC: Provides rigorous assessment under extreme class imbalance, sensitive to false positives, and reflecting

the operational cost of false alarms.

4 Synthetic Dataset Generation

This section presents Tide, our synthetic data generator designed to address the scarcity of high-quality, accessible

datasets for Anti-Money Laundering (AML) research. Unlike existing generators that often prioritize network topology

over precise transaction sequences, Tide explicitly models both the structural and temporal characteristics of financial

crime. The system creates directed, heterogeneous graphs containing both legitimate economic activity and injected

fraud patterns, providing a ground truth for training and benchmarking supervised detection models.

4.1 Guiding Principles and Design Goals

To effectively model these laundering typologies, the architecture of Tide was developed to meet four functional

requirements. These goals address specific limitations found in existing synthetic data tools:

Temporal Representation. The generator must model the temporal aspects of money laundering. Many schemes are

defined by the sequence, timing, and frequency of transactions. Therefore, the system needs to support time-ordered

interactions.

Complex Structural Patterns. The generator needs to create patterns based on both structural and temporal character-

istics. The implementation has to account for the attributes of the entities involved, allowing patterns to be defined by a

combination of who is transacting and how their profiles contribute to the scheme’s logic.

Customisability. To be a useful research tool, the generator needs to be highly configurable. This includes control


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Tide: A Customisable Dataset Generator for Anti-Money Laundering Research" (2026-02-03). https://arxiv.org/abs/2603.01863
