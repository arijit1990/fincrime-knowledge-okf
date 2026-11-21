---
type: Source Text
title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification - part 3 of 4 (pp. 7-9)'
description: 'Verbatim extracted text, pp. 7-9: 4.5 Production Deployment and Yield Rate; 5.1 Why ML Outperforms Rules; 5.2 The Value of LLM-Generated Narratives; and 4 more sections'
resource: https://arxiv.org/abs/2607.17586
tags:
- academic_finding
- data_features
- explainability
- global_academic
- model_development
- preprint
status: stable
source_id: arxiv-detection-attribution-narration-an-end-to-end-pipeline-for-expla
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-07-20'
legal_status: unknown
part: 3
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2607.17586
  title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification'
  author: org:arxiv
  last_modified: '2026-07-20T00:00:00Z'
---

# Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2026-07-20), part 3 of 4, pp. 7-9. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 4.5 Production Deployment and Yield Rate


[p. 7]

The complete pipeline has been deployed in a production AML environment for 1 month, with alerts surfaced to a team of 3 three full-time analysts. Table 5 compares the operational performance of the proposed pipeline against the incumbent rule-based system, which consists of 5 reports focused on identifying likely bad-actors based on customer profile, non-financial and financial transaction activity, and financial transaction network behaviour. The rulebased metrics are blended across all 5 reports.

Table 5: Operational comparison: proposed pipeline vs. incumbent rule-based system (metrics blended across 5 reports) on live production alerts.

|Metric|Rule-BasedProposed|
|---|---|
||(blended across 5 reports)|
|Yield Rate|61%89%|
|Monthly Alert Volume|211302|

The yield rate improvement from 61% to over 89% represents a substantial reduction in false positives surfaced to analysts, allowing the team to focus investigative effort on genuinely suspicious accounts. The concurrent rise in monthly alert volume from 211 to 302 reflects broader coverage rather than noise. This indicates that the model surfaces more true positives that the rule-based system had previously missed, without proportionally increasing analyst burden given the higher yield.

Analyst feedback on LLM narratives. Appendix B shows two representative LLM outputs alongside the analyst verdicts they received. Through structured feedback sessions, analysts reported that LLM-generated narratives meaningfully reduced the cognitive effort required during alert triage. Specifically, analysts noted that narratives allowed them to quickly assess whether a prediction was plausible before committing to a full investigation, and that the structured format (red flags, supporting reasons, and evidence references) aligned well with their existing workflow. Representative analyst feedback highlighted two particularly valued capabilities. First, analysts noted that the narratives _“provide clear guidance into why an alert is classified as higher risk rather than typical customer behaviour and draw attention to specific non-financial red flags that we may not typically monitor.”_ Second, analysts identified a proactive monitoring use case: the LLM _“has the capability to help filter higher-risk alerts with low transaction values”_ , cases where suspicious behavioural signals are present but adverse transactions have not yet materialised. Rather than dismissing these as low-priority, analysts noted that such alerts can be placed under short-term internal monitoring (typically a few weeks), as flagged accounts frequently exhibit adverse activity within that window. This suggests the system supports not only point-in-time triage but also early-warning identification of emerging money mule activity.

## 5.1 Why ML Outperforms Rules


[pp. 7-8]

The improvement in yield rate from 61% to over 89% reflects a fundamental difference in how the two approaches model the behavior of the mule. Rule-based systems operate on individual features in isolation: a single rule might flag accounts exceeding a velocity threshold, while another targets unusual counterparty counts. Each rule captures one behavioural dimension, and combining rules multiplicatively creates rigid decision boundaries that are brittle to slight variations in mule tactics.

The LightGBM model, by contrast, learns non-linear interactions across hundreds of features simultaneously. Money mule behaviour is inherently multi-dimensional, where no single feature is diagnostic, but the combination of moderate anomalies across transaction velocity, temporal patterns, and counterparty diversity creates a

Y. Zhang, Y. Zhang, Y. Jin, K. Razis, N. Choo, K. Wong, X. Tang, K. Zhu, W. Lee, and J. Zhao

distinctive signature. Gradient boosting captures these joint effects naturally through its sequential tree-building process, without requiring analysts to manually specify interaction rules.

A practical consequence is that the ML pipeline also produces higher-quality alerts at a greater volume, giving analysts more cases to review without sacrificing precision. Critically, when analyst capacity increases, the alert volume can be scaled up simply with only marginal loss in yield rate. Rule-based systems lack this flexibility, where tightening one rule often requires loosening another to maintain coverage. Consequently, it is difficult to scale detection without disproportionately inflating false positives.

## 5.2 The Value of LLM-Generated Narratives


