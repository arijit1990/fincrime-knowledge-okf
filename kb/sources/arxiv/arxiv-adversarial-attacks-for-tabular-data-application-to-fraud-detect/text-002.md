---
type: Source Text
title: 'Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data - part 2 of 2 (pp. 5-9)'
description: 'Verbatim extracted text, pp. 5-9: Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data > 5 Algorithms modifications; Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data > 6 Experiments and Results; Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data > 7 Conclusions and Future Work; and 1 more sections'
resource: https://arxiv.org/abs/2101.08030
tags:
- academic_finding
- advanced_analytics
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-adversarial-attacks-for-tabular-data-application-to-fraud-detect
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-01-20'
legal_status: unknown
part: 2
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2101.08030
  title: 'Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data'
  author: org:arxiv
  last_modified: '2021-01-20T00:00:00Z'
---

# Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data

[previous part](text-001.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2021-01-20), part 2 of 2, pp. 5-9. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data


### 5 Algorithms modifications


#### 5.5 Specifying a Custom Norm


[pp. 5-6]

Adversarial algorithms such as Boundary or HopSkipJump attacks use norms as measures of distance between adversarial and original examples. These algorithms try to minimize this distance as much as possible in order to make the adversarial example imperceptible. L2 norm considers the global distance between the original and the adversarial sample, disregarding that some features may have very large perturbations. Minimizing L∞ on the other hand means that the algorithm will try to avoid having a big perturbation on a single feature, giving preference to small perturbations on many features. None of these norms completely satisfy the needs of an imperceptible attack in the context of tabular data. In order to do that more successfully it is necessary to consider features differently, depending on whether they are checked by a human operator. This motivated the introduction of a novel custom norm that is expressed in Equation 5:

where p is the perturbation vector, h is a Boolean vector indicating whether a variable is checked, v is a vector of feature importance, α, β ∈ [0, 1] are weights on the check and importance of a feature respectively, and ||.||γ is a γ-norm such as L2 norm that is being used. It is known that algorithms using gradient descent can empirically derive values of coefficients such as α and β in a binary search (Carlini and Wagner 2017), but it is future work to verify whether these techniques are applicable to our approach.

For the definition of the custom norm, two properties were considered: 1) whether a feature is checked or ignored by the operators and 2) the importance of the feature for the model. The idea behind the custom norm is that changes to features that are checked and important lead to high values of the distance, so that the optimization algorithm prefers other solutions. Moreover, we also want to penalize solutions in which the feature is not checked and not important, because it will not have a significant effect in the attack. On the other hand, we would like the algorithm to prefer solutions based on perturbing features that are not checked and have high importance for the model. For these types of perturbations the custom norm returns low values. Finally, if checked variables need to be perturbed it is preferable that they are not important for the model, so we assign low distances for these situations. In conclusion, the goal of the custom norm is to drive the optimization procedure of the attack algorithms to obtain adversarial examples that are imperceptible and unnoticed by human operators.

### 6 Experiments and Results


[p. 6]

In this section we describe the experiments that were performed and the obtained results. After having modified the ART algorithms as discussed in Section 5, we applied them to the German Credit Dataset (Dua and Graff 2017) use case. The strategy described in the following sections was also applied to 2 additional datasets with similar results. The results obtained using the first dataset (the IEEE-CIS Fraud Detection dataset) are not detailed due to space limitations. The second dataset is an internal dataset that cannot be disclosed for confidentiality reasons.

German Credit Dataset (Dua and Graff 2017) is a publicly available dataset used for building models that evaluate the risk of a loan application, given account and customer information. Out of 1000 applications in total, 700 were accepted while 300 were rejected and deemed to be risky in terms of low propensity of the applicant of being able to pay back the loan. In the context of adversarial attacks, we considered the rejected applications as fraudulent, as the goal of a potential attacker would be to slightly modify their loan request such that it eventually gets accepted. The data contains 20 features with 7 integer and 13 categorical ones, such as age, sex, purpose of the loan or if the customer is a foreign worker. We applied a one-hot encoding to categorical features, obtaining a total of 61 numerical features for modeling.

