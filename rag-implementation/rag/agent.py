from .embedder import embed_query, generate_text
from .vector_store import query_chunks

def answer_question(question):
    query_embedding = embed_query(question)
    relevant_chunks = query_chunks(query_embedding)
    context = "\n".join(relevant_chunks)
    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    answer = generate_text(prompt)
    return answer
