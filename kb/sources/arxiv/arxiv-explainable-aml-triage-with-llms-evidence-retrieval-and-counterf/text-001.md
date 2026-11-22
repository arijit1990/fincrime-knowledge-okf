---
type: Source Text
title: 'Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks - part 1 of 3 (pp. 1-10)'
description: 'Verbatim extracted text, pp. 1-10: Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks; Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks > Abstraction; Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks > 2. PROBLEM SETUP & REQUIREMENTS; and 2 more sections'
resource: https://arxiv.org/abs/2604.19755
tags:
- academic_finding
- advanced_analytics
- alerts_triage
- explainability
- global_academic
- preprint
status: stable
source_id: arxiv-explainable-aml-triage-with-llms-evidence-retrieval-and-counterf
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-03-22'
legal_status: unknown
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.19755
  title: 'Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks'
  author: org:arxiv
  last_modified: '2026-03-22T00:00:00Z'
---

# Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2026-03-22), part 1 of 3, pp. 1-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks


[p. 1]

Dorothy Torres*a , Wei Chengb , Ke Hub

aSchool of Science, Technology, Engineering and Mathematics 263 Academy Street, Room S204 Jersey City, NJ 07306

bSchool of Electrical Engineering and Computer Science, The Pennsylvania State University, 207 Electrical Engineering West, University Park, PA 16802, USA

Anti-money laundering (AML) transaction monitoring generates large volumes of alerts that must be rapidly triaged by investigators under strict audit and governance constraints. While large language models (LLMs) can summarize heterogeneous evidence and draft rationales, unconstrained generation is risky in regulated workflows due to hallucinations, weak provenance, and explanations that are not faithful to the underlying decision. We propose an explainable AML triage framework that treats triage as an evidence-constrained decision process. Our method combines (i) retrieval-augmented evidence bundling from policy/typology guidance, customer context, alert triggers, and transaction subgraphs, (ii) a structured LLM output contract that requires explicit citations and separates supporting from contradicting or missing evidence, and (iii) counterfactual checks that validate whether minimal, plausible perturbations lead to coherent changes in both the triage recommendation and its rationale. We evaluate on public synthetic AML benchmarks and simulators and compare against rules, tabular and graph machine-learning baselines, and LLMonly/RAG-only variants. Results show that evidence grounding substantially improves auditability and reduces numerical and policy hallucination errors, while counterfactual validation further increases decision-linked explainability and robustness, yielding the best overall triage performance (PR-AUC 0.75; Escalate F1 0.62) and strong provenance and faithfulness metrics (citation validity 0.98; evidence support 0.88; counterfactual faithfulness 0.76). These findings indicate that governed, verifiable LLM systems can provide practical decision support for AML triage without sacrificing compliance requirements for traceability and defensibility.

### Abstraction


#### 1. INTRODUCTION


[pp. 1-2]

Anti-money laundering (AML) and counter-terrorist financing (CFT) controls are a core pillar of financial system integrity, enforced through regulatory expectations that financial institutions identify, monitor, and report suspicious activity. International standards emphasize a risk-based approach (RBA): controls should be commensurate with exposure, products, customers, and delivery channels, and institutions should demonstrate governance, effective monitoring, and defensible decision-making under supervision[1]–[4] . In practice, this responsibility concentrates pressure on transaction monitoring and alert handling workflows, particularly “triage,” where analysts must rapidly decide whether an alert is explainable as benign behavior, needs escalation for deeper investigation, or should be reported as suspicious.

However, the dominant operational reality of transaction monitoring is high alert volume and high false-positive burden. Industry analyses and qualitative studies repeatedly describe rules-driven monitoring as costly, difficult to tune, and prone to generating large numbers of alerts that rarely convert into actionable cases or suspicious activity reports (SARs), while still requiring time-consuming analyst review and documentation[5], [6] . These inefficiencies have direct implications: analysts spend disproportionate effort on routine, low-risk alerts; institutions face ballooning operational costs; and genuinely risky patterns may be delayed or missed in a queue dominated by noise. Moreover, regulators increasingly expect that decisions—both escalations and closures—are traceable and auditable, especially when monitoring systems incorporate advanced analytics[3], [4] .

