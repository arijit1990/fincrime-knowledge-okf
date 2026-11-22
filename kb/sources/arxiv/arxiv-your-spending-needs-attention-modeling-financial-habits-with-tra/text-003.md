---
type: Source Text
title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers - part 3 of 4 (pp. 7-10)'
description: 'Verbatim extracted text, pp. 7-10: 4.4 Generalizing the nuFormer Paradigm Across Tasks and Markets; 4.5 Component Ablation Study; 5 Conclusion; and 1 more sections'
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
part: 3
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2507.23267
  title: 'Your Spending Needs Attention: Modeling Financial Habits with Transformers'
  author: org:arxiv
  last_modified: '2025-07-31T00:00:00Z'
---

# Your Spending Needs Attention: Modeling Financial Habits with Transformers

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2025-07-31), part 3 of 4, pp. 7-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 4.4 Generalizing the nuFormer Paradigm Across Tasks and Markets


[pp. 7-8]

These results demonstrate that the nuFormer methodology transfers across diverse prediction tasks, markets, and problem types (classification and regression) without architectural modifications. The Market 2 credit model, pre-trained entirely on transaction data from that market, achieves gains comparable to the primary deployment, suggesting the approach is not specific to a single market’s

|Task|Market|Metric|Gain|
|---|---|---|---|
|Credit default (primary)|Market 1|AUC|+1.25% relative|
|Credit default|Market 2|AUC|+1.81% relative|
|Lending|Market 1|AUC|+2.23% relative|
|Income prediction|Market 1|F1|+7.54% relative|
|Spend prediction|Market 1|R2|+6.85% relative|

Table 2: nuFormer improvements across tasks and markets vs. baseline models, reported as ordinary relative lift.

transaction patterns. Each model presented in Table 2 is currently deployed in production and serving users.

## 4.5 Component Ablation Study


[p. 8]

The preceding experiments demonstrate that Joint Fusion improves credit prediction across markets and tasks. We now analyze which components drive these gains. Due to computational constraints, the following ablations use a 10M row benchmark subset with 1024 context length. Table 3 reports results across four dimensions: modality (what data the model sees), training strategy (how components are optimized), and tokenization (how transactions are represented). For the tokenization comparison, we also vary context length to control for the number of transactions observed, isolating the effect of representation choice from context efficiency.

|Model|Ctx|Txns|Relative Gain|
|---|---|---|---|
|_Modality_||||
|Tabular-only|—|—|-0.96%|
|Transformer-only|1024|81|-2.83%|
|_Training Strategy_||||
|Early Fusion|1024|81|-0.51%|
|Joint Fusion|1024|81|—|
|_Tokenization (matched t_|_xn coun_|_t)_||
|Joint Fusion|352|28|-0.36%|
|Text-only (scratch)|1024|31|-0.37%|
|Joint Fusion|224|18|-0.45%|
|Text-only (scratch)|662|20|-0.54%|
|Text-only (GPT-2 PT)|1024|18|-0.91%|
|Text-only (Qwen 0.6B)|1024|24|-0.41%|
|Text-only (Qwen 4B)|1024|24|-0.43%|

Table 3: Ablation on 10M rows. Relative gain is reported as ordinary relative change in AUC versus the Joint Fusion baseline. Joint Fusion uses special tokens; Text-only (scratch) uses domain BPE; GPT-2 PT/Qwen use pre-trained tokenizers.

_Both modalities contribute._ Tabular only (-0.96%) outperforms Transformer only (-2.83%), indicating that hand-crafted features remain valuable for credit prediction. However, combining both modalities via Early Fusion (-0.51%) exceeds either alone, demonstrating that transaction embeddings and tabular features capture complementary signals. The transformer learns patterns from raw sequences that are not fully captured by aggregated statistics.

_Joint training outperforms early fusion._ Joint Fusion outperforms Early Fusion by 0.51% despite using identical inputs. End-to-end training enables the model to learn interactions between transaction patterns and tabular features that cannot be captured when

representations are simply concatenated. This validates our architectural choice of jointly optimizing the transformer and DCNv2.

_Naive Usage of World Models is not Advantageous._ We evaluated open-source pre-trained models within Joint Fusion: a GPT-2 Medium model pre-trained on Wikipedia, architecturally identical to our from-scratch models, and the Qwen3 0.6B and 4B models [53]. Text-only GPT-2 PT achieves -0.91%, underperforming both Text-only scratch (-0.54%) and Joint Fusion scratch (-0.45%) despite access to pre-trained language understanding. The more modern Qwen3 models perform better, 0.6B and 4B achieve -0.41% and - 0.43%, respectively, but still fall below our from-scratch Joint Fusion baseline while requiring 3.7× and 9× the training time due to larger model and vocabulary sizes.

