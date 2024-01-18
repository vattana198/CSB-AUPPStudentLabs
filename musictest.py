class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

class MusicLibrary:
    def __init__(self):
        self.songs = set()
        self.artist_dict = {}
        self.album_dict = {}
        self.genre_dict = {}
        self.title_dict = {}

    def add_song(self, song):
        if song not in self.songs:
            self.songs.add(song)
            self._update_dicts(song)

    def _update_dicts(self, song):
        self.artist_dict.setdefault(song.artist, set()).add(song)
        self.album_dict.setdefault(song.album, set()).add(song)
        self.genre_dict.setdefault(song.genre, set()).add(song)
        self.title_dict.setdefault(song.title, set()).add(song)

    def get_songs_by_artist(self, artist):
        return self.artist_dict.get(artist, set())

    def get_songs_by_album(self, album):
        return self.album_dict.get(album, set())

    def get_songs_by_genre(self, genre):
        return self.genre_dict.get(genre, set())

    def get_songs_by_title(self, title):
        return self.title_dict.get(title, set())

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def reorder_songs(self, new_order):
        # Assuming new_order is a list of song objects
        self.songs = [song for song in new_order if song in self.songs]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song.title} - {song.artist}")

# Example Usage:

# Creating songs
song1 = Song("Song 1", "Artist 1", "Album 1", "Genre 1", "3:45")
song2 = Song("Song 2", "Artist 2", "Album 2", "Genre 2", "4:20")

# Creating a music library
library = MusicLibrary()
library.add_song(song1)
library.add_song(song2)

# Creating a playlist
playlist1 = Playlist("My Playlist 1")
playlist1.add_song(song1)
playlist1.add_song(song2)

# Displaying playlist
playlist1.display_playlist()

# Searching for songs by artist
artist1_songs = library.get_songs_by_artist("Artist 1")
print("Songs by Artist 1:")
for song in artist1_songs:
    print(f"{song.title} - {song.album}")
