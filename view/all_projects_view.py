from tkinter import Button, ttk, Canvas, PhotoImage

from view.command.project.show_create_project_command import ShowCreateProjectCommand
from view.project_view import ProjectView


class AllProjectsView(ttk.Frame):
    def __init__(self, root, prj_controller, employee_role, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_controller = prj_controller
        self.employee_role = employee_role
        self.prj_controller.view = self.root
        self.projects = self.prj_controller.get_all_entities()

        self.show_create_project_command = ShowCreateProjectCommand(self.prj_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.add_project_img0 = PhotoImage(file=f"view/static/all_projects/img0.png")
        self.add_project_hover_img1 = PhotoImage(file=f"view/static/all_projects/img1.png")
        self.background_img = PhotoImage(file=f"view/static/all_projects/background.png")

        if employee_role == "Admin":
            self.add_project_btn = Button(self, image=self.add_project_img0, borderwidth=0, background="#F9F4F5",
                                          relief="flat", activebackground="#F9F4F5",
                                          command=self.show_create_project_command)
            self.add_project_btn.place(x=1300, y=820, width=87, height=87)
            self.add_project_btn.bind("<Enter>", self.add_project_btn_on_enter)
            self.add_project_btn.bind("<Leave>", self.add_project_btn_on_leave)

        self.background = self.canvas.create_image(774, 1235, image=self.background_img)

        x = 260
        y = 105
        for i in range(min(12, len(self.projects))):
            if x == 1640:
                x = 260
                y += 182
            self.prj_info = self.prj_controller.get_project_details(self.projects[i])
            self.prj = ProjectView(self, self.prj_info)
            self.canvas.create_window(x, y, width=400, height=150, window=self.prj)
            x += 460

    def add_project_btn_on_enter(self, e):
        self.add_project_btn["image"] = self.add_project_hover_img1

    def add_project_btn_on_leave(self, e):
        self.add_project_btn["image"] = self.add_project_img0
