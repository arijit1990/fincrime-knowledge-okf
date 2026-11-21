---
type: Source Digest
title: 'Managing explanations: how regulators can address AI explainability - part 2 of 3 (pp. 12-20)'
description: 'Verified paraphrased digest, pp. 12-20: Managing explanations: how regulators can address AI explainability issues > Section 3 – Challenges in enforcing explainability requirements in the context of AI; Managing explanations: how regulators can address AI explainability issues > Section 4 – Potential adjustments to MRM guidelines; Managing explanations: how regulators can address AI explainability issues > Section 5 – Conclusion; and 1 more sections'
resource: https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
tags:
- explainability
- guidance
- international_standard
- intl
- model_governance
- model_validation
status: stable
source_id: bis-bcbs-managing-explanations-how-regulators-can-address-ai-explainab
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: guidance
normative_force: international_standard
publication_date: '2025-09-08'
legal_status: current
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T08:40:40Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T08:40:40Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T08:40:40Z'
sources:
- id: original
  resource: https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
  title: 'Managing explanations: how regulators can address AI explainability'
  author: org:bis_bcbs
  last_modified: '2025-09-08T00:00:00Z'
digest_points: 121
---

# Managing explanations: how regulators can address AI explainability (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 12-20) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 3.1 Existing methods for explaining AI models and potential limitations

- **descriptive / definition**: Among interpretable model types, a decision tree is explained by following its tree structure, which works through if-then-else rules. (p. 12)[^original]  
  <sub>anchor: "A model is explained by following the tree structure that follows an if-then-elserules approach."</sub>
- **descriptive / definition**: A generalised additive model is an interpretable model type that explains the relationships between input variables and the predicted output. (p. 12)[^original]  
  <sub>anchor: "A model that explains the relationships between input variables and predicted output."</sub>
- **descriptive / context**: Some black box models are inherently not interpretable because of their complexity, non-linearities and large number of parameters, which makes it impossible to connect the model output back to understandable rules, patterns or inputs. (p. 12)[^original]  
  <sub>anchor: "black box models that are inherently not interpretable because of their complexity, non-linearities"</sub>
- **permissive / method**: To contribute to the explainability of black box models, post hoc techniques can be used to analyse a black box model after it has made predictions or delivered an output. (p. 12)[^original]  
  <sub>anchor: "post hoc techniques can be used to analyse a black box model after it has made"</sub>
- **descriptive / context**: The paper distinguishes explainability from interpretability for regulatory purposes because they may have different implications for financial institutions, although some literature uses the terms interchangeably. (p. 12)[^original]  
  <sub>anchor: "this paper finds it useful to distinguish between these concepts for regulatory purposes"</sub>
- **descriptive / context**: NIST (2023) takes the opposite view to the paper: explainability answers how a decision was made in the system, while interpretability answers why a decision was made and its meaning or context for the user. (p. 12)[^original]  
  <sub>anchor: "stating that explainability answers the question of how a decision was made in the system"</sub>
- **descriptive / context**: Thampi (2022) states that explainability requires interpretability as a building block. (p. 12)[^original]  
  <sub>anchor: "Thampi (2022) states that explainability requires interpretability as a building block."</sub>
- **descriptive / context**: The paper focuses on the explainability of AI models that are not interpretable because such models pose regulatory challenges. (p. 12)[^original]  
  <sub>anchor: "This paper focuses on the explainability of AI models that are not interpretable, because such models pose regulatory challenges."</sub>
- **descriptive / context**: Under the definitions used, models that are interpretable should also be explainable and thus should pose fewer issues to regulators. (p. 12)[^original]  
  <sub>anchor: "models that are interpretable should also be explainable and, thus, should pose fewer issues to regulators"</sub>
- **descriptive / context**: European Data Protection Supervisor (2023) offers a similar classification to self-interpretable versus post hoc models but uses different terminology (white box versus black box). (p. 12)[^original]  
  <sub>anchor: "offers a similar classification but uses a different terminology"</sub>
- **descriptive / context**: Thomas (2024) summarises four main categories of general AI explainability techniques for GenAI models: feature-based, sample-based, mechanistic and probing-based. (p. 12)[^original]  
  <sub>anchor: "Thomas (2024) summarises four main categories of general AI explainability techniques for GenAI models: feature-based, sample-based, mechanistic and probing-based."</sub>
- **descriptive / definition**: Global explainability is the ability to explain the overall functioning of a model by capturing patterns, general trends and insights that apply broadly to its behaviour; this is more of a concern for model developers, validators and regulators. (p. 13)[^original]  
  <sub>anchor: "Global explainability refers to the ability to explain the overall functioning of a model"</sub>
