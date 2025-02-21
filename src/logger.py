import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("logging has started")
    logging.error("This is an error message")
    logging.warning("This is a warning message")
    logging.debug("This is a debug message")
    logging.critical("This is a critical message")