from controller.base_controller import BaseController


class TaskController(BaseController):

    def reload_all_tasks(self) -> None:
        return self.service.reload_all_tasks()

    def get_all_entities(self):
        return self._service.get_all_tasks()

    def reload_all_entities(self) -> None:
        return self._service.reload_all_tasks()

    def save_entities(self):
        return self._service.save_all_tasks()