#### 6.1 Use Case and Data Preparation


Capabilities of Attackers As discussed, the goal of attackers is to modify true-positive requests (i.e., applications that are deemed risky and should not be accepted) so that they can be accepted. Our assumption is that the attacker can make reasonable judgments about the importance of the features and estimate what are the fields that a human investigator most probably checks to measure the applicant’s ability to pay back the loan. In this experiment, we assumed that human investigators would mainly check 10 of the total 20 features such as the “Purpose (of the loan)”

and “Credit amount”. Moreover, we assumed that the features “Credit history”, “Personal status and sex”, “Other debtors/guarantors” and “Age in years” are not directly modifiable by the attacker and set them as non-editable. Although we conducted experiments under these hypothesis, different settings can be considered as well, depending on different assumptions on the system and the application context.

Model Construction We used XGBoost (Chen and Guestrin 2016) as a learning algorithm. At first, the dataset was split into train and test sets consisting of 70% and 30% of the data, respectively. Furthermore, train set was split into training and validation sets consisting 80% and 20% of the data, respectively. The training data was used to generate a binary classification model and the validation data was used to adjust the threshold. Before the threshold adjustment, the accuracy on validation set was 75.7%, the recall was 38.1% and the precision was 66.6%. An optimal threshold of 0.192 was obtained using the F2 score maximization as a target metric. With this threshold we obtained an accuracy of 60.0%, a recall of 95.2% and a precision of 42.6%. Using the resulting model on the test set, we were able to discriminate 82 true-positive data, representing a recall of 91% and a precision of 42.5%. These results show that, even without performing particularly sophisticated feature engineering, we obtained a fair model with satisfactory performance that can be effectively used to evaluate our study.

#### 6.2 Results


[pp. 6-7]

In this subsection we summarize the results obtained. Our goal is to show that the approaches we followed to build adversarial samples were successful.

We considered 4 parameters that can be switched on and off in our experiment designs: threshold (Section 5.2), realistic (Section 5.4), editability (Section 5.4) and custom norm (Section 5.5). As shown in Table 2, we obtained 5 different configurations.

|ID|Threshold|Realistic|CustomNorm|Editability|
|---|---|---|---|---|
|1|OFF|OFF|OFF|OFF|
|2|ON|OFF|OFF|OFF|
|3|ON|ON|OFF|OFF|
|4|ON|ON|ON|OFF|
|5|ON|ON|ON|ON|

Table 2: Configurations of the performed experiments

Experiment 1 is performed with ART as it is, without any changes or adaptations. In Experiment 2 we use custom thresholds as described in Section 5.2 and in Experiment 3 we make the attacks realistic (Section 5.4). In Experiment 4 we use the custom norm as described in Section 5.5 and in Experiment 5 we add editability constraints (Section 5.4). The results obtained are shown in Tables 3, 4 and 5.

|Boundary|1|2|3|4|5|
|---|---|---|---|---|---|
|Success Rate (%)|0|100|100|100|100|
|% of Unrealistic Values|-|47.6|0|0|0|
|# Checked Fields|-|-|592|214|228|
|# Non-Editable Fields|-|-|-|63|0|

Table 3: Results obtained with each experiment configuration for Boundary attack

|HopSkipJump|1|2|3|4|5|
|---|---|---|---|---|---|
|Success Rate (%)|0|100|100|100|100|
|% of Unrealistic Values|-|87.0|0|0|0|
|# Checked Fields|-|-|554|465|418|
|# Non-Editable Fields|-|-|-|159|0|

the pressure to change checked fields is higher.

Finally, it is important to mention that some successful adversarial examples were obtained by changing just a few fields. Table 6 shows an example where changing only the value of one attribute (Status checking account) caused the model to return a lower risk score and flip its decision from rejection to the acceptance of the loan application. It is evident that these types of adversarial examples are highly imperceptible and that it is very probable that they might remain unnoticed.

