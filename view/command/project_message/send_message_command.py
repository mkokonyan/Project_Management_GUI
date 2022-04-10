class SendMessageCommand:
    def __init__(self, project_message_controller, message, username):
        self.project_message_controller = project_message_controller
        self.message = message
        self.username = username

    def __call__(self):
        self.project_message_controller.send_message(self.message, self.username)
