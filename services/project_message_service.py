from datetime import datetime

from dao.employee_repository import EmployeeRepository
from dao.project_message_repository import ProjectMessageRepository
from entity.project_message import ProjectMessage
from helpers.validators.project_message_validators import validate_message_content


class ProjectMessageService:
    def __init__(self, project_message_repository: ProjectMessageRepository, employee_repository: EmployeeRepository):
        self._project_message_repository = project_message_repository
        self._employee_repository = employee_repository

    @property
    def project_message_repository(self):
        return self._project_message_repository

    @property
    def employee_repository(self):
        return self._employee_repository

    @staticmethod
    def repos_save(*args) -> None:
        for repo in args:
            repo.save()

    def send_message(self, message, username) -> ValueError | ProjectMessage:
        employee = self._employee_repository.find_by_id(username)

        formatted_message = ""
        for i, letter in enumerate(message):
            if i % 170 == 0:
                formatted_message += "\n"
            formatted_message += letter
        formatted_message = formatted_message[1:]


        project_message = ProjectMessage(
            message=formatted_message,
            employee=username
        )

        try:
            validate_message_content(message)
        except ValueError as ex:
            return ex

        self._project_message_repository.create(project_message)

        employee.add_message(project_message.obj_id)

        self.repos_save(self._project_message_repository, self._employee_repository)

        return project_message

    def edit_message(self, message_id, edited_message) -> ProjectMessage:
        message_to_edit = self._project_message_repository.find_by_id(message_id)
        message_to_edit.message = edited_message
        message_to_edit.edited_on = datetime.now()

        self._project_message_repository.update(message_to_edit)

        self._project_message_repository.save()
        return message_to_edit

    def delete_message(self, message_id) -> ProjectMessage:
        message_to_delete = self._project_message_repository.find_by_id(message_id)
        employee_sent = self._employee_repository.find_by_id(message_to_delete.employee)

        employee_sent.remove_message(message_to_delete.obj_id)
        self._project_message_repository.delete_by_id(message_id)

        self.repos_save(self._project_message_repository, self._employee_repository)

        return message_to_delete

    def get_all_messages(self) -> list[ProjectMessage]:
        return self._project_message_repository.find_all()

    def get_all_messages_sorted_by_date(self) -> list[ProjectMessage]:
        return self._project_message_repository.find_all_messages_sorted_by_date()

    def reload_all_messages(self) -> None:
        return self._project_message_repository.load()

    def save_all_messages(self) -> None:
        return self._project_message_repository.save()
