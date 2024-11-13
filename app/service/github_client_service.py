from github import Github

from app.config import GITHUB_AUTH_TOKEN


class GithubClientService:
    def __init__(self, user_name: str, repo_name: str, branch_name: str):
        self.token = GITHUB_AUTH_TOKEN
        self.github_client = Github(self.token)
        self.branch_name = branch_name
        self.repository = self.github_client.get_repo(f"{user_name}/{repo_name}")

    def get_commit_count(self, file_path):
        return self.repository.get_commits(path=file_path).totalCount

    def get_file_path_contents(self, file_path):
        return self.repository.get_contents(file_path, ref=self.branch_name)
