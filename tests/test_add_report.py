from unittest.mock import patch
from app.services.report import entry_user_report_service


def test_add_report_with_valid_inputs(mocker):
    uid = "test_user_id"
    lat = 12.345678
    lon = 98.7654321

    mocker.patch(
        "app.services.report.entry_user_report_service.generate_id_str",
        return_value="xyz987",
    )
    with patch(
        "app.services.report.entry_user_report_service.generate_id_str",
        return_value="xyz987",
    ):
        report_id = entry_user_report_service.add_report(uid, lat, lon)

    assert report_id == "xyz987"
