from dao.task_repository import TaskRepository
from entity.project import Project
from exceptions.entity_not_found_exception import EntityNotFoundException


def validate_task_name_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Task name must be at least 3 characters")


def validate_task_name_dublication(name: str, task_repo: TaskRepository) -> None:
    if task_repo.find_by_full_name(name):
        raise ValueError("Task with the same name already exist.")


def validate_project_name_existence(project: Project) -> None:
    if project is None:
        raise EntityNotFoundException(f"Project not found. Please try again")


def validate_description_length(value: str) -> None:
    if len(value) < 10:
        raise ValueError("Task description must be at least 10 characters")


def validate_task_time_estimation(hours: int) -> None:
    if hours < 1:
        raise ValueError("Please enter valid hours (min 1 hour)")
