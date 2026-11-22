---
type: Source Text
title: 'OpenSanctions Pairs: Large-Scale Entity Matching with LLMs - part 2 of 3 (pp. 7-12)'
description: 'Verbatim extracted text, pp. 7-12: OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching > 5 Experiments and analysis; OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching > 6 Limitations; OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching > 7 Conclusion; and 1 more sections'
resource: https://arxiv.org/abs/2603.11051
tags:
- academic_finding
- customer_risk
- data_features
- global_academic
- preprint
- sanctions_adjacent
status: stable
source_id: arxiv-opensanctions-pairs-large-scale-entity-matching-with-llms
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-02-24'
legal_status: unknown
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:42:06Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:42:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.11051
  title: 'OpenSanctions Pairs: Large-Scale Entity Matching with LLMs'
  author: org:arxiv
  last_modified: '2026-02-24T00:00:00Z'
---

# OpenSanctions Pairs: Large-Scale Entity Matching with LLMs

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2026-02-24), part 2 of 3, pp. 7-12. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching


### 5 Experiments and analysis


#### 5.2 Evaluation protocol


[p. 7]

Dataset sampling We construct label-stratified 10,000- and 1,000-pair samples from the 755,540pair corpus (seed 42). When MIPROv2 is applied, 200 pairs are held out as a dev split, so the test set is the remainder (9,800 or 800); the smaller sample is used where 10,000-pair runs are cost-prohibitive. RegressionV1 is tuned (threshold 0.15) on 2,000 pairs and evaluated on 8,000. Per-model test-set sizes: 9,800 for Llama-3.1-8B (0-shot opt, 8-shot opt), GPT-5 Nano (opt), and Claude Opus 4.5 (opt); 800 for Llama-3.1-8B (2-shot opt, 4-shot opt) and GPT-5.2 Pro; and 3,680 (opt) / 1,960 (unoptimized) for DeepSeek-R1-Distill-Qwen-14B, reduced for runtime. GPT-5.2 Pro is run without prompt optimization.

Metrics We report standard binary classification metrics: accuracy, precision, recall, and F1 score. Given the class imbalance (76.9% positive) and the asymmetric costs of false positives versus false negatives in compliance settings, we emphasize F1 as the primary metric. We include a confusion matrix to highlight the relative strengths and weaknesses between models. All metrics are reported on the full label-stratified samples drawn from the 755,540-pair corpus, including the auto-merge tier described in Section 3.4; because every method evaluates these pairs independently and identically, the resulting absolute-F1 inflation is uniform across baselines and does not affect relative rankings.

#### 5.3 Implementation details


[pp. 7-8]

Inference. Open-source models run via Hugging Face `transformers` with tensor parallelism on 8 _×_ 46 GB A40 or 8 _×_ 128 GB MI250X GPUs, with constrained decoding (Outlines) to enforce JSON output, temperature _≤_ 0 _._ 01, greedy sampling, 512 max new tokens, 4,096-token input truncation. API models are accessed via LightLLM5 or provider APIs at temperature 0; GPT-5.2 Pro uses `reasoning.effort=medium` .

> 5 `https://github.com/ModelTC/LightLLM`

Table 4: Per-method confusion matrix on the test split. DeepSeek-Qwen=DeepSeek-R1-DistillQwen-14B; all configurations are 0-shot, not optimized.

|Method|TP%|TN%|FP%|FN%|
|---|---|---|---|---|
|Nomenklatura|0.766|0.088|0.141|0.004|
|Llama-3.1-8B|0.759|0.145|0.086|0.010|
|DeepSeek-Qwen|0.758|0.208|0.030|0.005|
|GPT-3.5 Turbo|0.701|0.218|0.013|0.068|
|GPT-4o|0.762|0.222|0.009|0.007|
|GPT-5 Nano|0.761|0.163|0.068|0.008|
|GPT-5.2 Pro|0.756|0.221|0.013|0.010|
|Claude 3 Haiku|0.759|0.120|0.116|0.004|
|Claude 3.7 Sonnet|0.731|0.232|0.007|0.030|
|Claude Opus 4.5|0.708|0.225|0.006|0.061|

Optimization. We optimize prompts with DSPy MIPROv2 [4], initialized from the conflict-focused default prompt (Section A.1). MIPROv2 evaluates 15 candidate (instruction, _≤_ 8-demo) programs on the 200-pair dev set over _∼_ 22–23 trials, with instruction proposals sampled at temperature 1.

#### 5.4 Results


[p. 8]

