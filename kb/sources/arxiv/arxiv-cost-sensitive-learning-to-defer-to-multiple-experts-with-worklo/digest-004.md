---
type: Source Digest
title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints - part 4 of 5 (pp. 19-27)
description: 'Verified paraphrased digest, pp. 19-27: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > References; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > Notation; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > A Experimental Setting; and 2 more sections'
resource: https://arxiv.org/abs/2403.06906
tags:
- academic_finding
- alerts_triage
- global_academic
- model_development
- preprint
status: stable
source_id: arxiv-cost-sensitive-learning-to-defer-to-multiple-experts-with-worklo
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-11-03'
legal_status: unknown
part: 4
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
  resource: https://arxiv.org/abs/2403.06906
  title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints
  author: org:arxiv
  last_modified: '2024-11-03T00:00:00Z'
digest_points: 44
---

# Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (digest)

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 19-27) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## A.1 Alert Model

- **descriptive / method**: The Alert Model is a LightGBM classifier trained on the first 3 months of the BAF dataset and validated on the fourth month, minimising binary cross-entropy loss. (p. 20)[^original]  
  <sub>anchor: "The model was trained on the first 3 months of the BAF dataset, and validated on the fourth month."</sub>
- **descriptive / method**: Hyperparameters of the Alert Model were chosen by Bayesian search over an extensive grid, for 100 trials, with the objective of maximising recall at a 5% false positive rate on validation. (p. 20)[^original]  
  <sub>anchor: "for 100 trials, with validation done on the 4th month, where the optimization objective is to maximize recall at 5% false positive rate in validation"</sub>
- **descriptive / data or feature**: Table 5 gives the Alert Model LightGBM hyperparameter search space and selected values, including boosting type 'goss' (fixed), enable_bundle False, n_estimators in [50,5000] (log) selected 94, max_depth in [2,20] (uniform) selected 2, num_leaves in [10,1000] (log) selected 145, min_child_samples in [5,500] (log) selected 59, learning_rate in [0.01,0.5] (log) selected 0.3031421, reg_alpha in [0.0001,0.1] (log) selected 0.0012637, and reg_lambda in [0.0001,0.1] (log) selected 0.0017007. (p. 20)[^original]  
  <sub>anchor: "In Table 5 we present the hyperparameter search space used, as well as the parameters of the selected model."</sub>
- **descriptive / finding or result**: The Alert Model achieved a validation recall of 57.9% at threshold t = 0.050969, defined to obtain a 5% FPR in validation. (p. 21)[^original]  
  <sub>anchor: "This model yielded a recall of 57.9% in validation, for a threshold _t_ = 0 _._ 050969, defined to obtain a 5% FPR in validation."</sub>
- **descriptive / finding or result**: In the deployment split (months 4 to 8), used to train and test the assignment system, the Alert Model yields a recall of 52.1% using the same threshold. (p. 21)[^original]  
  <sub>anchor: "In the deployment split (months 4 to 8), used to train and test our assignment system, the model yields a recall of"</sub>
- **descriptive / data or feature**: Figure 4 presents the ROC curve for the Alert Model, calculated over months 4-8. (p. 21)[^original]  
  <sub>anchor: "In Figure 4 we present the ROC curve for the Alert Model, calculated in months 4-8."</sub>

## A.2 Determining λ based on Neyman-Pearson criterion

- **descriptive / context**: The optimisation goal is a Neyman-Pearson criterion: maximise recall subject to a fixed FPR of 5%, representing a trade-off between the cost of false positives and false negatives. (p. 21)[^original]  
  <sub>anchor: "the optimization goal is expressed by a Neyman-Pearson criterion, aiming to maximize recall subject to a fixed FPR of 5%."</sub>
- **descriptive / context**: In bank account fraud prevention, rejecting a legitimate application (false positive) must be weighed against accepting a fraudulent one (false negative). (p. 21)[^original]  
  <sub>anchor: "the consequence of committing a false positive mistake, that is, rejecting a legitimate application, must be weighed against the cost of a false negative mistake"</sub>
