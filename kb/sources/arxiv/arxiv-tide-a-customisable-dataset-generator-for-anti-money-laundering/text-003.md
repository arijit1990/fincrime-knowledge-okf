---
type: Source Text
title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research - part 3 of 5 (pp. 19-26)'
description: 'Verbatim extracted text, pp. 19-26: LI 36,629 7,642,030 0.10% 959:1 HI 36,653 7,618,299 0.19% 531:1'
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
part: 3
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.01863
  title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research'
  author: org:arxiv
  last_modified: '2026-02-03T00:00:00Z'
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2026-02-03), part 3 of 5, pp. 19-26. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## LI 36,629 7,642,030 0.10% 959:1 HI 36,653 7,618,299 0.19% 531:1


[p. 19] [ref: 4.6.3]

feature matrix contains only raw transactional fields, such as timestamp, amount, and currency. The is_fraudulent

label is retained as a target variable but excluded from the node features. For a detailed overview, see Table 15.

4.6.3 Data Export. Output formats are configured via boolean flags in the configuration YAML. The system supports

serialization into raw CSV files (node and edge lists) and direct export to graph objects for Python-based frameworks,

specifically PyTorch Geometric (.pt) and NetworkX (.gpickle). Additionally, JSON metadata is generated for each

pattern instance, recording the participating entities and transaction sequences.

4.6.4 Availability. The Tide data generation framework is open-source and publicly available at https://github.com/

mntijn/Tide.

4.7 Reference Benchmark: Datasets and Pipeline

Dataset Statistics. We publish two dataset variants generated from the same base population of 8,000 individuals,

differing in their target illicit ratio. Both datasets simulate a 12-month period (January–December 2025) and share the

same random seed, graph topology, and background activity configuration; only the fraud injection parameters differ.

Table 6 summarises the two variants.

The low-illicit variant (LI) and high-illicit variant (HI) use identical layering depth (2–5 hops) and fraud selection

parameters, differing only in the number of injected fraud patterns (90 vs. 320). The graph contains three node types:

accounts, individuals, and businesses.

Background transaction volume is derived from the target fraud ratio: the system generates fraud patterns first,

then scales legitimate background activity such that fraud edges/total edges ≈target ratio. The per-account daily

transaction rate is capped at 2 and scaled down as needed to meet the target ratio.

Data Partitioning. To prevent temporal data leakage and to simulate operational deployment scenarios, we adopt the

temporal split strategy proposed by Altman et al. [6]. Transactions are ordered by timestamp and partitioned using two

temporal thresholds, 𝑡1 and 𝑡2. Training indices correspond to transactions before 𝑡1, validation indices to transactions in

the interval [𝑡1,𝑡2), and test indices to transactions after 𝑡2. The split ratios are 60%, 20%, and 20% of the chronologically

ordered transaction sequence, respectively.

For GNN models, we construct three graphs to reflect the dynamic nature of financial transaction networks. The

training graph 𝐺train contains only transactions before 𝑡1. The validation graph 𝐺val contains all transactions before 𝑡2 (i.e., training and validation transactions), but evaluation is performed exclusively on validation indices. The test graph

𝐺test contains all transactions up to 𝑡max, with evaluation restricted to test indices. This construction simulates the

operational scenario where models must classify new transaction batches while having access to historical transaction

[pp. 19-20] [ref: 5.1]

graphs for pattern identification. This methodology ensures that models are evaluated on their ability to detect future

fraud given a complete historical context, reflecting the temporal constraints of production AML systems.

For GBT models (LightGBM and XGBoost), we apply the same temporal partitioning strategy but convert the graph

data to tabular feature vectors. Each transaction is represented by a feature vector comprising edge attributes (amount,

timestamp, currency), source-node features, and destination-node features. The training set uses transactions from

𝐺train, while validation predictions are computed only for new transactions in the interval [𝑡1,𝑡2), despite the feature

