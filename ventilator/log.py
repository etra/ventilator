from loguru import logger
import sys
import os


def init_logger():
    logger.info(f"Creating logger with log level {os.environ.get('LOG_LEVEL', 'ERROR')}")
    logger.remove()
    logger.add(sys.stderr, colorize=True, level=os.environ.get('LOG_LEVEL', 'ERROR'))
    return logger


log = init_logger()
