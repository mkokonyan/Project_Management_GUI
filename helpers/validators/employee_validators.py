import re


def validate_username_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Username must be at least 3 characters")


def validate_name_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Name must be at least 3 characters")


def validate_password(password: str) -> None:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not re.search("[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search("[0-9]", password):
        raise ValueError("Password must contain at least one digit")
    if re.search("\s", password):
        raise ValueError("Password must not have whitespace characters")


def validate_email(email: str) -> None:
    expression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(expression, email):
        raise ValueError("Please enter a valid email address")
