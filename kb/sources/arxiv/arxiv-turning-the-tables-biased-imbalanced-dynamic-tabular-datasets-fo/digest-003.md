---
type: Source Digest
title: 'Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation - part 3 of 3 (pp. 13-19)'
description: 'Verified paraphrased digest, pp. 13-19: Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > References; Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > Checklist; Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > A Appendix'
resource: https://arxiv.org/abs/2211.13358
tags:
- academic_finding
- data_features
- datasets_benchmarks
- fraud_screening_synergies
- global_academic
- preprint
- responsible_ai
status: stable
source_id: arxiv-turning-the-tables-biased-imbalanced-dynamic-tabular-datasets-fo
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-11-24'
legal_status: unknown
part: 3
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2211.13358
  title: 'Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation'
  author: org:arxiv
  last_modified: '2022-11-24T00:00:00Z'
digest_points: 52
---

# Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 13-19) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Checklist

- **descriptive / limitation**: The checklist reports that error bars were not reported, because the study did not vary random seeds. (p. 14)[^original]  
  <sub>anchor: "We do not experiment by varying random seeds in the process."</sub>
- **descriptive / context**: The checklist answers yes to whether limitations were described, stating that they are discussed in Section 5. (p. 14)[^original]  
  <sub>anchor: "Did you describe the limitations of your work? [Yes] This is discussed in Section 5."</sub>

## A.1 Hyperparameter spaces for trained CTGANs

- **descriptive / method**: The tested CTGAN hyperparameters include generator embedding layer dimension of 8 to 256 neurons, generator with 1 to 3 layers of 128 to 512 neurons per layer, critic with 1 to 2 layers of 64 to 256 neurons per layer, and learning rates of the generator and critic. (p. 15)[^original]  
  <sub>anchor: "Generator embedding layer dimension (8 to 256 neurons); Number of layers and neurons per layer in the generator"</sub>
- **descriptive / method**: Default values were used for CTGAN hyperparameters omitted from the search, taken from CTGAN's implementation. (p. 15)[^original]  
  <sub>anchor: "Default values were used for omitted hyperparameters available in CTGAN’s [38] implementation2"</sub>
- **descriptive / method**: Undersampling was included as a CTGAN hyperparameter, with target prevalence set to 5%, 10%, or 20%, and no undersampling was also one possible value. (p. 15)[^original]  
  <sub>anchor: "where the target prevalence was increased to either 5%, 10%, or 20%"</sub>

## A.2 Hyperparameter spaces for trained LightGBM models

- **descriptive / method**: LightGBM tuning also covered boosting algorithm (GBDT or GOSS), maximum buckets for numerical features (100 to 500), and exclusive feature bundling (True or False). (p. 15)[^original]  
  <sub>anchor: "Boosting algorithm (GBDT, GOSS); Minimum instances in leaf (5 to 200)"</sub>
- **descriptive / method**: Default values were used for LightGBM hyperparameters omitted from the search, taken from the official LGBM implementation. (p. 15)[^original]  
  <sub>anchor: "Default values were used for omitted hyperparameters available in LGBM’s [44] official implementation3"</sub>

## A.3 Results of Generative Models

- **descriptive / finding or result**: Of 70 trained generative models, 20 (about 28%) could not produce a candidate sample following the observed month and prevalence distribution and were excluded as they could not learn the data distribution over time to an acceptable extent. (p. 15)[^original]  
  <sub>anchor: "Out of these 70 models, 20 ( _≈_ 28%) were not able to produce a candidate sample"</sub>
- **descriptive / method**: Models were selected by performance when training and testing on generated data, ranked in descending order, because in practice both training and testing would use generated data. (p. 15)[^original]  
  <sub>anchor: "The selection criterion for the generative model was the performance when training and testing on generated data"</sub>

## A.2 Hyperparameter spaces for trained LightGBM models

- **descriptive / method**: LightGBM tuning tested maximum tree depth of 3 to 30 splits. (p. 15)[^original]  
  <sub>anchor: "Maximum tree depth (3 to 30 splits);"</sub>
- **descriptive / method**: LightGBM tuning tested maximum tree leaves between 10 and 100. (p. 15)[^original]  
  <sub>anchor: "Maximum tree leaves (10 to 100);"</sub>
