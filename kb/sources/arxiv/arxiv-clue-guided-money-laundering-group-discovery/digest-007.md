---
type: Source Digest
title: Clue-Guided Money Laundering Group Discovery - part 7 of 7 (pp. 18-19)
description: 'Verified paraphrased digest, pp. 18-19: IV. DENSITY-DEPENDENT EFFECTIVENESS OF LTCE'
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
part: 7
parts_total: 7
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
  resource: https://arxiv.org/abs/2606.26189
  title: Clue-Guided Money Laundering Group Discovery
  author: org:arxiv
  last_modified: '2026-06-24T00:00:00Z'
digest_points: 26
---

# Clue-Guided Money Laundering Group Discovery (digest)

[previous part](digest-006.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 18-19) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## IV. DENSITY-DEPENDENT EFFECTIVENESS OF LTCE

- **descriptive / definition**: Max-24h Coverage is the maximum proportion of laundering transactions in a group that can be covered by any 24-hour window. (p. 18)[^original]  
  <sub>anchor: "Max-24h Coverage measures the maximum proportion of laundering transactions in a group that can be covered by any 24-hour window."</sub>
- **descriptive / definition**: Laundering-Hit@5 indicates whether the selected top-5 historical transactions contain at least one laundering transaction. (p. 18)[^original]  
  <sub>anchor: "Laundering-Hit@5 indicates whether the selected top-5 historical transactions contain at least one laundering transaction."</sub>
- **descriptive / definition**: Same-Group-Hit@5 further requires the selected transaction to belong to the same true laundering group as the target transaction. (p. 18)[^original]  
  <sub>anchor: "Same-Group-Hit@5 further requires this transaction to belong to the same true laundering group as the target transaction."</sub>
- **descriptive / definition**: Normal-Noise@5 measures the average proportion of normal transactions in the selected top-5 context. (p. 18)[^original]  
  <sub>anchor: "Normal-Noise@5 measures the average proportion of normal transactions in the selected top-5 context."</sub>
- **descriptive / finding or result**: Both datasets achieve 100% Max-24h Coverage, suggesting that laundering transactions exhibit local temporal concentration. (p. 18)[^original]  
  <sub>anchor: "Both datasets achieve 100% Max-24h Coverage, suggesting that laundering transactions do exhibit local temporal concentration."</sub>
- **descriptive / finding or result**: The different effects of LTCE across datasets are not caused by a complete failure of the 24-hour window; they mainly stem from the quality of the selected top-5 historical transactions. (p. 18)[^original]  
  <sub>anchor: "Therefore, the different effects of LTCE across datasets are not caused by a complete failure of the 24-hour window."</sub>
- **descriptive / finding or result**: HI-Small has higher Laundering-Hit@5 and Same-Group-Hit@5 than HI-Medium, while its Normal-Noise@5 is lower. (p. 18)[^original]  
  <sub>anchor: "Specifically, HI-Small has higher Laundering-Hit@5 and Same-Group-Hit@5 than HI-Medium, while its Normal-Noise@5 is lower."</sub>
- **descriptive / finding or result**: The authors interpret that in HI-Small same-group laundering transactions are more likely among the nearest historical transactions, with less interference from normal transactions. (p. 18)[^original]  
  <sub>anchor: "This indicates that, in HI-Small, same-group laundering transactions are more likely to appear among the nearest historical transactions of the target transaction"</sub>
- **descriptive / finding or result**: HI-Medium also shows local temporal patterns but contains a higher density of irrelevant transactions within short time periods. (p. 18)[^original]  
  <sub>anchor: "although HI-Medium also shows local temporal patterns, it contains a higher density of irrelevant transactions within short time periods."</sub>
- **descriptive / limitation**: In HI-Medium the top-5 transactions are more likely to include normal-transaction noise, which limits the benefit of LTCE. (p. 18)[^original]  
  <sub>anchor: "As a result, the top-5 transactions selected in HI- Medium are more likely to include normal-transaction noise, which limits the benefit of LTCE."</sub>
- **descriptive / finding or result**: Fig. 1(a) shows that most target laundering transactions fall into the high-density range within the bidirectional 24-hour window, indicating LTCE usually has sufficient context. (p. 18)[^original]  
  <sub>anchor: "Fig. 1(a) shows that most target laundering transactions fall into the high-density range within the bidirectional 24-hour window"</sub>
- **descriptive / method**: LTCE uses a fixed 24-hour window and takes as its local temporal context the five historical transactions closest in time that share accounts with the target. (p. 18)[^original]  
  <sub>anchor: "LTCE uses a fixed 24-hour time window and selects the top-5 historical transactions"</sub>
- **descriptive / finding or result**: Where most samples sit in the high-density range, Fig. 1(b) and 1(c) report that Same-Group-Hit@5 on HI-Small is about 18.2% higher than on a comparison dataset whose name is cut off in the excerpt. (p. 18)[^original]  
  <sub>anchor: "in the high-density range where most samples are located, Same- Group-Hit@5 on HI-Small is about 18.2% higher than that on"</sub>
- **descriptive / data or feature**: Table II reports precision and F1 of LIC construction methods (NE, NE+ch, NE+cy, SACC) for k=1, 2 and 3 hops, under core and peripheral clue positions, on HI-Small and HI-Medium. (p. 19)[^original]  
  <sub>anchor: "PRECISION AND F1 OF LIC CONSTRUCTION METHODS UNDER DIFFERENT CLUE POSITIONS AND K-HOP."</sub>
