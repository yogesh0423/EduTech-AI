import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import requests


def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()['embeddings']
    return embedding


df = joblib.load('embeddings.joblib')



incoming_query = input("Ask a Question:  ")
question_embedding = create_embedding([incoming_query])[0]
# print(f"Question Embedding: {question_embedding}")


# Calculate cosine similarity between the question embedding and all chunk embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
print(f"Similarities: {similarities}")

top_results = 5  
max_indx = similarities.argsort()[::-1][0:top_results]  # Indices of chunks sorted by similarity (highest first)
print(max_indx)
new_df = df.loc[max_indx]
print(new_df[['id','title','text']])  
