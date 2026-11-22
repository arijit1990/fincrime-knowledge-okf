---
type: Source Digest
title: 'SAFE AI metrics: An integrated approach - part 2 of 3 (pp. 5-9)'
description: 'Verified paraphrased digest, pp. 5-9: Machine Learning with Applications > SAFE AI metrics: An integrated approach'
resource: https://doi.org/10.1016/j.mlwa.2025.100821
tags:
- academic_finding
- academic_paper
- explainability
- global_academic
- model_governance
- model_validation
- responsible_ai
status: stable
source_id: academic-publisher-safe-ai-metrics-an-integrated-approach
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2026-02-25'
legal_status: unknown
part: 2
parts_total: 3
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
  resource: https://doi.org/10.1016/j.mlwa.2025.100821
  title: 'SAFE AI metrics: An integrated approach'
  author: org:academic_publisher
  last_modified: '2026-02-25T00:00:00Z'
digest_points: 63
---

# SAFE AI metrics: An integrated approach (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 5-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 2.4. Integration

- **descriptive / definition**: The paper integrates three metrics (RGA, RGE and RGR) into a single measurement by computing a normalized volume under a three-dimensional surface defined by their metric vectors. (p. 5)[^original]  
  <sub>anchor: "We will compute a normalized volume under a threedimensional surface defined by RGA, RGE and RGR metric vectors."</sub>
- **descriptive / definition**: RGA captures how data quality degrades as input data is removed, RGE reflects how model explainability is affected when features are removed, and RGR shows robustness against increasing additional noise. (p. 5)[^original]  
  <sub>anchor: "RGA captures how data quality degrades as input data is removed, RGE reflects how model explainability is affected when features are removed"</sub>
- **descriptive / method**: For every triplet of indices across the n features, a mean aggregation function is applied to the corresponding RGA, RGE and RGR values, and three alternative mean calculations are used, producing an n by n by n tensor approximating the 3D surface. (p. 5)[^original]  
  <sub>anchor: "we apply a mean aggregation function to the corresponding metric values"</sub>
- **descriptive / method**: The compliance assessment yields a single metric for model readiness, and compliance score distributions across models are visualised with histogram plots. (p. 5)[^original]  
  <sub>anchor: "This compliance assessment provides a single metric for evaluating model readiness"</sub>
- **descriptive / method**: The aggregation methods are compared with TOPSIS, a multi-criteria method that minimises distance from the ideal solution and maximises distance from the negative-ideal solution. (p. 5)[^original]  
  <sub>anchor: "a multi-criteria decision analysis method that identifies the best alternative by minimizing distance from the ideal solution"</sub>
- **descriptive / context**: The approach is agnostic with respect to risk preferences: the three dimensions are not weighted and simple averages across all perturbation combinations are taken. (p. 5)[^original]  
  <sub>anchor: "we do not assign weights to the three dimensions but rather take simple averages across all perturbation combinations"</sub>
- **descriptive / context**: Weight assignment is beyond the paper's scope; one example is briefly shown as a possible future research direction. (p. 5)[^original]  
  <sub>anchor: "While it is beyond our scope, we will briefly demonstrate one example of weight assignment"</sub>

## Fig. 5

- **descriptive / finding or result**: For the Random Forest classifier on the California HMDA dataset, the RGE curve indicates that about 60% of the variables can be removed. (p. 5)[^original]  
  <sub>anchor: "The Figure shows that about 60% of the variables can be removed."</sub>

## 3. Data

- **descriptive / context**: HMDA was enacted in 1975 and implemented through Regulation C; it requires various financial institutions to report detailed information on individual mortgage applications. (p. 5)[^original]  
  <sub>anchor: "Enacted in 1975 and implemented through Regulation C, HMDA requires various financial institutions to report detailed information"</sub>
- **descriptive / context**: HMDA data is used to assess whether lenders meet community credit needs, help policy makers develop equitable housing initiatives, and highlight potential patterns of discriminatory lending. (p. 5)[^original]  
  <sub>anchor: "HMDA helps assess whether lenders are meeting community credit needs"</sub>
- **descriptive / context**: The publicly released HMDA data is anonymized to protect borrower privacy. (p. 5)[^original]  
  <sub>anchor: "To ensure the borrower’s privacy, the publicly released data is anonymized."</sub>
- **descriptive / data or feature**: Two HMDA subsets for 2017 loan applications are used: a New York dataset of 44 6902 loans (as written in the excerpt) and a California dataset of 1 714 459 loans. (p. 5)[^original]  
  <sub>anchor: "the New York dataset which consists of 44 6902 loans, and the California dataset containing 1 714 459 loans."</sub>
