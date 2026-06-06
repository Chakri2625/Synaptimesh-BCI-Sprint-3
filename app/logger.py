import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("BCI")
logger.setLevel(logging.INFO)

logger.handlers.clear()

file_handler = logging.FileHandler(
    "logs/command_log.txt",
    mode="a",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.propagate = False

logger.info("LOGGER INITIALIZED")