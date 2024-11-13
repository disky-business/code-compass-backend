import os
from dotenv import load_dotenv

from app.logger import logger

load_dotenv()

GITHUB_AUTH_TOKEN = os.getenv("GITHUB_AUTH_TOKEN", "")
