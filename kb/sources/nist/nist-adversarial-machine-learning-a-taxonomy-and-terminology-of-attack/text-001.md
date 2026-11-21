---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 1 of 17 (pp. 1-13)'
description: Verbatim extracted text, pp. 1-13
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
part: 1
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 1 of 17, pp. 1-13. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

[pp. 1-4]

NIST Trustworthy and Responsible AI

NIST AI 100-2e2025

Adversarial Machine Learning A Taxonomy and Terminology of Attacks and Mitigations

Apostol Vassilev

Alina Oprea Alie Fordyce Hyrum Anderson

Xander Davies

Maia Hamin

This publication is available free of charge from:

https://doi.org/10.6028/NIST.AI.100-2e2025

NIST Trustworthy and Responsible AI

NIST AI 100-2e2025

Adversarial Machine Learning A Taxonomy and Terminology of Attacks and Mitigations

Apostol Vassilev Alina Oprea Computer Security Division Northeastern University Information Technology Laboratory

Maia Hamin Alie Fordyce U.S. AI Safety Institute Hyrum Anderson National Institute of Standards and Cisco Technology

Xander Davies U.K. AI Security Institute

This publication is available free of charge from:

https://doi.org/10.6028/NIST.AI.100-2e2025

March 2025

U.S. Department of Commerce

Howard Lutnick, Secretary

National Institute of Standards and Technology Craig Burkhardt, Acting Under Secretary of Commerce for Standards and Technology and Acting NIST Director

Certain commercial equipment, instruments, software, or materials, commercial or non-commercial, are identified in this paper in order to specify the experimental procedure adequately. Such identification does not imply recommendation or endorsement of any product or service by NIST, nor does it imply that the materials or equipment identified are necessarily the best available for the purpose.

NIST Technical Series Policies Copyright, Use, and Licensing Statements NIST Technical Series Publication Identifier Syntax

Publication History Approved by the NIST Editorial Review Board on 2025-03-20

How to Cite this NIST Technical Series Publication: Vassilev A, Oprea A, Fordyce A, Anderson H, Davies X, Hamin M (2025) Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations. (National Institute of Standards and Technology, Gaithersburg, MD) NIST Trustworthy and Responsible AI, NIST AI 100-2e2025. https://doi.org/10.6028/NIST.AI.100-2e2025

Author ORCID iDs Apostol Vassilev: 0000-0002-9081-3042 Alina Oprea: 0000-0002-4979-5292 Maia Hamin: 0009-0009-3834-6553

Contact Information ai-100-2@nist.gov

Additional Information Additional information about this publication is available at https://csrc.nist.gov/pubs/ai/100/2/e2025/final, including related content, potential updates, and document history.

All comments are subject to release under the Freedom of Information Act (FOIA).

Abstract

[pp. 4-5]

This NIST Trustworthy and Responsible AI report provides a taxonomy of concepts and defines terminology in the field of adversarial machine learning (AML). The taxonomy is arranged in a conceptual hierarchy that includes key types of ML methods, life cycle stages of attack, and attacker goals, objectives, capabilities, and knowledge. This report also identifies current challenges in the life cycle of AI systems and describes corresponding methods for mitigating and managing the consequences of those attacks. The terminology used in this report is consistent with the literature on AML and is complemented by a glossary of key terms associated with the security of AI systems. Taken together, the taxonomy and terminology are meant to inform other standards and future practice guides for assessing and managing the security of AI systems by establishing a common language for the rapidly developing AML landscape.

Keywords

artificial intelligence; machine learning; attack taxonomy; abuse; data poisoning; evasion; privacy breach; attack mitigation; large language model; chatbot.

NIST Trustworthy and Responsible AI

The National Institute of Standards and Technology (NIST) promotes U.S. innovation and industrial competitiveness by advancing measurement science, standards, and technology in ways that enhance economic security and improve our quality of life. Among its broad range of activities, NIST contributes to the research, standards, evaluations, and data required to advance the development, use, and assurance of trustworthy artificial intelligence (AI).

Table of Contents

Audience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

Trademark Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

How to Read This Document . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ix

Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ix

Author Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ix

Predictive AI and Generative AI Taxonomy Index . . . . . . . . . . . . . . . . . . . x

