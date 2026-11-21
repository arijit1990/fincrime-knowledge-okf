---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 17 of 17 (pp. 126-127)'
description: 'Verbatim extracted text, pp. 126-127: T'
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
part: 17
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-016.md) | [source overview](overview.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 17 of 17, pp. 126-127. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## T


[pp. 126-127]

targeted poisoning attack A poisoning attack that changes the prediction on a small num­

ber of targeted samples. 6, 42 testing data control A capability with which an attacker controls the testing data input to

the machine learning model. 8 training data control A capability in which an attacker controls some or all of the training

data of a machine learning model. 7, 40 training data extraction The ability of an attacker to extract the training data of a genera­

tive model by prompting the model with specific inputs. 7, 46 training stage The stage of a machine learning pipeline in which a model learns parameters

that minimize its error against an objective function based on training data. 5, 37, 111 trojan In the machine learning context, a malicious modification to a model that is difficult

to detect, may appear harmless, but that can alter the intended function of the system upon a signal from an attacker to cause a malicious behavior desired by the attacker. For Trojan attacks to be effective, the trigger must be rare in the normal operating environment so that it does not affect the normal effectiveness of the AI and raise the suspicions of users. In the machine learning context, trojan may be used interchangeably with backdoor pattern. 2

unsupervised learning A type of machine learning in which a model learns based on pat­

terns in unlabeled data, such as learning a function to cluster or group data points. 5


---

[previous part](text-016.md) | [source overview](overview.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
