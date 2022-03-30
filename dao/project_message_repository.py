from dao.base_repository import BaseRepository
from entity.project_message import ProjectMessage


class ProjectMessageRepository(BaseRepository):
    def find_by_name(self, message_part: str) -> list[ProjectMessage]:
        result = [prjmsg for prjmsg in self.find_all() if message_part.lower() in prjmsg.message.lower()]
        return result

    def find_all_username_messages(self, username: str) -> list[ProjectMessage]:
        result = [prjmsg for prjmsg in self.find_all() if username == prjmsg.employee.username]
        return result
