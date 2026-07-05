from google import genai
from dotenv import load_dotenv
import chromadb
import os

load_dotenv()

# -------------------------------------
# Gemini Client
# -------------------------------------

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_KEY")
)

# -------------------------------------
# ChromaDB Client
# -------------------------------------

chromadb_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chromadb_client.get_or_create_collection(
    name="faculty_profiles"
)