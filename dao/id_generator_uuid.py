import uuid


class IdGeneratorUuid:
    @staticmethod
    def get_next_id():
        return uuid.uuid1()
