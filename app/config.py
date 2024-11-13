import os
from dotenv import load_dotenv


load_dotenv()

GITHUB_AUTH_TOKEN = os.getenv("GITHUB_AUTH_TOKEN", "")
CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
APP_KEY = os.getenv("CISCO_OPENAI_APP_KEY", "")
API_VERSION = os.getenv("API_VERSION", "")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "")
CISCO_IDP_TOKEN_URL = os.getenv("TOKEN_URL", "")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", "")
