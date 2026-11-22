---
type: Source Digest
title: 'FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection - part 2 of 3 (pp. 7-11)'
description: 'Verified paraphrased digest, pp. 7-11: FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection > 4.1 Experimental Setup; FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection > 4.2 Experimental Findings; FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection > 5 Conclusions and future work'
resource: https://arxiv.org/abs/2502.02290
tags:
- academic_finding
- advanced_analytics
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-fraud-rla-a-new-reinforcement-learning-adversarial-attack-agains
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-04-02'
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
  resource: https://arxiv.org/abs/2502.02290
  title: 'FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection'
  author: org:arxiv
  last_modified: '2025-04-02T00:00:00Z'
digest_points: 56
---

# FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-11) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.1.1 Datasets

- **descriptive / data or feature**: The Kaggle credit card fraud dataset was obtained by applying a PCA transformation to 250K real transactions made in September 2013 by European cardholders, and is described as one of the most widely used datasets in fraud detection. (p. 7)[^original]  
  <sub>anchor: "obtain by applying a PCA transformation [34] on 250K real transactions performed in September 2013 by European cardholders"</sub>
- **descriptive / data or feature**: Each Kaggle transaction carries a genuine or fraudulent label and 30 features, including the transaction amount. (p. 7)[^original]  
  <sub>anchor: "Each transaction has a label (genuine or fraudulent) and 30 features, including the amount."</sub>
- **descriptive / method**: Because the PCA transformation removed the semantics of the original columns, the authors randomly designated Kaggle features as known, controllable, or unknown, so that the number of unknown and uncontrollable features could be varied and its effect on attacks measured. (p. 7)[^original]  
  <sub>anchor: "Since the PCA transformation lost the semantics of the original columns, we randomly select features as known, controllable, and unknown."</sub>
- **descriptive / data or feature**: The SKLearn dataset is a binary classification problem made of clusters of normally distributed points; it allows selection of class distributions and problem dimensionality, which the authors use to help generalise their findings. (p. 7)[^original]  
  <sub>anchor: "A binary classification problem composed of clusters of normally distributed points generated using SKLearn"</sub>
- **descriptive / context**: The authors argue that not fine-tuning the attack lowers the entry barrier for deploying it, which makes the potential consequences more severe. (p. 7)[^original]  
  <sub>anchor: "this approach allows for a lower entrance barrier for deploying the attack"</sub>

## 4.1.2 Baseline: Mimicry

- **descriptive / context**: No attack reported in the related literature can be used against fraud detection engines when the attacker has no access to a training set beforehand. (p. 7)[^original]  
  <sub>anchor: "no attack reported in related literature can be employed against fraud detection engines under this condition"</sub>
- **descriptive / method**: To give a fair baseline, the authors assume the Mimicry attacker can access an unlabeled training set, an easier condition than having a labeled one. (p. 7)[^original]  
  <sub>anchor: "we assume that an attacker may access an unlabeled training set"</sub>
- **descriptive / context**: Fraud data are typically highly skewed towards the genuine class, so fraudsters may run Mimicry by modelling genuine users' behaviour. (p. 7)[^original]  
  <sub>anchor: "Since data in fraud detection are typically highly skewed towards the genuine class [15]"</sub>
- **descriptive / context**: FRAUD-RLA does not use a training set, so the comparison puts it at a disadvantage against attacks in a less challenging environment; the authors note this may make its assessment pessimistic but still give a reasonable baseline. (p. 7)[^original]  
  <sub>anchor: "we effectively put FRAUDRLA at a disadvantage as we compare it with attacks operating in a less challenging environment"</sub>
- **descriptive / method**: The Mimicry variant used assumes attackers lack knowledge of time-dependent features, so a simplified version approximating user behaviour with straightforward statistical methods is adopted rather than the more complex approach in the literature. (p. 7)[^original]  
  <sub>anchor: "we assume that attackers lack knowledge of time-dependent features"</sub>
- **descriptive / method**: The simplified Mimicry approach is said to need significantly less hyperparameter tuning, which the authors say fits the considered threat model. (p. 7)[^original]  
  <sub>anchor: "our approach has the significant advantage of requiring significantly less hyperparameter tuning"</sub>
