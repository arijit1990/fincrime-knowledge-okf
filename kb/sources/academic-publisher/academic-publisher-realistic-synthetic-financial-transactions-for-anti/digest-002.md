---
type: Source Digest
title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models - part 2 of 4 (pp. 7-13)
description: 'Verified paraphrased digest, pp. 7-13: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > 4 Performance Evaluation of Machine Learning Models; Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > 5 Future Work and Research Avenues; Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > 6 Conclusions; and 3 more sections'
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
part: 2
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
digest_points: 44
---

# Realistic Synthetic Financial Transactions for Anti-Money Laundering Models (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-13) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4 Performance Evaluation of Machine Learning Models

- **descriptive / context**: The paper gives a preliminary evaluation of whether its synthetic datasets can support effective machine learning models; a deeper treatment is beyond scope and is in the work of Egressy et al. [20]. (p. 7)[^original]  
  <sub>anchor: "A deeper treatment and evaluation is beyond the scope of this datasets and benchmarks submission"</sub>
- **descriptive / finding or result**: The authors argue that measurements on the synthetic data are even better than on real data because ground truth labels are complete, whereas many laundering transactions in real data are never detected. (p. 7)[^original]  
  <sub>anchor: "the ground truth labels are complete, whilst many laundering transactions in real data are never detected"</sub>
- **descriptive / method**: Gradient Boosted Tree (GBT) and message-passing Graph Neural Network (GNN) models are trained on the datasets from Section 3.5, using tabular and graph data representations respectively; tuning is described in Appendix Section C. (p. 7)[^original]  
  <sub>anchor: "We train Gradient Boosted Tree (GBT) and popular message-passing Graph Neural Network (GNN) models on the datasets introduced in Section 3.5"</sub>
- **descriptive / method**: Source and destination account IDs are not used as features, which prevents the models from recognising laundering transactions merely by learning account IDs. (p. 7)[^original]  
  <sub>anchor: "Source and destination account IDs of the transactions are not used as features in our experiments"</sub>
- **descriptive / method**: LightGBM (version 3.1.1) and XGBoost (version 1.7.6) are the GBT baselines. (p. 7)[^original]  
  <sub>anchor: "We use LightGBM [29] and XGBoost [16] as our GBT baselines"</sub>
- **descriptive / data or feature**: Graph Feature Preprocessor (GFP) is used to add features to the GBT models by interpreting the input as a graph and extracting features such as vertex statistics and number of simple cycles, letting GBTs exploit graph structure; configuration is in Appendix Section D. (p. 7)[^original]  
  <sub>anchor: "GFP interprets the input data as a graph and extracts various graph-based features from this graph"</sub>
- **descriptive / method**: GNN baselines are GIN with edge features, PNA, and GIN+EU, the last using edge updates and similar to the architecture of Cardoso et al. [15], used recently in self-supervised money laundering detection. (p. 7)[^original]  
  <sub>anchor: "Since AML is a transaction classification problem, we also include a baseline using edge updates (GIN+EU) [11]"</sub>
- **descriptive / limitation**: GNN results for the Large datasets are not reported because training them requires significantly more compute resources. (p. 7)[^original]  
  <sub>anchor: "Note that the GNN results for the _Large_ datasets are not available because training models for these datasets requires significantly more compute resources"</sub>
- **descriptive / method**: Because accounts are vertices and transactions edges, illicit transaction detection is framed as edge classification; GNNs use a final edge readout layer on edge and endpoint node embeddings. (p. 7)[^original]  
  <sub>anchor: "detection of illicit transactions is an edge classification problem"</sub>
- **descriptive / method**: To reduce complexity, neighbourhood sampling is used in GNN training and testing, sampling 100 one-hop and 100 two-hop neighbours. (p. 7)[^original]  
  <sub>anchor: "We sample 100 one-hop and 100 two-hop neighbors"</sub>
