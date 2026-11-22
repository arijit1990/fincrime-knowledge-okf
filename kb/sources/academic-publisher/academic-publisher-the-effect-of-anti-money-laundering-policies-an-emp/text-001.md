---
type: Source Text
title: 'The effect of anti-money laundering policies: an empirical network analysis - part 1 of 5 (pp. 1-8)'
description: Verbatim extracted text, pp. 1-8
resource: https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
tags:
- academic_finding
- academic_paper
- effectiveness
- global_academic
- regulation
status: stable
source_id: academic-publisher-the-effect-of-anti-money-laundering-policies-an-emp
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-03-18'
legal_status: unknown
part: 1
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T15:47:01Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T15:47:01Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
  title: 'The effect of anti-money laundering policies: an empirical network analysis'
  author: org:academic_publisher
  last_modified: '2022-03-18T00:00:00Z'
---

# The effect of anti-money laundering policies: an empirical network analysis

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-03-18), part 1 of 5, pp. 1-8. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Gerbrands et al. EPJ Data Science (2022) 11:15 https://doi.org/10.1140/epjds/s13688-022-00328-8

R E G U L A R A R T I C L E Open Access

The effect of anti-money laundering policies: an empirical network analysis

Peter Gerbrands1* , Brigitte Unger1, Michael Getzner2 and Joras Ferwerda1

Abstract

*Correspondence: p.gerbrands@uu.nl 1School of Economics, Utrecht University, Kriekenpitplein 21-22, 3584 EC Utrecht, The Netherlands Full list of author information is available at the end of the article

Aim: There is a growing literature analyzing money laundering and the policies to ﬁght it, but the overall eﬀectiveness of anti-money laundering policies is still unclear. This paper investigates whether anti-money laundering policies aﬀect the behavior of money launderers and their networks. Method: With an algorithm to match clusters over time, we build a unique dataset of multi-mode, undirected, binary, dynamic networks of natural and legal persons. The data includes ownership and employment relations and associated ﬁnancial ties and is enriched with criminal records and police-related activities. The networks of money launderers, other criminals, and non-criminal individuals are analyzed and compared with temporal social network analysis techniques and panel data regressions on centrality measures, transitivity and assortativity indicators, and levels of constraint. Findings: We ﬁnd that after the announcement of the fourth EU anti-money laundering directive in 2015, money laundering networks show a signiﬁcant increase in the use of foreigners and corporate structures. At the individual level, money launderers become more dominant in criminal clusters (increased closeness centrality). This paper shows that (the announcement of) anti-money laundering policies can aﬀect criminal networks and how such eﬀects can be tested.

Keywords: Money laundering; Social network analysis; Dynamic cluster detection; Policy evaluation

1 Introduction Money laundering means to disguise the illegal origin of criminal proceeds.1 When crim- inals are so successful that their criminal revenue exceeds their ordinary daily living and operating expenses plus re-investment into new crime, they have to recycle the surplus of criminal money and inject it into the legal economy. Criminal revenues from drugs, hu- man traﬃcking, cybercrime or fraud2 can be laundered in diﬀerent ways. The drug dealer, human traﬃcker or fraudulent manager can try to bring the criminal money to a bank,

1The precise deﬁnitions by each EU Member State in the native language and an English translation that are used for legal references to money laundering and tax crime are found in [1].

[pp. 1-2]

2See for the latest list of 22 crimes, so called predicate oﬀenses, which qualify for a money laundering crime the Fi- nancial Action Task Force website https://www.fatf-gaﬁ.org/glossary/d-i/ and the 6th AML Directive of June 2021, see https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0421

© The Author(s) 2022. This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

or heshe can set up companies and slip the criminal turnovers into the cash register of companies. He/she can do this in his/her own country or try to bring the money abroad. He/she can use cash couriers or set up complicated international constructions of shell companies with bank accounts in diﬀerent countries, Such shell companies in turn re- ceive and lend money with fake bills, or make mortgage payments to each other, without any or much real economic activity taking place. On average, this internationally circu- lating money through complex corporate constructions is pumped ﬁve times around the world [2] until it is ﬁnally parked in real estate, business, expensive cars or jewellery.

Over time, anti-money laundering (AML) policies became much stricter. Improved “know your customer” rules, and a wide range of ﬁnancial and non-ﬁnancial institutions like second-hand car dealers and real estate agents, who have to report unusual transac- tions, pose a new challenge for criminals. They have to ﬁnd alternative and more sophis- ticated solutions to deal with the new regulatory environment.

