import os
import sys
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Path setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.analyst import AnalystAgent
from data_plane.supabase_client import SupabaseManager
from vector_store.retriever import RAGRetriever

router = APIRouter()
analyst = AnalystAgent()
db = SupabaseManager()
rag = RAGRetriever()

class NLQueryRequest(BaseModel):
    query: str
    city: str = "Delhi"

@router.post("/query")
async def natural_language_query(request: NLQueryRequest):
    try:
        # 1. Fetch from Supabase
        sales_result = db.fetch_sales_data(request.city)
        # Handle Supabase PostgrestResponse object
        raw_rows = sales_result.data if hasattr(sales_result, 'data') else []
        
        # 2. Search Pinecone
        context = rag.search_context(request.query)
        
        # 3. AI Analysis
        report = await analyst.analyze_data_query(request.query, context, raw_rows)
        return {"agent_report": report}
    except Exception as e:
        print(f"❌ Route Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))