---
type: Source Digest
title: Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity - part 2 of 3 (pp. 4-7)
description: 'Verified paraphrased digest, pp. 4-7: 4 RESULTS; 5 CONCLUSION'
resource: https://arxiv.org/abs/2005.14635
tags:
- academic_finding
- advanced_analytics
- global_academic
- ml_statistics
- model_development
- preprint
status: stable
source_id: arxiv-machine-learning-methods-to-detect-money-laundering-in-the-bitco
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2020-05-29'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2005.14635
  title: Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity
  author: org:arxiv
  last_modified: '2020-05-29T00:00:00Z'
digest_points: 31
---

# Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 4-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4 RESULTS

- **descriptive / finding or result**: Table 1 reports illicit F1-scores by contamination level (0.05, 0.1, 0.15, 0.2) for the RF supervised baseline (0.82, 0.58, 0.46, 0.39) and for anomaly detection methods LOF, ABOD, KNN, OCSVM, CBLOF, PCA and IF; all anomaly detectors score far below the RF baseline. (p. 4)[^original]  
  <sub>anchor: "RF supervised baseline 0.82 0.58 0.46 0.39 LOF 0.11 0.15 0.19 0.18 ABOD 0.07 0.07 0.07 0.07"</sub>
- **descriptive / finding or result**: At contamination 0.05 LOF scores 0.11, ABOD 0.07, KNN 0.03, OCSVM 0.01, CBLOF 0.01, PCA 0.01 and IF 0.00 in illicit F1 terms, with the Table 1 figures for the other contamination levels also given. (p. 4)[^original]  
  <sub>anchor: "LOF 0.11 0.15 0.19 0.18 ABOD 0.07 0.07 0.07 0.07 KNN 0.03 0.04 0.05 0.06"</sub>

## 4.1 Supervised baselines

- **descriptive / finding or result**: Over five runs with different seeds, the authors reproduced Weber et al.'s results closely, obtaining illicit F1-scores on the test set of 0.76 for XGBoost, 0.45 for LR and 0.83 for RF. (p. 4)[^original]  
  <sub>anchor: "Over five runs (with different seeds), we achieve an illicit F1- score on the test set of 0.76 for XGBoost, 0.45 for LR, and 0.83 for RF."</sub>
- **descriptive / finding or result**: The RF model gave the best supervised baseline. (p. 4)[^original]  
  <sub>anchor: "Thus, the best supervised baseline is achieved with the RF model."</sub>
- **descriptive / finding or result**: As in Weber et al., model performance was profoundly affected by a sudden dark market shutdown at time-step 43. (p. 4)[^original]  
  <sub>anchor: "we observe that model performance is profoundly affected by a sudden dark market shutdown at time-step 43."</sub>

## 4.2 Anomaly detection

- **descriptive / finding or result**: Anomaly detection methods performed significantly below the RF supervised baseline across all contamination levels. (p. 4)[^original]  
  <sub>anchor: "Anomaly detection methods perform significantly below the RF supervised baseline across all contamination levels."</sub>
- **descriptive / finding or result**: The authors note their results differ from past studies where anomaly detection performed adequately for AML, and suggest those studies often used synthetically generated anomalies that are outliers by design. (p. 4)[^original]  
  <sub>anchor: "we note that these studies often use synthetically generated anomalous data points that are outliers by design."</sub>
- **permissive / context**: The authors suggest there could be differences between money laundering patterns in financial transactions and Bitcoin transfers. (p. 4)[^original]  
  <sub>anchor: "there could be differences between money laundering patterns in financial trans- actions and Bitcoin transfers."</sub>
- **descriptive / finding or result**: In the real-life Bitcoin dataset, illicit cases are not outlying. (p. 4)[^original]  
  <sub>anchor: "In the real-life Bitcoin transaction dataset, we see that illicit cases are indeed not outlying."</sub>
- **descriptive / method**: UMAP projection of the test set was used to plot observations, once coloured by the predicted label of the worst-performing method (IF) and once by the true label. (p. 5)[^original]  
  <sub>anchor: "we apply the Uniform Manifold Approximation and Projection (UMAP) [24] to the test set and build two plots"</sub>
- **descriptive / finding or result**: IF classifies most outlying instances as illicit, but true labels show illicit instances are not actually outlying and hide among licit transactions. (p. 5)[^original]  
  <sub>anchor: "the illicit instances in the dataset are not actually outlying, but instead hiding among licit transactions."</sub>
- **descriptive / context**: The authors state that sophisticated criminals obfuscate activity by mimicking normal behaviour, hiding in regions of high nominal density, and that Das et al. previously acknowledged this problem. (p. 5)[^original]  
  <sub>anchor: "sophisticated criminals obfuscate their activity by mimicking normal behaviour, hiding in regions of high nominal density."</sub>
- **descriptive / finding or result**: The authors conclude that anomaly detection methods are ineffective for the unsupervised classification task on this real-life Bitcoin dataset. (p. 5)[^original]  
  <sub>anchor: "we conclude that anomaly detection methods are ineffective for the unsupervised classification task in this real-life Bitcoin dataset."</sub>

## 4.3 Active learning

- **descriptive / finding or result**: Table 2 shows that switching to a supervised hot learner significantly improves performance over continued use of unsupervised warm-up learners, while there is no clear best policy among hot learners. (p. 5)[^original]  
  <sub>anchor: "We conclude that switching to a supervised hot-learner significantly improves performance over the continued use of an unsupervised warm-up learners."</sub>
- **descriptive / finding or result**: Random sampling as warm-up learner improves model performance faster (better at smaller labeled pool sizes) than anomaly detection methods, because anomaly methods fail to detect illicit instances to query. (p. 5)[^original]  
  <sub>anchor: "random sampling as the warm- up learner leads to a faster improvement in model performance"</sub>
