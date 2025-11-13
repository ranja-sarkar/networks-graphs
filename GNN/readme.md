
For neural networks in general, read https://ranjas.substack.com/p/hyper-parameters-of-a-neural-network

Introducing GNNs: https://distill.pub/2021/gnn-intro/


# CNN

GNNs on graphs with translational symmetry in all dimensions are CNNs (Convolutional Neural Networks).

<img width="533" alt="11" src="https://github.com/user-attachments/assets/524b4680-fb94-4384-8ceb-876e2c5ab8af">


# RNN 

GNNs on one-dimemsional directed line graph are RNNs (Recurrent Neural Networks).

<img width="461" alt="22" src="https://github.com/user-attachments/assets/54e1644e-1a26-48d8-88e0-e562cc2c627b">


# Transformer

The self-attention mechanism in a decoder in the transformer architecture can be viewed as GNN that is, a neural network on a fully connected graph on all tokens of the context window. 

<img width="508" alt="44" src="https://github.com/user-attachments/assets/145b6eed-fe4d-42db-bde8-cbda03b0665a">


For causal self-attention, it can be thought of as a (special) directed graph where one token is connected to all previous tokens in the context window.

<img width="303" alt="33" src="https://github.com/user-attachments/assets/695aab44-e1a9-4f47-b45e-ceb620f15248">

-----------

Retrieval augmented generation (RAG) currently is a go-to approach to reduce hallucination of LLMs by giving them access to new information via vector databases and graph databases. Typically this is done by identification of data via vector similarity from vector databases however, data stored in graph databases is better suited as input due to their ability to provide the complex relationships between data objects. This is why systems leveraging **graphRAG** are on the rise.