- **descriptive / method**: Mimicry fits a statistical model to a small training set and tests several distribution families: a uniform distribution, univariate normal distributions, a multivariate normal distribution, and a Gaussian mixture with 10 components. (p. 7)[^original]  
  <sub>anchor: "a uniform, various univariate normal distribution, a multivariate normal distribution, and a Gaussian mixture with 10 mixture components"</sub>
- **descriptive / method**: Two training set sizes are considered: a realistic case where the attacker observes 1000 observations, and a pessimistic case where the attacker observes the complete training set. (p. 7)[^original]  
  <sub>anchor: "the realistic one, where the attacker can observe a small training set of 1000 observations"</sub>
- **descriptive / method**: In each round, Mimicry samples the controllable feature values from the fitted distribution and sends the resulting transaction, combined with the fixed and unknown features, to the classifier. (p. 7)[^original]  
  <sub>anchor: "At each round, the attacker randomly samples the values of the controllable features from the trained distribution"</sub>

## 4.1.3 Methodology

- **descriptive / method**: The fraud detection engine in the experiments is simplified to two components: a machine learning classifier paired with a rule-based classifier. (p. 7)[^original]  
  <sub>anchor: "we imagine a simplified engine comprising two models: a machine-learning and a rulebased classifier"</sub>
- **descriptive / method**: Two machine learning classifiers are tested, a Random Forest (RF) and a feed-forward neural network (NN), trained with a standard random grid cross-validation strategy for hyperparameter tuning. (p. 7)[^original]  
  <sub>anchor: "we test two different machine learning classifiers: a Random Forest (RF) and a feed-forward neural network (NN)"</sub>

## 4.1.1 Datasets

- **descriptive / method**: The authors state that all tests use the same PPO implementation and hyperparameters, with no tuning for each dataset. They describe this as a pessimistic assumption for the attacker that still gives a lower bound on the attack's effectiveness. (p. 7)[^original]  
  <sub>anchor: "we will conduct all tests using the same PPO implementation and hyperparameters"</sub>

## 4.1.3 Methodology

- **descriptive / method**: The rule-based component rejects any transaction in which a feature falls within the 10% most extreme values of the training set, to penalise strategies based on extreme values. (p. 8)[^original]  
  <sub>anchor: "rejecting transactions where any feature would fall into the 10% most extreme values in the training set"</sub>
- **descriptive / method**: Attack success is measured as the average success rate, the percentage of successful frauds, over the first 300, 1000 and 4000 frauds. (p. 8)[^original]  
  <sub>anchor: "In particular, we measure it over the first 300, 1000, and 4000 frauds."</sub>
- **descriptive / data or feature**: Table 4 reports classifier performance: on the Generator data RF has accuracy 0.89, precision 0.95, recall 0.82, F1 0.88 and NN has 0.89, 0.95, 0.81, 0.88; on Kaggle RF has 0.95, 1.00, 0.91, 0.95 and NN has 0.93, 0.97, 0.90, 0.93; SKLearn 0 scores 1.00 on every measure for both RF and NN; SKLearn 1 scores 0.99 on every measure for both; SKLearn 2 has RF at 0.74, 0.75, 0.74, 0.75 and NN at 0.82, 0.82, 0.83, 0.82 (accuracy, precision, recall, F1). (p. 8)[^original]  
  <sub>anchor: "Table 4: Classifiers Performance over the tested datasets."</sub>

## 4.2 Experimental Findings

- **descriptive / finding or result**: Mimicry results on the synthetic generator data are analysed first, as they give the baseline for attacker performance; success rates are reported for different combinations of fixed, known and unknown features, grouped as terminal-based (T) and customer-based (C) aggregations. (p. 8)[^original]  
  <sub>anchor: "We group here features as terminal-based ( _T_ ) and customer-based ( _C_ ) aggregations."</sub>
- **descriptive / finding or result**: Increasing the Mimicry training set beyond 1000 samples does not significantly improve the algorithms' performance. (p. 8)[^original]  
  <sub>anchor: "increasing the size of the training set over 1000 samples does not significantly improve the performance of the algorithms"</sub>
