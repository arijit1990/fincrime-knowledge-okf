---
type: Source Digest
title: Clue-Guided Money Laundering Group Discovery - part 5 of 7 (pp. 12-15)
description: 'Verified paraphrased digest, pp. 12-15: TABLE V AVERAGE PER-ROUND RUNTIME OF CLUE2GROUP; REFERENCES; VI. CONCLUSION'
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
part: 5
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
digest_points: 26
---

# Clue-Guided Money Laundering Group Discovery (digest)

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 12-15) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Fig. 7 analysis (clue position sensitivity)

- **descriptive / finding or result**: Core clues show a clear advantage in early interaction rounds because core nodes lie in denser, more structurally representative regions, letting the framework build a more complete LIC from round one. (p. 12)[^original]  
  <sub>anchor: "Since core nodes are located in denser and more structurally representative regions of the target group"</sub>
- **descriptive / finding or result**: The LIC size under core clues in the first round is reported as nearly 20 times larger than under peripheral clues, leading to larger initial predictions and better early-stage performance. (p. 12)[^original]  
  <sub>anchor: "the LIC size under core clues in the first round is nearly 20 times larger than that under peripheral clues"</sub>
- **descriptive / finding or result**: Under peripheral clues, performance improves rapidly as analyst-validated true members are added each round; LIC size and predicted group size approach core-clue levels around round 5, and F1 intersects around round 4. (p. 12)[^original]  
  <sub>anchor: "Around round 5, they become close to those under core clues. The corresponding Recall and F1 also converge, with F1 intersecting around round 4."</sub>
- **descriptive / finding or result**: The authors conclude the interactive mechanism of Clue2Group can effectively reduce the negative impact of unfavorable initial clue positions. (p. 12)[^original]  
  <sub>anchor: "This shows that the interactive mechanism of Clue2Group can effectively reduce the negative impact of unfavorable initial clue positions."</sub>

## Efficiency analysis (Fig. 8)

- **descriptive / finding or result**: The local LIC contains only a few hundred nodes, increasing from about 425 to 449, which is several orders of magnitude smaller than the full graph of about 500K accounts. (p. 12)[^original]  
  <sub>anchor: "increasing slightly from about 425 to 449. This is several orders of magnitude smaller than the full graph"</sub>
- **descriptive / finding or result**: Because MIST-GNN heterogeneous and temporal modeling runs only on this small local region, SACC reduces the otherwise prohibitive cost of global training to a controlled range. (p. 12)[^original]  
  <sub>anchor: "By constraining the context to a local LIC, SACC reduces the otherwise prohibitive cost of global training"</sub>
- **descriptive / finding or result**: Per-round runtime stays around 12–22 seconds, with total runtime dominated by MIST-GNN training; the authors deem this latency acceptable given analyst inspection in each round. (p. 12)[^original]  
  <sub>anchor: "the per-round runtime remains stable at around 12–22 seconds. Since each analyst-in-the-loop round also involves analyst inspection and judgment, this latency is acceptable in practice"</sub>

## Case study implementation details

- **descriptive / method**: The case study visualises group ID 333 on the HI-Small dataset over 10 interaction rounds, with colour coding: red for true members in LIC, orange for recovered group, blue for clue nodes, green for analyst-confirmed benign feedback, gray for background nodes. (p. 12)[^original]  
  <sub>anchor: "we visualize a case with group ID 333 on HI-Small dataset. Fig. 9 shows the results over 10 interaction rounds"</sub>
- **descriptive / finding or result**: Clue position mainly affects early localization efficiency; core clues give higher-quality initial predictions, while peripheral clues can approach core-clue recovery quality through multi-round interaction, so Clue2Group does not fully depend on high-quality initial clues. (p. 12)[^original]  
  <sub>anchor: "This indicates that Clue2Group does not fully depend on high-quality initial clues"</sub>

## Efficiency analysis implementation details

- **descriptive / method**: Runtime efficiency was evaluated on HI-Small by recording per-round runtime of SACC, MIST-GNN, EDGA and the full pipeline over 10 interaction rounds, then averaging per module. (p. 12)[^original]  
  <sub>anchor: "We record the per-round runtime of SACC, MIST-GNN, EDGA, and the full pipeline over 10 interaction rounds"</sub>

## Efficiency analysis

- **descriptive / finding or result**: The LIC expands from 31 nodes in round 1 to 74 nodes in round 10 in the case study, allowing the investigation scope to grow with feedback. (p. 12)[^original]  
  <sub>anchor: "the LIC expands from 31 nodes in round 1 to 74 nodes in round 10"</sub>
