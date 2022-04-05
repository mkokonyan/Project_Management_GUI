from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, service, view=None):
        self._service = service
        self._view = view

    @property
    def service(self):
        return self._service

    @property
    def view(self):
        return self._view

    @abstractmethod
    def get_all_entities(self):
        pass

    @abstractmethod
    def reload_all_entities(self):
        pass

    @abstractmethod
    def save_entities(self):
        pass
