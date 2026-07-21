import sqlite3


DATABASE_PATH = "data/medical_research.db"
from utils.logger import logger

def connect_database():
    connection = sqlite3.connect(DATABASE_PATH)

    logger.info("SQLite database connected")

    return connection


if __name__ == "__main__":
    connect_database()
