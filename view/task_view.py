from tkinter import ttk, Canvas, PhotoImage, Button, Label

from view.command.project.delete_project_command import DeleteProjectCommand
from view.command.project.show_board_command import ShowBoardCommand
from view.command.project.show_edit_project_command import ShowEditProjectCommand


class TaskView(ttk.Frame):
    def __init__(self, root, tsk_controller, tsk, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.tsk_controller = tsk_controller
        self.tsk_data = tsk

        self.canvas = Canvas(self, bg="#f9f4f5", height=75, width=40, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.background_img = PhotoImage(file=f"view/static/project/background.png")

        self.background = self.canvas.create_image(75, 75, image=self.background_img)

