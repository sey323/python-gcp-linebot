from typing import Optional
from fastapi import APIRouter, Body, File, UploadFile
from app.models.user_report.list_user_reports import ListUserReportResponse
from app.models.user_report.entry_user_report import (
    EntryUserReportRequest,
    EntryUserReportResponse,
)
from app.models.user_report.update_user_report import (
    UpdateUserReportRequest,
    UpdateUserReportResponse,
)
from app.services.report import (
    entry_user_report_service,
    list_user_report_service,
    update_user_report_service,
)

import json

user_report_router = APIRouter(prefix="/report", tags=["report"])


@user_report_router.post("", response_model=EntryUserReportResponse)
async def post_user_report(
    request: EntryUserReportRequest = Body(...),
    file: Optional[UploadFile] = File(None),
):
    """ユースケース1: ユーザがHelpを申請する"""
    user_report_id = await entry_user_report_service.execute(request, file)
    return EntryUserReportResponse(user_report_id=user_report_id)


@user_report_router.put(
    "/{user_report_id}", response_model=UpdateUserReportResponse
)
async def put_user_report(
    user_report_id: str,
    request: UploadFile = File(...),
    file: Optional[UploadFile] = File(None),
):
    """ユースケース3: ユーザがヘルプ情報を更新する"""
    json_data = json.loads(request.file.read())
    userRequest = UpdateUserReportRequest.parse_obj(json_data)

    user_report_id = await update_user_report_service.execute(
        user_report_id, userRequest, file
    )

    return UpdateUserReportResponse(user_report_id=user_report_id)


@user_report_router.get("", response_model=ListUserReportResponse)
async def get_user_reports():
    """ユースケース2: 申告内容の一覧を取得する"""
    list_user_report = list_user_report_service.execute()
    return ListUserReportResponse(user_reports=list_user_report)


__dummy_user_report_router = APIRouter(
    prefix="/__dummy_report", deprecated=True
)


@__dummy_user_report_router.post("__dummy_post", deprecated=True)
async def _dummy_post_user_report(
    request: EntryUserReportRequest,
):
    """openapi-generatorの生成用"""
    pass


@__dummy_user_report_router.put("__dummy_put", deprecated=True)
async def _dummy_put_user_report(
    request: UploadFile,
):
    """openapi-generatorの生成用"""
    pass
