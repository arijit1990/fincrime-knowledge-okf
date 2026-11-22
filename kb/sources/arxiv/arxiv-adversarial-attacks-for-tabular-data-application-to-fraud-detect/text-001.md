---
type: Source Text
title: 'Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data - part 1 of 2 (pp. 1-5)'
description: 'Verbatim extracted text, pp. 1-5: Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data; Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data > Abstract; Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data > 1 Introduction; and 4 more sections'
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
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2101.08030
  title: 'Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data'
  author: org:arxiv
  last_modified: '2021-01-20T00:00:00Z'
---

# Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2021-01-20), part 1 of 2, pp. 1-5. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data


[p. 1]

Francesco Cartella1 * , Orlando Anunciac¸˜ao1 * , Yuki Funabiki1 * , Daisuke Yamaguchi1 , Toru Akishita1 , Olivier Elshocht1

> 1 Sony Corporation

> * Joint first author

Francesco.Cartella@sony.com, Orlando.Anunciacao@sony.com, Yuki.Funabiki@sony.com, Daisuke.C.Yamaguchi@sony.com, Toru.Akishita@sony.com, Olivier.Elshocht@sony.com

### Abstract


Guaranteeing the security of transactional systems is a crucial priority of all institutions that process transactions, in order to protect their businesses against cyberattacks and fraudulent attempts. Adversarial attacks are novel techniques that, other than being proven to be effective to fool image classification models, can also be applied to tabular data. Adversarial attacks aim at producing adversarial examples, in other words, slightly modified inputs that induce the Artificial Intelligence (AI) system to return incorrect outputs that are advantageous for the attacker. In this paper we illustrate a novel approach to modify and adapt state-of-the-art algorithms to imbalanced tabular data, in the context of fraud detection. Experimental results show that the proposed modifications lead to a perfect attack success rate, obtaining adversarial examples that are also less perceptible when analyzed by humans. Moreover, when applied to a real-world production system, the proposed techniques shows the possibility of posing a serious threat to the robustness of advanced AI-based fraud detection procedures.

### 1 Introduction


Fraud detection plays a crucial role in financial transactional systems such as banks, insurances or online purchases. The ability to detect early whether a transaction is fraudulent has a very high value and big investments have been made to make these systems more effective. It is however important to note that fraudsters are constantly developing new ways of fooling these systems, a phenomenon known as concept drift (Widmer and Kubat 1996). A fraud detection system therefore typically has high maintenance requirements.

Machine Learning (ML) is a classical approach for fraud detection systems (Abdallah, Maarof, and Zainal 2016; Ngai et al. 2011). The ability to retrain the models with new data helps in this need for adaptation to new fraud patterns. However, given the possibility of errors in the models decisions, which could lead to overlooking frauds or blocking licit transactions and sales opportunities, fraud detection systems often do not rely solely on the models but also contain one or more layers involving some form of human intervention (Carcillo et al. 2018; Dal Pozzolo et al. 2017).

Copyright © 2021 for this paper by its authors. Use permitted under Creative Commons License Attribution 4.0 International (CC BY 4.0).

Risky transactions can be manually inspected and a decision is made whether those transactions should go through or should be blocked.

Fraudsters may use a wide range of techniques to bypass fraud detection systems. Among these techniques, adversarial attacks are novel and innovative approaches that might be used as a next level of smart financial frauds. The goal of adversarial attacks is to generate adversarial examples, i.e., inputs that are almost indistinguishable from natural data and yet classified incorrectly by the machine learning model (Madry et al. 2018).

