from datetime import datetime
from tkinter import Canvas, PhotoImage, Button, Entry, ttk, StringVar, Toplevel

from tkcalendar import Calendar

from view.command.project.edit_project_command import EditProjectCommand
from view.command.project.go_main_menu_command import GoMainMenuCommand


class EditProjectView(ttk.Frame):

    def __init__(self, root, project_to_edit, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)
        self.root = root
        self.project_to_edit = project_to_edit
        self.root.prj_controller.view = self
        self.edited_data = {}

        self.go_main_menu_command = GoMainMenuCommand(self.root.prj_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/edit_project/entry_img.png")
        self.edit_project_img0 = PhotoImage(file=f"view/static/edit_project/img0.png")
        self.edit_project_hover_img1 = PhotoImage(file=f"view/static/edit_project/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/edit_project/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/edit_project/img3.png")
        self.background_img = PhotoImage(file=f"view/static/edit_project/background.png")

        self.project_name_entry_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.project_name_default_val = StringVar(root, value=self.project_to_edit.name)
        self.project_name_entry = Entry(self, **entry_options, textvariable=self.project_name_default_val)
        self.project_name_entry.place(x=583, y=262, width=298, height=32)

        self.client_entry_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.client_default_val = StringVar(root, value=self.project_to_edit.client)
        self.client_entry = Entry(self, **entry_options, textvariable=self.client_default_val)
        self.client_entry.place(x=583, y=364, width=298, height=32)

        self.time_estimation_entry_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.time_estimation_default_val = StringVar(root, value=self.project_to_edit.time_estimation)
        self.time_estimation = Entry(self, **entry_options, textvariable=self.time_estimation_default_val)
        self.time_estimation.place(x=583, y=466, width=298, height=32)

        self.due_date_button = Button(self, borderwidth=0, highlightthickness=0, background="#E0E0E0",
                                      command=lambda: self.show_calendar(self.due_date_default_val), relief="flat",
                                      activebackground="#E0E0E0")
        self.due_date_default_val = StringVar(root, value=self.project_to_edit.due_date)
        self.due_date_label = Entry(self, **entry_options, textvariable=self.due_date_default_val)
        self.due_date_button.place(x=577, y=568, width=304, height=32)
        self.due_date_label.place(x=577, y=568, width=100, height=32)

        self.create_project_btn = Button(self, image=self.edit_project_img0, borderwidth=0, highlightthickness=0,
                                         background="#f9f4f5", anchor="w", justify="left",
                                         command=self.get_edited_data, relief="flat", activebackground="#f9f4f5", )
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

    def get_edited_data(self):
        self.edited_data.update(
            {
                "name": self.project_name_entry.get(),
                "client": self.client_entry.get(),
                "time_estimation": self.time_estimation.get(),
                "due_date": self.due_date_default_val.get(),
            }
        )
        EditProjectCommand(self.root.prj_controller, self.project_to_edit.obj_id, self.edited_data)()

    def register_btn_on_enter(self, e):
        self.create_project_btn["image"] = self.edit_project_hover_img1

    def register_btn_on_leave(self, e):
        self.create_project_btn["image"] = self.edit_project_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2

    def show_calendar(self, date_val):
        def grad_date(view):
            date_val.set(cal.get_date())
            view.grab_release()
            view.destroy()

        cal_root = Toplevel(self, height=250, width=250)
        cal_root.grab_set()
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        cal_root.geometry("+%d+%d" % (x + 220, y + 400))

        cal = Calendar(cal_root, selectmode='day',
                       year=datetime.now().year, month=datetime.now().month,
                       day=datetime.now().day, date_pattern='yyyy-MM-dd')
        cal.pack()

        Button(cal_root, text="Get Date", command= lambda: grad_date(cal_root)).pack(pady=20)
