from datetime import datetime


def validate_task_name_length(value: str) -> None:
    if len(value) < 3:
        raise ValueError("Task name must be at least 3 characters")


def validate_description_length(value: str) -> None:
    if len(value) < 10:
        raise ValueError("Task description must be at least 10 characters")


def validate_task_time_estimation(hours: int) -> None:
    if hours < 1:
        raise ValueError("Please enter valid hours (more than 1 hour)")
