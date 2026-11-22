---
type: Source Digest
title: Clue-Guided Money Laundering Group Discovery - part 3 of 7 (pp. 6-8)
description: 'Verified paraphrased digest, pp. 6-8: ( )* S LIC; T; E R E E; and 6 more sections'
resource: https://arxiv.org/abs/2606.26189
tags:
- academic_finding
- advanced_analytics
- global_academic
- ml_statistics
- network_graph
- preprint
status: stable
source_id: arxiv-clue-guided-money-laundering-group-discovery
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-06-24'
legal_status: unknown
part: 3
parts_total: 7
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2606.26189
  title: Clue-Guided Money Laundering Group Discovery
  author: org:arxiv
  last_modified: '2026-06-24T00:00:00Z'
digest_points: 113
---

# Clue-Guided Money Laundering Group Discovery (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-8) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Final layer / Clue component

- **descriptive / method**: At the final layer, all four channel outputs are kept and projected into a shared latent space through channel-specific projections, then aggregated by mean pooling to form the final representation. (p. 6)[^original]  
  <sub>anchor: "we retain all four channel outputs and project them into a shared latent space via channel-specific projections"</sub>

## Clue component

- **descriptive / method**: When the clue set has multiple connected components, EDGA produces one recovered group view per component, each giving a different clue-conditioned perspective on the laundering group that can support further investigation. (p. 6)[^original]  
  <sub>anchor: "When the clue set contains multiple connected components, EDGA produces a set of recovered group views, one for each component."</sub>

## Greedy Expansion

- **descriptive / method**: Greedy expansion is restricted to the 1-hop boundary of the current group. (p. 6)[^original]  
  <sub>anchor: "restrict expansion to the 1-hop boundary"</sub>
- **descriptive / method**: At each expansion step the algorithm adds the boundary candidate with the highest marginal gain. (p. 6)[^original]  
  <sub>anchor: "At each step we add the candidate with the highest marginal gain"</sub>
- **descriptive / method**: The greedy expansion repeats until a stopping criterion is met. (p. 6)[^original]  
  <sub>anchor: "This repeats until a stopping criterion is met."</sub>

## Final layer / Clue component

- **descriptive / method**: At the final layer all four channel outputs are retained and projected into a shared latent space through channel-specific projections, then combined by mean pooling. (p. 6)[^original]  
  <sub>anchor: "project them into a shared latent space via channel-specific projections, then aggregate via mean pooling"</sub>
- **descriptive / method**: The final membership probability of a node is predicted from the aggregated representation; the exact equation is garbled in the extracted text. (p. 6)[^original]  
  <sub>anchor: "The final membership probability is predicted as:"</sub>

## Training Objective

- **descriptive / method**: In the initial investigation stage a PU learning setting is used, with clue nodes treated as positives and all other LIC nodes treated as unlabeled. (p. 6)[^original]  
  <sub>anchor: "clue nodes are treated as positives and all other nodes in the LIC are treated as unlabeled"</sub>
- **descriptive / method**: Training in the initial stage has a warm-up stage using BCE loss on positives only, followed by a main stage with ranking loss and hard negatives. (p. 6)[^original]  
  <sub>anchor: "a warm-up stage with BCE loss on positives only"</sub>
- **descriptive / method**: In the interactive investigation stage, analyst-confirmed benign nodes become explicit negatives, shifting the learning setting to PNU learning. (p. 6)[^original]  
  <sub>anchor: "analyst-confirmed benign nodes are introduced as explicit negatives"</sub>
- **descriptive / method**: In the initial investigation stage, a PU learning setting is used in which clue nodes are positives and all other LIC nodes are unlabeled. (p. 7)[^original]  
  <sub>anchor: "clue nodes are treated as positives and all other nodes in the LIC are treated as unlabeled"</sub>
- **descriptive / method**: Pseudo-negatives are drawn from the unlabeled set using the model's current prediction scores and their topological distance to the clues. (p. 7)[^original]  
  <sub>anchor: "their topological distance to the clues"</sub>
