import Song

class Round:
    def __init__(self, game_id, round_number, song: Song):
        self.round_id = str(uuid4())  # Unique round ID
        self.player_answers = {}  # Player answers {player_id: answer}
        self.song = song

    def set_song(self, song_data):
        """Set the song snippet for this round."""
        self.song = song_data["preview_url"]
        self.correct_answer = song_data["name"]

    def submit_answer(self, player_id, answer):
        """Save a player's answer."""
        self.player_answers[player_id] = answer

    def is_correct(self, player_id):
        """Check if a player's answer is correct."""
        return self.player_answers.get(player_id) == self.correct_answer
