---
type: Source Digest
title: 'FiFAR: A Fraud Detection Dataset for Learning to Defer - part 1 of 3 (pp. 1-3)'
description: 'Verified paraphrased digest, pp. 1-3: ABSTRACT; KEYWORDS; 1 INTRODUCTION; and 6 more sections'
resource: https://arxiv.org/abs/2312.13218
tags:
- academic_finding
- alerts_triage
- global_academic
- ml_statistics
- model_development
- preprint
status: stable
source_id: arxiv-fifar-a-fraud-detection-dataset-for-learning-to-defer
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-12-20'
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
  resource: https://arxiv.org/abs/2312.13218
  title: 'FiFAR: A Fraud Detection Dataset for Learning to Defer'
  author: org:arxiv
  last_modified: '2023-12-20T00:00:00Z'
digest_points: 51
---

# FiFAR: A Fraud Detection Dataset for Learning to Defer (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-3) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## ABSTRACT

- **descriptive / context**: Public dataset limitations have hindered development and benchmarking of learning to defer (L2D) algorithms, which combine human and AI capabilities in hybrid decision-making; obtaining human predictions for training and evaluation is costly. (p. 1)[^original]  
  <sub>anchor: "Public dataset limitations have significantly hindered the development and benchmarking of learning to defer"</sub>
- **descriptive / context**: The authors note that no publicly available L2D datasets existed for financial fraud detection, a high-stakes setting where algorithms and human experts work in tandem. (p. 1)[^original]  
  <sub>anchor: "there are no publicly available datasets for L2D concerning this important application of human-AI teaming"</sub>
- **descriptive / data or feature**: The paper introduces the Financial Fraud Alert Review (FiFAR) dataset, a synthetic bank account fraud detection dataset containing predictions of a team of 50 synthetic fraud analysts with varied bias and feature dependence. (p. 1)[^original]  
  <sub>anchor: "we introduce the _Financial Fraud Alert Review_ Dataset (FiFAR), a synthetic bank account fraud detection dataset"</sub>
- **descriptive / method**: The authors provide a definition of human work capacity constraints, an often overlooked aspect of L2D systems, enabling testing of assignment systems under real-world conditions. (p. 1)[^original]  
  <sub>anchor: "We also provide a realistic definition of human work capacity constraints, an aspect of L2D systems that is often overlooked"</sub>
- **descriptive / finding or result**: A capacity-aware L2D method and a rejection learning approach are developed under realistic data availability and benchmarked across 300 distinct testing scenarios. (p. 1)[^original]  
  <sub>anchor: "benchmark these baselines under an array of 300 distinct testing scenarios"</sub>
- **descriptive / context**: The public dataset and detailed synthetic expert information are released on GitHub. (p. 1)[^original]  
  <sub>anchor: "The public dataset and detailed synthetic expert information are available at"</sub>

## 1 INTRODUCTION

- **descriptive / context**: Financial fraud detection is a high-stakes use case for human-AI collaboration; in anti-money laundering, an automated system monitors transactions and raises alerts that human experts review. (p. 1)[^original]  
  <sub>anchor: "Machine Learning models can be used in anti-money laundering, where an automated system monitors transactions, raising alerts that are then reviewed by humanexperts"</sub>
- **descriptive / context**: In e-commerce transaction fraud detection, ML model advice may improve human decision-makers' accuracy and expedite decisions. (p. 1)[^original]  
  <sub>anchor: "In e-commerce transaction fraud detection, ML models’ advice may help improve the accuracy of human decision-makers"</sub>
- **descriptive / context**: Research applying L2D in fraud prevention is lacking, possibly due to a lack of adequate public datasets in this domain. (p. 1)[^original]  
  <sub>anchor: "research into applying L2D in fraud prevention settings is lacking, possibly due to a lack of adequate public datasets"</sub>
- **descriptive / data or feature**: FiFAR includes predictions of a team of 50 highly complex synthetic fraud analysts, generated to simulate varied human behaviours, with control over performance, feature dependence and bias towards a protected attribute, and capacity constraints limiting deferred instances per expert. (p. 2)[^original]  
  <sub>anchor: "which includes the predictions of a team of 50 highly complex synthetic fraud analysts, generated in order to simulate a wide variety of human behaviours"</sub>
- **descriptive / data or feature**: A version of the dataset simulates realistic data availability with only one expert prediction per instance during training. (p. 2)[^original]  
  <sub>anchor: "We also create a version of our dataset simulating realistic data availability conditions (only one expert prediction per instance) during training"</sub>
