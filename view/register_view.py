from tkinter import Canvas, PhotoImage, Button, Entry, ttk


class RegisterView(ttk.Frame):

    def __init__(self, root, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#e0e0e0",
                         "font": ("Helvetica", 14)
                         }

        super().__init__(root, *args, **kwargs)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.img0 = PhotoImage(file=f"view/static/register/img0.png")
        self.img1 = PhotoImage(file=f"view/static/register/img1.png")
        self.img2 = PhotoImage(file=f"view/static/register/img2.png")
        self.img3 = PhotoImage(file=f"view/static/register/img3.png")

        self.b0 = Button(self, image=self.img0, borderwidth=0, highlightthickness=0, command=self.btn_clicked,
                         relief="flat", activebackground="#f9f4f5")
        self.b0.place(x=592, y=905, width=250, height=70)

        self.b1 = Button(self, image=self.img2, borderwidth=0, highlightthickness=0, command=self.btn_clicked,
                         relief="flat", bg="#f9f4f5", activebackground="#f9f4f5")
        self.b1.place(x=1157, y=905, width=265, height=70)

        self.entry_img = PhotoImage(file=f"view/static/register/img_textBox.png")
        self.entry5_bg = self.canvas.create_image(732, 304, image=self.entry_img)
        self.entry5 = Entry(self, **entry_options)
        self.entry5.place(x=583, y=262, width=298, height=32)

        self.entry4_bg = self.canvas.create_image(732, 406, image=self.entry_img)
        self.entry4 = Entry(self, **entry_options)
        self.entry4.place(x=583, y=364, width=298, height=32)

        self.entry3_bg = self.canvas.create_image(732, 508, image=self.entry_img)
        self.entry3 = Entry(self, **entry_options)
        self.entry3.place(x=583, y=466, width=298, height=32)

        self.entry2_bg = self.canvas.create_image(732, 610, image=self.entry_img)
        self.entry2 = Entry(self, **entry_options)
        self.entry2.place(x=583, y=568, width=298, height=32)

        self.entry1_bg = self.canvas.create_image(732, 712, image=self.entry_img)
        self.entry1 = Entry(self, **entry_options)
        self.entry1.place(x=583, y=670, width=298, height=32)

        self.entry0_bg = self.canvas.create_image(732, 814, image=self.entry_img)
        self.entry0 = Entry(self, **entry_options)
        self.entry0.place(x=583, y=772, width=298, height=32)

        self.background_img = PhotoImage(file=f"view/static/register/background.png")
        self.background = self.canvas.create_image(790, 477, image=self.background_img)

        self.b0.bind("<Enter>", self.register_btn_on_enter)
        self.b0.bind("<Leave>", self.register_btn_on_leave)
        self.b1.bind("<Enter>", self.go_back_btn_on_enter)
        self.b1.bind("<Leave>", self.go_back_btn_on_leave)

        self.pack()

    def btn_clicked(self):
        print("Button Clicked")

    def register_btn_on_enter(self, e):
        self.b0["image"] = self.img1

    def register_btn_on_leave(self, e):
        self.b0["image"] = self.img0

    def go_back_btn_on_enter(self, e):
        self.b1["image"] = self.img3

    def go_back_btn_on_leave(self, e):
        self.b1["image"] = self.img2