- **descriptive / data or feature**: After filtering irrelevant and non-informative features and reducing categories, 21 features are used for analysis, as described in Table 1. (p. 5)[^original]  
  <sub>anchor: "we focus on 21 features for further analysis, as described in Table 1."</sub>
- **descriptive / data or feature**: A synthetic dataset of 3000 employee records with eight features (salary, age, education, job tenure, previous experience, minority status and gender) is used for comparison. (p. 5)[^original]  
  <sub>anchor: "which contains 3000 employee records with eight features including salary, age, education, job tenure, previous experience, minority status and gender."</sub>
- **descriptive / definition**: The synthetic binary target follows an XOR pattern on age and salary: positive class when exactly one of young-with-high-salary or older-with-low-salary holds, relative to medians. (p. 5)[^original]  
  <sub>anchor: "where the positive class is assigned when exactly one of two conditions holds"</sub>
- **descriptive / context**: The XOR relationship is non-linear and cannot be captured by a single hyperplane, so linear models such as logistic regression are fundamentally incapable of learning it without feature transformations or interactions. (p. 5)[^original]  
  <sub>anchor: "linear models such as logistic regression are fundamentally incapable of learning this pattern"</sub>
- **descriptive / context**: The synthetic dataset was designed to reveal variations in metrics that might be obscured in datasets where all models perform similarly. (p. 5)[^original]  
  <sub>anchor: "This design makes this dataset suitable for detecting meaningful variations in our metrics"</sub>

## 4. Empirical findings

- **descriptive / method**: The final normalized volume is the average height of the 3D surface across the cyber attack scenario space and is termed the Compliance Score, combining accuracy, explainability and robustness. (p. 5)[^original]  
  <sub>anchor: "This normalized volume represents the average ‘‘height’’ of the 3D surface"</sub>
- **descriptive / method**: Models from logistic, tree-based, ensemble and neural network families are applied as tools to generate predictions for evaluating the scoring methodology. (p. 6)[^original]  
  <sub>anchor: "The selection includes models from different algorithmic families: logistic, tree-based, ensemble and neural network approaches"</sub>

## Table 1

- **descriptive / data or feature**: Table 1 lists the HMDA variables: response variable action_taken (application denied or loan originated); binary variables loan_type, applicant_sex, lien_status and applicant_ethnicity; categorical variables loan_purpose, co-applicant ethnicity, applicant race, co-applicant race and co-applicant sex; continuous variables including loan amount, applicant income, county code, census tract number, MSAMD, population, minority population percentage, HUD median family income, tract-to-MSAMD income percentage, owner-occupied units and 1-to-4 family units. (p. 6)[^original]  
  <sub>anchor: "Summary of HMDA variables."</sub>

## 4.1. AURGA results

- **descriptive / finding or result**: AURGA for New York HMDA: LR 0.3837, RF 0.4121, XGB 0.4133, SEM 0.4137, VEM 0.4138, NN 0.4100, Random 0.3024. (p. 6)[^original]  
  <sub>anchor: "LR|0.3837|0.3709|0.4818|"</sub>
- **descriptive / finding or result**: AURGA for California HMDA: LR 0.3709, RF 0.3963, XGB 0.3995, SEM 0.3997, VEM 0.3993, NN 0.3960, Random 0.3030. (p. 6)[^original]  
  <sub>anchor: "RF|0.4121|0.3963|0.9999|"</sub>
- **descriptive / finding or result**: AURGA for the synthetic employee data: LR 0.4818, RF 0.9999, XGB 0.9999, SEM 0.9999, VEM 0.9999, NN not evaluated, Random 0.4978. (p. 6)[^original]  
  <sub>anchor: "Note that the Neural Network model was not evaluated on the Employee dataset due to insufficient data for reliable training."</sub>
- **descriptive / finding or result**: All models outperform the random baseline on real-world data as expected. (p. 6)[^original]  
  <sub>anchor: "On real-world data all models outperform the random baseline as"</sub>
- **descriptive / finding or result**: On HMDA data, Voting and Stacking ensembles slightly outperform individual models on New York data but are nearly identical to XGBoost on California data, all within a narrow 0.01–0.03 range. (p. 6)[^original]  
  <sub>anchor: "ensemble methods (Voting and Stacking) slightly outperform individual models on New York dataset"</sub>
