import os
from dotenv import load_dotenv
from supabase import create_client, Client

def db_connect():
    load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    return supabase
