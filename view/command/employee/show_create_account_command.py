class ShowCreateAccountCommand:
    def __init__(self, employee_controller):
        self.employee_controller = employee_controller

    def __call__(self):
        self.employee_controller.show_create_account()
