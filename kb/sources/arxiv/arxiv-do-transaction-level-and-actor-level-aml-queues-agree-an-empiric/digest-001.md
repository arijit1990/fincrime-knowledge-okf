---
type: Source Digest
title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph - part 1 of 4 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: Abstract; 1 Introduction; 2 Related Work > 2.1 Bitcoin AML Detection; and 9 more sections'
resource: https://arxiv.org/abs/2604.23494
tags:
- academic_finding
- alerts_triage
- global_academic
- model_development
- network_graph
- preprint
status: stable
source_id: arxiv-do-transaction-level-and-actor-level-aml-queues-agree-an-empiric
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-04-26'
legal_status: unknown
part: 1
parts_total: 4
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
  resource: https://arxiv.org/abs/2604.23494
  title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph
  author: org:arxiv
  last_modified: '2026-04-26T00:00:00Z'
digest_points: 68
---

# Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper argues that graph-based AML systems on blockchain networks can score activity at transaction or actor-address granularity, yet compliance action is taken per actor, so the choice of granularity matters for investigation queues under fixed budgets. (p. 1)[^original]  
  <sub>anchor: "yet the compliance action is conducted per actor"</sub>
- **descriptive / finding or result**: Using the public Elliptic++ Bitcoin dataset (203,769 transactions; 822,942 address occurrences), the study trains independent random forest classifiers at each granularity under a causal temporal protocol and compares review queues via Jaccard overlap, burden decomposition and feature-matching ablations. (p. 1)[^original]  
  <sub>anchor: "Using the public Elliptic++ Bitcoin dataset (203,769 transactions; 822,942 address occurrences)"</sub>
- **descriptive / finding or result**: At a one-percent review budget, temporal evaluation across ten test timesteps gives a mean Jaccard of 0.374 (standard deviation 0.171), while static pooled evaluation gives 0.087 (95% CI [0.079, 0.094]). (p. 1)[^original]  
  <sub>anchor: "temporal evaluation across ten test timesteps yields a mean Jaccard of 0.374"</sub>
- **descriptive / finding or result**: An enriched address model using all 237 features aggregated from transaction data yields even lower overlap (Jaccard = 0.051), with 4.3% illicit per 100 reviews versus 30.2% for the transaction-projected queue. (p. 1)[^original]  
  <sub>anchor: "An enriched address model receiving all 237 features aggregated from transaction data produces even lower overlap"</sub>
- **descriptive / finding or result**: Address-level detection value is temporally concentrated: two timesteps exceed 91% illicit per 100 reviews, while the static address-queue burden is only 3.4%. (p. 1)[^original]  
  <sub>anchor: "two timesteps exceed 91% illicit per 100 reviews while the static address-queue burden is only 3.4%"</sub>
- **descriptive / finding or result**: A fixed hybrid consensus policy underperforms the best single-level queue by 5.05 percentage points (CI [−10.2pp, −0.9pp]), indicating naive score combination cannot exploit temporally heterogeneous disagreement. (p. 1)[^original]  
  <sub>anchor: "A fixed hybrid consensus policy underperforms the best single-level queue by 5.05 percentage points"</sub>
- **descriptive / finding or result**: The authors conclude that, on this dataset and under the primary noisy-OR projection, scoring granularity is a consequential design variable for AML investigation systems. (p. 1)[^original]  
  <sub>anchor: "scoring granularity is a consequential design variable for AML investigation systems"</sub>

## 1 Introduction

- **descriptive / context**: Two models with identical AUROC can produce substantially different top-K queues, directing investigators toward different sets of addresses, so standard classification metrics miss operational consequences. (p. 2)[^original]  
  <sub>anchor: "Two models with identical AUROC can produce substantially different top- _K_ queues"</sub>
- **descriptive / context**: The paper notes that existing reviews of network analytics for AML compare architectures rather than the granularity at which an architecture scores and queues actors. (p. 2)[^original]  
  <sub>anchor: "evaluate graph-based detection methods but compare architectures (GCN, random walk, manual features)"</sub>
