---
type: Source Text
title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations - part 7 of 17 (pp. 66-75)'
description: 'Verbatim extracted text, pp. 66-75: LLM'
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
part: 7
parts_total: 17
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T07:21:49Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T07:21:49Z'
sources:
- id: original
  resource: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  title: 'Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations'
  author: org:nist
  last_modified: '2025-03-24T00:00:00Z'
---

# Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

> Verbatim text extracted from the original (NIST, 2025-03-24), part 7 of 17, pp. 66-75. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## LLM


[pp. 66-67] [ref: 3.4.4]

• Compromising connected resources. [NISTAML.039] [Back to Index] Attackers can use prompt injection attacks to cause a GenAI system to leak private information from the restricted resources it can access. For example, a model integrated as part of an email client could be prompted to forward certain emails to an attacker- controlled inbox [146]. Researchers have identified injection attacks that can force a model to exfiltrate user-uploaded data by querying an attacker-controlled URL with the sensitive data [298].

• Leaking information from user interactions. [NISTAML.036] [Back to Index] Re­ searchers have demonstrated a proof-of-concept indirect prompt injection attack in which they inject instructions for a model to persuade the end user to reveal a piece of information (in this case, their name) that the model then leaks to the attacker, such as by directly querying an attacker-controlled URL with the information or sug­ gesting such a URL to the user to visit [146]. Attackers may also be able to exploit features like markdown image rendering to exfiltrate data [323].

3.4.4. Mitigations

Various techniques (see Sec. 3.3.3) can be used throughout the development and deploy­ ment life cycle (Fig. 7) to mitigate attacks, including:

• Several training techniques have been developed to mitigate against indirect prompt injection, including fine-tuning task-specific models [296] and training models to fol­ low hierarchical trust relationships in prompts [387].

• Detection schemes have been proposed to detect indirect prompt injection, and many LLM-based defenses have been designed to mitigate both direct and indirect prompt injection [6, 18, 154, 204, 313].

• A range of input processing methods have been proposed to combat indirect prompt injection, including filtering out instructions from third-party data sources [146], de­ signing prompts to help aid LLMs in separating trusted and untrusted data (i.e., spot­ lighting [160, 206]), or instructing models to disregard instructions in untrusted data [206].

Many of the defenses described in the context of direct prompt injection can also be adapted to mitigate indirect prompt injection. Because current mitigations do not offer full protection against all attacker techniques, application designers may design systems

with the assumption that prompt injection attacks are possible if a model is exposed to un­ trusted input sources, such as by using multiple LLMs with different permissions [145, 405] or by allowing models to interact with potentially untrustworthy data sources only through well-defined interfaces [410]. Additionally, public education efforts can inform model users and application designers of the risks of indirect prompt injection [266].

3.5. Security of Agents

[pp. 67-68] [ref: 3.6]

An increasingly common use of GenAI models is constructing an (often LLM-based) AGENT, a software system that iteratively prompts a model, process its outputs – such as to select and call a function with specified inputs – and provides the results back to the model as a part of its next prompt [151, 155, 393]. Agents may be equipped to use tools such as web- browsing or code interpreters, and may have additional features such as memory and/or planning capabilities.

Because agents rely on GenAI systems to plan and execute their actions, they can be vul­ nerable to the many of the above categories of attacks against GenAI systems, including direct and indirect prompt injection. However, because agents can take actions using tools, these attacks can create additional risks in this context, such as enabling actors to hijack agents to execute arbitrary code or exfiltrate data from the environment in which they are operating. Security research focused specifically on agents is still in its early stages, but researchers have begun to evaluate the vulnerability of agents to particular AML attacks [12, 430] and to propose interventions to manage the security risks posed by agents [24].

3.6. Benchmarks for AML Vulnerabilities

There are several publicly available benchmarks for evaluating models’ vulnerability to AML attacks. Datasets like JailbreakBench [72], AdvBench [448], HarmBench [237], Stron­ gREJECT [351], AgentHarm [12], and Do-Not-Answer [399] provide benchmarks for evalu­ ating models’ susceptibility to jailbreaks. TrustLLM [169] is a benchmark intended to eval­ uate six dimensions of trust in LLMs: truthfulness, safety, fairness, robustness, privacy, and machine ethics. AgentDojo [101] is an evaluation framework for measuring the vulnerabil­ ity of AI agents to prompt injection attacks in which the data returned by external tools hi­ jacks the agent to execute malicious tasks. Additionally, open-source tools like Garak [106] and PyRIT [364] are intended to help developers identify vulnerabilities to AML attacks in models. Finally, several unlearning benchmarks have recently been proposed [212, 234].