LLMs reach near-ceiling F1. Table 3 reports the main results. The strongest LLMs reach nearceiling performance (98–99% F1), substantially outperforming the rule-based baseline (91.33% F1) used in production. GPT-4o achieves the highest score (98.95% F1), and the best open-source model (DeepSeek-R1-Distill-Qwen-14B, 98.23% F1) closely matches frontier proprietary models such as GPT-5.2 Pro (98.75% F1).

Prompt optimization provides minor gains. MIPROv2 prompt optimization yields modest, modeldependent improvements: Llama-3.1-8B improves from 94.05% to 95.94% F1 (+1.9), while frontier proprietary models change negligibly. The default and optimized prompts are shown side-by-side in Figure 3 (Appendix A.3).

Few-shot examples do not help once the prompt is optimized. Llama-3.1-8B with 2-, 4-, and 8-shot demonstrations matches or underperforms its optimized zero-shot baseline (95.46%, 95.64%, 95.94% vs. 95.94% F1); GPT-5 Nano shows the same pattern. In-context demonstrations appear to introduce inductive biases that compete with the optimized instruction.

Model size vs. throughput. DeepSeek-14B slightly outperforms Llama-3.1-8B (98.23% vs. 95.94% F1) but takes roughly 3 _×_ longer per example ( _∼_ 70s vs. _∼_ 25s); Llama-3.1-8B is the better accuracythroughput point for at-scale deployment.

Performance vs. release date. Figure 2 shows 0-shot F1 rising from 92–94% (early 2023) to 98–99% (late 2025), suggesting that pairwise matching is approaching a practical ceiling and that further gains are likelier to come from blocking, clustering, and uncertainty-aware review than from pairwise prompt tuning.

#### 5.5 Failure modes


[pp. 8-9]

The per-method confusion matrices in Table 4 reveal two distinct error profiles. RegressionV1 has near-perfect recall but many false positives, reflecting OpenSanctions’ operational preference for catching every potential match at the cost of analyst review (threshold 0.15). LLM errors instead concentrate in two narrow modes: cross-script transliteration differences (Latin / Cyrillic / Arabic) that obscure genuine matches, and over-weighting of minor data-entry noise (off-by-one dates or identifiers) into spurious negatives under the conflict-focused prompt.

Entity Resolution F1 vs. Model Release Date (0-shot, unoptimized)100GPT-4o (99.0%)Rule-based baseline (91.3%) GPT-5.2 Pro (98.5%)OpenAI Claude 3.7 Sonnet (97.5%)98 AnthropicOpen-sourceTrend (LLMs) DeepSeek-R1-Distill-Qwen-14B (97.8%)96Llama-3.1-8B (94.0%)GPT-5 Nano (95.2%)94 GPT-3.5 Turbo (94.5%)Claude Opus 4.5 (95.5%)92 Claude 3 Haiku (92.7%)9088Model Release DateFeb 2023May 2023Aug 2023Nov 2023 Feb 2024May 2024Aug 2024Nov 2024 Feb 2025May 2025Aug 2025Nov 2025 Feb 2026F1 Score (%)

Figure 2: Unoptimized (0-shot) F1 versus model release date. The dashed gray line is the Nomenklatura rule baseline (91.3% F1); the blue dashed line is a linear fit across LLMs. The LLM-rule gap widened from _∼_ 2 F1 points in 2023 to over 7 by late 2025.

### 6 Limitations


[p. 9]

We note three limitations. (1) Labels reflect analyst judgments under incomplete evidence, so modellabel disagreements may capture labeling uncertainty rather than prediction errors. (2) Evaluation sample sizes vary across models due to compute cost; all are label-stratified, but smaller ones carry greater statistical uncertainty. (3) Most OpenSanctions sources are public, so overlap with frontiermodel training corpora cannot be fully excluded; the released `first_seen` timestamps support a temporal hold-out for future leakage probes.

We released OpenSanctions Pairs, the first large-scale public benchmark for entity matching on sanctions OSINT data: 756K analyst-labeled pairs over 1.0M entities aggregated from 293 sources across 45 jurisdictions, multi-script and multi-schema, with set-valued partial-evidence attributes that mirror operational compliance workflows. Reference baselines establish that the benchmark is non-trivial yet within reach of current LLMs (91.3% rule baseline vs. 98–99% LLM ceiling), with complementary failure modes (rule over-matching vs. LLM cross-script transliteration) that point to future work on blocking, clustering, and uncertainty-aware review.

### 7 Conclusion


