---
type: Source Digest
title: Clue-Guided Money Laundering Group Discovery - part 4 of 7 (pp. 9-12)
description: 'Verified paraphrased digest, pp. 9-12: TABLE II PERFORMANCE OF MIST-GNN AND COMPARED MODELS; TABLE III PERFORMANCE COMPARISON OF EDGA AND BASELINE; TABLE IV SIZE COMPARISON OF LICS, GROUND-TRUTH GROUPS, AND'
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
part: 4
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
digest_points: 49
---

# Clue-Guided Money Laundering Group Discovery (digest)

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 9-12) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## TABLE II PERFORMANCE OF MIST-GNN AND COMPARED MODELS

- **descriptive / finding or result**: On HI-Small, MIST-GNN achieves the best AUC and AP among the compared models in Table II, and on HI-Medium it achieves the best AP. (p. 9)[^original]  
  <sub>anchor: "MIST-GNN achieves the best AUC and AP on HI-Small, and the best AP on HI-Medium"</sub>
- **descriptive / finding or result**: Table II reports homogeneous baselines GCN, GAT and GraphSAGE under sparse PU supervision: GCN AUC 0.4958 and AP 0.1125 on HI-Small, 0.4689 and 0.1519 on HI-Medium; GAT 0.6884/0.1576 on HI-Small and 0.5933/0.1682 on HI-Medium; GraphSAGE 0.7437/0.2322 on HI-Small and 0.6900/0.2932 on HI-Medium. (p. 9)[^original]  
  <sub>anchor: "GCN 0.4958 0.1125 0.4689 0.1519 GAT 0.6884 0.1576 0.5933 0.1682 GraphSAGE 0.7437 0.2322 0.6900 0.2932"</sub>
- **descriptive / finding or result**: Table II reports heterogeneous baselines R-GCN (AUC 0.7529, AP 0.1556 on HI-Small; 0.6184, 0.1898 on HI-Medium), HAN (0.5309/0.0988 on HI-Small; 0.4607/0.1286 on HI-Medium) and HGT (0.4894/0.0708 on HI-Small; 0.4818/0.1206 on HI-Medium). (p. 9)[^original]  
  <sub>anchor: "R-GCN 0.7529 0.1556 0.6184 0.1898 HAN 0.5309 0.0988 0.4607 0.1286 HGT 0.4894 0.0708 0.4818 0.1206"</sub>
- **descriptive / finding or result**: Table II ablation results on HI-Small and HI-Medium: w/o LTCE AUC 0.7645 and AP 0.2686 (HI-Small), 0.7611 and 0.3035 (HI-Medium); ac-channel 0.6552/0.2151 and 0.6675/0.2192; tx-channel 0.6880/0.1532 and 0.6077/0.1630; 1-channel 0.7123/0.2017 and 0.6416/0.1735; w/o tx(out & in) 0.7460/0.2674 and 0.6991/0.2303. (p. 9)[^original]  
  <sub>anchor: "w/o LTCE 0.7645 0.2686 0.7611 0.3035 ac-channel 0.6552 0.2151 0.6675 0.2192"</sub>
- **descriptive / finding or result**: Table II fusion variants: mean fusion AUC 0.7682 and AP 0.2658 on HI-Small, 0.7508 and 0.3018 on HI-Medium; attention fusion 0.7255/0.2109 and 0.7216/0.2543; mlp fusion 0.7633/0.2340 and 0.7234/0.2853; GCN layer 0.7766/0.2562 and 0.7699/0.2827; full MIST-GNN 0.7879/0.2945 and 0.7569/0.3048. (p. 9)[^original]  
  <sub>anchor: "mean fusion 0.7682 0.2658 0.7508 0.3018 attention fusion 0.7255 0.2109 0.7216 0.2543"</sub>
- **descriptive / method**: For evaluation, only accounts that belong to the target laundering group and are contained in the LIC, excluding clue nodes, are treated as ground-truth positives, and average Precision, Recall and F1 are reported over all cases. (p. 9)[^original]  
  <sub>anchor: "we treat only the accounts that belong to the target laundering group and are contained in the LIC, excluding clue nodes"</sub>
