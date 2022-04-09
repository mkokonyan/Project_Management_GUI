from datetime import datetime

from dao.project_repository import ProjectRepository
from entity.employee import Employee
from entity.project import Project
from entity.task import Task
from exceptions.entity_not_found_exception import EntityNotFoundException
from exceptions.tasks_not_finished_exception import TasksNotFinishedException
from exceptions.username_not_found_exception import UsernameNotFoundException


def validate_project_name_length(name: str) -> None:
    if len(name) < 3:
        raise ValueError("Project name must be at least 3 characters")


def validate_project_name_dublication(name: str, project_repo: ProjectRepository) -> None:
    if project_repo.find_by_full_name(name):
        raise ValueError("Project with the same name already exist.")


def validate_project_time_estimation(hours: str) -> None:
    if int(hours) < 10:
        raise ValueError("Please enter valid hours")


def validate_due_date(due_date: datetime) -> None:
    present_date = datetime.now()
    if due_date < present_date:
        raise ValueError("Please enter valid due date")


def validate_username_existence(user: Employee) -> None:
    if user is None:
        raise UsernameNotFoundException(f"Username not found. Please try again")



def check_employee_is_not_assigned(employee: Employee, project: Project) -> bool:
    if project.obj_id in employee.projects_id:
        raise ValueError(f"Current user is already assigned to this project")
    return True


def check_employee_is_assigned(employee: Employee, project: Project) -> bool:
    if project.obj_id not in employee.projects_id:
        raise ValueError(f"Current user is not assigned to this project")
    return True


def validate_tasks_count(project: Project, project_tasks: list[Task]) -> None:
    if len(project.tasks_id):
        for t in project_tasks:
            if not t.status == "DONE" and not t.is_finished:
                raise TasksNotFinishedException(f"Project has unfinished tasks.")
