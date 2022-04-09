from dao.employee_repository import EmployeeRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
from entity.employee import Employee
from entity.task import Task
from helpers.validators.project_validators import validate_username_existence
from helpers.validators.task_validators import validate_task_name_length, validate_description_length, \
    validate_task_time_estimation, validate_project_name_existence, validate_task_name_dublication


class TaskService:
    def __init__(self,
                 task_repository: TaskRepository,
                 project_repository: ProjectRepository,
                 employee_repository: EmployeeRepository,
                 ):
        self._task_repository = task_repository
        self._project_repository = project_repository
        self._employee_repository = employee_repository

    @property
    def task_repository(self):
        return self._task_repository

    @property
    def project_repository(self):
        return self._project_repository

    @property
    def employee_repository(self):
        return self._employee_repository

    @staticmethod
    def repos_save(*args) -> None:
        for repo in args:
            repo.save()

    def add_new_task(self,
                     name: str,
                     employee: str,
                     project_id: str,
                     description: str,
                     time_estimation: int,
                     ) -> Task:

        employee_to_add = self._employee_repository.find_by_id(employee)
        project_to_add = self._project_repository.find_by_id(project_id)

        validate_task_name_length(name)
        validate_task_name_dublication(name, self._task_repository, project_to_add)
        validate_username_existence(employee_to_add)
        validate_project_name_existence(project_to_add)
        validate_description_length(description)
        validate_task_time_estimation(time_estimation)

        task = Task(
            name=name,
            employee=employee,
            project_id=project_id,
            description=description,
            time_estimation=time_estimation,
        )
        self._task_repository.create(task)

        employee_to_add.tasks_id.append(task.obj_id)
        project_to_add.tasks_id.append(task.obj_id)
        if employee_to_add.username not in project_to_add.employees:
            project_to_add.add_employee(employee_to_add.username)
            employee_to_add.add_project(project_to_add.obj_id)

        self.repos_save(self._task_repository, self._project_repository, self._employee_repository)

        return task

    def edit_task(self, task_id, **kwargs) -> Task:

        task_to_edit = self._task_repository.find_by_id(task_id)
        project_to_edit = self._project_repository.find_by_id(task_to_edit.project_id)
        employee_to_edit = self._employee_repository.find_by_id(task_to_edit.employee)

        if kwargs.get("name") and not task_to_edit.name == kwargs.get("name"):
            validate_task_name_dublication(kwargs.get("name"), self._task_repository, project_to_edit)

        if kwargs.get("employee") and not kwargs.get("employee") == employee_to_edit.username:
            self.set_new_employee(task_id, kwargs.get("employee"))

        validate_task_name_length(kwargs.get("name"))
        validate_project_name_existence(project_to_edit)
        validate_description_length(kwargs.get("description"))
        validate_task_time_estimation(kwargs.get("time_estimation"))

        setattr(task_to_edit, "name", kwargs.get("name") if kwargs.get("name") else task_to_edit.name)
        setattr(task_to_edit, "description",
                kwargs.get("description") if kwargs.get("description") else task_to_edit.description)
        setattr(task_to_edit, "time_estimation",
                kwargs.get("time_estimation") if kwargs.get("time_estimation") else task_to_edit.time_estimation)
        setattr(task_to_edit, "status", kwargs.get("status") if kwargs.get("status") else task_to_edit.status)

        self._task_repository.update(task_to_edit)
        if employee_to_edit.username not in project_to_edit.employees:
            project_to_edit.add_employee(employee_to_edit.username)
        if task_to_edit.obj_id not in employee_to_edit.tasks_id:
            employee_to_edit.add_task(task_to_edit.obj_id)

        self.repos_save(self._task_repository, self._project_repository, self._employee_repository)

        return task_to_edit

    def delete_task(self, task_id) -> Task:
        task_to_delete = self._task_repository.find_by_id(task_id)
        project_to_edit = self._project_repository.find_by_id(task_to_delete.project_id)
        employee_to_edit = self._employee_repository.find_by_id(task_to_delete.employee)

        if task_to_delete.obj_id in employee_to_edit.tasks_id:
            employee_to_edit.remove_task(task_id)
        if task_to_delete.obj_id in project_to_edit.tasks_id:
            project_to_edit.remove_task(task_id)

        self._task_repository.delete_by_id(task_id)

        self.repos_save(self._task_repository, self._project_repository, self._employee_repository)
        return task_to_delete

    def set_new_employee(self, task_id: str, username: str) -> Employee:
        task_to_set = self._task_repository.find_by_id(task_id)
        employee_to_remove = self._employee_repository.find_by_id(task_to_set.employee)
        employee_to_set = self._employee_repository.find_by_id(username)
        project_to_set = self._project_repository.find_by_id(task_to_set.project_id)

        validate_username_existence(employee_to_set)

        if employee_to_remove:
            employee_to_remove.remove_task(task_id)

        task_to_set.employee = username
        employee_to_set.add_task(task_id)
        project_to_set.add_employee(employee_to_set.username)

        self.repos_save(self._task_repository, self._project_repository, self._employee_repository)
        return employee_to_set

    def set_task_finish_status(self, task_id: str) -> Task:
        task_to_set = self._task_repository.find_by_id(task_id)
        task_to_set._is_finished = not task_to_set._is_finished
        self._task_repository.save()

        return task_to_set

    def get_all_tasks(self) -> list[Task]:
        return self._task_repository.find_all()

    def get_project_tasks(self, prj_id) -> list[Task]:
        return self._task_repository.find_by_project_id(prj_id)

    def reload_all_tasks(self) -> None:
        return self._task_repository.load()

    def save_all_tasks(self) -> None:
        return self._task_repository.save()
