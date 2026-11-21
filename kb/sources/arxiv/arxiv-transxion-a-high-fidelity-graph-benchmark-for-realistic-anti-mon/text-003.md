---
type: Source Text
title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering - part 3 of 3 (pp. 10-12)'
description: 'Verbatim extracted text, pp. 10-12: Zaiyuan Chen > References; Zaiyuan Chen > A Details of Anomalous Transaction Synthesis A.1 Scope and Disclosure Policy; Zaiyuan Chen > A.2 System Overview; and 7 more sections'
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
part: 3
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.17420
  title: 'TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2026-04-19T00:00:00Z'
---

# TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering

[previous part](text-002.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2026-04-19), part 3 of 3, pp. 10-12. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Zaiyuan Chen


### References


[p. 10]

- [29] Mark Weber, Jie Chen, Toyotaro Suzumura, Aldo Pareja, Tengfei Ma, Hiroki Kanezashi, Tim Kaler, Charles E Leiserson, and Tao B Schardl. 2018. Scalable graph learning for anti-money laundering: A first look. _arXiv preprint arXiv:1812.00076_ (2018).

- [30] Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I Weidele, Claudio Bellei, Tom Robinson, and Charles E Leiserson. 2019. Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. _arXiv preprint arXiv:1908.02591_ (2019).

- [31] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. 2018. How powerful are graph neural networks? _arXiv preprint arXiv:1810.00826_ (2018).

### A Details of Anomalous Transaction Synthesis A.1 Scope and Disclosure Policy


This appendix describes the reinforcement-learning (RL) training pipeline used for anomaly synthesis, including monitor-based feedback, group-relative optimization, and key training settings for reproducibility. To reduce misuse risk, we avoid disclosing institutionspecific operational rules or case-identifying details, while reporting the model-agnostic optimization setup used to construct the benchmark. For GRPO-based synthesis, we use AdamW with learning rate 1 × 10−5 and weight decay 0 _._ 01, gradient accumulation steps of 4, and maximum gradient norm 1 _._ 0. The policy is adapted with LoRA using rank _𝑟_ = 8, _𝛼_ = 16, and dropout 0 _._ 05. In our implementation, LoRA updates approximately 0 _._ 07% of the base model parameters. This synthesis cost is incurred only once during benchmark construction; downstream users can directly use the released fixed benchmark for detection evaluation.

### A.2 System Overview


The system consists of two components: (i) a policy that generates candidate graph-edit actions, and (ii) an external detector monitor that evaluates transaction subgraphs and outputs detection-related performance metrics. These metrics are aggregated into a scalar score, which serves as the learning signal for policy optimization. Training follows the Group Relative Policy Optimization (GRPO) paradigm, which estimates advantages using within-group statistics rather than an explicit value function.

Let _𝐶_ denote a transaction cluster represented as a subgraph. For each cluster, the policy _𝜋𝜃_ samples _𝐾_ trajectories,

### A.3 Environment Interaction and Group Sampling


- { _𝜏_ 1 _, . . . ,𝜏𝐾_ } ∼ _𝜋𝜃_ (· | _𝐶_ ) _._

Each trajectory _𝜏𝑖_ consists of a sequence of interaction steps. At step _𝑡_ , the agent observes a state derived from the current graph, emits a structured action proposing a graph edit, and the environment applies this edit to obtain the next graph state.

At each interaction step _𝑡_ , the monitor is applied to both the preaction graph _𝐺𝑡_ and the post-action graph _𝐺𝑡_ +1, yielding scalar

### A.4 Monitor Feedback and Reward Construction


[p. 11]

Table 7: Dataset summary statistics

Days Accounts Transactions Laundering 1 per 𝑁365 47 , 526 3 , 029 , 170 4 , 641 652 . 70

Figure 6: Transaction counts by payment format. Bars report the number of transactions in each Payment Format category.

scores:

The score is computed as a weighted combination of multiple detection metrics produced by the monitor, such as F1 score, area under the ROC curve (AUC), and average precision (AP). Formally,

where _𝑤_ 1 _,𝑤_ 2 _,𝑤_ 3 are non-negative weights determined by the experimental configuration.

The step reward consists of two terms:

### A.6 Policy Optimization Objective


