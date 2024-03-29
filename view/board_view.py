from tkinter import Canvas, PhotoImage, Button, ttk, Frame, CENTER, Label

from view.command.project.go_main_menu_command import GoMainMenuCommand
from view.command.task.show_create_project_command import ShowCreateTaskCommand
from view.task_view import TaskView


class BoardView(ttk.Frame):
    BOARD_MAPPER = {
        0: "TO DO",
        1: "IN PROGRESS",
        2: "CHECKING",
        3: "DONE"
    }

    def __init__(self, root, prj_controller, current_project, employee_role, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.root = root
        self.prj_controller = prj_controller
        self.tsk_controller = self.root.tsk_controller
        self.current_project = current_project
        self.employee_role = employee_role
        self.prj_controller.view = self
        self.tsk_controller.view = self
        self.project_tasks = self.tsk_controller.get_project_tasks(self.current_project.obj_id)

        self.tsk_controller.reload_all_entities()

        self.go_main_menu_command = GoMainMenuCommand(self.prj_controller)
        self.show_create_task_command = ShowCreateTaskCommand(self.tsk_controller, self.current_project,
                                                              self.employee_role)

        self.canvas = Canvas(self, bg="#f9f4f5", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.create_task_img0 = PhotoImage(file=f"view/static/board/img0.png")
        self.create_task_hover_img1 = PhotoImage(file=f"view/static/board/img1.png")
        self.go_back_img2 = PhotoImage(file=f"view/static/board/img2.png")
        self.go_back_hover_img3 = PhotoImage(file=f"view/static/board/img3.png")
        self.background_img = PhotoImage(file=f"view/static/board/background.png")
        self.sections_background_img = PhotoImage(file=f"view/static/board/sections_background.png")

        self.create_task_btn = Button(self, image=self.create_task_img0, borderwidth=0, highlightthickness=0,
                                      command=self.show_create_task_command, relief="flat", bg="#f9f4f5",
                                      activebackground="#D945AA")
        self.create_task_btn.place(x=1275, y=1.2, width=165, height=53.8)
        self.create_task_btn.bind("<Enter>", self.add_task_btn_on_enter)
        self.create_task_btn.bind("<Leave>", self.add_task_btn_on_leave)
        self.go_back_btn = Button(self, image=self.go_back_img2, borderwidth=0, highlightthickness=0,
                                  command=self.go_main_menu_command, relief="flat", bg="#f9f4f5",
                                  activebackground="#f9f4f5")
        self.go_back_btn.place(x=1175, y=905, width=265, height=70)
        self.go_back_btn.bind("<Enter>", self.go_back_btn_on_enter)
        self.go_back_btn.bind("<Leave>", self.go_back_btn_on_leave)

        self.prj_title = Label(self, text=f"{self.current_project.name} Board",
                               font=("Helvetica", 21, "bold"), fg="#FFFFFF", bg="#5E214B")
        self.prj_title.place(x=75, y=7.5)

        self.background = self.canvas.create_image(720, 62.8, image=self.background_img)

        self.sections = Frame(self, height=920, width=1168, bg="#f9f4f5")
        self.sections_canvas = Canvas(self.sections, bg="#f9f4f5", height=920, width=1168, bd=0, highlightthickness=0,
                                      relief="ridge")
        self.sections_canvas.place(x=0, y=0)
        self.sections_background = self.sections_canvas.create_image(584, 440, image=self.sections_background_img)

        self.sections.place(x=16, y=123)
        for c_idx in range(0, 4):
            self.sections.columnconfigure(c_idx, minsize=292, weight=1)
        for r_idx in range(0, 9):
            self.sections.rowconfigure(r_idx, minsize=90, weight=1)

        for t in self.project_tasks:
            self.tsk = TaskView(self.sections, self.tsk_controller, t, highlightbackground="#771859",
                                highlightthickness=4, width=260, height=90)
            self.tsk.grid(row=t.board_coordinates[0], column=t.board_coordinates[1], sticky="nsew", padx=16, pady=5)
            self.tsk.bind("<Button-1>", self.drag_start)
            self.tsk.bind("<B1-Motion>", self.drag_motion)
            self.tsk.bind("<ButtonRelease>", self.on_release)

        self.rearrange_tasks()

    def rearrange_tasks(self):
        number_of_column_widgets = self.sections.grid_size()[0]
        for c in range(number_of_column_widgets):
            column_slaves = self.sections.grid_slaves(column=c)[::-1]
            for i in range(len(column_slaves)):
                current_task_id = column_slaves[i].tsk.obj_id
                current_task = self.tsk_controller.service.task_repository.find_by_id(current_task_id)
                column_slaves[i].grid(row=i)
                current_task.board_coordinates = [column_slaves[i].grid_info()["row"],
                                                  column_slaves[i].grid_info()["column"]]
                current_task.status = self.BOARD_MAPPER[column_slaves[i].grid_info()["column"]]



    def add_task_btn_on_enter(self, e):
        self.create_task_btn["image"] = self.create_task_hover_img1

    def add_task_btn_on_leave(self, e):
        self.create_task_btn["image"] = self.create_task_img0

    def go_back_btn_on_enter(self, e):
        self.go_back_btn["image"] = self.go_back_hover_img3

    def go_back_btn_on_leave(self, e):
        self.go_back_btn["image"] = self.go_back_img2

    def drag_start(self, event):
        widget = event.widget
        starting_column = widget.grid_info()["column"]
        widget.startX = event.x
        widget.startY = event.y
        widget.lift()

    def drag_motion(self, event):
        widget = event.widget
        x = event.x + event.widget.winfo_x()
        y = event.y + event.widget.winfo_y()
        widget.place(x=x, y=y, anchor=CENTER)

    def on_release(self, event):
        widget = event.widget

        widget_start_x = widget.winfo_x()
        widget_start_y = widget.winfo_y()

        widget_end_x = widget_start_x + widget.winfo_width()
        widget_end_y = widget_start_y + widget.winfo_height()

        widget_center_x = (widget_start_x + widget_end_x) / 2
        widget_center_y = (widget_start_y + widget_end_y) / 2

        new_column, new_row = self.sections.grid_location(widget_center_x, widget_center_y)
        if new_column > 3:
            new_column = 3
        elif new_column < 0:
            new_column = 0
        if new_row < 0:
            new_row = 0

        widget.grid(row=new_row, column=new_column)
        widget.tsk.board_coordinates = (new_row, new_column)

        self.rearrange_tasks()
        self.tsk_controller.save_entities()

