---
type: Source Digest
title: A Survey of Predictive Modelling under Imbalanced Distributions - part 2 of 5 (pp. 14-23)
description: 'Verified paraphrased digest, pp. 14-23: A Survey of Predictive Modelling under Imbalanced Distributions > 4 Modelling Strategies for Handling Imbalanced Domains'
resource: https://arxiv.org/abs/1505.01658
tags:
- academic_finding
- fraud_screening_synergies
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-a-survey-of-predictive-modelling-under-imbalanced-distributions
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2015-05-07'
legal_status: unknown
part: 2
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1505.01658
  title: A Survey of Predictive Modelling under Imbalanced Distributions
  author: org:arxiv
  last_modified: '2015-05-07T00:00:00Z'
digest_points: 61
---

# A Survey of Predictive Modelling under Imbalanced Distributions (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 14-23) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.1 Data Pre-processing

- **descriptive / context**: Pre-processing strategies use the available data set in a way more in accordance with user preference biases; a standard learning algorithm is then applied to the pre-processed data set rather than the raw training data. (p. 14)[^original]  
  <sub>anchor: "Any standard learning algorithm can be applied to the pre-processed data set."</sub>
- **descriptive / definition**: The survey groups data pre-processing approaches into three main types: re-sampling, active learning, and weighting the data space. (p. 14)[^original]  
  <sub>anchor: "Existing data pre-processing approaches can be grouped into three main types:"</sub>
- **descriptive / definition**: Re-sampling changes the data distribution so that the learner focuses on the least represented examples. (p. 14)[^original]  
  <sub>anchor: "change the data distribution of the data set forcing the learner to focus on the least represented examples"</sub>
- **descriptive / definition**: Active learning selects the most valuable samples to learn from, leaving those with less information to improve learner performance. (p. 14)[^original]  
  <sub>anchor: "actively selecting the best (more valuable) samples to learn, leaving the ones with less information"</sub>
- **descriptive / definition**: Weighting the data space modifies the training distribution using misclassification cost information so the learned model avoids costly errors. (p. 14)[^original]  
  <sub>anchor: "modify the training set distribution using information concerning misclassification costs"</sub>
- **descriptive / finding or result**: Applying re-sampling to obtain a more balanced distribution is described as an effective solution to the imbalance problem, citing Estabrooks et al. 2004, Batuwita and Palade 2010a, and Fernández et al. 2008, 2010. (p. 14)[^original]  
  <sub>anchor: "Applying re-sampling strategies to obtain a more balanced data distribution is an effective solution to the imbalance problem"</sub>
- **descriptive / context**: Table 3 summarises the main bibliographic references for data pre-processing strategy types: re-sampling (with sub-types random under/over-sampling, distance based, data cleaning based, recognition based, cluster based, synthesising new data, adaptive synthetic sampling, evolutionary sampling, and re-sampling combinations), active learning (Ertekin et al. 2007a,b; Zhu and Hovy 2007; Ertekin 2013; Mi 2013), and weighting the data space (Zadrozny et al. 2003; Wang and Japkowicz 2010). (p. 15)[^original]  
  <sub>anchor: "Table 3 summarizes the main bibliographic references for data pre-processing strategies."</sub>
- **descriptive / limitation**: Changing the data distribution is not as easy as expected: the optimal distribution is a domain-dependent decision and is not straightforward to determine. (p. 15)[^original]  
  <sub>anchor: "Decide what is the optimal distribution is not straightforward as it is a domain dependent decision."</sub>
- **descriptive / finding or result**: Weiss and Provost (2003) proved for classification tasks that a perfectly balanced distribution does not always give optimal results; later work (Weiss and Provost 2003; Chawla et al. 2005, 2008) proposed ways to find the right amount of re-sampling. (p. 15)[^original]  
  <sub>anchor: "it was proved for classification tasks that a perfectly balanced distribution does not always provide optimal results"</sub>
- **descriptive / finding or result**: For classification, changing the class distribution of training data improves classifier performance on imbalanced data because it imposes non-uniform misclassification costs; this equivalence was first pointed out by Breiman et al. (1984). (p. 15)[^original]  
  <sub>anchor: "This equivalence between the two concepts of altering the data distribution and the misclassification cost ratio is well-known"</sub>

## 4.1.1 Re-sampling

- **descriptive / definition**: Random under-sampling discards a random set of majority class examples, which may eliminate useful examples and worsen performance. (p. 16)[^original]  
  <sub>anchor: "In random under-sampling, a random set of majority class examples are discarded."</sub>