Sanctions matching has until now been evaluated almost entirely inside vendor labs, leaving research progress invisible to the field. OpenSanctions Pairs gives the community a shared target on the same data that banks, regulators, NGOs, and investigative journalists rely on to flag sanctioned individuals and shell companies. Each point of recall closes a route by which designated parties evade screening through aliases or transliterations; each point of precision spares analysts and legitimate counterparties from thousands of false hits.

This work releases a public benchmark for entity matching on real-world sanctions data, supporting realistic evaluation of LLMs on multi-script, cross-jurisdictional compliance tasks. Surfacing the complementary failure modes of rule-based and learned matchers encourages safer human-in-theloop deployment and reduces unnecessary false positives. We acknowledge dual-use risk: matching infrastructure that aids compliance can also support adversarial profiling, partly mitigated by the CC-BY-NC license and analyst-judgment caveats accompanying the release.

### References


[p. 10]

- [1] N. Barlaug and J. A. Gulla. Neural networks for entity matching: A survey. _ACM Trans. Knowl. Discov. Data_ , 15(3), Apr. 2021. ISSN 1556-4681. doi: 10.1145/3442200. URL `https://doi.org/10.1145/3442200` .

- [2] P. Christen. _Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection_ . Springer Berlin Heidelberg, 2012. ISBN 9783642311642. doi: 10.1007/978-3-642-31164-2. URL `http://dx.doi.org/10.1007/978-3-642-31164-2` .

- [3] V. Christophides, V. Efthymiou, T. Palpanas, G. Papadakis, and K. Stefanidis. End-to-end entity resolution for big data: A survey, 2020. URL `https://arxiv.org/abs/1905.06397` .

- [4] DSPy. Miprov2 — dspy api optimizer. `https://dspy.ai/api/optimizers/MIPROv2/` , n.d. URL `https://dspy.ai/api/optimizers/MIPROv2/` . Accessed: 2026-01-29.

- [5] A. K. Elmagarmid, P. G. Ipeirotis, and V. S. Verykios. Duplicate record detection: A survey. _IEEE Trans. on Knowl. and Data Eng._ , 19(1):1–16, Jan. 2007. ISSN 1041-4347.

- [6] M. Fan, X. Han, J. Fan, C. Chai, N. Tang, G. Li, and X. Du. Cost-effective in-context learning for entity resolution: A design space exploration, 2023. URL `https://arxiv.org/abs/ 2312.03987` .

- [7] G. Felbermayr, A. Kirilakha, C. Syropoulos, E. Yalcin, and Y. V. Yotov. The global sanctions data base. _European Economic Review_ , 129:103561, 2020. ISSN 0014-2921. doi: https://doi.org/10.1016/j.euroecorev.2020.103561. URL `https://www.sciencedirect. com/science/article/pii/S0014292120301914` .

- [8] I. P. Fellegi and A. B. Sunter. A theory for record linkage. _Journal of the American Statistical Association_ , 64(328):1183–1210, 1969. doi: 10.1080/01621459.1969.10501049. URL `https: //www.tandfonline.com/doi/abs/10.1080/01621459.1969.10501049` .

- [9] J. Fu, H. Tang, A. Khan, S. Mehrotra, X. Ke, and Y. Gao. In-context clustering-based entity resolution with large language models: A design space exploration. In _Proceedings of the ACM on Management of Data (SIGMOD)_ , 2026. URL `https://arxiv.org/abs/2506.02509` .

- [10] L. Getoor and A. Machanavajjhala. Entity resolution: Theory, practice & open challenges. _Proceedings of the VLDB Endowment_ , 5:2018–2019, 08 2012. doi: 10.14778/2367502.2367564.

- [11] M. A. Hernández and S. J. Stolfo. The merge/purge problem for large databases. In _Proceedings of the 1995 ACM SIGMOD international conference on Management of data - SIGMOD_

- _’95_ , SIGMOD ’95, page 127–138. ACM Press, 1995. doi: 10.1145/223784.223807. URL `http://dx.doi.org/10.1145/223784.223807` .

- [12] S. Kim and S. Yang. Accuracy improvement in financial sanction screening: is natural language processing the solution? _Frontiers in Artificial Intelligence_ , 7, Nov. 2024. ISSN 2624-8212. doi: 10.3389/frai.2024.1374323. URL `http://dx.doi.org/10.3389/frai.2024.1374323` .

[pp. 10-11]