- **descriptive / finding or result**: The authors develop a capacity-aware L2D algorithm and benchmark two versions of it plus a capacity-aware rejection learning method on performance and fairness across 300 testing scenarios. (p. 2)[^original]  
  <sub>anchor: "we develop a capacity aware L2D algorithm, and benchmark two versions of our method as well as a capacity aware version of _rejection learning_"</sub>

## 2 BACKGROUND AND RELATED WORK

- **mandatory / requirement**: In testing, the dataset must contain each expert's predictions for every test instance, because the assignment system may query any expert on any instance. (p. 2)[^original]  
  <sub>anchor: "in testing, we must have a set of each expert’s predictions for every instance in the test set"</sub>
- **descriptive / context**: The authors state there are only two public real-world datasets suitable for training multi-expert human-AI assignment systems. (p. 2)[^original]  
  <sub>anchor: "there are only two public real-world datasets suitable for training multi-expert human-AI assignment systems"</sub>
- **descriptive / case example**: The NIH Clinical Center X-ray dataset, used by Hemmer et al., aims at detecting airspace opacity, with predictions from an ensemble of 22 experts and a golden label from 3 radiologists; its main drawback is its size of 4,374 images. (p. 2)[^original]  
  <sub>anchor: "For each X-ray image, there are recorded predictions from an ensemble of 22 experts, and a golden label created by an independent team of 3 radiologists"</sub>
- **descriptive / limitation**: The NIH X-ray dataset contains only 4,374 X-ray images, which is its main drawback. (p. 2)[^original]  
  <sub>anchor: "it contains only 4,374 X-ray images"</sub>
- **descriptive / case example**: The Hate Speech and Offensive Language Detection dataset enriched by Keswani et al. has 1,471 tweets annotated by 170 crowd-sourcing workers, with about 10 labellers per tweet and about 87 instances per worker. (p. 2)[^original]  
  <sub>anchor: "consists of a subset of 1,471 tweets from the original dataset [10], annotated by a total of 170 crowd-sourcing workers"</sub>
- **descriptive / limitation**: The low volume of instances in the hate speech dataset hinders modelling individual expertise conditioned on the input space. (p. 2)[^original]  
  <sub>anchor: "The low volume of instances hinders the capacity to model individual expertise conditioned to the input space"</sub>

## 2.2 Simulation of Human Experts

- **descriptive / context**: Because real-world datasets are lacking, several authors synthesise expert behaviour; Madras et al. use a model-as-expert technique fitting a classifier to mimic experts on COMPAS and Heritage Health. (p. 2)[^original]  
  <sub>anchor: "Madras et al. [31] propose a _model-as-expert_ technique, fitting a ML classifier to mimic expert behavior"</sub>
- **descriptive / limitation**: In the model-as-expert approach, the expert shares the classifier's modelling bias and is trained on largely common features, which may produce artificially large agreement; the authors therefore chose not to use it. (p. 2)[^original]  
  <sub>anchor: "This may lead to artificially large agreement between the classifier and experts, which is why we choose not to use it."</sub>
- **descriptive / definition**: Instance-dependent label noise (IDN) is argued to be more realistic because human error depends on task difficulty and hence on the instance's features; the authors use this approach. (p. 2)[^original]  
  <sub>anchor: "Our approach will make use of _instance-dependent label noise_"</sub>

## 2.3 Current L2D Methods

- **descriptive / definition**: Rejection learning (ReL) defers instances from the model to humans; its simplest implementation estimates uncertainty per instance, ranks them, and rejects prediction when uncertainty exceeds a threshold. (p. 2)[^original]  
  <sub>anchor: "rejecting to predict if the uncertainty is above a given threshold"</sub>
- **descriptive / context**: Madras et al. argue ReL is sub-optimal because it ignores human performance and propose learning to defer, jointly training classifier and assignment system for a single model and single human. (p. 2)[^original]  
  <sub>anchor: "In the original L2D framework, the classifier and assignment system are jointly trained, taking into account a single model and a single human"</sub>
- **descriptive / context**: L2D was extended to the multi-expert setting by Keswani et al., followed by Hemmer et al. and Verma et al. (p. 2)[^original]  
  <sub>anchor: "expanding L2D to the multiexpert setting [25], followed by Hemmer et al. [18], Verma et al. [38]"</sub>
