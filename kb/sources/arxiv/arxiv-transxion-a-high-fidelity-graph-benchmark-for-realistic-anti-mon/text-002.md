---
type: Source Text
title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering - part 2 of 3 (pp. 6-10)'
description: 'Verbatim extracted text, pp. 6-10: Zaiyuan Chen > 5.2 Fidelity of Statistical Properties and Graph Invariants; Zaiyuan Chen > 5.3 Detection Hardness and Benchmark Utility; Zaiyuan Chen > 6 Conclusion; and 2 more sections'
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
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.17420
  title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2026-04-19T00:00:00Z'
---

# TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2026-04-19), part 2 of 3, pp. 6-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Zaiyuan Chen


### 5.2 Fidelity of Statistical Properties and Graph Invariants


[p. 6]

|Dataset|Metric|GBT Det|ectors|
|---|---|---|---|
|||LightGBM|XGBoost|
||AUC|0.4906|0.9931|
|AMLSim|AP|0.2035|0.9206|
||F1|0.3598|0.9171|
||AUC|0.8549|0.9631|
|AMLWorld|AP|0.1369|0.3761|
||F1|0.2569|0.4046|
||AUC|0.7906|0.8521|
|SAML-D|AP|0.1361|0.2436|
||F1|0.2654|0.1872|
||AUC|0.4128|0.7869|
|TransXion|AP|0.0313|0.1716|
||F1|0.1383|0.2375|

captures economically grounded flow heterogeneity while avoiding pathological tail behavior.

_Summary for RQ1._ Across macro connectivity, meso-scale tiering, and tail behavior, TransXion exhibits a consistently realistic structural profile that aligns with multiple stylized facts of operational payment networks. Across the compared benchmarks, we observe different emphases and trade-offs in connectivity, core–periphery organization, and tail regimes; in contrast, TransXion maintains a balanced combination of backbone connectivity, hierarchical depth, and economically plausible flow heterogeneity. Under this balance, TransXion offers a transaction graph that enables meaningful detection evaluation while retaining the topological richness required for effective graph-based learning.

### 5.3 Detection Hardness and Benchmark Utility


[pp. 6-7]

In this section, we evaluate the downstream utility of TransXion as a rigorous testbed for illicit activity detection. A robust benchmark

Table 3: Illicit-transaction detection performance comparison. For each detector, the lowest values are bolded and the second lowest values are underlined, highlighting the relative difficulty across benchmarks.

|Dataset|Metric|||GNN Detectors|||
|---|---|---|---|---|---|---|
|||Multi-GIN|Multi-GIN+EU|Multi-PNA|Multi-PNA+EU|Multi-GAT|
||AUC|0.929836|0.931760|0.948663|0.940602|0.931399|
|AMLSim|AP|0.693337|0.728561|0.637610|0.596686|0.458262|
||F1|0.775000|0.802885|0.697337|0.700535|0.486216|
||AUC|0.986481|0.982223|0.982513|0.985354|0.978961|
|AMLWorld|AP|0.638040|0.504771|0.630889|0.672263|0.395064|
||F1|0.636644|0.652040|0.627935|0.709499|0.451544|
||AUC|0.999975|0.999746|0.999934|0.999984|0.999757|
|SAML-D|AP|0.991920|0.991262|0.988842|0.994835|0.971794|
||F1|0.912689|0.937154|0.968137|0.976988|0.939498|
||AUC|0.968837|0.952841|0.968291|0.968088|0.951603|
|TransXion|AP|0.287842|0.268952|0.350831|0.345992|0.277935|
||F1|0.433980|0.424686|0.486515|0.467446|0.433566|

should present a non-trivial environment where detection models cannot achieve high scores through simple structural cues that do not reflect real-world laundering complexity.

[p. 7]