[p. 8]

A key observation from deployment is that classification performance alone was insufficient to drive analyst adoption. Early iterations of the pipeline surfaced SHAP waterfall plots alongside the mule probability score, but analyst feedback indicated that interpreting raw feature attributions was time-consuming and required familiarity with the model’s feature definitions.

The addition of LLM-generated narratives changed the interaction dynamic. Rather than synthesising meaning from a bar chart of 10 numeric values, analysts could read a concise summary that contextualised the risk factors in domain-relevant language (e.g., “a sudden spike in inflows relative to the account’s longer-term baseline” rather than “txn_credit_p7d_p180d_ratio_sum: SHAP = +0.34”). Analysts reported that this reduced the time to form an initial hypothesis about if an alert warranted deeper investigation.

This finding aligns with recent work on XAI narratives. Cedro and Martens [3] found that over 90% of non-experts rated SHAPbased narratives as convincing, and Zytek et al. [19] showed user preference for LLM narratives over SHAP plots. Our contribution extends these findings to a production AML environment, where the stakes and the scrutiny are considerably higher.

## 5.3 Limitations


We identify a few limitations of the current work as follows.

- Single-institution evaluation. All results are from one financial institution. Mule typologies, transaction patterns, and label distributions vary across geographies and banking products, and the pipeline’s performance may not transfer directly without retraining and feature adaptation.

- Label quality. Ground truth is constructed from police force filings and human analyst confirmations. Both carry inherent limitations. Police filings may be filed with a delay, and analysts may disagree on borderline cases. Furthermore, undetected mules represent survivorship bias in the negative class. The yield rate metric partially mitigates this by measuring confirmed outcomes, but underlying label noise remains.

- LLM hallucination residual risk. Despite prompt constraints and periodic human review, LLM-generated narratives can occasionally produce plausible-sounding statements that subtly misrepresent the underlying SHAP evidence. In a compliance context, even infrequent hallucinations carry reputational and regulatory risk. Ongoing monitoring and periodic manual audits are essential.

## 5.4 Ethical Considerations


Deploying ML for financial crime detection carries fairness and accountability risks. The model must not disproportionately flag customers based on protected or sensitive characteristics. The feature set excludes gender and ethnicity, but it does include age-related and geography-related variables, such as customer age, country of domicile, and transaction geographies. These variables may be relevant for financial crime risk assessment, but they can also introduce proxy-discrimination risks. We therefore treat demographic and geography-linked features as requiring explicit governance, monitoring, and periodic review rather than assuming that their inclusion is automatically fair or risk-free.

The LLM interpretation layer introduces an additional fairness and conduct risk. Generated narratives may influence analyst judgment even when they are intended only as explanatory aids. To mitigate this risk, the prompt template constrains the LLM to cite only SHAP-supported evidence from the case input and to avoid unsupported speculation. In addition, generated narratives are subject to periodic human review for factual consistency, discriminatory framing, and inappropriate escalation language. The LLM output is not treated as an independent basis for adverse action; final decisions remain with trained financial-crime analysts following the institution’s standard review process.

## 6 Conclusions


This paper presents an end-to-end pipeline for money mule detection that combines account-level classification, feature attribution, and LLM-generated natural-language explanations. A LightGBM model trained on 280 engineered features produces calibrated mule probability scores. TreeSHAP decomposes each prediction into per-feature contributions. A self-hosted LLM translates the top-10 attributions into analyst-facing narratives under structured prompt constraints. In live production deployment, the pipeline achieves a yield rate of 89%, up from 61% under the incumbent rule-based system. Monthly alert volume expanded from 211 to 302, reflecting broader true-positive coverage. This corresponds to 60% incremental adverse detection beyond existing review workflows, substantially outperforming the incumbent rule-based approaches. Analyst feedback confirms that LLM-generated narratives reduce cognitive load during triage compared to raw SHAP visualisations.

Three findings may be of broader interest to practitioners deploying ML in regulated financial environments. First, the operational bottleneck in AML detection is often not model accuracy but _explanation usability_ . Thus, the LLM interpretation layer was critical to analyst adoption. Second, open-weight models deployed on-premise can satisfy data residency requirements without sacrificing explanation quality, making this approach viable for institutions that cannot use external API-based services. Third, structured prompt templates and periodic human review offer a practical path to reducing hallucination risk in high-stakes settings, although residual risk remains and requires ongoing monitoring.

## References


[pp. 8-9]

> [1] Sandhini Agarwal, Lama Ahmad, Jason Ai, Sam Altman, Andy Applebaum, Edwin Arbus, Rahul K Arora, Yu Bai, Bowen Baker, Haiming Bao, et al. 2025. gpt-oss-120b & gpt-oss-20b model card. _arXiv preprint arXiv:2508.10925_ (2025).

