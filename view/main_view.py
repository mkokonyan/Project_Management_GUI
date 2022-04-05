from tkinter import ttk

from view.welcome_view import WelcomeView


class MainView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.welcome_view = WelcomeView(self)