This means that more complex networks between people (often family members) who can act as (straw) CEO of companies will emerge, and that lawyers, notaries, real estate agents, and bank employees will function as facilitators with higher risks of being detected by the authorities.

[pp. 2-3]

Organized crime, such as big drug cartels, can have specialized money launderers who cannot be easily replaced owing to their specialized knowledge of ﬁnance. These money launderers can be even more important to the cartel than the ‘padrone’ himself, who can be replaced by a successor. Given that these specialists cannot serve the entire ﬁeld of all necessary activities of money laundering anymore, they have to collaborate with other specialists to complete the laundering process.

Therefore, money laundering professionals become more specialized, and even more important for the criminal network. Such launderers might only be able to develop and maintain a network of professionals within a speciﬁc geographical region, or they develop the knowledge and skills to perform one speciﬁc money laundering activity, like trade- based only, through shell corporations, or via lawyers, bankers or notaries within the ﬁ- nancial system.

But are AML policies eﬀective and eﬃcient? In May 2015, the European Parliament an- nounced a directive “on the prevention and use of the ﬁnancial system for the purposes of money laundering or terrorist ﬁnancing” [3], commonly known as the fourth anti-money laundering directive or AML-IV. This paper analyzes the eﬀects that are caused by intro- ducing new anti-money laundering policies on money laundering networks, and on in- dividual launderers. Comparing network indicators from before and after the announce- ment allows us to get an indication of how money laundering networks react to policy changes. For example, we ﬁnd that money laundering networks become bigger (i.e. the cluster size increases) and more international (i.e. national diversity increases). At the in- dividual level money launderers normally want to minimize risks by linking to the least amount of people needed. In contrast, we ﬁnd that stricter anti-money laundering (AML) policies cause them to link to more people instead (i.e. the degree centrality increases).

For this analysis, we conceptualized and empirically developed a large network contain- ing diﬀerent ties among people and businesses that were registered in the Netherlands from 2005 until 2019. We use administrative data with information about people, their family ties, shared bank accounts, and employment history and data from the chamber of commerce with corporate information and ownership relations. We retrieve and link

criminal data about known police interventions and legal convictions to these links, and add all suspicious transactions of money laundering among them. Within this large net- work, we identify strongly connected clusters and follow these over time. We distinguish between three types of clusters: criminal clusters with known money laundering oﬀenses, criminal clusters without known money laundering activities, and clusters for which no criminal events are recorded at all.

[p. 3]

Large empirical datasets are usually scarce for criminological research in general, and in particular for studying criminal networks. The newly developed methodological approach applied in this paper can overcome this limitation and eventually increase our understand- ing of the behavior of criminals and the dynamics of social (criminal) network formation. Knowing how criminal networks respond to anti-money laundering policies helps regula- tors to design more eﬀective and eﬃcient policies. Increased knowledge on the formation of criminal networks also helps enforcement authorities improve the tools available for detection and investigation.

In general, AML policies are often accused of having high costs but not many visible beneﬁts [4–6]. Studies about AML eﬀectiveness often try to look whether money laun- dering decreases and use dark number estimation techniques with their accuracy being questionable, as well as the usefulness of the gained knowledge [7]. The method presented in this paper does not use such dark numbers estimations but is based on high quality ad- ministrative data instead. Our theoretical contribution adds to the literature on criminal networks through embedding the behavioral aspects of specialization, competition and collaboration. Empirically we test this by using a unique dataset from iCOV, the infobox Crimineel en Onverklaarbaar Vermogen, a collaboration between several Dutch author- ities to share information on criminal and unexplainable wealth. In addition, this study also theoretically contributes to the literature by developing a methodology to identify the eﬀects of AML policy measures using temporal cluster analysis.

This paper is structured as follows. Section 2 provides a brief literature review about money laundering and criminal networks. Next, Sect. 3 discusses the conceptual frame- work regarding our network measures and our model for network analysis. Section 4 de- scribes the data used and Sect. 5 discusses the results. Finally, Sect. 6 concludes.

2 Literature review 2.1 Money laundering AML regulations generally aim to reduce secrecy and enforce transparency with know- your-customer responsibilities and duties to report suspicious transactions for the gate- keepers of the ﬁnancial sector such as banks and notaries. This additional information should help law enforcement agencies to detect and prosecute money laundering better. A comprehensive and detailed overview of the regulations is provided by Cox [7] and more condensed alternatives by Anderson [8] and Unger, Annex A.1 [9]. Within the European context several initiatives to combat money laundering have been implemented following Financial Action Task-Force (FATF) recommendations [3, 10–15].

