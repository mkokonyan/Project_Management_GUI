import json

from dao.base_repository import BaseRepository
from helpers.json_helpers import dumper, object_hook


class JsonRepository(BaseRepository):
    DB_FILENAME = None
    ENTITY_CLASS = None

    def save(self):
        with open(self.DB_FILENAME, "wt", encoding="UTF-8") as f:
            json.dump(self.find_all(), f, indent=4, default=dumper)

    def load(self):
        self.clear()
        with open(self.DB_FILENAME, "rt", encoding="UTF-8") as f:
            objects = json.load(f, object_hook=object_hook(self.ENTITY_CLASS))
            for obj in objects:
                self.create(obj)
