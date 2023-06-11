from fastapi.testclient import TestClient
from app.main import app
from app.models.user_report_feedback.entry_user_report_feedback import (
    EntryUserReportFeedBackCommentRequest,
)
from app.models.user_report_feedback.entry_user_report_feedback_reaction import (
    EntryUserReportFeedBackReactionRequest,
)

client = TestClient(app)


def test_post_user_report_feedback_comment(mocker):
    report_id = "xyz"

    test_user_report_id = "U604309abc8d63179970c2bd130a8862b"
    mocker.patch(
        "app.services.report_feedback.entry_user_report_feedback_comment_service.generate_id_str",
        return_value=test_user_report_id,
    )

    request = EntryUserReportFeedBackCommentRequest(
        comment="test_comment",
        user_id="test_user",
    )
    response = client.post(
        f"/report/{report_id}/feedback_comment", data=request.json()
    )

    assert response.status_code == 200
    assert response.json() == {
        "user_report_feedback_comment_id": test_user_report_id
    }


def test_post_user_report_feedback_comment_status_change(mocker):
    report_id = "xyz"

    test_user_report_id = "test_id"
    mocker.patch(
        "app.services.report_feedback.entry_user_report_feedback_comment_service.generate_id_str",
        return_value=test_user_report_id,
    )

    request = EntryUserReportFeedBackCommentRequest(
        comment="今すぐ救援に向かいます！",
        user_id="test_user",
    )
    response = client.post(
        f"/report/{report_id}/feedback_comment", data=request.json()
    )

    assert response.status_code == 200
    assert response.json() == {
        "user_report_feedback_comment_id": test_user_report_id
    }


def test_post_user_report_feedback_reaction(mocker):
    report_id = "xyz"

    test_user_report_feedback_reaction_id = "fgh"
    mocker.patch(
        "app.services.report_feedback.entry_user_report_feedback_reaction_service.generate_id_str",
        return_value=test_user_report_feedback_reaction_id,
    )

    request = EntryUserReportFeedBackReactionRequest(
        reaction="test_reaction",
        user_id="test_user",
    )
    response = client.post(
        f"/report/{report_id}/feedback_reaction", data=request.json()
    )

    assert response.status_code == 200
    assert response.json() == {
        "user_report_feedback_reaction_id": test_user_report_feedback_reaction_id
    }
