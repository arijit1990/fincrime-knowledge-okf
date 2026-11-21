---
type: Source Digest
title: DP5/22 - Artificial Intelligence and Machine Learning - part 2 of 4 (p. 1)
description: 'Verified paraphrased digest, p. 1: DP5/22 - Artificial Intelligence and Machine Learning > 2. Supervisory authorities’ objectives and remits; DP5/22 - Artificial Intelligence and Machine Learning > 3. Potential benefits and risks; DP5/22 - Artificial Intelligence and Machine Learning > 4. Regulation'
resource: https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence
tags:
- consultation
- data_governance
- explainability
- hypothesis
- model_governance
- responsible_ai
- uk
status: stable
source_id: pra-boe-dp5-22-artificial-intelligence-and-machine-learning
issuer: pra_boe
issuer_name: Prudential Regulation Authority / Bank of England
jurisdictions:
- UK
tier: 1
instrument_type: consultation
normative_force: hypothesis
publication_date: '2026-10-01'
legal_status: consultation
part: 2
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T13:42:23Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T13:42:23Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T13:42:23Z'
sources:
- id: original
  resource: https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence
  title: DP5/22 - Artificial Intelligence and Machine Learning
  author: org:pra_boe
  last_modified: '2026-10-01T00:00:00Z'
digest_points: 56
---

# DP5/22 - Artificial Intelligence and Machine Learning (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **hypothesis**.

## What is AI?

- **descriptive / definition**: Paragraph 2.10: while there is no consensus on a single definition, AI is generally accepted to be the simulation of human intelligence by machines, including computer systems able to perform tasks demonstrating learning, decision-making, problem solving and other tasks that previously required human intelligence; machine learning is a sub-branch of AI, and AI is broadly seen as part of a spectrum of computational and mathematical methodologies including innovative data analytics and modelling techniques. (p. 1)[^original]  
  <sub>anchor: "While there is no consensus on a single definition, it is generally accepted that AI is the simulation"</sub>
- **descriptive / definition**: Paragraph 2.12: it is important to distinguish 'algorithm' from 'model' as they have specific meanings in financial services regulation; the CMA defines 'algorithmic systems' as shorthand for an automated system at the intersection of algorithms, data, models, processes, objectives and people, the authorities define 'algorithmic trading' for MiFID implementation, DRCF members define 'algorithmic processing', and the PRA defines 'model' in CP6/22 'Model risk management principles for banks'. Algorithms and models may be components of an AI system but may not in themselves necessarily be deemed to be AI. (p. 1)[^original]  
  <sub>anchor: "while both algorithms and models may be components of an AI system, they may not in themselves"</sub>
- **descriptive / context**: Paragraph 2.13: many AI-related issues are not new and apply to other analytics and modelling techniques; many traditional financial models not using AI, such as generalized linear models (GLM) used to classify insurance risk and internal ratings based (IRB) approaches to regulatory capital, may be as complex and difficult to understand or explain. (p. 1)[^original]  
  <sub>anchor: "Many of the issues related to AI are not new and apply to other data analytics, modelling techniques, and technologies."</sub>
- **descriptive / context**: Paragraph 2.14: three key areas in the AI lifecycle (Figure 1, source AIPPF) can introduce novel challenges and increase existing risks. (p. 1)[^original]  
  <sub>anchor: "there are three key areas in the AI lifecycle (see Figure 1 below) that can introduce novel challenges"</sub>
- **descriptive / typology or red flag**: Paragraph 2.15 (data): AI can analyse traditional data sources and also unstructured and alternative data such as image and text data; the greater volume and variety of data formats places added emphasis on data quality, and because AI may pick up bias in datasets and may not perform as intended when exposed to issues excluded from training/testing data, new data quality metrics such as representativeness and completeness may be needed. (p. 1)[^original]  
  <sub>anchor: "new data quality metrics like representativeness and completeness may be needed"</sub>
