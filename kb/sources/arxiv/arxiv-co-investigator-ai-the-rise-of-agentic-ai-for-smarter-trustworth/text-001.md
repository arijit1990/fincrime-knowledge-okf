---
type: Source Text
title: 'Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives - part 1 of 2 (pp. 1-10)'
description: 'Verbatim extracted text, pp. 1-10: Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives; Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives > Abstract; Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives > 1 Introduction; and 7 more sections'
resource: https://arxiv.org/abs/2509.08380
tags:
- academic_finding
- case_management
- genai
- global_academic
- investigations
- preprint
status: stable
source_id: arxiv-co-investigator-ai-the-rise-of-agentic-ai-for-smarter-trustworth
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-10-09'
legal_status: unknown
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2509.08380
  title: 'Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives'
  author: org:arxiv
  last_modified: '2025-10-09T00:00:00Z'
---

# Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2025-10-09), part 1 of 2, pp. 1-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives


[p. 1]

Prathamesh Vasudeo Naik_∗_ Naresh Kumar Dintakurthi_∗_ Zhanghao Hu_∗_ Yue Wang_∗_ Robby Qiu_∗_

Generating regulatorily compliant Suspicious Activity Report (SAR) remains a high-cost, low-scalability bottleneck in Anti-Money Laundering (AML) workflows. While large language models (LLMs) offer promising fluency, they suffer from factual hallucination, limited crime typology alignment, and poor explainability— posing unacceptable risks in compliance-critical domains. This paper introduces Co-Investigator AI , an agentic framework optimized to produce Suspicious Activity Reports (SARs) significantly faster and with greater accuracy than traditional methods. Drawing inspiration from recent advances in autonomous agent architectures, such as the AI Co-Scientist[2], our approach integrates specialized agents for planning, crime type detection, external intelligence gathering, and compliance validation. The system features dynamic memory management, an AI-Privacy Guard layer for sensitive data handling, and a real-time validation agent employing the Agent-as-a-Judge paradigm[5] to ensure continuous narrative quality assurance. Human investigators remain firmly in the loop, empowered to review and refine drafts in a collaborative workflow that blends AI efficiency with domain expertise. We demonstrate the versatility of Co-Investigator AI across a range of complex financial crime scenarios, highlighting its ability to streamline SAR drafting, align narratives with regulatory expectations, and enable compliance teams to focus on higher-order analytical work. This approach marks the beginning of a new era in compliance reporting—bringing the transformative benefits of AI agents to the core of regulatory processes and paving the way for scalable, reliable, and transparent SAR generation.

### Abstract


Index Terms: Large Language Model, AI Agent, Anti Money Laundering.

Compliance teams at financial institutions (FIs) routinely produce SAR narratives—crucial documents that elucidate suspicious conduct for regulatory and law-enforcement review. However, crafting these narratives is time-consuming and inconsistent. FinCEN estimates the final stages of SAR preparation take between 25 and 315 minutes , depending on complexity. This delay results from manually gathering transactional data, KYC records, communication metadata, and investigative context. Moreover, narrative quality varies widely across FIs, driven by differences in investigator experience, workload, and interpretive judgment—introducing compliance risks. Concurrently, mounting transaction volumes and evolving crime typologies (e.g., cryptocurrency layering, elder exploitation, digital fraud) are overwhelming traditional workflows.

### 1 Introduction


These challenges underscore an urgent need for scalable, reliable systems that ensure narrative quality and regulatory compliance while alleviating investigator burden. This paper presents Co-Investigator AI —a human-in-the-loop, agentic system that auto-

mates data parsing, crime type detection, and draft narrative generation, empowering FIs to enhance both investigator productivity and compliance robustness.

The Suspicious Activity Report (SAR) is a cornerstone in Anti-Money Laundering (AML) compliance, acting as the primary mechanism for financial institutions (FIs) to report suspicious activities—such as fraud, money laundering, terrorist financing, and sanctions evasion—to regulators like FinCEN in the U.S. SARs were institutionalized under the Bank Secrecy Act of 1970 , with the report format standardized in 1996 to ensure consistent and effective reporting practices. Since July 1, 2012, U.S. SARs are filed electronically, improving timeliness and data integrity.

### 2 AML, SAR and Compliance Landscape


#### 2.1 Regulatory Requirements and SAR Content


[pp. 1-2]