- **descriptive / context**: Q2 is a challenging early-investigation scenario in which only a small number of clue accounts are positive and all other LIC nodes are unlabeled, so Q2 results are described as a conservative estimate of performance. (p. 9)[^original]  
  <sub>anchor: "the current results can be viewed as a conservative estimate of model performance in the initial investigation stage"</sub>
- **descriptive / method**: Baselines for the assembly task are Louvain and LPA (general community detection) and PPR-Nibble and Weighted-PPR (random-walk local expansion); Weighted-PPR uses the MIST-GNN risk field as node weights, and all risk fields are generated by MIST-GNN. (p. 9)[^original]  
  <sub>anchor: "Weighted-PPR incorporates the MIST-GNN risk field as node weights"</sub>
- **descriptive / finding or result**: The authors attribute MIST-GNN's advantage over homogeneous and standard heterogeneous GNNs to its multi-semantic design: homogeneous models ignore the distinction between accounts and transaction events, and standard heterogeneous models do not separate fund inflows, outflows, and upstream or downstream relations. (p. 9)[^original]  
  <sub>anchor: "Homogeneous models tend to ignore the distinction between accounts and transaction events."</sub>
- **descriptive / method**: MIST-GNN decomposes the neighborhood into upstream accounts, downstream accounts, outgoing transactions and incoming transactions, capturing both account-level interaction patterns and event-level transaction behavior. (p. 9)[^original]  
  <sub>anchor: "By decomposing the neighborhood into upstream accounts, downstream accounts, outgoing transactions, and incoming transactions"</sub>
- **descriptive / context**: The authors state that MIST-GNN provides a domain-aware risk ranking signal under sparse PU supervision, which can be refined as more human feedback becomes available and is complementary to the structural entropy and chain/cycle prior evidence used in EDGA. (p. 9)[^original]  
  <sub>anchor: "Overall, MIST-GNN provides a domain-aware risk ranking signal under sparse PU supervision."</sub>
- **descriptive / finding or result**: The ablation results indicate that the account-based and transaction-based channels provide complementary information, and that a single semantic channel performs consistently worse than the full model. (p. 9)[^original]  
  <sub>anchor: "When only a single semantic channel is used, the performance is consistently lower than that of the full model."</sub>
- **descriptive / finding or result**: Removing directional transaction features causes a clear performance drop, which the authors take to show that distinguishing fund inflows from outflows matters for modeling laundering behavior. (p. 9)[^original]  
  <sub>anchor: "Removing directional transaction features also leads to a clear performance drop"</sub>
- **descriptive / finding or result**: LTCE improves AUC on HI-Small from 0.7645 to 0.7879 when the time window and neighbor sampling cover the true transaction rhythm of target groups; on HI-Medium, where transactions are sparser and span a longer time range, its gain is more limited. (p. 9)[^original]  
  <sub>anchor: "increasing AUC from 0.7645 to 0.7879"</sub>

## Evaluation on EDGA (Q3)

- **descriptive / method**: Sensitivity analysis of EDGA fusion weights is performed on a ternary simplex with 22 configurations: 3 vertex points for single-signal ablations, 12 edge points covering four mixing ratios for each pair of signals, 6 interior points for three-signal fusion, and the default configuration. (p. 9)[^original]  
  <sub>anchor: "3 vertex points for single-signal ablations, 12 edge points covering four mixing ratios for each pair of"</sub>

## Analysis

- **descriptive / finding or result**: Table III shows EDGA achieves the highest Precision and F1 on both HI-Small and HI-Medium; PPR-Nibble and WPPR-Nibble obtain higher Recall but clearly lower Precision, which the authors attribute to aggressive boundary expansion that introduces many background nodes. (p. 9)[^original]  
  <sub>anchor: "Although PPR-Nibble and WPPR-Nibble obtain higher Recall on both datasets, their Precision is clearly lower than that of EDGA."</sub>

## TABLE II PERFORMANCE OF MIST-GNN AND COMPARED MODELS

