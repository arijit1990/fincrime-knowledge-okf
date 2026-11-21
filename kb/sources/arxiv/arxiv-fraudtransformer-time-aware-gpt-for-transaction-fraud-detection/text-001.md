---
type: Source Text
title: 'FraudTransformer: Time-Aware GPT for Transaction Fraud Detection - part 1 of 2 (pp. 1-6)'
description: 'Verbatim extracted text, pp. 1-6: Tiger Li; Martin Brown > CCS Concepts; Martin Brown > Keywords; and 10 more sections'
resource: https://arxiv.org/abs/2509.23712
tags:
- academic_finding
- global_academic
- ml_statistics
- preprint
- transaction_behaviour
status: stable
source_id: arxiv-fraudtransformer-time-aware-gpt-for-transaction-fraud-detection
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-09-28'
legal_status: unknown
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2509.23712
  title: 'FraudTransformer: Time-Aware GPT for Transaction Fraud Detection'
  author: org:arxiv
  last_modified: '2025-09-28T00:00:00Z'
---

# FraudTransformer: Time-Aware GPT for Transaction Fraud Detection

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2025-09-28), part 1 of 2, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Gholamali Aminian The Alan Turing Institute London, UK gaminian@turing.ac.uk

Timothy Cheuk Hin Wong HSBC

London, UK

timothy.cheuk.hin.wong@hsbc.com

Carsten Maple

Warwick University

Coventry, UK cm@warwick.ac.uk

Andrew Elliott

Glasgow University Glasgow, UK andrew.elliott@glasgow.ac.uk

Victor Claude Dehon HSBC

London, UK

victor.claude.dehon@hsbc.com

Christopher Read HSBC London, UK christopherread@hsbc.com

HSBC London, UK tiger.li@hsbc.com

## Tiger Li


Łukasz Szpruch Edinburgh University Edinburgh, UK l.szpruch@ed.ac.uk

HSBC

London, UK martin.w.brown@hsbc.com

Gesine Reinert

Oxford University

Oxford, UK

gesine.reinert@keble.ox.ac.uk

Detecting payment fraud in real-world banking streams requires models that can exploit both the order of events and the irregular time gaps between them. We introduce FraudTransformer, a sequence model that augments a vanilla GPT-style architecture with (i) a dedicated time encoder that embeds either absolute timestamps or inter-event values, and (ii) a learned positional encoder that preserves relative order. Experiments on a large industrial dataset—tens of millions of transactions and auxiliary events—show that FraudTransformer surpasses four strong classical baselines (Logistic Regression, XGBoost and LightGBM) as well as transformer ablations that omit either the time or positional component. On the held-out test set it delivers the highest AUROC and PRAUC.

## Martin Brown


### CCS Concepts


• Computing methodologies → Neural networks ; _Machine learning_ ; • Information systems → _Data mining_ ; • Security and privacy → Intrusion/anomaly detection and malware mitigation.

Fraud detection, Transformers, GPT, Time-Encoder

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _Workshop at ACM ICAIF ’25, Singapore_

### Keywords


© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM

https://doi.org/10.1145/nnnnnnn.nnnnnnn

Mo Mamouei

HSBC

London, UK

mo.mamouei@hsbc.com

Gholamali Aminian, Andrew Elliott, Tiger Li, Timothy Cheuk Hin Wong, Victor Claude Dehon, Łukasz Szpruch, Carsten Maple, Christopher Read, Martin Brown, Gesine Reinert, and Mo Mamouei. 2025. FraudTransformer: Time-Aware GPT for Transaction Fraud Detection. In _AI for Financial Fraud Detection and Prevention ._ ACM, New York, NY, USA, 9 pages. https://doi. org/10.1145/nnnnnnn.nnnnnnn

### 1 Introduction


[pp. 1-2]

Fraudulent activities, such as financial fraud, e-commerce scams, and identity theft, are becoming increasingly sophisticated, necessitating the development of advanced detection methods [9].

Conventional approaches rely on handcrafted features and while can be effective in some cases, often fail to identify nuanced patterns of fraudulent behaviour, especially in dynamic and highdimensional datasets.