- **descriptive / typology or red flag**: Paragraph 2.16 (model): traditional financial models are usually rules-based with explicit fixed parameterisation, whereas AI models can learn the rules and alter parameterisation iteratively; AI models are a step change also because of the speed and frequency of updating (some learn continuously), the scale of data needed to train them and number of input features, and the complexity of certain techniques such as convolutional neural networks, which can make them opaque (the 'black box problem'). (p. 1)[^original]  
  <sub>anchor: "AI models are able to learn the rules and alter model parameterisation iteratively"</sub>
- **descriptive / typology or red flag**: Paragraph 2.17 (governance): AI may pose novel governance challenges, especially where used for autonomous decision-making that may limit or even eliminate human judgement and oversight; a lack of explainability or transparency in some AI models may mean extra care or actions are needed to ensure full accountability and sufficient oversight. (p. 1)[^original]  
  <sub>anchor: "may mean extra care or actions are needed to ensure full accountability and sufficient oversight"</sub>
- **descriptive / context**: Paragraph 2.18: regulators have generally distinguished AI from non-AI either by a more precise legal definition (e.g. 'artificial intelligence system' in the proposed European AI regulation and the proposed Canadian AI and Data Act), or by viewing AI as part of a wider spectrum of analytical techniques, possibly with a classification scheme or mapping of AI characteristics (e.g. the German financial regulators' consultation paper on machine learning in risk models, the OECD Classification System, the UK government's proposed framework). (p. 1)[^original]  
  <sub>anchor: "viewing AI as part of a wider spectrum of analytical techniques with a range of elements and characteristics"</sub>
- **descriptive / context**: Paragraph 2.19: each approach aims to clarify what constitutes AI within a regulatory regime, and so what restrictions and requirements may apply; depending on the requirements, this may help consumers understand where AI is used, firms use AI responsibly and manage trade-offs, and regulators assess whether firms use AI safely and responsibly with appropriate controls. (p. 1)[^original]  
  <sub>anchor: "firms to use the technology responsibly and manage the relevant trade-offs"</sub>
- **descriptive / context**: Paragraph 2.20: benefits of a more precise AI definition in the authorities' rulebooks may include a common language for firms and regulators that may ease uncertainty, a more uniform and harmonised regulatory response, and a basis for identifying whether use cases are captured by particular rules and principles. (p. 1)[^original]  
  <sub>anchor: "creating a common language for firms and regulators, which may ease uncertainty"</sub>
- **descriptive / limitation**: Paragraph 2.21: challenges of a more precise regulatory AI definition include the difficulty of a robust definition that stays relevant in a fast-developing field; a too-broad definition lacking specificity, precision and proportionality; potential for some use cases, products and services to fall outside scope when they should not; and creating ability and incentives for firms to misclassify AI to reduce regulatory oversight. The alternative approaches may address some of these challenges and could potentially be more suitable for UK financial services. (p. 1)[^original]  
  <sub>anchor: "creating the ability and incentives for firms to misclassify AI to reduce regulatory oversight"</sub>

## How AI is used in financial services

- **descriptive / finding or result**: Paragraph 2.23 trend 1: greater AI adoption is occurring in established firms and in newer fintech and insurtech companies, powered by improved software and hardware, greater use of cloud computing often provided via third parties, and partnerships and investment with smaller AI-specific vendors. (p. 1)[^original]  
  <sub>anchor: "Greater AI adoption is occurring both within established financial services firms and also newer fintech and insurtech companies."</sub>
- **descriptive / finding or result**: Paragraph 2.23 trend 2: firms are using AI for more material business areas and use cases, ranging from anti-money laundering (AML) functions and credit and regulatory capital modelling in banking, to claims management, product pricing and capital reserve modelling in insurance, to order routing, execution and generating trading signals in investment management. (p. 1)[^original]  
  <sub>anchor: "From anti-money laundering (AML) functions and credit and regulatory capital modelling in banking"</sub>
