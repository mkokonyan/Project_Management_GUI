from tkinter import Canvas, PhotoImage, Button, Entry, ttk, StringVar

from view.command.project.go_main_menu_command import GoMainMenuCommand


class CreateProjectView(ttk.Frame):

    def __init__(self, root, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.root.prj_controller.view = self
        self.project_data = {}

        self.go_main_menu_command = GoMainMenuCommand(self.root.prj_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/create_project/entry_img.png")
        self.create_project_img0 = PhotoImage(file=f"view/static/create_project/img0.png")
        self.create_project_hover_img1 = PhotoImage(file=f"view/static/create_project/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/create_project/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/create_project/img3.png")
        self.due_date_img4 = PhotoImage(file=f"view/static/create_project/img4.png")
        self.background_img = PhotoImage(file=f"view/static/create_project/background.png")

        self.project_name_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.project_name_entry = Entry(self, **entry_options)
        self.project_name_entry.place(x=583, y=262, width=298, height=32)

        self.client_entry_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.client_entry = Entry(self, **entry_options)
        self.client_entry.place(x=583, y=364, width=298, height=32)

        self.time_estimation_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.time_estimation = Entry(self, **entry_options)
        self.time_estimation.place(x=583, y=466, width=298, height=32)

        self.due_date_val = StringVar(self, value="Default val")
        self.due_date_button = Button(self, image=self.due_date_img4, borderwidth=0, highlightthickness=0,
                                      command=self.btn_clicked, relief="flat", activebackground="#f9f4f5", textvariable=self.due_date_val)

        self.due_date_button.place(x=577, y=565, width=304, height=32)

        self.create_project_btn = Button(self, image=self.create_project_img0, borderwidth=0, highlightthickness=0,
                                         command=self.get_project_data, relief="flat", activebackground="#f9f4f5")
        self.create_project_btn.place(x=592, y=905, width=250, height=70)
        self.create_project_btn.bind("<Enter>", self.register_btn_on_enter)
        self.create_project_btn.bind("<Leave>", self.register_btn_on_leave)

        self.go_back_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                  command=self.go_main_menu_command, relief="flat", bg="#f9f4f5",
                                  activebackground="#f9f4f5")
        self.go_back_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

    def get_project_data(self):
        self.project_data.update(
            {
                "name": self.project_name_entry.get(),
                "client": self.client_entry.get(),
                "time_estimation": self.time_estimation.get(),
                "due_date": self.due_date_val.get(),
            }
        )
        # print(self.project_data)
        # RegisterCommand(self.root.prj_controller, self.project_data)()

    def register_btn_on_enter(self, e):
        self.create_project_btn["image"] = self.create_project_hover_img1

    def register_btn_on_leave(self, e):
        self.create_project_btn["image"] = self.create_project_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2

    def btn_clicked(self):
        print("Button Clicked")