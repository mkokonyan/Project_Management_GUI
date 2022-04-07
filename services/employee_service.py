
from dao.employee_repository import EmployeeRepository
from entity.employee import Employee
from exceptions.existing_username_exception import ExistingUsernameException
from exceptions.username_not_found_exception import UsernameNotFoundException
from helpers.validators.employee_validators import \
    validate_password, validate_name_length, validate_email, validate_credentials_match, validate_username

class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self._employee_repository = employee_repository
        self._logged_user = None

    @property
    def employee_repository(self):
        return self._employee_repository

    @property
    def logged_user(self):
        return self._logged_user

    def login(self,
              username: str,
              password: str
              ) -> Employee:

        try:
            validate_credentials_match(username, password, self._employee_repository)
        except (UsernameNotFoundException, ValueError) as ex:
            return ex

        user = self._employee_repository.find_by_id(username)
        self._logged_user = user
        return user

    def logout(self) -> None:
        self._logged_user = None

    def register(self,
                 username: str,
                 password: str,
                 confirm_password: str,
                 first_name: str,
                 last_name: str,
                 email: str
                 ) -> Employee:

        try:
            validate_username(username, self._employee_repository)
            validate_password(password, confirm_password)
            validate_email(email)
            validate_name_length(first_name, last_name)
        except (ValueError, UsernameNotFoundException, ExistingUsernameException) as ex:
            return ex

        user = Employee(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        self._employee_repository.create(user)
        self._employee_repository.save()
        return user

    def edit_profile(self, **kwargs):
        user = self.logged_user

        try:
            validate_password(kwargs.get("password"), kwargs.get("confirm_password"))
            validate_email(kwargs.get("email"))
            validate_name_length(kwargs.get("first_name"), kwargs.get("last_name"))
        except ValueError as ex:
            return ex

        user.password = kwargs["password"]
        user.first_name = kwargs["first_name"]
        user.last_name = kwargs["last_name"]
        user.email = kwargs["email"]

        self._employee_repository.update(user)
        self._employee_repository.save()

        return user

    def get_logged_user_details(self) -> dict[str]:
        return {
            "username": self.logged_user.username,
            "email": self.logged_user.email,
            "first_name": self.logged_user.first_name,
            "last_name": self.logged_user.last_name
        }

    def get_all_employees(self):
        return self._employee_repository.find_all()

    def reload_all_employees(self) -> None:
        self._employee_repository.load()

    def save_all_employees(self):
        return self._employee_repository.save()
