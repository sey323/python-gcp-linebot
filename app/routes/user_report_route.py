from fastapi import APIRouter
from app.models.user_report.get_user_reports import UserReportsResponse
from app.models.user_report.post_user_report import (
    UserReportRequest,
    UserReportResponse,
)


user_report_router = APIRouter(prefix="/report", tags=["report"])


@user_report_router.post("", response_model=UserReportResponse)
async def post_user_report(request: UserReportRequest):
    """ユースケース1: ユーザがHelpを申請する"""
    return UserReportResponse(request_id="sample")


@user_report_router.get("", response_model=UserReportsResponse)
async def get_user_reports():
    """ユースケース2: 申告内容の一覧を取得する"""
    return []