Executive Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xii

[p. 5] [ref: 2.1]

1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

2. Predictive AI Taxonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.1. Attack Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.1.1. Stages of Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.1.2. Attacker Goals and Objectives . . . . . . . . . . . . . . . . . . . . . 6

2.1.3. Attacker Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.1.4. Attacker Knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.1.5. Data Modality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.2. Evasion Attacks and Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . 11

2.2.1. White-Box Evasion Attacks . . . . . . . . . . . . . . . . . . . . . . . 12

2.2.2. Black-Box Evasion Attacks . . . . . . . . . . . . . . . . . . . . . . . 15

2.2.3. Transferability of Attacks . . . . . . . . . . . . . . . . . . . . . . . . 15

2.2.4. Evasion attacks in the real world . . . . . . . . . . . . . . . . . . . . 16

2.2.5. Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2.3. Poisoning Attacks and Mitigations . . . . . . . . . . . . . . . . . . . . . . . . 19

[pp. 5-6] [ref: 2.3.1]

2.3.1. Availability Poisoning . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2.3.2. Targeted Poisoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.3.3. Backdoor Poisoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2.3.4. Model Poisoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

2.3.5. Poisoning Attacks in the Real World . . . . . . . . . . . . . . . . . . 27

2.4. Privacy Attacks and Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . 28

2.4.1. Data Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

2.4.2. Membership Inference . . . . . . . . . . . . . . . . . . . . . . . . . . 29

2.4.3. Property Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

2.4.4. Model Extraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

2.4.5. Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3. Generative AI Taxonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.1. Attack Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.1.1. GenAI Stages of Learning . . . . . . . . . . . . . . . . . . . . . . . . 36

3.1.2. Attacker Goals and Objectives . . . . . . . . . . . . . . . . . . . . . 39

[p. 6] [ref: 3.1.3]

3.1.3. Attacker Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3.2. Supply Chain Attacks and Mitigations . . . . . . . . . . . . . . . . . . . . . 41

3.2.1. Data Poisoning Attacks . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.2.2. Model Poisoning Attacks . . . . . . . . . . . . . . . . . . . . . . . . 42

3.2.3. Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.3. Direct Prompting Attacks and Mitigations . . . . . . . . . . . . . . . . . . . 43

3.3.1. Attack Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

3.3.2. Information Extraction . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.3.3. Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

3.4. Indirect Prompt Injection Attacks and Mitigations . . . . . . . . . . . . . . 50

3.4.1. Availability Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

3.4.2. Integrity Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

3.4.3. Privacy Compromise . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

3.4.4. Mitigations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3.5. Security of Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

[pp. 6-7] [ref: 3.6]

3.6. Benchmarks for AML Vulnerabilities . . . . . . . . . . . . . . . . . . . . . . . 54

4. Key Challenges and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

4.1. Key Challenges in AML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

4.1.1. Trade-Offs Between the Attributes of Trustworthy AI . . . . . . . . 55

4.1.2. Theoretical Limitations on Adversarial Robustness . . . . . . . . . . 56

4.1.3. Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4.2. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4.2.1. The Scale Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4.2.2. Supply Chain Challenges . . . . . . . . . . . . . . . . . . . . . . . . . 58

4.2.3. Multimodal Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

4.2.4. Quantized Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

4.2.5. Risk Management in Light of AML . . . . . . . . . . . . . . . . . . . 59

4.2.6. AML and Other AI System Characteristics . . . . . . . . . . . . . . 60

Appendix: Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

List of Figures

[pp. 7-9]

Figure 1. Taxonomy of attacks on PredAI systems . . . . . . . . . . . . . . . . 4 Figure 2. Taxonomy of attacks on GenAI systems . . . . . . . . . . . . . . . . . 35 Figure 3. Example LLM Training Pipeline used for InstructGPT [281] . . . . 36 Figure 4. LLM enterprise adoption pipeline . . . . . . . . . . . . . . . . . . . . . 37 Figure 5. LLM enterprise adoption reference architecture . . . . . . . . . . . . 38 Figure 6. Retrieval-augmented generation . . . . . . . . . . . . . . . . . . . . . . . 39 Figure 7. Map of the development and deployment life cycle of an AI model

