from tkinter import ttk, Canvas, PhotoImage, Button, Label

from view.command.project.delete_project_command import DeleteProjectCommand
from view.command.project.show_board_command import ShowBoardCommand
from view.command.project.show_edit_project_command import ShowEditProjectCommand


class ProjectView(ttk.Frame):
    def __init__(self, root, prj_data, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_data = prj_data
        self.prj_controller = self.root.prj_controller

        self.delete_project_command = DeleteProjectCommand(self.prj_controller, prj_data.get("obj_id"))
        self.edit_project_command = ShowEditProjectCommand(self.prj_controller, prj_data.get("obj_id"))
        self.show_board_command = ShowBoardCommand(self.prj_controller, prj_data.get("obj_id"), self.root.employee_role)

        self.canvas = Canvas(self, bg="#f9f4f5", height=150, width=400, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.delete_img = PhotoImage(file=f"view/static/project/img0.png")
        self.edit_img = PhotoImage(file=f"view/static/project/img1.png")
        self.background_img = PhotoImage(file=f"view/static/project/background.png")
        self.background_hover_img = PhotoImage(file=f"view/static/project/background1.png")

        self.prj_btn = Button(self, image=self.background_img, borderwidth=0, highlightthickness=0,
                              background="#e5e4e4", activebackground="#e5e4e4", relief="flat",
                              command=self.show_board_command)
        self.prj_btn.place(x=18, y=0, width=367, height=150)
        self.prj_btn.bind("<Enter>", self.prj_btn_on_enter)
        self.prj_btn.bind("<Leave>", self.prj_btn_on_leave)
        self.background = self.canvas.create_image(200, 75, image=self.background_img)

        if self.root.employee_role == "Admin":
            self.delete_btn = Button(self, image=self.delete_img, borderwidth=0, background="#771859", relief="flat",
                                     activebackground="#771859", command=self.delete_project_command)
            self.delete_btn.place(x=332, y=15, width=51, height=51)
            self.delete_btn.bind("<Enter>", self.delete_btn_on_enter)
            self.delete_btn.bind("<Leave>", self.delete_btn_on_leave)

            self.edit_btn = Button(self, image=self.edit_img, borderwidth=0, background="#771859", relief="flat",
                                   activebackground="#771859", command=self.edit_project_command)
            self.edit_btn.place(x=332, y=85, width=51, height=51)
            self.edit_btn.bind("<Enter>", self.edit_btn_on_enter)
            self.edit_btn.bind("<Leave>", self.edit_btn_on_leave)

        self.prj_name = Label(self, text=f"Project name: {self.prj_data.get('name'):.20s}",
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.prj_name.place(x=65, y=15)
        self.prj_name.bind("<Enter>", self.prj_btn_on_enter)
        self.prj_name.bind("<Leave>", self.prj_btn_on_leave)
        self.client = Label(self, text=f"Client: {self.prj_data.get('client')}", font=("Helvetica", 13, "bold"),
                            fg="#FFFFFF", bg="#771859")
        self.client.place(x=65, y=50)
        self.client.bind("<Enter>", self.prj_btn_on_enter)
        self.client.bind("<Leave>", self.prj_btn_on_leave)
        self.time_estimation = Label(self, text=f"Time estimation: {self.prj_data.get('time_estimation')}",
                                     font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.time_estimation.place(x=65, y=85)
        self.time_estimation.bind("<Enter>", self.prj_btn_on_enter)
        self.time_estimation.bind("<Leave>", self.prj_btn_on_leave)
        self.due_date = Label(self, text=f"Due date: {self.prj_data.get('due_date'):.12s}",
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.due_date.place(x=65, y=84)
        self.due_date.bind("<Enter>", self.prj_btn_on_enter)
        self.due_date.bind("<Leave>", self.prj_btn_on_leave)
        self.is_finished = Label(self, text=f"Project status: {self.prj_data.get('is_finished'):.20s}",
                                 font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.is_finished.place(x=65, y=117)
        self.is_finished.bind("<Enter>", self.prj_btn_on_enter)
        self.is_finished.bind("<Leave>", self.prj_btn_on_leave)

    def prj_btn_on_enter(self, e):
        self.prj_btn["image"] = self.background_hover_img
        self.canvas.itemconfig(self.background, image=self.background_hover_img)
        if self.root.employee_role == "Admin":
            self.delete_btn.configure(background="#D945AA", activebackground="#D945AA")
            self.edit_btn.configure(background="#D945AA", activebackground="#D945AA")
        self.prj_name["bg"] = "#D945AA"
        self.client["bg"] = "#D945AA"
        self.time_estimation["bg"] = "#D945AA"
        self.due_date["bg"] = "#D945AA"
        self.is_finished["bg"] = "#D945AA"

    def prj_btn_on_leave(self, e):
        self.prj_btn["image"] = self.background_img
        self.canvas.itemconfig(self.background, image=self.background_img)
        if self.root.employee_role == "Admin":
            self.delete_btn.configure(background="#771859", activebackground="#771859")
            self.edit_btn.configure(background="#771859", activebackground="#771859")
        self.prj_name["bg"] = "#771859"
        self.client["bg"] = "#771859"
        self.time_estimation["bg"] = "#771859"
        self.due_date["bg"] = "#771859"
        self.is_finished["bg"] = "#771859"

    def delete_btn_on_enter(self, e):
        self.delete_btn.configure(background="#D945AA", activebackground="#D945AA")
        self.edit_btn.configure(background="#D945AA", activebackground="#D945AA")
        self.prj_btn["image"] = self.background_hover_img
        self.canvas.itemconfig(self.background, image=self.background_hover_img)
        self.prj_name["bg"] = "#D945AA"
        self.client["bg"] = "#D945AA"
        self.time_estimation["bg"] = "#D945AA"
        self.due_date["bg"] = "#D945AA"
        self.is_finished["bg"] = "#D945AA"

    def delete_btn_on_leave(self, e):
        self.prj_btn["image"] = self.background_hover_img
        self.delete_btn["image"] = self.delete_img

    def edit_btn_on_enter(self, e):
        self.edit_btn.configure(background="#D945AA", activebackground="#D945AA")
        self.delete_btn.configure(background="#D945AA", activebackground="#D945AA")
        self.prj_btn["image"] = self.background_hover_img
        self.canvas.itemconfig(self.background, image=self.background_hover_img)
        self.prj_name["bg"] = "#D945AA"
        self.client["bg"] = "#D945AA"
        self.time_estimation["bg"] = "#D945AA"
        self.due_date["bg"] = "#D945AA"
        self.is_finished["bg"] = "#D945AA"

    def edit_btn_on_leave(self, e):
        self.prj_btn["image"] = self.background_hover_img
        self.edit_btn["image"] = self.edit_img

    def on_click(self):
        print("Clicked")