Algorithms to build adversarial examples have recently been shown to be very effective in fooling Machine Learning models, in particular Deep Neural Networks (DNNs) in Image Recognition (Papernot et al. 2016b). This is a cause of concern for many applications that rely on these technologies, such as self-driving cars or facial recognition. The reason adversarial examples exist is a consequence of the difference between the way humans and machines represent knowledge and relations of visual elements in object recognition tasks. This difference leads to the possibility for an attacker to perturb the pixels of an image in a way that the change is imperceptible to a human, but still induces an image classifier to produce a wrong interpretation. For instance, an attacker can induce an image classifier to recognize with very high confidence a gibbon in a picture that represents a panda, after the color of a few pixels has been slightly modified (Goodfellow, Shlens, and Szegedy 2014).

[pp. 1-2]

Recent studies (Ballet et al. 2019) have shown that adversarial algorithms can also be applied to other types of machine learning models using tabular data. The positive results obtained by these studies highlighted the need and the importance of investigating adversarial algorithms for a wider range of domains and applications, so that effective defensive strategies can be designed.

Motivated by the crucial role that security plays in the financial sector, in this paper we deal with the problem of creating adversarial examples for tabular data to effectively bypass fraud detection checks. In the particular case of this research, bypassing fraud checks means either inducing the system to classify a fraudulent transaction as non-fraud, or make the violation unnoticed by a potential human inspection. These kinds of misclassifications are particularly risky for fraud detection systems, as they would lead attackers to

succeed in their criminal intent and to obtain illegal economic advantages.

It is a well-known fact that the security of a system is related to the protection of multiple layers of an application (Zhu, Rieger, and Bas¸ar 2011). Therefore, the security of a particular part of a system should be treated independently, without relying on the integrity of other layers. In light of this concept, in this paper we assume that the training set is available to the attacker, as our main focus is the analysis of security risks affecting the Machine Learning layer of a fraud detection system. Using this data, a proper surrogate model can be created and used to evaluate the effectiveness of the obtained adversarial examples, before submitting them to the real system. Notice that we do not make any assumptions on the architecture of the real model, which can be considered as unknown by the attacker.

To build successful attacks we tackled several problems, like adapting adversarial algorithms to imbalanced fraud detection data and properly treating non-editable variables. Moreover, as fraud detection systems often involve human intervention, we also considered the problem of building imperceptible adversarial examples, that are more difficult to be detected by operators. Experimental results show that, with the modifications introduced in this paper, it is possible to build realistic and imperceptible adversarial examples for all the fraudulent transactions of the considered use case. In comparison with state-of-the-art techniques, we achieved a drop of up to 64% in the number of perturbed variables that are most commonly checked by human investigators and, for the most successful cases, adversarial examples were obtained by modifying just a minimum number of fields, reducing the probability for an attack to be discovered. Finally, by obtaining a 13.6% success rate in attacking a deployed production system, we also demonstrated that the resulting adversarial examples were transferable to a target real-world model, representing a real threat to businesses dealing with fraud detection operations.

### 2 Related Works


[p. 2]

Since the concept of adversarial examples was proposed (Szegedy et al. 2013), it has been a main topic in the field of adversarial machine learning. This topic is especially discussed in image recognition tasks using DNNs, but has recently been discussed in other tasks such as audio recognition (Carlini and Wagner 2018), text summarization (Cheng et al. 2020), neural network policy for reinforcement learning (Huang et al. 2017) and so on. Furthermore, the provision of tools to assist in the generation of adversarial examples is being promoted. This is intended to make the training of models more robust against adversarial machine learning. Adversarial examples can be easily generated using tools like Adversarial Robustness Toolbox (Nicolae et al. 2018), CleverHans (Papernot et al. 2016a), Foolbox (Rauber, Brendel, and Bethge 2017) and advertorch (Ding, Wang, and Jin 2019). However, despite such trends, there are only a few studies of adversarial examples on tabular data.

To the best of our knowledge, the paper (a) (Ballet et al. 2019) was the first systematic introduction to adversarial

