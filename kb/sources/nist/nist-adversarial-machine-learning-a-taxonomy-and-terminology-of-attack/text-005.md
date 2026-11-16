---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 5 of 17 (pp. 44-56)'
description: 'Verbatim extracted text, pp. 44-56: LLM'
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
part: 5
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 5 of 17, pp. 44-56. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

[pp. 44-45] [ref: 2.4.5]

Several techniques for mounting model extraction attacks have been introduced in the literature. The first method is that of direct extraction based on the mathematical formu­ lation of the operations performed in deep neural networks, which allows the adversary to compute model weights algebraically [58, 177, 376]. A second technique is to use learning methods for extraction. For example, active learning [70] can guide the queries to the ML model for more efficient extraction of model weights, and reinforcement learning can train an adaptive strategy that reduces the number of queries [280]. A third technique uses SIDE CHANNEL information for model extraction. Batina et al. [29] used electromagnetic side channels to recover simple neural network models, while Rakin et al. [303] showed how ROWHAMMER ATTACK can be used for model extraction of more complex convolutional

neural network architectures.

Model extraction is often not an end goal but a step toward other attacks. As the model weights and architecture become known, attackers can launch more powerful attacks that are typical for the white-box or gray-box settings. Therefore, preventing model extraction can mitigate downstream attacks that depend on the attacker having knowledge of the model architecture and weights.

2.4.5. Mitigations

The discovery of reconstruction attacks against aggregate information motivated the rig­ orous definition of differential privacy (DP) [112, 113], an extremely strong definition of privacy that guarantees a bound on how much an attacker with access to the algorithm output can learn about each individual record in the dataset. The original pure definition of DP has a privacy parameter ε (i.e., privacy budget), which bounds the probability that the attacker with access to the algorithm’s output can determine whether a particular record was included in the dataset. DP has been extended to the notions of approximate DP, which includes a second parameter δ that is interpreted as the probability of information accidentally being leaked in addition to ε and Rènyi DP [246].

DP has been widely adopted due to several useful properties: group privacy (i.e., the exten­ sion of the definition to two datasets that differ in k records), post-processing (i.e., privacy is preserved even after processing the output), and composition (i.e., privacy is composed if multiple computations are performed on the dataset). DP mechanisms for statistical computations include the Gaussian mechanism [113], the Laplace mechanism [113], and the Exponential mechanism [238]. The most widely used DP algorithm for training ML models is DP-SGD [1], and recent improvements include DP-FTRL [189] and DP matrix fac­ torization [105].

[pp. 45-46]

By definition, DP provides mitigation against data reconstruction and membership infer­ ence attacks. In fact, the definition of DP immediately implies an upper bound on the success of an adversary in mounting a membership inference attack. Tight bounds on the success of membership inference have been derived by Thudi et al. [369]. However, DP does not provide guarantees against model extraction attacks, as this method is designed to protect the training data, not the model. Several papers have reported negative results after using differential privacy to protect against property inference attacks that aim to extract the properties of subpopulations in the training set [74, 233].

One of the main challenges of using DP in practice is setting up the privacy parameters to achieve a trade-off between the level of privacy and the achieved utility, which is typically measured in terms of accuracy for ML models. Analysis of privacy-preserving algorithms (e.g., DP-SGD) is often worst-case and not tight, and selecting privacy parameters based purely on theoretical analysis results in utility loss. Therefore, large privacy parameters are often used in practice (e.g., the 2020 U.S. Census release used ε = 19.61), and the

exact privacy obtained in practice is difficult to estimate. Jagielski et al. [181] introduced privacy auditing with the goal of empirically measuring the actual privacy guarantees of an algorithm and determining privacy lower bounds by mounting privacy attacks. Many pri­ vacy auditing techniques are based on inserting canaries – synthetic and easy-to-identify out-of-distribution examples – into the training set, and then measuring the canary pres­ ence in model output. Auditing can also be performed with membership inference at­ tacks [183, 427], but intentional insertion of strong canaries may result in better estimates of privacy leakage [181, 265]. Recent advances in privacy auditing include tighter bounds for the Gaussian mechanism [263] and rigorous statistical methods that allow for the use of multiple canaries to reduce the sample complexity of auditing [297]. Additionally, two efficient methods for privacy auditing with training a single model have been proposed: Steinke et al. [355] use, multiple random data canaries without incurring the cost of group privacy; and Andrew et al. [10] used multiple random client canaries and cosine similarity test statistics to audit user-level private federated learning.

