import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from .prompts import ANALYST_SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

class AnalystAgent:
    def __init__(self):
        # Using Llama 3.1 8B Instant - The current fastest model on Groq
        self.llm = ChatGroq(
            temperature=0.2,
            model_name="llama-3.1-8b-instant",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    async def analyze_data_query(self, user_query: str, retrieved_context: str, structured_data: list):
        messages = [
            SystemMessage(content=ANALYST_SYSTEM_PROMPT),
            HumanMessage(content=f"REPORTS:\n{retrieved_context}\n\nDATA:\n{structured_data}\n\nQUERY:\n{user_query}")
        ]
        try:
            response = await self.llm.ainvoke(messages)
            return response.content
        except Exception as e:
            return f"Analyst Error: {str(e)}"