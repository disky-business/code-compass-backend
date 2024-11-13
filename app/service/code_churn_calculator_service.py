import math

from app.logger import logger


class CodeChurnCalculatorService:
    decay_factor = 0.1

    @classmethod
    def calculate_code_churn_for_file(self, file_path, github_client_service):
        commit_count = github_client_service.get_commit_count(file_path)
        return round((math.exp(-self.decay_factor * commit_count)) * 100, 2)
