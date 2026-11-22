---
type: Source Digest
title: Adaptive Fraud Detection System Using Dynamic Risk Features - part 2 of 3 (pp. 7-14)
description: 'Verified paraphrased digest, pp. 7-14: 3. Survey of Adaptive Algorithms; 4. Model with dynamic risk features; _4.1. Measuring concept drift using entity profile with fraud feedback_; and 1 more sections'
resource: https://arxiv.org/abs/1810.04654
tags:
- academic_finding
- data_features
- global_academic
- ml_statistics
- model_development
- preprint
status: stable
source_id: arxiv-adaptive-fraud-detection-system-using-dynamic-risk-features
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2018-10-10'
legal_status: unknown
part: 2
parts_total: 3
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
  resource: https://arxiv.org/abs/1810.04654
  title: Adaptive Fraud Detection System Using Dynamic Risk Features
  author: org:arxiv
  last_modified: '2018-10-10T00:00:00Z'
digest_points: 67
---

# Adaptive Fraud Detection System Using Dynamic Risk Features (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-14) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3. Survey of Adaptive Algorithms

- **descriptive / context**: Fraud detection systems in eCommerce use adaptive learning algorithms to process high-speed streams of data. (p. 7)[^original]  
  <sub>anchor: "Fraud detection systems in the eCommerce use adaptive learning algorithms to process high-speed flows of stream data"</sub>
- **descriptive / definition**: Adaptive algorithms for learning under concept drift are primarily based on either an active or a passive approach. Active algorithms detect concept drift, while passive algorithms continuously update the model with new data whether or not drift is present. (p. 7)[^original]  
  <sub>anchor: "Active algorithms detect concept drift, and passive algorithms constantly update the model with new data, regardless whether drift is present."</sub>
- **descriptive / definition**: The active approach to concept drift has two phases: change detection and adaptation. (p. 7)[^original]  
  <sub>anchor: "In an active approach that handles concept drift, there are two phrases: change detection and adaption."</sub>
- **descriptive / method**: Change detection rarely works on raw data; it works on independent features, often based on domain expert knowledge, extracted from the incoming data stream. (p. 7)[^original]  
  <sub>anchor: "The change detection mechanism rarely operates directly on raw data, but instead on independent features"</sub>
- **descriptive / method**: Adaptation can be carried out through windowing, weighting or random sampling. (p. 7)[^original]  
  <sub>anchor: "The adaption can be done through windowing, weighting or random sampling"</sub>
- **descriptive / method**: Two main change-detection approaches have been proposed and adopted, differing by the entity analysed: one based on the distribution of the input data and one based on classification error. (p. 7)[^original]  
  <sub>anchor: "two main approaches for change detection had been proposed and adopted, which differ for the different entity in analysis"</sub>
- **descriptive / method**: The first distribution-based approach detects change in the joint pdf structure. (p. 7)[^original]  
  <sub>anchor: "The first approach detects the change in the jointed pdf structure."</sub>
- **descriptive / method**: The error-based approach evaluates variations in classification error on supervised data, using either a fixed or an adaptive accuracy threshold. (p. 7)[^original]  
  <sub>anchor: "The second approach evaluates variations in the classification error on supervised data"</sub>
- **descriptive / method**: In both error-based and distribution-based cases, a change is flagged as soon as classifier accuracy falls below the threshold. (p. 7)[^original]  
  <sub>anchor: "a change is detected as soon as the classifier’s accuracy falls below the threshold"</sub>
- **descriptive / method**: The first approach assesses drift in the pdf of the inputs without regard to their label values. (p. 7)[^original]  
  <sub>anchor: "The first approach assesses the drift of the pdf of the inputs disregarding their label values"</sub>
- **expected / method**: Once a change is detected, the classifier needs to adapt to the newly available information, and the source says it should also discard obsolete information. (p. 7)[^original]  
  <sub>anchor: "the classifier needs to adapt to the change from the newly available information"</sub>
- **descriptive / method**: A combined approach assesses stationarity both in the joint pdf of labelled data and in the input distribution of unlabelled data. (p. 8)[^original]  
  <sub>anchor: "assesses the stationary in both the joint probability density function of the labeled data"</sub>
- **descriptive / method**: Dal Pozzolo et al. treat immediate-feedback samples and delayed samples separately, train two distinct classifiers on each feedback type, and then aggregate their outputs. (p. 8)[^original]  
  <sub>anchor: "They suggested to trained two distinct classifiers based on each type of feedback respectively, and then aggregate the outputs"</sub>
- **descriptive / method**: Gao et al. use an ensemble of classifiers built on sequential chunks of training samples; each classifier is trained on a short period and updated frequently. (p. 8)[^original]  
  <sub>anchor: "each classifier is trained on a short period of time and updated frequently"</sub>

