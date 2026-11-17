---
type: Source Text
title: 'Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks - part 2 of 3 (pp. 10-16)'
description: 'Verbatim extracted text, pp. 10-16: Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks > 4. DATASETS & EXPERIMENTAL SETUP; Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks > 5. EVALUATION; Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks > 6. Results & Analysis; and 3 more sections'
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
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2604.19755
  title: 'Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks'
  author: org:arxiv
  last_modified: '2026-03-22T00:00:00Z'
---

# Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2026-03-22), part 2 of 3, pp. 10-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks


### 4. DATASETS & EXPERIMENTAL SETUP


#### 4.3 Evidence Corpus Construction for Retrieval


[p. 10]

Because the method is retrieval-augmented, we must define what is retrievable and auditable. We construct a policy/typology corpus 𝑃as short, indexed documents that capture “what indicators matter and why,” written at the level of typical AML monitoring playbooks (e.g., structuring, rapid movement, high-risk counterparties). Each policy document is versioned and timestamped to enable time-consistency checks (e.g., retrieval must prefer the latest effective version).

For case-based retrieval 𝐻, we create a “case memory” by sampling training alerts with their associated transaction contexts and (where available) short human-readable summaries. In SynthAML10, this is implemented by generating standardized case summaries from structured features (e.g., top counterparties, concentration, unusual time patterns) to emulate a realistic case-note index without leaking test labels into retrieval. In AMLSim, case notes can be generated directly from the simulator’s typology annotations. This case memory enables similarity retrieval baselines and supports the proposed “evidence counterfactual” tests by allowing removal/substitution of specific evidence items.

#### 4.4 Data Splits and Leakage Control


To avoid optimistic bias that can arise from random splits in time-evolving transactional systems, we adopt a timeaware split whenever timestamps are available. Concretely, we sort alerts by alert time and allocate the earliest 70% to training, the next 10% to validation, and the latest 20% to test. This protocol better matches operational deployment where models are trained on past behavior and used on future alerts. We additionally enforce retrieval leakage controls : when constructing case memory for retrieval, we index only training-set cases, and we prevent any direct inclusion of test labels or post-decision artifacts in the retrievable text. These controls are especially important in RAG settings because retrieval can otherwise become an inadvertent label channel.

#### 4.5 Baselines


[pp. 10-11]

We compare the proposed system against a set of baselines that reflect both industry practice and research norms:

1. Rules / score-only baseline: a threshold-based disposition derived from alert scores or simple heuristics, representing a minimal monitoring configuration.

2. Tabular ML baseline: a gradient-boosted model (or logistic regression where appropriate) trained on alert-level aggregated features (amount statistics, counterparty counts, temporal burstiness).

3. Graph ML baseline: a transaction-graph model (e.g., GCN/GraphSAGE-style) trained to predict suspiciousness using local neighborhoods; graph learning has been explored for AML forensic analysis and motivates this baseline family.

4. LLM-only baseline: the LLM generates triage decisions and rationales from a fixed, non-retrieval prompt using only the alert summary and transaction slice (no external evidence).

5. RAG without counterfactual checks: retrieval-augmented generation with provenance constraints, but without the counterfactual validation layer (ablation to isolate the benefit of counterfactual checks).

6. Ours (RAG + counterfactual checks): the full pipeline described in Section 3.

#### 4.6 Model and Retrieval Configuration


[p. 11]

To reflect realistic deployment choices, we evaluate two representative LLM settings: a high-capacity general-purpose LLM and a smaller, cost-efficient LLM (or an open-source instruct model) to study the performance–cost tradeoff. The retrieval subsystem is implemented as a hybrid retriever with (i) structured filtering (time window, customer ID, alert type, ACL) and (ii) dense semantic ranking over the evidence corpus. Unless otherwise stated, we retrieve a compact bundle of 𝑘evidence items per alert using fixed per-type quotas (policy, KYC/context, transaction slice/graph, and similar cases). We tune 𝑘and quota ratios on the validation set to balance coverage and prompt length.

