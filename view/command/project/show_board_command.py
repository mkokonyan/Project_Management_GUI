class ShowBoardCommand:
    def __init__(self, project_controller, project_id, employee_role):
        self.project_controller = project_controller
        self.project_id = project_id
        self.employee_role = employee_role

    def __call__(self):
        self.project_controller.show_board(self.project_id, self.employee_role)
