---
type: Source Digest
title: 'FiFAR: A Fraud Detection Dataset for Learning to Defer - part 2 of 3 (pp. 3-5)'
description: 'Verified paraphrased digest, pp. 3-5: 3.3 Human Decision-Making Properties; 3.4 Definition of Capacity Constraints; 3.5 HAIC Setup; and 1 more sections'
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
part: 2
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
digest_points: 55
---

# FiFAR: A Fraud Detection Dataset for Learning to Defer (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 3-5) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.3 Human Decision-Making Properties

- **expected / expectation**: The authors expect human experts to be dependent on the features of the instance being decided, since experts base decisions on information related to that instance. (p. 3)[^original]  
  <sub>anchor: "we expect experts to be dependent on the instance’s features"</sub>
- **descriptive / context**: In some real-world deferral systems, instance features are accompanied by an AI model score estimating the probability that the instance belongs to the positive class; the score is meant to give extra information and possibly speed up decisions. (p. 3)[^original]  
  <sub>anchor: "the instance’s features are accompanied by an AI model’s score"</sub>
- **descriptive / finding or result**: Prior work has shown that presenting the model score when deferring a case to an expert can impact the expert's performance, so the simulated experts are considered to be impacted by the ML classifier. (p. 3)[^original]  
  <sub>anchor: "It has been shown that, in this scenario, expert’s performance can be impacted by presenting the model’s score"</sub>
- **expected / expectation**: If the generated experts use an AI assistant, the authors expect them not to fully agree with the model, based on the assumption that humans and models have complementary strengths and weaknesses. (p. 3)[^original]  
  <sub>anchor: "we expect experts not to be in perfect agreement with the model"</sub>
- **descriptive / context**: Humans and AI are assumed to perform better than one another in separate regions of the feature space. (p. 3)[^original]  
  <sub>anchor: "we would assume humans and AI perform better than one another in separate regions of the feature space"</sub>
- **descriptive / context**: The degree of algorithmic bias varies between humans and is measured as the model's impact on a human's performance; synthetic experts therefore also show varying levels of model dependence. (p. 3)[^original]  
  <sub>anchor: "The degree of "algorithmic bias" [1] varies between humans"</sub>
- **expected / expectation**: Human decision processes are expected to vary even among a team of experts. (p. 3)[^original]  
  <sub>anchor: "human decision processes can be expected to be varied even amongst a team of experts"</sub>
- **descriptive / finding or result**: Experts may make drastically different decisions on similar cases at different times, reflecting inconsistency; a human decision process is therefore not expected to be entirely deterministic. (p. 3)[^original]  
  <sub>anchor: "experts may perform drastically different decisions [9, 15]"</sub>
- **descriptive / context**: The assignment system can mitigate unfairness by learning not to defer certain cases to an expert determined to be unfair with respect to a protected attribute. (p. 3)[^original]  
  <sub>anchor: "the assignment system can learn not to defer certain cases to that expert"</sub>
- **descriptive / method**: To test the fairness of the whole system, the authors create a team of individuals with varying propensity for unfair decisions. (p. 3)[^original]  
  <sub>anchor: "it is useful to create a team of individuals with varying propensity for unfair decisions"</sub>
- **descriptive / context**: For the team of experts to be realistic, the authors state it is important that the experts exhibit varying levels of overall performance, since experts in a field differ in expertise and some are outperformed by ML models. (p. 3)[^original]  
  <sub>anchor: "it is important that these exhibit varying levels of overall performance"</sub>
- **descriptive / data or feature**: The Standard expert group is on average as unfair as the model, depends on the model score, and on average uses twelve different features. (p. 4)[^original]  
  <sub>anchor: "on average as unfair as the model, dependent on model score and, on average, twelve different features"</sub>
- **descriptive / method**: The Unfair expert group consists of experts more likely to incorrectly reject an older customer's application. (p. 4)[^original]  
  <sub>anchor: "Unfair: experts which are more likely to incorrectly reject an older customer’s application"</sub>
- **descriptive / method**: The Model agreeing expert group consists of experts heavily swayed by the model score. (p. 4)[^original]  
  <sub>anchor: "Model agreeing : experts which are heavily swayed by the model score"</sub>
- **descriptive / method**: The Sparse expert group consists of experts who depend on fewer features. (p. 4)[^original]  
  <sub>anchor: "Sparse : experts which are dependent on fewer features"</sub>

## 3.4 Definition of Capacity Constraints

- **descriptive / method**: The dataset is divided into batches and, for each batch, a maximum number of instances each expert can process is defined. (p. 4)[^original]  
  <sub>anchor: "for each batch, define the maximum number of instances that can be processed by each expert"</sub>
