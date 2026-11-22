---
type: Source Digest
title: 'FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection - part 1 of 3 (pp. 1-6)'
description: 'Verified paraphrased digest, pp. 1-6: FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection; FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection > Abstract; FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection > 1 Introduction; and 8 more sections'
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
part: 1
parts_total: 3
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
  resource: https://arxiv.org/abs/2502.02290
  title: 'FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection'
  author: org:arxiv
  last_modified: '2025-04-02T00:00:00Z'
digest_points: 92
---

# FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The attack FRAUD-RLA is designed to maximise the attacker's reward by optimising the exploration-exploitation tradeoff while working with significantly less required knowledge than competitors. (p. 1)[^original]  
  <sub>anchor: "designed to maximize the attacker’s reward by optimizing the exploration-exploitation tradeoff"</sub>
- **descriptive / finding or result**: The experiments were conducted on three different heterogeneous datasets and against two fraud detection systems, and indicate that FRAUD-RLA is effective even under the severe limitations of the threat model. (p. 1)[^original]  
  <sub>anchor: "conducted on three different heterogeneous datasets and against two fraud detection systems"</sub>

## 1 Introduction

- **descriptive / context**: Credit card payments in the euro area accounted for over 50 trillion euros in the first half of 2023. (p. 1)[^original]  
  <sub>anchor: "In the first half of 2023, credit card payments in the euro area accounted for over 50 trillion euros"</sub>
- **descriptive / context**: Given the size and economic relevance of the domain, the paper states that ensuring the robustness of payment systems is paramount and that large resources are spent on improving fraud detection. (p. 1)[^original]  
  <sub>anchor: "ensuring the robustness of payment systems is paramount"</sub>
- **descriptive / limitation**: Proper assessments of the risk posed by adaptive fraudsters' strategies are lacking in the literature. (p. 1)[^original]  
  <sub>anchor: "proper assessments of the risk posed by adaptive fraudsters’ strategies are lacking in the literature"</sub>
- **descriptive / context**: Most adversarial attacks created over the past decade focus on image recognition, which makes generalisation to credit card fraud detection challenging. (p. 1)[^original]  
  <sub>anchor: "the majority of them focus on image recognition"</sub>
- **descriptive / finding or result**: Only a handful of works have studied adversarial machine learning in credit card fraud detection, and the main ones attack the BankSealer fraud detection engine. (p. 1)[^original]  
  <sub>anchor: "The main works [10, 11] attack the same realistic fraud detection engine called BankSealer [9]"</sub>
- **descriptive / limitation**: The prior works assume fraudsters can access customers' transaction history, which the authors note may be achieved by introducing malware into victims' devices. (p. 1)[^original]  
  <sub>anchor: "they operate under the assumption that fraudsters can access the customers’ transaction history"</sub>
- **descriptive / limitation**: Compromising a device to observe past transactions is significantly more complex than stealing or cloning a card, which may limit the scalability of such attacks. (p. 1)[^original]  
  <sub>anchor: "This may limit the scalability of such attacks and, therefore, their capacity to compromise the overall system security"</sub>
- **descriptive / context**: Earlier works noted the lack of human supervision and the significance of aggregated features, but did not develop a systemic analysis of the threat. (p. 1)[^original]  
  <sub>anchor: "Past works have discussed the lack of human supervision [30] and the significance of aggregated features [31]"</sub>
- **descriptive / finding or result**: Table 1 shows that existing approaches fail to cope with unknown features, restricted access to the fraud detection engine, and the inability to exploit the absence of human investigation. (p. 1)[^original]  
  <sub>anchor: "existing approaches fail to cope with unknown features, restricted access to the fraud detection engine"</sub>
- **descriptive / context**: The source says research on fraud detection has focused on the statistical properties of frauds, and that proper assessments of the risk posed by adaptive fraudster strategies are lacking in the literature. (p. 1)[^original]  
  <sub>anchor: "Research on fraud detection, however, has focused on the statistical properties of frauds"</sub>
- **descriptive / method**: The main contribution models the generation of fraudulent transactions not detectable by the classifier as a reinforcement learning problem, in which the agent is rewarded when it fools the classifier. (p. 2)[^original]  
  <sub>anchor: "We model the problem of generating fraudulent transactions not detectable by the classifier as an RL problem"</sub>
