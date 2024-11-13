import time
from fastapi import APIRouter, status

from app.logger import logger
from app.models import UploadRequestBody
from app.service.github_client_service import GithubClientService

router = APIRouter()


@router.post("/calculateCodeChurn", status_code=status.HTTP_201_CREATED)
async def calculate_code_churn(json_request: UploadRequestBody):
    logger.info("Uploading repo...")
    github_client_service = GithubClientService(
        json_request.repo_link, json_request.branch_name
    )
    commits_history_list = github_client_service.calculate_churn("")
    return {"fileChurnScores": commits_history_list}
