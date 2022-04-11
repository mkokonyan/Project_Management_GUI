from tkinter import messagebox

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

    def send_message(self, message, username, message_id=None):
        if message_id:
            result = self.service.edit_message(message_id, message)
        else:
            result = self.service.send_message(message, username)
        if isinstance(result, Exception):
            return messagebox.showerror("Error", str(result))
        self.go_to_messages()

    def delete_message(self, message_id):
        action_result = messagebox.askquestion("Warning", "Do you really want to delete message?")
        if action_result == "yes":
            self.service.delete_message(message_id)
            self.go_to_messages()

    def get_all_entities(self):
        return self._service.get_all_messages()

    def get_all_entities_sorted_by_date(self):
        return self._service.get_all_messages_sorted_by_date()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_messages()

    def save_entities(self):
        return self._service.save_all_messages()