- **descriptive / method**: Proximal Policy Optimization is identified as a suitable RL algorithm and is used to create the attack named FRAUD-RLA. (p. 2)[^original]  
  <sub>anchor: "We identify Proximal Policy Optimization [42, PPO] as a suitable RL algorithm"</sub>
- **descriptive / finding or result**: The authors claim that their analysis and experiments show FRAUD-RLA to be the most effective attack against credit card fraud detection systems. (p. 2)[^original]  
  <sub>anchor: "Our analysis and experiments show that FRAUD-RLA is the most effective attack against credit card fraud detection systems"</sub>
- **descriptive / finding or result**: Unlike previous works, FRAUD-RLA does not require the same degree of access to the model or to users' transaction history. (p. 2)[^original]  
  <sub>anchor: "Unlike previous works, FRAUD-RLA does not require the same degree of access to the model or the users’ transaction history"</sub>
- **descriptive / method**: Using RL allows the tradeoff between the quality of the attack pattern found and the time required to find it to be modelled explicitly. (p. 2)[^original]  
  <sub>anchor: "using RL allows us to explicitly model the tradeoff between the quality of the attack pattern found and the time required to find it"</sub>
- **descriptive / method**: The method is tested against fraud detection engines on real and synthetic datasets, with results reported in Section 4.2. (p. 2)[^original]  
  <sub>anchor: "we test our method against fraud detection engines on real and synthetic datasets"</sub>

## 2 Background

- **descriptive / definition**: A transaction is an amount paid to a merchant by a cardholder at a given time. (p. 2)[^original]  
  <sub>anchor: "Essentially, a transaction consists of an amount paid to a merchant by a cardholder at a given time"</sub>
- **descriptive / definition**: Raw features are the features characterising cards and terminals and those directly chosen by the user, such as the transaction amount. (p. 2)[^original]  
  <sub>anchor: "We call raw features these features and the ones directly chosen by the user, such as the transaction amount"</sub>
- **descriptive / definition**: Aggregated features are generated by aggregating transactions based on the card or terminal identifier, using customer or terminal history. (p. 2)[^original]  
  <sub>anchor: "These aggregations are then used to generate a set of features called"</sub>
- **descriptive / context**: The fraud detection system is built on a composition of human-made rules and machine learning, which signal the most likely frauds to investigators. (p. 2)[^original]  
  <sub>anchor: "This system is built on a composition of human-made rules and machine learning"</sub>

## 2.1.2 Attackers

- **descriptive / definition**: The attacker's goal in credit card fraud detection is to deceive the system into misclassifying their frauds as genuine transactions. (p. 2)[^original]  
  <sub>anchor: "deceive the fraud detection system into misclassifying their frauds as genuine transactions"</sub>
- **descriptive / context**: Fraudsters can access only a limited set of cards, which may be blocked over time, so they must maximise successful frauds from the start. (p. 2)[^original]  
  <sub>anchor: "fraudsters can access a limited set of cards, which may be blocked over time"</sub>
- **descriptive / context**: Fraud detection data are subject to concept drift, forcing classifiers to adapt, so attack patterns may stop working after a model update. (p. 2)[^original]  
  <sub>anchor: "fraud detection data are subject to concept drift"</sub>
- **expected / expectation**: In fraud detection, imperceptibility should not be part of the attackers' goal, because humans observe only a few suspicious transactions. (p. 2)[^original]  
  <sub>anchor: "In fraud detection, imperceptibility should not be part of the attackers’ goal"</sub>
- **descriptive / definition**: The attackers are assumed to know the principles on which the system is built, such as its feature engineering process, but not the weights of the trained classifier, which change over time. (p. 3)[^original]  
  <sub>anchor: "we assume that attackers may know the principles around which the system is built"</sub>
- **descriptive / context**: Reconstructing the card's and terminal's transaction history to know aggregated features is challenging, and malware use would impose a strong requirement on attackers. (p. 3)[^original]  
  <sub>anchor: "To know these, fraudsters must reconstruct the card’s and terminal’s transaction history, which is challenging"</sub>
- **descriptive / definition**: Attackers are assumed to know the feature transformation and general model characteristics, and may know some fixed card features, but not the aggregate features. (p. 3)[^original]  
  <sub>anchor: "attackers know the feature transformation and the general model characteristics and may know some fixed card features, but do not know the aggregate features"</sub>
