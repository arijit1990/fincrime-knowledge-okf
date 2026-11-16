---
type: Source Text
title: Survey on deep learning with class imbalance - part 7 of 9 (pp. 41-49)
description: 'Verbatim extracted text, pp. 41-49: LMLE-; PANDA 85 93 98 97 89 99 95 78 66 67 77 84 56 72 78 66 85 67 77 87 92; CRL 81 94 92 95 87 98 90 79 66 71 80 88 67 77 83 72 84 79 84 93 95; and 1 more sections'
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
part: 7
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 7 of 9, pp. 41-49. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## LMLE-


[p. 41]

6 6 7 8 8 11 13 14 14 15 16 17 18 19 20 22 23 24 43

1 1 1 1 1 1 2 2 3 3 3 3 3 3 4 4 4 4 4 5 6

77 89 90 92 84 95 87 70 63 67 79 84 61 73 75 66 82 73 76 88 90

78 87 90 91 80 90 89 70 58 63 70 80 61 76 80 61 76 71 70 88 88

78 89 90 91 85 93 89 75 64 65 78 85 61 74 75 67 84 74 76 88 90

69 89 88 89 83 95 89 77 72 72 76 86 66 76 24 73 81 76 76 15 93

Blond

hair Bushy

Attractive Mouth

ance

(1:x)

ance

(1:x)

kNN 83 92 92 91 86 91 88 77 61 61 73 82 55 68 75 63 76 63 69 82 81

kNN 81 68 50 47 66 60 73 82 64 73 64 71 43 84 60 63 72 57 75 72

sam-

pling

sam-

pling

sensi-

tive

old-

Adj

kNN 88 96 99 99 92 99 98 83 68 72 79 92 60 80 87 73 87 73 83 96 98

Table 16 CRL with CelebA Data (Balanced Accuracy) [118]

Imbal-

Imbal-

Triplet-

Triplet-

## PANDA 85 93 98 97 89 99 95 78 66 67 77 84 56 72 78 66 85 67 77 87 92


[pp. 41-42]

ANet 87 96 97 95 89 99 96 81 67 69 76 90 57 78 84 69 83 70 83 93 90

DeepID2 78 89 89 92 84 94 88 73 63 66 77 83 62 73 76 65 79 74 75 88 91

Over-

Down-

Cost-

Thresh-

hair Mustache Bald Mean

skin Gray

chin Pale

hat Double

cheeks Goatee Chubby Sideburns Blurry Wear

## CRL 81 94 92 95 87 98 90 79 66 71 80 88 67 77 83 72 84 79 84 93 95


[p. 42]

necktie Eyeglasses Rosy

hairline Wear

eyes 5 o’clock shadow Receding

necklace Narrow

eyebrows Wear

90 80 71 65 85 82 79 91 90 89 83 90 76 89 84 82 90 90 92 82

85 75 66 61 82 79 80 85 82 85 78 80 68 90 80 78 88 60 79 78

92 84 62 71 82 83 76 95 82 89 81 89 78 95 83 85 91 86 93 79

Blond

hair Bushy

sam-

pling

sam-

pling

sitive 89 79 71 65 84 81 82 91 92 86 82 90 76 90 84 80 90 88 93 82

old-

Adj

kNN 99 82 59 59 82 76 90 98 78 95 79 88 59 99 74 80 91 73 90 84

Table 16 (continued)

Bold-italic and italic scores indicate best and second best class scores, respectively

ANet 90 82 59 57 81 70 79 95 76 86 70 79 56 90 68 77 85 61 73 80

DeepID2 90 78 70 64 85 81 83 92 86 90 81 89 74 90 83 81 90 88 93 81

Over-

Down-

Cost-sen-

Thresh-

## CRL 95 84 73 73 89 88 87 99 90 95 87 95 86 99 89 92 96 93 99 87


[p. 43]

that the minority classes account for at most half the training batch. Both class-level and instance-level hardness metrics are considered when performing hard sample mining. At the class-level, hard positives refer to weak recognitions, the correctly labelled samples with low prediction scores. Alternatively, hard negatives are the obvious mistakes, the samples incorrectly labelled with high prediction scores. At the instance-level, hard posi- tives are defined by correctly labelled images with far distances in feature space distance, while hard negatives are the images incorrectly labelled which are close in feature space.

