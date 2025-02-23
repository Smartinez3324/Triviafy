import uuid
from bson.binary import UUID 

class Game:
    def __init__(self, host_id: UUID, game_id: UUID):
        self.__host_id = host_id
        self.__players = []
        self.__rounds = [] 
        
    def start_game(self): 



