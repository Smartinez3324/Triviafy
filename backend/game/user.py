import uuid

from bson.binary import UUID 

class User:
    def __init__ (self, id: UUID, user_name: str):
        self.__id = uuid.uuid4
        self.__user_name = 

