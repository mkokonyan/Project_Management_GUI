from dao.base_repository import BaseRepository
from entity.employee import Employee
from exceptions.existing_username_exception import ExistingUsernameException
from exceptions.username_not_found_exception import UsernameNotFoundException


class EmployeeRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(idGenerator=None)

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