_5.3.1 Hardness Evaluation with Representative Detectors._ We formulate illicit activity detection as a supervised edge-level classification task. For each dataset, we keep the original event granularity as a directed temporal multigraph, where nodes are accounts and edges are timestamped transactions with associated amounts. We retain parallel edges between the same ordered account pair to capture repeated interactions and temporal dynamics. Since several benchmarks provide no node attributes, we train and evaluate all models using edge features only to ensure fair comparison. Each dataset is chronologically split into train, validation, and test sets with a 6:2:2 ratio by timestamp, ensuring that models are trained on earlier transactions and evaluated on later transactions. We report AUC, AP, and F1 on the held-out test set.

_Detection Models._ To evaluate TransXions hardness, we evaluate various representative detection paradigms, including Gradient Boosted Trees (GBTs) and Graph Neural Networks (GNNs).

GBT Detectors. We include gradient-boosted tree models as strong tabular baselines, evaluating LightGBM [18] and XGBoost [9]. Both are trained as standard binary classifiers directly on pertransaction attributes from the event logs. Since they do not leverage graph structure, they serve as a non-graph reference point for assessing the value of relational and multi-hop signals.

GNN Detectors. We evaluate graph neural networks for edgelevel classification on directed temporal multigraphs. We adopt the directed-multigraph framework of Egressy et al. [13] and instantiate Multi-GIN [31] and Multi-PNA [11] backbones, which aggregate incoming and outgoing neighborhoods and support parallel edges. We additionally consider an edge-update variant (+EU) [6] and a Multi-GAT [27] baseline for direction-specific attention. For fair comparison, all GNNs are trained using edge-level attributes only.

_Main Benchmark Results._ Tables 2 and 3 summarize detection performance across tabular and graph-based paradigms on all benchmarks. We highlight two complementary observations: feature-only tabular detectors degrade most on TransXion, and graph-based detectors also show their largest degradation in practical operating performance on TransXion. We analyze these patterns below for GBT and GNN models, respectively.

_GBT: Event-level attributes alone do not support reliable detection under profile-conditioned behavior._ Table 2 shows that gradientboosted tree baselines trained only on per-transaction attributes degrade most severely on TransXion. In particular, LightGBM and XGBoost attain their weakest performance on TransXion, with AP dropping to 0.0313 and 0.1716, indicating that event-log fields and timestamp-derived cues that work well on prior benchmarks become substantially less discriminative. This drop is unlikely to be explained solely by scale or class imbalance, since feature-only models still perform well across metrics on the other benchmarks.

[pp. 7-8]

These observations match our goal of profile-conditioned synthesis: transactions that look similar at the event level can carry different risk depending on the participating accounts. Consequently, event-level features alone are less discriminative, and detection benefits from broader contextual signals, as reflected by the gains observed when profile information is introduced in Sec. 5.3.2.

_GNN: Hardness concentrates in operating-point performance rather than global ranking._ Table 3 shows a consistent pattern across all GNN detectors: TransXion yields the lowest AP and the lowest F1, while its AUC is the second-lowest among benchmarks. This is expected because AUC evaluates pairwise ranking over all positive– negative pairs and is influenced by separability across the entire score distribution. In contrast, AP and F1 are dominated by the highscore region and by thresholded operating points, which better reflect practical alerting under extreme class imbalance.

This perspective also clarifies why AMLSim attains the lowest AUC while maintaining relatively strong AP and F1. AUC penalizes

175 XGBoost AUC 0.30 AUC 0.295 AUCXGBoost AP AP AP150LightGBM AUC 0.25125 LightGBM AP 0.20100 0.15 0.1240.10 0.08575 0.0640.05 0.034 0.046500.00-0.02125 0.05 Ours AMLWorld-0.033 Ours AMLWorld00.00 0.25 0.50 0.75 1.00 XGBoost LightGBMNode Profile Feature RatioRelative Performance Gain (%) Metric (Profile No-Profile)

Figure 4: Sensitivity of XGBoost and LightGBM performance to the fraction of node profiles used during training on TransXion, reported in relative AUC and AP change.

