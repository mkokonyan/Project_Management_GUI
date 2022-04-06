from tkinter import ttk


class ProjectsView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.root.prj_controller.view = self
        self.prj_controller = self.root.prj_controller

        self._projects = self.prj_controller.get_all_entities()
        print(self._projects)