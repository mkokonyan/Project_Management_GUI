from tkinter import messagebox

from controller.base_controller import BaseController
from entity.project import Project
from view.board_view import BoardView
from view.create_project_view import CreateProjectView
from view.edit_project_view import EditProjectView
from view.main_view import MainView


class ProjectController(BaseController):

    @staticmethod
    def get_project_details(project: Project) -> dict[str]:
        return {
            "obj_id": project.obj_id,
            "name": project.name,
            "client": project.client,
            "time_estimation": project.time_estimation,
            "due_date": project.due_date,
            "is_finished": 'ARCHIVED' if project.is_finished else 'IN PROGRESS'
        }

    def go_main_menu(self):
        self.reload_all_entities()
        self.view.forget()
        return MainView(self.view.root).pack()

    def create_project(self, registration_data):
        result = self.service.add_new_project(**registration_data)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.view.forget()
        return MainView(self.view.root).pack()

    def edit_project(self, project_id, edited_data):
        result = self.service.edit_project(project_id, **edited_data)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.view.forget()
        return MainView(self.view.root).pack()

    def delete_project(self, project_id):
        action_result = messagebox.askquestion("Warning", "Do you really want to delete project?")
        if action_result == "yes":
            self.service.delete_project(project_id)
            self.view.forget()
            return MainView(self.view.root).pack()

    def show_create_project(self):
        self.view.forget()
        return CreateProjectView(self.view.root).pack()

    def show_edit_project(self, project_id):
        project_to_edit = self.service.get_project(project_id)
        self.view.forget()
        return EditProjectView(self.view.root, project_to_edit).pack()

    def show_board(self, project_id):
        project = self.service.get_project(project_id)
        self.view.forget()
        return BoardView(self.view.root, project).pack()

    def get_all_entities(self):
        return self._service.get_all_projects()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_projects()

    def save_entities(self):
        return self._service.save_all_projects()



