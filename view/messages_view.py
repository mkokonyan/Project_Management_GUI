from tkinter import ttk, Canvas, PhotoImage, Entry, NSEW, Frame, Button, Label, Scrollbar, VERTICAL, NS, W, CENTER, EW, \
    LEFT, RIGHT, E

from view.command.project_message.delete_message_command import DeleteMessageCommand
from view.command.project_message.edit_message_command import EditMessageCommand
from view.command.project_message.send_message_command import SendMessageCommand


class MessagesView(ttk.Frame):
    def __init__(self, root, prj_msg_controller, *args, **kwargs):
        entry_options = {"bd": 0,
                         "bg": "#E0E0E0",
                         "font": ("Helvetica", 14)
                         }
        super().__init__(root, *args, **kwargs)

        self.rowconfigure(0, minsize=820)
        self.rowconfigure(1, minsize=150)
        self.columnconfigure(0, minsize=1420)

        self.root = root
        self.prj_msg_controller = prj_msg_controller
        self.emp_controller = self.root.emp_controller
        self.logged_user = self.emp_controller.get_logged_user()
        self.edit_message_id = None

        self.prj_msg_controller.view = self.root
        self.emp_controller.view = self.root

        self.messages = self.prj_msg_controller.get_all_entities_sorted_by_date()

        self.bg_background_img = PhotoImage(file=f"view/static/project_message/messages_background.png")
        self.send_img0 = PhotoImage(file=f"view/static/project_message/img0.png")
        self.send_hover_img1 = PhotoImage(file=f"view/static/project_message/img0.png")
        self.delete_img2 = PhotoImage(file=f"view/static/project_message/img2.png")
        self.edit_img3 = PhotoImage(file=f"view/static/project_message/img3.png")

        self.bg_canvas = Canvas(self,
                                bg="#f9f4f5",
                                height=820,
                                width=1420,
                                bd=0,
                                highlightthickness=0,
                                relief="ridge",
                                )
        self.bg_canvas.grid(row=0, column=0, sticky=NSEW)

        self.bg_background = self.bg_canvas.create_image(712, 422, image=self.bg_background_img)
        self.messages_canvas = Canvas(self.bg_canvas,
                                      bg="#E5E4E4",
                                      height=741,
                                      width=1320,
                                      bd=0,
                                      highlightthickness=0,
                                      relief="ridge",
                                      )
        self.messages_canvas.place(x=50, y=50)
        self.canvas_scrollbar = Scrollbar(self, orient=VERTICAL, command=self.messages_canvas.yview)
        self.canvas_scrollbar.grid(row=0, column=1, sticky=NS)
        self.messages_canvas.bind("<Configure>",
                                  lambda v: self.messages_canvas.configure(
                                      yscrollcommand=self.canvas_scrollbar.set,
                                      scrollregion=self.messages_canvas.bbox("all"),
                                  ))

        self.canvas_container = Frame(self.messages_canvas, bg="#E5E4E4")
        self.canvas_container.columnconfigure(0, minsize=1320)
        self.messages_canvas.create_window((0, 0), window=self.canvas_container, width=1320)

        for i in range(len(self.messages)):
            minsize_row = 120 + 20 * self.messages[i].message.count("\n")
            self.canvas_container.rowconfigure(i, minsize=minsize_row)
            self.message = Frame(self.canvas_container,
                                 bd=5,
                                 relief="flat",
                                 highlightbackground="grey",
                                 highlightthickness=1,
                                 background="#f9f4f5",
                                 )

            self.message.grid(column=0, row=i, sticky=EW)

            self.username_label = Label(self.message,
                                        font=("Helvetica", 14, "bold"),
                                        foreground="#771859",
                                        text=f"{self.messages[i].employee}",
                                        anchor="e",
                                        justify=LEFT,
                                        background="#f9f4f5",
                                        )
            self.username_label.grid(row=0, column=0, sticky=W)
            self.sent_on_label = Label(self.message,
                                       font=("Helvetica", 11),
                                       fg="grey",
                                       text=f"{self.messages[i].sent_on if not hasattr(self.messages[i], 'edited_on') else 'Edited ' + self.messages[i].edited_on}",
                                       anchor="e",
                                       justify=LEFT,
                                       background="#f9f4f5",
                                       )
            self.sent_on_label.grid(row=1, column=0, sticky=W)
            self.message_label = Label(self.message,
                                       font=("Helvetica", 13),
                                       text=f"{self.messages[i].message}",
                                       anchor="e",
                                       justify=LEFT,
                                       background="#f9f4f5",
                                       )
            self.message_label.grid(row=2, column=0, sticky=W)

            if self.logged_user.role == "Admin" or self.logged_user.username == self.messages[i].employee:
                self.delete_message_command = DeleteMessageCommand(self.prj_msg_controller, self.messages[i].obj_id)
                self.delete_btn = Button(self.message,
                                         image=self.delete_img2,
                                         borderwidth=0,
                                         highlightthickness=0,
                                         command=self.delete_message_command,
                                         relief="flat", bg="#FFF4FC",
                                         activebackground="#FFF4FC"
                                         )
                self.delete_btn.place(x=1270, y=5, width=30, height=30)

                self.edit_message_command = EditMessageCommand(self.messages[i].message, self.messages[i].obj_id, self.show_message_to_edit)
                self.edit_btn = Button(self.message,
                                       image=self.edit_img3,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       command=self.edit_message_command,
                                       relief="flat", bg="#FFF4FC",
                                       activebackground="#FFF4FC"
                                       )
                self.edit_btn.place(x=1240, y=5, width=30, height=30)

            if i % 2 == 0:
                self.message.config(background="#FFF4FC", highlightbackground="#771859", )
                self.username_label.config(background="#FFF4FC")
                self.sent_on_label.config(background="#FFF4FC")
                self.message_label.config(background="#FFF4FC")

        self.messages_canvas.update_idletasks()
        self.messages_canvas.yview_moveto('1.0')

        self.message_box = Frame(self, background="#f9f4f5")
        self.message_box.grid(row=1, column=0, sticky=NSEW)
        self.message_box_canvas = Canvas(self.message_box,
                                         bg="#f9f4f5",
                                         height=150,
                                         width=1175,
                                         bd=0,
                                         highlightthickness=0,
                                         relief="ridge",
                                         )
        self.message_box_canvas.place(x=20, y=14)

        self.message_box_background_img = PhotoImage(file=f"view/static/project_message/message_box_background.png")
        self.message_box_background = self.message_box_canvas.create_image(582,
                                                                           54,
                                                                           image=self.message_box_background_img,
                                                                           )

        self.message_entry = Entry(self.message_box, **entry_options, fg="grey")
        self.message_entry.insert(0, 'Type your message...')
        self.message_entry.bind('<FocusIn>', self.entry_on_click)
        self.message_entry.place(x=65, y=50, width=1050, height=32)

        self.send_message_command = SendMessageCommand(self.prj_msg_controller, self.message_entry.get(),
                                                       self.logged_user.username)

        self.send_btn = Button(self.message_box,
                               image=self.send_img0,
                               borderwidth=0,
                               highlightthickness=0,
                               command=self.get_message_data,
                               relief="flat",
                               bg="#f9f4f5",
                               activebackground="#f9f4f5",
                               )
        self.send_btn.place(x=1175, y=30, width=265, height=70)

        self.send_btn.bind("<Enter>", self.send_btn_on_enter)
        self.send_btn.bind("<Leave>", self.send_btn_on_leave)

    def send_btn_on_enter(self, e):
        self.send_btn["image"] = self.send_hover_img1

    def send_btn_on_leave(self, e):
        self.send_btn["image"] = self.send_img0

    def entry_on_click(self, e):
        if self.message_entry.get() == 'Type your message...':
            self.message_entry.delete(0, "end")
            self.message_entry.insert(0, '')
            self.message_entry.config(fg='black')

    def get_message_data(self):
        message = self.message_entry.get()
        if message == "Type your message...":
            message = ""
        if self.edit_message_id:
            SendMessageCommand(self.prj_msg_controller, message, self.logged_user.username, self.edit_message_id)()
        else:
            SendMessageCommand(self.prj_msg_controller, message, self.logged_user.username)()

    def show_message_to_edit(self, old_msg, msg_id):
        self.message_entry.delete(0, "end")
        self.message_entry.insert(0, old_msg)
        self.message_entry.config(fg='black')
        self.edit_message_id = msg_id
