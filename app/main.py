from fastapi import FastAPI
from app.routes.routes import router
from app.logger import logger

def start_application():
    app = FastAPI()
    logger.info("Starting FastAPI server...")
    app.include_router(router)

if __name__=="__main__":
    start_application()