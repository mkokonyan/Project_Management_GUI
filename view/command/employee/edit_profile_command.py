class EditProfileCommand:
    def __init__(self, employee_controller, edited_data):
        self.employee_controller = employee_controller
        self.edited_data = edited_data

    def __call__(self):
        self.employee_controller.edit_profile(self.edited_data)