U.S. financial institutions must electronically file SARs within 30 calendar days from the initial detection

* Corresponding authors: pratnaik@paypal.com, ndintakurthi@paypal.com, zhanhu@paypal.com, ywang49@paypal.com, xqiu1@paypal.com

of suspicious activity. If the subject is unidentified, the reporting window may be extended to 60 days in total. In cases of extreme urgency—such as suspected terrorist financing—immediate filings and direct notification of law enforcement are mandatory.

FinCEN requires SARs to include:

1. Subject Details : Identifying information (name, address, date of birth, SSN, associated accounts).

2. Suspicious Activity Description : A date range and classification code describing suspicious behavior.

3. Institution Information : Details about the reporting FI and the relevant branch, platform, or system.

4. Filer Contact Details : Compliance officer’s full contact info for regulatory follow-up.

5. Narrative Explanation : A comprehensive account covering who, what, when, where, and how the activity unfolded.

6. Supporting Documentation : Transaction logs, communications, account records retained for at least five years .

#### 2.2 Challenges in Narrative Generation


[p. 2]

The narrative section is both the most critical and the most resource-intensive component of the SAR. It must convey a clear, legally compliant story without “tipping off” the subject—making it a complex blend of factual clarity and strategic discretion. Traditional methods—manual drafting, disparate tool usage, and data aggregation—are time-consuming and subject to interpretation, resulting in potential errors, inconsistencies, and compliance vulnerabilities.

FIs face increasingly stringent regulatory scrutiny from bodies such as FinCEN, the Financial Action Task Force (FATF), and other global regulators. Noncompliance—including late SAR filings or incomplete narratives—can trigger severe penalties, reputational harm, and heightened supervisory oversight.

#### 2.3 Compliance Pressure and Institutional Burden


Furthermore, SARs serve a dual role: they aid immediate law enforcement investigations and contribute to long-term trend analysis and regulatory strategy development based on aggregated SAR data.

Given the escalating data volumes, increasing transaction complexity, and stricter AML regulatory demands, financial institutions urgently need scalable, accurate, and explainable approaches to SAR generation. Our Co-Investigator AI addresses these issues by:

- Automating narrative drafting while maintaining human interpretability.

- Ensuring narratives meet structure and substance requirements mandated by regulators.

- Accelerating investigation timelines without sacrificing compliance quality.

By aligning with established SAR frameworks— timeliness requirements, content mandates, and narrative best practices—our research aims to strike the balance between accelerated workflow and rigorous regulatory adherence.

### 3 Why Traditional SAR Workflows Break: Data Friction, Scalability Limits, and GenAI Gaps


Financial institutions continue to rely heavily on manual workflows to generate Suspicious Activity Reports (SARs), despite the growing complexity and volume of financial crimes. These workflows—while humanguided and context-rich—are increasingly inadequate under the pressures of modern AML operations. Institutions face tighter regulatory timelines, growing typology diversity, and rising expectations around auditability and consistency.

While recent advances in large language models (LLMs) have opened the door to semi-automated text generation, the limitations of unstructured, monolithic GenAI applications remain poorly understood in compliance contexts. Before proposing a modular agentic alternative, we first characterize the failure modes of traditional and baseline LLM-driven SAR generation methods.

#### 3.1 Manual Drafting: Fragmented Tools, High Latency, and Cognitive Overload


[pp. 2-3]

Suspicious Activity Reports are synthesized from multiple sources: structured transaction data, account metadata, communication logs, external alerts, and

KYC profiles. Investigators manually gather and interpret this information across siloed tools like spreadsheets, case management dashboards, and third-party research platforms.

This workflow presents multiple systemic limitations:

- Complexity & Time Burden : Investigators often spend several hours per narrative due to the intricate nature of the data and required regulatory detail.

- Inconsistency : Narrative quality is susceptible to variance in experience and style, negatively affecting interpretability.

- Scalability Limits : Increasing SAR volumes overwhelm manual capacities, risking incomplete or delayed filings.

- Error Risk : Human-curated narratives are prone to omissions, misinterpretation, and potential regulatory non-compliance.

- Operational Overhead : Investigators frequently juggle multiple tools—Excel, case management systems, external databases—leading to fragmented workflows and reduced efficiency.

These constraints underscore the pressing need for automation technologies that maintain narrative rigor while reducing investigators' cognitive and operational burdens.