- **descriptive / method**: A 60-20-20 temporal train-validation-test split is used, ordering transactions by timestamp and defining the split by two timestamps t1 and t2: training before t1, validation between t1 and t2, test after t2. (p. 8)[^original]  
  <sub>anchor: "We use a 60-20-20 temporal train-validation-test split, i.e., we split the transaction indices after ordering them by their timestamps"</sub>
- **descriptive / method**: For GNNs, three graph snapshots are built at t1, t2 and t3 = tmax: the train graph holds only training transactions, the validation graph holds training and validation transactions, and the test graph holds all transactions, with only the relevant indices used for evaluation. (p. 8)[^original]  
  <sub>anchor: "The train graph contains only the training transactions (and corresponding nodes)"</sub>
- **descriptive / context**: The authors describe this temporal setup as the most likely scenario faced by banks and financial authorities when classifying unseen batches of transactions. (p. 8)[^original]  
  <sub>anchor: "This is the most likely scenario faced by banks and financial authorities when classifying unseen batches of transactions"</sub>
- **descriptive / method**: Because the datasets are very imbalanced, accuracy is not regarded as reliable; the F1 score for the minority (laundering) class is emphasised. (p. 8)[^original]  
  <sub>anchor: "traditional metrics like accuracy do not provide a reliable measure of model performance"</sub>
- **descriptive / finding or result**: Message-passing GNNs exploiting account connectivity are reported as effective at capturing laundering transactions, with PNA and GIN+EU significantly enhancing GNN performance. (p. 8)[^original]  
  <sub>anchor: "message-passing GNNs that exploit the connectivity between accounts are effective in capturing laundering transactions"</sub>
- **descriptive / finding or result**: GFP combined with LightGBM and XGBoost shows strong performance across datasets; PNA performs near par with GBT baselines without handcrafted features. (p. 8)[^original]  
  <sub>anchor: "An interesting observation is the near-par performance of PNA with GBT baselines, even without relying on handcrafted features"</sub>
- **descriptive / finding or result**: LI datasets are more challenging than HI datasets, attributed to lower illicit ratios and the longer time span of laundering patterns; criminals launder less frequently in LI datasets. (p. 8)[^original]  
  <sub>anchor: "The LI datasets present more significant predictive challenges compared to the HI datasets"</sub>
- **descriptive / method**: The models weight minority-class predictions more heavily in the loss function to address LI difficulty. (p. 8)[^original]  
  <sub>anchor: "our models incorporate the measure of weighting the predictions of the minority class higher in the loss function"</sub>
- **recommended / recommendation**: Other strategies for LI datasets, such as the Pick and Chose method (label-balanced sampler) and GraphSMOTE (synthetic minority samples in embedding space), may be imperative to explore. (p. 8)[^original]  
  <sub>anchor: "exploring other strategies, such as the Pick and Chose method [36], which employs a label-balanced sampler, or GraphSMOTE [66]"</sub>
- **descriptive / finding or result**: Table 2 reports minority-class F1 scores (%) for GIN, GIN+EU, PNA, GFP+LightGBM and GFP+XGBoost across HI and LI Small, Medium and Large datasets; GIN+EU scores 47.73±7.86 on HI-Small and 20.62±2.41 on LI-Small, and GFP+XGBoost scores 65.70±0.26 on HI-Medium and 28.16±0.14 on LI-Medium. (p. 8)[^original]  
  <sub>anchor: "Table 2: Minority class F1 scores (%). HI indicates a higher illicit ratio. LI indicates a lower ratio."</sub>
- **descriptive / finding or result**: Table 2 scores for the Large datasets are NA for the GIN, GIN+EU and PNA rows; GFP+LightGBM scores 48.67±0.24 on HI-Large and 17.09±0.46 on LI-Large, and GFP+XGBoost scores 42.68±12.93 on HI-Large and 24.23±0.12 on LI-Large. (p. 8)[^original]  
  <sub>anchor: "GFP [48, 49] + XGBoost [16]|63_._23_±_0_._17|27_._30_±_0_._33"</sub>
