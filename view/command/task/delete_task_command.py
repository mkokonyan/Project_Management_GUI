class DeleteTaskCommand:
    def __init__(self, task_controller, task_id):
        self.task_controller = task_controller
        self.task_id = task_id

    def __call__(self):
        self.task_controller.delete_task(self.task_id)
