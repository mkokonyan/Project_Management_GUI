from tkinter import ttk


class ProjectsView(ttk.Frame):
    def __init__(self, root, project_controller, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.project_controller = project_controller
        self.project_controller.view = self
