🚀 Agentic Autonomous Data Pipeline

An end-to-end autonomous ETL and analysis pipeline built with Llama 3.1 (Groq), Supabase, and Pinecone. This system doesn't just process data; it heals itself and reasons through business questions.

🌟 Features

Self-Healing Agent: Automatically detects schema drift and writes Python repair functions on-the-fly.

Agentic RAG: Combines SQL (Supabase) and Vector search (Pinecone) to answer complex natural language queries.

Ultra-Low Latency: Powered by Groq LPU for near-instant agent reasoning.

Local Embeddings: Uses HuggingFace all-MiniLM-L6-v2 for zero-cost vector search.

🛠️ Tech Stack

Backend: FastAPI (Python)

AI Brain: Llama 3.3 70B & 3.1 8B via Groq

Database: Supabase (PostgreSQL)

Vector Store: Pinecone

Frontend: React + Tailwind (Single-file Dashboard)

🚦 Quick Start

Clone the repo.

Install dependencies: pip install -r requirements.txt

Setup .env with Groq, Supabase, and Pinecone keys.

Run the backend: python api/main.py

Open dashboard.html in your browser.