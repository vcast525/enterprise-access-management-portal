from src.auth.password_utils import verify_password
from src.models.user_model import User
from src.services.database_user_service import (
    get_user_by_username,
    save_user_to_database,
)


def register_user(
    username: str,
    email: str,
    password: str,
    role: str = "User",
) -> User:
    """
    Register a new user in the database.
    """

    return save_user_to_database(
        username=username,
        email=email,
        password=password,
        role=role,
    )


def login_user(
    username: str,
    password: str,
) -> User | None:
    """
    Validate user login credentials using database persistence.
    """

    user = get_user_by_username(
        username
    )

    if user is None:
        return None

    if verify_password(
        password,
        user.password,
    ):
        return user

    return None