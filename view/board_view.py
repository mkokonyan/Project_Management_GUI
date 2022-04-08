from tkinter import Canvas, PhotoImage, Button, ttk

from view.command.project.go_main_menu_command import GoMainMenuCommand


class BoardView(ttk.Frame):
    def __init__(self, root, prj_controller, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_controller = prj_controller
        self.root.prj_controller.view = self

        self.go_main_menu_command = GoMainMenuCommand(self.root.prj_controller)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.entry_img = PhotoImage(file=f"view/static/edit_project/entry_img.png")
        self.edit_project_img0 = PhotoImage(file=f"view/static/edit_project/img0.png")
        self.edit_project_hover_img1 = PhotoImage(file=f"view/static/edit_project/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/edit_project/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/edit_project/img3.png")
        self.background_img = PhotoImage(file=f"view/static/edit_project/background.png")

        self.go_back_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                  command=self.go_main_menu_command, relief="flat", bg="#f9f4f5",
                                  activebackground="#f9f4f5")
        self.go_back_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.background = self.canvas.create_image(790, 477, image=self.background_img)

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2
