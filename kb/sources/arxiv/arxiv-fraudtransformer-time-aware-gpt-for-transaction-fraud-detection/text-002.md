---
type: Source Text
title: 'FraudTransformer: Time-Aware GPT for Transaction Fraud Detection - part 2 of 2 (pp. 6-9)'
description: 'Verbatim extracted text, pp. 6-9: Martin Brown > 7.1 Evaluation Metrics; Martin Brown > 7.6 Results; Martin Brown > 7.7 Discussion; and 4 more sections'
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
part: 2
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2509.23712
  title: 'FraudTransformer: Time-Aware GPT for Transaction Fraud Detection'
  author: org:arxiv
  last_modified: '2025-09-28T00:00:00Z'
---

# FraudTransformer: Time-Aware GPT for Transaction Fraud Detection

[previous part](text-001.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2025-09-28), part 2 of 2, pp. 6-9. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Martin Brown


### 7.1 Evaluation Metrics


[p. 6]

|Model|PRAUC↑|AUROC↑|ΔPRAUC|ΔAUROC|
|---|---|---|---|---|
|_Feature-based baselines_|||||
|Logistic Regression|0_._92491±0_._00000|0_._93784±0_._00000|+0_._00453|+0_._00182|
|XGBoost|0_._93447±0_._00000|0_._95894±0_._00000|+0_._01409|+0_._02292|
|LightGBM|0_._94536±0_._00000|0_._96212±0_._00000|+0_._02498|+0_._02610|
|_Transformer – no positional encoder_|||||
|Vanilla (baseline) (no TE, no PE)|0_._92038±0_._00019|0_._93602±0_._00067|+0_._00000|+0_._00000|
|_RA_(rotary, Abs)|0_._91278±0_._00010|0_._93003±0_._00021|−0_._00760|−0_._00599|
|_RR_(rotary, Rel)|0_._92145±0_._00049|0_._93989±0_._00072|+0_._00107|+0_._00387|
|_SA_(sinusoidal, Abs)|0_._91539±0_._00043|0_._93034±0_._00079|−0_._00499|−0_._00568|
|_SR_(sinusoidal, Rel)|0_._92477±0_._00012|0_._94212±0_._00067|+0_._00439|+0_._00610|
|_Transformer – with positional encode_|_r_||||
|_NTE_(no TE, with PE)|0_._94689±0_._00109|0_._95664±0_._00064|+0_._02651|+0_._02062|
|_RAP_ (rotary, Abs)|0_._94436±0_._00080|0_._95539±0_._00022|+0_._02398|+0_._01937|
|_RRP_ (rotary, Rel)|0_._95610±0_._00118|0_._96497±0_._00041|+0_._03572|+0_._02895|
|_SAP_ (sinusoidal, Abs)|0_._94713±0_._00042|0_._95639±0_._00093|+0_._02675|+0_._02037|
|SRP(sinusoidal, Rel)|0_._95816 ± 0_._00092|0_._96723 ± 0_._00011|+0_._03778|+0_._03121|
|_SRP – without LayerNorm (WOL)_SRP/WOL|0_._95304±0_._00102|0_._96301±0_._00091|+0_._03266|+0_._02699|

held-out test set. We report PRAUC and AUROC. The combinations of time and positional encoders which we investigate are shown in Table 3. The results for this study are provided in next section.

Table 4 contrasts the proposed _GPT with Time encoder and Positional encoder_ model with different positional encoders with the three classical feature-based learners from Section 7.2 and with different reduced GPT variants. All runs used fixed train/validation/test splits and deterministic hyperparameters1 . Consequently, training and evaluation are deterministic, yielding identical results across repeated runs. Features are from a single time snapshot for these comparisons. Accordingly, the standard deviation of the results for the three baselines are zero. The results are shown in Table 4.

### 7.6 Results


Among the non-transformer baselines, LightGBM achieves the strongest performance but is outperformed by the transformerbased models with positional encoding (e.g., GPT-style) and time encoding (relative scheme) on both evaluation metrics.

To assess the contribution of LayerNorm (Step 2 of the FraudTransformer algorithm; Section 6), we perform an ablation in which SRP omits LayerNorm on the time-encoder output. The result (SRP/WOL) in Table 4 shows a slight but significant deterioration.

Regarding the fraud-types, we evaluated the performance of our best model (SRP) against a vanilla GPT for scams, account takeover (ATO), and a category of other types of frauds. The results are reported in Table 5; the SRP model improves on the vanilla model for all three fraud types considered.

