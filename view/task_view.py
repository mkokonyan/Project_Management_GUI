from tkinter import Button, Frame

from view.command.task.show_edit_task_command import ShowEditTaskCommand


class TaskView(Frame):
    def __init__(self, root, tsk_controller, tsk, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.tsk_controller = tsk_controller
        self.tsk = tsk

        self.show_edit_task_command = ShowEditTaskCommand(self.tsk_controller, self.tsk, self.tsk_controller.view.employee_role)

        self.tsk_btn = Button(self, borderwidth=0, highlightthickness=0, background="#771859",
                              activebackground="#D945AA", relief="flat", text=f"{self.tsk.name}\n/{self.tsk.employee}/",
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859",
                              command=self.show_edit_task_command)
        self.tsk_btn.place(x=0, y=0, width=260, height=45)