There is promise in using an automated feature creation methods such as those provided by a transformer architecture. Such an architecture should be able to identify novel subtle patterns before even human monitors detect them. However transformer architectures cannot easily detect temporal information [24], potentially limiting their utility for fraud detection, as this is a time-sensitive application.

In this paper we assess the combination of a GPT architecture with time-encoders to provide time embeddings on a dataset of financial transactions. The time-encoders used here are rotational and sinusoidal embeddings combined with a positional encoder; the embeddings can be based on absolute time, or on the relative time between events. We evaluate their ability to improve detection of frauds on a dataset of financial transaction which is held by a national HSBC Payment Fraud Group. These large-scale real-world data consist of temporal patterns of customers’ digital journeys

and payments. While the limited scale and granularity of public synthetic datasets restricts the generalisability of findings based on them to real-world settings, the data used in this study naturally incorporates the noise, outliers and irregularities that are common in production systems.

Our key findings are as follows.

- Using time-encoder with a lightweight LayerNorm-based integration of the time embeddings can improve the performance of a model for fraud-detection tasks.

- Event-level relative sinusoidal embeddings paired with a learned positional encoder deliver the highest performance on the test set, outperforming three classical baselines. This comparison varies the timestamp scheme (absolute vs relative), the encoder (sinusoidal vs rotary), and the presence or absence of a positional encoder.

Based on these findings we propose an algorithm which we call _FraudTransformer_ , combining a vanilla GPT architecture with time and positional encoders.

This paper is organized as follows. Section 2 surveys related work on transformer-based fraud detection. Section 3 defines the problem. Section 6 details our FraudTransformer algorithm and GPT model. Section 4 describes the dataset, and Section 7 presents the experiments and results. Section 8 concludes and outlines directions for future work. Hyperparameter tuning results are deferred to the Appendix.

### 2 Related Works


[p. 2]

Fraud detection methods typically fall into two main groups: classical supervised learning on tabular transaction data and deep learning for tabular inputs For tabular supervised learning, gradientboosted decision trees—most notably XGBoost and LightGBM—are strong, low-latency baselines because they exploit hand-engineered behavioral features; LightGBM remains a standard reference point for card and e-commerce fraud tasks [13]. In tabular deep learning, multilayer perceptrons (MLPs) and autoencoders are common supervised and reconstruction-based options, while specialized models such as TabNet, which uses sequential feature attention to improve interpretability and often narrows the gap to boosted trees [4], and TabTransformer, which applies self-attention to categorical embeddings [11], have gained traction. In this work, we focus on transformers applications for fraud detection.

Transformer architectures have revolutionised the field of machine learning over the last 10 years. While transformer models are computationally expensive to train, once trained they can be deployed in real time. Fundamental to the advances of this approach is so-called attention, the ability of this architecture when considering a large sequence of inputs to decide what to pay attention to.

Its strengths make transformers suitable for fraud detection (e.g. see [10, 15, 23, 25]). Indeed, transformer architectures are increasingly central to fraud detection research, with investigations spanning encoder-only, decoder-only, and hierarchical designs. Encodertype models, like BERT, are typically adapted through transfer learning; for instance, [20] showed that fine-tuning a pre-trained BERT on an online-recruitment corpus led to substantial gains in detection accuracy. Similarly, decoder-only transformers have been explored by tokenizing transactional events and pre-training

GPT models on these sequences, leveraging their autoregressive nature to flag anomalous patterns, as demonstrated in [18]. To capture richer structures in tabular data, hierarchical variants have been proposed, such as TabFormer, a BERT-based architecture that embeds individual transactions before aggregating them into tablelevel representations, achieving state-of-the-art performance [15]. Building on this, [25] proposed FATA-trans to incorporate static fields—constant across all transactions—via separate encoders, further enhancing the ability of the model to detect fraud. In the FATA-trans structure, inspired by sinusoidal positional embedding, a time-aware positional embedding based on absolute timestamps of transactions is added to embedding of transactions.

Motivated by the success of generative pretrained transformers (GPT) for large language models, GPT architectures have also been employed for social security fraud detection [12]. A more detailed survey on transformer-based anomaly detection can be found for example in [14].

