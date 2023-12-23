from datetime import datetime
import json
from typing import Union
from pydantic import BaseModel, Field

from app.models.user_report.domain import (
    Location,
    ReportLevel,
    ReportStatus,
)


class UpdateUserReportRequest(BaseModel):
    location: Location = Field(..., description="申告者の位置情報")
    title: str = Field(
        "タイトルなし", description="画面に表示されるタイトル。報告内容などからChatGPTから自動で生成される"
    )
    content: str = Field(..., description="報告内容、選択式にする？")
    report_level: ReportLevel = Field(..., description="申告内容の深刻度")
    report_status: ReportStatus = Field(..., description="申告内容の状態")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class UpdateUserReportRequestDto(UpdateUserReportRequest):
    updated_at: Union[datetime, None] = Field(None, description="最終更新時間")
    image_url: Union[str, None] = Field(None, description="画像のURL")
    report_score: Union[int, None] = Field(None, description="スコア")


class UpdateUserReportResponse(BaseModel):
    user_report_id: str = Field(..., description="発行された申告ID")
