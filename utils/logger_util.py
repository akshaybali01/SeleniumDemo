import logging
import os
from datetime import datetime


def create_logger(logger_name):
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file = os.path.join(logs_dir, f"{logger_name}_{time_stamp}.log")
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter("%(asctime)s,%(levelname)s,%(message)s")
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(asctime)s,%(levelname)s,%(message)s")
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