- **descriptive / context**: The authors do not have access to the values of the false positive cost and false negative cost, so they must derive a value λt equivalent to the error cost trade-off enforced by the Neyman-Pearson criterion, setting cFP = λ and cFN = 1. (p. 21)[^original]  
  <sub>anchor: "we do not have access to the values of _c_ FP and _c_ FN."</sub>
- **descriptive / method**: Following Elkan (2001), a relationship is drawn between the ideal threshold of a binary classifier and misclassification costs: the optimal prediction is class 1 only if the expected cost of predicting 1 is less than or equal to that of predicting 0, with p = P(y=1|xi) estimated by the Alert Model score. (p. 21)[^original]  
  <sub>anchor: "the optimal prediction for any given instance _xi_ is 1 only if the expected cost of predicting 1 is less than, or equal to the expected cost of predicting 0"</sub>
- **descriptive / limitation**: Sheng & Ling (2006) showed that the relationship between cost structure and classifier threshold does not always hold in practice. (p. 22)[^original]  
  <sub>anchor: "It has been shown by Sheng & Ling (2006) that this relationship between the cost-structure and the classifier’s threshold does not always hold in practice."</sub>
- **descriptive / limitation**: The value of λ obtained this way depends on the classifier trained; a different classifier gives a different optimal threshold and hence a different λ for the same task. (p. 22)[^original]  
  <sub>anchor: "A different classifier would yield another value for the optimal threshold according to the Neyman-Pearson criterion"</sub>
- **descriptive / method**: Because the aim is to test different cost structures, the default λt is used and the cost structures tested are λ in {λt/5, λt, 5λt}. (p. 22)[^original]  
  <sub>anchor: "we will use this as the default value for _λ_ , testing the cost-structures"</sub>

## B Classifier h

- **descriptive / method**: The classifier h is a LightGBM model trained on alerts raised by the Alert Model, using months four to six of the BAF dataset, minimising weighted log-loss. (p. 22)[^original]  
  <sub>anchor: "The model is trained on the alerts raised by the Alert Model, ranging from months four to six of the BAF dataset."</sub>
- **descriptive / method**: Hyperparameters for classifier h were chosen by Bayesian search for 300 total trials with 200 start-up trials, validated on the seventh month, minimising weighted log-loss. (p. 22)[^original]  
  <sub>anchor: "for 300 total trials, with 200 start-up trials, with validation done on the seventh month."</sub>
- **descriptive / method**: Several values of the initial probability estimate of the boosting base predictor were tested, to see whether a bias towards predicting fraud helps, since false negatives incur higher cost across all scenarios; g_initial is searched over {gd, gd+0.2, gd+0.4, ..., gd+2}. (p. 22)[^original]  
  <sub>anchor: "This was done in order to test if introducing a bias towards predicting fraud can be beneficial to our model"</sub>
- **descriptive / finding or result**: In a first series of experiments, a low number of estimators and maximum depth gave the best results. (p. 22)[^original]  
  <sub>anchor: "In a first series of experiments, we found that a low number of estimators and maximum depth resulted in the best results."</sub>
- **descriptive / data or feature**: Table 6 gives the first hyperparameter search space for classifier h: boosting_type 'dart', enable_bundle [False,True], n_estimators [50,250] uniform, max_depth [2,5] uniform, num_leaves [100,1000] uniform, min_child_samples [5,200] uniform, learning_rate [0.001,1] uniform, reg_alpha [0.001,2] uniform, reg_lambda [0.001,2] uniform. (p. 22)[^original]  
  <sub>anchor: "we use the parameter space represented in Table 6."</sub>
- **descriptive / finding or result**: Across all scenarios, LightGBM classifiers with maximum tree depth 2 achieved the best performance, so a second experiment of 1700 total trials (1500 start-up) fixed max depth at 2 with the Table 6 space. (p. 22)[^original]  
  <sub>anchor: "In this set of experiments, across all scenarios, LGBM classifiers with a maximum tree depth of 2 achieved the best performance."</sub>

## C.1 Expert Desiderata

- **expected / expectation**: Experts are expected to depend on an instance's features when making an informed decision. (p. 23)[^original]  
  <sub>anchor: "Therefore, we expect experts to be dependent on an instance’s features in order to make an informed decision."</sub>
