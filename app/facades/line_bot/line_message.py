from typing import Any
from app.facades.line_bot import line_bot_api
from linebot.models import SendMessage


def reply_message(reply_token: Any, message: SendMessage):
    """メッセージを返信

    Args:
        reply_token (Any): _description_
        message (SendMessage): 返信するメッセージ
    """
    line_bot_api.reply_message(reply_token=reply_token, messages=message)


def push_message(user_id: str, message: SendMessage):
    """メッセージを送信

    Args:
        user_id (str): _description_
        message (SendMessage): _description_
    """
    line_bot_api.push_message(to=user_id, messages=message)

def broadcast_message(message: SendMessage):
    """メッセージを送信

    Args:
        message (SendMessage): _description_
    """
    line_bot_api.broadcast(messages=message)