- **descriptive / definition**: Local explainability identifies the specific inputs that drive a specific output; this is more of a concern for individual customers seeking explanations in use cases such as credit decisions. (p. 13)[^original]  
  <sub>anchor: "while the latter is more of a concern for individual customers seeking explanations in use cases like credit decisions"</sub>
- **descriptive / method**: The SHAP (SHapley Additive exPlanations) method is a post hoc technique that attributes a model's prediction to individual input features or factors. (p. 13)[^original]  
  <sub>anchor: "SHapley Additive exPlanations (SHAP) method,32 which attributes a model"</sub>
- **descriptive / method**: The LIME (Local Interpretable Model-agnostic Explanations) method is a post hoc technique that explains the most significant features influencing a prediction by fitting a simpler model using data slightly altered from the original data point. (p. 13)[^original]  
  <sub>anchor: "by fitting a simpler model using data that are slightly altered from the original data point"</sub>
- **descriptive / method**: Counterfactual explanation is a post hoc technique that explains a model output by identifying the smallest change to the features that would change the prediction or output. (p. 13)[^original]  
  <sub>anchor: "explains a model output by identifying the smallest change to the features that would change the prediction/output."</sub>
- **descriptive / context**: Post hoc techniques are useful for overcoming human cognitive limits; Candelon et al (2023) cite cognitive load theory, which suggests humans can only understand up to about seven rules or nodes, making it virtually impossible to fully understand decisions of sophisticated AI systems. (p. 13)[^original]  
  <sub>anchor: "humans can only understand up to about seven rules or nodes"</sub>
- **descriptive / context**: A firm may document how an AI model works while human supervisors may still not completely understand it. (p. 13)[^original]  
  <sub>anchor: "while a firm may document how an AI model works, human supervisors may not completely understand"</sub>
- **descriptive / context**: IMDA and PDPC (2020) point out that technical explainability may not always be sufficient, especially where the target audience is the average consumer; providing laypersons with counterfactuals (for example, a mortgage would have been approved if average debt was 15% lower) could be more appropriate in such cases. (p. 13)[^original]  
  <sub>anchor: "technical explainability may not always be sufficient, especially if the target audience is the average consumer"</sub>
- **descriptive / context**: Open source explainability algorithms are available to generate post hoc explanations. (p. 13)[^original]  
  <sub>anchor: "Open source explainability algorithms are available to generate post hoc explanations"</sub>
- **descriptive / context**: For a credit underwriting AI model, SHAP can explain the extent to which each feature or risk factor (such as income or credit history) contributes to the model output (the underwriting decision). (p. 13)[^original]  
  <sub>anchor: "SHAP can explain the extent to which each"</sub>
- **descriptive / finding or result**: Bank of England and Financial Conduct Authority (2024) find that feature importance and SHAP are the most widely used explainability techniques among surveyed UK financial institutions. (p. 13)[^original]  
  <sub>anchor: "feature importance and SHAP are the most widely used by surveyed financial institutions in the United Kingdom"</sub>
- **descriptive / method**: Apley and Zhu (2020) introduce accumulated local effects (ALE) plots, an efficient way to visualise feature effects by integrating local changes in predictions. (p. 13)[^original]  
  <sub>anchor: "Apley and Zhu (2020) introduces accumulated local effects (ALE) plots"</sub>
- **descriptive / case example**: IAIS (2025) gives insurer examples of explainability techniques; for instance SHAP can be used to tell consumers that their premium was influenced primarily by driving history (40% impact), vehicle type (30% impact) and location (20% impact). (p. 13)[^original]  
  <sub>anchor: "driving history (40% impact), vehicle type (30% impact) and location (20% impact)"</sub>
- **descriptive / case example**: In a LIME example for a credit underwriting recommendation, the value of one or several risk factors is changed slightly and the model re-run; higher weights are assigned to risk factors producing outputs more similar to the original, illustrating how the model reaches its recommendation. (p. 13)[^original]  
  <sub>anchor: "the value of one or several risk factors is changed slightly and the model is re-run"</sub>
- **descriptive / context**: Ribeiro et al (2018) provide an improved version of LIME called anchors. (p. 13)[^original]  
  <sub>anchor: "Ribeiro et al (2018) provides an improved version of LIME called anchors."</sub>
- **descriptive / case example**: Dandl et al (2020) give a counterfactual statement example: a loan was denied because annual income was GBP 30,000, and with an income of GBP 45,000 a loan would have been offered. (p. 13)[^original]  
  <sub>anchor: "You were denied a loan because your annual income was GBP 30,000"</sub>
- **descriptive / finding or result**: EBA (2023) lists several measures used by surveyed banks to explain machine learning techniques, including counterfactual explanations. (p. 13)[^original]  
  <sub>anchor: "EBA (2023) lists several measures used by surveyed banks to explain machine learning techniques"</sub>
