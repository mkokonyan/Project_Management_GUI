class CreateTaskCommand:
    def __init__(self, task_controller, task_data):
        self.task_controller = task_controller
        self.task_data = task_data

    def __call__(self):
        self.task_controller.create_task(self.task_data)