- **descriptive / finding or result**: Random under-sampling was combined with boosting (Seiffert et al. 2010), bagging (Wang and Yao 2009; Chang et al. 2003; Tao et al. 2006), and applied to both classes in random forests as Balanced Random Forest (BRF) (Chen et al. 2004). (p. 16)[^original]  
  <sub>anchor: "was applied to both classes in random forests in a method named Balanced Random Forest (BRF)"</sub>
- **descriptive / method**: For regression, Torgo et al. (2013) perform random under-sampling of common values using a relevance function and a user-defined threshold to identify common, uninteresting values to under-sample. (p. 16)[^original]  
  <sub>anchor: "This method uses a relevance function and an user defined threshold to determine which are the common and uninteresting values"</sub>
- **descriptive / method**: Distance-based under-sampling (Chyi 2003; Mani and Zhang 2003) keeps majority examples chosen by a distance criterion; these strategies are very time consuming, a major disadvantage especially for large data sets. (p. 16)[^original]  
  <sub>anchor: "These strategies are very time consuming which is a major disadvantage, specially"</sub>
- **permissive / limitation**: Random over-sampling may increase the likelihood of overfitting, especially at higher over-sampling rates. (p. 16)[^original]  
  <sub>anchor: "This may increase the likelihood of overfitting, specially for higher over-sampling rates"</sub>
- **permissive / limitation**: Random over-sampling may also decrease classifier performance and may increase the computational effort. (p. 16)[^original]  
  <sub>anchor: "Moreover, it may decrease the classifier performance and increase the computational effort."</sub>
- **descriptive / method**: Data cleaning methods identify possibly noisy examples or overlapping regions and decide on their removal to under-sample. (p. 17)[^original]  
  <sub>anchor: "The main goal of these methods is to identify possibly noisy examples or overlapping regions and then decide on the removal of examples."</sub>
- **descriptive / definition**: Tomek links are pairs of points that are each other's closest neighbours but have different class labels; removal can be restricted to majority-class links or applied to both classes (Batista et al. 2004). (p. 17)[^original]  
  <sub>anchor: "consist of points that are each other’s closest neighbours, but do not share the same class label"</sub>
- **descriptive / definition**: Condensed Nearest Neighbour (CNN) finds a subset of examples consistent with the training set, i.e. one that correctly classifies the training examples with a 1-nearest neighbour classifier. (p. 17)[^original]  
  <sub>anchor: "a subset that correctly classifies the training examples using a 1-nearest neighbour classifier"</sub>
- **descriptive / method**: Kubat and Matwin (1997) combined CNN and Tomek links in that order as One-Sided-Selection (OSS); Batista et al. (2004) used the reverse order. (p. 17)[^original]  
  <sub>anchor: "CNN and Tomek links methods were combined in this order by Kubat and Matwin (1997) in a strategy called One-Sided-Selection (OSS)"</sub>
- **descriptive / definition**: Recognition-based methods such as one-class learning or autoencoders perform the most extreme under-sampling, removing all majority class examples and learning only from the target class. (p. 18)[^original]  
  <sub>anchor: "Recognition-based methods as one-class learning or autoencoders offer the possibility to perform the most extreme type of under-sampling"</sub>
- **descriptive / definition**: The key distinguishing feature between recognition-based and discrimination-based learning is the absence of counter examples from other classes. (p. 18)[^original]  
  <sub>anchor: "This lack of examples from the other class(es) is the key distinguishing feature"</sub>
- **descriptive / limitation**: One-class learning requires tuning a similarity threshold: too narrow a threshold disregards minority examples, too wide a threshold may include majority examples, so establishing an efficient threshold is vital; some learners need examples from more than one class and cannot adapt. (p. 18)[^original]  
  <sub>anchor: "One-class learning methods have the disadvantage of requiring the tuning of the threshold imposed on the similarity."</sub>
- **descriptive / finding or result**: Recognition-based learning algorithms have been shown to provide good prediction performance in most domains despite their disadvantages. (p. 18)[^original]  
  <sub>anchor: "recognition-based learning algorithms have been proved to provide good prediction performance in most domains"</sub>
- **descriptive / method**: Developments in recognition-based methods include one-class SVMs (Schölkopf et al. 2001; Manevitz and Yousef 2002; Raskutti and Kowalczyk 2004; Zhuang and Dai 2006a,b; Lee and Cho 2006) and autoencoders or autoassociators (Japkowicz et al. 1995; Japkowicz 2000). (p. 18)[^original]  
  <sub>anchor: "Developments made in this context include one-class SVMs"</sub>