Differential privacy provides a rigorous notion of privacy and protects against membership inference and data reconstruction attacks. To achieve the best bal­ ance between privacy and utility, empirical privacy auditing is recommended to complement the theoretical analysis of private training algorithms.

[pp. 46-47] [ref: 3.1]

There are other mitigation techniques against model extraction, such as limiting user queries to the model, detecting suspicious queries to the model, or creating more robust architec- tures to prevent side-channel attacks. However, these techniques can be circumvented by motivated and well-resourced attackers and should be used with caution. There are practice guides available for securing ML deployments [69, 274]. A completely differ­ ent approach to potentially mitigating privacy leakage of a user’s data is to perform MA­ CHINE UNLEARNING, a technique that enables a user to request the removal of their data from a trained ML model. Existing techniques for machine unlearning are either exact (i.e., retraining the model from scratch or from a certain checkpoint) [45, 52] or approx­ imate (i.e., updating the model parameters to remove the influence of the unlearned records) [139, 175, 268]. They offer different tradeoffs between computation and privacy guarantees, with exact unlearning methods offering stronger privacy, at additional compu­ tational cost.

3. Generative AI Taxonomy

GenAI is a branch of AI that develops models that can generate content (e.g., images, text, and other media) with similar properties to their training data. GenAI includes sev­ eral different types of AI technologies with distinct origins, modeling approaches, and re­ lated properties, including: GENERATIVE ADVERSARIAL NETWORKS, GENERATIVE PRE-TRAINED TRANSFORMER (GPT), and DIFFUSION MODELS, among others. Recently, GenAI systems have emerged with multi-modal content generation or comprehension capabilities [119], some­ times through combining two or more model types.

3.1. Attack Classification

While many attack types in the PredAI taxonomy apply to GenAI (e.g., data poisoning, model poisoning, and model extraction), recent work has also introduced novel AML at­ tacks specific to GenAI systems.

[pp. 47-49] [ref: 3.1.1]

Figure 2 shows a taxonomy of attacks in AML for GenAI systems. Similar to the PredAI taxonomy in Fig. 1, this taxonomy is first categorized by the system properties that attackers seek to compromise in each case, including availability breakdowns, integrity violations, and privacy compromises, as well as the additional category of AML attack relevant to GenAI of misuse enablement, in which attackers seek to circumvent restrictions placed on the outputs of GenAI systems (see Sec. 2.1.2). The capabilities that an adversary must leverage to achieve their objectives are shown in the outer layer of the objective circles. Attack classes are shown as callouts connected to the capabilities required to mount each attack. Where there are specific types of a more general class of attack (for example, a jailbreak is a specific kind of direct prompting attack attack), the specific attack is linked to the more general attack class through an additional callout. Certain attack classes are listed multiple times because the same attack technique can be used to achieve different attacker goals.

Direct Prompting Attack

Query Access

Increased Computation

Availability Indirect Prompt Injection

Control

Training Data

Data Poisoning

Resource Control

Indirect Prompt Injection

Direct Prompting Attack

Indirect Prompt Injection

Direct Prompting Attack

Jailbreaking

Query Access

Query Access

Resource Control

Resource Control

Integrity

Misuse

Targeted Poisoning

Targeted Poisoning

Training Data Control

Data Poisoning

Model Control

Model Poisoning

Model Control

Training Data Control

Data Poisoning

Fine-tuning Circumvention

Backdoor Poisoning

Backdoor Poisoning

Backdoor Poisoning

Prompt Extraction

Direct Prompting

