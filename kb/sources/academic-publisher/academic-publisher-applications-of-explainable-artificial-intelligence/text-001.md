---
type: Source Text
title: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature - part 1 of 6 (pp. 1-10)
description: Verbatim extracted text, pp. 1-10
resource: https://link.springer.com/article/10.1007/s11301-023-00320-0
tags:
- academic_finding
- academic_paper
- explainability
- global_academic
- responsible_ai
status: stable
source_id: academic-publisher-applications-of-explainable-artificial-intelligence
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-02-28'
legal_status: unknown
part: 1
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:31:16Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:31:16Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s11301-023-00320-0
  title: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature
  author: org:academic_publisher
  last_modified: '2023-02-28T00:00:00Z'
---

# Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-02-28), part 1 of 6, pp. 1-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[pp. 1-2]

Management Review Quarterly (2024) 74:867–907 https://doi.org/10.1007/s11301-023-00320-0

Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature

Patrick Weber1 · K. Valerie Carl1 · Oliver Hinz1

Received: 16 November 2022 / Accepted: 13 January 2023 / Published online: 28 February 2023 © The Author(s) 2023

Abstract Digitalization and technologization affect numerous domains, promising advantages but also entailing risks. Hence, when decision-makers in highly-regulated domains like Finance implement these technological advances—especially Artificial Intelli- gence—regulators prescribe high levels of transparency, assuring the traceability of decisions for third parties. Explainable Artificial Intelligence (XAI) is of tremen- dous importance in this context. We provide an overview of current research on XAI in Finance with a systematic literature review screening 2,022 articles from lead- ing Finance, Information Systems, and Computer Science outlets. We identify a set of 60 relevant articles, classify them according to the used XAI methods and goals that they aim to achieve, and provide an overview of XAI methods used in different Finance areas. Areas like risk management, portfolio optimization, and applications around the stock market are well-researched, while anti-money laundering is under- studied. Researchers implement both transparent models and post-hoc explainabil- ity, while they recently favored the latter.

Keywords Explainable artificial intelligence · Finance · Systematic literature review · Machine learning · Review

JEL Classification G00 · L50

* Patrick Weber weber@wiwi.uni-frankfurt.de

K. Valerie Carl kcarl@wiwi.uni-frankfurt.de

Oliver Hinz ohinz@wiwi.uni-frankfurt.de

1 Chair of Information Systems and Information Management, Goethe University Frankfurt, Theodor‑W‑Adorno‑Platz 4, 60629 Frankfurt am Main, Germany

Vol.:(0123456789)

1 3

1 Introduction

[p. 2]

The Finance industry is under constant development, always using and adapting to new technological opportunities (Gimpel et al. 2018)—like Artificial Intelli- gence (AI) and Data Analytics—that shape private and working lives worldwide. Financial institutions benefit from technological advances, recently from AI deployment (Alt et al. 2018; Goodell et al. 2021): Due to their strong predictive performance, AI-based systems are becoming increasingly crucial for decision- making in various settings and offer a wide range of opportunities for companies to exploit the economic potential of augmentation (Collins et al. 2021). In line with this development, academia renewed its interest in researching the applica- tion of AI in the financial sector (Cao 2022; Padmanabhan et al. 2022). The appli- cation scenarios in the area of Finance are very diverse and have specific require- ments for implementing automated systems. However, they have in common that they illustrate resentment against the black-box nature of AI-based systems, thus limiting their widespread use and hampering exploiting their full potential. This is where Explainable Artificial Intelligence (XAI) methods can help to counteract these adoption and implementation hurdles and exploit automation’s full potential in regulated industries like Finance. Therefore, research on XAI in Finance gains interest (Adadi and Berrada 2018).