#### 3.2 Limitations of Direct GenAI Narrative Generation


[p. 3]

Recent research highlights the increasing adoption of AI techniques in AML contexts[4][6]. To explore whether modern LLMs can bypass these bottlenecks, we tested direct prompting approaches using raw AML case data. While LLMs (e.g., GPT-4, Claude 3) performed reasonably on clean, low-complexity cases, results degraded sharply in real-world conditions.

- Template Scenarios : For highly structured, low-complexity cases, the model produced coherent drafts that aligned with expected formats, showing promise in straightforward contexts.

- Performance Breakdown : Once confronted with real-world complexity—multiple subjects, overlapping financial crime typologies, and extensive transaction histories—the model produced inconsistent and unreliable outputs.

- Hallucination Risks : The LLM invented details such as fabricated interactions, spurious transaction events, and contextually unsupported notes, even when explicitly instructed not to add information. This aligns with documented hallucination rates—frequently exceeding 20–30% in LLM-generated content[7].

- Review Cost : Although drafting appeared rapid, the required manual validation and correction nullified any time benefits, shifting the burden to investigators.

These limitations highlight a critical gap: LLMs can produce grammatically correct outputs, but lack traceability, modular reasoning, and typologyspecific sensitivity . This motivates a shift away from monolithic generation toward agentic decomposition , where specialized AI agents reason, validate, and interact in concert with human investigators.

### 4 Agentic AI and the Co Investigator Paradigm: Enhancing SAR Generation


[pp. 3-4]

To address the shortcomings revealed by direct Gen AI experimentation, we propose the Co-Investigator Paradigm —a fully agentic AI framework tailored for high-stakes compliance tasks. This paradigm draws inspiration from the multi-agent coordination seen in systems like the AI Co-Scientist[2] but adapts these concepts for financial crime investigations.

Figure 1: Agentic AI in action: Perceive–Reason–Act architecture

Agentic AI , as surveyed by Xi et al[9], defines intelligent systems that can perceive inputs, reason adaptively, and act[23] —often collaboratively in multiagent settings or alongside humans[10]. AI systems are becoming increasingly capable—a trend that is likely to accelerate with the development of more agentic AI systems in the future[14][15]. Co-Investigator AI embodies these principles, featuring purpose-built agents that independently:

1. Perceive : ingest and normalize transaction data, KYC records, and external intelligence.

2. Reason : identify typologies, assess regulatory compliance, and draft coherent narratives using transparent Chain-of-Thought prompting[3].

3. Act : generate initial SAR drafts and flag compliance concerns in real-time.

This architecture encompasses distinct yet interconnected functional agents, ensuring precise compliance analysis, efficient workflow orchestration, transparent reasoning processes, and structured human-agent collaboration. Key modules within the system include:

- Data Ingestion And Structuring Layer

- AI-Privacy Guard Layer

- Crime Type Detection

- Planning Agent

- Typology Detection Agents

- External Intelligence Agent

- Narrative Generation Agent

- Compliance Validation Agent

This agentic structure supports a human-agent collaborative ecosystem . Specialized agents— responsible for tasks such as crime type detection, narrative drafting, and compliance validation—work in concert under human oversight. Investigators receive structured SAR drafts and refine them using iterative feedback guided by the model. This humanin-the-loop design maintains accountability and interpretability, ensuring outputs meet regulatory standards and cultural nuances.

By combining autonomous agentic operations with human expertise, Co-Investigator AI delivers scalable, transparent, and reliable SAR narrative generation— far surpassing monolithic LLM approaches in both performance and auditability.

### 5 Detailed System Design


[p. 4]

The Co-Investigator AI deploys a modular, agentic architecture (Figure 2) for purpose-built efficient, high-quality Suspicious Activity Report (SAR) narrative generation. The system orchestrates specialized AI agents supported by dynamic memory, investigator feedback loops, automated compliance checks, and explicit reasoning protocols. This cohesive, human-centered framework significantly improves scalability, narrative accuracy, and adherence to regulatory standards.

The Co-Investigator AI is structured as a sophisticated, modular, agentic architecture designed explicitly for the automated generation and iterative refinement of Suspicious Activity Report (SAR) narratives.

#### 5.1 Agentic Modular Architecture Overview


- Feedback Agent

- Dynamic Memory

