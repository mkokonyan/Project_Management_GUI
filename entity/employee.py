from helpers.validators.employee_validators import validate_username_length, validate_password, validate_email, validate_name_length


class Employee:
    def __init__(self,
                 username: str = None,
                 password: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 role: str = "Employee",
                 ) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._role = role

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        validate_username_length(value)
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        validate_password(value)
        self._password = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        validate_name_length(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        validate_name_length(value)
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        validate_email(value)
        self._email = value

    @property
    def role(self):
        return self._role

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_info(self) -> str:
        return f"Username: {self.username + '(' + self.role + ')':<20.15s} " \
               f"| Name: {self.first_name + ' ' + self.last_name:<20.15s} " \
               f"| Email: {self.email:<15.15s}"


class Admin(Employee):
    def __init__(self,
                 username: str = None,
                 password: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 role: str = "Admin",
                 ) -> None:
        super().__init__(username, password, first_name, last_name, email, role)
