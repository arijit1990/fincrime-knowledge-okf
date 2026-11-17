---
type: Source Text
title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers - part 1 of 4 (pp. 1-4)'
description: 'Verbatim extracted text, pp. 1-4: 1 Introduction; 2 Related Work; 3 A Transformer-Based Model for Transactions; and 1 more sections'
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
part: 1
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2507.23267
  title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers'
  author: org:arxiv
  last_modified: '2025-07-31T00:00:00Z'
---

# Your Spending Needs Attention: Modeling Financial Habits with Transformers

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2025-07-31), part 1 of 4, pp. 1-4. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

D. T. Braithwaite* , Misael Cavalcanti* , R. Austin McEver* , Hiroto Udagawa, Daniel Silva, Rohan Ramanath, Felipe Meneses, Arissa Yoshida, Evan Wingert, Matheus Ramos, Brian Zanfelice,

Aman Gupta

Nubank

{daniel.braithwaite,misael.cavalcanti,austin.mcever}@nubank.com.br

The industry standard for credit risk modeling relies on manually transforming raw transactions into tabular features, a process that often results in information loss. We propose nuFormer, a Transformer-based model that learns representations directly from raw financial sequences. Each transaction is encoded as a compact sequence of special tokens for structured attributes (amounts, timestamps) alongside tokenized descriptions, reducing token count by approximately 4× compared to text-only approaches and enabling the model to capture long-range spending patterns. To retain static risk factors, we introduce Joint Fusion, which trains the Transformer end-to-end with a tabular network. On a large-scale credit default prediction task, nuFormer achieves a 1.25% relative AUC improvement. This model was trained on ∼500 billion tokens and deployed to 100% of customers in one of our markets, serving over 100 million users. The architecture has also driven improvements in different applications (such as lending risk and income prediction) as well as in other countries with different languages. Crucially, these gains are achieved solely through enhanced representation learning rather than incorporating new data sources, validating that automated feature discovery is a scalable, operationally efficient alternative to manual feature engineering in financial systems.

## 1 Introduction


Credit risk modeling involves estimating the probability that borrowers will default on their obligations, and determines whether hundreds of millions of consumers gain access to financial products. Prediction errors in credit risk models translate to substantial financial losses and misallocated credit. Yet the richest source of predictive signal, detailed transaction histories, remains underutilized. These records capture spending patterns, payment reliability, and financial stress signals over months or years, but most production systems still compress this sequential data into handcrafted tabular features and then train traditional models such as gradientboosted trees (GBTs). While this pipeline is simple and relatively interpretable, it is labor-intensive and often discards useful information. It also handles text poorly: signals that are hard to encode as categorical variables (e.g., such as free-form descriptions) are frequently dropped altogether.

In many domains, ML has advanced toward learning representations from raw data. One example is convolutional neural networks, which automatically learn features such as edges, textures, and shapes from raw images [32, 47]. Similar approaches are employed by YouTube [8], Pinterest [38], Meta [43], and Alibaba [33, 39] to

learn user representations from event sequences. Pre-trained representations extend this, training on massive unlabeled datasets with self-supervised objectives producing effective embeddings across vision [2, 40], audio [1, 11, 41, 54, 56], and language [5, 36, 50].

Despite this aforementioned progress in representation learning, financial applications have largely remained dependent on hand-crafted features. One recent work by [3] proposes contrastive learning for event sequences (CoLES) with self-supervision for learning embeddings of user transaction sequences. A subsequent work by [48] proposes an autoregressive next-event prediction approach called NPPR. While both CoLES and NPPR facilitate the automatic discovery of features from raw transaction data, this paper addresses three limitations of these studies.

The first limitation of NPPR and CoLES is that they only utilize categorical or numerical features from the event sequence. On the other hand, we hypothesize that there is much value in learning from natural language features, e.g., descriptions. Secondly, both use RNN models, which struggle to capture long-range dependencies compared to Transformers [51], a significant limitation for transaction data with seasonal patterns. Finally, the scale of data in these studies (billions of transactions) is orders of magnitude smaller than what we work with (over 100 billion transactions across 100M+ members). This is important because scaling often improves model quality [24, 28].

[pp. 1-2]

