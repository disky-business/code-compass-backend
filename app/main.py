from fastapi import FastAPI
from app.routes.routes import router
from app.logger import logger
from app.config import load_environment

def start_application() -> FastAPI:
    app = FastAPI()
    logger.info("Starting FastAPI server...")
    app.include_router(router)
    return app

load_environment()
app = start_application()
