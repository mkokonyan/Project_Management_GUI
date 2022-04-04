from datetime import datetime

from dao.employee_repository import EmployeeRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
from entity.employee import Employee
from entity.project import Project
from helpers.validators.project_validators import validate_project_name_length, validate_project_time_estimation, \
    validate_due_date, validate_username_existence, check_current_project_is_set, check_employee_is_not_assigned, \
    validate_project_name_dublication, check_employee_is_assigned


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

    @property
    def current_project(self):
        return self._current_project

    def set_current_project(self, project_name: str) -> Project:
        current_project = self._project_repository.find_by_full_name(project_name)
        self._current_project = current_project
        return current_project

    def add_new_project(self,
                        name: str,
                        client: str,
                        time_estimation: int,
                        due_date: str
                        ) -> Project:
        validate_project_name_dublication(name, self._project_repository)
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

        if not updated_prj.name == kwargs.get("name"):
            validate_project_name_dublication(kwargs.get("name"), self._project_repository)

        validate_project_name_length(kwargs.get("name"))
        validate_project_time_estimation(kwargs.get("time_estimation"))
        validate_due_date(datetime.strptime(kwargs.get("name"), "%Y-%m-%d"))

        setattr(updated_prj, "name", kwargs.get("name") if kwargs.get("name") else updated_prj.name)
        setattr(updated_prj, "client", kwargs.get("client") if kwargs.get("client") else updated_prj.client)
        setattr(updated_prj, "time_estimation", kwargs.get("time_estimation") if kwargs.get("time_estimation") else updated_prj.time_estimation)
        setattr(updated_prj, "due_date", kwargs.get("due_date") if kwargs.get("due_date") else updated_prj.client)


        self._project_repository.update(updated_prj)
        self._project_repository.save()

        return updated_prj

    def assign_employee(self, username: str) -> Employee:
        check_current_project_is_set(self._current_project)

        new_employee = self._employee_repository.find_by_id(username)

        validate_username_existence(new_employee)
        check_employee_is_not_assigned(new_employee, self._current_project)

        self.add_employee(username)
        new_employee.add_project(self._current_project.obj_id)

        self._project_repository.save()
        self._employee_repository.save()

        return new_employee

    def unassign_employee(self, username: str) -> Employee:
        employee_to_remove = self._employee_repository.find_by_id(username)

        validate_username_existence(employee_to_remove)
        check_employee_is_assigned(employee_to_remove, self._current_project)

        employee_tasks_id = [t_id for t_id in employee_to_remove.tasks_id if t_id in self._current_project.tasks_id]
        if employee_tasks_id:
            for t_id in employee_tasks_id:
                employee_to_remove.remove_task(t_id)
                setattr(self._task_repository.find_by_id(t_id), "employee", None)

        self.remove_employee(username)
        employee_to_remove.remove_project(self._current_project.obj_id)

        self._project_repository.save()
        self._employee_repository.save()
        self._task_repository.save()

        return employee_to_remove

    def get_all_projects(self) -> list[Project]:
        return self._project_repository.find_all()

    def save_projects(self) -> None:
        return self._project_repository.save()

    def load_all_projects(self) -> list[Project]:
        return self._project_repository.load()

    def add_employee(self, username: str) -> str:
        self.current_project.employees.append(username)
        return username

    def remove_employee(self, username: str) -> str:
        self.current_project.employees.remove(username)
        return username