To the best of our knowledge, using the relative time at event level in combination with a GPT model for financial fraud detection tasks has not yet been proposed. This paper fills that gap.

### 3 Problem Statement


[pp. 2-3]

Fraud detection requires capturing complex temporal and contextual dependencies across various data modalities, such as transactional metadata, user behaviour, and timestamps. Traditional machine learning models often struggle to process such intricate relationships.

While a GPT architecture is fast, by default all tokens are assigned the same importance. Although attention mechanisms are learnt to focus on the most important features, empirically, learning time and position-dependence in features is a challenge for GPT models [16]. To address this issue, so-called positional encoders have been proposed. Positional encodings aid transformers in utilising positional information, originally regarding words in sequences. There are two widely used positional encoding schemes for transformers,

- Sinusoidal positional encoding [21];

- Rotary positional encoding [19].

A GPT transformer does not have an intrinsic notion of time and hence detecting time-dependent patterns tends to be difficult. To give the model temporal awareness, we use positional encoders but now as time encoders, replacing the usual position indices in the positional encoders with time identifiers (time-ids). In practice, we pair the two encoding methods – sinusoidal and rotary – with one of the timestamps schemes below:

- Absolute scheme: Each event has a unique timestamp in milliseconds, and we feed this absolute timestamp to the time encoders.

- Relative scheme: Instead of raw timestamps, we use the difference between timestamps of tokens or events as input to the time encoders.

The intuition behind using the Relative scheme is that of detecting patterns of time difference in the data. Also, the Absolute scheme expose calendar signals (hour-of-day, day-of-week, seasonality) and long-term trends, and let the model compare events across sequences on a shared external clock. Each account may have its

Figure 1: Event and Tokens Timestamps

own patterns, such as paying many bills at the beginning of the month and then reduced activity towards the end of the month. For detecting such patterns, rather than the Absolute timestamp, it is the time between transactions that should contains (most of) the signal.

[p. 3]

Furthermore, regarding the Relative scheme, there are two options, a _token-level_ option and an _event-level_ option. To clarify these options, as in Figure 1, suppose Event 1 has timestamp _𝐸_ 1 and tokens _𝑇_ 11, _𝑇_ 12, and _𝑇_ 13, while Event 2 has timestamp _𝐸_ 2 and tokens _𝑇_ 21, and _𝑇_ 23. In a token-level approach, we assign each token the timestamp from the corresponding event. Thus, each token in Event 1 is assigned timestamp _𝐸_ 1, and each token in Event 2 is assigned timestamp _𝐸_ 2. To compute the time difference for a token, we take the time difference to its previous token which is subsequently input to the time encoders. In the example above, the time difference for tokens _𝑇_ 12 and _𝑇_ 13 would be 0, while the time difference for token _𝑇_ 21 is _𝐸_ 2 − _𝐸_ 1; the time differences for _𝑇_ 22 and _𝑇_ 23 would again be 0. In the event-level approach, we use instead the time difference between the event to which the token belongs, and the previous event, as input to the time encoder. Now, _𝑇_ 21 would be assigned time difference _𝐸_ 2 − _𝐸_ 1, and _𝑇_ 22 as well as _𝑇_ 23 would also be assigned the time difference _𝐸_ 2 − _𝐸_ 1. After a brief exploration, we decided to use the event-level approach.

### 4 Dataset


The HSBC Payment Fraud Group dataset used in this study consists of transactions and digital journeys with labelled fraud events. The evaluation dataset was sampled to conceal the fraud rate of the main data. While this implies that the performance of all models presented here may be different on datasets with other fraud rates, the primary aim of the study is to evaluate the efficacy of different time-embedding approaches for capturing nuanced patterns in temporally irregular events like payments. We employ this dataset to evaluate the pipelines discussed in the previous section, with the following specifications.

