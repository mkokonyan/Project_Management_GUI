from exceptions.entity_not_found_exception import EntityNotFoundException


class BaseRepository:
    def __init__(self, idGenerator) -> None:
        self._entities = {}
        self._idGenerator = idGenerator

    def __len__(self) -> int:
        return len(self._entities)

    def __iter__(self):
        for entity in self._entities.values():
            yield entity

    def create(self, entity):
        entity.obj_id = self._idGenerator.get_next_id()
        self._entities[entity.obj_id] = entity
        return entity

    def find_all(self) -> list:
        return list(self._entities.values())

    def find_by_id(self, entity_id: str):
        if entity_id not in self._entities:
            raise EntityNotFoundException(f"Entity with ID:{entity_id} not found")
        searched_entity = self._entities.get(entity_id)
        return searched_entity

    def update(self, entity):
        self.find_by_id(entity.obj_id)
        self._entities[entity.obj_id] = entity
        return entity

    def delete_by_id(self, entity_id: str):
        entity_to_del = self.find_by_id(entity_id)
        del self._entities[entity_id]
        return entity_to_del
