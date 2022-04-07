from tkinter import Button, ttk, Canvas

from view.project_view import ProjectView


class AllProjectsView(ttk.Frame):
    def __init__(self, root, prj_controller, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_controller = prj_controller
        self.prj_controller.view = self
        self.projects = self.prj_controller.get_all_entities()

        self.canvas = Canvas(self, bg="#f9f4f5", height=760, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        x = 260
        y = 105
        for i in range(min(12,len(self.projects))):
            if x == 1640:
                x = 260
                y += 182

            self.prj_info = self.prj_controller.get_project_details(self.projects[i])
            self.prj = ProjectView(self, self.prj_info)
            self.canvas.create_window(x, y, width=400, height=150, window=self.prj)
            x += 460

    #     self.show_create_account_command = ShowCreateAccountCommand(self.root.emp_controller)
    #
    #     self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
    #     self.canvas.pack()
    #
    #     self.entry_img = PhotoImage(file=f"view/static/welcome/entry_img.png")
    #     self.login_img0 = PhotoImage(file=f"view/static/welcome/img0.png")
    #     self.login_hover_img1 = PhotoImage(file=f"view/static/welcome/img1.png")
    #     self.create_img2 = PhotoImage(file=f"view/static/welcome/img2.png")
    #     self.create_hover_img3 = PhotoImage(file=f"view/static/welcome/img3.png")
    #     self.background_img = PhotoImage(file=f"view/static/welcome/background.png")
    #
    #     self.username_entry_bg = self.canvas.create_image(1188, 480, image=self.entry_img)
    #     self.username_entry = Entry(self, **entry_options)
    #     self.username_entry.place(x=1039, y=463, width=298, height=32)
    #
    #     self.password_entry_bg = self.canvas.create_image(1188, 610, image=self.entry_img)
    #     self.password_entry = Entry(self, **entry_options, show="\u2022")
    #     self.password_entry.place(x=1039, y=593, width=298, height=32)
    #
    #     self.login_btn = Button(self, image=self.login_img0, borderwidth=0, highlightthickness=0, background="#E0E0E0",
    #                             activebackground="#e0e0e0", relief="flat", command=self.get_login_data)
    #     self.login_btn.place(x=1049, y=680, width=250, height=81)
    #     self.login_btn.bind("<Enter>", self.login_btn_on_enter)
    #     self.login_btn.bind("<Leave>", self.login_btn_on_leave)
    #
    #     self.create_btn = Button(self, image=self.create_img2, borderwidth=0, background="#F9F4F5", relief="flat",
    #                              command=self.show_create_account_command)
    #     self.create_btn.place(x=1231, y=903, width=57, height=22)
    #     self.create_btn.bind("<Enter>", self.create_btn_on_enter)
    #     self.create_btn.bind("<Leave>", self.create_btn_on_leave)
    #
    #     self.background = self.canvas.create_image(263, 768, image=self.background_img)
    #
    # def get_login_data(self):
    #     self.login_data.update(
    #         {
    #             "username": self.username_entry.get(),
    #             "password": self.password_entry.get(),
    #
    #         }
    #     )
    #     LoginCommand(self.root.emp_controller, self.login_data)()
    #
    # def login_btn_on_enter(self, e):
    #     self.login_btn["image"] = self.login_hover_img1
    #
    # def login_btn_on_leave(self, e):
    #     self.login_btn["image"] = self.login_img0
    #
    # def create_btn_on_enter(self, e):
    #     self.create_btn["image"] = self.create_hover_img3
    #     self.create_btn["cursor"] = "hand2"
    #     self.create_btn.place(
    #         x=1231, y=901.2,
    #         width=57,
    #         height=22)
    #
    # def create_btn_on_leave(self, e):
    #     self.create_btn["image"] = self.create_img2
