---
type: Source Text
title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers - part 4 of 4 (pp. 10-11)'
description: 'Verbatim extracted text, pp. 10-11: A Data Source Combinations; B Tabular Feature Modeling Parity with DNNs; C Architecture and Training Details'
resource: https://arxiv.org/abs/2507.23267
tags:
- academic_finding
- data_features
- global_academic
- ml_statistics
- preprint
- transaction_behaviour
status: stable
source_id: arxiv-your-spending-needs-attention-modeling-financial-habits-with-tra
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-07-31'
legal_status: unknown
part: 4
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2507.23267
  title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers'
  author: org:arxiv
  last_modified: '2025-07-31T00:00:00Z'
---

# Your Spending Needs Attention: Modeling Financial Habits with Transformers

[previous part](text-003.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2025-07-31), part 4 of 4, pp. 10-11. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## A Data Source Combinations


[p. 10]

We show that even though every source of data adds a different view of the consumer’s activity, they might not all incrementally add value to the predictive power of the model. To study the effect of each transaction set, we pretrained numerous 24M models with various combinations of 3 anonymized data sources ( _𝐴_ , _𝐵_ , _𝐶_ ), extracted those pretrained embeddings, and trained a GBT to make predictions based on the information stored in the pretrained embeddings (i.e, early fusion). Importantly, table 4 presents an ablation study comparing transaction source combinations. Unlike other tables, the baseline here is early fusion using all sources (ABC), as the goal is to understand the relative importance of each source rather than improvement over production. All other tables report improvements to the production LightGBM baseline trained on tabular features only. Overall, data source _𝐴_ clearly contains powerful information relevant for credit default. Transactions from _𝐵_ also contain useful signal that appears to be orthogonal to _𝐴_ , but _𝐶_ may slightly confuse the model or take attention from more pertinent transactions when combined with other sources.

|Source|Relative AUC Gain|vs. ABC (%)|
|---|---|---|
|A||+3.92%|
|B||-44.67%|
|C||-111.64%|
|AB||+4.95%|
|BC||-66.59%|
|AC||-1.47%|
|ABC||0.00%|

Table 4: Relative AUC gain versus the all-sources baseline (ABC) for different source combinations, computed as shortfall reduction.

Interestingly, in some cases, adding a data source can cause a decrease in performance. For example, _𝐵𝐶_ < _𝐵_ and _𝐴𝐵𝐶_ < _𝐴𝐵_ . This is caused by the additional transactions causing increased contention in the already limited context window. In this case, transactions from _𝐵_ appear to contain the least useful information, and when we include them, it pushes more useful transactions from _𝐴_ and _𝐶_ out of the model’s visibility.

This aforementioned effect can be caused by the difference in information densities and transaction frequencies between sources. In some cases, transaction sources can be sparse but relevant. For example, bill items can contain information about buy-now-pay-later loans. On the other hand, debit card can contain many (frequent) small transactions which are overall less important.

## B Tabular Feature Modeling Parity with DNNs


In this section, we explore the aspects of the DNN model that allow us to match the LightGBM performance when modeling the tabular features (numerical and categorical) highlighting the incremental gains obtained towards the challenger DNN model. Table 5 shows the improvement over the baseline (LightGBM) as we improve our DNN tabular feature model. It is important to highlight that the results shown here for each DNN and LightGBM model are obtained via hyperparameter tuning. See Appendix C for complete architecture and hyperparameter details.

The first model was a multilayer perceptron architecture (MLP), preceded by a processing step that applies standardization to numerical features and one hot encoding to categorical features. Table 5 shows that the MLP approach was unable to match the performance of LightGBM. The second was the Deep Cross Network V2 (DCNv2) architecture designed by Google [52], which is capable of modeling explicit and implicit interactions of input features to make the final prediction. For this particular network, a different feature processing is employed: numerical features are transformed through a signed _log1p_ function and categorical features are mapped to learnable embeddings via lookup table. These transformations were necessary to avoid numerical instability in the cross layers, as they do not work with sparse vectors.

Although DCNv2 achieved higher performance than MLP, it still lagged behind LightGBM baseline. Recent work [19] has shown that representing numerical attributes as dense embeddings helps to improve the performance of neural networks on tabular-based problems, either for MLP or Transformer based architectures. Following that idea, we retrained both MLP and DCNv2 models using the periodic linear (PLR) embedding approach for numerical features, which maps a real number to a dense embedding of parametrized size (number of frequencies), whose elements are periodic activations (sin and cosine) of the numerical value. Results on Table 5 show the effectiveness of this embedding technique: MLP and DCNv2 with numerical periodic embeddings outperform their previous performances, and DCNv2 + periodic embeddings was able to match the performance of LightGBM.

The use of numerical embeddings usually leads to an increase in the number of parameters of DNNs because the input vector becomes wider (depending on the dimension of the embedding). Naturally, the model becomes more prone to overfit and requires regularization to avoid losses in generalization power. Thus, in a following step, we applied L2 regularization to DCNv2 weights, which further increased performance on the test set, furthering the DCNv2 advantage against LightGBM for this problem.

[pp. 10-11]

|Model|Relative AUC Gain vs. LightGBM|
|---|---|
|MLP|-0.44 %|
|DCNv2|-0.09 %|
|MLP + PLR|-0.23 %|
|LightGBM|(baseline)|
|DCNv2 + PLR|+0.06 %|
|DCNv2 + PLR + L2|+0.08 %|

Table 5: DNN configurations vs. LightGBM baseline on tabular features.

|_DCNv2 A_|_rchitecture_|_Training_||
|---|---|---|---|
|Cross network|Low-rank|Batch size|2048|
|Deep network|[1024,512,256,128]|Epochs|1|
|Tabular projection|1024|LR (transformer)|1e-4|
|Numerical embed.|PLR, dim=8, freq=48|LR (DCNv2)|1.5e-4|
|Activation|GELU|Scheduler|Cosine|
|_Lo_|_RA_|_Optimize_|_r_|
|Rank|64|Adam_𝛽_1_, 𝛽_2|0.9, 0.999|
|Dropout|0.1|Warmup ratio|0.05|
|Target modules|c_attn, c_proj, c_fc|Weight decay|0.001|

## C Architecture and Training Details


[p. 11]

Table 6 summarizes the complete model configuration. Joint hyperparameter search is computationally prohibitive (a single 203M training run requires 7 days on 8 A100s). We instead adopt a two-stage approach: (1) freeze the pre-trained transformer and search DCNv2 hyperparameters via 60 Ray Tune trials (∼3 days on 5 H100s), then (2) perform end-to-end Joint Fusion with the selected configuration. This reduces search cost by ∼100×.

Table 6: Model and training configuration.


---

[previous part](text-003.md) | [source overview](overview.md)

[^original]: arXiv, "Your Spending Needs Attention: Modeling Financial Habits with Transformers" (2025-07-31). https://arxiv.org/abs/2507.23267
