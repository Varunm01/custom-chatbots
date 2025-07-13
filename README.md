# custom-chatbots
<br>
rag-implementation/<br>
│<br>
├── data/<br>
│   └── sample.pdf          # Place your PDFs here<br>
│<br>
├── chromadb_data/          # ChromaDB persists vector store here (auto created)<br>
│<br>
├── rag/<br>
│   ├── __init__.py<br>
│   ├── pdf_parser.py       # PDF parsing & chunking<br>
│   ├── embedder.py         # Cohere embedding logic<br>
│   ├── vector_store.py     # ChromaDB init & store/query<br>
│   ├── agent.py            # The RAG agent that generates answers<br>
│<br>
├── main.py                 # Entry point to index & query<br>
│<br>
├── requirements.txt        # Dependencies<br>
└── README.md               # How to run it<br>