- **descriptive / method**: For EDGA, the top 20% and top 50% of boundary candidates are used, corresponding to R values of 0.2 and 0.5. (p. 9)[^original]  
  <sub>anchor: "For EDGA, we set 0.2 R = and 0.5 R = , corresponding to the top 20% and top 50% of boundary candidates."</sub>
- **descriptive / method**: In the plateau stage, R is set to 0.95 for the risk signal and 0.8 for the prior signal. (p. 9)[^original]  
  <sub>anchor: "In the plateau stage, we set 0.95 R  = for the risk"</sub>

## Baselines

- **descriptive / method**: All baselines are evaluated on the same LICs and clue nodes, and all risk fields are generated by MIST-GNN. (p. 9)[^original]  
  <sub>anchor: "All baselines are evaluated on the same LICs and clue nodes"</sub>

## Analysis

- **descriptive / finding or result**: Table IV shows EDGA recovers a group size closer to the ground-truth size within the LIC; on HI-Medium the average ground-truth group size is 13 and EDGA recovers 12 nodes on average. (p. 10)[^original]  
  <sub>anchor: "where the average ground-truth group size is 13 and EDGA recovers 12 nodes on average"</sub>
- **descriptive / finding or result**: The authors conclude that the three-signal design of EDGA gives complementary constraints during expansion, reducing noisy nodes while preserving valid members and giving a better Precision–Recall trade-off. (p. 10)[^original]  
  <sub>anchor: "It helps reduce the inclusion of noisy nodes while preserving valid group members"</sub>

## Evaluation on Clue2Group (Q4)

- **descriptive / finding or result**: Table III reports group recovery: Louvain Precision/Recall/F1 0.112/0.312/0.144 on HI-Small and 0.160/0.316/0.197 on HI-Medium; LPA 0.226/0.236/0.163 and 0.258/0.201/0.210; PPR-Nibble 0.103/0.465/0.163 and 0.156/0.601/0.234; WPPR-Nibble 0.223/0.607/0.260 and 0.209/0.613/0.265; EDGA 0.303/0.325/0.273 and 0.351/0.312/0.286. (p. 10)[^original]  
  <sub>anchor: "Louvain 0.112 0.312 0.144 0.160 0.316 0.197 LPA 0.226 0.236 0.163 0.258 0.201 0.210"</sub>
- **descriptive / finding or result**: Table III EDGA row: Precision 0.303, Recall 0.325, F1 0.273 on HI-Small; Precision 0.351, Recall 0.312, F1 0.286 on HI-Medium. (p. 10)[^original]  
  <sub>anchor: "EDGA 0.303 0.325 0.273 0.351 0.312 0.286"</sub>

## Implementation Details

- **descriptive / method**: In the group-recovery experiments, the initial clue set contains one connected component obtained by sampling about 10% of intra-group transactions, and each experiment runs for 10 interaction rounds. (p. 10)[^original]  
  <sub>anchor: "the initial clue set contains only one connected component, which is obtained by sampling approximately 10% of the intra-group transactions"</sub>
- **descriptive / method**: Each round, if the output contains true group members, one is randomly added to the clue set as a positive label; if it contains benign accounts, one is randomly added to the benign node set as a negative label; if neither exists, the label set is not updated that round. (p. 10)[^original]  
  <sub>anchor: "If no such node exists, the label set is not updated in that round."</sub>
- **descriptive / method**: In each interaction round, clue nodes are excluded and Precision, Recall and F1 are reported. (p. 10)[^original]  
  <sub>anchor: "we exclude the clue nodes and report Precision, Recall, and F1."</sub>

## TABLE IV SIZE COMPARISON OF LICS, GROUND-TRUTH GROUPS, AND

- **descriptive / finding or result**: Table IV reports the ground-truth group size in LIC as 16 on HI-Small and 13 on HI-Medium, LIC subgraph size 2298 and 1089, and recovered group sizes: Louvain 82 and 25, LPA 368 and 9, PPR-Nibble 69 and 43, WPPR-Nibble 230 and 40, EDGA 37 and 12. (p. 10)[^original]  
  <sub>anchor: "GT group size in LIC 16 13 LIC subgraph size 2298 1089 Louvain 82 25 LPA 368 9 PPR-Nibble 69 43 WPPR-Nibble 230 40 EDGA 37 12"</sub>

