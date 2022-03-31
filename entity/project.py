from datetime import datetime

from dao.project_message_repository import ProjectMessageRepository
from dao.task_repository import TaskRepository
from entity.employee import Employee
from entity.task import Task
from helpers.id_generator_uuid import IdGeneratorUuid
from helpers.validators.project_validators import validate_project_time_estimation, validate_project_name_length, \
    validate_due_date


class Project:
    def __init__(self,
                 project_id: str = None,
                 project_name: str = None,
                 client: str = None,
                 time_estimation: int = None,
                 due_date: str = None,
                 idGenerator=IdGeneratorUuid,
                 ) -> None:
        self._obj_id = project_id
        self.name = project_name
        self._client = client
        self.time_estimation = time_estimation
        self.due_date = due_date
        self._employees: list[Employee] = []
        self._is_finished: bool = False
        self.tasks_repo = TaskRepository(IdGeneratorUuid)
        self.project_message_repo = ProjectMessageRepository(idGenerator)

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    @property
    def name(self):
        return self._project_name

    @name.setter
    def name(self, value):
        validate_project_name_length(value)
        self._project_name = value

    @property
    def client(self):
        return self._client

    @property
    def time_estimation(self):
        return self._time_estimation

    @time_estimation.setter
    def time_estimation(self, value):
        validate_project_time_estimation(value)
        self._time_estimation = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        new_due_date = datetime.strptime(value, "%Y-%m-%d")
        validate_due_date(new_due_date)
        self._due_date = new_due_date

    @property
    def employees(self):
        return self._employees

    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        if value and len(self.tasks_repo) == 0:
            self._is_finished = True

    def __repr__(self) -> str:
        return f"{self._project_name}"

    def get_info(self) -> str:
        return f"Project name: {self._project_name:<10.15s} " \
               f"| Client {self._client:<10.15s} " \
               f"| Employees assigned: {', '.join([str(e) for e in self._employees]) if self._employees else 'None':<30.40s} " \
               f"| Number of tasks: {len(self.tasks_repo):<3}" \
               f"| Project status:{'Archived' if self._is_finished else 'In progress':<10.11s}"
