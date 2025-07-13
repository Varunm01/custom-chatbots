from chromadb import PersistentClient

client = PersistentClient(path="./chromadb_data")

collection = client.get_or_create_collection("pdf_chunks")

def store_chunks(chunks, embeddings):
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks
    )

def query_chunks(query_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0]
