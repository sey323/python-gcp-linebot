from io import BytesIO
from typing import Union
from fastapi import UploadFile
from PIL import Image
from app.facades.storage import thumbnail
from app.models.user_report.domain import UserReportModel
from app.models.user_report.update_user_report import (
    UpdateUserReportRequest,
    UpdateUserReportRequestDto,
)
from app.repositories import user, user_report
from app.facades.chatgpt import chatGPT
from app.utils import now
from linebot.models import (
    TextSendMessage,
)
from app.facades.line_bot import line_message


async def execute(
    user_report_id: str, request: UpdateUserReportRequest, file
) -> str:
    """ユーザレポートを更新する

    Args:
        user_report_id (str): 更新するユーザレポートのID
        request (UpdateUserReportRequest): 更新内容

    Returns:
        str: 更新が完了したユーザレポートのID
    """
    user_report_model: UserReportModel = user_report.fetch_user_report(
        id=user_report_id
    )

    if file:
        update_image_url = await _upload_thumbnail_image(
            user_report_id, file=file
        )
    else:
        update_image_url = user_report_model.image_url

    # マイナ連携済みユーザであればスコアを返す
    target_user = user.fetch_user(user_report_model.user_id)
    report_score = target_user.score if target_user else -1

    update_user_report_model: UpdateUserReportRequestDto = (
        UpdateUserReportRequestDto.parse_obj(
            {
                **request.dict(),
                **chatGPT.create_report_title(request.content).dict(),
                "report_score": report_score,
                "updated_at": now(),
                "image_url": update_image_url,
            },
        )
    )

    user_report.update_user_report(user_report_id, update_user_report_model)

    # レポートの発信者にリプライ
    try:
        target_user_report = user_report.fetch_user_report(
            user_report_model.user_id
        )
        text_message = TextSendMessage(text="救援報告の更新が完了しました")

        line_message.push_message(
            user_id=target_user_report.user_id, message=text_message
        )
    except Exception as e:
        print(e)

    return user_report_id


async def _upload_thumbnail_image(
    id: str, file: UploadFile
) -> Union[str, None]:
    """pdfからサムネイル画像を生成しGoogle Cloud Storageに保存する"""
    try:
        thumbnail_filename = f"{id}.jpeg"
        data = await file.read()
        img_pil = Image.open(BytesIO(data))
        image_url = thumbnail.upload(
            destination_blob_name=thumbnail_filename, image=img_pil
        )
        return image_url
    except Exception as e:
        print("画像ファイルの読み込みにし敗しました", e)
        return None
