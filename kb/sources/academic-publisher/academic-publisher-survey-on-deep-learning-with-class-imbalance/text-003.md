---
type: Source Text
title: Survey on deep learning with class imbalance - part 3 of 9 (pp. 14-22)
description: 'Verbatim extracted text, pp. 14-22: 2 × (TPR + TNR)'
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
part: 3
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 3 of 9, pp. 14-22. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 2 × (TPR + TNR)


[pp. 14-15]

Hensman and Masko presented their results as the percentage of correct answers per class, and included the mean score for all classes, denoted by Total. To ensure results were valid, a total of three runs were completed for each experiment and then aver- aged. Table 3 shows the results of the CNN without any data sampling. These results demonstrate the impact of class imbalance when training a CNN model. Most of the imbalanced distributions saw a loss in performance. Dist. 6 and Dist. 7, which contained very slight imbalance and no over-representation, performed just as well as the origi- nal balanced distribution. Some of the imbalanced distributions that contained over- represented classes, e.g. Dist. 5 and Dist. 9, yielded useless models that were completely biased towards the majority group.

Table 4 includes the results of training the CNN with balanced data that was generated through ROS. It shows that over-sampling performs significantly better than the base- line results from Table 3. Dist. 1 is excluded from Table 4 because it is already balanced, i.e. ROS is not applicable. In this experiment, ROS improved the classification results for all distributions. Dist. 5 and Dist. 9 saw the largest performance gains, increasing

Table 3 Imbalanced CIFAR-10 classification [79]

Total Airplane Automobile Bird Cat Deer Dog Frog Horse Ship Truck

Dist. 1 0.73 0.78 0.84 0.62 0.57 0.70 0.62 0.80 0.76 0.84 0.80

Dist. 2 0.69 0.74 0.75 0.58 0.33 0.58 0.65 0.84 0.78 0.87 0.79

Dist. 3 0.66 0.71 0.75 0.59 0.30 0.52 0.61 0.79 0.77 0.85 0.73

Dist. 4 0.27 0.78 0.24 0.12 0.08 0.19 0.24 0.33 0.27 0.21 0.27

Dist. 5 0.10 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00

Dist. 6 0.73 0.74 0.86 0.65 0.53 0.71 0.63 0.81 0.76 0.83 0.79

[p. 15]

Dist. 7 0.73 0.75 0.86 0.66 0.52 0.71 0.63 0.80 0.78 0.84 0.79

Dist. 8 0.66 0.63 0.75 0.55 0.35 0.51 0.58 0.82 0.74 0.84 0.80

Dist. 9 0.10 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00

Dist. 10 0.69 0.75 0.77 0.56 0.42 0.66 0.63 0.76 0.70 0.81 0.79

Dist. 11 0.69 0.74 0.82 0.58 0.44 0.59 0.64 0.80 0.69 0.83 0.81

Table 4 Imbalanced CIFAR-10 classification with ROS [79]

Total Airplane Automobile Bird Cat Deer Dog Frog Horse Ship Truck

Dist. 2 0.72 0.77 0.80 0.57 0.51 0.68 0.64 0.81 0.78 0.84 0.82

Dist. 3 0.73 0.73 0.80 0.59 0.53 0.63 0.65 0.82 0.81 0.87 0.83

Dist. 4 0.73 0.76 0.82 0.60 0.54 0.68 0.63 0.81 0.78 0.85 0.83

Dist. 5 0.73 0.80 0.84 0.61 0.55 0.68 0.63 0.82 0.79 0.82 0.81

Dist. 6 0.73 0.75 0.86 0.65 0.51 0.65 0.66 0.81 0.78 0.85 0.80

Dist. 7 0.73 0.73 0.85 0.62 0.51 0.71 0.66 0.81 0.79 0.86 0.80

[pp. 15-16]

Dist. 8 0.73 0.78 0.84 0.62 0.56 0.66 0.64 0.81 0.77 0.83 0.80

Dist. 9 0.72 0.73 0.84 0.58 0.55 0.68 0.59 0.79 0.78 0.83 0.82

Dist. 10 0.73 0.78 0.85 0.63 0.50 0.67 0.63 0.82 0.75 0.87 0.80

