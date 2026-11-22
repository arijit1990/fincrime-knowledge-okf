---
type: Source Digest
title: Precision–recall curve (PRC) classification trees - part 3 of 3 (pp. 16-19)
description: 'Verified paraphrased digest, pp. 16-19: 4 Experimental Studies > 4.2 Real-world data set experiment; 5 Conclusion; References'
resource: https://arxiv.org/abs/2011.07640
tags:
- academic_finding
- fraud_screening_synergies
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-precision-recall-curve-prc-classification-trees
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-04-13'
legal_status: unknown
part: 3
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2011.07640
  title: Precision–recall curve (PRC) classification trees
  author: org:arxiv
  last_modified: '2021-04-13T00:00:00Z'
digest_points: 44
---

# Precision–recall curve (PRC) classification trees (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 16-19) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2 Real-world data set experiment

- **descriptive / finding or result**: The real-world data set comparison is summarised in Tables 9 to 11, with the best performance shown in bold, the best tree model highlighted in green and the best non-tree model in blue. (p. 16)[^original]  
  <sub>anchor: "Then we experiment with real-world data sets and summarize the performance comparison in Tables 9 to 11."</sub>
- **descriptive / finding or result**: The real-world results are described as consistent with the out-of-bag error rate table. (p. 16)[^original]  
  <sub>anchor: "The results are quite consistent with the out-of-bag error rate table."</sub>
- **descriptive / finding or result**: The proposed algorithm can achieve higher recall and F1-score than traditional random forest in general. (p. 16)[^original]  
  <sub>anchor: "In general, the proposed algorithm can achieve higher recall and F1-score than traditional random forest."</sub>
- **descriptive / finding or result**: In the first data case, PRC random forest achieves the largest accuracy and F1-score, while PRC-ROC RF attains the highest precision. (p. 16)[^original]  
  <sub>anchor: "PRC random forest achieves the largest accuracy, F1-score and PRC-ROC attains the highest precision in the first case."</sub>
- **descriptive / finding or result**: Random forest achieves slightly higher specificity in the first case, but its recall and F1-score are much lower than those of PRC random forest and PRC-ROC RF. (p. 16)[^original]  
  <sub>anchor: "Despite random forest achieving a slightly higher specificity, the recall and F1-score are much lower than PRC random forest and PRC-ROC RF."</sub>
- **descriptive / finding or result**: In the Financial Distress Prediction Data, SVM tends to classify all cases as the majority class. (p. 16)[^original]  
  <sub>anchor: "In this distress data, SVM tends to classify all the cases as the majority class."</sub>
- **descriptive / finding or result**: Weighted RF performs well on precision and accuracy in the Financial Distress Prediction Data. (p. 16)[^original]  
  <sub>anchor: "Weighted RF did a good job in the performance of precision and accuracy."</sub>
- **descriptive / data or feature**: Table 10 reports recall, specificity, precision, accuracy and F1 score for twelve algorithms on the Financial Distress Prediction Data, including SVM, Neural Network, CART, Weighted CART, ROC Tree, PRC Tree, PRC-ROC Tree, RF, Weighted RF, ROC RF, PRC RF and PRC-ROC RF. (p. 16)[^original]  
  <sub>anchor: "Table 10: Summary of performance results for Financial Distress Prediction Data"</sub>
- **descriptive / finding or result**: In Table 10, SVM has recall 0.0000, specificity 1.0000, precision NaN, accuracy 0.9600 and F1 score NaN. (p. 16)[^original]  
  <sub>anchor: "|SVM|0.0000|1.0000|NaN|0.9600|NaN|"</sub>
- **descriptive / finding or result**: In Table 10, Neural Network has recall 0.3100, specificity 0.9774, precision 0.3514, accuracy 0.9528 and F1 score 0.3294. (p. 16)[^original]  
  <sub>anchor: "|Neural Network|0.3100|0.9774|0.3514|0.9528|0.3294|"</sub>
- **descriptive / finding or result**: In Table 10, CART has recall 0.1951, specificity 0.9830, precision 0.3077, accuracy 0.9537 and F1 score 0.2388. (p. 16)[^original]  
  <sub>anchor: "|CART|0.1951|0.9830|0.3077|0.9537|0.2388|"</sub>
- **descriptive / finding or result**: In Table 10, Weighted CART has recall 0.8049, specificity 0.8727, precision 0.1964, accuracy 0.8702 and F1 score 0.3158. (p. 16)[^original]  
  <sub>anchor: "|Weighted CART|0.8049|0.8727|0.1964|0.8702|0.3158|"</sub>
- **descriptive / finding or result**: In Table 10, ROC Tree has recall 0.0730, specificity 0.9906, precision 0.2308, accuracy 0.9564 and F1 score 0.1110. (p. 16)[^original]  
  <sub>anchor: "|ROC Tree|0.0730|0.9906|0.2308|0.9564|0.1110|"</sub>