- **descriptive / context**: The way explanations are delivered may influence the comprehension of the intended audience; Pearl and Mackenzie (2018) opine that humans are more attuned to causal narratives than abstract statistical concepts. (p. 13)[^original]  
  <sub>anchor: "Pearl and Mackenzie (2018) opines that humans are more attuned to causal narratives than abstract statistical concepts."</sub>
- **descriptive / context**: The explainability techniques are not mutually exclusive, and there are pros and cons for each method. (p. 13)[^original]  
  <sub>anchor: "these explainability techniques are not mutually exclusive and there are pros and cons for each method.38"</sub>
- **expected / expectation**: From a supervisory perspective, understanding the limitations of explainability techniques is important; Table 2 gives a non-exhaustive list of such limitations. (p. 13)[^original]  
  <sub>anchor: "understanding the limitations of explainability techniques is important"</sub>
- **descriptive / method**: A footnote notes that Goldstein et al (2015) put forward individual conditional expectation (ICE) plots as a visualisation technique; these show prediction-versus-feature curves for each instance, revealing heterogeneity and interactions that average partial dependence can hide, and they also give a simple visual way to test for additivity. (p. 13)[^original]  
  <sub>anchor: "Goldstein et al (2015) proposes individual conditional expectation (ICE) plots, which display per-instance prediction-feature curves"</sub>
- **descriptive / limitation**: Table 2, limitation 'Inaccuracy': explanations may not faithfully represent an AI model's actual decision; Rudin (2019) explains that post hoc techniques like LIME or SHAP can be unfaithful to the underlying AI models. (p. 14)[^original]  
  <sub>anchor: "Rudin (2019) explains how post hoc techniques like LIME or SHAP can be unfaithful to the underlying AI models."</sub>
- **descriptive / limitation**: Table 2, limitation 'Instability and sensitivity': small changes to data input can lead to drastically different explanations; Alvarez-Melis and Jaakkola (2018) explain that model-agnostic perturbation-based techniques are more prone to instability than gradient-based techniques. (p. 14)[^original]  
  <sub>anchor: "Small changes to data input can lead to drastically different explanations.2"</sub>
- **descriptive / limitation**: Table 2, limitation 'Inability to generalise': explanations may not hold true when generalised to a broader population or data set; Molnar et al (2020) explain that even for global explainability techniques, under- or overfitting can result in poor model generalisation. (p. 14)[^original]  
  <sub>anchor: "Explanations may not hold true when generalised to a broader population/data set.3"</sub>
- **descriptive / limitation**: Table 2, limitation 'Non-existence of ground truth': there are no universally accepted metrics to assess the correctness or completeness of explanations; Bordt et al (2022) explain that post hoc techniques are not effective in adversarial contexts due to inherent ambiguity, susceptibility to manipulation and inability to provide unique, truthful reasons for algorithmic decisions. (p. 14)[^original]  
  <sub>anchor: "There are no universally accepted metrics to assess the correctness or completeness"</sub>
- **descriptive / limitation**: Table 2, limitation 'Misleading interpretations': misleading explanations can appear plausible; Lakkaraju and Bastani (2020) show that black box models can be manipulated to provide misleading explanations. (p. 14)[^original]  
  <sub>anchor: "Lakkaraju and Bastani (2020) shows how black box models can be manipulated to provide misleading explanations."</sub>
- **descriptive / context**: Retzlaff et al (2024) outline criteria that can be used to compare explainability methods. (p. 14)[^original]  
  <sub>anchor: "Retzlaff et al (2024) outlines criteria that can be used to compare explainability methods."</sub>
- **descriptive / context**: In banking supervision, SHAP can answer which factors contributed most to the credit score of applicants in general; Alonso-Robisco and Carbó (2025) show how to assess the relative reliability of SHAP and Permutation Feature Importance in explaining credit decision predictions of selected AI models. (p. 14)[^original]  
  <sub>anchor: "In the context of banking supervision, SHAP can provide an answer to the question"</sub>
- **descriptive / context**: Buckmann and Joseph (2023) introduce a three-step workflow to make machine learning forecasts interpretable and reveal economically meaningful non-linearities. (p. 14)[^original]  
  <sub>anchor: "introduces a three-step workflow to make machine learning forecasts interpretable"</sub>
- **descriptive / context**: Alonso-Robisco et al (2025) propose constraining a model's internal logic during training to improve both credit prediction performance and interpretability. (p. 14)[^original]  
  <sub>anchor: "Alonso-Robisco et al (2025) proposes constraining a model"</sub>
- **descriptive / context**: New explainability techniques are being developed and existing methods improved, which may prove useful in future to help financial sector regulators better understand AI models used by financial institutions. (p. 14)[^original]  
  <sub>anchor: "may prove useful in the future to assist financial sector regulators in better understanding AI models"</sub>

## 3.2 Challenges in applying existing requirements

