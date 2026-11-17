---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 2 of 17 (pp. 13-24)'
description: Verbatim extracted text, pp. 13-24
resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
tags:
- industry_practice
- model_monitoring
- model_validation
- responsible_ai
- standard
- us
status: stable
source_id: nist-adversarial-machine-learning-a-taxonomy-and-terminology-of-attack
issuer: nist
issuer_name: NIST
jurisdictions:
- US
tier: 2
instrument_type: standard
normative_force: industry_practice
publication_date: '2025-03-24'
legal_status: current
part: 2
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 2 of 17, pp. 13-24. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

[pp. 13-14]

In addition to defining a taxonomy of attacks, this report provides corresponding methods for mitigating and managing the consequences of those attacks in the life cycle of AI sys­ tems, and outlines the limitations of widely used mitigation techniques to raise awareness and help organizations increase the efficacy of their AI risk-mitigation efforts. The termi­ nology used in this report is consistent with the literature on AML and is complemented by a glossary that defines key terms associated with the field of AML in order to assist non-expert readers. Taken together, the taxonomy and terminology are meant to inform other standards and future practice guides for assessing and managing the security of AI systems by establishing a common language for the rapidly developing AML landscape. Like the taxonomy, the terminology and definitions are not intended to be exhaustive but rather to serve as a starting point for understanding and aligning on key concepts that have emerged in the AML literature.

xiii

1. Introduction

Artificial intelligence (AI) systems have been on a global expansion trajectory for several years [267]. These systems are being developed by and widely deployed into the economies of numerous countries, with increasing opportunities for people to use AI systems in many spheres of their lives [92]. This report distinguishes between two broad classes of AI sys­ tems: predictive AI (PredAI) and generative AI (GenAI). Although the majority of industrial applications of AI systems are still dominated by PredAI systems, there has been a recent increase in the adoption of GenAI systems in business and consumer contexts. As these systems permeate the digital economy and become essential parts of daily life, the need for their secure, robust, and resilient operation grows. These operational attributes are critical elements of trustworthy AI in the NIST AI Risk Management Framework [274] and the NCSC Machine Learning Principles [266].

[pp. 14-15]

The field of ADVERSARIAL MACHINE LEARNING (AML) studies attacks against ML systems that exploit the statistical, data-based nature of ML systems. Despite the significant progress of AI and machine learning (ML) in different application domains, these technologies remain vulnerable to attacks that can cause spectacular failures. The chances of these kinds of failure increase as ML systems are used in contexts where they may be subject to novel or adversarial interactions, and the consequences grow more dire as these systems are used in increasingly high-stakes domains. For example, in PredAI computer vision applications for object detection and classification, well-known cases of adversarial perturbations of input images have caused autonomous vehicles to swerve into lanes going in the oppo­ site direction, stop signs to be misclassified as speed limit signs, and even people wearing glasses to be misidentified in high-security settings [121, 187, 332, 349]. Similarly, the po­ tential for adversarial input to trick ML models into revealing hidden information has be­ come more urgent as more ML models are being deployed in fields like medicine, where medical record leaks can expose sensitive personal information [25, 171].

In GenAI, large language models (LLMs) [13, 15, 49, 85, 102, 236, 247, 277, 279, 348, 365, 371, 372, 436] are increasingly becoming an integral part of software applications and internet infrastructure. LLMs are being used to create more powerful online search tools, help software developers write code, and power chatbots that are used by millions of people every day [255]. LLMs are also being augmented to create more useful AI sys­ tems, including through interactions with corporate databases and documents to enable powerful RETRIEVAL-AUGMENTED GENERATION (RAG) (RAG) [210] and through training- or inference-time techniques to enable LLMs to take real-world actions, such as browsing the web or using a bash terminal as an LLM-based AGENT [167, 261, 278, 419]. Thus, vulner­ abilities in GenAI systems may expose a broad attack surface for threats to the privacy of sensitive user data or proprietary information about models’ architecture or training data, and create risks to the integrity and availability of widely used systems.

As GenAI adoption has grown, the increasing capability of these systems has created an­ other challenge for model developers: how to manage the risks created by unwanted or

