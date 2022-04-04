from dao.employee_repository import EmployeeRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
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
        return self._project_repository

    def add_new_task(self,
                     name: str,
                     employee: str,
                     project: str,
                     description: str,
                     time_estimation: int,
                     ) -> Task:
        employee_to_add = self._employee_repository.find_by_id(employee)
        project_to_add = self._project_repository.find_by_full_name(project)

        validate_task_name_length(name)
        validate_task_name_dublication(name, self._task_repository)
        validate_username_existence(employee_to_add)
        validate_project_name_existence(project_to_add)
        validate_description_length(description)
        validate_task_time_estimation(time_estimation)

        task = Task(
            name=name,
            employee=employee,
            project=project,
            description=description,
            time_estimation=time_estimation,
        )
        self._task_repository.create(task)



        employee_to_add.tasks_id.append(task.obj_id)
        project_to_add.tasks_id.append(task.obj_id)
        if employee_to_add.username not in project_to_add.employees:
            project_to_add.employees.append(employee_to_add.username)

        self._task_repository.save()
        self._project_repository.save()
        self._employee_repository.save()

        return task
