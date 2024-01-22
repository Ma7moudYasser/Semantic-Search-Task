# Semantic-Search-Task
This GitHub repository contains a semantic search application implemented using the SentenceTransformer model. The project integrates Flask for building a web interface and Pyngrok for exposing the local Flask server to the internet.

You can find the model directory [here](https://drive.google.com/drive/folders/1osUmMcWjSixdSRD2lJyDaS-eM0qOrqMH?usp=sharing) 
# Project Documentation

# Introduction
This project focuses on implementing a semantic search model using Sentence Transformers, specifically the 'LaBSE' model. The primary aim is to create a search engine capable of retrieving relevant sentences from a corpus of articles. The dataset used for this task is sourced from the 'articles.csv' file, which contains articles in different languages.

# Data Description:
The dataset, loaded from 'articles.csv', comprises articles with multiple sentences in various languages. For simplicity, the project uses the first 200 sentences for encoding. The goal is to generate embeddings for each sentence in the corpus using the 'LaBSE' model.

# The project is deployed through using Flask and ngrok


![Home page](https://github.com/Ma7moudYasser/Semantic-Search-Task/assets/57537704/2966e89c-07fd-469a-8d6a-897251d624c8)



![semantic results](https://github.com/Ma7moudYasser/Semantic-Search-Task/assets/57537704/8ec489a0-d0ef-4197-94f3-916a28821c2d)
