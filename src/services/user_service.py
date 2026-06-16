from src.models.user_model import User

users = []

def register_user(
    username: str,
    email: str,
    password: str,
    role: str = "User",
) -> User:
    """
    Register a new user in memory.
    """

    user_id = len(users) + 1

    user = User(
        user_id=user_id,
        username=username,
        email=email,
        password=password,
        role=role,
        is_active=True,
    )

    users.append(user)

    return user