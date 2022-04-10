from tkinter import Canvas, PhotoImage, Button, ttk, LEFT, RIGHT, N

from view.all_projects_view import AllProjectsView
from view.command.employee.logout_command import LogoutCommand
from view.command.employee.show_user_details_command import ShowUserDetailsCommand
from view.command.project.go_main_menu_command import GoMainMenuCommand
from view.command.project_message.go_to_messages_command import GoToMessagesCommand


class MainView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root

        self.emp_controller = self.root.emp_controller
        self.prj_controller = self.root.prj_controller
        self.tsk_controller = self.root.tsk_controller
        self.prj_msg_controller = self.root.prj_msg_controller

        self.emp_controller.view = self
        self.prj_controller.view = self
        self.tsk_controller.view = self
        self.prj_msg_controller.view = self

        self.logout_command = LogoutCommand(self.emp_controller)
        self.user_details_command = ShowUserDetailsCommand(self.emp_controller)
        self.go_main_menu_command = GoMainMenuCommand(self.prj_controller)
        self.go_to_messages_command = GoToMessagesCommand(self.prj_msg_controller)


        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.prj_frame = AllProjectsView(self, self.prj_controller, self.emp_controller.get_role())
        self.prj_frame.place(x=0, y=55)

        self.projects_img0 = PhotoImage(file=f"view/static/navbar/img0.png")
        self.projects_hover_img1 = PhotoImage(file=f"view/static/navbar/img1.png")
        self.messages_img2 = PhotoImage(file=f"view/static/navbar/img2.png")
        self.messages_hover_img3 = PhotoImage(file=f"view/static/navbar/img3.png")
        self.user_details_img4 = PhotoImage(file=f"view/static/navbar/img4.png")
        self.user_details_hover_img5 = PhotoImage(file=f"view/static/navbar/img5.png")
        self.logout_img6 = PhotoImage(file=f"view/static/navbar/img6.png")
        self.logout_hover_img7 = PhotoImage(file=f"view/static/navbar/img7.png")
        self.background_img = PhotoImage(file=f"view/static/navbar/background.png")

        self.projects_btn = Button(self, image=self.projects_img0, borderwidth=0, highlightthickness=0,
                                   command=self.go_main_menu_command, relief="flat", activebackground="#5D204A")
        self.projects_btn.place(x=94, y=0, width=128, height=55)
        self.projects_btn.bind("<Enter>", self.projects_btn_on_enter)
        self.projects_btn.bind("<Leave>", self.projects_btn_on_leave)

        self.messages_btn = Button(self, image=self.messages_img2, borderwidth=0, highlightthickness=0,
                                   command=self.go_to_messages_command, relief="flat", activebackground="#5D204A")
        self.messages_btn.place(x=222, y=0, width=122, height=55)
        self.messages_btn.bind("<Enter>", self.messages_btn_on_enter)
        self.messages_btn.bind("<Leave>", self.messages_btn_on_leave)

        self.background = self.canvas.create_image(720, 24, image=self.background_img)

        self.user_details_btn = Button(self, image=self.user_details_img4, borderwidth=0, highlightthickness=0,
                                       command=self.user_details_command, relief="flat", activebackground="#5D204A",
                                       activeforeground='#FFFFFF',
                                       text=f"{'Welcome, ' + self.emp_controller.service.logged_user.first_name + ' (' + self.emp_controller.service.logged_user.role + ')':<30.30s}",
                                       font=("Helvetica", 13, "bold"), fg='#FFFFFF', compound="center")
        self.user_details_btn.place(x=967, y=0, width=353, height=55)
        self.user_details_btn.bind("<Enter>", self.user_details_btn_on_enter)
        self.user_details_btn.bind("<Leave>", self.user_details_btn_on_leave)

        self.logout_btn = Button(self, image=self.logout_img6, borderwidth=0, highlightthickness=0,
                                 command=self.logout_command, relief="flat", activebackground="#5D204A")
        self.logout_btn.place(x=1320, y=0, width=120, height=55)
        self.logout_btn.bind("<Enter>", self.logout_btn_on_enter)
        self.logout_btn.bind("<Leave>", self.logout_btn_on_leave)

    def projects_btn_on_enter(self, e):
        self.projects_btn["image"] = self.projects_hover_img1

    def projects_btn_on_leave(self, e):
        self.projects_btn["image"] = self.projects_img0

    def messages_btn_on_enter(self, e):
        self.messages_btn["image"] = self.messages_hover_img3

    def messages_btn_on_leave(self, e):
        self.messages_btn["image"] = self.messages_img2

    def user_details_btn_on_enter(self, e):
        self.user_details_btn["image"] = self.user_details_hover_img5

    def user_details_btn_on_leave(self, e):
        self.user_details_btn["image"] = self.user_details_img4

    def logout_btn_on_enter(self, e):
        self.logout_btn["image"] = self.logout_hover_img7

    def logout_btn_on_leave(self, e):
        self.logout_btn["image"] = self.logout_img6