In general, XAI tries to mitigate the problem of non-transparency of AI and pro- vides explanations to make the inner workings of AI models interpretable and easy to understand, as AI-generated rules from data are often unintelligible for humans. This unintelligibility creates a barrier concerning explainability and ultimately hin- ders the practical deployment of AI models, especially in highly-regulated applica- tion domains like Finance. Thus, XAI is a driver of further AI usage and adoption (Adadi and Berrada 2018; Janiesch et al. 2021; Mirbabaie et al. 2021; Sigrist and Hirnschall 2019) in particular in these domains as it helps to mitigate the current black-box nature of AI-based systems, i.e., unobservable inner workings.

Therefore it is not surprising that technological development has already found its way into the Finance domain. There are multiple areas of Finance examining and the first already employing XAI techniques, including risk management and port- folio optimization. One application scenario within risk management, which refers to a state of corporate failure (Sigrist and Hirnschall 2019), is default prediction. This specific area deals with predicting the probability of lenders committing default by using information such as profiles or loan history. As a mass business, there is a frequent and continuous need to reevaluate the default risk. AI methods support these endeavors, e.g., by assessing enormous amounts of available data and making informed recommendations. However, the reasons for these recommendations are often not transparent or comprehensible, leading to implementation resentment. XAI addresses these reservations by complementing AI-based suggestions with explana- tions to ensure they are discrimination-free and thoroughly founded, rendering the AI methods usable in the industry (Park et al. 2021).

In addition to these adoption hurdles, in a highly-regulated application domain such as Finance, laws and regulations condition the need for using XAI systems,

1 3

[p. 3]

as AI systems often would not comply with the law (Weber et al. 2020). Recent law initiatives, e.g., the US Financial Transparency Act of 2021 (FTA) (Maloney 2021) or the EU Artificial Intelligence Act (AIA) (European Commission 2021), prescribe very high levels of transparency when applying AI-supported decision- making in practice (Hoofnagle 2013; Elliott et al. 2021) in order to ensure trust in and reliability of these systems. The proposed US FTA gives the following justifi- cation: The act aspires to make reported information electronically searchable, to enable the creation of RegTech (i.e., technology supporting regulatory processes) and AI applications, and to decrease regulatory compliance burdens through standards and the enhancement of transparency and accountability.1 The proposed EU AIA addresses AI’s risks or negative consequences for individuals or society, stating: “Rules for AI available in the Union market or otherwise affecting people in the Union should therefore be human centric, so that people can trust that the technology is used in a way that is safe and compliant with the law, including the respect of fundamental rights.” Regarding transparency, the AIA underlines pro- portionality, imposing higher transparency requirements on so-called high-risk AI systems such as those in Finance or Healthcare. Besides, the EU General Data Protection Regulation (GDPR) requires that decisions must always be the respon- sibility of people (Art. 22 GDPR), requiring some trust from employees and their ability to trace decisions made by an AI. Furthermore, some national authori- ties, e.g., the German Federal Financial Supervisory Authority, enforce additional requirements on the financial industry in particular, e.g., about the traceability of decisions and thus increased transparency (Pasquale 2015; BaFin 2018), which has always played an essential role (Vishwanath and Kaufmann 1999). Accord- ingly, evaluating XAI systems in Finance is essential for the applicability of such systems in these highly-regulated application domains, as automation aside from XAI models is less feasible from a regulatory point of view.

Nevertheless, research on XAI in Finance is widely dispersed (Elliott et al. 2021), making it more difficult for researchers and practitioners to unlock the full potential of XAI in the Finance domain. This paper aims to aggregate this scattered knowledge to provide an overview of the current state of research, including pos- sible future research avenues, and to support practitioners’ implementation of XAI in financial business practice. A structured overview could represent another step towards realizing the full potential of AI-based systems, especially XAI systems, due to prevailing regulations, in the financial industry.

[pp. 3-4]

While there is research dealing with AI in Finance, from a more technological perspective in IS and CS, or XAI in general, there is no paper reviewing the current state of research on XAI in Finance in leading international journals and conferences (Arrieta et al. 2019). Searching for related research, we were only able to find quali- tative literature reviews. These include dealing with aspects of the trustworthiness of AI employment in systemic risk assessment (Daníelsson et al. 2021), deep learning

