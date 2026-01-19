import os
from openai import OpenAI
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
import streamlit as st
from chat import query_rag

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")

def get_clients():
    chromadb_client=chromadb.PersistentClient("chromaDB")
    openai_ef=embedding_functions.OpenAIEmbeddingFunction(api_key=openai_api_key, model_name="text-embedding-3-small")
    collections = chromadb_client.get_collection(name="my_vector_knowledge", embedding_function=openai_ef)
    openai_client = OpenAI(api_key=openai_api_key)

    return openai_client, collections

openai_client, collections = get_clients()

st.title("🤖 My RAG Chatbot")
st.write("Ask me anything about the uploaded documents!")

user_question = st.text_input("Type your question here:")

if st.button("Ask"):
    if user_question:
        with st.spinner("Thinking..."):
            answer = query_rag(user_question, collections=collections, openai_client=openai_client)
            st.success("Here is the answer:")
            st.write(answer)
    else:
        st.warning("Please enter a question first.")