4. Key Challenges and Discussion

4.1. Key Challenges in AML

There are several fundamental challenges that make fully addressing the problems dis­ cussed in this report more difficult. We discuss several here: The trade off between in­ creasing accuracy (or average-case performance) and other attributes including robust­ ness (or worst-case performance); the theoretical limitations and results that imply that fully robust systems may be mathematically impossible without additional assumptions; and the challenge of evaluating progress in AML mitigations rigorously and robustly.

4.1.1. Trade-Offs Between the Attributes of Trustworthy AI

[pp. 68-69] [ref: 4.1.2]

The trustworthiness of an AI system depends on all of the attributes that characterize it [274]. There are trade-offs between explainability and adversarial robustness [176, 245] and between privacy and fairness [178]. For example, AI systems that are optimized for accuracy alone tend to underperform in terms of adversarial robustness and fairness [71, 111, 302, 379, 433]. Conversely, an AI system that is optimized for adversarial robustness may exhibit lower accuracy and deteriorated fairness outcomes [32, 391, 433]. Unfortu­ nately, it may not be possible to simultaneously maximize the performance of an AI system with respect to these attributes.

accuracy Pareto improvement

Pareto front

Pareto inefficient

feasible region

adversarial

robustness

Figure 8. Pareto optimality

The full characterization of the trade-offs between the different attributes of trustworthy AI is an open research problem that is gaining importance with the adoption of AI technology in many areas of modern life. One promising practical approach is based on the concept of

multi-objective optimization and Pareto optimality [285, 286]. In most cases, there is no mathematically best trade-off. However, Fig. 8 illustrates a hypothetical example of a trade- off between accuracy and adversarial robustness. Any point in the feasible region that is not on the Pareto front is a bad point (i.e., Pareto inefficient). There is a better solution (i.e., Pareto improvement) that can significantly help with one objective without harming the other, which is a goal of Pareto optimization. Moreover, if there is a single optimum in some use case, Pareto optimization naturally attains it. Organizations may need to accept trade- offs between these properties and decide which of them to prioritize depending on the AI system, the use case, and other relevant implications of the AI technology [274, 326, 382].

4.1.2. Theoretical Limitations on Adversarial Robustness

Given the multitude of powerful attacks, appropriate mitigations must be designed before AI systems are deployed in critical domains. This challenge is exacerbated by the lack of theoretically secure ML algorithms for many tasks in the field (see Sec. 1). This implies that designing mitigations is an inherently ad hoc and fallible process, though there are practice guides for securing ML deployments [69, 274] and existing guidelines for mitigating AML attacks [120].

[pp. 69-70] [ref: 4.1.3]

An ongoing challenge in AML is the ability to detect when a model is under attack. Knowing this would provide an opportunity to counter the attack before any information is lost or an adverse behaviour is triggered in the model. However, Tramèr [373] has shown that designing techniques to detect adversarial examples is equivalent to robust classification, which is inherently difficult to solve. Adversarial examples may come from the same data distribution on which the model was trained and to which it expects the inputs to belong or may be OUT-OF-DISTRIBUTION (OOD) inputs. Thus, the ability to detect OOD inputs is also an important challenge in AML. Fang et al. [124] established useful theoretical bounds on detectability, particularly an impossibility result when there is an overlap between the in- distribution and OOD data.

Formal methods verification has a long history in other fields that require high assurance, such as avionics and cryptography. Although the results of applying this methodology of­ fer security and safety assurances, they come at a very high cost, which has prevented formal methods from being widely adopted. Currently, formal methods in these fields are primarily used in applications that are mandated by regulations. Applying formal methods to neural networks has the potential to provide much-needed security guarantees, espe­ cially in high-risk applications. However, the viability of this technology will be determined by a combination of technical and business criteria — namely, the ability to handle today’s complex ML models of interest at acceptable costs. More research is needed to extend this technology to the algebraic operations used in ML algorithms, scale it up to the large mod­ els used today, and accommodate rapid changes in the code of AI systems while limiting the costs of applying formal verification.

4.1.3. Evaluation

Another general problem of AML mitigations for both evasion and poisoning attacks is the lack of reliable benchmarks, which causes results from AML papers to be routinely incom­ parable, as they do not rely on the same assumptions and methods. While there have been some promising developments in this direction [97, 327], more research and encour­ agement are needed to foster the creation of standardized benchmarks to gain reliable insights into the actual performance of proposed mitigations.