1 Note, that this does not decrease regulatory compliance requirements (e.g., transparency, account- ability) themselves. The decrease affects the burdens imposed by the requirements on the private sector through harmonization and standardized business reporting.

1 3

and anti-money laundering as a combination of a specific XAI method with a spe- cific area in Finance (Kute et al. 2021), the design of smart markets, that, by using computational tools, help human decision-makers make real-time decisions in com- plex trading environments (Bichler et al. 2010), or banking in general (Burgt 2020). With our study presenting a systematic literature review (SLR), we follow calls for further research from the academic community concerning the compliance behavior in highly-regulated application domains such as Finance and how researchers, prac- titioners, and regulators should react to recent developments in AI and XAI (Ciatto et al. 2020). The need for this research is deepened by practitioners agreeing on the necessity of trustworthiness of AI in Finance, which is achievable through explain- ability (IEEE 2021). Besides, regulators in many countries demand greater transpar- ency and explainability of decisions in the financial sector by requiring XAI rather than AI-based systems (Kalyanathaya 2022). Accordingly, we advance research and practice by reviewing relevant Finance, IS, and CS literature and performing an SLR to aggregate yet disorganized research on XAI in Finance.

[pp. 4-5] [ref: 2.1]

With the paper at hand, we contribute to academia’s emerging interest in XAI in Finance research in different dimensions. First, our research offers guidance for scientists to understand the growing emphasis on XAI in Finance research that we also found in other domains (Wells and Bednarz 2021; Islam et al. 2022). Second, when taking a closer look at the goals these research endeavors and the application of XAI in practice try to achieve, we confirm an imbalance already highlighted by prior research (e.g., Arrieta et al. 2019). Third, scientists looking for the distribution of a specific XAI method in Finance may find answers in our results, as we provide an overview of current research on XAI, especially in Finance. As our final set of articles reveals, only a few papers deal with whether the developed or applied XAI methods meet regulatory requirements (except for, e.g., Park et al. 2021). This is a prerequisite for the implementation in practice, thus highlighting a critical future research avenue.

Practitioners, such as legislators, regulators, and Finance managers, benefit from our research, as we provide basics of XAI methods employed in Finance, a yet dis- persed research area. Looking for existing XAI applications in their specific Finance areas, Finance managers may consult our study to learn about ready-to-employ solu- tions to add transparency to their AI-based systems. Alternatively, existing knowl- edge about XAI models and possible application scenarios in the company can be matched. Practitioners can use our study to gain a quick overview of already accept- able methods from a regulatory point of view. Policymakers may respond to the shift from transparent models to post-hoc explainability by designing corresponding laws and regulatory requirements. Finally, practitioners may infer trends in XAI in Finance to prepare their employees for future challenges through specialized XAI trainings.

The remainder of this study is structured as follows. Next, we present a section about related literature introducing the areas of AI and XAI on the one hand and the Finance domain (i.e., technological influences and areas where AI and XAI are applicable) on the other. In this way, we establish common ground for the character- istics of different XAI models, reconvene why the explainability of AI is crucial for decision-making, describe the main concepts of how to achieve it, and introduce the

1 3

possibilities for usage of (X)AI-based systems in Finance. Then, we give an over- view of our research method, followed by a presentation of our results. We conclude with a discussion of the theoretical and managerial implications of our research next to limitations and avenues for future research.

2 Related literature

2.1 Artificial Intelligence

[p. 5]

AI is a key technology of the 21st century which is applied in various areas, e.g., search engines, voice recognition, and interactive interpreters (Russell et al. 2016). Starting from the mid of last century (McCarthy et al. 1955), benefiting from Big Data, cheap computing power and storage, and improved algorithms, AI faces unseen opportunities nowadays. It is expected to largely change society through pro- ductivity-enhancing automation and job replacement.2