- **descriptive / finding or result**: Bellinger et al. (2012) found that as imbalance increased, binary classifiers' performance decreased while one-class classifiers' performance stayed relatively stable, on both artificial and real-world data sets. (p. 18)[^original]  
  <sub>anchor: "as the level of imbalance increased, the performance of binary classifiers decreased, whereas the performance of one-class classifiers stayed relatively stable"</sub>
- **descriptive / context**: Imbalanced domains can influence the performance and efficiency of clustering algorithms (Xuan et al. 2013), but clustering flexibility has led to several approaches for imbalanced data. (p. 18)[^original]  
  <sub>anchor: "Imbalanced domains can influence the performance and the efficiency of clustering algorithms"</sub>
- **descriptive / definition**: Small disjuncts are subclusters of a class with low coverage, i.e. classifying only few examples (Holte et al. 1989). (p. 18)[^original]  
  <sub>anchor: "Small disjuncts are subclusters of a certain class which have a low coverage, i.e., classify only few examples"</sub>
- **descriptive / method**: Cluster-based oversampling (CBO) by Jo and Japkowicz (2004) addresses imbalance and small disjuncts by clustering each class separately with k-means and randomly over-sampling each cluster, bringing majority clusters up to the size of the largest majority cluster and then balancing minority subclusters. (p. 18)[^original]  
  <sub>anchor: "CBO consists of clustering the training data of each class separately with the k-means technique"</sub>
- **descriptive / context**: Other clustering-based proposals include Yen and Lee (2006, 2009) and Cohen et al. (2006). (p. 18)[^original]  
  <sub>anchor: "Several other proposals based on clustering techniques exist"</sub>
- **descriptive / finding or result**: Synthesising new data reduces the overfitting risk introduced by replicated examples and improves generalisation compromised by over-sampling, according to Chawla et al. (2002) and Menardi and Torelli (2010). (p. 18)[^original]  
  <sub>anchor: "reduces the risk of overfitting which is introduced when replicas of the examples are inserted in the training set"</sub>
- **descriptive / method**: Synthetic data methods fall into two groups: those using interpolation of existing examples and those introducing perturbations. (p. 18)[^original]  
  <sub>anchor: "one that uses interpolation of existing examples, and (ii) another that introduces perturbations"</sub>
- **descriptive / method**: SMOTE over-samples the minority class by generating synthetic examples along the line segment joining a seed example and one of its k minority class nearest neighbours; k is a user-defined parameter and each minority example generates examples according to a predefined over-sampling percentage. (p. 18)[^original]  
  <sub>anchor: "introduces a new example along the line segment joining a seed example"</sub>
- **descriptive / method**: SMOTE is combined with a certain percentage of random under-sampling of the majority class, where that percentage depends on a user-defined parameter. (p. 18)[^original]  
  <sub>anchor: "This technique is then combined with a certain percentage of random undersampling of the majority class"</sub>
- **descriptive / finding or result**: SMOTE was integrated with boosting (Chawla et al. 2003) and bagging (Wang and Yao 2009). (p. 19)[^original]  
  <sub>anchor: "SMOTE algorithm has been applied with several different classifiers and was also integrated with boosting"</sub>
- **descriptive / limitation**: SMOTE generates positive-labelled synthetic examples without regard to negative examples, which may lead to overgeneralisation; this is especially problematic for highly skewed distributions where minority examples are sparse, causing greater class mixture. (p. 19)[^original]  
  <sub>anchor: "SMOTE generates synthetic examples with the positive class label disregarding the negative class examples"</sub>
- **descriptive / method**: Lee (1999) proposed oversampling that produces noisy replicates of rare cases by adding normally distributed noise to minority examples, keeping the majority class unchanged; Lee (2000) generated multiple noisy training versions and averaged the model estimates. (p. 19)[^original]  
  <sub>anchor: "The synthetic examples are generated by adding normally distributed noise to the minority class examples."</sub>
- **descriptive / method**: ROSE (Random Over Sampling Examples), by Menardi and Torelli (2010), uses smoothed bootstrap re-sampling, combining over- and under-sampling; observations are drawn with equal probability for both classes and new examples are generated in their neighbourhood using a width set by a smoothing matrix. (p. 19)[^original]  
  <sub>anchor: "ROSE generates a more balanced and completely new data set from the given training set combining over- and under-sampling"</sub>
