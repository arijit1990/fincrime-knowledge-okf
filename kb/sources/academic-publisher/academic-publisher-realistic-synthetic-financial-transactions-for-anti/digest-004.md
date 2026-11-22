---
type: Source Digest
title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models - part 4 of 4 (pp. 20-24)
description: 'Verified paraphrased digest, pp. 20-24: Supplementary Material > E Additional GNN Experiments; Supplementary Material > F Additional GBT Experiments; Supplementary Material > G Datasheet'
resource: https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
tags:
- academic_finding
- academic_paper
- datasets_benchmarks
- global_academic
- network_graph
status: stable
source_id: academic-publisher-realistic-synthetic-financial-transactions-for-anti
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-12-15'
legal_status: unknown
part: 4
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:02Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:02Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:02Z'
sources:
- id: original
  resource: https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
  title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models
  author: org:academic_publisher
  last_modified: '2023-12-15T00:00:00Z'
digest_points: 32
---

# Realistic Synthetic Financial Transactions for Anti-Money Laundering Models (digest)

[previous part](digest-003.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 20-24) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## E Additional GNN Experiments

- **descriptive / context**: The GNN code is publicly available on GitHub under an Apache License and is implemented with PyTorch Geometric version 2.3.1 and PyTorch version 2.0.1. (p. 20)[^original]  
  <sub>anchor: "Our GNN code is included with the supplementary material and available publicly on GitHub4 under an Apache License."</sub>
- **descriptive / method**: All baseline GNN experiments were run on an internal cluster using Nvidia Tesla V100 GPUs, with the same model size of 2 GNN layers and a hidden embedding size of 64. (p. 20)[^original]  
  <sub>anchor: "All the baseline GNN experiments were run on an internal cluster on Nvidia Tesla V100 GPUs."</sub>
- **descriptive / finding or result**: Total GPU time, including initial experiments and hyperparameter optimization, is estimated at around 1000 GPU hours. (p. 20)[^original]  
  <sub>anchor: "The total GPU time, including initial experiments and hyperparameter optimization, is estimated to have been around 1000 GPU hours."</sub>
- **descriptive / finding or result**: Table 12 reports training times (TTT, seconds) and inference throughput (TPS) for GIN: HI-Small 22703 s and 17210 TPS; LI-Small 29655 s and 15784 TPS; HI-Medium 85652 s and 7101 TPS; LI-Medium 85994 s and 7316 TPS. (p. 20)[^original]  
  <sub>anchor: "|GIN|22703|17210|29655|15784|85652|7101|85994|7316|"</sub>
- **descriptive / finding or result**: Table 12 reports for GIN+EU: HI-Small 26046 s and 11844 TPS; LI-Small 36625 s and 11640 TPS; HI-Medium 85753 s and 4981 TPS; LI-Medium 85887 s and 5097 TPS. (p. 20)[^original]  
  <sub>anchor: "|GIN+EU|26046|11844|36625|11640|85753|4981|85887|5097|"</sub>
- **descriptive / finding or result**: Table 12 reports for PNA: HI-Small 27745 s and 16557 TPS; LI-Small 39648 s and 14994 TPS; HI-Medium 85654 s and 6725 TPS; LI-Medium 85827 s and 6819 TPS. (p. 20)[^original]  
  <sub>anchor: "|PNA|27745|16557|39648|14994|85654|6725|85827|6819|"</sub>
- **descriptive / definition**: Precision measures the accuracy of laundering predictions, recall measures the ability to identify all laundering instances, and the F1 score is the harmonic mean of precision and recall. (p. 20)[^original]  
  <sub>anchor: "Precision evaluates the accuracy of laundering predictions, recall measures the model’s ability to identify all laundering instances"</sub>
- **descriptive / finding or result**: Table 13 gives minority-class laundering recall for GIN: HI-Small 38.16 ± 5.92; LI-Small 14.59 ± 2.37; HI-Medium 39.86 ± 3.61; LI-Medium 8.07 ± 9.32 (%). (p. 20)[^original]  
  <sub>anchor: "|GIN [65, 25]|38_._16_±_5_._92|14_._59_±_2_._37|39_._86_±_3_._61|8_._07_±_9_._32|"</sub>
