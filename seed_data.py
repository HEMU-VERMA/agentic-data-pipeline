import os
from dotenv import load_dotenv
from data_plane.supabase_client import SupabaseManager

load_dotenv()

def seed_system():
    print("🚀 Seeding Supabase with Sample Sales Data...")
    db = SupabaseManager()
    
    # Sample records to test the "Analyst" logic
    sample_sales = [
        {"city": "Delhi", "amount": 500, "product": "Laptop", "notes": "High demand"},
        {"city": "Delhi", "amount": 150, "product": "Mouse", "notes": "Stable"},
        {"city": "Mumbai", "amount": 1200, "product": "Server", "notes": "Bulk order"}
    ]
    
    try:
        db.upsert_data("sales", sample_sales)
        print("✅ Data successfully pushed to Supabase!")
    except Exception as e:
        print(f"❌ Error: {e}\n(Make sure you created the 'sales' table in Supabase SQL Editor first!)")

if __name__ == "__main__":
    seed_system()