- **descriptive / finding or result**: Early rounds recover a relatively small group around initial clues; as positive and benign feedback accumulates, the predicted boundary is refined toward the true group structure. (p. 12)[^original]  
  <sub>anchor: "As positive and benign feedback are gradually incorporated, the predicted boundary is progressively refined"</sub>
- **descriptive / finding or result**: The authors suggest the model jointly exploits risk scores, structural consistency and prior pattern evidence rather than a single risk signal. (p. 12)[^original]  
  <sub>anchor: "suggesting that the model jointly exploits risk scores, structural consistency, and prior pattern evidence"</sub>
- **descriptive / finding or result**: Table V reports an average per-round runtime of about 18.97 seconds; MIST-GNN training takes 17.93 seconds (about 94.5% of total), while SACC and EDGA together take less than 1 second. (p. 12)[^original]  
  <sub>anchor: "the average per-round runtime is about 18.97 seconds. MIST-GNN training takes 17.93 seconds"</sub>
- **descriptive / finding or result**: The authors argue each interaction round costs almost the same as refitting the risk field, with context construction and group assembly overhead negligible. (p. 12)[^original]  
  <sub>anchor: "the overhead of context construction and group assembly is negligible"</sub>

## Case study implementation details

- **descriptive / finding or result**: Performance of interactive Clue2Group does not improve monotonically with more rounds but shows an optimal interaction window. (p. 13)[^original]  
  <sub>anchor: "exhibits an optimal interaction window"</sub>
- **permissive / expectation**: Because labels are costly, analysts need not provide feedback indefinitely; interaction can stop once recovery becomes stable or false positives begin to increase. (p. 13)[^original]  
  <sub>anchor: "analysts do not need to provide feedback indefinitely"</sub>
- **descriptive / finding or result**: The case shows Clue2Group recovers the target laundering group and provides an interpretable investigation trajectory with limited rounds and high-value feedback. (p. 13)[^original]  
  <sub>anchor: "Clue2Group can not only recover the target laundering group, but also provide an interpretable investigation trajectory"</sub>

## Conclusion

- **descriptive / context**: The paper formulates Clue-Guided Group Discovery (CGGD) and proposes the Clue2Group framework to address limits of existing methods in supporting real AML investigation workflows. (p. 13)[^original]  
  <sub>anchor: "we formulate Clue-Guided Group Discovery (CGGD) and propose the Clue2Group framework"</sub>
- **descriptive / finding or result**: Experiments on two large-scale AML benchmarks show Clue2Group more accurately recovers clue-related laundering groups and supports multi-round interactive investigation; it is robust to clue quantity and position and its cost suits analyst-in-the-loop use. (p. 13)[^original]  
  <sub>anchor: "Experimental results on two large-scale AML benchmarks show that Clue2Group can more accurately recover clue- related laundering groups"</sub>

## VI. CONCLUSION

- **descriptive / limitation**: Experiments rely mainly on public AML benchmarks; the authors state future work should validate the framework on more real financial networks and more complex laundering scenarios. (p. 13)[^original]  
  <sub>anchor: "Future work should further validate the framework on more real financial networks and more complex laundering scenarios"</sub>
- **descriptive / limitation**: The current setting assumes initial clues and interactive feedback are reliable, without considering noisy clues or mislabeled feedback. (p. 13)[^original]  
  <sub>anchor: "the current setting assumes that both initial clues and interactive feedback are reliable, without considering noisy clues or mislabeled feedback"</sub>
- **permissive / recommendation**: Future work can extend Clue2Group to real financial settings with noisy and imperfect interactions. (p. 13)[^original]  
  <sub>anchor: "Future work can extend Clue2Group to real financial settings with noisy and imperfect interactions"</sub>

## Supplementary Material, Neighborhood expansion

- **descriptive / method**: For each clue node, SACC performs a k-hop breadth-first search, with the number of nodes visited from one clue node upper-bounded by a term in d raised to the power k, where d is the maximum in-degree/out-degree. (p. 15)[^original]  
  <sub>anchor: "For each clue node V c C  , SACC performs a k-hop"</sub>

## Supplementary Material

- **descriptive / method**: The supplementary material gives the total complexity of the structural enhancement stage as a single big-O expression combining all paths, with the formula partly illegible in the extracted text. (p. 15)[^original]  
  <sub>anchor: "Combining all paths, the total complexity of the structural enhancement stage is"</sub>
- **descriptive / method**: For neighborhood expansion, SACC runs a k-hop breadth-first search from each clue node, where d is the maximum in-degree or out-degree of the graph. (p. 15)[^original]  
  <sub>anchor: "For each clue node V c C  , SACC performs a k-hop"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

[^original]: arXiv, "Clue-Guided Money Laundering Group Discovery" (2026-06-24). https://arxiv.org/abs/2606.26189
