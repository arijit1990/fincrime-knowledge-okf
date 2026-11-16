---
type: Source Text
title: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature - part 2 of 6 (pp. 10-19)
description: Verbatim extracted text, pp. 10-19
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
part: 2
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

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-02-28), part 2 of 6, pp. 10-19. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 10]

Risk management (e.g., default and bankruptcy prediction, fraud detection) is concerned with identifying, measuring, and controlling financial risks (Zheng et al. 2019). Financial institutions continuously perform it, and regulators require it (Adams and Hagras 2020). Default and bankruptcy prediction refers to a state of (corporate) failure (Sigrist and Hirnschall 2019). Default prediction is concerned with predicting the probability of debtors, e.g., credit card holders and financial institutions, to commit default using available information, e.g., profiles, loan his- tory, and repayment history. Bankruptcy prediction deals with publicly available information and derives, e.g., accounting ratios to determine the likelihood of a company going bankrupt, a valuable information for potential investors and cur- rent creditors (Sigrist and Hirnschall 2019; Zheng et al. 2019). Fraud detection involves uncovering unauthorized (fraudulent) transactions on accounts (Jarovsky et al. 2018). AI methods support these endeavors by assessing numerous cases, e.g., credit card applications, or enormous amounts of available data, e.g., in the case of public companies, and suggesting possible actions, like approving or denying credit card applications or loans. XAI complements these suggestions with explanations to ensure they are discrimination-free and thoroughly founded, rendering the AI methods usable in the industry (Park et al. 2021). More precisely, in the case of default prediction, e.g., a gradient tree-boosted model may get employed (Sigrist and Hirnschall 2019). This model performs a binary classification by assigning loans to small and medium-sized enterprises into two categories: defaults and non-defaults. Among approximately 50 different predictor variables, this AI model uses the num- ber of days of delay until repayment (delay days) to predict rare events, such as loan defaults. Here, the authors introduce two model-agnostic post-hoc explainability tools for the interpretation of the AI model (i.e., two XAI models): variable impor- tance measures (feature relevance explanation) and partial dependence plots (visual explanation). Variable importance measures quantify and illustrate single variables’ importance for the prediction (Sigrist and Hirnschall 2019). Further, partial depend- ence plots (see Fig. 3) visualize the model by showing how a single variable influ- ences the prediction outcome aggregated for several observations. For instance, plot- ting the age of the accounting data provided by a company (age accounting data) or the delay days against default probability illustrates the model. As Fig. 3 shows, a lower age accounting data and fewer delay days are related to a lower default prob- ability. Additionally, the linear relationship in the case of age accounting data and the non-linear relationship in the case of delay days is recognizable. These illustra- tions help overcoming the black-box nature of AI-based systems.

[pp. 10-11]

Trading in the stock market benefits from AI usage, as the latter is expected to impede emotionally, and thus irrational, investment decisions and find patterns beyond human recognizability (Ferreira et al. 2021). Price prediction estimates the future value of a specific stock, option, or index. To achieve this, human and AI

1 3

Fig. 3 Example partial dependence plots (Sigrist and Hirnschall 2019, p. 28)

predictors use various input factors from within the stock market, e.g., past prices and trading volumes, and outside of it, e.g., press releases, annual reports, and social media (Ito et al. 2021). XAI supports this automated process by delivering explana- tions to highlight on which specific input variables investment decisions or price predictions are based. To give another example of the application of XAI from the area of trading in the stock market, we closer inspect technical analysts. They rely in their trading strategies on historical charts and heuristic approaches, trying to extrapolate future asset prices, as opposed to fundamentalists, who strictly base their trading behavior on asset prices derived from efficient market hypothesis’ fundamen- tal values (Brock and Hommes 1998). Technical analysts’ behavior provides ground for applying reinforcement learning to retrieve the used “rules-of-thumb” (rule-base learners). This refers to determining “the amount of relevant historical information as well as the optimal parameters of the technical rules employed” (Bekiros 2010, p. 1154), as a common problem discussed with the technical analysts’ approach is the lack thereof. Here, using AI that is by design interpretable, as its outcome con- sists of parameters of fuzzy inference rules (transparent XAI model), supports the cause of XAI (Bekiros 2010).