In research, AI is considered a subarea of Computer Science (CS) (Shapiro 1992). Still, consensus lacks a single AI definition, as intelligence itself is not ade- quately defined (Legg and Hutter 2007; Rzepka and Berger 2018). Thus, there are numerous definitions of AI. The founders of AI gave the first definition as “making a machine behave in ways that would be called intelligent if a human were so behav- ing” (McCarthy et al. 1955, p. 11). More recently, Russell et al. (2016) systematized eight currently discussed definitions by seeking human intelligence or rationality and focusing on either thinking or acting. Recent definitions emphasize intelligent agents interacting with their environment and pre-set goals (Russell et al. 2016). AI is also influenced by other disciplines (Shapiro 1992), e.g., mathematics, economics, and psychology (Russell et al. 2016).

Although there is a plethora of AI research (e.g., Abdel-Karim et al. 2021; Cao 2020, 2022; Goodell et al. 2021; Martin 2019; Rai et al. 2019; Zheng et al. 2019), practical implementation lags due to the so-called black-box nature of most AI- based systems, thus missing to unlock the full potential of AI implementation. The black-box nature refers to a lack of explainability and interpretability of AI-based systems, primarily arising from the opacity of many of today’s AI-based systems. Hence, the nature of inputs and outputs can be observed and understood chiefly, but not the exact processing steps in between—the black box. Accordingly, users or programmers of these systems cannot determine what influence which variable had on the decision or how this decision arose from the input variables. This is dif- ficult for traceability, which is partly mandatory for regulatory purposes, but also the trust in such systems. XAI, a sub-class of AI systems, counteracts the general black-box nature of AI-based systems (Doran et al. 2017; Rosenfeld and Richardson 2019; Arrieta et al. 2019; Ciatto et al. 2020; Sanneman and Shah 2020; Verhagen et al. 2021).

[pp. 5-6] [ref: 2.2]

2 For further information see Russell et al. (2016).

1 3

2.2 Explainable Artificial Intelligence

In our work, we follow the definition of XAI given by Arrieta et al. (2019), that states as follows: “Given an audience, an explainable Artificial Intelligence is one that produces details or reasons to make its functioning clear or easy to under- stand.” (Arrieta et al. 2019, p. 6). Thereby, we impose ease of understanding of AI for humans and use targeted explanation techniques such as XAI. In general, we can view explainability as a vital attribute of AI models, which indicates any pro- cedure that intends to clarify its inner workings. This is predominantly known as understandability in the XAI literature and denotes specifically the model charac- teristics that help a human understand how the AI system works (Montavon et al. 2018). Additionally, this is tied to interpretability, which we can define as the ability to provide a model with meaning in understandable terms to humans through, e.g., transparency, if an AI model is by itself understandable. Thus, explainability is two- fold, leading to model explainability, i.e., the ability of the system to reveal its inner workings, and human understandability, i.e., the capability of humans to understand the factors and the knowledge contained within an AI model. Employing XAI can lead to increased trust, e.g., by consumers and employees, and accountability in deployed AI models (Rai et al. 2019; Martin 2019; Elliott et al. 2021). Increased trust ultimately results in more widespread adoption of AI applications (Adadi and Berrada 2018; Janiesch et al. 2021; Mirbabaie et al. 2021; Sigrist and Hirnschall 2019). Especially in highly-regulated application domains or in environments with highly consequential decisions—like Finance, Healthcare, and Automotive—this requirement can be crucial for a successful application. Nevertheless, these indus- tries are predestined for the application of AI systems due to the vast amounts of available data and automatable processes. In this vein, the need for XAI emerged, as it supports the evaluation and justification of AI systems (Zheng et al. 2019; Meske et al. 2022). Recent calls for, e.g., trustworthy (Thiebes et al. 2021) or sustainable AI (Bawack et al. 2022) underline the need for an exaggerated concept of AI.

[pp. 6-7]