- **descriptive / context**: Multi-granularity graph methods (HAN, HGT) mix node types within one architecture rather than comparing independent queues. (p. 2)[^original]  
  <sub>anchor: "Multi-granularity graph methods (HAN, HGT) mix node types within a single architecture"</sub>
- **descriptive / context**: Contribution 1: a formal projection framework defining four aggregation operators (noisy-OR, max-score, capped-sum, top-m mean) and quantifying their directional sensitivity on bipartite transaction-address edges. (p. 2)[^original]  
  <sub>anchor: "defining four aggregation operators (noisy-OR, max-score, capped-sum, top- _m_ mean)"</sub>
- **descriptive / method**: Contribution 2: budgeted metrics for AML including yield@budget, burden decomposition, case fragmentation and novel-positive rate measuring illicit-population turnover across timesteps. (p. 2)[^original]  
  <sub>anchor: "plus novel-positive rate, which measures illicit-population turnover across timesteps"</sub>
- **descriptive / finding or result**: A fixed geometric-mean consensus rule underperforms the best single-level queue by 5.05 percentage points on the temporal test horizon, motivating future work on adaptive switching. (p. 2)[^original]  
  <sub>anchor: "underperforming the best single-level queue by 5.05 percentage points on the temporal test horizon"</sub>
- **descriptive / finding or result**: Even with the actor model enriched by the full set of transaction features, the projected transaction queue and native actor queue still differ substantially, with Jaccard overlap of 0.051. (p. 2)[^original]  
  <sub>anchor: "the projected transaction queue and native actor queue remain substantially different (Jaccard = 0.051)"</sub>
- **descriptive / context**: The paper's structure: Section 2 reviews related work, Section 3 the methodology, Section 4 results across three hypotheses, Section 5 discussion and limitations, Section 6 concludes. (p. 3)[^original]  
  <sub>anchor: "Section 4 presents results across three hypotheses (queue disagreement, asymmetric burden, hybrid policy)"</sub>
- **descriptive / data or feature**: The original Elliptic dataset contains 203,769 Bitcoin transactions across 49 timesteps, with 4,545 illicit and 42,019 licit labels. (p. 3)[^original]  
  <sub>anchor: "introduced a labeled transaction graph of 203,769 Bitcoin transactions across 49 timesteps"</sub>
- **descriptive / context**: Prior Elliptic work used GCNs and random forests as baselines, evaluated on AUROC and F1, and later methods operated uniformly at the transaction level. (p. 3)[^original]  
  <sub>anchor: "Graph convolutional networks (GCNs; Kipf and Welling, 2017) and random forests served as baselines"</sub>
- **descriptive / context**: Address-level classification using transaction history summarisation has been explored in prior work, but without cross-level queue comparison. (p. 3)[^original]  
  <sub>anchor: "Address-level classification using transaction history summarization has been explored"</sub>

## 2.1 Bitcoin AML Detection

- **descriptive / data or feature**: Elliptic++ adds an actor (address) layer with 822,942 temporal occurrences, 55 address-level features, and bipartite edges linking addresses to their incident transactions. (p. 3)[^original]  
  <sub>anchor: "adding an actor (address) layer with 822,942 temporal occurrences, 55 address-level features"</sub>
- **descriptive / limitation**: The Elliptic++ paper evaluates each level independently, reporting per-level accuracy without comparing the queues each produces. (p. 3)[^original]  
  <sub>anchor: "the Elliptic++ paper evaluates each level independently, reporting per-level classification accuracy"</sub>
- **descriptive / finding or result**: Deprez et al. (2025) find that GNNs struggle under class imbalance, but do not address whether the same architecture at different graph levels produces different queues. (p. 3)[^original]  
  <sub>anchor: "finding that GNNs struggle under class imbalance, but does not address the orthogonal question of scoring granularity"</sub>

