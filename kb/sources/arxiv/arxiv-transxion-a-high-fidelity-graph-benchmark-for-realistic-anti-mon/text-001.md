---
type: Source Text
title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering - part 1 of 3 (pp. 1-6)'
description: 'Verbatim extracted text, pp. 1-6: Zaiyuan Chen; Zaiyuan Chen > Abstract; Zaiyuan Chen > CCS Concepts; and 10 more sections'
resource: https://arxiv.org/abs/2604.17420
tags:
- academic_finding
- customer_risk
- datasets_benchmarks
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-transxion-a-high-fidelity-graph-benchmark-for-realistic-anti-mon
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-04-19'
legal_status: unknown
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T14:32:20Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T14:32:20Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.17420
  title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2026-04-19T00:00:00Z'
---

# TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2026-04-19), part 1 of 3, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Keyang Chen∗ Fudan University Shanghai, China chenky25@m.fudan.edu.cn

Yongsheng Zhao

Mingxuan Jiang∗ Fudan University Shanghai, China mxjiang24@m.fudan.edu.cn

Fudan University Shanghai, China zhaoys25@m.fudan.edu.cn

Zeping Li Fudan University Shanghai, China zepingli23@m.fudan.edu.cn

Weiqi Luo Fudan University Shanghai, China wqluo25@m.fudan.edu.cn

## Zaiyuan Chen


Fudan University Shanghai, China zaiyuanchen25@m.fudan.edu.cn

Zhixin Li Sen Liu Fudan University Fudan University Shanghai, China Shanghai, China lizhixin@fudan.edu.cn senliu@fudan.edu.cn Guangnan Ye† Xihong Wu Fudan University Peking University Shanghai, China Beijing, China yegn@fudan.edu.cn wxh@cis.pku.edu.cn

Yinan Jing Fudan University Shanghai, China jingyn@fudan.edu.cn

Fudan University Shanghai, China senliu@fudan.edu.cn

Hongfeng Chai Fudan University Shanghai, China hfchai@fudan.edu.cn

### Abstract


structure. Across a diverse array of detection models spanning multiple algorithmic paradigms, TransXion yields substantially lower detection performance than widely used benchmarks, demonstrating increased difficulty and realism. TransXion provides a more faithful testbed for developing context-aware and robust AML detection methods. The dataset and code are publicly available at https://github.com/chaos-max/TransXion.

Money laundering poses severe risks to global financial systems, driving the widespread adoption of machine learning for transaction monitoring. However, progress remains stifled by the lack of realistic benchmarks. Existing transaction-graph datasets suffer from two pervasive limitations: (i) they provide sparse nodelevel semantics beyond anonymized identifiers, and (ii) they rely on template-driven anomaly injection, which biases benchmarks toward static structural motifs and yields overly optimistic assessments of model robustness. We propose TransXion, a benchmark ecosystem for Anti-Money Laundering (AML) research that integrates profile-aware simulation of normal activity with stochastic, non-template synthesis of illicit subgraphs.TransXion jointly models persistent entity profiles and conditional transaction behavior, enabling evaluation of "out-of-character" anomalies where observed activity contradicts an entity’s socio-economic context. The resulting dataset comprises approximately 3 million transactions among 50,000 entities, each endowed with rich demographic and behavioral attributes. Empirical analyses show that TransXion reproduces key structural properties of payment networks, including heavy-tailed activity distributions and localized subgraph

### CCS Concepts


- Computing methodologies → Modeling and simulation ;

- Artificial intelligence ; • Applied computing → _Economics_ .

Anti-Money Laundering, Transaction Monitoring, Synthetic Data Generation, Financial Networks, Anomaly Detection.

Keyang Chen, Mingxuan Jiang, Yongsheng Zhao, Zeping Li, Zaiyuan Chen, Weiqi Luo, Zhixin Li, Sen Liu, Yinan Jing, Guangnan Ye, Xihong Wu, and Hongfeng Chai. 2026. TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering. In _Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’26), August 09–13, 2026, Jeju Island, Republic of Korea._ ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3770855.3817550

### Keywords


#### ACM Reference Format:


∗Both authors contributed equally to this research.

†Corresponding authors.

This work is licensed under a Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License.

_KDD ’26, Jeju Island, Republic of Korea_

© 2026 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-2259-2/2026/08 https://doi.org/10.1145/3770855.3817550

