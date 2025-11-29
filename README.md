
During my postdoctoral research (2013 - 2018) I had studied the very dynamic **proteins** as [networks](https://www.pnas.org/doi/full/10.1073/pnas.0902159106) and published my findings in journal papers for a class (structurally homologous) of proteins. These are [coarse-grained](https://pmc.ncbi.nlm.nih.gov/articles/PMC6320916/) (molecular level) or fine-grained (atomic level) network models to study protein dynamics. And I did it with [python](http://prody.csb.pitt.edu/tutorials/enm_analysis/). Another open-source resource is [R](http://thegrantlab.org/bio3d_v2/tutorials/normal-mode-analysis/) that can be used to study native dynamics of proteins.

<img width="287" alt="1" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/c5f569bd-69ef-42b9-aaf3-ec9d817d405c">

I utilized elastic network model (ENM) and atomic anisotropic network model (ANM) to figure out protein conformational flexibility essential for the proteins in that class to function. I had to [leverage Principal component analysis](https://www.cell.com/biophysj/fulltext/S0006-3495(14)01570-7) (PCA) also to understand the [normal modes or equilibrium conformations](https://www3.mpibpc.mpg.de/groups/de_groot/pdf/Hayward_deGroot_nm_ed.pdf) of the proteins.

📌 My papers:

1. [Native flexibility of structurally homogous proteins](https://link.springer.com/article/10.1186/s13628-017-0034-9)

2. [Stiffening of flexible SUMO1 protein upon peptide-binding: Analysis with ANM](https://www.sciencedirect.com/science/article/abs/pii/S0025556417303140)

-----

*Having shifted my research focus from Mathematical Physics (doctoral) to Biophysics (postdoctoral), little did I realize at that time that **Network Science** is relevant for other systems like social media, logistics & transportation, recommenders. When I come to think of it, it only takes knowing how to connect the nodes (entities) with edges (relationships) in a complex world. It is no surprise at all that the importance of networks is ever-growing.*

-----

**Chapter 6** (**Graphs**) of my book [*A handbook of mathematical models with python*](https://ranja-sarkar.github.io/) published in 2023 is dedicated to graphs and networks, graph-structured data, and how these structures of text, images etc. serve as inputs to graph neural networks (GNNs). 

<img width="299" alt="3" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/be422333-5db9-4afb-90c6-b2150109aef6">

-----

# OTHER USE CASES

📌 Optimal flight routes in terms of distance & airtime using **Dijkstra algorithm** from ([**weighted**](https://distill.pub/2021/gnn-intro/)) graphs

<img width="464" alt="ff" src="https://github.com/user-attachments/assets/b38b587e-ac0b-4603-90ca-a596da47feab" />

The Dijkstra algorithm for a graph geodesic is in [the Wolfram webpage](https://mathworld.wolfram.com/DijkstrasAlgorithm.html).

**For many decades, Dijkstra's algorithm has been the undisputed champion for finding the shortest path in graphs. However, the first major breakthrough for the directed Single-Source Shortest Path (SSSP) problem on real-weighted graphs, breaking the long-standing "sorting barrier" that made Dijkstra's algorithm seem optimal arrived in [2025](https://arxiv.org/pdf/2504.17033).**

The method ingeniously combines the logic of Dijkstra's and the Bellman-Ford algorithms. Through a clever recursive technique, it avoids the need to fully sort vertices by distance which was the bottleneck. The result is a [faster](https://ranjas.substack.com/p/data-structures-and-algorithms), deterministic algorithm that runs in O(mlog2/3n) time. This has practical implications for speeding up route calculations in GPS, optimizing data flow in computer networks, and improving efficiency in logistics. 

💡*A fundamental problem just got a new & faster solution*.

-----

📌 **Knowledge graphs** ([directed](https://colab.research.google.com/drive/1EF_ra7u6qHqG5p5vmYDYC9X5Y06hsub7)) from unstructured data (document, web, etc.)

📌 **Social network analysis** with graphs from your [data of connections](https://github.com/ranja-sarkar/networks-graphs/blob/444b74e376a707b09870ddfe6e282da526f1a75d/notebook/graphs-network.ipynb) on social networking site

📌 **Operations research (OR)** problems like routing, packing, etc.are solved utilizing [mathematical optimization](https://developers.google.com/optimization)


