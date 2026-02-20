###Architecture

Frontend (HTML/JS)
        ↓
Django API (/ask)
        ↓
Embed Query (BGE)
        ↓
Pinecone (Top-k chunks)
        ↓
Construct Prompt
        ↓
Gemini API
        ↓
Return Answer