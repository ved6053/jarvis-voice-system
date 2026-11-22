import logging
import os

# setting logger
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "application.log")
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    os.makedirs(LOG_DIR, exist_ok=True)
    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)

    # Create a console handler to print logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

setup_logger()