## 2.2 Multi-Granularity Graph Analysis

- **descriptive / context**: Heterogeneous GNNs (HAN, HGT, R-GCN, GraphSAGE) learn joint representations across levels but produce a single prediction per target node type, not independent queues. (p. 3)[^original]  
  <sub>anchor: "These approaches learn joint representations across granularity levels but produce a single prediction per target node type"</sub>
- **descriptive / context**: Entity resolution maps transactions to accounts or beneficial owners as a data-integration step; this paper instead treats the two levels as parallel scoring systems using the blockchain address as common action unit. (p. 3)[^original]  
  <sub>anchor: "using the blockchain address as the common action unit"</sub>

## 2.3 Decision Support Under Operational Constraints

- **descriptive / context**: AML compliance is a resource-allocation problem: investigation teams have fixed analyst capacity, so the scored queue determines which accounts receive review. (p. 4)[^original]  
  <sub>anchor: "AML compliance is fundamentally a resource-allocation problem"</sub>
- **descriptive / definition**: Precision-at-K measures how many of the top-K scored items are true positives, while yield@budget extends this to the fraction of all positives captured within the budget. (p. 4)[^original]  
  <sub>anchor: "Yield@budget extends this to the fraction of all positives captured within the budget"</sub>
- **descriptive / definition**: Rank-biased overlap is a top-weighted measure of ranked list similarity; Jaccard at fixed K is a simpler set-based overlap; neither has been used to quantify granularity-driven queue divergence. (p. 4)[^original]  
  <sub>anchor: "Neither has been used to quantify queue divergence arising from granularity choice"</sub>
- **descriptive / data or feature**: On Elliptic++, approximately 66% of test-period actors lack ground-truth labels, so a large fraction of any review queue may be cases whose true status is unresolved. (p. 4)[^original]  
  <sub>anchor: "approximately 66% of test-period actors lack ground-truth labels"</sub>

## 2.4 Ensemble and Hybrid Methods

- **descriptive / context**: The hybrid policy combines consensus scoring with disagreement-based escalation, drawing on cascading and escalation logic from ensemble learning. (p. 4)[^original]  
  <sub>anchor: "Our hybrid policy combines consensus scoring with disagreement-based escalation"</sub>
- **descriptive / finding or result**: The fixed hybrid underperforms temporally, suggesting static consensus rules cannot exploit time-varying disagreement. (p. 4)[^original]  
  <sub>anchor: "static consensus rules cannot exploit time-varying disagreement"</sub>
- **descriptive / definition**: In this paper 'actor' refers to a blockchain address (a public-key hash), not a resolved real-world entity or beneficial owner, since Elliptic++ provides no entity resolution beyond the address level. (p. 4)[^original]  
  <sub>anchor: "Throughout this paper, “actor” refers to a blockchain address (a public-key hash)"</sub>

## 3.1 Problem Formulation

- **descriptive / method**: Two independent classifiers are trained: a transaction-level model producing scores in [0,1] and an actor-level model producing scores in [0,1]; transaction scores are projected to actor level by an aggregation operator over incident transactions. (p. 4)[^original]  
  <sub>anchor: "Two independent classifiers are trained: _ftx_ : _Vtx →_ [0 _,_ 1] producing transaction-level risk scores"</sub>
- **descriptive / method**: At a fixed review budget K = floor(beta times the number of actors), the transaction-projected queue and native actor queue are each the top-K items and may differ. (p. 5)[^original]  
  <sub>anchor: "the transactionprojected queue _Qtx_ = top- _K_ ( _π_ ( _ftx_ )) and the native actor queue"</sub>
- **descriptive / context**: The study asks whether observed disagreement reflects a feature-set confound or a genuine granularity effect. (p. 5)[^original]  
  <sub>anchor: "We measure this disagreement and ask whether it reflects a feature-set confound or a genuine granularity effect"</sub>

## 3.2 Dataset: Elliptic++