Money laundering is the process of disguising the origins of illegally obtained funds to integrate them seamlessly into the global economy[25]. Despite extensive regulatory interventions, the global scale of money laundering remains immense, with conservative estimates situating the volume between 2% and 5% of global GDP [22]. This massive scale creates systemic risks beyond individual crimes,

### 1 Introduction


[p. 2]

Figure 1: Limitations of prior AML benchmarks versus TransXion. Prior benchmarks use edge-only logs and motif-based injection, whereas TransXion combines profile-rich entities with adaptive anomaly synthesis for contextual detection.

which undermines financial integrity, distorts investment decisions, and can destabilize macroeconomic conditions [14, 26, 28].

To counter these systemic threats, regulatory bodies and financial institutions are intensifying Anti-Money Laundering (AML) efforts by augmenting traditional rule-based frameworks with machine learning-driven transaction monitoring. However, real transaction data are rarely shareable at scale due to legal, privacy, and confidentiality constraints, and labels are sparse and incomplete because many laundering activities remain undetected and verification requires expert investigation. As a result, high-fidelity data synthesis has become essential for developing and benchmarking data-driven AML methods [3, 17]. In practice, existing benchmarks share a common data organization where transactions are natively recorded as relational event logs. These logs can be cast as a directed multigraph to expose higher-order behavioral patterns exemplified by temporal cascades and localized subgraph motifs[21]. However, existing benchmarks fail to capture the complex integration of semantic context and transactional topology inherent in financial networks, primarily due to two pervasive limitations:

(i) Limited Node-Level Context: In operational AML, effective detection depends not only on transactional topology but also on whether behaviors align with customer profiles under Know Your Customer (KYC) standards [5, 15]. However, most public benchmarks are constructed as edge-centric event logs, where nodes are either anonymized or limited to categorical identifiers [3]. In rare cases where node features exist, they are often embedded representations lacking semantic interpretability, making compliance auditing and model accountability difficult [24]. Without structured entity context, models are prone to overlook "out-of-character" behaviors—transactions that deviate from an entity’s expected socioeconomic profile but appear plausible in isolation.

(ii) Template-Driven Anomaly Injection: Illicit activity in existing benchmarks is frequently generated by instantiating a restricted set of predefined templates. Under this paradigm, prior works typically synthesize suspicious flows by explicitly manually prescribing sequential laundering stages or by replicating an enumerated set of static graph motifs [3, 21]. While practical, such reliance on fixed templates restricts benchmarks to predictable patterns. This can overestimate models’ robustness: models may perform strongly on these benchmarks yet fail to capture diverse and adaptive laundering strategies encountered in real-world AML.

To address these limitations, we introduce TransXion , a profilerich transaction-graph benchmark built as an end-to-end synthesis and evaluation ecosystem. TransXion follows a simple three-step pipeline: (i) a normal backbone that jointly generates structured entity profiles and a time-ordered transaction stream; (ii) anomaly synthesis that derives illicit clusters by controlled structural and temporal edits on real illicit subgraphs under budget limits; and (iii) profile-conditioned embedding that inserts each illicit cluster as an intact subgraph by aligning anomalous roles to compatible entities and feasible time windows. The resulting dataset contains roughly _3M transactions_ among _50K entities_ , with semantically meaningful metadata per entity to support evaluation beyond edge-only logs, including detection of _profile-violating_ behaviors. We validate TransXion by matching key stylized properties of payment networks, preserving extreme class imbalance, and demonstrating that template-based baselines can mask performance gaps. Overall, TransXion provides a practical benchmark for developing and stress-testing deployable and auditable AML monitoring under realistic constraints. Our contributions can be summarized as follows:

- The First Profile-Rich Transaction Benchmark: We introduce TransXion, the first large-scale transaction-graph benchmark that integrates approximately 3 million transactions with rich semantically meaningful entity profiles. By providing structured demographics and behavioral metadata, TransXion enables evaluation of AML models conditioned on realistic customer context, filling a critical gap in existing edge-only datasets.

- Non-Template Anomaly Synthesis: We propose a novel generation framework that replaces rigid template-driven motifs with perturbation-based synthesis. By injecting diverse anomalies derived from real illicit subgraphs under budget constraints, our framework mitigates benchmark bias toward a set of predefined templates, providing a stronger stress test for detectors.