- **descriptive / requirement**: An overarching model risk management (MRM) requirement is for an AI model to be explainable with regard to how it arrived at an outcome. (p. 14)[^original]  
  <sub>anchor: "An overarching MRM requirement is for an AI model to be explainable with regard to how it arrived"</sub>
- **descriptive / limitation**: If interpreted strictly, the requirement for explainability of how an outcome was reached may be challenging for certain AI models such as deep learning methods. (p. 14)[^original]  
  <sub>anchor: "If interpreted strictly, this requirement may be challenging for certain AI models such as deep learning methods."</sub>
- **descriptive / limitation**: Deep neural networks have multiple hidden layers with thousands of parameters interacting non-linearly, so it is not possible to conclusively attribute the model output to combinations of the data input. (p. 14)[^original]  
  <sub>anchor: "It is not possible to conclusively attribute the model output to combinations of the data input."</sub>
- **descriptive / limitation**: Complex models such as GPTs that use billions of parameters are another example where existing explainability requirements may not be fit for purpose; Heaven (2023) reports GPT-3 has 175 billion parameters, which are values in a neural network adjusted during training. (p. 14)[^original]  
  <sub>anchor: "has 175 billion parameters, which are values in a neural network that are adjusted during the training process"</sub>
- **descriptive / limitation**: Explainability requirements may need to be tailored to the target audience, for example senior management, consumers or regulators, yet most existing requirements do not make such a differentiation. (p. 14)[^original]  
  <sub>anchor: "explainability requirements may need to be tailored to the target audience, for example senior management, consumers or regulators.43"</sub>
- **descriptive / context**: IAIS (2025) discusses tailoring explanations of AI outputs to different stakeholders; Davis et al (2022) analyse the explainability of machine learning consumer credit risk models for loan companies, regulators, loan applicants and data scientists. (p. 14)[^original]  
  <sub>anchor: "IAIS (2025) discusses tailoring explanations of AI outputs to different stakeholders."</sub>
- **descriptive / context**: FINMA (2024) mentions that where decisions had to be justified to investors, clients, employees, the supervisory authority or the audit firm, it assessed the explainability of the applications in greater depth, including understanding the drivers of the applications or their behaviour under different conditions to assess the plausibility and robustness of results. (p. 14)[^original]  
  <sub>anchor: "FINMA assessed the explainability of the applications in greater depth."</sub>
- **descriptive / limitation**: Some MRM requirements specify model change processes that firms need to follow, but it is unclear what constitutes a change for AI models. (p. 14)[^original]  
  <sub>anchor: "it is unclear what constitutes a change when it comes to AI models"</sub>
- **expected / expectation**: Because it is unclear what counts as a change for AI models, the paper says it would be necessary to specify what constitutes a model change for AI models; it cites Bank of England (2025) on complex AI models that may update themselves automatically as new data arrive. (p. 14)[^original]  
  <sub>anchor: "It would be necessary to specify what constitutes a model change for AI models."</sub>
- **descriptive / limitation**: The use of AI models provided by third-party providers poses multiple challenges in observing MRM requirements. (p. 15)[^original]  
  <sub>anchor: "The use of AI models provided by third-party providers poses multiple challenges in observing MRM requirements.44"</sub>
- **descriptive / limitation**: In certain jurisdictions firms are required to engage independent third parties to undertake model validation; for proprietary models licensed from third parties this may be challenging because providers may be reluctant to explain how their model works or is trained for proprietary reasons. (p. 15)[^original]  
  <sub>anchor: "In certain jurisdictions, firms are required to engage independent third parties to undertake model validation."</sub>
- **descriptive / limitation**: For LLMs, firms generally have neither the financial nor the computational resources to develop their own models, so the third-party validation difficulty is observed in this area. (p. 15)[^original]  
  <sub>anchor: "firms generally have neither the financial nor the computational resources to develop their own models.45"</sub>
- **descriptive / context**: In the EU the third-party transparency problem is somewhat mitigated by the Code of Practice for model developers/providers, whose first chapter covers transparency and includes a model documentation form setting out the information providers need to share. (p. 15)[^original]  
  <sub>anchor: "In the EU, this is somehow mitigated by the Code of Practice for model developers/providers."</sub>
- **descriptive / context**: MAS (2024) highlights that, unlike conventional AI trained for specific use cases, generative AI is more general-purpose and can be used in a wider range of use cases in the bank. (p. 15)[^original]  
  <sub>anchor: "is more general-purpose in nature and can be used in a wider range of use cases in the bank"</sub>
- **descriptive / limitation**: In some newer GenAI use cases it might be difficult to find readily available ground truths for evaluating and testing GenAI models. (p. 15)[^original]  
  <sub>anchor: "it might be difficult to find readily available ground truths for evaluating and testing GenAI models"</sub>