- **descriptive / finding or result**: In Table 10, PRC Tree has recall 0.3902, specificity 0.9802, precision 0.4324, accuracy 0.9583 and F1 score 0.4102. (p. 16)[^original]  
  <sub>anchor: "|PRC Tree|0.3902|0.9802|0.4324|0.9583|0.4102|"</sub>
- **descriptive / finding or result**: In Table 10, PRC-ROC Tree has recall 0.2439, specificity 0.9934, precision 0.5882, accuracy 0.9655 and F1 score 0.3448. (p. 16)[^original]  
  <sub>anchor: "|PRC-ROC Tree|0.2439|0.9934|0.5882|0.9655|0.3448|"</sub>
- **descriptive / finding or result**: In Table 10, RF has recall 0.0244, specificity 0.9981, precision 0.3333, accuracy 0.9619 and F1 score 0.0455. (p. 16)[^original]  
  <sub>anchor: "|RF|0.0244|0.9981|0.3333|0.9619|0.0455|"</sub>
- **descriptive / finding or result**: In Table 10, Weighted RF has recall 0.1951, specificity 0.9953, precision 0.6154, accuracy 0.9655 and F1 score 0.2963. (p. 16)[^original]  
  <sub>anchor: "|Weighted RF|0.1951|0.9953|0.6154|0.9655|0.2963|"</sub>
- **descriptive / finding or result**: In Table 10, ROC RF has recall 0.9512, specificity 0.8021, precision 0.1566, accuracy 0.8076 and F1 score 0.2689. (p. 16)[^original]  
  <sub>anchor: "|ROC RF|0.9512|0.8021|0.1566|0.8076|0.2689|"</sub>
- **descriptive / finding or result**: In Table 10, PRC RF has recall 0.9024, specificity 0.8633, precision 0.2033, accuracy 0.8648 and F1 score 0.3318. (p. 16)[^original]  
  <sub>anchor: "|PRC RF|0.9024|0.8633|0.2033|0.8648|0.3318|"</sub>
- **descriptive / finding or result**: In Table 10, PRC-ROC RF has recall 0.9268, specificity 0.8681, precision 0.2135, accuracy 0.8702 and F1 score 0.3471. (p. 16)[^original]  
  <sub>anchor: "|PRC-ROC RF|0.9268|0.8681|0.2135|0.8702|0.3471|"</sub>
- **descriptive / finding or result**: The authors conclude that PRC Random Forest is superior to other algorithms, especially traditional random forest, in identifying the minority class, which they describe as the goal of imbalanced classification. (p. 17)[^original]  
  <sub>anchor: "To conclude, PRC Random Forest is superior to other algorithms especially traditional random forest in identifying the minority class"</sub>
- **descriptive / finding or result**: In the last two instances, PRC-ROC Random Forest has higher accuracy and F1-score than other algorithms, and PRC RF behaves close to it. (p. 17)[^original]  
  <sub>anchor: "In the last two instances, the PRC-ROC Random Forest has higher accuracy and F1-score compared to other algorithms"</sub>
- **descriptive / finding or result**: In Table 11 for the Breast Cancer Data, SVM and Neural Network have identical results: recall 0.9672, specificity 0.9909, precision 0.9833, accuracy 0.9616 and F1 score 0.9751. (p. 17)[^original]  
  <sub>anchor: "|SVM|0.9672|0.9909|0.9833|0.9616|0.9751|"</sub>
- **descriptive / finding or result**: In Table 11, CART has recall 0.9016, specificity 0.9909, precision 0.9821, accuracy 0.9591 and F1 score 0.9401. (p. 17)[^original]  
  <sub>anchor: "|CART|0.9016|0.9909|0.9821|0.9591|0.9401|"</sub>
- **descriptive / finding or result**: In Table 11, Weighted CART has recall 0.9344, specificity 0.9818, precision 0.9661, accuracy 0.9649 and F1 score 0.9500. (p. 17)[^original]  
  <sub>anchor: "|Weighted CART|0.9344|0.9818|0.9661|0.9649|0.9500|"</sub>
- **descriptive / finding or result**: In Table 11, ROC Tree has recall 0.8197, specificity 0.9909, precision 0.9804, accuracy 0.9298 and F1 score 0.8929. (p. 17)[^original]  
  <sub>anchor: "|ROC Tree|0.8197|0.9909|0.9804|0.9298|0.8929|"</sub>
- **descriptive / finding or result**: In Table 11, PRC Tree has recall 0.9180, specificity 0.9455, precision 0.9032, accuracy 0.9357 and F1 score 0.9105. (p. 17)[^original]  
  <sub>anchor: "|PRC Tree|0.9180|0.9455|0.9032|0.9357|0.9105|"</sub>
- **descriptive / finding or result**: In Table 11, PRC-ROC Tree has recall 0.9344, specificity 0.9818, precision 0.9661, accuracy 0.9649 and F1 score 0.9476. (p. 17)[^original]  
  <sub>anchor: "|PRC-ROC Tree|0.9344|0.9818|0.9661|0.9649|0.9476|"</sub>