Dist. 11 0.72 0.82 0.87 0.58 0.64 0.64 0.49 0.78 0.69 0.84 0.80

from baseline Total F1-scores of 0.10 up to 0.73 and 0.72, respectively. The ROS classi- fication results for distributions Dist. 2–Dist. 11 are comparable to the results achieved by the baseline CNN on Dist. 1, suggesting that ROS has completely restored model performance.

The experiments by Hensman and Masko show that applying ROS to the level of class balance can be effective in addressing slight class imbalance in image data. It is also made clear by some of the results in Table 3 that small levels of imbalance are able to prevent a CNN from converging to an acceptable solution. We believe that the low imbalance levels tested ( ρ = 2.3 ) is the biggest limitation of this experiment, as imbal- ance levels are typically much higher in practice. Besides exploring additional data sets and higher levels of imbalance, one area worth pursuing further is the total number of epochs completed during training on the imbalanced data. In these experiments, only 10 epochs over the training data were completed because the authors were more inter- ested in comparing performance than they were in achieving high performance. Run- ning additional epochs would help to rule out whether or not the poor performance was due to the slow convergence phenomenon described by Anand et al.

At the time of writing, May 2015, Hensman and Masko observed no existing research that examined the impact of class imbalance on deep learning with popular benchmark data sets. Our literature review also finds this to be true, confirming that addressing class imbalance with deep learning is still relatively immature and understudied.

[p. 16]

Two‑phase learning Lee et al. [20] combined RUS with transfer learning to classify highly-imbalanced data sets of plankton images, WHOI-Plankton [81]. The data set contains 3.4 million images spread over 103 classes, with 90% of the images comprised of just five classes and the 5th largest class making up just 1.3% of the entire data set. Imbalance ratios of ρ > 650 are exhibited in the data set, with many classes making up less than 0.1% of the data set. The proposed method is the two-phase learning procedure, where a deep CNN is first pre-trained with thresholded data, and then fine-tuned using all data. The thresholded data sets for pre-training are constructed by randomly under-sam- pling large classes until they reach a threshold of N examples. The authors selected a threshold of N = 5000 through preliminary experiments, then down-sampled all large classes to N samples. The proposed model (G) was compared to six alternative methods (A–F), a combination of transfer learning and augmentation techniques, using unweighted average F1-scores to compare results.

(A) Full: CNN trained with original imbalanced data set. (B) Noise: CNN trained with augmented data, where minority classes are duplicated

through noise injection until all classes contain at least 1000 samples. (C) Aug: CNN trained with augmented data, where minority classes are duplicated

through rotation, scaling, translation, and flipping of images until all classes contain at least 1000 samples. (D) Thresh: CNN trained with thresholded data, generated through random under-

sampling until all classes have at most 5000 samples. (E) Noise + full: CNN pre-trained with the noise-augmented data from (B), then fine-

tuned using the full data set. (F) Aug + full: CNN pre-trained with the transform-augmented data from (C), then

fine-tuned using the full data set. (G) Thresh + full: CNN pre-trained using the thresholded data set from (D), then fine-

tuned using the full imbalanced data set.

[pp. 16-17]

Results from Lee et al.’s experiments are presented in Table 5, where the L5 and Rest columns are the unweighted average F1-scores for the largest five classes and the remaining minority classes, respectively. Comparing methods (B–D) shows that under-sampling (D) outperforms both noise injection (B) and augmentation (C) over- sampling methods on the given data set for all classes. Methods (B–D) saw moder- ate improvements on the Rest group when compared to the baseline (A), but the L5 group suffered sufficient loss in performance. Re-training the model with the full data set in (E–G) allowed the models to re-capture the distribution of the L5 group. The proposed model (G) achieved the highest F1-score (0.7791) on the L5 group, and

Table 5 Two-phase learning with WHOI-Plankton (Avg. F1-score) [20]

Classifier All classes L5 Rest

(A) Full 0.1773 0.7773 0.1548

(B) Noise 0.2465 0.5409 0.3599

(C) Aug 0.2726 0.5776 0.3700

(D) Thresh 0.3086 0.6510 0.4044

(E) Noise + full 0.3038 0.7531 0.2971

(F) Aug + full 0.3212 0.7668 0.3156