- **descriptive / method**: For regression, Torgo et al. (2013) adapted SMOTE, adapting three components: defining relevant and normal cases via a relevance function and user threshold (DR and DN sets), generating synthetic examples by SMOTE's interpolation, and setting the target value as a distance-inverse weighted average of the two seed examples' target values. (p. 19)[^original]  
  <sub>anchor: "Three key components of the SMOTE algorithm required adaptation for regression"</sub>
- **descriptive / context**: For regression, only one method for generating new synthetic data was proposed in the surveyed literature, the Torgo et al. (2013) SMOTE adaptation. (p. 19)[^original]  
  <sub>anchor: "for regression problems only one method for generating new synthetic data was proposed"</sub>
- **descriptive / typology or red flag**: Three main types of SMOTE variants are identified: pre- or post-processing around SMOTE; applying SMOTE only in selected regions of the input space; and small modifications to the SMOTE algorithm. (p. 20)[^original]  
  <sub>anchor: "We can identify three main types of SMOTE variants"</sub>
- **descriptive / method**: Post-processing SMOTE variants include SMOTE+Tomek, SMOTE+ENN (Batista et al. 2004), SMOTE+FRST (Ramentol et al. 2012b) and SMOTE+RSB (Ramentol et al. 2012a); FRIPS (Verbiest et al. 2012) is an exception that pre-processes data before SMOTE. (p. 20)[^original]  
  <sub>anchor: "An exception is the Fuzzy Rough Imbalanced Prototype Selection (FRIPS) (Verbiest et al., 2012) method"</sub>
- **descriptive / method**: Second-type SMOTE variants generate synthetic examples only in regions considered useful, focusing on class borders or on hard-to-learn instances; examples include Borderline-SMOTE, ADASYN, MSMOTE, MWMOTE and FSMOTE. (p. 20)[^original]  
  <sub>anchor: "Some of these variants focus the synthesising effort on the borders between classes"</sub>
- **descriptive / method**: Third-type SMOTE variants modify how synthetic examples are generated, placing them closer or further from a seed depending on a measure; examples include Safe-Level-SMOTE, Safe Level Graph, LN-SMOTE and DBSMOTE. (p. 20)[^original]  
  <sub>anchor: "the synthetic examples may be generated closer or further apart from a seed depending on some measure"</sub>
- **descriptive / method**: Evolutionary Algorithms began to be applied to imbalanced domains as a strategy for under-sampling through prototype selection (e.g. Garcia et al. 2006a; Garcia and Herrera 2009). (p. 20)[^original]  
  <sub>anchor: "as a strategy to perform under-sampling through a prototype selection (PS) procedure"</sub>
- **descriptive / method**: Garcia et al. (2006a) proposed an evolutionary method for balancing data sets with a new fitness function designed for prototype selection. (p. 21)[^original]  
  <sub>anchor: "The method presented uses a new fitness function designed to perform a prototype selection process"</sub>
- **descriptive / method**: Genetic Algorithms combined with clustering performed both under- and over-sampling (Maheshwari et al. 2011; Yong 2012); evolutionary under-sampling was combined with boosting (Galar et al. 2013). (p. 21)[^original]  
  <sub>anchor: "Genetic Algorithms (GA) and clustering techniques were combined to perform both under and over-sampling"</sub>
- **descriptive / method**: Jeatrakul et al. (2010) use Complementary Neural Networks (CMTNN) for under-sampling combined with SMOTE. (p. 21)[^original]  
  <sub>anchor: "uses Complementary Neural Networks (CMTNN) to perform under-sampling and combines it with SMOTE"</sub>
- **descriptive / method**: EnSVM (Liu et al. 2006) rebalances by combining SMOTE over-sampling and under-sampling to form new training sets while using all positive examples, then builds an ensemble of SVMs. (p. 21)[^original]  
  <sub>anchor: "adopts a rebalance strategy combining the over-sampling strategy of SMOTE algorithm and under-sampling"</sub>
- **descriptive / context**: Ensembles have been adapted and combined with re-sampling for imbalanced domains across all ensemble types; a fuller review is given in Galar et al. (2012). (p. 21)[^original]  
  <sub>anchor: "Essentially, for every type of ensembles, some attempt has been made"</sub>

## 4.1.2 Active Learning