- Multi-dimensional Fidelity and Utility Analysis: We evaluate TransXion along two axes: fidelity, via structural and distributional diagnostics, and utility, via downstream illicit-transaction detection. The results show that TransXion preserves realistic graph signatures while providing a more challenging benchmark than existing alternatives.

### 2 Related Work


[pp. 2-3]

Public AML datasets and benchmarks. Real financial transaction data are rarely shareable at scale due to privacy, regulatory, and commercial constraints, and even anonymized records often

Figure 2: Overview of the TransXion generation framework. Normal transactions are generated by an agent-based backbone that jointly simulates entity profiles, temporal activity, and network interactions in a closed loop. Realistic illicit behaviors are then synthesized via interpretable perturbations on extracted laundering subgraphs, guided by an adversarial monitor, and embedded back into the normal backbone under structural, profile, and temporal constraints.

lack complete and reliable ground truth because many illicit activities remain undiscovered. As noted in prior work, “there are no real public data sets that can be used to investigate and compare anti-money laundering (AML) methods in banks”, and this severe confidentiality barrier limits research on core AML challenges such as extreme class imbalance and model interpretability [17]. As a result, only a small number of public benchmarks are available for method development and evaluation.

The Elliptic dataset, a partially labeled Bitcoin transaction graph with around 200K nodes and handcrafted features, has become a widely used benchmark for AML research. However, only a minority of its transactions are annotated as licit or illicit, and the illicit portion is extremely small, which restricts the reliability of supervised evaluation [30]. For traditional finance, benchmarks such as T-Finance simulate bank transaction networks with anonymous account nodes described by a limited set of behavioral attributes [24]. While such datasets enable controlled experimentation, they provide little semantic information about the underlying entities and their socio-economic roles.

More recent public benchmarks have begun to rely on fully synthetic transaction data to increase scale and labeling coverage. For instance, SAML-D provides millions of generated transactions spanning a range of laundering typologies, extending beyond the limited labeled scope of earlier datasets [21]. Nevertheless, despite differences in scale and construction, public benchmarks share limitations: they primarily expose transaction-level or topological

information, offer sparse or no entity-level semantic context, and abstract away the long-term monitoring setting faced in operational AML systems. Consequently, while these benchmarks are valuable for demonstrating algorithmic feasibility, they remain insufficient to represent the rich entity context and evolving behavioral semantics required for realistic AML risk assessment.

Synthetic data generation for AML. To overcome the limited availability of shareable transaction data and the scarcity of reliable labels, AML research has increasingly relied on simulation and synthesis frameworks to construct controllable, fully annotated transaction networks. Early benchmarks such as PaySim [19] and AMLSim [29] adopt agent-based simulation: they generate routine customer activities according to predefined behavioral rules and inject canonical laundering motifs (e.g., fan-in/fan-out or smurfing) to create labeled anomalies. This paradigm enables reproducible experimentation under known ground truth and has played an important role in establishing initial baselines.

[pp. 3-4]

However, these early generators typically depend on a small set of manually specified templates, restricted transaction types, and simplified institutional assumptions. Such design choices limit the diversity of emergent abnormal patterns that depart from operational banking environments, where laundering strategies are heterogeneous and adaptive rather than fixed. Consequently, performance gains on these benchmarks may primarily reflect a model’s ability to recognize injected motifs, rather than its capacity to generalize to unseen or evolving illicit behaviors.

Recent work has sought to improve realism by expanding the synthetic domain or incorporating empirical distributions. For instance, AMLWorld [3] constructs multi-bank, multi-currency virtual environments and simulates a broader range of laundering stages while preserving extreme class imbalance observed in practice. Datadriven approaches such as SynthAML [17] fit probabilistic models to real-bank statistics to generate large-scale transaction streams with labeled alerts. These advances substantially enhance fidelity at the level of marginal topology and temporal patterns, and reduce the gap between synthetic and real transaction dynamics.

Despite improved realism, many synthetic benchmarks remain template-centric and evaluate models on predictable injected motifs, which can overstate robustness. In addition, they rarely enforce joint consistency across entity context and temporal behavior, limiting the study of out-of-character laundering. This motivates benchmarks that integrate rich entity profiles with non-template, controllable anomalies and evaluation protocols aligned with operational monitoring.

### 3.1 Normal-Transaction Simulation Backbone


[p. 4]

