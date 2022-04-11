class EditMessageCommand:
    def __init__(self, old_message, message_id, edit_func):
        self.old_message = old_message
        self.message_id = message_id
        self.edit_func = edit_func

    def __call__(self):
        self.edit_func(self.old_message, self.message_id)