- [13] P. Konda, S. Das, P. Suganthan G. C., A. Doan, A. Ardalan, J. R. Ballard, H. Li, F. Panahi, H. Zhang, J. Naughton, S. Prasad, G. Krishnan, R. Deep, and V. Raghavendra. Magellan: toward building entity matching management systems. _Proc. VLDB Endow._ , 9(12):1197–1208, Aug. 2016. ISSN 2150-8097. doi: 10.14778/2994509.2994535. URL `https://doi.org/10. 14778/2994509.2994535` .

- [14] H. Köpcke, A. Thor, and E. Rahm. Evaluation of entity resolution approaches on realworld match problems. _Proceedings of the VLDB Endowment_ , 3(1–2):484–493, Sept. 2010. ISSN 2150-8097. doi: 10.14778/1920841.1920904. URL `http://dx.doi.org/10.14778/ 1920841.1920904` .

- [15] H. Köpcke, A. Thor, and E. Rahm. Learning-based approaches for matching web data entities. _IEEE Internet Computing_ , 14(4):23–31, July 2010. ISSN 1089-7801. doi: 10.1109/mic.2010.58. URL `http://dx.doi.org/10.1109/MIC.2010.58` .

- [16] H. Li, L. Feng, S. Li, F. Hao, C. J. Zhang, and Y. Song. On leveraging large language models for enhancing entity resolution: A cost-efficient approach, 2024. URL `https://arxiv.org/ abs/2401.03426` .

- [17] H. Li, S. Li, F. Hao, C. J. Zhang, Y. Song, and L. Chen. Booster: Leveraging large language models for enhancing entity resolution. In _Companion Proceedings of the ACM Web Conference 2024_ , WWW ’24, page 1043–1046, New York, NY, USA, 2024. Association for Computing Machinery. ISBN 9798400701726. doi: 10.1145/3589335.3651245. URL `https://doi.org/ 10.1145/3589335.3651245` .

[p. 11]

- [18] Y. Li, J. Li, Y. Suhara, A. Doan, and W.-C. Tan. Deep entity matching with pre-trained language models. _Proceedings of the VLDB Endowment_ , 14(1):50–60, Sept. 2020. ISSN 2150-8097. doi: 10.14778/3421424.3421431. URL `http://dx.doi.org/10.14778/3421424.3421431` .

- [19] J. Montenarh and S. Marsden. Unmasking the oligarchs – using open source data to detect sanctions violations. _Journal of Economic Criminology_ , 3:100055, Mar. 2024. ISSN 2949-7914. doi: 10.1016/j.jeconc.2024.100055. URL `http://dx.doi.org/10.1016/j.jeconc.2024. 100055` .

- [20] M. H. Moslemi, A. Mousavi, B. Behkamal, and M. Milani. Heterogeneity in entity matching: A survey and experimental analysis, 2026. URL `https://arxiv.org/abs/2508.08076` . Revised February 2026.

- [21] S. Mudgal, H. Li, T. Rekatsinas, A. Doan, Y. Park, G. Krishnan, R. Deep, E. Arcaute, and V. Raghavendra. Deep learning for entity matching: A design space exploration. In _Proceedings of the 2018 International Conference on Management of Data_ , SIGMOD ’18, page 19–34, New York, NY, USA, 2018. Association for Computing Machinery. ISBN 9781450347037. doi: 10.1145/3183713.3196926. URL `https://doi.org/10.1145/3183713.3196926` .

- [22] S. Mudgal, H. Li, T. Rekatsinas, A. Doan, Y. Park, G. Krishnan, R. Deep, E. Arcaute, and V. Raghavendra. Datasets for the deepmatcher paper. `https://github.com/anhaidgroup/ deepmatcher/blob/master/Datasets.md` , 2018. Used in SIGMOD 2018 paper “Deep Learning for Entity Matching”; accessed 2026-01-28.

[pp. 11-12]

- [23] A. Narayan, I. Chami, L. Orr, S. Arora, and C. Ré. Can foundation models wrangle your data?, 2022. URL `https://arxiv.org/abs/2205.09911` .

- [24] OpenSanctions. How we deduplicate companies and people across data sources, 2021. URL `https://www.opensanctions.org/articles/2021-11-11-deduplication/` . Accessed: 2025-01-15.

- [25] OpenSanctions. Nomenklatura: Framework and command-line tools for integrating followthemoney data streams from multiple sources. `https://github.com/opensanctions/ nomenklatura/` , 2025. Accessed: 2026-01-20.

- [26] OpenSanctions. Matcher training data, 2025. URL `https://www.opensanctions.org/ docs/opensource/pairs/` . Accessed: 2025-01-15.

