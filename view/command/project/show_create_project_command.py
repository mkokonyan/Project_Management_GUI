class ShowCreateProjectCommand:
    def __init__(self, prj_controller):
        self.prj_controller = prj_controller

    def __call__(self):
        self.prj_controller.show_create_project()