harmful uses of these systems’ capabilities.[275] As model developers have increasingly sought to apply technical interventions to reduce models’ potential for misuse, another surface for high-stakes AML attacks has emerged in attacks that attempt to circumvent or disrupt these protections.

[pp. 15-16]

Fundamentally, many AI systems are susceptible both to AML attacks and to attacks that more closely resemble traditional cybersecurity attacks, including attacks against the plat­ forms on which they are deployed. This report focuses on the former and considers the latter to be within the scope of traditional cybersecurity taxonomies.

Both PredAI and GenAI systems are vulnerable to attacks enabled by a range of attacker capabilities throughout the development and deployment life cycle. Attackers can manipu­ late training data [327], including the Internet data used in large-scale model training [57], or can modify test-time inference data and resources by adding adversarial perturbations or suffixes. Attackers can also attack the components used to make AI systems by inserting TROJAN functionality. As organizations increasingly rely on pre-trained models that could be used directly or fine-tuned with new datasets to enable different tasks, their vulnera­ bility to these attacks increases.

Modern cryptography often relies on algorithms that are secure in an information-theoretic sense, that is, those that can be formally proven to ensure security under certain condi­ tions. However, there are no information-theoretic security proofs for the widely used ML algorithms in modern AI systems. Moreover, information-theoretic impossibility results that set limits on the effectiveness of widely used mitigation techniques have begun to appear in the literature [124, 140, 432]. As a result, many of the advances in developing mitigations against different classes of AML attacks tend to be empirical and limited in na­ ture, adopted because they appear to work in practice rather than because they provide information-theoretic security guarantees. Thus, many of these mitigations may them­ selves be vulnerable to new discoveries and evolutions in attacker techniques.

This report offers guidance for the development of:

• Standardized terminology for AML terms that can be used across relevant ML and cy­ bersecurity communities. There are notable differences in terminology in different stakeholder communities and it is important to work towards bridging the differ­ ences as AI is increasingly adopted throughout enterprise and consumer contexts.

• A taxonomy of the most widely studied and currently effective attacks in AML, in­ cluding:

– Evasion, poisoning, and privacy attacks for PredAI systems

– Poisoning, direct prompting, and indirect prompt injection attacks for GenAI

systems

• A discussion of potential mitigations for these attacks and the limitations of existing mitigation techniques

NIST intends to update this report as new developments emerge in AML attacks and miti- gations.

This report provides a categorization of common classes of attacks and their mit- igations for PredAI and GenAI systems. This report is not intended to provide an exhaustive survey of all available literature on Adversarial ML, which includes more than 11,354 references on arXiv.org since 2021 as of July 2024.

This report is organized into three sections.

[pp. 16-18] [ref: 2.1]

• Section 2 considers PredAI systems. Section 2.1 introduces the taxonomy of attacks for PredAI systems, which defines the broad categories of attacker objectives and goals, and identifies the capabilities that an adversary must leverage to achieve the corresponding objectives. Specific attack classes are also introduced for each type of capability. Sections 2.2, 2.3, and 2.4 discuss the major classes of attacks: evasion, poisoning, and privacy, respectively. A corresponding set of mitigations for each class of attacks is provided in the attack class sections.

• Section 3 considers GenAI systems. Section 3.1 introduces the taxonomy of attacks for GenAI systems and defines the broad categories of attacker objectives and ad­ versary capabilities relevant to these systems. Specific attack classes are introduced for each type of capability, along with relevant mitigations.

• Section 4 discusses remaining challenges in the field, including limitations to widely used mitigation techniques. The intent is to raise awareness of open questions in the field of AML and to call attention to trends that may shape risk and risk management practices in future.

2. Predictive AI Taxonomy

2.1. Attack Classification

Figure 1 introduces a taxonomy of attacks in AML on PredAI systems, based on attacker goals and objectives, capabilities, and knowledge.

Model Poisoning

Model Control

Clean-Label

Availability Energy Latency

Poisoning

Label Limit

Query Access

Training Data

Clean-Label

Control

Poisoning

Model Poisoning Clean-Label

Data Poisoning

Backdoor

Label

Limit

Model Control

Black-Box

Evasion

Integrity

Query Access

Control

Source Code

Backdoor Poisoning

Test Data Control

Training Data Control