There are several studies on the eﬀectiveness of AML regulations. Examples are pub- lications focusing on AML policies within the European Union [16], within developing countries [17], and comparing Singapore, Switzerland, and the UK [18].

[pp. 3-4]

Money laundering is an interdisciplinary ﬁeld of research. Lawyers, political scientists, and public policy scholars traditionally focus on the development, implementation and

execution of anti-money laundering policies, e.g. [19–21]. Criminologists typically study the behavior of money launderers, e.g. [22–24]. Economists tend to focus on analyzing the impact of money laundering on society and estimating the amount of money being laundered, e.g. [2, 25, 26].

If money laundering is policy relevant, it has to be a sizable problem with a huge im- pact on either the economy, society or politics, which legitimizes anti money laundering policy interventions. And if anti money laundering policy is eﬀective, there should exist less money laundering over time, or at least a visible impact of this policy, such as de- tecting more money laundering activities, catching more launderers or conﬁscating more laundered money.

The literature focusing on the size of the problem by estimating the amount of money being laundered uses diverse techniques (see for a good overview Sect. 1 in [27]) ranging from more qualitative research methods like case studies, surveys, and interviews to quan- titative studies like the currency demand [28] or the DYMIMIC [29] approach, and trade based quantitative models that analyse the expected extent of trade, and trade-pricing diﬀerences [30], or that use a gravity model [31, 32]. Ferwerda et al. [2] estimate all global money laundering ﬂows at the bilateral level with such a gravity model. Although the es- timates diﬀer as much as their approaches, money laundering is generally seen as a large global phenomenon that can only be countered using a multi-disciplinary multi-national approach [33].

Grouped in 25 categories within a literature review, Ferwerda [26] identiﬁes 86 diﬀerent economic, social, and political eﬀects that money laundering can have on the real, ﬁnan- cial, and public sector. This indicates the importance of countering money laundering and helps setting the research agenda. Most of the eﬀects mentioned in the literature have not yet been empirically tested, though.

[pp. 4-5] [ref: 2.2]

Besides the amount of money being laundered and the signiﬁcance of this problem, an- other strand of research aims at detecting laundering activities. For instance, some ap- plied research uses machine learning within the banking system to detect potential money laundering activities [34]. Gao and Ye [35] review machine learning techniques that can improve the eﬃciency of money laundering detection, and promotes the use of network analysis? centrality measures to destabilize money laundering networks, as also promoted by e.g. Baker and Faulkner [36]. Duijn et al. [37] show that this can have adverse eﬀects, by strengthening the networks instead.

Analyzing social networks, Fronzetti Colladon and Remondi [38] provide insights into the structural position and detection of high-risk money laundering proﬁles within the scope of a factoring company. They collected only 19 months of data and therefore cannot explore the long-term eﬀects of AML regulation. We use the same structural measures, not for detecting potential laundering activities, but for analyzing the eﬀects of AML pol- icy.

2.2 Criminal organizations and dark networks Due to the evolving AML and law enforcement policies aforementioned, criminal orga- nizations have to navigate in an increasingly complex environment. This requires inno- vations in money laundering methods, the use of new technologies, and higher levels of international cooperation. Such developments can lead to changes in the structures

and competences of criminal organizations and dark networks in general and the associ- ated network indicators, especially for networks involving money laundering. For exam- ple, based on interviews with arrested drug criminals, Benson and Decker [39] argue that revenue-generating criminal organizations are, in contrast to what is believed about them, not highly hierarchically structured. Instead, they often consist of small isolated groups without any formal connections. Raab and Milward [40] point out that dark networks are dealing with two competing and contradictory needs of secrecy and information- processing. Since concealment tends to be more important, illegal networks have a ten- dency toward a decentralized structure unless the task necessitates a centralized one [41]. From a transnational perspective, Williams [42] states that organized crime is “increas- ingly operating through ﬂuid network structures rather than more formal hierarchies”. Additionally, these papers show that criminal networks typically have both a core (strongly connected by friendship and family ties) and a less dense periphery which enables diversity and geographic coverage.

[p. 5]

