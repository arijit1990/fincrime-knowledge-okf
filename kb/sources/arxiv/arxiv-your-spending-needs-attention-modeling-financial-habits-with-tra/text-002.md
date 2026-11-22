---
type: Source Text
title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers - part 2 of 4 (pp. 4-7)'
description: 'Verbatim extracted text, pp. 4-7: 3.2 Finetuning Embedding Models; 3.3 Modeling Tabular Features with DNNs; 4 Experimental Results; and 3 more sections'
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
part: 2
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:50:18Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:50:18Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2507.23267
  title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers'
  author: org:arxiv
  last_modified: '2025-07-31T00:00:00Z'
---

# Your Spending Needs Attention: Modeling Financial Habits with Transformers

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2025-07-31), part 2 of 4, pp. 4-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 3.2 Finetuning Embedding Models


[p. 4]

In the previous section, we introduced a formulation of transaction sequences as natural language. This facilitated pre-training user embedding models on transaction data, and learning general embeddings of user behavior. In practice, however, such models are often fine-tuned for specific tasks to achieve state-of-the-art performance. While in this section, we consider finetuning our models for binary classification problems, the same technique can be used for multi-class or even regression problems.

During supervised finetuning, a member consists of a sequence of transactions: _𝑢𝑖_ = { _𝑡_ 1(_𝑢𝑖_) _,_ · · · _,𝑡𝑁_(_𝑢_ _𝑢𝑖__𝑖_)}, and a label_𝑙𝑖_. We wish to learn a function _𝑓𝜃_ ( _𝑢𝑖_ ) = _𝑙𝑖_ . To achieve this, we take the final token (before any padding) embedding as the user representation, and

Figure 3: nuFormer pre-training pipeline from raw transactions to next-token prediction.

add an MLP network to the model, which reduces this embedding to a score. We choose the final token embedding because, since the model is causal, it is the only token with the full context of the user. Then, we optimize the MLP and the transformer weights to minimize the cross-entropy error.

Full fine-tuning of the transformer is memory-intensive, particularly when training jointly with the DCNv2 tabular network. To make training with Distributed Data Parallel (DDP) on our GPU resources feasible, we use LoRA [26], which freezes the pretrained weights and injects trainable low-rank matrices into each transformer layer. This reduces memory requirements substantially while retaining most of the performance benefit of full fine-tuning (see Section 4.5).

## 3.3 Modeling Tabular Features with DNNs


[pp. 4-5]

A motivation for transaction-based user embedding models is to alleviate the need for manual feature engineering. In the previous section, we saw how to refine the transaction embeddings for specific tasks through finetuning. However, in many cases, there are either hand-crafted features from non-transaction sources or features that are tabular by nature that are critical to model quality. Since these handcrafted features are orthogonal to the transaction data used to train the embedding models, we need to incorporate them into the final prediction. This process of combining embeddings with tabular features is denoted _blending_ or _fusion_ .

Gradient-boosted tree (GBT) models are generally considered state-of-the-art for dealing with tabular data [4], e.g., XGBoost [6] or LightGBM [31]. There are two common approaches for blending with GBTs. The first is early fusion, which blends pre-trained embeddings with tabular features using GBTs. The second is late fusion, a two-stage process, where we first finetune the transformer on a subset of the data and then train the GBT model to combine the finetuned embeddings with tabular features.

Late fusion allows for embeddings that are tailored to the task of interest and performs better than early fusion. However, these finetuned embeddings are learned in isolation from the features.

Figure 4: The difference between late fusion and joint fusion (green boxes indicate learnable parameters).

We hypothesize that finetuning jointly with blending will allow the transformer to better capture interactions between the tabular features and embedded transaction data. Hence, in contrast to both early/late fusion, we propose a system that can be trained end-toend, allowing the model to learn an optimal blending of tabular and sequential data, which we denote as joint fusion. Figure 4 shows the joint and late fusion systems.

GBTs are not compatible with joint fusion because there are no gradients from the GBT to propagate to the transformer. Motivated by these observations, we invested in DNN-based tabular feature networks, for which recent works have started to show they can be competitive with GBTs [55]. However, the performance of DNN tabular feature networks can vary drastically between problems. For example, one survey paper [35] evaluated 19 different tabular feature models (NN + GBT) on 176 distinct datasets. The authors found that each of the 19 different models outperformed all others on at least one dataset. On the other hand, there also existed at least one dataset where each model simultaneously performed the worst. Hence, making it challenging to have a one-size-fits-all approach. Therefore, we need to find a configuration that works for our problems.

