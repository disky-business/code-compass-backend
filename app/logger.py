import logging


# Configure logger for console output only
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(filename)s:%(funcName)s,%(lineno)d | %(message)s",
)
# Create logger instance
logger = logging.getLogger(__name__)
