class Song:
    def __init__(self, artist: str, song: str, album: str, song_id: int):
        self.__artist = artist
        self.__song = song
        self.__album = album
        self.__song_id = song_id
    
    def get_artist(self) -> str :
        return self.__artist
    
    def get_song(self) -> str :
        return self.__song

    def get_album(self) -> str :
        return self.__album

    def get_song_id(self) -> int :
        return self.__song_id
