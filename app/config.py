import os
from dotenv import load_dotenv

from app.logger import logger

GITHUB_AUTH_TOKEN = ""

def load_environment():
    load_dotenv()
    global GITHUB_AUTH_TOKEN
    GITHUB_AUTH_TOKEN = os.getenv("GITHUB_AUTH_TOKEN", "")
    