Portfolio optimization deals with asset allocation, which is considered one of the most relevant research fields in asset management (Zhang et al. 2020a). It refers to finding a set of investment assets that fulfills the needs of a particular investor while usually simultaneously maximizing a particular goal (Ferreira et al. 2021). Advanced models allow investors to include their expectations and confidence level, while Big Data enables the incorporation of, e.g., market sentiments or other mac- roeconomic factors such as gross domestic product growth or inflation (Zhu et al. 2020). AI models help solve this complex problem by automatically deriving con- clusions from these large amounts of data with multiple input variables. At the same time, XAI adds interpretability to these conclusions, e.g., a portfolio output, to nar- row down the relevant factors for specific asset allocations.

[pp. 11-12]

Money laundering refers to techniques of “hiding proceeds of crime” (Levi and Reuter 2006, p. 289). Anti-money laundering measures are, e.g., know-your- customer requirements that ensure that banks verify their customers’ identity by

1 3

checking government-issued IDs. The application of AI models may improve this process by handling large amounts of data and detecting anomalies, thus revealing potential money laundering cases. However, as money laundering suspicions can prevent customers from financial transactions, interpretability in the form of XAI for these automatically generated suspicions is needed (Kute et al. 2021). The mere results of an AI model are not sufficient in this case. Instead, explanations for the decisions are crucial.

Electronic financial transaction classification is concerned with classifying trans- actions that bank account holders perform into categories, e.g., groceries or trans- portation (Maree et al. 2020). While less regulated than others, this area is of pivotal importance for AI applications in Finance. Hence, we include this area in our con- sideration. Financial institutions may use this classification to present value-adding products to customers like digital financial advisors. Individuals’ electronic financial transactions are highly personal (Achituve et al. 2019). Thus, applications based on these transactions include the risk of privacy intrusions and discrimination. Misclas- sification of transactions could also impede the usability, and thus profitability, of a digital financial advisor, which determines the need for explainability.

To sum up, Finance is a highly-regulated application domain with a tremendous need for explanations when employing AI techniques (Zheng et al. 2019). Regula- tors and supervisors require banks to illuminate their activities when using AI (Burgt 2020; Weber et al. 2020; Adams and Hagras 2020), hence requiring the deployment of XAI models in specific application scenarios.

3 Method

The conducted SLR aims to provide a comprehensive overview of previously dis- persed research and a research agenda for XAI in Finance. This contributes to the goal of anchoring and facilitating XAI usage in the financial sector, thereby advanc- ing theory and practice alike. In the following, we describe the methodology and employed search strategy for our SLR.

[pp. 12-13]

SLRs present the current state of research on a particular topic by aggregating prior research results. In this vein, SLRs also uncover less researched areas of the topic under investigation (e.g., Kitchenham et al. 2011; Okoli and Schabram 2010; Snyder 2019). Consequently, SLRs aim to aggregate the extracted research out- comes of previously conducted studies and their propositions (Okoli and Schabram 2010; Kitchenham et al. 2011). Thus, SLRs cluster the current state of research according to predefined criteria and thereby contribute to the conceptualization of the topic under investigation (Paré et al. 2015; Snyder 2019). Derived results of an SLR target researchers and practitioners (Kitchenham et al. 2011; van Aaken and Buchner 2020). Researchers benefit from a comprehensive overview of previous research and the developed future avenues for research, whereas practitioners can employ the derived overview as a guideline for their operations (Kitchenham et al. 2011; Snyder 2019). We designed our SLR according to well-established guidelines in IS research, specifically those by Kitchenham (2004). By following these guidelines, we ensured

1 3

Table 2 Search terms used

Domain Keywords

Explainability “Transparen*” or “explain*” or “explanat*” or “interpret*” or “black box” or

“white box”

AI Implementation “Artificial intelligence” or “machine learning” or “natural language processing” or

“data mining” or “data science” or “text mining”

Finance “Financ*” or “banking” or “trading” or “credit scoring” or “money laundering”

Note This study employs wildcards (*) and Boolean operators in the search terms. The final search term consists of the three domain keyword sets connected with the Boolean operator “AND”

a transparent and reproducible process, providing trustable, reliable, and rigorous research outcomes. Besides, we employed a detailed review protocol to ensure fur- ther transparency and reproducibility. The review protocol covered the whole pro- cess from conceptualization to the actual search and evaluation of results. It pro- vided detailed information on the conducted search, inclusion and exclusion criteria, search strategy, and analysis procedure.

[pp. 13-14]

The initial search for articles employed three search term domains connected by the operator “AND” to ensure the fit with the topic under investigation. One domain aimed at explainability, one fostered AI implementation, and a third one ensured the applicability to the financial domain (see Table 2). This helped us to limit the number of retrieved articles and ensured the relevance of the derived studies. We searched the title and abstract for the chosen search terms to provide a broad set of relevant prior research. Nevertheless, an SLR does not aim at providing an exhaus- tive overview of prior research on a particular topic but rather guidance on the previ- ously conducted research. Summing up, the search focused on publications address- ing XAI in the financial context while excluding prior research emphasizing AI or other application scenarios (e.g., Healthcare, Automotive).