Features: The HSBC Payment Fraud dataset contains more than 10 numerical features (e.g., transaction amount) and more than 10 categorical features (e.g., sort code); this comprehensive set of features based on events is in line of what is reported in the literature. Due to commercial sensitivity of this application domain we are unable to give a full account of all of the features. However, we highlight that in contrast to prior works that rely on the Tabformer dataset [15], our approach leverages the complete set of information throughout the customer payment journey. To construct the consumers digital journey we consider around the last 500 events.

Data splits: The dataset is constructed first using a temporal split to extract an independent test set, and a training set guaranteeing that the models are evaluated on future data. Each of these sets are

subsampled to allow scalability in training and inference and to conceal the fraud rate. The fraud rate in the test data is around 43%; this rate does not represent the fraud rate in the whole dataset but is instead obtained through undersampling non-fraud cases. An additional validation set for hyperparameter tuning is constructed by sampling from the training set. This results in a total dataset with 332 _,_ 000 samples, consisting of training ≈60 % training, ≈ 30 % validation, and ≈ 10 % test samples.

### 5 Encoding process


We reduced the cardinality of categorical variables by grouping rare and low-risk events. Numerical variables were binned. The number of bins and bin edges were chosen to closely follow their underlying distribution while minimizing the number of bins.

Similar to [18], we encode features for GPT model using a customized tokenization process with vocabulary size ( _𝑉_ ) around 4000 tokens. We do not use sub-word tokenization; every category or bucket is treated as a single token. Then, we apply token embedding for tokens. We also tokenize each column separately, so identical strings in different columns become distinct tokens. For example, “true” in column A is a different token from “true” in column B. We also apply column embedding. In the following we provide more details regarding token and column embeddings.

In the following, we let _𝑑_ emb denote the embedding size of GPT model.

This contributes _𝑉_ · _𝑑_ emb parameters and is trained end-to-end. We tie weights with the LM head (the output projection reuses _𝑊_ tok⊤), so the encoder does not introduce an additional vocabulary-scale matrix.

_Column embedding (_ _𝑒𝑡__col)._To disambiguate identical surface tokens that occur in different fields (e.g., “100” as an _amount_ vs. a _merchant_id_ ), we add a schema-aware embedding:

where _𝑐𝑡_ ∈{0 _, . . . ,𝐶_ −1} indexes the token’s source column and _𝐶_ is the number of columns. This adds _𝐶_ · _𝑑_ emb parameters and is learned jointly with the model. Intuitively, _𝑒𝑡_col provides a field-specific signal that helps the attention layers learn different patterns for different columns of features, even when the raw tokens overlap.

The input embedding, which serves as the base representation for each token, is obtained by adding the token and column embeddings.

### 6 Algorithm and Model


[pp. 3-4]

In this section, we introduce our model and algorithm for fraud detection using time-encoders and positional encoders based on absolute and relative timestamps. The diagram of our transformer block is shown in Figure 2.

We let _𝐿_ max denote the maximum sequence length (context length). We implement a vanilla GPT-style architecture [16] with 8 heads, 6 layers, context length ( _𝐿_ max) of 1024, and embedding size

Table 1: Controlled ablation axes. Only one factor is changed per row; all other settings match the full model.

|Block tested|Main question to answer?|What is varied / removed|
|---|---|---|
|Time embedding|Is any explicit time signal needed?|Remove the entire time-encoder stack (“no-time”baseline)|
|Positional encoding|Do sequence-order signals contributebeyond time stamps?|Remove the positional embeddings|
|Encoder type|Extrapolation vs. locality trade-off|Swap the rotary and the sinusoidal time encoders|
|Timestamp schemeNormalization|Absolute vs. Relative time schemeRole of Layer-Norm|Feed Absolute Unix time at event-levelRemove the LayerNorm block from time-encoders|

Figure 2: GPT Transformer with Time Encoder

( _𝑑_ emb) of 512, resulting in a model with around 20 _𝑀_ parameters. A summary of the model configuration is provided in Table 2.

This model is augmented with time and positional encoders. We train the model using the binary cross entropy loss function over the fraud and non-fraud classes. The resulting algorithm, which we call _FraudTransformer_ , supports both _Absolute_ and _Relative_ timestamps; the attention mechanism in the GPT is unchanged. The details are as follows.

