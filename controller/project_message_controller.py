from controller.base_controller import BaseController


class ProjectMessageController(BaseController):
    def go_to_messages(self):
        self.reload_all_entities()
        self.view.children['!allprojectsview'].destroy()

    def get_all_entities(self):
        return self._service.get_all_messages()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_messages()

    def save_entities(self):
        return self._service.save_all_messages()
