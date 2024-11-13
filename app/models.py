import pydantic


class UploadRequestBody(pydantic.BaseModel):
    repo_link: str = pydantic.Field(..., alias="repoLink")
    branch_name: str = pydantic.Field(..., alias="branchName")
