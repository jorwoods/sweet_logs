"""Top-level package for Sweet Logs."""

__author__ = """Jordan Woods"""
__email__ = "jorwoods@example.com"
__version__ = "0.1.0"

import logging.config
from typing import Optional
from sweet_logs import config, formatters  # noqa: F401


def setup_logging(config: Optional[config.LogConfig] = None):
    """
    Set up logging configuration. If no configuration is provided, the default
    configuration is used. The default configuration is defined in
    sweet_logs.config.base_config.

    Parameters
    ----------
    config : Optional[config.LogConfig], optional
        A dictionary that contains configuration for the logger.
    """
    if config is None:
        config = config.base_config
    logging.config.dictConfig(config)