- **descriptive / finding or result**: Previous literature supports this hypothesis, since most fraudsters seem not to be influenced by the cardholder's behaviour before their first fraud with a new stolen card. (p. 3)[^original]  
  <sub>anchor: "most fraudsters seem not to be influenced by the cardholder’s behavior before their first fraud with a new stolen card"</sub>
- **descriptive / definition**: Attackers are able to decide the values of transaction features such as the amount, but cannot modify fixed card features. (p. 3)[^original]  
  <sub>anchor: "First, they are able to decide the value of transaction features, such as the amount"</sub>
- **descriptive / context**: Image recognition attacks are designed to be indistinguishable by humans, whereas investigators in fraud detection can only observe the most likely frauds. (p. 3)[^original]  
  <sub>anchor: "image recognition attacks are designed to be indistinguishable by humans, but investigators can only observe the most likely frauds"</sub>
- **descriptive / context**: In fraud detection, fraudsters are evaluated over each transaction, with no difference between query and attack time, unlike standard adversarial attacks. (p. 3)[^original]  
  <sub>anchor: "fraudsters are evaluated over each transaction, with no difference between query and attack time"</sub>

## 2.2.1 Taxonomy

- **descriptive / definition**: Query-based attacks acquire information through queries, i.e., attempted attacks, and use the target classifier's feedback to improve attack quality. (p. 3)[^original]  
  <sub>anchor: "Query-based attacks acquire information through queries, i.e., attempted attacks"</sub>
- **descriptive / method**: Boundary Attack first samples the data space to find a valid attack and then moves along the decision boundary toward the original observation. (p. 3)[^original]  
  <sub>anchor: "Boundary Attack [7] first samples the data space to find a valid attack"</sub>
- **descriptive / limitation**: Query-based attacks have no mechanism to optimise the exploration-exploitation tradeoff, since each attack requires a constant number of queries. (p. 3)[^original]  
  <sub>anchor: "they have no mechanism to optimize the exploration-exploitation tradeoff"</sub>
- **descriptive / limitation**: Image-recognition imperceptibility constraints make query-based attacks incredibly inefficient when that constraint is irrelevant. (p. 3)[^original]  
  <sub>anchor: "making them incredibly inefficient when such constraint is irrelevant"</sub>
- **descriptive / limitation**: Query-based attacks assume full data knowledge to estimate the local decision boundaries. (p. 3)[^original]  
  <sub>anchor: "Finally, they assume full data knowledge to estimate the local boundaries"</sub>

## 2.2 Adversarial Attacks

- **descriptive / method**: Surrogate model attacks train a substitute classifier on a labelled training set and use attack transferability to break the target classifier. (p. 3)[^original]  
  <sub>anchor: "if the attacker can access a labeled training set, they can train a surrogate model"</sub>
- **descriptive / limitation**: Fraud detection datasets are realistically hard for an attacker to obtain, so surrogate model attacks are extremely hard to apply. (p. 4)[^original]  
  <sub>anchor: "Fraud detection datasets, however, are realistically challenging for an attacker to obtain"</sub>
- **descriptive / method**: Mimicry attacks craft inputs that mimic a particular class of data so the classifier recognises them as belonging to that class. (p. 4)[^original]  
  <sub>anchor: "they might craft attacks that mimic those data so that the classifier recognizes them as belonging to that class"</sub>
- **descriptive / finding or result**: The key advantage of Mimicry over surrogate model attacks is that Mimicry only needs genuine data. (p. 4)[^original]  
  <sub>anchor: "The key advantage compared to Surrogate Model attacks is that Mimicry attacks only need genuine data"</sub>
- **descriptive / context**: Credit card fraud data are highly unbalanced, so an unsupervised dataset is likely composed primarily of genuine transactions and suits training Mimicry. (p. 4)[^original]  
  <sub>anchor: "Credit card fraud detection data are highly unbalanced, meaning that any random sample of data is likely to be composed mainly of genuine data"</sub>
- **descriptive / limitation**: Reinforcement learning attacks used in cross-site scripting and malware detection are domain-specific, leaving many questions unanswered for fraud detection. (p. 4)[^original]  
  <sub>anchor: "These works, however, are domain-specific, and their application to credit card fraud detection leaves many unanswered questions"</sub>
- **descriptive / context**: Unlike malware attacks, fraud attackers can choose their feature values freely, without a starting point to modify. (p. 4)[^original]  
  <sub>anchor: "attackers can choose the values of their features freely, without a starting point to modify"</sub>

## 2.2.2 Attacks on Credit Card Fraud Detection

