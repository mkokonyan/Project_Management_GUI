
from dao.base_repository import BaseRepository
from entity.task import Task


class TaskRepository(BaseRepository):
    def find_by_name(self, name_part: str) -> list[Task]:
        result = [tsk for tsk in self.find_all() if name_part.lower() in tsk.name.lower()]
        return result

    def find_by_description(self, descr_part: str) -> list[Task]:
        result = [tsk for tsk in self.find_all() if descr_part.lower() in tsk.description.lower()]
        return result

    def find_by_finished_status(self) -> list[Task]:
        result = [tsk for tsk in self.find_all() if tsk.is_finished]
        return result