### 7.7 Discussion


[pp. 6-7]

Our strongest configuration is sinusoidal time embeddings with learned positional embeddings, event-level Relative, and LayerNorm, appearing as SRP in Table 4. In the following, we provide a more detailed discussion based on our observations in experiments.

PRAUC Values: The PRAUC baseline is the proportion of positive (that is here, fraudulent) entries. Hence with a 43% fraud rate in our evaluation set, the random baseline is 0 _._ 43, which may make the PRAUC values appear to be high. Therefore, instead of reporting absolute PRAUC, we emphasise relative differences between models on the same test set. For this purpose the Δ of PRAUC with respect to baseline, Vanilla GPT, is reported in Table 4.

Time and positional encoding (SRP) vs Vanilla GPT model: The model with a relative time embedding strongly outperforms the baseline on both PRAUC and AUROC. This strongly demonstrates that incorporating time embedding features and positional features into the model improves the performance of the model.

Sinusoidal vs Rotary Time embedding: We observe relatively similar performance between these two schemes when holding all other variables constant. Sinusoidal encoding has a modest advantage over Rotary encoding. This pattern is robust to both choice of performance measure (AUROC vs PRAUC), and relative or absolute time embeddings in this dataset.

Relative vs Absolute Time encoding: As observed in Table 4, the relative time encoding options outperform the absolute time encoding options in both AUROC and PRAUC.

> 1We select no row/feature subsampling: LightGBM bagging_fraction=1.0, feature_fraction=1.0; XGBoost subsample=1.0, colsample_bytree=1.0.

Table 5: Performance comparison of Vanilla vs. SRP across fraud types. Improvements are absolute gains (SRP - Vanilla).

|Fraud Type|Vanill|a GPT|SR|P|Impro|vement|
|---|---|---|---|---|---|---|
||PRAUC|AUROC|PRAUC|AUROC|ΔPRAUC|ΔAUROC|
|Scam|0.8806|0.9406|0.9337|0.9704|+0.0531|+0.0297|
|Other Frauds|0.8477|0.9374|0.8958|0.9627|+0.0481|+0.0254|
|ATO|0.8198|0.9329|0.8737|0.9591|+0.0538|+0.0263|

[p. 7]

Positional Encoding: Adding only a positional encoder yields a modest but consistent lift over the feature-based baselines, confirming that sequential structure carries information not captured by raw features alone.

LayerNorm: Table 4 demonstrates that adding LayerNorm to SRP improves performance and lowers the standard deviation relative to SRP without LayerNorm.

Fraud Sub-types: As shown in Table 5, SRP improves detection across all fraud subtypes, with the largest gains in PRAUC on account takeover (ATO) fraud and in AUROC on scam fraud, relative to the vanilla transformer. Because ATO frauds happen over short temporal windows, the relative-time modeling in the SRP model appears captures these transient patterns more effectively than the vanilla model. This improvement is particularly encouraging as ATO is the type of fraud which is most difficult for the Vanilla model to detect in this data set.

### 8 Conclusion and Future Works


We have introduced _FraudTransformer_ , a GPT-style sequence model that is made explicitly time-aware through sinusoidal or rotary _time encoders_ and an additional learned positional encoder. On a large real-world banking dataset held by a national HSBC Payment Fraud Group, the full variant that combines relative, event-level sinusoidal time embeddings with positional encoder consistently outperforms three strong feature-based baselines: Logistic Regression, XGBoost and LightGBM. The gains hold across both AUROC and PRAUC, confirming that fine-grained temporal structure carries signal beyond what raw features capture.

In practice, FraudTransformer remains computationally lightweight, requiring only a single training epoch for hyperparameter sweeps. Moreover, FraudTransformer delivers stable improvements that translate into fewer missed frauds and lower false-alarm rates.

Some improvements are possible. This work trains the model end-to-end with a binary cross-entropy objective for sequence-level fraud classification. In future work, wesuggest to pre-train the GPT backbone using a next-token prediction objective [22], with the expectation that the token positions will be learnt more accurately. While our current task is binary fraud vs. non-fraud, we could extend the model to multi-class prediction over fraud subtypes in future works. Finally, our approach can be extended to new GPT architectures which support larger context lengths.

### DISCLAIMER


This paper was prepared for information purposes, and is not a product of HSBC or its affiliates. Neither HSBC nor any of its affiliates make any explicit or implied representation or warranty