Although the popularity and maturity of social network analysis is continuously grow- ing, such analyses are rarely applied in the study of criminal networks. Caused by the nature of criminal networks, several major problems for network analysis occur, being: (i) the amount of data and computational power needed, (ii) the covertness of criminal ac- tivities rendering data incomplete, (iii) ambiguities due to mixing criminal and legitimate activities and actors, causing fuzzy boundaries, and (iv) the timing of network interactions changing the strengths of ties, making detection algorithms report diﬀerent results over time [43]. Given that this paper was written almost 30 years ago, technological develop- ments can almost fully eliminate the ﬁrst argument.

Social network analysis within the ﬁeld of criminology has emerged rapidly since 2005 [44] but has been primarily descriptive [45]. One such report on known criminal networks, which is very elaborate, provides insights into their organization and activities [46]. The United Nations Oﬃce on Drugs and Crime has identiﬁed ﬁve common network struc- tures: the standard, regional and clustered hierarchies, the core group, and criminal net- works [46]. The hierarchical structures are typically vertical in structure and are based on control and division of labour, while the other structures are more horizontally organized and based on trust and professional expertise. The core group construction is typically associated with tax fraud and money laundering, due to their strong connections with the legitimate economy, their small size, and high professional expertise. The core group con- struct typically consists of a small, strongly connected group of individuals, surrounded by participants that are unrelated to each other.

Based on empirical data from Columbian criminal organizations and the Italian Maﬁa, the UNODC [46] observed that law enforcement transformed several hierarchical struc- tures into core groups, making both typologies a common observation. An alternative explanation is that globalization has contributed similarly to crime as to legitimate busi- ness, by transforming hierarchical structures into more ﬂexible collaborative networks [47]. The observed developments therefore seem to be fully explained neither by stronger enforcement nor by globalization alone. Inconsistencies in the UNODC [46] report are also observed in the analysis of 40 known criminal organizations. Money laundering, or “having a strong connection with the legitimate economy”, is mentioned for 25 of these organizations, of which only ﬁve are considered to have ﬁnancial crimes as their main ob- jective. Another three groups are expected to have signiﬁcant links to money laundering

[p. 6] [ref: 2.3]

in addition to their regular criminal activities. Out of the ten criteria on which each crim- inal organization is proﬁled, money laundering is argued to be best ﬁtted for core groups with less than 20 people involved [46]. These groups portray little sense of identity, low amounts of violence, a strong penetration in the legitimate economy, and have access to a multitude of collaborators from other criminal organizations either within or outside their home country. Strangely though, when matching the six deﬁned characteristics for money laundering networks with the eight money laundering intensive organizations se- lected, only 18 out of the possible 47 match the criteria [46].

There are only a few papers dealing with the eﬀects of competition both within and between criminal networks. Most often, competition between criminals and regulators is analyzed, e.g. [48, 49]. Shifting the focus to competition and collaboration in public service delivery, Entwistle and Martin [50] propose three ﬁelds of interest, of which one can be applied speciﬁcally to the delivery of money laundering services: “encouraging trust may reduce conﬂict in relational exchange” (p. 237) [50]. Therefore, we expect decreasing trust when law enforcement agencies can force the constant rebuilding of relationships and trust. Contract self-enforcement within crime is frequently built on violence because neither legal enforcement nor police protection is a viable solution [51].

2.3 Criminal network structures and resilience Social network analysis plays an important role in determining key persons to target, and how to disrupt networks [40, 52, 53]. For example, people with a high degree centrality are more likely to get arrested than those with a high betweenness centrality. Morselli [54] explains these dynamics in terms of brokerage, which is found to be higher in more sophisticated and developed criminal organizations. In the ﬁeld of network analysis, the term brokerage is more technically referred to as “structural holes”, and usually provides competitive advantages in business networks [55]. Going even further back in time leads to similar insights into the importance of weak ties between groups versus the so-called strong ties within groups [56].

The risk of detection also inﬂuences the hierarchy of criminal networks. By studying criminal organizations in the Balkans, Stanojoska et al. [57] explain the need for horizon- tal and vertical division of roles. Vertical structures are aimed at protecting the criminal activities by reducing the knowledge known by each participant and hence a possible sell- out to the authorities. Horizontal role division is mainly related to specialization i.e. the complexity of the overall criminal activity. Horizontal structures are associated with high local autonomy, self-organizing governance, in-dividual reputation, reciprocity and trust, direct personal contacts, and consensus-based decision-making.

[pp. 6-7]

