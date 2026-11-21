---
type: Source Text
title: Survey on deep learning with class imbalance - part 5 of 9 (pp. 29-34)
description: 'Verbatim extracted text, pp. 29-34: RUS (%) SMOTE; SOSR CNN (%)'
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
part: 5
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

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 5 of 9, pp. 29-34. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## RUS (%) SMOTE


[p. 29] [ref: 94.5]

Dataset Imbalance protocol

CoSen RF (%)

Baseline CNN (%)

CoSen SVM (%)

CoSen CNN (%)

94.5 92.1 96.0 96.8 96.3 97.8 97.6 98.6

MNIST 10% of odd classes

32.2 28.8 37.5 39.9 39.0 55.8 55.0 60.1

CIFAR-100 10% of odd classes

67.7 61.4 68.2 70.1 68.7 77.4 77.4 83.2

## SOSR CNN (%)


[pp. 29-30] [ref: 33.9]

Caltech-101 10% of odd classes

33.9 28.4 34.0 35.5 35.2 49.8 50.4 56.9

MIT-67 10% of odd classes

DIL Standard

50.3 46.7 52.6 55.3 54.7 68.9 69.5 72.6

split

MLC Standard

38.9 31.4 43.0 47.7 46.5 65.7 66.1 68.6

split

Italic scores indicate the top performance for each data set

The CoSen CNN is evaluated against the baseline CNN, multiple sampling meth- ods, and multiple cost-sensitive methods. A two-layered neural network was used for the sampling classification methods, and a SVM and RF were used for the cost-sensitive methods. The SVM and RF baseline classifiers used the features that were extracted by the pre-trained VGG-16 CNN as input. The SOSR CNN is a cost-sensitive deep learning method that incorporates a fixed cost matrix into the loss function [108].

Overall accuracy was used to show that the proposed CNN outperforms all seven alternative techniques across all data sets. Table 10 shows that the CoSen CNN per- formed exceptionally well, outperforming the runner-up classifier by more than 5% on CIFAR-100, Caltech-101, and MIT-67. The second best classifier listed in the experi- mental results is between the SOSR CNN and the baseline CNN. In all cases SMOTE outperformed RUS, and hybrid sampling method SMOTE-RSB [109] outperformed SMOTE. Unfortunately, with accuracy being the only performance metric reported between all seven class imbalance methods, and accuracy being unreliable in cases of class imbalance, these results may be misleading.

F1 and G-Mean scores were reported to show that the proposed CoSen CNN out- performs the baseline CNN on all data sets, e.g. increasing the F1-score from 0.389 to 0.416 on the Caltech-101 data set. Khan et al. also included sample network training times, showing that the added cost parameter training increases each training epoch by several seconds but has little to no impact on the inference step. In another experi- ment, the authors defined three fixed cost matrices using class representation, data separability, and classification errors to derive the costs, and showed that the dynamic cost matrix method outperforms all three cases.

[pp. 30-31]

It is interesting that the baseline CNN, with no class imbalance modifications, is a close runner-up to the CoSen CNN, outperforming the sampling methods, SVM, and RF classifiers in all cases. This does not imply that a deep CNN with no class imbalance modifications is better equipped to address class imbalance than tradi- tional sampling methods. Rather, this demonstrates the power of re-using strong fea- ture extractors that have been trained on large volumes of data, e.g. over 1.3 million images in this experiment.

As mentioned previously, one of the difficulties of cost-sensitive learning is choos- ing an appropriate cost matrix, often requiring a domain expert or a grid search pro- cedure. The CoSen method proposed by Khan et al. removes this requirement, and offers more of an end-to-end deep learning framework capable of learning from class imbalanced data. The authors report results on a number of experiments across a variety of data sets, and the joint learning of network parameters and cost parameters appears to be an excellent candidate for learning from class imbalanced data. Future experiments should explore this cost-sensitive method’s ability to learn from prob- lems containing alternative data types, big data, and class rarity.

Cost‑sensitive DBN with differential evolution (CSDBN‑DE) Zhang et al. [90] set out to automatically learn costs for the purpose of cost-sensitive deep learning. More specifically, they use a differential evolutionary algorithm [110] to improve the cost matrix each training iteration, and incorporate these learned costs into a DBN. The proposed cost-sensitive deep belief network with differential evolution

