---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 6 of 17 (pp. 56-66)'
description: 'Verbatim extracted text, pp. 56-66: LLM'
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
part: 6
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:50:18Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:50:18Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 6 of 17, pp. 56-66. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## LLM


[pp. 56-57] [ref: 3.3]

3.3. Direct Prompting Attacks and Mitigations

[NISTAML.018] [Back to Index] DIRECT PROMPTING ATTACK attacks arise when the attacker is the primary user of the system, interacting with the model through query access. A subset of these attacks, in which the main user provides in-context instructions that are appended to higher-trust instructions like those provided by the application designer (such as the model’s SYSTEM PROMPT), are known as DIRECT PROMPT INJECTION attacks.

As in PredAI, attacks may be applicable to a single setting and model, or may instead be uni­ versal (affecting models on a range of separate queries, see Sec. 2.2.1) and/or transferable (affecting models beyond the model they are found on, see Sec. 2.2.3).

An attacker may have a variety of goals when performing these attacks [219, 220, 337], such as to:

• Enable misuse. Attackers may use direct prompting attacks to bypass model-level defenses that a model developer or deployer has created to restrict models from producing harmful or undesirable output [237]. A JAILBREAK is a direct prompting attack intended to circumvent restrictions placed on model outputs, such as circum­ venting refusal behavior to enable misuse.

• Invade privacy. Attackers may use direct prompting to extract the system prompt or reveal private information that was provided to the model in context but not in­ tended for unfiltered access by the user.

• Violate integrity. When LLMs are used as agents, an attacker may use direct prompt­ ing attacks to manipulate tool usage and API calls, and potentially compromise the backend of the system (e.g. executing attacker’s SQL queries).

3.3.1. Attack Techniques

A range of techniques exist for launching direct prompting attacks, many of which gener­ alise across various attacker objectives. With a focus on direct prompting attacks to enable misuse, we note the following broad categories of direct prompting techniques (see [393]):

• Optimization-based attacks design attack objective functions and use gradient or other search-based methods to learn adversarial inputs that cause a particular be­ havior, similar to PredAI attacks discussed in Sec. 2.2.1. Objective functions may be designed to force affirmative starts (e.g., looking for responses that begin with ”Sure”, which may indicate compliance with a malicious request [60, 320, 448]) or other metrics of attack success (e.g., similarity to a toxified finetune [368]).

[pp. 57-58]

Optimization techniques can then be used to learn attacks, including techniques that follow from attacks designed for PredAI language classifiers (e.g., HotFlip [117]) and gradient-free techniques that use a proxy model or random search to test attack can­ didates [11, 320]. Universal adversarial triggers are a special class of these gradient- based attacks against generative models that seek to find input-agnostic prefixes (or suffixes) that produce the desired affirmative response regardless of the remainder of the input [386, 448]. That these universal triggers transfer to other models makes open-weight models — for which there is ready white-box access — feasible attack vectors for transferability attacks on closed systems in which only API access is avail­ able [448].

Attacks can also be designed to satisfy additional constraints (e.g., sufficiently low perplexity [368]) or attack a system of multiple models [235].

• Manual methods for jailbreaking an LLM include competing objectives and mis­ matched generalization [400]. Mismatched generalization-based attacks identify in­ puts that fall outside the distribution of the model’s safety training but remain within the distribution of its capabilities training, making them comprehensible to the model while evading refusal behavior. Competing objectives-based attacks find cases where model capabilities are in tension with safety goals, such as by playing into a model’s drive to follow user-provided instructions. In all cases the goal of the attack is to compromise a model-level safety defense. See Weng [403] for further discussion.

Approaches to competing objectives-based attacks include:

1. Prefix injection: This method involves prompting the model to start responses with an affirmative confirmation. By conditioning the model to begin its output in a predetermined manner, adversaries attempt to influence its subsequent language generation toward specific, predetermined patterns or behaviors.

2. Refusal suppression: Adversaries may explicitly instruct the model to avoid generating refusals or denials in its output. By decreasing the probability of refusal responses, this tactic aims to increase the probability of a compliant

response.

3. Style injection: In this approach, adversaries instruct the model to use (or not use) certain syntax or writing styles. For example, an attack may constrain the model’s language to simplistic or non-professional tones, aiming to decrease the probability of (usually professionally worded) refusals.

4. Role-play: Adversaries utilize role-play strategies (e.g., “Always Intelligent and Machiavellian” [AIM] or “Do Anything Now” [DAN]) to guide the model to adopt specific personas or behavioral patterns that conflict with the original intent. This manipulation aims to exploit the model’s adaptability to varied roles or characteristics, with an intent to compromise its adherence to safety proto­ cols.