Recent FinTech research has increasingly explored how heterogeneous data, machine learning, and language models can support financial decision-making beyond conventional structured indicators. Studies using satellite imagery and spatial signals to analyze Chinese B-share discounts demonstrate the value of alternative data in financial market analysis[7] , while research on analyst following and greenwashing decisions illustrates how financial information environments shape corporate disclosure and ESG-related behavior[8] . In parallel, financial NLP and retrieval-augmented systems have

been developed for financial RAG and financial report question answering, showing that retrieval, reranking, and document-routing mechanisms can improve robustness and precision in finance-specific language tasks[9], [10] . Other studies on cross-market volatility forecasting and volume-price-adjusted MACD trading strategies further reflect the broader trend of using data-driven models for financial risk, market prediction, and trading decision support[11], [12] . These studies collectively show that FinTech systems are moving toward multi-source, model-assisted decision support, but regulated AML triage imposes a stricter requirement: outputs must not only be accurate, but also explainable, auditable, and faithful to the underlying evidence.

[p. 2]

Research has responded with machine learning (ML) and graph-based approaches that model customer and counterparty networks, detect atypical flows, or learn representations of transactional behavior. Early work demonstrates the promise of graph learning for AML by capturing relational structure at scale and highlighting the limitations of pointwise feature engineering when laundering typologies are inherently networked[13] . Similar graph-based modeling ideas have also been applied in other high-volume decision settings, further illustrating the practical value of learning over relational structures[14] . More recent work on uncertainty quantification for graph neural networks and uncertainty-aware spatiotemporal graph modeling further suggests that graph-based systems should not only predict outcomes, but also represent uncertainty in complex temporal and relational environments[15], [16] . This perspective is highly relevant to AML alert triage, where transaction networks are dynamic, labels are imbalanced, and missing or noisy evidence can materially affect risk interpretation.

Yet progress in AML remains constrained by the confidentiality of real bank transaction data, limiting reproducibility and benchmark-driven comparison. To mitigate this, the community has developed and released synthetic data resources: benchmark datasets such as SynthAML10 provide large-scale synthetic alerts and transactions designed specifically to evaluate AML methods under realistic constraints such as imbalance and concept drift[17] , while agent-based simulators such as AMLSim generate transactions with embedded laundering patterns for testing machine learning and graph-based AML methods[18] . More broadly, adjacent financial risk early-warning research has shown the value of integrating heterogeneous signals, including market, network, sentiment, and regulatory information, in rare-event prediction settings, reinforcing the importance of multi-source evidence design for AML decision support[19] . While these efforts enable algorithmic benchmarking, they do not directly solve a persistent pain point for institutions: analyst triage is fundamentally an explanation-and-evidence task, not only a classification task.

Large language models (LLMs) offer a new opportunity to improve triage because they can read heterogeneous, partially structured artifacts—alert narratives, KYC profiles, adverse media snippets, transaction descriptions, internal policy text—and generate coherent rationales. Surveys of financial-domain LLMs highlight rapid progress in domain adaptation, instruction tuning, and specialized evaluation for finance workloads, while also noting deployment challenges such as hallucination, privacy, and reliability under strict compliance requirements[20] . These challenges are particularly acute in AML triage: a plausible-sounding but incorrect rationale is not merely a quality issue; it can become a compliance and model-risk issue if it influences decisions without verifiable grounding. Recent work on intrinsic hallucinations over financial tabular data underscores how small numerical or contextual errors can undermine decisionmaking, especially when the underlying evidence is proprietary and must be handled with precision[21] .

[pp. 2-3]