[p. 7]

|ZOO algorithm|Original|Adversarial|
|---|---|---|
|Status checking account|A12|A14|
|Model’s Risk Score|0.275|0.127|

Table 6: One adversarial example obtained with ZOO algorithm.

Table 4: Results obtained with each experiment configuration for HopSkipJump attack

|ZOO|1|2|3|4|5|
|---|---|---|---|---|---|
|Success Rate (%)|0|100|100|100|100|
|% of Unrealistic Values|-|1.6|0|0|0|
|# Checked Fields|-|-|159|133|153|
|# Non-Editable Fields|-|-|-|37|0|

### 7 Conclusions and Future Work


Table 5: Results obtained with each experiment configuration for ZOO attack

Experiment 1 was very unsuccessful, with no adversarial samples found. This means that the original algorithms cannot be applied directly to an unbalanced problem. When changes are made to the algorithm to use a proper threshold in Experiment 2, the success rate increases to 100% for the three algorithms. This experiment however still generates unrealistic values for some features. As an example, Table 4 shows that 87% of the values generated by HopSkipJump are unrealistic. This makes it easy for a human operator to detect the attack. In Experiment 3 this problem is solved and only realistic values are generated. Experiment 3 does not use the custom norm, which is done in Experiment 4. By observing the results we can check that, by using the custom norm, the number of perturbed checked fields decreased in the application of each of the 3 adversarial algorithms, thus increasing imperceptibility. For instance, Table 3 shows that, in Experiment 3, a total of 592 fields that are checked by human operators were perturbed by the boundary attack. When the proposed custom norm is used in Experiment 4, only 214 of these fields are modified, representing a drop of 64%, with respect to the state-of-the-art norm. Experiment 5 considers editability constraints and we observe that the number of non-editable fields that are changed is reduced to 0 in each algorithm. For Boundary and ZOO attacks on Experiment 5 there is a slight increase on the number of checked fields that are changed. This can be explained by the fact that the algorithms are not allowed to change non-editable fields and

In this paper we illustrated the process we followed to adapt state-of-the-art adversarial algorithms, that are commonly used in the image classification domain, to imbalanced tabular data. In particular we targeted fraud detection use cases.

After verifying the inadequacy of existing techniques to handle tabular data, we introduced modifications to address the shortcomings. In particular (i) we allowed adversarial algorithms to deal with biased model scores through the usage of a custom threshold within the algorithms and the introduction of a novel loss function for ZOO algorithm; (ii) we introduced constraints in the allowed perturbation to obtain realistic adversarial examples and avoid out-of-bound values; (iii) we improved imperceptibility through a proper management of not editable fields and through the introduction of a custom norm that drives the creation of adversarial examples that have a higher chance to be unnoticed by human investigators.

In terms of results, the changes we made contributed to increase the attack success rate from 0% to 100%. Moreover we showed examples of successful imperceptible attacks that were obtained by changing the value of just a few features.

[pp. 7-8]

Ultimately, we conducted a final experiment on the transferability of the adversarial examples to a real-world production system. To this extent, we could not perform attack transferability for the use case we considered in this paper, given the lack of a real deployed AI system. For this reason, we executed the full adversarial attack process on a real-world use case that is currently in production. For confidentiality reasons and due to the substantial economical dangers that sharing information on internal system vulnerabilities might cause, only final results can be reported, without disclosing any detail about the analyzed use case. We submitted 44 modified fraudulent transactions, created using a surrogate side model, to the real production system. For 35 transactions, representing 80% of the submitted adversarial examples, the production model returned a lower risk score than for the original transaction. More importantly,

6 cases, representing 13.6% of the submitted transactions, were flagged as safe by the system and automatically accepted, bypassing the human check. These results demonstrate that the techniques introduced in this paper represent a real threat for many AI-based fraud detection models, used in day-to-day business.

Future work will be conducted in the direction of performing more extensive experiments on attack transferability, by setting a lower target threshold for the adversarial algorithms, in order to increase the success probability of attacks for the considered real-world use case.