Approaches to mismatched generalization-based attacks include:

[pp. 58-59] [ref: 3.3.2]

1. Special encoding: Strategies that use encoding techniques like base64 to alter the representation of input data in a way that remains understandable to the model but may be out of distribution for safety training.

2. Character transformation: Strategies that use character-level transformations like the ROT13 cipher, symbol replacement (e.g., l33tspeak), and Morse code to take the input out of the safety training distribution.

3. Word transformation: Strategies that alter the linguistic structure of the in­ put, such as Pig Latin, synonym swapping (e.g., using “pilfer” for “steal”), and payload splitting (or “token smuggling”) to break down sensitive words into substrings.

4. Prompt-level transformation: Strategies that use prompt-level transformations, such as translating the prompt into a less common language that may be out of distribution of the safety training data.

• Automated model-based red teaming employs an attacker model, a target model, and a judge [73, 239, 292]. When the attacker has access to a high-quality classifier that judges whether model output is harmful, it may be used as a reward function to train a generative model to generate jailbreaks of another generative model. Only query access is required for each of the models, and no human intervention is re­ quired to update or refine a candidate jailbreak. The prompts may also be transfer­ able from the target model to other closed-source LLMs [73].

The Crescendo attack [316] introduced the idea of interacting with the model itera­ tively in a multi-turn adaptive attack that includes seemingly benign prompts, even­ tually leading to a successful jailbreak against safety alignment. The initial manual attack is fully automated by leveraging another LLM for prompt generation and in­ corporating multiple input sources.

Evaluations of leading models suggest LLMs remain vulnerable to these many of these attacks [11, 338, 381].

3.3.2. Information Extraction

[NISTAML.038] [Back to Index] Both during training and at run-time, GenAI models are ex­ posed to a range of information which may be of interest to attackers, like personally iden­ tifying information (PII) in the training data, sensitive information in RETRIEVAL-AUGMENTED GENERATION (RAG) databases provided in-context, or even the SYSTEM PROMPT constructed by the application designer. Additionally, features of the model itself—such as the model weights or architecture—may be targets of attack. Though many of the techniques in Sec. 3.3.1 apply to extracting such data, we note several specific goals and techniques specific to data extraction.

[pp. 59-60]

Leaking sensitive training data. Carlini et al. [59] were the first to practically demonstrate TRAINING DATA EXTRACTION attacks in generative language models. By inserting canaries– synthetic, easy-to-recognize out-of-distribution examples–in the training data, they devel­ oped a methodology for extracting the canaries and introduced a metric called exposure to measure memorization. Subsequent work demonstrated the risk of data extraction in LLMs based on transformers (e.g., GPT-2 [63]) by prompting the model with different pre­ fixes and mounting a membership inference attack to determine which generated content was part of the training set. Since these decoder stack transformers are autoregressive models, a verbatim textual prefix about personal information can sometimes result in the model completing the text input with sensitive information that includes email addresses, phone numbers, and locations [229]. This behavior of verbatim memorization of sensitive information in GenAI language models has also been observed in more recent transformer models with the additional characterization of extraction methods [165]. Unlike PredAI models in which tools like Text Revealer are created to reconstruct text from transformer- based text classifiers [434], GenAI models can sometimes simply be asked to repeat pri­ vate information that exists in the context as part of the conversation. Results show that information like email addresses can be revealed at rates exceeding 8% for certain mod­ els. However, their responses may wrongly assign the owner of the information and be otherwise unreliable. In general, extraction attacks are more successful when the model is seeded with more specific and complete information — the more the attacker knows, the more they can extract. Researchers have leveraged this fact to incrementally extract fragments of copyrighted New York Times articles from LLMs by seeding it with a single sentence, and allowing the LLM to recurrently extract additional text [356]. Intuitively, larger models with a higher capacity are more susceptible to exact reconstruction [56]. Fine-tuning interfaces also amplify the risk of data extraction attacks, as demonstrated by an attack that extracts PII from pre-training data using fine-tuning API for open-weight models [83], though this is not a direct prompting attack.

Prompt and context stealing. Prompts are vital to align LLMs to a specific use case and are

Post-Training

1 2

Before Training Pre-Training

Evaluation

Capability Improvements 7

Fine-Tuning Capabilities Eval.

Setup Infrastructure

Tool Use

Safeguards Eval.

Editing

Collect Data

Process Data

Interpretability

Iteration

Unlearning

Exposure Exposure Exposure

... ...

Predictive Evaluations

Checkpoint Evaluations

Internal Deployment

Broad Query Access

