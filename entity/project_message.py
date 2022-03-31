from datetime import datetime


class ProjectMessage:
    def __init__(self,
                 project_message_id: str = None,
                 message: str = None,
                 username: str = None,
                 project_name: str = None
                 ) -> None:
        self.obj_id = project_message_id
        self._comment = message
        self._username = username
        self._project = project_name
        self._sent_on = datetime.now()

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    @property
    def message(self):
        return self._comment

    @property
    def username(self):
        return self._username

    @property
    def project(self):
        return self._project

    @property
    def sent_on(self):
        return self._sent_on

    def __repr__(self) -> str:
        return f"{self._comment} by {self._username}"

    def get_info(self) -> str:
        return f"Message: {self._comment} " \
               f"by {self._username} " \
               f"sent on {self._sent_on.strftime('%H:%M:%S, %Y-%m-%d')}"