These results do not preclude the value of world knowledge for transaction modeling, but suggest that naive application of pretrained language models is insufficient. Promising directions for future work include domain-adaptive pre-training on transaction corpora, optimizing the text-only representation of transaction data, developing tokenizers optimized for financial text, optimizing prompts to improve the presentation of transaction data to the model, and hybrid approaches such as semantic IDs [42].

_Controlled comparison by transaction count._ To isolate the effect of tokenization from context efficiency, we compare models at matched transaction counts by varying context length. At approximately 28 to 31 transactions, Joint Fusion (352 context, -0.36%) performs comparably to Text-only scratch (1024 context, -0.37%). At approximately 18 to 20 transactions, Joint Fusion (224 context, -0.45%) slightly outperforms Text-only scratch (662 context, -0.54%). These results suggest that, under equal behavioral context, the two representations achieve similar performance. However, the advantage of compact tokenization is primarily efficiency, enabling 3× more transactions within the same context window.

## 5 Conclusion


In this paper, we introduced a novel approach to leveraging transformer based embedding models for financial data, transforming raw transactions into actionable insights. While these models build on standard data sources used throughout the industry, they facilitate automatically learning informative features that may not be obvious to data scientists. In an empirical evaluation, we saw how using joint fusion to tune our transaction-based transformer models for a credit default prediction task could generate substantial lifts both offline and online, deployed to over 100M+ customers. These models can be leveraged for tasks across markets, improving our ability to understand our customers so we can help them meet their financial needs at the right time. Moreover, we saw a clear advantage to scaling the model size, context length, and training data. In future work, we plan to develop scaling laws for these models and further explore exploiting world knowledge.

## References


[pp. 8-9]

> [1] J. Ao, R. Wang, L. Zhou, et al. 2021. SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing. _arXiv preprint arXiv:2110.07205_ (2021).

> [2] M. Awais, M. Naseer, S. Khan, et al. 2023. Foundational Models Defining a New Era in Vision: A Survey and Outlook. _arXiv preprint arXiv:2307.13721_ (2023).

- [3] D. Babaev, N. Ovsov, I. Kireev, et al. 2022. CoLES: Contrastive Learning for Event Sequences with Self-Supervision. In _Proceedings of the 2022 International Conference on Management of Data_ . 1190–1199.

- [4] V. Borisov, T. Leemann, K. Seßler, et al. 2022. Deep Neural Networks and Tabular Data: A Survey. _IEEE Transactions on Neural Networks and Learning Systems_ (2022).

- [5] T. Brown, B. Mann, N. Ryder, et al. 2020. Language Models are Few-Shot Learners. _Advances in Neural Information Processing Systems_ 33 (2020), 1877–1901.

- [6] T. Chen and C. Guestrin. 2016. XGBoost: A Scalable Tree Boosting System. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ . 785–794.

- [7] Kyunghyun Cho, Bart van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014. Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation. In _Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ . 1724–1734.

- [8] P. Covington, J. Adams, and E. Sargin. 2016. Deep Neural Networks for YouTube Recommendations. In _Proceedings of the 10th ACM Conference on Recommender Systems_ . 191–198.

- [9] T. Dao. 2023. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. _arXiv preprint arXiv:2307.08691_ (2023).

[p. 9]

- [10] T. Dao, D. Fu, S. Ermon, et al. 2022. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. _Advances in Neural Information Processing Systems_ 35 (2022), 16344–16359.

- [11] N. Das, S. Dingliwal, S. Ronanki, et al. 2024. SpeechVerse: A Large-Scale Generalizable Audio Language Model. _arXiv preprint arXiv:2405.08295_ (2024).

- [12] J. Devlin, M.-W. Chang, K. Lee, et al. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ . 4171–4186.

- [13] H. Ding, Y. Ma, A. Deoras, et al. 2021. Zero-Shot Recommender Systems. _arXiv preprint arXiv:2105.08318_ (2021).

- [14] Yingtong Dou, Zhimeng Jiang, Tianyi Zhang, Mingzhi Hu, Zhichao Xu, Shubham Jain, Uday Singh Saini, Xiran Fan, et al. 2025. TransactionGPT. _arXiv preprint arXiv:2511.08939_ (2025).

- [15] Jeffrey L. Elman. 1990. Finding Structure in Time. _Cognitive Science_ 14, 2 (1990), 179–211.

