---
type: Source Digest
title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph - part 2 of 4 (pp. 7-12)
description: 'Verified paraphrased digest, pp. 7-12: 3 Methodology > 3.6 Evaluation Metrics; 3 Methodology > 3.7 Feature-Matching Ablations; 3 Methodology > 3.8 Hybrid Consensus Policy; and 7 more sections'
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
part: 2
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:34Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:34Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:34Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.23494
  title: Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph
  author: org:arxiv
  last_modified: '2026-04-26T00:00:00Z'
digest_points: 69
---

# Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-12) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.6 Evaluation Metrics

- **descriptive / method**: Static bootstrap uses 1,000 paired resamples of the test universe with K recalculated per resample as floor of beta times resampled universe size, reporting 95% percentile intervals for Jaccard, burden and yield. (p. 7)[^original]  
  <sub>anchor: "1,000 paired resamples from the test universe [Efron and Tibshirani, 1993], with"</sub>
- **descriptive / method**: Hybrid temporal bootstrap resamples the 10 paired timestep-level improvement values (hybrid yield minus best-single yield) 1,000 times, with the resampling unit being the timestep rather than the address, reporting a 95% percentile interval. (p. 7)[^original]  
  <sub>anchor: "1,000 resamples of the 10 paired timestep-level improvement values"</sub>
- **descriptive / method**: Bootstrap seeds start sequentially from 0 in both designs. (p. 7)[^original]  
  <sub>anchor: "Seeds sequential from 0 in both cases."</sub>
- **descriptive / method**: For temporal evaluation the common universe at each timestep is the set of deduplicated addresses with at least one incident transaction at that timestep, and both queues are scored and ranked over this identical set. (p. 7)[^original]  
  <sub>anchor: "the common universe at timestep t is the set of all deduplicated addresses with at least one incident transaction at t"</sub>
- **descriptive / method**: For static evaluation the common universe is all 202,107 deduplicated test addresses; the hybrid evaluation further restricts to addresses scoreable by both pipelines, which in practice equals the active set. (p. 7)[^original]  
  <sub>anchor: "For static evaluation, the common universe is all 202,107 deduplicated test addresses."</sub>
- **descriptive / method**: Platt scaling is implemented with scikit-learn CalibratedClassifierCV using a sigmoid method and prefit cross-validation; the base random forest is trained on the training split and the sigmoid is fitted on its validation-split probabilities, then applied to test scores for ranking. (p. 7)[^original]  
  <sub>anchor: "The base RF is trained on the training split; its predicted probabilities on the validation split are used to fit the sigmoid calibrator."</sub>
- **descriptive / definition**: Expected calibration error uses 10 equal-width bins over the 0 to 1 probability range, weighting absolute gaps between observed positive rate and mean predicted probability by bin counts. (p. 7)[^original]  
  <sub>anchor: "Expected calibration error uses 10 equal-width bins over the [0 _,_ 1] probability range."</sub>
- **descriptive / method**: The activity baseline ranks addresses by raw incident transaction count at each evaluation scope, using both AddrTx and TxAddr edges for temporal evaluation and all test-split transactions for static evaluation; ties are broken arbitrarily by numpy default sort order. (p. 7)[^original]  
  <sub>anchor: "addresses are ranked by raw incident transaction count at each evaluation scope"</sub>
- **descriptive / method**: The activity baseline queue is compared to both detection queues via Jaccard at 1% on the static test universe. (p. 8)[^original]  
  <sub>anchor: "The resulting queue is compared to both detection queues via Jaccard@1% on the static test universe."</sub>
- **descriptive / method**: When addresses tie at the K-th position, all tied addresses are included, so the queue may be slightly larger than K; in reported analyses no boundary tie expansion exceeded 1% of nominal K and all metrics use the post-tie queue size. (p. 8)[^original]  
  <sub>anchor: "all tied addresses are included, potentially producing a queue slightly larger than _K_ ."</sub>
- **descriptive / method**: Degree strata are built by sorting active addresses at each timestep by incident transaction count and dividing them into 10 equal-sized deciles, with tied counts kept in the same decile and residual imbalance absorbed by the last decile. (p. 8)[^original]  
  <sub>anchor: "divided into 10 equal-sized groups (deciles)."</sub>

## 3.7 Feature-Matching Ablations