At the same time, emerging research on LLM systems suggests that reliability depends on system design rather than model capability alone. Work on agentic memory has emphasized the importance of memory structures, retrieval behavior, and evaluation limitations in LLM-based systems[22] , which is directly relevant to AML case memory and prior-alert retrieval. Benchmarking work on LLM agents has also shown the need for multi-metric evaluation rather than single accuracy scores[23] , aligning with the auditability-oriented metrics required in regulated financial workflows. Other studies on dynamic reputation filtering for LLM agents, long-context compression for efficient reasoning, and task-specific efficiency analysis of small versus large language models further highlight practical concerns around credibility, evidence compression, latency, and deployment cost[24]–[26] . These directions motivate a governed LLM architecture in which retrieval, verification, and cost-aware model selection are treated as first-class design requirements.

This paper argues that “LLM-assisted AML triage” must be designed as an evidence-grounded decision support system, not a free-form text generator. We propose an approach that couples (i) evidence retrieval to force citations to institutionapproved sources and (ii) counterfactual checks to test decision robustness. First, we use retrieval-augmented generation (RAG) to bind each triage rationale to a compact set of retrieved documents, such as relevant account history slices,

KYC attributes, prior-case notes, typology guidance, and policy snippets, producing explanations with explicit provenance rather than model-internal assertions. Second, we integrate counterfactual reasoning to evaluate whether the recommended decision is stable under minimal, plausible changes to input facts—an explanation paradigm that has been widely discussed as a practical route to actionable transparency in automated decisions[27] . In the AML setting, counterfactual checks can take the form of “what-if” perturbations aligned with typology logic, such as altering the presence or absence of corroborating risk indicators, adjusting time windows, or removing a key transaction link, and verifying whether the triage conclusion still holds. Recent AML-specific work shows how counterfactual samples can be injected to build probabilistic explanatory structures around black-box detectors, reinforcing the feasibility of counterfactual mechanisms tailored to laundering detection[28] .

Concretely, our paper’s theme is to make LLM explanations auditable by construction and make decisions defensible by stress-testing them with counterfactual checks. We focus on triage because it is the highest-throughput human decision point in the AML pipeline and the place where small efficiency gains and quality improvements compound into large operational and risk impacts. We also emphasize system design choices that are aligned with supervisory expectations for RBA governance, documentation quality, and consistent application across business lines, including banking, securities, and broader FinTech compliance settings.

#### Our contributions are threefold:


[p. 3]

Evidence-grounded triage formulation: We formalize AML triage as a retrieval-grounded explanation task with explicit provenance requirements, building on RAG principles to reduce unsupported assertions. Counterfactual robustness layer: We introduce AML-specific counterfactual checks to probe whether model recommendations are sensitive to minimal, compliance-relevant changes, drawing on counterfactual explanation theory and AML explainability techniques.

Reproducible evaluation blueprint: We outline an evaluation methodology that can be instantiated on public synthetic benchmarks, such as SynthAML10 and AMLSim-derived graphs, to measure triage quality, evidence faithfulness, and robustness under controlled perturbations[17], [18] , while remaining adaptable to private institutional deployments.

The remainder of the paper is organized as follows. Section II reviews related work on AML monitoring, graph learning, financial-domain LLMs, and evidence-grounded decision support. Section III defines the evidence-grounded triage task and system requirements. Section IV presents our RAG-based evidence retrieval design and provenance constraints. Section V introduces counterfactual check construction and decision-robustness metrics. Section VI reports experiments and ablations on synthetic benchmarks and case-style evaluations. Section VII discusses governance, limitations, and deployment considerations under RBA supervision, and Section VIII concludes.

### 2. PROBLEM SETUP & REQUIREMENTS


#### 2.1 AML Triage as a Decision-and-Evidence Task


Financial institutions are expected to implement risk-based AML/CFT controls, including ongoing monitoring and the ability to identify and report suspicious activity, with governance and documentation that can withstand supervisory scrutiny.

