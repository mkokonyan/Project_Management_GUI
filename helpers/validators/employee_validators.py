import re

from dao.employee_repository import EmployeeRepository
from entity.employee import Employee
from exceptions.existing_username_exception import ExistingUsernameException
from exceptions.username_not_found_exception import UsernameNotFoundException


def validate_credentials_match(user: str, password: str, repo: EmployeeRepository):
    user = repo.find_by_id(user)
    if user is None:
        raise UsernameNotFoundException(f"Username not found. Please try again")
    if not password == user.password:
        raise ValueError("Passwords do not match. Please try again")


def validate_username(username: str, repo: EmployeeRepository) -> None:
    if repo.find_by_id(username):
        raise ExistingUsernameException(f"Username already exists")
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters")


def validate_name_length(first_name: str, last_name: str) -> None:
    if len(first_name) < 3 or len(last_name) < 3:
        raise ValueError("Name must be at least 3 characters")


def validate_password(password: str, confirm_password: str) -> None:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not re.search("[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search("[0-9]", password):
        raise ValueError("Password must contain at least one digit")
    if re.search("\s", password):
        raise ValueError("Password must not have whitespace characters")
    if not password == confirm_password:
        raise ValueError("Passwords do not match. Please try again")


def validate_email(email: str) -> None:
    expression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(expression, email):
        raise ValueError("Please enter a valid email address")


def validate_username_change(user: Employee, new_username: str):
    if not user:
        raise UsernameNotFoundException(f"You have to login")
    if not user.username == new_username:
        raise ValueError(f"You can't change your username")