- **descriptive / finding or result**: Elliptic envelope performs above isolation forest, consistent with earlier results. (p. 5)[^original]  
  <sub>anchor: "We observe that elliptic envelope performs above IF (also consistent with previous results)."</sub>
- **descriptive / finding or result**: Figure 6 compares AL with random sampling using an RF classifier against the RF baseline at 2% illicit rate; Figure 7 does the same at 0.5% illicit rate. (p. 5)[^original]  
  <sub>anchor: "AL versus Random Sampling (RS) with a RF classi- fier and the RF supervised baseline at 2% illicit rate."</sub>

## 4 RESULTS

- **descriptive / finding or result**: Table 2 per-setup results for the AL benchmark include, for the random forest classifier with random sampling warm-up and uncertainty sampling hot learner, illicit F1-scores of 0.73, 0.75, 0.81, 0.82 and 0.82 at labeled pool sizes of 200, 500, 1000, 1500 and 3000. (p. 5)[^original]  
  <sub>anchor: "random sampling uncertainty sampling 0.73 0.75 0.81 0.82 0.82"</sub>

## 4.3 Active learning

- **descriptive / finding or result**: XGBoost and LR temporarily surpass their own supervised baselines with AL when trained on a sample of labels, then converge to those baselines as the labeled pool grows; neither surpasses the best RF baseline. (p. 6)[^original]  
  <sub>anchor: "XGBoost and LR temporarily sur- pass their supervised baseline"</sub>
- **descriptive / context**: The authors suggest the temporary surpassing occurs because early labeled samples are most relevant and class imbalance grows over time; Laws and Schätze acknowledge early stopping might prevent this degradation. (p. 6)[^original]  
  <sub>anchor: "Laws and Schätze [19] acknowledge that, in some cases, early stopping of an AL process might prevent this model degra- dation."</sub>
- **descriptive / finding or result**: With the best AL setup, all classifiers stabilize after 1000 labels, with RF and XGBoost showing faster performance increase. (p. 6)[^original]  
  <sub>anchor: "stabilize after 1000 labels, with RF and XGBoost exhibiting faster performance increase."</sub>
- **descriptive / finding or result**: RF reaches its baseline performance with only 5% of the original labels, i.e. 1500 of the original 30000 labels, and near-optimal performance with as few as 500 labels. (p. 6)[^original]  
  <sub>anchor: "RF reaches its baseline’s performance with only 5% of the original labels, or 1500 out of the original 30000 labels"</sub>
- **descriptive / finding or result**: AL query strategies increasingly outperform random sampling as imbalance increases; for highly imbalanced datasets the best setup is random sampling warm-up followed by uncertainty sampling hot learner. (p. 6)[^original]  
  <sub>anchor: "For highly imbalanced datasets, the best setup uses random sampling (warm-up) followed by uncertainty sampling (hot learner)."</sub>

## 5 CONCLUSION

- **descriptive / finding or result**: Random sampling achieves similar performance to the more sophisticated AL strategies in Table 2, which the authors attribute to the dataset having about 10% illicit cases so random sampling quickly gathers enough illicit instances. (p. 6)[^original]  
  <sub>anchor: "because the dataset has approximately 10% of illicit cases, random sampling can quickly reach that sufficient number."</sub>
- **descriptive / context**: The study used the Bitcoin transaction dataset released by Elliptic, with a supervised setting similar to Weber et al. as baseline, and examined detection in a setting with restricted label access using unsupervised methods and Active Learning. (p. 6)[^original]  
  <sub>anchor: "we conducted experiments to detect illicit activity on the Bitcoin transaction dataset released by Elliptic."</sub>
- **descriptive / context**: Financial crime is extremely rare among licit transactions, so datasets are highly imbalanced; the authors therefore compared AL with random sampling on data randomly undersampled from the minority class to illicit rates of 2% and 0.5%. (p. 6)[^original]  
  <sub>anchor: "we apply a random undersampling of the minority class of the Ellipic dataset to achieve illicit rates of 2% and 0.5%."</sub>
- **descriptive / finding or result**: The authors conclude that experiments on (partially) synthetic data can be misleading, emphasising the importance of experiments on real-life datasets for reliable conclusions. (p. 6)[^original]  
  <sub>anchor: "This find- ing highlights that experiments conducted on (partially) synthetic data can be misleading"</sub>
- **descriptive / finding or result**: The authors' results indicate that unsupervised anomaly detection methods have poor performance, and they present evidence that anomalies in the feature space are not indicative of illicit behaviour. (p. 6)[^original]  
  <sub>anchor: "we present evidence that anomalies in the feature-space are not indicative of illicit behaviour."</sub>
- **descriptive / finding or result**: A few hundred labels (5% of the total) gave performance similar to the best supervised baseline when using AL. (p. 7)[^original]  
  <sub>anchor: "We obtained similar performance to the best supervised baseline by using just a few hundred labels (5% of the total)."</sub>
- **descriptive / limitation**: The authors note it remains unexplored whether the class distribution found in the Bitcoin dataset holds for other real-life datasets and different labeling strategies. (p. 7)[^original]  
  <sub>anchor: "It remains to explore if the distribution of classes that we found in the Bitcoin dataset holds for other real-life datasets"</sub>
- **expected / recommendation**: The authors state it is crucial to conduct similar benchmarks on other verticals such as bank transfers, deposits or loans, using real datasets with proper labels, given the need for proper AML processes across the financial system. (p. 7)[^original]  
  <sub>anchor: "it is crucial to conduct sim- ilar benchmarks on other verticals such as bank transfers, deposits or loans"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity" (2020-05-29). https://arxiv.org/abs/2005.14635
