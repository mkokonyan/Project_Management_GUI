class SendMessageCommand:
    def __init__(self, project_message_controller, message, username, edit_message_id=None):
        self.project_message_controller = project_message_controller
        self.message = message
        self.username = username
        self.edit_message_id = edit_message_id

    def __call__(self):
        self.project_message_controller.send_message(self.message, self.username, self.edit_message_id)
