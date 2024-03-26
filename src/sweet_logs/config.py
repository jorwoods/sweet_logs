import sys
from typing import Dict, List, Literal, TypedDict

if sys.version_info.minor < 12:
    from typing_extensions import NotRequired
else:
    from typing import NotRequired


LogFormattersConfig = TypedDict(
    "LogFormattersConfig",
    {
        "format": NotRequired[str],
        "datefmt": NotRequired[str],
        "style": NotRequired[str],
        "()": NotRequired[str],
    },
)


log_levels = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]


class LogLoggers(TypedDict):
    level: NotRequired[log_levels]
    filters: NotRequired[List[str]]
    propagate: NotRequired[bool]
    handlers: NotRequired[List[str]]


LogHandlers = TypedDict(
    "LogHandlers",
    {
        "class": str,
        "level": NotRequired[log_levels],
        "formatter": NotRequired[str],
        "filters": NotRequired[List[str]],
    },
)


class LogConfig(TypedDict):
    """
    A dictionary that contains configuration for the logger.
    """

    version: Literal[1]
    formatters: NotRequired[Dict[str, LogFormattersConfig]]
    filters: NotRequired[Dict[str, dict]]
    handlers: NotRequired[Dict[str, LogHandlers]]
    root: NotRequired[LogLoggers]
    incremental: NotRequired[bool]
    disable_existing_loggers: NotRequired[bool]
    loggers: NotRequired[Dict[str, LogLoggers]]


base_config: LogConfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "sweet_logs.formatters.JSONFormatter",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "fmt_keys": {
                "line": "lineno",
                "function": "funcName",
                "logger": "name",
                "relative_created": "relativeCreated",
                "thread": "thread",
                "thread_name": "threadName",
                "process": "process",
                "process_name": "processName",
                "task_name": "taskName",
            },
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
}
