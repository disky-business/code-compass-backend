import os
from dotenv import load_dotenv


load_dotenv()

GITHUB_AUTH_TOKEN = os.getenv("GITHUB_AUTH_TOKEN", "")
