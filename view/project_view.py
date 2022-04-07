from tkinter import ttk, Canvas, PhotoImage, Button, Label


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
                                  background="#e5e4e4", activebackground="#e5e4e4", relief="flat",
                                  command=self.on_click)
        self.prj_img_btn.place(x=18, y=0, width=367, height=150)
        if self.root.employee_role == "Admin":
            self.delete_btn = Button(self, image=self.delete_img, borderwidth=0, background="#771859", relief="flat",
                                     activebackground="#771859", command=self.on_click)
            self.delete_btn.place(x=341, y=5, width=51, height=51)
            self.delete_btn.bind("<Enter>", self.delete_btn_on_enter)
            self.delete_btn.bind("<Leave>", self.delete_btn_on_leave)
        self.background = self.canvas.create_image(200, 75, image=self.background_img)

        self.prj_name = Label(self, text=f"Project name: {self.prj_data.get('name'):.20s}",
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.prj_name.place(x=65, y=15)
        self.client = Label(self, text=f"Client: {self.prj_data.get('client')}", font=("Helvetica", 13, "bold"),
                            fg="#FFFFFF", bg="#771859")
        self.client.place(x=65, y=50)
        self.time_estimation = Label(self, text=f"Time estimation: {self.prj_data.get('time_estimation')}",
                                     font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.time_estimation.place(x=65, y=85)
        self.due_date = Label(self, text=f"Due date: {self.prj_data.get('due_date'):.12s}",
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.due_date.place(x=65, y=84)
        self.is_finished = Label(self, text=f"Project status: {self.prj_data.get('is_finished'):.20s}",
                                 font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859")
        self.is_finished.place(x=65, y=117)

    def delete_btn_on_enter(self, e):
        self.delete_btn["image"] = self.delete_img_hover

    def delete_btn_on_leave(self, e):
        self.delete_btn["image"] = self.delete_img

    def on_click(self):
        print("Clicked")
