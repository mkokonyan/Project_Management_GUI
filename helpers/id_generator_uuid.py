import uuid


class IdGeneratorUuid:
    @staticmethod
    def get_next_id():
        return str(uuid.uuid1())