- **descriptive / finding or result**: Although RF and NN have practically the same recall on the test set, all Mimicry attacks achieve a significantly higher success rate against Neural Networks, which the authors read as showing the superior robustness of Random Forests; this agrees with earlier literature on RF robustness against traditional adversarial attacks. (p. 8)[^original]  
  <sub>anchor: "all Mimicry attacks achieve a significantly higher success rate against Neural Networks, showing the superior robustness of Random Forests"</sub>
- **descriptive / finding or result**: When fraudsters control all features, Mimicry achieves a very high success rate against classifiers with recall above 0.9 on non-adversarial data, but its effectiveness drops sharply as the number of controllable features is reduced. (p. 8)[^original]  
  <sub>anchor: "attacks’ effectiveness dramatically decreases when we reduce the number of controllable features"</sub>
- **descriptive / finding or result**: Compared with the best baseline in each setting, FRAUD-RLA's average cumulative reward rises over time as it learns the best attack policy; for random forests it starts significantly below the baseline and then reaches or surpasses it, while neural networks are breached from the first rounds. (p. 8)[^original]  
  <sub>anchor: "In the case of random forests, FRAUD-RLA starts with an average cumulative reward that is significantly lower than the baseline"</sub>
- **descriptive / finding or result**: The authors state that FRAUD-RLA in most settings surpasses the baselines in average cumulative reward from early rounds, which they attribute to a good exploration-exploitation tradeoff. (p. 8)[^original]  
  <sub>anchor: "FRAUD-RLA in most settings surpasses the baselines in Average Cumulative Reward from early rounds"</sub>
- **descriptive / finding or result**: On the generator data, knowing fixed features without being able to control them does not help FRAUD-RLA, because customer and terminal features are produced by independent processes in the generator. (p. 8)[^original]  
  <sub>anchor: "as customers’ and terminals’ features are created by independent processes in the generator [28]"</sub>
- **descriptive / finding or result**: On the Kaggle dataset the classifiers perform better than on the generator data, with recall from 0.9 for both RF and NN, and the baseline stays highly effective when the attacker has full control of features but falls quickly as fixed and unknown features increase. (p. 8)[^original]  
  <sub>anchor: "classifiers perform better on this dataset than on the generator data"</sub>
- **descriptive / finding or result**: Table 5 (Generator, Random Forest) gives Mimicry success rates for baselines trained on 1k or 100% of the data, in the order multivariate, univariate, uniform, mixture: no fixed and no unknown features 0.84/0.83, 0.67/0.66, 0.68/0.69, 0.85/0.86; fixed none with unknown T 0.52/0.52, 0.40/0.39, 0.39/0.39, 0.57/0.57; unknown C 0.60/0.60, 0.60/0.60, 0.66/0.65, 0.56/0.56; unknown C,T 0.23/0.23 in all four; fixed T unknown none 0.52/0.52, 0.40/0.39, 0.39/0.39, 0.57/0.58; fixed T unknown C 0.23/0.23, 0.23/0.23, 0.26/0.26, 0.23/0.23; fixed C 0.60/0.60, 0.60/0.60, 0.66/0.65, 0.56/0.56; fixed C unknown T 0.23/0.23 in all four; fixed C,T 0.23/0.23 in all four. (p. 9)[^original]  
  <sub>anchor: "Table 5: Generator, Random Forest. Baselines Success Rate comparison under various scenarios."</sub>
- **descriptive / finding or result**: Table 6 (Generator, Neural Network) gives Mimicry success rates in the same layout: no fixed and no unknown features 0.90/0.89, 0.72/0.71, 0.67/0.66, 0.89/0.89; unknown T 0.58/0.58, 0.45/0.44, 0.43/0.43, 0.60/0.60; unknown C 0.69/0.69, 0.70/0.69, 0.75/0.72, 0.66/0.66; unknown C,T 0.32/0.32, 0.32/0.31, 0.33/0.33, 0.32/0.32; fixed T unknown none 0.58/0.57, 0.45/0.44, 0.43/0.43, 0.60/0.60; fixed T unknown C 0.32/0.32, 0.32/0.32, 0.33/0.33, 0.31/0.32; fixed C 0.70/0.69, 0.70/0.69, 0.75/0.72, 0.66/0.66; fixed C unknown T 0.32/0.32, 0.32/0.32, 0.33/0.33, 0.31/0.32; fixed C,T 0.32/0.32, 0.32/0.32, 0.33/0.33, 0.31/0.32. (p. 9)[^original]  
  <sub>anchor: "Table 6: Generator, Neural Network. Baselines Success Rate comparison under various scenarios."</sub>