[p. 5]

The first step in our approach was to achieve parity between DNNs and GBT models on only the tabular features. We selected the DCNv2 architecture [52] as it has shown success on related problems at a large scale (e.g., used by Google). However, initial results showed much worse performance for the DNN-based DCNv2 models than for the GBTs.

The recent paper [19] found that by embedding numerical attributes, they achieved significant gains when modeling numerical tabular features in DNNs. These numerical embeddings are constructed using periodic activations at different (learned) frequencies. We combined this with trainable embedding tables to also facilitate categorical feature embeddings. Combined with L2 regularization on the cross layers, this DCNv2 + PLR configuration matches and slightly exceeds the LightGBM baseline (+0.08 %) on tabular features alone, giving us a DNN tabular branch suitable for Joint Fusion. Appendix B reports the full ablation across MLP, DCNv2, and embedding variants.

Despite achieving parity with only tabular features, the last challenge to overcome was incorporating embeddings into these models while maintaining or beating the GBT model’s performance with DNNs. Three key factors were critical in achieving this. First, we

implement modifications to the DCNv2 architecture for our use case, utilizing its cross-layer capabilities to process only the embedded tabular features and project the result into a low-dimensional embedding. This feature embedding is concatenated with the transaction embedding (from the transformer), and a multi-layer perceptron is used to make the final prediction. Secondly, adding regularization in the form of weight decay and/or dropout to the customized DCNv2 layers reduced overfitting. Finally, adding normalization to the transaction embeddings improved the consistency of the customized DCNv2, allowing the DNN model to outperform the GBTs reliably. Despite the challenges in using DNNs with tabular data, we achieved a model that works well for our current tasks of interest by combining DCNv2, numerical, and categorical feature embeddings, along with regularization. We denote this joint fusion model as _nuFormer_ .

In summary, Joint Fusion required overcoming several key challenges. Specifically, replacing GBTs with neural networks that can propagate gradients, achieving DNN-GBT parity through the aforementioned careful architectural choices, and managing the memory and compute costs of jointly optimizing a 330M-parameter transformer with DCNv2. We address the latter two through LoRA [26] for memory-efficient fine-tuning and a two-stage hyperparameter search that reduces cost by approximately 100× (see Appendix C).

## 4 Experimental Results


In this section, we empirically evaluate our transformer-based embedding model for transaction data on a practical credit default prediction task. First, in section 4.1 we introduce the credit default problem in more detail as well as the LightGBM baseline. Then, in section 4.2 we explore how pre-training and joint fusion scale as a function of several model properties (model size, context length, data volume). Next, in section 4.3, we apply our transformer-based embedding models to a practical credit default modeling task using backtest data. Importantly, we show that we can achieve a 1.25% improvement in test set AUC by using our transformer models; this lift in performance is 3x a typical model launch that leads to a significant business outcome. This section includes a discussion of our production deployment of these models to over 100M+ users. Following this, in section 4.4 we show the ability of this approach to work across tasks and other regions. Finally, in section 4.5, we present an ablation of several aspects of the nuFormer model, including a comparison against a text-only model.

## 4.1 Credit Default Prediction Problem and Baseline Setup


[pp. 5-6]

In this section, we introduce the credit default prediction problem that we use in following sections to demonstrate the success of our representation learning models. The data consists of 203M training rows and 2M testing rows, where each row corresponds to a particular label and timestamp combination for a given user. Specifically, the same user might occur multiple times in the dataset, but at different times, with potentially different labels and/or transaction sets. The label is binary and represents whether user being 65 days late on a payment 6 months from the label date (1 yes, 0 no). Importantly, this label is time-delayed, which means we are attempting

to predict the user behavior in six months from the score date. The time periods covered by the train and test sets are disjoint.