- **descriptive / context**: Prior fraud attacks assume fraudsters can inject the victim's device with a banking Trojan, allowing them to perform frauds and observe previous transactions. (p. 4)[^original]  
  <sub>anchor: "assume that fraudsters can inject the victim’s device with a banking Trojan"</sub>
- **descriptive / method**: One prior fraud attack uses a previously acquired dataset of genuine transactions to model genuine users' behaviour and blend frauds into it. (p. 4)[^original]  
  <sub>anchor: "fraudsters can use a previously acquired dataset of genuine transactions to build a model"</sub>
- **descriptive / method**: Another prior attack trains a substitute model called Oracle on a set of transactions resembling the training data, and uses it to craft frauds. (p. 4)[^original]  
  <sub>anchor: "they can train a substitute model, called Oracle, and use it to craft their frauds"</sub>
- **descriptive / context**: The substitute training set can be old or belong to a different institution, provided the patterns are close enough to allow attack transferability. (p. 4)[^original]  
  <sub>anchor: "such a training set can be old or belong to a different institution"</sub>
- **descriptive / finding or result**: Both prior attacks can be performed in a Black-Box setting, and modelling the target before attacking implicitly solves the exploration-exploitation tradeoff. (p. 4)[^original]  
  <sub>anchor: "using a training set to model the target classifier before starting the attacks implicitly solves the exploration-exploitation tradeoff"</sub>
- **descriptive / limitation**: The prior attacks require data to build a surrogate training set, which may be hard and costly to acquire for most attackers. (p. 4)[^original]  
  <sub>anchor: "they require data to build a surrogate training set, which may be hard to acquire for most attackers"</sub>
- **descriptive / limitation**: Attacking a customer requires a banking Trojan, a much stronger assumption than cloning or stealing the card, which may limit the number of attackers. (p. 4)[^original]  
  <sub>anchor: "attacking a customer requires injecting their device with a banking Trojan"</sub>
- **descriptive / limitation**: The prior attacks assume classifiers use only raw and customer-based features, whereas other works also use terminal-based aggregations. (p. 4)[^original]  
  <sub>anchor: "these attacks assume that classifiers use only raw and customer-based features"</sub>
- **descriptive / context**: Attacking terminal-based aggregations would require fraudsters to also control the terminal, further increasing difficulty. (p. 4)[^original]  
  <sub>anchor: "To attack them using these methods, fraudsters would also need to control the terminal"</sub>

## 3 FRAUD-RLA

- **descriptive / method**: FRAUD-RLA's design has three core elements: problem formulation, a task definition as a single-step POMDP, and a PPO-based solution. (p. 4)[^original]  
  <sub>anchor: "where we reformulate the problem as a single-step Partially Observable Markov Decision Process (POMDP) [35,46]"</sub>
- **descriptive / method**: Proximal Policy Optimization is a gradient-based technique capable of online learning the best attack policy. (p. 4)[^original]  
  <sub>anchor: "a gradient-based technique capable of online learning the best attack policy"</sub>

## 3.1 Problem Formulation

- **descriptive / data or feature**: A transaction is a triplet of controllable features chosen by the attacker, known features and unknown features. (p. 4)[^original]  
  <sub>anchor: "such as the history of previous transactions"</sub>
- **descriptive / definition**: Controllable features are chosen by the attacker, such as the transaction amount, while known features such as the card number are visible to the attacker. (p. 5)[^original]  
  <sub>anchor: "are the features _controllable_ by the attacker, such as the amount of the transaction"</sub>
- **descriptive / definition**: The fraud detection engine returns a block/accept decision and combines a rule-based classifier and a data-driven classifier. (p. 5)[^original]  
  <sub>anchor: "This fraud detection engine is internally composed of a mix of rule-based and data-driven classification algorithms"</sub>
- **descriptive / method**: The attacker observes the known features, chooses the controllable features, and submits them; the operation is repeated for a fixed number of rounds to model the limited number of frauds. (p. 5)[^original]  
  <sub>anchor: "To model the limited number of frauds an attacker can perform"</sub>

## Table 1

- **descriptive / definition**: Table 1 compares prominent adversarial attack families against fraud detection constraints; YES means full fulfilment, NO means the design makes the constraint exceptionally challenging, and Partially means the design does not explicitly make it difficult. (p. 5)[^original]  
  <sub>anchor: "Attacks can completely fulfill the requirement (YES), be designed in a way that makes it exceptionally challenging to tackle (NO)"</sub>