- **descriptive / finding or result**: Table 3 reports minority-class F1 (%) of models trained on HI and evaluated on LI: PNA 0.00±0.00 (LI-Small), 36.60±0.74 (LI-Medium); PNA with fine-tuning for 5 epochs 27.38±1.03 (LI-Small), 36.84±1.64 (LI-Medium); GFP+LightGBM 0.02±0.03 (LI-Small), 32.51±0.24 (LI-Medium), 21.77±0.15 (LI-Large); GFP+XGBoost 0.00±0.00 (LI-Small), 30.31±0.28 (LI-Medium), 17.48±6.90 (LI-Large). (p. 9)[^original]  
  <sub>anchor: "Table 3: Minority class F1 scores (%) of models trained on HI datasets and evaluated on LI datasets."</sub>
- **descriptive / finding or result**: Fine-tuning HI PNA models on the LI dataset improves LI-Small performance, where directly using HI-trained models is ineffective. (p. 9)[^original]  
  <sub>anchor: "by fine-tuning the HI PNA models using the LI dataset"</sub>
- **descriptive / method**: Figure 6 uses GFP and LightGBM on HI-Medium and HI-Large for individual banks, focusing on the top-30 banks by transaction count; LI results are in Appendix Section F. (p. 9)[^original]  
  <sub>anchor: "For brevity, we focus on the top-30 banks that participate in the largest number of transactions in each dataset"</sub>
- **descriptive / method**: Shared graph, shared model setup: banks share all transactions to build one graph, GFP features are shared, and one shared LightGBM model scores each bank's own transactions. (p. 9)[^original]  
  <sub>anchor: "banks share all their transactions with each other to create a shared financial transaction graph"</sub>
- **descriptive / method**: Private graph, private model setup: each bank builds a graph only from its own account holders' transactions, runs GFP on it, and trains its own LightGBM model with no model sharing. (p. 9)[^original]  
  <sub>anchor: "each bank trains its own model on its own data, so there is no model sharing either"</sub>
- **descriptive / method**: Private graph, shared model setup: each bank builds a private graph and GFP features, and a shared LightGBM model is trained after banks share remaining features but not source and destination account IDs. (p. 9)[^original]  
  <sub>anchor: "The banks do not share the source and destination account ids with each other, but share the remaining transaction features"</sub>
- **descriptive / finding or result**: Figure 6 indicates financial institutions generally achieve higher F1 by building shared models, and shared models on shared transaction graphs give even larger improvements. (p. 9)[^original]  
  <sub>anchor: "Figure 6 shows that, in general, financial institutions can achieve higher F1 scores by building shared machine learning models"</sub>
- **permissive / recommendation**: Financial institutions can use differentially-private model and topology sharing techniques to achieve accuracy gains in a privacy-preserving manner; evaluating these techniques is outside the paper's scope. (p. 9)[^original]  
  <sub>anchor: "financial institutions can use differentially-private model and topology sharing techniques"</sub>

## 5 Future Work and Research Avenues

- **descriptive / recommendation**: Future research: historically AML models used single-bank data; synthetic data enables cross-bank analysis, which needs privacy-preserving models and graph topology-sharing techniques. (p. 9)[^original]  
  <sub>anchor: "Historically, AML models have focused on transactions at one bank"</sub>
- **descriptive / recommendation**: There is a need for machine learning and deep learning models that detect complex AML patterns in graph datasets, whether at one bank or across banks. (p. 9)[^original]  
  <sub>anchor: "there is a need for machine learning and deep learning models that can detect complex AML patterns in graph datasets"</sub>

## 4 Performance Evaluation of Machine Learning Models

- **descriptive / finding or result**: Table 3 reports minority-class F1 scores of models trained on HI datasets and evaluated on LI datasets: PNA scores 0.00 on LI-Small and 36.60 on LI-Medium, with no LI-Large result given (NA). (p. 9)[^original]  
  <sub>anchor: "Table 3: Minority class F1 scores (%) of models trained on HI datasets and evaluated on LI datasets."</sub>

