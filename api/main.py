import uvicorn
import os
import sys

# Standard Path Handling
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from api.routes import router as api_router
from agents.self_healing import SelfHealingAgent
# Add CORS middleware so the dashboard can talk to the backend
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(
    title="Agentic Data Pipeline",
    version="1.0.0"
)

# Enable CORS so your browser doesn't block the requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Agent
healing_agent = SelfHealingAgent()

# Attach API routes
app.include_router(api_router, prefix="/api/v1")

class HealingRequest(BaseModel):
    target_schema: dict
    sample_data: list

@app.get("/")
async def health():
    return {"status": "online", "engine": "Llama-3-via-Groq"}

@app.post("/auto-heal")
async def trigger_healing(request: HealingRequest):
    """Triggers the Agentic AI to write repair code for broken data formats."""
    code = await healing_agent.generate_fix(request.target_schema, request.sample_data)
    return {"status": "HEALED", "repair_code": code}

if __name__ == "__main__":
    # CHANGED: Use 127.0.0.1 instead of 0.0.0.0 for better browser compatibility
    print("🚀 Starting Agentic Backend on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
