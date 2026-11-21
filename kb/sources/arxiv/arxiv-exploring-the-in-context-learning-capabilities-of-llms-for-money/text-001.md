---
type: Source Text
title: Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs - part 1 of 1 (pp. 1-4)
description: 'Verbatim extracted text, pp. 1-4: Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs; Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs > I. INTRODUCTION; Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs > _A. Financial Graph Representation and Subgraph Extraction_; and 9 more sections'
resource: https://arxiv.org/abs/2507.14785
tags:
- academic_finding
- explainability
- genai
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-exploring-the-in-context-learning-capabilities-of-llms-for-money
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-07-20'
legal_status: unknown
part: 1
parts_total: 1
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2507.14785
  title: Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs
  author: org:arxiv
  last_modified: '2025-07-20T00:00:00Z'
---

# Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs

[source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2025-07-20), part 1 of 1, pp. 1-4. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs


[p. 1]

Erfan Pirmorad

_The Vanguard Group, Inc._ erfan pirmorad@vanguard.com

_Abstract_ —The complexity and inter-connectivity of entities involved in money laundering demand investigative reasoning over graph-structured data. This paper explores the use of large language models (LLMs) as reasoning engines over localized subgraphs extracted from a financial knowledge graph. We propose a lightweight pipeline that retrieves k-hop neighborhoods around entities of interest, serializes them into structured text, and prompts an LLM via few-shot in-context learning to assess suspiciousness and generate justifications. Using synthetic antimoney laundering (AML) scenarios that reflect common laundering behaviors, we show that LLMs can emulate analyst-style logic, highlight red flags, and provide coherent explanations. While this study is exploratory, it illustrates the potential of LLM-based graph reasoning in AML and lays groundwork for explainable, language-driven financial crime analytics.

_Index Terms_ —Anti Money Laundering (AML), In-context Learning, Large Language Model (LLM), Financial Graph

### I. INTRODUCTION


As financial data becomes increasingly interconnected, institutions are turning to knowledge graphs to capture the complex relationships between customers, accounts, transactions, devices, and geographic entities. These graphs provide a rich structure for reasoning about risk, behavior, and anomalies. However, leveraging their full potential requires tools capable of understanding and explaining multi-hop, heterogeneous patterns.

Recent advances in large language models (LLMs) have demonstrated their ability to reason over structured data, including relational chains and graph-like abstractions. A growing body of research has shown that LLMs can be adapted to perform graph reasoning tasks via graph-structured prompting [4], or language-guided message passing [9]. Surveys on this topic highlight a promising direction for unifying natural language and graph reasoning under a shared framework [8].

Building on this momentum, we explore whether LLMs can support investigative-style reasoning over _financial knowledge graphs_ . These graphs represent real-world financial systems, where relational complexity is not only common but essential to risk analysis, trend analysis, etc., [5]. Our goal is to evaluate the feasibility of using LLMs as interpretable reasoning engines over such data. As a motivating case study, we focus on anti-money laundering (AML) in this study. AML is a domain where identifying suspicious behavior involves tracing

©2025 The Vanguard Group, Inc. All rights reserved.

intricate financial flows across individuals, shell entities, and intermediary accounts [2], [3]. AML and financial crime investigations increasingly rely on graph-based representations to detect patterns such as layering, rapid movement of funds, and shared infrastructure [6], [7].

For this study, we utilize the publicly available IBM AML Synthetic Dataset [1], which simulates financial activities through a realistic knowledge graph of accounts, banks, and transactions, designed to model common laundering typologies based on real-world intelligence. This allows us to explore LLM-based reasoning in a controlled yet representative environment.

This work positions LLMs not merely as text generators, but as _in-context reasoning engines_ capable of interpreting graph-structured financial activity. In-context learning offers a flexible, parameter-free mechanism to inject domain knowledge and reasoning capabilities into black-box LLMs, aligning naturally with investigative workflows. By leveraging this mechanism, we evaluate whether LLMs can emulate analyststyle reasoning in AML detection without retraining or labeled supervision.