- **descriptive / method**: Positive and pseudo-negative samples receive different weights to reduce label noise. (p. 7)[^original]  
  <sub>anchor: "we assign different weights to positive and pseudo-negative samples"</sub>
- **descriptive / method**: Training has two stages: a warm-up stage using BCE loss on positives only, and a main stage using ranking loss and hard negatives. (p. 7)[^original]  
  <sub>anchor: "a warm-up stage with BCE loss on positives only, and a main stage with ranking loss and hard negatives"</sub>
- **descriptive / method**: Details of the training setup are given in the supplementary material. (p. 7)[^original]  
  <sub>anchor: "Details are given in the supplementary material."</sub>
- **descriptive / method**: In the interactive investigation stage, analyst-confirmed benign nodes are added as explicit negatives, so the learning setting becomes PNU learning. (p. 7)[^original]  
  <sub>anchor: "analyst-confirmed benign nodes are introduced as explicit negatives, shifting the learning setting to PNU learning"</sub>
- **descriptive / method**: The model is trained with a supervised binary cross-entropy loss, combined with ranking constraints and cross-semantic consistency regularization. (p. 7)[^original]  
  <sub>anchor: "the model is trained with a supervised binary cross-entropy loss, combined with ranking constraints and cross-semantic consistency regularization"</sub>

## Evidence Signals

- **descriptive / method**: Three complementary evidence signals are constructed to measure the marginal benefit of adding a candidate node to the current group. (p. 7)[^original]  
  <sub>anchor: "We construct three complementary signals to measure the marginal benefit of adding a candidate node u to the current group"</sub>

## Evidence Signals (1) Risk Consistency

- **descriptive / method**: MIST-GNN outputs a node-level risk field, and the risk-consistency signal is the risk value of the candidate node. (p. 7)[^original]  
  <sub>anchor: "MIST-GNN outputs a node-level risk field"</sub>
- **descriptive / definition**: The risk-consistency signal reflects the likelihood that the candidate account belongs to the target laundering group. (p. 7)[^original]  
  <sub>anchor: "account u belongs to the target laundering group"</sub>

## Evidence Signals (2) Structural Consistency

- **descriptive / definition**: Structure entropy quantifies the organizational quality of a graph by measuring the average coding length of a random walk under a given partition. (p. 7)[^original]  
  <sub>anchor: "quantifies the organizational quality of a graph by measuring the average coding length of a random walk"</sub>
- **descriptive / definition**: A lower structure entropy value indicates denser intra-cluster connections and sparser boundary cuts. (p. 7)[^original]  
  <sub>anchor: "A lower value indicates denser intra-cluster connections and sparser boundary cuts."</sub>
- **descriptive / method**: The two-dimensional structure entropy is used, which restricts the partition tree height to 2. (p. 7)[^original]  
  <sub>anchor: "we adopt the two-dimensional structure entropy, which restricts the partition tree height to 2"</sub>
- **descriptive / method**: During assembly the current group is treated as one cluster and all remaining nodes as singletons, and the structural-consistency signal is the entropy reduction from adding the candidate. (p. 7)[^original]  
  <sub>anchor: "is the entropy reduction from adding"</sub>
- **descriptive / method**: A local incremental formulation updates the entropy using only local quantities, without recomputing it over the full graph. (p. 7)[^original]  
  <sub>anchor: "which updates the entropy using only local quantities without recomputing it over the full graph"</sub>
- **descriptive / method**: Only three local quantities need to be maintained and updated at each step, so the per-iteration computation is stated as O(d(u)). (p. 7)[^original]  
  <sub>anchor: "Thus, at each step we only need to maintain and update these three local quantities"</sub>

## Evidence Signals (3) Prior Structure

- **descriptive / method**: SACC enumerates chain and cycle instances that pass amount consistency checks during context construction, and candidates are rewarded for advancing the completeness and continuity of these patterns. (p. 7)[^original]  
  <sub>anchor: "SACC enumerates chain and cycle instances that pass amount consistency checks during context construction"</sub>
- **descriptive / method**: Cycles reward late-stage closure and are scored with a convex completion function. (p. 7)[^original]  
  <sub>anchor: "Cycles reward late-stage closure, so we use a convex completion function"</sub>