_Preliminaries._ Let _𝑡_ index tokens and _𝑙_ index layers. Let _ℎ𝑡_(_𝑙_) ∈ R_𝑑_emb be the residual (pre-attention) hidden state in layer _𝑙_ for token _𝑡_ . Define a discrete time-id id _𝑡_ ∈{0 _,_ 1 _,_ 2 _, . . ._ } from wall-clock time

Table 2: Model configuration summary.

[pp. 4-5]

|Component|Setting|
|---|---|
|Architecture|Vanilla GPT-style [16]|
|Layers|6 Transformer blocks|
|Attention heads|8 per layer|
|Context length (_𝐿_max)|1024|
|Embedding size (_𝑑_emb)|512|
|Parameter count|∼20M|
|Vocabulary size|∼4000|

or offsets:

where _𝑡_ event= _𝑡_ event ( _𝑡_ ) is the time of event to which the token _𝑡_ belongs. Let _𝑝𝑡_ ∈{0 _,_ 1 _, . . ._ } be the position index of token _𝑡_ ; often, this is different from _𝑡_ event ( _𝑡_ ). For vectors _𝑎,𝑏_ ∈ R_𝑛_ , the Hadamard product is _𝑎_ ⊙ _𝑏_ = ( _𝑎_ 1 _𝑏_ 1 _, . . . ,𝑎𝑛𝑏𝑛_ ).

- (1) Time encoding (additive features). For a given base frequency _𝑓_ base, which is a hyperparameter, we build _𝑒𝑡_ ∈ R_𝑑_emb from id _𝑡_ using one of the two options below.

- _Sinusoidal encoding (GPT-style Fourier features):_ for even _𝑑_ emb, let _𝜃𝑖_ = _𝑓_ base−2_𝑖_/_𝑑_emb with base frequency _𝑓_ base and _𝑖_ =

- 0 _, . . . ,__𝑑_emb 2 − 1, and set _𝑒𝑡_sin = � sin( _𝜃_ ⊙ id _𝑡_ ) ; cos( _𝜃_ ⊙ id _𝑡_ ) � ∈ R_𝑑_emb _._

- _Rotary-derived (used additively):_ Assume _𝑑_ emb is even. Define the inverse-frequency values with base frequency _𝑓_ base:

Form angles by taking the outer product with the time-ids:

Details on the hyperparameter tuning results are given in Section 7.3.

[p. 5]

(2) Preparation (Normalization). Apply LayerNorm [5] _only_ to the time embedding _𝑒𝑡_ (with learnable parameters _𝛽𝑒,𝜏𝑒_ ):

where _𝜀 >_ 0 is used for numerical stability and

- (3) Learned Positional Encoders. We use GPT-2–style learnable positional embeddings [1]. We maintain a parameter matrix EmbPos ∈ R_𝐿_max×_𝑑_emb and perform a row lookup by position index _𝑝𝑡_ ∈{0 _, . . . , 𝐿_ max − 1}:

- We emphasize that no LayerNorm is applied to _𝑝𝑡_learn

- _𝑡_ .

- (4) Hidden-state update. Let _𝜆_ ∈ R+ be a tunable parameter which represents time gain. Update the residual stream and feed it to the unmodified block of transformer:

- _ℎ_ ¯ _𝑡_(1) = _ℎ𝑡_(1) + _𝑝𝑡_learn + _𝜆𝑒_ ˆ _𝑡,_ with _ℎ𝑡_(1) = _𝑒𝑡_tok + _𝑒𝑡_col_,_ (2) where _𝑒𝑡_tok _,𝑒𝑡_col ∈ R_𝑑_emb are token and column embeddings, respectively and _𝑝𝑡_learn _,_ ˆ _𝑒𝑡_ ∈ R_𝑑_emb . The Transformer blocks then proceed _unchanged_ with _ℎ_¯ _𝑡_(1) as input embedding.

Table 3: Model variants considered in the time–encoder ablation study. Each variant toggles three binary choices: _time scheme_ (absolute vs. Relative), _encoder type_ (sinusoidal vs. rotary), and the presence of an additional _positional_ encoder. These abbreviations are used throughout the results section.

