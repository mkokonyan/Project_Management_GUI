from tkinter import ttk


class ProjectsView(ttk.Frame):
    def __init__(self, root, project_controller, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.project_controller = project_controller
        self.project_controller.view = self

        # self._projects = self.project_controller.get_all_projects()
        # print(self._projects)