import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # API Configuration - NO STATIC FALLBACKS
    # These will be None/empty if not set in .env
    API_BASE_URL = os.getenv("API_BASE_URL")
    API_PREVIEW_URL = os.getenv("API_PREVIEW_URL")
    API_TOKEN = os.getenv("API_TOKEN", "")