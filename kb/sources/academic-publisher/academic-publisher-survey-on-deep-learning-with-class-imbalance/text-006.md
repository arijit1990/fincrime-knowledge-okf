---
type: Source Text
title: Survey on deep learning with class imbalance - part 6 of 9 (pp. 34-41)
description: 'Verbatim extracted text, pp. 34-41: AU26 25.6% 0.64 0.73 0.74 0.73 0.74 0.73; PANDA 91 74 51 51 76 67 85 88 68 84 65 81 50 90 64 69 79 63 74 77; LMLE-'
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
part: 6
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:42:06Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:42:06Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 6 of 9, pp. 34-41. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## AU26 25.6% 0.64 0.73 0.74 0.73 0.74 0.73


[p. 34]

Average – 0.29 0.48 0.48 0.49 0.49 0.50

for training and 40,000 images were randomly selected for validation. The images in this data set contain 11 possible FAUs. Since an image can be positive for more than one FAU, the authors treated the classification problem as a set of 11 binary problems. Sev- eral FAUs are present in less than 1% of the data set, e.g. nose wrinkler, chin raiser, and upper lid raiser. The lip stretcher FAU is only present in 0.01% of the data, creating a max imbalance ratio to ρ = 10, 000 . Six deep CNN architectures are compared, all of which include 3 × 3 convolution filter layers and are trained for 100 epochs:

(A) Handcraft: 6-layer CNN (B) Plain34: 34-layer CNN (C) Res10: 10-layer ResNet CNN (D) Res18: 18-layer ResNet CNN (E) Res34: 34-layer ResNet CNN (F) Res50: 50-layer ResNet CNN.

F1-scores from the first experiment are presented in Table 12. The shallow network (A) was unable to capture classes containing high imbalance, e.g. AU2–AU5, during the 100 training epochs. The non-residual 34-layer CNN (B) saw a large boost in performance compared to the shallow network (A), with average F1-score increasing from 0.29 to 0.48. It can also be observed that the 10-layer ResNet (C) achieved an equal F1-score of 0.48. The FAU with the largest imbalance, i.e. lip stretcher (AU20), received an F1-score of 0.0 in all experiments. There is no noticeable difference in F1-scores between the net- works with 10 layers or more (B–F). The 34-layer ResNet (E) won first place at the first track EmotioNet Challenge in 2017 [116].

In a second experiment, Ding et al. compare the convergence rate of a very-deep 18-layer CNN to a shallower 6-layer CNN across 100 epochs. The experiment shows that the very-deep 18-layer CNN converges faster than the shallower network, as the error decreases at a faster rate. The authors suggest that the shallower network will con- tinue to converge, provided additional epochs.

The experiments by Ding et al. show that additional hidden layers can increase the convergence rate on facial action recognition. Training very-deep neural networks

[p. 35]

comes at a cost, however, as it increases the total number of matrix operations and the memory footprint. Additional experiments are required to determine if this increased convergence rate is observed with alternative deep learning architectures and data sets. With the convergence rate in question, other methods that have been shown to impact convergence rates should be included in future studies, e.g. alternative optimization methods, dynamic learning rates, and weight initialization.

Summary of algorithm‑level methods This section included eight algorithm-level methods for addressing class imbalance with DNNs. The MFE and MSFE loss functions presented by Wang et al. outperform the standard MSE loss on several image and text data sets. Lin et al.’s focal loss, which down-weights easy-to-classify samples, was used to outperform several state-of-the- art one-stage and two-stage object detectors on the COCO data set. Nemoto et al. also explored focal loss for the purpose of detecting rare building changes, but the results were somewhat contradictory. A cost-sensitive method that incorporates pre-defined misclassification costs into the CE loss function was used by Wang et al. to predict hos- pital readmissions. Khan et al. proposed a cost-sensitive deep CNN (CoSen) that jointly learns network parameters and cost matrix parameters during training. Overall accuracy was used to show that the CoSen CNN outperforms a baseline CNN, multiple sampling methods, and multiple cost-sensitive methods consistently across six image data sets. Similarly, Zhang et al. combined a DBN with an evolutionary algorithm that searches for optimal misclassification costs, but results were again reported with the accuracy metric and are difficult to interpret. Buda et al. demonstrated how prior class probabili- ties can be used to adjust DNN output thresholds to improve overall accuracy in classi- fying image data. Zhang et al. presented category centers, a method that addresses class imbalance by combining transfer learning, deep CNN feature extraction, and a nearest deep feature cluster discrimination rule. Finally, Ding et al. experimented with very-deep neural networks ( > 10 layers) and showed that deeper networks may converge faster due to changes in the error surfaces that allow for faster optimization.

