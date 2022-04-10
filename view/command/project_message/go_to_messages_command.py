class GoToMessagesCommand:
    def __init__(self, project_message_controller):
        self.project_message_controller = project_message_controller

    def __call__(self):
        self.project_message_controller.go_to_messages()
