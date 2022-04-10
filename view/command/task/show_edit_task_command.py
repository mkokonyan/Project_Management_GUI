class ShowEditTaskCommand:
    def __init__(self, tsk_controller, task, employee_role):
        self.tsk_controller = tsk_controller
        self.task = task
        self.employee_role = employee_role

    def __call__(self):
        self.tsk_controller.show_edit_task(self.task, self.employee_role)