In operational transaction monitoring, these expectations materialize as a high-throughput alert triage workflow: given an automatically generated alert (often produced by rules, thresholds, or statistical/ML detectors), an analyst must rapidly determine whether the alert is (i) explainable/benign, (ii) requires continued monitoring, or (iii) should be escalated into a case for deeper investigation and potential reporting. Programs are also expected to consider more than “transactions-only” signals by incorporating customer behavior and attributes—consistent with modern guidance on effective monitoring.

#### 2.2 Inputs and Evidence Sources


[pp. 3-4]

We model each alert 𝑎as a bundle of structured and unstructured information:

a. Alert metadata 𝑚: triggering rule(s)/model score(s), thresholds, time window, and alert type (e.g., structuring, rapid movement of funds, unusual counterparties).

b. Transactional context 𝑇: a sequence or graph of transactions associated with the alert window (amounts, timestamps, channels, counterparties, geography).

c. Customer context 𝐾: KYC and risk-profile attributes (customer type, industry, beneficial ownership signals, onboarding notes, prior alerts/cases). Risk-based guidance stresses that controls should be commensurate with customer risk and context.

d. Policy and typology corpus 𝑃: institution policies, AML typologies, “how we interpret indicators” documents, and monitoring playbooks; monitoring guidance explicitly frames “effective monitoring for suspicious activity” as a program with factors beyond a one-size-fits-all template.

e. Case memory 𝐻: prior internal cases and dispositions (when available), plus curated exemplars.

We denote the retrievable evidence pool as ℰ= {𝐸𝑃, 𝐸𝐾, 𝐸𝑇, 𝐸𝐻}, where each evidence item carries a unique identifier, timestamp, source type, and access-control tag.

#### 2.3 Output Space and Explainable Triage Objective


[p. 4]

The system produces a structured triage output:

Disposition 𝑦∈{dismiss,monitor,escalate}(or an institution-specific label set),

Confidence / uncertainty 𝑢(calibrated score or interval),

Rationale 𝑟(natural language explanation),

Evidence set 𝑆⊆ℰ(explicit citations that support each major claim in 𝑟), and

Next actions 𝐴(e.g., “request missing information,” “expand lookback window,” “check related accounts”), consistent with investigative best practices.

Because AML decisions are accountable and must be defensible under a risk-based regime, we treat the primary optimization goal as evidence-grounded decision support rather than unconstrained text generation:

maximize TriageQuality(𝑦)subject to Auditability(𝑟, 𝑆), PolicyConsistency(𝑟, 𝑃), DataMinimization.

These constraints reflect the governance emphasis in international standards and banking supervision guidance.

#### 2.4 Counterfactual Checks for Faithful Explanations


A central thesis of this paper is that an explanation should be faithful to the evidence and decision logic: if a minimal, plausible change to key facts should flip the triage decision, then the system should (a) surface that condition and (b) respond consistently when that counterfactual is applied.

We define a set of counterfactual transformations Δthat alter a small subset of features or evidence availability while remaining plausible under AML typology logic (e.g., removing one key high-risk counterparty link; changing the presence of structuring indicators; narrowing the alert window). A counterfactual check evaluates:

a. Decision sensitivity: whether 𝑓(𝑎)changes as expected under Δ, and

b. Rationale alignment: whether the evidence cited in 𝑆changes coherently with the altered facts (e.g., the system should not continue citing a removed evidence item).

AML-focused counterfactual explainability has been explored in prior work (e.g., using counterfactual samples to build explanatory structures), motivating counterfactual mechanisms as more than post-hoc narratives.

#### 2.5 System Requirements


We distill requirements from AML governance expectations and “effective monitoring” guidance into implementable constraints.

Every material claim in the rationale must be grounded in retrievable evidence items with stable identifiers (policy snippet, KYC field, transaction subgraph, prior-case excerpt). This supports auditability and aligns with risk-based expectations for governance and defensible monitoring decisions.

The system must reflect institution policies and typologies (and avoid inventing policy). Guidance on effective monitoring stresses program factors and contextual analysis beyond one-size-fits-all heuristics.

R3. Counterfactual faithfulness checks.

