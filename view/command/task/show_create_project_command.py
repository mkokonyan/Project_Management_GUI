class ShowCreateTaskCommand:
    def __init__(self, tsk_controller, current_project, employee_role):
        self.tsk_controller = tsk_controller
        self.current_project = current_project
        self.employee_role = employee_role

    def __call__(self):
        self.tsk_controller.show_create_task(self.current_project, self.employee_role)