extractor having access to 𝐺val for computing graph-based features. This ensures that GBT models are evaluated under

the same temporal constraints as GNN models, thereby maintaining comparability across model classes.

Pipeline Implementation. We implement and publish the experimental workflow as a modular Kedro pipeline to ensure

reproducibility. The pipeline handles data loading, temporal splitting, model training (GNN and GBT), evaluation, and

result serialization. Hyperparameters are externalized, allowing researchers to reproduce our benchmarks or evaluate

new models against the published datasets with minimal modification.

Availability. Both dataset variants (LI and HI) are publicly available on Zenodo at https://zenodo.org/records/18804069.

The Kedro pipeline and all accompanying code are released at https://github.com/mntijn/tide-model-comparison.

5 Evaluation

We split the evaluation into three parts: we first validate the correctness of generated patterns, we then assess the

system’s scalability and performance, and finally, we evaluate the quality of the generated datasets through the

performance of supervised machine learning models trained on transaction classification tasks. The experimental design

follows the methodology described in Section 3, employing both GNN and GBT baselines under identical temporal split

configurations.

5.1 Structural Validation

The structural validation assesses how well Tide generates money-laundering patterns that conform to their formal

definitions. We analyse the structural accuracy, financial compliance, and temporal correctness of generated patterns

across all three pattern types. The results demonstrate whether our pattern generation algorithms successfully implement

the theoretical frameworks established in Section 2.

Additionally, the pattern visualisation results provide insights into the quality and recognisability of the generated

patterns, indicating whether they exhibit the characteristic structures expected in real money laundering scenarios.

For each pattern, we show our test results and a visualisation of both the structure and the timeline of transactions.

5.1.1 Front Business Pattern. Our validation confirmed that all generated instances of the Front Business Activity

pattern met their defined constraints. The tests verified a structure where 5 to 15 large cash deposits between €15,000

and €75,000 are each rapidly layered through overseas transfers. Each transfer, amounting to 80-100% of the deposit,

[pp. 20-21] [ref: 5.1.2]

was executed within 0.5 to 6 hours of the deposit, which is consistent across all tested instances.

The isolated generated pattern topology and the corresponding timeline of deposits and transfers are shown in

Figure 7. In Figure 7a, on the left one can see the source business, that deposits funds into its accounts, which is then

followed by transfers to other overseas businesses. This is visible on the timeline (Figure 7b), where all transfers follow

quickly after the deposits.

5.1.2 Rapid Fund Movement Pattern. Our tests showed that all three generated instances successfully met the predefined

constraints.

(b) Timeline of the transactions. All transfers happen within hours after deposits.

(a) The front business activity pattern. The source business (red- yellow node on the left) deposits funds into its accounts (blue nodes), which is then followed by transfers to overseas busi- nesses (green nodes on the right). Brackets display the country that the node is located in.

Fig. 7. The front business pattern shown as a network graph and a transaction timeline.

We examined the attributes as we detailed before. The financial and timing constraints were all satisfied. All individual

inflow transactions stayed below the €10,000 reporting threshold. Second, we calculated the outflow-to-inflow ratio for

each instance and found that all three fell within the required 0.85-0.95 range. Third, we verified the timing requirements

and found that the transaction ordering was correct in all cases. The inflow phase completed within 24 hours, there was

at least a 1-hour delay before withdrawals began, and the entire pattern finished well under the 128-hour maximum

duration.

The topology in Figure 8a shows a similar structure as illustrated in Section 4.4.3. The overseas accounts first transfer

money to multiple accounts owned by the beneficiary, after which these funds are withdrawn. Additionally, the timeline

in Figure 8b demonstrates the rapid succession of inflows within a compressed timeframe, followed by the distinct

outflow phase.

5.1.3 Repeated Overseas Transfer Pattern. Our tests demonstrated that all three generated instances successfully

satisfied the predefined constraints for the Repeated Overseas Transfer pattern.

