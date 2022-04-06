class RegisterCommand:
    def __init__(self, employee_controller, registration_data):
        self.employee_controller = employee_controller
        self.registration_data = registration_data

    def __call__(self):
        self.employee_controller.register(self.registration_data)