- **descriptive / finding or result**: Paragraph 2.23 trend 3: firms are using more complex AI techniques because complexity often corresponds to improved performance and use of greater volumes of data; as they apply more complex methods, data sets and use cases they will likely become more comfortable and adoption of even more complex techniques will increase further. (p. 1)[^original]  
  <sub>anchor: "complexity often corresponds to improved performance and use of ever greater volumes of data"</sub>
- **descriptive / context**: Paragraph 2.24 refers readers to the authorities' report Machine Learning in UK Financial Services 2022 (2022 ML Survey) for more detail. (p. 1)[^original]  
  <sub>anchor: "recent report on Machine Learning in UK Financial Services 2022 (2022 ML Survey)"</sub>

## Box 3: The supervisory authorities’ use of AI

- **descriptive / context**: The supervisory authorities use AI where appropriate to support their capabilities; RegTech is the use of technology by firms to help fulfil regulatory obligations and SupTech is the use of technology by regulators to facilitate supervisory duties; AI may also support central bank functions such as economic analysis. (p. 1)[^original]  
  <sub>anchor: "SupTech, which refers to the use of technology by regulators to facilitate their supervisory duties"</sub>
- **descriptive / case example**: The Bank uses AI for predictive analytics, study of non-linear interactions and analysis of larger datasets, which can help forecast GDP growth, bank distress and financial crises, and is exploring AI text analysis of newspapers and 'faster indicators' for real-time economic analysis; the PRA introduced a cognitive search tool with AI capabilities that extracts key patterns from unstructured and complex firm management information and is developing other AI tools. (p. 1)[^original]  
  <sub>anchor: "The PRA successfully introduced a cognitive search tool with AI capabilities"</sub>
- **descriptive / case example**: The FCA is exploring AI for additional insight, including Natural Language Processing on unstructured text documentation, predictive analytics to forecast where risks may lie across its supervisory waterfront, and simulation techniques to generate realistic synthetic data sets; the potential for AI to assist regulators depends significantly on access to data and technology, which may have implications for the data firms are required to share. (p. 1)[^original]  
  <sub>anchor: "simulation techniques to generate realistic synthetic data sets"</sub>

## Questions: Supervisory authorities’ objectives and remits

- **descriptive / context**: Question Q1 asks whether a sectoral regulatory definition of AI in the authorities' rulebooks, underpinning specific rules and requirements, would help UK financial services firms adopt AI safely and responsibly, and if so what the definition should be; Q2 asks whether there are equally effective approaches not relying on a definition and which are most suitable. (p. 1)[^original]  
  <sub>anchor: "Would a sectoral regulatory definition of AI, included in the supervisory authorities’ rulebooks"</sub>
- **descriptive / context**: Paragraph 3.1: Chapter 3 summarises potential benefits and risks of AI in financial services and how drivers of AI benefits and risks can occur at different levels within AI systems (data, models and governance) and result in a range of outcomes depending on how the system is used. (p. 1)[^original]  
  <sub>anchor: "the drivers of AI benefits and risks in financial services can occur at different levels within AI systems"</sub>

## 3. Potential benefits and risks

- **descriptive / context**: Paragraph 3.2: benefits and risks are divided by the supervisory authorities' objectives: consumer protection, competition, safety and soundness of firms, insurance policyholder protection, financial stability and market integrity. (p. 1)[^original]  
  <sub>anchor: "namely consumer protection, competition, safety and soundness of firms, insurance policyholder protection, financial stability, and market integrity"</sub>
- **descriptive / limitation**: Paragraph 3.3: the benefits, risks and harms discussed are neither exhaustive nor applicable to every AI use case, and while many are neither new nor unique to AI, AI use may amplify existing risks and introduce novel challenges. (p. 1)[^original]  
  <sub>anchor: "the use of AI in financial services may amplify existing risks and introduce novel challenges"</sub>
- **descriptive / finding or result**: Paragraph 3.4: previous work shows AI risk drivers occur at different levels (Figure 1), starting with risks from the use of data to train, test and run models, which feed into risks from model design and use, which in turn challenge the governance structures needed to manage those risks. (p. 1)[^original]  
  <sub>anchor: "starting with the risks associated with the use of data to train, test, and run AI models"</sub>
