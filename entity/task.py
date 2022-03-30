from entity.employee import Employee
from helpers.validators.task_validators import validate_task_name_length, validate_description_length, \
    validate_task_time_estimation


class Task:
    def __init__(self,
                 task_id: str = None,
                 task_name: str = None,
                 employee: Employee = None,
                 description: str = None,
                 time_estimation: int = None,
                 ) -> None:
        self.obj_id = task_id
        self.name = task_name
        self._employee = employee
        self.description = description
        self.time_estimation = time_estimation
        self._is_finished: bool = False

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    @property
    def name(self):
        return self._task_name

    @name.setter
    def name(self, value):
        validate_task_name_length(value)
        self._task_name = value

    @property
    def employee(self):
        return self._employee

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        validate_description_length(value)
        self._description = value

    @property
    def time_estimation(self):
        return self._time_estimation

    @time_estimation.setter
    def time_estimation(self, value):
        validate_task_time_estimation(value)
        self._time_estimation = value

    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        if value:
            self._is_finished = True

    def __repr__(self) -> str:
        return f"{self._task_name}"

    def get_info(self) -> str:
        return f"Task name: {self._task_name:<10.15s} " \
               f"| Assigned to: {str(self.employee):<10.15s} " \
               f"| Description: {self.description:<20.40s}" \
               f"| Time estimation: {self._time_estimation:<3}" \
               f"| Task status: {'Archived' if self._is_finished else 'In progress':<10.11s}"