- **descriptive / method**: Chains reward early path formation and their reward diminishes as the chain extends, so a concave function is used. (p. 7)[^original]  
  <sub>anchor: "Chains reward early path formation and diminish as the chain extends, so we use a concave function"</sub>
- **descriptive / method**: A continuous coverage reward based on adjacent-edge coverage is added beyond node completeness. (p. 7)[^original]  
  <sub>anchor: "Beyond node completeness, we introduce a continuous coverage reward based on adjacent-edge coverage"</sub>
- **descriptive / method**: The prior-structure signal is the sum of the cycle and chain components, and the signal is sparse, so a candidate receives a vote from it whenever its prior signal is nonzero. (p. 7)[^original]  
  <sub>anchor: "a candidate receives one vote from this signal as long as"</sub>

## Rank-based Three-evidence Voting

- **descriptive / method**: Because the three signals are heterogeneous, a rank-based three-evidence voting mechanism is adopted. (p. 7)[^original]  
  <sub>anchor: "we adopt a rank-based three-evidence voting mechanism"</sub>
- **descriptive / method**: For each signal, boundary candidates are ranked in descending order of their scores, and the rank is then linearly mapped to a strength score. (p. 7)[^original]  
  <sub>anchor: "For each signal, candidates in the current boundary are ranked in descending order according to their scores"</sub>
- **descriptive / method**: For the risk and structural-entropy signals, the top proportions of boundary candidates are selected for voting. (p. 7)[^original]  
  <sub>anchor: "Considering the heterogeneity of the three signals"</sub>
- **descriptive / method**: Each candidate's three binary votes determine its multi-evidence status, and a candidate is retained only if it is supported by at least two evidence sources. (p. 7)[^original]  
  <sub>anchor: "a candidate is retained only if it is supported by at least two evidence sources"</sub>
- **descriptive / method**: Ties between candidates with the same score are broken in the order of voting consistency, structural consistency, risk consistency, and prior consistency. (p. 7)[^original]  
  <sub>anchor: "If multiple candidates have the same score, ties are broken in the order of"</sub>

## Evidence Signals (3) Prior Structure

- **descriptive / method**: Taking the maximum over pattern instances avoids double counting when a node is in several patterns, so a candidate is primarily explained by its strongest structural evidence. (p. 7)[^original]  
  <sub>anchor: "Using max over instances avoids double counting when a node participates in multiple patterns"</sub>
- **descriptive / method**: The E, R and P signal weights are constrained to sum to 0.9, so the remaining 0.10 is reserved for the voting-consistency reward that favours candidates supported by multiple sources. (p. 7)[^original]  
  <sub>anchor: "so that the remaining 0.10 is reserved for the voting-consistency reward"</sub>

## Evidence Signals (1) Risk Consistency

- **descriptive / method**: The risk-consistency signal treats the node-level risk value p(u) as the likelihood that account u belongs to the target laundering group. (p. 7)[^original]  
  <sub>anchor: "account u belongs to the target laundering group"</sub>

## Evidence Signals (2) Structural Consistency

- **descriptive / definition**: Structure entropy measures the organisational quality of a graph as the average coding length of a random walk under a partition; lower values indicate denser intra-cluster connections and sparser boundary cuts. (p. 7)[^original]  
  <sub>anchor: "A lower value indicates denser intra-cluster connections and sparser boundary cuts"</sub>
- **descriptive / method**: The two-dimensional structure entropy used restricts the partition tree height to 2. (p. 7)[^original]  
  <sub>anchor: "which restricts the partition tree height to 2"</sub>

## Rank-based Three-evidence Voting

- **descriptive / method**: For each signal, boundary candidates are ranked in descending score order and the rank is linearly mapped to a strength score. (p. 7)[^original]  
  <sub>anchor: "candidates in the current boundary are ranked in descending order according to their scores"</sub>
- **descriptive / method**: For the risk and structural entropy signals, the top proportions R and E of boundary candidates are selected for voting. (p. 7)[^original]  
  <sub>anchor: "we select the top R  and top E  proportions of boundary"</sub>
