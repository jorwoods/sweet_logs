import logging.config
from typing import Any, Dict, Optional

import sweet_logs.config


def setup_logging(config: Optional[Dict[str, Any]] = None) -> None:
    """
    Set up logging configuration. If no configuration is provided, the default
    configuration is used. The default configuration is defined in
    sweet_logs.config.base_config.

    Parameters
    ----------
    config : Optional[Dict[str, Any]], optional
        A dictionary that contains configuration for the logger.
    """
    if config is None:
        config = sweet_logs.config.base_config
    logging.config.dictConfig(config)
