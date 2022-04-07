from controller.base_controller import BaseController
from entity.project import Project


class ProjectController(BaseController):

    @staticmethod
    def get_project_details(project: Project) -> dict[str]:
        return {
            "obj_id": project.obj_id,
            "name": project.name,
            "client": project.client,
            "time_estimation": project.time_estimation,
            "due_date": project.due_date,
            "is_finished": 'Archived' if project.is_finished else 'In progress'
        }

    def get_all_entities(self):
        return self._service.get_all_projects()

    def reload_all_entities(self) -> None:
        return self.service.reload_all_projects()

    def save_entities(self):
        return self._service.save_all_projects()

