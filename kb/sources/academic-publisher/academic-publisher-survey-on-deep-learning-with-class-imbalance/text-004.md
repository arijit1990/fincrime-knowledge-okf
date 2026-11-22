---
type: Source Text
title: Survey on deep learning with class imbalance - part 4 of 9 (pp. 22-29)
description: 'Verbatim extracted text, pp. 22-29: 2 × (TPR + TNR); (15) MSFE = FPE2 + FNE2; MSE MFE MSFE MSE MFE MSFE'
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
part: 4
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:50:18Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:50:18Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 4 of 9, pp. 22-29. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 2 × (TPR + TNR)


[pp. 22-23]

Algorithm‑level methods This section includes surveyed works that modify deep learning algorithms for the pur- pose of addressing class imbalance. These methods can be further divided into new loss functions, cost-sensitive learning, and threshold moving. Wang et al. [18] and Lin et al. [88] introduced new loss functions that allow the minority samples to contribute more to the loss. Wang et al. [89], Khan et al. [19], and Zhang et al. [90] experimented with cost-sensi- tive DNNs. The methods proposed by Khan et al. and Zhang et al. have the advantage of

learning cost matrices during training. The work by Buda et al. in the "ROS, RUS, and two- phase learning" section has also been included in this section, as they experimented with threshold adjusting. Zhang et al. [91] combine transfer learning, CNN feature extraction, and a cluster-based nearest neighbor rule to improve the classification of imbalanced image data. Finally, Ding et al. [92] experiment with very-deep CNNs to determine if increasing neural network depth improves convergence rates with imbalanced data.

Mean false error (MFE) loss Wang et al. [18] found some success in modifying the loss function as they experimented with classifying imbalanced data with deep MLPs. A total of eight imbalanced binary data sets, including three image data sets and five text data sets, were generated from the CIFAR- 100 [93] and 20 Newsgroup [94] collections. The data sets are all relatively small, with most training sets containing fewer than 2000 samples and the largest training set containing just 3500 samples. For each data set generated, imbalance ratios ranging from ρ = 5 to ρ = 20 were tested.

The authors first show that the mean squared error (MSE) loss function poorly captures the errors from the minority group in cases of high class imbalance, due to many nega- tive samples dominating the loss function. They then propose two new loss functions that are more sensitive to the errors from the minority class, mean false error (MFE) and mean squared false error (MSFE). The proposed loss functions were derived by first splitting the MSE loss into two components, mean false positive error (FPE) and mean false negative error (FNE). The FPE (Eq. 12) and FNE (Eq. 13) values are then combined to define the total system loss, MFE (Eq. 14), as the sum of the mean error from each class.

Wang et al. introduce the MSFE loss (Eq. 15) as an improvement to the MFE loss, assert- ing that it better captures errors from the positive class. The MSFE can be expanded into the form 1

[p. 23]

2((FPE + FNE)2 + (FPE −FNE)2) , demonstrating how the optimization process minimizes the difference between FPE and FNE. The authors believe this improved version will better balance the error rates between the positive and negative classes.

n )2

1 2(d(i) n −y(i)

n

i=1

n )2