- **descriptive / context**: The study tests whether transaction-actor disagreement reflects a genuine granularity effect or a feature-set confound, using four controlled regimes. (p. 8)[^original]  
  <sub>anchor: "To distinguish these hypotheses, we construct four controlled regimes:"</sub>
- **descriptive / method**: Shared-core regime keeps 17 transaction features and 23 actor features matched by semantic category: degree, BTC value summaries, transaction count or volume, and address count. (p. 8)[^original]  
  <sub>anchor: "17 transaction features and 23 actor features selected by semantic overlap."</sub>
- **descriptive / method**: Matching pairs features from the 182 transaction features and 55 actor features whose column names indicate the same quantity, covering in-degree, out-degree, total degree, BTC value statistics for incoming and outgoing, transaction count, and input/output address counts. (p. 8)[^original]  
  <sub>anchor: "identify pairs whose column names indicate the same underlying quantity."</sub>
- **descriptive / method**: The 17 versus 23 asymmetry arises because some actor features have multiple transaction-side analogs that collapse to one semantic category; the counts are locked in ablation_results.json. (p. 8)[^original]  
  <sub>anchor: "The asymmetry (17 vs 23) arises because some actor features have multiple transaction-side analogs that collapse to one semantic category."</sub>
- **descriptive / method**: Actor-enriched regime gives the actor model its 55 original features plus 182 transaction features aggregated by mean across incident transactions, yielding 237 dimensions. (p. 8)[^original]  
  <sub>anchor: "The actor model receives all 55 original actor features plus 182 transaction features aggregated by mean across incident transactions."</sub>
- **descriptive / method**: Aggregation uses a causal horizon: timesteps 1 to 34 for training actors, 1 to 39 for validation actors, and 1 to 49 for static test actors. (p. 8)[^original]  
  <sub>anchor: "for training actors, only transactions from timesteps 1–34; for validation actors, timesteps 1–39; for test actors (static evaluation), timesteps 1–49."</sub>
- **descriptive / method**: Test actors with no incident transactions within the horizon keep their 55 static features with the 182 aggregated columns set to zero. (p. 8)[^original]  
  <sub>anchor: "Test actors with no incident transactions within this horizon retain their 55 static features with the 182 aggregated columns set to zero."</sub>
- **descriptive / method**: The enriched actor queue is compared against the main static RF transaction-level Platt queue (30.2% illicit per 100), described as the strongest test of the information-confound hypothesis. (p. 9)[^original]  
  <sub>anchor: "The enriched actor queue is compared against the main static RF transactionlevel Platt queue (30.2% illicit per 100), providing the strongest test of the information-confound hypothesis."</sub>
- **descriptive / method**: Low-info shared regime uses four identically defined features per level: for actors, degree, total volume, mean value and mean timestep of incident transactions; for transactions, the corresponding quantities over 1-hop neighbour transactions. (p. 8)[^original]  
  <sub>anchor: "Four features per level, identically defined."</sub>
- **descriptive / method**: Isolated transaction nodes with degree 0 receive zero for all four low-info features. (p. 8)[^original]  
  <sub>anchor: "Isolated transaction nodes (degree 0) receive zero for all four features."</sub>
- **descriptive / method**: PCA count-matched regime extracts 55 principal components from the 182 transaction features using sklearn PCA with full solver, centering, no standardisation and random state 42, fit on the training split only, retaining 99.9999% of variance. (p. 9)[^original]  
  <sub>anchor: "55 principal components extracted from 182 transaction features via sklearn PCA"</sub>
- **descriptive / method**: All ablation models use the same RF hyperparameters as the main model and are Platt-calibrated on the validation split, and all are evaluated on the static test universe with K equal to 2,021 at 1% budget. (p. 9)[^original]  
  <sub>anchor: "All ablation models use the same RF hyperparameters (§3.5) and are Platt-calibrated on the validation split."</sub>
- **descriptive / definition**: Verdict logic: if all primary regime Jaccards are below 0.80 the disagreement is granularity-driven; if all are at or above 0.80 it is information-driven; otherwise mixed. The 0.80 threshold was prespecified as a heuristic before examining ablation results. (p. 9)[^original]  
  <sub>anchor: "The 0.80 threshold is a prespecified heuristic chosen before examining ablation results."</sub>

## 3.8 Hybrid Consensus Policy