- **descriptive / finding or result**: In Table 11, RF has recall 0.8689, specificity 0.9909, precision 0.9814, accuracy 0.9473 and F1 score 0.9217. (p. 17)[^original]  
  <sub>anchor: "|RF|0.8689|0.9909|0.9814|0.9473|0.9217|"</sub>
- **descriptive / finding or result**: In Table 11, Weighted RF has recall 0.9180, specificity 1.0000, precision 1.0000, accuracy 0.9707 and F1 score 0.9572. (p. 17)[^original]  
  <sub>anchor: "|Weighted RF|0.9180|1.0000|1.0000|0.9707|0.9572|"</sub>
- **descriptive / finding or result**: In Table 11, ROC RF has recall 0.8361, specificity 0.9099, precision 0.9808, accuracy 0.9357 and F1 score 0.9027. (p. 17)[^original]  
  <sub>anchor: "|ROC RF|0.8361|0.9099|0.9808|0.9357|0.9027|"</sub>
- **descriptive / finding or result**: In Table 11, PRC RF has recall 0.9836, specificity 0.9636, precision 0.9375, accuracy 0.9708 and F1 score 0.9600. (p. 17)[^original]  
  <sub>anchor: "|PRC RF|0.9836|0.9636|0.9375|0.9708|0.9600|"</sub>
- **descriptive / finding or result**: In Table 11, PRC-ROC RF has recall 0.9836, specificity 0.9727, precision 0.9524, accuracy 0.9766 and F1 score 0.9677. (p. 17)[^original]  
  <sub>anchor: "|PRC-ROC RF|0.9836|0.9727|0.9524|0.9766|0.9677|"</sub>
- **descriptive / finding or result**: PRC random forest and PRC-ROC RF achieve good performance in F1 score on average. (p. 17)[^original]  
  <sub>anchor: "forest and PRC-ROC RF achieve good performance in F1 score on average."</sub>

## 5 Conclusion

- **descriptive / finding or result**: Table 31 shows the F1-score performance of the proposed classifiers compared with other tree-based algorithms across all datasets. (p. 17)[^original]  
  <sub>anchor: "Table 31 shows the F1-score performance of the proposed classifiers against other tree-based algorithms in all datasets."</sub>
- **descriptive / finding or result**: The authors state that their methods are superior to other rivals for skewed classification problems. (p. 17)[^original]  
  <sub>anchor: "The results indicate that our methods are superior to other rivals for skewed classification problems."</sub>

## 4.2 Real-world data set experiment

- **descriptive / finding or result**: The authors conclude that PRC Random Forest is superior to other algorithms, especially traditional random forest, at identifying the minority class. (p. 17)[^original]  
  <sub>anchor: "PRC Random Forest is superior to other algorithms especially traditional random forest in identifying the minority class"</sub>
- **descriptive / finding or result**: In the financial distress data, SVM tends to classify all cases as the majority class. (p. 17)[^original]  
  <sub>anchor: "SVM tends to classify all the cases as the majority class."</sub>

## 5 Conclusion

- **descriptive / context**: The authors note that there are many other potential possibilities for classifying imbalanced data, which is gaining increasing attention in academia and industry. (p. 17)[^original]  
  <sub>anchor: "There are absolutely many other potential possibilities about classification of imbalanced data"</sub>
- **descriptive / definition**: The paper investigates the PRC classification tree for the class imbalance problem and extends it to a general PRC-ROC tree and random forest by adding a weight parameter that selects the best weighted combination of AUPRC and AUC from training data for each problem. (p. 18)[^original]  
  <sub>anchor: "We also extend this to the general PRC-ROC tree and random forest by setting an additional weight parameter"</sub>
- **descriptive / finding or result**: Four new tree-based algorithms are studied: PRC Tree, PRC RF, PRC-ROC Tree and PRC-ROC Tree RF, alongside several existing related algorithms. (p. 18)[^original]  
  <sub>anchor: "Four new tree-based algorithms (i.e., PRC Tree, PRC RF, PRC-ROC Tree and PRC-ROC Tree RF) are studied"</sub>
- **descriptive / limitation**: The current PRC tree/forest and PRC-ROC tree/forest are designed only for binary classification. (p. 18)[^original]  
  <sub>anchor: "Our current PRC tree/forest and PRC-ROC tree/forest are all designed for binary classifications."</sub>
- **expected / recommendation**: The authors state they will extend the methods to accommodate multiple-class classification. (p. 18)[^original]  
  <sub>anchor: "We shall extend them to accommodate multiple-class classifications arising naturally from many practical scenarios."</sub>
- **descriptive / limitation**: The experimental study did not consider interaction terms, so uncovering interaction effects within the PRC classification tree framework is named as a further task. (p. 18)[^original]  
  <sub>anchor: "In our experimental study, we do not consider the interaction term."</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: Jiaju Miao, Wei Zhu, "Precision–recall curve (PRC) classification trees" (2021-04-13). https://arxiv.org/abs/2011.07640
