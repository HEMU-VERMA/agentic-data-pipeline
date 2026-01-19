import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class SupabaseManager:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(url, key)

    def upsert_data(self, table, data):
        """Used for seeding and real-time ingestion."""
        return self.client.table(table).upsert(data).execute()

    def fetch_sales_data(self, city):
        """This name MUST match what is called in routes.py"""
        return self.client.table("sales").select("*").eq("city", city).execute()