from tkinter import Canvas, PhotoImage, Button, Entry, ttk


class WelcomeView(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        # self.configure(bg="#f9f4f5")
        self.canvas = Canvas(
            root,
            bg="#f9f4f5",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.img0 = PhotoImage(file=f"static/welcome_view/img0.png")
        self.img3 = PhotoImage(file=f"static/welcome_view/img3.png")
        self.b0 = Button(
            image=self.img0,
            borderwidth=0,
            background="#F9F4F5",
            command=self.btn_clicked,
            relief="flat")

        self.b0.place(
            x=1231, y=903,
            width=57,
            height=22)

        self.background_img = PhotoImage(file=f"static/welcome_view/background.png")
        self.background = self.canvas.create_image(
            263.5, 768.0,
            image=self.background_img)

        self.img1 = PhotoImage(file=f"static/welcome_view/img1.png")
        self.img2 = PhotoImage(file=f"static/welcome_view/img2.png")
        self.b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            background="#E0E0E0",
            activebackground="#e0e0e0",
            command=self.btn_clicked,
            relief="flat")

        self.b1.place(
            x=1049, y=680,
            width=250,
            height=81)

        self.entry0_img = PhotoImage(file=f"static/welcome_view/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            1188.0, 480.0,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#e0e0e0",
            font=("Helevetica neue", 16),
            highlightthickness=0)

        self.entry0.place(
            x=1039, y=463,
            width=298,
            height=32)

        self.entry1_img = PhotoImage(file=f"static/welcome_view/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            1188.0, 610.0,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            bg="#e0e0e0",
            font=("Helevetica neue", 16),
            highlightthickness=0)

        self.entry1.place(
            x=1039, y=593,
            width=298,
            height=32)

        self.b0.bind("<Enter>", self.create_btn_on_enter)
        self.b0.bind("<Leave>", self.create_btn_on_leave)
        self.b1.bind("<Enter>", self.login_btn_on_enter)
        self.b1.bind("<Leave>", self.login_btn_on_leave)

    def btn_clicked(self):
        print("Button Clicked")

    def login_btn_on_enter(self, e):
        self.b1["image"] = self.img2

    def login_btn_on_leave(self, e):
        self.b1["image"] = self.img1

    def create_btn_on_enter(self, e):
        self.b0["image"] = self.img3
        self.b0["cursor"] = "hand2"
        self.b0.place(
            x=1231, y=901.2,
            width=57,
            height=22)

    def create_btn_on_leave(self, e):
        self.b0["image"] = self.img0