- **descriptive / method**: The exploratory hybrid policy computes the geometric mean of transaction-projected and actor Platt scores for each address in the common universe and selects the top floor(alpha K) by consensus score. (p. 9)[^original]  
  <sub>anchor: "compute the geometric mean of transactionprojected and actor-level Platt scores."</sub>
- **descriptive / method**: Among remaining addresses, the hybrid computes disagreement as the absolute difference of the two scores and selects the top K minus floor(alpha K) by maximum score from those exceeding threshold delta. (p. 9)[^original]  
  <sub>anchor: "Select the top-( _K −⌊αK⌋_ ) by max( _stx, sactor_ ) from those exceeding disagreement threshold _δ_ ."</sub>
- **descriptive / method**: Alpha is searched over 0.5 to 0.9 in steps of 0.1 and delta over 0.1 to 0.5 in steps of 0.1 by grid search on the validation split, maximising top-K illicit fraction at 1% budget. (p. 9)[^original]  
  <sub>anchor: "are tuned by grid search on the validation split, maximizing top- _K_ illicit fraction at 1% budget."</sub>
- **descriptive / finding or result**: Tuned values are alpha 0.9 and delta 0.3; on validation at 1% budget (K=323) all 323 top-ranked addresses are illicit, and the true yield is 323 of 1,756 validation illicit addresses, about 0.184. (p. 9)[^original]  
  <sub>anchor: "On validation at 1% budget ( _K_ = 323), all 323 top-ranked addresses are illicit"</sub>
- **descriptive / method**: All three queues (hybrid, transaction and actor) are evaluated on an identical common universe per timestep and per static evaluation, ensuring comparable denominators. (p. 9)[^original]  
  <sub>anchor: "All three queues—hybrid, transaction, and actor—are evaluated on an identical common universe per timestep and per static evaluation"</sub>

## 4.1 Queue Disagreement (H1)

- **descriptive / finding or result**: Temporal: across 10 test timesteps at 1% budget, mean Jaccard is 0.374 (SD 0.171); per-timestep values range from 0.136 at t49 to 0.633 at t42, and at no timestep does Jaccard exceed 0.65. (p. 9)[^original]  
  <sub>anchor: "Across 10 test timesteps at 1% budget, mean Jaccard = 0.374 (SD 0.171)."</sub>
- **descriptive / finding or result**: Static: pooled over all 202,107 test addresses with K equal to 2,021, Jaccard is 0.087 with 95% CI 0.079 to 0.094, so only 8.7% of the union of the two top-1% queues is shared. (p. 10)[^original]  
  <sub>anchor: "Pooled across all test addresses ( _n_ = 202 _,_ 107, _K_ = 2 _,_ 021), Jaccard = 0.087, 95% CI [0.079, 0.094]."</sub>
- **descriptive / finding or result**: The static bootstrap interval is narrow, which the authors read as high precision under the chosen resampling scheme. (p. 10)[^original]  
  <sub>anchor: "The bootstrap CI is narrow, indicating high precision under the chosen resampling scheme."</sub>
- **descriptive / finding or result**: Budget sensitivity: static Jaccard rises from 0.000 at 0.1% budget to 0.152 at 5%, remaining below 0.2 even at 5%, so disagreement is not confined to a thin top slice. (p. 10)[^original]  
  <sub>anchor: "static Jaccard rises from 0.000 at 0.1% to 0.152 at 5%."</sub>
- **descriptive / finding or result**: Degree-1 stratum (addresses with exactly one incident transaction, where projection is the identity) has mean Jaccard at 1% of 0.470 across 10 test timesteps, ranging from 0.238 at t48 to 0.689 at t40; queues still disagree substantially in this stratum. (p. 10)[^original]  
  <sub>anchor: "exhibit a mean Jaccard@1% of 0.470 across 10 test timesteps (range: 0.238 at _t_ 48 to 0.689 at _t_ 40)."</sub>
- **descriptive / finding or result**: Decile strata: the lowest decile has mean Jaccard 0.498, ranging from 0.286 at t48 to 0.786 at t45, showing a pattern similar to the degree-1 stratum. (p. 10)[^original]  
  <sub>anchor: "the lowest decile has mean Jaccard = 0.498 (range: 0.286 at _t_ 48 to 0.786 at _t_ 45)."</sub>
