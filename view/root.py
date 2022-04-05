import os
from tkinter import Tk

from controller.employee_controller import EmployeeController
from controller.project_controller import ProjectController
from controller.project_message_controller import ProjectMessageController
from controller.task_controller import TaskController
from dao.employee_repository import EmployeeRepository
from dao.project_message_repository import ProjectMessageRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
from services.employee_service import EmployeeService
from services.project_message_service import ProjectMessageService
from services.project_service import ProjectService
from services.task_service import TaskService


class Root(Tk):
    ICON_PATH = os.path.join(os.path.dirname(__file__), "static/root/mkk_logo.ico")
    HEIGHT = 1440
    WIDTH = 1040

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title("MK Project Management 1.00")
        self.center_resize_window(self.HEIGHT, self.WIDTH)
        self.configure(bg="#ffffff")
        self.iconbitmap(self.ICON_PATH)

        self.emp_repo = EmployeeRepository()
        self.prj_msg_repo = ProjectMessageRepository()
        self.prj_repo = ProjectRepository()
        self.tsk_repo = TaskRepository()

        self.emp_service = EmployeeService(self.emp_repo)
        self.prj_service = ProjectService(self.prj_repo, self.emp_repo, self.tsk_repo)
        self.tsk_service = TaskService(self.tsk_repo, self.prj_repo, self.emp_repo)
        self.prj_msg_service = ProjectMessageService(self.prj_msg_repo, self.emp_repo)

        self.emp_controller = EmployeeController(self.emp_service)
        self.prj_controller = ProjectController(self.prj_service)
        self.tsk_controller = TaskController(self.tsk_service)
        self.prj_msg_controller = ProjectMessageController(self.prj_msg_service)

        self.emp_controller.reload_all_entities()
        self.prj_controller.reload_all_entities()
        self.tsk_controller.reload_all_entities()
        self.prj_msg_controller.reload_all_entities()

    def center_resize_window(self, width=1440, height=1024):
        left, top = self.calculate_position(width, height)
        self.geometry(f"{width}x{height}+{left}+{top}")

    def calculate_position(self, width=600, height=400):
        parent_width = self.winfo_screenwidth()
        parent_height = self.winfo_screenheight()
        left = (parent_width - width) // 2
        top = (parent_height - height) // 2
        return left, top
