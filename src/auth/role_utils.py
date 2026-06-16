ADMIN_ROLE = "Admin"
USER_ROLE = "User"
MANAGER_ROLE = "Manager"


def is_valid_role(role: str) -> bool:
    """
    Check whether a role is supported.
    """

    valid_roles = [
        ADMIN_ROLE,
        USER_ROLE,
        MANAGER_ROLE,
    ]

    return role in valid_roles


def has_admin_access(role: str) -> bool:
    """
    Check whether a role has admin access.
    """

    return role == ADMIN_ROLE


def has_user_access(role: str) -> bool:
    """
    Check whether a role has standard user access.
    """

    return role in [
        USER_ROLE,
        MANAGER_ROLE,
        ADMIN_ROLE,
    ]