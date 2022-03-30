from datetime import datetime, timedelta

from dao.base_repository import BaseRepository
from entity.project import Project


class ProjectRepository(BaseRepository):
    def find_by_name(self, name_part: str) -> list[Project]:
        result = [prj for prj in self.find_all() if name_part.lower() in prj.name.lower()]
        return result

    def find_by_client(self, client_part: str) -> list[Project]:
        result = [prj for prj in self.find_all() if client_part.lower() in prj.client.lower()]
        return result

    def find_by_due_date_approaching(self) -> list[Project]:
        result = [prj for prj in self.find_all() if prj.due_date - timedelta(days=10) <= datetime.today()]
        return result

    def find_by_finished_status(self) -> list[Project]:
        result = [prj for prj in self.find_all() if prj.is_finished]
        return result