The CRL loss function (Eq. 17), where α = η imb is linearly proportional to the level of class imbalance, places a batch-wise class balancing constraint on the optimization process. This reduces the learning bias caused by the majority group’s over-represen- tation. The CRL regularization imposes an imbalance-adaptive learning mechanism, applying more weight to the more highly imbalanced labels, while reducing the weight for the less imbalanced labels. Three different loss criteria Lcrl are explored through experimentation, where the Triplet Ranking loss [126] is selected as the default for many of the experiments.

(17) Lbln = αLcrl + (1 −α)Lce, α = ηimb

Experiments are conducted by extending state-of-the-art CNN architectures with the proposed method and performing classification on three benchmark data sets. The Cel- ebA data set contains a max imbalance level of ρ = 49 . The X-Domain [127] data set contains 245,467 retail store clothing images that are annotated with 9 multi-class attrib- ute labels, 165,467 of which are set aside for training. The X-Domain contains extreme class imbalance ratios of ρ > 4000 . Several imbalanced data sets are generated from the CIFAR-100 set, with imbalance ratios up to ρ = 20 , to demonstrate how CRL handles increasing levels of imbalance.

Table 16 contains the CelebA facial attribute recognition results. All class imbal- ance methods presented were implemented on top of the 5-layer CNN, DeepID2, [128]. Referring to the bottom half of the data attributes, with imbalance ratios ρ ≥6 , under-sampling almost always performs worse than over-sampling, cost-sensitive learning, and threshold moving. According to the mean sensitivity scores, over-sam- pling and cost-sensitive learning perform the same, outperforming thresholding and under-sampling by 3% and 4%, respectively.

[pp. 43-44]

When compared to the best non-imbalanced learning method (DeepID2) and the best imbalanced learning method (LMLE), the proposed CRL method improves the mean sensitivity by 6% and 3%, respectively. By analyzing the attribute-level scores, we can see that LMLE outperforms CRL in many cases where class imbalance lev- els are low, e.g. outperforming CRL on the attractive attribute by 7%. Dong et al. acknowledge that LMLE appears to handle low-level imbalance better than CRL. For many of the high-imbalance attributes, the non-imbalance method DeepID2 outper- forms the LMLE method. It is when class imbalance is highest that the proposed CRL method performs its best and achieves its most significant performance gains over alternative methods.

In another experiment with the X-Domain data set, CRL outperforms LMLE on all categories, achieving a mean sensitivity performance gain over LMLE of almost 5%. Cost-sensitive learning, thresholding, and ROS all score roughly 6% below CRL,

while RUS again performs very poorly. When experimenting with balanced distribu- tions from the CIFAR-100 data set, the CRL method is applied to three state-of-the- art CNN models: CifarNet [129], ResNet32 [98], and DenseNet [130]. For each model, the CRL method consistently improves upon the baseline, increasing mean sensitivity by 3.6%, 1.2%, and 0.8%, respectively. Additional cost analysis by Dong et al. shows that CRL is significantly faster than LMLE, taking just 27.2 h to train versus LMLE’s 166.6 h on the given test case. The advantages of CRL over alternative methods on large-scale class imbalanced image data were demonstrated through comprehensive experiments. It was shown to efficiently outperform many popular class imbalanced methods, including ROS, RUS, thresholding, cost-sensitive learning, and LMLE. It was also shown to train sig- nificantly faster than the LMLE method. The authors were clear to distinguish this method as effective in large-scale image data containing high levels of imbalance, and results on facial attribute detection showed that LMLE performed better for many facial attributes with lower levels of imbalance. This suggests that the CRL method may not be a good fit for class imbalance problems containing low levels of class imbalance. Despite this initial observation, CRL should be evaluated on a wide range of data sets with varying levels of complexity to better understand when it should be used. Exploring the CRL method’s ability to learn from non-image data is also of interest.

[pp. 44-45]

Summary of hybrid methods This section analyzed three hybrid deep learning methods for addressing class imbal- ance. The LMLE method proposed by Huang et al. outperformed several state-of-the-art models on the CelebA and BSDS500 image data sets. Ando and Huang introduced the DOS method, which learns an embedding layer that produces more discriminative fea- tures, and then supplements the minority group by over-sampling in deep feature space. DOS was shown to outperform LMLE and baseline CNNs on multiple class imbalanced image data sets. Lastly, Dong et al.’s CRL loss function was shown to outperform four state-of-the-art models, ROS, RUS, cost-sensitive learning, output thresholding, and LMLE on the CelebA data set.

