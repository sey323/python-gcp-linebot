from typing import List
from pydantic import BaseModel, Field

from app.models.user_report.domain import UserReportModel


class UserReportsResponse(BaseModel):
    user_reports: List[UserReportModel] = Field([], description="ユーザが申告した情報一覧")