Backdoor Poisoning

Model Poisoning

Model Extraction

Attack

Model

Query Access

Model Control

Privacy

Data

Backdoor Poisoning

Query

Data Poisoning

Training Data

Access

Direct Prompting

Training Data Control

Resource

Extraction

Attack

Control

Leaking Data from

Indirect Prompt

User Interaction

Injection

Figure 2. Taxonomy of attacks on GenAI systems

An attack can be further categorized by the learning stage to which it applies and by the attacker’s knowledge and access. These are reviewed in the following sections. Where pos­ sible, the discussion broadly applies to GenAI models, though some attacks may be most relevant to particular kinds of GenAI models or model-based systems such as RETRIEVAL­ AUGMENTED GENERATION (RAG) [RAG] systems, chatbots, or AGENT systems.

3.1.1. GenAI Stages of Learning

Reinforcement

Pre-Training Supervised Fine-Tuning

Reward Modeling

Learning

Raw internet data

low quality/ large

Human Prompts low quantity/ high

quantity

Sets of ideal labeled assistant responses low quantity/high quality

Comparisons human written, low quantity/high quality

quality

Binary Classification

Reinforcement Learning

Language modeling predict the next token

Language modeling predict the next token

predict rewards according to preferences

generate tokens that maximize the reward

Base Model SFT Model RM Model (not released) RLHF Model

Figure 3. Example LLM Training Pipeline used for

InstructGPT [281]

[pp. 49-50]

The GenAI development pipeline shapes the space of possible AML attacks against GenAI models and systems. In GenAI moreso than in PredAI, different activities such as data col­ lection, model training, model deployment, and application development are often carried out by multiple different organizations or actors.

For example, a common paradigm in GenAI is the use of a smaller number of foundation models to support a diverse range of downstream applications. Foundation models are pre-trained on large-scale data using self-supervised learning in order to encode general patterns in text, images, or other data that may be relevant for many different applica­ tions [311]. Data at the scale used in foundation models is often collected from a variety of internet sources (which attackers can target, such as in DATA POISONING attacks).

This generalist learning paradigm equips foundation models with a variety of capabilities and tendencies — many of which are desirable, but some of which may be harmful or unwanted by the model developer. Techniques such as supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF) can be used after initial pre-training to better align the base model with human preferences and to curb undesirable or harmful model outputs [281] (see Fig. 3). However, these interventions can later be targeted using AML techniques by attackers seeking to recover or re-enable potentially harmful capabili­ ties.

Developers can make trained foundation models available to downstream users and de­ velopers in a variety of ways, including openly releasing the model’s weights for re-use and

Scope Select Adapt and Align Model Application Integration

Define the problem Choose model Prompt engineering

Optimize and deploy model

Augment model & build LLM -powered

Fine-tuning Align with human feedback

Evaluate

for inference

apps

Figure 4. LLM enterprise adoption pipeline

modification, or hosting the model and offering access as a service through an API. These release decisions impact attacker capabilities that shape the space of possible AML attacks, such as whether attackers possess MODEL CONTROL.

Depending on how a foundation model has been made available, downstream developers can customize and build upon the model to create new applications, such as by further fine-tuning the model for a specific use case, or by integrating a foundation model with a software system, such as to build a retrieval-augmented generation (RAG) or agent (see Figure 4). Thus, a foundation model’s vulnerabilities to AML attacks can potentially impact a wide range of downstream applications and end users. At the same time, the specific application context in which a foundation model is integrated can create additional vectors for and risks from AML attacks, such as the potential exposure of application-specific data.

AML attacks differ and depend on different phases of the GenAI development lifecycle. One major division is between attacks that target the training stage and those that target model inference during the deployment stage.

[p. 50]

Training-time attacks. [NISTAML.037] [Back to Index] The TRAINING STAGE for GenAI of­ ten consists of foundation model PRE-TRAINING and model FINE-TUNING. This pattern exists for generative image models, text models, audio models, and multimodal models, among others. Since foundation models are most effective when trained on large datasets, it has become common to scrape data from a wide range of public sources, increasing the vul­ nerability of these models to DATA POISONING attacks. Additionally, GenAI systems trained or fine-tuned by third parties are often used in downstream applications, leading to the risk of MODEL POISONING attacks from maliciously constructed models.