#### R2. Policy-consistent decision support.


[pp. 4-5]

The system must support “what-if” perturbations and verify that decision + rationale change coherently when key inputs change, reducing brittle or non-faithful explanations. (We operationalize this using counterfactual transformations and validation metrics.)

Only the minimum necessary evidence should be retrieved and exposed for triage, consistent with supervisory expectations to manage ML/TF risks through appropriate controls and governance.

AML alert streams are highly imbalanced and often incomplete; the system should degrade gracefully (e.g., express uncertainty and recommend next actions) rather than hallucinate missing facts. Benchmark datasets are explicitly designed to stress AML methods under practical constraints such as imbalance.

#### R5. Robustness to missing, noisy, and imbalanced signals.


[p. 5]

R6. Low hallucination risk for numbers and timelines.

Amounts, timestamps, thresholds, and ordering are core to AML typology reasoning; the system must include numerical and temporal consistency checks and avoid fabricating figures, consistent with known failure modes of LLMs over financial tabular content.

Outputs must be structured for analyst review: concise disposition, prioritized evidence, explicit unknowns, and recommended next steps. Monitoring guidance emphasizes program effectiveness and contextual analysis; triage tooling must therefore be built to support, not obscure, human judgment.

R8. Reproducible evaluation under limited real-data access.

#### R7. Human-in-the-loop usability.


Because real transaction data is rarely shareable, the evaluation should be reproducible on public synthetic resources (e.g., SynthAML10) and/or simulators (e.g., AMLSim) that encode laundering patterns and enable controlled stress tests.

We propose an explainable AML triage framework (figure 1) that treats triage as an evidence-constrained decision process rather than free-form text generation. Given an alert 𝑎, the system outputs (i) a triage disposition 𝑦∈ {dismiss,monitor,escalate}, (ii) a structured rationale 𝑟whose key claims are explicitly grounded in retrieved evidence items, and (iii) a set of validated counterfactual conditions 𝐶describing minimal, plausible changes to the alert context that would alter the recommended outcome. The method is built around three components that operate end-to-end: an evidence retrieval module that constructs a compact “evidence bundle” from heterogeneous sources, an LLM module that produces a decision and an audit-ready rationale under strict provenance constraints, and a counterfactual-check module that probes the faithfulness and robustness of the decision and explanation through minimal perturbations. This design follows the general retrieval-augmented generation (RAG) principle that grounding model outputs in nonparametric retrieved context can improve factuality, provenance, and updatability. We further adopt counterfactual reasoning as a validation instrument: counterfactual explanations provide actionable, decision-linked conditions without requiring access to the internal mechanics of the underlying model, which makes them well-suited for regulated decision support.

### 3. METHOD


#### 3.1 Overview


[p. 6]

Figure 1: AML Triage Architecture

We represent every retrievable artifact as an evidence item 𝑒∈ℰwith a stable identifier, a source type, an effective timestamp, and an access-control label (ACL). Evidence types include (i) policy and typology guidance, (ii) customer and KYC profile attributes, (iii) alert trigger metadata (e.g., rule identifiers, thresholds, scoring outputs), (iv) transaction slices and/or transaction subgraphs associated with the alert window, and (v) similar historical cases or investigator notes when available. Each item has a canonical text form used for retrieval and citation, plus optional structured fields (e.g., amounts, timestamps, counterparties) used for validation and consistency checks. Retrieval is implemented as a hybrid of structured filtering and semantic search: structured constraints restrict candidates by customer ID, alert time window, rule type, geography, product line, and ACL, while semantic retrieval ranks the remaining candidates by relevance to a query derived from the alert context.

#### 3.2 Evidence Representation and Retrieval


[pp. 6-7]

