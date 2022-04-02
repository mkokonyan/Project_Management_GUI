from datetime import datetime

from dao.employee_repository import EmployeeRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
from entity.employee import Employee
from entity.project import Project
from helpers.validators.project_validators import validate_project_name_length, validate_project_time_estimation, \
    validate_due_date, validate_username_existence, check_current_project_is_set, check_employee_is_not_assigned


class ProjectService:
    def __init__(self,
                 project_repository: ProjectRepository,
                 employee_repository: EmployeeRepository,
                 task_repository: TaskRepository
                 ):
        self._project_repository = project_repository
        self._employee_repository = employee_repository
        self._task_repository = task_repository
        self._current_project = None

    @property
    def project_repository(self):
        return self._project_repository

    @property
    def employee_repository(self):
        return self._employee_repository

    @property
    def task_repository(self):
        return self._task_repository

    def add_new_project(self,
                        name: str,
                        client: str,
                        time_estimation: int,
                        due_date: str
                        ) -> Project:
        validate_project_name_length(name)
        validate_project_time_estimation(time_estimation)
        validate_due_date(datetime.strptime(due_date, "%Y-%m-%d"))

        project = Project(
            name=name,
            client=client,
            time_estimation=time_estimation,
            due_date=due_date
        )

        self._project_repository.create(project)
        self._project_repository.save()
        return project

    def edit_project(self, **kwargs) -> Project:
        check_current_project_is_set(self._current_project)
        updated_prj = self._current_project

        validate_project_name_length(kwargs["name"])
        validate_project_time_estimation(kwargs["time_estimation"])
        validate_due_date(datetime.strptime(kwargs["due_date"], "%Y-%m-%d"))

        updated_prj.name = kwargs["name"]
        updated_prj.client = kwargs["client"]
        updated_prj.time_estimation = kwargs["time_estimation"]
        updated_prj.due_date = kwargs["due_date"]

        self._project_repository.update(updated_prj)
        self._project_repository.save()

        return updated_prj

    def get_all_projects(self) -> list[Project]:
        return self._project_repository.find_all()

    def save_projects(self) -> None:
        return self._project_repository.save()

    def load_all_projects(self) -> list[Project]:
        return self._project_repository.load()

    def set_current_project(self, project_name: str) -> Project:
        current_project = self._project_repository.find_by_full_name(project_name)
        self._current_project = current_project
        return current_project

    def assign_employee(self, username: str) -> Employee:
        check_current_project_is_set(self._current_project)

        employee_to_add = self._employee_repository.find_by_id(username)
        validate_username_existence(employee_to_add)
        check_employee_is_not_assigned(employee_to_add, self._current_project)

        #TODO to check assignment
        self._current_project.employees(employee_to_add)
        employee_to_add.projects(self._current_project)

        self._project_repository.save()
        self._employee_repository.save()

        return employee_to_add