import datetime as dt
import logging
import json

import pytest

import sweet_logs


@pytest.fixture
def get_date(monkeypatch):
    def mock_date(*args, **kwargs):
        return dt.datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=dt.timezone.utc)

    monkeypatch.setattr(sweet_logs.formatters, "_date_from_timestamp", mock_date)


def test_JSONFormatter_no_fmt_keys(get_date):
    fmt = sweet_logs.formatters.JSONFormatter()

    # def __init__(self, name, level, pathname, lineno,
    #              msg, args, exc_info, func=None, sinfo=None, **kwargs):
    record = logging.LogRecord(name="test", level=10, pathname="pytest", lineno=10, exc_info=None, msg="test", args=())
    output = fmt.format(record)
    record_dict = json.loads(output)
    parsed_date = dt.datetime.fromisoformat(record_dict["timestamp"])

    assert record_dict["message"] == "test"
    assert parsed_date == dt.datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=dt.timezone.utc)