An alternative line of work treats sequential data as natural language. In sequential recommendation, Recformer [34] serializes item attributes into text strings, enabling standard language model pre-training and generalization to unseen items. However, this textonly formulation becomes prohibitive for transaction modeling: serializing amounts, timestamps, and descriptions as natural language requires approximately 55 tokens per transaction, limiting a 2048-context model to roughly 37 transactions. Credit risk patterns (e.g., payment behavior before due dates, seasonal spending shifts, gradual financial stress) often span months of history, requiring observation of hundreds of transactions.

In this paper, we propose nuFormer, a transformer-based model for learning representations from financial transaction sequences. Our contributions are: (1) a compact tokenization scheme that encodes transactions as special tokens for structured attributes alongside BPE-tokenized descriptions, reducing per-transaction token count by 4× compared to text-only approaches; (2) Joint Fusion, an end-to-end architecture that combines transformer embeddings with tabular features via a modified DCNv2 network with periodic numerical embeddings; (3) deployment at scale to credit default prediction in one of our markets with 1.25% relative AUC improvement

*These authors contributed equally and are listed alphabetically by last name.

, and 100M+ users served; and (4) analysis of scaling properties across model size, context length, and data volume.

## 2 Related Work


[p. 2]

_Sequential Recommendation._ Sequential recommendation (SR) systems involve modeling a user’s behavior from a sequence of item interactions (e.g., purchases, clicks, etc.) and attempting to predict future actions to recommend these to the user. This is closely related to modeling transaction sequences, as items also consist of a rich set of attributes, such as text, numerical, categorical, and images.

One of the earliest applications of transformer models to SR is SASRec [27], which utilizes an ID-based representation of items. In this setup, each item is assigned a unique ID, and item embeddings are obtained from an embedding table. Importantly, item attributes are not utilized. A causal transformer is then trained using a generative next-item prediction objective, which is a self-supervised loss. This approach outperformed other state-of-the-art models on standard SR tasks. However, ID-based approaches suffer from the so-called cold-start problem, where it is not possible to generalize to items unseen during training.

[49] builds on the result of SASRec, using the same ID-based approach. The authors propose the BERT4Rec model, which uses a bi-directional attention mechanism rather than a causal one. Hence, they also use a masked language modeling task. The authors show that using this alternative model consistently improves performance across many baselines.

More recent works have looked to alleviate the cold start problem by using language models (LMs) to embed items. For example, [13] proposes a model called ZESRec, which uses a pre-trained BERT [12] model to generate item embeddings. The authors then use a Bayesian approach to model the user sequences of item interactions. The trained model can outperform existing methods and generalize across domains. Another related paper proposes the UniSRec [25] model, which learns item embeddings by applying a parameterized whitening procedure to BERT embeddings. Finally, [21] extends the BERT4Rec model to use LLM (i.e., large models) based item embeddings as input. This straightforward change results in 15-20% improvement on benchmark tasks.

The models discussed thus far use LM embeddings to improve the ability of product recommendation systems to generalize to unseen items and domains. However, these LMs are pre-trained on general natural language rather than the specific data used in each task. [34] proposes formulating the SR problem as a text problem. Their approach, denoted the _Recformer_ , constructs item sentences by flattening the key-value pairs into a string and treating everything as text. This model is then trained using the standard masked language modeling objective, along with an additional contrastive task designed to enhance item representations. The Recformer outperforms all other approaches discussed in this section thus far.

Finally, [38] and [43] propose PinnerFormer and NxtPost, respectively, for delivering content recommendations at Pinterest and Meta. In both cases, the recommended items are complex and can comprise images, text, and tabular features. Both papers utilize an event encoding model to embed pins or posts into a latent space, followed by the training of a causal transformer model to predict

future behavior. Both of these papers are good examples of how these models can be extended to multimodal domains.

_Foundation Models for Tabular Data._ Recent work has explored tabular foundation models, broadly falling into two paradigms [17]. Serialization approaches convert tabular rows into natural language strings and leverage pretrained language models [22]. Model-based approaches like FT-Transformer [20] apply attention mechanisms directly to feature embeddings. However, comprehensive benchmarks show that no single approach consistently outperforms across the broad range of tabular tasks, with gradient boosted trees remaining highly competitive [35].