(CSDBN-DE) is evaluated against 42 data sets from the Knowledge Extraction based on Evolutionary Learning (KEEL) [111] repository. The training data sets are structured data sets, ranging in size from 171 samples to 3339 samples and containing between 6 and 13 attributes each. Imbalance ratios range from ρ = 9.28 up to ρ = 128.21.

The DBN pre-training phase follows the original layer-wise training method first pro- posed by Hinton et al. [65]. The cost matrix is then incorporated into the output layer’s softmax probabilities during the fine-tuning phase. Cost matrices are first randomly ini- tialized, then training set evaluation scores are used to select a new cost matrix for the next population. Mutation and cross-over operations are applied to evolve and generate the next population of cost matrices. Once training is complete, the best cost matrix is selected and applied to the output layer of the DBN, forming the final version of the cost-sensitive DBN to be used for inference.

[pp. 31-32]

Accuracy and error rate are used to compare the proposed method to an extreme learning machine (ELM) [112]. The ELM network is a type of single-hidden layer feed- forward network that does not use backpropagation and is known to train thousands of times faster than neural networks. Experiments are repeated 20 times and results are averaged. The proposed CSDBN-DE model outperformed the ELM network on 28 out of 42 data sets, i.e. 66% of the experiments. Similar to the CoSen CNN [19], the biggest advantage of the CSDBN-DE is its ability to learn an effective cost matrix throughout training, as this is often a difficult and time- consuming process. Unfortunately, it is not very clear how well the CSDBN-DE handles class imbalanced data, because it is compared to a single baseline built on a completely different architecture. Also, the accuracy performance metric provides no real insight into the network’s true performance when class imbalance is present. The concept of incorporating an evolutionary algorithm to iteratively update a cost matrix shows prom- ise, but more robust experiments are required to validate its ability to classify imbal- anced data.

Output thresholding In addition to the data sampling methods discussed in the "ROS, RUS, and two-phase learning" section, Buda et al. [23] experimented with adjusting CNN output thresholds to improve overall performance. They used the MNIST and CIFAR-10 data sets with varying levels of class imbalance ratios in the range of ρ ∈[1, 5000] and ρ ∈[1, 50] , respectively. Accuracy scores were used to compare thresholding with the baseline CNN, ROS, and RUS methods as they were described in the "ROS, RUS, and two-phase learning" section.

The authors applied thresholding by dividing the network outputs for each class by its estimated prior probability, effectively reducing the likelihood of misclassifying examples from the minority group. They also considered hybrid methods by combin- ing threshold moving with RUS and ROS. The thresholding method outperformed the baseline CNN for all levels of class imbalance on the MNIST and CIFAR-10 data sets. Thresholding outperformed ROS and RUS for all levels of imbalance on the MNIST data, but on the CIFAR-10 data there were several instances were ROS outperformed

thresholding. Thresholding combined with ROS performed especially well, outperform- ing all other methods in nearly all cases.

[p. 32]

As discussed in the "ROS, RUS, and two-phase learning" section, Buda et al. explored a variety of deep learning methods for addressing a wide range of class imbalance levels. They have shown that overall accuracy can be improved with threshold moving, and that it can be implemented relatively easily with prior class probabilities. Unfortunately, the accuracy score does not explain individual class-wise performances and trade-offs. Since thresholding is only applied during inference, it does not affect training times. This also means that thresholding does not impact weight tuning and therefore does not improve a model’s ability to discriminate between classes. Regardless, it is still an appropriate method for reducing majority class bias that can be quickly implemented on top of an already trained network to improve classification results.

Category centers Zhang et al. [91] experimented with deep representation learning of class imbalanced image data from the CIFAR-10 and CIFAR-100 data sets. They present a method for addressing class imbalance, category centers (CC), that combines transfer learning, deep CNN feature extraction, and a nearest neighbor discriminator. Three class imbalanced distributions are created from each original data set through random under-sampling, i.e. Dist. A, Dist. B, and Dist. C. In Dist. A and Dist. B, half of the classes are reduced in size, creating imbalance levels of ρ = 10 and ρ = 20 , respectively. In Dist. C, class reduc- tion levels increase linearly across all classes with a max imbalance of ρ = 20 . For exam- ple, Dist. C for the CIFAR-100 data set contains 25 images in each of the first 10 classes, 75 images in each of the next 10 classes, then 125 images in each of the next 10 classes, etc. The proposed model is compared to both a baseline CNN and an over-sampling method. The mean precision performance metric is used to compare results.