- **descriptive / data or feature**: Capacity constraints are represented by a batch vector b, whose component gives the batch each instance belongs to, and a human capacity matrix H, whose non-negative integer entries give how many instances each expert can process in each batch. (p. 4)[^original]  
  <sub>anchor: "as well as a human capacity matrix _𝐻_ , where element _𝐻𝑏,𝑗_ is a non-negative integer"</sub>
- **descriptive / method**: Capacity matrices are generated from four parameters: deferral rate, distribution (homogeneous or variable), absence rate, and expert pool. (p. 4)[^original]  
  <sub>anchor: "To define the capacity matrix, we consider 4 separate parameters"</sub>
- **descriptive / data or feature**: Deferral rate is the maximum fraction of each batch that can be deferred to the human team. (p. 4)[^original]  
  <sub>anchor: "Deferral_rate: maximum fraction of each batch that can be deferred to the human team"</sub>
- **descriptive / method**: Under a homogeneous distribution every expert has the same capacity; under a variable distribution each expert's capacity is sampled from a normal distribution with mean equal to deferral rate times batch size divided by number of experts and standard deviation 0.2 times that mean. (p. 4)[^original]  
  <sub>anchor: "chosen so that each expert’s capacity fluctuates around the value corresponding to an homogeneous distribution"</sub>
- **descriptive / data or feature**: Absence rate is the fraction of experts absent in each batch, allowing different team configurations without generating new experts. (p. 4)[^original]  
  <sub>anchor: "Absence rate, defined as the fraction of experts that are absent in each batch"</sub>
- **descriptive / data or feature**: Expert pool defines which expert types (standard, unfair, sparse or model agreeing) can be part of the team. (p. 4)[^original]  
  <sub>anchor: "Expert Pool, defined as which types of experts (standard, unfair, sparse or model agreeing) can be part of the team"</sub>
- **descriptive / method**: A large set of capacity constraint combinations was created for testing, with several seeds set for batch, expert absence and capacity sampling. (p. 4)[^original]  
  <sub>anchor: "several seeds were set for the batch, expert absence, and capacity sampling"</sub>

## 3.5 HAIC Setup

- **descriptive / method**: Temporal splits are used: the fraud detection classifier is trained on the first three months and validated on the fourth month. (p. 4)[^original]  
  <sub>anchor: "This model is trained on the first three months of the dataset and validated on the fourth month"</sub>
- **descriptive / method**: The classifier used is LightGBM, chosen for its proven high performance on tabular data. (p. 4)[^original]  
  <sub>anchor: "We utilize the LightGBM [24] algorithm, due to its proven high performance on tabular data"</sub>
- **descriptive / finding or result**: The ML model achieves a recall of 57.9% in validation at threshold t = 0.051, chosen to obtain a 5% FPR. (p. 4)[^original]  
  <sub>anchor: "The ML model yields a recall of 57.9% in validation, for a threshold of"</sub>
- **descriptive / context**: Simulated experts act alongside the ML model over months four to eight. (p. 4)[^original]  
  <sub>anchor: "Our simulated experts are assumed to act alongside the ML model on the period ranging from the fourth to the eighth month"</sub>
- **descriptive / context**: In L2D testing any instance can be deferred to either the model or the expert team, whereas in real settings an ML model commonly raises alerts that human experts then review. (p. 4)[^original]  
  <sub>anchor: "in a real world setting, it is common to use an ML model to raise alerts that are then reviewed by human experts"</sub>
- **descriptive / method**: Without an assignment method, the highest-scoring fraction of instances is flagged by the model for review and randomly assigned to experts for final decision; the rest are automatically accepted. (p. 4)[^original]  
  <sub>anchor: "a fraction of the highest scoring instances are flagged for human review, and, finally, these instances are randomly assigned to experts"</sub>
- **descriptive / method**: The alert review system is assumed to run from months four to seven, producing human-prediction data used to train assignment algorithms on months four to six and validate on month seven. (p. 4)[^original]  
  <sub>anchor: "we train our assignment algorithms with the data of months four to six, validating them on the seventh month"</sub>
- **descriptive / method**: At testing, flagged cases are distributed to humans by an assignment algorithm trained on the gathered data. (p. 4)[^original]  
  <sub>anchor: "the cases flagged by the ML classifier for review are distributed to the humans according to an assignment algorithm trained on the gathered data"</sub>

## 4.1 Evaluating Assignments

- **descriptive / definition**: The optimisation goal is to maximise recall at a 5% FPR, known as the Neyman-Pearson criterion. (p. 4)[^original]  
  <sub>anchor: "the optimization goal is to maximize the recall at a 5% FPR (Neyman-Pearson Criterion)"</sub>