- **descriptive / finding or result**: Table 13 gives minority-class recall for GIN+EU: HI-Small 55.41 ± 5.96; LI-Small 23.26 ± 2.87; HI-Medium 48.06 ± 6.45; LI-Medium 5.51 ± 6.82 (%). (p. 20)[^original]  
  <sub>anchor: "|GIN+EU [11, 15]|55_._41_±_5_._96|23_._26_±_2_._87|48_._06_±_6_._45|5_._51_±_6_._82|"</sub>
- **descriptive / finding or result**: Table 13 gives minority-class recall for PNA: HI-Small 53.15 ± 2.26; LI-Small 16.43 ± 2.62; HI-Medium 47.42 ± 4.30; LI-Medium 20.44 ± 0.66 (%). (p. 20)[^original]  
  <sub>anchor: "|PNA [60]|53_._15_±_2_._26|16_._43_±_2_._62|47_._42_±_4_._30|20_._44_±_0_._66|"</sub>
- **descriptive / finding or result**: Table 14 gives minority-class precision for GIN: HI-Small 27.40 ± 7.98; LI-Small 5.14 ± 3.42; HI-Medium 47.78 ± 5.20; LI-Medium 5.23 ± 3.60 (%). (p. 20)[^original]  
  <sub>anchor: "|GIN [65, 25]|27_._40_±_7_._98|5_._14_±_3_._42|47_._78_±_5_._20|5_._23_±_3_._60|"</sub>
- **descriptive / finding or result**: Table 14 gives minority-class precision for GIN+EU: HI-Small 42.29 ± 10.69; LI-Small 21.60 ± 10.83; HI-Medium 52.56 ± 8.27; LI-Medium 12.13 ± 19.35 (%). (p. 20)[^original]  
  <sub>anchor: "|GIN+EU [11, 15]|42_._29_±_10_._69|21_._60_±_10_._83|52_._56_±_8_._27|12_._13_±_19_._35|"</sub>
- **descriptive / finding or result**: Table 14 gives minority-class precision for PNA: HI-Small 58.48 ± 10.67; LI-Small 17.37 ± 5.80; HI-Medium 69.12 ± 4.26; LI-Medium 36.50 ± 10.51 (%). (p. 20)[^original]  
  <sub>anchor: "|PNA [60]|58_._48_±_10_._67|17_._37_±_5_._80|69_._12_±_4_._26|36_._50_±_10_._51|"</sub>
- **descriptive / method**: Figure 9 gives example precision-recall curves, taken from the best-performing seed of the best-performing model (PNA) on all small and medium AML datasets, showing the trade-off across decision thresholds. (p. 20)[^original]  
  <sub>anchor: "The examples are taken from the best-performing seed from the best-performing model (PNA) on all small and medium AML datasets."</sub>

## F Additional GBT Experiments

- **descriptive / finding or result**: Precision-recall curves for XGBoost models using Graph Feature Preprocessor features correspond to the 'GFP+XGBoost' row of Table 2; the steep slope after the threshold-0.5 point shows that higher recall is hard to obtain without significantly degrading precision. (p. 20)[^original]  
  <sub>anchor: "The steep slope of each curve after the red dot, which represent a data point obtained using the prediction threshold of 0.5, indicates that it is challenging to obtain higher recall"</sub>
- **descriptive / finding or result**: Higher XGBoost precision can be achieved by reducing recall by a few percent. (p. 20)[^original]  
  <sub>anchor: "Note that it is possible to achieve higher precision of these XGBoost models by simply reducing the recall by a few percent."</sub>
- **descriptive / method**: Figure 10 shows per-bank performance for the LI-Medium and LI-Large datasets, analogous to Figure 6, comparing private graph/private model, private graph/shared model and shared graph/shared model settings across banks. (p. 21)[^original]  
  <sub>anchor: "The experiment is explained in Section 4 and the plot is analogous to Figure 6, but here we are using the LI - _Medium_ and LI - _Large_ datasets."</sub>
- **descriptive / finding or result**: The LI datasets contain fewer illicit transactions than the HI-Medium and HI-Large datasets, making it more challenging to build a model for a bank using only local data. (p. 21)[^original]  
  <sub>anchor: "These dataset contain fewer illicit transactions compared to the HI - _Medium_ and HI - _Large_ datasets (see Table 4)."</sub>
- **descriptive / finding or result**: Average minority-class F1 across 30 banks with only local data is 4.9% for LI-Medium and 8.7% for LI-Large. (p. 22)[^original]  
  <sub>anchor: "the average minority-class F1 score across 30 banks shown in Figure 10 is only 4 _._ 9% for LI - _Medium_ and 8 _._ 7% for LI - _Large_ ."</sub>