In general, there is a constant trade-oﬀbetween eﬃciency and security in criminal net- works. Security-focused networks tend to have a longer time-to-task span (i.e. eﬃciency is of lower importance), and centralities are more evenly distributed causing such networks to seemingly have no central players [58]. Actors in a criminal network can be purposely placed either strategically or vulnerably when the network is known to be under police scrutiny. Morselli [54] ﬁnds that members of a criminal network with higher levels of de- gree centrality (i.e. the number of connections to other members) have an increased prob- ability to be arrested while a higher betweenness centrality (i.e. the brokerage position of the respective member) decreases this possibility.

The structure of a network also inﬂuences its resilience. Ayling [59] deﬁnes resilience as “the capacity to absorb and withstand disruption and to adapt to change when nec- essary” (p. 182), and argues that temporal analyses of such organizations are required to understand this concept. She warns that (police) interventions may lead to worsening cir- cumstances [59], resilience of the networks increases. For example, using the concept of optimal criminal networks, based on the costs and beneﬁts of network ties supported by their simulation, Easton and Karaivanov [60] argue that removing key actors from a crim- inal network may counter-intuitively lead to a more optimized structure, especially when the law enforcement policies are known. Bramoullé et al. [61] ﬁnd that exogenously in- creasing the costs of crime (e.g. by implementing AML policies) may reduce the baseline level of crime, but it also increases the value of a (criminal) social network. In their re- search, this dynamic causes criminals to be isolated from a multitude of networks, which increases gang membership and its associated violence. In a similar fashion using Dutch Police data, Duijn et al. [37] conﬁrm police interventions can strengthen criminal network eﬃciency (i.e. reduced dimensionality) due to the removal of old ineﬃcient ties. Their study indicates that disrupting continuously and quickly, forces networks to become more redundant, making them better observable and reduces their secrecy and security. They argue that temporal analysis is needed to assess these eﬀects. Also Everton and Cunning- ham [62] highlight the potential of analyzing dark networks over time and detect changes.

McBride and Hewitt [63] show in a laboratory experiment that when network structures are not completely known, disruption eﬀorts should focus on actors in the network that are not monitored, even though this is risky (see also [64] for a discussion about the problems of fuzzy boundaries).

[pp. 7-8] [ref: 3.1]

With our temporary analysis of criminal and laundering networks we hope to contribute to this literature. Though we are aware of the ﬁndings of Milward and Raab [65] who conclude that disruption eﬀorts of dark networks will likely fail and dark networks stay resilient as long as the central problems behind their existence, such as larger societal and political problems, are not tackled.

3 Conceptual framework and model for network analysis Social network analysis terminology is relatively established in the literature, but opera- tionalization for criminal networks speciﬁcally requires some additional explanation (see Sect. 3.1 and Sect. 3.2). The hypotheses (Sect. 3.3) and their analysis approach (Sect. 3.4) are further explained.

3.1 Centrality measures In general, centrality measures provide insight into the inner workings of a network and the structural importance of individual nodes. These levels indicate, e.g. the extent to which there is a centralized level of control in a network or leadership, the distance that needs to be traveled between nodes in terms of eﬃcient communication patterns, or the ability of nodes to connect others.3

Degree centrality The degree centrality provides an indication to what extent a person is connected to others in the network. It is one of the most common measures in network

3Several crime-related examples are [43, 54, 66].

analysis and counts the number of edges a speciﬁc node has. In a criminal network, a high degree centrality can have the disadvantage of more exposure to the risk of getting caught [54].

Betweenness centrality Betweenness centrality, or brokerage, is linked to the importance of the node in connecting other nodes. It is deﬁned as the sum of shortest paths (geodesics) between any two nodes that include the node of interest. This measure can be normalized by dividing the betweenness centrality by the maximum number of geodesics possible [67]. According to Morselli [54], higher betweenness centralities ensure bigger network gains and, if money laundering services are scarce, launderers can sustain a prominent position with respect to their betweenness and larger gains.

Closeness centrality An indication to how close or distant one node is in comparison to all other nodes is assessed by the closeness centrality. Originally presented by Bavelas [68], closeness centrality is deﬁned as the reciprocal of the sum of all geodesics’ length between all nodes that include the node of interest and is typically associated with the ability to control a network [69]. When anti-money laundering policies intensify, money launderers in the network need more of such control to mitigate the increased risk of exposure.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Peter Gerbrands, Brigitte Unger, Michael Getzner, Joras Ferwerda, "The effect of anti-money laundering policies: an empirical network analysis" (2022-03-18). https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
