from uuid import UUID
from game.Song import Song
import uuid

class Round:
    def __init__(self, game_id: UUID, round_number: int, song: Song):
        self.round_id = uuid.uuid4()  # Unique round ID
        self.round_number = round_number
        self.round_answer = song.song_name

    def is_correct(self, answer: str):
        """Check if a player's answer is correct."""
        return answer == self.round_answer