- **descriptive / finding or result**: On the employee data, Logistic Regression scores 0.4818, worse than random, while other models reach about 0.9999, indicating they capture the XOR pattern. (p. 6)[^original]  
  <sub>anchor: "Logistic Regression achieves only 0.4818 (worse than random performance)"</sub>

## 4.2. AURGR results

- **descriptive / finding or result**: AURGR under Swapping perturbation for New York HMDA: LR 0.4484, RF 0.5181, XGB 0.5372, SEM 0.5279, VEM 0.5289, NN 0.5242, Random 1.0. (p. 7)[^original]  
  <sub>anchor: "LR|0.4484|0.4619|0.3121|"</sub>
- **descriptive / finding or result**: AURGR under Swapping perturbation for California HMDA: LR 0.4619, RF 0.5504, XGB 0.5557, SEM 0.5580, VEM 0.5531, NN 0.5481, Random 1.0. (p. 7)[^original]  
  <sub>anchor: "RF|0.5181|0.5504|0.6778|"</sub>
- **descriptive / finding or result**: AURGR under Swapping perturbation for synthetic employee data: LR 0.3121, RF 0.6778, XGB 0.6665, SEM 0.6779, VEM 0.6780, NN not available, Random 1.0. (p. 7)[^original]  
  <sub>anchor: "XGB|0.5372|0.5557|0.6665|"</sub>
- **descriptive / finding or result**: AURGR under Gaussian noise for New York HMDA: LR 0.9807, RF 0.5070, XGB 0.5082, SEM 0.5096, VEM 0.5078, NN 0.7608, Random 1.0. (p. 7)[^original]  
  <sub>anchor: "LR|0.9807|0.9668|0.9815|"</sub>
- **descriptive / finding or result**: AURGR under Gaussian noise for California HMDA: LR 0.9668, RF 0.5135, XGB 0.5104, SEM 0.5114, VEM 0.5123, NN 0.8152, Random 1.0; for synthetic employee data LR 0.9815, RF 0.5133, XGB 0.5167, SEM 0.5180, VEM 0.5166. (p. 7)[^original]  
  <sub>anchor: "RF|0.5070|0.5135|0.5133|"</sub>
- **descriptive / finding or result**: Logistic Regression is the weakest performer across datasets, with a 0.51 gap to non-linear models on the Employee data and only a 0.03 gap on HMDA datasets. (p. 7)[^original]  
  <sub>anchor: "the performance gap between LR and non-linear models is 0.51 on the Employee data with only 0.03 gap on HMDA datasets."</sub>
- **descriptive / finding or result**: Almost all models score significantly below the Random baseline of 1.0 on AURGR. The random baseline is a benchmark rather than a model, because it does not depend on the input data. (p. 7)[^original]  
  <sub>anchor: "baseline is just a benchmark, and not a model, as it does not depend on the input data."</sub>

## 4.1. AURGA results

- **descriptive / finding or result**: The RGA curves in Figure 6 (California HMDA) indicate that Stacking, Voting and XGB are the best models. (p. 7)[^original]  
  <sub>anchor: "The curves indicates that Stacking, Voting and Gradient Boosting Classifier (XGB) classifiers are the best models."</sub>

## 4.2. AURGR results

- **descriptive / finding or result**: Under Swapping, tree-based methods (RF, XGB, SEM, VEM) consistently outperform LR, reaching AURGR 0.5181–0.6780 versus LR's 0.3121–0.4619, while Neural Network shows intermediate performance (0.5242 and 0.5481). (p. 8)[^original]  
  <sub>anchor: "tree-based methods (RF, XGB, SEM, VEM) consistently outperform Logistic Regression across all datasets"</sub>
- **descriptive / finding or result**: Under Gaussian noise the hierarchy reverses: LR achieves near-perfect robustness (0.9668–0.9815), NN shows strong robustness (0.7608 and 0.8152), and other models remain around 0.5070–0.5180. (p. 8)[^original]  
  <sub>anchor: "Under Gaussian noise, this hierarchy reverses completely"</sub>
- **descriptive / finding or result**: Logistic Regression and Neural Network are robust under Gaussian noise but degrade more under Swapping, the paper's stated explanation being that Gaussian noise preserves expected values while Swapping disrupts learned feature-outcome associations. (p. 8)[^original]  
  <sub>anchor: "Based on our results, Logistic Regression and Neural Network tend to maintain high robustness under Gaussian noise"</sub>