for broad-scale query access . . . . . . . . . . . . . . . . . . . . . . . . . 47 Figure 8. Pareto optimality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

Audience

The intended primary audience for this document includes individuals and groups who are responsible for designing, developing, deploying, evaluating, and governing AI systems.

Background

This document is the result of an extensive literature review, conversations with experts in adversarial machine learning, and research performed by the authors in adversarial ma­ chine learning.

Trademark Information

All trademarks and registered trademarks belong to their respective organizations.

The Information Technology Laboratory (ITL) at NIST develops tests, test methods, refer­ ence data, proof of concept implementations, and technical analyses to advance the de­ velopment and productive use of information technology. ITL’s responsibilities include the development of management, administrative, technical, and physical standards and guide­ lines.

This NIST Trustworthy and Responsible AI report focuses on identifying, addressing, and managing risks associated with adversarial machine learning. While practical guidance1

published by NIST may serve as an informative reference, this guidance remains voluntary.

The content of this document reflects recommended practices. This document is not in­ tended to serve as or supersede existing regulations, laws, or other mandatory guidance.

1In the context of this paper, the terms “practice guide,” “guide,” “guidance,” and the like are consensus- created informative references that are intended for voluntary use. They should not be interpreted as equal to the use of the term “guidance” in a legal or regulatory context. This document does not establish any legal standard or any other legal requirement or defense under any law, nor does it have the force or effect of law.

viii

How to Read This Document

[pp. 9-10]

This document uses the terms “AI technology,” “AI system,” and “AI applications” inter­ changeably. Terms related to the machine learning pipeline, such as “ML model” or “algo­ rithm,” are also used interchangeably in this document. Depending on context, the term “system” may refer to the broader organizational and/or social ecosystem within which the technology was designed, developed, deployed, and used instead of the more traditional use related to computational hardware or software.

Important reading notes:

• This document includes a series of blue callout boxes that highlight nuances and important takeaways.

• This document contains links shown in blue. Clicking on them will bring the reader to the relevant resource. Links links in the References point to external sources.

• Terms that are used but not defined or explained in the text are listed and defined in the Glossary. They are displayed in small caps in the text. Clicking on a word shown in SMALL CAPS (e.g., ADVERSARIAL EXAMPLE) takes the reader directly to the definition of that term in the Glossary. From there, one may click on the page number shown at the end of the definition to return.

• This document provides an Index of attack types to easily navigate and reference attacks and corresponding mitigations.

Acknowledgments

The authors wish to thank all of the people and organizations who submitted comments on the draft version of this paper. The received comments and suggested references were essential to improving the document and the future direction of this work. The authors also want to thank the many NIST, U.S. AI Safety Institute, and U.K. AI Security Institute colleagues who assisted in updating this document.

Author Contributions

The authors contributed equally to this work.

ix

Predictive AI and Generative AI Taxonomy Index

• Predictive AI Attacks Taxonomy

– Availability Violations (ID: NISTAML.01)

* Model Poisoning (ID: NISTAML.011)

* Clean-label Poisoning (ID: NISTAML.012)

* Data Poisoning (ID: NISTAML.013)

* Energy-latency (ID: NISTAML.014)

– Integrity Violations (ID: NISTAML.02)

* Clean-label Poisoning (ID: NISTAML.012)

* Clean-label Backdoor (ID: NISTAML.021)

* Evasion (ID: NISTAML.022)

* Backdoor Poisoning (ID: NISTAML.023)

* Targeted Poisoning (ID: NISTAML.024)

* Black-box Evasion (ID: NISTAML.025)

* Model Poisoning (ID: NISTAML.026)

– Privacy Compromises (ID: NISTAML.03)

* Model Extraction (ID: NISTAML.031)

* Reconstruction (ID: NISTAML.032)

* Membership Inference (ID: NISTAML.033)

[pp. 10-12]

* Property Inference (ID: NISTAML.034)

– Supply Chain Attacks (ID: NISTAML.05)

* Model Poisoning (ID: NISTAML.051)

• Generative AI Attacks Taxonomy

– Availability Violations (ID: NISTAML.01)

* Data Poisoning (ID: NISTAML.013)

