from dao.json_repository import JsonRepository
from entity.employee import Employee
from exceptions.existing_username_exception import ExistingUsernameException
from exceptions.username_not_found_exception import UsernameNotFoundException


class EmployeeRepository(JsonRepository):
    DB_FILENAME = "db/employees.json"
    ENTITY_CLASS = Employee

    def create(self, entity: Employee) -> Employee:
        if entity.username in self._entities:
            raise ExistingUsernameException(f"Username already exists!")
        self._entities[entity.username] = entity
        return entity

    def find_by_id(self, username: str) -> Employee:
        if username not in self._entities:
            raise UsernameNotFoundException(f"Username :{username} not found")
        return self._entities.get(username)

    def update(self, entity: Employee) -> Employee:
        if entity.username not in self._entities:
            raise ValueError(f"You can't change your username")
        self.find_by_id(entity.username)
        self._entities[entity.username] = entity
        return entity