The policy is optimized by maximizing the likelihood of actions or tokens associated with higher relative advantage. The resulting objective can be written as

This formulation enables stable optimization without training a separate critic network, while retaining a relative-performance baseline within each group.

We use a synthetically generated transaction dataset for AMLrelated experiments. Each row represents a directed transaction from a sender to a receiver at a specific timestamp. The sender endpoint is identified by From Bank and From Account, and the receiver endpoint is identified by To Bank and To Account. Transaction values are recorded on both sides: Amount Paid in Payment Currency for the payer side, and Amount Received in Receiving Currency for the payee side, allowing paid and received amounts to differ under currency conversion. The transaction channel is captured by Payment Format. A binary label, is_laundering, indicates whether a transaction is laundering (1) or benign (0).

### B.1 Dataset Overview


For subsequent statistics, we construct a unique account key by combining bank and account identifiers to avoid cross-bank identifier collisions. When computing account activity, each transaction contributes one count to both the sender and receiver accounts. Since the dataset provides transaction-level laundering labels but not pattern-level typology identifiers, we report aggregate laundering prevalence and distributional characteristics without patternwise breakdowns.

with

The validity term _𝑅_ validity ( _𝑎𝑡_ ) penalizes malformed or non-executable structured actions and may terminate the trajectory in case of severe violations. The monitor-difference term Δ _𝑆𝑡_ provides feedback proportional to the reduction in the monitor’s detection performance induced by the applied edit, scaled by the coefficient _𝜆_ mon.

### A.5 Group-Relative Advantage Estimation


GRPO estimates advantages using group-level statistics. Let _𝐽𝑖_ denote the cumulative return of trajectory _𝜏𝑖_ . The group mean and standard deviation are computed as

The standardized advantage for trajectory _𝑖_ is then defined as

Table 7 reports the dataset scale and the laundering label prevalence. The dataset spans 365 days and contains 47,526 unique bank accounts and 3,029,170 transactions. Among them, 4,641 transactions are labeled as laundering. This corresponds to a prevalence of 0.153% (approximately 1 in 653 transactions). The resulting class imbalance is substantial, so downstream evaluations should emphasize ranking- and precision-oriented metrics (e.g., PR-AUC, precision@K) rather than accuracy.

### B.3 Transaction-Level Characteristics


[pp. 11-12]

Figure 6 summarizes the transaction composition by Payment Format. Mobile payments account for the largest share, followed by card payments, while transfers and cash are less frequent. This skewed mix implies that channel information can be a strong cue in modeling. To avoid learning trivial shortcuts, we later report results with metrics that are robust to class imbalance and recommend stratified analyses by payment format when comparing methods.

where _𝜖 >_ 0 is a small constant for numerical stability.

Table 8: Tail-fit diagnostics under automatic _𝑥_ min selection. _𝐷_ is the KS distance; ( _𝑥_ min | _𝑛_ tail ) reports the selected threshold and tail size; ( _𝑅, 𝑝_ ) compares power law against lognormal.

[p. 12]

|Dataset|Distribution|_𝑥_min | _𝑛_tail|_𝛼_|_𝐷_|_𝑅, 𝑝_|
|---|---|---|---|---|---|
|Ours|degree_unique|56 | 24.0k|2.904|0.190|−4_._34×102,4_._92×10−30|
|Ours|degree_tx_count|79 | 23.8k|2.904|0.108|−3_._88,6_._25×10−1|
|Ours|strength|120.8k | 20.0k|2.405|0.057|−1_._12,1_._48×10−1|
|Ours|amount|40.3k | 30.3k|2.926|0.042|−3_._26×101,3_._11×10−3|
|AMLWorld|degree_unique|4 | 111.3k|3.000|0.045|−1_._79×103,1_._04×10−80|
|AMLWorld|degree_tx_count|40 | 79.6k|3.000|0.049|−2_._97×103,1_._82×10−87|
|AMLWorld|strength|531.0M | 5.2k|1.788|0.020|−4_._23,6_._84×10−2|
|AMLWorld|amount|623.8k | 253.9k|1.542|0.022|−1_._32×103,2_._01×10−202|
|AMLSim|degree_unique|12 | 4.5k|2.931|0.044|−5_._96×101,6_._42×10−11|
|AMLSim|degree_tx_count|219 | 4.9k|2.968|0.030|−2_._23×101,3_._86×10−5|
|AMLSim|strength|21.5M | 4.4k|2.148|0.105|−2_._56×102,2_._47×10−39|
|AMLSim|amount|85.5k | 26.5k|1.327|0.158|−5_._56×103,_−300|
|SAML-D|degree_unique|1 | 855.5k|3.000|0.118|−3_._52×104,_−300|
|SAML-D|degree_tx_count|215 | 17.1k|2.235|0.240|−5_._77×103,_−300|
|SAML-D|strength|80.6k | 402.1k|2.228|0.045|1_._57×101,7_._05×10−308|
|SAML-D|amount|10.2k | 2471.3k|3.000|0.030|−2_._19×102,4_._54×10−23|

