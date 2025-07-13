# custom-chatbots

rag-implementation/
│
├── data/
│   └── sample.pdf          # Place your PDFs here
│
├── chromadb_data/          # ChromaDB persists vector store here (auto created)
│
├── rag/
│   ├── __init__.py
│   ├── pdf_parser.py       # PDF parsing & chunking
│   ├── embedder.py         # Cohere embedding logic
│   ├── vector_store.py     # ChromaDB init & store/query
│   ├── agent.py            # The RAG agent that generates answers
│
├── main.py                 # Entry point to index & query
│
├── requirements.txt        # Dependencies
└── README.md               # How to run it