- **descriptive / limitation**: Most L2D approaches need predictions from every team member for every training instance, imposing significant and often unrealistic data requirements, and the limited work capacity of team members often goes unaddressed. (p. 2)[^original]  
  <sub>anchor: "Most L2D approaches require predictions from every human team member, for every training instance"</sub>
- **descriptive / finding or result**: The authors conclude that available L2D algorithms need realistic datasets, and that generating realistic synthetic expert predictions is a promising avenue since collecting real expert predictions at scale is unfeasible. (p. 2)[^original]  
  <sub>anchor: "a promising avenue is to develop methods to generate synthetic expert predictions that look realistic"</sub>

## 3 DATASET AND HAIC SCENARIO

- **descriptive / data or feature**: The FiFAR dataset has three components: a base dataset of instance features, a table of each synthetic expert's predictions per instance, and capacity constraints on instances each expert can process in a time interval. (p. 2)[^original]  
  <sub>anchor: "The FiFAR Dataset is comprised by three components"</sub>

## 2 BACKGROUND AND RELATED WORK

- **mandatory / requirement**: A dataset suitable for L2D training and evaluation must contain a sizeable amount of predictions from each member of the expert team, to enable modelling of human behaviour. (p. 2)[^original]  
  <sub>anchor: "Firstly, the dataset must contain a sizeable amount of predictions from each member of the expert team"</sub>
- **mandatory / requirement**: The human who made each prediction must be identifiable, allowing individual modelling of each expert's behaviour. (p. 2)[^original]  
  <sub>anchor: "The human which made each prediction must be identifiable, allowing for individual modelling of each expert’s behavior."</sub>
- **mandatory / requirement**: In testing, a set of each expert's predictions must be available for every instance in the test set, because the assignment system may query any expert on a given instance. (p. 2)[^original]  
  <sub>anchor: "in testing, we must have a set of each expert’s predictions for every instance in the test set"</sub>

## 2.2 Simulation of Human Experts

- **descriptive / limitation**: The main drawback of label-noise synthetic experts is that their expertise is either feature-independent or dependent on only a single feature or concept. (p. 2)[^original]  
  <sub>anchor: "The main drawback of these synthetic experts is that their expertise is either feature-independent or only dependent on a single feature or concept"</sub>
- **descriptive / finding or result**: In the Mozannar and Sontag example on CIFAR-10, the simulated expert has perfect accuracy on a fraction of the classes and random accuracy on the others. (p. 2)[^original]  
  <sub>anchor: "they simulate an expert with perfect accuracy on a fraction of the 10 classes, but random accuracy on the others"</sub>

## 2 BACKGROUND AND RELATED WORK

- **descriptive / finding or result**: The NIH Clinical Center X-ray dataset has predictions from 22 experts and golden labels from 3 radiologists, but contains only 4,374 X-ray images, which is its main drawback. (p. 2)[^original]  
  <sub>anchor: "it contains only 4,374 X-ray images"</sub>
- **descriptive / finding or result**: The Hate Speech and Offensive Language dataset subset has 1,471 tweets labelled by 170 crowd-sourcing workers, about 10 workers per tweet and about 87 instances per worker. (p. 2)[^original]  
  <sub>anchor: "Each tweet was labelled by an average of 10 workers, meaning that each worker labelled an average of 87 instances."</sub>

## 2.3 Current L2D Methods

- **descriptive / limitation**: Most L2D approaches require predictions from every human team member for every training instance, and the limited work capacity of team members often goes unaddressed. (p. 2)[^original]  
  <sub>anchor: "Most L2D approaches require predictions from every human team member, for every training instance"</sub>

## 3 DATASET AND HAIC SCENARIO

- **descriptive / method**: The FiFAR authors instantiate a scenario simulating the development and testing of an L2D system under realistic conditions, using the dataset's base data, expert predictions and capacity constraints. (p. 2)[^original]  
  <sub>anchor: "we instantiate a scenario simulating the development and testing of a L2D system under realistic conditions"</sub>

## 3.1 Base Dataset

- **descriptive / data or feature**: The base dataset is the publicly available bank-account-fraud tabular dataset, with one million rows, generated by tabular data generation techniques on an anonymised real-world bank account opening fraud dataset. (p. 3)[^original]  
  <sub>anchor: "This dataset is sizeable (one million rows) and boasts other key properties that are relevant for our use case"</sub>
