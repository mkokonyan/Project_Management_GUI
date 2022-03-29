class ProjectMessage:
    def __init__(self,
                 project_message_id=None,
                 project_name=None,
                 comment=None,
                 employee=None,
                 ):
        self._project_message_id = project_message_id
        self._project_name = project_name
        self._comment = comment
        self._employee = employee

    def __str__(self):
        return f"{self._comment} by {self._employee}"
