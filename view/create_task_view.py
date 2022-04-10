from tkinter import Canvas, PhotoImage, Button, Entry, ttk, END, StringVar
from tkinter.scrolledtext import ScrolledText

from view.command.project.create_project_command import CreateProjectCommand
from view.command.project.show_board_command import ShowBoardCommand


class CreateTaskView(ttk.Frame):

    def __init__(self, root, current_project, employee_role, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.current_project = current_project
        self.employee_role = employee_role
        self.root.tsk_controller.view = self
        self.root.prj_controller.view = self
        self.task_data = {}

        self.go_back_board_command = ShowBoardCommand(self.root.prj_controller, self.current_project.obj_id,
                                                      self.employee_role)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/create_task/entry_img.png")
        self.create_task_img0 = PhotoImage(file=f"view/static/create_task/img0.png")
        self.create_task_hover_img1 = PhotoImage(file=f"view/static/create_task/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/create_task/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/create_task/img3.png")
        self.background_img = PhotoImage(file=f"view/static/create_task/background.png")

        self.task_name_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.task_name_entry = Entry(self, **entry_options)
        self.task_name_entry.place(x=583, y=262, width=298, height=32)

        self.assigned_to_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.assigned_to_default_val = StringVar(root, value=self.root.emp_controller.service.logged_user.username)
        self.assigned_to_entry = Entry(self, **entry_options, state="disabled", disabledbackground="#E0E0E0", textvariable=self.assigned_to_default_val)
        self.assigned_to_entry.place(x=583, y=364, width=298, height=32)

        self.description_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.description_entry = ScrolledText(self, **entry_options)
        self.description_entry.place(x=583, y=466, width=298, height=165)

        self.time_estimation_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.time_estimation_entry = Entry(self, **entry_options)
        self.time_estimation_entry.place(x=583, y=705, width=298, height=32)

        self.create_project_btn = Button(self, image=self.create_task_img0, borderwidth=0, highlightthickness=0,
                                         background="#f9f4f5", anchor="w", justify="left",
                                         command=self.get_task_data, relief="flat", activebackground="#f9f4f5", )
        self.create_project_btn.place(x=592, y=905, width=250, height=70)
        self.create_project_btn.bind("<Enter>", self.register_btn_on_enter)
        self.create_project_btn.bind("<Leave>", self.register_btn_on_leave)

        self.go_back_board_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                        command=self.go_back_board_command, relief="flat", bg="#f9f4f5",
                                        activebackground="#f9f4f5")
        self.go_back_board_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_board_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_board_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

    def get_task_data(self):
        self.task_data.update(
            {
                "name": self.task_name_entry.get(),
                "employee": self.assigned_to_default_val.get(),
                "project_id": self.current_project.obj_id,
                "description": self.description_entry.get('1.0', END).strip(),
                "time_estimation": self.time_estimation_entry.get()
            }
        )
        print(self.task_data)
        # CreateTaskCommand(self.root.tsk_controller, self.task_data)()

    def register_btn_on_enter(self, e):
        self.create_project_btn["image"] = self.create_task_hover_img1

    def register_btn_on_leave(self, e):
        self.create_project_btn["image"] = self.create_task_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_board_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_board_btn["image"] = self.go_back_img2