## LLM


[pp. 51-52]

External Data Sources (E.g. Documents,

Database, Web)

Prompt Injection/Jailbreaking:

token smuggling. role playing

Trigger API Calls

Orchestration

Email Generation

Library

External Applications

Perform Calculations

Figure 5. LLM enterprise adoption reference architecture

Inference-time attacks. The DEPLOYMENT STAGE for GenAI models and systems varies both based on how models are hosted or otherwise made available to users, and in how they are integrated into downstream applications. However, GenAI models and applications often share properties that leave them vulnerable to similar types of attacks. For example, underlying many of the security vulnerabilities in LLM applications is the fact that data and instructions are not provided in separate channels to the LLM, which allows attackers to use data channels to inject malicious instructions in inference-time attacks (a similar flaw to that which underlies decades-old SQL injection attacks). Many of the attacks in this stage are due to the following practices that are common in applications of text-based generative models:

1. In-context instructions and system prompts: [NISTAML.035] [Back to Index] The behavior of LLMs can be shaped through inference-time prompting, whereby the developer or user provides in-context instructions that are often prepended to the model’s other input and context. These instructions comprise a natural language de­ scription of the model’s application-specific use case (e.g., “You are a helpful finan­ cial assistant who responds gracefully and concisely....”) and is known as a SYSTEM PROMPT. A PROMPT INJECTION overrides these instructions, exploiting the concatena­ tion of untrusted user output to the system prompt to induce unintended behavior. For example, an attacker could inject a JAILBREAK that overrides the system prompt to cause the model to generate restricted or unsafe outputs. Since these prompts have been carefully crafted through prompt engineering and may be security-relevant, a PROMPT EXTRACTION attack may attempt to steal these system instructions. These attacks are also relevant to multimodal and text-to-image models.

2. Runtime data ingestion from third-party sources: In RETRIEVAL-AUGMENTED GENERA­

TION (RAG) applications, chatbots, and other applications in which GenAI models are used to interface with additional resources, context is often crafted at runtime in a query-dependent way and populated from external data sources (e.g., documents, web pages, etc.) that are to be used as part of the application. INDIRECT PROMPT INJECTION attacks depend on the attacker’s ability to modify external sources of in­ formation that will be ingested into the model context, even if not provided directly by the primary system user.

[pp. 52-53] [ref: 3.1.2]

3. Output handling: The output of an GenAI model may be used dynamically, such as to populate an element on a web page or to construct a command that is executed without any human supervision, which can lead to a range of availability, integrity or privacy violations in downstream applications if an attacker can induce behavior in this output that the developer has not accounted for.

4. Agents: An LLM-based AGENT relies on iteratively processing the output of an LLM (item 3 above) to perform a task and then provides the results as additional con­ text back to the LLM input (item 2) [151, 155, 393]. For example, an agent system may select from among a configured set of external dependencies and invoke the code with templates filled out by the LLM using information in the context. Adver­ sarial inputs into this context, such as from interactions with untrusted resources, could hijack the agent into performing adversary-specified actions instead, leading to potential security or safety violations.

System

You are a helpful financial assistant. Be concise.

User

What was the net income of ACME in 2020 Q1?

Context

Assistant

$2.5B, down from $3.6B in 2019 Q1.

Input

User

What was their operating cash flow?

Assistant

doc1: ACME announces Q1 results... doc2: Financial results ending Mar 31, 2020...

Assistant

Resources (e.g. vector db)

Figure 6. Retrieval-augmented generation

3.1.2. Attacker Goals and Objectives

As with PredAI, attacker objectives can be classified broadly along the dimensions of avail­ ability, integrity, and privacy, along with a new, GenAI-specific category of attacks designed to enable misuse.

