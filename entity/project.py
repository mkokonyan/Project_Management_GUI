from datetime import datetime


class Project:
    def __init__(self,
                 project_id: str = None,
                 project_name: str = None,
                 client: str = None,
                 time_estimation: datetime = None,
                 due_date: datetime = None,
                 ):
        self._project_id = project_id
        self._project_name = project_name
        self._client = client
        self._time_estimation = time_estimation
        self._due_date = due_date
        self._employees = []
        self._tasks = []

    def __str__(self):
        return f"{self._project_name}"
