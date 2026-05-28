# ✈️ A320 AI Assistant RAG Chatbot

A Retrieval-Augmented Generation (RAG) based AI chatbot built using **Django**, **Pinecone**, **HuggingFace Embeddings**, and **Groq LLM**.  

This system allows users to query a technical PDF document (A320 Aircraft Characteristics – Airport & Maintenance Planning) and receive context-grounded answers.

## 🚀 Features

- 📄 PDF-based knowledge system
- 🔍 Semantic search using vector embeddings
- 🧠 Context-aware AI responses (RAG architecture)
- ⚡ Fast LLM inference using Groq (Llama 3.1)
- 🎨 Modern animated UI (Glassmorphism design)
- 🔐 Secure API key management via `.env`

---

## 🏗️ Architecture
```
Frontend (HTML/JS)                         User Question
        ↓                                        ↓
Django API (/ask)                          Django Backend
        ↓                                        ↓
Embed Query (BGE)                    SentenceTransformer Embedding
        ↓                                        ↓
Pinecone (Top-k chunks)                  Pinecone Vector Search
        ↓                                        ↓
Construct Prompt                          Retrieve Top Chunk
        ↓                                        ↓
Gemini API                               Groq LLM (Llama 3.1)
        ↓                                        ↓
Return Answer                           Context-Grounded Answer
```


---

## 🧠 How RAG Works in This Project

1. PDF is parsed and chunked (in Google Colab).
2. Each chunk is converted into embeddings.
3. Embeddings are stored in Pinecone.
4. When user asks a question:
   - Question is embedded.
   - Most relevant chunk is retrieved.
   - Retrieved context is sent to Groq LLM.
   - LLM generates answer strictly from context.

## 🛠️ Tech Stack

| Layer        | Technology Used |
|--------------|-----------------|
| Backend      | Django          |
| Embeddings   | BAAI/bge-small-en-v1.5 |
| Vector DB    | Pinecone (Free Tier) |
| LLM          | Groq (Llama 3.1-8b-instant) |
| Frontend     | HTML + CSS + JS |
| Deployment   | Render (Planned) |

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Yash-Lade/RAG_chatbot
cd rag_backend
```
### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
If requirements.txt not created, install manually:
```
pip install django
pip install sentence-transformers
pip install pinecone-client
pip install groq
pip install python-dotenv
```
### 🔐 Environment Variables

Create a .env file in project root:

```
PINECONE_API_KEY=your_pinecone_key
GROQ_API_KEY=your_groq_key
```
Add .env to .gitignore:
```
.env
venv/
__pycache__/
```
### ▶️ Running the Project
```
python manage.py migrate
python manage.py runserver
```
Open browser:
```
http://127.0.0.1:8000/
```
📂 Project Structure
```
rag_backend/
│
├── manage.py
├── .env
│
├── rag_backend/
│   ├── settings.py
│   ├── urls.py
│
└── chatbot/
    ├── views.py
    ├── rag_utils.py
    ├── urls.py
    ├── templates/
    │     └── index.html
    └── static/
          └── style.css
```
### 🧪 Sample Test Questions

- What is the maximum ramp weight of the A320-200?
- Describe the jacking procedure for maintenance.
- What wind limits apply during aircraft jacking?
- What protections are provided by the engine nacelle?

### Out-of-scope questions should return:

"Not available in document."

### ⚙️ Configuration Details
Embedding Model
```
BAAI/bge-small-en-v1.5
Dimension: 384
Similarity: Cosine
```
LLM Model
```
llama-3.1-8b-instant
```
Retrieval Strategy
Top K = 1

Context limited to 1200 characters

Max output tokens = 300