- **descriptive / finding or result**: At k=1 on HI-Small, NE attains precision 0.5763 (core) and 0.5215 (peripheral); NE+ch 0.5446 and 0.4898; NE+cy 0.5877 and 0.5318; SACC 0.5479 and 0.4931. (p. 19)[^original]  
  <sub>anchor: "NE 0.5763 0.5215 0.3751 0.2644 0.5477 0.4359 0.3415 0.2209"</sub>
- **descriptive / finding or result**: At k=1 on HI-Small, F1 is 0.3751 (core) and 0.2644 (peripheral) for NE; 0.4509 and 0.3403 for NE+ch; 0.3963 and 0.2838 for NE+cy; 0.4572 and 0.3466 for SACC. (p. 19)[^original]  
  <sub>anchor: "NE+ch 0.5446 0.4898 0.4509 0.3403 0.4822 0.4082 0.4083 0.2883"</sub>
- **descriptive / finding or result**: At k=1 on HI-Medium, precision is 0.5477 (core) and 0.4359 (peripheral) for NE and NE+cy, and 0.4822 and 0.4082 for NE+ch and SACC; F1 is 0.3415 and 0.2209 for NE and NE+cy, and 0.4083 and 0.2883 for NE+ch and SACC. (p. 19)[^original]  
  <sub>anchor: "SACC 0.5479 0.4931 0.4572 0.3466 0.4822 0.4082 0.4083 0.2883"</sub>
- **descriptive / finding or result**: At k=2 on HI-Small, precision is 0.2920 (core) and 0.3273 (peripheral) for NE; 0.3026 and 0.3344 for NE+ch; 0.2962 and 0.3316 for NE+cy; 0.3040 and 0.3359 for SACC. (p. 19)[^original]  
  <sub>anchor: "k=2 NE 0.2920 0.3273 0.3758 0.4034 0.2304 0.2470 0.3050 0.3010"</sub>
- **descriptive / finding or result**: At k=2, F1 values on HI-Small are 0.3758 (core) and 0.4034 (peripheral) for NE; 0.4023 and 0.4255 for NE+ch; 0.3827 and 0.4102 for NE+cy; 0.4048 and 0.4279 for SACC. (p. 19)[^original]  
  <sub>anchor: "SACC 0.3040 0.3359 0.4048 0.4279 0.2407 0.2540 0.3308 0.3203"</sub>
- **descriptive / finding or result**: At k=2 on HI-Medium, precision is 0.2304 (core) and 0.2470 (peripheral) for NE and NE+cy; 0.2407 and 0.2540 for NE+ch and SACC; F1 is 0.3050 and 0.3010 for NE and NE+cy, and 0.3308 and 0.3203 for NE+ch and SACC. (p. 19)[^original]  
  <sub>anchor: "NE+cy 0.2962 0.3316 0.3827 0.4102 0.2304 0.2470 0.3050 0.3010"</sub>
- **descriptive / finding or result**: At k=3 on HI-Medium, precision for NE is 0.0422 (core) and 0.0554 (peripheral), F1 is 0.0742 and 0.0936; NE+ch and SACC reach 0.0453 and 0.0578 precision and 0.0800 and 0.0983 F1. (p. 19)[^original]  
  <sub>anchor: "SACC 0.0652 0.0833 0.1097 0.1347 0.0453 0.0578 0.0800 0.0983"</sub>
- **descriptive / context**: Fig. 2 shows interactive group recovery performance under including-clue evaluation. (p. 19)[^original]  
  <sub>anchor: "Interactive group recovery performance under including-clue evaluation."</sub>
- **descriptive / finding or result**: Table II at k=3 reports for the NE method on HI-Small core precision 0.0616, peripheral precision 0.0807, core F1 0.1031 and peripheral F1 0.1299, with HI-Medium core precision 0.0422 and peripheral precision 0.0554. (p. 19)[^original]  
  <sub>anchor: "k=3 NE 0.0616 0.0807 0.1031 0.1299 0.0422 0.0554 0.0742 0.0936"</sub>
- **descriptive / finding or result**: At k=3 the NE+ch method on HI-Small has core precision 0.0650, peripheral precision 0.0831, core F1 0.1094 and peripheral F1 0.1344. (p. 19)[^original]  
  <sub>anchor: "NE+ch 0.0650 0.0831 0.1094 0.1344 0.0453 0.0578 0.0800 0.0983"</sub>
- **descriptive / finding or result**: At k=3 the NE+cy method on HI-Small has core precision 0.0621, peripheral precision 0.0813, core F1 0.1041 and peripheral F1 0.1309; on HI-Medium its core precision is 0.0422 and peripheral precision 0.0554, with core F1 0.0742 and peripheral F1 0.0936. (p. 19)[^original]  
  <sub>anchor: "NE+cy 0.0621 0.0813 0.1041 0.1309 0.0422 0.0554 0.0742 0.0936"</sub>
- **descriptive / finding or result**: At k=3 the SACC method has the highest HI-Small core precision in the table, 0.0652, with core F1 0.1097 and peripheral F1 0.1347, and peripheral precision 0.0833. (p. 19)[^original]  
  <sub>anchor: "SACC 0.0652 0.0833 0.1097 0.1347 0.0453 0.0578 0.0800 0.0983"</sub>

---

[previous part](digest-006.md) | [source overview](overview.md)

[^original]: arXiv, "Clue-Guided Money Laundering Group Discovery" (2026-06-24). https://arxiv.org/abs/2606.26189