We analysed the pattern attributes using the same approach applied to previous patterns. The transfer frequency

requirements were met across all instances, with each pattern generating between 4-12 individual transfers as specified.

We verified that every transfer amount fell within the required €5,000-€20,000 range. The destination diversity constraint

was also satisfied, with each instance directing transfers to 2-5 distinct overseas accounts as intended. All patterns

maintained regular scheduling at 7-, 14-, or 30-day intervals throughout the sequence. The temporal consistency

remained stable across the entire pattern duration, with no significant deviations from the established intervals.

Additionally, we validated that all destination accounts were properly classified as overseas entities.

[pp. 21-22] [ref: 5.1.4]

The isolated generated pattern topology and the corresponding timeline of deposits and transfers are shown in

Figure 9.

(a) The rapid fund movement pattern. Overseas accounts (green nodes) first transfer money into multiple accounts of the same entity (purple nodes), which is then withdrawn. Brackets display the country that the node is located in.

(b) Timeline of the transactions over simulation time. First there is a ‘burst’ of incoming transfers (blue) into the accounts, which is later followed by a burst of withdrawals (pink).

Fig. 8. The rapid fund movement pattern shown as a network graph and a transaction timeline.

5.1.4 U-turn transactions. Our tests showed that all three generated instances successfully met the predefined con-

straints for the U-Turn transactions pattern. We examined the attributes following the same approach we used before.

The chain length requirements were satisfied in all cases, with each instance containing between 4-7 entities as specified.

Additionally, we checked that every pattern started with an international transfer in the correct €10,000-€100,000 range.

We also calculated the fees applied at each intermediary hop and found that all instances properly applied fees between

1-3% of the transaction amount at every step. We found that each pattern successfully returned between 70-90% of the

remaining amount back to the source entity after accounting for cumulative fees.

We also checked the timing constraints and found that all inter-hop delays stayed within the required 1-5 day range.

The transaction sequences maintained proper ordering throughout each chain, and the complete U-Turn patterns

finished within reasonable timeframes while meeting all specified timing requirements.

The isolated generated pattern topology and its timeline are shown in Figure 10. Both orange accounts are owned by

the same entity, either directly or indirectly through an owned business.

5.2 Machine Learning Model Performance Evaluation

5.2.1 Machine Learning Models. To evaluate the quality of the datasets generated by Tide, we employ a spectrum

of supervised learning models, with both Graph Neural Networks (GNNs) and Gradient-Boosted Trees (GBTs). Our

selection criterion is both based on Altman et al. [6], and diagnostic: each model architecture is sensitive to a different

modality of the generated data. By observing which models succeed or fail, we can disentangle the contributions of

topological structure, transactional attributes, and temporal dynamics within our synthetic patterns.

GIN (Graph Isomorphism Network). We select GIN [39] as our primary baseline for structural validation. GIN is

theoretically designed to be as powerful as the Weisfeiler-Lehman (WL) isomorphism test, making it the ideal candidate

to determine if the topological shapes of our injected fraud patterns are distinguishable from background activity.

[pp. 23-24]

(a) The repeated overseas transfers pattern. An individual (blue node on the left) repeatedly deposits money into their account (middle yellow node), which is then followed by repeated overseas transfers to the same beneficiaries (green nodes on the right). Brackets display the country that the node is located in.

(c) Timeline of the periodic transactions. The deposit phase con- sists of frequent deposits followed by transfers every ≈7 days.

(b) Timeline of the high-frequency transactions over simulation time. The transfer phase consists of a similar burst of transactions as the deposit phase.

Fig. 9. The repeated overseas transfer pattern shown as a network graph and two distinct transaction timelines: one for high-frequency activity and one for periodic behaviour.

• Mechanism: Unlike standard GCNs that average neighbor features, GIN utilizes a sum aggregator. The node

update rule is defined as:

∑︁