broad overlap between positive and negative score distributions across the full ranking, leading to frequent mis-orderings among randomly sampled pairs. Meanwhile, AP and F1 can remain favorable when positives are sufficiently concentrated among the highest scores, yielding a high-precision region and a viable operating threshold, even if substantial interleaving persists in the midand low-score regions. Therefore, AMLSim may admit reasonable thresholded performance even when the overall score distributions exhibit substantial overlap.

[p. 8]

By comparison, TransXion shifts difficulty toward the decisioncritical region: illicit edges are synthesized to be behaviorally plausible and context-consistent, which increases ambiguity among high-score candidates and suppresses early precision. Consequently, neighborhood aggregation alone does not recover reliable operatingpoint performance. Overall, these results indicate that TransXion reduces shortcut learning from template-like motifs and provides a more demanding evaluation setting.

_5.3.2 Effect of Node-Level Context._ We investigate whether nodelevel semantic context provides measurable utility for illicit transaction detection by comparing profile-blind and profile-aware variants of tabular detectors on both TransXion and AMLWorld. Profileaware models augment transaction features with entity profile attributes, whereas profile-blind models rely solely on edge-level statistics. To assess whether profiles improve a detector’s ranking and retrieval of illicit transactions under varying decision thresholds, we focus on AUC and AP as the primary criteria throughout this section.

_Progressive node-context ablation._ We first perform an ablation on TransXion by gradually increasing the number of available profile attributes used during training. As shown in Fig 4, both XGBoost and LightGBM exhibit consistent performance gains as more node attributes are retained, which indicates that node context provides complementary signal beyond transaction-level features.

_Cross-benchmark gain comparison._ We compare the marginal benefit of adding node-level context across benchmarks. Fig 5 reports the change in ranking and retrieval performance after enabling profile features, measured by ΔAUC and ΔAP relative to profile-blind

Figure 5: Change in AUC and AP after adding node profile features to GBT detectors on TransXion and AMLWorld.

Table 4: Effect of profile-aware node features on GNN detectors on TransXion.

|Setting|Metric|Multi-GIN|Multi-GIN+EU|Multi-PNA|Multi-GAT|
|---|---|---|---|---|---|
|Edge-only|AUC|0.9688|0.9528|0.9683|0.9516|
||AP|0.2878|0.2690|0.3508|0.2779|
||F1|0.4340|0.4247|0.4865|0.4336|
|Profile+Edge|AUC|0.9550|0.9718|0.9759|0.9452|
||AP|0.3173|0.3176|0.3746|0.2916|
||F1|0.4666|0.4660|0.4732|0.4654|

[pp. 8-9]

baselines on TransXion and AMLWorld. The gains are consistently larger on TransXion, with ΔAUC = 0 _._ 085 and ΔAP = 0 _._ 034 for XGBoost, and ΔAUC = 0 _._ 295 and ΔAP = 0 _._ 124 for LightGBM. In contrast, AMLWorld exhibits smaller and model-dependent effects, including slight degradations for XGBoost. This gap indicates that the entity profiles in TransXion provide richer and more predictive semantic context, enabling detectors to better disambiguate transactions that appear similar at the event level and supporting a more rigorous evaluation of semantic consistency reasoning.

_Profile-aware GNN detection._ We further evaluate whether semantic profiles also benefit graph-based detectors. In the profile-aware setting, node attributes are fused with edge-level transaction features before edge classification. As shown in Table 4, adding profile information improves AP for all evaluated GNN backbones and improves F1 for three out of four backbones. This confirms that TransXion’s entity profiles provide useful semantic signals not only for tabular detectors, but also for relational models that jointly encode transaction topology and node context.

_5.3.3 Effect of Anomaly Synthesis Mechanism._ To verify that the increased detection difficulty of our benchmark is not caused by stochastic noise or structural degradation, we conduct a controlled hardening experiment using AMLWorld as a fixed topological substrate. By keeping the underlying graph backbone constant, this design isolates the impact of our synthesis agent and decouples the effect of adversarial optimization from confounding factors such as dataset scale and inherent metadata distributions.