• In an AVAILABILITY BREAKDOWN attack [NISTAML.01] [Back to Index], an attacker

seeks to interfere with a GenAI model or system to disrupt the ability of other users or processes to obtain timely and consistent access to its outputs or functionality.

• In an INTEGRITY VIOLATION attack [NISTAML.02] [Back to Index], an attacker seeks to interfere with a GenAI system to force it to misperform against its intended ob­ jectives and produce output that aligns with the attacker’s objective. As users and businesses rely on GenAI systems to perform tasks like research and productivity as­ sistance, these violations can allow attackers to weaponize the trust that these users place in GenAI systems.

[pp. 53-54] [ref: 3.1.3]

• In a PRIVACY COMPROMISE attack [NISTAML.03] [Back to Index], an attacker seeks to gain unauthorized access to restricted or proprietary information that is part of a GenAI system, including information about a model’s training data, weights or ar­ chitecture; or sensitive information that the model accesses such as the knowledge base of a RETRIEVAL-AUGMENTED GENERATION (RAG) application. GenAI systems may be exposed to sensitive data (intentionally or otherwise) during training or inference, and attacks may seek to extract such information (e.g., through INDIRECT PROMPT IN­ JECTION attacks, where a third party exfiltrates in-context user information [307], or a MODEL EXTRACTION attack to exfiltrate model information [61]).

• Misuse enablement [NISTAML.04][Back to Index]. An additional attacker objective that is especially relevant in the GenAI context is the goal of MISUSE ENABLEMENT. In these attacks, an attacker seeks to deliberately circumvent technical restrictions imposed by the GenAI system’s owner on its use, such as restrictions designed to pre­ vent the system from producing outputs that could cause harm to others, cf. [325].

Technical restrictions refer in this context to defenses applied to the GenAI system such as the use of system prompts or RLHF for safety alignment. While the specific technical restrictions in place will vary between models, the techniques for circum­ venting such defenses are often common between different kinds of models and different kinds of misuse, allowing them to be taxonomized as a part of AML with­ out specificity as to the particular kinds of misuse that model developers seek to prevent.

3.1.3. Attacker Capabilities

AML attacks can be taxonomized with respect to the capabilities that an attacker has in controlling inputs to the GenAI model or system. These capabilities include:

• TRAINING DATA CONTROL: The attacker might take control of a subset of the training data by inserting or modifying training samples. This capability is used in DATA POI­ SONING attacks.

• QUERY ACCESS: Many GenAI models and their applications are deployed as services that can be accessed over the internet by users. In these cases, attackers can sub­

mit adversarially crafted queries to the model to elicit specific desired behavior or extract information. This capability is used for PROMPT INJECTION, PROMPT EXTRAC­ TION, and MODEL EXTRACTION attacks. Query access can vary based on the degree of generation control (e.g., modifying the temperature or adding a logit bias) and the richness of the returned generation (e.g., with or without log probabilities or multiple choices).

• RESOURCE CONTROL: The attacker might modify resources (e.g., documents, web pages) that will be ingested by the GenAI model at runtime. This capability is used for INDIRECT PROMPT INJECTION attacks.

[pp. 54-55] [ref: 3.2]

• MODEL CONTROL: The attacker might have the ability to modify model parameters, such as through public fine-tuning APIs or openly accessible model weights. This capability is used in MODEL POISONING attacks, as well FINE-TUNING CIRCUMVENTION attacks which remove refusal behavior or other model-level safety interventions [132, 153, 300].

As in PredAI, attackers can also vary in their knowledge of the underlying ML model, from full knowledge of the ML system including model weights (white-box attacks), to minimal knowledge and systems with deliberately obscured or misleading information (black-box attacks), to somewhere in between (gray-box attacks). See Sec. 2.1.4, which discusses attacker knowledge in greater detail and applies to GenAI attacks.

3.2. Supply Chain Attacks and Mitigations

[NISTAML.05] [Back to Index]