For all LLM-based systems, we enforce a structured output schema (decision, confidence, supporting evidence IDs, contradicting/missing evidence IDs, rationale with citations, and recommended next actions). We then apply an automatic verifier that rejects outputs containing non-existent citations, inconsistent amounts/dates, or unsupported claims, and triggers a repair step with targeted feedback. This configuration ensures the experimental comparison measures not only accuracy but also the audit-ready characteristics required by AML triage.

### 5. EVALUATION


#### 5.1 Triage Effectiveness (Operational Utility)


We first evaluate whether the system improves the core triage objective: prioritizing truly suspicious alerts while controlling investigator workload. Using the alert-level labels (or simulator typology ground truth), we report precision, recall, and F1 for the “escalate” class, since escalation quality is the most operationally critical decision in triage. We additionally report PR-AUC to reflect performance under extreme class imbalance, which is typical in AML monitoring (figure 4). To connect model performance to workflow efficiency, we compute a simple workload proxy: the proportion of alerts routed to “monitor” or “escalate” under a fixed recall target, reflecting the practical requirement that institutions often tune systems to avoid missing suspicious activity while managing capacity. Results are compared against rulebased and ML baselines, LLM-only, RAG-only, and our full method.

#### 5.2 Evidence Quality and Auditability


[p. 12]

Because AML decisions must be auditable, we evaluate whether rationales are genuinely grounded in retrieved evidence. We measure citation validity (fraction of cited evidence IDs that exist in the retrieved bundle, i.e., no fabricated citations) and evidence support rate (fraction of rationale sentences whose cited evidence actually contains the referenced entities/numerical values, such as amounts, timestamps, counterparties, and risk tiers). For a stricter auditability check, we compute coverage of decision drivers, defined as whether the top stated reasons for escalation are backed by at least one policy/typology item and one case/customer/transaction item in the cited set, reflecting that AML justification typically requires both “what rule/typology this matches” and “what in this customer/transaction context supports it.” We also report the average number of evidence items cited per alert to quantify the trade-off between auditability and analyst readability.

#### 5.3 Counterfactual Robustness and Faithfulness


We then test whether explanations are decision-linked rather than decorative by applying the counterfactual protocol described in Section 4.7. We report CF-Flip Rate, the fraction of alerts for which the system can produce a _valid minimal flip condition_ within a bounded edit budget, where validity means the validator’s outcome (or risk score) changes beyond a threshold. We also report Evidence-Faithfulness under Removal, where we remove a “critical” cited evidence item and re-run the model; we measure whether the model (i) stops citing the removed item and (ii) adjusts its rationale/decision in the expected direction. Finally, we evaluate CF-Stability by applying irrelevant perturbations (e.g., benign re-ordering of equivalent transactions or small noise that should not affect typology indicators) and measuring the rate at which the decision remains unchanged. Together, these metrics quantify whether the model is sensitive to decision-relevant changes but stable to irrelevant ones, an essential property for reliable triage support.

#### 5.4 Safety and Failure Modes


Finally, we assess risks specific to deploying LLMs in financial compliance workflows. We measure numerical inconsistency rate (incorrect amounts, totals, thresholds, or temporal ordering relative to evidence), policy hallucination rate (claims that cite policy but cannot be found in the policy corpus), and unsupported assertion rate (sentences that introduce new entities or facts not present in any cited evidence). We also include an adversarial evidence test in which the retrieved bundle contains mildly conflicting or incomplete information (common in real workflows) and quantify whether the model appropriately flags uncertainty (via the “unknowns” field) rather than fabricating missing facts. These stress tests complement accuracy metrics by explicitly targeting the failure modes most likely to undermine auditability and compliance acceptance in AML triage.

### 6. Results & Analysis


#### 6.1 Triage Effectiveness Under Class Imbalance


[pp. 12-13]