- **descriptive / finding or result**: Table 7 (Generator, Random Forest) compares FRAUD-RLA at 300, 1000 and 4000 frauds with the best baseline: no fixed and no unknown 0.15, 0.37, 0.75 vs 0.86; unknown T 0.12, 0.28, 0.53 vs 0.57; unknown C 0.32, 0.57, 0.74 vs 0.66; unknown C,T 0.24, 0.25, 0.28 vs 0.26; fixed T 0.13, 0.30, 0.53 vs 0.58; fixed T unknown C 0.24, 0.25, 0.28 vs 0.26; fixed C 0.33, 0.57, 0.73 vs 0.66; fixed C unknown T 0.24, 0.25, 0.28 vs 0.26; fixed C,T 0.24, 0.25, 0.28 vs 0.26. (p. 9)[^original]  
  <sub>anchor: "Table 7: Generator, Random Forest. Comparison between the average Cumulative Reward"</sub>
- **descriptive / finding or result**: Table 8 (Generator, Neural Network) compares FRAUD-RLA at 300, 1000 and 4000 frauds with the best baseline: no fixed and no unknown 0.72, 0.86, 0.89 vs 0.90; unknown T 0.64, 0.85, 0.91 vs 0.60; unknown C 0.79, 0.90, 0.92 vs 0.75; unknown C,T 0.80, 0.93, 0.97 vs 0.33; fixed T 0.62, 0.85, 0.91 vs 0.60; fixed T unknown C 0.77, 0.92, 0.97 vs 0.33; fixed C 0.79, 0.91, 0.93 vs 0.75; fixed C unknown T 0.78, 0.92, 0.97 vs 0.33; fixed C,T 0.79, 0.93, 0.97 vs 0.33. (p. 9)[^original]  
  <sub>anchor: "Table 8: Generator, Neural Network. Comparison between the average Cumulative Reward"</sub>
- **descriptive / finding or result**: Table 9 (Kaggle, Random Forest) compares FRAUD-RLA at 300, 1000 and 4000 frauds with the best baseline: no fixed and no unknown 0.87, 0.90, 0.91 vs 0.99; unknown 25% 0.83, 0.89, 0.90 vs 0.91; fixed 25% 0.86, 0.91, 0.91 vs 0.92; unknown 50% 0.76, 0.86, 0.89 vs 0.71; fixed 25% unknown 25% 0.77, 0.88, 0.90 vs 0.71; fixed 50% 0.76, 0.87, 0.90 vs 0.65; fixed 25% unknown 50% 0.46, 0.57, 0.64 vs 0.34; fixed 50% unknown 25% 0.48, 0.62, 0.69 vs 0.35. (p. 9)[^original]  
  <sub>anchor: "Table 9: Kaggle, Random Forest. Comparison between the average Cumulative Reward of FRAUD-RLA"</sub>
- **descriptive / finding or result**: Table 10 (Kaggle, Neural Network) compares FRAUD-RLA at 300, 1000 and 4000 frauds with the best baseline: no fixed and no unknown 0.87, 0.90, 0.93 vs 0.94; unknown 25% 0.87, 0.91, 0.94 vs 0.58; fixed 25% 0.86, 0.92, 0.94 vs 0.60; unknown 50% 0.88, 0.92, 0.95 vs 0.41; fixed 25% unknown 25% 0.88, 0.93, 0.95 vs 0.39; fixed 50% 0.87, 0.92, 0.95 vs 0.41; fixed 25% unknown 50% 0.88, 0.94, 0.96 vs 0.26; fixed 50% unknown 25% 0.88, 0.94, 0.96 vs 0.28. (p. 10)[^original]  
  <sub>anchor: "Table 10: Kaggle, Neural Network. Comparison between the average Cumulative Reward"</sub>
- **descriptive / finding or result**: FRAUD-RLA's average success rate on Kaggle decreases very slowly as the number of fixed or unknown features grows, and only some Random Forest configurations fall below 0.9. (p. 10)[^original]  
  <sub>anchor: "FRAUD-RLA average success rate decreases very slowly with the number of fixed or unknown features"</sub>
