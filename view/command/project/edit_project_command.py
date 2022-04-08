class EditProjectCommand:
    def __init__(self, project_controller, project_id, project_data):
        self.project_controller = project_controller
        self.project_id = project_id
        self.project_data = project_data

    def __call__(self):
        self.project_controller.edit_project(self.project_id, self.project_data)