examples in tabular domain using recent terminology. However, similar concepts, such as performing small changes in features to get desired outputs or executing model inversion, were studied before (Grosse et al. 2017; Papernot, McDaniel, and Goodfellow 2016; Bella et al. 2010). Although it is very difficult to discuss the imperceptibility of perturbations in the tabular domain as opposed to the image domain, the authors of (Ballet et al. 2019) proposed to use the feature importance (the contribution of each feature to the model) as an indicator and applied more perturbations on the less important features. Another recent paper (b) (Hashemi and Fathi 2020) treated the adversarial examples on tabular data as counterfactual examples to help the explainability of the model. Another paper (c) (Levy et al. 2020) proposed a method of conversion to a surrogate model that maintains the properties of the target model in order to apply existing generation methods.

The main differentiators of our research with respect to the contributions mentioned above consist of: (a) they adopted a gradient-based attack method, which is applicable to models like DNNs but not to architectures with discrete gradients (such as decision trees), while we propose a model agnostic approach applicable to any architecture; (b) they provide a counterfactual explanation for model interpretation, while we assume a more realistic scenario of attack attempts; (c) the generation method they used is a variant of the black-box attack via surrogate model, while we assume that less information about the model is available to the attacker.

### 3 Main Contributions


[pp. 2-3]

As discussed in Section 1, in this paper we present a novel approach to adapt adversarial attack algorithms, that are commonly used in the image recognition domain, to tabular data. In particular, we target fraud detection use cases. Achieving this goal requires facing and solving several challenges that arise from the different nature of data and model types used, compared to image classification applications.

One of the main differences between image and fraud detection data is the balance of samples that represent each class. While image classification is a multiclass problem where each of the classes is represented by a relatively similar amount of instances, fraud detection data sets are usually binary (i.e., they contain only two classes) and are typically characterized by a large imbalance between genuine and fraudulent transactions, the first being in big majority. Fraud detection models return a risk score that represents the estimated probability that the classified transaction is fraudulent. The large imbalance in the data leads to highly biased models that tend to attribute a risk score that takes into account the higher probability of observing instances belonging to the most numerous class. Differently from image classification, where the image is generally attributed to highest predicted probability class (with some exception, like in the case of diagnosis or fault detection applications), a decision threshold is normally tuned for fraud detection, according to some business requirements. The input transaction is deemed to be fraudulent if the predicted risk score is bigger than the threshold. In this research, we introduced

the concept of the decision threshold within the attack algorithms, as it represents essential information to verify if the perturbations correctly resulted in the creation of adversarial samples.

Moreover, ensemble models and, in particular, Extreme Gradient Boosting techniques are commonly used in applications handling imbalanced tabular data, having proven to be particularly effective for these kind of settings. Applying adversarial attack algorithms in a model agnostic fashion, rather than closely targeted to Deep Neural Networks, was also one of the main challenges of this research.

Another aspect that differentiates image and tabular data is the value range that each feature can assume. Representing pixel values, image data can normally vary within limited ranges and data types (i.e., integer numbers between 0 and 255). On the other hand, tabular data can represent disparate pieces of information, like email addresses, surnames or amounts. As such, features representing a transaction can be extremely different from each other. Even if ultimately encoded as numerical values, a proper handling and representation of data types and range was essential to enable algorithms to generate realistic adversarial transactions.

[p. 3]

Field editability also represents a crucial aspect to take into account when dealing with transactional data. Differently from the image domain, where an attacker can potentially modify any of the pixels independently, for tabular data there might be fields that are not directly controllable by the user but that are rather automatically determined by the system. Examples of these fields could be the historical amount borrowed in a loan application or the discount rate applied for an online purchase. To simulate the fact that direct changes to these values are not allowed by the system, specific constraints were added to the algorithm to prevent the modification of non-editable information.

