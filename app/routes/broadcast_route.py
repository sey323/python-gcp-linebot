from fastapi import APIRouter
from app.facades.line_bot import line_message
from app.models.broadcast.broadcast import BroadcastRequest, BroadcastResponse

from linebot.models import (
    TextSendMessage,
    TemplateSendMessage,
    MessageAction,
    ButtonsTemplate,
)

broadcast_router = APIRouter(prefix="/bloadcast", tags=["bloadcast"])


@broadcast_router.post(
    "/",
    response_model=BroadcastResponse,
)
async def broadcast(
    request: BroadcastRequest,
):
    """ユーザに安否確認を配信する"""
    text = f"【{request.disaster_name}が発生しました】\n安否確認を行います。\n救援の必要な方は救援申請を実施します。"
    message = TemplateSendMessage(
            alt_text="にゃーん",
            template=ButtonsTemplate(
                text=text,
                actions=[
                    MessageAction(label="無事です", text="無事です"),
                    MessageAction(label="救援を要請する", text="救援を要請する"),
                ],
            ),
        )
    line_message.broadcast_message(message)

    return BroadcastResponse(status=200)
