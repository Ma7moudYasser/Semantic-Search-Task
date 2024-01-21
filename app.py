from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import time
import os

app = Flask(__name__)

# Load SentenceTransformer model
model_path = 'C:/Users/hp/Downloads/cyshield task/Semantic_keywords/NLP-main/Semantic Search/model_directory/sentence_transformer_model'
model = SentenceTransformer(model_path)

# Load corpus embeddings
embeddings_path = 'C:/Users/hp/Downloads/cyshield task/Semantic_keywords/NLP-main/Semantic Search/model_directory/corpus_embeddings.pth'
corpus_embeddings = torch.load(embeddings_path)

# Load paper texts
df = pd.read_csv('article_titles.csv')
paper_texts = df['Titles'].to_list()

def search(inp_question):
    start_time = time.time()
    question_embedding = model.encode(inp_question, convert_to_tensor=True)
    hits = util.semantic_search(question_embedding, corpus_embeddings)
    end_time = time.time()
    hits = hits[0]  # Getting the hit of the first query

    results = []
    for hit in hits[0:10]:
        score = hit['score']
        document = paper_texts[hit['corpus_id']]
        results.append({"score": score, "document": document})

    return {
        "input_question": inp_question,
        "time_taken": end_time - start_time,
        "results": results
    }

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/search', methods=['POST'])
def search_route():
    query = request.form['query']
    if query:
        result = search(query)
        return render_template('search_results.html', result=result)
    else:
        return render_template('index.html', error='Please enter a valid question.')

if __name__ == '__main__':
    app.run(debug=True)
