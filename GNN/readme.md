An excerpt from **Chapter 6** of my book:

<img width="285" alt="00" src="https://github.com/user-attachments/assets/c405b727-d5d6-45b7-a078-b1dcbd6de7fc">


**Deep learning architectures** like the following are all Graph Neural Networks (GNNs) at their core. 


GNNs on graphs with translational symmetry in all dimensions are **CNNs (Convolutional Neural Networks)**.

<img width="533" alt="11" src="https://github.com/user-attachments/assets/524b4680-fb94-4384-8ceb-876e2c5ab8af">


GNNs on one-dimemsional directed line graph (which dictates how the tokens of a sentence flow in for instance) are **RNNs (Recurrent Neural Networks)**.

<img width="461" alt="22" src="https://github.com/user-attachments/assets/54e1644e-1a26-48d8-88e0-e562cc2c627b">



The self-attention mechanism in decoders of **transformers** can be viewed as a neural network on a fully connected graph on all tokens of the context window. 

<img width="508" alt="44" src="https://github.com/user-attachments/assets/145b6eed-fe4d-42db-bde8-cbda03b0665a">


For causal self-attention, it can be thought of as special directed graph where one token is connected to all previous tokens 
in the context window.

<img width="303" alt="33" src="https://github.com/user-attachments/assets/695aab44-e1a9-4f47-b45e-ceb620f15248">


**Outside of the core network architecture, graphs can push the performance of model by giving it access to additional knowledge about the world.** 

Retrieval augmented generation (RAG) currently is a go-to approach to reduce hallucination of LLMs by giving them access to new information.
Typically this is done by text or tabular data identified via vector similarity. However, data stored in graph databases is much better suited as input here, due to their ability to provide the complex relationships between data objects. This is why systems leveraging **graphRAG** are on the rise.


