from github import Github
from concurrent.futures import ThreadPoolExecutor

from app.config import GITHUB_AUTH_TOKEN
from app.logger import logger
from app.service.code_churn_calculator_service import CodeChurnCalculatorService


class GithubClientService:
    _thread_pool_executor = ThreadPoolExecutor(max_workers=100)

    def __init__(self, repo_link: str, branch_name: str):
        self.token = GITHUB_AUTH_TOKEN
        self.github_client = Github(self.token)
        self.branch_name = branch_name
        self.repo = self.github_client.get_repo(repo_link)

    def get_commit_count(self, file_path):
        return self.repo.get_commits(path=file_path).totalCount

    def calculate_churn(self, file_path: str):
        logger.info(f"Getting contents for path : {file_path}...")
        contents = self.repo.get_contents(file_path, ref=self.branch_name)
        file_tree = []
        for content in contents:
            if content.type == "dir":
                children_content = self.calculate_churn(content.path)
                file_tree.append(
                    {
                        "name": content.name,
                        "type": "dir",
                        "path": content.path,
                        "children": children_content.result(),
                    }
                )
            else:
                file_tree.append(
                    {
                        "name": content.name,
                        "type": "file",
                        "path": content.path,
                        "codeChurnScore": CodeChurnCalculatorService.calculate_code_churn_for_file(
                            content.path, self
                        ),
                    }
                )
        return file_tree

    def get_repo_churn(self):
        logger.info(f"Getting contents for {self.repo.full_name}...")
        repo_churn_tree_dict = self.calculate_churn("")
        logger.info(f"Contents for {self.repo.full_name} retrieved successfully.")
        logger.info(f"Contents : {repo_churn_tree_dict}")
        return repo_churn_tree_dict
