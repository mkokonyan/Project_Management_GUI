class DeleteProjectCommand:
    def __init__(self, project_controller, project_id):
        self.project_controller = project_controller
        self.project_id = project_id

    def __call__(self):
        self.project_controller.delete_project(self.project_id)
