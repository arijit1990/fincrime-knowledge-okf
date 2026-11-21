---
type: Source Text
title: Survey on deep learning with class imbalance - part 1 of 9 (pp. 1-5)
description: 'Verbatim extracted text, pp. 1-5: SURVEY PAPER'
resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
status: stable
source_id: academic-publisher-survey-on-deep-learning-with-class-imbalance
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2019-03-19'
legal_status: unknown
part: 1
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 1 of 9, pp. 1-5. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Johnson and Khoshgoftaar ﻿J Big Data (2019) 6:27 https://doi.org/10.1186/s40537-019-0192-5

Open Access

Survey on deep learning with class imbalance

Justin M. Johnson* and Taghi M. Khoshgoftaar

*Correspondence: jjohn273@fau.edu Florida Atlantic University, 777 Glades Road, Boca Raton, FL, USA

Abstract The purpose of this study is to examine existing deep learning techniques for address- ing class imbalanced data. Effective classification with imbalanced data is an impor- tant area of research, as high class imbalance is naturally inherent in many real-world applications, e.g., fraud detection and cancer detection. Moreover, highly imbalanced data poses added difficulty, as most learners will exhibit bias towards the majority class, and in extreme cases, may ignore the minority class altogether. Class imbalance has been studied thoroughly over the last two decades using traditional machine learning models, i.e. non-deep learning. Despite recent advances in deep learning, along with its increasing popularity, very little empirical work in the area of deep learning with class imbalance exists. Having achieved record-breaking performance results in several complex domains, investigating the use of deep neural networks for problems contain- ing high levels of class imbalance is of great interest. Available studies regarding class imbalance and deep learning are surveyed in order to better understand the efficacy of deep learning when applied to class imbalanced data. This survey discusses the imple- mentation details and experimental results for each study, and offers additional insight into their strengths and weaknesses. Several areas of focus include: data complexity, architectures tested, performance interpretation, ease of use, big data application, and generalization to other domains. We have found that research in this area is very limited, that most existing work focuses on computer vision tasks with convolutional neural networks, and that the effects of big data are rarely considered. Several tradi- tional methods for class imbalance, e.g. data sampling and cost-sensitive learning, prove to be applicable in deep learning, while more advanced methods that exploit neural network feature learning abilities show promising results. The survey concludes with a discussion that highlights various gaps in deep learning from class imbalanced data for the purpose of guiding future research.

## SURVEY PAPER


[pp. 1-2]

Keywords: Deep learning, Deep neural networks, Class imbalance, Big data

Introduction Supervised learning methods require labeled training data, and in classification prob- lems each data sample belongs to a known class, or category [1, 2]. In a binary classifi- cation problem with data samples from two groups, class imbalance occurs when one class, the minority group, contains significantly fewer samples than the other class, the majority group. In many problems [3–7], the minority group is the class of inter- est, i.e., the positive class. A well-known class imbalanced machine learning scenario is the medical diagnosis task of detecting disease, where the majority of the patients are

© The Author(s) 2019. This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creat​iveco​mmons​.org/licen​ses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

healthy and detecting disease is of greater interest. In this example, the majority group of healthy patients is referred to as the negative class. Learning from these imbalanced data sets can be very difficult, especially when working with big data [8, 9], and non-standard machine learning methods are often required to achieve desirable results. A thorough understanding of the class imbalance problem and the methods available for addressing it is indispensible, as such skewed data exists in many real-world applications.

When class imbalance exists within training data, learners will typically over-clas- sify the majority group due to its increased prior probability. As a result, the instances belonging to the minority group are misclassified more often than those belonging to the majority group. Additional issues that arise when training neural networks with imbal- anced data will be discussed in the "Deep learning methods for class imbalanced data" section. These negative effects make it very difficult to accomplish the typical objective of accurately predicting the positive class of interest. Furthermore, some evaluation met- rics, such as accuracy, may mislead the analyst with high scores that incorrectly indi- cate good performance. Given a binary data set with a positive class distribution of 1%, a naïve learner that always outputs the negative class label for all inputs will achieve 99% accuracy. Many traditional machine learning techniques, which are summarized in the "Machine learning techniques for class imbalanced data" section, have been devel- oped over the years to combat these adverse effects.

