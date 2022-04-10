from tkinter import ttk, Canvas, PhotoImage, Entry, NSEW, Frame, Button, StringVar, END


class MessagesView(ttk.Frame):
    def __init__(self, root, prj_msg_controller, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#E0E0E0",
                         "font": ("Helvetica", 14)
                         }
        super().__init__(root, *args, **kwargs)

        self.rowconfigure(0, minsize=820)
        self.rowconfigure(1, minsize=150)
        self.columnconfigure(0, minsize=1440)

        self.root = root
        self.prj_msg_controller = prj_msg_controller
        self.prj_msg_controller.view = self.root
        self.messages = self.prj_msg_controller.get_all_entities()

        self.chat_window = Frame(self, background="red")
        self.chat_window.grid(row=0, column=0, sticky=NSEW)
        self.btn = Button(self.chat_window, text="hello").grid()

        self.message_box = Frame(self, background="#f9f4f5")
        self.message_box.grid(row=1, column=0, sticky=NSEW)

        self.message_box_canvas = Canvas(self.message_box, bg="#f9f4f5", height=150, width=1175, bd=0, highlightthickness=0, relief="ridge")
        self.message_box_canvas.place(x=10, y=9)

        self.message_box_background_img = PhotoImage(file=f"view/static/project_message/background.png")
        self.message_box_background = self.message_box_canvas.create_image(582, 54, image=self.message_box_background_img)


        self.message_entry = Entry(self.message_box, **entry_options, fg="grey")
        self.message_entry.insert(0, 'Type your message...')
        self.message_entry.bind('<FocusIn>', self.entry_on_click)

        self.message_entry.place(x=35, y=45, width=1100, height=32)

        self.send_img2 = PhotoImage(file=f"view/static/project_message/img2.png")
        self.send_hover_img3 = PhotoImage(file=f"view/static/project_message/img3.png")
        self.send_btn = Button(self.message_box, image=self.send_img2, borderwidth=0, highlightthickness=0,
                                  command="pass", relief="flat", bg="#f9f4f5",
                                  activebackground="#f9f4f5")
        self.send_btn.place(x=1175, y=30, width=265, height=70)
        self.send_btn.bind("<Enter>", self.send_btn_on_enter)
        self.send_btn.bind("<Leave>", self.send_btn_on_leave)

    def send_btn_on_enter(self, e):
        self.send_btn["image"] = self.send_hover_img3

    def send_btn_on_leave(self, e):
        self.send_btn["image"] = self.send_img2

    def entry_on_click(self, e):
        if self.message_entry.get() == 'Type your message...':
            self.message_entry.delete(0, "end")
            self.message_entry.insert(0, '')
            self.message_entry.config(fg='black')

