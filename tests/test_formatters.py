import datetime as dt
import logging
import json

# import pytest

import sweet_logs


def test_JSONFormatter_no_fmt_keys():
    fmt = sweet_logs.formatters.JSONFormatter()

    # def __init__(self, name, level, pathname, lineno,
    #              msg, args, exc_info, func=None, sinfo=None, **kwargs):
    record = logging.LogRecord(name="test", level=10, pathname="pytest", lineno=10, exc_info=None, msg="test", args=())
    output = fmt.format(record)
    record_dict = json.loads(output)
    dt.datetime.fromisoformat(record_dict["timestamp"])

    assert record_dict["message"] == "test"
