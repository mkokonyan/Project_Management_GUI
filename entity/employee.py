class Employee:
    def __init__(self,
                 username: str = None,
                 password: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 role: str = "Employee",
                 ) -> None:
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._role = role
        self._projects = []
        self._tasks = []
        self._project_messages = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def projects(self):
        return self._projects

    @projects.setter
    def projects(self, value):
        self._projects.append(value)

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

    @property
    def project_messages(self):
        return self._project_messages

    @project_messages.setter
    def project_messages(self, value):
        self._project_messages = value

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
