import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.auth.password_utils import hash_password
from src.services.database_user_service import (
    get_user_by_username,
    save_user_to_database,
)


hashed_password = hash_password(
    "SecurePassword123"
)

saved_user = save_user_to_database(
    username="database_user",
    email="database@example.com",
    password=hashed_password,
    role="Admin",
)

retrieved_user = get_user_by_username(
    "database_user"
)

missing_user = get_user_by_username(
    "missing_user"
)

print(f"Saved User: {saved_user}")
print(f"Retrieved User: {retrieved_user}")
print(f"Missing User: {missing_user}")