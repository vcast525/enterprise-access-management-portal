import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.auth.password_utils import (
    hash_password,
    verify_password,
)


plain_password = "SecurePassword123"

hashed_password = hash_password(
    plain_password
)

print(f"Plain Password: {plain_password}")
print(f"Hashed Password: {hashed_password}")

correct_password = verify_password(
    plain_password,
    hashed_password,
)

incorrect_password = verify_password(
    "WrongPassword123",
    hashed_password,
)

print(f"Correct password valid: {correct_password}")
print(f"Incorrect password valid: {incorrect_password}")