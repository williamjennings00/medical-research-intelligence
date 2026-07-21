import sqlite3


DATABASE_PATH = "data/medical_research.db"


def connect_database():
    connection = sqlite3.connect(DATABASE_PATH)

    print("SQLite database connected")

    return connection


if __name__ == "__main__":
    connect_database()