- **descriptive / limitation**: The lack of established or globally accepted explainability methods, especially for newer forms of AI models, is a barrier to meeting MRM guidelines. (p. 15)[^original]  
  <sub>anchor: "The lack of established or globally accepted explainability methods, especially for newer forms of AI models, is a barrier"</sub>
- **descriptive / finding or result**: MAS (2024) observes a general lack of established methods for explaining GenAI outputs and assessing their fairness. (p. 15)[^original]  
  <sub>anchor: "there is a general lack of established methods for explaining GenAI outputs and assessing their fairness"</sub>
- **descriptive / context**: A footnote records that OSFI and Global Risk Institute (2023) set out four factors for deciding the right level of explainability: what has to be explained, who the audience is, how material the use case is, and how complex the model is. (p. 15)[^original]  
  <sub>anchor: "what needs to be explained, target audience, materiality of the use case and complexity of the model"</sub>
- **descriptive / context**: A footnote reports MAS (2024) as stating that external model providers' lack of transparency may add to the difficulty of understanding and explaining GenAI outputs and behaviour. (p. 15)[^original]  
  <sub>anchor: "the lack of transparency of external model providers may contribute to challenges in understanding and explaining the outputs"</sub>

## Explainability of large language models

- **descriptive / context**: Financial institutions are increasingly using LLMs across many activities, from information search and summarisation to generating client or management reports. (p. 16)[^original]  
  <sub>anchor: "Large language models (LLMs) are increasingly being used by financial institutions across many activities"</sub>
- **descriptive / context**: LLMs are very powerful because their underlying foundation models are trained on massive data sets. (p. 16)[^original]  
  <sub>anchor: "their underlying foundation models are trained on massive data sets"</sub>
- **descriptive / context**: A growing number of users have admiration and confidence in LLMs despite not knowing exactly how the models work. (p. 16)[^original]  
  <sub>anchor: "despite the fact that they do not know exactly how the models work"</sub>
- **descriptive / limitation**: Explaining and understanding LLMs is an extremely complex task because of the many parameters and non-linear relationships involved. (p. 16)[^original]  
  <sub>anchor: "explaining and understanding LLMs is an extremely complex task due to the many parameters"</sub>
- **descriptive / method**: Ameisen et al (2025) use attribution graphs on Anthropic's Claude 3.5 Haiku, which aim to partially trace the chain of intermediate steps the model uses to transform a specific input prompt into an output response. (p. 16)[^original]  
  <sub>anchor: "using attribution graphs, which aim to partially trace the chain of intermediate steps that the model uses"</sub>
- **descriptive / method**: Chain-of-thought (CoT) prompting, first coined by Wei et al (2023), originally referred to humans detailing their reasoning process in the prompt, giving the model reasoning steps to use as an example for other tasks, mimicking structured human reasoning to improve performance. (p. 16)[^original]  
  <sub>anchor: "chain-of-thought (CoT) prompting, first coined by Wei et al (2023)"</sub>
- **descriptive / limitation**: CoT prompts are interpretable, but how LLMs use them is not. (p. 16)[^original]  
  <sub>anchor: "These prompts are interpretable; however, how LLMs use them is not."</sub>
- **descriptive / limitation**: Explanations generated by newer-generation reasoning models may appear to mimic human reasoning but do not necessarily reflect how the models actually arrive at their conclusions. (p. 16)[^original]  
  <sub>anchor: "they do not necessarily reflect how the models actually arrive at their conclusions"</sub>
- **descriptive / limitation**: Producing an appealing explanation does not guarantee that it represents the model's internal reasoning process. (p. 16)[^original]  
  <sub>anchor: "producing an appealing explanation does not guarantee that it represents the model"</sub>
- **descriptive / context**: Depending on the use case, it may become more of a regulatory concern if firms cannot fully explain how LLM-based applications work, and this problem will not go away soon because firms may never know how foundation models were trained, including the data used. (p. 16)[^original]  
  <sub>anchor: "it may become more of a regulatory concern if they are unable to fully explain how the applications work"</sub>
- **descriptive / context**: OpenAI states its reasoning models are LLMs trained with reinforcement learning to perform reasoning, producing an internal chain of thought before responding and considering multiple approaches to generating a response. (p. 16)[^original]  
  <sub>anchor: "OpenAI states that its reasoning models are LLMs trained with reinforcement learning to perform reasoning"</sub>

## Section 4 – Potential adjustments to MRM guidelines

- **expected / expectation**: MRM guidelines do not need to be technology-specific, but they do need to be regularly updated to reflect issues associated with newer technologies, which is especially important as use of models with advanced technologies becomes more prevalent. (p. 16)[^original]  
  <sub>anchor: "MRM guidelines do not need to be technology-specific, but they do need to be regularly updated"</sub>
