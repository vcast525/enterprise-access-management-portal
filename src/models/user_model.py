from dataclasses import dataclass

@dataclass
class User:
    """
    Represents a user in the Enterprise Access Management Portal.
    """

    user_id: int
    username: str
    email: str
    password: str
    role: str = "User"
    is_active: bool = True