5 6 Monitoring & Reporting

Safety Improvements

AI <> World User <> AI Access Control

API Security

Continuous

Evaluation

Safety Improvements

Tools Data

Exposure

Access Control

Figure 7. Map of the development and deployment life cycle of an AI model for broad-scale query access

[pp. 60-61] [ref: 3.3.3]

a key ingredient to their utility in following human instructions. These prompts can there­ fore be regarded as commercial secrets, and are sometimes the target of direct prompting attacks. PromptStealer is a learning-based method that reconstructs prompts from text-to­ image models using an image captioning model and a multi-label classifier to steal both the subject and the prompt modifiers [339]. For certain LLMs, researchers have found that a small set of fixed attack queries (e.g., Repeat all sentences in our conversation) were sufficient to extract more than 60 % of prompts across certain model and dataset pairs [439]. In some cases, effective prompts may draw from significant technical or do­ main expertise; prompt-stealing attacks may violate or threaten these investments. Fur­ thermore, in RAG applications (see Fig. 6), the same techniques can be used to extract sensitive information provided in the LLMs’ context. For example, rows from a database or text from a PDF document that are intended to be summarized generically by the LLM can be verbosely extracted by simply asking for them via direct prompting, or performing simple prompting attacks.

Model extraction. As in PredAI (Sec. 2.4.4), attackers may perform MODEL EXTRACTION at­ tacks which attempt to learn information about the model architecture and parameters by submitting specially-crafted queries. Recently, Carlini et al. [61] demonstrated that such information could be extracted from black-box production LLMs, deriving previously un­ known hidden dimensions and the embedding projection layer (up to symmetries).

3.3.3. Mitigations

The following defense strategies can be employed throughout the deployment life cycle of an AI model or system to reduce the risk that the model or system will be vulnerable to direct prompt injections. The numbers in parentheses refer to the numbering in Fig. 7, which shows a map of the deployment life cycle for broad-scale query access.

• Interventions during pre-training (2) and post-training (3). A range of training strate­ gies have been proposed to increase the difficulty of accessing harmful model capa­ bilities through direct prompt injection, including safety training during pre-training [197] or post-training [147, 445], adversarial training methods[340], and other meth­ ods to make jailbreak attacks more difficult [447].

[pp. 61-62]

• Interventions during evaluation (4). Evaluations can measure the vulnerability of models to query-based attacks, which can then inform trust and affordance deci­ sions, as well as developer and user education. Evaluations can include broad auto­ mated vulnerability assessments [72, 107, 324] as well as targeted expert red team­ ing [381] and bug bounties [16]. Current evaluation approaches, though a useful tool, may underestimate vulnerabilities accessible to actors with more time, resourc­ ing, or luck. Evaluations measure model vulnerabilities at a particular moment in time; assessments may change if new attacks are developed, additional data is col­ lected post-training, or model capabilities are improved. Continuous evaluations following deployment can help combat these challenges.

• Interventions during deployment (5). A broad set of deployment-time interventions have been proposed:

– Prompt instruction and formatting techniques. Model instructions can cue the

model to treat user input carefully, such as by wrapping user input in XML tags, appending specific instructions to the prompt, or otherwise attempting to clearly separate system instructions from user prompts [14, 206, 219].

– Detecting and terminating harmful interactions. Rather than preventing harm­

ful model generations, AI systems may be able to detect these generations and terminate interactions. Several open [5, 6, 154] and closed [18, 204, 313] so­ lutions have explored LLM-based detection systems with distinctly prompted and/or fine-tuned models that classify user input and/or model output as harm­ ful or undesirable. These may provide supplementary assurance through a defense-in-depth philosophy. However, these detection systems are also vul­ nerable to attacks [235] and may have correlated failures to the main models that they are monitoring. Some lines of research have investigated constrain­ ing the space of generations to enable deterministic guardrails [306].Early work suggests that interpretability-based techniques can also be used to detect anoma­ lous input [31], as well as keyword- or perplexity-based defenses [9, 164].

– Prompt stealing detection. A common approach to mitigating prompt stealing

is to compare the model utterance to the prompt, which is known by the sys­ tem provider. Defenses differ in how this comparison is made, which might include looking for a specific token, word, or phrase, as popularized by [59], or comparing the n-grams of the output to the input [439]. Similarly, defenses for prompt stealing have yet to be proven rigorous.

– Input modification. User input can additionally be modified prior to being

passed to the model, such as paraphrasing or retokenizing [182]. However, such methods may be expensive and/or have trade-offs with model perfor­ mance.

– Aggregating output from multiple prompts. Motivated by randomized smooth­

