import os
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

class RAGRetriever:
    def __init__(self):
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = "agentic-data"
        
        if not api_key:
            print("⚠️ Pinecone API Key missing in .env")
            self.vectorstore = None
            return

        try:
            # 1. Initialize Pinecone
            self.pc = Pinecone(api_key=api_key)
            
            self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            
            # 3. Connect to Vector Store
            self.vectorstore = PineconeVectorStore(
                index_name=index_name, 
                embedding=self.embeddings
            )
            print("✅ Vector Store Connected (Using HuggingFace Embeddings).")
        except Exception as e:
            print(f"⚠️ Vector Store Connection Error: {e}")
            self.vectorstore = None

    def search_context(self, query):
        if not self.vectorstore:
            return "No report context available."
        try:
            docs = self.vectorstore.similarity_search(query, k=2)
            return "\n".join([d.page_content for d in docs])
        except Exception as e:
            return f"Retrieval failed: {str(e)}"