[pp. 2-3]

Methods for handling class imbalance in machine learning can be grouped into three categories: data-level techniques, algorithm-level methods, and hybrid approaches [10]. Data-level techniques attempt to reduce the level of imbalance through various data sampling methods. Algorithm-level methods for handling class imbalance, commonly implemented with a weight or cost schema, include modifying the underlying learner or its output in order to reduce bias towards the majority group. Finally, hybrid systems strategically combine both sampling and algorithmic methods [10].

Over the last 10 years, deep learning methods have grown in popularity as they have improved the state-of-the-art in speech recognition, computer vision, and other domains [11]. Their recent success can be attributed to an increased availability of data, improve- ments in hardware and software [12–16], and various algorithmic breakthroughs that speed up training and improve generalization to new data [17]. Despite these advances, very little statistical work has been done which properly evaluates techniques for han- dling class imbalance using deep learning and their corresponding architectures, i.e. deep neural networks (DNNs). In fact, many researchers agree that the subject of deep learning with class imbalanced data is understudied [18–23]. For this reason, our survey is limited to just 15 deep learning methods for addressing class imbalance.

A comprehensive literature review was performed in order to identify a broad range of deep learning methods for addressing class imbalance. We have documented the spe- cific details of the literature search process so that other scholars may more confidently use this survey in future research, an essential step in any literature review [24]. Can- didate papers were first discovered through the Google Scholar [25] and IEEE Xplore [26] databases. Keyword searches included combinations of query terms such as: “class imbalance”, “class rarity”, “skewed data”, “deep learning”, “neural networks” and “deep neural networks”. Search results were reviewed and filtered, removing those that did

not demonstrate learning from class imbalanced data with neural networks containing two or more hidden layers. No restrictions were placed on the date of publication. The matched search results were then used to perform backward and forward searches, i.e. reviewing the references of matched articles and additional sources that have cited these articles. This was repeated until all relevant papers were identified, to the best of our knowledge.

Additional selection criteria were applied to exclude papers that only tested low lev- els of class imbalance, that did not compare proposed methods to other existing class imbalance methods, or that only used a single data set for evaluation. We discovered that papers meeting these criteria are very limited. Therefore, in order to increase the total number of selected works, these additional requirements were relaxed. The final set of 15 publications includes journal articles, conference papers, and student theses that employ deep learning methods with class imbalanced data.

[pp. 3-4]

We explore a variety of data-level, algorithm-level, and hybrid deep learning meth- ods designed to improve the classification of imbalanced data. Implementation details, experimental results, data set details, network topologies, class imbalance levels, perfor- mance metrics, and any known limitations are included in each surveyed work’s discus- sion. Tables 17 and 18, in the "Discussion of surveyed works" section, summarize all of the surveyed deep learning methods and the details of their corresponding data sets. This survey provides the most current analysis of deep learning methods for addressing class imbalance, summarizing and comparing all related work to date, to the best of our knowledge.

The remainder of this paper is organized as follows. The "Class imbalance background" section provides background information on the class imbalance problem, reviews per- formance metrics that are more sensitive to class imbalanced data, and discusses some of the more popular traditional machine learning (non-deep learning) techniques for handling imbalanced data. The "Deep learning background" section provides neces- sary background information on deep learning. The neural network architectures used throughout the survey are introduced, along with several important milestones and the use of deep learning in solving big data analytics challenges. The "Deep learning meth- ods for class imbalanced data" section surveys 15 published studies that analyze deep learning methods for addressing class imbalance. The "Discussion of surveyed works" section summarizes the surveyed works and offers further insight into their various strengths and weaknesses. The "Conclusion" section concludes the survey and discusses potential areas for future work.

Class imbalance background The task of binary classification, comprised of one positive group and one negative group, is used to discuss class imbalance and various techniques for addressing its challenges in this section. These concepts can be extended to the multi-class problem, because it is possible to convert multi-class problems into a set of two-class problems through class decomposition [27].

The class imbalance problem Skewed data distributions naturally arise in many applications where the positive class occurs with reduced frequency, including data found in disease diagnosis [3], fraud detection [4, 5], computer security [6], and image recognition [7]. Intrinsic imbalance is the result of naturally occurring frequencies of data, e.g. medical diagnoses where the majority of patients are healthy. Extrinsic imbalance, on the other hand, is introduced through external factors, e.g. collection or storage procedures [28].

