---
type: Source Digest
title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph - part 4 of 4 (pp. 17-20)
description: 'Verified paraphrased digest, pp. 17-20: A Per-Timestep Results; B Degree-Strata Analysis; C Reproducibility; and 1 more sections'
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
part: 4
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
digest_points: 32
---

# Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph (digest)

[previous part](digest-003.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 17-20) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## A Per-Timestep Results

- **descriptive / method**: Table 1 reports results for all 10 test timesteps at the 1% budget under noisy-OR projection. (p. 17)[^original]  
  <sub>anchor: "Table 1 reports all 10 test timesteps at 1% budget under noisy-OR projection."</sub>
- **descriptive / finding or result**: Table 1, timestep 40: 26,723 active addresses, 451 illicit, K 267, J@1% 0.618, transaction illicit per 100 26.6, actor illicit per 100 18.4, transaction yield 15.7%, actor yield 10.9%, fragmentation 0.356. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 41: 22,253 active addresses, 179 illicit, K 222, J@1% 0.547, transaction illicit per 100 36.9, actor illicit per 100 39.2, transaction yield 45.8%, actor yield 48.6%, fragmentation 0.694. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 42: 32,531 active addresses, 410 illicit, K 325, J@1% 0.633, transaction illicit per 100 52.9, actor illicit per 100 47.4, transaction yield 42.0%, actor yield 37.6%, fragmentation 0.812. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 43: 24,600 active addresses, 103 illicit, K 246, J@1% 0.359, transaction illicit per 100 0.4, actor illicit per 100 0.4, transaction yield 1.0%, actor yield 1.0%, fragmentation 0.585. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 44: 19,668 active addresses, 284 illicit, K 196, J@1% 0.221, transaction illicit per 100 2.0, actor illicit per 100 36.7, transaction yield 1.4%, actor yield 25.4%, fragmentation 0.158. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 45: 25,060 active addresses, 29 illicit, K 250, J@1% 0.412, zero illicit per 100 for both queues, zero yield for both queues, fragmentation 0.524. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 46: 18,184 active addresses, 506 illicit, K 181, J@1% 0.160, transaction illicit per 100 37.6, actor illicit per 100 91.2, transaction yield 13.4%, actor yield 32.6%, fragmentation 0.298. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 47: 21,079 active addresses, 203 illicit, K 210, J@1% 0.377, zero illicit per 100 for both queues, zero yield for both queues, fragmentation 0.633. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 48: 18,717 active addresses, 388 illicit, K 187, J@1% 0.276, transaction illicit per 100 1.6, actor illicit per 100 0.0, transaction yield 0.8%, actor yield 0.0%, fragmentation 0.433. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Table 1, timestep 49: 12,199 active addresses, 652 illicit, K 121, J@1% 0.136, transaction illicit per 100 41.3, actor illicit per 100 94.2, transaction yield 7.7%, actor yield 17.5%, fragmentation 0.248. (p. 17)[^original]  
  <sub>anchor: "Table 1: Per-timestep results at 1% budget"</sub>
- **descriptive / finding or result**: Timesteps 45 and 47 show zero detection at the 1% budget for both queues. (p. 17)[^original]  
  <sub>anchor: "Note: _t_ 45 and _t_ 47 have zero detection at 1% budget for both queues."</sub>

## B Degree-Strata Analysis

- **descriptive / method**: At each test timestep the active address set is split into 10 equal-sized deciles by incident transaction count, and Jaccard@1% is computed within each stratum. (p. 17)[^original]  
  <sub>anchor: "stratified into 10 equal-sized deciles by incident transaction count"</sub>
- **descriptive / method**: Jaccard@1% is computed separately within each degree stratum at every test timestep. (p. 17)[^original]  
  <sub>anchor: "Jaccard@1% is computed within each stratum."</sub>
- **descriptive / finding or result**: Table 2 reports lowest-degree decile 1 universe sizes, K and Jaccard@1% for timesteps 40 to 49: 2,673/26/0.677; 2,226/22/0.517; 3,254/32/0.306; 2,460/24/0.412; 1,967/19/0.583; 2,506/25/0.786; 1,819/18/0.500; 2,108/21/0.313; 1,872/18/0.286; 1,220/12/0.600. (p. 17)[^original]  
  <sub>anchor: "Table 2: Lowest-degree decile (decile 1) Jaccard@1% per timestep"</sub>
- **descriptive / finding or result**: Across the ten timesteps, the mean decile 1 Jaccard@1% is 0.498 with a standard deviation of 0.160. (p. 17)[^original]  
  <sub>anchor: "Table 2: Lowest-degree decile (decile 1) Jaccard@1% per timestep"</sub>

## A Per-Timestep Results