- Analytical Tools

The process begins with the Data Ingestion & Structuring Layer , which operates independently of the central orchestration component. This layer systematically ingests raw alert data—transaction records, account metadata, customer identifiers, and risk signals—and transforms it into structured summaries. These parsed outputs provide the foundational inputs for the downstream AI-Privacy Guard and subsequent analytic pipeline.

To address critical data privacy and compliance requirements, our architecture integrates with a dedicated AI-Privacy Guard layer positioned upstream of the Large Language Model (LLM) processing pipeline. The primary objective of this layer is to systematically identify and anonymize sensitive entities, specifically data categorized as class-1 or class-2 confidential information, prior to submission to external LLM services. This AI-Privacy Guard layer serves as a horizontal capability ensuring robust protection and regulatory compliance of sensitive data.

#### 5.3 AI-Privacy Guard Layer


[pp. 4-6]

Unlike conventional Named Entity Recognition (NER) tasks, our model faces distinct challenges due to the nature and variability of input data:

Figure 2: Modular agentic architecture of Co-Investigator AI for SAR generation

- Highly Unstructured Input Data: Input data originates from diverse formats including source code (HTML, etc.), conversational text, and miscellaneous free-form prompts, creating substantial variability and complexity.

- Extended Context Length: Inputs frequently reach the maximum token limits of contemporary LLMs, demanding models capable of efficiently processing lengthy, contextually dense texts without loss of performance or accuracy.

- Critical SLA Requirements: Real-time performance and strict adherence to service-level agree-

ments (SLAs) are mandatory, requiring rapid inference even on extensive, highly unstructured text inputs containing potentially unlimited sensitive entities.

To effectively address these specific demands, our AI-Privacy Guard solution employs a robust RoBERTa[16] model combined with Conditional Random Fields (CRF) , optimized through advanced methods including model quantization and deep speed-based inference acceleration. This optimization approach ensures both computational efficiency and consistent compliance with stringent SLAs,

while maintaining high-precision anonymization capabilities across a diverse array of complex, lengthy, and sensitive data inputs.

AI-Privacy Guard layer operates dynamically across multiple agents, facilitating secure interactions at critical workflow stages:

- Pre-Processing Integration: After the Data Ingestion and Structuring Layer processes raw data, the AI-Privacy Guard anonymizes sensitive elements before data is routed to crime type detection agents and external LLMs.

- Typology Agents Integration: Ensures sensitive data is consistently masked across all specialized typology detection agents during their analytical processing, maintaining robust data protection and compliance.

- Narrative Generation Interaction: After analytical processing, the anonymized data is unmasked by the AI-Privacy Guard before incorporation into the narrative drafts, enabling investigators to interpret and validate precise, contextually rich narratives.

- Feedback Agent Integration: Prior to transmitting narratives to external feedback systems or review interfaces, the AI-Privacy Guard re-masks sensitive details to ensure continued confidentiality during human-in-the-loop interactions.

#### 5.4 Crime Type Detection Layer


[p. 6]

Accurate crime type detection is a critical yet resourceintensive component within AML compliance and Suspicious Activity Report (SAR) generation. Financial crime investigations frequently involve multiple, overlapping types, such as elder financial exploitation, romance scams, human trafficking, money mule schemes, terrorist financing, CSAM, identity theft, and various fraud schemes. Traditional manual classification approaches consume substantial investigative resources, underscoring the need for systematic automation.

The Co-Investigator AI addresses this challenge through a specialized Crime Type Detection Agent , designed with two integrated analytical components:

- Risk-Indicator Extraction Tools: The Crime Type Detection Agent leverages automated riskbased tools to scan all relevant compliance data— both structured records and free-form text—and

surface key risk indicators. It abstracts away lowlevel details, instead flagging broad “red flag” categories (e.g., anomalous access, atypical payment behavior, and potential exploitation patterns) for downstream analysis.

- Machine Learning Classification Models: Complementing these automated tools, sophisticated tree-based ensemble models (e.g., Random Forest, Gradient Boosting) systematically analyze extracted risk indicators alongside historical data, transaction patterns, and entity relationships. These models produce probabilistic assessments of potential financial crime typologies, allowing precise multi-typology classification.