- **descriptive / finding or result**: The activity-ranked queue shares Jaccard 0.038 with the transaction queue and 0.014 with the actor queue at 1% budget, so both detection queues are far from trivial activity ordering. (p. 10)[^original]  
  <sub>anchor: "A queue ranked by raw transaction count (activity) shares Jaccard = 0.038 with the transaction queue and 0.014 with the actor queue at 1% budget."</sub>

## 4.2 Asymmetric Burden (H2)

- **descriptive / finding or result**: Temporal: at 1% budget the arithmetic mean illicit per 100 reviews is 19.9% for the transaction queue and 32.7% for the actor queue, an average dominated by a few high-performing timesteps. (p. 10)[^original]  
  <sub>anchor: "the arithmetic mean illicit per 100 reviews is 19.9% for the transaction queue and 32.7% for the actor queue."</sub>
- **descriptive / finding or result**: At timestep 46 the actor queue achieves 91.2% illicit per 100 reviews (reviews per true positive 1.10) versus 37.6% for the transaction queue; at t49 actor reaches 94.2% versus 41.3%. (p. 10)[^original]  
  <sub>anchor: "At timestep 46, the actor queue achieves 91.2% illicit per 100 reviews (reviews/TP = 1.10) versus 37.6% for the transaction queue."</sub>
- **descriptive / finding or result**: At t42 the transaction queue dominates with 52.9% versus 47.4% for the actor queue. (p. 10)[^original]  
  <sub>anchor: "At _t_ 42, the transaction queue dominates: 52.9% versus 47.4%."</sub>
- **descriptive / finding or result**: At t43 and t45 both queues produce near-zero detection; at t45 there are 29 illicit among 25,060 active addresses, 0.12% prevalence. (p. 10)[^original]  
  <sub>anchor: "t 45: 29 illicit among 25,060 active addresses, 0.12% prevalence)."</sub>
- **descriptive / finding or result**: The K-weighted means, which account for differing active set sizes, are 20.5% for the transaction queue and 29.1% for the actor queue. (p. 10)[^original]  
  <sub>anchor: "The _K_ -weighted means—which account for differing active set sizes—are 20.5% (transaction) and 29.1% (actor)."</sub>
- **descriptive / finding or result**: Static: transaction queue 30.2% illicit per 100 (CI 27.7 to 32.3); actor queue 3.4% (CI 2.7 to 4.1); burden difference 26.8 percentage points (CI 24.3 to 28.9). (p. 10)[^original]  
  <sub>anchor: "Transaction: 30.2% illicit per 100, CI [27.7, 32.3]. Actor: 3.4%, CI [2.7, 4.1]."</sub>
- **descriptive / finding or result**: The static actor queue is dominated by unknown-status addresses, which make up 89.4% of the top-K. (p. 10)[^original]  
  <sub>anchor: "The static actor queue is dominated by unknown-status addresses (89.4% of top- _K_ )."</sub>
- **descriptive / finding or result**: Case fragmentation: across temporal test timesteps at 1% budget, mean fragmentation is 0.474, ranging from 0.158 at t44 to 0.812 at t42. (p. 10)[^original]  
  <sub>anchor: "mean fragmentation is 0.474 (range: 0.158 at _t_ 44 to 0.812 at _t_ 42)."</sub>
- **descriptive / finding or result**: Labeled-only sensitivity: restricting burden to labeled addresses gives temporal means of 52.2% for transaction and 53.2% for actor, so the gap narrows substantially, suggesting much of the burden difference is driven by ranking of unlabeled addresses. (p. 10)[^original]  
  <sub>anchor: "the temporal means are 52.2% (transaction) and 53.2% (actor) illicit per 100."</sub>

## 4.3 Quality-Disentanglement

- **descriptive / definition**: The actor-only illicit rate is the fraction of illicit addresses ranked in the actor top-K but not in the transaction top-K, while actor queue burden is the illicit fraction of the entire actor top-K; these are different quantities. (p. 11)[^original]  
  <sub>anchor: "The actor-only illicit rate measures the fraction of illicit addresses among those ranked in the actor queue’s top- _K_ but not in the transaction queue’s top- _K_ ."</sub>
- **descriptive / finding or result**: Static actor-only illicit rate is 0.24%, below the 1.55% base rate, yielding a verdict of representation weakness. (p. 11)[^original]  
  <sub>anchor: "The static actor-only illicit rate (0.24%) falls below the base rate (1.55%), yielding a verdict of representation weakness."</sub>
