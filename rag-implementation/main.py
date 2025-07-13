from rag.pdf_parser import extract_text_from_pdf, chunk_text
from rag.embedder import embed_texts
from rag.vector_store import store_chunks
from rag.agent import answer_question

def index_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)
    store_chunks(chunks, embeddings)
    print(f"Indexed {len(chunks)} chunks.")

def ask(question):
    answer = answer_question(question)
    print("Answer:", answer)

if __name__ == "__main__":
    index_pdf("data/git-cheat-sheet-education.pdf")

    ask("How to create a new branch in Git?")