- **descriptive / data or feature**: The transaction graph contains 203,769 nodes and 234,355 directed edges across 49 timesteps, with 182 features (93 local, 72 aggregated 1-hop, 17 structural). (p. 5)[^original]  
  <sub>anchor: "The transaction graph contains 203,769 nodes and 234,355 directed edges across 49 timesteps"</sub>
- **descriptive / data or feature**: Transaction labels: 4,545 illicit (class 1), 42,019 licit (class 2), and 157,205 unknown (class 3). (p. 5)[^original]  
  <sub>anchor: "Labels: 4,545 illicit (class 1), 42,019 licit (class 2), and 157,205 unknown (class 3)."</sub>
- **descriptive / data or feature**: The actor table has 822,942 temporal occurrences deduplicating to 530,840 train, 89,995 validation and 202,107 test unique addresses, each with 55 features. (p. 5)[^original]  
  <sub>anchor: "deduplicating to 530,840 (train), 89,995 (validation), and 202,107 (test) unique addresses"</sub>
- **descriptive / data or feature**: Among test addresses there are 3,132 illicit, 65,102 licit and 133,873 unknown labels (68,234 labeled in total). (p. 5)[^original]  
  <sub>anchor: "Labels: 3,132 illicit, 65,102 licit, and 133,873 unknown among test addresses (68,234 labeled total)"</sub>
- **descriptive / data or feature**: Actor features are globally static: none of the 273,268 addresses appearing more than once shows feature variation between occurrences. (p. 5)[^original]  
  <sub>anchor: "Actor features are globally static: across 273,268 addresses appearing more than once, zero exhibit feature variation"</sub>
- **descriptive / data or feature**: Bipartite edges: AddrTx (input/spending) 1,574,027 edges and TxAddr (output/receiving) 1,847,262 edges; the AddrAddr graph of 3,740,066 edges carries no timestamps, precluding temporal masking. (p. 5)[^original]  
  <sub>anchor: "AddrTx (input/spending, 1,574,027 edges) and TxAddr (output/receiving, 1,847,262 edges)"</sub>
- **descriptive / data or feature**: Transaction feature missingness is minimal: 16,405 NaN values (0.044%) across 17 columns, handled by median imputation from the training split; actor features have no missing values. (p. 5)[^original]  
  <sub>anchor: "16,405 NaN values (0.044%) across 17 columns, addressed by median imputation from the training split"</sub>

## 3.3 Causal Temporal Evaluation

- **descriptive / method**: A causal protocol uses timesteps 1–34 for training, 35–39 for validation and 40–49 for testing; for each test timestep only transactions and edges with timestamp at or before that timestep are available. (p. 5)[^original]  
  <sub>anchor: "Training uses timesteps 1–34, validation 35–39, and testing 40–49"</sub>
- **descriptive / finding or result**: Static actor-only features give a weak queue in isolation: illicit rate 0.24% versus 1.55% base rate, with Brier score 0.035 after Platt calibration on validation. (p. 5)[^original]  
  <sub>anchor: "static actor-only illicit rate 0.24% versus 1.55% base rate; Brier score 0.035 after Platt calibration on validation"</sub>
- **descriptive / method**: Path A causal actor features aggregate each address's incident transaction features up to timestep t via mean pooling, appending incident count and recency, giving 184-dimensional features. (p. 5)[^original]  
  <sub>anchor: "we aggregate its incident transaction features from timesteps _≤ t_ via mean pooling, appending incident count and recency"</sub>
- **descriptive / finding or result**: Path A is selected by two criteria: passing the Brier gate (Platt Brier 0.0013 on validation, below the 0.10 threshold) and showing actor-only illicit enrichment on validation; the static actor RF passes the Brier gate but fails the enrichment criterion. (p. 5)[^original]  
  <sub>anchor: "the causal actor RF passes the Brier gate (Platt Brier = 0.0013 on validation, well below the 0.10 threshold)"</sub>