ℎ(𝑘)

ℎ(𝑘−1)

𝑣 +

(1 + 𝜖(𝑘)) · ℎ(𝑘−1)

(7)

𝑣 = MLP(𝑘) ©­

𝑢∈N(𝑣)

«

𝑢 ª® ¬

• relevance to Dataset: The sum aggregator allows GIN to distinguish neighborhoods based on cardinality and

total volume rather than just distribution. In the context of our generated data, this tests whether the specific

connectivity patterns of money laundering are structurally preserved and learnable.

GIN with Edge Updates (GIN+EU). While standard GIN excels at structure, it treats edges as binary connections. To

evaluate the fidelity of the transactional attributes generated by Tide (specifically amounts and timestamps), we employ

a GIN variant extended with edge updates. We use the exact implementation by Altman et al. [6].

• Mechanism: This architecture explicitly incorporates edge features 𝑒𝑢𝑣into the message-passing framework.

The message from neighbor 𝑢to node 𝑣transforms from a simple node feature ℎ𝑢to a fused representation

𝜙(ℎ𝑢,𝑒𝑢𝑣).

(a) U-turn transaction pattern. The orange nodes are accounts, which con- trolled by the same entity. Funds flow from the left to the right node. Brackets display the country that the node is located in.

(b) Timeline of the U-turn transaction pattern.

Fig. 10. The U-turn transaction pattern shown as a network graph and a transaction timeline.

• Relevance to Dataset: This model tests the "Interaction Hypothesis": does the combination of who is transacting

and how much/when they transact provide a stronger signal than structure alone? High performance here would

confirm that Tide’s edge attributes contain discriminative signal beyond the graph topology.

[pp. 24-25] [ref: 5.2.2]

PNA (Principal Neighbourhood Aggregation). Real-world financial crime often manifests as subtle statistical anomalies

rather than obvious structural shapes. We include PNA [12] to test the distributional complexity of the generated data.

• Mechanism: PNA generalizes the message passing by employing multiple aggregators (Mean, Max, Min, Std)

and degree-scalers simultaneously.

• Relevance to Dataset: If our generator successfully creates complex laundering typologies (e.g., structuring

amounts to minimize variance, or high-value outliers), PNA is the architecture best equipped to detect these

second-order statistical properties.

Gradient Boosted Trees (Tabular Baselines). Finally, we evaluate LightGBM and XGBoost to isolate the quality of

the temporal dynamics independent of graph topology. For this reason, even though our model selection is based on

Altman et al. [6], we do not employ the same Graph Feature Preprocessor for these tabular models.

• Mechanism: These models operate on "flattened" tabular data. Unlike GNNs, they cannot see the network

structure directly. Instead, they rely on the manually engineered temporal features described in the preprocessing

step (very much learning from features like time since last transaction).

• Relevance to Dataset: These baselines provide a crucial control. If GBTs perform well, it validates that Tide

generates temporally consistent sequences that are predictive in their own right. It proves that the temporal

signal (bursts, delays, periodicities) is strong enough to drive detection even when the explicit graph structure

is removed.

5.2.2 Performance Assessment Metrics. All metrics are computed on the test set using predictions from the best model

checkpoint, selected based on the minimum validation loss. As detailed in Section 3.4, we report standard classification

metrics including F1 Score, Precision, Recall, and Area Under the Precision-Recall Curve (PR-AUC).

For all models, we perform threshold optimization on the validation set to determine the decision boundary that

maximizes Youden’s J statistic. This optimal threshold is then applied to the test predictions. This approach simulates

operational deployment, where the system is calibrated on historical data to find the cut-off point that best separates

illicit and legitimate transactions. In contrast to F1 optimization, which balances precision and recall, maximizing

Youden’s J identifies the threshold with the greatest statistical separation between the positive and negative class

distributions. This ensures the decision boundary is driven by the model’s fundamental discriminatory power rather

