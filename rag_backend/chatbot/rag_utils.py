import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from groq import Groq

load_dotenv()

# ===============================
# ENV KEYS
# ===============================
PINECONE_KEY = os.getenv("PINECONE_API_KEY")
GROQ_KEY = os.getenv("GROQ_API_KEY")

# ===============================
# EMBEDDING MODEL
# ===============================
embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# ===============================
# PINECONE
# ===============================
pc = Pinecone(api_key=PINECONE_KEY)
index = pc.Index("rag-pdf-index")

# ===============================
# GROQ CLIENT  ← IMPORTANT
# ===============================
client = Groq(api_key=GROQ_KEY)


# ===============================
# RETRIEVAL
# ===============================
def retrieve_chunks(query, top_k=1):
    query_embedding = embedding_model.encode([query])[0]

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_metadata=True
    )

    contexts = [match["metadata"]["text"] for match in results["matches"]]
    return contexts


# ===============================
# GENERATION
# ===============================
def generate_answer(query, contexts):
    combined_context = "\n\n".join(contexts)
    combined_context = combined_context[:1200]

    prompt = f"""
You are an aircraft maintenance assistant.
Answer ONLY from the provided context.
If not found, say: "Not available in document."

Context:
{combined_context}

Question:
{query}

Answer:
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=300,
    )

    return completion.choices[0].message.content