- **descriptive / data or feature**: Active set sizes per timestep range from 12,199 (t=49) to 32,531 (t=42). (p. 5)[^original]  
  <sub>anchor: "Active set sizes range from 12,199 ( _t_ 49) to 32,531 ( _t_ 42)."</sub>

## 3.4 Projection Operators

- **descriptive / method**: Noisy-OR (primary operator) combines transaction scores as one minus the product of (one minus each score), a standard probabilistic aggregation assuming independent evidence. (p. 5)[^original]  
  <sub>anchor: "Standardprobabilisticaggregation assuming independent evidence. Used as the primary operator throughout."</sub>
- **descriptive / method**: Top-m mean averages the top m scores with m = 5, reducing the influence of low-risk incident transactions. (p. 6)[^original]  
  <sub>anchor: "Reduces influence of low-risk incident transactions."</sub>
- **descriptive / method**: All operators are applied directionally (input-side only, output-side only, or both), and direction sensitivity is reported in the results. (p. 6)[^original]  
  <sub>anchor: "All operators are applied directionally: using input-side transactions only, output-side only, or both."</sub>
- **descriptive / method**: In temporal evaluation the projection uses only transactions incident to the address at timestep t (not cumulative), while static evaluation uses all incident transactions in timesteps 40–49. (p. 6)[^original]  
  <sub>anchor: "the set of incident transactions _N_ ( _a_ ) used by projection operators includes all transactions incident to address _a_ at timestep _t_ only"</sub>

## 3.5 Models and Calibration

- **descriptive / method**: Both classifiers are random forest ensembles built with scikit-learn 1.3.2, using 500 trees, max_depth 20, balanced class weights, max_features sqrt and random_state 42; other parameters are defaults. (p. 6)[^original]  
  <sub>anchor: "Hyperparameters: n_estimators = 500, max_depth = 20, class_weight = “balanced”"</sub>
- **descriptive / method**: Only labeled examples (illicit and licit) are used for training and calibration; unknown-status cases are excluded at both levels. (p. 6)[^original]  
  <sub>anchor: "Unknown-status cases (class 3) are excluded from training at both levels."</sub>
- **descriptive / data or feature**: The transaction RF trains on 29,894 labeled transactions from timesteps 1–34. (p. 6)[^original]  
  <sub>anchor: "The transaction RF trains on 29,894 labeled transactions (timesteps 1–34)."</sub>
- **descriptive / method**: Path A horizon: for training actors the horizon is t=34, for validation actors t=39, for temporal test evaluation the horizon is the timestep itself, and for static test evaluation t=49. (p. 6)[^original]  
  <sub>anchor: "For training actors (timesteps 1–34), _t_ = 34 (the training split endpoint)"</sub>

## 3.4 Projection Operators

- **descriptive / method**: Max-score takes the highest incident transaction score and is conservative, so a single high-risk transaction dominates; capped-sum is volume-sensitive, with its cap parameter set to 1.0, the median incident count on the training set. (p. 6)[^original]  
  <sub>anchor: "with _ncap_ = 1 _._ 0 (median incident count on training set)"</sub>
- **descriptive / method**: The top-m mean operator averages the top m scores with m set to 5, reducing the influence of low-risk incident transactions. (p. 6)[^original]  
  <sub>anchor: "Top- _m_ mean: _πtop_ ( _a_ ) = mean of top- _m_ scores, with _m_ = 5."</sub>

## 3.5 Models and Calibration

- **descriptive / method**: Both classifiers are random forests with n_estimators 500, max_depth 20, balanced class weights, min_samples_split 2, min_samples_leaf 1, max_features sqrt and random_state 42; other parameters are scikit-learn defaults. (p. 6)[^original]  
  <sub>anchor: "min_samples_split = 2, min_samples_leaf = 1, max_features = “sqrt”, random_state = 42"</sub>