The combined outputs—ranked typologies with associated confidence scores—inform the Central Orchestration and Planning Agent, which dynamically coordinates specialized analytical agents tailored to each identified type. This systematic, integrated approach significantly reduces investigator workloads, enhances narrative accuracy, and ensures rigorous compliance, underscoring the operational effectiveness of automated typology detection.

#### 5.5 Planning Agent


The Planning Agent serves as the central orchestrator within the agentic architecture, primarily responsible for dynamically spawning specialized typology detection agents and external intelligence agents. It leverages outputs from the crime type detection agent, real-time feedback from operational agents, and structured investigator input to determine which agents to activate. This dynamic orchestration ensures precise resource allocation, optimized investigative efficiency, and consistent regulatory compliance throughout the SAR generation lifecycle.

The following specialized agents systematically analyze specific financial crime typologies, each dedicated to distinct risk-detection tasks:

- Transaction Fraud Detection Agent: Detects suspicious transaction patterns indicative of potential fraud.

#### 5.6 Specialized Typology Detection Agents


[pp. 6-7]

- Payment Volume Velocity Detection Agent: Flags abnormal transaction frequencies or highvolume activity.

- Country Risk Detection Agent: Evaluates transactions linked to high-risk or sanctioned jurisdictions.

- Textual Content Detection Agent: Identifies anomalies in textual customer communications and transaction notes using advanced NLP.

- Geographic Anomaly Detection Agent: Detects location-based inconsistencies and transaction anomalies.

- Account Health Assessment Agent: Assesses historical account activities for potential compromise or misuse.

- Dispute Pattern Detection Agent: Analyzes dispute patterns to detect suspicious or fraudulent claims.

To enrich SAR narratives with pertinent external risk intelligence, our system incorporates an External Intelligence Agent that leverages the Model Context Protocol (MCP)[24] an emerging open standard for secure, tool-agnostic AI integration. MCP enables seamless and dynamic access to external data sources (e.g., news feeds, sanctions list, media reports) through standardized servers without requiring bespoke API integrations.

#### Key Design Features


[p. 7]

- Standardized Tool Discovery & Invocation The agent dynamically identifies data sources exposed via MCP servers—treating each as a tool with well-defined metadata. This allows it to select and invoke sources at runtime without personalization or hard-coded logic.

- Context-Driven Intelligence Retrieval Upon crime type detection or investigator request (e.g., linking a subject to a high-risk jurisdiction), the agent issues MCP queries. Returned data—such as negative news articles, regulatory advisories, or watchlist flags—is integrated into narrative drafts, providing timely contextualization.

Integrating analytical insights from previous modules, the Narrative Generation Agent synthesizes

#### 5.8 Narrative Generation Agent


structured SAR narrative drafts. Utilizing explicit Chain-of-Thought (CoT)[3][30] prompting methods, it transparently articulates its reasoning, aggregating risk indicators, transaction details, external intelligence, and historical regulatory context. This agent generates comprehensive and structured drafts explicitly intended for investigator review and refinement.

Figure 3: Chain-of-Thought reasoning within CoInvestigator AI’s narrative generation

- Compliance Validation Agent (Agent-as-aJudge): Employs rigorous automated evaluation methodologies—combining semantic coherence assessments and rule-based regulatory accuracy checks—to systematically verify narrative quality and compliance alignment. Guided explicitly by the Agent-as-a-Judge methodology[5], this agent ensures consistently high-quality SAR narratives.

#### 5.9 Compliance Validation and Explicit Reasoning


[pp. 7-8]

- Confidence Score-Based Reasoning Framework: Within the Chain-of-Thought methodology, agents assign structured confidence scores reflecting evidentiary strength, contextual relevance, and regulatory adherence. This transparent scoring mechanism ensures clear interpretability, accountability, and investigator trust in the generated narrative components. These techniques are also used to estimate LLM confidence in the factual accuracy of its responses[32].

The dedicated Feedback Agent systematically integrates structured human feedback into iterative

refinement processes. Investigators provide narrative reviews and adjustments through a secure editing interface, with their inputs explicitly captured and dynamically incorporated into subsequent narrative cycles, ensuring continuous improvements and refined narrative precision. This mirrors recent work on feedback-driven refinement frameworks such as _Self-Refine_ , which employs iterative feedback loops to significantly enhance LLM output quality without requiring additional training data[33].

#### 5.12 Supporting Analytical Tools


[p. 8]