Given an alert 𝑎, the retriever returns an evidence bundle 𝐵(𝑎)designed to be both compact and coverage-preserving, i.e., it should capture the minimal set of items that a human investigator would want to see to justify a triage decision. Concretely, we partition 𝐵(𝑎)by evidence type to ensure that the LLM has access to complementary perspectives rather than a single narrow source. We also enforce practical constraints to reduce redundancy and stale information. First, we apply deduplication and diversity-aware selection so that near-duplicate items do not dominate the bundle. Second, we prioritize time-consistent policy materials by preferring the most recent effective versions and excluding superseded items where possible. Third, we apply hard ACL filtering so that disallowed evidence is never retrieved into the model

context. In doing so, the retrieval stage becomes the primary mechanism for controlling both the factual scope and the compliance boundary of the downstream generation step.

#### 3.3 LLM-Based Triage Under Provenance Constraints


[p. 7]

The LLM is not asked to “write an explanation” in the open-ended sense. Instead, it is constrained to produce a structured triage record that is auditable and verifiable. Specifically, the model outputs: the disposition 𝑦, a calibrated confidence or uncertainty indicator, a ranked list of suspected typologies (optional but useful for workflow routing), a short rationale 𝑟, and explicit evidence citations 𝑆⊆𝐵(𝑎)that support each material claim. To prevent the model from constructing persuasive but ungrounded narratives, we require that (i) every paragraph in 𝑟contains at least one evidence reference, and (ii) the model explicitly separates supporting evidence from contradicting or missing evidence. This separation matters operationally: in AML triage, uncertainty and absence of corroboration are often as decision relevant as positive indicators, and investigators must be able to see what is known versus what remains unclear.

We implement these constraints by presenting 𝐵(𝑎)to the model as labeled evidence blocks (policy, KYC, alert triggers, transactions, similar cases), each with stable evidence IDs, and by instructing the model to reference only those IDs when making factual assertions. After generation, a verifier checks basic provenance, integrity and consistency. Provenance integrity requires that all cited evidence IDs exist in the supplied bundle and that no citations are fabricated. Consistency checks validate that key numerical and temporal claims (amounts, dates, ordering, threshold comparisons) align with the retrieved evidence text or structured fields. If any check fails, the system returns targeted feedback to the model (e.g., “you referenced an evidence ID that is not present” or “your total amount conflicts with evidence e_T3”) and regenerates a corrected output. This verification-and-repair loop operationalizes a core benefit of RAG systems, explicit traceability of claims to sources, while making the output more robust for audit and review.

Figure 2. Evidence bundle construction and provenance constraints.

#### 3.4 Counterfactual Checks for Faithfulness and Robustness


[p. 8]

Grounded citations alone do not guarantee that the explanation is faithful to the decision logic. A model can cite relevant-looking passages while still basing its decision on spurious cues, or it can maintain the same conclusion even when the key factor it claims to rely on is removed. To address this, we introduce a counterfactual-check module that treats counterfactual reasoning as a validation layer. Counterfactual explanations, in their canonical form, express actionable minimal changes that would alter an automated decision; they have been argued to provide practical transparency without opening the black box. In AML, such counterfactuals are particularly meaningful because typologies are often expressed as combinations of conditions (e.g., structuring signals, unusual counterparty risk, rapid movement of funds), and investigators routinely ask, “what would make this clearly benign or clearly suspicious?” We consider two complementary counterfactual families. The first family comprises decision counterfactuals, which search for minimal plausible edits 𝛿to the alert context such that the disposition flips: 𝑓(𝑎⊕𝛿) ≠𝑓(𝑎). These edits are restricted to a small, domain-reasonable set of manipulable factors, such as toggling the presence of a key indicator that the system claims is central (e.g., a structuring pattern), adjusting a counterparty risk tier, narrowing or widening a time window within policy limits, or removing a single suspicious path in the transaction graph representation. The purpose is not to “game” the system but to check whether the stated drivers of the decision are truly decision relevant. The second family comprises evidence counterfactuals, which remove or substitute a key evidence item 𝑒\* from the bundle and test whether (i) the model’s disposition and rationale react appropriately, and (ii) the explanation ceases to rely on citations that are no longer available. This is a direct test against “decorative citations”: if the model continues to cite or implicitly depend on removed evidence, then its explanation is not faithful.