Next to defining XAI, it is essential to reconvene various goals of explainability of AI evolved from the literature. In general, all these goals help to understand why the explainability of AI is needed and performed, especially when acting in a highly- regulated application domain such as Finance (Cao 2022). Thus, we follow an estab- lished nomenclature of XAI goals (Arrieta et al. 2019) and include the following nine goals: trustworthiness, causality, transferability, informativeness, confidence, fairness, accessibility, interactivity, and privacy awareness. These goals, presented in Table 1, relate to what XAI aspires to compel.

Finally, it is crucial to inspect how we can achieve explainability. The first impor- tant distinction is between understandable models by design and so-called black- box models, which require external XAI techniques to enable human understand- ing. Thus, we differentiate between transparent models and post-hoc explanation techniques.3

3 For further information and an explanation of each of the models see Arrieta et al. (2019).

1 3

Table 1 Goals of XAI based on Arrieta et al. (2019)

XAI goals Description of the goal

Trustworthiness Trustworthiness refers to the degree of confidence a model will react as expected

when opposing a specific problem.

Causality Causality among data variables means finding cause-effect relationships leading to

higher model comprehensiveness.

Transferability Transferability deals with uncovering boundary constraints of models to better assess

their applicability in other cases.

Informativeness Informativeness is concerned with the distinction between the original human

decision-making problem and the problem solved by a given model, including its inner mechanisms.

Confidence Confidence describes the robustness and stability of a model, including its working

regime.

Fairness Fairness tries to prohibit the unfair or unethical use of model results and outputs by

ethical analysis and illumination of results affecting relations.

Accessibility Accessibility refers to the involvement of (non-technical) end users in the AI mod-

eling process.

Interactivity Interactivity deals with the level of interaction between end users and XAI models to

improve the latter.

Privacy awareness Privacy awareness is about enlightening possible privacy breaches by informing

users.

[pp. 7-8]

Transparent models must satisfy specific properties to be explainable to decision- makers. First, they are decomposable in that each part is fully explainable or inter- pretable by design, e.g., input parameters or computations. For instance, complex and non-interpretable input features would fail this criterion, making an AI model less understandable (Lou et al. 2012). Second, transparent models should satisfy algorithmic transparency, i.e., a decision-maker’s need to understand the process of the model to produce its output derived from its inputs. Thus, the decision-maker knows how the model would react in any given situation. Commonly used transpar- ent models are linear/logistic regression, decision trees, k-nearest neighbors, rule- based learners, general additive models, or Bayesian models.3 To give an example, decision trees consist of a hierarchical structure for decision-making, primarily sup- porting classification problems. Decision trees display different features and feature values on each tree level. Generally, they are easy to understand for a human deci- sion-maker as they easily represent input features and the output variable. Figure 1 provides an exemplary decision tree for forecasting bank loans loss-given-default. The tree reflects a recovery horizon of 24 months and estimates the expected recov- ery rate (RR), depending on features like the loan size (Debt) and the age of the cli- ent’s relationship with the bank (AoR) measured in months.

When AI models do not satisfy the properties of transparent models, post-hoc explainability methods come into place. These methods provide interpretable infor- mation for decision-makers to understand the AI model’s process of producing its output for a given input. The literature (e.g., Arrieta et al. 2019) distinguishes between two different post-hoc explainability methods: model-agnostic and model- specific.3 Model-agnostic methods can be applied to any given AI model. Such

1 3

Fig. 1 Example decision tree (Bastos 2010, p. 2514)

Fig. 2 Example ICE plot (Fernández 2020, p. 145)

[pp. 8-9] [ref: 2.3]