Zhang et al. observe that similar images of the same class tend to cluster well in CNN deep feature space. They discuss the decision boundary that is created by the final layer of the CNN, the classification layer responsible for separating these deep feature clus- ters, stating that there is a greater chance for large errors in boundary placement when class imbalance is present. To avoid this boundary error in scenarios of class imbalance, they propose using high-level features extracted by the CNN to calculate each class’s centroid in deep feature space. These category centers in deep feature space can then be used to classify new images, by assigning new images to their nearest deep feature

Table 11 Category centers with CIFAR-10 data (AP) [91]

Classifier Dist A ( ρ = 10) Dist B ( ρ = 20) Dist C ( ρ ∈[1, 20])

(A) Baseline CNN 0.779 0.747 0.857

[pp. 32-33]

(B) CC last conv. layer 0.824 0.775 0.859

(C) CC last FC layer 0.826 0.772 0.865

(D) Baseline CNN + over-sampling 0.787 0.770 0.850

(E) CC last conv. layer + over-sampling 0.831 0.792 0.861

(F) CC last FC layer + over-sampling 0.830 0.796 0.862

category center. The VGG-16 network, pre-trained on ImageNet data, is used through- out the experiments as the baseline CNN. The proposed method fine-tunes the CNN on the imbalanced distribution, maps all images to their corresponding deep feature repre- sentations, then calculates the centroid for each class. At test time the trained CNN is used to extract features from new images, and each new image is assigned to the class of its nearest category center in feature space, defined by the Euclidean distance between the features. Zhang et al. claim that the category center is significantly more stable than the boundary generated by a CNN’s classification layer, but no evidence was provided to support this.

A portion of Zhang et al.’s results are displayed in Table 11. The authors tried using two different CNN layers for feature extraction, the last convolutional layer (B) and the last fully connected layer (C), to determine if one set of features performed bet- ter. Finally, over-sampling was applied to the baseline and the category centers meth- ods to determine the impact of data sampling on CC (D–F). These results show that the CC methods (B, C) outperform the baseline CNN (A) on mean precision for all three imbalance scenarios. Results also show that the addition of over-sampling (D–F) led to improved results on the CIFAR-10 distributions, with the exception of Dist. C. For example, the CC method with over-sampling (E) increased mean precision on Dist. A from a baseline (A) of 0.779 to 0.830. CIFAR-100 results were similar, in the sense that the proposed method (B, C) outperformed the baseline (A) for all three distributions. Unlike the CIFAR-10 data, interestingly, over-sampling did not improve the results of the proposed method when classifying the CIFAR-100 distributions, but it did improve the baseline CNN.

[pp. 33-34]

We believe that the biggest limitation to the CC method is that it is highly dependent on the DNN’s ability to generate discriminative features that cluster well. If a large vol- ume of class balanced, labelled training data is not available to pre-train the DNN, deep feature boundaries may not be strong enough to apply the CC method. The specifics of the over-sampling method used in methods (D–F) are unknown, so we do not know if over-sampling was applied to a level of class balance or some other ratio. In addition, we do not know if these results are the average of several rounds of experiments, or are just results from a single instance. With no balanced distribution results, an unclear over- sampling method, and only one performance metric, it is difficult to understand how well the proposed CC method does in learning from class imbalance.

Very‑deep neural networks Ding et al. [92] experimented with very-deep CNN architectures, e.g. 50 layers, to deter- mine if deeper networks perform better on imbalanced data. The authors observe in literature that the error surfaces of deeper networks have better qualities for training convergence than smaller sized networks [113, 114]. They claim that larger networks contain more local minimum with good performance, making acceptable solutions eas- ier to locate with gradient descent. The networks are tested on the problem of Facial Action Units (FAUs) recognition, i.e. the detection of basic facial actions as defined by the Facial Action Coding System [115].

The EmotioNet Challenge Track 1 data set [116] is used to compare methods. From the original data set, with over one million images, 450,000 images were randomly selected

Table 12 Comparing very-deep CNNs on FAU recognition (F1-score) [92]

FAU class Imbalance level (A) Handcraft (B) Plain34 (C) Res10 (D) Res18 (E) Res34 (F) Res50


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