More broadly, the effectiveness of a mitigation is determined not just by how well it will de­ fend against existing attack, but also how well it defends against unforeseen attacks. This means that new mitigations should be tested adversarially, with the researchers proposing the mitigation also trying to break it. This is often difficult and time-consuming, leading to less rigorous and reliable evaluations of novel mitigations; often they appear very power­ ful, but are quickly shown lack robustness to unforeseen types of attacks.

[pp. 70-71] [ref: 4.2]

Finally, this difficulty combines with the difficulty of trading off between different attributes discussed above. Instead of evaluating each attribute in isolation, they should be evalu­ ated simultaneously for any new mitigations, and mitigations should be compared on a Pareto plot (as in Fig. 8) capturing the various tradeoffs that have to be made. This addi­ tionally increases the cost to evaluating new mitigations, and can make comparing mitiga­ tions difficult - if the green dot represents a new method, it is not possible to say it is an improvement on the red dot, as it is better on one axis but worse on the other.

4.2. Discussion

4.2.1. The Scale Challenge

Data is fundamentally important for training models. Recent trends in GenAI have been towards significant investment in larger models and larger datasets for training them. Few developers of foundation models publish key details about the data sources used in their training [44]. Those who do [247, 371] show the scale of the footprint and the massive amount of data consumed during training. The most recent multi-modal GenAI systems further exacerbate the demand by requiring large amounts of data for each modality.

In most cases, no single entity controls all of the data used to train a particular foundation model. Data repositories are not monolithic data containers but a list of labels and data links to other servers that actually contain the corresponding data samples. This paradigm challenges the classic definition of the corporate cybersecurity perimeter and creates new risks that are difficult to mitigate [57]. Recently published open-source data poisoning tools [241] increase the risk of large-scale attacks on image training data. Although created to enable artists to protect the copyright of their work, these tools may become harmful in the hands of people with malicious intent.

There are several ways this new class of attacks could be mitigated, although it is unclear

how effective mitigations will prove to be as the sophistication of attacks increase. Data and model sanitization techniques (see Sec. 2.3) reduce the impacts of a range of poison­ ing attacks. They can be combined with cryptographic techniques for origin and integrity attestation to provide assurances downstream, as recommended in the final report of the National Security Commission on AI [267]. Robust training techniques (see Sec. 2.3) offer different approaches to developing theoretically certified defenses against data poison­ ing attacks with the intention of providing much-needed information-theoretic guaran­ tees for security. The results are encouraging, but more research is needed to extend this methodology to more general assumptions about data distributions, the ability to handle out-of-distribution inputs, more complex models, multiple data modalities, and better per­ formance. Another challenge is applying these techniques to very large models like LLMs and generative diffusion models, which are becoming targets of attacks [55, 90].

4.2.2. Supply Chain Challenges

[pp. 71-72] [ref: 4.2.3]

The literature on AML shows a trend of designing new attacks that are more difficult to detect. Since the poisoning of AI models can persist through safety training and be trig­ gered by attackers on demand [170], significant concerns arise regarding the potential for models to be created with intentional exploits that are hard for organizations deploying and using models to detect. The potential for attacks against open-source dependencies may be particularly acute in the AI context because organizations and researchers may not be able to audit and identify vulnerabilities encoded into a model’s weights in the same way it is often possible to audit open-source software. As users come to rely more on the outputs of AI systems — for example, some research suggests that software engineers who over-rely on AI coding assistants’ suggestions may produce less secure code [290, 294, 308] — the potential for malicious actors to subtly manipulate the outputs of AI systems may create increased risk.

Additionally, Goldwasser et al. [142] introduced a new class of attacks: information-theoretically undetectable Trojans that can be planted in ML models. If proven practical, the unde­ tectable nature of such attacks would pose significant challenges for AI supply-chain risk management and increase the importance of preventing insider threat throughout the supply chain. DARPA and NIST have also jointly created TrojAI to research the defense of AI systems from intentional, malicious Trojans by developing the technology to detect and investigate these attacks.

4.2.3. Multimodal Models

MULTIMODAL MODELS have shown great potential for achieving high performance on many ML tasks [27, 30, 258, 304, 435]. However, emerging evidence from practice shows that a redundancy of information across the different modalities does not necessarily make the model more robust against adversarial perturbations of a single modality. Combining modalities and training the model on clean data alone does not seem to improve adver­

sarial robustness. In addition, adversarial training, which is widely used in single modality applications, may become prohibitively expensive as the number of modality combina- tions increases. Additional effort is required to benefit from the redundant information in order to improve robustness against single modality attacks [417]. Without such an ef- fort, single modality attacks can be effective and compromise multimodal models across a wide range of multimodal tasks despite the information contained in the remaining unper- turbed modalities [417, 424]. Moreover, researchers have devised efficient mechanisms for constructing simultaneous attacks on multiple modalities, which suggests that mul- timodal models might not be more robust against adversarial attacks despite improved performance [77, 333, 415].

