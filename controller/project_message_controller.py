from controller.base_controller import BaseController
from view.messages_view import MessagesView


class ProjectMessageController(BaseController):
    def go_to_messages(self):
        self.reload_all_entities()
        try:
            self.view.children['!allprojectsview'].destroy()
        except KeyError:
            pass
        self.msg_frame = MessagesView(self.view, self)
        self.msg_frame.place(x=0, y=55)

    def get_all_entities(self):
        return self._service.get_all_messages()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_messages()

    def save_entities(self):
        return self._service.save_all_messages()
