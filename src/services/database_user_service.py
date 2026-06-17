import sqlite3

from src.database.database import (
    get_database_connection,
    initialize_database,
)
from src.models.user_model import User


def save_user_to_database(
    username: str,
    email: str,
    password: str,
    role: str,
) -> User:
    """
    Save a user record to the SQLite database.
    """

    initialize_database()

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (
                username,
                email,
                password,
                role,
                is_active
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                username,
                email,
                password,
                role,
                1,
            ),
        )

        connection.commit()

        user_id = cursor.lastrowid

        return User(
            user_id=user_id,
            username=username,
            email=email,
            password=password,
            role=role,
            is_active=True,
        )

    except sqlite3.IntegrityError:
        raise ValueError(
            "Username already exists. Please choose another username."
        )

    finally:
        connection.close()


def get_user_by_username(
    username: str,
) -> User | None:
    """
    Retrieve a user from the SQLite database by username.
    """

    initialize_database()

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            user_id,
            username,
            email,
            password,
            role,
            is_active
        FROM users
        WHERE username = ?
        """,
        (username,),
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return User(
        user_id=row["user_id"],
        username=row["username"],
        email=row["email"],
        password=row["password"],
        role=row["role"],
        is_active=bool(row["is_active"]),
    )