Unlike data sampling methods, the algorithm-level methods presented do not alter the training data and do not require any pre-processing steps. Compared to ROS, which was recommended by multiple authors in the "Data-level methods" section, algorithm-level methods are less likely to impact training times. This suggests that algorithm-level meth- ods may be better equipped for big data problems. With the exception of defining mis- classification costs, the algorithm-level methods require little to no tuning. Fortunately, two methods were presented for automatically learning cost parameters. Methods which are able to adapt to different problems with minimal tuning are preferred, as they can be quickly applied to new problems and do not require specific domain knowledge. The focal loss function and CoSen CNN demonstrate this flexibility, and we believe they will generalize well to many complex problem domains.

[pp. 35-36]

In general, there is a lack of research that appropriately compares deep learning algo- rithm-level methods to alternative class imbalance methods. This is due to poor choices in baseline models, insufficient performance metrics, and domain-specific experiments that fail to isolate the proposed class imbalance method. Similar to the surveyed deep

learning data-level methods, most of the methods in this section were evaluated on image data with deep CNNs. We are most interested in understanding how deep learn- ing methods for addressing class imbalance compare to each other and to traditional machine learning techniques for class imbalance. We believe that filling these research gaps and properly evaluating these methods will have a great impact on future deep learning applications.

Hybrid‑methods The deep learning techniques for addressing class imbalance in this section combine algorithm-level and data-level methods. Huang et al. [22] use a novel loss function and sampling method to generate more discriminative representations in their Large Mar- gin Local Embedding (LMLE) method. Ando and Huang [117] presented the first deep feature over-sampling method, Deep Over Sampling (DOS). Finally, class imbalance in large-scale image classification is addressed by Dong et al. [118] with a novel loss func- tion and hard sample mining.

Large Margin Local Embedding (LMLE) Huang et al. [22] proposed the LMLE method for learning more discriminative deep representations of imbalanced image data. The method is motivated by the observa- tion that minority groups are sparse and typically contain high variability, allowing the local neighborhood of these minority samples to be easily invaded by samples of another class. By combining a new informed quintuplet sampling method with a new triple- header hinge loss function, deep feature representations that preserve same class locality and increase inter-class discrimination are learned from imbalanced image data. These deep feature representations, which form well-defined clusters, are then used to label new samples with a fast cluster-wise K-NN classification method. The proposed LMLE method is shown to achieve state-of-the-art results on the CelebA [119] data set, which contains high imbalance levels up to ρ = 49.

The quintuplet sampling method selects an anchor and four additional samples based on inter-class and intra-class cluster distances. During training, each mini-batch selects an equal number of quintuplets from both the minority and majority classes. The five samples obtained by the quintuplet sampling method are fed to five identical CNNs, and their outputs are aggregated into a single result. The triple-header hinge loss is then used to compute the error and update the network parameters accordingly. This regular- ized loss function constrains the deep feature representation such that clusters collapse into small neighborhoods with appropriate margins between inter-class and intra-class clusters.

[pp. 36-37]

The CelebA data set contains facial images annotated with 40 attributes, with imbal- ance levels as high as ρ = 49 (Bald vs not Bald). A total of 160,000 images are used to train a CNN, and the learned deep representations are then fed to a modified K-NN classifier. The Balanced Accuracy (Eq. 9) metric is calculated for each facial attribute. The LMLE-kNN model is compared to three state-of-the-art models in the facial attrib- ute recognition domain: Triplet-kNN [120], PANDA [121], and ANet [122]. Results in Table 13 show that the LMLE-kNN performs as good as, or better than, alternative methods for all facial attributes. Performance gains over alternative methods increased

beard Bangs

earings No

hair Mustache Bald Average

under eyes Wear

skin Gray

hair Bags

chin Pale

hair Brown

hat Double

nose Young Straight

lips Big

hair Big

eyebrows Black

cheeks Goatee Chubby Sideburns Blurry Wear

