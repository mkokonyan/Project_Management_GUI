from tkinter import messagebox

from controller.base_controller import BaseController
from view.board_view import BoardView
from view.create_task_view import CreateTaskView
from view.edit_task_view import EditTaskView


class TaskController(BaseController):

    def show_create_task(self, current_project, employee_role):
        self.view.forget()
        return CreateTaskView(self.view.root, current_project, employee_role).pack()

    def show_edit_task(self, task, employee_role):
        self.view.forget()
        return EditTaskView(self.view.root, task, employee_role).pack()

    def get_project_tasks(self, prj_id):
        return self.service.get_project_tasks(prj_id)

    def create_task(self, task_data):
        result = self.service.add_new_task(**task_data)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.view.forget()
        return BoardView(self.view.root, self.view.root.prj_controller, self.view.current_project, self.view.employee_role).pack()

    def edit_task(self, task_id, edited_data, current_project):
        result = self.service.edit_task(task_id, **edited_data)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.view.forget()
        return BoardView(self.view.root, self.view.root.prj_controller,current_project, self.view.employee_role).pack()

    def delete_task(self, task_id):
        action_result = messagebox.askquestion("Warning", "Do you really want to delete task?")
        if action_result == "yes":
            self.service.delete_task(task_id)
            self.view.forget()
            return BoardView(self.view.root, self.view.root.prj_controller, self.view.current_project, self.view.employee_role).pack()

    def reload_all_tasks(self) -> None:
        return self.service.reload_all_tasks()

    def get_all_entities(self):
        return self._service.get_all_tasks()

    def reload_all_entities(self) -> None:
        return self._service.reload_all_tasks()

    def save_entities(self):
        return self._service.save_all_tasks()
