---
type: Source Digest
title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph - part 3 of 4 (pp. 12-17)
description: 'Verified paraphrased digest, pp. 12-17: 5 Discussion > 5.1 Practical Implications for Queue Design; 5 Discussion > 5.2 The Temporal Heterogeneity Story; 5 Discussion > 5.3 Why Enrichment Fails; and 5 more sections'
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
part: 3
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
digest_points: 40
---

# Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 12-17) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 5.1 Practical Implications for Queue Design

- **descriptive / finding or result**: At a 1% review budget on Elliptic++, the transaction-level and actor-level queues have a Jaccard overlap of 0.087 in static evaluation and 0.374 on average across temporal test periods. (p. 12)[^original]  
  <sub>anchor: "At a 1% review budget on Elliptic++, the two queues have a Jaccard overlap of only 0.087 in static evaluation"</sub>
- **descriptive / finding or result**: The transaction queue is more efficient in static evaluation, with 30.2% illicit per 100 reviews versus 3.4% for the actor queue. (p. 12)[^original]  
  <sub>anchor: "The transaction queue is more efficient in static evaluation (30.2% illicit per 100 versus 3.4%)"</sub>
- **descriptive / finding or result**: The actor queue dominates at specific temporal regimes, reaching 91.2% illicit per 100 at timestep 46. (p. 12)[^original]  
  <sub>anchor: "but the actor queue dominates at specific temporal regimes ( _t_ 46: 91.2%)"</sub>
- **descriptive / context**: A compliance manager faces a choice between committing to one granularity level, which is simpler but forfeits episodic gains from the other, or maintaining parallel queues, which is costlier but captures temporal complementarity. (p. 12)[^original]  
  <sub>anchor: "commit to one granularity level (simpler, but forfeits episodic gains from the other) or maintain parallel queues"</sub>

## 5.2 The Temporal Heterogeneity Story

- **descriptive / finding or result**: The actor-level classifier oscillates between near-zero performance at timesteps 43 and 45 and exceptionally high top-K illicit rate at timestep 46 (91.2% illicit per 100 reviews). (p. 12)[^original]  
  <sub>anchor: "The actor-level classifier oscillates between near-zero performance ( _t_ 43, _t_ 45) and exceptionally high top- _K_ illicit rate"</sub>
- **descriptive / context**: The authors interpret the temporal variation as consistent with Elliptic++ structure: actor features are globally static, so actor model discrimination depends entirely on causally reconstructed features whose informativeness varies with recent transaction history. (p. 12)[^original]  
  <sub>anchor: "actor features are globally static, so the actor model’s discrimination depends entirely on causally reconstructed features"</sub>
- **descriptive / finding or result**: A geometric-mean combination with fixed weights cannot adapt to which queue is dominant at a given timestep, which the authors give as why the fixed hybrid fails. (p. 12)[^original]  
  <sub>anchor: "A geometric-mean combination with fixed weights cannot adapt to which queue is dominant at a given timestep"</sub>
- **recommended / recommendation**: An adaptive switching policy selecting the transaction or actor queue per timestep based on a regime indicator is described as the natural next step, requiring a reliable regime classifier that the authors leave to future work. (p. 12)[^original]  
  <sub>anchor: "An adaptive switching policy—selecting the transaction or actor queue per timestep based on a regime indicator—is the natural next step"</sub>

## 5.3 Why Enrichment Fails

- **descriptive / finding or result**: The actor-enriched ablation with 237 features has a Jaccard overlap of 0.051, consistent with disagreement persisting under mean-aggregation enrichment and noisy-OR projection rather than an information confound. (p. 12)[^original]  
  <sub>anchor: "The actor-enriched ablation (237 features, Jaccard = 0.051) is consistent with disagreement persisting"</sub>
- **descriptive / finding or result**: Even though the actor model receives all transaction features aggregated by mean over incident transactions, it achieves only 4.3% illicit per 100 versus 30.2% for the transaction model. (p. 12)[^original]  
  <sub>anchor: "Yet it achieves only 4.3% illicit per 100 versus 30.2% for the transaction model."</sub>
- **descriptive / finding or result**: The actor-enriched ablation with 237 features (Jaccard = 0.051) is consistent with disagreement persisting under mean-aggregation enrichment and noisy-OR projection, which the authors say is rather than an information confound. (p. 12)[^original]  
  <sub>anchor: "consistent with disagreement persisting under the tested mean-aggregation enrichment and noisy-OR projection"</sub>
