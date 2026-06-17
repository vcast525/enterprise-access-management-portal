import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/enterprise_access.db")


def get_database_connection():
    """
    Create and return a SQLite database connection.
    """

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create required database tables.
    """

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            is_active INTEGER NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()