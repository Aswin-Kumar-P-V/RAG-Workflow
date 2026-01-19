# 🤖 RAG Chatbot with Python & ChromaDB

A custom Retrieval-Augmented Generation (RAG) engine built from scratch using Python. This application allows users to add text documents, convert them into vector embeddings, and chat with the data using OpenAI's GPT models via a Streamlit web interface.

## 🚀 Features

* **Custom Ingestion Pipeline:** Reads text files and performs chunking based on "\n" character.
* **Vector Embeddings:** Uses `text-embedding-3-small` to convert text into mathematical vectors.
* **Local Vector Database:** Stores embeddings locally using **ChromaDB** (no external server required).
* **Strict RAG Retrieval:** Retrieves the top 2 most relevant chunks for every query.
* **Grounded Answers:** "Temperature 0" setting ensures the bot only answers based on provided data, reducing hallucinations.
* **Web UI:** Clean, interactive chat interface built with **Streamlit**.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **LLM & Embeddings:** OpenAI API
* **Vector Database:** ChromaDB
* **Frontend:** Streamlit
* **Environment Management:** Python-dotenv

## 📂 Project Structure

```text
my-rag-bot/
├── data/                  # Place your .txt documents here
├── chromaDB/              # Local vector database (auto-generated)
├── venv/                  # Virtual Environment (ignored by Git)
├── .env                   # API Keys (ignored by Git)
├── .gitignore             # Git configuration
├── requirements.txt       # Project dependencies
├── ingest.py              # Logic for reading and chunking text
├── store_vectors.py       # Script to embed chunks and save to ChromaDB
├── chat.py                # Terminal-based chat script
└── app.py                 # Streamlit Web Application

```

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd my-rag-bot

```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a file named `.env` in the root directory and add your OpenAI API key:

```properties
OPENAI_API_KEY=sk-your-actual-api-key-here

```

## 🏃‍♂️ How to Run

### Step 1: Ingest Data

Place your text files (e.g., `knowledge.txt`) inside the `data/` folder. Then, run the script to process and store them in the vector database:

```bash
python store_vectors.py

```

*You should see a message confirming that documents were added to ChromaDB.*

### Step 2: Launch the Chat App

Start the web interface using Streamlit:

```bash
streamlit run app.py

```

Your browser will open automatically at `http://localhost:8501`.

## 🧪 Testing Strictness

To verify the "Grounding" (anti-hallucination) capability:

1. Ask a question found in your `data` files -> **Bot provides answer.**
2. Ask a random question (e.g., "Who won the World Cup?") -> **Bot replies: "I do not have that information in my knowledge base."**

## 🔮 Future Roadmap

* [ ] Add support for PDF and Docx ingestion.
* [ ] Add "Chat Memory" so the bot remembers previous questions in the session.
* [ ] Deploy to Streamlit Community Cloud.