Most transaction-graph benchmarks release edge-only logs, which removes the entity context needed to evaluate whether activity deviates from an entity’s profile. Post hoc attributes cannot recover this coupling because identity and behavior co-evolve through interaction history. We therefore build an agent-based backbone that generates profiles and transactions jointly in a closed loop. Concretely, in each one-hour window we (i) sample initiators, (ii) sample counterparties, (iii) sample event attributes, and (iv) update the interaction state for the next window.

Profile-grounded behavior for individual consistency. Each entity is initialized with a persistent, semantically meaningful profile that constrains both its activity propensity and attribute ranges. For accounts, profiles include socio-economic attributes and behavioral priors such as daily intensity, typical amount scale, and diurnal rhythms; for merchants, they include business type and operating scale. Operationally, profiles parameterize the per-window activation probability and the attribute samplers, so per-entity behavior stays stable and auditable, while still allowing _out-of-character_ deviations to be defined relative to profile expectations.

Scenario modulation for macro-level variation. To capture low-frequency shifts such as holidays or regional demand changes, we add a lightweight scenario controller that updates at a fixed daily cadence. Each day it outputs a small set of multiplicative modifiers, including a global intensity factor and region-level mixing weights. These modifiers only affect aggregate volume and regional composition; they do not specify individual events or override profile-driven micro behavior. Fixing the update granularity and the affected variables makes the macro layer reproducible and prevents unconstrained tuning.

Socially structured sampling for realistic graph topology. Within each hourly window, initiators are sampled proportional to profile-derived activity weights to reflect heterogeneous participation. Counterparties are then selected by combining four terms: locality preference, time-decayed interaction memory, merchant attractiveness, and limited exploration for new ties. In minimal form,

this is a weighted mixture over candidate counterparties, where the memory term is updated from past interactions and decays with time. This yields heavy-tailed participation and non-trivial clustering patterns, while keeping amounts and other attributes consistent with the initiator profile.

Evolving interaction state for temporal stability. We maintain an interaction state that summarizes recent history and feeds back into future sampling. The state stores time-decayed partner preferences and region hotspots, and it is updated after each hourly window. This creates path dependence: repeated ties become more likely, but new links still emerge stochastically. As a result, the generated graphs exhibit temporal persistence and stable diurnal structure, alongside heavy-tailed activity patterns observed in empirical financial networks and interbank transaction systems [3].

### 3.2 Anomalous Transaction Synthesis


To generate diverse and adaptive money laundering behaviors, we synthesize anomalies by applying controlled, interpretable edits to realistic illicit transaction subgraphs. Each edit preserves basic transaction sanity, including valid endpoints, non-negative amounts, and a consistent time order. We define a compact action space with four operation families: Intermediary Injection inserts additional intermediate accounts to lengthen transaction chains and obscure direct fund provenance; Account Merging consolidates behaviorally similar accounts to reduce redundant structures and mask repetitive patterns; Account Splitting disperses transaction flows across multiple recipients to dilute concentrated signals that commonly trigger detection heuristics; and Transaction Adjustment perturbs transaction amounts or timestamps within feasible ranges to break exploitable regularities while remaining consistent with surrounding activity.

While these operations provide the necessary tools, the core challenge lies in selecting the optimal edit sequence to bypass detection. To address this, we frame the synthesis as an adversarial process guided by a pre-trained monitor. The synthesis agent proposes edits for each illicit cluster, while the monitor scores results to encourage modifications that reduce detectability without sacrificing operational plausibility. To bridge the gap between static edits and dynamic strategy, we formulate operation selection as a constrained sequential decision process, refining the agent through a lightweight iterative optimization loop driven by the monitor’s feedback. This allows the agent to discover sophisticated, multistep evasion patterns that are difficult to capture through simple heuristic rules. Further details are in Appendix A.

### 3.3 Anomaly-to-Normal Embedding


[pp. 4-5]

To prevent injection artifacts, we avoid naive placement and instead embed synthesized clusters as intact subgraphs into the normal backbone. Our objective is to preserve the illicit semantics characterized by internal flow topology and temporal ordering, while ensuring operational feasibility within the normal account space. Crucially, labels are transferred along fund traces during embedding, so that illicitness is preserved by construction.

The embedding is accepted only if it satisfies three constraints: (i) Structural Preservation: preserve all sender–receiver pairs under a one-to-one mapping of cluster participants; (ii) Profile

