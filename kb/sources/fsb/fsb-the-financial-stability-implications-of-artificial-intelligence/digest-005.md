---
type: Source Digest
title: The Financial Stability Implications of Artificial Intelligence - part 5 of 5 (pp. 35-40)
description: 'Verified paraphrased digest, pp. 35-40: Annex 1: Supply chain for large language models; Annex 1: Supply chain for large language models > Table A1: Primary distribution channels for foundation models and derivative products; Glossary; and 1 more sections'
resource: https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/
tags:
- data_governance
- international_standard
- intl
- model_governance
- responsible_ai
- risk_assessment
status: stable
source_id: fsb-the-financial-stability-implications-of-artificial-intelligence
issuer: fsb
issuer_name: Financial Stability Board
jurisdictions:
- INTL
tier: 2
instrument_type: risk_assessment
normative_force: international_standard
publication_date: '2024-11-14'
legal_status: current
part: 5
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:12:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:12:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:12:05Z'
sources:
- id: original
  resource: https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/
  title: The Financial Stability Implications of Artificial Intelligence
  author: org:fsb
  last_modified: '2024-11-25T00:00:00Z'
digest_points: 30
---

# The Financial Stability Implications of Artificial Intelligence (digest)

[previous part](digest-004.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 35-40) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Annex 1: Supply chain for large language models

- **descriptive / data or feature**: Key sources of training data used by AI firms include open-source web crawl data, proprietary data, purchased data and synthetic data. (p. 35)[^original]  
  <sub>anchor: "include opensource web crawl data, proprietary data, purchased data, and synthetic data."</sub>
- **descriptive / finding or result**: End users, including FIs, can use curated products such as chatbots and code generation services, which are currently generally affordable and need no special computing pre-requisites. Developers can use LLMs to build applications, using models as-is or customising ("fine-tuning") them with additional data for domain specificity. Another emerging technique is retrieval augmented generation (RAG), which gives LLMs access to external, authoritative data sources for more up-to-date and well-sourced results. Customising LLMs needs less computing power than training, but GPU access is still advantageous for performance and scalability. (p. 35)[^original]  
  <sub>anchor: "build retrieval augmented generation (RAG) systems, which involves giving LLMs access to external, authoritative data sources"</sub>
- **descriptive / context**: Figure A1 captures the supply chain for foundation models and derivative products: key inputs are GPUs, data and SDKs; developers buy GPUs directly or rent them from cloud service providers, train foundation models and distribute them directly to end-users, through cloud services and through public repositories; some developers charge a fee for model access (source: author illustration). (p. 35)[^original]  
  <sub>anchor: "Model developers buy GPUs directly or rent them from cloud service providers."</sub>
- **descriptive / context**: Figure A1 gives an overview of the current LLM and GenAI supply chain. The main inputs to producing a model are GPUs, data, and software development toolkits (SDKs) that help put ML architectures into practice. (p. 35)[^original]  
  <sub>anchor: "Key inputs to model production include GPUs, data, and software development toolkits (SDKs)"</sub>
- **descriptive / context**: LLMs are trained by specialty AI labs, major technology companies and consortiums of researchers. These firms either buy accelerated computing chips from GPU suppliers or rent them from cloud service providers, and the markets for GPU design and fabrication are highly concentrated. (p. 35)[^original]  
  <sub>anchor: "Entities that train LLMs include specialty AI labs, major technology companies, and consortiums of researchers."</sub>
- **descriptive / finding or result**: The report identifies three main channels by which LLMs and GenAI-based products reach users: directly to the end-user, through open repositories, and through cloud service providers (summarised in a table of channels). (p. 35)[^original]  
  <sub>anchor: "(1) direct to end-user, (2) through open repositories, and (3) via cloud service providers"</sub>

## Table A1: Primary distribution channels for foundation models and derivative products

- **descriptive / finding or result**: Table A1, direct to end-user: leading model developers often provide direct access to LLMs through curated products such as chatbots and code generation tools, and through developer-centric methods such as application programming interfaces (APIs); some developers charge end-users a fee for premium products. (p. 36)[^original]  
  <sub>anchor: "Leading model developers often provide direct access to LLMs throughcurated products"</sub>
- **descriptive / finding or result**: Table A1, open repository: some developers post pre-trained LLMs to open repositories, from which end-users can download them and customise them or use them as-is. Footnote 131: as of late April 2024 there were 98 text generation models on Hugging Face with over 100,000 downloads, and the AI Index 2024 shows most foundation models developed in 2023 were open. (p. 36)[^original]  
  <sub>anchor: "Some model developers post pre-trained LLMs to open repositories."</sub>
