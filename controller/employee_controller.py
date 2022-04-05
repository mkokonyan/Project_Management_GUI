from controller.base_controller import BaseController


class EmployeeController(BaseController):

    def get_all_entities(self):
        return self._service.get_all_employees()

    def reload_all_entities(self) -> None:
        return self._service.reload_all_employees()

    def save_entities(self):
        return self._service.save_all_employees()