Our pipeline (Fig. 1) extracts a k-hop subgraph, serializes it into structured text, and prompts an LLM in a few-shot setup to classify suspiciousness and provide human-readable justification.

Fig. 1. Pipeline Overview for LLM-based AML Analysis.

We evaluate this pipeline using synthetic AML scenarios that reflect realistic laundering behaviors, constructed from

[p. 2]

publicly available datasets. Our early results indicate that LLMs can highlight meaningful red flags, trace multi-step patterns, and generate rationales that align with human intuition. This case study illustrates the potential of LLMs for reasoning over financial knowledge graphs, offering a path toward explainable, language-driven fraud analytics. To our knowledge, this is the first work to apply in-context learning with LLMs for money laundering detection over financial graphs. The proposed pipeline bridges localized graph structure with natural language reasoning in a scalable and interpretable way.

We propose a three-stage framework: (1) extract subgraphs around suspicious transactions, (2) serialize them into text, and (3) prompt an LLM with laundering typologies in a few-shot setup. The model outputs suspiciousness, rationale, and typology, letting us evaluate classification accuracy and reasoning transparency.

### _A. Financial Graph Representation and Subgraph Extraction_


Money laundering schemes often involve complex transactional relationships that can be naturally represented as graphs. In this work, we use the publicly available IBM AML Synthetic Dataset [1], which models financial activities as a knowledge graph. In this graph, nodes represent _accounts_ (individual or corporate) and _banks_ , while edges represent _financial transactions_ between accounts. Each node is annotated with metadata such as entity type and account creation date; each transaction edge is labeled with attributes including transaction amount and timestamp.

Our goal is to reason about the suspiciousness of specific transactions by analyzing the surrounding graph structure. For each candidate transaction (i.e., a transfer between two accounts), we extract a localized _k_ -hop subgraph centered on the transaction edge. The subgraph includes the source and destination accounts, their neighboring transactions within _k_ hops, and any associated bank nodes. An example of an extracted subgraph is shown below. Each extracted structure provides the LLM with a focused local context to assess whether the transaction may reflect suspicious activity.

Fig. 2. Snapshot of a sample 2-hop subgraph centered around a transaction between _acct_ _80FF89190_ and _acct_ _810147BB0_ .

This extraction strategy frames the detection task as an _edge-centric classification problem_ over the transaction graph, where the objective is to predict whether the given transaction edge represents money laundering activity.

### _B. Textual Serialization_


Each subgraph is serialized into structured text: nodes as tagged entities and edges as relations with direction, amounts, and timestamps. Example:

- Serialized Subgraph Example Nodes: - acct_810147BB0 (type: Account) - acct_8101A5D70 (type: Account) - acct_811416D0 (type: Account) - acct_8117F9960 (type: Account) - acct_80FF8910 (type: Account) - bank_217 (type: Bank) - bank_4049 (type: Bank) Edges: - acct_810147BB0 belongs_to bank_217 - acct_810147BB0 transfers_to acct_8101A5D70 amount: 225756.22 Shekel via: Reinvestment timestamp: 2022/09/01 00:02

- _...additional edges omitted for brevity..._

### _C. Few-Shot Prompting with AML Typologies_


[pp. 2-3]

A defining characteristic of anti-money laundering (AML) investigations is the presence of recurring structural patterns in transactional behavior. Some of these patterns have been studied and documented in financial intelligence reports and academic studies, including the IBM AML dataset, which models them as prototypical graph topologies. Figure 3 visualizes eight canonical laundering structures used in our prompting framework: (a) _fan-out_ , (b) _fan-in_ , (c) _gatherscatter_ , (d) _scatter-gather_ , (e) _simple cycle_ , (f) _random_ , (g) _bipartite_ , and (h) _stack_ .

Fig. 3. Canonical money laundering patterns used as reasoning demonstrations. Image adapted from the IBM AML dataset paper.

To help the LLM learn to reason over financial subgraphs, our approach uses a few-shot prompting setup where each demonstration example showcases one of these laundering patterns. Each example consists of (i) a brief serialized subgraph in the textual format described in Section II-B, and (ii) a natural language rationale that explains why the activity is suspicious, grounded in the structure of the graph. Both the graph serialization and the rationale are derived from samples in the IBM AML dataset, which provides well-annotated synthetic cases.