The results provided by Dong et al. are most informative, as they compare their CRL method to LMLE and several other data-level and algorithm-level deep learning methods for addressing class imbalance. Not only did they show that the CRL method outperforms alternative methods as class imbalance levels increase, but they also illus- trated the effectiveness of RUS, ROS, thresholding, and cost-sensitive learning. From their results on the CelebA data set, we observe that ROS and cost-sensitive learning outperform RUS and threshold moving on average. These results are consistent with those from the "Data-level methods" section, suggesting that ROS is generally a good choice in addressing class imbalance with DNNs. Dong et al. also confirmed our original observation, that LMLE is rather complex and resource intensive, by showing that CRL is capable of training 6× faster than LMLE. Comparing DOS and CRL directly will prove useful, as both methods were shown to outperform the LMLE method.

In general, hybrid methods for learning from class imbalanced data will be more complex, and more difficult to implement than algorithm-level methods and data-level

Table 17 Summary of deep learning class imbalance methods

Method Network type Method type Description

ROS [23, 79] CNN Data ROS of minority classes until class balance is

achieved

RUS [23] CNN Data RUS of majority classes until class balance is

achieved

Two-phase learning [20, 23] CNN Data Pre-training with RUS or ROS, then fine-tuning

with all data

Dynamic sampling [21] CNN Data Sampling rates adjust throughout training based

on previous iteration’s class-wise F1-scores

MFE and MSFE loss [18] MLP Algorithm New loss functions allow positive and negative

classes to contribute to loss equally

Focal loss [88, 103] CNN Algorithm New loss function down-weights easy-to-classify

samples, reducing their impact on total loss

CSDNN [89] MLP Algorithm CE loss function modified to incorporate a pre-

defined cost matrix

CoSen CNN [19] CNN Algorithm Cost matrix is learned through backpropagation

and incorporated into output layer

[pp. 45-46]

CSDBN-DE [90] DBN Algorithm Cost matrix is learned through evolutionary algo-

rithm and incorporated into output layer

Threshold moving [23] CNN Algorithm Decision threshold is adjusted by dividing output

probabilities by prior class probabilities

Category centers [91] CNN Algorithm Class centroids are calculated in deep feature

space and K-NN method discriminates

Very-deep NNs [92] CNN Algorithm CNN network depths of up to 50 layers are used to

examine convergence rates

LMLE [22] CNN Hybrid Triple-header hinge loss and quintuplet sampling

generate more discriminative features

DOS [117] CNN Hybrid Minority class over-sampled in deep feature space

using K-NN and micro-cluster loss

CRL loss [118] CNN Hybrid Class Rectification loss and hard sample mining

produce more discriminative features

methods. This is expected, since both algorithm-level and data-level methods are being combined for the purpose of improving classification performance. As learners become more complex, their flexibility and ease of use will decrease, which may make them more difficult to adapt to new problems.

Class-wise performance scores on the CelebA data set in Table 16 show that differ- ent methods perform better when subjected to different levels of class imbalance. This observation supports our demand for future research that evaluates multiple deep learn- ing methods across a variety of class imbalance levels and problem complexities. We expect to see similar trade-offs between models when they are evaluated across a variety of data types and DNN architectures. Filling these gaps in current research will help to shape future deep learning applications that involve class imbalance, class rarity, and big data.

Discussion of surveyed works To provide a high-level summary and better compare the current deep learning meth- ods for class imbalance, the surveyed works and their data sets have been summarized in Tables 17 and 18. The methods presented by each group have been categorized in

Table 18 Summary of data sets and class imbalance levels

Paper Data sets Data type Class count Data set size Min class size Max class size ρ (Eq. 1)

[79] CIFAR-10 Image 10 60,000 2340 3900 2.3

[20] WHOI-Plankton Image 103 3,400,000 < 3500 2,300,000 657

[21] Public cameras Image 19 10,000 14 6986 499

[18] CIFAR-100 (1) Image 2 6000 150 3000 20

CIFAR-100 (2) Image 2 1200 30 600 20

CIFAR-100 (3) Image 2 1200 30 600 20

20 News Group (1) Text 2 1200 30 600 20

20 News Group (2) Text 2 1200 30 600 20

[p. 46]

[88] COCO Image 2 115,000 10 100,000 10,000

[103] Building changes Image 6 203,358 222 200,000 900

[89] GHW Structured 2 2565 406 2159 5.3

ORP Structured 2 700 124 576 4.6

[19] MNIST Image 10 70,000 600 6000 10

CIFAR-100 Image 100 60,000 60 600 10

CALTECH-101 Image 102 9144 15 30 2

MIT-67 Image 67 6700 10 100 10

DIL Image 10 1300 24 331 13

MLC Image 9 400,000 2600 196,900 76