Gender Age Education Marital Status Occupation36-45 retiredbachelor's degreemarried25-35 otherMale 46-55 associate degree blue-collar workerbusiness owner56-65>65 below high schoolgraduate degree or higher divorcedwhite-collar workerfreelancerstudent25-35 associate degree othermarriedFemale 36-45 bachelor's degree white-collar workerblue-collar worker46-55 high school single unemployed56-65>65 below high schoolgraduate degree or higher divorced business ownerfreelancerstudent

Figure 3: Entity profile co-occurrence in TransXion. Sankey diagram of joint distribution of account-holder attributes.

Alignment: match each anomalous role to a normal account whose profile-consistent activity regime falls within the role’s required range; (iii) Temporal Coherence: place the cluster into a feasible time window while preserving all intra-cluster sequencing.

We adopt an atomic injection policy, rejecting any cluster that violates these constraints to maintain semantic integrity. At the dataset level, we verify that the augmented backbone preserves key stylized properties, such as heavy-tailed activity statistics. These properties are empirically verified in our experiments. Overall, this embedding balances structural preservation with contextual feasibility, ensuring the benchmark evaluates structure-aware illicit patterns rather than artifacts of injection.

### 4 Proposed Datasets


[p. 5]

The TransXion Dataset . We introduce TransXion , a relational dataset generated by our framework that contains 3 million transactions among 50,000 entities and is organized into _Persons_ , _Merchants_ , and _Transactions_ .TransXion tightly couples transaction-network topology with rich semantic context: the entity tables provide structured profiles linked to unique accounts. Figure 3 visualizes the co-occurrence structure of these profile attributes, illustrating the rich and heterogeneous diversity of account contexts available for learning. Detailed statistical characterization and distribution analyses are provided in Appendix B.

This section provides a comprehensive empirical evaluation of TransXion from two complementary perspectives: structural fidelity to stylized facts of transaction networks and utility as a challenging benchmark for illicit-activity detection. Accordingly, we organize our analysis around two research questions. RQ1 (Fidelity). To what extent do the statistical properties and graph invariants of TransXion align with patterns documented in real-world payment systems?

### 5 Experiments


RQ2 (Detection Hardness). To what extent does TransXion increase the difficulty of illicit-transaction detection relative to established benchmark datasets?

_Experimental Protocol._ To evaluate both generative fidelity and benchmark utility, we represent the transaction data in two complementary forms. For structural invariants (RQ1), we project the transactions into an undirected simple graph, allowing us to measure stable topological signatures such as connectivity, transitivity, and core-periphery structures. For illicit detection tasks (RQ2), we preserve the full granularity of the data using a directed, weighted temporal multigraph, enabling models to learn from both flow directionality and temporal dynamics.

### 5.1 Experimental Setups


_Baselines._ We evaluate our benchmark against three established synthetic transaction datasets, each representing a different generation of modeling approaches:

AMLSim [29]: A synthetic transaction dataset generated by a multi agent simulation framework. It provides account level transactions together with injected illicit activity patterns and has been used in prior work as a standard synthetic benchmark.

AMLWorld [3]: An agent-based synthetic financial transaction generator that builds a multi-agent virtual world with both legitimate and criminal agents, producing realistic, standardized AML datasets at large scale and providing complete laundering labels and pattern annotations for benchmarking AML detection models. SAML-D [21]: A synthetic AML transaction monitoring dataset generated by an enhanced transaction simulation framework. It contains millions of tabular transaction records annotated with 11 normal transaction types and 17 suspicious typologies.

### 5.2 Fidelity of Statistical Properties and Graph Invariants


[pp. 5-6]

Following Soramäki et al. [23], we construct daily directed transaction networks and evaluate fidelity by checking whether TransXion reproduces stable regularities of transaction graphs at both the global topology level and the distributional tail level. For comparability across datasets, we compute graph invariants on daily undirected projections and report results as mean ± std. Furthermore, tail diagnostics are reported on aggregated distributions using a consistent selection rule.

_Macro-topology: Backbone Connectivity and Fragmentation._ Empirical literature show that payment networks are sparse yet dominated by a large connected backbone [7, 12]. Motivated by this evidence, we quantify macro-level integration using the giant connected component ratio. As shown in Table 1, TransXion preserves an integrated daily topology with a mean GCC ratio of 0 _._ 8924 ± 0 _._ 0321, avoiding the excessive fragmentation observed in some baselines. Such structural integrity is important for downstream utility, since it enables large-scale information diffusion and contagion-style propagation over realistic payment backbones [1, 2]. Accordingly, TransXion provides a more faithful substrate for graph learning, where models operate on globally connected transaction networks rather than fragmented components.