- **descriptive / context**: In some real-world deferral systems the features are accompanied by an AI model score; presenting that score can affect expert performance, and the L2D framework allows experts with or without dependence on a separate classifier score. (p. 23)[^original]  
  <sub>anchor: "It has been shown that, in this scenario, expert’s performance can be impacted by presenting the model’s score when deferring a case to an expert"</sub>
- **expected / expectation**: If experts use an AI assistant, they are expected not to be in perfect agreement with the model, since humans and models are assumed to have complementary strengths and weaknesses. (p. 23)[^original]  
  <sub>anchor: "we expect experts not to be in perfect agreement with the model"</sub>
- **descriptive / context**: The degree of model dependence (algorithmic bias) varies between humans, measured by the model's impact on human performance, so the synthetic team may show varying dependence on the model score. (p. 23)[^original]  
  <sub>anchor: "The degree of "model dependence", or "algorithmic bias" (Alon-Barkat & Busuioc, 2023),varies between humans"</sub>
- **expected / expectation**: Expert teams should be realistic by exhibiting varying levels of overall performance, since experts within a field have varying expertise and some are outperformed by ML models. (p. 23)[^original]  
  <sub>anchor: "it is important that these exhibit varying levels of overall performance."</sub>
- **expected / expectation**: Human decisions are expected to be non-deterministic, because experts may decide differently on similar cases at different times. (p. 23)[^original]  
  <sub>anchor: "Therefore we can expect a human’s decision making process not to be entirely deterministic."</sub>
- **descriptive / context**: The assignment system can mitigate unfairness by not deferring cases to experts found unfair with respect to a protected attribute; a team with varying propensity for unfair decisions may be used to test system fairness. (p. 23)[^original]  
  <sub>anchor: "If an expert can be determined to be particularly unfair with respect to a given protected attribute"</sub>

## C.2 Expert Parameter Sampling

- **descriptive / method**: Each expert's error probabilities are a function of a pre-processed version of its features and the Alert Model score, parameterised by β0, β1, α, w and wM, using a sigmoid function. (p. 24)[^original]  
  <sub>anchor: "Each expert’s probabilities of the two types of error are parameterized by five parameters"</sub>
- **descriptive / method**: Feature weights w use a spike-and-slab prior with spike at zero; each component is zero unless a Bernoulli(0.3) latent selects the slab N(0,1), inducing sparsity. (p. 24)[^original]  
  <sub>anchor: "we first sample a Bernoulli latent variable _Z ∼ Ber_ (0 _._ 3) to select if _wi_ is sampled from the _spike_ or the _slab_"</sub>
- **descriptive / method**: The model-score weight wM is drawn from N(-2, 0.5) so all experts have some model dependency, and the protected-attribute weight wp is drawn from N(-1, 0.1) with the protected attribute being customer age, so all experts show some unfairness; fairness was not explored in this work. (p. 24)[^original]  
  <sub>anchor: "so that all experts have a degree of unfairness in their simulated predictions, however, an exploration of fairness was not conducted in this work."</sub>
- **descriptive / method**: The global influence parameter α is sampled from N(4, 0.2) so that a wide variety of error probabilities exist across the feature space; α = 0 would make error probability identical for all instances. (p. 24)[^original]  
  <sub>anchor: "We chose _α ∼ N_ (4 _,_ 0 _._ 2) so that a wide variety of probability of errors exist throughout the feature space."</sub>
- **descriptive / requirement**: The expected misclassification cost of each synthetic expert is assumed to be at most 70% of the cost of rejecting all applications. (p. 24)[^original]  
  <sub>anchor: "We assume that E[ _C_ ] _j_ must be, at most, 70% of the cost of rejecting all applications."</sub>
- **descriptive / method**: Target expected cost for each expert is sampled from N(E[C]_h, 0.2E[C]_h), where E[C]_h is the classifier's average cost known in advance, so expert performance is evenly distributed around the classifier's; targets above 70% of rejection cost are capped at that value. (p. 24)[^original]  
  <sub>anchor: "we sample the target value of E[ _C_ ] for each expert from _T_ E[ _C_ ] _j ∼ N_ (E[ _C_ ] _h,_ 0 _._ 2E[ _C_ ] _h_ )"</sub>
