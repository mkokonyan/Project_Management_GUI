class Task:
    def __init__(self,
                 task_id=None,
                 task_name=None,
                 employee=None,
                 description=None,
                 time_estimation=None,
                 due_date=None,
                 ):
        self._task_id = task_id
        self._task_name = task_name
        self._employee = employee
        self._description = description
        self._time_estimation = time_estimation
        self._due_date = due_date

    def __str__(self):
        return f"{self._task_name}"