nose Arched

face Pointy

hair Oval

necktie Eyeglasses Rosy

makeup Wavy

hairline Wear

cheekbones Male Heavy

eyes 5 o’clock shadow Receding

lipstick High

necklace Narrow

eyebrows Wear

open Smiling Wear

Blond

hair Bushy

1 2 2 3 5 8 11 18 22 22 23 26 26 27 28 29 30 30 31 33 35

Attractive Mouth

level 35 36 38 38 39 42 43 44 44 44 44 44 45 45 45 46 46 46 48

ance

level

kNN 83 92 92 91 86 91 88 77 61 61 73 82 55 68 75 63 76 63 69 82 81

kNN 88 96 99 99 92 99 98 83 68 72 79 92 60 80 87 73 87 73 83 96 98

Triplet-kNN 81 68 50 47 66 60 73 82 64 73 64 71 43 84 60 63 72 57 75 72

## PANDA 91 74 51 51 76 67 85 88 68 84 65 81 50 90 64 69 79 63 74 77


[p. 37]

ANet 90 82 59 57 81 70 79 95 76 86 70 79 56 90 68 77 85 61 73 80

LMLE-kNN 99 82 59 59 82 76 90 98 78 95 79 88 59 99 74 80 91 73 90 84

Imbalance

Table 13 LMLE CelebA facial attribute recognition (Balanced Accuracy) [22]

Imbal-

Triplet-

ANet 87 96 97 95 89 99 96 81 67 69 76 90 57 78 84 69 83 70 83 93 90

## LMLE-


[p. 38]

as levels of imbalance increased, e.g. LMLE increased accuracy on the Bald attribute from 75 to 90 when compared to its runner-up. The authors achieved similar results when comparing the LMLE-kNN to 14 state-of-the-art models on the BSDS500 [123] edge detection data set.

Huang et al. were one of the first to study deep representation learning with class imbalanced data. The proposed LMLE method combines several powerful concepts, achieves state-of-the-art results on a popular image data benchmark, and shows poten- tial for future works in other domains. The high-performance results do come with a cost, however, as the system is both complex and computationally expensive. The data must be pre-clustered before quintuplet sampling can take place, which may be dif- ficult if a suitable feature extractor is not available for the given data set. The authors do suggest that the initial clustering is not important, because the learning procedure can be used to re-cluster the data throughout training. Furthermore, each forward pass through the system requires computation from five CNNs, one for each of the quintu- plets sampled. We are in agreement with the statement made by Ando and Huang [117], that adapting LMLE to new problems will require many task and model specific con- figurations. This will likely deter many practitioners from using this method when trying to solve class imbalanced problems, as most will resort to simpler and faster methods. Results provided by Dong et al. in the "Class rectification loss (CRL) and hard sample mining" section will show that LMLE outperforms ROS, RUS, thresholding, and cost- sensitive learning on the CelebA data set.

Deep over‑sampling (DOS) Ando and Huang [117] introduced over-sampling to the deep feature space produced by CNNs in their DOS framework. The proposed method is extensively evaluated by generating imbalanced data sets from five popular image benchmark data sets, including MNIST, MNIST-back-rot, SVHN [124], CIFAR-10, and STL-10 [125]. Class-wise preci- sion and recall, F1-scores, and AUC are used to evaluate the DOS framework against alternative methods.

[pp. 38-39] [ref: 0.95]

The DOS framework consists of two simultaneous learning procedures, optimizing the lower layer and upper layer parameters separately. The lower layers are responsible for acquiring the embedding function, while the upper layers learn to discriminate between classes using the generated embeddings. In order to learn the embedding features, the CNN’s input is presented with both a class label and a set of deep feature targets, an in-class nearest neighbor cluster from deep feature space. Then the micro-cluster loss computes the distances between each of the deep feature targets and their mean, con- straining the optimization of the lower layers to shift deep feature embeddings towards the class mean. Ando and Huang state that shifting target representations to their cor- responding local mean will induce smaller in-class variance and strengthen class distinc- tion in the learned representations. The upper layers used for discriminating between classes are trained by taking the weighted sum of the CE losses, i.e. the CE loss for each deep feature target.

The deep over-sampling component is the process of selecting k in-class neigh- bors from deep feature space. In order to address class imbalance, the number of in- class neighbors to select should vary between classes. For example, using k = 3 for the