[90] KEEL Structured 2 3339 26 3313 128

[91] CIFAR-10 Image 10 60,000 250 5000 20

CIFAR-100 Image 100 60,000 25 500 20

[22] CelebA Image 2 160,000 3200 156,800 49

[117] MNIST Image 10 60,000 50 5000 100

MNIST-back-rot Image 10 62,000 12 1200 100

CIFAR-10 Image 10 60,000 5000 5000 1

SVHN Image 10 99,000 73 7300 100

STL-10 Image 10 13,000 500 500 1

[118] CelebA Image 2 160,000 3200 156,800 49

[92] EmotioNet Image 2 450,000 45 449,955 10,000

[23] MNIST Image 10 60,000 1 5000 5000

CIFAR-10 Image 10 60,000 100 5000 50

ImageNet Image 1000 1,050,000 10 1000 100

Images from CelebA and EmotioNet are treated as a set of binary classification problems, because they are each annotated with 40 and 11 binary attributes, respectively. The COCO data class imbalance arises from the extreme imbalance between background and foreground concepts

Table 17 as one of three types: data, algorithm, or hybrid. All of the general methods for handling class imbalance in traditional machine learning have been extended to deep learning, including: random sampling, informed sampling, cost-sensitive learning, thresholding, and hybrid methods.

[pp. 46-47]

Data-level techniques for addressing class imbalance in deep learning include ROS [23, 79], RUS [23], two-phase learning with sampling [20, 23], and performance-based dynamic sampling [21]. The ROS experiments reported that over-sampling to the level of class balance works best on imbalanced image data. The two-phase learning method uses RUS or ROS to pre-train a DNN with class balanced data sets, then fine-tunes the network using all data. The dynamic sampling method uses class-wise F1-scores to determine sampling rates, allowing the model to sample difficult classes at a higher rate.

Algorithm-level methods were explored by nine studies, and can be further broken down into new loss functions, cost-sensitive methods, output thresholding, and a deep feature 1-NN rule. MFE and MSFE loss functions [18] are modifications of the MSE loss that allow the positive and negative class to equally contribute to the loss. The focal loss function [88, 103] improves classification by down-weighting easy-to-classify samples, preventing easily-classified negative samples from dominating the loss. Wang et al. modified the CE loss slightly to incorporate pre-defined class costs into the learning pro- cess, creating an optimization process that minimizes total cost. The final two cost-sen- sitive methods evaluated are unique in the sense that they iteratively improve the cost matrix throughout training, instead of requiring pre-defined costs. The CoSen CNN [19] uses an additional loss function to learn the cost parameters through backpropagation, while the CSDBN-DE [90] utilizes an evolutionary algorithm to produce increasingly better cost values. Buda et al. used class prior probabilities to adjust deep CNN output thresholds and reduce bias towards the majority group. The category centers method [91] uses CNN-generated features to calculate class centers in feature space, then uses the 1-NN rule to classify new data by its nearest class centroid. Very-deep CNNs (> 10 layers) were explored by Ding et al. to determine if deeper networks would converge faster than shallow networks when trained on imbalanced data.

Three hybrid methods that combine data-level and algorithm-level changes to address the class imbalance problem were compared to baselines and alternative methods. LMLE [22] combines quintuplet sampling with the triple-header hinge loss to learn more discriminative features. The CRL loss function combined with hard sample mining [118] was shown to improve representation learning and outperform LMLE. Ando and Huang were the first to explore over-sampling in deep feature space, showing that DOS is able to outperform LMLE on imbalanced image data.

[pp. 47-48]

Two-phase learning [20] and dynamic sampling [21] both outperformed transfer learning and augmentation methods in classifying imbalanced image data. Buda et al. presented conflicting results, however, that suggested that plain ROS performs better than both two-phase learning and RUS. Dong et al. showed that ROS and cost-sensi- tive learning methods perform equivalently on the CelebA dataset, both outperforming RUS and thresholding methods. Experiments by Khan et al., evaluated over six data sets, showed that a cost-sensitive CNN can outperform data sampling methods with neural networks and cost-sensitive SVM and RF learners. Wang et al. deployed a state-of-the- art hospital readmission predictor built using a cost-sensitive DNN that outperformed existing models. A class balanced version of the MSE loss, MFE and MSFE [18], showed improvements in classifying imbalanced image and text data. In [117], over-sampling in the deep feature space is used to perform classification on five data sets, showing that the DOS framework can outperform LMLE and TL-RS-CSL. The focal loss [88] function was shown to outscore leading one-stage and two-stage detectors on the COCO data set. The CRL loss [118] outperformed LMLE, data sampling, cost-sensitive learning, and thresholding on the CelebA facial attribute detection task.