On the core triage objective—identifying truly suspicious alerts while managing false positives—our full system achieves the strongest overall performance. Compared to traditional monitoring heuristics, the improvement is large: the rule/threshold baseline attains high recall (0.78) but very low precision (0.18), yielding a modest Escalate F1 of 0.29, which is consistent with the well-known false-positive burden of purely rules-driven monitoring. In contrast, supervised ML baselines improve precision materially: the tabular model (GBDT) reaches an Escalate F1 of 0.51, and the graph model (GNN) further improves to 0.56, reflecting the benefit of modeling relational structure. Nevertheless, our approach still outperforms these models on ranking quality and triage outcomes, improving PR-AUC from 0.69 (GNN) to 0.75 and improving Escalate F1 from 0.56 to 0.62. Notably, the gains are primarily driven by higher precision at similar recall (Precision 0.53 vs. 0.46; Recall 0.75 vs. 0.71), which aligns with operational triage goals: false positives are costly, and raising precision without sacrificing recall is the most valuable improvement. A key takeaway is that LLMs are not, by themselves, competitive triage predictor. The LLM-only baseline underperforms even the classical ML baselines (PR-AUC 0.52; F1 0.41), indicating that free-form reasoning over limited alert context does not reliably capture the decision boundary. However, once the LLM is placed in an evidence-grounded workflow (RAG), performance becomes competitive with graph ML (PR-AUC 0.71; F1 0.59), and our full method improves further (PR-AUC 0.75; F1 0.62). This suggests that the primary value of LLMs in AML triage is not “reasoning in the abstract,” but structured decision support that leverages explicit evidence and validation.

Table 1. Overall performance comparison on AML alert triage

[p. 13]

|Method|PR-AUC|EscalatePrecision|EscalateRecall|EscalateF1|CitationValidity|EvidenceSupport|CF-FlipRate|CF-Faithfulness(Removal)|NumericalInconsistency|PolicyHallucination|
|---|---|---|---|---|---|---|---|---|---|---|
|Rule/ThresholdBaseline|0.41|0.18|0.78|0.29|—|—|—|—|—|—|
|Tabular ML(GBDT)|0.63|0.42|0.66|0.51|—|—|—|—|—|—|
|Graph ML(GNN)|0.69|0.46|0.71|0.56|—|—|—|—|—|—|
|LLM-only (noretrieval)|0.52|0.31|0.60|0.41|0.62|0.54|0.28|0.39|0.11|0.14|
|RAG(evidenceretrieval, noCF checks)|0.71|0.49|0.73|0.59|0.96|0.83|0.41|0.57|0.06|0.05|
|Ours: RAG +CounterfactualChecks|0.75|0.53|0.75|0.62|0.98|0.88|0.58|0.76|0.03|0.02|

#### 6.2 Auditability and Evidence Grounding


Beyond accuracy, AML triage requires defensible documentation. Table 1 shows that evidence grounding is decisive for auditability. The LLM-only baseline exhibits weak provenance behavior: citation validity is only 0.62 and evidence support is 0.54, implying frequent fabricated citations and/or rationales that mention facts not actually present in the cited sources. In a regulated workflow, this is a critical failure mode because rationales may appear coherent while being impossible to audit.

Introducing retrieval grounding transforms this picture. RAG raises citation validity to 0.96 and evidence support to 0.83, indicating that the model can produce rationale text that is substantially more traceable to concrete sources when it is forced to cite within a bounded evidence bundle. Our full system improves these metrics further (citation validity 0.98; evidence support 0.88). While the absolute gains over RAG are smaller than the leap from LLM-only to RAG, they are practically meaningful because the residual failures in provenance tend to be precisely the kind that create compliance risk (e.g., a single fabricated policy reference can invalidate the entire record). The results support the design choice of making evidence IDs first-class citizens in the output contract and using a verifier to reject invalid citations.

#### 6.3 Counterfactual Faithfulness and Robustness


A central claim of this paper is that explanations should be decision-linked rather than decorative. The counterfactual metrics in Table 1 provide direct evidence that counterfactual validation improves faithfulness. RAG alone can often generate plausible counterfactual narratives, but it is less consistent at producing counterfactuals that are both valid and aligned with the actual decision logic. This is reflected in the lower CF-Flip Rate (0.41) and modest faithfulness under evidence removal (0.57). In contrast, our full method increases CF-Flip Rate to 0.58 and evidence-removal faithfulness to 0.76.

These gains have two interpretations. First, the higher CF-Flip Rate suggests the system can more frequently identify minimal, actionable “flip conditions” that match the validator’s decision boundary—precisely the kind of diagnostic signal investigators want when deciding what additional information would resolve uncertainty. Second, the stronger faithfulness under evidence removal indicates that the model is less likely to cite evidence it does not truly depend on: when a critical evidence item is removed, the model more consistently updates its rationale and citations appropriately. Together, these results support the hypothesis that counterfactual checks act as a practical test of explanation faithfulness and reduce brittle, non-causal rationalization.

