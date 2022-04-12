from tkinter import Canvas, PhotoImage, Button, Entry, ttk, StringVar

from view.command.employee.edit_profile_command import EditProfileCommand
from view.command.project.go_main_menu_command import GoMainMenuCommand


class UserDetailsView(ttk.Frame):

    def __init__(self, root, logged_user_details, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.logged_user_details = logged_user_details
        self.emp_controller = self.root.emp_controller
        self.prj_controller = self.root.prj_controller
        self.emp_controller.view = self
        self.prj_controller.view = self
        self.edited_data = {}

        self.go_main_menu_command = GoMainMenuCommand(self.prj_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/edit_profile/entry_img.png")
        self.edit_img0 = PhotoImage(file=f"view/static/edit_profile/img0.png")
        self.edit_hover_img1 = PhotoImage(file=f"view/static/edit_profile/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/edit_profile/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/edit_profile/img3.png")
        self.background_img = PhotoImage(file=f"view/static/edit_profile/background.png")

        self.username_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.username_default_val = StringVar(root, value=self.logged_user_details.get("username"))
        self.username_entry = Entry(self, **entry_options, state='disabled', disabledbackground="#E0E0E0",
                                    textvariable=self.username_default_val)
        self.username_entry.place(x=583, y=262, width=298, height=32)

        self.password_entry_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.password_entry = Entry(self, **entry_options, show="\u2022")
        self.password_entry.focus()
        self.password_entry.place(x=583, y=364, width=298, height=32)

        self.confirm_password_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.confirm_password = Entry(self, **entry_options, show="\u2022")
        self.confirm_password.place(x=583, y=466, width=298, height=32)

        self.email_entry_bg = self.canvas.create_image(732, 610, image=self.entry_img)
        self.email_default_val = StringVar(root, value=self.logged_user_details.get("email"))
        self.email_entry = Entry(self, **entry_options, textvariable=self.email_default_val)
        self.email_entry.place(x=583, y=568, width=298, height=32)

        self.first_name_entry_bg = self.canvas.create_image(732, 712, image=self.entry_img)
        self.first_name_default_val = StringVar(root, self.logged_user_details.get("first_name"))
        self.first_name_entry = Entry(self, **entry_options, textvariable=self.first_name_default_val)
        self.first_name_entry.place(x=583, y=670, width=298, height=32)

        self.last_name_entry_bg = self.canvas.create_image(732, 814, image=self.entry_img)
        self.last_name_default_val = StringVar(root, self.logged_user_details.get("last_name"))
        self.last_name_entry = Entry(self, **entry_options, textvariable=self.last_name_default_val)
        self.last_name_entry.place(x=583, y=772, width=298, height=32)

        self.edit_btn = Button(self, image=self.edit_img0, borderwidth=0, highlightthickness=0,
                               command=self.get_edited_data, relief="flat", activebackground="#f9f4f5")
        self.edit_btn.place(x=592, y=905, width=250, height=70)
        self.edit_btn.bind("<Enter>", self.edit_btn_on_enter)
        self.edit_btn.bind("<Leave>", self.edit_btn_on_leave)

        self.go_back_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                  command=self.go_main_menu_command, relief="flat", bg="#f9f4f5", activebackground="#f9f4f5")
        self.go_back_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

    def get_edited_data(self):
        self.edited_data.update(
            {
                "password": self.password_entry.get(),
                "confirm_password": self.confirm_password.get(),
                "email": self.email_entry.get(),
                "first_name": self.first_name_entry.get(),
                "last_name": self.last_name_entry.get(),
            }
        )
        EditProfileCommand(self.emp_controller, self.edited_data)()

    def edit_btn_on_enter(self, e):
        self.edit_btn["image"] = self.edit_hover_img1

    def edit_btn_on_leave(self, e):
        self.edit_btn["image"] = self.edit_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2
