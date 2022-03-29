import os
from tkinter import Tk


class WindowView(Tk):
    icon_path = os.path.join(os.path.dirname(__file__), "static/window/mkk_logo.ico")

    def __init__(self):
        super().__init__()
        self.title("MK Project Management 1.00")
        self.geometry("1440x1024")
        self.configure(bg="#ffffff")
        self.iconbitmap(self.icon_path)