- **descriptive / method**: LightGBM tuning tested minimum instances in a leaf from 5 to 200. (p. 15)[^original]  
  <sub>anchor: "Minimum instances in leaf (5 to 200);"</sub>
- **descriptive / method**: LightGBM tuning tested a maximum number of buckets for numerical features from 100 to 500. (p. 15)[^original]  
  <sub>anchor: "Maximum number of buckets for numerical features (100 to 500);"</sub>
- **descriptive / method**: Exclusive feature bundling was tested with True or False settings. (p. 15)[^original]  
  <sub>anchor: "Exclusive feature bundling (True or False)."</sub>
- **descriptive / method**: Tested LightGBM hyperparameters also include number of estimators, learning rate and boosting algorithm (GBDT or GOSS). (p. 15)[^original]  
  <sub>anchor: "The tested hyperparameters for trained LightGBM models were:"</sub>
- **descriptive / method**: Omitted LightGBM hyperparameters used default values from the LGBM official implementation. (p. 15)[^original]  
  <sub>anchor: "Default values were used for omitted hyperparameters available in LGBM’s [44] official implementation"</sub>

## A.3 Results of Generative Models

- **descriptive / finding or result**: Models that could not learn the distribution of the data over time to an acceptable extent were excluded from the analysis. (p. 15)[^original]  
  <sub>anchor: "These were excluded from the analysis, as they were incapable of learning the distribution of the data"</sub>

## Checklist

- **descriptive / finding or result**: Compute for training the dataset-related models was omitted from the reporting, as it was negligible compared with generative model computation time. (p. 15)[^original]  
  <sub>anchor: "was omitted, as it was negligible when compared to the computation time"</sub>
- **descriptive / context**: The paper states that personally identifiable and offensive content is discussed throughout, and feature engineering and a generative model were used partly for that reason. (p. 15)[^original]  
  <sub>anchor: "This is discussed throughout the paper, and one of the main reasons to do feature engineering"</sub>

## A.3 Results of Generative Models

- **descriptive / method**: Three evaluation columns were defined: Train and Test on generated data; Train on generated train set and test on original test set, corresponding to the tabular GAN literature methodology; and Train on original training set and test on generated test set. (p. 16)[^original]  
  <sub>anchor: "the column Train Set represents training on the generated train set and testing on the original test set"</sub>
- **descriptive / finding or result**: Table 2 gives train generated and test original TPR of 62.7%, 63.1%, 63.6%, 65.3%, 53.3% and 62.5% for the six rows, with mean 30.9% (std 23.3%). (p. 16)[^original]  
  <sub>anchor: "|Mean (Std.)|26.5% (16.3%)|30.9% (23.3%)|16.7% (13.7%)|0.127 (0.061)|0.031 (0.012)|"</sub>
- **descriptive / finding or result**: No generative model reached performance similar to training and testing on original data, which gave a TPR of 75.4%. (p. 16)[^original]  
  <sub>anchor: "No model was able to achieve performance similar to training and testing on the original data, which was of 75.4% TPR."</sub>
- **descriptive / finding or result**: Performance degraded more when only the generated test set was used; the selected model gave the best result with the generated test set, while other models were slightly better with generated training sets. (p. 16)[^original]  
  <sub>anchor: "we notice a larger degradation in performance when using the generated test set only"</sub>
- **descriptive / finding or result**: Some models failed to converge and performed close to a random estimator, with TPR matching FPR in the ROC space. (p. 16)[^original]  
  <sub>anchor: "a part of the models was not capable of converging, with performances close to a random estimator in the ROC space"</sub>
- **descriptive / finding or result**: Statistical similarity metrics were not correlated with ML performance, although the best generated datasets for ML performance tended to also have better statistical similarity. (p. 16)[^original]  
  <sub>anchor: "we observe that these values are not correlated with the ML performance of the datasets"</sub>
- **descriptive / finding or result**: Table 2 lists six rows: an anonymized model and IDs 1 to 5, with train and test on generated data TPR running from 48.4% to 56.0%. (p. 16)[^original]  
  <sub>anchor: "Table 2: Results of the evaluation on trained generative models (Top 5 Models)."</sub>
- **descriptive / finding or result**: The Table 2 mean row gives 26.5% (std 16.3%) for train and test on generated data, and 16.7% (std 13.7%) for train original and test generated. (p. 16)[^original]  
  <sub>anchor: "Table 2: Results of the evaluation on trained generative models (Top 5 Models)."</sub>