- **descriptive / context**: The optimisation goal expresses a trade-off between misclassification costs of false positives and false negatives, making it a cost-sensitive problem. (p. 4)[^original]  
  <sub>anchor: "Implicitly, this optimization goal expresses a tradeoff between the misclassification costs of FP and FN mistakes"</sub>
- **descriptive / method**: Performance is evaluated with a cost-sensitive loss in which a parameter lambda sets the relative cost of a false positive versus a false negative; lambda is set from the model's threshold, using the relationship from Elkan. (p. 4)[^original]  
  <sub>anchor: "The parameter _𝜆_ enforces a relationship between the cost of a FP and the cost of a FN"</sub>

## 3.3 Human Decision-Making Properties

- **descriptive / method**: Four distinct synthetic expert groups were created to simulate varied human behaviour; all have similar TPR and FPR performance, and a fraction of the team performs worse than the ML model. (p. 4)[^original]  
  <sub>anchor: "All groups have similar performance as measured by their TPR and FPR"</sub>
- **descriptive / data or feature**: The Unfair expert type is more likely to incorrectly reject an older customer's application. (p. 4)[^original]  
  <sub>anchor: "Unfair: experts which are more likely to incorrectly reject an older customer’s application"</sub>
- **descriptive / data or feature**: The Sparse expert type depends on fewer features than the Standard group. (p. 4)[^original]  
  <sub>anchor: "experts which are dependent on fewer features"</sub>

## 3.4 Definition of Capacity Constraints

- **descriptive / context**: Human capacity is limited in the number of instances that can be processed in a time period such as a work day, and in real-world systems it must be applied over batches of instances rather than the whole dataset at once. (p. 4)[^original]  
  <sub>anchor: "human capacity must be applied over batches of instances, not over the whole dataset at once"</sub>

## 4.1 Evaluating Assignments

- **descriptive / limitation**: Because FPR values may differ across experiments, this hinders a direct comparison of the recall of different algorithms. (p. 4)[^original]  
  <sub>anchor: "This hinders our ability to directly compare the recall of different algorithms"</sub>
- **descriptive / finding or result**: Table 2 (varying expert pool, agreeing pool, batch size 250 and deferral 0.2, no absence): ReL loss 813 with PE 0.37, ReLgreedy loss 873 with PE 0.37, and ReLlinear loss 810 with PE 0.34. (p. 5)[^original]  
  <sub>anchor: "agreeing|250|0.2|0.0|0.0|813±8|0_._37|873±7|0_._37|810±3|0_._34|"</sub>
- **descriptive / finding or result**: Table 2 for the agreeing pool with batch size 250 and deferral 0.5 reports ReL loss 815 with PE 0.39, ReLgreedy loss 900 with PE 0.40, and ReLlinear loss 783 with PE 0.36. (p. 5)[^original]  
  <sub>anchor: "agreeing|250|0.5|0.0|0.0|815±11|0_._39|900±4|0_._40|783±5|0_._36|"</sub>
- **descriptive / finding or result**: Table 2 for the agreeing pool with batch size 5000 and deferral 0.2 reports ReL loss 816 with PE 0.37, ReLgreedy loss 875 with PE 0.37, and ReLlinear loss 808 with PE 0.34; with deferral 0.5 it reports ReL loss 814 with PE 0.39, ReLgreedy loss 905 with PE 0.40, and ReLlinear loss 784 with PE 0.36. (p. 5)[^original]  
  <sub>anchor: "agreeing|5000|0.5|0.0|0.0|814±12|0_._39|905±3|0_._40|784±3|0_._36|"</sub>
- **descriptive / finding or result**: Table 2 for the sparse pool with batch size 250 reports ReL losses 766 (deferral 0.2) and 752 (deferral 0.5), ReLgreedy 770 and 738, and ReLlinear 755 and 737, with PE values of about 0.28 to 0.34. (p. 5)[^original]  
  <sub>anchor: "sparse|250|0.2|0.0|0.0|766±9|0_._29|770±6|0_._31|755±6|0_._31|"</sub>
- **descriptive / finding or result**: Table 2 for the sparse pool with batch size 5000 reports ReL losses 752 (deferral 0.2) and 764 (deferral 0.5), ReLgreedy 767 and 758, and ReLlinear 738 and 737, with PE values of about 0.29 to 0.34. (p. 5)[^original]  
  <sub>anchor: "sparse|5000|0.2|0.0|0.0|752±4|0_._29|767±5|0_._31|738±3|0_._32|"</sub>
- **descriptive / finding or result**: Table 2 for the standard pool with batch size 250 reports ReL losses 742 (deferral 0.2) and 739 (deferral 0.5), ReLgreedy 782 and 773, and ReLlinear 788 and 782, with PE values of about 0.30 to 0.34. (p. 5)[^original]  
  <sub>anchor: "standard|250|0.2|0.0|0.0|742±13|0_._30|782±12|0_._32|788±7|0_._33|"</sub>
