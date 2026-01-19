import os
import chromadb
from dotenv import load_dotenv
from chromadb.utils import embedding_functions
from ingest import load_and_chunk

load_dotenv()

openai_api_key=os.getenv("OPENAI_API_KEY")

chromadb_client=chromadb.PersistentClient("chromaDB")

openai_ef=embedding_functions.OpenAIEmbeddingFunction(api_key=openai_api_key, model_name="text-embedding-3-small")

collections=chromadb_client.get_or_create_collection(name="my_vector_knowledge", embedding_function=openai_ef)

def add_documents_to_db():
    documents = load_and_chunk()
    if not documents:
        print("No documents to store...")
        return
    print("Adding chunks to the database...")
    ids = [f"id_{i}" for i in range(0, len(documents))]
    try:
        collections.upsert(ids=ids,documents=documents)
    except Exception as e:
        print(f"Couldnt add chunks to db... Error : {e}")

    print("Successfully added chunks added to db")