Backdoor Poisoning

Evasion

Model Extraction

Targeted Poisoning

Query Access

Model

Privacy

Data

Query Access

Reconstruction; Membership Inference;

Property Inference

Figure 1. Taxonomy of attacks on PredAI systems

The attacker’s objectives are shown as disjointed circles with the attacker’s goal at the center of each circle: availability breakdown, integrity violation, and privacy compromise. The capabilities that an adversary must leverage to achieve their objectives are shown in the outer layer of the objective circles. Attack classes are shown as callouts connected to the capabilities required to mount each attack. Multiple attack classes that require the same capabilities to reach the same objective are shown in a single callout.

These attacks are classified according to the following dimensions: 1) learning method and stage of the learning process when the attack is mounted, 2) attacker goals and objectives,

3) attacker capabilities, and 4) attacker knowledge of the learning process. Several adver­ sarial attack classification frameworks have been introduced in prior works [42, 358], and the goal here is to create a standard terminology for adversarial attacks on ML that unifies existing work.

2.1.1. Stages of Learning

[pp. 18-19]

Predictive machine learning involves a TRAINING STAGE in which a model is learned and a DEPLOYMENT STAGE in which the model is deployed on new, unlabeled data samples to generate predictions. In the case of SUPERVISED LEARNING, labeled training data is given as input to a training algorithm in the training stage, and the ML model is optimized to mini­ mize a specific loss function. Validation and testing of the ML model is usually performed before the model is deployed in the real world. Common supervised learning techniques include CLASSIFICATION in which the predicted labels or classes are discrete and REGRESSION in which the predicted labels or response variables are continuous.

Other learning paradigms in the ML literature include UNSUPERVISED LEARNING, which trains models using unlabeled data at training time; SEMI-SUPERVISED LEARNING in which a small set of examples have labels, while the majority of samples are unlabeled; REINFORCEMENT LEARNING in which an agent interacts with an environment and learns an optimal policy to maximize its reward; FEDERATED LEARNING in which a set of clients jointly train an ML model by communicating with a server that performs an aggregation of model updates; and ENSEMBLE LEARNING, which is an approach that seeks better predictive performance by combining the predictions from multiple models.

Most PredAI models are DISCRIMINATIVE, i.e., learn only a decision boundary, such as LOGIS­ TIC REGRESSION, SUPPORT VECTOR MACHINES, and CONVOLUTIONAL NEURAL NETWORKS. GenAI models may also be used in predictive tasks, such as sentiment analysis [125] .

AML literature predominantly considers adversarial attacks against AI systems that could occur at either the training stage or the deployment stage. During the training stage, the attacker might control part of the training data, their labels, the model parameters, or the code of ML algorithms, resulting in different types of poisoning attacks. During the deployment stage, the ML model is already trained, and the adversary could mount evasion attacks to create integrity violations and change the ML model’s predictions, as well as privacy attacks to infer sensitive information about the training data or the ML model.

Training-time attacks. POISONING ATTACKS [40] occur during the ML training stage. In a DATA POISONING attack [40, 148], an adversary controls a subset of the training data by either inserting or modifying training samples. In a MODEL POISONING attack [222], the adversary controls the model and its parameters. Data poisoning attacks are applicable to all learning paradigms, while model poisoning attacks are most prevalent in federated learning [190], where clients send local model updates to the aggregating server, and in supply-chain attacks, where malicious code may be added to the model by suppliers of

model technology.

[p. 19] [ref: 2.1.2]

Deployment-time attacks. Other types of attacks can be mounted against deployed mod­ els. Evasion attacks modify testing samples to create ADVERSARIAL EXAMPLE [38, 144, 362], which are similar to the original sample (e.g., according to certain distance metrics) but alter the model predictions to the attacker’s choices. Other attacks, such as availability attacks and privacy attacks including membership inference [342] and data reconstruc­ tion [110], can also be mounted by attackers with query access to a deployed ML model.

2.1.2. Attacker Goals and Objectives

The attacker’s objectives are classified along three dimensions according to the three main types of security violations considered when analyzing the security of a system: availability breakdown, integrity violation, and privacy compromise. Figure 1 separates attacks into three disjointed circles according to their objective, and the attacker’s objective is shown at the center of each circle.

