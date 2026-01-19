import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

class SelfHealingAgent:
    def __init__(self):
        # Using Llama 3.3 70B - The new state-of-the-art for Groq
        self.llm = ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.prompt = ChatPromptTemplate.from_template("""
            You are an Autonomous Data Engineer.
            Write a Python function `repair_data(input_data: list)` to map the 'Actual Sample' to the 'Target Schema'.
            
            Target Schema: {target_schema}
            Actual Sample: {sample_data}
            
            Return ONLY the code block starting with 'def repair_data'.
        """)
        self.chain = self.prompt | self.llm | StrOutputParser()

    async def generate_fix(self, target_schema, sample):
        try:
            return await self.chain.ainvoke({
                "target_schema": str(target_schema), 
                "sample_data": str(sample)
            })
        except Exception as e:
            return f"# Healing Error: {str(e)}"