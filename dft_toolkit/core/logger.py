"""
=========================================================
DFT Toolkit for VASP
Logging Manager
=========================================================
"""

import logging
from pathlib import Path

from dft_toolkit.core.config import ConfigManager


def get_logger(name="DFTToolkit"):
    """
    Create and return a configured logger.
    """

    logger = logging.getLogger(name)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    cfg = ConfigManager().load()

    level_name = cfg.get("logging.level", "INFO")
    log_file = cfg.get("logging.file", "logs/dft.log")

    level = getattr(logging, level_name.upper(), logging.INFO)

    logger.setLevel(level)

    root = cfg.root
    logfile = root / log_file

    logfile.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":

    log = get_logger()

    log.info("DFT Toolkit logger started.")
    log.warning("This is a warning.")
    log.error("This is an error.")

    print("\nLog file created successfully.")