Multiple authors [19, 23, 79] suggested the use of deep learning with ROS to address class imbalance, showing that ROS outperforms RUS in almost all cases. Buda et al. and Hensman and Masko both suggest applying ROS until class imbalance is elimi- nated in the training set, but experiments did not consider big data scenarios. We

believe that applying ROS to this level will not hold when subjected to big data or class rarity. Duplicating such large volumes of data may cause over-fitting and is very computationally expensive. In a contrastive example, Bauder et al. [131] found RUS to be more effective than ROS when using traditional machine learning algorithms to detect fraud in big data with class rarity. Future work should consider these big data scenarios, and should experiment with RUS methods that remove duplicates and strengthen class boundaries.

Almost all (80%) of the surveyed works employed deep CNN architectures to address class imbalanced image data. Yet, all of the methods presented can be extended to non-CNN architectures and non-image data. The popularity of CNNs, image classification, and object detection in the research community can be partly attributed to popular benchmark data sets like MNIST and CIFAR, and the continu- ous improvements being driven by competitive events like LSVRC. Class imbalance is not limited to image data, and additional work must be done to evaluate the use of these deep learning class imbalance methods in other domains.

[p. 48]

Approximately half of the studies used only one data set when evaluating their deep learning methods for addressing class imbalance. The authors are not at fault for this, as most were focused on solving a specific problem or benchmark task. However, more comprehensive studies that evaluate these methods across a wider range of data sets, with varying levels of class imbalance and complexity, will better demonstrate their strengths and weaknesses. Also, only a third of the studies indicate the number of rounds or repetitions executed for each experiment. In other words, the remaining groups either did not perform multiple runs, or failed to include those details and pre- sented the most favorable results. To their defense, training a deep learning model on a large data set can take days or even weeks, making it difficult to conduct several rounds of experiments. This creates several avenues for future research, as comparing various deep learning methods on many data sets with repetition will increase confidence in results and help guide future practitioners in model selection.

Less than half of the surveyed works experimented with data sets larger than 100,000 samples. Lee et al. were the only ones to work with more than a million samples con- taining imbalanced data. Pouyanfar et al. provided a big data analytics workflow to clas- sify fast-streaming network camera data, but their experiment was limited to just 10,000 images. This is an extremely important area of research that demands attention if we expect deep learning to provide big data analytics solutions. It is also very likely that the methods proposed throughout this survey, e.g. ROS and RUS, will behave very differ- ently in the context of big data.

It is not currently possible to compare the methods which have been presented directly, as they are evaluated across a variety of data sets with varying levels of class imbalance, and results are reported with inconsistent performance metrics. In addition, some studies report contradictory results, further suggesting that performance is highly dependent on problem complexity, class representation, and the performance metrics reported. Overall, there is a lack of evidence which distinguishes any one deep learning method as superior for learning from class imbalanced data, and additional experiments are required before such conclusions can be made.

[p. 49]

Conclusion To the best of our knowledge, this survey provides the most comprehensive analysis of deep learning methods for addressing the class imbalance data problem. Fifteen studies published between 2015 and 2018 are summarized and discussed, exploring a number of advanced techniques for learning from imbalanced data with DNNs. It has been shown that traditional machine learning techniques for handling class imbalance can be extended to deep learning models with success. The survey also finds that nearly all research in this area has been focused on computer vision tasks with CNNs. Despite a growing demand for big data analytics solutions, there is very little research that properly evaluates deep learning in the context of class imbalance and big data. Deep learning from class imbalanced data is still largely understudied, and statistical evidence which compares newly published meth- ods across a variety of data sets and imbalance levels does not exist.

Several areas for future work are apparent. Applying the newly proposed methods to a larger variety of data sets and class imbalance levels, comparing results with multiple com- plementary performance metrics, and reporting statistical evidence will help to identify the preferred deep learning method for future applications containing class imbalance. Experi- menting with deep learning methods for addressing class imbalance in the context of big data and class rarity will prove valuable to the future of big data analytics. More work is required with non-convolutional DNNs to determine if the methods presented will gener- alize well to alternative architectures, e.g. MLPs and RNNs. Finally, research that evaluates the use of deep learning to address class imbalance in non-image data is limited and should be expanded upon.


---

[previous part](text-006.md) | [source overview](overview.md) | [next part](text-008.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