Availability breakdown [NISTAML.01] [Back to Index]. An AVAILABILITY BREAKDOWN attack is a deliberate interference with a PredAI system to disrupt the ability of other users or processes to obtain timely and reliable access to its services. This attack type may be initi­ ated at training or deployment time, although its impacts are typically experienced at de­ ployment time. Availability attacks can be mounted via data poisoning, when the attacker controls a fraction of the training set; via model poisoning, when the attacker controls the model parameters; or as ENERGY-LATENCY ATTACK via query access. Data poisoning availabil­ ity attacks have been proposed for SUPPORT VECTOR MACHINES [40], linear regression [179], and even neural networks [228, 260], while model poisoning attacks have been designed for neural networks [222] and federated learning [22].

• Energy latency attacks [NISTAML.014] [Back to Index]. Recently, ENERGY-LATENCY ATTACK, a type of availability attacks that require only black-box access to the model, have been developed for neural networks across many different tasks in computer vision and natural language processing (NLP) [345].

[pp. 19-20]

Integrity violation [NISTAML.02] [Back to Index]. An INTEGRITY VIOLATION attack is a de­ liberate interference with a PredAI system to force it to misperform against its intended objectives and produce predictions that align with the adversary’s objective. An attacker can cause an integrity violation by mounting an evasion attack at deployment time or a poi­ soning attack at training time. Evasion attacks require the modification of testing samples to create adversarial examples that are misclassified by the model while often remaining stealthy and imperceptible to humans [38, 144, 362]. Integrity attacks via poisoning can be classified as TARGETED POISONING ATTACK [137, 330], BACKDOOR POISONING ATTACK [148], and MODEL POISONING [22, 36, 123]. Targeted poisoning tries to violate the integrity of a few targeted samples and assumes that the attacker has training data control to insert the poi­ soned samples. Backdoor poisoning attacks require the generation of a BACKDOOR PATTERN,

which is added to both the poisoned samples and the testing samples to cause misclassi­ fication. Backdoor attacks are the only attacks in the literature that require both training and testing data control. Model poisoning attacks could result in either targeted or back- door attacks, and the attacker modifies model parameters to cause an integrity violation. They have been designed for centralized learning [222] and federated learning [22, 36].

Privacy compromise [NISTAML.03] [Back to Index]. A PRIVACY COMPROMISE attack causes the unintended leakage of restricted or proprietary information from a PredAI system, in­ cluding details about a model’s training data, weights, or architecture [100, 309]. While the term “confidentiality” is more widely used in taxonomies of traditional cybersecurity attacks, the AML field has tended to use the top-level term “privacy” to encompass both attacks against the confidentiality of a model (e.g., those that extract information about a model’s weights or architecture) and those that cause violations of expected privacy prop­ erties of model outputs (e.g. by exposing model training data) [310]. DATA CONFIDENTIAL­ ITY during ML training can be achieved through secure computation methods based on cryptographic techniques [2, 253, 288, 385], which ensure that training data and model parameters remain protected during the training phase. However, even models trained using paradigms that enforce data confidentiality may be vulnerable to privacy attacks, in which adversaries interacting with a model can extract information about its training data or parameters. In this report, we focus on privacy compromises that can occur at deploy­ ment time, regardless of the training method used, or whether data confidentiality was maintained during training.

[pp. 20-21] [ref: 2.1.3]

In privacy attacks, attackers might be interested in learning information about the training data (resulting in DATA PRIVACY ATTACKS) or the ML model (resulting in MODEL PRIVACY AT­ TACKS). The attacker could have different objectives for compromising the privacy of train­ ing data, such as DATA RECONSTRUCTION [110] (inferring the content or features of train­ ing data), MEMBERSHIP-INFERENCE ATTACK [162, 343] (inferring the presence of data in the training set), TRAINING DATA EXTRACTION [59, 63] (extracting training data from generative models), ATTRIBUTE INFERENCE ATTACKS [184, 409] (inferring sensitive attributes of training records) and PROPERTY INFERENCE [134] (inferring properties about the training data dis­ tribution). MODEL EXTRACTION is a model privacy attack in which attackers aim to extract information about the model [177].