## 5 Future Work and Research Avenues

- **descriptive / finding or result**: Synthetic cross-bank data may be used for pre-training deep networks before fine-tuning on real-world data; the authors say Table 3 shows transfer learning is a viable approach. (p. 10)[^original]  
  <sub>anchor: "it may be possible to use our synthetic cross-bank data for pre-training, before fine-tuning with real-world data"</sub>
- **descriptive / recommendation**: New models should run efficiently in time, memory, CPU and GPU use; efficiency techniques for financial transactions differ from those in other domains. (p. 10)[^original]  
  <sub>anchor: "it is important that they run efficiently in terms of time, memory consumption, CPU and GPU use"</sub>
- **descriptive / limitation**: The agent-based data generation can be unstable: minor parameter tweaks can sometimes significantly change aggregate results such as the laundering rate; generative graph models are suggested as a possible avenue. (p. 10)[^original]  
  <sub>anchor: "minor parameter tweaks can sometimes yield significant changes in aggregate results, such as the laundering rate"</sub>

## 6 Conclusions

- **descriptive / context**: AMLworld is described as a detailed, multi-agent virtual world approach to generating synthetic financial data labelled for money laundering; the authors claim the data matches real-world data in key regards. (p. 10)[^original]  
  <sub>anchor: "We have outlined _AMLworld_ , a detailed, multi-agent, virtual world approach to generating synthetic financial data labeled for money laundering"</sub>
- **descriptive / finding or result**: AMLworld data has perfect tagging of laundering activity, which is essentially impossible with real data where tags typically miss much laundering. (p. 10)[^original]  
  <sub>anchor: "AMLworld data also has perfect tagging for laundering activity"</sub>
- **descriptive / finding or result**: Six AMLworld datasets are publicly available on Kaggle; initial results indicate GNNs and GBTs can be effective, with GBTs needing feature engineering while GNNs often are competitive without it. (p. 10)[^original]  
  <sub>anchor: "While GBTs require some feature engineering to capture complex laundering patterns, GNNs often produce competitive results without any feature engineering"</sub>
- **descriptive / recommendation**: Further research is needed to enable collaboration between financial institutions using differentially-private graph topology and model sharing. (p. 10)[^original]  
  <sub>anchor: "Further research is needed to enable collaboration and cooperation between financial institutions"</sub>

## 7 Ethics

- **descriptive / context**: The authors believe releasing the synthetic laundering data helps the fight against AML, given that most laundering currently goes undetected, unlike credit card fraud which is largely detected. (p. 10)[^original]  
  <sub>anchor: "As noted in the Introduction, most laundering activity currently goes undetected"</sub>
- **descriptive / context**: Credit card fraud benefits from a close ground truth via customer feedback; no good ground truth exists for laundering in real data, leading to high error rates, whereas the synthetic data provides such ground truth. (p. 10)[^original]  
  <sub>anchor: "Unfortunately, no good ground truth exists for laundering activities in real financial data"</sub>
- **descriptive / limitation**: The authors see limited potential for misuse of the data; publishing the detection algorithms could let launderers adapt, whereas a static dataset is harder to exploit. (p. 10)[^original]  
  <sub>anchor: "With only a static set of data, it is much harder for launderers to change their behavior to avoid detection"</sub>
- **descriptive / context**: Only the dataset is open-sourced, not the code that generates it, to make it harder for launderers to tweak data and test against detection algorithms. (p. 10)[^original]  
  <sub>anchor: "what we have open-sourced is a set of data _not_ the code to generate the data"</sub>
- **descriptive / context**: Further ethics observations are given in Appendix B. (p. 10)[^original]  
  <sub>anchor: "We offer a few additional observations on ethics in Appendix B"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "Realistic Synthetic Financial Transactions for Anti-Money Laundering Models" (2023-12-15). https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
