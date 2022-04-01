class Task:
    def __init__(self,
                 obj_id: str = None,
                 name: str = None,
                 employee: str = None,
                 project: str = None,
                 description: str = None,
                 time_estimation: int = None,
                 status: str = "TO DO"
                 ) -> None:
        self._obj_id = obj_id
        self._name = name
        self._employee: str = employee
        self._project: str = project
        self._description = description
        self._time_estimation = time_estimation
        self._status = status
        self._is_finished: bool = False

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, value):
        self._employee = value

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def time_estimation(self):
        return self._time_estimation

    @time_estimation.setter
    def time_estimation(self, value):
        self._time_estimation = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        self._is_finished = value

    def __repr__(self) -> str:
        return self.name

    def get_info(self) -> str:
        return f"Task name: {self.name} " \
               f"| Assigned to: {self.employee:<15.15s} " \
               f"| Description: {self.description:<40.40s}" \
               f"| Time estimation: {self.time_estimation:<3}" \
               f"| Task status: {'Archived' if self.is_finished else self.status}"
