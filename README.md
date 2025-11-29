
During my postdoctoral research (2013 - 2018) I had studied proteins (very dynamic entities) as networks and published my findings in journal papers for a class (structurally homologous) of proteins. These are coarse-grained (molecular level) or fine-grained (atomic level) models to study protein dynamics. And I did it with [python](http://prody.csb.pitt.edu/tutorials/enm_analysis/)

<img width="287" alt="1" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/c5f569bd-69ef-42b9-aaf3-ec9d817d405c">

I utilized elastoc network model (ENM) or anisotropic network model (ANM) to figure out the conformational flexibility essential for the proteins to (specific) function. 

Having shifted my research focus from Mathematical Physics to Biophysics, little did I realize at that time that 'Network Science' is relevant for other systems too, like social media, logistics & transportation, recommenders. 

When I come to think of it, it is only about knowing how to connect the nodes in a complex world. It’s no surprise at all that the importance of hashtag#networks is ever-growing.

**Chapter 6** called **Graph Theory** in my book [*A handbook of mathematical models with python*](https://ranja-sarkar.github.io/) talks about graphs, graph-structured data, and how they serve as inputs to graph neural networks (GNNs). 

<img width="299" alt="3" src="https://github.com/ranja-sarkar/networks-graphs/assets/101544669/be422333-5db9-4afb-90c6-b2150109aef6">

-----

**Studying a protein with an elastic network model (ENM) that includes coarse-grained Gaussian network model (GNM) and atomic anisotropic network model (ANM):**

https://www.pnas.org/doi/full/10.1073/pnas.0902159106

https://www3.mpibpc.mpg.de/groups/de_groot/pdf/Hayward_deGroot_nm_ed.pdf

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6320916/

-----



1) **Paper 1**: https://link.springer.com/article/10.1186/s13628-017-0034-9
   
2) **Paper 2**: https://www.sciencedirect.com/science/article/abs/pii/S0025556417303140

------

# OTHER USE CASES

📌 Most optimal flight routes in terms of distance & airtime using **Dijkstra algorithm** from (weighted) graphs

<img width="464" alt="ff" src="https://github.com/user-attachments/assets/b38b587e-ac0b-4603-90ca-a596da47feab" />

The Dijkstra algorithm for a graph geodesic is in [the Wolfram webpage](https://mathworld.wolfram.com/DijkstrasAlgorithm.html).

**For many decades, Dijkstra's algorithm has been the undisputed champion for finding the shortest path in graphs. However, the first major breakthrough for the directed Single-Source Shortest Path (SSSP) problem on real-weighted graphs, breaking the long-standing "sorting barrier" that made Dijkstra's algorithm seem optimal arrived in [2025](https://arxiv.org/pdf/2504.17033).**

The method ingeniously combines the logic of Dijkstra's and the Bellman-Ford algorithms. Through a clever recursive technique, it avoids the need to fully sort vertices by distance which was the bottleneck. The result is a [faster](https://ranjas.substack.com/p/data-structures-and-algorithms), deterministic algorithm that runs in O(mlog2/3n) time. This has practical implications for speeding up route calculations in GPS, optimizing data flow in computer networks, and improving efficiency in logistics. 

💡 A fundamental problem just got a new, faster solution.

-----

📌 **Knowledge graphs** ([directed](https://colab.research.google.com/drive/1EF_ra7u6qHqG5p5vmYDYC9X5Y06hsub7)) from unstructured data (document, web, etc.)

📌 **Social network analysis** with graphs from your [data of connections](https://github.com/ranja-sarkar/networks-graphs/blob/444b74e376a707b09870ddfe6e282da526f1a75d/notebook/graphs-network.ipynb) on social networking site

📌 **Operations research (OR)** problems like routing, packing, etc.are solved utilizing [mathematical optimization](https://developers.google.com/optimization)