- **descriptive / finding or result**: On Kaggle, known fixed features appear to improve FRAUD-RLA compared with unknown features; the authors say more tests are needed to establish the significance of this effect. (p. 10)[^original]  
  <sub>anchor: "known fixed features seem to improve the performance of FRAUD-RLA compared to unknown features"</sub>
- **descriptive / limitation**: The authors state that more tests should be performed to study the significance of the observed effect of known fixed features on FRAUD-RLA. (p. 10)[^original]  
  <sub>anchor: "More tests should be performed to study the significance of this effect."</sub>
- **descriptive / method**: The SKLearn experiments vary dimensionality and complexity across three scenarios: Scenario 1 (easy) with 16 features, 1 cluster per class and high class separation; Scenario 2 (intermediate) with 64 features, 8 clusters per class and high separation; Scenario 3 (hard) with 64 features, 16 clusters per class and small separation. (p. 10)[^original]  
  <sub>anchor: "Scenario 1 (easy): A problem with 16 features, 1 cluster per class, and high separation between the classes."</sub>
- **descriptive / finding or result**: Both classifiers perform well in SKLearn Scenarios 1 and 2 but struggle in Scenario 3. (p. 10)[^original]  
  <sub>anchor: "both classifiers perform nicely when applied in the first two scenarios while struggling in the third one"</sub>
- **descriptive / finding or result**: Against Neural Networks, FRAUD-RLA is the best attack in all SKLearn scenarios, achieving an excellent success rate, particularly compared with Mimicry, and NNs are more frequently breached by it despite outperforming RFs on the original datasets. (p. 10)[^original]  
  <sub>anchor: "FRAUD-RLA is the best attack against Neural Networks, where it achieves an excellent success rate in all scenarios"</sub>
- **descriptive / finding or result**: Against Random Forests on SKLearn, FRAUD-RLA is still the best method in Scenario 3, breaking the classifier even when most features are uncontrollable or unknown. (p. 10)[^original]  
  <sub>anchor: "FRAUD-RLA is still the best method in Scenario 3, with attacks breaking the classifier even when most features are uncontrollable or unknown"</sub>
- **descriptive / finding or result**: Scenarios 1 and 2 are difficult for all attacks against Random Forests, and in Scenario 2 the baseline outperforms FRAUD-RLA. (p. 10)[^original]  
  <sub>anchor: "but in Scenario 2, the baseline outperforms FRAUD-RLA"</sub>
- **descriptive / finding or result**: The authors explain that the current FRAUD-RLA implementation performs better in exploration scenarios, so it outperforms Mimicry when more features are hidden. (p. 10)[^original]  
  <sub>anchor: "the current implementation of FRAUD-RLA performs better in exploration scenarios"</sub>
- **descriptive / finding or result**: Mimicry performs better than FRAUD-RLA in the cases where classes are clearly divided and all features are controllable, which the authors say is most evident in the first three table lines. (p. 10)[^original]  
  <sub>anchor: "classes are clearly divided and all features are controllable"</sub>
- **descriptive / limitation**: The authors state that the cases where Mimicry outperforms FRAUD-RLA are useful for thorough analysis but very unlikely in real-world settings, where most features are routinely unknown or fixed. (p. 10)[^original]  
  <sub>anchor: "It is worth noting that such cases, although useful in a thorough analysis, are very unlikely in real-world settings"</sub>
- **expected / finding or result**: The authors expect FRAUD-RLA to be an excellent tool for most practical scenarios. (p. 10)[^original]  
  <sub>anchor: "Hence, we expect FRAUD-RLA to be an excellent tool for most practical scenarios."</sub>
- **descriptive / context**: The work aims to address this gap by analysing the main features of the fraud domain, with attention to differences from traditional domains such as image recognition and malware detection. (p. 10)[^original]  
  <sub>anchor: "focusing on differences with more traditional domains, such as image recognition and malware detection"</sub>