## 4. Model with dynamic risk features

- **descriptive / context**: The paper proposes a dynamic model intended to overcome the performance degradation caused by concept drift. (p. 8)[^original]  
  <sub>anchor: "In this paper, we propose a dynamic model that can overcome the model performance degradation caused by concept drift."</sub>
- **descriptive / method**: The strategy is to incorporate concept drift measures as dynamic risk features into both model training and scoring, so the model learns from static and dynamic features and self-adapts when drift occurs. (p. 8)[^original]  
  <sub>anchor: "Our strategy is to incorporate concept drift measures as dynamic risk features into model training and scoring."</sub>
- **descriptive / finding or result**: The approach is claimed to avoid the effort of constantly retraining the model to prevent performance degradation. (p. 8)[^original]  
  <sub>anchor: "This approach saves the effort to constantly retrain the model for preventing the performance degradation."</sub>
- **descriptive / method**: Tracking drift requires monitoring the probability distributions over time, using estimates of p_t(Y), p_t(X|Y) and p_t(Y|X). (p. 8)[^original]  
  <sub>anchor: "we need to consistently monitor the probability distributions with respect to time"</sub>
- **descriptive / limitation**: Instantaneous estimates of the probabilities are not an adequate measure of concept drift because they often vary from the norm. (p. 8)[^original]  
  <sub>anchor: "they are the instantaneous measures and could vary from the norm most of them time"</sub>
- **descriptive / method**: The authors use average probabilities within a sliding window as surrogates, approximated by frequency ratios. (p. 8)[^original]  
  <sub>anchor: "we use the average probabilities within a sliding window as surrogates"</sub>

## 4.1. Measuring concept drift using entity profile with fraud feedback

- **descriptive / method**: Two sliding windows of lengths h and H are used, computing statistics over short-term and long-term time spans before time t. (p. 8)[^original]  
  <sub>anchor: "Our approach is to use two sliding windows with lengths of"</sub>
- **descriptive / method**: The text illustrates the statistics calculation only on the short-term span, the long-term calculation being very similar. (p. 8)[^original]  
  <sub>anchor: "Later discussion will illustrate the statistics calculation only on short-term time span"</sub>
- **descriptive / method**: The probability of fraud at time t is estimated by the overall fraud rate (FR) within the time window before t. (p. 8)[^original]  
  <sub>anchor: "estimated by overall fraud rate (FR) within the time window"</sub>
- **descriptive / method**: The overall dollar-weighted fraud rate ($FR) is also proposed as a dynamic risk feature because it gives more weight to higher-value transactions and helps the model learn changes in fraud pattern. (p. 8)[^original]  
  <sub>anchor: "but it puts more weights on higher dollar value transactions and helps model to learn the fraud pattern change"</sub>
- **descriptive / data or feature**: Figure 3 plots overall fraud rate for one business partner on long-term and short-term sliding windows, with solid lines computed at time t and dashed lines giving final fraud rates computed offline. (p. 8)[^original]  
  <sub>anchor: "Figure 3 shows overall fraud rate calculated on the long-term sliding window (left) and short-term sliding window (right)."</sub>
- **descriptive / finding or result**: The solid (time t) and dashed (final) fraud-rate lines follow the same trending pattern, which the authors cite as justification for the formula used. (p. 8)[^original]  
  <sub>anchor: "These two lines follow the same trending pattern."</sub>
- **descriptive / limitation**: There is a varied time delay before the chargeback signal is received, which affects recent fraud-rate estimates. (p. 8)[^original]  
  <sub>anchor: "There is a varied time delay before receiving the chargeback signal."</sub>
- **descriptive / finding or result**: The gap between solid and dashed lines narrows because recent transactions have a higher share of chargebacks not yet received when plotted. (p. 8)[^original]  
  <sub>anchor: "The difference between the solid and dashed lines diminishes because that more recent transactions"</sub>

## 4. Model with dynamic risk features

- **descriptive / definition**: The paper uses the average probabilities within a sliding window as surrogates for the time-varying probabilities. (p. 8)[^original]  
  <sub>anchor: "we use the average probabilities within a sliding window as surrogates"</sub>

## 4.1. Measuring concept drift using entity profile with fraud feedback

- **descriptive / method**: The average probabilities are approximated by frequency ratios. (p. 8)[^original]  
  <sub>anchor: "and the average probabilities are approximated by frequency ratios."</sub>
- **expected / requirement**: The length of the sliding window needs to be chosen carefully. (p. 8)[^original]  
  <sub>anchor: "The length of the sliding window needs to be chosen carefully."</sub>
