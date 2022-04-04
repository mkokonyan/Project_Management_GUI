from dao.employee_repository import EmployeeRepository
from dao.project_message_repository import ProjectMessageRepository
from dao.project_repository import ProjectRepository
from dao.task_repository import TaskRepository
from entity.employee import Employee, Admin
from entity.project import Project
from entity.project_message import ProjectMessage
from entity.task import Task
from exceptions.entity_not_found_exception import EntityNotFoundException
from exceptions.username_not_found_exception import UsernameNotFoundException
from services.login_service import LoginService
from services.project_service import ProjectService
from services.task_service import TaskService

if __name__ == '__main__':
    # # Employee CRUD operations:
    # e_repo = EmployeeRepository()
    # # Create entity instances:
    # a = Admin("mkk", "12345qwe", "Martin", "Kokonyan", "mkk@const.com")
    # print(a.username)
    # print(a.password)
    # print(a.first_name)
    # print(a.last_name)
    # print(a.email)
    # print(a.role)
    #
    # e1 = Employee("idm", "12345qwe", "Ivan", "Dimitrov", "idm@const.com")
    # e2 = Employee("spt", "12345qwe", "Simona", "Petrova", "spt@const.com")
    # e3 = Employee("giv", "12345qwe", "Georgi", "Ivanov", "giv@const.com")
    #
    # # Create
    # e_repo.create(a)
    # e_repo.create(e1)
    # e_repo.create(e2)
    # e_repo.create(e3)
    #
    # # Read
    # [print(e.get_info()) for e in e_repo.find_all()]
    #
    # e_repo.find_by_id("mkk")
    # try:
    #     e_repo.find_by_id("nonexistuser")
    # except UsernameNotFoundException:
    #     print("User do not exist!")
    # print(e_repo.find_all())
    #
    # # Update
    # e_to_update = Employee("giv", "12345qwe", "Georgi", "Ivanov", "updated@mail.com")
    # e_repo.update(e_to_update)
    # print(e_repo.find_by_id("giv").email)
    #
    # try:
    #     username_change = Employee("usernametochange", "12345qwe", "Georgi", "Ivanov", "updated@mail.com")
    #     e_repo.update(username_change)
    # except ValueError:
    #     print("You can't change your username")
    #     print()
    #
    #     # Delete
    # e_repo.delete_by_id("giv")
    #
    # [print(e.get_info()) for e in e_repo.find_all()]
    #
    # # Project CRUD operations:
    # prj_repo = ProjectRepository()
    # # Create entity instances:
    # prj1 = Project(None, "Parking", "InjStroy", 200, "2022-05-24")
    # print(prj1.name)
    # print(prj1.client)
    # print(prj1.time_estimation)
    # print(prj1.due_date)
    # print(prj1.employees)
    # print(prj1.tasks)
    # print(prj1.is_finished)
    # prj2 = Project(None, "House", "IvanovStroy", 400, "2022-04-03")
    # prj3 = Project(None, "Bridge", "Stoyanov", 500, "2023-01-05")
    #
    # # Create
    # prj_repo.create(prj1)
    # prj_repo.create(prj2)
    # prj_repo.create(prj3)
    # # Read
    # [print(prj.get_info()) for prj in prj_repo.find_all()]
    #
    # searched_id = prj1.obj_id
    # print(prj_repo.find_by_id(searched_id))
    # try:
    #     print(prj_repo.find_by_id("invalidID"))
    # except EntityNotFoundException:
    #     print("Not found Entity")
    #
    # print(prj_repo.find_by_name("e"))
    # print(prj_repo.find_by_client("Stroy"))
    # print(prj_repo.find_by_due_date_approaching())
    # prj1.is_finished = True
    # print(prj_repo.find_by_finished_status())
    #
    # # Update
    # prj3.name = "Updated Bridge"
    # prj_repo.update(prj3)
    # print(prj3.name)
    #
    # # Delete
    # prj_repo.delete_by_id(prj3.obj_id)
    # [print(prj.get_info()) for prj in prj_repo.find_all()]
    #
    # # Task CRUD operations:
    # tsks_repo = TaskRepository()
    # # Create entity instances:
    # tsk1 = Task(None, "Lower Rebar", a.username, prj1.name, "Calculations and make drawing", 6)
    # print(tsk1.name)
    # print(tsk1.employee)
    # print(tsk1.description)
    # print(tsk1.time_estimation)
    # print(tsk1.is_finished)
    # tsk2 = Task(None, "Upper Rebar", a.username, prj1.name, "Calculations and make drawing", 12)
    # tsk3 = Task(None, "3D Model", e1.username, prj2.name, "Make model of building", 14)
    # # Create
    # tsks_repo.create(tsk1)
    # tsks_repo.create(tsk2)
    # tsks_repo.create(tsk3)
    # # Read
    # [print(tsk.get_info()) for tsk in tsks_repo.find_all()]
    # print(tsks_repo.find_by_name("Rebar"))
    # print(tsks_repo.find_by_description("drawing"))
    # tsk1.is_finished = True
    # print(tsks_repo.find_by_finished_status())
    #
    # # Update
    # tsk3.description = "Make model of building and calculations"
    # tsks_repo.update(tsk3)
    # print(tsk3.description)
    #
    # # Delete
    # tsks_repo.delete_by_id(tsk3.obj_id)
    # [print(tsk.get_info()) for tsk in tsks_repo.find_all()]
    #
    # # Project Messages CRUD operations:
    # prj_msg_repo = ProjectMessageRepository()
    # # Create entity instances:
    # msg1 = ProjectMessage(None, "You should check first drawing", e1.username)
    # msg2 = ProjectMessage(None, "You should make new drawing", e1.username)
    # print(msg1.message)
    # print(msg1.username)
    # print(msg1.sent_on)
    #
    # # Create
    # prj_msg_repo.create(msg1)
    # prj_msg_repo.create(msg2)
    #
    # # Read
    # [print(msg.get_info()) for msg in prj_msg_repo.find_all()]
    # print(prj_msg_repo.find_by_content("new"))
    # print(prj_msg_repo.find_all_username_messages("idm"))
    #
    # e_repo.save()
    # prj_repo.save()
    # tsks_repo.save()
    # prj_msg_repo.save()
    #
    # e_repo.load()
    # prj_repo.load()
    # tsks_repo.load()
    # prj_msg_repo.load()
    # [print(obj.get_info()) for obj in e_repo]
    # [print(obj.get_info()) for obj in prj_repo]
    # [print(obj.get_info()) for obj in tsks_repo]
    # [print(obj.get_info()) for obj in prj_msg_repo]

    emp_repo = EmployeeRepository()
    prj_repo = ProjectRepository()
    tsk_repo = TaskRepository()
    prj_msg_repo = ProjectMessageRepository()

    emp_repo.load()
    prj_repo.load()
    tsk_repo.load()

    e_service = LoginService(emp_repo)

    # e_service.register(username="mkk", password="12345qwe", confirm_password="12345qwe", first_name="Martin",
    #                    last_name="Kokonyan", email="mkk@const.com")
    # e_service.register(username="idm", password="12345qwe", confirm_password="12345qwe", first_name="Ivan",
    #                    last_name="Dimitrov", email="idm@const.com")
    # e_service.register(username="spt", password="12345qwe", confirm_password="12345qwe", first_name="Simona",
    #                    last_name="Petrova", email="spt@const.com")
    # e_service.register(username="giv", password="12345qwe", confirm_password="12345qwe", first_name="Georgi",
    #                    last_name="Ivanov", email="giv@const.com")
    # e_service.register(username="NewUser", password="12345678a", confirm_password="12345678a", first_name="New",
    #                    last_name="User", email="mkk@const.com")
    # e_service.register(username="AnotherUser", password="12345678a", confirm_password="12345678a", first_name="Another",
    #                    last_name="User", email="anuser@const.com")

    print(emp_repo.find_all())

    print(e_service.login("mkk", "12345qwe"))

    e_service.logout()
    print(e_service.logged_user)
    # print(e_service.register("NewUser", "12345678a", "12345678a", "New", "User", "mkk@const.com"))
    print(e_service.login("NewUser", "12345678a"))
    print(e_service.logged_user)

    print(e_service.edit_profile(username="NewUser", password="12345678a", confirm_password="12345678a",
                                 first_name="Real", last_name="Name", email="mkk@const.com"))

    print([obj.username for obj in e_service.employee_repository])

    prj_service = ProjectService(prj_repo, emp_repo, tsk_repo)

    # prj_service.add_new_project(name="Parking", client="InjStroy", time_estimation=200, due_date="2022-05-24")
    # prj_service.add_new_project(name="House", client="IvanovStroy", time_estimation=400, due_date="2022-04-08")
    # prj_service.add_new_project(name="Bridge", client="Stoyanov", time_estimation=500, due_date="2023-01-05")
    # prj_service.add_new_project(name="Skyscraper", client="SofiaStroy", time_estimation=21, due_date="2022-05-20")
    # prj_service.add_new_project(name="Warehouse-Varna", client="Techstroy", time_estimation=211, due_date="2023-05-20")

    # print(prj_service.set_current_project("Skyscraper"))
    # prj_service.edit_project(name="Skyscraper-Sofia", client="SofiaStroyInfo", time_estimation=750, due_date="2022-12-20")
    # prj_service.edit_project(name="SkyscraperSofia", client="SofiaStroy", time_estimation=750, due_date="2022-12-20")
    # prj_service.edit_project(name="SkyscraperLast", client="SofiaStroy", time_estimation=750, due_date="2023-12-20")

    print(prj_service.set_current_project("Warehouse"))
    # prj_service.edit_project(name="Warehouse", client="Sofia", time_estimation=750, due_date="2023-12-20")

    # prj_service.assign_employee("mkk")
    # prj_service.assign_employee("NewUser")
    # print(prj_service.set_current_project("Bridge"))
    # prj_service.assign_employee("NewUser")
    # prj_service.assign_employee("AnotherUser")
    # print(prj_service.set_current_project("SkyscraperLast"))
    # prj_service.unassign_employee("mkk")

    tsk_service = TaskService(tsk_repo, prj_repo, emp_repo)

    # tsk_service.add_new_task(name="Lower Rebar", employee="mkk", project="House",
    #                          description="Calculations and make drawing", time_estimation=6)
    #
    # tsk_service.add_new_task(name="Upper Rebar", employee="mkk", project="House",
    #                          description="Calculations and make drawing", time_estimation=12)
    #
    # tsk_service.add_new_task(name="3D Model", employee="NewUser", project="Parking",
    #                          description="Make model of building", time_estimation=14)
