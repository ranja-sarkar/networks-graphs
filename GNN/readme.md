
**Deep learning architectures that are GNNs at the core**:-

-> **CNN**

GNNs on graphs with translational symmetry in all dimensions are Convolutional Neural Networks.

<img width="533" alt="11" src="https://github.com/user-attachments/assets/524b4680-fb94-4384-8ceb-876e2c5ab8af">


-> **RNN**
GNNs on one-dimemsional directed line graph dictating how the tokens of a sentence flow in are RNNs.

-> **Transformer**
The self-attention mechanism in decoders can be viewed as a neural network on a fully connected graph on all tokens of the context window. 
For causal self-attention, it can be thought of as special directed graph where one token is connected to all previous tokens 
in the context window.

Outside of the core network architecture, graphs can push the performance of model by giving it access to additional knowledge about the world. 
Retrieval augmented generation (RAG) currently is a go-to approach to reduce hallucination of LLMs by giving them access to new information.
Typically this is done by text or tabular data identified via vector similarity. 
On the other hand, data stored in graph databases is much better suited as input here, due to their ability to provide the complex relationships 
between data objects. This is why systems leveraging graphRAG are on the rise.