- [2] Marilyn Bello, Rafael Bello, María-Matilde García, Ann Nowé, Iván SevillanoGarcía, and Francisco Herrera. 2025. A three-Level Framework for LLM-Enhanced eXplainable AI: From technical explanations to natural language. _Information Systems Frontiers_ (2025), 1–22.

- [3] Mateusz Cedro and David Martens. 2025. GraphXAIN: narratives to explain graph neural networks. In _World Conference on Explainable Artificial Intelligence_ . Springer, 91–114.

- [4] European Parliament and Council of the European Union. 2024. Regulation (EU) 2024/1689. https://eur-lex.europa.eu/eli/reg/2024/1689/oj Official Journal of the European Union.

- [5] Zhenfeng Huang. 2025. Enhancing Anti-Money Laundering by Money Mules Detection on Transaction Graphs. In _Proceedings of the 2025 International Conference on Generative Artificial Intelligence for Business_ . 83–88.

- [6] Ganesh Jambhrunkar, Harsh Sharma, Saurav Singla, and Thirumalai Kailasam. 2025. MuleTrack: A Lightweight Temporal Learning Framework for Money Mule Detection in Digital Payments. In _International Work-Conference on Artificial Neural Networks_ . Springer, 384–397.

- [7] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. 2017. Lightgbm: A highly efficient gradient boosting decision tree. _Advances in neural information processing systems_ 30 (2017).

- [8] Scott M Lundberg, Gabriel Erion, Hugh Chen, Alex DeGrave, Jordan M Prutkin, Bala Nair, Ronit Katz, Jonathan Himmelfarb, Nisha Bansal, and Su-In Lee. 2020. From local explanations to global understanding with explainable AI for trees. _Nature machine intelligence_ 2, 1 (2020), 56–67.

- [9] Scott M Lundberg and Su-In Lee. 2017. A unified approach to interpreting model predictions. _Advances in neural information processing systems_ 30 (2017).

[p. 9]

- [10] David Martens, James Hinns, Camille Dams, Mark Vergouwen, and Theodoros Evgeniou. 2025. Tell me a story! Narrative-driven XAI with Large Language Models. _Decision Support Systems_ 191 (2025), 114402.

- [11] Office of the Comptroller of the Currency. 2011. Supervisory Guidance on Model Risk Management. https://www.occ.gov/news-issuances/bulletins/2011/bulletin2011-12a.pdf Board of Governors of the Federal Reserve System.

- [12] Tahereh Pourhabibi, Kok-Leong Ong, Booi H Kam, and Yee Ling Boo. 2020. Fraud detection: A systematic literature review of graph-based anomaly detection approaches. _Decision Support Systems_ 133 (2020), 113303.

- [13] David Savage, Qingmai Wang, Xiuzhen Zhang, Pauline Chou, and Xinghuo Yu. 2017. Detection of Money Laundering Groups: Supervised Learning on Small Networks.. In _AAAI Workshops_ . 5–11.

- [14] Altyeb Altaher Taha and Sharaf Jameel Malebary. 2020. An intelligent approach to credit card fraud detection using an optimized light gradient boosting machine. _IEEE access_ 8 (2020), 25579–25587.

- [15] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juliette Love, et al. 2024. Gemma: Open models based on gemini research and technology. _arXiv preprint arXiv:2403.08295_ (2024).

- [16] Biao Xu, Yao Wang, Xiuwu Liao, and Kaidong Wang. 2023. Efficient fraud detection using deep boosting decision trees. _Decision Support Systems_ 175 (2023), 114037.

- [17] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. 2025. Qwen3 technical report. _arXiv preprint arXiv:2505.09388_ (2025).

- [18] Xianlong Zeng. 2024. Enhancing the interpretability of SHAP values using large language models. _arXiv preprint arXiv:2409.00079_ (2024).

- [19] Alexandra Zytek, Sara Pido, Sarah Alnegheimish, Laure Berti-Equille, and Kalyan Veeramachaneni. 2024. Explingo: Explaining ai predictions using large language models. In _2024 IEEE International Conference on Big Data (BigData)_ . IEEE, 1197– 1208.

This appendix reproduces the prompt used for production deployment and for the LLM evaluation reported in Section 4.4. The prompt consists of a system message (Listing 1) that defines the analyst role, input fields, and required JSON schema, followed by a user message (Listing 2) that injects the per-case SHAP attribution payload at the position marked .


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification" (2026-07-20). https://arxiv.org/abs/2607.17586
