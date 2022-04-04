from dao.json_repository import JsonRepository
from entity.employee import Employee


class EmployeeRepository(JsonRepository):
    DB_FILENAME = "db/employees.json"
    ENTITY_CLASS = Employee

    def create(self, entity: Employee) -> Employee:
        self._entities[entity.username] = entity
        return entity

    def find_by_id(self, username: str) -> Employee:
        return self._entities.get(username)

    def update(self, entity: Employee) -> Employee:
        self.find_by_id(entity.username)
        self._entities[entity.username] = entity
        return entity

