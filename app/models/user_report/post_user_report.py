from pydantic import BaseModel, Field

from app.models.user_report.domain import Location


class UserReportRequest(BaseModel):
    """ユーザ通知リクエストに含める項目"""

    user_id: str = Field(..., description="UserID、LINEのIDなど？")
    location: Location = Field(..., description="申告者の位置情報")
    content: str = Field(..., description="報告内容、選択式にする？")


class UserReportResponse(BaseModel):
    request_id: str = Field(..., description="申告に対するリクエストID")