than the specific prevalence of fraud in the validation set.

Temporal Feature Preprocessing. Prior to GNN training, the temporal split procedure augments static node features

with eight temporal statistics: in-degree, out-degree, and transaction amount statistics (mean, standard deviation,

maximum) for both incoming and outgoing edges. These features are computed exclusively from edges available up to

each split’s temporal boundary: training features use only training edges, validation features use training edges, and

[pp. 25-26] [ref: 5.2.3]

test features use training and validation edges. This prevents temporal leakage by ensuring that node features never

aggregate information from future transactions. Consequently, GNN models receive rich temporal features as input,

reducing the representational burden on the message-passing layers.

5.2.3 Experimental Results. Table 7 summarises PR-AUC performance across two experimental conditions: LI (0.10%

fraud rate) and HI (0.19% fraud rate). Full results including F1, Precision, Recall, and Lift are provided in Appendix

Tables 20–21. PR-AUC serves as our primary evaluation metric given its robustness to class imbalance; threshold-

dependent metrics are computed at Youden’s optimal threshold for completeness. Results report mean ± standard

deviation over five runs.

Results. In the LI condition (0.10%), LightGBM achieves the highest PR-AUC (78.05±3.61) and Lift (749.19×), followed

by XGBoost (72.01 ± 0.50) and GIN (69.86 ± 6.55). At higher illicit ratio (HI, 0.19%), XGBoost achieves the strongest

PR-AUC (85.12 ± 0.52) and Lift (452.78×). GIN shows stable PR-AUC across conditions (69.86 →71.14), while PNA

improves from 69.20 to 75.63 ± 5.85.

Precision remains low across most models (2–12%) despite strong PR-AUC and Youden’s 𝐽scores. This is expected:

Youden’s threshold optimises sensitivity and specificity rather than precision, and under extreme class imbalance, even a

modest false positive rate produces many false alarms relative to the small number of true positives. In operational AML

systems, threshold selection is typically guided by alert-handling capacity and cost constraints rather than statistical

optimisation criteria such as Youden’s 𝐽; we report these metrics for methodological comparability rather than as

deployment recommendations.

The +GFP variants consistently underperform their base models, likely because the generic graph features extracted

by the preprocessor do not align with the specific structural and temporal patterns encoded by Tide’s fraud injection

mechanism. GIN+EU exhibits high variance across runs (e.g., 39.43 ± 20.99 in LI), suggesting sensitivity to initialisation

that may limit its reliability in practice.

ROC-AUC exceeds 93% for all models across both conditions, confirming strong class separability but illustrating why

ROC-AUC is inadequate for AML evaluation: the metric fails to capture the precision challenges inherent to extreme

class imbalance.

Analysis. These results validate Tide as a benchmarking tool for AML detection research. The generator produces

realistic class imbalance scenarios that differentiate model robustness: tabular models (XGBoost, LightGBM) maintain

[p. 26]

or improve PR-AUC as fraud prevalence increases, while GNN variants exhibit higher variance. The divergent model

rankings across conditions (LightGBM optimal at 0.10%; XGBoost optimal at 0.19%) demonstrate that Tide’s reference

datasets can meaningfully distinguish model capabilities, supporting their use as standardised benchmarks for future

work.

Table 7. PR-AUC across experimental conditions. Bold indicates best performance per condition. Results are mean ± standard deviation over 5 runs.

Model Illicit Ratio

GIN 69.86 ± 6.55 71.14 ± 8.70 GIN+EU 39.43 ± 20.99 48.42 ± 17.05 PNA 69.20 ± 0.00 75.63 ± 5.85 LightGBM+GFP 21.45 ± 13.23 64.40 ± 24.36 XGBoost+GFP 35.45 ± 2.59 32.20 ± 1.68


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Tide: A Customisable Dataset Generator for Anti-Money Laundering Research" (2026-02-03). https://arxiv.org/abs/2603.01863
