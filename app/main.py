from fastapi import FastAPI
from app.routes.routes import router
from app.logger import logger


def start_application() -> FastAPI:
    app = FastAPI()
    logger.info("Starting FastAPI server...")
    app.include_router(router)
    return app


app = start_application()