- **descriptive / finding or result**: Table 11 (SKLearn, Random Forest) reports the best baseline success for Datasets 1, 2 and 3 and the FRAUD-RLA variation from it after 4000 frauds, across fixed and unknown feature settings: 0/0 baseline 1, 1, 0.72 with variation -0.12, -0.47, 0.02; 0/25 0.97, 0.93, 0.62 with -0.12, -0.41, 0.17; 25/0 0.99, 0.94, 0.63 with -0.11, -0.43, 0.09; 0/50 0.53, 0.45, 0.5 with 0.08, -0.05, 0.13; 25/25 0.43, 0.46, 0.5 with 0.17, -0.04, 0.12; 50/0 0.58, 0.46, 0.5 with 0.05, 0.12, 0.10; 25/50 0.03, 0.04, 0.37 with 0.00, 0.03, 0.24; 50/25 0.01, 0.04, 0.38 with 0.00, 0.02, 0.23. (p. 11)[^original]  
  <sub>anchor: "Table 11: SKLearn, Random Forest. Best baseline performance over different datasets"</sub>
- **descriptive / finding or result**: Table 12 (SKLearn, Neural Network) reports the same measures: 0/0 baseline 1.00, 1.00, 0.80 with variation -0.08, -0.22, -0.07; 0/25 0.91, 0.87, 0.65 with 0.02, -0.06, 0.10; 25/0 0.97, 0.87, 0.66 with 0.04, -0.06, 0.10; 0/50 0.39, 0.44, 0.49 with 0.54, 0.39, 0.30; 25/25 0.42, 0.45, 0.50 with 0.51, 0.39, 0.31; 50/0 0.45, 0.41, 0.49 with 0.49, 0.43, 0.31; 25/50 0.02, 0.08, 0.33 with 0.94, 0.80, 0.54; 50/25 0.04, 0.09, 0.33 with 0.92, 0.75, 0.55. (p. 11)[^original]  
  <sub>anchor: "Table 12: SKLearn, Neural Network. Best baseline performance over different datasets"</sub>

## 5 Conclusions and future work

- **descriptive / method**: The authors expanded existing threat models for credit card fraud detection, updating them to consider the lack of human supervision, the limited data knowledge and control, and the exploration-exploitation tradeoff. (p. 11)[^original]  
  <sub>anchor: "we updated existing approaches to consider the lack of human supervision, the limited data knowledge and control"</sub>
- **descriptive / method**: FRAUD-RLA is formulated as a Partially Observable Markov Decision Process in which the known fixed features form the visible state and the action is selecting values for the controllable features, with the aim of finding a successful fraudulent pattern in the shortest possible time. (p. 11)[^original]  
  <sub>anchor: "modeled the problem of finding a successful fraudulent pattern in the shortest possible time"</sub>
- **descriptive / method**: The attack is optimised with Proximal Policy Optimization (PPO), described as a robust algorithm able to optimise continuous policies with little hyperparameter optimisation. (p. 11)[^original]  
  <sub>anchor: "a robust algorithm able to optimize continuous policies with little hyperparameter optimization"</sub>
- **descriptive / finding or result**: The authors report that FRAUD-RLA quickly achieves a high average success rate under most settings and beats the baselines without hyperparameter optimisation against the different datasets and target classifiers. (p. 11)[^original]  
  <sub>anchor: "consistently beating the baselines without optimizing the hyperparameters against the different datasets and target classifiers"</sub>
- **descriptive / limitation**: The authors state FRAUD-RLA is not intended as an off-the-shelf attack for real-world use; categorical variables, possible limits on how often frauds can be carried out without raising alarms, and other real-case challenges mean it is not an immediate threat to any real system. (p. 11)[^original]  
  <sub>anchor: "The presence of categorical variables, eventual limitations to the frequency at which frauds can be performed"</sub>
- **expected / recommendation**: The authors say it is imperative to use the appropriate tools for comprehensive security assessments and improvements of fraud detection systems, through red teaming. (p. 11)[^original]  
  <sub>anchor: "it is imperative to use the appropriate tools for comprehensive assessments and improvements"</sub>
- **descriptive / context**: The authors argue that improving understanding of the adversarial security of fraud detection systems is crucial for developing effective defences. (p. 11)[^original]  
  <sub>anchor: "improving our understanding of adversarial security of fraud detection systems will be crucial in developing effective defenses"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection" (2025-04-02). https://arxiv.org/abs/2502.02290