- **descriptive / method**: Because the prior signal is sparse, a candidate receives one vote from it as long as its prior score is nonzero. (p. 7)[^original]  
  <sub>anchor: "Since the prior signal Ps is sparse, a candidate receives one vote from this signal as long as"</sub>
- **descriptive / method**: A candidate is retained in the multi-evidence set only if it is supported by at least two evidence sources. (p. 7)[^original]  
  <sub>anchor: "a candidate is retained only if it is supported by at least two evidence sources"</sub>
- **descriptive / method**: The final fusion score for retained candidates is computed as a combination of the vote and strength terms; the equation is partly garbled in the extracted text. (p. 7)[^original]  
  <sub>anchor: "we compute the final fusion score as"</sub>

## Stopping Criterion

- **descriptive / method**: Because the boundary of the growing set may become increasingly loose, the conductance of the current set is used to monitor expansion quality. (p. 8)[^original]  
  <sub>anchor: "As Y grows, its boundary may become increasingly loose"</sub>
- **descriptive / method**: After entering the plateau stage, expansion continues only when a strong-evidence candidate exists. (p. 8)[^original]  
  <sub>anchor: "After entering this stage, the algorithm continues expanding only when there exists a strong-evidence candidate"</sub>
- **descriptive / method**: Expansion also terminates when the maximum size is reached or when the boundary is exhausted. (p. 8)[^original]  
  <sub>anchor: "or when the boundary is exhausted"</sub>

## Experiments

- **descriptive / context**: The experiments evaluate the Clue2Group framework through four research questions. (p. 8)[^original]  
  <sub>anchor: "We organize the experiments in a hierarchical manner and analyze the framework through four research questions."</sub>
- **descriptive / context**: Q1 asks whether SACC can construct high-quality local investigation contexts from sparse initial clues at different clue positions. (p. 8)[^original]  
  <sub>anchor: "Given sparse initial clues and different clue positions, can SACC construct high-quality local investigation contexts (LICs)?"</sub>
- **descriptive / context**: Q2 asks whether MIST-GNN produces a stable and effective conditional risk field under PU supervision in the initial stage. (p. 8)[^original]  
  <sub>anchor: "Under PU supervision in the initial stage"</sub>
- **descriptive / context**: Q3 asks whether EDGA recovers money laundering group boundaries more accurately and whether the evidence-driven assembly is stable and robust. (p. 8)[^original]  
  <sub>anchor: "Can EDGA recover money laundering group boundaries more accurately?"</sub>
- **descriptive / context**: Q4 asks whether Clue2Group outperforms the general ICS-GNN baseline in the interactive setting and whether it is robust, efficient and able to give interpretable evidence chains. (p. 8)[^original]  
  <sub>anchor: "In the interactive setting, can Clue2Group outperform the general ICS-GNN baseline?"</sub>

## Datasets

- **descriptive / data or feature**: The public AML benchmark AMLSim is used, a simulation benchmark encompassing 8 money laundering typologies. (p. 8)[^original]  
  <sub>anchor: "a widely-adopted simulation benchmark encompassing 8 money laundering typologies"</sub>
- **descriptive / data or feature**: HI-Small contains approximately 500K accounts and 5M transactions. (p. 8)[^original]  
  <sub>anchor: "HI-Small, which contains approximately 500K accounts and 5M transactions"</sub>
- **descriptive / data or feature**: HI-Medium scales up to approximately 2M accounts and 32M transactions, to assess scalability and robustness. (p. 8)[^original]  
  <sub>anchor: "HI-Medium, which further scales up to ~2M accounts and 32M transactions"</sub>
- **descriptive / limitation**: The dataset provides malicious labels only at the transaction level. (p. 8)[^original]  
  <sub>anchor: "the dataset provides malicious labels only at the transaction level"</sub>
- **descriptive / method**: Ground-truth groups are built by first inducing a subgraph of all accounts involved in illicit transactions. (p. 8)[^original]  
  <sub>anchor: "we first induce a subgraph containing all accounts involved in illicit transactions"</sub>
