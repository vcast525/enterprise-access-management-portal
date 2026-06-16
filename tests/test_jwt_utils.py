import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.auth.jwt_utils import (
    create_access_token,
    decode_access_token,
)


token = create_access_token(
    username="standard_user",
    role="User",
)

decoded_token = decode_access_token(
    token
)

invalid_token = decode_access_token(
    "invalid.token.value"
)

print(f"Token: {token}")
print(f"Decoded Token: {decoded_token}")
print(f"Invalid Token Result: {invalid_token}")