from datetime import datetime


def validate_project_name_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Project name must be at least 3 characters")


def validate_project_time_estimation(hours: int) -> None:
    if hours < 10:
        raise ValueError("Please enter valid hours")


def validate_due_date(due_date: datetime) -> None:
    present_date = datetime.now()
    if due_date < present_date:
        raise ValueError("Please enter valid due date")