- **descriptive / typology or red flag**: Paragraph 3.5 (data risk drivers): because AI relies on large volumes of data for training, testing and implementation, drivers of data risk include errors in training data, incomplete or unrepresentative data, significant outliers or noise, historical data biases and insufficient data; poor data preparation, validation and management can also be drivers. (p. 1)[^original]  
  <sub>anchor: "errors in the training data, incomplete or unrepresentative data, significant outliers or noise, historical data biases, insufficient data"</sub>
- **descriptive / typology or red flag**: Paragraph 3.6 (model risk drivers): poor AI model performance may come from data risks or model risks such as inappropriate model choices, errors in design or construction, lack of explainability, unexpected behaviour, unintended consequences, degradation in performance, and model or concept drift; poor model risk management (validation, change management, monitoring) can also be a driver, and the extent to which poor performance leads to poor outcomes can depend on the model's degree of autonomy. (p. 1)[^original]  
  <sub>anchor: "inappropriate model choices, errors in the model design or construction, lack of explainability, unexpected behaviour"</sub>
- **descriptive / typology or red flag**: Paragraph 3.7 (governance risk drivers): drivers can include absence of clearly defined roles and responsibilities for AI, insufficient skillsets, governance functions that do not include relevant business areas or consider relevant risks (such as ethical risks), lack of challenge at board and executive level, and general lack of accountability. (p. 1)[^original]  
  <sub>anchor: "the absence of clearly defined roles and responsibilities for AI, insufficient skillsets"</sub>
- **descriptive / context**: Paragraph 3.8: if risk drivers are mitigated AI may deliver benefits (high-quality data, appropriate model choices and good governance can give a well-performing system and accurate outputs); benefits and risks depend on context and purpose, e.g. data quality issues in a consumer-facing system are likely to relate to consumer protection, whereas in an AI trading system they are likely to relate to firms' safety and soundness and potentially financial stability. (p. 1)[^original]  
  <sub>anchor: "both the benefits and risks that AI deliver are dependent on the context in which it is used"</sub>

## Consumer protection – FCA

- **descriptive / finding or result**: Paragraph 3.9: AI can use large volumes of data to identify consumer characteristics and preferences, with uses from providing access to consumers with non-standard histories, identifying vulnerability and better product matching; a more granular understanding may also make it easier to identify and exploit behavioural biases and vulnerability, from exploiting inertia to harmful price discrimination, and whether AI benefits consumers depends on how and for what purpose it is used. (p. 1)[^original]  
  <sub>anchor: "from exploiting inertia, to harmful price discrimination, to exploiting actual characteristics of vulnerability"</sub>
- **descriptive / typology or red flag**: Paragraph 3.10: AI use could be associated with discriminatory decisions; bias related to protected characteristics such as race or sex could arise inadvertently in model development because, even if those variables are excluded, they may be correlated with other data points; bias can come from historical biases in training data (e.g. certain groups less able to access credit) or an unrepresentative dataset, and models can amplify historical biases in input data. (p. 1)[^original]  
  <sub>anchor: "even if these variables are excluded from the model, they could still be correlated from other data points"</sub>
- **descriptive / typology or red flag**: Paragraph 3.11: AI applications could exclude certain consumers; AI-based insurance screening or credit provision could enable greater segmentation between 'low-risk' and 'high-risk' groups, affecting risk pooling and possibly leading providers to exclude or offer unaffordable premiums to high-risk consumers, and personalisation such as individual pricing could lead to products not being offered to some groups, potentially resulting in unlawful discrimination based on protected characteristics. (p. 1)[^original]  
  <sub>anchor: "could lead providers to exclude or offer unaffordable premiums to ‘high-risk’ consumers"</sub>

## Competition – FCA

