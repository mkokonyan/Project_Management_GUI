class LoginCommand:
    def __init__(self, employee_controller, login_data):
        self.employee_controller = employee_controller
        self.login_data = login_data

    def __call__(self):
        self.employee_controller.login(self.login_data)
