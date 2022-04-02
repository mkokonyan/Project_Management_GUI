from dao.employee_repository import EmployeeRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository


class ProjectService:
    def __init__(self,
                 project_repository: ProjectRepository,
                 employee_repository: EmployeeRepository,
                 task_repository: TaskRepository
                 ):
        self._project_repository = project_repository
        self._employee_repository = employee_repository
        self._task_repository = task_repository

    @property
    def project_repository(self):
        return self._project_repository

    @property
    def employee_repository(self):
        return self._employee_repository

    @property
    def task_repository(self):
        return self._task_repository

    def add_new_project(self):
        pass

