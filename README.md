# Semantic-Search-Task
This GitHub repository contains a semantic search application implemented using the SentenceTransformer model. The project integrates Flask for building a web interface and Pyngrok for exposing the local Flask server to the internet.

You can find the model directory [here](https://drive.google.com/drive/folders/1osUmMcWjSixdSRD2lJyDaS-eM0qOrqMH?usp=sharing) 
# Project Documentation

# Introduction
This project focuses on implementing a semantic search model using Sentence Transformers, specifically the 'LaBSE' model. The primary aim is to create a search engine capable of retrieving relevant sentences from a corpus of articles. The dataset used for this task is sourced from the 'articles.csv' file, which contains articles in different languages.

# Data Description:
The dataset, loaded from 'articles.csv', comprises articles with multiple sentences in various languages. For simplicity, the project uses the first 200 sentences for encoding. The goal is to generate embeddings for each sentence in the corpus using the 'LaBSE' model.


# Baseline Experiments:

The baseline experiments involve encoding the corpus using Sentence Transformers and the 'LaBSE' model. The embeddings are created for the first 200 sentences in the dataset. The corpus_embeddings variable holds the encoded representations of these sentences.

# Search Function:

A search function is implemented to query the corpus and retrieve relevant results. This function takes a user's input question, encodes it using the same 'LaBSE' model, and performs semantic search in the corpus.

![Screenshot 2024-01-22 114315](https://github.com/Ma7moudYasser/Semantic-Search-Task/assets/57537704/b0e852ad-dbc8-4a31-9e80-e79ce1869ad8)


# The project is deployed through using Flask and ngrok
The model is deployed using Flask, and Ngrok is utilized for exposing the local Flask server to the internet. Deployment involves making the search functionality accessible on the web form

## Deployment Demo
![Home page](https://github.com/Ma7moudYasser/Semantic-Search-Task/assets/57537704/2966e89c-07fd-469a-8d6a-897251d624c8)


## Deployment Demo
![semantic results](https://github.com/Ma7moudYasser/Semantic-Search-Task/assets/57537704/8ec489a0-d0ef-4197-94f3-916a28821c2d)



## Challenges faced in the project
The biggest challenge which I have faced was the problem itself as it is the first time for me to tackle the semantic search problem but I have read serveral articles about this topic, and I have seen different videos.

## Resources and learning

1. [Pinecone NLP Series](https://www.pinecone.io/learn/series/nlp/) \\
   An excellent resource for understanding Natural Language Processing (NLP) concepts relevant to semantic search.

2. [Medium Article: Semantic Search Engine using NLP](https://medium.com/analytics-vidhya/semantic-search-engine-using-nlp-cec19e8cfa7e) \\
   A comprehensive article providing insights into building a semantic search engine using NLP techniques.

3. [Zilliz Glossary: Semantic Search](https://zilliz.com/glossary/semantic-search) \\
   Explore a glossary of terms related to semantic search for a deeper understanding of the concepts.

4. [YouTube: Semantic Search Explained](https://www.youtube.com/watch?v=fFt4kR4ntAA) \\
   A video tutorial explaining the fundamentals of semantic search.

5. [YouTube: Sentence Transformers Tutorial](https://www.youtube.com/watch?v=sHBwRfh9c54) \\
   A tutorial on using Sentence Transformers for various NLP tasks, including semantic search.

6. [Sentence Transformers Documentation - Semantic Search Example](https://www.sbert.net/examples/applications/semantic-search/README.html) \\
   Refer to the official Sentence Transformers documentation for a hands-on example of implementing semantic search.



   # Conclusion
In conclusion, the semantic search task aimed to enhance information retrieval by leveraging advanced techniques in natural language processing (NLP). The utilization of the Sentence Transformers library, specifically the 'LaBSE' model, provided a robust foundation for encoding textual information into semantically meaningful embeddings.
The deployment of the semantic search model using Flask and Ngrok showcased the practical application of the developed solution. By exposing the search functionality through an API endpoint, the model became accessible for integration into various applications, extending its usability beyond the scope of the initial experiments.
