import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.auth.role_utils import (
    has_admin_access,
    has_user_access,
    is_valid_role,
)


print(f"Admin valid: {is_valid_role('Admin')}")
print(f"User valid: {is_valid_role('User')}")
print(f"Manager valid: {is_valid_role('Manager')}")
print(f"Invalid role valid: {is_valid_role('Guest')}")

print(f"Admin has admin access: {has_admin_access('Admin')}")
print(f"User has admin access: {has_admin_access('User')}")

print(f"Admin has user access: {has_user_access('Admin')}")
print(f"Manager has user access: {has_user_access('Manager')}")
print(f"User has user access: {has_user_access('User')}")
print(f"Guest has user access: {has_user_access('Guest')}")