To further enhance the analytical capabilities of our agentic system, we have integrated specialized analytical tools designed to accelerate and deepen investigative processes. These tools systematically analyze data, extract critical insights, and enrich investigative contexts, thereby significantly improving the accuracy, efficiency, and interpretability of compliance investigations. Specifically, the supporting analytical tools include:

To enhance narrative coherence and regulatory consistency, the architecture employs sophisticated memory management techniques across multiple layers:

- Regulatory Memory: Maintains up-to-date regulatory guidelines, AML standards, and compliance expectations, ensuring ongoing regulatory compliance.

- Historical Narrative Memory: Stores prior SAR narratives and investigative outcomes, promoting consistent narrative generation and continuity.

#### 5.11 Dynamic Memory Management


- Typology-Specific Memory: Captures and recalls historical typology-specific analytical patterns, risk indicators, and prior investigative insights, enabling contextually precise risk assessment and narrative accuracy.

While Retrieval-Augmented Generation (RAG) pipelines[37] typically inject relevant documents into prompt contexts at inference time, they are limited by stateless execution and prompt length constraints. In contrast, Co-Investigator AI's memory system provides persistent and updateable memory layers , tightly integrated into agent workflows and continuously synchronized across tasks.

This multi-tiered memory strategy reflects recent advancements in hierarchical and agentic memory systems for LLM agents. For example, MemoryOS[34] introduces a three-level memory hierarchy—shortterm, mid-term, and long-term—and dynamic update mechanisms to preserve contextual integrity over extended interactions. Similarly, A-MEM[35] implements an agentic, structured memory network inspired by Zettelkasten methods, dynamically indexing and evolving memory content based on contextual relevance. Together, these frameworks underline the importance of structured memory design for maintaining system coherence, recall accuracy, and longitudinal consistency in agentic workflows.

- Risk Indicator Extraction Tool: Automatically scans structured and unstructured data to proactively identify and extract critical risk indicators, streamlining subsequent investigative efforts and enhancing narrative precision.

- External Intelligence Search Tool: Integrates external data sources, such as negative news, sanctions alerts, and regulatory advisories, via secure search APIs. This tool provides relevant external context to investigations, significantly enriching the interpretative depth of narratives.

- Account-Linking Analysis Tool: Systematically identifies hidden relationships and interconnected patterns among accounts, entities, and subjects. By highlighting complex networks of suspicious activity, it supports investigators in uncovering organized financial crime schemes.

Collectively, these analytical tools serve as essential support mechanisms for our specialized typology detection agents. By proactively extracting relevant risk indicators, seamlessly integrating external intelligence, and uncovering complex relational patterns, these tools significantly enhance investigative depth, efficiency, and accuracy. As a result, the Co-Investigator AI system consistently generates detailed, compliant, and comprehensive SAR narratives, greatly augmenting the effectiveness of compliance investigations.

### 6 Agentic Architecture: Sub-Agent Pattern


[pp. 8-9]

In designing Co-Investigator AI system, we adopted a sub-agent architecture, inspired by modular decomposition principles analogous to microservices. This design decomposes a complex compliance workflow into independently operating, specialized agents—each aligned to a distinct function (e.g., crime type detection, narrative generation, compliance validation).

This approach enhances system robustness, adaptability, and maintainability.

Benefits of the Sub-Agent Pattern:

1. Isolation and Fault Tolerance : Each subagent is an encapsulated module responsible for a focused task. Failures or updates in a single agent—such as the Narrative Generation Agent— do not cascade across the system. This reduces system-wide downtime and simplifies error diagnostics, enhancing overall fault tolerance.

2. Scalability and Maintainability : Agents can be scaled, optimized, or replaced individually without disrupting other components. This modularity allows for focused updates, enabling faster development cycles and easier adaptation to evolve compliance requirements or new typologies.

3. Dynamic Orchestration : The Planning Agent serves as a lightweight orchestrator, dynamically spawning sub-agents based on crime type detection results or investigator feedback. Unlike monolithic, code-heavy routing logic, this eventdriven approach enables flexibility and cleaner workflows—agents operate independently yet collaborate cohesively.

4. Frictionless Innovation : The modular design encourages targeted experimentation. Enhancing one agent—for example, integrating a new ML model into the Crime Type Detection Agent— can be done independently. This promotes clean feature rollouts, quicker experimentation, and easier regression control across modules.

