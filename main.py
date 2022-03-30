from dao.employee_repository import EmployeeRepository
from dao.project_message_repository import ProjectMessageRepository
from dao.task_repository import TaskRepository
from entity.project_message import ProjectMessage
from entity.task import Task
from helpers.id_generator_uuid import IdGeneratorUuid
from dao.project_repository import ProjectRepository
from entity.employee import Employee, Admin
from entity.project import Project
from exceptions.entity_not_found_exception import EntityNotFoundException
from exceptions.username_not_found_exception import UsernameNotFoundException

if __name__ == '__main__':

    # Employee CRUD operations:
    e_repo = EmployeeRepository()
        # Create entity instances:
    a = Admin("mkk", "12345qwe", "Martin", "Kokonyan", "mkk@const.com")
    print(a.username)
    print(a.password)
    print(a.first_name)
    print(a.last_name)
    print(a.email)
    print(a.role)

    e1 = Employee("idm", "12345qwe", "Ivan", "Dimitrov", "idm@const.com")
    e2 = Employee("spt", "12345qwe", "Simona", "Petrova", "spt@const.com")
    e3 = Employee("giv", "12345qwe", "Georgi", "Ivanov", "giv@const.com")

        # Create
    e_repo.create(a)
    e_repo.create(e1)
    e_repo.create(e2)
    e_repo.create(e3)

        # Read
    [print(e.get_info()) for e in e_repo.find_all()]

    e_repo.find_by_id("mkk")
    try:
        e_repo.find_by_id("nonexistuser")
    except UsernameNotFoundException:
        print("User do not exist!")
    print(e_repo.find_all())

        # Update
    e_to_update = Employee("giv", "12345qwe", "Georgi", "Ivanov", "updated@mail.com")
    e_repo.update(e_to_update)
    print(e_repo.find_by_id("giv").email)

    try:
        username_change = Employee("usernametochange", "12345qwe", "Georgi", "Ivanov", "updated@mail.com")
        e_repo.update(username_change)
    except ValueError:
        print("You can't change your username")
        [print(e.get_info()) for e in e_repo.find_all()]
        print()

        # Delete
    e_repo.delete_by_id("giv")

    [print(e.get_info()) for e in e_repo.find_all()]


    # Project CRUD operations:
    prj_repo = ProjectRepository(IdGeneratorUuid)
        # Create entity instances:
    prj1 = Project(None, "Parking", "InjStroy", 200, "2022-05-24")
    print(prj1.name)
    print(prj1.client)
    print(prj1.time_estimation)
    print(prj1.due_date)
    print(prj1.employees)
    print(prj1.tasks)
    print(prj1.is_finished)
    prj2 = Project(None, "House", "IvanovStroy", 400, "2022-04-03")
    prj3 = Project(None, "Bridge", "Stoyanov", 500, "2023-01-05")

        # Create
    prj_repo.create(prj1)
    prj_repo.create(prj2)
    prj_repo.create(prj3)
        # Read
    [print(prj.get_info()) for prj in prj_repo.find_all()]

    searched_id = prj1.obj_id
    print(prj_repo.find_by_id(searched_id))
    try:
        print(prj_repo.find_by_id("invalidID"))
    except EntityNotFoundException:
        print("Not found Entity")

    print(prj_repo.find_by_name("e"))
    print(prj_repo.find_by_client("Stroy"))
    print(prj_repo.find_by_due_date_approaching())
    prj1.is_finished = True
    print(prj_repo.find_by_finished_status())

        # Update
    prj3.name = "Updated Bridge"
    prj_repo.update(prj3)
    print(prj3.name)

        # Delete
    prj_repo.delete_by_id(prj3.obj_id)
    [print(prj.get_info()) for prj in prj_repo.find_all()]



    # Task CRUD operations:
    tsk_repo = TaskRepository(IdGeneratorUuid)
        # Create entity instances:
    tsk1 = Task(None, "Lower Rebar", a, "Calculations and make drawing", 6)
    print(tsk1.name)
    print(tsk1.employee)
    print(tsk1.description)
    print(tsk1.time_estimation)
    print(tsk1.is_finished)
    tsk2 = Task(None, "Upper Rebar", a, "Calculations and make drawing", 12)
    tsk3 = Task(None, "3D Model", e1, "Make model of building", 14)
        # Create
    tsk_repo.create(tsk1)
    tsk_repo.create(tsk2)
    tsk_repo.create(tsk3)
        # Read
    [print(tsk.get_info()) for tsk in tsk_repo.find_all()]
    print(tsk_repo.find_by_name("Rebar"))
    print(tsk_repo.find_by_description("drawing"))
    tsk1.is_finished = True
    print(tsk_repo.find_by_finished_status())

        # Update
    tsk3.description = "Make model of building and calculations"
    tsk_repo.update(tsk3)
    print(tsk3.description)

        # Delete
    tsk_repo.delete_by_id(tsk3.obj_id)
    [print(tsk.get_info()) for tsk in tsk_repo.find_all()]

    # Project Messages CRUD operations:
    msg_repo = ProjectMessageRepository(IdGeneratorUuid)
    # Create entity instances:
    msg1 = ProjectMessage(None, "You should check first drawing", a)
    msg2 = ProjectMessage(None, "You should make new drawing", a)
    print(msg1.message)
    print(msg1.employee)
    print(msg1.sent_on)

    # Create
    msg_repo.create(msg1)
    msg_repo.create(msg2)

    # Read
    [print(msg.get_info()) for msg in msg_repo.find_all()]
    print(msg_repo.find_by_name("You should"))
    print(msg_repo.find_all_username_messages("mkk"))
