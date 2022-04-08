class CreateProjectCommand:
    def __init__(self, project_controller, project_data):
        self.project_controller = project_controller
        self.project_data = project_data

    def __call__(self):
        self.project_controller.create_project(self.project_data)
