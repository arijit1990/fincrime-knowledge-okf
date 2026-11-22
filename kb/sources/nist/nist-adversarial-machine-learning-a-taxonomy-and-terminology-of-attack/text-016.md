---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 16 of 17 (pp. 120-126)'
description: 'Verbatim extracted text, pp. 120-126: B; C; D; and 12 more sections'
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
part: 16
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-015.md) | [source overview](overview.md) | [next part](text-017.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 16 of 17, pp. 120-126. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## B


[p. 120]

adversary-specified behaviour in a model that has been subject to a backdoor poi­ soning attack. For example, in computer vision, an adversary could poison a model such that the insertion of a square of white pixels induces a desired target label. 6, 22, 107 backdoor poisoning attack A poisoning attack that causes a model to perform an adversary-

selected behaviour in response to inputs that follow a particular BACKDOOR PAT­ TERN. 6, 42

classification The task of predicting which of a set of discrete categories an input belongs

to. 5 convolutional neural networks A class of feed-forward neural networks that include at

## C


[pp. 120-121]

least one convolutional layer, referred to as CNNs. In convolutional layers, feature detectors (known as kernels or filters) detect specific features across the input data. CNNs are primarily used for processing grid-like data, such as images, and are particularly effective for tasks like image classification, object detection, and image segmentation. 5, 31

data confidentiality A well-established concept in cybersecurity referring to the protection

of sensitive information from unauthorized access and disclosure. 7 data poisoning A POISONING ATTACKS in which an adversary controls part of the training

data. 5, 36, 37, 40, 111 data privacy attacks Attacks against machine learning models that extract sensitive infor­

## D


[p. 121]

mation about training data. 7 data reconstruction Privacy attacks that reconstruct sensitive data in a model’s training

data from aggregate information. 7, 28 deployment stage The stage of the machine learning pipeline in which a model is deployed

into a live or real-world environment for use, such as being integrated into an en­ terprise application or made available to end users through an API. 5, 37, 38 diffusion models A class of latent variable generative models consisting of three major

components: a forward process, a reverse process, and a sampling procedure. The goal of the diffusion model is to learn a diffusion process that generates the probability distribution of a given dataset. It is widely used in computer vision on a variety of tasks, including image denoising, inpainting, super-resolution, and image generation. 34 direct prompt injection A DIRECT PROMPTING ATTACK in which the attacker exploits PROMPT

INJECTION. 43, 110 direct prompting attack In the generative AI context, an attack conducted by the primary

user of the system through QUERY ACCESS (e.g., as opposed to through RESOURCE CONTROL). 34, 43, 108, 110 discriminative A type of machine learning method that learns to discriminate between

classes. 5

## E


energy-latency attack An attack that exploits the performance dependency on hardware

and model optimizations to negate the effects of hardware optimizations, increase computational latency, increase hardware temperature, and massively increase the amount of energy consumed. 6, 8 ensemble learning A type of a meta machine learning approach that combines the predic­

tions of several models to improve performance. 5 expectation over transformation A method for strengthening adversarial examples to re­

main adversarial under image transformations that occur in the real world, such as angle and viewpoint changes. EOT models these perturbations within the opti­ mization procedure. Rather than optimizing the log-likelihood of a single example, EOT uses a chosen distribution of transformation functions that take an input con­ trolled by the adversary to the “true” input perceived by the classifier. 16

## F


[p. 122]

federated learning A type of machine learning in which a model is trained in a decentral­

ized fashion using multiple data sources without pooling or combining the data in any centralized location. Federated learning allows entities or devices to collabo­ ratively train a global model by exchanging model updates without directly sharing the data that each entity controls. 5, 31 feedforward neural networks Artificial neural networks in which the connections between

nodes is from one layer to the next and do not form a cycle. 31 fine-tuning The process of adapting a pre-trained model to perform specific tasks or spe­

cialize in a particular domain. This phase follows the initial pre-training phase and involves further training the model on task-specific data. This is often a supervised learning task. 37 fine-tuning circumvention Fine-tuning to remove model refusal behaviour or other model-

level safety interventions. 41 formal methods A mathematically rigorous technique for the specification, development,

and verification of software systems. 18 foundation model In generative AI, models trained on broad data using SELF-SUPERVISED

LEARNING that can be adapted such as through fine-tuning for a variety of down­ stream tasks [311]. 111 functional attack An adversarial attack that is optimized for a set of data in a domain rather

than per data point. 13, 23

## G


generative adversarial networks A machine learning framework in which two neural net­

works contest with each other in the form of a zero-sum game, where one agent’s gain is another agent’s loss. A GAN learns to generate new data with the same statistics as the training set. See [143] for further details. 31, 34 generative pre-trained transformer (GPT) A family of machine learning models based on

the transformer architecture [383] that are pre-trained through SELF-SUPERVISED LEARNING on large data sets of unlabelled text. This is the current predominant architecture for large language models. 34 graph neural network A neural network designed to process graph-structured data. GNNs

perform optimizable transformations on graph attributes (e.g., nodes, edges, global context) while preserving graph symmetries such as permutation invariance. GNNs utilize a “graph-in, graph-out” architecture that takes an input graph with informa­ tion and progressively transforms it into an output graph with the same connec­ tivity as that of the input graph. 31

## H


[pp. 122-123]

hidden Markov model A Markov model in which the system being modeled is assumed

to be a Markov process with unobservable states. The model provides an observ­ able process whose outcomes are influenced by the outcomes of a Markov model in a known way. An HMM can be used to describe the evolution of observable

events that depend on internal factors that are not directly observable. In ma­ chine learning, it is assumed that the internal state of a model is hidden but not its hyperparameters. 31

indirect prompt injection A type of PROMPT INJECTION executed through RESOURCE CONTROL

rather than through user-provided input as in a DIRECT PROMPT INJECTION. 39–41, 50 integrity violation In the AML context, an AI system being forced to misperform against

## I


[p. 123]

its intended objectives, producing outputs or predictions that align with the at­ tacker’s objective. 6, 40

jailbreak A DIRECT PROMPTING ATTACK intended to circumvent restrictions placed on model

outputs, such as circumventing refusal behaviour to enable misuse. 34, 38, 42, 43, 52

label flipping A type of data poisoning attack in which an adversary is restricted to changing

the training labels. 20 label limit A capability with which an attacker does not control the labels of training sam­

ples in supervised learning. 8 logistic regression A type of linear classifier that predicts the probability of an observation

## L


being part of a class. 5

machine unlearning A technique that involves selectively removing the influences of spe­

cific training data points from a trained machine learning model, such as to remove unwanted capabilities or knowledge in a foundation model, or to enable a user to request the removal of their records from a model. Efficient approximate unlearn­ ing techniques may not require retraining the ML model from scratch. 33 membership-inference attack A data privacy attack to determine whether a data sample

was part of the training set of a machine learning model. 7, 28 misuse enablement In the AML context, a circumvention of technical restrictions imposed

## M


[pp. 123-124]

by the AI system’s owner on its use, such as restrictions designed to prevent a GenAI system from producing outputs that could cause harm to others. 40 model control A capability with which an attacker can control the machine learning model

parameters. 8, 37, 41, 111 model extraction A type of privacy attack that extracts details of the model architecture

and/or parameters. 7, 28, 31, 40, 41, 47

model poisoning A POISONING ATTACKS which operates through MODEL CONTROL. 5, 6, 37,

41, 111 model privacy attacks An attack against machine learning models to extract sensitive in­

formation about the model. 7 multimodal models A model that processes and relates information from multiple sensory

modalities that each represent primary human channels of communication and sensation, such as vision and touch. 58

## O


[p. 124]

out-of-distribution Data that was collected at a different time and possibly under different

conditions or in a different environment than the data collected to train the model. 56

poisoning attacks Adversarial attacks in which an adversary interferes with a model during

its TRAINING STAGE, such as by inserting malicious training data (DATA POISONING) or modifying the training process itself (MODEL POISONING). 5, 108, 111 pre-training A component of the TRAINING STAGE in which a model learns general patterns,

features, and relationships from vast amounts of unlabeled data, such as through SELF-SUPERVISED LEARNING. Pre-training can equip models with knowledge of gen­ eral features or patterns which may be useful in downstream tasks (see FOUN­ DATION MODEL), and can be followed with additional training or fine-tuning that specializes the model for a specific downstream task. 37 privacy compromise In the AML context, the unauthorized access of restricted or pro­

## P


prietary information that is part of an AI system, including information about a model’s training data, weights or architecture; or sensitive information that the model accesses such as the knowledge base of a GenAI RETRIEVAL-AUGMENTED GEN­ ERATION (RAG) application. 7, 40 prompt extraction An attack that tries to divulge the system prompt or other information

in the context of a large language model that would normally be hidden from a user. 38, 41 prompt injection An attack which exploits the concatenation of untrusted input with a

prompt constructed by a higher-trust party such as the application designer. 38, 41, 108, 110 property inference A data privacy attack that infers a global property about the training

data of a machine learning model. 7

## Q


[pp. 124-125]

query access A capability with which an attacker can issue queries to a trained machine

learning model and obtain predictions or generations. 8, 40, 108

receiver operating characteristic (ROC) A curve that plots the true positive rate versus the

false positive rate for a classifier. 107 red teaming in the AI context, means a structured testing effort, often adopting adversarial

methods, to find flaws and vulnerabilities in an AI system, including unforeseen or undesirable system behaviors or potential risks associated with the misuse of the system. [366]. 60 regression A type of supervised machine learning model that is trained on data, including

## R


[p. 125]

numerical labels (i.e., response variables). Types of regression algorithms include linear regression, polynomial regression, and various non-linear regression meth­ ods. 5 reinforcement learning A type of machine learning in which a model learns to optimize its

behavior according to a reward function by interacting with and receiving feedback from an environment. 5 resource control A capability in which an attacker controls one or more external resources

consumed by a machine learning model at inference time, particularly for GenAI systems such as retrieval-augmented generation applications. 41, 50, 108, 110 retrieval-augmented generation (RAG) A type of GenAI system in which a model is paired

with a separate information retrieval system (or ”knowledge base”). Based on a user query, the RAG system identifies relevant information within the knowledge base and provides it to the GenAI model in context for the model to use in formu­ lating its response. RAG systems allow the internal knowledge of a GenAI model to be modified without the need for retraining. 1, 35, 37, 38, 40, 46, 50, 111 rowhammer attack A software-based fault-injection attack that exploits dynamic random-

access memory disturbance errors via user-space applications and allows the at­ tacker to infer information about certain victim secrets stored in memory cells. Mounting this attack requires the attacker to control a user-space unprivileged process that runs on the same machine as the victim’s machine learning model. 31

## S


[pp. 125-126]

self-supervised learning A type of machine learning that relies on generating implicit la­

bels from unstructured data rather than relying on explicit, human-created labels. Self-supervised learning tasks are constructed to allow the true labels to be auto­ matically inferred from the training data (enabling the use of large-scale training data) and to require models to capture essential features or relationships within the data to solve them. For example, a common self-supervised learning task is providing a model with partial data with the task to accurately generate the re­ mainder. 109, 111 semi-supervised learning A type of machine learning in which a small number of training

samples are labeled, while the majority are unlabeled. 5 shadow model A model that imitates the behavior of the target model. The training datasets

and the truth about membership in these datasets are known for these models.

Typically, the attack model is trained on the labeled inputs and outputs of the shadow model. 25 side channel Allows an attacker to infer information about a secret by observing the non­

functional characteristics of a program (e.g., execution time or memory) or mea­ suring or exploiting the indirect coincidental effects of the system or its hardware (e.g., power consumption variation, electromagnetic emanations) while the pro­ gram is executing. Most commonly, such attacks aim to exfiltrate sensitive infor­ mation, including cryptographic keys. 31 source code control A capability with which an attacker controls the source code of a ma­

chine learning algorithm. 8 supervised learning A type of machine learning in which a model learns to predict explicit

(often human-generated) labels or output values for data. 5 support vector machines Models that implement a decision function in the form of a hy­

perplane that serves to separate (i.e., classify) observations that belong to one class from another based on patterns of information about those observations (i.e., features). 5, 6, 31 system prompt Application-specific instructions provided in-context to a GenAI system

by the model developer or application designer. System prompts are typically prepended to other input, and may be higher-trust than other forms of input. 38, 43, 46, 52


---

[previous part](text-015.md) | [source overview](overview.md) | [next part](text-017.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
