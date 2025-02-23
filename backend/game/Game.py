import uuid
from typing import List
from bson.binary import UUID
from game.Song import Song

class Game:
    def __init__(self, game_id: UUID, songs: List[Song]):
        self.players = []
        self.game_id = game_id
        self.songs = songs 
        self.songs_done = []
    
    



