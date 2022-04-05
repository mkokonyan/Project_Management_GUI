from controller.base_controller import BaseController


class ProjectController(BaseController):

    def get_all_entities(self):
        return self._service.get_all_projects()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_projects()

    def save_entities(self):
        return self._service.save_all_projects()