- **descriptive / finding or result**: Table 2 KS values range from 0.071 to 0.125 and correlation differences from 0.017 to 0.027; the mean row gives KS 0.127 (std 0.061), which lies above that range as written. (p. 16)[^original]  
  <sub>anchor: "Table 2: Results of the evaluation on trained generative models (Top 5 Models)."</sub>
- **descriptive / finding or result**: Statistical similarity metrics were not correlated with ML performance of the datasets, though the best ML performers tended to have better similarity metrics. (p. 16)[^original]  
  <sub>anchor: "Regarding the statistical similarity metrics, we observe that these values are not correlated with the ML performance of the datasets"</sub>
- **descriptive / finding or result**: A part of the models did not converge, with performance close to a random estimator in the ROC space. (p. 16)[^original]  
  <sub>anchor: "In this regard, a part of the models was not capable of converging, with performances close to a random estimator in the ROC space"</sub>
- **descriptive / finding or result**: No generative model matched the original-data performance of training and testing on original data, which was 75.4% TPR. (p. 16)[^original]  
  <sub>anchor: "training and testing on the original data, which was of 75.4% TPR"</sub>
- **descriptive / finding or result**: Figure 2 shows no clear correlation between ML performance and statistical similarity; better performing models had better than average statistical similarity results. (p. 17)[^original]  
  <sub>anchor: "there is no clear correlation between ML performance and statistical similarity"</sub>
- **descriptive / method**: Figure 3 illustrates the privacy-promoting interventions: feature selection, Laplacian noise addition, categorization of age and income, GAN training on privatized data, and post-generation filtering and transformations. (p. 17)[^original]  
  <sub>anchor: "Illustration of the privacy-promoting interventions conducted."</sub>
- **descriptive / method**: Figure 4 used 100 TPE-optimized LightGBM trials per noise scale, recording TPR at 5% FPR on the original test set; blue line added noise only to training data, orange line to both training and test data. (p. 17)[^original]  
  <sub>anchor: "For each point of noise, 100 trials of TPE optimized LightGBM were run"</sub>

## A.4 Laplacian Noise Mechanism Results

- **descriptive / context**: The original data was already anonymized and most features were aggregations not posing a significant privacy threat to specific applicants, but improving privacy of the resource was still considered important. (p. 17)[^original]  
  <sub>anchor: "The original data had already been anonymized, and most features were aggregations"</sub>
- **descriptive / method**: Privatization pipeline: a subset of the best and most intuitive features was pre-selected to aid GAN convergence; Laplacian noise with varying privacy budgets was added to the original data, including categorical features; continuous personal columns (customer age and income) were categorized; the GAN was trained on noisy data without access to real applicant records. (p. 17)[^original]  
  <sub>anchor: "we pre-selected a subset of the best and most intuitive features to also improve convergence of the GAN"</sub>
- **descriptive / method**: After generation, a filter ensured no generated instance matched an original data point, and some key categorical features were label encoded. (p. 17)[^original]  
  <sub>anchor: "a filter was applied after generation to guarantee that no generated instance matched an original data point"</sub>
- **descriptive / finding or result**: The noise scale 10^-4 was chosen as it gave a TPR of 70% on the noisy test set, used later for GAN training, corresponding to a utility decrease of about 5 percentage points. (p. 17)[^original]  
  <sub>anchor: "we chose the noise scale (10_−_4 ) that yielded a TPR of 70% in the noisy test set"</sub>
- **descriptive / context**: The GAN model is not publicly released, which the authors say further increases the difficulty of attacking applicant privacy. (p. 17)[^original]  
  <sub>anchor: "We do not make the GAN model publicly available, which further increases the difficulty of conducting an attack"</sub>
- **descriptive / limitation**: Steeper decreases in utility would compromise the usefulness of the proposed resource. (p. 17)[^original]  
  <sub>anchor: "Steeper decreases in utility would compromise the usefulness of the proposed resource."</sub>
- **descriptive / finding or result**: The chosen noise scale gave a TPR of 70% in the noisy test set, corresponding to a utility decrease of about 5 percentage points. (p. 17)[^original]  
  <sub>anchor: "corresponding to a decrease in model utility of about 5p.p.."</sub>

## A.5 Correlation of Features

