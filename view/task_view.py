from tkinter import Button, Frame


class TaskView(Frame):
    def __init__(self, root, tsk_controller, tsk, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.tsk_controller = tsk_controller
        self.tsk = tsk

        self.tsk_btn = Button(self, borderwidth=0, highlightthickness=0, background="#771859",
                              activebackground="#D945AA", relief="flat", text=self.tsk.name,
                              font=("Helvetica", 13, "bold"), fg="#FFFFFF", bg="#771859",
                              command=self.btn_clicked)
        self.tsk_btn.place(x=0, y=0, width=260, height=45)

    def btn_clicked(self):
        print("Button Clicked")
