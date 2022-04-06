from tkinter import ttk

from view.register_view import RegisterView
from view.welcome_view import WelcomeView


class MainView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.register_view = RegisterView(self)
        self.welcome_view = WelcomeView(self)
        self.pack()