- **descriptive / method**: Each expert's probabilities of the two types of error are parameterized by five parameters. (p. 24)[^original]  
  <sub>anchor: "the two types of error are parameterized by five parameters"</sub>
- **descriptive / finding or result**: For very large alpha, the probability of error would saturate at the extremes of the sigmoid codomain, producing a deterministic decision-making process. (p. 24)[^original]  
  <sub>anchor: "the probability would saturate at the extremes of the codomain of the sigmoid function"</sub>
- **descriptive / method**: β0 and β1 are solved so that the expert's expected cost equals the target; a target FNR is sampled and the target FPR computed, both in ]0,1[, and monotonicity plus uniqueness allow solving via bisection on a month 7 partition. (p. 25)[^original]  
  <sub>anchor: "we solve it through a bisection method (Burden & Faires, 1985)."</sub>
- **descriptive / limitation**: Because targets are computed on month 7 empirical rates, deviations from target performance may occur due to temporal distribution shifts. (p. 25)[^original]  
  <sub>anchor: "meaning that deviations from the target performance metrics may occur due to temporal distribution shifts."</sub>
- **descriptive / method**: Numeric features are transformed to quantile values shifted by -0.5 into [-0.5,0.5]; categorical features are target-encoded by ascending target prevalence, divided by the number of categories and shifted to zero mean. (p. 25)[^original]  
  <sub>anchor: "Numeric features in X are transformed to quantile values, and shifted by _−_ 0 _._ 5"</sub>

## C.3 Expert Properties

- **descriptive / data or feature**: One expert team was generated per {ar, λ} pair, giving 6 distinct teams of 9 synthetic fraud analysts. (p. 25)[^original]  
  <sub>anchor: "resulting in 6 distinct teams of 9 synthetic fraud analysts."</sub>
- **descriptive / finding or result**: All expert teams use the same feature weights so that scenario differences are mainly due to alert rate and cost structure; Figure 5 heatmap shows the normalised weight vector and a variety of decision processes. (p. 26)[^original]  
  <sub>anchor: "we generate all expert teams with the same feature weights so that their probabilities are similarly swayed by each instance."</sub>
- **descriptive / method**: In the Full Rejection plot of FNR against FPR, the combinations lying on the single line have the same expected misclassification cost as rejecting all alerts. (p. 26)[^original]  
  <sub>anchor: "are represented by a single line."</sub>
- **descriptive / finding or result**: In Figure 6, the green area marks combinations of FPR and FNR with a lower expected misclassification cost, while the red area marks a higher misclassification cost. (p. 26)[^original]  
  <sub>anchor: "while the red area represents a higher misclassification cost."</sub>
- **descriptive / finding or result**: E[C]_j affects only the intercept of the Full Rejection line, so parallel lines represent (FPR,FNR) pairs with the same expected cost; Figure 7 shows FPR and FNR distributions on the test split for all expert teams plus classifier h. (p. 27)[^original]  
  <sub>anchor: "Note that E[ _C_ ] _j_ only influences the intercept, meaning that lines parallel to the one represented in Figure 6"</sub>
- **expected / requirement**: For the decision-making complementarity assumption to hold, there should be regions of the feature space where a given expert's probability of correctness surpasses that of other experts, and vice versa. (p. 27)[^original]  
  <sub>anchor: "we need to ensure that there are regions of the feature space where the probability of correctness of a given expert surpasses that of other experts"</sub>
- **descriptive / finding or result**: Figure 8 heatmap shows a significant number of instances in all scenarios where one decision-maker is correct and another incorrect, so the testbed is judged appropriate for testing L2D methods. (p. 27)[^original]  
  <sub>anchor: "There is a significant number of instances, for all scenarios, where a given expert/classifier is a better choice than another decision-maker"</sub>

---

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

[^original]: arXiv, "Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints" (2024-11-03). https://arxiv.org/abs/2403.06906
