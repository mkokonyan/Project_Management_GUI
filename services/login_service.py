from dao.employee_repository import EmployeeRepository
from entity.employee import Employee
from helpers.validators.employee_validators import \
    validate_password, validate_name_length, validate_email, validate_username_match, validate_username, \
    validate_username_change


class LoginService:
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
        validate_username_match(username, password, self._employee_repository)
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
        validate_username(username, self._employee_repository)
        validate_password(password, confirm_password)
        validate_name_length(first_name, last_name)
        validate_email(email)

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

    def edit_profile(self, **kwargs) -> Employee:
        user = self.logged_user

        validate_username_change(user, kwargs["username"])
        validate_password(kwargs["password"], kwargs["confirm_password"])

        user.password = kwargs["password"]
        user.first_name = kwargs["first_name"]
        user.last_name = kwargs["last_name"]
        user.email = kwargs["email"]

        self._employee_repository.update(user)
        self._employee_repository.save()

        return user