- **descriptive / finding or result**: Tree-based models are disrupted by Gaussian noise, which alters feature distributions that determine split points, though ensemble averaging mitigates this; they are more resilient to Swapping because trees use feature-specific thresholds. (p. 8)[^original]  
  <sub>anchor: "Their hierarchical split-based decision rules can be disrupted by Gaussian noise"</sub>
- **descriptive / limitation**: The paper notes that actual robustness patterns depend on perturbation severity, swapping methodology, and specific model configurations. (p. 8)[^original]  
  <sub>anchor: "the actual robustness patterns depend on perturbation severity, swapping methodology, and specific model configurations."</sub>

## 4.3. AURGE results

- **descriptive / finding or result**: AURGE values are: New York HMDA LR 0.9661, RF 0.9454, XGB 0.9416, SEM 0.9471, VEM 0.9467, NN 0.9414; California HMDA LR 0.9644, RF 0.9547, XGB 0.9350, SEM 0.9406, VEM 0.9486, NN 0.9381; Employee LR 0.9100, RF 0.8943, XGB 0.9042, SEM 0.9045, VEM 0.9002; Random 1.0. (p. 8)[^original]  
  <sub>anchor: "LR|0.9661|0.9644|0.9100|"</sub>
- **descriptive / finding or result**: All models score below the Random baseline on AURGE, which by construction is perfectly explainable because removing variables does not affect its predictions and it is not a model. (p. 8)[^original]  
  <sub>anchor: "All models achieve AURGE scores below the Random baseline (1.0)"</sub>
- **descriptive / finding or result**: Logistic Regression consistently shows the highest explainability across all three datasets, which the paper says aligns with the theoretical expectation for this metric. (p. 8)[^original]  
  <sub>anchor: "Logistic Regression consistently demonstrates the highest explainability across all three datasets"</sub>
- **descriptive / finding or result**: Tree-based and ensemble models show comparable explainability, while XGBoost and Neural Network consistently rank among the least explainable models on all datasets. (p. 8)[^original]  
  <sub>anchor: "XGBoost and Neural Network consistently rank among the least explainable models on all datasets."</sub>
- **descriptive / finding or result**: AURGE curve visualisations confirm LR as the most explainable model and give clearer differentiation between models than previous metric graphs. (p. 8)[^original]  
  <sub>anchor: "The AURGE curve visualizations confirm that across all datasets Logistic Regression is the most explainable model"</sub>
- **descriptive / method**: RGE scores are compared with Shapley values for HMDA datasets using only XGBoost, with Spearman's rank correlation assessing agreement. (p. 8)[^original]  
  <sub>anchor: "we limit this comparison to one representative model, XGBoost."</sub>
- **descriptive / finding or result**: Table 6 (New York HMDA, XGBoost) lists top features: loan_purpose RGE 0.1266 and Shapley 0.5472; applicant_income 0.0852 and 0.3822; loan_amount 0.0756 and 0.2263; applicant_race_1 0.0231 and 0.1067; hud_median_family_income 0.0163 and 0.1334; minority_population 0.0077 and 0.0610; census_tract_number 0.0074 and 0.0551, with Spearman rho 0.853 (p<0.0001). (p. 8)[^original]  
  <sub>anchor: "loan_purpose|0.1266|0.5472|1|1|"</sub>
- **descriptive / finding or result**: Table 7 (California HMDA, XGBoost) lists: loan_purpose RGE 0.1679 and Shapley 0.4331; loan_amount 0.1488 and 0.3631; applicant_income 0.1382 and 0.3571; hud_median_family_income 0.0192 and 0.0862; applicant_race_1 0.0162 and 0.0667; tract_to_msamd_income 0.0150 and 0.0748; lien_status 0.0127 and 0.0182 (RGE rank 7, Shapley rank 18), with Spearman rho 0.878 (p<0.0001). (p. 8)[^original]  
  <sub>anchor: "loan_purpose|0.1679|0.4331|1|1|"</sub>
- **descriptive / finding or result**: RGE and Shapley show strong alignment in feature importance rankings across both HMDA datasets, with Spearman coefficients of 0.853 for New York and 0.878 for California, both p<0.0001. (p. 8)[^original]  
  <sub>anchor: "The Spearman’s rank correlation coefficients of _𝜌_ = 0.853 for New York data"</sub>
- **descriptive / finding or result**: Figure 9 (California HMDA RGE curves) indicates that about 40% of the variables can be removed for all models. (p. 8)[^original]  
  <sub>anchor: "The figure indicates that about 40% of the variables can be removed, for all models."</sub>