Finally, we addressed imperceptibility as one of the main challenges of our research. Differently from image data, where imperceptibility is an intuitive concept related to human perception, for fraud detection we assume that imperceptibility is related to the number and entity of changes made to important features, such as fields that are most commonly checked by human operators within the specific application context. From a purely practical point of view, we define as imperceptible an adversarial attack that ultimately passes the fraud check, remaining unnoticed. We approached imperceptibility by introducing a custom norm as a measure of distance between the original transaction and the adversarial sample. The distance is obtained through weights assigned to each feature that are proportional to a novel definition of importance that takes into account the propensity of a feature to be inspected. We will show that the custom norm properly drives the algorithm procedures to prioritize changes made on features that are rarely checked by human operators, obtaining less perceptible attacks.

Details of the contributions described above will be given in Section 5, together with other aspects introduced in this research, including some algorithms specific solutions, like a novel loss function definition for the Zeroth Order Optimization (ZOO) algorithm (Chen et al. 2017) and an improved initialization strategy for Bound-

ary attack (Brendel, Rauber, and Bethge 2018) and HopSkipJumpAttack (Chen, Jordan, and Wainwright 2020).

### 4 Problem Statement


In this paper we address the problem of building adversarial examples for fraud detection systems on financial data.

A financial transaction is a vector of m variables, v1, ..., vm with each vi ∈ R1 .

Fraud detection systems in financial data analyze a set of n transactions t1, ..., tn in a certain period of time. A model M is used to label each transaction ti with a corresponding class ci ∈{0, 1} in which 0 corresponds to Non-Fraud and 1 corresponds to Fraud: M (ti) = ci.

The first goal of an attacker is to find a perturbation vector pi = [p1 i, ..., pm i] such that:

for values of i = 1, ..., n such that M (ti) = 1 and ti is a real fraud.

If such a perturbation vector pi can be found then t˜ i = ti + pi is a successful adversarial sample.

For the purpose of our experiments, our goal is to create an adversarial sample t˜ i such that M (t˜ i) = 0 for each fraudulent transaction ti that is correctly identified by model M (M (ti) = 1).

### 5 Algorithms modifications


In this section we describe the main problems that were faced to create successful adversarial examples. We used the Adversarial Robustness Toolbox (ART) (Nicolae et al. 2018) as the reference tool. ART is a Python library for Machine Learning Security that provides tools to enable developers and researchers to defend and evaluate Machine Learning models and applications against adversarial attacks.

Even though some ART algorithms can be applied to tabular data, the majority of the tool’s algorithms is designed to deal with image data. So it was no surprise that it was necessary to make changes in order to build successful adversarial examples for tabular data, and more specifically fraud detection.

#### 5.1 A Generic Adversarial Algorithm


[pp. 3-4]

Adversarial algorithms can be used by attackers to retrieve the optimal changes that, when applied to the fraudulent transactions they want to submit, induce the fraud check to fail, by erroneously accepting the submitted transactions as legitimate. To simulate this scenario in our experimental setup, we applied adversarial algorithms on fraudulent samples that are correctly detected as fraud by the model under attack. An adversarial algorithm is considered successful if it outputs adversarial examples that are classified as non-frauds by the same model. A generic adversarial algorithm starts with an initial sample and makes perturbations

> 1Some variables can be textual, booleans, naturals or integers, but for the sake of simplicity we assume that there is a feature processing step that transforms all values into real numbers.

to that sample until the model misclassifies it. A second goal of adversarial algorithms is to make the adversarial sample as similar as possible to the original sample. Algorithm 1 shows the pseudo-code of a simple generic algorithm that serves the purpose of illustrating the main concepts. This algorithm receives a fraudulent transaction t, a model M such that M (t) = 1 and a similarity threshold ρ. The perturbations can be selected through many different ways. Two of the most common approaches involve the use of distance metrics to get the adversarial sample t˜ closer to the original sample t (e.g.: Boundary or HopSkipJump) or calculations based on the gradient of the model (e.g.: ZOO algorithm). Algorithm 1 uses a similarity function and a similarity threshold ρ. The similarity function can be based on the distance between t and t˜ , calculated using a norm such as L2 or L∞. Threshold ρ can be provided explicitly, as is the case in our generic algorithm. However, some algorithms calculate it in an indirect way. As an example, Boundary attack algorithm converges when it is close enough to the decision boundary. Algorithms usually also have a maximum number of allowed steps in the while loop. This was not included in the pseudo-code for simplicity reasons.

