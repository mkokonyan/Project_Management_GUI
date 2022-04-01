from datetime import datetime


class ProjectMessage:
    def __init__(self,
                 obj_id: str = None,
                 message: str = None,
                 username: str = None,
                 ) -> None:
        self._obj_id = obj_id
        self._message = message
        self._username = username
        self._sent_on = datetime.now()

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def sent_on(self):
        return self._sent_on

    @sent_on.setter
    def sent_on(self, value):
        self._sent_on = value

    def __repr__(self) -> str:
        return f"{self._message} (by {self._username})"

    def get_info(self) -> str:
        return f"Message: {self._message} " \
               f"(by {self._username}) " \
               f"sent on {self._sent_on}"
