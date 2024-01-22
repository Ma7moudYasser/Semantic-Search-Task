from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util
from pyngrok import ngrok
import pandas as pd
import torch
import time
import os

app = Flask(__name__)

#setting the auth token for ngrok
ngrok.set_auth_token('2bGNhxtmw4FNSHnRghEXqpvYD7e_7NRqeyCSCpT9n2ce6Zv66')



# Start the ngrok when the app is running 
# Start Ngrok when the app is run
public_url = ngrok.connect(5000)

# Load SentenceTransformer model
model_path = 'C:/Users/20109/Downloads/assignment/Semantic_keywords/model_directory'
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
    print(' * Running on', public_url)
    app.run(debug=True)
