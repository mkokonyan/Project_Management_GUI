from controller.base_controller import BaseController
from view.create_task_view import CreateTaskView


class TaskController(BaseController):

    def show_create_task(self, current_project, employee_role):
        self.view.forget()
        return CreateTaskView(self.view.root, current_project, employee_role).pack()

    def get_project_tasks(self, prj_id):
        return self.service.get_project_tasks(prj_id)

    def reload_all_tasks(self) -> None:
        return self.service.reload_all_tasks()

    def get_all_entities(self):
        return self._service.get_all_tasks()

    def reload_all_entities(self) -> None:
        return self._service.reload_all_tasks()

    def save_entities(self):
        return self._service.save_all_tasks()
