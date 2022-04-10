class EditTaskCommand:
    def __init__(self, task_controller, task_id, task_data, current_project):
        self.task_controller = task_controller
        self.task_id = task_id
        self.task_data = task_data
        self.current_project = current_project

    def __call__(self):
        self.task_controller.edit_task(self.task_id, self.task_data, self.current_project)