(G) Thresh + full 0.3339 0.7791 0.3262

greatly improved the F1-score of the Rest group from 0.1548 to 0.3262 with respect to the baseline.

The two-phase learning procedure presented by Lee et al. has proven effective in increas- ing the minority class performance while still preserving the majority class performance. Unlike plain RUS, which completely removes potentially useful information from the train- ing set, the two-phase learning method only removes samples from the majority group during the pre-training phase. This allows the minority group to contribute more to the gradient during pre-training, and still allows the model to see all of the available data during the fine-tuning phase. The authors did not include details on the pre-training phase, such as the number of pre-training epochs or the criteria used to determine when pre-training was complete. These details should be considered in future works, as pre-training that results in high bias or high variance will certainly impact the final model’s class-wise performance. Future work can also consider a hybrid approach, where the model is pre-trained with data that is generated through a combination of under-sampling majority classes and augment- ing minority classes.

[pp. 17-18]

The previous year, Havaei et al. [82] used a similar two-phase learning procedure to man- age class imbalance when performing brain tumor image segmentation. The brain tumor data contains minority classes that make up less than 1% of the total data set. Havaei et al. stated that the two-phase learning procedure was critical in dealing with the imbalanced dis- tribution in their image data. The details of this paper are not included in this survey because the two-phase learning is just one small component of their domain-specific experiments.

Dynamic sampling Pouyanfar et al. [21] used a dynamic sampling technique to perform classification of imbal- anced image data with a deep CNN. The basic idea is to over-sample the low performing classes and under-sample the high performing classes, showing the model less of what it has already learned and more of what it does not understand yet. This is somewhat analo- gous to how humans learn, by moving on from easy tasks once learned and focusing atten- tion on the more difficult tasks. The author’s self-collected data set contains over 10,000 images captured from publicly available network cameras, including a total of 19 semantic concepts, e.g. intersection, forest, farm, sky, water, playground, and park. From the original data set, 70% is used for training models, 20% is used for validation, and 10% is set aside for testing. The authors report imbalance ratios in the data set as high as ρ = 500 . Average F1-scores and weighted average F1-scores are used to compare the proposed model to a baseline CNN (A) and four alternative methods for handling class imbalance (B–E).

The system presented by Pouyanfar et al. includes three core components: real time data augmentation, transfer learning, and a novel dynamic sampling method. Real time data augmentation improves generalization by applying various transformations to select images in each training batch. Transfer learning is achieved by fine-tuning an Inception-V3 net- work [83] that was pre-trained using ImageNet [84] data. The dynamic sampling method is the main contribution relative to class imbalance.

(11) Sample size (F1i, cj) = 1 −f 1i,j

ck∈C(1 −f 1i,k) × N ∗

[pp. 18-19]

F1i is a vector containing all individual class F1-scores after iteration i, and f 1i,j denotes the F1-score for class j on iteration i, where F1-scores are calculated for each class in a one-versus-all manner. During the next iteration, classes with lower F1-scores are sam- pled at a higher rate, forcing the learner to focus more on examples previously misclassi- fied. Eq. 11 is used to obtain the next iteration’s sample size for a given class cj , where N ∗ is the average class size. To prevent over-fitting of the minority group, a second model is trained through transfer learning without sampling. At time of inference, the output label is computed as a function of both models.

The proposed model is compared with the following alternative methods:

(A) Basic CNN: VGGNet [85] CNN trained on entire data set. (B) Deep CNN features + SVM: Support vector machine (SVM) classifier trained with

deep features generated by CNN. (C) Transfer learning without augmentation: Fine-tuned Inception-V3 with no data

augmentation. (D) Transfer learning with augmentation: Fine-tuned Inception-V3 with data augmen-

tation. (E) Transfer learning with balanced augmentation: Fine-tuned Inception-V3 with data

augmentation that enforces class balanced training batches with over-sampling and under-sampling. (F) Proposed model: Dynamic sampling, data augmentation, and transfer learning on

Inception-V3 network.