## Baselines

- **descriptive / method**: ICS-GNN is the main baseline because it follows a similar interactive, feedback-driven task paradigm to Clue2Group, but is designed for general social networks, whereas Clue2Group is domain-specific for money laundering investigations. (p. 10)[^original]  
  <sub>anchor: "ICS-GNN and Clue2Group follow a similar task paradigm."</sub>
- **descriptive / method**: The variant ICS-MIST-GNN replaces the GCN module in ICS-GNN with MIST-GNN, to test whether upgrading the GNN backbone can close the gap between a general framework and a domain-specific one. (p. 10)[^original]  
  <sub>anchor: "In this variant, the GCN module in ICS-GNN is replaced with MIST-GNN."</sub>
- **descriptive / method**: For Clue2Group the LIC is built by SACC with k=1 and no size constraint, simulating a scenario where the LIC need not cover all laundering group members; EDGA hyperparameters follow the Q3 setting. (p. 10)[^original]  
  <sub>anchor: "For Clue2Group, the LIC is constructed by SACC with k=1 and without a size constraint."</sub>
- **descriptive / method**: Because ICS-GNN and its variant require the output group size in advance, their output size in each round is set to the group size EDGA produces in that round for a fair comparison. (p. 10)[^original]  
  <sub>anchor: "we set the output size of both baselines in each round to be the same as the group size produced by EDGA in that round"</sub>

## Analysis

- **descriptive / finding or result**: Fusion weight sensitivity: on HI-Small, F1 varies only within [0.273, 0.278], the default configuration is within 1.8% of the best F1, and on HI-Medium the default achieves the best Recall and F1 with Precision only 0.2% below the best. (p. 10)[^original]  
  <sub>anchor: "The default configuration is within 1.8% of the best F1."</sub>
- **descriptive / finding or result**: On HI-Small the risk signal yields the highest Recall but lower Precision, suggesting more aggressive expansion, while structural entropy and prior pattern evidence give more conservative outputs; the best regions differ across datasets and no single signal dominates. (p. 10)[^original]  
  <sub>anchor: "On HI-Small, the risk signal achieves the highest Recall but relatively lower Precision"</sub>
- **descriptive / finding or result**: On HI-Medium the default three-signal configuration achieves F1 of 0.286, outperforming the best single-signal and two-signal configurations. (p. 10)[^original]  
  <sub>anchor: "the default configuration achieves an F1 of 0.286, outperforming the best single-signal and two-signal configurations"</sub>
- **descriptive / finding or result**: The authors conclude that the fusion mechanism is robust to weight selection, so EDGA does not depend on dataset-specific weight tuning and does not require fine-grained weight tuning. (p. 10)[^original]  
  <sub>anchor: "Therefore, EDGA does not require fine-grained weight tuning."</sub>
- **descriptive / finding or result**: Clue2Group consistently outperforms ICS-GNN and ICS-MIST-GNN on Precision, Recall and F1 over 10 interaction rounds on both datasets when clue nodes are excluded; the authors infer domain-specific design matters and that backbone replacement alone does not match Clue2Group. (p. 10)[^original]  
  <sub>anchor: "Clue2Group consistently outperforms ICS-GNN and ICS-MIST-GNN on Precision, Recall, and F1."</sub>
- **descriptive / finding or result**: The default fusion weights lie within the robust region, so EDGA does not require fine-grained weight tuning. (p. 10)[^original]  
  <sub>anchor: "the default weights lie within this robust region"</sub>
- **descriptive / finding or result**: Clue quantity sensitivity: under four initial clue ratios, Precision, Recall and F1 curves are largely consistent; Recall and F1 gaps are small in early and middle rounds, and predicted group sizes converge, with the cross-setting range decreasing from about 6.5 in round 1 to about 1.8 in round 10. (p. 11)[^original]  
  <sub>anchor: "The cross-setting range decreases from about 6.5 in round 1 to about 1.8 in round 10."</sub>
