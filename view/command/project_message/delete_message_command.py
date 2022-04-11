class DeleteMessageCommand:
    def __init__(self, project_message_controller, message_id):
        self.project_message_controller = project_message_controller
        self.message_id = message_id


    def __call__(self):
        print(self.message_id)
        self.project_message_controller.delete_message(self.message_id)