- **descriptive / finding or result**: Sharing the transaction graph and global model across banks raises average minority-class F1 to 20.8% for LI-Medium and 22.1% for LI-Large, a improvement described as still significant compared with the private graph, private model case. (p. 22)[^original]  
  <sub>anchor: "Sharing the transaction graph and the global model across the banks increases the average minority-class F1 score to 20 _._ 8% for LI - _Medium_ and to 22 _._ 1% for LI - _Large_ ."</sub>
- **descriptive / data or feature**: Figure 11 shows precision-recall curves for XGBoost models trained on all six AML datasets (HI/LI Small, Medium, Large) using GFP graph-based features, with the threshold-0.5 F1 point marked in red. (p. 22)[^original]  
  <sub>anchor: "Figure 11: Precision-Recall Curves for the XGBoost models for all AML datasets trained using graph-based features of GFP."</sub>

## G Datasheet

- **descriptive / context**: The datasheet follows the framework of Gebru et al.; some parts were omitted because the datasets are synthetic. (p. 23)[^original]  
  <sub>anchor: "We include a datasheet based on the framework set forward by Gebru et al. [22]. Some parts of the proposed datasheet are omitted since our datasets are synthetic."</sub>
- **descriptive / context**: The dataset was created to test, develop and improve machine-learning models for financial crime detection, focusing on identifying money laundering transactions; it was created by Erik Altman on behalf of IBM and funded by IBM. (p. 23)[^original]  
  <sub>anchor: "The dataset was created to test, develop, and improve machine-learning models for financial crime detection."</sub>
- **descriptive / data or feature**: The datasets are synthetic financial transaction networks where nodes are accounts or entities and directed edges are transactions; edge features include amount, currency and transaction type, and some transactions are labelled as money laundering. (p. 23)[^original]  
  <sub>anchor: "Each node in the network represents an account/entity and each directed edge represents a transaction from one account to another."</sub>
- **descriptive / context**: All information is simulated; no real account or transaction details were used to create the datasets. (p. 23)[^original]  
  <sub>anchor: "All the information is simulated. No real account or transaction details were used to create the datasets."</sub>

## G.2 Composition

- **descriptive / data or feature**: There are 6 datasets, each consisting of one graph, with between 5M and 180M transactions. (p. 23)[^original]  
  <sub>anchor: "There are 6 datasets. Each dataset consists of one graph. The number of transactions (samples) ranges from 5M to 180M."</sub>
- **descriptive / data or feature**: Each transaction instance has features such as amount, currency, date, time and type, and its position in the whole network may be considered part of the instance because network topology matters. (p. 24)[^original]  
  <sub>anchor: "Each instance consists of a set of transaction features (incl., amount, currency, date, time, and type)."</sub>
- **descriptive / data or feature**: Each instance has a label or target; no information is missing from individual instances. (p. 24)[^original]  
  <sub>anchor: "Is there a label or target associated with each instance? Yes."</sub>
- **descriptive / context**: The datasheet states recommended data splits exist, that the authors know of no errors, noise or redundancies, and that the dataset is self-contained. (p. 24)[^original]  
  <sub>anchor: "Are there recommended data splits (e.g., training, development/validation, testing)? Yes."</sub>
- **descriptive / context**: The dataset contains no confidential data and no data that would be offensive or cause anxiety, per the datasheet answers. (p. 24)[^original]  
  <sub>anchor: "Does the dataset contain data that might be considered confidential"</sub>
- **descriptive / context**: The Kaggle page is the single source of distribution and will maintain the dataset; the generation process is in Section 4 and Appendix A, usage in the paper and potential uses in Appendix B. (p. 24)[^original]  
  <sub>anchor: "The Kaggle page acts as the single source of distribution [50]. The dataset will be maintained there."</sub>
- **descriptive / context**: The datasets are synthetic, and any number of transactions could be generated for them. (p. 24)[^original]  
  <sub>anchor: "The datasets are synthetic. Any number of transactions could be generated."</sub>

---

[previous part](digest-003.md) | [source overview](overview.md)

[^original]: Academic publisher / repository, "Realistic Synthetic Financial Transactions for Anti-Money Laundering Models" (2023-12-15). https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