1 2(d(i) n −y(i)

n

i=1

A deep MLP trained with the standard MSE loss is used as the baseline model. This same MLP architecture is then used to evaluate both the MFE and MSFE loss. Image classifi- cation results (Table 7) and text classification results (Table 8) show that the proposed models outperform the baseline in nearly all cases, with respect to F-measure and AUC scores.

## (15) MSFE = FPE2 + FNE2


[p. 24]

Table 7 CIFAR-100 classification with MFE and MSFE [18]

F-measure AUC​

Data set Imbalance level (%)

Household 20 0.3913 0.4138 0.4271 0.7142 0.7397 0.7354

10 0.2778 0.2797 0.3151 0.7125 0.7179 0.7193

5 0.1143 0.1905 0.2353 0.6714 0.6950 0.6970

## MSE MFE MSFE MSE MFE MSFE


Tree 1 20 0.5500 0.5500 0.5366 0.8100 0.8140 0.8185

10 0.4211 0.4211 0.4211 0.7960 0.7990 0.7990

5 0.1667 0.2353 0.2353 0.7920 0.8000 0.8000

Tree 2 20 0.4348 0.4255 0.4255 0.8480 0.8450 0.8440

10 0.1818 0.2609 0.2500 0.8050 0.8050 0.8060

5 0.0000 0.1071 0.1481 0.5480 0.6520 0.7000

Italic scores indicate MFE/MSFE loss outperforming MSE loss

Table 8 20 Newsgroup classification with MFE and MSFE[18]

F-measure AUC​

Data set Imbalance level (%)

Doc. 1 20 0.2341 0.2574 0.2549 0.5948 0.5995 0.5987

10 0.1781 0.1854 0.1961 0.5349 0.5462 0.5469

5 0.1356 0.1456 0.1456 0.5336 0.5436 0.5436

Doc. 2 20 0.3408 0.3393 0.3393 0.6462 0.6464 0.6464

10 0.2094 0.2000 0.2000 0.6310 0.6319 0.6322

5 0.1256 0.1171 0.1262 0.6273 0.6377 0.6431

Doc. 3 20 0.2929 0.2957 0.2957 0.5862 0.5870 0.5870

10 0.1596 0.1627 0.1698 0.5577 0.5756 0.5865

5 0.0941 0.1118 0.1084 0.5314 0.5399 0.5346

Doc. 4 20 0.3723 0.3843 0.3668 0.6922 0.7031 0.7054

10 0.1159 0.2537 0.2574 0.5623 0.6802 0.6816

[pp. 24-25]

5 0.1287 0.1720 0.1720 0.6041 0.6090 0.6090

Doc. 5 20 0.3103 0.3222 0.3222 0.6011 0.5925 0.5925

10 0.1829 0.1808 0.1839 0.5777 0.5836 0.5837

5 0.0946 0.1053 0.1053 0.5682 0.5730 0.5730

Italic scores indicate MFE/MSFE loss outperforming MSE loss

Results show that the MFE and MSFE loss functions outperform MSE loss in almost all cases. Improvements over the baseline MSE loss are most apparent when class imbalance is greatest, i.e. imbalance levels of 5%. The MFE and MSFE performance gains are also more pronounced on the image data than on the text data. For example, the MSFE loss improved the classification of Household image data, increasing the F1-score from 0.1143 to 0.2353 when the class imbalance level was 5%.

Being relatively easy to implement and integrate into existing models is one of the big- gest advantages of using custom loss functions for addressing class imbalance. Unlike data-level methods that increase the size of the training set, the loss function is less likely to increase training times. The loss functions should generalize to other domains with ease, but as seen in comparing the image and text performance results, performance gains will vary from problem to problem. Additional experiments should be performed

to validate MFE and MSFE effectiveness, as it is currently unclear how many rounds were conducted per experiment and the F1-score and AUC gains over the baseline are only minor improvements. On the image data experiments, for example, the average AUC gain over the baseline is just 0.025, with a median AUC gain over the baseline of only 0.008.

[p. 25]

Focal loss Lin et al. [88] proposed a model that effectively addresses the extreme class imbalance commonly encountered in object detection problems, where positive foreground sam- ples are heavily outnumbered by negative background samples. Two-stage and one- stage detectors are well-known methods for solving such problems, where the two-stage detectors typically achieve higher accuracy at the cost of increased computation time. Lin et al. set out to determine whether a fast single-stage detector was capable of achiev- ing state-of-the-art results on par with current two-stage detectors. Through analysis of various two-stage detectors (e.g. R-CNN [95] and its successors) and one-stage detectors (e.g. SSD [96] and YOLO [97]), class imbalance was identified as the primary obstacle preventing one-stage detectors from achieving state-of-the-art performance. The over- whelming number of easily classified negative background candidates create imbalance ratios commonly in the range of ρ = 1000 , causing the negative class to account for the majority of the system’s loss.

To combat these extreme imbalances, Lin et al. presented the focal loss (FL) (Eq. 16), which re-shapes the cross entropy (CE) loss in order to reduce the impact that easily classified samples have on the loss. This is achieved by multiplying the CE loss by a mod- ulating factor, αt(1 −pt)γ . Hyper parameter γ ≥0 adjusts the rate at which easy exam- ples are down weighted, and αt ≥0 is a class-wise weight that is used to increase the importance of the minority class. Easily classified examples, where pt →1 , cause the modulating factor to approach 0 and reduce the sample’s impact on the loss.

(16) FL(pt) = −αt(1 −pt)γ log(pt)

Table 9 RetinaNet (focal loss) on COCO [88]

Backbone AP AP50 AP75 APS APM APL

Two-stage methods

Faster R-CNN+++ ResNet-101-C4 34.9 55.7 37.4 15.6 38.7 50.9

Faster R-CNN w FPN ResNet-101-FPN 36.2 59.1 39.0 18.2 39.0 48.2

Faster R-CNN by G-RMI Inception-ResNet-v2 34.7 55.5 36.7 13.5 38.1 52.0

Faster R-CNN w TDM Inception-ResNet-v2-TDM 36.8 57.7 39.2 16.2 39.8 52.1

One-stage methods

YOLOv2 DarkNet-19 21.6 44.0 19.2 5.0 22.4 35.5

[pp. 25-26]

SSD513 ResNet-101-SSD 31.2 50.4 33.3 10.2 34.5 49.8

DSSD513 ResNet-101-DSSD 33.2 53.3 35.2 13.0 35.4 51.1

RetinaNet ResNet-101-FPN 39.1 59.1 42.3 21.8 42.7 50.2

RetinaNet ResNeXt-101-FPN 40.8 61.1 44.1 24.1 44.2 51.2

Italic scores indicate top AP performances

The proposed one-stage focal loss model, RetinaNet, is evaluated against several state- of-the-art one-stage and two-stage detectors. The RetinaNet model is composed of a backbone model and two subnetworks, where the backbone model is responsible for producing feature maps from the input image, and the two subnetworks then perform object classification and bounding box regression. The authors selected the feature pyra- mid network (FPN) [88], built on top of the ResNet architecture [98], as the backbone model and pre-trained it on ImageNet data. They found that the FPN CNN, which pro- duces features at different scales, outperforms the plain ResNet in object detection. Two additional CNNs with separate parameters, the subnetworks, are then used to perform classification and bounding box regression. The proposed focal loss function is applied to the classification subnet, where the total loss is computed as the sum of the focal loss over all ≈100, 000 candidates. The COCO [99] data set was used to evaluate the pro- posed model against its competitors.

The first attempt to train RetinaNet using standard CE loss quickly fails and diverges due to the extreme imbalance. By initializing the last layer of the model such that the prior probability of detecting an object is π = 0.01 , results improve significantly to an average precision (AP) of 30.2. Additional experiments are used to determine appropri- ate hyper parameters for the focal loss, selecting γ = 2.0 and α = 0.25 for all remaining experiments.

[pp. 26-27]

Experiments by Lin et al. show that the RetinaNet, with the proposed focal loss, is able to outperform existing one-stage and two-stage object detectors. It outscores the runner-up one-stage detector (DSSD513 [100]) and the best two-stage detector (Faster R-CNN with TDM [101]) by 7.6-point and 4.0-point AP gains, respectively. When com- pared to several online hard example mining (OHEM) [102] methods, RetinaNet out- scores the best method with an increase in AP from 32.8 to 36.0. Table 9 compares results between RetinaNet and seven state-of-the-art one-stage and two-stage detectors.

Lin et al. provide additional information to illustrate the effectiveness of the focal loss method. In one experiment, they use a trained model to compute the focal loss over ≈107 negative images and ≈105 positive images. By plotting the cumulative distribution

function for positive and negative samples, they show that as γ increases, more and more weight is placed onto a small subset of negative samples, i.e. the hard negatives. In fact, with γ = 2 , they show that most of the loss is derived from a very small fraction of sam- ples, and that the focal loss is indeed reducing the impact of easily-classified negative samples on the loss. Run time statistics were included in the report to demonstrate that they were able to construct a fast one-stage detector capable of outperforming accurate two-stage detectors.

The new FL method lends itself to not just class imbalance problems, but also hard sample problems. It addresses the primary minority class gradient issue defined by Anand et al. by preventing the majority group from dominating the loss and allowing the minority group to contribute more to the weight updates. Similar to the MFE and MSFE loss functions, advantages include being relatively easy to integrate into existing models and having minimal impact on training time. We believe that the FL method’s ability to down-weight easily-classified samples will allow it to generalize well to other domains. The authors compared FL directly to the CE loss, but we do not know how FL compares to other existing class imbalance methods. Future works should compare this

Fig. 4 Focal loss and building change detection [103]

loss function to alternative class imbalance methods across a variety of data sets and class imbalance levels.

[pp. 27-28]

Nemoto et al. [103] later used the focal loss in another image classification task, the automated detection of rare building changes, e.g. new construction. The airborne building images are annotated with the labels: no change, new construction, rebuild- ing, demolished, repaint roofs, and laying solar panel. The training data contains 203,358 images in total, where 200,000 comprise the negative class, i.e. no change. The repaint roofs and laying solar panel classes contain just 326 and 222 images, respectively, yield- ing class imbalance ratios as high as ρ = 900.

The experiments by Nemoto et al. utilize the VGG-16 [85] CNN architecture, where the baseline CNN uses the standard CE loss. Images were augmented by rotation and inversion, creating 20,000 samples per class. Class-wise accuracy on the validation set was used to compare the focal loss to the CE loss. The first experiment uses the CE loss function and shows that the accuracy on the repaint roof and laying solar panel classes begins to deteriorate after 25,000 iterations, suggesting over-fitting. In the second exper- iment, focal loss was evaluated using the same VGG-16 architecture and the same image augmentation procedure, generating 20,000 images per class. Unlike the first experi- ment, however, only three classes were selected for training and validation: no change, repaint roof, and laying solar panel images. The value of the focal loss’s down-weighting parameter γ was varied in the range γ ∈[0, 5] to better understand its impact.

Figure 4 shows the training validation loss and accuracy of the focal loss method. Nemoto et al. conclude that focal loss improves problems related to class imbalance and over-fitting by adjusting the per-class learning speed. By comparing the loss plots, it is clear that as γ increases, the total loss decreases faster and the model is slower to over- fit. It is not clear, however, if FL with γ > 0 is producing better classification results. First, the results from the first experiment cannot be compared to the results of the sec- ond experiment, because the total number of classes has been reduced from six to three, significantly reducing the complexity of the classification problem. Second, the results from the no change and laying solar panel classes in Fig. 4 show that the highest accu- racy is achieved when γ = 0 , where the laying solar panel class is the smallest class. The focal loss, with γ = 0 , reduces to the standard cross entropy loss, suggesting that the CE

loss outperforms the focal loss on two of the three classes in this experiment. To better understand the effectiveness of FL, future work should include a baseline with consistent training data, several alternative methods for addressing class imbalance, and additional performance metrics.

[p. 28]

Cost‑sensitive deep neural network (CSDNN) Wang et al. [89] employed a cost-sensitive deep neural network (CSDNN) method to detect hospital readmissions, a class imbalanced problem where a small percentage of patients are readmitted to a hospital shortly after their original visit. Two data sets were provided by the Barnes-Jewish Hospital, containing patient records spanning from 2007 to 2011. The first data set, general hospital wards (GHW), contains vital signs, clini- cal processes, demographics, real-time bedside monitoring, and other electronic data sources. Of the 2565 records in GHW, 406 patients were readmitted within 30 days and 538 patients were readmitted within 60 days, producing imbalance ratios of ρ = 5.3 and ρ = 3.8 , respectively. The second data set, the operating room pilot data (ORP), contains vital signs, pre-operation data, laboratory tests, medical history, and procedure details. There are 700 records in the ORP data set, with 157 readmissions within 1 year and 124 readmissions within 30 days. The imbalance ratio of the ORP data is unclear; the authors merely state that the ORP data is less imbalanced than the GHW data ( ρ < 3.8 ). A vari- ety of performance metrics, including ROC, AUC, accuracy, recall, precision, positive predictive value (PPV), and negative predictive value (NPV) are used for evaluation. The PPV and NPV metrics are equivalent to positive and negative class precision scores. The proposed CSDNN method was found to outperform existing hospital readmission pre- diction systems, and has been deployed at the Barnes-Jewish Hospital.

Instead of representing categorical values with traditional one-hot encoding, Wang et al. use a categorical feature embedding approach to create more meaningful represen- tations. In addition, they employed a CNN for automatic feature extraction from time series data, i.e. the patient vital signs data. The extracted features and categorical embed- dings are concatenated, forming a final input feature vector that is fed to a DNN for clas- sification. The DNN was composed of two hidden layers, with 128 and 64 neurons per layer. The CE loss function was modified to incorporate a pre-defined cost matrix, forc- ing the network to minimize misclassification cost. For the GHW data set, false negative errors were given a cost 2× the cost of false positive errors. Similarly for the ORP data set, the false negative cost was set to 1.5× the cost of false positive errors.

[pp. 28-29]

Wang et al.’s CSDNN method is compared to five baseline classifiers, including three decision tree methods, a SVM, and an ANN. Only one of the baseline methods addresses class imbalance, using under-sampling with a Random Forest (RF) classifier. The pro- posed method outperformed all of the baseline classifiers across all performance metrics except for NPV. We were able to observe the class-wise performance trade-off because multiple complementary performance metrics were reported. On the GHW data set, the CSDNN’s AUC of 0.70 outscored the runner up’s (ANN classifier) AUC of 0.62. Unfortunately, however, it is not possible to determine if the cost-sensitive loss function is the cause of the improved performance, as there are several other factors that may have contributed to improvements, e.g. categorical feature embedding and time-series

feature extraction. A baseline that includes the CNN feature extractor and the categori- cal embeddings is required to isolate the efficacy of the cost-sensitive loss function.

Incorporating the cost matrix into the CE loss is a minor implementation detail that should generalize well to other domains and architectures with minimal impact on train- ing times. The process of identifying an ideal cost matrix is likely the biggest limitation. In traditional machine learning problems with relatively small data sets, models can be validated across a range of costs and the best cost matrix can be selected for the final model. When working with DNNs and large data sets, however, this process of searching for the best cost parameters can be very time consuming and even impractical. Including results from a range of cost matrices in future work will help to demonstrate the class- wise performance trade-offs that occur as costs vary.

Learning cost matrices with cost‑sensitive CNN (CoSen) Khan et al. [19] introduced an effective cost-sensitive deep learning procedure which jointly learns network weight parameters and class misclassification costs during train- ing. The proposed method, CoSen CNN, is evaluated against six multi-class data sets with varying levels of imbalance: MNIST, CIFAR-100, Caltech-101 [104], MIT-67 [105], DIL [106], and MLC [107]. Class imbalance ratios of ρ = 10 are tested for the MNIST, CIFAR-100, Caltech-101, and MIT-67 data sets. The DIL and MLC data sets have imbal- ance ratios of ρ = 13 and ρ = 76 , respectively. The VGG-16, pre-trained on ImageNet data, is used as a feature extractor and the baseline CNN throughout the experiments.

[p. 29]

The cost matrix that is learned by the CoSen CNN is used to modify the output of the VGG-16 CNN’s last layer, giving higher importance to samples with higher cost. The group presents three modified loss functions, incorporating the learned cost parame- ters into MSE loss, SVM hinge loss, and CE loss. The training process learns network weight parameters and misclassification cost parameters by keeping one fixed at a time, and minimizing cost with respect to the other during training. The cost matrix update is dependent on the current classification errors, the overall classification error, and the class-to-class separability (C2C). The C2C separability measures relationships between within-class sample distances and the size of class-separating boundaries.

Table 10 Cost-sensitive CoSen CNN results (accuracy) [19]


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