- **descriptive / finding or result**: Table A1, cloud services: end-users can access some LLMs through cloud services; providers of some of the largest closed models have partnered with specific CSPs to develop cloud-based access channels, which also offer access to some open-source LLMs. (p. 36)[^original]  
  <sub>anchor: "providers of some of the largest closedmodels have partnered with specific CSPs"</sub>
- **descriptive / finding or result**: Three potential sources of concentration risk in the LLM supply chain are model training, cloud services and hardware. Currently the most competitive is model training: there are distinct market leaders but several firms train competitive LLMs. (p. 36)[^original]  
  <sub>anchor: "Three potential sources of concentration risk in the LLM supply chain include model training, cloud services, and hardware."</sub>
- **descriptive / finding or result**: Many end users, including FIs, building LLM applications are likely to use cloud-based access channels because: (1) working with LLMs in the cloud enables more seamless integration with computing resources advantageous for fine tuning and running inference on large models; (2) firms can access some of the most performant closed models via specific CSPs without sending queries directly to model providers via API; and (3) many FIs have built institutional capacity and governance structures for vetting cloud security. (p. 36)[^original]  
  <sub>anchor: "First, working with LLMs in the cloud enables more seamless integration with computing resources"</sub>
- **descriptive / finding or result**: Currently the biggest source of concentration risk in the LLM supply chain is the hardware market, where there are dominant firms in GPU design and fabrication. Alternatives exist: an industry participant from a large financial institution at the FSB-OECD joint roundtable on AI in finance in May 2024 said their institution works with small LLMs using on-premises GPUs owned by the firm. (p. 36)[^original]  
  <sub>anchor: "the biggest source of concentration risk in the LLM supply chain is in the hardware market"</sub>

## Glossary

- **descriptive / context**: The glossary is a non-exhaustive list of commonly used AI terms compiled from their general understanding and usage in the community, serving as a reference for the report's context; it may not cover all interpretations in other contexts. (p. 37)[^original]  
  <sub>anchor: "This glossary sets out a (non-exhaustive) list of terms used in the report."</sub>
- **descriptive / definition**: Algorithm: a set of steps or rules to solve a mathematical problem; more recently the term refers to a process to be followed, often by a computer. Machine learning: a method of designing a sequence of actions (algorithms) to solve a problem that optimise automatically through experience with limited or no human intervention. (p. 37)[^original]  
  <sub>anchor: "An algorithm is a set of steps to be performed or rules to be followed to solve a mathematical problem."</sub>
- **descriptive / definition**: Deep learning: a form of machine learning using algorithms that work in 'layers' inspired by the structure and function of the brain; the structures are called artificial neural networks and can be used for supervised, unsupervised or reinforcement learning. (p. 37)[^original]  
  <sub>anchor: "Deep learning is a form of machine learning that uses algorithms that work in"</sub>
- **descriptive / definition**: Foundation models: an umbrella term for models usually trained by applying deep learning to massive quantities of data such as text and images; because expertise, time and computing power for training from scratch are typically prohibitive for most non-specialist firms, they are usually pre-trained and shared with end-users for further use and refinement. (p. 37)[^original]  
  <sub>anchor: "An umbrella term referring to a diversity of models that are usually trained by applying deep learning"</sub>
- **descriptive / definition**: Generative AI (GenAI): AI that generates new content such as text, images and videos, often based on user prompts, powered by foundation models such as LLMs. Large Language Models (LLMs): a type of foundation model trained on and designed to perform tasks with natural language; most are trained using the Transformer architecture, and key tasks include text generation, document classification, summarisation, question-and-answer and sentiment analysis. (p. 37)[^original]  
  <sub>anchor: "AI that generates new content, such as text, images, and videos, often based on user prompts."</sub>
- **descriptive / definition**: Reinforcement learning: falls between supervised and unsupervised learning; the algorithm is fed an unlabelled data set, chooses an action for each data point and receives feedback (perhaps from a human) that helps it learn, for instance in robotics, game theory and self-driving cars. Semi-supervised learning: a combination of supervised and unsupervised learning in which some input data is labelled. (p. 37)[^original]  
  <sub>anchor: "the algorithm is fed an unlabelled set of data, chooses an action for each data point, and receives feedback"</sub>
- **descriptive / definition**: Supervised learning: the algorithm is fed 'training' data labelling some portion of observations; for instance a data set of transactions may label some points as fraudulent or not, and the algorithm learns a general classification rule to predict labels for the remaining observations. Unsupervised learning: the data contain no labels and the algorithm detects patterns by identifying clusters of observations with similar underlying characteristics; for example, it could look for securities similar to an illiquid security that is hard to price, and use pricing of other securities in the cluster to help price it. (p. 37)[^original]  
  <sub>anchor: "a data set of transactions may contain labels on some data points identifying those that are fraudulent"</sub>
