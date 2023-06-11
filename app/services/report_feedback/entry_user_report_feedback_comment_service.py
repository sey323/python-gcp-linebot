from email import message
from app.facades import line_bot
from app.facades.line_bot import line_message
from app.models.user_report.domain import ReportStatus
from app.models.user_report.update_user_report import (
    UpdateUserReportRequestDto,
)
from app.models.user_report_feedback.domain import UserReportFeedbackComment
from app.models.user_report_feedback.entry_user_report_feedback import (
    EntryUserReportFeedBackCommentRequest,
)
from app.repositories import user_report
from app.utils import generate_id_str
from linebot.models import (
    TextSendMessage,
)

from app.facades.chatgpt import chatGPT


async def execute(
    report_id: str, request: EntryUserReportFeedBackCommentRequest
):
    id = generate_id_str()

    content = UserReportFeedbackComment.parse_obj(
        {**request.dict(), "user_report_feedback_comment_id": id}
    )
    user_report.add_comment(report_id, content)

    # レポートの発信者にリプライ
    try:
        target_user_report = user_report.fetch_user_report(report_id)
        text_message = TextSendMessage(
            text=f"""あなたの申告に対してメッセージが追加されました！
----
{request.comment}"""
        )

        line_message.push_message(
            user_id=target_user_report.user_id, message=text_message
        )
    except Exception as e:
        print(e)

    if chatGPT.check_rescore(request.comment):
        user_report.update_user_status(report_id, ReportStatus.COMPLETE)

    return id
