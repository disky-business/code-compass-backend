import time
from fastapi import APIRouter, status

from app.logger import logger
from app.models import UploadRequestBody
from app.service.code_churn_calculator_service import CodeChurnCalculatorService

router = APIRouter()


@router.post("/calculateCodeChurn", status_code=status.HTTP_201_CREATED)
async def calculate_code_churn(json_request: UploadRequestBody):
    logger.info("Uploading repo...")
    code_churn_report = CodeChurnCalculatorService.calculate_code_churn_for_repository(
        json_request.user_name, json_request.repo_name, json_request.branch_name
    )
    return {"fileChurnScores": code_churn_report}