- **descriptive / definition**: Frag in Table 1 denotes case fragmentation, and the note records zero detection at 1% budget for both queues at t 45 and t 47. (p. 17)[^original]  
  <sub>anchor: "Note: _t_ 45 and _t_ 47 have zero detection at 1% budget for both queues. Frag = case fragmentation."</sub>

## B Degree-Strata Analysis

- **descriptive / finding or result**: Table 3 reports exact degree-1 address Jaccard@1% for timesteps 40 to 49: 0.689, 0.528, 0.364, 0.455, 0.412, 0.460, 0.598, 0.283, 0.238 and 0.678. (p. 18)[^original]  
  <sub>anchor: "Table 3: Exact degree-1 addresses Jaccard@1% per timestep"</sub>
- **descriptive / finding or result**: Across the ten timesteps, the mean exact degree-1 Jaccard@1% is 0.470 with a standard deviation of 0.146. (p. 18)[^original]  
  <sub>anchor: "Table 3: Exact degree-1 addresses Jaccard@1% per timestep"</sub>
- **descriptive / finding or result**: For degree-1 addresses the projection operator is the identity function. (p. 18)[^original]  
  <sub>anchor: "For these addresses the projection operator is the identity function"</sub>
- **descriptive / limitation**: The authors interpret remaining disagreement among degree-1 addresses as consistent with differences in the underlying classifiers, not with multi-incident aggregation ambiguity. (p. 18)[^original]  
  <sub>anchor: "remaining disagreement is consistent with differences in the underlying classifiers"</sub>

## C Reproducibility

- **descriptive / context**: All results are derived from locked output files. (p. 18)[^original]  
  <sub>anchor: "All results are derived from locked output files"</sub>
- **descriptive / data or feature**: SHA-256 hashes are given for data_prep.json, rf_results.json, ablation_results.json and hybrid_results.json, with full hashes in supplementary material. (p. 18)[^original]  
  <sub>anchor: "All results are derived from locked output files. SHA-256 hashes:"</sub>
- **descriptive / context**: Full hash values are provided in the supplementary material. (p. 18)[^original]  
  <sub>anchor: "Full hashes in supplementary material. Software: Python 3.10.12"</sub>
- **descriptive / context**: Software used was Python 3.10.12, scikit-learn 1.3.2 and numpy 1.24.4. (p. 18)[^original]  
  <sub>anchor: "Software: Python 3.10.12, scikit-learn 1.3.2, numpy 1.24.4."</sub>
- **descriptive / method**: Random state 42 is used for RF training, and bootstrap seeds run sequentially from 0. (p. 18)[^original]  
  <sub>anchor: "Random state: 42 (RF training), bootstrap seeds sequential from 0."</sub>
- **descriptive / context**: Hardware was a single machine with a 12-core CPU and 32 GB RAM, with no GPU used. (p. 19)[^original]  
  <sub>anchor: "no GPU used. Total pipeline runtime under 30 minutes."</sub>
- **descriptive / finding or result**: Total pipeline runtime was under 30 minutes. (p. 19)[^original]  
  <sub>anchor: "no GPU used. Total pipeline runtime under 30 minutes."</sub>

## D Shared-Core Feature Mapping

- **descriptive / method**: The shared-core ablation uses 17 transaction features and 23 actor features chosen by semantic column-name overlap. (p. 19)[^original]  
  <sub>anchor: "uses 17 transaction features and 23 actor features selected by semantic column-name overlap"</sub>
- **descriptive / data or feature**: Table 4 lists the 17 transaction-side shared-core features: in_txs_degree, out_txs_degree, in_BTC_total, in_BTC_mean, in_BTC_median, in_BTC_max, in_BTC_min, out_BTC_total, out_BTC_mean, out_BTC_median, out_BTC_max, out_BTC_min, total_BTC, fees, size, num_input_addresses and num_output_addresses. (p. 19)[^original]  
  <sub>anchor: "Table 4: Transaction-side shared-core features (17)"</sub>
- **descriptive / data or feature**: Actor-side column names are taken from the public Elliptic++ wallets_features.csv header, and the count of 23 is locked in ablation_results.json. (p. 20)[^original]  
  <sub>anchor: "actor column names are from the public Elliptic++ wallets_features.csv header"</sub>
- **descriptive / data or feature**: Table 5 lists the 23 actor-side shared-core features: in and out degree, incoming and outgoing BTC value statistics (total, mean, median, max, min, std), total_BTC, fee statistics (mean, median, std), size statistics (mean, median, std), and input and output address counts. (p. 20)[^original]  
  <sub>anchor: "The shared-core ablation (§3.7) uses 17 transaction features and 23 actor features selected by semantic column-name overlap."</sub>

---

[previous part](digest-003.md) | [source overview](overview.md)

[^original]: arXiv, "Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph" (2026-04-26). https://arxiv.org/abs/2604.23494