and none of them accept any liability in connection with this paper but not limited to, the completeness, accuracy, reliability of information contained herein and the potential legal, compliance, tax or accounting effects thereof. Copyright HSBC Group 2025. The content of this manuscript was reviewed by HSBC’s publication clearance team to ensure no disclosure of sensitive data.

- [1] OpenAI GPT2,Transformers v4.38.0 documentation. https://huggingface.co/docs/ transformers/v4.38.0/en/model_doc/gpt2.

### References


- [2] Account Takeover – HSBC UK Business Banking. https://www.business.hsbc. uk/en-gb/account-takeover, August 2025. Accessed: 2025-08-31.

- [3] Common scams. https://www.hsbc.co.uk/help/security-centre/fraud-guide/ common-scams/, 2025. Accessed: 2025-08-31.

- [4] Sercan Ö Arik and Tomas Pfister. Tabnet: Attentive interpretable tabular learning. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 35, pages 6679–6687, 2021.

- [5] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016.

- [6] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. In _Proceedings of the 22nd ACMSIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 785–794, 2016.

- [7] David R Cox. The regression analysis of binary sequences. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 20(2):215–232, 1958.

- [8] Jesse Davis and Mark Goadrich. The relationship between precision-recall and ROC curves. In _Proceedings of the 23rd International Conference on Machine learning_ , pages 233–240, 2006.

- [9] Waleed Hilal, S Andrew Gadsden, and John Yawney. Financial fraud: a review of anomaly detection techniques and recent advances. _Expert Systems With Applications_ , 193:116429, 2022.

- [10] Sihao Hu, Zhen Zhang, Bingqiao Luo, Shengliang Lu, Bingsheng He, and Ling Liu. Bert4eth: A pre-trained transformer for ethereum fraud detection. In _Proceedings of the ACM Web Conference 2023_ , pages 2189–2197, 2023.

- [11] Xin Huang, Ashish Khetan, Milan Cvitkovic, and Zohar Karnin. Tabtransformer: Tabular data modeling using contextual embeddings. _arXiv preprint arXiv:2012.06678_ , 2020.

- [12] Ruohua Jin, Yanyan Wen, Tao Liu, and Cong Shen. Large language models for fraud detection. In _2025 8th International Conference on Artificial Intelligence and Big Data (ICAIBD)_ , pages 441–446. IEEE, 2025.

[pp. 7-8]

- [13] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. Lightgbm: A highly efficient gradient boosting decision tree. _Advances in Neural Information Processing Systems_ , 30, 2017.

- [14] Mingrui Ma, Lansheng Han, and Chunjie Zhou. Research and application of Transformer based anomaly detection model: A literature review. _arXiv preprint arXiv:2402.08975_ , 2024.

- [15] Inkit Padhi, Yair Schiff, Igor Melnyk, Mattia Rigotti, Youssef Mroueh, Pierre Dognin, Jerret Ross, Ravi Nair, and Erik Altman. Tabular transformers for modeling multivariate time series. In _ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 3565–3569. IEEE, 2021.

- [16] Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language understanding by generative pre-training. 2018.

- [17] scikit-learn developers. Logisticregression — scikit-learn documentation. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model. LogisticRegression.html. Accessed: 2025-08-27.

- [18] Alex Stein, Samuel Sharpe, Doron Bergman, Senthil Kumar, C Bayan Bruss, John Dickerson, Tom Goldstein, and Micah Goldblum. A simple baseline for predicting events with auto-regressive tabular transformers. _arXiv preprint arXiv:2410.10648_ , 2024.

- [19] Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. _Neurocomputing_ , 568:127063, 2024.

- [20] Khushboo Taneja, Jyoti Vashishtha, and Saroj Ratnoo. Fraud-BERT: transformer based context aware online recruitment fraud detection. _Discover Computing_ , 28(1):1–16, 2025.

- [21] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. _Advances in Neural Information Processing Systems_ , 30, 2017.

[p. 8]

- [22] Xinlong Wang, Xiaosong Zhang, Zhengxiong Luo, Quan Sun, Yufeng Cui, Jinsheng Wang, Fan Zhang, Yueze Wang, Zhen Li, Qiying Yu, et al. Emu3: Next-token prediction is all you need. _arXiv preprint arXiv:2409.18869_ , 2024.