- **descriptive / method**: Each connected component of that illicit-account subgraph is taken as a distinct money laundering group. (p. 8)[^original]  
  <sub>anchor: "identify each connected component within that subgraph as a distinct money laundering group"</sub>

## Implementation Details (Q1)

- **descriptive / method**: For Q1, 20 groups were randomly selected, and accounts in each induced subgraph were divided into core and peripheral nodes by node degree. (p. 8)[^original]  
  <sub>anchor: "we randomly selected 20 groups for evaluation"</sub>
- **descriptive / method**: Five clue nodes were randomly selected from each category, and a single clue node was used as the starting point in each experiment. (p. 8)[^original]  
  <sub>anchor: "randomly selected five clue nodes from each category"</sub>
- **descriptive / method**: Four LIC construction methods were compared under k values of 1, 2 and 3. (p. 8)[^original]  
  <sub>anchor: "compared four LIC construction methods under"</sub>
- **descriptive / method**: The four compared methods are neighborhood expansion (NE), NE with chain structure (NE+ch), NE with cycle structure (NE+cy), and SACC. (p. 8)[^original]  
  <sub>anchor: "NE+ch with chain-structure, NE+cy with cycle-structure, and SACC"</sub>
- **descriptive / method**: Average Recall is the primary metric, because the main goal of LIC construction is to cover as many true group members as possible. (p. 8)[^original]  
  <sub>anchor: "as the primary goal of LIC construction is to cover as many true group members"</sub>
- **descriptive / context**: Precision and F1 are reported in the supplementary material. (p. 8)[^original]  
  <sub>anchor: "Precision and F1 are provided in supplementary material"</sub>
- **descriptive / finding or result**: SACC also performs strongly on precision and F1, indicating the improvement does not come from blindly expanding the local context. (p. 8)[^original]  
  <sub>anchor: "indicating that the improvement does not come from blindly expanding the local context"</sub>

## Table I

- **descriptive / finding or result**: At k=2, recall values are NE 0.7935, 0.7786, 0.6554 and 0.5956; NE+ch 0.8643, 0.8388, 0.7434 and 0.6663 across the four columns. (p. 8)[^original]  
  <sub>anchor: "NE 0.7935 0.7786 0.6554 0.5956 NE+ch 0.8643 0.8388 0.7434 0.6663"</sub>
- **descriptive / finding or result**: At k=2, NE+cy recall is 0.8121, 0.7973, 0.6554 and 0.5956, while SACC reaches 0.8718, 0.8463, 0.7434 and 0.6663 across the same four columns. (p. 8)[^original]  
  <sub>anchor: "NE+cy 0.8121 0.7973 0.6554 0.5956 SACC 0.8718 0.8463 0.7434 0.6663"</sub>
- **descriptive / finding or result**: At k=3, recall values are NE 0.8742, 0.8546, 0.7824 and 0.7175; NE+ch 0.9170, 0.8924, 0.8362 and 0.7620 across the four columns. (p. 8)[^original]  
  <sub>anchor: "NE 0.8742 0.8546 0.7824 0.7175 NE+ch 0.9170 0.8924 0.8362 0.7620"</sub>
- **descriptive / finding or result**: At k=3, NE+cy recall is 0.8853, 0.8658, 0.7824 and 0.7175, while SACC reaches 0.9207, 0.8962, 0.8362 and 0.7620 across the same columns. (p. 8)[^original]  
  <sub>anchor: "SACC 0.9207 0.8962 0.8362 0.7620"</sub>
- **descriptive / finding or result**: SACC consistently outperforms or matches the baselines at the same k, so its gains reflect more than a larger neighborhood. (p. 8)[^original]  
  <sub>anchor: "same k, SACC consistently outperforms or matches the baselines"</sub>
- **descriptive / finding or result**: SACC shows consistent advantages across clue positions, k-hop settings and both datasets, indicating its LIC reliably covers true group members. (p. 8)[^original]  
  <sub>anchor: "From Table I, SACC shows consistent advantages across different clue positions, k-hop settings, and both datasets"</sub>