On the other hand, these preliminary results highlighted the need of assuring a better robustness of production fraud detection models. To this extent, we started exploring the topic of defense techniques, with the goal of improving their ability to detect and block also the most sophisticated adversarial attacks. After conducting a survey of existing defensive methodologies, our plan is to identify their shortcomings and, eventually, come up with new approaches, following a similar process we used for the attack techniques.

### References


[p. 8]

Abdallah, A.; Maarof, M. A.; and Zainal, A. 2016. Fraud detection system: A survey. Journal of Network and Computer Applications 68: 90–113.

Ballet, V.; Renard, X.; Aigrain, J.; Laugel, T.; Frossard, P.; and Detyniecki, M. 2019. Imperceptible Adversarial Attacks on Tabular Data. arXiv preprint arXiv:1911.03274 .

Bella, A.; Ferri, C.; Hern´andez-Orallo, J.; and Ram´ırez-Quintana, M. J. 2010. Data mining strategies for CRM negotiation prescription problems. In International Conference on Industrial, Engineering and Other Applications of Applied Intelligent Systems, 520–530. Springer.

Brendel, W.; Rauber, J.; and Bethge, M. 2018. Decision-Based Adversarial Attacks: Reliable Attacks Against Black-Box Machine Learning Models. In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. OpenReview.net. Carcillo, F.; Dal Pozzolo, A.; Le Borgne, Y.-A.; Caelen, O.; Mazzer, Y.; and Bontempi, G. 2018. Scarff: a scalable framework for streaming credit card fraud detection with spark. Information fusion 41: 182–194.

Carlini, N.; and Wagner, D. A. 2017. Towards Evaluating the Robustness of Neural Networks. In 2017 IEEE Symposium on Security and Privacy, SP 2017, San Jose, CA, USA, May 22-26, 2017, 39–57. IEEE Computer Society. URL https://doi.org/10.1109/SP.2017.49.

Carlini, N.; and Wagner, D. A. 2018. Audio Adversarial Examples: Targeted Attacks on Speech-to-Text. In 2018 IEEE Security and Privacy Workshops, SP Workshops 2018, San Francisco, CA, USA, May 24, 2018, 1–7. IEEE.

Chen, J.; Jordan, M. I.; and Wainwright, M. J. 2020. HopSkipJumpAttack: A Query-Efficient Decision-Based Attack. In 2020 IEEE Symposium on Security and Privacy, SP 2020, San Francisco, CA, USA, May 18-21, 2020, 1277–1294. IEEE.

Chen, P.; Zhang, H.; Sharma, Y.; Yi, J.; and Hsieh, C. 2017. ZOO: Zeroth Order Optimization Based Black-box Attacks to Deep Neural Networks without Training Substitute Models. In Thuraisingham, B. M.; Biggio, B.; Freeman, D. M.; Miller, B.; and Sinha, A.,

eds., Proceedings of the 10th ACM Workshop on Artificial Intelligence and Security, AISec@CCS 2017, Dallas, TX, USA, November 3, 2017, 15–26. ACM.

Chen, T.; and Guestrin, C. 2016. XGBoost: A Scalable Tree Boosting System. In Krishnapuram, B.; Shah, M.; Smola, A. J.; Aggarwal, C. C.; Shen, D.; and Rastogi, R., eds., Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, August 13-17, 2016, 785–794. ACM.

Cheng, M.; Yi, J.; Chen, P.; Zhang, H.; and Hsieh, C. 2020. Seq2Sick: Evaluating the Robustness of Sequence-to-Sequence Models with Adversarial Examples. In The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, New York, NY, USA, February 7-12, 2020, 3601–3608. AAAI Press.

Dal Pozzolo, A.; Boracchi, G.; Caelen, O.; Alippi, C.; and Bontempi, G. 2017. Credit card fraud detection: a realistic modeling and a novel learning strategy. IEEE transactions on neural networks and learning systems 29(8): 3784–3797.

