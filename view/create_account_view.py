from tkinter import Canvas, PhotoImage, Button, Entry, ttk

from view.command.employee.go_back_command import GoBackCommand
from view.command.employee.register_command import RegisterCommand


class CreateAccountView(ttk.Frame):

    def __init__(self, root, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.root.emp_controller.view = self
        self.registration_data = {}

        self.go_back_command = GoBackCommand(self.root.emp_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/register/entry_img.png")
        self.register_img0 = PhotoImage(file=f"view/static/register/img0.png")
        self.register_hover_img1 = PhotoImage(file=f"view/static/register/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/register/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/register/img3.png")
        self.background_img = PhotoImage(file=f"view/static/register/background.png")

        self.username_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.username_entry = Entry(self, **entry_options)
        self.username_entry.focus()
        self.username_entry.place(x=583, y=262, width=298, height=32)

        self.password_entry_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.password_entry = Entry(self, **entry_options, show="\u2022")
        self.password_entry.place(x=583, y=364, width=298, height=32)

        self.confirm_password_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.confirm_password = Entry(self, **entry_options, show="\u2022")
        self.confirm_password.place(x=583, y=466, width=298, height=32)

        self.email_entry_bg = self.canvas.create_image(732, 610, image=self.entry_img)
        self.email_entry = Entry(self, **entry_options)
        self.email_entry.place(x=583, y=568, width=298, height=32)

        self.first_name_entry_bg = self.canvas.create_image(732, 712, image=self.entry_img)
        self.first_name_entry = Entry(self, **entry_options)
        self.first_name_entry.place(x=583, y=670, width=298, height=32)

        self.last_name_entry_bg = self.canvas.create_image(732, 814, image=self.entry_img)
        self.last_name_entry = Entry(self, **entry_options)
        self.last_name_entry.place(x=583, y=772, width=298, height=32)

        self.register_btn = Button(self, image=self.register_img0, borderwidth=0, highlightthickness=0,
                                   command=self.get_register_data, relief="flat", activebackground="#f9f4f5")
        self.register_btn.place(x=592, y=905, width=250, height=70)
        self.register_btn.bind("<Enter>", self.register_btn_on_enter)
        self.register_btn.bind("<Leave>", self.register_btn_on_leave)

        self.go_back_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                  command=self.go_back_command, relief="flat", bg="#f9f4f5", activebackground="#f9f4f5")
        self.go_back_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

    def get_register_data(self):
        self.registration_data.update(
            {
                "username": self.username_entry.get(),
                "password": self.password_entry.get(),
                "confirm_password": self.confirm_password.get(),
                "email": self.email_entry.get(),
                "first_name": self.first_name_entry.get(),
                "last_name": self.last_name_entry.get(),
            }
        )
        RegisterCommand(self.root.emp_controller, self.registration_data)()

    def register_btn_on_enter(self, e):
        self.register_btn["image"] = self.register_hover_img1

    def register_btn_on_leave(self, e):
        self.register_btn["image"] = self.register_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2