Notably, we deliberately select _AMLWorld_ for this validation rather than our own _TransXion_ backbone to ensure an impartial

Table 5: Ablation of synthesis strategies on the _AMLWorld_ dataset. For each detector, the lowest values are bolded and the second lowest values are underlined

|Configuration|Metric|Multi-GIN|XGBoost|
|---|---|---|---|
||AUC|0.9864|0.9631|
|Original|AP|0.6380|0.3761|
||F1|0.6366|0.4046|
||AUC|0.9841|0.9481|
|LLM-Only|AP|0.5384|0.4008|
||F1|0.5741|0.4573|
||AUC|0.9796|0.9474|
|RL-Optimized|AP|0.5121|0.3276|
||F1|0.5037|0.3849|

[p. 9]

and objective evaluation. By demonstrating that our synthesis agent can successfully "harden" a well-established third-party benchmark, we prove that the observed hardness of TransXion is a universal property of our adversarial framework rather than an artifact of a specific synthetic data distribution. This controlled design, with the AMLWorld backbone held fixed, allows us to directly observe how the optimization procedure reshapes detection boundaries.

We evaluate three graph-level configurations that differ only in whether and how the benchmark has been modified. Original is the released AMLWorld graph in its unmodified form. LLM-Only is a hardened variant produced by an LLM-based synthesis agent without monitor-guided optimization. RL-Optimized is a hardened variant produced by the same synthesis pipeline using an agent whose decision policy is obtained through monitor-guided training, after which the learned policy is used to generate edits.

As summarized in Table 5, the three configurations exhibit a clear progression in detection difficulty. The LLM-Only hardening produces mixed effects: it reduces Multi-GIN performance across metrics, yet it can improve some operating-point metrics for XGBoost, indicating that unguided hardening does not consistently increase difficulty across detector families. In contrast, the RL-Optimized variant yields a consistent degradation for both Multi-GIN and XGBoost, with lower scores across all reported metrics relative to the Original setting. This contrast suggests that monitor-guided optimization is necessary to produce systematic hardening, whereas LLM-only edits can shift the data distribution in ways that are not uniformly adversarial to different model classes. Overall, these results emphasize that the high detection difficulty of TransXion is a deliberate consequence of adaptive adversarial optimization rather than stochastic noise or structural degradation.

_Cross-family transferability._ To examine whether monitor-guided hardening overfits to a specific detector family, we further conduct a cross-family transfer experiment: the synthesis process is guided by a GBT-based monitor, while evaluation is performed using MultiGIN. As shown in Table 6, GBT-guided hardening still substantially degrades Multi-GIN performance, reducing AP from 0.6380 to 0.4297 and F1 from 0.6366 to 0.4807. This degradation is stronger than the LLM-Only variant, suggesting that the generated anomalies are not merely tailored to a specific GNN monitor, but encode transferable challenging patterns across detector families.

Table 6: Cross-family transfer of hardened anomalies. Synthesis is guided by a GBT monitor and evaluated by MultiGIN.

|Configuration|AUC|AP|F1|
|---|---|---|---|
|Original|0.9864|0.6380|0.6366|
|LLM-Only|0.9841|0.5384|0.5741|
|GBT-Guided|0.9738|0.4297|0.4807|

_Summary for RQ2._ Across tabular and graph-based detectors, TransXion provides a more challenging and informative AML benchmark than prior public datasets. Under a unified edge-featureonly protocol, TransXion yields the weakest practical detection performance for both GBT and GNN detectors, especially in AP and F1, which are more relevant to alerting under extreme class imbalance. Adding entity profiles consistently improves detection performance, indicating that TransXion provides predictive semantic context beyond edge-level transaction statistics. Finally, the controlled hardening experiments on AMLWorld show that the increased difficulty is not merely caused by random noise or dataset scale, but is systematically induced by the monitor-guided non-template anomaly synthesis process. Together, these results show that TransXion shifts AML evaluation from shortcut recognition of fixed motifs toward context-aware reasoning over profiles, temporal behavior, and transaction topology.

