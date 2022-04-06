from tkinter import ttk

from view import create_account_view
from view.create_account_view import CreateAccountView
from view.welcome_view import WelcomeView


class MainView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.welcome_view = WelcomeView(self, self.root.emp_controller)
        self.welcome_view.pack()
        # self.register_view = CreateAccountView(self)
        self.pack()
