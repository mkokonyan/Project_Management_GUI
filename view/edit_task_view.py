from tkinter import ttk, Canvas, PhotoImage, Button, Entry, StringVar, END
from tkinter.scrolledtext import ScrolledText

from view.command.project.show_board_command import ShowBoardCommand
from view.command.task.delete_task_command import DeleteTaskCommand
from view.command.task.edit_project_command import EditTaskCommand


class EditTaskView(ttk.Frame):

    def __init__(self, root, current_task, employee_role, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.current_task = current_task
        self.employee_role = employee_role
        self.logged_user_name = self.root.emp_controller.service.logged_user.username
        self.tsk_controller = self.root.tsk_controller
        self.prj_controller = self.root.prj_controller
        self.current_project = self.prj_controller.service.get_project(self.current_task.project_id)


        self.root.tsk_controller.view = self
        self.root.prj_controller.view = self
        self.edited_data = {}

        self.go_back_board_command = ShowBoardCommand(self.prj_controller, self.current_task.project_id,
                                                      self.employee_role)
        self.delete_task_command = DeleteTaskCommand(self.tsk_controller, self.current_task.obj_id)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/edit_task/entry_img.png")
        self.edit_task_img0 = PhotoImage(file=f"view/static/edit_task/img0.png")
        self.edit_task_hover_img1 = PhotoImage(file=f"view/static/edit_task/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/edit_task/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/edit_task/img3.png")
        self.delete_img4 = PhotoImage(file=f"view/static/edit_task/img4.png")
        self.delete_hover_img4 = PhotoImage(file=f"view/static/edit_task/img5.png")
        self.background_img = PhotoImage(file=f"view/static/edit_task/background.png")

        self.task_name_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.task_name_default_val = StringVar(root, value=self.current_task.name)
        self.task_name_entry = Entry(self, **entry_options, textvariable=self.task_name_default_val)
        self.task_name_entry.place(x=583, y=262, width=298, height=32)

        self.assigned_to_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.assigned_to_default_val = StringVar(root, value=self.current_task.employee)
        self.assigned_to_entry = Entry(self, **entry_options, state="disabled", disabledbackground="#E0E0E0",
                                       textvariable=self.assigned_to_default_val)
        self.assigned_to_entry.place(x=583, y=364, width=298, height=32)

        self.description_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.description_default_val = StringVar(root, value=self.current_task.description)
        self.description_entry = ScrolledText(self, **entry_options)
        self.description_entry.insert("1.0", self.description_default_val.get())
        self.description_entry.place(x=583, y=466, width=298, height=165)

        self.time_estimation_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.time_estimation_default_val = StringVar(root, value=self.current_task.time_estimation)
        self.time_estimation_entry = Entry(self, **entry_options, textvariable=self.time_estimation_default_val)
        self.time_estimation_entry.place(x=583, y=705, width=298, height=32)

        self.edit_project_btn = Button(self, image=self.edit_task_img0, borderwidth=0, highlightthickness=0,
                                       background="#f9f4f5", anchor="w", justify="left",
                                       command=self.get_edited_data, relief="flat", activebackground="#f9f4f5", )
        self.edit_project_btn.place(x=592, y=905, width=250, height=70)
        self.edit_project_btn.bind("<Enter>", self.edit_btn_on_enter)
        self.edit_project_btn.bind("<Leave>", self.edit_btn_on_leave)

        self.go_back_board_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                        command=self.go_back_board_command, relief="flat", bg="#f9f4f5",
                                        activebackground="#f9f4f5")
        self.go_back_board_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_board_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_board_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.delete_btn = Button(self, image=self.delete_img4, borderwidth=0, highlightthickness=0,
                                        command=self.delete_task_command, relief="flat", bg="#E5E4E4",
                                        activebackground="#E5E4E4")
        self.delete_btn.place(x=864, y=172, width=60, height=60)
        self.delete_btn.bind("<Enter>", self.delete_btn_on_enter)
        self.delete_btn.bind("<Leave>", self.delete_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

        if not self.logged_user_name == self.current_task.employee and not self.employee_role == "Admin":
            self.task_name_entry.configure(state="disabled", disabledbackground="#E0E0E0", disabledforeground="black")
            self.assigned_to_entry.configure(disabledforeground="black")
            self.description_entry.configure(state="disabled"),
            self.time_estimation_entry.configure(state="disabled", disabledbackground="#E0E0E0", disabledforeground="black")
            self.edit_project_btn.place_forget()
            self.delete_btn.place_forget()

    def get_edited_data(self):
        self.edited_data.update(
            {
                "name": self.task_name_entry.get(),
                "employee": self.assigned_to_default_val.get(),
                "description": self.description_entry.get('1.0', END).strip(),
                "time_estimation": self.time_estimation_entry.get()
            }
        )
        EditTaskCommand(self.tsk_controller, self.current_task.obj_id, self.edited_data, self.current_project)()

    def edit_btn_on_enter(self, e):
        self.edit_project_btn["image"] = self.edit_task_hover_img1

    def edit_btn_on_leave(self, e):
        self.edit_project_btn["image"] = self.edit_task_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_board_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_board_btn["image"] = self.go_back_img2

    def delete_btn_on_enter(self, e):
        self.delete_btn["image"] = self.delete_hover_img4

    def delete_btn_on_leave(self, e):
        self.delete_btn["image"] = self.delete_img4

