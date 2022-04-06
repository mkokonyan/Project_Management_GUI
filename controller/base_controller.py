from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, service, view=None):
        self._service = service
        self._view = view

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value

    @abstractmethod
    def get_all_entities(self):
        pass

    @abstractmethod
    def reload_all_entities(self):
        pass

    @abstractmethod
    def save_entities(self):
        pass