Average class-wise F1-scores are compared across all 19 concepts, showing that the basic CNN performs the worst in all cases. The basic CNN was unable to classify a single instance correctly for several concepts with very high imbalance ratios, including Play- ground and Airport with imbalance ratios of ρ = 200 and ρ = 500 , respectively. Transfer learning methods (C–E) performed significantly better than the baseline CNN, increas- ing the weighted average F1-score from 0.630 to as high as 0.779. Results in Table 6 show that the proposed method (F) outperforms all other models tested on the given data set. Compared to transfer learning with basic augmentation (D), the dynamic sampling method (F) improved the weighted average F1-score from 0.779 to 0.794.

The dynamic sampling method’s ability to self-adjust sampling rates is its most attractive feature. This allows the method to adapt to different problems contain- ing varying levels of complexity and class imbalance, with little to no hyperparam- eter tuning. By removing samples that have already been captured by the network

Table 6 Dynamic sampling with network camera image data [21]

Classifier Acc. Avg. F1 WAvg. F1

(A) Basic CNN 0.649 0.254 0.630

[p. 19]

(B) Deep CNN features + SVM 0.746 0.528 0.747

(C) TL + no aug. 0.765 0.432 0.755

(D) TL + basic aug. 0.792 0.502 0.779

(E) TL + balanced aug. 0.759 0.553 0.766

(F) Proposed model 0.802 0.599 0.794

parameters, gradient updates will be driven by the more difficult positive class sam- ples. The dynamic sampling method outperforms a hybrid of over-sampling and under-sampling (E) according to F1-scores, but the details of the sampling method are not included in the description. We also do not know how dynamic sampling per- forms against plain RUS and ROS, as these methods were not tested. This should be examined closely in future works to determine if dynamic sampling can be used as a general replacement for RUS and ROS. One area of concern is the method’s depend- ency on a validation set to calculate the class-wise performance metrics that are required to determine sampling rates. This will certainly be problematic in cases of class rarity, where very few positive samples exist, as setting aside data for valida- tion may deprive the model of valuable training data. Methods for maximizing the total available training data should be included in future research. In addition, future research should extend the dynamic sampling method to non-CNN architectures and other domains.

ROS, RUS, and two‑phase learning Buda et al. [23] compare ROS, RUS, and two-phase learning using three multi- class image data sets and deep CNNs. MNIST [86], CIFAR-10, and ImageNet data sets are used to create distributions with varying levels of imbalance. Both MNIST and CIFAR-10 training sets contain 50,000 images spread evenly across 10 classes, i.e. 5000 images per class. Imbalanced distributions were created from MNIST and CIFAR-10 in the range of ρ ∈[10, 5000] and ρ ∈[2, 50] , respectively. The ImageNet training data, containing 100 classes with a maximum of 1000 samples per class, was used to create imbalanced distributions in the range of ρ ∈[10, 100].

[pp. 19-21]

A different CNN architecture was empirically selected for each data set based off recent state-of-the-art results. For the MNIST and CIFAR-10 experiments, a version of the LeNet-5 [58] and the All-CNN [87] architectures were used for classification, respectively. Baseline results were established for each CNN architecture by perform- ing classification on the data sets without any form of class imbalance technique, i.e. no data sampling or thresholding. Next, seven different methods for addressing class imbalance were integrated with the CNN architectures and tested. ROC AUC was extended to the multi-class problem by averaging the one-versus-all AUC for each class, and used to compare the methods. A portion of their results are presented in Fig. 3.

Fig. 3 ROS, RUS, and two-phase learning with MNIST (a–c) and CIFAR-10 (d–f) [23]

(A) ROS: All minority classes were over-sampled until class balance was achieved,

where any class smaller than the largest class size is considered a minority class. In almost all experiments, over-sampling displayed the best performance, and never showed a decrease in performance when compared to the baseline. (B) RUS: All majority classes were under-sampled until class balance was achieved,

where any class larger than the smallest class size is considered a majority class. RUS performed poorly when compared to the baseline models, and never displayed a notable advantage to ROS. RUS was comparable to ROS only when the total num- ber of minority classes was very high, i.e. 80–90%. (C) Two-phase training with ROS: The model is first pre-trained on a balanced data set

which is generated through ROS, and then fine-tuned using the complete data set. In general, this method performed worse than strict ROS (A). (D) Two-phase training with RUS: Similar to (C), except the balanced data set used for