- **descriptive / limitation**: Recency is constant zero on the temporal active set because every active address has a transaction at timestep t, reducing effective informative features from 184 to 183; trees never split on constant features so predictions are unaffected. (p. 7)[^original]  
  <sub>anchor: "reduces the effective dimensionality from 184 to 183 informative features on the temporal active set"</sub>
- **descriptive / method**: Predicted probabilities are calibrated with Platt scaling on the validation split (timesteps 35–39; 5,486 labeled transactions; 24,217 labeled validation addresses). (p. 7)[^original]  
  <sub>anchor: "on the validation split (timesteps 35–39; 5,486 labeled transactions; 24,217 labeled validation addresses)"</sub>
- **descriptive / finding or result**: Transaction RF calibration: Brier raw 0.0128, Brier Platt 0.0075, ECE Platt 0.0022. (p. 7)[^original]  
  <sub>anchor: "Transaction RF: Brier (raw) = 0.0128, Brier (Platt) = 0.0075, ECE (Platt) = 0.0022."</sub>
- **descriptive / finding or result**: Actor RF (Path A) calibration: Brier raw 0.0027, Brier Platt 0.0013, ECE Platt 0.0005; isotonic calibration was computed but not used for queue construction. (p. 7)[^original]  
  <sub>anchor: "Actor RF (Path A): Brier (raw) = 0.0027, Brier (Platt) = 0.0013, ECE (Platt) = 0.0005."</sub>
- **descriptive / method**: The whole pipeline, including data preparation, training, evaluation and a 1,000-resample bootstrap, runs in under 30 minutes on a single machine. (p. 7)[^original]  
  <sub>anchor: "Total pipeline execution (data preparation, training, evaluation, 1,000-resample bootstrap) completes in under 30 minutes."</sub>

## 3.6 Evaluation Metrics

- **descriptive / definition**: Jaccard at K is the intersection over union of the two queues, ranging from 0 (no overlap) to 1 (identical queues). (p. 7)[^original]  
  <sub>anchor: "Ranges from 0 (no overlap) to 1 (identical queues)."</sub>
- **descriptive / finding or result**: Static rank-biased overlap is near zero (about 2.3 times 10 to the minus 12) due to extreme rank divergence, reported for completeness but not used inferentially. (p. 7)[^original]  
  <sub>anchor: "static RBO is near zero (point estimate 2 _._ 3 _×_ 10_−_12 ) due to extreme rank divergence"</sub>
- **descriptive / definition**: Burden decomposition partitions the top-K queue into illicit, known-licit and unknown-status cases, reported as rates per 100 reviews; reviews per true positive equal K divided by the illicit count. (p. 7)[^original]  
  <sub>anchor: "Reported as rates per 100 reviews. Reviews per TP = _K/_ illicit count"</sub>
- **descriptive / definition**: Yield at K is the fraction of total illicit actors captured within the budget. (p. 7)[^original]  
  <sub>anchor: "Fraction of total illicit actors captured within the budget: yield = _|Q∩_ illicit _|/|_ illicit _|_ ."</sub>
- **descriptive / definition**: Actor-only illicit rate is the illicit fraction among top-K addresses unique to the actor queue, measuring whether unique selections detect genuine positives or noise. (p. 7)[^original]  
  <sub>anchor: "This measures whether the actor queue’s unique selections are detecting genuine positives or noise."</sub>
- **descriptive / definition**: Case fragmentation is the fraction of the transaction queue's top-K projected addresses whose score derives from more than one incident transaction. (p. 7)[^original]  
  <sub>anchor: "fragmentation is the fraction whose projected score derives from more than one incident transaction"</sub>
- **descriptive / definition**: Novel-positive rate at each timestep is the fraction of illicit addresses not labeled illicit at any prior timestep, measuring illicit population turnover. (p. 7)[^original]  
  <sub>anchor: "the fraction of all illicit addresses at _t_ that were not labeled illicit at any prior timestep"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph" (2026-04-26). https://arxiv.org/abs/2604.23494