Figure 7: Annualized transaction frequency per account. Each account’s incoming and outgoing transactions are counted and scaled to a yearly rate; bars report the number of accounts in each bin.

Figure 7 reports the distribution of annualized transaction frequency per account. We define an account as a bank–account pair and count both incoming and outgoing transactions. Most accounts fall in the mid-frequency bins (10–250 transactions per year), while a small fraction is either rarely active or highly active. This heterogeneity implies a skewed degree distribution in the induced transaction graph, which can affect both sampling and evaluation. Accordingly, we later interpret performance with care for activitydriven bias, rather than treating all accounts as equally informative.

### C Detailed Evidence of Fidelity


Table 8 reports tail-fit diagnostics under automatic _𝑥_ min selection. These diagnostics are intended to complement the main graphinvariant analysis rather than to claim that a single metric universally determines realism. In particular, we examine whether tail regions are non-degenerate, whether fitted exponents vary across different observables, and whether structural and monetary variables exhibit distinct regimes. Under these criteria, the results are

most consistent with _Ours_ exhibiting coherent and non-degenerate tail behavior across both structural and monetary variables.

_Coherent and Non-Templated Tails._ A key realism signal is that different observables should not collapse to a single universal exponent. In _Ours_ , the fitted _𝛼_ varies across structural and monetary variables: structural quantities such as degree_tx_count and strength remain in plausible heavy-tail regimes, while monetary amount follows a different tail pattern. In contrast, several baseline settings repeatedly return boundary values such as _𝛼_ = 3 _._ 0000, suggesting more rigid or over-regularized tail behavior rather than organically emerging heterogeneity.

_Automatic Tail Selection._ Under automatic _𝑥_ min selection, _Ours_ achieves small KS distances for degree_tx_count ( _𝐷_ = 0 _._ 1083), strength ( _𝐷_ = 0 _._ 0570), and amount ( _𝐷_ = 0 _._ 0418). These values indicate that, once the tail region is selected in a data-adaptive manner, the empirical tails of _Ours_ are well captured by the fitted model. We do not interpret the smallest KS value alone as the sole criterion of realism; instead, we consider it together with exponent stability, non-degenerate tail sizes, and the distinction between structural and monetary variables.

_Non-Degenerate Tail Definitions._ Some baselines produce degenerate or weakly informative tail regions. For example, SAML-D degree_unique selects _𝑥_ min = 1 with _𝑛_ tail = _𝑛_ , making the tail effectively equal to the full distribution. This weakens the interpretability of the fitted tail because no meaningful separation exists between the body and the tail. In contrast, _Ours_ retains meaningful tail sizes across variables, with selected tails that cover neither the entire support nor an extremely small residual subset.

_Mixed Monetary and Structural Regimes._ For monetary amount, _Ours_ favors a lognormal-like regime over a strict power law, while structural variables preserve credible heavy-tail signatures. This mixed behavior is plausible for payment systems: account activity and transaction volume can exhibit heavy-tailed participation, whereas transaction amounts often arise from multiplicative or mixture mechanisms rather than a pure power law. Therefore, the fidelity evidence is not that every observable follows the same distributional law, but that TransXion preserves heterogeneous tail behavior across semantically different variables.


---

[previous part](text-002.md) | [source overview](overview.md)

[^original]: arXiv, "TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering" (2026-04-19). https://arxiv.org/abs/2604.17420