#### 6.4 Safety: Numerical and Policy Hallucination Failures


[pp. 13-14]

Finally, we examine failure modes that are particularly costly in AML documentation: numerical inconsistencies (amounts, thresholds, timelines) and policy hallucinations (invented or misquoted policy logic). The LLM-only baseline shows the highest error rates (numerical inconsistency 0.11; policy hallucination 0.14), reinforcing that unconstrained generation is unsafe even when responses sound confident. RAG substantially reduces both errors (0.06 and 0.05), consistent with the notion that explicit evidence reduces ungrounded statements. Our full method reduces these rates

further (0.03 and 0.02), indicating that counterfactual validation and the verification/repair loop provide additional protection beyond retrieval alone.

Importantly, these safety improvements are not achieved at the cost of triage accuracy; rather, they co-occur with improved PR-AUC and Escalate F1. This suggests that the system’s reliability controls—provenance constraints, verification, and counterfactual checks—do not merely “sanitize” outputs, but also help the model focus on decisionrelevant evidence, improving both performance and trustworthiness.

### 7. DISCUSSION


#### 7.1 Practical Implications for AML Operations


[p. 14]

Our results suggest that the most meaningful contribution of LLMs to AML triage is not “better classification in isolation,” but better decision support under audit and governance constraints. Traditional rules-based monitoring can achieve high recall but produces a large false-positive burden, while classical ML and graph models improve ranking quality yet still leave investigators with the problem of _why_ an alert should be escalated and _what evidence_ supports that decision. In contrast, our evidence-grounded pipeline turns the triage output into an artifact that is closer to what investigators and reviewers actually need: a disposition paired with a compact set of cited, reviewable evidence and explicit uncertainty. The counterfactual module further improves usability by translating model behavior into actionable conditions (e.g., which missing corroboration would materially change the recommendation), which can naturally map to analyst next-steps and escalation playbooks.

From a program perspective, this supports a “human-in-the-loop” operating model where investigators remain accountable for outcomes, while the system reduces cognitive load and increases consistency. In organizations where triage throughput is a bottleneck, even moderate improvements in precision at comparable recall can translate into significant capacity relief; our table-level findings are consistent with the hypothesis that grounding and validation mechanisms can improve both model quality and the operational acceptability of generated rationales.

#### 7.2 Auditability, Model Risk, and Governance


A key challenge in deploying LLMs in compliance workflows is that fluent language can disguise unsupported claims. Our findings highlight that retrieval grounding dramatically improves citation validity and evidence support, but also that retrieval alone does not fully guarantee faithful reasoning. The counterfactual checks address this gap by operationalizing a test of decision-linked explanations: if the system claims that a factor is central, then minimal changes to that factor should alter the recommendation, and removal of critical evidence should be reflected in updated rationales. In practice, this gives risk and compliance teams a concrete mechanism for model governance: logs of retrieved evidence, model outputs, verifier failures, and counterfactual outcomes can form a structured audit trail for model risk management, internal validation, and periodic performance reviews.

We emphasize, however, that counterfactuals should be treated as decision support rather than ground truth. Their value lies in providing a structured lens to interrogate model behavior, not in proving correctness. A well-designed governance process would include periodic sampling-based review by experienced investigators, scenario-driven stress testing, and monitoring for drift in alert distributions and typology prevalence.

#### 7.3 Generalization and Real-World Data Constraints


A primary limitation of AML research is restricted access to real transaction and case data. Our evaluation relies on public synthetic resources (e.g., SynthAML10 and AMLSim) that enable reproducibility and controlled perturbations, but synthetic data may not fully capture operational complexities such as evolving customer behavior, data quality issues, cross-product interactions, and institution-specific monitoring rules. This creates two risks: (i) methods can overfit to synthetic typologies and (ii) measured gains may not transfer directly to production. To mitigate these risks in practice, we recommend a staged validation approach: start with synthetic benchmarks for functional correctness and failure-mode analysis, then run shadow-mode evaluations on internal historical alerts under strict privacy controls, and finally deploy with conservative guardrails and human approval gates. In future work, stronger external validity would come from multi-institution collaborations, privacy-preserving evaluation protocols, or additional benchmark releases that better reflect real alert generation and investigative artifacts.

