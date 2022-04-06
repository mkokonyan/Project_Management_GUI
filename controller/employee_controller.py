from tkinter import messagebox

from controller.base_controller import BaseController
from view.create_account_view import CreateAccountView
from view.welcome_view import WelcomeView


class EmployeeController(BaseController):

    def show_create_account(self):
        self.view.forget()
        return CreateAccountView(self.view.root, self).pack()

    def go_back(self):
        self.view.forget()
        return WelcomeView(self.view.root, self).pack()

    def register(self, registration_data):
        result = self.service.register(**registration_data)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.view.forget()
        return WelcomeView(self.view.root, self).pack()

    def get_all_entities(self):
        return self._service.get_all_employees()

    def reload_all_entities(self) -> None:
        return self._service.reload_all_employees()

    def save_entities(self):
        return self._service.save_all_employees()