##### Algorithm 1 Generic Adversarial Algorithm


[p. 4]

- 6: end function

In ART, adversarial algorithms are fed with the model that is being attacked. Adversarial examples are iteratively refined and, at every iteration, the model is used to evaluate the current samples’ success. Because fraud detection is binary, the adversarial algorithms stop as soon as the current adversarial example is deemed to be successful, i.e., when it is classified as non-fraud with a score higher than 0.5. While this may work well for an image recognition model, it is problematic for a fraud detection model.

In fraud detection use cases, a decision threshold τ ∈ [0, 1] is commonly tuned and an input transaction is classified as fraud if [M (t)]1 > τ ,where [M (t)]1 is the probability that the transaction t belongs to class 1, i.e., fraud. The threshold τ is typically very small and much lower than 0.5, to compensate for the tendency of the model to attribute very low risk scores to new transactions, given the big majority of non-fraud samples observed at training time.

#### 5.2 Using Custom Threshold


Our initial results when applying the default ART algorithms were poor because a threshold of 0.5 was used, misleading the algorithms by assuming that a successful adversarial sample had been found. To correct the problem we modified the Boundary (Brendel, Rauber, and Bethge 2018), HopSkipJumpAttack (Chen, Jordan, and Wainwright 2020) and ZOO (Chen et al. 2017) attacks. These algorithms are

now fed with a custom threshold and whenever the model is evaluated internally, the custom threshold is taken into account for the models’ decision. With this correction, the adversarial algorithms have access to true information about whether a sample is classified as fraud or not by the model.

#### 5.3 Specifying a Custom Loss Function for ZOO


To drive the creation of adversarial examples, the ZOO algorithm uses a specific loss function that, as detailed below, implicitly considers a balanced threshold of 0.5 in its standard formulation. For this reason, the introduction of a novel loss function was essential to adapt the algorithm to biased cases.

To adapt the ZOO algorithm formulation to the specific case of binary classification and fraud detection, following the notation introduced in Section 4, let us define the model under attack as a function M (t) that takes a transaction t and returns a two dimensional vector M (t) ∈ [0, 1]2 . The two dimensions of this vector represent the probability score of class 0 (not fraud) and of class 1 (fraud), respectively. As a consequence, [M (t)]0 + [M (t)]1 = 1

Given a fraudulent transaction tf correctly classified by the model, the ZOO attack finds the corresponding adversarial sample t˜ by solving the following optimization problem:

where ||v||2 = ��mi=1v i2denotes the Euclidean norm (or the L2 norm) of the vector v = [v1, ..., vm]T and r > 0 is a regularization parameter. Equation 2 is expressed as a sum of two terms to be minimized: the first term ||t˜ − tf ||22repre- sents a measure of distance between the adversarial example t˜ and the original transaction tf ; the f (˜t) of the second term represents a loss function that measures how unsuccessful an adversarial attack is. The minimization of Equation 2 is performed using stochastic coordinate descent methods (see (Chen et al. 2017) for details). The loss function proposed in the standard formulation of the ZOO algorithm is the following:

[pp. 4-5]

where ν >= 0 is a tuning parameter for attack transferability, commonly set to 0 for attacking a targeted model or to a larger value when performing a transfer attack. If, for simplicity, we consider ν = 0, the loss function above will return its minimum value of 0 for all the adversarial samples t˜ having [M (t˜ )]0 >= [M (t˜ )]1, i.e., probability of not fraud bigger or equal than fraud. As explained previously, in the context of biased models, assigning to a transaction a not fraud probability higher than the probability of fraud, does not necessarily imply that the transaction is classified as licit, but it is necessary that [M (t)]1 ≤ τ , where τ ∈ [0, 1] is the decision threshold. As a consequence, the loss function of Equation 3 is minimized also by a set of adversarial examples that, being still classified as fraud, are unsuccessful. This is the set of adversarial examples t˜ for which [M (t˜ )]0 ≥ [M (t˜ )]1 and [M (t)]1 > τ .