- **descriptive / finding or result**: The 20% clue setting shows lower Precision and F1 in most rounds mainly because excluding clue nodes removes more true members from evaluation and the LIC is larger with more irrelevant nodes, so the model must select similar numbers of nodes from a larger search space. (p. 11)[^original]  
  <sub>anchor: "The 20% clue setting shows relatively lower Precision and F1 in most rounds."</sub>
- **descriptive / finding or result**: Precision declines as the candidate space grows: candidate subgraph size and predicted group size both increase over rounds. (p. 11)[^original]  
  <sub>anchor: "both the candidates subgraph size and the predicted group size increase over interaction rounds"</sub>
- **descriptive / finding or result**: Recall and F1 first rise and then fall on both datasets, peaking around rounds 4–6, which the authors read as an optimal interaction window rather than monotonic improvement with more rounds. (p. 11)[^original]  
  <sub>anchor: "Recall and F1 first increase and then decrease on both datasets, with their peaks appearing around rounds 4–6."</sub>
- **descriptive / finding or result**: When clue nodes are included in evaluation, the 20% clue setting achieves clearly better Recall and F1, which the authors attribute to richer structural information and stronger supervision from more initial clues. (p. 11)[^original]  
  <sub>anchor: "the 20% clue setting achieves clearly better Recall and F1"</sub>
- **descriptive / limitation**: Clue2Group shows a larger drop in later rounds than baselines because its multi-evidence fusion depends on the quality of risk, structural and prior-pattern signals, which weaken as the boundary moves away from original clues; MIST-GNN may accumulate bias under limited supervision. (p. 11)[^original]  
  <sub>anchor: "MIST-GNN may accumulate bias under limited supervision."</sub>
- **expected / recommendation**: The authors suggest EDGA should be paired with a proper stopping strategy to avoid expansion when evidence becomes sparse. (p. 11)[^original]  
  <sub>anchor: "This suggests that EDGA should be paired with a proper stopping strategy to avoid expansion when evidence becomes sparse."</sub>
- **descriptive / finding or result**: Clue2Group keeps stable discovery under sparse clue settings and improves practical investigation output when more clues are available. (p. 11)[^original]  
  <sub>anchor: "Overall, Clue2Group maintains stable discovery ability under sparse clue settings"</sub>

## Implementation Details

- **descriptive / method**: Clue quantity robustness is tested on HI-Small by randomly sampling 3%, 5%, 10% and 20% of nodes from each true laundering group as initial clues. (p. 11)[^original]  
  <sub>anchor: "randomly sampling 3%, 5%, 10%, and 20% of nodes from each true laundering group as initial clues"</sub>

## Analysis

- **descriptive / finding or result**: Including clue nodes in evaluation is described as closer to real investigation, where analysts care about the final group output formed by initial clues and model-expanded nodes; results including clue nodes are placed in supplementary material to show cumulative discovery effect. (p. 11)[^original]  
  <sub>anchor: "Results including clue nodes are reported in the supplementary material to show the cumulative discovery effect perceived by analysts."</sub>
- **descriptive / context**: The authors note that analyst feedback in practical AML settings is costly and timely decisions are required, which is consistent with the finding of an optimal interaction window. (p. 11)[^original]  
  <sub>anchor: "where analyst feedback is costly and timely decisions are required"</sub>

## Component time

- **descriptive / finding or result**: Runtime components: SACC 0.72 seconds, MIST-GNN training 17.93 seconds, EDGA 0.27 seconds, and Clue2Group total 18.97 seconds. (p. 12)[^original]  
  <sub>anchor: "Component Time(sec) SACC 0.72 MIST-GNN Training 17.93 EDGA 0.27 Clue2Group(Total) 18.97"</sub>

---

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

[^original]: arXiv, "Clue-Guided Money Laundering Group Discovery" (2026-06-24). https://arxiv.org/abs/2606.26189