- [16] Egor Fadeev, Dzhambulat Mollaev, Aleksei Shestov, Dima Korolev, Omar Zoloev, Ivan Kireev, Andrey Savchenko, and Maksim Makarenko. 2025. LATTE: Learning Aligned Transactions and Textual Embeddings for Bank Clients. In _Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track (EMNLP ’25)_ .

- [17] X. Fang, W. Xu, F. A. Tan, et al. 2024. Large Language Models (LLMs) on Tabular Data: Prediction, Generation, and Understanding – A Survey. _arXiv preprint arXiv:2402.17944_ (2024).

- [18] P. Gage. 1994. A New Algorithm for Data Compression. _The C Users Journal_ 12, 2 (1994), 23–38.

- [19] Y. Gorishniy, I. Rubachev, and A. Babenko. 2022. On Embeddings for Numerical Features in Tabular Deep Learning. _Advances in Neural Information Processing Systems_ 35 (2022), 24991–25004.

- [20] Y. Gorishniy, I. Rubachev, V. Khrulkov, et al. 2021. Revisiting Deep Learning Models for Tabular Data. _Advances in Neural Information Processing Systems_ 34 (2021), 18932–18943.

- [21] J. Harte, W. Zorgdrager, P. Louridas, et al. 2023. Leveraging Large Language Models for Sequential Recommendation. In _Proceedings of the 17th ACM Conference on Recommender Systems_ . 1096–1102.

- [22] S. Hegselmann, A. Buendia, H. Lang, et al. 2023. TabLLM: Few-shot Classification of Tabular Data with Large Language Models. In _International Conference on Artificial Intelligence and Statistics_ . PMLR, 5549–5581.

- [23] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long Short-Term Memory. _Neural Computation_ 9, 8 (1997), 1735–1780.

- [24] J. Hoffmann, S. Borgeaud, A. Mensch, et al. 2022. Training Compute-Optimal Large Language Models. _Advances in Neural Information Processing Systems_ 35 (2022), 30016–30030.

- [25] Y. Hou, S. Mu, W. X. Zhao, et al. 2022. Towards Universal Sequence Representation Learning for Recommender Systems. In _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 585–593.

- [26] E. J. Hu, Y. Shen, P. Wallis, et al. 2022. LoRA: Low-Rank Adaptation of Large Language Models. In _International Conference on Learning Representations_ .

- [27] W.-C. Kang and J. McAuley. 2018. Self-Attentive Sequential Recommendation. In _2018 IEEE International Conference on Data Mining (ICDM)_ . IEEE, 197–206.

- [28] J. Kaplan, S. McCandlish, T. Henighan, et al. 2020. Scaling Laws for Neural Language Models. _arXiv preprint arXiv:2001.08361_ (2020).

- [29] Ivan Karpukhin and Andrey Savchenko. 2025. HT-Transformer: Event Sequences Classification by Accumulating Prefix Information with History Tokens. _arXiv preprint arXiv:2508.01474_ (2025).

- _Neural Information Processing Systems_ 36 (2023), 24892–24928.

- [31] G. Ke, Q. Meng, T. Finley, et al. 2017. LightGBM: A Highly Efficient Gradient Boosting Decision Tree. _Advances in Neural Information Processing Systems_ 30 (2017).

- [32] A. Krizhevsky, I. Sutskever, and G. E. Hinton. 2012. ImageNet Classification with Deep Convolutional Neural Networks. _Advances in Neural Information Processing Systems_ 25 (2012).

- [33] C. Li, Z. Liu, M. Wu, et al. 2019. Multi-Interest Network with Dynamic Routing for Recommendation at Tmall. In _Proceedings of the 28th ACM International Conference on Information and Knowledge Management_ . 2615–2623.

- [34] J. Li, M. Wang, J. Li, et al. 2023. Text Is All You Need: Learning Language Representations for Sequential Recommendation. In _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 1258–1267.

- [35] D. McElfresh, S. Khandagale, J. Valverde, et al. 2023. When Do Neural Nets Outperform Boosted Trees on Tabular Data? _Advances in Neural Information Processing Systems_ 36 (2023), 76336–76369.

- [36] OpenAI, J. Achiam, S. Adler, et al. 2023. GPT-4 Technical Report. _arXiv preprint arXiv:2303.08774_ (2023).

- [37] Inkit Padhi, Yair Schiff, Igor Melnyk, Mattia Rigotti, Youssef Mroueh, Pierre Dognin, Jerret Ross, Ravi Nair, and Erik Altman. 2021. Tabular Transformers for Modeling Multivariate Time Series. In _ICASSP 2021 – 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ . IEEE, 3565–3569.