[pp. 62-63]

ing [95] used to improve robustness against evasion attacks for ML classifiers, SmoothLLM [312] proposes aggregating the LLM output from multiple ran­ domly perturbed prompts. This defense incurs a cost of generating multiple LLM queries for each prompt and might reduce the quality of the generated output.

– Monitoring and response. Following deployment, monitoring and logging of

user activity may allow model deployers to identify and respond to instances of attempted and successful direct prompt injection attacks [266]. This response could include banning or otherwise acting against users if their intentions ap­ pear malicious, or remediating the prompt injection vulnerability in the event of a successful attack. Standard user- or organization-level vetting or identity verification procedures, as well as clear incentive mechanisms (such as a policy of restricting model access in response to violations) may enhance the efficacy of this mitigation.

– Usage restrictions. Other interventions have focused on choices about how

models are offered to users: for example, the efficacy of some attacks can be reduced by limiting the inference parameters that are accessible to users (e.g., temperature or logit bias), as well as the richness of the model generations re­ turned (e.g., logit probabilities) [250]. Additionally, limiting the release of pub­ lic information [252, 266] and artifacts [249] and restricting the total number of model queries available to users [251] may make attacks more challenging. These techniques may have additional drawbacks in limiting positive use cases.

Indirect mitigations. Despite the growing number of proposed defenses at both the model and the system levels, recent findings suggest that current generation models remain highly vulnerable to direct prompt injection attacks [11, 381]. Thus, other potential mitigations for prompt injection rely not on directly increasing an AI system’s robustness against such attacks, but instead on designing systems under the assumption that the AI model can and will produce malicious output if it is exposed to malicious actors. For example, deploy­ ers can design AI systems under the assumption that models with access to sensitive data

or the ability to take undesirable actions may leak that data or take those actions [266]. Additionally, developers or deployers might use other technical mitigations to reduce the misuse potential of outputs obtained through direct prompt injection, such as:

• Training data sanitization. Model training data can be sanitized to remove sensitive or toxic content and data that are largely or exclusively relevant for developing un­ desirable capabilities. Such sanitization may prevent harmful capabilities from being learned and reduce the potential harms from direct prompt injection, though they may harm generalization and harmful content detection abilities [224].

[pp. 63-64] [ref: 3.4]

• Unlearning. There have also been attempts to “unlearn” harmful knowledge or ca­ pabilities post-training [212], with the goal of reducing harms from maliciously di­ rected models [158]. However, these methods remain vulnerable to adversarial at­ tacks, including attacks on jailbreak-specific training approaches [367] and inversion attacks on unlearning methods [328], which extract supposedly unlearned data.

• Watermarking. Developers or deployers may watermark content generated by an AI model to help trace its provenance, distinguish it from human-generated con­ tent, and reduce risks from malicious use cases (e.g., by flagging content as model- generated when it appears online). While the literature has proposed various tech­ niques with different strengths and weaknesses [194], there is no watermarking technique that is universally effective and robust under all circumstances. Many powerful attacks have been developed against watermarking with high success rates [188, 319]. Moreover, theoretical impossibility results regarding the robustness of water­ marking have also been established [432].

Finally, beyond interventions at the developer or deployer levels, society and infrastructure can become more resilient to maliciously directed model capabilities over time [7, 33]. For example, defenders could adopt AI-based vulnerability discovery tools [99] to make their systems more resilient to malicious actors misusing GenAI models to find vulnerabilities for exploitation.

3.4. Indirect Prompt Injection Attacks and Mitigations

[NISTAML.015] [Back to Index] Many use cases for GenAI models involve models interact­ ing with additional resources, from an internet-connected AGENT to a RETRIEVAL-AUGMENTED GENERATION (RAG) system depicted in Fig. 6. Because GenAI models combine the data and instruction channels, attackers can leverage the data channel to affect system operations by manipulating resources with which the system interacts. Thus, INDIRECT PROMPT INJECTION attacks are enabled by RESOURCE CONTROL that allows an attacker to indirectly (or remotely) inject system prompts without directly interacting with the application [146, 408]. Indirect prompt injection attacks can result in violations across at least three categories of attacker goals: 1) availability violation, 2) integrity violation, and 3) privacy compromise. However, unlike in direct prompt injection attacks, indirect prompt injection attacks are mounted not

by the primary user of a model but instead by a third party. In fact, in many cases, it is the primary user of the model who is harmed by the compromise of the integrity, availability, or privacy of the GenAI system through an indirect prompt injection attack.

3.4.1. Availability Attacks

[pp. 64-65] [ref: 3.4.2]