- **descriptive / context**: One explanation offered is that mean aggregation over heterogeneous transaction feature vectors loses distributional information such as variance, skewness and extreme values that contributes to per-transaction risk scores. (p. 13)[^original]  
  <sub>anchor: "mean aggregation over heterogeneous transaction feature vectors loses distributional information—variance, skewness, extreme values—"</sub>
- **descriptive / context**: The transaction model can identify a single high-risk transfer among many benign ones, whereas the actor model sees only the average, which may be unremarkable. (p. 13)[^original]  
  <sub>anchor: "The transaction model can identify a single high-risk transfer among many benign ones"</sub>

## 5.4 Limitations

- **descriptive / limitation**: The magnitude of queue disagreement is operator-dependent and the operator ranking is not consistent across timesteps; no tested operator eliminates disagreement entirely. (p. 13)[^original]  
  <sub>anchor: "The magnitude of queue disagreement is operator-dependent and the operator ranking is not consistent across timesteps."</sub>
- **descriptive / limitation**: Quantitative claims about disagreement magnitude are conditioned on the noisy-OR primary operator. (p. 13)[^original]  
  <sub>anchor: "Quantitative claims about disagreement magnitude are conditioned on the noisy-OR primary operator."</sub>
- **descriptive / limitation**: Results are specific to Elliptic++; generalisation to other blockchain graphs, Ethereum token networks, or traditional banking transaction data is not established. (p. 13)[^original]  
  <sub>anchor: "Results are specific to Elliptic++. Generalization to other blockchain graphs, Ethereum token networks, or traditional banking transaction data is not established."</sub>
- **descriptive / definition**: In this study, 'actor' means a blockchain address (a public-key hash), not a resolved real-world entity, customer or account. (p. 13)[^original]  
  <sub>anchor: "Throughout this study, “actor” is a blockchain address (a public-key hash), not a resolved real-world entity"</sub>
- **expected / limitation**: Results should be interpreted as queue-level divergence at the address granularity, with mapping to real-world investigation workflows depending on entity-resolution quality. (p. 13)[^original]  
  <sub>anchor: "Results should be interpreted as queue-level divergence at the address granularity"</sub>
- **descriptive / limitation**: Only random forest is used at both levels; a graph convolutional network was excluded because the address-to-address graph lacks per-timestep edge timestamps, preventing causal temporal masking. (p. 13)[^original]  
  <sub>anchor: "A graph convolutional network was excluded because the Elliptic++ address-to-address graph lacks per-timestep edge timestamps"</sub>
- **descriptive / limitation**: GNN robustness checks are deferred to future work. (p. 13)[^original]  
  <sub>anchor: "GNN robustness checks are deferred to future work."</sub>
- **descriptive / finding or result**: Of 273,268 multi-occurrence addresses in Elliptic++, none exhibit feature variation between occurrences, so all temporal actor signal derives from the Path A causal reconstruction. (p. 13)[^original]  
  <sub>anchor: "Across 273,268 multi-occurrence addresses in Elliptic++, zero exhibit feature variation between occurrences."</sub>
- **descriptive / limitation**: Datasets with genuinely dynamic actor features might yield different results. (p. 13)[^original]  
  <sub>anchor: "Datasets with genuinely dynamic actor features might yield different results."</sub>
- **descriptive / limitation**: Approximately 66% of test actors lack ground-truth labels; illicit-per-100 and yield@K are computed only against known labels, although the burden decomposition's unknown category captures this. (p. 13)[^original]  
  <sub>anchor: "Approximately 66% of test actors lack ground-truth labels."</sub>
- **descriptive / finding or result**: The static RBO point estimate of 2.3×10^-12 has a confidence interval [8.3×10^-10, 4.8×10^-8] that does not bracket the point estimate, due to bootstrap resampling producing different extreme-rank configurations; the authors draw no inferential conclusions from static RBO. (p. 13)[^original]  
  <sub>anchor: "The static RBO point estimate (2 _._ 3 _×_ 10_−_12 ) with CI [8 _._ 3 _×_ 10_−_10 , 4 _._ 8 _×_ 10_−_8 ] does not bracket the point estimate."</sub>
- **descriptive / limitation**: Timesteps 43, 45, 47 and 48 have very low illicit prevalence; at timestep 45, 29 illicit addresses among 25,060 active addresses (0.12%), making queue comparison largely uninformative there. (p. 13)[^original]  
  <sub>anchor: "Timesteps 43, 45, 47, and 48 have very low illicit prevalence"</sub>
- **descriptive / limitation**: The address-to-address edge list of 3,740,066 edges carries no timestep information, precluding per-timestep causal masking of the actor graph. (p. 13)[^original]  
  <sub>anchor: "The address-to-address edge list (3,740,066 edges) carries no timestep information"</sub>
