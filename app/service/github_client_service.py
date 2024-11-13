from github import Github
from concurrent.futures import ThreadPoolExecutor

from app.config import GITHUB_AUTH_TOKEN
from app.logger import logger
from app.service.code_churn_calculator_service import CodeChurnCalculatorService


class GithubClientService:
    _thread_pool_executor = ThreadPoolExecutor(max_workers=100)

    def __init__(self, user_name: str, repo_name: str, branch_name: str):
        self.token = GITHUB_AUTH_TOKEN
        self.github_client = Github(self.token)
        self.branch_name = branch_name
        self.repository = self.github_client.get_repo(f"{user_name}/{repo_name}")

    def get_commit_count(self, file_path):
        return self.repository.get_commits(path=file_path).totalCount

    def calculate_churn(self, file_path: str):
        logger.info(f"Getting contents for path : {file_path}...")
        contents = self.repository.get_contents(file_path, ref=self.branch_name)
        file_tree = []
        for content in contents:
            if content.type == "dir":
                children_content = self.calculate_churn(content.path)
                file_tree.append(
                    {
                        "fileName": content.name,
                        "fileType": "dir",
                        "filePath": content.path,
                        "children": children_content.result(),
                    }
                )
            else:
                file_tree.append(
                    {
                        "fileName": content.name,
                        "fileType": "file",
                        "filePath": content.path,
                        "codeChurnScore": CodeChurnCalculatorService.calculate_code_churn_for_file(
                            content.path, self
                        ),
                    }
                )
        return file_tree

    def get_repo_churn(self):
        logger.info(f"Getting contents for {self.repository.full_name}...")
        repo_churn_tree_dict = self.calculate_churn("")
        logger.info(f"Contents for {self.repository.full_name} retrieved successfully.")
        logger.info(f"Contents : {repo_churn_tree_dict}")
        return repo_churn_tree_dict