Since AI is software, it inherits many of the vulnerabilities of the traditional software sup­ ply chain, such as reliance on third-party dependencies. AI development also introduces new types of dependencies, including data collection and scoring, the integration or adap­ tation of third-party-developed AI models, and the integration of third-party-developed plugins into AI systems. Mitigating the security challenges in AI supply chain manage­ ment is complex and requires a multifaceted approach that combines existing practices for software supply chain risk management with the management of AI-specific supply chain risks, such as through the use of provenance information for the additional arti­ facts involved [159, 267]. Studies of real-world security vulnerabilities against ML suggest that security is best addressed comprehensively and by considering the full attack sur­ face, including data and model supply chains, software, and network and storage systems [17, 370]. While all of these supply chain risks are critical in the broader context of securing AI systems, there are certain types of attacks that rely on exploiting the specific statistical and data-based properties of ML systems, thus falling within the domain of AML.

3.2.1. Data Poisoning Attacks

The performance of GenAI text-to-image and text-to-text models has been found to scale with dataset size (among other properties like model size and data quality); for example, Hoffmann et al. [161] suggest compute-optimally training a 520 billion parameter model may require 11 trillion tokens of training data. Thus, it has become common for GenAI foundation model developers to scrape data from a wide range of sources. In turn, the scale of this data and the diversity of its sources provides a large potential attack surface into which attackers may seek to insert adversarially constructed data points. For example, dataset publishers may provide a list of URLs to constitute a training dataset, and attackers may be able to purchase some of the domains that serve those URLs and replace the site content with their own malicious content [57].

[pp. 55-56] [ref: 3.2.2]

Beyond the vast quantities of pre-training data, data poisoning attacks may also affect other stages of the LLM training pipeline, including instruction tuning [389] and reinforce­ ment learning from human feedback [305], which may intentionally source data from a large number of human participants.

As with PredAI models (see Sec. 2.1), data poisoning attacks could lead to attackers control­ ling model behavior through the insertion of a backdoor (see BACKDOOR POISONING ATTACK) such as a word or phrase that, when submitted to a model, acts as a universal JAILBREAK [305]. Attackers could also use data poisoning attacks to modify model behavior on partic­ ular user queries (see TARGETED POISONING ATTACK), such as causing the model to incorrectly summarize or otherwise produce degenerate outputs in response to queries that contain a particular trigger word or phrase [389]. These attacks may be practical—requiring a rel­ atively small portion of the total dataset [46]—and may lead to a range of bad outcomes, such as code suggestion models which intentionally suggest insecure code [3].

3.2.2. Model Poisoning Attacks

[NISTAML.051] [Back to Index]

In GenAI, it is common for developers to use foundation models developed by third parties. Attackers can take advantage of this fact by offering maliciously designed models, such as pre-trained models that enable a BACKDOOR POISONING ATTACK or TARGETED POISONING AT­ TACK. While this attack relies on the attacker having control over the initial poisoned model, researchers have identified attacks in which malicious backdoors in pre-trained models can persist even after downstream users fine-tune the model for their own use [201] or apply additional safety training measures [170].

3.2.3. Mitigations

GenAI poisoning mitigations largely overlap with PredAI poisoning mitigations (see Sec. 2.3). For preventing data poisoning with web-scale data dependencies, this includes ver­

ifying web downloads as a basic integrity check to ensure that domain hijacking has not injected new sources of data into the training dataset [57]. That is, the provider publishes cryptographic hashes, and the downloader verifies the training data. Data filtering can also attempt to remove poisoned samples, though detecting poisoned data within a large training corpus may be very difficult.

While traditional software supply chain risk management practices such as vulnerability scanning of model artifacts can help manage some kinds of AI supply chain risks, new ap­ proaches are required to detect vulnerabilities in models such as those introduced through model poisoning attacks. Current proposed approaches include using methods from the field of mechanistic interpretability to identify backdoor features [67] and detecting and counteracting triggers when they are seen at inference time. Beyond these mitigations, risks can be reduced by understanding models as untrusted system components and de­ signing applications such that risks from attacker-controlled model outputs are reduced [266].


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