2.1.3. Attacker Capabilities

AML attacks for PredAI systems can be taxonomized with respect to the capabilities that an attacker controls. An adversary might leverage six types of capabilities to achieve their objectives, as shown in the outer layer of the objective circles in Fig. 1:

• TRAINING DATA CONTROL: The attacker might take control of a subset of the training data by inserting or modifying training samples. This capability is used in data poi­ soning attacks (e.g., availability poisoning, targeted or backdoor poisoning).

• MODEL CONTROL: The attacker might take control of the model parameters by either generating a Trojan trigger and inserting it in the model or by sending malicious local model updates in federated learning.

• TESTING DATA CONTROL: The attacker might add perturbations to testing samples at model deployment time, as performed in evasion attacks to generate adversarial examples or in backdoor poisoning attacks.

• LABEL LIMIT: This capability is relevant to restrict adversarial control over the labels of training samples in supervised learning. Clean-label poisoning attacks assume that the attacker does not control the label of the poisoned samples, while regular poisoning attacks assume label control over the poisoned samples.

• SOURCE CODE CONTROL: The attacker might modify the source code of the ML algo­ rithm, such as the random number generator or any third-party libraries, which are often open source.

• QUERY ACCESS: The attacker might submit queries to the model and receive predic­ tions (i.e., labels or model confidences), such as when interacting with an AI system hosted by a cloud provider as a machine learning as a service (MLaaS) offering. This capability is used by black-box evasion attacks, ENERGY-LATENCY ATTACK, and all pri­ vacy attacks that do not require knowledge of the model’s training data, architecture, or parameters.

[pp. 21-22] [ref: 2.1.4]

Even if an attacker does not have the ability to modify training/testing data, source code, or model parameters, access to these may still be crucial for mounting stronger white- box attacks that require knowledge of the ML system. See Sec. 2.1.4 for more details on attacker knowledge, and detailed definitions of white-box and black-box attacks.

Figure 1 connects each attack class with the capabilities required to mount the attack. For example, backdoor attacks that cause integrity violations require control of the training and testing data to insert the backdoor pattern. Backdoor attacks can also be mounted via source code control, particularly when training is outsourced to a more powerful en­ tity. Clean-label backdoor attacks do not allow label control on the poisoned samples in addition to the capabilities needed for backdoor attacks.

2.1.4. Attacker Knowledge

Another dimension of attack classification is how much knowledge the attacker has about the ML system. There are three main types of attacks:

White-box attacks. These assume that the attacker operates with full knowledge about the ML system, including the training data, model architecture, and model hyperparam­ eters. While these attacks operate under very strong assumptions, the main reason for analyzing them is to test the vulnerability of a system against worst-case adversaries and

to evaluate potential mitigations. This definition is more general and encompasses the no­ tion of adaptive attacks in which knowledge of the mitigations applied to the model or the system is explicitly tracked.

Black-box attacks. These attacks assume that the attacker operates with minimal, and sometimes no knowledge at all about the ML system. An adversary might have query access to the model, but they have no other information about how the model is trained. These attacks are the most practical since they assume that the attacker has no knowledge of the AI system and utilizes system interfaces readily available for normal use.

Gray-box attacks. There are a range of gray-box attacks that capture adversarial knowl­ edge between black-box and white-box attacks. Suciu et al. [358] introduced a framework to classify gray-box attacks. An attacker might know the model architecture but not its pa­ rameters, or the attacker might know the model and its parameters but not the training data. Other common assumptions for gray-box attacks are that the attacker has access to data distributed identically to the training data and knows the feature representation. The latter assumption is important for applications in which feature extraction is used before training an ML model, such as cybersecurity, finance, and healthcare.

2.1.5. Data Modality

Until recently, most attacks and defenses in adversarial machine learning have operated under a single modality, but a new trend in the field is to use multimodal data. The tax­ onomy of attacks defined in Fig. 1 is independent of the modality of the data in specific applications.

The most common data modalities in the AML literature include:

[pp. 22-23]

• Image: Adversarial examples of image data [144, 362] have the advantage of a con­ tinuous domain, and gradient-based methods can be applied directly for optimiza­ tion. Backdoor poisoning attacks were first invented for images [148], and many privacy attacks are run on image datasets (e.g., [342]). The image modality includes other types of imaging (e.g., LIDAR, SAR, IR, hyperspectral).

