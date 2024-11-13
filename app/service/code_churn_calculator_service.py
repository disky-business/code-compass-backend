import math

from app.logger import logger
from app.service.github_client_service import GithubClientService


class CodeChurnCalculatorService:
    DECAY_FACTOR = 0.1

    @classmethod
    def calculate_code_churn_for_file(self, file_path, github_client_service):
        commit_count = github_client_service.get_commit_count(file_path)
        return round((math.exp(-self.DECAY_FACTOR * commit_count)) * 100, 2)

    @staticmethod
    def _get_code_churn_report_for_file_path(file_path: str, github_client_service: GithubClientService):
        logger.debug(f"Gettnig code churn report for {file_path}...")
        file_path_contents = github_client_service.get_file_path_contents(file_path)
        code_churn_report = []
        for file_path_content in file_path_contents:
            if file_path_content.type == "dir":
                children_code_churn_report = CodeChurnCalculatorService._get_code_churn_report_for_file_path(
                    file_path_content.path, github_client_service
                )
                code_churn_report.append(
                    {
                        "fileName": file_path_content.name,
                        "fileType": "dir",
                        "filePath": file_path_content.path,
                        "children": children_code_churn_report,
                    }
                )
            else:
                code_churn_report.append(
                    {
                        "fileName": file_path_content.name,
                        "fileType": "file",
                        "filePath": file_path_content.path,
                        "codeChurnScore": CodeChurnCalculatorService.calculate_code_churn_for_file(
                            file_path_content.path, github_client_service
                        ),
                    }
                )
        return code_churn_report
    
    @staticmethod
    def calculate_code_churn_for_repository(user_name: str, repo_name: str, branch_name: str = "main"):
        logger.info(f"Calculating code churn for {repo_name}...")
        github_client_service = GithubClientService(
            user_name, repo_name, branch_name
        )
        code_churn_report = CodeChurnCalculatorService._get_code_churn_report_for_file_path("", github_client_service)
        return code_churn_report
        