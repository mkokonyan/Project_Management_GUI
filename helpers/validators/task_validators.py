from dao.task_repository import TaskRepository
from entity.employee import Employee
from entity.project import Project
from exceptions.entity_not_found_exception import EntityNotFoundException


def validate_task_name_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Task name must be at least 3 characters")


def validate_task_name_dublication(name: str, task_repo: TaskRepository, project: Project) -> None:
    task_names = [task_repo.find_by_id(t_id).name for t_id in project.tasks_id]
    if name in task_names:
        raise ValueError("Task with the same name already exist.")


def validate_task_time_estimation(hours: str) -> None:
    if int(hours) < 1:
        raise ValueError("Please enter valid hours (min 1 hour)")