- **descriptive / finding or result**: All methods improve noticeably as k increases, suggesting that a larger local search scope helps include more true members. (p. 8)[^original]  
  <sub>anchor: "As k increases, all methods improve noticeably, suggesting that enlarging the local search scope helps include more true members"</sub>
- **descriptive / finding or result**: The advantage of SACC is most pronounced at k=1, where chain and cycle augmentation mitigate structural fragmentation when the initial clue gives limited context. (p. 8)[^original]  
  <sub>anchor: "The advantage is most pronounced at"</sub>
- **descriptive / finding or result**: Results from core clues are generally better than those from peripheral clues, so clue position affects how well the local context is recovered. (p. 8)[^original]  
  <sub>anchor: "results from core clues are generally better than those from peripheral clues"</sub>
- **descriptive / finding or result**: SACC maintains clear improvements in peripheral settings, indicating stronger robustness under weak clues. (p. 8)[^original]  
  <sub>anchor: "Still, SACC maintains clear improvements in peripheral settings, demonstrating stronger robustness under weak clues"</sub>
- **descriptive / finding or result**: On HI-Medium, SACC achieves the same performance as NE+ch, so the main gain there comes from chain-based enhancement while the cycle benefit is relatively limited. (p. 8)[^original]  
  <sub>anchor: "SACC achieves the same performance as NE+ch"</sub>

## Implementation Details (Q2)

- **descriptive / method**: For Q2, 20 laundering groups each with at least 10 accounts were randomly selected, and each experiment was repeated 3 times. (p. 8)[^original]  
  <sub>anchor: "We randomly select 20 laundering groups"</sub>
- **descriptive / method**: In each trial the initial investigation stage is simulated with a clue set containing only one connected component. (p. 8)[^original]  
  <sub>anchor: "repeat each experiment 3 times. In each trial, we simulate the initial investigation stage"</sub>
- **descriptive / method**: About 10 percent of intra-group transactions are sampled via connected expansion, and the involved accounts serve as clue nodes. (p. 8)[^original]  
  <sub>anchor: "~10% of intra-group transactions are sampled via connected expansion"</sub>
- **descriptive / method**: LICs are built by SACC with k set to 2, with size constrained to between 100 and 15000 nodes to exclude abnormally small or large subgraphs. (p. 8)[^original]  
  <sub>anchor: "their size is constrained to [100, 15000] nodes to exclude abnormally small or large subgraphs"</sub>
- **descriptive / method**: Training follows a PU setting in which clue accounts are positive, remaining LIC nodes are unlabeled, and pseudo-negatives are mined dynamically. (p. 8)[^original]  
  <sub>anchor: "Training follows a PU setting: clue accounts are positive, remaining LIC nodes are unlabeled, with pseudo-negatives mined dynamically"</sub>
- **descriptive / method**: For evaluation, only accounts that belong to the target laundering group and are contained in the LIC, excluding clue nodes, are treated as ground-truth positives. (p. 8)[^original]  
  <sub>anchor: "we treat only the accounts that belong to the target laundering group and are contained in the LIC"</sub>
- **descriptive / method**: Performance is measured by AUC and AP. (p. 8)[^original]  
  <sub>anchor: "Performance is measured by AUC and AP"</sub>

## Baselines and Variants

- **descriptive / method**: Six GNN baselines are compared, spanning homogeneous (GCN, GAT, GraphSAGE) and heterogeneous (R-GCN, HAN, HGT) paradigms. (p. 8)[^original]  
  <sub>anchor: "We compare against six GNN baselines spanning homogeneous (GCN, GAT, GraphSAGE) and heterogeneous (R-GCN, HAN, HGT) paradigms"</sub>
- **descriptive / method**: Ablation studies remove or replace key components, including LTCE, channel-only variants and removal of tx(out & in). (p. 8)[^original]  
  <sub>anchor: "Ablation studies remove or replace key components"</sub>
- **descriptive / method**: Variant studies substitute design choices in fusion (mean, attention, MLP) and convolution (GCN layer). (p. 8)[^original]  
  <sub>anchor: "Variant studies substitute design choices in fusion"</sub>

