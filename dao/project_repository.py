from datetime import datetime, timedelta

from dao.json_repository import JsonRepository
from entity.project import Project


class ProjectRepository(JsonRepository):
    DB_FILENAME = "db/projects.json"
    ENTITY_CLASS = Project

    def find_by_full_name(self, full_name: str) -> Project:
        result = [prj for prj in self.find_all() if full_name.lower() == prj.name.lower()]
        if result:
            return result[0]

    def find_by_name_part(self, name_part: str) -> list[Project]:
        result = [prj for prj in self.find_all() if name_part.lower() in prj.name.lower()]
        return result

    def find_by_client(self, client_part: str) -> list[Project]:
        result = [prj for prj in self.find_all() if client_part.lower() in prj.client.lower()]
        return result

    def find_by_due_date_approaching(self) -> list[Project]:
        result = [prj for prj in self.find_all() if
                  datetime.strptime(prj.due_date, "%Y-%m-%d") - timedelta(days=10) <= datetime.today()]
        return result

    def find_by_finished_status(self) -> list[Project]:
        result = [prj for prj in self.find_all() if prj.is_finished]
        return result