- **descriptive / finding or result**: Both methods identify loan_purpose, applicant_income and loan_amount as the three most important variables across datasets, though their relative ordering differs slightly; in California the top four features are ranked identically. (p. 9)[^original]  
  <sub>anchor: "Both methods identify loan_purpose, applicant_income, and loan_amount as the three most important variables across datasets"</sub>
- **descriptive / finding or result**: Divergence appears in middle-to-lower importance ranks; for example lien_status ranks seventh by RGE but eighteenth by Shapley in California. (p. 9)[^original]  
  <sub>anchor: "For example, in California, lien_status ranks seventh by RGE but eighteenth by Shapley values."</sub>
- **descriptive / context**: The paper attributes the differences to methodology: RGE measures performance degradation upon feature removal through perturbation, whereas Shapley values measure marginal contribution based on coalitional game theory. (p. 9)[^original]  
  <sub>anchor: "RGE measures performance degradation upon feature removal through perturbation, while Shapley values calculate marginal contribution"</sub>
- **descriptive / limitation**: The authors state that the RGE-Shapley relationship needs further comparison across additional datasets and model architectures to be fully characterised, and that the preliminary evidence is limited. (p. 9)[^original]  
  <sub>anchor: "further comparative analysis across additional datasets and model architectures would be necessary"</sub>
- **descriptive / finding or result**: Fig. 10 compares RGE and Shapley for the New York HMDA (shown for a single representative visualisation), showing both methods identify the same dominant features but greater spread for lower-importance features. (p. 9)[^original]  
  <sub>anchor: "The visualization shows that while both methods identify the same dominant features"</sub>

## 4.4. Integration

- **descriptive / method**: The integrated compliance metric is computed directly from raw RGA, RGE and RGR values without preprocessing, using arithmetic mean, geometric mean (1/3), root mean square and TOPSIS methods. (p. 9)[^original]  
  <sub>anchor: "We now calculate the integrated compliance metric directly from the original RGA, RGE, and RGR values"</sub>
- **descriptive / finding or result**: Results are presented only for the California dataset due to space; Tables 8 and 9 report all models, and Figs. 12–14 show distributions of the three means under Swapping. (p. 9)[^original]  
  <sub>anchor: "For lack of space, we present the results only for the California dataset."</sub>
- **descriptive / finding or result**: Under Swapping, SEM achieves the highest TOPSIS score (0.40590) and geometric mean (0.53229), indicating balanced performance across the three dimensions. (p. 9)[^original]  
  <sub>anchor: "The Stacked Ensemble Model (SEM) achieves the highest TOPSIS score (0.40590) and Geometric Mean (0.53229)"</sub>
- **descriptive / finding or result**: Under Swapping, Random Forest has the highest arithmetic mean (0.63218) and quadratic mean (0.69337) but a relatively low TOPSIS score (0.40138). (p. 9)[^original]  
  <sub>anchor: "Random Forest demonstrates strong overall performance, achieving the highest Arithmetic Mean (0.63218) and"</sub>
- **descriptive / finding or result**: Under Swapping, Logistic Regression ranks lowest across all aggregation methods, reflecting its vulnerability to feature relationship disruption. (p. 9)[^original]  
  <sub>anchor: "Logistic Regression ranks the lowest across all aggregation methods"</sub>
- **descriptive / finding or result**: Under Swapping, models generally cluster in a close range, suggesting comparable overall compliance. (p. 9)[^original]  
  <sub>anchor: "all models usually cluster in a close range, suggesting comparable overall compliance under Swapping perturbations."</sub>
- **descriptive / finding or result**: Under Gaussian noise, Logistic Regression is the top performer with the highest TOPSIS score and all mean-based metrics, attributed to resilience to additive noise that preserves linear relationships. (p. 9)[^original]  
  <sub>anchor: "Logistic Regression emerges as the top performer with the highest TOPSIS score and all mean-based metrics"</sub>
- **descriptive / finding or result**: Under Gaussian noise, the Neural Network achieves the second-highest compliance, suggesting its learned representations tolerate distributional shifts. (p. 9)[^original]  
  <sub>anchor: "The Neural Network achieves the second-highest compliance"</sub>
- **descriptive / finding or result**: Under Gaussian noise, the other models show degraded performance compared with swapping scenarios, indicating sensitivity to threshold-disrupting noise. (p. 9)[^original]  
  <sub>anchor: "All the other models show a degraded performance compared to swapping scenarios"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "SAFE AI metrics: An integrated approach" (2026-02-25). https://doi.org/10.1016/j.mlwa.2025.100821