|ID|Time encoder|Time scheme|Positional encoder|
|---|---|---|---|
|SA|Sinusoidal|Absolute|✗|
|SAP|Sinusoidal|Absolute|✓|
|SR|Sinusoidal|Relative|✗|
|SRP|Sinusoidal|Relative|✓|
|RA|Rotary|Absolute|✗|
|RAP|Rotary|Absolute|✓|
|RR|Rotary|Relative|✗|
|RRP|Rotary|Relative|✓|

### 7.2 Baselines


Here we detail the baselines against which we compare our new architecture.

_LightGBM._ A tuned gradient–boosted decision tree ensemble, [13], trained on the same partition of the training dataset. For a fair comparison, we use the same set of features in LightGBM as in the transformer models.

_GPT (“no time”)._ A transformer encoder identical to our proposed architecture except that all Absolute and Relative time encodings and positional encoding are removed. We include two versions, with and without positional encoding. These two baselines isolate the impact of explicit time modelling.

_XGBoost._ We also train an _eXtreme Gradient Boosting_ ensemble [6] on the same training split. For direct comparability, the feature set fed to XGBoost is identical to that of LightGBM.

_Logistic Regression._ As a strong linear baseline, we fit an _ℓ_ 2- regularized logistic regression model [7] on the same feature matrix. The inverse regularization strength _𝐶_ and class-weight ratio are selected by grid search on the validation fold, while all features are standardised to zero mean and unit variance. Apart from these tuned hyperparameters, we keep the scikit-learn [17] defaults, ensuring that the only difference from the tree-based models is the underlying learning algorithm.

### 7.3 Hyperparameter Tuning


We consider the time gain _𝜆_ , as defined in (2), and the base frequency, _𝑓_ base, of the sinusoidal and rotary positional encoders as tunable hyperparameters. For a fair comparison, for every hyperparameter pair, the model is trained for a single epoch and assessed on the validation set at the end of first epoch. We consider _𝜆_ = 0 _._ 01 and _𝑓_ base = 107 for our main experiments. The results are found in the Appendix 8.

### 7.4 Fraud Types


We consider multiple fraud subtypes (such as scams [3], and account takeover [2]). Although our model is trained as a binary classifier (fraud vs. non-fraud), we examine whether its performance varies by subtype. For this purpose, we create subtype-specific test sets that include only non-fraud transactions and one fraud subtype, excluding all other fraud labels. We then evaluate the fixed model (our best model) on each subset and report AUROC and PR-AUC. For example, for the scam subset, the test set contains only scam and non-fraud cases; the resulting AUROC and PR-AUC quantify how well the model separates scams from non-fraud transactions.

### 7.1 Evaluation Metrics


[pp. 5-6]

We report PRAUC (area under the precision–recall curve) and AUROC (area under the receiver–operating characteristic curve). PRAUC is particularly informative for fraud detection because the class imbalance ratio can be very high. More details can be found for example in [8].

Our ablation study is designed to isolate the contribution of each component in the temporal encoding stack. We consider three factors: (a) the _time encoder family_ (sinusoidal vs. rotary), (b) the _time scheme_ (absolute vs. event-level relative), (c) the presence of an additional _positional_ encoder (learned vs. none) and (d) the presence of Layer-Norm layer (Normalize vs. none) detailed in Table 1.

We keep the architecture, optimization settings, data splits, and preprocessing fixed across variants. We evaluate each model on the

Table 4: Baseline models and Transformer variants evaluated on the HSBC Payment Fraud Group’s test set (mean ± standard deviation over three runs; higher is better; denoted by ↑ ). TE=time encoder, PE=positional encoder. Time–encoder codes follow Table 3: S=sinusoidal, R=rotary; A=absolute timestamps, R=relative. The Δ PRAUC and Δ AUROC columns report the difference of the PRAUC and AUROC, respectively, to the mean of the Vanilla baseline (no TE, no PE).


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "FraudTransformer: Time-Aware GPT for Transaction Fraud Detection" (2025-09-28). https://arxiv.org/abs/2509.23712
