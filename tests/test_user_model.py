import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.models.user_model import User


user = User(
    user_id=1,
    username="admin_user",
    email="admin@example.com",
    password="temporary_password",
    role="Admin",
    is_active=True
)

print(user)