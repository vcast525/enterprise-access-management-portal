import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.services.user_service import (
    register_user,
    users,
)

new_user = register_user(
    username="standard_user",
    email="standard@example.com",
    password="temporary_password",
)

admin_user = register_user(
    username="admin_user",
    email="admin@example.com",
    password="admin_password",
    role="Admin",
)

print(new_user)
print(admin_user)
print(f"Total users registered: {len(users)}")