• Text: Text is a popular modality, and all classes of attacks have been proposed for text models, including evasion [150], poisoning [82, 213], and privacy [426].

• Audio: Audio systems and text generated from audio signals have also been at­ tacked [66].

• Video: Video comprehension models have shown increasing capabilities in vision and language tasks [428], but such models are also vulnerable to attacks [402].

• Cybersecurity2

: The first poisoning attacks were discovered in cybersecurity for worm

2Cybersecurity data may not include a single modality but rather multiple modalities, such as network-level, host-level, or program-level data.

signature generation (2006) [291] and spam email classification (2008) [269]. Since then, poisoning attacks have been shown for malware classification, malicious PDF detection, and Android malicious app classification [329]. Evasion attacks against similar data modalities have been proposed as well: malware classification [103, 357], PDF malware classification [352, 414], Android malicious app detection [295], and network instrusion detection [93]. Poisoning unsupervised learning models has been shown for clustering used in malware classification [41] and network traffic anomaly detection [315].

Anomaly detection based on data-centric approaches allows for automated feature learning through ML algorithms. However, the application of ML to such problems comes with specific challenges related to the need for very low false negative and low false positive rates (e.g., the ability to catch zero-day attacks). This challenge is compounded by the fact that trying to accommodate all of these together makes ML models susceptible to adversarial attacks [198, 301, 446].

• Tabular data: There have been numerous attacks against ML models working on tabular data, such as poisoning availability attacks against healthcare and business applications [179], privacy attacks against healthcare data [422], and evasion attacks against financial applications [141].

Recently, the use of ML models trained on multimodal data has gained traction, particu­ larly the combination of image and text data modalities. Several papers have shown that multimodal models may provide some resilience against attacks [417], but other papers show that multimodal models themselves could be vulnerable to attacks mounted on all modalities at the same time [77, 333, 415] (see Sec. 4.2.3).

[pp. 23-24] [ref: 2.2]

An open challenge is to test and characterize the resilience of a variety of multi- modal ML models against evasion, poisoning, and privacy attacks.

2.2. Evasion Attacks and Mitigations

[NISTAML.022] [Back to Index]

The discovery of evasion attacks against ML models has led to significant growth in AML research over the last decade. In an evasion attack, the adversary’s goal is to generate adversarial examples: samples whose classification can be changed to an arbitrary class of the attacker’s choice – often with only minimal perturbation [362]. For example, in the context of image classification, the perturbation of the original sample might be small so that a human cannot observe the transformation of the input; while the ML model can be tricked to classify the adversarial example in the target class selected by the attacker, humans still recognize it as part of the original class.

Early known instances of evasion attacks date back to 1988 with the work of Kearns and Li [192] and 2004 when Dalvi et al. [98] and Lowd and Meek [226] demonstrated the ex­ istence of adversarial examples for linear classifiers used in spam filters. Later, Szedegy et al. [362] showed that deep neural networks used for image classification could be eas­ ily manipulated through adversarial examples. In 2013, Szedegy et al. [362] and Biggio et al. [38] independently discovered an effective method for generating adversarial exam­ ples against linear models and neural networks by applying gradient optimization to an adversarial objective function. Both of these techniques require white-box access to the model and were improved by subsequent methods that generated adversarial examples with even smaller perturbations [20, 65, 232].

Adversarial examples are also applicable in more realistic black-box settings in which at­ tackers only obtain query access capabilities to the trained model. Even in the more chal­ lenging black-box setting in which attackers obtain the model’s predicted labels or confi­ dence scores, deep neural networks are still vulnerable to adversarial examples. Meth­ ods for creating adversarial examples in black-box settings include zeroth-order optimiza­ tion [80], discrete optimization [254], Bayesian optimization [344], and transferability, which involves the white-box generation of adversarial examples on a different model before transferring them to the target model [282, 283, 377]. While cybersecurity and image clas­ sifications were the first application domains to showcase evasion attacks, ML technology in many other application domains has come under scrutiny, including speech recogni­ tion [66], natural language processing [185], and video classification [215, 401].


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