- [27] J. T. Ornstein. Probabilistic record linkage using pretrained text embeddings. _Political Analysis_ , 34(2):205–216, 2025. doi: 10.1017/pan.2025.10016.

- [28] K. O’Hare, A. Jurek-Loughrey, and C. d. Campos. _A Review of Unsupervised and Semisupervised Blocking Methods for Record Linkage_ , page 79–105. Springer International Publishing, 2019. ISBN 9783030018726. doi: 10.1007/978-3-030-01872-6_4. URL `http://dx.doi.org/10.1007/978-3-030-01872-6_4` .

- [29] G. Papadakis, D. Skoutas, E. Thanos, and T. Palpanas. A survey of blocking and filtering techniques for entity resolution, 2020. URL `https://arxiv.org/abs/1905.06167` .

- [30] R. Peeters. _Entity Matching using Deep Neural Networks: From Discriminative Pre-trained Language Models to Generative Large Language Models_ . PhD thesis, University of Mannheim, 2025. URL `https://madoc.bib.uni-mannheim.de/69425/` .

- [31] R. Peeters and C. Bizer. Using chatgpt for entity matching, 2023. URL `https://arxiv.org/ abs/2305.03423` .

[p. 12]

- [32] R. Peeters, R. C. Der, and C. Bizer. Wdc products: A multi-dimensional entity matching benchmark, 2023. URL `https://arxiv.org/abs/2301.09521` .

- [33] R. Peeters, A. Steiner, and C. Bizer. Entity matching using large language models, 2024. URL `https://arxiv.org/abs/2310.11244` .

- [34] A. Primpeli, R. Peeters, and C. Bizer. The WDC training dataset and gold standard for large-scale product matching. In _Companion of the 2019 World Wide Web Conference (WWW ’19)_ , pages 381–386. ACM, 2019. doi: 10.1145/3308560.3316609. URL `https://webdatacommons. org/largescaleproductcorpus/v2/` .

- [35] E. Rahm and D. G. Leipzig. Benchmark datasets for entity resolution, 2019. URL `https://dbs.uni-leipzig.de/research/projects/ benchmark-datasets-for-entity-resolution` . Dataset collection released 2010– 2019; accessed 2026-01-28.

- [36] M. Sadinle. Bayesian estimation of bipartite matchings for record linkage, 2016. URL `https: //arxiv.org/abs/1601.06630` .

- [37] A. Steiner, R. Peeters, and C. Bizer. Fine-tuning large language models for entity matching, 2025. URL `https://arxiv.org/abs/2409.08185` .

- [38] R. C. Steorts, R. Hall, and S. E. Fienberg. A bayesian approach to graphical record linkage and de-duplication, 2015. URL `https://arxiv.org/abs/1312.4645` .

- [39] T. Sterling and B. H. Meijer. Dutch bank ing fined $900 million for failing to spot money laundering. `https://www.reuters.com/article/ us-ing-groep-settlement-money-laundering-idUSKCN1LK0PE/` , September 4 2018. Accessed: 2026-01-13.

- [40] J. Tang, Y. Zuo, L. Cao, and S. Madden. Generic entity resolution models. In _NeurIPS 2022 First Table Representation Workshop_ , 2022. URL `https://openreview.net/forum?id= tRkVo1jMas` .

- [41] T. Wang, X. Chen, H. Lin, X. Chen, X. Han, L. Sun, H. Wang, and Z. Zeng. Match, compare, or select? an investigation of large language models for entity matching. In O. Rambow, L. Wanner, M. Apidianaki, H. Al-Khalifa, B. D. Eugenio, and S. Schockaert, editors, _Proceedings of the 31st International Conference on Computational Linguistics_ , pages 96–109, Abu Dhabi, UAE, Jan. 2025. Association for Computational Linguistics. URL `https://aclanthology.org/ 2025.coling-main.8/` .

- [42] A. Zeakis, G. Papadakis, D. Skoutas, and M. Koubarakis. Distiller: Knowledge distillation in entity resolution with large language models, 2026. URL `https://arxiv.org/abs/2602. 05452` .

- [43] Z. Zhang, P. Groth, I. Calixto, and S. Schelter. ANYMATCH – efficient zero-shot entity matching with a small language model. In _AAAI 2025 Workshop on Preparing Good Data for Generative AI: Challenges and Approaches_ , 2025. URL `https://openreview.net/forum? id=Nees1OD5td` .


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "OpenSanctions Pairs: Large-Scale Entity Matching with LLMs" (2026-02-24). https://arxiv.org/abs/2603.11051