- **descriptive / definition**: Traditional AI: a suite of computational techniques that pre-date recent advances such as GenAI. Transformer architecture: a type of neural network with two key innovations, self-attention (each word in a text relates to every other word, enhancing understanding of context and relationships) and positional encoding (lets transformers process data concurrently, using less compute than other models). (p. 38)[^original]  
  <sub>anchor: "Traditional AI models refer to a suite of computational techniques that pre-date recent advances"</sub>

## Abbreviations

- **descriptive / definition**: Abbreviations list: AI means Artificial Intelligence; AML means Anti-Money Laundering; API means Application Programming Interface; ASIC means Application-Specific Integrated Circuit. (p. 39)[^original]  
  <sub>anchor: "|AI|Artificial Intelligence|
|AML|Anti-Money Laundering|
|API|Application Programming Interface|
|ASIC|Application-Specific Integrated Circuit|"</sub>
- **descriptive / definition**: Abbreviations list: BCBS is the Basel Committee on Banking Supervision; BIS is the Bank for International Settlements; BoE is the Bank of England; CFT is Counter-Terrorist Financing; CSP is a Cloud Service Provider. (p. 39)[^original]  
  <sub>anchor: "|BCBS|Basel Committee on Banking Supervision|
|BIS|Bank for International Settlements|
|BoE|Bank of England|
|CFT|Counter-Terrorist Financing|
|CSP|Cloud Service Provider|"</sub>
- **descriptive / definition**: Abbreviations list: ECB is the European Central Bank; EBA is the European Banking Authority; EU is the European Union; FCA is the Financial Conduct Authority; FI is a Financial Institution; FSB is the Financial Stability Board. (p. 39)[^original]  
  <sub>anchor: "|ECB|European Central Bank|
|EBA|European Banking Authority|
|EU|European Union|
|FCA|Financial Conduct Authority|
|FI|Financial Institution|
|FSB|Financial Stability Board|"</sub>
- **descriptive / definition**: Abbreviations list: FSOC is the Financial Stability Oversight Council; FSSCC is the Financial Services Sector Coordinating Council; GenAI is Generative Artificial Intelligence; GPU is a Graphics Processing Unit. (p. 39)[^original]  
  <sub>anchor: "|FSOC|Financial Stability Oversight Council|
|FSSCC|Financial Services Sector Coordinating Council|
|GenAI|Generative Artificial Intelligence|
|GPU|Graphics Processing Unit|"</sub>
- **descriptive / definition**: Abbreviations list: HKMA is the Hong Kong Monetary Authority; IAIS is the International Association of Insurance Supervisors; IMF is the International Monetary Fund. (p. 39)[^original]  
  <sub>anchor: "|HKMA|Hong Kong Monetary Authority|
|IAIS|International Association of Insurance Supervisors|
|IMF|International Monetary Fund|"</sub>
- **descriptive / definition**: Abbreviations list: IOSCO is the International Organization of Securities Commissions. The final row of the first table is garbled in the extracted text: it reads "IRBKYC" with the expansion "Internal Ratings-BasedKnow Your Customer", and is reported here as written rather than split. (p. 39)[^original]  
  <sub>anchor: "|IOSCO|International Organization of Securities Commissions|
|IRBKYC|Internal Ratings-BasedKnow Your Customer|"</sub>
- **descriptive / definition**: Abbreviations list (second table): LLM is a Large Language Model; ML is Machine Learning. (p. 39)[^original]  
  <sub>anchor: "|LLM|Large Language Model|
|---|---|
|ML|Machine Learning|"</sub>
- **descriptive / definition**: Abbreviations list: NIST is the National Institute of Standards and Technology; NLP is Natural Language Processing. (p. 39)[^original]  
  <sub>anchor: "|NIST|National Institute of Standards and Technology|
|NLP|Natural Language Processing|"</sub>
- **descriptive / definition**: Abbreviations list: OECD is the Organisation for Economic Co-operation and Development; PRA is the Prudential Regulation Authority; RAG is Retrieval Augmented Generation; RegTech is Regulatory Technology. (p. 39)[^original]  
  <sub>anchor: "|OECD|Organisation for Economic Co-operation and Development|
|PRA|Prudential Regulation Authority|
|RAG|Retrieval Augmented Generation|
|RegTech|Regulatory Technology|"</sub>
- **descriptive / definition**: Abbreviations list: SDK is a Software Development Kit; SSB is a Standard Setting Body; SupTech is Supervisory Technology; UK is the United Kingdom; US is the United States. (p. 39)[^original]  
  <sub>anchor: "|SDK|Software Development Kit|
|SSB|Standard Setting Body|
|SupTech|Supervisory Technology|
|UK|United Kingdom|
|US|United States|"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md)

[^original]: Financial Stability Board, "The Financial Stability Implications of Artificial Intelligence" (2024-11-14). https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/