In order to do justice to the topic at hand, we included the top-ranked (A + and A) Finance journals according to the German Academic Association of Business Research (VHB) in the search. Further, we included the eight Information Systems (IS) basket journals (i.e., European Journal of Information Systems, Information Systems Journal, Information Systems Research, Journal of AIS, Journal of Infor- mation Technology, Journal of MIS, Journal of Strategic Information Systems, MIS Quarterly), and the top CS journals according to the Scimagor Journal Ranking. We included CS as a research area to capture a more technical angle to the topic and IS as research on the intersection of technology and practical implementation. Besides, the search process also covered several databases (i.e., ACM Digital Library, AIS eLibrary, IEEE Xplore) related to IS and CS research to provide an extensive over- view of current research findings, thus following similar SLRs (e.g., Bouncken et al. 2015; Sageder et al. 2018; Malinova and Mendling 2021). We included peer- reviewed publications in leading international journals and conference proceedings to ensure high-quality standards. Besides, we limited the search to publications since 2010 to provide a more recent overview of current research in a rapidly changing environment of XAI research endeavors. The same search strategy (i.e., search terms

1 3

Fig. 4 Visualization of the SLR process

[pp. 14-15]

and criteria) is independently applied to each outlet and database. The search took place from October 2021 to January 2022 to provide the most recent picture of cur- rent research, up to and including the year 2021. The initial search yielded 2,022 results. Upon excluding duplicates, the set consisted of 2,000 results. Figure 4 visu- alizes the steps of our SLR process and provides additional information on the par- ticular quantities (i.e., initially, 545 results from Finance, 870 results from IS, and 607 results from CS). The screening process employed a set of exclusion criteria to ensure the relevance of the results and the focus on the research goal. Besides publication date and focus

1 3

on peer-reviewed outlets, we defined the following rigid exclusion criteria4 to filter out irrelevant publications:

• The paper deals with Finance but not with XAI. • The paper deals with XAI but not with Finance. • The paper deals with AI and Finance but not with XAI.

The screening process consisted of several steps. First, we checked the result set for relevance to the research project and the criteria utilizing their titles, abstracts, and keywords. In questionable cases, we also screened additional publication sec- tions like the introduction and conclusion. We excluded all articles with a misfit concerning research goals and search criteria, in our case, 1,757 publications. This led to 243 publications relevant to the following screening step. Within the next step, we evaluated these publications in detail according to their full texts. Fifty-four publications finally matched the search criteria and research goals. The far-reaching search caused relatively high exclusion rates during the process. However, conduct- ing a more comprehensive search was necessary to provide an overview of the inter- section of XAI and Finance. After screening the derived publications for relevance, we browsed these retained publications for key publications (i.e., backward search). The backward search yielded another six relevant publications. Hence, the final set featured a total of 60 articles (see Appendix 1 for the complete list).

The last step of the SLR covered the coding of the final publication set. We coded according to publication details (i.e., publication, year, methodology) and the the- matic focus and application (i.e., XAI method and goal, area of Finance). To the best of our knowledge, no suitable coding scheme is available. Thus, we developed a multiple classification-coding scheme (i.e., coders can assign one publication to sev- eral classifications). The developed coding scheme spanned a matrix that connects the XAI application and the area of Finance (according to the presented nomencla- tures). However, the developed coding scheme should ensure an iterative, discursive process instead of being a rigid scheme. Three coders independently performed the coding, discussing possible deviations and settling them in mutual agreement.

4 Results

[pp. 15-17] [ref: 4.1]

4.1 General overview

We present the publication trend of XAI research in Finance in Fig. 5. The graph shows the number of articles published in the respective year. Figure 5 indicates that XAI research in Finance was already relevant a decade ago, followed by a pau- city around 2013 and 2014. We find the most articles for 2020 with n = 17 articles, followed by 2021 with the second-most n = 16 articles. Thus, the two recent years

4 We applied these criteria in each of the screening steps to ensure the consistent pursuing of the research goal.

1 3

17 16

Fig. 5 Publication trend of XAI research in Finance (n = 60)

Number of Ar cle(s)

1 2

2 1 0 0

Year

Case Study, 2

Algorithm Review, 3

Fig. 6 Methodological overview of XAI research in Finance (n = 60)