- [38] N. Pancha, A. Zhai, J. Leskovec, et al. 2022. PinnerFormer: Sequence Modeling for User Representation at Pinterest. In _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 3702–3712.

- [39] Q. Pi, W. Bian, G. Zhou, et al. 2019. Practice on Long Sequential User Behavior Modeling for Click-Through Rate Prediction. In _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ . 2671– 2679.

- [40] A. Radford, J. W. Kim, C. Hallacy, et al. 2021. Learning Transferable Visual Models from Natural Language Supervision. In _International Conference on Machine Learning_ . PMLR, 8748–8763.

- [41] A. Radford, J. W. Kim, T. Xu, et al. 2023. Robust Speech Recognition via LargeScale Weak Supervision. In _International Conference on Machine Learning_ . PMLR, 28492–28518.

- [42] S. Rajput, N. Mehta, A. Singh, et al. 2023. Recommender Systems with Generative Retrieval. In _Advances in Neural Information Processing Systems_ , Vol. 36.

- [43] K. Rangadurai, Y. Liu, S. Malreddy, et al. 2022. NxtPost: User to Post Recommendations in Facebook Groups. In _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 3792–3800.

- [44] R. Sennrich, B. Haddow, and A. Birch. 2015. Neural Machine Translation of Rare Words with Subword Units. _arXiv preprint arXiv:1508.07909_ (2015).

- [45] J. Shah, G. Bikshandi, Y. Zhang, et al. 2024. FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision. _Advances in Neural Information Processing Systems_ 37 (2024), 68658–68685.

- [46] Aleksei Shestov, Omar Zoloev, Maksim Makarenko, Mikhail Orlov, Egor Fadeev, Ivan Kireev, and Andrey Savchenko. 2025. LLM4ES: Learning User Embeddings from Event Sequences via Large Language Models. In _Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM ’25)_ . 5238–5242.

- [47] K. Simonyan and A. Zisserman. 2014. Very Deep Convolutional Networks for Large-Scale Image Recognition. _arXiv preprint arXiv:1409.1556_ (2014).

- [48] P. Skalski, D. Sutton, S. Burrell, et al. 2023. Towards a Foundation Purchasing Model: Pretrained Generative Autoregression on Transaction Sequences. In _Proceedings of the Fourth ACM International Conference on AI in Finance_ . 141– 149.

- [49] F. Sun, J. Liu, J. Wu, et al. 2019. BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer. In _Proceedings of the 28th ACM International Conference on Information and Knowledge Management_ . 1441–1450.

- [50] H. Touvron, T. Lavril, G. Izacard, et al. 2023. LLaMA: Open and Efficient Foundation Language Models. _arXiv preprint arXiv:2302.13971_ (2023).

- [51] A. Vaswani, N. Shazeer, N. Parmar, et al. 2017. Attention Is All You Need. _Advances in Neural Information Processing Systems_ 30 (2017).

- [52] R. Wang, R. Shivanna, D. Cheng, et al. 2021. DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-Scale Learning to Rank Systems. In _Proceedings of the Web Conference 2021_ . 1785–1797.

- [53] A. Yang, A. Yang, B. Yang, et al. 2025. Qwen3 Technical Report. _arXiv preprint arXiv:2505.09388_ (2025).

- [54] D. Yang, J. Tian, X. Tan, et al. 2023. UniAudio: An Audio Foundation Model Toward Universal Audio Generation. _arXiv preprint arXiv:2310.00704_ (2023).

- [55] G. Zabërgja, A. Kadra, and J. Grabocka. 2024. Tabular Data: Is Attention All You Need? _arXiv preprint arXiv:2402.03970_ (2024).

- [56] D. Zhang, S. Li, X. Zhang, et al. 2023. SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities. _arXiv preprint arXiv:2305.11000_ (2023).

[pp. 9-10]

- [30] A. Kazemnejad, I. Padhi, K. Natesan Ramamurthy, et al. 2023. The Impact of Positional Encoding on Length Generalization in Transformers. _Advances in_

Our users can have multiple types of accounts, cards, and transactions within their event history, which can be broken down into numerous data sources, including credit card, debit card, open finance, wires, transfer activity, and a variety of bill items like credit card payments and fees. Importantly, when using the tokenization procedure described in figure 1, each transaction consumes 14 tokens on average. Hence, given that our LMs have a limited capacity and context window, it is important to explore the power and impact of each individual data source to find the blend and balance for optimal performance.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Your Spending Needs Attention: Modeling Financial Habits with Transformers" (2025-07-31). https://arxiv.org/abs/2507.23267