Table 14 DOS with varying imbalance [117]

Model Reduction rate Class MNIST MNISTbr SVHN

Pr Re F1 AUC​ Pr Re F1 AUC​ Pr Re F1 AUC​

CNN 0.90 mnr 0.98 0.93 0.96 0.99 0.31 0.76 0.43 0.68 0.62 0.77 0.55 0.78

mjr 0.96 0.99 0.97 1.00 0.77 0.56 0.65 0.77 0.80 0.76 0.75 0.89

0.95 mnr 0.99 0.89 0.94 0.99 0.27 0.76 0.23 0.57 0.13 0.86 0.21 0.61

mjr 0.93 0.98 0.95 0.99 0.52 0.69 0.58 0.67 0.89 0.61 0.71 0.87

0.99 mnr 0.65 0.98 0.77 0.96 0.31 0.71 0.43 0.68 0.50 0.72 0.42 0.74

mjr 0.99 0.82 0.89 0.99 0.78 0.56 0.65 0.77 0.73 0.67 0.60 0.81

[p. 39] [ref: 0.95]

CNN-CL 0.90 mnr 0.99 0.90 0.94 1.00 0.22 0.77 0.31 0.69 0.59 0.60 0.42 0.78

mjr 0.94 0.99 0.96 0.98 0.78 0.53 0.63 0.78 0.77 0.75 0.73 0.86

0.95 mnr 0.99 0.83 0.90 0.97 0.28 0.77 0.24 0.60 0.04 0.68 0.07 0.61

mjr 0.89 0.99 0.94 1.00 0.52 0.68 0.57 0.69 0.89 0.60 0.70 0.84

0.99 mnr 0.75 0.98 0.85 0.95 0.22 0.72 0.31 0.69 0.47 0.71 0.37 0.72

mjr 0.99 0.86 0.92 0.99 0.78 0.53 0.63 0.78 0.71 0.57 0.56 0.78

0.90 mnr 0.99 0.97 0.98 1.00 0.66 0.77 0.71 0.79 0.71 0.82 0.72 0.84

DOS (k = 5)

mjr 0.98 0.99 0.98 1.00 0.75 0.68 0.71 0.81 0.85 0.79 0.81 0.92

0.95 mnr 0.98 0.96 0.97 1.00 0.56 0.75 0.63 0.72 0.40 0.89 0.55 0.73

mjr 0.97 0.99 0.98 1.00 0.64 0.74 0.69 0.78 0.90 0.69 0.78 0.91

0.99 mnr 0.91 0.99 0.95 0.99 0.61 0.73 0.66 0.75 0.51 0.91 0.64 0.80

mjr 0.98 0.94 0.96 1.00 0.77 0.70 0.73 0.82 0.89 0.68 0.77 0.90

Table 15 DOS with varying k [117]

Classifier k Class MNIST MNISTbr SVHN

Pr Re F1 AUC​ Pr Re F1 AUC​ Pr Re F1 AUC​

CNN mnr 0.65 0.98 0.77 0.96 0.31 0.76 0.43 0.68 0.50 0.72 0.42 0.74

mjr 0.99 0.82 0.89 0.99 0.78 0.56 0.65 0.77 0.73 0.67 0.60 0.81

CNN-CL mnr 0.75 0.98 0.85 0.95 0.22 0.77 0.31 0.69 0.47 0.71 0.37 0.72

mjr 0.99 0.86 0.92 0.99 0.78 0.53 0.63 0.78 0.71 0.57 0.56 0.78

DOS 3 mnr 0.91 0.98 0.95 0.99 0.65 0.77 0.70 0.78 0.67 0.77 0.66 0.83

mjr 0.99 0.94 0.96 1.00 0.75 0.68 0.71 0.80 0.80 0.74 0.74 0.86

5 mnr 0.91 0.99 0.95 0.99 0.66 0.77 0.71 0.79 0.51 0.91 0.64 0.80

mjr 0.98 0.94 0.96 1.00 0.75 0.68 0.71 0.81 0.89 0.68 0.77 0.90

10 mnr 0.91 0.99 0.95 0.99 0.61 0.73 0.66 0.75 0.40 0.89 0.55 0.73

[pp. 39-40]

