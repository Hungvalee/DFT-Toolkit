"""
=========================================================
DFT Toolkit for VASP
Logging Manager
=========================================================
"""

import logging
from pathlib import Path

from python.core.config import get_value


def get_logger(name="DFTToolkit"):
    """
    Create and return a configured logger.
    """

    logger = logging.getLogger(name)

    # Tránh tạo nhiều handler nếu gọi nhiều lần
    if logger.handlers:
        return logger

    level_name = get_value("logging", "level", default="INFO")
    log_file = get_value("logging", "file", default="logs/dft.log")

    level = getattr(logging, level_name.upper(), logging.INFO)

    logger.setLevel(level)

    root = Path(__file__).resolve().parents[2]
    logfile = root / log_file

    logfile.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # File handler
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(formatter)

    # Console handler
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
