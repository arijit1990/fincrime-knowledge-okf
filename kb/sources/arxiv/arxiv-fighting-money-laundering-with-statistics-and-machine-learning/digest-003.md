---
type: Source Digest
title: Fighting Money Laundering with Statistics and Machine Learning - part 3 of 5 (pp. 13-18)
description: 'Verified paraphrased digest, pp. 13-18: Fighting Money Laundering with Statistics and Machine Learning > 5 Future Research Directions; Fighting Money Laundering with Statistics and Machine Learning > 6 Conclusion; Fighting Money Laundering with Statistics and Machine Learning > References'
resource: https://arxiv.org/abs/2201.04207
tags:
- academic_finding
- customer_risk
- datasets_benchmarks
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-fighting-money-laundering-with-statistics-and-machine-learning
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-11-01'
legal_status: unknown
part: 3
parts_total: 5
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
  resource: https://arxiv.org/abs/2201.04207
  title: Fighting Money Laundering with Statistics and Machine Learning
  author: org:arxiv
  last_modified: '2022-11-01T00:00:00Z'
digest_points: 26
---

# Fighting Money Laundering with Statistics and Machine Learning (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 13-18) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 5.4 Interpretable and Fair Machine Learning

- **descriptive / definition**: Fairness is an ambiguous concept in machine learning with many different and overlapping definitions. (p. 13)[^original]  
  <sub>anchor: "Fairness” is an ambiguous concept in machine learning with many different and overlapping definitions"</sub>
- **descriptive / definition**: Equalized odds definition: different protected groups should have equal true and false positive rates. (p. 13)[^original]  
  <sub>anchor: "The equalized odds definition states that different protected groups (e.g., genders or races) should"</sub>
- **descriptive / definition**: Conditional statistical parity definition: given a set of legitimate discriminative features, the likelihood of a positive prediction should be the same across protected groups. (p. 13)[^original]  
  <sub>anchor: "The conditional statistical parity definition takes a set of legitimate discriminative features into account"</sub>
- **descriptive / definition**: Counterfactual fairness definition: a prediction is fair if it remains unchanged in a counterfactual world where features of interest are changed. (p. 13)[^original]  
  <sub>anchor: "the counterfactual fairness definition is based on a notation that a prediction is fair if it remains unchanged"</sub>
- **descriptive / method**: Louizos et al. use variational autoencoders to ensure fairness, treating sensitive features as nuisance or noise variables and encouraging separation from informative latent features via factorized priors and a maximum mean discrepancy penalty term. (p. 13)[^original]  
  <sub>anchor: "The authors treat sensitive features as nuisance or noise variables, encouraging separation between these and"</sub>
- **descriptive / method**: Zhang et al. propose adversarial learning, where a primary model predicts an outcome while minimising an adversarial model's ability to predict protected feature values; the adversary takes the primary model's predictions and other relevant features as inputs, depending on the fairness definition of interest. (p. 13)[^original]  
  <sub>anchor: "Here, a primary model tries to predict an outcome variable while minimizing an adversarial model’s ability to predict protected feature values."</sub>
- **descriptive / definition**: Following Du et al., interpretability is distinguished as intrinsic or post-hoc; intrinsically interpretable models are easy to understand by design, such as simple decision trees and linear regression. (p. 14)[^original]  
  <sub>anchor: "we follow Du et al. [170] and distinguish between intrinsic and _post-hoc_ interpretability."</sub>
- **descriptive / method**: Attention mechanisms exhibit some intrinsic interpretability; attention scores can be investigated to see which part of an input sequence a network focuses on. (p. 14)[^original]  
  <sub>anchor: "Notably, attention mechanisms also exhibit some intrinsic interpretability"</sub>
- **descriptive / definition**: Black-box models require post-hoc interpretability methods, which can be global (overall model behaviour) or local (individual predictions). (p. 14)[^original]  
  <sub>anchor: "Other models and architectures work as “black boxes” and require _post-hoc_ interpretability methods."</sub>
- **descriptive / method**: LIME generates permuted observations around a single observation with black-box outputs, trains an intrinsically interpretable model on this synthetic data, and uses it to explain the original black-box prediction. (p. 14)[^original]  
  <sub>anchor: "The method then first generates a set of permutated observations (relative to the original observation)"</sub>