#### 7.4 Security, Privacy, and Misuse Considerations


[pp. 14-15]

Because AML systems process sensitive customer information, privacy and access control are not optional. Our method’s retrieval stage naturally serves as a boundary: it can enforce role-based permissions, data minimization, and

redaction before any text reaches the LLM. That said, LLM-based systems introduce new attack surfaces such as prompt injection through untrusted documents, model inversion risks, and unintended disclosure in generated rationales. Deployments should therefore include strict input sanitization, retrieval whitelists for policy sources, secure prompt templates, and output filtering to prevent leakage of unnecessary personally identifiable information. Additionally, AML-related outputs must be carefully scoped to avoid generating actionable instructions that could enable evasion; counterfactuals, in particular, should be framed as investigative diagnostics for authorized analysts, with access controls and logging.

#### 7.5 Cost, Latency, and Deployment Trade-offs


[p. 15]

Operationalizing RAG + verification + counterfactual checks has computational cost. Retrieval itself is typically fast, but repeated LLM calls (initial generation, repair loops, counterfactual re-runs) can increase latency. Institutions should treat this as an engineering trade-off: not every alert needs the full pipeline. A practical design is to apply lightweight triage scoring first, then route only the top 𝑥%highest-risk alerts (or those that are ambiguous) through the full explainable pipeline. Another practical strategy is to cap the counterfactual budget (e.g., 1–2 validated counterfactuals per alert) and to restrict repairs to a small number of iterations. These strategies preserve the benefits of auditability and faithfulness where they matter most while keeping cost and latency within acceptable limits.

#### 7.6 Limitations and Future Work


Our study has several limitations. First, the triage label mapping (dismiss/monitor/escalate) is necessarily an approximation when using public synthetic datasets; real institutions differ in disposition taxonomies and escalation thresholds. Second, evidence support metrics, while informative, are imperfect proxies for auditability; stronger evaluation would include expert review of rationales and counterfactuals against internal investigative standards. Third, counterfactual plausibility is challenging: a minimal edit may be mathematically small but operationally unrealistic. Future work should incorporate domain-constraint models and investigator feedback loops to ensure counterfactuals are both minimal and meaningful. Finally, we focus on triage rather than the full case lifecycle (investigation, SAR drafting, post-filing monitoring). Extending the framework to later stages, while maintaining provenance, privacy, and governance, remains an important direction.

### 8. Conclusion


This paper investigated how to make LLM-assisted AML alert triage auditable and decision-faithful. We proposed an explainable triage framework that combines retrieval-augmented evidence grounding with structured LLM outputs and a counterfactual validation layer. The evidence retrieval module constrains the model’s factual scope to permissionapproved sources, enabling provenance-linked rationales suitable for review. The verifier-and-repair loop reduces fabricated citations and numerical/policy inconsistencies. Finally, counterfactual checks provide a practical test of explanation faithfulness by validating whether minimal, compliance-relevant perturbations produce coherent changes in both decisions and rationales.

Across baselines, the results indicate that LLMs are most useful in AML triage when embedded in an evidenceconstrained workflow: LLM-only generation is both less accurate and substantially less reliable, while retrieval grounding improves auditability and reduces hallucination-like errors. Adding counterfactual checks further improves decision-linked explainability, strengthens robustness, and reduces failure modes that would undermine compliance acceptance. Overall, these findings support a broader conclusion: deploying generative models in regulated FinTech settings requires treating them as components in a governed system, one that enforces provenance, validates consistency, and surfaces uncertainty, rather than as standalone text generators.

In future work, we plan to validate the approach under more realistic institutional conditions, including shadow-mode trials on private alert streams, richer policy corpora, and expert-in-the-loop evaluation of counterfactual usefulness. We also aim to extend the framework beyond triage to downstream AML case investigation workflows, where auditability and faithfulness are equally critical but the evidence space and decision stakes are even larger.