- **expected / requirement**: The sliding window should be long enough to give a good sample size for reliable estimation, while being short enough to remain sensitive to fluctuation. (p. 8)[^original]  
  <sub>anchor: "It should be long enough to have a good sample size for reliable estimation"</sub>

## 4.1.2. Using fraud rate of each transaction entity FRt(E) to measure pt(Y|X)

- **descriptive / method**: A transaction entity is described by a set of features X, and the authors propose measuring fraud rates profiled on important features. (p. 10)[^original]  
  <sub>anchor: "Therefore, we propose measuring the fraud rates profiled on important features."</sub>
- **descriptive / data or feature**: Table 1 gives, for each feature value within the window, the counts and dollar amounts of bad (Y=1) and good (Y=0) transactions, with marginal totals. (p. 10)[^original]  
  <sub>anchor: "the number of good and bad transactions and their dollar amounts for each transaction entity and marginal totals are shown in Table 1."</sub>
- **descriptive / definition**: Fraud rates and dollar-weighted fraud rates for the entity within the window are the risk features used to measure p_t(Y|X). (p. 10)[^original]  
  <sub>anchor: "Thus, the fraud rates and dollar weighted fraud rates for entity"</sub>
- **descriptive / case example**: Figure 4 illustrates entity-profiled fraud rate for a selected object, such as one particular product chosen as the entity. (p. 11)[^original]  
  <sub>anchor: "For example, we can select ?product name? as the entity and one particular product as the selected object."</sub>
- **descriptive / data or feature**: In the Figure 4 example, the red line is the fraud rate over 4-week sliding windows and the black line is over 8-week sliding windows. (p. 11)[^original]  
  <sub>anchor: "Red line is the fraud rate calculated by 4-week sliding windows and the black line is for 8-week sliding windows."</sub>
- **descriptive / case example**: The selected product was under attack around November 2016. (p. 11)[^original]  
  <sub>anchor: "As we can see, this object is under attack around the November 2016."</sub>
- **descriptive / finding or result**: The 4-week window fraud rate is more sensitive to fraud attacks than the 8-week one. (p. 11)[^original]  
  <sub>anchor: "FR calculated within the 4-week sliding window is more sensitive to fraud attack."</sub>
- **descriptive / typology or red flag**: When short-term FR is higher than long-term FR, fraudsters are attacking that product recently. (p. 11)[^original]  
  <sub>anchor: "When the short-term FR is higher than long-term FR, it indicates that fraudsters are attacking this product recently."</sub>
- **descriptive / typology or red flag**: When short-term FR is lower, fraudsters have diverted their attention to other products. (p. 11)[^original]  
  <sub>anchor: "if short-term FR is lower, it means fraudsters divert their attention to the other products."</sub>
- **descriptive / finding or result**: The gap between long-term and short-term FR reflects the severity of the fraud attack. (p. 11)[^original]  
  <sub>anchor: "the difference between long-term FR and short-term FR reflects the fraud attack severity."</sub>

## 4.1.3. Using Weight of Evidence on features of entities to measure pt(X|Y)

- **descriptive / method**: The authors propose estimating Weight of Evidence (WoE) on entity features to measure p_t(X|Y), because X is high-dimensional. (p. 11)[^original]  
  <sub>anchor: "We propose to use the estimation of"</sub>
- **descriptive / definition**: WoE is known in credit risk modelling and is computed from the counts and dollar amounts of bad and good transactions in the window. (p. 11)[^original]  
  <sub>anchor: "where Ni 1($ i 1) Ni 0($10) are the count and dollar amount for bad and good transactions"</sub>
- **descriptive / definition**: WoE of a feature value is the difference between the log of odds ratios of that value and that of the overall population. (p. 11)[^original]  
  <sub>anchor: "the difference between the log of odds ratios of"</sub>
- **descriptive / finding or result**: WoE indicates which feature values fraudsters are attacking. (p. 11)[^original]  
  <sub>anchor: "That is to say, WoE provides an indication of fraudsters? attacking target feature."</sub>
- **descriptive / case example**: In Figure 5, among ten products A-J, Product B was targeted by fraudsters on March 1st, when its WoE was above zero. (p. 11)[^original]  
  <sub>anchor: "Product B is targeted by fraudsters on March 1st where its WoE is above zero."</sub>
- **descriptive / case example**: Later, Product G became the attack target, on April 15, while Product B was no longer attacked. (p. 11)[^original]  
  <sub>anchor: "Product G becomes the attack target on April 15."</sub>
- **descriptive / method**: Feature selection is pivotal; example features include product name, account email domain, billing country and merchant name. (p. 11)[^original]  
  <sub>anchor: "Important features could include product name, account email domain, billing country, merchant name, and so forth."</sub>