* Indirect Prompt Injection (ID: NISTAML.015)

* Prompt Injection (ID: NISTAML.018)

– Integrity Violations (ID: NISTAML.02)

x

* Data Poisoning (ID: NISTAML.013)

* Indirect Prompt Injection (ID: NISTAML.015)

* Prompt Injection (ID: NISTAML.018)

* Backdoor Poisoning (ID: NISTAML.023)

* Targeted Poisoning (ID: NISTAML.024)

* Misaligned Outputs (ID: NISTAML.027)

– Privacy Compromises (ID: NISTAML.03)

* Indirect Prompt Injection (ID: NISTAML.015)

* Prompt Injection (ID: NISTAML.018)

* Backdoor Poisoning (ID: NISTAML.023)

* Membership Inference (ID: NISTAML.033)

* Prompt Extraction (ID: NISTAML.035)

* Leaking information from user interactions (ID: NISTAML.036)

* Training Data Attacks (ID: NISTAML.037)

* Data Extraction (ID: NISTAML.038)

* Compromising connected resources (ID: NISTAML.039)

– Misuse Violations (ID: NISTAML.04)

* Prompt Injection (ID: NISTAML.018)

– Supply Chain Attacks (ID: NISTAML.05)

* Model Poisoning (ID: NISTAML.051)

xi

Executive Summary

This NIST Trustworthy and Responsible AI report describes a taxonomy and terminology for ADVERSARIAL MACHINE LEARNING (AML) that may aid in securing applications of artificial intelligence (AI) against adversarial manipulations and attacks.

The statistical, data-based nature of ML systems opens up new potential vectors for at­ tacks against these systems’ security, privacy, and safety, beyond the threats faced by tra­ ditional software systems. These challenges span different phases of ML operations such as the potential for adversarial manipulation of training data; the provision of adversar­ ial inputs to adversely affect the performance of the AI system; and even malicious ma­ nipulations, modifications, or interactions with models to exfiltrate sensitive information from the model’s training data or to which the model has access. Such attacks have been demonstrated under real-world conditions, and their sophistication and impacts have been increasing steadily.

[pp. 12-13]

The field of AML is concerned with studying these attacks. It must consider the capabilities of attackers, the model or system properties that attackers might seek to violate in pursuit of their objectives, and the design of attack methods that exploit vulnerabilities during the development, training, and deployment phases of the ML life cycle. It is also concerned with the design of ML algorithms and systems that can withstand these security and privacy challenges, a property often known as robustness [274].

To taxonimize these attacks, this report differentiates between predictive and generative AI systems and the attacks relevant to each. It considers the components of an AI system including the data; the model itself; the processes for training, testing, and deploying the model; and the broader software and system contexts into which models may be embed­ ded, such as cases where Generative Artificial Intelligence (GenAI) models are deployed with access to private data or equipped with tools to take actions with real-world conse­ quences.

Thus, the attacks within this taxonomy are classified relative to: (i) the AI system type, (ii) the stage of the ML life cycle process in which the attack is mounted, (iii) the attacker’s goals and objectives in terms of the system properties they seek to violate, (iv) the at­ tacker’s capabilities and access, and (v) the attacker’s knowledge of the learning process and beyond.

This report adopts the concepts of security, resilience, and robustness of ML systems from the NIST AI Risk Management Framework. Security, resilience, and robustness are gauged by risk, which is a measure of the extent to which an entity (e.g., a system) is threatened by a potential circumstance or event (e.g., an attack) and the severity of the outcome should such an event occur. However, this report does not make recommendations on risk toler­ ance (i.e., the level of risk that is acceptable to organizations or society) because it is highly contextual and specific to applications and use cases.

xii

The spectrum of effective attacks against ML is wide, rapidly evolving, and covers all phases of the ML lifecycle — from design and implementation to training, testing, and deployment in the real world. The nature and power of these attacks are different and their impacts may depend not only on the vulnerabilities of the ML models but also the weaknesses of the infrastructure in which the AI systems are deployed. AI system components may also be adversely affected by design and implementation flaws that cause failures outside the context of adversarial use, such as inaccuracy. However, these kinds of flaws are not within the scope of the literature on AML or the attacks in this report.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