- **descriptive / method**: Static evaluation confidence intervals are based on 1,000 paired bootstrap resamples of the test universe with K recalculated per resample. (p. 13)[^original]  
  <sub>anchor: "Static evaluation confidence intervals are based on 1,000 paired bootstrap resamples of the test universe"</sub>
- **descriptive / limitation**: Timestep dead zones: timesteps 43, 45, 47 and 48 have very low illicit prevalence, and detection is near-zero at these timesteps, so queue comparison there is largely uninformative. (p. 13)[^original]  
  <sub>anchor: "Detection is near-zero at these timesteps, making queue comparison largely uninformative."</sub>
- **descriptive / method**: The hybrid temporal confidence interval uses a separate design: 1,000 resamples of the 10 paired timestep-level improvement values. (p. 14)[^original]  
  <sub>anchor: "The hybrid temporal CI uses a separate design: 1,000 resamples of the 10 paired timestep-level improvement values"</sub>
- **recommended / recommendation**: Possible extensions include an adaptive switching policy, graph neural networks with proper per-timestep causal graph construction, extension to Ethereum or permissioned-ledger datasets, and multi-hop actor aggregation to provide richer features without mean-aggregation information loss. (p. 14)[^original]  
  <sub>anchor: "Multi-hop actor aggregation—using not just incident transactions but their neighborhoods—could provide richer actor features"</sub>

## 6 Conclusion

- **descriptive / finding or result**: On the Elliptic++ Bitcoin dataset under causal temporal evaluation and fixed review budgets, transaction-projected and actor-level queues overlap at Jaccard 0.374 on average across temporal test periods at 1% budget, dropping to 0.087 in static evaluation. (p. 14)[^original]  
  <sub>anchor: "Transaction-projected and actor-level queues overlap at only Jaccard = 0.374 on average across temporal test periods"</sub>
- **descriptive / finding or result**: Even with 237 features the enriched actor model's queue differs sharply from the transaction model's queue (Jaccard 0.051), so disagreement persists after feature-matching controls. (p. 14)[^original]  
  <sub>anchor: "even with 237 features, the enriched actor model’s queue differs sharply from the transaction model’s (Jaccard = 0.051)"</sub>
- **descriptive / finding or result**: Actor-level value is temporally concentrated, with specific timesteps exceeding 91% illicit per 100 reviews while the static actor-queue burden is only 3.4%. (p. 14)[^original]  
  <sub>anchor: "Actor-level value is temporally concentrated, with specific timesteps exceeding 91% illicit per 100 reviews"</sub>
- **descriptive / finding or result**: The fixed hybrid policy underperforms the best single queue by 5.05 percentage points and cannot exploit the temporal structure. (p. 14)[^original]  
  <sub>anchor: "underperforming the best single queue by 5.05 percentage points"</sub>
- **descriptive / finding or result**: Under the primary noisy-OR projection, scoring granularity is a design variable that substantially affects investigative outcomes rather than a detail to be resolved during implementation. (p. 14)[^original]  
  <sub>anchor: "it is a design variable that substantially affects investigative outcomes"</sub>

## Declarations

- **descriptive / context**: The declarations state no external funding, no competing interests, and that ethics approval is not applicable. (p. 14)[^original]  
  <sub>anchor: "Funding: This research received no external funding."</sub>

## 6 Conclusion

- **expected / recommendation**: Compliance teams deploying graph-based detection should explicitly evaluate queue divergence across granularity levels. (p. 14)[^original]  
  <sub>anchor: "Compliance teams deploying graph-based detection should explicitly evaluate queue divergence across granularity levels"</sub>
- **recommended / recommendation**: Compliance teams deploying graph-based detection should consider adaptive policies that can track temporal regime changes. (p. 14)[^original]  
  <sub>anchor: "consider adaptive policies that can track temporal regime changes"</sub>

## Acknowledgments

- **descriptive / context**: The authors disclosed that Claude (Anthropic, Claude Opus model) was used as a coding assistant for the experiment pipeline and as a drafting aid for prose, with the author stating responsibility for design, analysis and claims. (p. 14)[^original]  
  <sub>anchor: "Claude (Anthropic, Claude Opus model) was used in two capacities"</sub>
- **descriptive / data or feature**: The Elliptic++ dataset is publicly available from a GitHub repository, and experiment output files with SHA-256 hashes are supplied as supplementary material; experiment code is available on reasonable request.[^original]  
  <sub>anchor: "The Elliptic++ dataset is publicly available at"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: arXiv, "Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph" (2026-04-26). https://arxiv.org/abs/2604.23494