- **descriptive / method**: Gradient-based methods use gradients of a particular observation and black-box model to capture importance; larger gradients, positive or negative, imply larger feature importance. (p. 14)[^original]  
  <sub>anchor: "The fundamental idea is that larger gradients (either positive or negative) imply larger feature importance."</sub>
- **descriptive / method**: Individual conditional expectation plots show what happens to a particular black-box prediction when one feature value of the observation is varied. (p. 14)[^original]  
  <sub>anchor: "These illustrate what happens to a particular black box prediction if we vary one feature value"</sub>
- **descriptive / method**: Partial dependence plots support global interpretability by averaging results of feature variations over all observations; this may be misleading when input features are highly correlated. (p. 14)[^original]  
  <sub>anchor: "This may, however, be misleading if input features are highly correlated."</sub>
- **descriptive / method**: Accumulated local effects plots are presented as an attractive alternative when features are correlated; they rely on conditional feature distributions and employ prediction differences. (p. 14)[^original]  
  <sub>anchor: "In this case, accumulated local effects plots [175] present an attractive alternative."</sub>
- **descriptive / finding or result**: Counterfactual generation methods generally need to query the underlying model multiple times, while efficient methods using invertible neural networks have also been proposed. (p. 14)[^original]  
  <sub>anchor: "While these generally need to query an underlying model multiple times, efficient methods utilizing invertible neural networks have also been proposed"</sub>
- **descriptive / context**: Quantitative evaluation of counterfactual examples is a related problem, discussed in depth by Hvilshøj et al. (p. 14)[^original]  
  <sub>anchor: "A related problem concerns the quantitative evaluation of counterfactual examples"</sub>
- **descriptive / method**: SHAP, based on Shapley values with a game-theoretical foundation, records for an observation the average marginal feature contributions over all feature coalitions; it gives local and global interpretability, and summed over a data set shows accumulated feature importance. (p. 14)[^original]  
  <sub>anchor: "For a given observation, SHAP values record average marginal feature contributions"</sub>
- **descriptive / finding or result**: SHAP values are computationally expensive, but polynomial time estimation is possible for tree-based models. (p. 14)[^original]  
  <sub>anchor: "Although SHAP values are computationally expensive, polynomial time estimation is possible for tree-based models"</sub>

## 6 Conclusion

- **descriptive / method**: The authors propose a terminology for AML in banks built on two central tasks: client risk profiling (general risk scores, e.g. for KYC) and suspicious behaviour flagging (alarms on clients, accounts or transactions, e.g. for transaction monitoring). (p. 14)[^original]  
  <sub>anchor: "we propose a terminology for AML in banks structured around two central tasks"</sub>
- **descriptive / finding or result**: Literature on client risk profiling is characterised by diagnostics, i.e. efforts to find and explain risk factors. (p. 14)[^original]  
  <sub>anchor: "the literature on client risk profiling is characterized by diagnostics"</sub>
- **descriptive / finding or result**: Literature on suspicious behaviour flagging is characterised by non-disclosed features and hand-crafted risk indices. (p. 14)[^original]  
  <sub>anchor: "is characterized by non-disclosed features and hand-crafted risk indices."</sub>
- **descriptive / limitation**: The AML-in-banks literature has problems; two named challenges are class imbalance and a lack of public data sets. (p. 15)[^original]  
  <sub>anchor: "Two challenges are class imbalance and a lack of public data sets."</sub>
- **permissive / recommendation**: Various data augmentation methods may be used to address class imbalance. (p. 15)[^original]  
  <sub>anchor: "To address class imbalance, a multitude of different data augmentation methods may be used."</sub>
- **permissive / recommendation**: Given the sensitivity of bank data, synthetic data generation may be a viable way to address the lack of public data sets. (p. 15)[^original]  
  <sub>anchor: "synthetic data generation may be a viable way to address the lack of public data sets."</sub>
- **descriptive / finding or result**: Synthetic public data sets would facilitate better evaluation and reproducibility of methods and comparisons between new and existing methods. (p. 15)[^original]  
  <sub>anchor: "Synthetic public data sets would, in particular, facilitate better evaluation and reproducibility of"</sub>
- **expected / recommendation**: The authors strongly advise against using accuracy as an evaluation metric for AML applications, instead emphasising ROC or PR curves. (p. 15)[^original]  
  <sub>anchor: "we strongly advise against the use of accuracy as an evaluation metric for AML applications"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: arXiv, "Fighting Money Laundering with Statistics and Machine Learning" (2022-11-01). https://arxiv.org/abs/2201.04207