Ding, G. W.; Wang, L.; and Jin, X. 2019. AdverTorch v0. 1: An adversarial robustness toolbox based on pytorch. arXiv preprint arXiv:1902.07623 .

Dua, D.; and Graff, C. 2017. UCI Machine Learning Repository. URL http://archive.ics.uci.edu/ml.

Goodfellow, I. J.; Shlens, J.; and Szegedy, C. 2014. Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572 .

Grosse, K.; Manoharan, P.; Papernot, N.; Backes, M.; and McDaniel, P. 2017. On the (statistical) detection of adversarial examples. arXiv preprint arXiv:1702.06280 .

Hashemi, M.; and Fathi, A. 2020. PermuteAttack: Counterfactual Explanation of Machine Learning Credit Scorecards. arXiv preprint arXiv:2008.10138 .

Huang, S. H.; Papernot, N.; Goodfellow, I. J.; Duan, Y.; and Abbeel, P. 2017. Adversarial Attacks on Neural Network Policies. In 5th International Conference on Learning Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Workshop Track Proceedings. OpenReview.net.

Levy, E.; Mathov, Y.; Katzir, Z.; Shabtai, A.; and Elovici, Y. 2020. Not All Datasets Are Born Equal: On Heterogeneous Data and Adversarial Examples. arXiv preprint arXiv:2010.03180 .

Madry, A.; Makelov, A.; Schmidt, L.; Tsipras, D.; and Vladu, A. 2018. Towards Deep Learning Models Resistant to Adversarial Attacks. In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. OpenReview.net.

Ngai, E. W.; Hu, Y.; Wong, Y. H.; Chen, Y.; and Sun, X. 2011. The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature. Decision support systems 50(3): 559–569.

Nicolae, M.-I.; Sinn, M.; Tran, M. N.; Buesser, B.; Rawat, A.; Wistuba, M.; Zantedeschi, V.; Baracaldo, N.; Chen, B.; Ludwig, H.; et al. 2018. Adversarial Robustness Toolbox v1. 0.0. arXiv preprint arXiv:1807.01069 .

Papernot, N.; Faghri, F.; Carlini, N.; Goodfellow, I.; Feinman, R.; Kurakin, A.; Xie, C.; Sharma, Y.; Brown, T.; Roy, A.; et al. 2016a. Technical report on the cleverhans v2. 1.0 adversarial examples library. arXiv preprint arXiv:1610.00768 .

Papernot, N.; McDaniel, P.; and Goodfellow, I. 2016. Transferability in machine learning: from phenomena to black-box attacks using adversarial samples. arXiv preprint arXiv:1605.07277 .

[p. 9]

Papernot, N.; McDaniel, P. D.; Jha, S.; Fredrikson, M.; Celik, Z. B.; and Swami, A. 2016b. The Limitations of Deep Learning in Adversarial Settings. In IEEE European Symposium on Security and Privacy, EuroS&P 2016, Saarbr¨ucken, Germany, March 21-24, 2016, 372–387. IEEE.

Rauber, J.; Brendel, W.; and Bethge, M. 2017. Foolbox: A python toolbox to benchmark the robustness of machine learning models. arXiv preprint arXiv:1707.04131 .

Szegedy, C.; Zaremba, W.; Sutskever, I.; Bruna, J.; Erhan, D.; Goodfellow, I.; and Fergus, R. 2013. Intriguing properties of neural networks. arXiv preprint arXiv:1312.6199 .

Widmer, G.; and Kubat, M. 1996. Learning in the presence of concept drift and hidden contexts. Machine learning 23(1): 69–101. Zhu, Q.; Rieger, C.; and Bas¸ar, T. 2011. A hierarchical security architecture for cyber-physical systems. 2011 4th international symposium on resilient control systems 15–20.


---

[previous part](text-001.md) | [source overview](overview.md)

[^original]: arXiv, "Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data" (2021-01-20). https://arxiv.org/abs/2101.08030