- **descriptive / finding or result**: Spearman correlations between the fraud label and each feature were compared for original and generated base data; signs are preserved for almost all features, with only feat_22 inverting its tendency. (p. 18)[^original]  
  <sub>anchor: "We observe that the signs are preserved for almost all the features (except for `feat_22` )"</sub>
- **descriptive / finding or result**: Correlations are generally slightly weaker for most features in generated data, which the authors suggest may explain the lower ML performance with generated data. (p. 18)[^original]  
  <sub>anchor: "correlations are generally slightly weaker for most features, when observing the generated data"</sub>
- **descriptive / data or feature**: Table 3 reports Spearman correlations with the target for feat_1 to feat_25 in original vs generated data: feat_1 0.090 vs 0.050; feat_2 -0.028 vs -0.037; feat_3 -0.032 vs -0.046; feat_4 0.030 vs 0.049; feat_5 0.042 vs 0.058; feat_6 0.005 vs -0.014; feat_7 -0.022 vs -0.018; feat_8 0.013 vs 0.006; feat_9 -0.001 vs -0.016; feat_10 -0.011 vs -0.011. (p. 18)[^original]  
  <sub>anchor: "|`feat_1`|0.090|0.050|"</sub>
- **descriptive / data or feature**: Table 3 continued: feat_11 -0.013 vs -0.014; feat_12 -0.034 vs -0.032; feat_13 -0.030 vs -0.046; feat_14 0.055 vs 0.060; feat_15 0.036 vs 0.028; feat_16 -0.030 vs -0.035; feat_17 -0.010 vs -0.013; feat_18 -0.032 vs -0.011; feat_19 -0.039 vs -0.035; feat_20 0.049 vs 0.057; feat_21 0.012 vs 0.017; feat_22 -0.003 vs 0.002; feat_23 -0.036 vs -0.050; feat_24 0.089 vs 0.037; feat_25 0.013 vs 0.013. (p. 18)[^original]  
  <sub>anchor: "|Mean Absolute Difference|-|0.011|"</sub>
- **descriptive / finding or result**: The mean absolute difference between original and generated correlations in Table 3 is 0.011. (p. 18)[^original]  
  <sub>anchor: "|Mean Absolute Difference|-|0.011|"</sub>

## Customer Age

- **descriptive / data or feature**: Figure 5 compares the distribution of customer age and fraud prevalence by age in real and generated datasets, with ages truncated to 80 due to low frequencies and higher noise at higher values. (p. 19)[^original]  
  <sub>anchor: "Ages truncated to 80, due to the lower frequencies and higher noise in higher values."</sub>

## A.7 Overlap in Most Important Features

- **descriptive / method**: The feature-selection study of Section 3.2 was replicated with Random Forests, Decision Trees and Logistic Regressions; for each, 100 models were trained with random-search hyperparameters and the 5 best were kept, and their 30 most important features were joined. (p. 19)[^original]  
  <sub>anchor: "For each algorithm, we trained 100 models with hyperparameters selected by a random search algorithm."</sub>
- **descriptive / method**: For Logistic Regressions, feature values were standardized using the distributions in the training set. (p. 19)[^original]  
  <sub>anchor: "In the case of Logistic Regressions, feature values were standardized with the distributions in train."</sub>
- **descriptive / finding or result**: Table 4: Random Forest shared 27 features with LightGBM (Jaccard 0.443) and 21 with the final selection (Jaccard 0.477), with recall at 5% FPR of 69.1% for the best model. (p. 19)[^original]  
  <sub>anchor: "|Random Forest|27|0.443|21|0.477|69.1%|"</sub>
- **descriptive / finding or result**: Table 4: Decision Tree shared 27 features with LightGBM (Jaccard 0.450) and 24 with the final selection (Jaccard 0.480), with recall at 5% FPR of 60.6% for the best model. (p. 19)[^original]  
  <sub>anchor: "|Decision Tree|27|0.450|24|0.480|60.6%|"</sub>
- **descriptive / finding or result**: Table 4: Logistic Regression shared 24 features with LightGBM (Jaccard 0.407) and 15 with the final selection (Jaccard 0.333), with recall at 5% FPR of 62.9% for the best model. (p. 19)[^original]  
  <sub>anchor: "|Log. Regression|24|0.407|15|0.333|62.9%|"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: arXiv, "Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation" (2022-11-24). https://arxiv.org/abs/2211.13358