The existence of simultaneous attacks on multimodal models suggests that miti- gation techniques that only rely on single modality perturbations are not likely to be robust.

4.2.4. Quantized Models

[pp. 72-73] [ref: 4.2.5]

Quantization is a technique for efficiently deploying models to edge platforms, such as smart phones and IoT devices [138]. It reduces the computational and memory costs of running inference on a given platform by representing the model weights and activations with low-precision data types. For example, quantized models typically use 8-bit integers (int8) or even more compact 4-bit representations instead of the usual 32-bit floating point (float32) numbers for the original non-quantized model.

This technique has been widely used with PredAI and increasingly with GenAI models [108]. However, quantized models inherit the vulnerabilities of the original models and introduce additional weaknesses that make them vulnerable to adversarial attacks. Error amplifica­ tion from reduced computational precision adversely affects the adversarial robustness of the quantized models. While there are some useful mitigation techniques for PredAI models [216], the effects of quantization on GenAI models have not been studied as thor­ oughly. Organizations that deploy such models should continuously monitor their behav­ ior. Recent results [118] reveal that widely used quantization methods can be exploited to produce a harmful quantized LLM, even though the full-precision counterpart appears benign, potentially tricking users into deploying the malicious quantized model.

4.2.5. Risk Management in Light of AML

A key question that this taxonomy deliberately leaves aside is how organizations can make decisions about the development and use of AI systems in light of evidence about the increasing diversity of AML attacks and the efficacy and limitations of available mitigations.

Especially in GenAI, some model developers and application builders have moved towards paradigms for testing adversarial risks as part of pre-deployment testing and evaluation

of models, such as through a structured process for RED TEAMING [68, 133]. NIST has pro­ duced an initial public draft of guidance for model developers on managing risks associ­ ated with the misuse of foundation model capabilities, including through pre-deployment evaluations. [275] NIST [273] and Barrett et al. [28] have also developed risk profiles for generative AI systems that map to the NIST AI RMF [274] that may assist model developers and users in assessing risks, including those from adversarial attacks.

However, a persistent challenge remains in the fact that many AML mitigations are empir­ ical in nature and lack theoretical or provable guarantees. In fact, several research results have pointed to theoretical limits on AML mitigations, including the impossibility of model- based detection to prevent all impermissible outputs [140] and findings that, so long as a model has any probability of exhibiting an undesired behavior, there exist prompts that can trigger that behavior, implying that any alignment process that attenuates but does not re­ move an unwanted behavior will remain vulnerable to adversarial prompting attacks. [406]

[pp. 73-74] [ref: 4.2.6]

These theoretical limitations do not obviate the utility of pre-deployment adversarial test­ ing, since such testing can potentially foreclose many attack vectors and thus increase the difficulty of mounting a successful attack above would-be attackers’ threshold of effort or capability. However, they suggest that organizations seeking to manage risks related to the development of models with potentially harmful capabilities or the delegation of trust to models in high stakes contexts may need to consider practices and measures beyond adversarial testing to manage the risks associated with AML attacks.

4.2.6. AML and Other AI System Characteristics

A final consideration with respect to adversarial machine learning, and one closely related to questions of risk management, is how to relate and integrate consideration of AML at­ tacks to definitions and processes relating to other desired AI system characteristics.

For example, managing the security of AI systems will require combining mitigations from the field of AML with best practices for the development of secure software from the field of cybersecurity. Understanding and relating these practices to each other, as well as iden­ tifying whether there are other key considerations for AI security that fall outside of the scope of either AML or cybersecurity, will be critical as organizations seek to extend exist­ ing cybersecurity processes and best practices to address the security of newly adopted AI systems.

Similarly, robustness to AML attacks may play an important role in areas beyond the remit of security, such as in AI safety [275] or in achieving other characteristics of trustworthy AI systems [274]. AML is neither a complete solution to, nor a subset of, any one of these characteristics, and as such, more precisely relating AML attacks and mitigations to pro­ cesses for achieving these goals and managing risks in AI systems is an area for ongoing work.

References

[1] Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya Mironov, Kunal

Talwar, and Li Zhang. Deep learning with differential privacy. In ACM Conference on Computer and Communications Security, CCS ’16, pages 308–318, 2016. https: //arxiv.org/abs/1607.00133. doi:10.48550/arXiv.1607.00133. [2] Mark Abspoel, Daniel Escudero, and Nikolaj Volgushev. Secure training of decision

