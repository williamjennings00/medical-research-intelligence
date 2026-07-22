"""
Basic configuration loader.

Reads settings from environment variables (with defaults), and exposes
them through a single `settings` object.

Usage:
    from config.settings import settings
    print(settings.DATABASE_URL)
"""

import os
from dotenv import load_dotenv

# Load variables from config/.env into the environment
load_dotenv()


class Config:
    def __init__(self):
        # Application
        self.APP_NAME = os.getenv("APP_NAME", "ScraperApp")
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
        self.DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

        # Database
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

        # User
        self.EMAIL = os.getenv("")


settings = Config()