- **descriptive / finding or result**: Paragraph 3.12: consumer-facing AI systems such as those used in Open Banking might improve competition by improving consumers' ability to assess, access and act on information; Open Banking lets third parties access transaction data with explicit consent in a secured environment, and AI systems can remove some of the sellers' informational advantage over buyers in markets with complex financial products. (p. 1)[^original]  
  <sub>anchor: "Open Banking enables third parties to access consumers’ transaction data (with their explicit consent)"</sub>
- **descriptive / finding or result**: Paragraph 3.14: where AI is particularly relevant to a business's practice, costs of entry (staff and skills, data and technology) may rise to a level that limits market entry, with potentially harmful effects on competition; the CMA published 'Algorithms: How they can reduce competition and harm consumers' and a call for information in January 2021. (p. 1)[^original]  
  <sub>anchor: "the costs of entry (including both the staff and skills, as well as the data"</sub>

## Safety and soundness – PRA and FCA

- **descriptive / finding or result**: Paragraph 3.15: AI can help firms create better decision-making tools, insights and products, largely due to uplift in predictive power, more granular classification and segmentation, ability to capture non-linear relationships and ability to analyse larger volumes of data and new sources such as unstructured and alternative data. (p. 1)[^original]  
  <sub>anchor: "the uplift in predictive power, more granular classification and segmentation"</sub>
- **descriptive / finding or result**: Paragraph 3.16: firms already benefit from AI through improved operational efficiency, reducing costs and processing times; AI models can also be more accurate in predicting default risk for consumer and corporate credit, and improved probability of default estimates could lead to more appropriate modelling of regulatory capital. (p. 1)[^original]  
  <sub>anchor: "AI models can also be more accurate in predicting default risk for consumer and corporate credit"</sub>
- **descriptive / typology or red flag**: Paragraph 3.17: AI challenges may amplify prudential risks (credit, liquidity, market, operational, reputational etc.); for example, in credit risk, accuracy or consistency errors in the dataset will likely affect the AI model's ability to quantify probability of default and risk of loss, which could lead to inaccurate capital modelling. (p. 1)[^original]  
  <sub>anchor: "accuracy or consistency errors within the dataset will likely impact the ability of the AI model"</sub>
- **descriptive / typology or red flag**: Paragraph 3.18: dynamic AI systems that learn continuously from data, with hyperparameters, functional form and outputs that adapt, can be more susceptible to data drift and concept drift, making them less stable; increasing complexity can cause lack of explainability or interpretability (the 'black box problem'), and drift combined with lack of explainability can create prudential risks, e.g. complex or opaque AI modelling of probability of default and loss given default in IRB credit models could lead to incorrect regulatory capital levels. (p. 1)[^original]  
  <sub>anchor: "the use of complex and/or opaque AI systems to model probability of default and loss given default"</sub>

## Insurance policyholder protection – PRA and FCA

- **descriptive / finding or result**: Paragraph 3.19: AI in insurance has potential to improve efficiency of data processing and decision-making in underwriting and claims; in life insurance firms could use AI to support policyholders' investment choices, in general insurance for automating claims management, and insurers can analyse new unstructured data sources such as telematics or wearable-device data for more tailored products and pricing. (p. 1)[^original]  
  <sub>anchor: "like telematics or data collected from wearable devices, to provide more tailored products and/or pricing"</sub>
- **descriptive / typology or red flag**: Paragraph 3.20: underwriting risks could lead to inappropriate pricing and marketing (e.g. models trained on historical data may not account for a breakthrough healthcare treatment, mispricing policies); concept drift and lack of explainability in claims management AI could affect policyholders' ability to claim; and AI models for cash-flow and capital reserve estimates could produce inaccurate predictions and reserve levels, affecting insurers' ability to meet future liabilities. (p. 1)[^original]  
  <sub>anchor: "AI models trained on historical data may not account for a breakthrough healthcare treatment"</sub>

## Financial stability and market integrity – the Bank and FCA

- **descriptive / finding or result**: Paragraph 3.21: benefits for individual firms may extend to the financial system, e.g. more efficient processing in credit decisions, insurance contracts and customer interaction; AI can be a powerful tool for modelling macro financial risks and, by processing large multidimensional data, detecting patterns in unstructured data and identifying shifts in secular trends and narrative consensus. (p. 1)[^original]  
  <sub>anchor: "AI can be a powerful tool for modelling macro financial risks and dynamics"</sub>