[pp. 4-5]

It is important to consider the representation of the minority and majority classes when learning from imbalanced data. It was suggested by Krawczyk [10] that good results can be obtained, regardless of class disproportion, if both groups are well rep- resented and come from non-overlapping distributions. Japkowicz [29] examined the effects of class imbalance by creating artificial data sets with various combinations of complexity, training set size, and degrees of imbalance. The results show that sensitivity to imbalance increases as problem complexity increases, and that non-complex, linearly separable problems are unaffected by all levels of class imbalance.

In some domains, there is a genuine lack of data due to the low frequency with which events occur, e.g. detecting oil spills [7]. Learning from extreme class imbalanced data, where the minority class accounts for as few as 0.1% of the training data [10, 30], is of great importance because it is typically these rare occurrences that we are most inter- ested in. Weiss [31] discusses the difficulties of learning from rare events and various machine learning techniques for addressing these challenges.

The total number of minority samples available is of greater interest than the ratio or percentage of the minority. Consider a minority group that is just 1% of a data set con- taining 1 million samples. Regardless of the high level of imbalance, there are still many positive samples (10,000) available to train a model. On the other hand, an imbalanced data set where the minority class displays rarity or under-representation is more likely to compromise the performance of the classifier [30].

(1) ρ = maxi{|Ci|}

mini{|Ci|}

For the purpose of comparing experimental results across all works presented in this survey, a ratio ρ (Eq. 1) [23] will be used to indicate the maximum between-class imbal- ance level. Ci is a set of examples in class i, and maxi{|Ci|} and mini{|Ci|} return the max- imum and minimum class size over all i classes, respectively. For example, if a data set’s largest class has 100 samples and its smallest class has 10 samples, then the data has an imbalance ratio of ρ = 10 . Since the actual number of samples may prove more impor- tant than the ratio, Table 18 also includes the maximum and minimum class sizes for all experiments in this survey.

Performance metrics The confusion matrix in Table 1 summarizes binary classification results. The FP and FN errors correspond to Type I and Type II errors, respectively. All of the performance met- rics listed in this section can be derived from the confusion matrix.

Table 1 Confusion matrix

Actual positive Actual negative

Predicted positive True positive (TP) False positive (FP)

Predicted negative False negative (FN) True negative (TN)

[p. 5]

(2) Accuracy = TP + TN TP + TN + FP + FN

(3) Error Rate = 1 −Accuracy

Accuracy (Eq. 2) and error rate (Eq. 3) are the most frequently used metrics when evalu- ating classification results. When working with class imbalance, however, both are insuf- ficient, as the resulting value is dominated by the majority group, i.e. the negative class. As mentioned previously, when given a data set whose positive group distribution is just 1% of the data set, a naïve classifier can achieve a 99% accuracy score by simply labeling all examples as negative. Of course, such a model would provide no real value. For this reason, we review several popular evaluation metrics commonly used with imbalanced data problems.

(4) Precision = TP TP + FP

(5) Recall = TPR = TP TP + FN

(6) Selectivity = TNR = TN TN + FP

Precision (Eq. 4) measures the percentage of the positively labeled samples that are actu- ally positive. Precision is sensitive to class imbalance because it considers the number of negative samples incorrectly labeled as positive. Precision alone is insufficient, however, because it provides no insight into the number of samples from the positive group that were mislabeled as negative. On the other hand, Recall (Eq. 5), or the True Positive Rate (TPR), measures the percentage of the positive group that was correctly predicted to be positive by the model. Recall is not affected by imbalance because it is only depend- ent on the positive group. Recall does not consider the number of negative samples that are misclassified as positive, which can be problematic in problems containing class imbalanced data with many negative samples. There is a trade-off between precision and recall, and the metric of greater importance varies from problem to problem. Selectivity (Eq. 6), or the True Negative Rate (TNR), measures the percentage of the negative group that was correctly predicted to be negative.

(7) F-Measure =(1 + β2) × Recall × Precision

β2 × Recall + Precision

√

(8) G-Mean =


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