The prompt includes eight such examples, each corresponding to one of the patterns shown in Figure 3, before appending the test case. By explicitly conditioning the LLM on real-world-style typologies and human-readable rationales, we align the reasoning process with investigative workflows. Importantly, these demonstrations emphasize graph topology and multi-hop interactions rather than superficial statistical cues, which makes the model more likely to generalize beyond seen entities.

This methodology leverages the core advantage of few-shot learning via in-context learning: enabling the model to acquire

structural priors without any fine-tuning. It effectively bootstraps the LLM into a role akin to a fraud analyst by showing what suspicious behavior “looks like” in multiple formats. The choice to use real pattern types, realistic transactions, and natural language justifications makes the prompting setup robust, interpretable, and well-aligned with human investigator expectations. To further refine the model’s discrimination ability, we also include several examples of non-suspicious financial activity—subgraphs that contain no red flags—within the same prompt. This ensures that the model learns not only to detect suspicious patterns, but also to distinguish them from legitimate transactional behavior.

The final structure of the LLM prompt follows the template below, showing how demonstration subgraphs and rationales are interleaved. The subgraphs are serialized using the format shown previously in the _Serialized Subgraph Example_ box in Section II-B.

### Final Prompt Template


[p. 3]

|Prompt Header:You are an expert financial crime investigator reviewingpatterns of financial activities and behaviors ofinvolved accounts to identify potential cases of moneylaundering. The data is represented as a graph, where:- Nodes are of type Account or Bank.- Edges represent relationships of type transfers_toor belongs_to, and include metadata such as amount,currency, payment method, and timestamp.|
|---|
|For training purposes, you will be shown examplesof subgraph typologies that are known to be eithersuspicious (indicative of laundering tactics) ornon-suspicious (routine financial activity). Thesetypologies illustrate common structural patterns infinancial networks.|
|Few-shot Examples:>|
|Explanation: This pattern resembles fan-out behavior,where a single account disperses funds to many accountswithin a short window, often to obscure the origin.>|
|Explanation: This reflects a gather-scatter pattern,where funds from multiple sources converge briefly beforedispersing again, which is a common layering tactic.... (examples 3 through 7 omitted for brevity) ...|
|>Explanation: A highly connected bipartite structure,consistent with mule networks or coordinated burstactivity.|
|non-suspicious Examples:>|
|Explanation: These transfers occur across a regularschedule, between known parties with consistent values.No indicators of laundering behavior.|
|... (examples 2 through 4 omitted for brevity) ...|
|Task: Given a transaction (edge) with Transaction ID, along with its surrounding subgraph, determine|
|whether the transaction is suspicious, or not suspicious.Your reasoning should be based on whether the surroundingsubgraph resembles any of the suspicious typologiesprovided in the examples.Test Example:>Answer Format:- Conclusion: Suspicious or Not Suspicious- Explanation: (2-3 sentences reasoning)- Observed Pattern: (e.g., gather-scatter)|

### III. EXPERIMENTS AND RESULTS


We evaluate the proposed reasoning pipeline on the AML HI Small dataset, which simulates real-world money laundering typologies through graph-structured financial transactions. Our primary goal at this stage is to assess both the

classification ability and the reasoning quality of a large language model (LLM) over structured financial subgraphs.

We construct a balanced evaluation set consisting of 2,000 examples: 1,000 laundering transactions and 1,000 nonlaundering transactions. While this does not reflect the class imbalance typically observed in real-world AML investigations, it enables a controlled evaluation of the model’s ability to distinguish suspicious patterns without being dominated by prior class frequencies. This design isolates the core reasoning capabilities of the LLM pipeline and ensures that performance metrics reflect meaningful classification behavior rather than dataset skew. Extending the evaluation to realistic, highly imbalanced distributions remains an important direction for future work. Each subgraph is serialized following the format described in Section II-B and embedded into the final prompt template described in Section II-C. The prompt includes eight suspicious pattern examples and four non-suspicious examples, with task instructions asking the model to: (1) classify the subgraph as suspicious or not suspicious, and (2) list any observed money laundering patterns. We use the GPT4o model accessed via the OpenAI API (temperature = 0). Each test sample is independently prompted with no carryover memory.