Table 1: Comparison of graph invariants and tail diagnostics. Invariants are reported as mean ± std over daily projections. Tail diagnostics use MLE-based fitting with automatically selected _𝑥_ min [10]. Strength and Amount denote node transaction volume and individual transaction values, respectively. Parenthetical values indicate ( _𝑥_ min | _𝑛_ tail ) .

[p. 6]

|Indicator|Ours|AMLWorld|AMLSim|SAML-D|
|---|---|---|---|---|
|GCC ratio|0.8924±0.0321|0.3824±0.3373|0.8355±0.0130|0.0009±0.0001|
|Number of Connected Components|308.5±49.7|24,102.7±41,639.3|389.5±24.7|9,624.9±461.9|
|Max_𝑘_-core|2.9151±0.4264|1.8333±0.7638|2.93±0.2551|1.0000±0.0000|
|Max-core fraction|0.0703±0.0875|0.4581±0.4456|0.0602±0.0616|1.0000±0.0000|
|Degree assortativity|-0.4943±0.0279|-0.2593±0.2817|-0.2009±0.0114|-0.1188±0.0048|
|Global Transitivity|0.0021±0.0005|0.0007±0.0028|0.0012±0.0002|0.0000±0.0000|
|Strength-tail KS_𝐷_(_𝑥_min |_𝑛_tail)|0.0570 (120.8k | 20.0k)|0.0204 (531.0M | 5.2k)|0.1046 (21.5M | 4.4k)|0.0445 (80.6k | 402.1k)|
|Amount-tail exponent_𝛼_(_𝑥_min |_𝑛_tail)|2.9255 (40.3k | 30.3k)|1.5423 (623.8k | 253.9k)|1.3267 (85.5k | 26.5k)|3.0000∗(10.2k | 2,471.3k)|

∗ Indicates reaching the boundary of the powerlaw fitting range (typically _𝛼_ ∈[1 _,_ 3]).

_Triadic Closure and Localized Structure._ Real interbank and moneymarket networks typically exhibit low clustering, yet still show non-trivial local closure attributable to repeated relationships and market segmentation [7, 8]. We quantify this via undirected transitivity, representing the fraction of closed triplets among all connected triplets. On daily graph projections, TransXion yields a transitivity of 0 _._ 0021 ± 0 _._ 0005, consistent with sparse closure in common benchmarks. This demonstrates that TransXion captures the subtle yet essential signature of localized closure, maintaining the cohesive community structures found in real-world financial interactions. Such structural fidelity yields a meaningful topology in which graph-based models can learn local relational patterns, whereas overly fragmented environments often eliminate these closure signals and render such learning ineffective.

_Tiering, Mixing Patterns, and Structural Hierarchy._ A defining feature of financial networks is a tiered architecture, where central institutions intermediate flows for a wide periphery [4]. Such structures are typically characterized by disassortative mixing, where high-degree hubs connect disproportionately to low-degree peripheral nodes. Table 1 shows that TransXion exhibits a pronounced negative assortativity coefficient of −0 _._ 4943, consistent with huband-spoke intermediation [20]. We further probe hierarchical depth via _𝑘_ -core decomposition. TransXion attains a maximum core number of 2 _._ 9151, indicating a multi-layered core structure compared to shallower baselines. In contrast to the degenerate 1-core structures found in simpler baselines, TransXion provides the necessary topological depth to evaluate detection models against sophisticated, multi-stage financial interactions.

_Heavy Tails and Economic Plausibility of Flows._ Heavy-tailed distributions are ubiquitous in financial systems, particularly for exposure proxies such as node transaction volume and transfer amounts [16]. We assess tails using MLE-based fitting with an automatically selected lower cutoff _𝑥_ min following standard practice [10]. Under this protocol, TransXion exhibits a low strength-tail KS distance and an amount-tail exponent in a plausible range, indicating that the tail behavior is both heavy-tailed and statistically coherent. Overall, these diagnostics support that TransXion better

Table 2: Illicit-transaction detection performance using GBT baselines. For each detector, the lowest values are bolded and the second lowest values are underlined.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering" (2026-04-19). https://arxiv.org/abs/2604.17420
