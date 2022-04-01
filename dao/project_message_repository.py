from dao.json_repository import JsonRepository
from entity.project_message import ProjectMessage


class ProjectMessageRepository(JsonRepository):
    DB_FILENAME = "db/project_messages.json"
    ENTITY_CLASS = ProjectMessage

    def find_by_content(self, message_part: str) -> list[ProjectMessage]:
        result = [msg for msg in self.find_all() if message_part.lower() in msg.message.lower()]
        return result

    def find_all_username_messages(self, username: str) -> list[ProjectMessage]:
        result = [msg for msg in self.find_all() if username == msg.username]
        return result
