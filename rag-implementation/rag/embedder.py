import cohere
import os


with open(".\credentials.txt") as f:
    API_KEY = f.read().strip()
API_KEY = API_KEY.split("=")[1].strip().strip('"')


co = cohere.Client(API_KEY)

def embed_texts(texts):
    response = co.embed(
        texts=texts,
        model="embed-english-v3.0",
        input_type="search_document"
    )
    return response.embeddings

def embed_query(query):
    response = co.embed(
        texts=[query],
        model="embed-english-v3.0",
        input_type="search_query"
    )
    return response.embeddings[0]

def generate_text(prompt):
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=300
    )
    return response.generations[0].text