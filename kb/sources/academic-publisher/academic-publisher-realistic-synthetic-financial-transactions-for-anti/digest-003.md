---
type: Source Digest
title: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models - part 3 of 4 (pp. 13-19)
description: 'Verified paraphrased digest, pp. 13-19: Realistic Synthetic Financial Transactions for Anti-Money Laundering Models > References; Supplementary Material; Supplementary Material > A Realism of Data Generation; and 3 more sections'
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
part: 3
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
digest_points: 46
---

# Realistic Synthetic Financial Transactions for Anti-Money Laundering Models (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 13-19) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## References

- **descriptive / context**: The reference list cites works on cryptocurrency transaction knowledge discovery, GNN-based fraud detection, and the PaySim mobile money simulator, among other sources. (p. 13)[^original]  
  <sub>anchor: "Knowledge Discovery in Cryptocurrency Transactions: A Survey. _IEEE Access_ 9 (2021)"</sub>

## A Realism of Data Generation

- **descriptive / method**: The authors used the AMLworld virtual world, described in Section 3.5, to create several synthetic AML datasets, which are published on Kaggle under a Community Data License Agreement. (p. 16)[^original]  
  <sub>anchor: "As described in Section 3.5, we used _AMLworld_ to create several synthetic AML datasets."</sub>
- **descriptive / data or feature**: The data is divided into two high-level groups, HI and LI; HI datasets have slightly higher illicit ratios (more laundering) than LI datasets. (p. 16)[^original]  
  <sub>anchor: "The HI datasets have slightly higher illicit ratios (more laundering) than LI ."</sub>
- **descriptive / data or feature**: Both HI and LI are further divided into small, medium and large datasets, with the large datasets having 175M to 180M transactions. (p. 16)[^original]  
  <sub>anchor: "with _large_ having 175 _M −_ 180 _M_ transactions."</sub>
- **descriptive / data or feature**: Table 4 gives basic statistics for all six public Kaggle datasets. For Small HI the table lists 10 days spanned, 515K bank accounts, 5M transactions, 3.6K laundering transactions and a laundering rate of 1 per 981 transactions; for Small LI, 10 days, 705K accounts, 7M transactions, 4.0K laundering transactions and 1 per 1942. (p. 16)[^original]  
  <sub>anchor: "Table 4 provides a number of basic statistics about all six Kaggle datasets."</sub>
- **descriptive / data or feature**: Table 4 for Medium HI shows 16 days, 2077K accounts, 32M transactions, 35K laundering transactions and a rate of 1 per 905; Medium LI shows 16 days, 2028K accounts, 31M transactions, 16K laundering transactions and a rate of 1 per 1948. (p. 16)[^original]  
  <sub>anchor: "Table 4: Public Synthetic Data Statistics. HI = Higher Illicit (more laundering). LI = Lower Illicit."</sub>
- **descriptive / data or feature**: Table 4 for Large HI shows 97 days, 2116K accounts, 180M transactions, 223K laundering transactions and a rate of 1 per 807; Large LI shows 97 days, 2064K accounts, 176M transactions, 100K laundering transactions and a rate of 1 per 1750. (p. 16)[^original]  
  <sub>anchor: "# of Transactions|5M|7M|32M|31M|180M|176M|"</sub>
- **descriptive / finding or result**: Figure 7 histograms annualized transactions per account, and its numbers roughly align with U.S. Federal Reserve data cited as a reference point. (p. 16)[^original]  
  <sub>anchor: "Figure 7 also provides a touch point to real data: numbers roughly align with U.S. Federal Reserve data [51]."</sub>
- **descriptive / finding or result**: Table 5 shows the distribution of transaction formats (such as ACH, wire and cheque), and the numbers correspond roughly with Federal Reserve statistics. (p. 16)[^original]  
  <sub>anchor: "Table 5 shows the distribution of transaction formats used in the dataset, such as ACH, wire, and cheque."</sub>
- **descriptive / data or feature**: Table 5 gives transaction counts by format for LI-Large: Cheque 69,720,485; Credit Card 49,923,366; ACH 21,650,558; Cash 18,069,965; Reinvestment 7,258,251; Wire 6,346,402; Bitcoin 3,601,817. (p. 16)[^original]  
  <sub>anchor: "|Cheque|69,720,485|Reinvestment|7,258,251|"</sub>
