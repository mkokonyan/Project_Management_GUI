from dao.json_repository import JsonRepository
from entity.task import Task


class TaskRepository(JsonRepository):
    DB_FILENAME = "db/tasks.json"
    ENTITY_CLASS = Task

    def find_by_full_name(self, full_name: str) -> Task:
        result = [tsk for tsk in self.find_all() if full_name.lower() == tsk.name.lower()]
        if result:
            return result[0]

    def find_by_name_part(self, name_part: str) -> list[Task]:
        result = [tsk for tsk in self.find_all() if name_part.lower() in tsk.name.lower()]
        return result

    def find_by_description(self, descr_part: str) -> list[Task]:
        result = [tsk for tsk in self.find_all() if descr_part.lower() in tsk.description.lower()]
        return result

    def find_by_finished_status(self) -> list[Task]:
        result = [tsk for tsk in self.find_all() if tsk.is_finished]
        return result
