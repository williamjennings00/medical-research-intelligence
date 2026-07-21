import logging
import sys


# Create the application logger
logger = logging.getLogger("medical_research")

# Set logging level
logger.setLevel(logging.INFO)


# Prevent duplicate handlers
if not logger.handlers:

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)

    # Add handler
    logger.addHandler(console_handler)