Counterfactual generation is performed in a constrained manner. We first extract the system’s claimed decision drives from the triage record, including the top supporting evidence IDs and any explicitly listed indicators. Conditioned on these drivers, the model proposes a small set of candidate counterfactual edits that are bounded by an edit budget (to encourage minimality) and validated by plausibility rules (to prevent impossible or nonsensical perturbations such as negative amounts or inconsistent timestamps). Each candidate is then validated by a triage validator, which can be instantiated as a policy-approximate rules engine and/or a lightweight scoring model trained on available labels. A candidate is accepted only if it produces a meaningful change in the validator’s risk score or disposition (flip validity), and if a re-run of the LLM on the counterfactual context yields a rationale whose citations and stated drivers align with the modified facts (rationale alignment). This perspective is consistent with prior AML explainability work that leverages counterfactual constructions to build explanatory structures around laundering detection.

#### 3.5 End-to-End Procedure


[p. 9]

End-to-end, the workflow proceeds as follows. For each alert 𝑎, we retrieve a permission-aware evidence bundle 𝐵(𝑎)with coverage guarantees across policy, customer context, triggers, and transactions. The LLM then produces a structured triage record constrained to cite only evidence items in 𝐵(𝑎). A verifier checks provenance integrity and numerical/temporal consistency; failed outputs are repaired through targeted feedback and regeneration. Next, the counterfactual module proposes minimal, plausible perturbations derived from the model’s stated drivers and validates them using a triage validator; accepted counterfactuals are those that both produce the expected decision change and induce aligned updates in rationale and citations. The final output includes disposition, confidence, evidence-linked rationale, explicit unknowns, recommended next actions, and a small set of validated counterfactual conditions that make the recommendation more transparent and auditable.

### 4. DATASETS & EXPERIMENTAL SETUP


#### 4.1 Datasets


[p. 10]

To ensure reproducibility under the practical constraint that real bank transaction data is rarely public, we evaluate primarily on public synthetic AML benchmarks that preserve key operational properties (large-scale transactional volume, strong class imbalance, and realistic alert-generation artifacts). Our main dataset is SynthAML10, released as a benchmarking resource for statistical and machine-learning AML methods. SynthAML10 is generated by fitting a probabilistic model to confidential bank data (from Spar Nord) and then sampling synthetic transactions and alerts at scale; it contains over 16 million transactions and 20,000 AML alerts across two tables, enabling both transaction-level and alert-level modeling.

In addition, we use AMLSim as a controllable simulator to generate transaction networks with known laundering patterns (typologies) and to support stress tests that require intervention on the underlying generative factors (e.g., removing a laundering motif or weakening an indicator). AMLSim is an open-source, multi-agent simulator originally designed to generate synthetic banking transactions together with embedded laundering behaviors for testing ML and graph algorithms.

As an optional external validity check (particularly relevant when positioning the method as “FinTech broadly,” including crypto compliance), we also consider the Elliptic Bitcoin transaction graph dataset, which provides an anonymized transaction graph with licit/illicit labels and is widely used for AML-style graph classification benchmarks.

#### 4.2 Task Definition and Labels


We frame AML triage as an alert-level decision problem. For each alert 𝑎, the model outputs a disposition 𝑦∈ {dismiss,monitor,escalate}plus an evidence-linked rationale. Since public AML datasets typically provide labels that are closer to “suspicious vs. non-suspicious” than to institution-specific triage states, we operationalize a standard mapping that supports a realistic triage workflow: alerts labeled as suspicious (or associated with laundering typologies in the simulator) are treated as “escalate,” while clearly normal alerts are treated as “dismiss,” and ambiguous or borderline cases can be assigned to “monitor” either via a calibrated score band or a predefined policy threshold. This mapping is kept explicit in the experimental protocol so that comparisons remain fair and reproducible across methods.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks" (2026-03-22). https://arxiv.org/abs/2604.19755
