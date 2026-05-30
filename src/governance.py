ALLOWED_USERS = [
    "admin",
    "analyst"
]

def can_access(user):

    return user in ALLOWED_USERS