- **descriptive / data or feature**: Table 8 splits laundering transactions between transactions following one of 8 standard patterns and integration transactions disguised as other activities such as employee payroll or company supplies. (p. 16)[^original]  
  <sub>anchor: "Table 8 breaks down laundering transactions between (a) transactions following one of 8 standard patterns"</sub>
- **descriptive / data or feature**: Table 6 gives a histogram of the number of nodes (accounts) in LI-Large laundering patterns, by node-count bands, for fan-out, fan-in, cycle, random, bipartite, stack, scatter-gather and gather-scatter patterns; the gather-scatter pattern has two counts, nodes from which initial funds come and nodes to which funds ultimately go. (p. 16)[^original]  
  <sub>anchor: "Gather Scatter has 2 counts: (a) # of nodes from which initial funds come;"</sub>
- **descriptive / data or feature**: Table 7 gives pattern counts and transactions in pattern for LI-Large: Fan-out 277 patterns and 2,014 transactions; Fan-in 279 and 2,003; Cycle 298 and 2,326; Bipartite 277 and 1,858; Stack 259 and 3,239; Random 278 and 1,831; Scatter-gather 276 and 4,202; Gather-scatter 284 and 4,010. (p. 17)[^original]  
  <sub>anchor: "|Fan-out|277|2,014|Stack|259|3,239|"</sub>
- **descriptive / finding or result**: Table 8 reports for LI-Large laundering transactions: patterns 19,461 transactions with ratio 9,047; other laundering 81,143 with ratio 2,170; total laundering 100,604 with ratio 1,750. (p. 17)[^original]  
  <sub>anchor: "Laundering Trans. - Patterns 19,461 9,047Laundering Trans. - Other 81,143 2,170"</sub>
- **descriptive / method**: Salary and pension amounts are based on real data from the US Internal Revenue Service, with Figure 8 showing the number of 2018 tax-year returns for each amount of salary and pension income. (p. 17)[^original]  
  <sub>anchor: "we base salary and pension amounts on real data, in this case from the US Internal Revenue Service [54]."</sub>
- **descriptive / finding or result**: About 3.4 times as many returns show salary income as show pension income, and returns can show both. (p. 17)[^original]  
  <sub>anchor: "Figure 8 indicates that there are about 3.4 _×_ as many returns showing salary income as pension income, although returns can show both"</sub>
- **descriptive / method**: The authors assume about 62.5% of people in their models have salaries, matching the U.S. Department of Labor labor force participation value for the adult workforce. (p. 17)[^original]  
  <sub>anchor: "We assume about 62.5% of people in our models havesalaries"</sub>
- **descriptive / finding or result**: Following the IRS ratios, about 18.3% of the population in the datasets has pension income, with around half of those pensioners also receiving a salary. (p. 17)[^original]  
  <sub>anchor: "about 18.3% of the population in our datasets has pension income, with around half of those pensioners also receiving a salary."</sub>
- **descriptive / data or feature**: Figure 7 shows annualized transaction rates across accounts in LI-Large. (p. 17)[^original]  
  <sub>anchor: "Figure 7: Annualized transaction rate across accounts in LI - _Large_ ."</sub>