### 6 Conclusion


We introduce TransXion, a high-fidelity transaction-graph benchmark designed to address two fundamental limitations of existing AML datasets: the lack of rich entity-level context and the reliance on template-driven anomaly injection. By jointly modeling persistent entity profiles, profile-conditioned normal behavior, and adaptive non-template anomaly synthesis, TransXion captures realistic interactions between transactional topology and semantic context that are central to operational AML.

Extensive fidelity analyses show that TransXion preserves key stylized properties of real payment networks, including connected backbones, hierarchical core–periphery structure, disassortative mixing, and economically plausible heavy-tailed behavior. At the same time, detection experiments demonstrate that TransXion is substantially more challenging than widely used benchmarks across both graph-based and feature-based models. The observed performance degradation reflects reduced shortcut learning and increased reliance on contextual reasoning, rather than artifacts of noise or synthetic complexity.

Overall, TransXion provides a more faithful and demanding testbed for developing, evaluating, and stress-testing AML detection methods. We hope this benchmark will support future research on context-aware, robust, and auditable transaction monitoring systems that better reflect the realities of financial crime detection.

### Acknowledgments


[pp. 9-10]

This work was supported by the National Key R&D Program of China (No. 2023YFC3304800) and the National Natural Science Foundation of China (No. 72595845, No. 72595840).

- [1] Daron Acemoglu, Asuman Ozdaglar, and Alireza Tahbaz-Salehi. 2015. Systemic risk and stability in financial networks. _American Economic Review_ 105, 2 (2015), 564–608.

- [2] Franklin Allen and Douglas Gale. 2000. Financial contagion. _Journal of political economy_ 108, 1 (2000), 1–33.

### References


[p. 10]

- [3] Erik Altman, Jovan Blanuša, Luc Von Niederhäusern, Béni Egressy, Andreea Anghel, and Kubilay Atasu. 2023. Realistic synthetic financial transactions for anti-money laundering models. _Advances in Neural Information Processing Systems_ 36 (2023), 29851–29874.

- [4] Kartik Anand, Iman Van Lelyveld, Ádám Banai, Soeren Friedrich, Rodney Garratt, Grzegorz Hałaj, Jose Fique, Ib Hansen, Serafín Martínez Jaramillo, Hwayun Lee, et al. 2018. The missing links: A global study on uncovering financial network structures from partial data. _Journal of Financial Stability_ 35 (2018), 107–119.

- [5] Robert M. Arasa. 2015. Determinants of Know Your Customer (KYC) Compliance among Commercial Banks in Kenya. _Journal of Economics and Behavioral Studies_ 7 (2015), 162–175. https://api.semanticscholar.org/CorpusID:15673285

- [6] Peter W Battaglia, Jessica B Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinicius Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner, et al. 2018. Relational inductive biases, deep learning, and graph networks. _arXiv preprint arXiv:1806.01261_ (2018).

- [7] Morten L Bech and Enghin Atalay. 2010. The topology of the federal funds market. _Physica A: Statistical mechanics and its applications_ 389, 22 (2010), 5223–5246.

- [8] Michael Boss, Helmut Elsinger, Martin Summer, and Stefan Thurner 4. 2004. Network topology of the interbank market. _Quantitative finance_ 4, 6 (2004), 677–684.

- [9] Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A scalable tree boosting system. (2016), 785–794.

- [10] Aaron Clauset, Cosma Rohilla Shalizi, and Mark EJ Newman. 2009. Power-law distributions in empirical data. _SIAM review_ 51, 4 (2009), 661–703.

- [11] Gabriele Corso, Luca Cavalleri, Dominique Beaini, Pietro Liò, and Petar Veličković. 2020. Principal neighbourhood aggregation for graph nets. _Advances in neural information processing systems_ 33 (2020), 13260–13271.