methods can be classified into three categories: explanation by simplification, fea- ture relevance explanation, and visual explanation. One example of explanation by simplification is local explanation techniques such as Local Interpretable Model- Agnostic Explanations (LIME) and all its variants. LIME is a rule extraction tech- nique and builds locally linear models around the prediction of the model that it tries to explain (Ribeiro et al. 2016). Other well-known model-agnostic techniques, such as Shapley Additive explanations (SHAP), fall within the feature relevance expla- nation. With SHAP, the authors offer a way to measure the influence of relevant input features by calculating a feature importance score for each particular predic- tion (Lundberg and Lee 2017). Although LIME and SHAP may be visualized, it is not their defining characteristic, leading to the third category: visualization tech- niques such as Individual Conditional Expectation (ICE) (Goldstein et al. 2015). ICE allows graphing the functional relationship between the predicted response and

1 3

the feature for individual observations. For instance, Fernández (2020) predicts bank solvency in the United States and uses ICE plots for sensitivity analysis. Figure 2 shows the individual observations, plotting the mortgage rate on the x-axis and the bank solvency (measured as the level of regulatory capital among risk-weighted assets) on the y-axis. From here, one can deduce two breakpoints in solvency: With rising mortgage rates, there are two drops in bank solvency, one at mortgage rates of 5% and the other at about 8.5%. These techniques help visualize the model parameters of any supervised AI algorithm. However, visualizations are less common model-agnostic explanation techniques since ensuring their applicability to any AI model’s inner structure is challenging.

Model-specific methods can only be applied to their respective category of AI models such as, e.g., ensembles and multiple classifier systems, support vector machines (SVMs), and neural networks.3 For the latter, simplification techniques like DeepLIFT compute importance scores for multi-layer neural networks. With this approach, one can compare various neuron activations to a reference activation and assign a score based on the computed difference (Shrikumar et al. 2017).

2.3 Technological advances in Finance

[pp. 9-10]

Finance is a broad field of applications with very diverse requirements for technical systems and automation, mainly due to regulatory and legal requirements. Still, the domain continuously uses and adapts to new technological opportunities (Gimpel et al. 2018; Zheng et al. 2019), like AI and XAI. This phenomenon is also referred to as FinTech, i.e., financial technology. Previously, research emphasized the applica- tion of AI in Finance (e.g., Cao 2020, 2022; Goodell et al. 2021; Zheng et al. 2019). Cao (2020, 2022) evaluates the challenges of financial businesses and provides a comprehensive overview of solutions through classic and modern AI in Finance and economics. Goodell et al. (2021) present a holistic retrospection of the extant lit- erature on AI application in Finance through co-citation and bibliometric-coupling analyses of 283 articles for the last three decades. They derive the following the- matic clusters: financial distress and corporate failure, algorithmic and high-fre- quency trading, forecasting and predictive analysis, text mining and sentiment anal- ysis, financial fraud, pricing and valuation, scheduling, and investor behavior and trade classification. Zheng et al. (2019) specifically analyze financial intelligence, which they define as FinTech 3.0, i.e., the third stage of technological advancements in Finance after computers (FinTech 1.0) and the internet (FinTech 2.0). Financial intelligence achieves “intelligent and accurate calculation responsibility and (…) lead[s] the overall change in the financial industry” (Zheng et al. 2019, p. 914). They describe the AI key application areas of wealth management, risk manage- ment, financial security, financial consulting, and blockchain. While there is a con- siderable amount of publications aggregating research on AI in Finance, there is no paper reviewing the current state of research on XAI in Finance. Due to the high regulations applying to domains like Finance and practical requirements, e.g., for the transparency of decisions, XAI can play a decisive role in augmenting processes in

1 3

such domains. Hence, it is necessary to discuss XAI related to the different applica- tion areas in Finance. Research divides Finance into several areas (e.g., Huang et al. 2020; Hentzen et al. 2021; Goodell et al. 2021). Particularly pivotal and commonly discussed for AI deployment are the Finance areas of risk management, stock mar- ket, portfolio optimization, anti-money laundering, and electronic financial transac- tion classification.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Patrick Weber, K. Valerie Carl, Oliver Fast Hinz, "Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature" (2023-02-28). https://link.springer.com/article/10.1007/s11301-023-00320-0
