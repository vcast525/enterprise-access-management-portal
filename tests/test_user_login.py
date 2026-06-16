import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.auth.password_utils import hash_password
from src.services.user_service import (
    login_user,
    register_user,
)


hashed_password = hash_password(
    "SecurePassword123"
)

registered_user = register_user(
    username="standard_user",
    email="standard@example.com",
    password=hashed_password,
)

successful_login = login_user(
    username="standard_user",
    password="SecurePassword123",
)

failed_login_wrong_password = login_user(
    username="standard_user",
    password="WrongPassword123",
)

failed_login_wrong_username = login_user(
    username="missing_user",
    password="SecurePassword123",
)

print(f"Registered User: {registered_user}")
print(f"Successful Login: {successful_login}")
print(f"Failed Login Wrong Password: {failed_login_wrong_password}")
print(f"Failed Login Wrong Username: {failed_login_wrong_username}")