- **descriptive / typology or red flag**: Paragraph 3.22: AI use may amplify financial stability risks; similar datasets and AI algorithms may produce uniformity across firms, amplifying procyclical behaviour and herding in uses such as algorithmic trading, and markets could become vulnerable to manipulation and prone to flash bubbles or crashes if sentiment analysis and social media signals were used at scale in AI trading, with the data/algorithm feedback loop exacerbating effects. (p. 1)[^original]  
  <sub>anchor: "the use of similar datasets and AI algorithms may result in uniformity across models and approaches at multiple firms"</sub>
- **descriptive / typology or red flag**: Paragraph 3.23: a key challenge is monitoring operations and risk management at third parties; increased reliance on third parties, often outside the regulatory perimeter, for datasets, AI algorithms and IT outsourcing such as cloud may amplify systemic risks, as operational failures and cyberattacks at critical third parties could disrupt AI services and create a single point of failure affecting multiple firms and markets; DP3/22 'Operational resilience: Critical third parties to the UK financial sector' explores these issues. (p. 1)[^original]  
  <sub>anchor: "lead to a single point of failure that could impact multiple firms and markets"</sub>
- **descriptive / context**: Paragraph 3.24: AI risks can also be assessed by outcome (impact on markets, consumers or the environment); the OECD has developed a baseline framework including risk metrics and NIST is developing a framework to manage AI risks; a key question is whether support for safe and responsible AI adoption is best delivered through a process-based or outcomes-based framework, or a combination. (p. 1)[^original]  
  <sub>anchor: "best delivered through a process-based or an outcomes-based framework, or indeed a combination of the two"</sub>
- **descriptive / context**: Paragraph 3.25: for an outcomes-based approach, the question arises of the most relevant metrics to measure impact, including what evidence is required to demonstrate good outcomes and how it can be collected. (p. 1)[^original]  
  <sub>anchor: "what are the most relevant metrics to measure impact"</sub>
- **descriptive / context**: Paragraph 3.26: use of AI by FMI firms, including in clearing, settlement and recording of transactions, may have financial stability implications; the DP does not consider these in detail, but the authorities would encourage stakeholders with an interest in the FMI sector to provide feedback on FMI-specific benefits and risks. (p. 1)[^original]  
  <sub>anchor: "the use of AI by FMI firms, including in the clearing, settlement, and recording of financial transactions"</sub>

## Questions: Benefits, risks, and harms of AI

- **descriptive / context**: Questions Q3 and Q4 ask which potential benefits and risks supervisory authorities should prioritise and how they are likely to change as the technology evolves; Q5 asks about novel AI challenges in financial services not covered in the DP; Q6 asks how AI could affect groups sharing protected characteristics and how firms and/or the authorities can mitigate impacts; Q7 asks which metrics are most relevant for assessing AI benefits and risks, including under an outcomes-focused approach. (p. 1)[^original]  
  <sub>anchor: "How could the use of AI impact groups sharing protected characteristics?"</sub>
- **descriptive / context**: Paragraph 4.1: Chapter 4 discusses current legal requirements and guidance the authorities consider most relevant to mitigating AI risks, how financial services regulation sits alongside cross-sectoral legislation, and the domestic and international context of emerging AI-specific requirements. (p. 1)[^original]  
  <sub>anchor: "how financial services regulation sits alongside a body of cross-sectoral legislation and regulation"</sub>

## 4. Regulation

- **descriptive / context**: Paragraph 4.2 and 4.3: Chapter 4 focuses on legal requirements and guidance applicable to PRA and FCA authorised firms, rather than Bank-supervised FMIs; a central question in the wide-ranging debate is whether AI can be managed through extensions of existing frameworks or a new approach is needed. (p. 1)[^original]  
  <sub>anchor: "legal requirements and guidance that are applicable to PRA and FCA authorised firms, rather than Bank supervised FMIs"</sub>

