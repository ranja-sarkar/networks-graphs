
Graphs are fundamental mathematical structures, representing objects (or nodes) and their connections (or edges). Networks are graphs with added meaning like weights or directions, used to model real-world systems from social connections to biomacromaolecules. Networks have vertices (or nodes) linked by relationships (or edges) providing tools to understand complex systems in various fields.

<img width="299" alt="3" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/be422333-5db9-4afb-90c6-b2150109aef6">

During my postdoctoral research (2013 - 2018) I had studied proteins as [networks](https://www.pnas.org/doi/full/10.1073/pnas.0902159106). Proteins are very dynamic entities and I studied their dynamics with [coarse-grained](https://pmc.ncbi.nlm.nih.gov/articles/PMC6320916/) (molecular level) and fine-grained (atomic level) network models. I published my findings in journal papers 👇 for a class of structurally homologous proteins. 

Having shifted my research focus from Mathematical Physics (doctoral) to Biophysics (postdoctoral), I did not really realize at that time that **Network Science** is relevant for other systems like social media, logistics & transportation, recommenders as well. When I come to think of it now, it only takes knowing how to connect the nodes with edges in a complex world. It is no surprise at all that the importance of networks is ever-growing.

---

I used the python package [Prody](http://prody.csb.pitt.edu/tutorials/enm_analysis/) for my study on proteins. Another open-source resource is [Bio3D](http://thegrantlab.org/bio3d_v2/tutorials/normal-mode-analysis/) that uses R, and explores the native dynamics of proteins.

<img width="287" alt="1" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/c5f569bd-69ef-42b9-aaf3-ec9d817d405c">

I utilized elastic network model (ENM), and anisotropic network model (ANM) at the atomic level to study conformational flexibility of proteins or their [equilibrium structures](https://mode-task.readthedocs.io/en/latest/theory.html). Flexibility in conformations is essential for the proteins to function. I leveraged [principal component analysis (PCA)](https://www.cell.com/biophysj/fulltext/S0006-3495(13)03575-3) to understand their [normal modes](https://www3.mpibpc.mpg.de/groups/de_groot/pdf/Hayward_deGroot_nm_ed.pdf). For proteins, normal mode analysis is useful to study the large amplitude motions for a selected conformation. 

My publications - 

1. [Native flexibility of structurally homologous proteins](https://link.springer.com/article/10.1186/s13628-017-0034-9)

2. [Stiffening of flexible SUMO1 protein upon peptide-binding: Analysis with ANM](https://www.sciencedirect.com/science/article/abs/pii/S0025556417303140)


**Chapter 6** (Graphs) of my book [A handbook of mathematical models with python](https://ranja-sarkar.github.io/) published in 2023 is dedicated to graphs and networks. It is about how graph data structures serve as input to [graph neural networks (GNNs)](https://distill.pub/2021/gnn-intro/). 

<img width="322" height="125" alt="11" src="https://github.com/user-attachments/assets/666c72ea-b711-4c95-b847-3cfaad799c1c" />

It is mentionworthy that **all neural networks are networks, but all networks are not neural**. 
In neural networks, there is one input layer of nodes, (one or multiple) hidden layer (s) of nodes, and an output layer of one or multiple nodes. All or not all nodes of the input and hidden layers are linked, the input and output layers are indirectly connected via the hidden layer.

<img width="149" height="179" alt="nn" src="https://github.com/user-attachments/assets/53367291-5d2d-4a62-b9ee-1bcc02dcdb04" />

-----

# Where else are networks/graphs used?

They are used to represent complex systems visually and mathematically. They are used to find shortest paths like in GPS. They are also used to develop efficient ways of solving optimization problems.

📌 Finding optimal flight routes in terms of distance & airtime, with [Dijkstra algorithm](https://mathworld.wolfram.com/DijkstrasAlgorithm.html) used for a graph geodesic 

<img width="464" alt="ff" src="https://github.com/user-attachments/assets/b38b587e-ac0b-4603-90ca-a596da47feab" />

---

*For many decades, Dijkstra's algorithm has been the undisputed champion for finding the shortest path in graphs. However, the first major breakthrough for the directed Single-Source Shortest Path (SSSP) problem on real-weighted graphs, breaking the long-standing "sorting barrier" that made Dijkstra's algorithm seem optimal arrived in [2025](https://arxiv.org/pdf/2504.17033).* A fundamental problem just got a new & faster solution. 

The method ingeniously combines the logic of Dijkstra's and the Bellman-Ford algorithms. Through a clever recursive technique, it avoids the need to fully sort vertices by distance which was the bottleneck. The result is a faster (reducing time complexity) and deterministic algorithm. This has practical implications for speeding up route calculations in GPS, optimizing data flow in computer networks, and improving efficiency in logistics. 

---

📌 Developing [knowledge graphs](https://colab.research.google.com/drive/1EF_ra7u6qHqG5p5vmYDYC9X5Y06hsub7) from unstructured data (documents, web, etc.)

A knowledge graph makes data more valuable by extracting, connecting, and serving up knowledge. It provides structure and context, so AI can reason with more accuracy and transparency. 

[Deciding what belongs in the graph](https://aijourn.com/prioritizing-data-lake-information-to-build-a-knowledge-graph-aka-dont-boil-the-whole-lake/) is the most important step. This is knowing what nodes or features (and their edges) are necessary, there maybe nodes which are not supported due to missing data, etc.. The first layer in the network might represent a small fraction of all the data (knowledge is signal, not noise). Layers are connected to it when value emerges, gradually expanding the model by adding new data sources to address other business problems. Essentially, a knowledge graph lets us focus on the macroscopic level first, then addition of layers is focusing on the microscopic or granular events as and when demanded by the business. 

📌 Solving operations research (OR) problems like routing, [packing](https://github.com/ranja-sarkar/Optimization-NOGD/blob/443c4fe051343b33fe8c16aa878c5b9b97f2b9d3/knapsack_problem.md), scheduling, utilizing [mathematical optimization](https://developers.google.com/optimization) (Google OR-Tools)

A network flow can be represented by a graph whose nodes are cities and whose arcs (links) are rail lines between them. Network flow problems involve transporting goods or material across a network, such as a railway system. They are called flows because their properties are similar to those of water flowing through a network of pipes. A key constraint in network flows is that each arc has a capacity of the maximum amount that can be transported across it in a fixed period of time. The maximum flow problem is to determine the maximum (total) amount that can be transported across all arcs in the network, subject to the capacity constraint.


📌 Analysis of [social networks](https://github.com/ranja-sarkar/networks-graphs/blob/444b74e376a707b09870ddfe6e282da526f1a75d/notebook/graphs-network.ipynb)

Social networks represent relationships involving social entities such as friendships among individuals, communication in a group, or transactions between corporations. Finding important actors, discovering cohesive groups/communities, or identifying actors that are similar in some way are examples of analysis that can be done for social networks. Social networks are accessible from a variety of sources, including directly from networking sites (Linkedin, Facebook, etc.). The analysis of such networks makes it possible to rank actors from their centralities, or provide recommendations based on similar actors, etc..

-----

The subject that expresses and understands real-world systems as a network is Network Science.

<img width="226" height="188" alt="net" src="https://github.com/user-attachments/assets/d37ee910-5a70-40de-88d7-257fe38ba713" />




