# logger.py
import logging

# Create custom logger
logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.DEBUG)  # Set level: DEBUG, INFO, WARNING, ERROR

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter for logs
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)