trees with continuous attributes. In Proceedings on Privacy Enhancing Technologies (PoPETs) 2021, Issue 1, 2020. [3] Hojjat Aghakhani, Wei Dai, Andre Manoel, Xavier Fernandes, Anant Kharkar, Christo­

[p. 74]

pher Kruegel, Giovanni Vigna, David Evans, Ben Zorn, and Robert Sim. TrojanPuzzle: Covertly poisoning code-suggestion models, 2024. URL: https://arxiv.org/abs/2301 .02344, arXiv:2301.02344, doi:10.48550/arXiv.2301.02344. [4] Hojjat Aghakhani, Dongyu Meng, Yu-Xiang Wang, Christopher Kruegel, and Giovanni

Vigna. Bullseye polytope: A scalable clean-label poisoning attack with improved transferability. In IEEE European Symposium on Security and Privacy, 2021, Vienna, Austria, September 6-10, 2021, pages 159–178. IEEE, 2021. URL: https://ieeexplo re.ieee.org/document/9581207, doi:10.1109/EuroSP51992.2021.00021. [5] Meta AI. Llama guard 3 documentation, 2024. Accessed: 2024-08-13. URL: https:

//llama.meta.com/docs/model-cards-and-prompt-formats/llama-guard-3/. [6] Meta AI. Prompt guard documentation, 2024. Accessed: 2024-08-13. URL: https:

//llama.meta.com/docs/model-cards-and-prompt-formats/prompt-guard/. [7] AI Safety Institute. Systemic ai safety fast grants. https://www.aisi.gov.uk/grants,

2024. Accessed: 2024-08-22. [8] Dan Alistarh, Zeyuan Allen-Zhu, and Jerry Li. Byzantine Stochastic Gradient Descent.

In NeurIPS, 2018. URL: https://arxiv.org/abs/1803.08917, doi:10.48550/arXiv .1803.08917. [9] Gabriel Alon and Michael Kamfonas. Detecting language model attacks with per­

plexity, 2023. URL: https://arxiv.org/abs/2308.14132, arXiv:2308.14132, doi:10.48550/arXiv.2308.14132. [10] Galen Andrew, Peter Kairouz, Sewoong Oh, Alina Oprea, H. Brendan McMahan, and

Vinith Suriyakumar. One-shot empirical privacy estimation for federated learning, 2023. URL: https://arxiv.org/abs/2302.03098, arXiv:2302.03098, doi:10.485 50/arXiv.2302.03098. [11] Maksym Andriushchenko, Francesco Croce, and Nicolas Flammarion. Jailbreaking

[pp. 74-75]

leading safety-aligned LLMs with simple adaptive attacks, 2024. URL: https://arxiv. org/abs/2404.02151, arXiv:2404.02151, doi:10.48550/arXiv.2404.02151. [12] Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, Derek Duenas,

Maxwell Lin, Justin Wang, Dan Hendrycks, Andy Zou, Zico Kolter, Matt Fredrikson, Eric Winsor, Jerome Wynne, Yarin Gal, and Xander Davies. Agentharm: A bench­ mark for measuring harmfulness of llm agents, 2024. URL: https://arxiv.org/abs/24 10.09024, arXiv:2410.09024.

[13] Anthropic. Model Card and Evaluations for Claude Models. https://www-files.ant

hropic.com/production/images/Model-Card-Claude-2.pdf, July 2023. Anthropic. [14] Anthropic. Anthropic’s interactive prompt engineering tutorial. https://github.com

/anthropics/prompt-eng-interactive-tutorial, 2024. Accessed: 2024-08-22. [15] Anthropic. Claude 3.5 Sonnet. https://www.anthropic.com/news/claude-3-5-son

net, June 2024. Anthropic. [16] Anthropic. Expanding our model safety bug bounty program. https://www.anthro

pic.com/news/model-safety-bug-bounty, 2024. Accessed: 2024-08-22. [17] Giovanni Apruzzese, Hyrum S Anderson, Savino Dambra, David Freeman, Fabio Pier­

azzi, and Kevin Roundy. “real attackers don’t compute gradients”: Bridging the gap between adversarial ml research and practice. In 2023 IEEE Conference on Se­ cure and Trustworthy Machine Learning (SaTML), pages 339–364. IEEE, 2023. URL: https://arxiv.org/abs/2212.14315, doi:10.48550/arXiv.2212.14315. [18] Arthur. Shield, 2023. URL: https://www.arthur.ai/product/shield. [19] Giuseppe Ateniese, Luigi V. Mancini, Angelo Spognardi, Antonio Villani, Domenico


---

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

[^original]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (2025-03-24). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
