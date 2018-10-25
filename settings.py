from dotenv import load_dotenv
import os

load_dotenv()
_mongo_url = os.getenv("MONGODB_ADDRESS")
_debug = os.getenv("DEBUG_MODE") == "DEBUG"