- **permissive / recommendation**: In principle, where AI models are used for decisions in critical activities, MRM guidelines could require financial institutions to use inherently explainable AI models or at least adopt sufficiently informative explainability techniques for black box models. (p. 16)[^original]  
  <sub>anchor: "MRM guidelines could require financial institutions to use inherently explainable AI models46 or at least adopt sufficiently"</sub>
- **descriptive / limitation**: For complex models, using just one existing explainability method may not be fully informative, so it may be necessary to require a suite of methods to address the differing needs of stakeholders. (p. 16)[^original]  
  <sub>anchor: "it may be necessary to require a suite of methods to address the differing needs of stakeholders"</sub>
- **descriptive / finding or result**: Stocktakes, surveys and thematic reviews by the private and public sectors show financial institutions use several explainability techniques to better understand complex AI models (see EBA (2023), Bank of England and FCA (2024), MAS (2024) and IIF-EY (2025)). (p. 16)[^original]  
  <sub>anchor: "financial institutions are using several explainability techniques to better understand complex AI models.47"</sub>
- **permissive / recommendation**: MRM guidelines may need to require financial institutions to establish acceptable explainability standards for relevant use cases. (p. 16)[^original]  
  <sub>anchor: "MRM guidelines may need to require financial institutions to establish acceptable explainability standards for relevant use cases."</sub>
- **expected / expectation**: Firms' model documentation, including validation reports, should include information on how the explainability of AI models used in high-impact cases has been addressed. (p. 16)[^original]  
  <sub>anchor: "including validation reports, should include information on how the explainability of AI models used in high-impact cases"</sub>
- **expected / expectation**: The information provided in model documentation should enable supervisors to assess why a model has made specific predictions. (p. 16)[^original]  
  <sub>anchor: "The information provided should enable supervisors to assess why a model has made specific predictions."</sub>
- **descriptive / context**: Graph 1 illustrates the different levels of explainability a supervisor might require, depending on the criticality of a specific use case and the complexity of the model. (p. 16)[^original]  
  <sub>anchor: "Graph 1 illustrates the different levels of explainability that a supervisor might require"</sub>
- **recommended / recommendation**: Tailoring regulatory explainability requirements to the different levels of riskiness of AI use cases could be considered. (p. 16)[^original]  
  <sub>anchor: "tailoring regulatory explainability requirements to the different levels of riskiness of AI use cases could be considered"</sub>
- **descriptive / context**: Tiering or rating of models based on riskiness, already required in existing MRM guidelines, can be used to identify use cases where explainability is more relevant, and banks, other financial institutions and authorities are already starting to do this (see OCC (2021), MAS (2024), FINMA (2024), EIOPA (2025)). (p. 16)[^original]  
  <sub>anchor: "Tiering or rating of models based on their riskiness, which is already required in existing MRM guidelines"</sub>
- **permissive / recommendation**: In light of the preceding discussion, authorities may need to review their existing MRM guidelines and decide whether new guidelines, or adjustments to existing ones, are required to keep them relevant in the age of AI. (p. 16)[^original]  
  <sub>anchor: "authorities may need to review existing MRM guidelines and determine whether new guidelines or adjustments to existing ones"</sub>
- **permissive / recommendation**: As financial institutions extend AI models to more functions and business areas, financial authorities may need to issue guidance on model use that goes beyond regulatory capital purposes. (p. 16)[^original]  
  <sub>anchor: "financial authorities may need to provide guidance on the use of models beyond regulatory capital purposes"</sub>
- **descriptive / context**: The paper states that clear AI guidance gives regulatory certainty and can help support safe and sound use of models while protecting consumer interests. (p. 16)[^original]  
  <sub>anchor: "Clear AI guidance provides regulatory certainty and can help support the use of models in a safe and sound manner"</sub>
- **expected / expectation**: The paper cites OCC (2021) as requiring that, for models that may be hard to assess for conceptual soundness, a determination should be made on whether the degree of explainability suits how the specific model is used. (p. 16)[^original]  
  <sub>anchor: "a determination should be made as to whether the level of explainability is appropriate to the specific model’s use"</sub>
- **descriptive / context**: AI use cases subject to higher standards of explainability are typically those resulting in decisions that likely require explanations to external stakeholders such as regulators and customers. (p. 17)[^original]  
  <sub>anchor: "AI use cases that are subject to higher standards of explainability are those that result in decisions"</sub>
- **descriptive / context**: AI use cases subject to higher explainability standards also include those for which inaccurate model outputs can have significant (financial) implications. (p. 17)[^original]  
  <sub>anchor: "or those for which inaccurate model outputs can have significant (financial) implications."</sub>
- **expected / expectation**: There should be explicit recognition of possible trade-offs between explainability and model performance. (p. 17)[^original]  
  <sub>anchor: "There should be explicit recognition of possible trade-offs between explainability and model performance."</sub>
