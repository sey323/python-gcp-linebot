from pydantic import BaseModel, Field

from app.models.user_report.domain import UserReportModel


class UpdateUserReportRequest(UserReportModel):
    pass


class UpdateUserReportResponse(BaseModel):
    request_id: str = Field(..., description="申告に対するリクエストID")