### _B. Sample Model Output_


Below we present a representative output generated by the LLM for a test subgraph classified as suspicious:

Conclusion: Suspicious Explanation: Transaction ID ‘3064852‘ is part of a networks that exhibits characteristics of fan-out. The originating account ‘acct_8089DC420‘ rapidly transfers large amounts to multiple accounts across different banks, including the target account ‘acct_807051670‘. The high volume of transactions, diverse endpoints, and rapid movement suggest layering and potential laundering activity. Observed Pattern: fan-out

Given the computational cost of LLM inference at scale, rerunning the model over multiple randomized test sets was infeasible. Instead, to assess the robustness of our results without incurring additional inference cost, we apply bootstrap resampling over the fixed set of 2,000 model outputs. Specifically, we generate 1,000 bootstrap samples (sampling with replacement) and recompute key evaluation metrics for each resample. This procedure allows us to estimate the mean and 95% confidence intervals for classification accuracy, precision, and recall. Reporting confidence intervals provides insight into the stability of both classification and reasoning performance. Table I summarizes the model’s binary classification performance.

### _C. Classification Performance_


[pp. 3-4]

To evaluate the model’s reasoning quality and tendency to hallucinate patterns, we measure the precision and recall of the patterns listed by the LLM relative to ground-truth pattern labels provided by the IBM dataset.

TABLE I

CLASSIFICATION PERFORMANCE WITH 95% CONFIDENCE INTERVALS

|Metric|Value (95% CI)|
|---|---|
|Overall Accuracy|63.7% _±_ 3.3%|
|Precision|62.7% _±_ 4.4%|
|Recall|67.7% _±_ 4.4%|

TABLE II

PATTERN RECOGNITION PERFORMANCE (PER PATTERN) WITH 95% CONFIDENCE INTERVALS

|Pattern|Precision (95% CI)|Recall (95% CI)|
|---|---|---|
|Fan-out|75.1% _±_ 4.0%|80.3% _±_ 3.8%|
|Fan-in|73.8% _±_ 4.1%|81.5% _±_ 4.0%|
|Gather-scatter|66.2% _±_ 4.5%|70.7% _±_ 4.3%|
|Scatter-gather|64.9% _±_ 4.5%|68.8% _±_ 4.3%|
|Simple cycle|62.5% _±_ 4.6%|65.9% _±_ 4.5%|
|Random|51.5% _±_ 5.0%|53.5% _±_ 4.9%|
|Bipartite|55.0% _±_ 5.0%|56.1% _±_ 5.0%|
|Stack|52.0% _±_ 5.1%|58.0% _±_ 5.0%|

Detection performance generally reflects the underlying structural complexity of the laundering patterns. Highly organized patterns such as _fan-out_ and _fan-in_ achieve the strongest results, while moderately complex patterns like _gather-scatter_ , _scatter-gather_ , and _simple cycle_ show intermediate performance. Among the harder patterns, such as _random_ , _bipartite_ , and _stack_ , we observe some variability, reflecting the increased difficulty in consistently capturing less structured behaviors. Overall, these preliminary findings suggest that prompting LLMs over serialized financial graphs provides a viable pathway for both suspicious activity classification and explainable pattern-driven reasoning.

### IV. CONCLUSION AND FUTURE WORK


[p. 4]

In this paper, we explored the feasibility of using large language models (LLMs) to perform structured reasoning over financial knowledge graphs for anti-money laundering (AML) investigations. By constructing localized subgraphs around transactions, serializing them into textual prompts, and conditioning the LLM with a few-shot setup based on canonical laundering patterns, we demonstrated that LLMs can not only classify suspicious behavior but also provide interpretable rationales for their decisions through in-context learning.