Algorithm Demonstraon, 3

Qualitave

Literature Review, 2

Theorecal Model + Real

Market Datasets, 32 Experiment, 18

account for over 55% of the articles we found, indicating this research area to be of considerable growth. We assume this to manifest the current AI and XAI trend in research (Collins et al. 2021), e. g. due to rising transparency needs by policymak- ers, we also find in other domains regarding XAI (Wells and Bednarz 2021; Islam et al. 2022).

In Fig. 6, we provide an overview of the methods used in XAI research in Finance.5 The majority of the reviewed articles present theoretical models, which are subsequently applied to real market datasets (n = 32). For instance, Liu et al. (2021) propose a logistic regression model empowered with cross-features gener- ated through deep neural networks, which they apply to multiple public and business

5 We chose to include qualitative literature reviews in our sample, as it presents a broader picture of the relevant literature. Also, in this, we follow other SLRs (e.g., Bouncken et al. 2015; Sageder et al. 2018; Malinova and Mendling 2021).

1 3

Fig. 7 Overview of publication disciplines, forms, and ratings (n = 60)

[p. 17]

datasets from real-world credit risk assessment applications. The runner-up method is the experiment performed by n = 18 articles in our subset. For instance, Ghandar and Michalewicz (2011) experiment with multi-objective evolutionary algorithms for stock price prediction to pursue the XAI goals of informativeness and confi- dence. Least used are the methods of qualitative literature review and case study, which are only employed by two research teams each, e.g., a case study by Mayer et al. (2020), who conduct an in-depth case study of a large German bank imple- menting an AI system supporting credit risk decisions.

We figure this focus on theoretical models with real market datasets and experi- ments to be an expression of the data-driven characteristic of AI and, subsequently, XAI. Most researchers employed either real or experiment-crafted datasets to pre- sent their XAI-related results in Finance. This adds to the practical applicability of the study at hand, as it shows Finance practitioners that XAI is already well-con- nected to, e.g., real market datasets and is thus more readily available for implemen- tation in their specific Finance areas.

We find an imbalance in the disciplines from which the reviewed research articles originated. As Fig. 7 shows in the first bar, roughly a quarter (n = 13) of the sam- ple is published in Finance literature such as the Journal of Banking and Finance, while the majority (n = 47) is based in the IS and CS disciplines with research out- lets like Information Systems Research. This paucity of XAI research in Finance literature we found in our sample fosters further inspection. We conclude there is a further need for the Finance discipline to engage with research on XAI due to the specific requirements of this industry for such systems. Accordingly, it is insuf- ficient if only more technically oriented disciplines, i.e., IS and CS, deal with it. Instead, the view of the application-specific discipline, i.e., Finance, is also valu- able and essential. Besides, due to high regulatory requirements in this industry, law researchers should respond to law initiatives and laws such as the US FTA, the EU AIA, and the GDPR next to scientific calls for transparency in Finance (Vishwanath and Kaufmann 1999; Pasquale 2015; Weber et al. 2020) and deepen their research on XAI in regulated domains. We find a balanced distribution by looking at the pub- lication form the authors in our subsample chose. Half of the articles were published in journals (n = 28), while the other half were introduced at conferences (n = 32), as

1 3

[p. 18] [ref: 4.2]

the second bar of Fig. 7 shows. This balance implies that XAI in Finance is an estab- lished research field future scientists might want to look at, as it is well-represented in both research trends capturing conferences and basic research advancing journals. In the lower bar of Fig. 7, we can see the distribution of the rankings the respective publication outlets received. We adopt the rating provided by the VHB, ranking out- lets from A + (best quality and impact) to D (lower quality and impact), considering all discipline ratings.6 We find only one article with the highest rank A + , while a fifth of our subsample’s articles were published in outlets receiving the second- best rank, A (n = 11). Interestingly, researchers publish most articles in journals or conference proceedings that received no rating (n.r.) by the VHB (n = 45). This fact may show that XAI in Finance is yet predominantly concerned with an application point of view, thus, possibly neglecting the theory-building and development part of research that could further pave the way for realizing the full potential of XAI in Finance. Additionally, research is driven by non-management disciplines such as IS and CS.

4.2 Overview concerning XAI goals and methods