## Introduction

- **descriptive / context**: Paragraph 4.4: governments and regulators have published emerging regulations and laws (e.g. in the EU, China and Canada), cross-sectoral principles for regulators (the UK government proposal, OECD principles), and sector-specific principles for financial firms (e.g. from De Nederlandsche Bank, the Hong Kong Monetary Authority and the Monetary Authority of Singapore); the DP focuses on regulation of AI within UK financial services. (p. 1)[^original]  
  <sub>anchor: "sector-specific principles for financial services firms (such as the ones issued by the De Nederlandsche Bank"</sub>
- **descriptive / finding or result**: Paragraph 4.5: previous work (the AIPPF and the 2022 ML survey) found that a challenge to AI adoption in UK financial services is the lack of clarity about how current rules, regulations and principles apply to AI and what that means for firms in practice. (p. 1)[^original]  
  <sub>anchor: "the lack of clarity surrounding the current rules, regulations, and principles"</sub>
- **descriptive / context**: Paragraph 4.6: the chapter discusses parts of the current framework the authorities consider most relevant to AI regulation, and they want stakeholder feedback on whether additional clarification of existing requirements would help, whether the framework could be extended to better encompass AI, and how they can best support safe and responsible AI adoption. (p. 1)[^original]  
  <sub>anchor: "whether additional clarification of existing legal requirements and guidance in respect of AI may be helpful"</sub>

## Box 4: Proportionality and the supervisory authorities’ approach to regulation

- **descriptive / context**: Under FSMA 2000 the PRA and FCA must have regard, in discharging general functions, to the regulatory principle that a burden or restriction imposed on a person or activity should be proportionate to the benefits, considered in general terms, expected from it; this principle informs their thinking on AI including any future regulatory interventions. (p. 1)[^original]  
  <sub>anchor: "should be proportionate to the benefits, considered in general terms, which are expected to result"</sub>
- **descriptive / context**: IOSCO guidance on AI use by market intermediaries and asset managers states members and firms should consider proportionality, judged by the activity undertaken, its complexity, risk profiles, degree of autonomy of the AI applications, and potential impact on client outcomes and market integrity; De Nederlandsche Bank states its AI principles should be applied in light of the scale, complexity and materiality of an organisation's AI applications. (p. 1)[^original]  
  <sub>anchor: "the degree of autonomy of the AI applications, and the potential impact that the technology has on client outcomes"</sub>

## What is AI?

- **descriptive / definition**: Paragraph 2.11: the Bank and the FCA have previously given a non-legal definition of AI as the theory and development of computer systems able to carry out tasks that formerly needed human intelligence. (p. 1)[^original]  
  <sub>anchor: "the theory and development of computer systems able to perform tasks which previously required human intelligence"</sub>
- **descriptive / definition**: Paragraph 2.11: the term AI system means the set of integrated computational elements and microservices that input, output, process and store data and information, so a single AI system can contain several AI algorithms, models and datasets. (p. 1)[^original]  
  <sub>anchor: "The term AI system refers to the set of integrated computational elements and microservices"</sub>

## How AI is used in financial services

- **descriptive / context**: Paragraph 2.22: financial services firms are making growing use of AI across a range of business areas, and the Covid-19 pandemic has sped up how quickly it is being adopted. (p. 1)[^original]  
  <sub>anchor: "the Covid-19 pandemic has accelerated the pace of adoption"</sub>

## Competition – FCA

- **descriptive / finding or result**: Paragraph 3.13: according to academic research, AI systems that spot rivals' price changes and allow quick or automatic responses could potentially help sellers pursue collusive strategies and penalise any seller that departs from them. (p. 1)[^original]  
  <sub>anchor: "AI systems could potentially facilitate collusive strategies between sellers and punish deviation"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Prudential Regulation Authority / Bank of England, "DP5/22 - Artificial Intelligence and Machine Learning" (2026-10-01). https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence
