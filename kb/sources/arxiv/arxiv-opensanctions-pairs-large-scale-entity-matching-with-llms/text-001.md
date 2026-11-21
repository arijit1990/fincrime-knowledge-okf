---
type: Source Text
title: 'OpenSanctions Pairs: Large-Scale Entity Matching with LLMs - part 1 of 3 (pp. 1-7)'
description: 'Verbatim extracted text, pp. 1-7: OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching; OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching > 1 Introduction; OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching > 2 Related work; and 3 more sections'
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
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.11051
  title: 'OpenSanctions Pairs: Large-Scale Entity Matching with LLMs'
  author: org:arxiv
  last_modified: '2026-02-24T00:00:00Z'
---

# OpenSanctions Pairs: Large-Scale Entity Matching with LLMs

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2026-02-24), part 1 of 3, pp. 1-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## OpenSanctions Pairs: A Large-Scale Dataset for Pairwise Entity Matching


[p. 1]

Chandler Smith1_,∗_

Magnus Sesodia1_,∗_ Friedrich Lindenberg2 Christian Schroeder de Witt1

1University of Oxford 2OpenSanctions _∗_ Equal Contribution

We release OpenSanctions Pairs,1 the first large-scale public benchmark for entity matching on sanctions and OSINT data. The dataset includes 755,540 expertlabeled pairs over 1 million entities, aggregated from 293 source datasets across 45 jurisdictions. It captures real-world diversity in compliance data, spanning multiple languages and writing systems (e.g., Latin, Cyrillic, Arabic), inconsistent structure, and time-varying provenance, and is substantially more heterogeneous than prior entity matching benchmarks. As baselines, we evaluate the production rule-based matcher (nomenklatura RegressionV1) alongside open- and closed-source LLMs in both zero- and few-shot settings, each tested with and without MIPROv2 prompt optimization to control for prompt sensitivity. The rule-based baseline reaches 91.3% F1; GPT-4o achieves the best result at 99.0% F1, and a locally deployable open-source model (DeepSeek-R1-Distill-Qwen-14B) achieves 98.2% F1. The rule-based baseline and LLMs fail in complementary ways: rules over-match, while LLMs struggle with cross-script transliteration. These results suggest that pairwise matching performance is approaching a practical ceiling and shift attention toward pipeline components such as blocking, clustering, and uncertainty-aware review.

### 1 Introduction


[pp. 1-2]

Entity matching (EM) determines whether two records refer to the same real-world entity. The task is also known as entity resolution, record linkage, field matching, and deduplication, with the latter typically referring to matching records within the same dataset and record linkage to matching across different datasets [2, 8]. EM is a core component of data integration pipelines, as matching errors propagate directly to downstream entity graph construction and analysis [8, 10]. We focus on the open-source intelligence (OSINT) setting, in which entity records are aggregated from publicly published sanctions designations, regulatory watchlists, politically exposed person (PEP) registers, and corporate registries [24].

Sanctions screening is one of the most operationally consequential applications of entity matching: banks and other regulated firms are legally required to check every customer against sanctions lists published by major jurisdictions, and compliance failures attract fines in the hundreds of millions of dollars [39]. Effective matching is also central to detecting sanctions evasion, where individuals obscure ownership through shell companies and name variations across jurisdictions [19]. Despite this importance, sanctions data are typically proprietary or access-restricted, and to our knowledge no public benchmark for pairwise entity matching on sanctions data has been published.

Existing EM benchmarks, meanwhile, are largely drawn from e-commerce and bibliographic domains and typically rely on a small number of datasets, often as few as two, with closely aligned schemas, fixed field sets, and relatively standardized entity representations [14, 15, 22, 32]. As a result, they

> 1Dataset: `https://huggingface.co/datasets/sanctions-er-anon/opensanctions_pairs` . Code: `https:// github.com/chansmi/OSINT_entity_resolution` .

Preprint.

fail to reflect deployment settings such as sanctions, in which matching is performed across tens to hundreds of datasets with heterogeneous schemas, overlapping but non-identical fields, missing values, and entities represented through aliases or transliterations across multiple scripts (e.g., Cyrillic, Arabic, Chinese, Japanese, and Korean).

To address this gap, we present the first systematic study of pairwise EM techniques on large-scale sanctions data in collaboration with OpenSanctions2 . We aggregate 293 datasets from 45 jurisdictions, with human analysts performing pairwise matching [24]. From this process, we extract 755,540 labeled entity pairs covering over one million unique entities.

[p. 2]

Our experiments show that LLM-based methods reach F1 scores up to 99.0%, compared to 91.3% for the legacy rule-based matcher previously used in production. We accordingly position OpenSanctions Pairs as a benchmark supporting evaluative claims about (i) pairwise matching accuracy on heterogeneous, multi-script, partial-evidence records, (ii) failure-mode analysis across rule-based and learned systems, and (iii) generalization across source provenance and entity schemas. End-to-end clustering, real-time screening latency, and adversarial sanctions-evasion robustness are out of scope; we discuss these boundaries and the broader pipeline (blocking, clustering, uncertainty-aware review) in Section 6 [3, 10].

Within that scope, the accuracy gap on the pairwise task carries tangible operational weight. Sanctions screening underpins anti-money-laundering, counter-terrorism financing, and enforcement against kleptocratic regimes, and is run continuously at scale by every regulated financial institution; the difference between a 91% and a 99% F1 matcher compounds into both materially fewer missed designations slipping into the legitimate economy and a substantial reduction in the analyst hours spent triaging false positives.

Our contributions:

1. Dataset. We release OpenSanctions Pairs, a 756K-pair, 1.0M-entity benchmark spanning 293 sources across 45 jurisdictions. It is the first public sanctions-OSINT entity-matching dataset and is an order of magnitude larger and substantially more heterogeneous than prior EM benchmarks.

2. Reference baselines. We benchmark a production rule-based matcher and a range of openand closed-source LLMs (zero-shot, few-shot, and DSPy-optimized) to characterize task difficulty and surface failure modes that motivate future entity-resolution research.

### 2 Related work


[pp. 2-3]

Entity matching datasets Standard benchmarks include product datasets such as Abt/Buy [35] and Amazon/Google Products [35], as well as bibliographic datasets such as DBLP/ACM [35] and DBLP/Scholar [35]. These typically involve pairwise matching between two sources with clean, structured, and monolingual attributes. More recent benchmarks such as WDC Products increase scale and difficulty, but remain focused on e-commerce settings with limited source heterogeneity. The closely related WDC Large-Scale Product Corpus [34] reaches 16M offers via distantly-supervised schema.org cluster identifiers rather than expert review, trading label fidelity for scale within a single e-commerce domain. Across domains, existing datasets are characterized by few sources, scalar attributes, and limited variation in scripts or provenance. Moslemi et al. [20] formalize this gap, distinguishing representation from semantic heterogeneity and noting that current benchmarks rarely stress both dimensions simultaneously.

Our benchmark differs in scale (755,540 expert-labeled pairs), source heterogeneity (293 sources across 45 jurisdictions), and representation (multi-script names, set-valued and time-dependent attributes), reflecting operational sanctions OSINT rather than clean bilateral catalogs; Table 1 provides a quantitative comparison.

Entity matching methods EM originated in probabilistic formulations developed for administrative record linkage [5, 8]. Early work established the core pipeline of blocking, matching, and clustering, introducing methods to reduce candidate comparison costs [10, 11, 28, 29]. Neural approaches subsequently improved robustness to noisy and text-heavy data by learning attribute representations

> 2 `https://opensanctions.org`

Table 1: Comparison with existing entity matching benchmarks. Entities reports the total number of distinct entity records appearing in the labeled corpus (undeduplicated across sources for all rows). Matches is the count of ground-truth positive pairwise matches; * denotes deduplicated product clusters, not pairwise matches.

[p. 3]

|Dataset|Entities|Matches|Sources|Unique Fields|Domain|
|---|---|---|---|---|---|
|Fodors-Zagat [21,22]|864|110|2|6|Restaurant|
|Abt-Buy [35]|2,173|1,097|2|4|E-commerce|
|Amazon-GoogleProducts [35]|4,589|1,300|2|4|E-commerce|
|DBLP-ACM [35]|4,910|2,220|2|4|Bibliographic|
|BeerAdvo-RateBeer [21,22]|7,345|68|2|4|Beverage|
|WDC Products [32]|11,715|2,162_∗_|3,259|5|E-commerce|
|MusicBrainz20k [35]|19,375|16,250|5|10|Music|
|Walmart-Amazon [21,22]|24,628|962|2|5|E-commerce|
|Company [21,22]|56,316|28,200|2|1|Company|
|iTunes-Amazon [21,22]|62,830|132|2|8|Music|
|DBLP-Scholar [35]|66,879|5,347|2|4|Bibliographic|
|OpenSanctions (ours)|1,002,093|581,149|293|131|Sanctions|

directly, with systems such as Magellan demonstrating gains over rule-based methods [13, 21]. Pretrained language models further advanced EM by encoding entire entity pairs as sequences and fine-tuning transformer-based classifiers [18, 27]. Parallel work has explored probabilistic and Bayesian formulations that explicitly model uncertainty and matching constraints [36, 38].

The most recent line of work applies large language models to entity matching via prompting, incontext learning, and fine-tuning, often achieving strong performance with minimal task-specific adaptation [6, 16, 17, 23, 30, 31, 37, 40, 41]; most closely related, Peeters et al. [33] show LLM-based methods are more robust to out-of-distribution entities than fine-tuned pretrained language models. Beyond pairwise prompting, in-context clustering [9], smaller-LM variants [43], and knowledge distillation from large to small models [42] address inference cost at scale. Recent work has also applied NLP methods specifically to sanctions screening, improving over traditional fuzzy matching [12]; surveys cover classical and neural approaches [1].

### 3 Dataset: OpenSanctions Pairs


#### 3.1 Background


International sanctions are imposed by authorities including the UN Security Council, the US Treasury’s Office of Foreign Assets Control (OFAC), the EU Foreign Service, and HM Treasury (UK) [7], and their enforcement notices are published as open-source intelligence (OSINT) that downstream users such as banks, NGOs, and investigative journalists must aggregate and reconcile. These lists overlap substantially, and the same individual may appear on multiple lists under different name transliterations, aliases, or with varying metadata. OpenSanctions addresses this fragmentation by aggregating 293 source datasets from 45 jurisdictions into a unified database. As part of this integration, human analysts perform pairwise deduplication to identify when records from different sources refer to the same real-world entity.

#### 3.2 Source aggregation


[pp. 3-4]

OpenSanctions Pairs is constructed from the OpenSanctions database, a continuously maintained aggregator of sanctions, regulatory, and OSINT records contributed by 293 source datasets spanning 45 jurisdictions of provenance.3 Sources fall into five functional categories: (i) national regulator sanctions lists (US OFAC SDN, EU consolidated list, Ukrainian sanctions list, and similar); (ii) politically-exposed-person (PEP) and political-position registries derived primarily from Wikidata; (iii) general knowledge-graph extracts from Wikidata; (iv) national corporate registries; and (v) a long tail of leak-derived datasets (notably ICIJ Offshore Leaks) and other watchlist publications,

> 3 `https://www.opensanctions.org/datasets/`

Table 2: Pair-level schema combinations. Analyst-judged pairs (top block) are over genuine matching subjects and contain both positive and negative judgments. Auto-merge pairs (bottom block) are relational records (Occupancy, Succession, Ownership, etc.) that propagate when a parent entity match is recorded; they are 100% positive by construction.

|Schema combination|Pairs|Share|Pos / Neg|
|---|---|---|---|
|_Analyst-judged matching subjects_||||
|Person, Person|284,808|37.7%|203K / 81K|
|Company / Organization / LegalEntity (any)|175,311|23.2%|89K / 86K|
|Position, Position|26,330|3.5%|24K / 3K|
|Vessel, Vessel|7,550|1.0%|5K / 2K|
|Person, LegalEntity, other cross-schema|7,299|1.0%|7K / 0.3K|
|Subtotal, analyst-judged|501,298|66.4%|328K / 173K|
|_Auto-merge propagations (100% positive)_||||
|Occupancy, Occupancy|213,448|28.3%|213K / 0|
|Succession, Succession|33,607|4.4%|34K / 0|
|Ownership / Family / Directorship / other|7,187|1.0%|7K / 0|
|Subtotal, auto-merge|254,242|33.6%|254K / 0|
|Total|755,540|100.0%|581K / 174K|

[p. 4]

contributing under 1% of pairs. Contribution is heavy-tailed: the top ten datasets account for 82.0% of entity appearances (Gini coefficient 0.934 over per-source entity counts), while the remaining 283 sources together contribute the other 18%. A small number of large public registries dominate volume; most of the benchmark’s diversity in jurisdiction, language, and schema comes from the long tail.

Time period. Underlying source publications such as the US OFAC SDN list and the EU consolidated list date back decades. The entities in this release were ingested into the OpenSanctions store between May 2019 and November 2025, with the bulk added from 2023 onward as the aggregator matured (44.8K entities ingested in 2019, 196K in 2023, 421K in 2024, 337K in 2025).4 Analyst pairwise judgments were accumulated continuously over the OpenSanctions deduplication workflow between 2021 and 2025 [24]. The contribution of the present paper is to freeze, version, and publicly release the resulting labeled pair corpus as a research benchmark with reference baselines, rather than to document the production matcher itself [24, 26].

#### 3.3 Construction pipeline


[pp. 4-5]

The corpus consists of 755,540 pairwise entity-matching judgments produced by a two-stage pipeline that combines automated candidate generation with manual analyst review [24, 26].

Blocking. An inverted index over name n-grams, identifiers (passport, tax ID, phone), and other indexable attributes generates candidate pairs from the _O_ ( _n_2 ) comparison space. The blocker is tolerant to spelling and transliteration variation through character n-gram matching and Unicode normalization; implementation details are documented in the `nomenklatura` package [25]. Records sharing no indexable surface features are filtered out before review, producing the 76.9%/23.1% positive/negative skew in the labeled corpus.

Manual review. Analysts review candidate pairs through a text-based side-by-side interface, comparing fields, aliases, and source provenance, and may consult external public sources for ambiguous cases. Each judgment is audit-logged against a canonical entity ID and may be revisited as new evidence arrives. Labels are produced by full-time OpenSanctions analysts in the production deduplication workflow, not by anonymous crowdworkers.

> 4 `first_seen` timestamps reflect ingestion into the OpenSanctions store, not publication of the underlying source list, which is typically older.

{ {"id": "pk -cnic "id": "pk -cnic-3520114139885" , -3710502620181" ,"caption ": "Khalid Mehmood", "caption ": "Khalid Mehmood","datasets ": [" pk_proscribed "datasets ": [" pk_proscribed"], "],"properties ": { "properties ": {"name ": [" Khalid Mehmood "name ": [" Khalid Mehmood"], "],"fatherName ": [" Muhammad = "fatherName ": [" HajiKhan"], Muhammad "],"idNumber ": "idNumber ":["3520114139885"] , ["3710502620181"] ,"address ": ["LAHORE , "address ": ["ATTOCK ,Punjab "], Punjab "],"country ": ["pk"] "country ": ["pk"]... ...} }} }

Figure 1: Example entity pair illustrating the difficulty of pairwise matching. These two individuals on Pakistan’s proscribed persons list share the _exact same name_ , country, and sanctions program, yet they are different people with distinct national ID numbers and fathers. The Nomenklatura baseline assigned this pair a 0.98 match score, near the maximum possible, demonstrating how name-based matching fails for common names without unique identifiers.

[p. 5]

What blocking leaves behind. Surviving negatives are not random: they share surface features such as common names, sanctions programs, or nationalities, and their interquartile ranges of shared exact-value fields nearly coincide with those of positives (Section 3.4). The benchmark therefore measures methods on the _hard_ portion of the matching distribution, not the easy portion already triaged by the index.

We characterize the labeled corpus along the axes that matter for entity resolution: schema mix, source and field structure, script coverage, and cross-source provenance.

Schema mix and the auto-merge tier. Table 2 breaks the 755,540 labeled pairs down by the schema combination on the two sides. Two-thirds (66.4%) are pairs over genuine matching subjects: Person– Person (37.7%), any combination of Company / Organization / LegalEntity (23.2%), Position–Position (3.5%), Vessel–Vessel (1.0%), and a small set of cross-schema pairs (1.0%). The remaining 33.6% are pairs over relational records that propagate automatically when a parent Person or Organization match is recorded. For example, an Occupancy record links a person to a political position, so whenever two Person records are merged, their two Occupancies that link to the same Position are merged with them. These auxiliary pairs are part of the released corpus, and they are 100% positive by construction with zero analyst-recorded negatives. Because every method evaluates these pairs in the same way and they are independent per-pair predictions, the auto-merge tier inflates absolute F1 uniformly across all baselines without changing relative rankings; we publish the schema-combination flag in the released metadata so that future work training across pairs (where the leakage matters more) can subset to the analyst-judged 66.4% directly.

#### 3.4 Statistics and heterogeneity


[pp. 5-6]

Sources, fields, and scripts. The 293 sources contribute entity volume very unequally (Gini 0.934, top-10 = 82% of entity appearances), and entities re-appear across sources at a median of one dataset (mean 1.32, max 28). Property fields are sparse: the median entity has 5 populated fields (mean 6.06, p25/p75 = 4/8, max 35), and only 13.8% have an `alias` or `weakAlias` populated. The benchmark therefore reflects the partial-evidence regime real compliance workflows operate in, not the densely populated record style typical of academic EM datasets. Entity captions span seven Unicode scripts (94.19% Latin, 5.25% Cyrillic, 0.40% Chinese/Japanese/Korean, 0.10% Arabic, with Greek, Hebrew, Devanagari, and Thai together making up the remainder). 6.87% of pairs include at least one non-

Latin entity and 3.83% are cross-script (Latin on one side, non-Latin on the other), so a system that ignores transliteration will miss roughly one in twenty-five labeled pairs.

Cross-source structure and difficulty. The most distinctive property of OpenSanctions Pairs is that 64.7% of all pairs, and 82.0% of _positive_ pairs, are cross-source: the two entities under comparison originate in different source datasets and share no common dataset of origin. The labels overwhelmingly capture aggregation-level identity claims across heterogeneous publishers, not within-source duplicates of a single registry. A further 12,453 positive pairs cross country fields outright, with both sides carrying non-empty but disjoint country values. Pair difficulty follows from this construction. Positive and negative pairs differ in mean shared fields (4.71 vs. 3.73, medians 4 vs. 3) but their interquartile ranges overlap, because blocking has already triaged the easy negatives. A naive constant-positive predictor on the 76.9%-positive distribution achieves _F_ 1 = 0 _._ 870 and accuracy = 0 _._ 769, comfortably below the 91.3% rule baseline (Table 3) and far below the LLM ceiling near 99%, so the benchmark discriminates non-trivial methods from trivial ones.

#### 3.5 Data and code availability


[p. 6]

The dataset is released under CC-BY-NC 4.0 (matching upstream OpenSanctions terms) and is hosted on Hugging Face at `https://huggingface.co/datasets/sanctions-er-anon/ opensanctions_pairs` ; a Croissant metadata file (with Responsible AI fields) accompanies the release. Reproduction code is at `https://github.com/chansmi/OSINT_entity_resolution` .

Given a structured corpus _D_ and two entities _e, e__′_ _∈D_ , each represented as a set of attribute-value pairs, the task is to predict a binary judgment _M_ ( _e, e__′_ ) _∈{_ 0 _,_ 1 _}_ , where 1 indicates that the two records refer to the same real-world entity. Attribute values are sets rather than scalars, since sanctions records routinely carry multiple aliases, nationalities, or addresses, and the empty-set case captures missing fields uniformly. Each released record is a JSON object `{"left": {...}, "right": {...}, "judgement": "positive"` _|_ `"negative"}` , where each side carries the entity schema shown in Figure 1.

### 4 Task formalization and example


Figure 1 illustrates why the task is non-trivial even on the labeled, post-blocking portion of OpenSanctions. Two distinct individuals on Pakistan’s proscribed-persons list share an exact name, country, and sanctions program; the RegressionV1 rule-based baseline scores them at 0.98, near the ceiling. Only their national ID numbers and fathers’ names betray the mismatch, and a method without per-field conflict reasoning has no way to recover the correct label.

We use the dataset to benchmark three method families. The aim is not to set a new state of the art, but to characterize task difficulty, show that the dataset discriminates between methods, and surface failure modes that motivate future work on the broader resolution pipeline.

### 5 Experiments and analysis


#### 5.1 Reference baselines


[pp. 6-7]

We compare three method categories aligned with Table 3:

1. Rule-Based Baseline. OpenSanctions’ production matcher RegressionV1 [25]: a logistic regression over 18 features covering name similarity (token overlap, Levenshtein, phonetic), date comparison, identifier overlap, and demographic consistency.

2. Open-Source LLMs. Llama-3.1-8B-Instruct and DeepSeek-R1-Distill-Qwen-14B (Qwen2.5-14B backbone), chosen for local deployability and reproducibility.

3. Proprietary LLMs. Seven closed-source models accessed via API, spanning lightweight (GPT-5 Nano) to frontier (GPT-5.2 Pro, Claude Opus 4.5).

Table 3: Main results. Configurations marked “(opt)” use DSPy MIPROv2 prompt optimization. Best results in Accuracy and F1 are shown in bold . See Section 5.2 for the sample sizes used.

[p. 7]

|Model|Config|Acc._↑_|F1_↑_|Prec._↑_|Recall_↑_|
|---|---|---|---|---|---|
|_Rule-Based Baseline_nomenklatura/RegressionV1|—|85.45|91.33|84.46|99.42|
|_Open-Source Models_||||||
|Llama-3.1-8B|0-shot|90.40|94.05|89.84|98.67|
|Llama-3.1-8B|0-shot (opt)|93.88|95.94|97.98|93.97|
|Llama-3.1-8B|2-shot (opt)|93.00|95.46|94.85|96.08|
|Llama-3.1-8B|4-shot (opt)|93.25|95.64|94.72|96.57|
|Llama-3.1-8B|8-shot (opt)|93.88|95.94|97.98|93.97|
|DeepSeek-R1-Distill-Qwen-14B|0-shot|96.53|97.76|96.24|99.33|
|DeepSeek-R1-Distill-Qwen-14B|0-shot (opt)|97.31|98.23|98.60|97.86|
|_Proprietary Models_||||||
|GPT-3.5 Turbo|0-shot|91.84|94.49|98.16|91.10|
|GPT-4o|0-shot|98.38|98.95|98.78|99.11|
|GPT-5 Nano|0-shot|92.40|95.24|91.77|98.99|
|GPT-5 Nano|0-shot (opt)|92.76|95.46|92.21|98.94|
|GPT-5.2 Pro|0-shot|97.75|98.53|98.37|98.69|
|GPT-5.2 Pro|4-shot|98.07|98.75|98.75|98.75|
|GPT-5.2 Pro|8-shot|97.79|98.56|98.46|98.65|
|Claude 3 Haiku|0-shot|88.00|92.68|86.77|99.44|
|Claude 3.7 Sonnet|0-shot|96.25|97.50|99.00|96.05|
|Claude Opus 4.5|0-shot|93.26|95.45|99.11|92.05|
|Claude Opus 4.5|0-shot (opt)|93.54|95.65|99.13|92.41|


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "OpenSanctions Pairs: Large-Scale Entity Matching with LLMs" (2026-02-24). https://arxiv.org/abs/2603.11051