- **descriptive / finding or result**: Table 1 rates Query-Based attacks as Black Box YES but NO for imperceptibility, starting point, data knowledge and exploration-exploitation tradeoff, and YES for training set access. (p. 5)[^original]  
  <sub>anchor: "Compliance of prominent adversarial attack families to fraud detection constraints"</sub>
- **descriptive / finding or result**: Table 1 rates Surrogate Model, Mimicry and Fraud Attacks as mostly YES or Partially, with Fraud Attacks marked NO for data knowledge, while the FRAUD-RLA row is YES for all six columns. (p. 5)[^original]  
  <sub>anchor: "With FRAUD-RLA we refer to the attack proposed in this paper"</sub>

## 3 FRAUD-RLA

- **descriptive / method**: Algorithm 1 aims to maximise the sum of successful frauds, that is the total reward, over the training time budget. (p. 5)[^original]  
  <sub>anchor: "FRAUD-RLA to maximize the sum of successful frauds (total reward) over training time"</sub>

## 3.2 RL environment

- **descriptive / method**: The environment is modelled as a single-step POMDP with state, observation, action, transition, reward and observation functions. (p. 5)[^original]  
  <sub>anchor: "We model the environment as a single-step Partially Observable Markov Decision Process (POMDP) [35, 46]"</sub>
- **descriptive / definition**: The state space is continuous and contains every possible transaction. (p. 5)[^original]  
  <sub>anchor: "is a continuous space of size R_U_+_K_+_C_ , i.e. every possible transaction"</sub>
- **descriptive / definition**: The observation space is the continuous set of possible observations, consisting of every possible known feature. (p. 5)[^original]  
  <sub>anchor: "is the continuous space set of possible observations"</sub>
- **descriptive / definition**: The action space is continuous and of controllable-feature dimension. (p. 5)[^original]  
  <sub>anchor: "is a continuous action space of size"</sub>
- **descriptive / definition**: The transition function is deterministic, mapping each state-action pair to a next state, and each initial state is followed by a terminal state since there is a single step. (p. 5)[^original]  
  <sub>anchor: "is a deterministic transition function that maps each state-action"</sub>
- **descriptive / definition**: The observation function extracts the known features from the full transaction. (p. 5)[^original]  
  <sub>anchor: "extracts the observation from the state, i.e. extracts"</sub>

## 3.3 RL agent

- **descriptive / method**: PPO is chosen as a single-agent Deep RL algorithm because it handles continuous action spaces and requires little hyperparameter tuning. (p. 5)[^original]  
  <sub>anchor: "PPO is known to require little hyperparameter tuning compared to other Deep RL methods"</sub>

## 3.1 Problem Formulation

- **descriptive / definition**: A transaction is considered genuine if it is accepted by both the rule-based and the data-driven classifiers. (p. 5)[^original]  
  <sub>anchor: "A transaction is considered genuine if accepted by both classifiers"</sub>
- **descriptive / method**: Algorithm 1 describes FRAUD-RLA as an approach that aims to maximize the sum of successful frauds (total reward) over training time. (p. 5)[^original]  
  <sub>anchor: "FRAUD-RLA to maximize the sum of successful frauds (total reward) over training time"</sub>

## 3.3 RL agent

- **descriptive / method**: Each round, FRAUD-RLA receives known features, PPO produces a conditional multivariate Gaussian over controllable features, samples them, and receives reward 1 minus the classifier output. (p. 6)[^original]  
  <sub>anchor: "which generates a conditional multivariate Gaussian distribution over the controllable features space"</sub>
- **descriptive / method**: Attackers are assumed to operate without prior knowledge of the data, so they must learn it throughout training. (p. 6)[^original]  
  <sub>anchor: "we assume that the attackers operate without prior knowledge of the data"</sub>
- **descriptive / method**: The actor outputs C values used as means and C-squared values used as the covariance matrix of the multivariate normal distribution from which actions are sampled. (p. 6)[^original]  
  <sub>anchor: "values as the covariance matrix of the multivariate normal distribution from which actions are sampled"</sub>
- **descriptive / context**: Prior domain works learn only the means of a normal distribution and use either a hand-crafted constant or an annealed value for the variance. (p. 6)[^original]  
  <sub>anchor: "only learn the means of a normal distribution and either use a hand-crafted constant or an annealed value for the variance"</sub>