pre-training is generated through RUS. Results show that this approach was less effective than RUS (B). (E) Thresholding with prior class probabilities: The network’s decision threshold is

adjusted during the test phase based on the prior probability of each class, effec- tively shifting the output class probabilities. Thresholding showed improvements to overall accuracy, especially when combined with ROS. (F) ROS and thresholding: The thresholding method (E) is applied after training the

model with a balanced data set, where the balanced data set is generated through ROS. Thresholding combined with ROS performed better than the baseline thresh- olding (E) in most cases. (G) RUS and thresholding: The thresholding method (E) is applied after training the

model with a balanced data set, where the balanced data set is produced through RUS. Thresholding with RUS performed worse than (E) and (F) in all cases.

[pp. 21-22]

The work by Buda et al., which varies levels of class imbalance and problem complexity, is comprehensive, having trained almost 23,000 deep CNNs across three popular data sets. The impact of class imbalance was validated on a set of baseline CNNs, showing that classification performance is severely compromised as imbalance increases and that the impact of class imbalance seems to increase as problem complexity increases, e.g. CIFAR-10 versus MNIST. The authors conclude that ROS is the best overall method for addressing class imbalance, that RUS generally performs poorly, and that two-phase learning with ROS or RUS is not as effective as their plain ROS and RUS counterparts.

While it does provide a reasonable high-level view of each method’s performance, the multi-class ROC AUC score provides no insight into the underlying class-wise perfor- mance trade-offs. It is not clear if there is high variance in the class-wise scores, or if one extremely low class-wise score is causing a large drop in the average AUC score. We believe that additional performance metrics, including class-wise scores, will better explain the effectiveness of each method in addressing class imbalance and help guide practitioners in model selection.

Buda et al. conclude that ROS should be performed until all class imbalance is elimi- nated. Despite their experimental results, we do not readily agree with this blanket state- ment, and argue that this is likely problem-dependent and requires further exploration.

The MNIST data set, both relatively low in complexity and small in size, was used to demonstrate that over-sampling until all classes are balanced performs best. We do not know how well over-sampling to this level will perform on more complex data sets, or in problems containing big data or class rarity. Furthermore, over-sampling to this level of class balance in a big data problem can be extremely resource intensive, drastically increasing training time by introducing large volumes of redundant data.

[p. 22]

Summary of data‑level methods Two of the surveyed works [23, 79] have shown that eliminating class imbalance in the training data with ROS significantly improves classification results. Lee et al. have shown that pre-training DNNs with semi-balanced data generated through RUS or augmen- tation-based over-sampling improves minority group performance. In contrast to Lee et al., Buda et al. found that plain ROS and RUS generally perform better than two-phase learning. Unlike Lee et al., however, Buda et al. pre-trained their networks with data that was sampled until class balance was achieved. Since Lee et al. and Buda et al. used dif- ferent imbalance levels for pre-training, and reported results with different performance metrics, it is difficult to understand the efficacy of two-phase learning. The dynamic sampling method outperformed baseline CNNs, but we do not know how it compares to ROS, RUS, or two-phase learning. Despite this limitation, the dynamic sampling meth- od’s ability to automatically adjust sampling rates throughout the training process is very appealing. Methods that can automatically adjust to varying levels of complexity and imbalance levels are favorable, as they reduce the number of tunable hyperparameters.

The experimental results suggest the use of ROS to eliminate class imbalance during the training of DNNs. This may be true for relatively small data sets, but we believe this will not hold true for problems containing big data or extreme class imbalance. Apply- ing ROS until classes are balanced in very-large data sets, e.g. WHOI-Plankton data, will result in the duplication of large volumes of data and will drastically increase training times. RUS, on the other hand, reduces training time and may therefore be more practi- cal in big data problems. We believe that RUS methods that remove redundant samples, reduce class noise, and strengthen class borders will prove helpful in these big data prob- lems. Future work should explore these scenarios further.

All of the data-level methods presented were tested on class imbalanced image data with deep CNNs. In addition, differences in performance metrics and problem complexity make it difficult to compare methods directly. Future works should test these data-level methods on a variety of data types, imbalance levels, and DNN architectures. Multiple complemen- tary performance metrics should be used to compare results, as this will better illustrate method trade-offs and guide future practitioners.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