We research which goals XAI in our subsample pursuits. For this purpose, our cod- ing scheme grounds on the well-accepted nomenclature of XAI goals by Arrieta et al. (2019) and considers the nine goals of XAI mentioned above: trustworthiness, causality, transferability, informativeness, confidence, fairness, accessibility, inter- activity, and privacy awareness. Table 3 provides an overview of the respective arti- cles dealing with specific XAI goals. As the literature indicates (e.g., Arrieta et al. 2019), most XAI papers deal with the goal of informativeness, while the least deal with privacy awareness. We confirm these results for our sample of papers. Most of our sample (n = 43) deals with informativeness, while only two articles target the XAI goal of privacy awareness. This paucity of research with the goal of privacy awareness is somewhat interesting, as laws, e.g., the GDPR, emphasize privacy and the right to informational self-determination, especially in industries like the finan- cial sector. Future research has to unravel this mismatch and identify potential rea- sons for it.

[pp. 18-19]

Next to the goals of XAI, we take a closer look at the XAI methods used in the reviewed sample. As for the list of XAI goals, we base our coding of XAI methods on prior literature (e.g., Arrieta et al. 2019). We distinguish between transparent AI models, which are interpretable without any further additions, and so-called post- hoc explainability, which complements existing AI models to create or improve their interpretability. For the latter, there is model-agnostic explainability on the one side, providing explainability regardless of the model, and model-specific explainability on the other, which improves explainability for distinct AI models (Arrieta et al. 2019).

6 https://​vhbon​line.​org/​en/​vhb4y​ou/​vhb-​jourq​ual/​vhb-​jourq​ual-3/​compl​ete-​list.

1 3

Ge et al. (2021)

(2021); Park et al. (2021); Mariotti et al. (2021); Daníelsson et al. (2021); Lusinga et al. (2021)

(2017); Renault (2017); Li et al. (2018); Horel et al. (2018); Rajab and Sharma (2019); Zhang et al. (2020b);

Zhang et al. (2019); Chou (2019); Achituve et al. (2019); Oppold and Herschel (2019); Wu and Yan (2019);

Ariza-Garzón et al. (2020); Cong et al. (2020); Rosati et al. (2020); Zheng et al. (2020); Attanasio et al.

(2020); Adams and Hagras (2020); Dattachaudhuri et al. (2020a, b); Kong et al. (2020); Dastile and Celik

(2021); Ferdaus et al. (2021); Kute et al. (2021); Guo et al. (2021); Liu et al. (2021); Nian et al. (2021)

et al. (2015); Duan and Zeng (2015); Butaru et al. (2016); Xu et al. (2017); Yang et al. (2018); Li et al.

(2018); Rajab and Sharma (2019); Sigrist and Hirnschall (2019); Shi et al. (2019); Zhang et al. (2020a);

[p. 19]

Zhang et al. (2020b); Zhang et al. (2019); Chou (2019); Achituve et al. (2019); Oppold and Herschel (2019);

Cong et al. (2020); Kraus et al. (2020); Mayer et al. (2020); Rosati et al. (2020); Schnaubelt et al. (2020);

Adams and Hagras (2020); Dattachaudhuri et al. (2020a, b); Kong et al. (2020); Maree et al. (2020); Wang

et al. (2020); Zhu et al. (2020); Carta et al. (2021); Cheong et al. (2021); Dastile and Celik (2021); Ferdaus

et al. (2021); Kute et al. (2021); Park et al. (2021); Ito et al. (2021); Guo et al. (2021); Mariotti et al. (2021);

Lusinga et al. (2021); Ge et al. (2021)

Herschel (2019); Ariza-Garzón et al. (2020); Zheng et al. (2020); Kong et al. (2020); Carta et al. (2021); Liu

et al. (2021)

Cheong et al. (2021)

Wang et al. (2020); Kute et al. (2021); Daníelsson et al. (2021); Lusinga et al. (2021); Ge et al. (2021)

Privacy awareness 2 Maree et al. (2020); Kute et al. (2021)

Interactivity 6 Kamalloo and Abadeh (2010); Horel et al. (2018); Shi et al. (2019); Rosati et al. (2020); Cheong et al. (2021);

Accessibility 5 Hayashi et al. (2015); Duan and Zeng (2015); Alam et al. (2020); Rosati et al. (2020); Attanasio et al. (2020)

Fairness 9 Mayer et al. (2020); Adams and Hagras (2020); Koshiyama et al. (2020); Maree et al. (2020); Kute et al.

Confidence 30 Bekiros (2010); Khandani et al. (2010); Ghandar and Michalewicz (2011); Hayashi et al. (2015); Xu et al.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Patrick Weber, K. Valerie Carl, Oliver Fast Hinz, "Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature" (2023-02-28). https://link.springer.com/article/10.1007/s11301-023-00320-0