- **descriptive / finding or result**: Table 2 for the standard pool with batch size 5000 reports ReL losses 739 (deferral 0.2) and 731 (deferral 0.5), ReLgreedy 773 and 757, and ReLlinear 773 and 777, with PE values of about 0.31 to 0.35. (p. 5)[^original]  
  <sub>anchor: "standard|5000|0.5|0.0|0.0|731±12|0_._31|757±2|0_._33|777±4|0_._35|"</sub>
- **descriptive / finding or result**: Table 2 for the unfair pool with batch size 250 reports ReL losses 736 (deferral 0.2) and 722 (deferral 0.5), ReLgreedy 721 and 708, and ReLlinear 714 and 687, with PE values of about 0.19 to 0.25. (p. 5)[^original]  
  <sub>anchor: "unfair|250|0.2|0.0|0.0|736±8|0_._22|721±6|0_._24|714±1|0_._25|"</sub>
- **descriptive / finding or result**: Table 2 for the unfair pool with batch size 5000 reports ReL losses 724 (deferral 0.2) and 712 (deferral 0.5), ReLgreedy 726 and 712, and ReLlinear 711 and 682, with PE values of about 0.20 to 0.26. (p. 5)[^original]  
  <sub>anchor: "unfair|5000|0.2|0.0|0.0|724±11|0_._23|726±2|0_._25|711±2|0_._26|"</sub>
- **descriptive / finding or result**: Where two methods obtain the same recall, the one with the lowest FPR is preferred. (p. 5)[^original]  
  <sub>anchor: "If two methods obtain the same recall, the one with the lowest FPR is preferred"</sub>
- **descriptive / finding or result**: Table 1 for batch size 250 and deferral rate 0.2 (absence 0.0, FPR disparity 0.2) reports Model Only loss 918 with PE 0.33, ReL loss 753 with PE 0.29, ReLgreedy loss 780 with PE 0.31, and ReLlinear loss 780 with PE 0.32. (p. 5)[^original]  
  <sub>anchor: "all|250|0.2|0.0|0.2|918|0.33|753±12|0_._29|780±10|0_._31|780±9|0_._32|"</sub>
- **descriptive / finding or result**: Table 1 for batch size 5000 and deferral rate 0.2 reports ReL losses about 752 to 762 with PE 0.30, ReLgreedy losses about 776 to 780 with PE 0.31 to 0.32, and ReLlinear losses about 773 to 782 with PE 0.33. (p. 5)[^original]  
  <sub>anchor: "all|5000|0.2|0.0|0.2|918|0.33|752±8|0_._30|780±4|0_._32|779±5|0_._33|"</sub>
- **descriptive / finding or result**: Table 2, agreeing expert pool: ReL losses about 813 to 816 with PE 0.37 to 0.39, ReLgreedy losses about 873 to 905 with PE 0.37 to 0.40, and ReLlinear losses about 783 to 810 with PE 0.34 to 0.36. (p. 5)[^original]  
  <sub>anchor: "agreeing|250|0.2|0.0|0.0|813±8|0_._37|873±7|0_._37|810±3|0_._34|"</sub>
- **descriptive / finding or result**: Table 2, sparse expert pool: ReL losses about 752 to 766 with PE 0.28 to 0.29, ReLgreedy losses about 738 to 770 with PE 0.31 to 0.32, and ReLlinear losses about 737 to 755 with PE 0.31 to 0.34. (p. 5)[^original]  
  <sub>anchor: "sparse|250|0.2|0.0|0.0|766±9|0_._29|770±6|0_._31|755±6|0_._31|"</sub>
- **descriptive / finding or result**: Table 2, standard expert pool: ReL losses about 731 to 742 with PE 0.30 to 0.31, ReLgreedy losses about 757 to 782 with PE 0.32 to 0.33, and ReLlinear losses about 773 to 788 with PE 0.33 to 0.35. (p. 5)[^original]  
  <sub>anchor: "standard|250|0.2|0.0|0.0|742±13|0_._30|782±12|0_._32|788±7|0_._33|"</sub>
- **descriptive / finding or result**: Table 2, unfair expert pool: ReL losses about 712 to 736 with PE 0.19 to 0.23, ReLgreedy losses about 708 to 726 with PE 0.21 to 0.25, and ReLlinear losses about 682 to 714 with PE 0.23 to 0.26. (p. 5)[^original]  
  <sub>anchor: "unfair|250|0.2|0.0|0.0|736±8|0_._22|721±6|0_._24|714±1|0_._25|"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "FiFAR: A Fraud Detection Dataset for Learning to Defer" (2023-12-20). https://arxiv.org/abs/2312.13218