## 3.3.2 Partial observability

- **descriptive / method**: PPO uses an actor-critic architecture, in which the actor maps observations to actions and the critic estimates the value of observations. (p. 6)[^original]  
  <sub>anchor: "Internally, PPO uses an actor-critic architecture [6]"</sub>
- **descriptive / method**: In a single-step environment the critic's value of an observation equals the reward associated with that observation. (p. 6)[^original]  
  <sub>anchor: "Since we are working in a single-step environment, we can express it as the reward associated with the observation"</sub>
- **descriptive / method**: Training optimises the actor's policy with a clipped objective to keep updates stable, and optimises the critic with a mean squared error loss. (p. 6)[^original]  
  <sub>anchor: "using a clipped objective function to maximize the updates’ stability"</sub>
- **descriptive / method**: The actor and critic each use a straightforward architecture with two fully connected inner layers of 32 nodes, chosen to avoid specific hyperparameter tuning. (p. 6)[^original]  
  <sub>anchor: "Since we want FRAUD-RLA to work in different settings and on different datasets without specific hyperparameter tuning, we opted for a straightforward architecture"</sub>
- **descriptive / method**: A normalisation layer was added to the Critic Network to facilitate algorithm convergence. (p. 6)[^original]  
  <sub>anchor: "A normalization layer in the Critic Network was added to facilitate the algorithm convergence"</sub>
- **descriptive / method**: Recurrent networks are not used because they serve to remember earlier steps of an episode, and each episode here has only one step. (p. 6)[^original]  
  <sub>anchor: "Since we work in an environment where there is only one step in an episode, there is no need for recurrent networks"</sub>

## 3.3.1 Correlations in the action space

- **descriptive / method**: Unlike most single-agent RL works with continuous actions, FRAUD-RLA learns both the means and the covariance matrix of a multivariate normal action distribution. (p. 6)[^original]  
  <sub>anchor: "we differ from most of them by learning the parameters (both the means and the covariance matrix) of a multivariate normal distribution for the action space"</sub>

## 4 Experiments Design

- **descriptive / method**: All three datasets were balanced for the experiments, because class balance does not directly affect FRAUD-RLA. (p. 6)[^original]  
  <sub>anchor: "Because class balance does not directly affect FRAUD-RLA, all datasets have been balanced for these experiments"</sub>
- **descriptive / method**: The Mimicry attack is trained using only genuine transactions so that balancing does not negatively affect it. (p. 6)[^original]  
  <sub>anchor: "To guarantee Mimicry is not negatively affected by this change, we train it using only genuine transactions"</sub>
- **descriptive / data or feature**: The Generator Dataset is generated with the synthetic credit card fraud detection generator from reference [28]. (p. 6)[^original]  
  <sub>anchor: "Generator Dataset generated employing the synthetic credit card fraud detection generator from [28]"</sub>
- **descriptive / data or feature**: The generator builds transactions from customers interacting with terminals, inserting frauds according to previously defined patterns. (p. 6)[^original]  
  <sub>anchor: "is built on a set of customers interacting with terminals to create transactions, where frauds are inserted according to previously defined patterns"</sub>
- **descriptive / data or feature**: Unlike other works, the generated datasets keep feature semantics so that aggregated features can be composed. (p. 6)[^original]  
  <sub>anchor: "the resulting datasets maintain the features’ semantics, allowing aggregated features to be composed"</sub>
- **descriptive / data or feature**: Generated features can be split into purely transaction-based features such as the amount, customer-aggregated features and terminal-aggregated features. (p. 6)[^original]  
  <sub>anchor: "This allows us to divide features into purely transaction-based (like the amount), aggregated on the customer, and aggregated on the terminal"</sub>

## 3.3 RL agent

- **descriptive / method**: One motivation for learning the covariance matrix is the assumption that the features of a transaction (the action) are correlated. (p. 6)[^original]  
  <sub>anchor: "we assume that the features of a transaction (i.e. the action) are correlated"</sub>

## 3.3.2 Partial observability

- **descriptive / method**: The two fully connected inner layers of both the actor and critic networks each have 32 nodes, chosen as a straightforward architecture so FRAUD-RLA can work across settings without specific hyperparameter tuning. (p. 6)[^original]  
  <sub>anchor: "with both networks presenting only two fully connected inner layers of 32 nodes each"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection" (2025-04-02). https://arxiv.org/abs/2502.02290
