import pydantic


class UploadRequestBody(pydantic.BaseModel):
    user_name: str = pydantic.Field(..., alias="userName")
    repo_name: str = pydantic.Field(..., alias="repoName")
    branch_name: str = pydantic.Field(..., alias="branchName")