Each row can contain potentially many transactions, though in some cases, members might have no transaction history. For these experiments, the transactions of a member can be generated from three independent financial products. The specific products don’t matter as much for the experiment so we denote them as sources A, B and C. In Appendix A, we ablate combinations of these sources via early fusion: source A provides the strongest single signal, source B adds orthogonal information, and source C can dilute performance by displacing higher-signal transactions within the context window. Our main experiments below use all three sources.

In total there are 291 tabular (numerical or categorical) features. Some are derived from transaction sources (e.g., average spend over a given period), but non-transaction sources such as bureau scores are also included. Unless otherwise noted, all improvements are reported as relative improvement (%) in AUC over a LightGBM model trained on tabular features only, which is our production baseline.

Our joint fusion model learns features that make some handcrafted transaction features redundant. Although not all transaction sources used to construct these features are currently provided to the model as raw transactions, in practice we can remove 90% of the redundant hand-crafted transaction features with no loss in performance.

## 4.2 Exploring Pre-Training and Finetuning of Transformer-Based User Embedding Models


[p. 6]

This section presents an analysis of how the embeddings of our finetuned LMs improve in quality as we scale and various other ablations. To begin, we define the baseline models, of which there are two, with 24M and 330M parameters, respectively. Both have a context length of 2048 and use all the transaction sources. These models are pre-trained and finetuned on 20M rows. The baseline transformers take advantage of description, amount, and date, as described in figure 1. All subsequent experiments use joint fusion, and results are reported as the relative improvement in AUC over a GBT baseline trained only on tabular features using all 203M rows. In section 4.2.1 we show that using larger models allows us to learn better features from the raw transaction data. Then, in section 4.2.2, we examine how varying the context length affects the performance of joint fusion. Finally, in section 4.2.3, we explore how the volume of finetuning data affects the downstream performance.

_4.2.1 Impact of Model Size._ We compare the AUC performance of finetuned models of two different sizes: one model consists of approximately 24M parameters while the other has approximately 330M parameters. We use a causal GPT-like decoder-only model, with 24 attention layers, each with 16 attention heads. Importantly, the two model configurations differ only in the hidden embedding size where the 330M model has a 1024 length embedding and the 24M model has a smaller 256 length embedding.

The 24M and 330M models achieve a lift of 0.37% and 0.62% over the baseline model configuration, respectively. We see an improvement from the increased capacity. The findings in this section suggest that there is a rich set of information in our data that larger models can exploit. In future work, we plan to continue

Figure 5: _nuFormer_ relative test AUC gain for different context lengths (512, 1024, 2048) with 24M and 330M models.

Figure 6: _nuFormer_ relative test AUC gain for different amounts of training data (5M, 20M, 40M, 100M) with 24M and 330M models.

experimenting with scaling up to larger models, and derive scaling laws for these transaction based user embedding models.

_4.2.2 Effect of Context Length on Joint Fusion._ In this section, we explore how varying the context length affects the performance of joint fusion. More specifically, we compare the baseline configuration using context lengths of 512, 1024 and 2048 tokens for both the 24M and 330M variants. Figure 5 shows these results, where we see that larger context lengths lead to improved performance. Moreover, we see that the larger model is better able to exploit the information in the longer contexts.

_4.2.3 Effect of Training Data Volume for Joint Fusion._ In this section, we demonstrate that the performance of our joint fusion scales as a function of the data volume. Specifically, we take two models, one 24M and one 330M, both pre-trained on 20M rows. We then finetune each of these two models on 5M, 20M, 40M, 100M rows, and plot the results, which is shown in figure 6. Importantly, we see a clear advantage to using more data with joint fusion, and that bigger models obtain a larger advantage from more data.

## 4.3 Production Deployment for Credit Default Prediction


[pp. 6-7]

This section presents a practical application of our transaction data model to a credit default prediction problem. This problem involves predicting whether a member default on a loan if given a credit limit increase. The baseline for this task attempts to predict this behavior from hand-crafted tabular features using LightGBM. Importantly, some of these tabular features are derived from transactions. Hence, our transaction embeddings do not add any new sources of data to the model. Rather, we are allowing the model to learn its own transaction features from the raw data.

|Model|Relative AUC Improvement|
|---|---|
|Late Fusion (LightGBM)|0.97%|
|Late Fusion (DCNv2)|0.97%|
|_nuFormer_|1.25%|

Table 1: Relative AUC Improvement (%) over the baseline (LGBM) for different blending approaches.