[NISTAML.016] [Back to Index] Attackers can manipulate resources to inject prompts into GenAI models that are designed to disrupt the availability of the model for legitimate users. Availability attacks can indiscriminately render a model unusable (e.g., failure to generate helpful outputs) or specifically block certain capabilities (e.g., specific APIs) [146].

Attacker techniques. Researchers have demonstrated several proof-of-concept methods by which attackers can disrupt the availability of a GenAI system:

• Time-consuming background tasks. [NISTAML.017] [Back to Index] An indirectly injected prompt can instruct the model to perform a time-consuming task prior to answering the request. The prompt itself can be brief, such as by requesting looping behavior in the evaluating model [146].

• Inhibiting capabilities. An indirectly injected prompt can instruct the model that it is not permitted to use certain APIs (e.g., the search API for an internet-connected chatbot). This selectively disarms key components of the service [146].

• Disruptive output formatting. An attacker can use indirect prompt injection to in­ struct the model to modify its output in a way that disrupts the availability of the system. For example, an attacker could instruct the model to replace the characters in retrieved text with homoglyph equivalents, disrupting subsequent API calls [146]; or could request that the model begins each sentence with an to­ ken, forcing the model to return an empty output [146].

3.4.2. Integrity Attacks

[NISTAML.027] [Back to Index]

Through indirect prompt injection, attackers can use malicious resources to prompt GenAI systems to become untrustworthy and generate content that deviates from benign behav­ ior to align with adversarial objectives. These attacks often involve disrupting the model’s behavior in subtle ways that may not be obvious to the end user.

For example, researchers have demonstrated attacks through indirect prompt injection that can cause a GenAI system to produce arbitrarily incorrect summaries of sources, to respond with attacker-specified information, or to suppress or hide certain information sources [146]. Attackers could use these capabilities to weaponize GenAI systems such as internet-connected chatbots against their users for a range of malign purposes, includ­ ing spreading targeted misleading information, recommending fraudulent products or ser­ vices, or redirecting consumers to malicious websites that spoof legitimate log-in pages or

contain downloadable malware. Attackers may also use indirect prompt injection attacks to hijack a GenAI AGENT, causing it to perform a malicious, attacker-specified task instead of (or in addition to) its intended, user-provided task [353].

Attacker techniques. Researchers have demonstrated integrity attacks through malicious resources that manipulate the primary task of the LLM:

[pp. 65-66] [ref: 3.4.3]

• Jailbreaking. Attackers can leverage techniques for indirect prompt injection that are similar to those used in direct prompt injection attacks, such as using a JAILBREAK that allows the attacker to substitute their own malicious instructions in place of the model’s SYSTEM PROMPT. As in direct prompting attacks, these attacks may be crafted through optimization-based or manual methods, and may rely on techniques such as mismatched generalization.

• Execution triggers. Researchers have automated manual indirect prompt injection attacks using execution triggers generated via optimization with a technique called Neural Exec [287]. These execution triggers can also persist through RAG processing pipelines that include multiple phases, such as chunking and contextual filtering.

• Knowledge base poisoning. The knowledge database of a RAG system can be poi­ soned to achieved targeted LLM output to specific user queries, as in PoisonedRAG [449]. Recently, a general optimization framework called Phantom [75] has shown how a single poisoned document can be crafted and inserted into the knowledge database of a RAG system to induce a number of adversarial objectives in the LLM generator.

• Injection hiding. Attackers may use techniques to hide or obfuscate their injections, such as by hiding injections in non-visible portions of a resource; using multi-stage injections, in which the initial injection directs the model to visit another resource which contains additional injections; or encoding injection commands such as in Base64 and then instructing the model to decode the sequence[146].

• Self-propagating injections. Attackers may be able to use indirect prompt injection attacks to turn GenAI systems into vectors for spreading attacks. For example, an attacker could send a malicious email that, when read by a model integrated as part of an email client, instructs the model to spread the infection by sending similar malicious emails to everyone in the user’s contact list. In this way, certain malicious prompts could serve as worms [146].

3.4.3. Privacy Compromise

Attackers can use indirect prompt injection attacks to compromise the privacy of a GenAI system or its primary users. For example, attackers could use indirect prompt injection attacks to compel a model to leak information from restricted resources, such as a user’s private data that is processed by the GenAI system. Alternately, in a blend of integrity and

privacy attacks, an attacker could gather information about the primary user or users of the system by instructing a model to obtain and then leak that information.

Attacker techniques. Researchers have theorized and demonstrated a variety of indirect prompt injection attacks to compromise information from internet-connected chatbots, RAG systems, and other GenAI systems. Some of these techniques include:


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