- **descriptive / data or feature**: Table 9 lists successive halving configurations for multi-bank models (shared across all banks of a dataset) and single-bank models (private, one bank's data), with x0, eta and r0 values per dataset. (p. 17)[^original]  
  <sub>anchor: "Successive halving parameter configurations used for hyperparameter tuning of shared models"</sub>

## B Ethical Use of the Data

- **descriptive / context**: The authors note that money laundering enables criminal activities such as phishing and human trafficking, and detecting laundering can help authorities uncover them. (p. 18)[^original]  
  <sub>anchor: "ranging from phishing attacks to human trafficking."</sub>
- **permissive / recommendation**: The data could be used for pretraining detection models before fine-tuning on real data. (p. 18)[^original]  
  <sub>anchor: "the data could be used for pretraining detection models before fine-tuning on real data."</sub>
- **descriptive / finding or result**: Because the dataset is synthetic, the authors state there is no risk of it containing personally identifiable information or offensive content. (p. 18)[^original]  
  <sub>anchor: "Given that the dataset is synthetic, there is no risk of it containing personally identifiable information or offensive content."</sub>
- **expected / limitation**: Researchers do not need special care with the data's use, but they should bear in mind that performance might not translate one-to-one to real data. (p. 18)[^original]  
  <sub>anchor: "researchers do not need to take special care with its use, but they should bear in mind that performance might not translate one-to-one to real data."</sub>

## C Hyperparameter Tuning of Machine Learning Models

- **descriptive / method**: Gradient boosted tree baselines (LightGBM and XGBoost) are tuned with successive halving: x0 random parameter configurations are sampled, each evaluated on a fraction r0 of the initial training set, and the best x0/eta configurations advance to the next round using eta times r0 of the training set until the fraction reaches 1. (p. 18)[^original]  
  <sub>anchor: "Successive halving starts by randomly sampling _x_ 0 model parameter configurations."</sub>

## B Ethical Use of the Data

- **descriptive / context**: The authors describe ethical use of the data as including benchmarking and improving models for detecting money laundering, and foresee significant positive societal impacts from such uses. (p. 18)[^original]  
  <sub>anchor: "Ethical use of the data includes using it for benchmarking and improving models for the detection of money laundering activity."</sub>
- **descriptive / context**: The authors state that money laundering has a huge cost for society in itself, and that it enables criminal activities ranging from phishing attacks to human trafficking. (p. 18)[^original]  
  <sub>anchor: "Money laundering has a huge cost for society in itself, but more importantly, money laundering enables a whole range of criminal activities"</sub>
- **descriptive / context**: The authors suggest detecting laundering transactions can help authorities uncover such activities and identify the criminals behind them, and that the data could pretrain detection models before fine-tuning on real data. (p. 18)[^original]  
  <sub>anchor: "Detecting money laundering transactions can help authorities uncover such activities and identify the criminals behind them."</sub>
- **descriptive / context**: Because the dataset is synthetic, the authors state there is no risk of it containing personally identifiable information or offensive content. (p. 18)[^original]  
  <sub>anchor: "Given that the dataset is synthetic, there is no risk of it containing personally identifiable information or offensive content."</sub>
- **expected / recommendation**: Researchers should bear in mind that performance on the synthetic data might not translate one-to-one to real data, although they need not take special care in its use. (p. 18)[^original]  
  <sub>anchor: "they should bear in mind that performance might not translate one-to-one to real data."</sub>

## C Hyperparameter Tuning of Machine Learning Models

- **descriptive / method**: Successive halving starts by randomly sampling x0 model parameter configurations, each evaluated on a fraction r0 of the initial training set, keeping the best x0/η configurations for the next round. (p. 18)[^original]  
  <sub>anchor: "Successive halving starts by randomly sampling _x_ 0 model parameter configurations."</sub>
- **descriptive / method**: The GBT (LightGBM and XGBoost) tuning uses successive halving, with different configurations per dataset as shown in Table 9. (p. 18)[^original]  
  <sub>anchor: "We use successive halving [26] for the hyperparameter tuning of the LightGBM and XGBoost models."</sub>
- **descriptive / method**: GNN hyperparameters were first identified by random sampling, then a second random sampling round within a narrower range picked the final set, varying layers, embedding size, learning rate, dropout and minority class weight. (p. 18)[^original]  
  <sub>anchor: "A second round of random sampling was conducted with this narrower range to pick our final set of hyperparameters."</sub>
- **descriptive / method**: GNN hyperparameters were found by random sampling, followed by a second round of random sampling in a narrower range; varied were number of GNN layers, hidden embedding size, learning rate, dropout and minority class weight for the weighted loss. (p. 19)[^original]  
  <sub>anchor: "We varied the following hyperparameters: the number of GNN layers, hidden embedding size, learning rate, dropout, and minority class weight"</sub>
- **descriptive / data or feature**: Table 10 gives LightGBM parameter ranges: small range used for HI-Large and LI-Large LightGBM models, large range for other datasets; e.g. num_leaves (32,256) small and (1,16384) large; num_round (32,512) small and (10,1000) large. (p. 19)[^original]  
  <sub>anchor: "The small parameter range, indicated with _Range-small_ , is only used for hyperparameter tuning of LightGBM models"</sub>
- **descriptive / data or feature**: XGBoost parameter ranges in Table 10 include num_round (10,1000), max_depth (1,15), learning_rate, lambda, scale_pos_weight (1,10) and colsample_bytree and subsample (0.5,1.0). (p. 19)[^original]  
  <sub>anchor: "|colsample_bytreesubsample|(0_._5_,_1_._0)(0_._5_,_1_._0)|"</sub>
- **descriptive / data or feature**: Table 11 gives GNN parameter ranges, optimised on small datasets: for GIN(+EU) hidden embedding size (16,72), learning rate (0.005,0.05), layers (2,4), dropout (0,0.5), minority class weight (6,8); for PNA hidden size (16,64), learning rate (0.0001,0.002), layers (2,4), dropout (0,0.2), minority class weight (6,8). (p. 19)[^original]  
  <sub>anchor: "Table 11: Model parameter ranges used for hyperparameter tuning of GNN models."</sub>
- **descriptive / method**: The Graph Feature Preprocessor processes transactions as temporal edges in a streaming fashion, inserting them into an in-memory dynamic graph and extracting graph features such as scatter-gather patterns, simple cycles and vertex statistics. (p. 19)[^original]  
  <sub>anchor: "The Graph Feature Preprocessor (GFP) processes transactions represented as temporal edges in a streaming fashion."</sub>
- **descriptive / method**: The GFP library is part of Snap ML and the experiments used version 1.14 of Snap ML. (p. 19)[^original]  
  <sub>anchor: "the experiments in this paper were performed using version 1.14 of Snap ML."</sub>

## D Graph Feature Preprocessor Configuration

- **descriptive / method**: Graph-based features are extracted with a batch size of 128 and the GFP generates scatter-gather features, temporal cycles, simple cycles of length up to 10, and vertex statistics. (p. 19)[^original]  
  <sub>anchor: "The graph-based features for our experiments are extracted using the batch size of 128."</sub>
- **descriptive / method**: The GFP uses a time window of six hours for scatter-gather patterns and one day for the other graph-based features. (p. 19)[^original]  
  <sub>anchor: "We set the GFP to use a time window of six hours for scattergather patterns and a time window of one day for the rest of the graph-based features."</sub>
- **descriptive / method**: Vertex statistic features are computed from the Amount and Timestamp fields of the basic transaction features, and this configuration is used for all datasets and experiments using GFP. (p. 19)[^original]  
  <sub>anchor: "The vertex statistic features are computed using the "Amount" and "Timestamp" fields of the basic transaction features"</sub>
- **descriptive / method**: GFP processes transactions in increasing timestamp order so each transaction's graph features use only past data, meaning training-set transactions do not contain features computed from validation or test sets, which prevents data leakage. (p. 19)[^original]  
  <sub>anchor: "This ordering ensures that the graph-based features for each transaction are extracted using the past data."</sub>

## C Hyperparameter Tuning of Machine Learning Models

- **descriptive / method**: To obtain final results, the hyperparameters with the best validation score are used to train four models initialized with different random seeds. (p. 19)[^original]  
  <sub>anchor: "we use the hyperparameters with the best validation score to train four models initialized with different random seeds."</sub>
- **descriptive / data or feature**: Table 10 gives LightGBM small-range and large-range parameter ranges, and XGBoost ranges, for GBT hyperparameter tuning; the small range is used only for LightGBM on HI-Large and LI-Large datasets. (p. 19)[^original]  
  <sub>anchor: "The small parameter range, indicated with _Range-small_ , is only used for hyperparameter tuning of LightGBM models related to HI - _Large_ and LI - _Large_ datasets."</sub>
- **descriptive / data or feature**: Table 10 gives the LightGBM lambda_l2 range as (0.01, 0.5) in the small range and 10^(-2, 2) in the large range, with the XGBoost lambda range as 10^(-2, 2). (p. 19)[^original]  
  <sub>anchor: "lambda_l2|(0_._01_,_0_._5)|10(_−_2_,_2)|lambda|10(_−_2_,_2)"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Academic publisher / repository, "Realistic Synthetic Financial Transactions for Anti-Money Laundering Models" (2023-12-15). https://proceedings.neurips.cc/paper_files/paper/2023/hash/5f38404edff6f3f642d6fa5892479c42-Abstract-Datasets_and_Benchmarks.html