## Stopping Criterion

- **descriptive / method**: After a conductance-improvement condition holds for two consecutive steps, the expansion is regarded as entering a plateau stage; the exact condition is garbled in extraction. (p. 8)[^original]  
  <sub>anchor: "for two consecutive steps, we regard the expansion as entering a plateau stage"</sub>
- **descriptive / method**: Once in the plateau stage, expansion continues only when a strong-evidence candidate exists, and expansion also terminates when the size limit K is reached or the boundary is exhausted. (p. 8)[^original]  
  <sub>anchor: "the algorithm continues expanding only when there exists a strong-evidence candidate"</sub>

## Table I

- **descriptive / finding or result**: At k=1 the NE row reports recall values of 0.3333, 0.1887, 0.2872 and 0.1670, and the NE+ch row reports 0.4590, 0.3006, 0.4329 and 0.2853, in the table's column order (column headers are ambiguous in extraction). (p. 8)[^original]  
  <sub>anchor: "k=1 NE 0.3333 0.1887 0.2872 0.1670 NE+ch 0.4590 0.3006 0.4329 0.2853"</sub>
- **descriptive / finding or result**: At k=1 the NE+cy row reports recall values of 0.3610, 0.2148, 0.2872 and 0.1670, and the SACC row reports 0.4702, 0.3118, 0.4329 and 0.2853, in the table's column order. (p. 8)[^original]  
  <sub>anchor: "NE+cy 0.3610 0.2148 0.2872 0.1670 SACC 0.4702 0.3118 0.4329 0.2853"</sub>
- **descriptive / finding or result**: At k=2 the NE+cy row reports recall values of 0.8121, 0.7973, 0.6554 and 0.5956, and the SACC row reports 0.8718, 0.8463, 0.7434 and 0.6663. (p. 8)[^original]  
  <sub>anchor: "NE+cy 0.8121 0.7973 0.6554 0.5956 SACC 0.8718 0.8463 0.7434 0.6663"</sub>
- **descriptive / finding or result**: At k=3 the NE+cy row reports recall values of 0.8853, 0.8658, 0.7824 and 0.7175, and the SACC row reports 0.9207, 0.8962, 0.8362 and 0.7620. (p. 8)[^original]  
  <sub>anchor: "NE+cy 0.8853 0.8658 0.7824 0.7175 SACC 0.9207 0.8962 0.8362 0.7620"</sub>

## V. Experiments

- **descriptive / context**: The experiments evaluate Clue2Group through four research questions covering LIC construction, MIST-GNN under PU supervision, EDGA group recovery, and the interactive setting against ICS-GNN. (p. 8)[^original]  
  <sub>anchor: "We organize the experiments in a hierarchical manner and analyze the framework through four research questions"</sub>
- **descriptive / method**: AMLSim is the public AML benchmark used, a widely adopted simulation encompassing 8 money laundering typologies. (p. 8)[^original]  
  <sub>anchor: "a widely-adopted simulation benchmark encompassing 8 money laundering typologies"</sub>
- **descriptive / data or feature**: The HI-Small configuration contains approximately 500K accounts and 5M transactions. (p. 8)[^original]  
  <sub>anchor: "HI-Small, which contains approximately 500K accounts and 5M transactions"</sub>
- **descriptive / data or feature**: The HI-Medium configuration scales further to about 2M accounts and 32M transactions. (p. 8)[^original]  
  <sub>anchor: "which further scales up to ~2M accounts and 32M transactions"</sub>
- **descriptive / data or feature**: The dataset provides malicious labels only at the transaction level, so ground-truth groups had to be constructed. (p. 8)[^original]  
  <sub>anchor: "the dataset provides malicious labels only at the transaction level"</sub>
- **descriptive / method**: Ground-truth groups are built by inducing a subgraph of all accounts in illicit transactions and treating each connected component of that subgraph as a distinct laundering group. (p. 8)[^original]  
  <sub>anchor: "identify each connected component within that subgraph as a distinct money laundering group"</sub>