### REFERENCES


[pp. 15-16]

[1] Financial Action Task Force, “International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation: The FATF Recommendations,” Feb. 2012 (updated Feb. 2025).

[2] Financial Action Task Force, “Guidance for a Risk-Based Approach: The Banking Sector,” Oct. 2014.

[3] Financial Action Task Force, “Risk-Based Approach Guidance for the Securities Sector,” Oct. 2018.

[4] Basel Committee on Banking Supervision, “Sound management of risks related to money laundering and financing of terrorism,” Feb. 2016 (rev. July 2020).

[5] Association for Financial Markets in Europe and Ernst & Young, “Anti-Money Laundering Transaction Monitoring in the Markets Sector: An industry perspective,” Oct. 2021.

[6] B. Oztas, D. Cetinkaya, F. Adedoyin, M. Budka, G. Aksu, and H. Dogan, “Transaction Monitoring in Anti-Money Laundering: A Qualitative Analysis and Points of View from Industry,” Future Generation Computer Systems, vol. 159, pp. 161–171, Oct. 2024, doi: 10.1016/j.future.2024.05.027.

[7] Y. Dai, M. Chen, and Z. Zuo, “Neighbors in space: Satellite imagery and Chinese B-share discount,” _China Economic Review_ , vol. 82, Art. no. 102063, 2023, doi: 10.1016/j.chieco.2023.102063.

[8] Y. Liu, J. Zhang, and Y. Dai, “Analyst following and greenwashing decision,” _Finance Research Letters_ , vol. 58, Art. no. 104510, 2023, doi: 10.1016/j.frl.2023.104510.

[9] Z. Cheng, L. Lai, and Y. Liu, “Resolving the robustness-precision trade-off in financial RAG through hybrid document-routed retrieval,” arXiv preprint arXiv:2603.26815, 2026, doi: 10.48550/arXiv.2603.26815. [10] Z. Cheng, L. Lai, Y. Liu, K. Cheng, and X. Qi, “Enhancing financial report question-answering: A retrievalaugmented generation system with reranking analysis,” arXiv preprint arXiv:2603.16877, 2026, doi: 10.48550/arXiv.2603.16877.

[p. 16]

[11] K. Cheng, X. Qi, Z. Cheng, and L. Lai, “Volatility persistence and model choice in cross-market volatility forecasting,” SSRN preprint, 2026, doi: 10.2139/ssrn.6610278.

[12] L. Lin, L. Lin, Z. Zhang, M. Zheng, and Y. Wang, “A volume-price-adjusted MACD trading strategy with sensitivity calibration for U.S. equity indices,” arXiv preprint arXiv:2604.26063, 2026, doi: 10.48550/arXiv.2604.26063. [13] M. Weber, J. Chen, T. Suzumura, A. Pareja, T. Ma, H. Kanezashi, T. Kaler, C. E. Leiserson, and T. B. Schardl, “Scalable Graph Learning for Anti-Money Laundering: A First Look,” arXiv preprint arXiv:1812.00076, 2018, doi: 10.48550/arXiv.1812.00076.

[14] K. Liu, S. Yang, and J. Xia, “Research and Practice of Advertisement Recommendation Algorithm Based on Graph Neural Network,” in Proceedings of the 2nd International Symposium on Integrated Circuit Design and Integrated Systems (ICDIS ’25), 2025, pp. 210–215, doi: 10.1145/3772326.3774734.

[15] D. Yu, D. Zhuang, L. Jiang, R. Xu, X. Ye, Y. Bu, S. Wang, and G. Wang, “UQGNN: Uncertainty quantification of graph neural networks for multivariate spatiotemporal prediction,” in _Proceedings of the 33rd ACM International Conference on Advances in Geographic Information Systems_ , 2025, pp. 52–65, doi: 10.1145/3748636.3762709.

[16] D. Yu, L. Jiang, R. Xu, and G. Wang, “HealthMamba: An uncertainty-aware spatiotemporal graph state space model for effective and reliable healthcare facility visit prediction,” arXiv preprint arXiv:2602.05286, 2026, doi: 10.48550/arXiv.2602.05286.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks" (2026-03-22). https://arxiv.org/abs/2604.19755