- **descriptive / finding or result**: Temporal actor-only illicit rate averages 29.7% across 10 test timesteps but ranges from 0.0% at t43, t45, t47 and t48 to 100% at t46 and t49, where every actor-unique address is illicit. (p. 11)[^original]  
  <sub>anchor: "The temporal actor-only illicit rate averages 29.7% across 10 test timesteps"</sub>
- **descriptive / finding or result**: Actor queue burden peaks at 91.2% at t46 and 94.2% at t49 illicit per 100 reviews and falls to 0.0% at t45 and t47. (p. 11)[^original]  
  <sub>anchor: "the actor queue burden peaks at 91.2% ( _t_ 46) and 94.2% ( _t_ 49) illicit per 100 reviews, while falling to 0.0% at _t_ 45 and _t_ 47."</sub>
- **descriptive / finding or result**: The authors attribute the temporal pattern to heterogeneity: static actor features are globally constant with zero variation across 273,268 multi-occurrence addresses, producing a weak pooled classifier. (p. 11)[^original]  
  <sub>anchor: "Static actor features are globally constant— zero variation across 273,268 multi-occurrence addresses—producing a weak pooled classifier."</sub>
- **descriptive / finding or result**: Causal Path A features, reconstructed from incident transactions up to each evaluation timestep, produce regime-dependent value concentrated in specific timesteps. (p. 11)[^original]  
  <sub>anchor: "Causal Path A features, reconstructed from incident transactions up to each evaluation timestep (§3.3), produce regime-dependent value that concentrates in specific timesteps."</sub>

## 4.4 Feature-Matching Ablations (H1 Robustness)

- **descriptive / finding or result**: All three primary ablation regimes give Jaccard@1% below 0.80 under the primary noisy-OR operator on static evaluation, yielding an overall verdict of granularity-driven disagreement. (p. 11)[^original]  
  <sub>anchor: "All three primary ablation regimes produce Jaccard@1% below 0.80 under the primary noisy-OR operator on static evaluation"</sub>
- **descriptive / finding or result**: Shared-core regime gives Jaccard 0.061; transaction queue 11.7% illicit per 100 and actor queue 5.6%, so queues still diverge with matched feature semantics. (p. 11)[^original]  
  <sub>anchor: "Shared-core ( _ntx_ = 17, _nactor_ = 23): Jaccard = 0.061. Transaction queue: 11.7% illicit per 100. Actor queue: 5.6%."</sub>
- **descriptive / finding or result**: Actor-enriched regime gives Jaccard 0.051; the main transaction queue is 30.2% illicit per 100 and the enriched actor queue 4.3%, so giving the actor model all transaction features via mean aggregation does not produce a similar queue. (p. 11)[^original]  
  <sub>anchor: "Actor-enriched ( _nactor_ = 237): Jaccard = 0.051. Transaction queue (main RF, 182 features): 30.2% illicit per 100. Actor queue (55 + 182 aggregated): 4.3%."</sub>
- **descriptive / finding or result**: Low-info shared regime gives Jaccard 0.082; transaction 15.4% and actor 8.0% illicit per 100, slightly more overlap than the full models but far below 0.80. (p. 11)[^original]  
  <sub>anchor: "Low-info shared ( _n_ = 4 per level): Jaccard = 0.082. Transaction: 15.4% illicit per 100. Actor: 8.0%."</sub>
- **descriptive / finding or result**: PCA count-matched regime gives Jaccard 0.355 between the PCA-reduced and main transaction queues and 0.042 against the original actor queue, showing near-lossless reduction does not preserve top-K ranking. (p. 11)[^original]  
  <sub>anchor: "Jaccard of PCA-reduced transaction queue versus main transaction queue = 0.355; versus original actor queue = 0.042."</sub>
- **descriptive / finding or result**: The authors interpret the enrichment result as possibly reflecting that averaging features over a variable number of incident transactions attenuates the per-transaction signal used in transaction-level scoring. (p. 11)[^original]  
  <sub>anchor: "One interpretation is that computing feature means across a variable number of incident transactions attenuates the per-transaction signal"</sub>

## 4.5 Projection Sensitivity