- **descriptive / method**: For the Q1 evaluation, 20 groups were randomly selected, with accounts split into core and peripheral nodes by degree and five clue nodes drawn from each category. (p. 8)[^original]  
  <sub>anchor: "we randomly selected 20 groups for evaluation"</sub>
- **descriptive / method**: The Q1 evaluation compares four LIC construction methods, NE, NE+ch, NE+cy and SACC, under k values 1, 2 and 3, and reports average Recall as the primary metric. (p. 8)[^original]  
  <sub>anchor: "We report the average Recall in Table 1, as the primary goal of LIC construction is to cover as many true group members as possible"</sub>
- **descriptive / method**: For the MIST-GNN evaluation, 20 laundering groups with at least 10 accounts are randomly selected and each experiment is repeated 3 times. (p. 8)[^original]  
  <sub>anchor: "We randomly select 20 laundering groups (each with ≥10 accounts) and repeat each experiment 3 times"</sub>
- **descriptive / method**: LICs for the MIST-GNN evaluation are built by SACC with k = 2, and their size is constrained to between 100 and 15000 nodes. (p. 8)[^original]  
  <sub>anchor: "their size is constrained to [100, 15000] nodes"</sub>
- **descriptive / method**: For evaluation, only accounts that belong to the target group and lie in the LIC, excluding clue nodes, count as ground-truth positives, and performance is measured by AUC and AP. (p. 8)[^original]  
  <sub>anchor: "Performance is measured by AUC and AP"</sub>
- **descriptive / finding or result**: SACC consistently outperforms or matches the baselines at the same k, and its gains are attributed to the additional evidence from structural enhancement, not only a larger neighbourhood. (p. 8)[^original]  
  <sub>anchor: "This shows that its gains come not only from a larger neighborhood, but also from the additional evidence introduced by structural enhancement"</sub>
- **descriptive / finding or result**: On HI-Medium, SACC achieves the same performance as NE+ch, suggesting the main gain there comes from chain-based enhancement while the cycle benefit is limited. (p. 8)[^original]  
  <sub>anchor: "It is also worth noting that on HI-Medium, SACC achieves the same performance as NE+ch"</sub>
- **descriptive / finding or result**: The advantage of chain and cycle augmentation is most pronounced at k=1, where the initial clue gives limited context and augmentation mitigates structural fragmentation. (p. 8)[^original]  
  <sub>anchor: "This suggests that when the initial clue provides limited context, chain and cycle augmentation can effectively mitigate structural fragmentation"</sub>
- **descriptive / finding or result**: Results from core clues are generally better than those from peripheral clues, indicating that clue position affects how well the local context can be recovered. (p. 8)[^original]  
  <sub>anchor: "results from core clues are generally better than those from peripheral clues"</sub>
- **descriptive / finding or result**: SACC keeps clear improvements over the baselines in peripheral settings, indicating stronger robustness under weak clues. (p. 8)[^original]  
  <sub>anchor: "Still, SACC maintains clear improvements in peripheral settings, demonstrating stronger robustness under weak clues"</sub>
- **descriptive / method**: Six GNN baselines are compared, spanning homogeneous (GCN, GAT, GraphSAGE) and heterogeneous (R-GCN, HAN, HGT) paradigms. (p. 8)[^original]  
  <sub>anchor: "We compare against six GNN baselines spanning homogeneous (GCN, GAT, GraphSAGE) and heterogeneous (R-GCN, HAN, HGT) paradigms"</sub>
- **descriptive / method**: Variant studies substitute design choices in fusion (mean, attention, MLP) and in convolution (GCN layer). (p. 8)[^original]  
  <sub>anchor: "Variant studies substitute design choices in fusion (mean/attention/MLP), convolution (GCN layer)"</sub>
- **descriptive / finding or result**: As k increases all methods improve noticeably, suggesting that a larger local search scope helps include more true group members. (p. 8)[^original]  
  <sub>anchor: "As k increases, all methods improve noticeably, suggesting that enlarging the local search scope helps include more true members"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: arXiv, "Clue-Guided Money Laundering Group Discovery" (2026-06-24). https://arxiv.org/abs/2606.26189