- [12] Ben Craig and Goetz Von Peter. 2014. Interbank tiering and money center banks. _Journal of Financial Intermediation_ 23, 3 (2014), 322–347.

- [13] Béni Egressy, Luc Von Niederhäusern, Jovan Blanuša, Erik Altman, Roger Wattenhofer, and Kubilay Atasu. 2024. Provably powerful graph neural networks for directed multigraphs. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , Vol. 38. 11838–11846.

- [14] Joras Ferwerda. 2013. The effects of money laundering. In _Research handbook on money laundering_ . Edward Elgar Publishing, 35–46.

- [15] Financial Crimes Enforcement Network (FinCEN). 2016. _Frequently Asked Questions Regarding Customer Due Diligence Requirements for Financial Institutions_ . Guidance FIN-2016-G003. U.S. Department of the Treasury. https://www.fincen. gov/system/files/2016-09/FAQs_for_CDD_Final_Rule_%287_15_16%29.pdf Issued July 19, 2016. Interprets the CDD Final Rule and clarifies ongoing monitoring and customer risk profile requirements.

- [16] Xavier Gabaix. 2016. Power laws in economics: An introduction. _Journal of Economic Perspectives_ 30, 1 (2016), 185–206.

- [17] Rasmus Ingemann Tuffveson Jensen, Joras Ferwerda, Kristian Sand Jørgensen, Erik Rathje Jensen, Martin Borg, Morten Persson Krogh, Jonas Brunholm Jensen, and Alexandros Iosifidis. 2023. A synthetic data set to benchmark anti-money laundering methods. _Scientific data_ 10, 1 (2023), 661.

- [18] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. 2017. Lightgbm: A highly efficient gradient boosting decision tree. _Advances in neural information processing systems_ 30 (2017).

- [19] Edgar Lopez-Rojas, Ahmad Elmir, and Stefan Axelsson. 2016. PaySim: A financial mobile money simulator for fraud detection. In _28th European Modeling and Simulation Symposium, EMSS, Larnaca_ . Dime University of Genoa, 249–255.

- [20] Mark EJ Newman. 2002. Assortative mixing in networks. _Physical review letters_ 89, 20 (2002), 208701.

- [21] Berkan Oztas, Deniz Cetinkaya, Festus Adedoyin, Marcin Budka, Huseyin Dogan, and Gokhan Aksu. 2023. Enhancing anti-money laundering: Development of a synthetic transaction monitoring dataset. In _2023 IEEE International Conference on e-Business Engineering (ICEBE)_ . IEEE, 47–54.

- [22] Peter Reuter. 2013. Are estimates of the volume of money laundering either feasible or useful? In _Research handbook on money laundering_ . Edward Elgar Publishing, 224–231.

- [23] Kimmo Soramäki, Morten L Bech, Jeffrey Arnold, Robert J Glass, and Walter E Beyeler. 2007. The topology of interbank payment flows. _Physica A: Statistical Mechanics and its Applications_ 379, 1 (2007), 317–333.

- [24] Jianheng Tang, Jiajin Li, Ziqi Gao, and Jia Li. 2022. Rethinking graph neural networks for anomaly detection. In _International conference on machine learning_ . PMLR, 21076–21089.

- [25] Mr Vito Tanzi. 1996. _Money laundering and the international financial system_ . International Monetary Fund.

- [26] Brigitte Unger, Melissa Siegel, Joras Ferwerda, Wouter De Kruijf, Madalina Busuioic, Kristen Wokke, and Greg Rawlings. 2006. The amounts and the effects

of money laundering. _Report for the Ministry of Finance_ 16, 2020.08 (2006), 22.

- [27] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. 2017. Graph attention networks. _arXiv preprint arXiv:1710.10903_ (2017).

- [28] John Walker. 1999. How big is global money laundering? _Journal of Money Laundering Control_ 3, 1 (1999), 25–37.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering" (2026-04-19). https://arxiv.org/abs/2604.17420
