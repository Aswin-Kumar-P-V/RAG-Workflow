import os

DATA_DIR = "data"

def load_and_chunk():
    print("Loading documents...")
    documents = []

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(DATA_DIR, filename)
            with open(file=filepath, mode="r", encoding="utf-8") as f:
                text = f.read()
                chunks = text.split("\n")
                chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
                print(f"Read file : {filename} and split into chunks of len : {len(chunks)}")
        documents.extend(chunks)
    return documents
