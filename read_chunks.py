import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()['embeddings']
    return embedding



jsons = os.listdir("jsons")       # List all the jsons
# print(jsons) 
my_dict = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}", "r") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}...")
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk['id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dict.append(chunk)
        
    
# print(my_dict)

df = pd.DataFrame.from_records(my_dict)
# print(df)


incoming_query = input("Ask a Question:  ")
question_embedding = create_embedding([incoming_query])[0]
# print(f"Question Embedding: {question_embedding}")


# Calculate cosine similarity between the question embedding and all chunk embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
print(f"Similarities: {similarities}")
max_indx = similarities.argsort()[::-1]  # Indices of chunks sorted by similarity (highest first)
print(max_indx)

top_k = 5
top_indices = similarities.argsort()[::-1][:top_k]

print("\nTop Results:\n")

for idx in top_indices:
    print("=" * 80)
    print(f"Similarity: {similarities[idx]:.4f}")
    print(df.iloc[idx]["text"])