- **descriptive / definition**: Active learning is a semi-supervised strategy in which the learner interactively obtains information from the user; it is traditionally used with unlabelled data but can also be applied when all labels are known, to select the most informative examples. (p. 21)[^original]  
  <sub>anchor: "Although this method is traditionally used with unlabelled data, it can also be applied when all class labels are known"</sub>

## 4.1.1 Re-sampling

- **descriptive / method**: Kang and Cho (2006) present an ensemble of under-sampled SVMs in which multiple training sets combine sampled majority class examples with the minority class examples, each training set trains one SVM, and the individual outputs are aggregated. (p. 21)[^original]  
  <sub>anchor: "Multiple different training sets are built by sampling examplesfrom the majority class and combining them with the minority class examples"</sub>

## 4.1.2 Active Learning

- **descriptive / method**: Active learning approaches for imbalanced domains (Ertekin et al. 2007a,b; Zhu and Hovy 2007; Ertekin 2013) concentrate on SVM learners, where the most informative examples are those closest to the hyperplane, used to guide under-sampling. (p. 22)[^original]  
  <sub>anchor: "the most informative examples are the ones closest to the hyperplane"</sub>
- **descriptive / method**: VIRTUAL (Virtual Instances Resampling Technique Using Active Learning), by Ertekin (2013), is an adaptive over-sampling algorithm that generates minority synthetic examples during training, removing the need for a separate pre-processing step; with SVMs it outperforms competitive over-sampling techniques in generalisation performance and computational complexity. (p. 22)[^original]  
  <sub>anchor: "VIRTUAL generates synthetic examples for the minority class during the training pro-"</sub>
- **descriptive / method**: Mi (2013) developed a method combining SMOTE and active learning with SVMs. (p. 22)[^original]  
  <sub>anchor: "Mi (2013) developed a method that combines SMOTE and active learning with SVMs."</sub>
- **descriptive / method**: Hu (2012) proposed an active learning method for imbalanced data using the Localized Generalization Error Model (L-GEM) of radial basis function neural networks. (p. 22)[^original]  
  <sub>anchor: "Hu (2012) proposed an active learning method for imbalance data using the Localized Generalization Error Model"</sub>

## 4.1.3 Weighting the Data Space

- **descriptive / method**: Weighting the data space implements cost-sensitive learning by multiplying each case by a factor proportional to its importance (relative cost), letting any standard learner minimise expected cost on the original distribution; drawbacks include risk of overfitting and possible unavailability of real cost values. (p. 22)[^original]  
  <sub>anchor: "changing the original sampling distribution by multiplying each case by a factor that is proportional to its importance"</sub>
- **descriptive / method**: Zadrozny et al. (2003) built on a Translation Theorem and gave two ways to convert costs: a transparent box approach (weights given to the classifier, which cannot apply to arbitrary learners) and a black box approach (subsampling by weights, which overfits severely with replacement). (p. 22)[^original]  
  <sub>anchor: "The first approach cannot be applied to an arbitrary learner, while the second one results in severe overfitting"</sub>
- **descriptive / method**: Cost-proportionate rejection sampling, proposed by Zadrozny et al. (2003), accepts each input example with probability proportional to its associated weight. (p. 22)[^original]  
  <sub>anchor: "accepts each example in the input sample with probability proportional to its associated weight"</sub>
- **descriptive / method**: Wang and Japkowicz (2010) propose an ensemble of SVMs with asymmetric misclassification costs, modifying the SVM base classifier with costs and using boosting as the combination scheme. (p. 22)[^original]  
  <sub>anchor: "The proposed system works by modifying the base classifier (SVM) using costs and uses boosting as the combination scheme."</sub>

## 4.2 Special-purpose Learning Methods

- **descriptive / context**: Table 4 lists the main bibliographic references for special-purpose learning methods (section 4.2), including works by Maloof (2003), Akbani et al. (2004), Tang et al. (2009), Zhou and Liu (2006), Sun et al. (2007), Joshi et al. (2001), Wu and Chang (2003, 2005), Imam et al. (2006), Barandela et al. (2003), Cieslak and Chawla (2008), Torgo and Ribeiro (2003) and others. (p. 23)[^original]  
  <sub>anchor: "Table 4: Special-purpose Learning Methods, corresponding section and main bibliographic references"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Paula Branco, Luı́s Torgo, Rita P. Ribeiro, "A Survey of Predictive Modelling under Imbalanced Distributions" (2015-05-07). https://arxiv.org/abs/1505.01658