mjr 0.99 0.94 0.96 1.00 0.77 0.70 0.73 0.82 0.90 0.69 0.78 0.91

minority class, and k = 0 for the majority class, will supplement the minority class with additional embeddings while leaving the majority class as is.

In the first DOS experiment, they compare the DOS framework with two alternative methods for handling class imbalance, Large Margin Local Embedding (LMLE) [22] and Triplet re-sampling with cost-sensitive learning (TL-RS-CSL). MNIST back-rotation images were used to create three data sets with class reduction rates of 0%, 20%, and 40%. It was shown that the DOS framework outperformed TL-RS-CSL and LMLE for reduction rates of 20% and 40%, and that DOS performance deteriorates slower than both TL-RS-CSL and LMLE as imbalance levels increase. For example, on imbalanced MNIST-back-rot data (40% reduction), DOS scored an average class-wise recall of 75.43, compared to the LMLE score of 70.13.

In a second experiment, the DOS framework is compared to a basic CNN and a K-NN classifier that is trained with CNN deep features (CNN-CL). Three different data sets are used to generate imbalanced data sets with reduction rates of 90%, 95%, and 99%, producing imbalance ratios up to ρ = 100 . The results in Table 14 show again that the improved performance of the DOS framework becomes more apparent as the level of class imbalance increases. The third level of imbalance, with reduction rates of 99%, show that the DOS framework clearly outperforms both the CNN and CNN-CL across all data sets and all performance metrics.

The final experiment uses balanced data sets to examine the sensitivity of DOS param- eter k, which defines the number of deep feature in-class neighbors to sample. Table 15 shows that when k is increased to 10 the performance on the minority group begins to deteriorate. These results also show that the proposed DOS framework outperforms the baseline CNN and CNN-CL on balanced data sets.

[pp. 40-41]

The DOS method displayed no visible performance trade-offs between the majority and minority groups, or between precision and recall. Its ability to outperform alterna- tive methods when class imbalance is not present is also very appealing, as this qual- ity is not common among class imbalance learning methods. Most importantly, some of the performance gains observed when comparing the CNN or CNN-CL to the DOS model on the minority group were very large, e.g. MNIST-back-rot and SVHN F1-scores increasing from 0.43 to 0.66 and 0.42 to 0.64, respectively, under an imbalance reduc- tion rate of 99%. Like other hybrid methods, DOS is more complex than more common data-level and algorithm-level methods, which may discourage statisticians from using it. We agree with Ando and Huang, however, that the DOS method is generally extend- able to other domains and deep learning architectures. Future works should evaluate the DOS method in these new contexts and should compare results to other class imbalance methods presented throughout this survey.

Class rectification loss (CRL) and hard sample mining Dong et al. [118] present an end-to-end deep learning method for addressing high class imbalance in large-scale image classification. They explicitly distinguish their work from more traditional small-scale class imbalance problems containing small levels of imbalance, suggesting that this method may not generalize to small-scale problems. Experimental results compare the proposed method against data sampling, cost-sen- sitive learning, threshold moving, and several relevant state-of-the-art methods. Mean sensitivity scores are used as the primary performance metric by averaging together class-wise recall scores. The proposed method combines hard sample mining from the minority groups with a regularized objective function, the class rectification loss (CRL).

The hard sample mining selects minority samples which are expected to be more informative for each mini-batch, allowing the model to learn more effectively with less data. Dong et al. strive to rectify, or correct, the class distribution bias in an incremental manner, resulting in progressively stronger minority class discrimination through train- ing. Unlike LMLE [22], which attempts to strengthen the structure of both majority and minority groups, this method only enhances minority class discrimination. To identify the minority classes, all classes are sorted by their size and then selected from smallest to largest until they collectively sum up to at most half the size of the data set, ensuring

beard Bangs

earings No

hair Mustache Bald Mean

under eyes Wear

skin Gray

hair Bags

chin Pale

hair Brown

hat Double

nose Young Straight

lips Big

hair Big

eyebrows Black

nose Arched

cheeks Goatee Chubby Sideburns Blurry Wear

face Pointy

hair Oval

makeup Wavy

necktie Eyeglasses Rosy

hairline Wear

cheekbones Male Heavy

lipstick High

eyes 5 o’clock shadow Receding

necklace Narrow

open Smiling Wear

eyebrows Wear


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