- **descriptive / finding or result**: At timestep 46 noisy-OR gives Jaccard 0.160 while top-m mean gives 0.631; at timestep 49 capped-sum gives 0.136 while top-m mean gives 0.681. (p. 11)[^original]  
  <sub>anchor: "At timestep 46 (high disagreement), noisy-OR yields Jaccard = 0.160 while top- _m_ mean yields 0.631."</sub>
- **descriptive / finding or result**: The operator ranking is not consistent across timesteps: noisy-OR and max-score exceed capped-sum and top-m mean at t40 to t42, while top-m mean is highest and noisy-OR and capped-sum lowest at t46 and t49. (p. 11)[^original]  
  <sub>anchor: "The operator ranking is not consistent across timesteps"</sub>
- **descriptive / finding or result**: Direction sensitivity: input-side (spending) transactions only give a temporal mean Jaccard of 0.383, and output-side (receiving) only give 0.109. (p. 11)[^original]  
  <sub>anchor: "Using input-side (spending) transactions only yields a temporal mean Jaccard of 0.383; output-side (receiving) only yields 0.109."</sub>
- **descriptive / context**: The authors state that no tested operator eliminates disagreement entirely and that they do not claim a projection-independent granularity effect. (p. 11)[^original]  
  <sub>anchor: "The paper does not claim a projectionindependent granularity effect."</sub>

## 4.6 Hybrid Policy (H3)

- **descriptive / finding or result**: The tuned hybrid (alpha 0.9, delta 0.3) fails to outperform the best single-level queue on the temporal horizon. (p. 11)[^original]  
  <sub>anchor: "The hybrid consensus policy (tuned: _α_ = 0 _._ 9, _δ_ = 0 _._ 3) fails to outperform the best single-level queue on the temporal test horizon."</sub>
- **descriptive / finding or result**: Temporal: mean hybrid yield 13.3% versus mean best-single yield 18.3%; mean improvement is -5.05 percentage points with 95% CI from -10.2 to -0.9 percentage points, entirely below zero. (p. 12)[^original]  
  <sub>anchor: "Mean improvement = _−_ 5.05pp, 95% CI [ _−_ 10.2pp, _−_ 0.9pp]."</sub>
- **descriptive / finding or result**: The hybrid loses because the best single queue switches between transaction and actor across timesteps, with actor dominating at t44, t46 and t49 and transaction at t40 and t42, and a fixed-weight combination cannot track these regime changes. (p. 12)[^original]  
  <sub>anchor: "a fixed-weight combination cannot track these regime changes."</sub>
- **descriptive / finding or result**: Static: hybrid 39.4% illicit per 100 versus transaction 30.2% and actor 3.4%, so the hybrid outperforms either single queue in the pooled setting. (p. 12)[^original]  
  <sub>anchor: "Hybrid: 39.4% illicit per 100. Transaction: 30.2%. Actor: 3.4%."</sub>
- **descriptive / finding or result**: At t46 actor scores 91.2% and hybrid 54.7%; at t49 actor 94.2% and hybrid 51.2%, so the hybrid dilutes the actor signal with the weaker transaction component. (p. 12)[^original]  
  <sub>anchor: "At timesteps where the actor queue dominates ( _t_ 46: actor 91.2%, hybrid 54.7%; _t_ 49: actor 94.2%, hybrid 51.2%), the hybrid dilutes the actor signal"</sub>
- **descriptive / finding or result**: At dead-zone timesteps t45 and t47, where both queues are at 0%, the hybrid cannot improve on zero. (p. 12)[^original]  
  <sub>anchor: "At dead-zone timesteps ( _t_ 45, _t_ 47: both queues at 0%), the hybrid cannot improve on zero."</sub>

## 4.7 Novel-Positive Rate

- **descriptive / finding or result**: Most illicit addresses at each test timestep are newly appearing rather than carried over: 98.4% (444 of 451) at t40, 99.8% (505 of 506) at t46, and 99.5% (649 of 652) at t49. (p. 12)[^original]  
  <sub>anchor: "At _t_ 40, 98.4% of all illicit addresses at that timestep (444 of 451) are novel"</sub>
- **descriptive / context**: The authors conclude that a queue relying mainly on re-flagging previously known illicit addresses would miss most illicit activity at each timestep on this dataset. (p. 12)[^original]  
  <sub>anchor: "a queue relying primarily on re-flagging previously known illicit addresses would miss the vast majority of illicit activity at each timestep."</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph" (2026-04-26). https://arxiv.org/abs/2604.23494