Figure 7: Extended out-of-time test-set stability analysis, comparing _nuFormer_ against the baseline.

We compare several different strategies to clearly demonstrate the advantage of our final Joint Fusion approach, which achieves an overall relative improvement of +1 _._ 25% in test AUC over the baseline model trained only on the tabular features. For reference, this is 3x the improvement typically observed when successful models realize material business impact. Furthermore, historical model improvements were obtained from adding new data sources or signals to the model. In our case, this improvement is entirely from advancements in modeling.

The data consists of one record per user interaction. Hence, the total amount of data is much greater than just one row per member. In the following experiments, we want to analyze the gain in test AUC from adding the transformer model user embeddings. We blend this model with the tabular features in the following ways:

- (1) Baseline: The existing model uses the handcrafted tabular features and is a LightGBM trained on the entire dataset. This model has no user embeddings.

- (2) Late Fusion: We finetune the model on a 20% subset of the data rows without any features, and then we use the remaining rows to train the downstream models to predict the label from the embeddings and features.

- (3) _nuFormer_ : Uses the joint fusion procedure on 203M rows.

Table 1 shows the improvements over the baseline in the test AUC from adding transaction based user embeddings.

[p. 7]

A major concern was whether the joint fusion based solution would overfit to transaction attributes (e.g., descriptions) from specific time periods. This is especially important because labels take six months to mature, so we cannot train these models on the most recent transactions. During the back-testing, we constructed an extended test set, covering a 6 month period after the data used during joint fusion. Figure 7 shows the difference in AUC for this extended test set. Importantly, we see a consistent gain over the baseline as we get further from the train period.

The nuFormer model (Joint Fusion with DCNv2) was deployed to production with the primary goal of reducing long-term user defaults. The system’s success is measured by the reduction in users being late on payments. The long lead-up to collecting the label required for the business outcome prevented us from A/B testing every variant. Hence, nuFormer is currently deployed to

100% of customers in one of our markets, serving credit decisions for over 100 million users. The remainder of this section describes the infrastructure, data integrity safeguards, and monitoring systems required for production operation.

_Inference Infrastructure._ Inference runs as a daily batch job across the full customer base. Processing 100M+ users typically requires approximately 5 hours on 60 A100 GPUs (or 150-300 L4 nodes). With a batch size of 22 on A100s, the model consumes roughly 90% of available GPU memory, reflecting the cost of long-context transformer inference at scale.

_Data Integrity._ Financial transactions are mutable: amounts, descriptions, and status fields can change as transactions move from pending to approved to reversed. If models observe updated values that were unavailable at label generation time, data leakage occurs. We implement two safeguards. Firstly, for training and inference, transactions are presented as they existed at the score date, ensuring the model only accesses information available at decision time. Secondly, automated systems compare current records against historical snapshots to detect unintended field changes. This uncovered an issue where Buy-Now-Pay-Later prepayments altered transaction timestamps, leaking future information into the present.

_Drift Monitoring._ We continuously compare recent data against training-period distributions to detect shifts that could degrade model performance. Firstly, we examine field-level drift by monitoring every input field (e.g., description text, amounts, timestamps) for distributional changes. Secondly, we examine behavioral drift by tracking shifts in usage patterns across aggregate metrics (daily transaction counts, transactions per user, total spend).

_Online Performance._ The deployed model drove a 32% increase in our long-term surrogate metric, a contribution equivalent in magnitude to an entire year’s typical cumulative gains and approximately 3× the impact of a standard modeling upgrade. Crucially, these improvements came purely from enhanced representation learning on existing transaction data, without adding new data sources or manual feature engineering. Figure 7 shows that performance gains remain stable across a 6-month out-of-time evaluation period, indicating the model does not overfit to transaction descriptions or temporal artifacts from the training period.

To evaluate whether nuFormer’s methodology generalizes beyond the primary credit task, we applied the same approach to four additional problems across markets. Each model follows the same architecture and training procedure: pre-training a transaction transformer on local transaction data, followed by Joint Fusion fine-tuning for the target task. Table 2 reports the offline results.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Your Spending Needs Attention: Modeling Financial Habits with Transformers" (2025-07-31). https://arxiv.org/abs/2507.23267