- **descriptive / definition**: Each instance is a bank account opening application with application and applicant features and a label marking the application as fraudulent (1) or legitimate (0). (p. 3)[^original]  
  <sub>anchor: "Each instance represents a bank account opening application, with features containing information about the application and the applicant"</sub>
- **descriptive / definition**: The decision maker either accepts (predicted negative) or rejects (predicted positive) an application, and a positive prediction results in a declined application. (p. 3)[^original]  
  <sub>anchor: "The task of a decision maker (automated or human) is to either accept (predicted negative) or reject (predicted positive) it"</sub>
- **descriptive / context**: False positives in account opening fraud can significantly affect a person's life, as they prevent opening a bank account or accessing credit, making this a cost-sensitive problem. (p. 3)[^original]  
  <sub>anchor: "false positives in account opening fraud can significantly affect a person’s life"</sub>
- **descriptive / requirement**: The optimisation goal is to maximise recall at a fixed false positive rate of 5%, which implicitly establishes a relationship between the costs of false positives and false negatives. (p. 3)[^original]  
  <sub>anchor: "The optimization goal is to maximize recall at a fixed FPR (we use 5%)"</sub>
- **descriptive / context**: The task raises fairness concerns because ML models trained on this dataset tend to raise more false fraud alerts for clients aged 50 years or older, reducing their access to bank accounts. (p. 3)[^original]  
  <sub>anchor: "ML models trained on this dataset tend to raise more false fraud alerts for older clients (≥ 50 years)"</sub>

## 3.2 Decision Generation Method

- **descriptive / method**: The expert generation approach uses instance-dependent noise so that each synthetic expert's probability of error varies with the properties of each instance, generating predictions by flipping labels with an instance-specific probability. (p. 3)[^original]  
  <sub>anchor: "Our expert generation approach is based on _instance-dependent noise_ , in order to obtain more realistic experts"</sub>
- **descriptive / method**: An expert's decision may also depend on the ML model score, which is shown to the expert in some HAIC systems, so the error probability is defined as a function of features and model score. (p. 3)[^original]  
  <sub>anchor: "so an expert’s decision may also be dependent on an ML model score"</sub>
- **descriptive / method**: Each expert's two error probabilities are parameterised by five variables: beta0, beta1, alpha, the feature weight vector w, and w_M; w_M controls dependence on the model score, and alpha separately controls the magnitude of feature-driven variation. (p. 3)[^original]  
  <sub>anchor: "Each expert’s probabilities of the two types of error are parameterized by five variables"</sub>
- **descriptive / method**: Beta1 and beta0 control the base probability of error, while the feature weights are normalised so alpha can control the overall variation due to features. (p. 3)[^original]  
  <sub>anchor: "The values of _𝛽_ 1 and _𝛽_ 0 control the base probability of error"</sub>

## 3.1 Base Dataset

- **descriptive / data or feature**: The base dataset is the publicly available bank-account-fraud tabular dataset, with one million rows, generated from an anonymised real-world bank account opening fraud dataset. (p. 3)[^original]  
  <sub>anchor: "This dataset is sizeable (one million rows) and boasts other key properties that are relevant for our use case."</sub>
- **descriptive / context**: The optimisation goal is to maximise recall at a fixed false positive rate of 5%, which implicitly sets a relationship between false positive and false negative costs. (p. 3)[^original]  
  <sub>anchor: "The optimization goal is to maximize recall at a fixed FPR (we use 5%)"</sub>
- **descriptive / finding or result**: ML models trained on this dataset tend to raise more false fraud alerts for older clients (50 years or older), reducing their access to a bank account. (p. 3)[^original]  
  <sub>anchor: "ML models trained on this dataset tend to raise more false fraud alerts for older clients"</sub>

## 3.2 Decision Generation Method

- **descriptive / method**: Synthetic expert predictions are generated by flipping each label with a probability that depends on the instance's features and label, so the error probability varies per instance. (p. 3)[^original]  
  <sub>anchor: "We generate synthetic predictions by flipping each label _𝑦𝑖_ with probability"</sub>
- **descriptive / method**: Each expert's error probabilities are parameterised by five variables, with feature weights normalised so the parameter alpha controls the magnitude of feature-driven variation. (p. 3)[^original]  
  <sub>anchor: "Each expert’s probabilities of the two types of error are parameterized by five variables"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "FiFAR: A Fraud Detection Dataset for Learning to Defer" (2023-12-20). https://arxiv.org/abs/2312.13218