- **expected / expectation**: Improved performance from complex models should be weighed against the consequences of insufficient explainability; OSFI and Global Risk Institute (2023) offer an alternative view that complex models may not always yield more accurate predictive performance than interpretable models. (p. 17)[^original]  
  <sub>anchor: "Complex models may bring improved performance, which should be weighed against the consequences of insufficient explainability.49"</sub>
- **permissive / recommendation**: The balance between performance and explainability could be achieved by requiring developers to justify selecting a complex model over a simpler one, which could involve showing the extent of performance improvement relative to challenger models in a variety of scenarios entailing substantially different model inputs. (p. 17)[^original]  
  <sub>anchor: "by requiring developers to justify the selection of a complex model over a simpler one."</sub>
- **permissive / recommendation**: A more consequential approach would be to allow the use of complex models that do not fully meet established explainability standards but whose performance is unambiguously and significantly better than that of more traditional and simpler models. (p. 17)[^original]  
  <sub>anchor: "allow the use of complex models that do not fully meet the established explainability standards"</sub>
- **expected / expectation**: Explainability waivers should imply the application of sufficient safeguards. (p. 17)[^original]  
  <sub>anchor: "it should imply the application of sufficient safeguards"</sub>
- **permissive / recommendation**: As safeguards for waivers, frequent stability/repeatability testing, also by third parties, and ongoing monitoring of model outputs could be required to ascertain whether outputs remain consistent under varying conditions. (p. 17)[^original]  
  <sub>anchor: "frequent stability/repeatability testing,50 also by third parties, and ongoing monitoring of model outputs could be required"</sub>
- **permissive / recommendation**: Alternative enhanced risk management measures, data governance and human oversight may be required to compensate for insufficient explainability. (p. 17)[^original]  
  <sub>anchor: "alternative enhanced risk management measures, data governance and human oversight may be required to compensate for insufficient explainability.51"</sub>
- **permissive / recommendation**: Firms can disclose how they adjust complex AI models to make model outputs more reliable; for LLMs such adjustments include fine-tuning pre-trained models with use-case-relevant data or using retrieval-augmented generation to feed relevant documents or information and confine the output to that information. (p. 17)[^original]  
  <sub>anchor: "Firms can disclose how they adjust complex AI models to make model outputs more reliable.52"</sub>
- **permissive / recommendation**: Circuit breakers can act as automated mechanisms to halt model use in extreme or unexpected scenarios, providing protection against adverse outcomes. (p. 17)[^original]  
  <sub>anchor: "circuit breakers can act as automated mechanisms to halt model use in extreme or unexpected scenarios"</sub>
- **recommended / recommendation**: Citing EBA (2023), the paper suggests a possible first step on the performance versus explainability trade-off: ask financial institutions to strike an appropriate balance between model performance and explainability by avoiding needless complexity. (p. 17)[^original]  
  <sub>anchor: "to ask financial institutions to find an appropriate balance between model performance and explainability results"</sub>
- **expected / expectation**: Any explainability waivers should apply only to AI models with a limited explainability gap, taking into account how risky the use of those models is. (p. 17)[^original]  
  <sub>anchor: "the introduction of explainability waivers should only affect AI models whose explainability gap is limited"</sub>
- **permissive / recommendation**: For use cases that could significantly affect an institution's safety and soundness or consumers' interests, MRM guidelines could require banks to be prepared to stop using the models quickly once relevant performance flaws are found. (p. 17)[^original]  
  <sub>anchor: "MRM guidelines could require banks to be ready to rapidly cease the use of those models as soon as relevant"</sub>
- **descriptive / limitation**: Addressing low explainability of AI models used for regulatory purposes is trickier, because complex AI models may fail to meet existing MRM guidelines, including those for regulatory use. (p. 18)[^original]  
  <sub>anchor: "Addressing the low explainability of AI models used for regulatory purposes is trickier."</sub>
- **descriptive / context**: The use of AI models for regulatory purposes could be disallowed, but this removes incentives for financial institutions to use potentially good performing models for risk management and could hamper development of such AI use cases. (p. 18)[^original]  
  <sub>anchor: "this removes incentives for financial institutions to use potentially good performing models for risk management"</sub>
- **permissive / recommendation**: A compromise might be that well performing complex AI models could be allowed to a limited degree for calculating provisions, minimum capital or other regulatory obligations. (p. 18)[^original]  
  <sub>anchor: "for the calculation of provisions, minimum capital or other regulatory obligations could be allowed to a limited degree"</sub>
- **permissive / recommendation**: Such complex models could be allowed only for certain risk categories and exposures. (p. 18)[^original]  
  <sub>anchor: "such models will only be allowed for certain risk categories and exposures"</sub>
