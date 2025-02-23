import requests


def get_songs_by_artist(artist_name, limit = 20):
    base_url = "https://itunes.apple.com/search"

    params = {
        "term": artist_name,
        "media": "music",
        "entity": "musicTrack",
        "limit": limit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        songs = [track["trackName"] for track in data.get("results", [])]
        return songs
    else:
        print(f"Error: {response.status_code}")
        return []
    


"""Get data bout songs"""
def get_song_data(song_name, limit=1):

    base_url = "https://itunes.apple.com/search"
    params = {
        "term": song_name,
        "media": "music",
        "entity": "musicTrack",
        "limit": limit
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["resultCount"] > 0:
            results = [
                {
                    "song": track["trackName"],
                    "artist": track["artistName"],
                    "album": track["collectionName"],
                    "release_date": track["releaseDate"],
                    "preview_url": track["previewUrl"],
                    "artwork": track["artworkUrl100"] 
                }
                for track in data["results"]
            ]
            return results
        else:
            return {"error": "No results found."}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
    

def get_top_songs_by_genre(genre, limit=10, country="US"):
    """Fetches the most popular songs in a given genre from the iTunes API."""
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": genre,
        "mediaType": "music",
        "entity": "musicTrack",
        "limit": limit,
        "country": country
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["resultCount"] > 0:
            return [
                {
                    "rank": idx + 1,
                    "song": track.get("trackName", "Unknown Song"),
                    "artist": track.get("artistName", "Unknown Artist"),
                    "album": track.get("collectionName", "Unknown Album"),
                    "preview_url": track.get("previewUrl", "No Preview Available"),
                    "artwork": track.get("artworkUrl100", "No Image Available")
                }
                for idx, track in enumerate(data.get("results", []))
            ]
        else:
            return []  # Ensure function always returns a list
    else:
        return []  # Return an empty list if the request fails

# Example usage
genre = "Rock"
top_songs = get_top_songs_by_genre(genre, limit=3)

if not top_songs:  # Check if list is empty
    print("No songs found.")
else:
    for song in top_songs:
        print(f"#{song['rank']} {song['song']} by {song['artist']}")
        print(f"Album: {song['album']}")
        print(f"Preview: {song['preview_url']}")
        print(f"Album Art: {song['artwork']}\n")

test = requests.get("https://itunes.apple.com/search?term=Rock&mediaType=music")
print(test)


artist = "Kendrick Lamar"
songs = get_songs_by_artist(artist)
print(f"Top songs by {artist}: {songs}\n")

song = "Shape of You"
data = get_song_data(song)

for track in data:
    print(f"{track['song']} by {track['artist']}")
    print(f"Album: {track['album']} (Released: {track['release_date']})")
    print(f"Preview: {track['preview_url']}")
    print(f"Album Art: {track['artwork']}\n")