As Equation 3 results inadequate for imbalanced use cases, we propose to use the following loss function in the

optimization of Equation 2:

The loss function above assures that minimum values are obtained only for successful adversarial examples t˜ , for which [M (t˜ )]1 <= τ (i.e., classified as not frauds).

#### 5.4 Creating Realistic Attacks with Editability Constraints


[p. 5]

We analyzed the nature of the perturbations that were obtained by the adversarial algorithms. In particular, tabular data has features of different types: boolean, integer, hotencoded variables, integers that only take positive values, etc. Without imposing any constraint, the adversarial algorithms created perturbations that led to illegal values, with respect to the type of features that are taken into consideration (e.g.: a boolean feature having value different from 0 or 1, or a positive integer feature that becomes negative). It was then necessary to make sure that perturbations assume only what we designated by realistic values. Each variable vi can assume values from a specific domain Di (e.g.: for a real variable vi, Di = R). An adversarial sample t˜ has a realistic value x for variable vi ∈ Di if x ∈ Di. In the case that x ∈/ Di a transformation needs to be made in order to ensure that x ∈ Di.

The inspection of adversarial samples raised awareness about the presence of non-editable fields in the data (i.e., fields that cannot be directly modified by the user), but are rather calculated automatically by the system. An example of this could be the total amount of money borrowed by a customer in the past, in the context of a loan management application. This value cannot be changed when a new loan is requested. Adversarial algorithms should take this into account and only make changes to variables that the user can have access to. In order to address this we defined an editability vector that contains the variables that can be changed by adversarial algorithms.

In order to address realistic and editability problems, we modified the adversarial algorithms ZOO, Boundary and HopSkipJump. In the execution of each algorithm, whenever a potential adversarial sample is modified, editability and realistic properties are enforced by correcting the illegal values.

In order to make adversarial samples realistic we considered the data types and the corresponding corrections for a specific value x that are listed on Table 1:

In order to implement corrections listed on Table 1, adversarial algorithms now receive a data specification dictionary containing a list of features for each data type.

The editability constraints are enforced by defining a vector of editable features and passing it to the adversarial algorithms. The editability vector e for variables vi, ..., vm is defined as ei = 1 if vi is editable, 0 otherwise, for i = 1, ..., m. Algorithms will only allow perturbations on features vi, with i = 1, ..., m for which ei = 1. Features vj, with j = 1, ..., m for which ej = 0 are not perturbed and forced to maintain their original values. Which feature vi are editable is a property of the system under consideration.

|Type|Correction|
|---|---|
|Boolean|0 ifx≤0.5, 1 otherwise|
|Integer|round(x)|
|Positive Integer|round(x)ifx≥0, 0 otherwise|
|Positive Float|0 ifx 0 for other fields of same group|

Table 1: Data types and corresponding corrections for adversarial samples

After creating realistic adversarial samples and taking editability into consideration, it was important to go one step further in terms of imperceptibility of the attack. Besides editability considerations, adversarial algorithms pick up any available feature as a candidate for a perturbation. Within a specific application context, an attacker can guess that, in the case of a hypothetical manual inspection, some features may capture the attention of human operators more than others. For instance, in a loan request application, the applicant salary information is usually more informative than other fields, like the number of owned pets (Ballet et al. 2019). Nevertheless, less important features are also considered by the model to estimate the request’s risk score. As a consequence, the attacker’s goal is to minimize the perturbations made on features that have a bigger chance to be checked.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data" (2021-01-20). https://arxiv.org/abs/2101.08030
