class Employee:
    def __init__(self,
                 user_id: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 password: str = None,
                 email: str = None,
                 role: str = "Employee",
                 ):
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        self._email = email
        self._role = role

    def __str__(self):
        return f"{self._username}({self._role}): {self._first_name} {self._last_name}"


class Admin(Employee):
    def __init__(self,
                 user_id: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 password: str = None,
                 email: str = None,
                 role: str = "Admin",
                 ):
        super().__init__(user_id, first_name, last_name, username, password, email, role)