Our work addresses a distinct problem: learning representations from time-ordered transaction sequences, not static tabular rows. Within the context of ordered transaction sequences, serialization approaches are unsuitable because text-encoding tabular features is token-intensive, leaving insufficient context for long transaction histories; we compare against text-only serialization in Section 4.5. On the other hand, model-based tabular approaches are designed for single-row prediction and do not model dependencies across timeordered sequences. Rather than replacing tabular models, our Joint Fusion architecture combines learned representations of transaction history with static task-specific tabular features, leveraging the strengths of both.

_Sequential Modeling for Financial Data._ Several lines of work apply sequential modeling to financial transaction data. RNN-based approaches include CoLES [3], which trains an RNN encoder with a contrastive objective that pulls subsequences from the same user together and pushes apart subsequences from different users, and NPPR [48], which trains an RNN autoregressively with a nextitem-prediction objective and additionally optimizes the current embedding to predict past behavior. Both report consistent gains over hand-crafted features on banking benchmarks; however, both rely on RNN encoders that struggle with long-range dependencies, and both use only categorical and numerical event attributes, discarding free-text descriptions.

[pp. 2-3]

Transformer-based approaches have followed. TabBERT/TabGPT [37] introduce hierarchical BERT- and GPT-style architectures with fieldlevel transformers over tabular time series. HT-Transformer [29] addresses transformer under-performance on event-sequence classification by introducing _history tokens_ that accumulate context during next-token-prediction pretraining. TransactionGPT [14] presents a 3D-Transformer foundation model trained on billionscale payment transactions, supporting downstream classification and generation tasks. A parallel line of work leverages pretrained LLMs directly. LLM4ES [46] textualizes event sequences and finetunes an LLM via next-token prediction; LATTE [16] aligns raw event embeddings with frozen LLM embeddings via contrastive learning, partly to mitigate the high inference cost of text-based serialization in production.

Our work differs from these in three respects: it operates at production scale (100M+ users, ∼500B tokens) with a deployed system; it proposes Joint Fusion to combine learned sequence representations with task-specific tabular features end-to-end rather

than producing standalone embeddings; and its compact tokenization is purpose-built to fit hundreds of transactions inside a 2048token context window, where text-only and hierarchical-token approaches become prohibitively expensive at scale.

## 3 A Transformer-Based Model for Transactions


[p. 3]

Our goal is to ingest a member’s time-ordered transactions and represent their financial behavior as an embedding. Each transaction is represented by text along with numerical and categorical attributes. As is common in other domains like natural language, images, and audio, we show that it is possible to efficiently summarize member behavior by learning to predict their future transactions.

In this section, we introduce our model formulation based on the transformer [51]. We choose a causal transformer architecture (GPT-like), as opposed to a BERT-like model or an RNN, for several reasons. First, the state-of-the-art industry approaches to sequential recommendation use a transformer backbone [38, 43]. Secondly, transformers offer computational advantages over RNNs [7, 15, 23] during training and inference time, since we are not performing autoregressive generation. We use a causal (rather than masked / BERT-style) objective because next-event prediction aligns naturally with the forward-looking nature of credit risk and matches the dominant approach in production-scale sequential recommendation [38, 43]. Finally, transformers support long range dependencies between inputs. This is especially useful for transaction data because spending money has seasonal variation (e.g. people might spend more money in the holiday season).

In what follows, we outline the structure of this section: Firstly, in section 3.1, we introduce a modified version of the text-is-all-youneed approach of [34] as our interface between transactions and transformers. Following this, in section 3.2 we discuss a supervised finetuning setup to allow tuning embeddings for specific tasks. Finally, in section 3.3 we present an extension of the model, denoted joint fusion, that facilitates end-to-end finetuning with additional tabular features. This is especially important since there are often critical features that are tabular by nature. We denote our joint fusion model _nuFormer_ .

## 3.1 Transaction Transformer Formulation


In this section, we begin by introducing our approach for converting a user, which consists of thousands of transactions, into something that transformer [51] based sequence-to-sequence models can process (i.e., a sequence of embeddings). Formally, we define a _transaction_ as a collection of key-value pairs _𝑡_ = {( _𝑘_ 1 _, 𝑣_ 1) _,_ · · · _,_ ( _𝑘𝑚, 𝑣𝑚_ )}. Then, a member consists of a sequence of transactions:

For the purposes of this paper, we will assume a transaction consists of three attributes: the amount represented as a floating point number, the date represented as a timestamp, and finally, a description represented as a string. Hence, in this case each user transaction is defined as:

Figure 1: The process of converting a transaction into a stringified and then tokenized form.

While this setup is simplistic, we can build representations for the many unique attributes of transactions, such as merchant ID, location, status, merchant category, number of installments, etc.

As discussed, we must first construct an interface between transactions and transformers. One option is to assign IDs to transactions as done in sequential recommendation literature, like SASRec [27]. However, this faces challenges such as the variability of transaction descriptions over time, leading to a large ID space, and the cold start problem for unseen transactions. Alternatively, we could adopt a text-is-all-you-need [34] approach, converting transaction attributes into a JSON string treated as natural language, which helps in generalizing to unseen transactions. The downside of this method is the large number of tokens it generates per transaction, raising concerns about the quadratic scaling of attention operation costs with context length.

For this initial modeling approach, we chose a modified version of text-is-all-you-need. Specifically, we represent numerical and categorical features using special tokens (numerical features are first quantized into bins to make them categorical). Formally, we define a tokenizer as having a vocabulary V size of |V| = _𝑉_ tokens. This vocabulary contains a subset of predefined _special tokens_ V _𝑆_ , with |V _𝑆_ | = _𝑉𝑆_ . The remaining tokens, Vtext = V −V _𝑆_ , are for general text and constructed using an algorithm like byte-pairencoding (BPE) [18, 44]. The special token set is crafted from the specific attributes we want to model, specifically the amount, date and description. Specifically, we have the following feature to token mappings:

- Amount Sign ( _𝜙_ sign : R →Vsign, where |Vsign| = 2): A separate token to represent whether the transaction amount is an inflow or outflow.

[pp. 3-4]

- Amount Bucket ( _𝜙_ amt : R →Vamt, where |Vamt| = 21): The amounts are binned and a separate token is assigned to each bin.

- Date Features: are all represented with their own tokens. – Month ( _𝜙_ month : R →Vmonth, where |Vmonth| = 12): One of the 12 possible months of the year.

- Day ( _𝜙_ day : R →Vday, where |Vday| = 31): One of the possible 31 days.

- Weekday ( _𝜙_ weekday : R →Vweekday, where |Vweekday| = 7): One of the possible 7 week days.

- Text Description ( _𝜙_ BPE : str →( _𝜏_ 1 _,_ · · · ) _,𝜏𝑖_ ∈Vtext: Tokenized as natural language using a standard tokenizer.

Figure 2: The process of constructing a tokenized member.

where ⊕ denotes vector concatenation. An example of (1) is shown in figure 1. Next we can extend this technique to tokenize a member’s account, given by _𝑢𝑖_ = { _𝑡_ 1(_𝑢𝑖_) _,_ · · · _,𝑡𝑁_(_𝑢𝑖_) }, by concatenating the transaction strings with intermediate separator tokens, _𝜏_ sep ∈Vtext:

Figure 2 shows this process.

Finally, we pre-train causal transformers on our tokenized user representation using the standard next token prediction (NTP) task, which involves classifying the next token to occur out of all possible tokens. This choice is due to the success of standard language modeling tasks in the text-is-all-you-need approach [34]. As with transformers trained on natural language, transaction tokens are embedded using a lookup table. Figure 3 shows this structure.

Since the attention operation is invariant to a given token’s position in the sequence, it is common to add an encoding of each token’s position to the input of the model. [30] showed that causal models learn their own form of position representation. The position information induced by training with a causal mask also generalises to longer sequences during inference [30]. Hence, we choose to use no positional embeddings (NoPE) [30]. Finally, we also use FlashAttention [9, 10, 45]. Both NoPE and FlashAttention allow us to train on large context lengths within a single A100 80GB GPU. In practice, we often train on clusters of H100 or H200 GPUs using distributed data parallel or fully sharded training.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Your Spending Needs Attention: Modeling Financial Habits with Transformers" (2025-07-31). https://arxiv.org/abs/2507.23267