- **permissive / recommendation**: Alternatively, risk weights calculated using such complex models could be subject to a more stringent output floor than that currently envisaged in Basel III for more traditional internal models. (p. 18)[^original]  
  <sub>anchor: "the risk weights calculated using such models will be subject to a more stringent output floor"</sub>

## Section 5 – Conclusion

- **descriptive / context**: AI use is expected to become more prevalent across financial institutions' business activities and could spread from internal productivity purposes to critical business areas. (p. 19)[^original]  
  <sub>anchor: "could also spread to critical business areas of financial institutions"</sub>
- **expected / expectation**: Financial authorities need to be attuned to the potential implications of AI use for both the risks facing individual financial institutions and the risks facing the entire financial system. (p. 19)[^original]  
  <sub>anchor: "Financial authorities therefore need to be attuned to the potential implications of the use of AI"</sub>
- **descriptive / context**: The lack of explainability of certain AI models is a key concern for financial authorities. (p. 19)[^original]  
  <sub>anchor: "The lack of explainability of certain AI models is a key concern for financial authorities."</sub>
- **descriptive / limitation**: Available explainability techniques have limitations when applied to more complex AI models such as LLMs, and rollout of complex models in critical business areas has implications for consumers, regulatory compliance and systemic risk, heightening financial institutions' model risks. (p. 19)[^original]  
  <sub>anchor: "these have limitations when applied to more complex AI models such as LLMs"</sub>
- **expected / expectation**: Specific attention is needed for closed source, proprietary models, including many LLMs whose foundation models are not transparent. (p. 19)[^original]  
  <sub>anchor: "Specific attention is needed for closed source, proprietary models, including many LLMs for which the foundation models are not transparent."</sub>
- **descriptive / limitation**: Firms using LLMs do not know how the foundation models were trained, and this lack of explainability may limit use cases to low-risk activities. (p. 19)[^original]  
  <sub>anchor: "this lack of explainability may limit use cases to low-risk activities"</sub>
- **expected / expectation**: It is imperative that financial authorities seek to foster sound MRM practices in financial institutions that take into account AI developments, which authorities can do through MRM guidelines. (p. 19)[^original]  
  <sub>anchor: "It is therefore imperative that financial authorities seek to foster sound MRM practices"</sub>
- **descriptive / recommendation**: Authorities can foster sound MRM practices through MRM guidelines that, as item (1), address the use of models more broadly in financial institutions, not just for regulatory purposes. (p. 19)[^original]  
  <sub>anchor: "(1) address the use of models more broadly in financial institutions, ie not just for regulatory purposes;"</sub>
- **descriptive / recommendation**: Authorities can issue MRM guidelines that, as item (2), recognise that models used or to be used by financial institutions have evolved to include those that use AI. (p. 19)[^original]  
  <sub>anchor: "recognise that models used or that will be used by financial institutions have evolved to include"</sub>
- **descriptive / recommendation**: Authorities can issue MRM guidelines that, as item (3), reflect industry practices and adapt as these evolve. (p. 19)[^original]  
  <sub>anchor: "reflect industry practices and adapt as these evolve."</sub>
- **permissive / recommendation**: For AI explainability, MRM guidelines could include requiring financial institutions to employ explainability techniques to explain black box models. (p. 19)[^original]  
  <sub>anchor: "MRM guidelines could include requiring financial institutions to employ explainability techniques to explain black box models"</sub>
- **permissive / recommendation**: MRM guidelines could include establishing explainability standards based on the potential impact and riskiness of the model. (p. 19)[^original]  
  <sub>anchor: "establishing explainability standards based on the potential impact and riskiness of the model"</sub>
- **permissive / recommendation**: MRM guidelines could include requiring complementary safeguards such as enhanced data governance and human oversight to mitigate risks of using complex AI models in critical business areas. (p. 19)[^original]  
  <sub>anchor: "requiring complementary safeguards such as enhanced data governance and human oversight"</sub>
- **permissive / recommendation**: Some conditional and constrained flexibility in applying explainability requirements could be envisaged for models with robustly proven good performance. (p. 19)[^original]  
  <sub>anchor: "conditional and constrained flexibility in the application of explainability requirements for models with robustly proven good performance"</sub>
- **expected / expectation**: Authorities will need to upskill their staff to be able to understand explainability submissions by firms, which is no trivial task as even inherently interpretable models may be challenging to understand, let alone explainability techniques for black box models. (p. 19)[^original]  
  <sub>anchor: "Authorities will also need to upskill their staff to be able to understand explainability submissions by firms."</sub>
- **permissive / recommendation**: The conclusion says there may be a need to accept trade-offs between explainability and model performance, provided the risks are properly assessed and effectively managed. (p. 19)[^original]  
  <sub>anchor: "there may be a need to recognise trade-offs between explainability and model performance, so long as"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Bank for International Settlements / Basel Committee, "Managing explanations: how regulators can address AI explainability" (2025-09-08). https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