By adopting a sub-agent design, our framework achieves clarity, adaptability, and resilience— empowering domain experts to scale, evolve, and maintain the system efficiently in response to changing regulatory landscapes and investigative demands.

### 7 Automated Evaluation Framework for Rapid Iteration


[p. 9]

To systematically validate the performance of the CoInvestigator AI framework and ensure the consistent generation of high-quality Suspicious Activity Report (SAR) narratives, we established an automated preproduction evaluation framework (Figure 4) specifically designed for accelerated iterative development. Developed collaboratively with the compliance investigators, this evaluation system leverages expertly

annotated "golden datasets" as authoritative benchmarks, enabling rapid assessment, transparent scoring, and continuous model refinement prior to deployment in live operational environments. Key elements of the pre-production evaluation include:

- Systematically compares AI-generated narratives against investigator-crafted SAR narratives.

- Employs a hybrid evaluation approach combining rule-based logical assessments and semantic similarity analyses powered by Large Language Models (LLMs).

#### Structured Multi-Component Scoring:


- Intro Scoring: Precisely evaluates narrative introductory elements—such as date ranges, transaction amounts, and subject identification—using weighted accuracy checks to ensure factual correctness and regulatory compliance.

- Narrative Scoring: Assesses the narrative body across seven distinct compliance dimensions, applying semantic similarity metrics with configurable category-specific weights to rigorously measure coherence, analytical completeness, and regulatory adherence.

- Combines the Intro and Narrative scoring components into a single, transparent weighted final score.

- Enables quantitative benchmarking against regulatory standards, promoting clear interpretability and structured iterative improvements to SAR narrative outputs.

Early Performance Validation: Demonstrates consistently high-quality scores effectively evaluating complex financial crime typologies such as elderly financial exploitation.

#### Aggregated Weighted Final Scoring:


[pp. 9-10]

We incorporate Google Gemini 2.5 Pro as an independent evaluation LLM, selected for its extended context handling and high factuality alignment. Gemini is used to perform semantic similarity scoring, logical coherence analysis, and interpretability assessments across SAR sections.

Figure 4: Automated evaluation framework for SAR narrative quality and regulatory alignment

To ensure the sustained quality and regulatory compliance of Suspicious Activity Report (SAR) narratives generated by the Co-Investigator AI in live production environments, we have deployed a dedicated live-evaluation agent: the Compliance Validation Agent , implementing the Agent-as-a-Judge methodology[5]. This agent autonomously and continuously validates narrative outputs immediately upon generation, systematically ensuring their accuracy, coherence, and compliance alignment, and facilitating refinement.

### 8 Live Evaluation via Compliance Validation Agent (Agent-as-a-Judge)


#### 8.1 Integration and Workflow within Agentic Architecture


[p. 10]

The Compliance Validation Agent operates seamlessly within the existing framework, interacting dynamically with multiple components to comprehensively evaluate live-generated narratives. Its operational workflow and integrations are detailed as follows:

- Coordination with Planning Agent: Upon narrative completion by narrative agent, the Planning Agent activates the Compliance Validation

Agent, triggering real-time narrative assessments based on predefined compliance priorities and regulatory risk profiles.

- Interaction with Specialized Typology Detection Agents: The Compliance Validation Agent references detailed outputs from specialized typology detection agents—including Transaction Fraud Detection, Geographic Anomaly Detection, Country Risk Detection, and others—to verify the narrative’s accuracy and completeness. It ensures narratives accurately reflect insights from typology-specific risk assessments.

- Dynamic Memory Utilization: To conduct precise evaluations, the Compliance Validation Agent accesses critical dynamic memory layers:

- Regulatory Memory: Retrieves updated AML standards, compliance guidelines, and narrative-quality benchmarks to ensure regulatory compliance.

- Historical Narrative Memory: Crossreferences previously approved narratives, ensuring consistency and continuity of narrative structure and quality.

- Typology-Specific Memory: Accesses historical typological insights and past narrative-quality outcomes, verifying the consistency and accuracy of risk assessments.

- Feedback Agent Interaction: Identified narrative-quality concerns or compliance discrepancies are immediately communicated to the Feedback Agent, triggering investigator reviews and iterative narrative refinements, thus maintaining robust human-in-the-loop oversight.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives" (2025-10-09). https://arxiv.org/abs/2509.08380