While this work presents an initial exploration rather than a production-ready system, it is not intended as a fully benchmarked replacement for existing graph-based fraud detection methods. Instead, our goal was to assess the feasibility and interpretability of in-context LLM reasoning over financial knowledge graphs. This study provides a conceptual foundation for hybrid approaches that integrate explainability and investigative logic, while also recognizing that computational and scalability challenges must be addressed for future practical deployments. One of the most important advantages of this approach is its strong interpretability. Unlike traditional graph neural networks (GNNs) or other embedding-based methods,

which often act as black boxes, the LLM produces humanreadable explanations that align with investigative reasoning. This opens the door for models that are not only accurate but also transparent and auditable, addressing a key pain point in the deployment of machine learning systems for financial crime detection.

While promising, the approach also presents practical limitations. In particular, the computational cost of prompting large language models at inference time makes it impractical as a stand-alone solution for large-scale production. Instead, we envision a hybrid system where a lightweight classifier, such as a GNN or a graph feature engineering model with a gradient boosting classifier, performs initial triage. Only cases with low classification confidence (borderline decisions) are escalated to the LLM for additional reasoning. This selective invocation strategy maintains scalability while leveraging LLM-generated rationales to improve decision quality and explainability. In future work, we plan to benchmark such systems and assess their impact on detection performance and transparency. We will also explore whether smaller LLMs, fine-tuned for financial graph reasoning, can deliver similar interpretability with significantly reduced computational overhead. These steps will help unlock scalable, interpretable, and effective fraud and financial crime detection systems for real-world environments.

### DISCLAIMER


This material is provided for informational purposes only and is not intended to be investment advice or a recommendation to take any particular investment action.

- [1] Erik Altman, Jovan Blanuˇsa, Luc von Niederh¨ausern, B´eni Egressy, Andreea Anghel, and Kubilay Atasu. Realistic synthetic financial transactions for anti-money laundering models. In _Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Datasets and Benchmarks Track_ , 2023.

- [2] Zhiyuan Chen, Le Dinh Khoa, Ee Na Teoh, Amril Nazir, Ettikan Kandasamy Karuppiah, and Kim Sim Lam. Machine learning techniques for anti-money laundering (aml) solutions in suspicious transaction detection: a review. _Knowl. Inf. Syst._ , 57(2):245–285, November 2018.

### REFERENCES


- [3] Jenny Domashova and Natalia Mikhailina. Usage of machine learning methods for early detection of money laundering schemes. _Procedia Computer Science_ , 190:184–192, 2021. 2020 Annual International Conference on Brain-Inspired Cognitive Architectures for Artificial Intelligence: Eleventh Annual Meeting of the BICA Society.

- [4] Bahare Fatemi, Jonathan J. Halcrow, and Bryan Perozzi. Talk like a graph: Encoding graphs for large language models. _ArXiv_ , abs/2310.04560, 2023.

- [5] Xiaohui Victor Li and Francesco Sanna Passino. Findkg: Dynamic knowledge graphs with large language models for detecting global trends in financial markets. In _International Conference on AI in Finance_ , 2024.

- [6] Soroor Motie and Bijan Raahemi. Financial fraud detection using graph neural networks: A systematic review. _Expert Systems with Applications_ , 240:122156, 2024.

- [7] Berkan Oztas, Deniz Cetinkaya, Festus Adedoyin, Marcin Budka, Gokhan Aksu, and Huseyin Dogan. Transaction monitoring in anti-money laundering: A qualitative analysis and points of view from industry. _Future Generation Computer Systems_ , 159:161–171, 2024.

- [8] Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, and Xindong Wu. Unifying large language models and knowledge graphs: A roadmap. _IEEE Transactions on Knowledge and Data Engineering_ , 36:3580–3599, 2023.

- [9] Bryan Perozzi, Bahare Fatemi, Dustin Zelle, Anton Tsitsulin, Mehran Kazemi, Rami Al-Rfou, and Jonathan J. Halcrow. Let your graph do the talking: Encoding structured data for llms. _ArXiv_ , abs/2402.05862, 2024.


---

[source overview](overview.md)

[^original]: arXiv, "Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs" (2025-07-20). https://arxiv.org/abs/2507.14785
