from tkinter import ttk, Canvas, PhotoImage, Button


class ProjectView(ttk.Frame):
    def __init__(self, root, prj_data, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_data = prj_data
        print(self.prj_data)

        self.canvas = Canvas(self, bg="#f9f4f5", height=150, width=400, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.delete_img = PhotoImage(file=f"view/static/project/img0.png")
        self.delete_img_hover = PhotoImage(file=f"view/static/project/img1.png")
        self.background_img = PhotoImage(file=f"view/static/project/background.png")

        self.prj_img_btn = Button(self, image=self.background_img, borderwidth=0, highlightthickness=0,
                                  background="#e5e4e4", activebackground="#e5e4e4", relief="flat", command=self.on_click)
        self.prj_img_btn.place(x=18, y=0, width=367, height=150)
        if self.root.employee_role == "Admin":
            self.delete_btn = Button(self, image=self.delete_img, borderwidth=0, background="#C4C4C4", relief="flat",
                                     activebackground="#C4C4C4", command=self.on_click)
            self.delete_btn.place(x=341, y=5, width=51, height=51)
            self.delete_btn.bind("<Enter>", self.delete_btn_on_enter)
            self.delete_btn.bind("<Leave>", self.delete_btn_on_leave)

        self.background = self.canvas.create_image(200, 75, image=self.background_img)

    def delete_btn_on_enter(self, e):
        self.delete_btn["image"] = self.delete_img_hover

    def delete_btn_on_leave(self, e):
        self.delete_btn["image"] = self.delete_img

    def on_click(self):
        print("Clicked")
