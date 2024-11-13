from fastapi import FastAPI
from app.routes.routes import router
from app.logger import logger

app = FastAPI()
logger.info("Starting FastAPI app...")
app.include_router(router)