- **descriptive / limitation**: Too few feature values make the feature too broad for probability fluctuations to appear; the example given is market country, which hides attacks on different products within one country. (p. 11)[^original]  
  <sub>anchor: "then fraudster attack different product within the same country won?t appear in the tracking"</sub>
- **descriptive / limitation**: Too many feature values make the frequency-ratio approximations for each feature unstable. (p. 11)[^original]  
  <sub>anchor: "Otherwise, the frequency ratio approximations for each feature would be unstable."</sub>
- **descriptive / definition**: The Weight of Evidence for a feature value is the difference between the log odds ratio of that value and the log odds ratio of the overall population. (p. 11)[^original]  
  <sub>anchor: "is the difference between the log of odds ratios of"</sub>
- **descriptive / typology or red flag**: A positive WoE indicates that the odds of a feature value being fraudulent are higher than average, which points to fraudsters' attack target; a negative WoE means the odds are lower than average. (p. 11)[^original]  
  <sub>anchor: "WoE provides an indication of fraudsters? attacking target feature."</sub>
- **expected / requirement**: A feature should be selected so that the number of its values is neither too few nor too many. (p. 11)[^original]  
  <sub>anchor: "An feature should be selected such that the number of feature values should not be too few or too many."</sub>

## 4.2. Measuring concept drift using entity profile with fraud feedback

- **descriptive / method**: A dynamic risk feature set is built from the chosen set of entities, with each entity's features computed from the statistics above. (p. 13)[^original]  
  <sub>anchor: "The dynamic risk feature set is constructed as"</sub>
- **descriptive / method**: At each update time stamp the feature set is calculated from transactions in the two sliding windows, and then applied to transactions in the following interval. (p. 13)[^original]  
  <sub>anchor: "Later, for transactions happened within time span"</sub>
- **descriptive / data or feature**: Each transaction is assembled with its dynamic risk features, so the assembled vector has p original static features plus q dynamic risk features. (p. 13)[^original]  
  <sub>anchor: "calculated in a relative frequent fashion"</sub>
- **descriptive / context**: The authors state that the justification for their equation comes from the indicating power of the feature to the probability. (p. 13)[^original]  
  <sub>anchor: "The justification for Equation (26) comes from the indicating power of"</sub>
- **expected / requirement**: Dynamic risk features need to be updated relatively frequently to approximate real-time fluctuation, at pre-defined update time stamps. (p. 13)[^original]  
  <sub>anchor: "To approximate real-time fluctuation, dynamic risk features need to be updated relative frequently."</sub>
- **descriptive / method**: The dynamic model is trained with the dynamic risk features as training inputs, since it includes the dynamic risk features. (p. 13)[^original]  
  <sub>anchor: "it includes the dynamic risk features"</sub>
- **descriptive / finding or result**: For the dynamic model, the output score at time t+1, using the assembled dynamic risk feature as input, is stated to satisfy Equation (26), which the paper justifies by the indicating power of the dynamic feature for the probability. (p. 13)[^original]  
  <sub>anchor: "The justification for Equation (26) comes from the indicating power"</sub>
- **descriptive / finding or result**: Without updating the existing model between t and t+1, the dynamic model can overcome concept drift and predict fraud probability at t+1 more accurately, according to the authors. (p. 14)[^original]  
  <sub>anchor: "the dynamic model can overcome concept drift phenomenon to predict the probability of a transaction being fraudulent"</sub>
- **descriptive / method**: The approach was validated on online purchase transaction data from two Microsoft business partners. (p. 14)[^original]  
  <sub>anchor: "Online purchase transaction data from two of Microsoft’s business partners were used to valid our approach."</sub>
- **descriptive / method**: For each business partner, 70% of transactions were randomly selected for training and the remaining 30% for testing. (p. 14)[^original]  
  <sub>anchor: "Within each, we randomly select 70% transactions for training and the rest 30% for testing."</sub>
- **descriptive / method**: Static and dynamic models are trained on the same transactions and evaluated on the same test dataset for each partner. (p. 14)[^original]  
  <sub>anchor: "static and dynamic models are trained over the same set of transactions and evaluated on the same test dataset."</sub>
- **descriptive / method**: FastTree, an efficient implementation of the MART gradient boosting algorithm, is used as the model training algorithm. (p. 14)[^original]  
  <sub>anchor: "FastTree, known as an efficient implementation of the MART gradient boosting algorithm [2], is used as our model training algorithm."</sub>
- **descriptive / context**: The configuration for the dynamic model is described next, but the excerpt ends before the details are given. (p. 14)[^original]  
  <sub>anchor: "The configuration for dynamic model is"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Adaptive Fraud Detection System Using Dynamic Risk Features" (2018-10-10). https://arxiv.org/abs/1810.04654