- [23] Xinze Yang, Chunkai Zhang, Yizhi Sun, Kairui Pang, Luru Jing, Shiyun Wa, and Chunli Lv. Finchain-BERT: A high-accuracy automatic fraud detection model based on nlp methods for financial scenarios. _Information_ , 14(9):499, 2023.

- [24] Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series forecasting? In _Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence_ , pages 11121–11128, 2023.

- [25] Dongyu Zhang, Liang Wang, Xin Dai, Shubham Jain, Junpeng Wang, Yujie Fan, Chin-Chia Michael Yeh, Yan Zheng, Zhongfang Zhuang, and Wei Zhang. Fatatrans: Field and time-aware transformer for sequential tabular data. In _Proceedings of the 32nd ACM International Conference on Information and Knowledge Management_ , pages 3247–3256, 2023.

### Appendix: Hyperparameter Tuning Results


[p. 9]

Table 6 and Table 7 show the hyperparameter tuning results for the RAP, RRP, SAP and SRP schemes. The boldface parameters are selected as hyperparameters and are then also applied in the RA, RR, SA and SR schemes.

Received 1 October 2025

Table 6: Hyperparameter Tuning for the Rotary Scheme, for Relative and Absolute time encoding. The best performing choice is in bold.

|Encoding|_𝑓_base|_𝜆_|PRAUC(at epoch 1)|
|---|---|---|---|
|Rotary (R|elative)|||
|RRP|100000000|0.01|0.95602|
|RRP|10000000|0.01|0.95615|
|RRP|1000000|0.01|0.95498|
|RRP|100000|0.01|0.95209|
|RRP|1000|0.01|0.95070|
|RRP|10|0.01|0.94543|
|RRP|1|0.01|0.94427|
|RRP|100000000|0.1|0.94004|
|RRP|10000000|0.1|0.94304|
|RRP|1000000|0.1|0.94277|
|RRP|10000|0.1|0.93950|
|RRP|1000|0.1|0.92553|
|RRP|10|0.1|0.92564|
|RRP|1|0.1|0.91268|
|Rotary (A|bsolute)|||
|RAP|100000000|0.01|0.94425|
|RAP|10000000|0.01|0.94430|
|RAP|1000000|0.01|0.94235|
|RAP|100000|0.01|0.94201|
|RAP|1000|0.01|0.93931|
|RAP|10|0.01|0.93360|
|RAP|1|0.01|0.92663|
|RAP|100000000|0.1|0.93936|
|RAP|10000000|0.1|0.93931|
|RAP|1000000|0.1|0.93054|
|RAP|100000|0.1|0.93226|
|RAP|1000|0.1|0.92893|
|RAP|10|0.1|0.92001|
|RAP|1|0.1|0.91676|

Table 7: Hyperparameter Tuning for the Sinusoidal Scheme, for Relative and Absolute time encoding. The best performing choice is in bold.

|Encoding|_𝑓_base|_𝜆_|PRAUC(at epoch 1)|
|---|---|---|---|
|Sinusoidal|(Relative)|||
|SRP|100000000|0.01|0.95705|
|SRP|10000000|0.01|0.95820|
|SRP|1000000|0.01|0.95597|
|SRP|100000|0.01|0.95399|
|SRP|1000|0.01|0.95144|
|SRP|10|0.01|0.94041|
|SRP|1|0.01|0.93827|
|SRP|100000000|0.1|0.94114|
|SRP|10000000|0.1|0.94403|
|SRP|1000000|0.1|0.94336|
|SRP|10000|0.1|0.94050|
|SRP|1000|0.1|0.92633|
|SRP|10|0.1|0.92124|
|SRP|1|0.1|0.91368|
|Sinusoidal|(Absolute)|||
|SAP|100000000|0.01|0.94525|
|SAP|10000000|0.01|0.94730|
|SAP|1000000|0.01|0.94335|
|SAP|100000|0.01|0.94371|
|SAP|1000|0.01|0.94330|
|SAP|10|0.01|0.93469|
|SAP|1|0.01|0.92797|
|SAP|100000000|0.1|0.94036|
|SAP|10000000|0.1|0.94131|
|SAP|1000000|0.1|0.93154|
|SAP|100000|0.1|0.93326|
|SAP|1000|0.1|0.93293|
|SAP|10|0.1|0.92111|
|SAP|1|0.1|0.91776|


---

[previous part](text-001.md) | [source overview](overview.md)

[^original]: arXiv, "FraudTransformer: Time-Aware GPT for Transaction Fraud Detection" (2025-09-28). https://arxiv.org/abs/2509.23712
