from datetime import datetime


class Project:
    def __init__(self,
                 obj_id: str = None,
                 name: str = None,
                 client: str = None,
                 time_estimation: int = None,
                 due_date: str = None,
                 ) -> None:
        self._obj_id = obj_id
        self._name = name
        self._client = client
        self._time_estimation = time_estimation
        self._due_date = due_date
        self._employees: list[str] = []
        self._tasks: list[str] = []
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
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def time_estimation(self):
        return self._time_estimation

    @time_estimation.setter
    def time_estimation(self, value):
        self._time_estimation = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = datetime.strptime(value, "%Y-%m-%d")

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, value):
        self._employees = value

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        self._is_finished = value

    def __repr__(self) -> str:
        return f"{self.name}"

    def get_info(self) -> str:
        return f"Project name: {self.name:<10.15s} " \
               f"| Client {self.client:<10.15s} " \
               f"| Employees assigned: {', '.join([e for e in self.employees]) if self.employees else 'None':<30.40s} " \
               f"| Number of tasks: {len(self.tasks):<3}" \
               f"| Project status:{'Archived' if self.is_finished else 'In progress':<10.11s}"
