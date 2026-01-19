import os
import chromadb
from chromadb.utils import embedding_functions
from openai import OpenAI
from dotenv import load_dotenv


def query_rag(question, collections, openai_client):
    result = collections.query(query_texts=[question], n_results=2)
    if not result:
        print("Couldn't find any maching resource in the db")
        return
    chunks = result["documents"][0]
    print("Chunks retrieved successfully...")
    print("---------------------Retrieved-Chunks-------------------------")
    for chunk in chunks:
        print(f"Chunk: {chunk}")
    print("------------------------End------------------------------------")
    system_prompt = "You are a helpful assistant. You must answer the user's question STRICTLY based on the provided context below. If the answer is not found in the context, reply exactly: \"I do not have that information in my knowledge base.\"Do NOT use your own outside knowledge."
    chunk_text = "\n\n".join(chunks)
    user_prompt=f"Context : {chunk_text}, question : {question}"

    try : 
        result = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role" : "system", "content" : system_prompt},
                {"role" : "user", "content" : user_prompt}
            ],
            temperature=0
        )
    except Exception as e:
        print("Error fetching response from bot..\nError : {e}")
    return result.choices[0].message.content