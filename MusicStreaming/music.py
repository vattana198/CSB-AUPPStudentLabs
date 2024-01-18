
# Prototype code, you can follow different implementation process
import csv


class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    def __init__(self,name):
        self.name = name
        self.songs = []
        self.artist_dict = {}
        self.album_dict = {}
        self.genre_dict = {}
        self.title_dict = {}

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            self._update_dicts()

    def _update_dicts(self):
        for song in self.songs:
            self.artist_dict.setdefault(song.artist, []).append(song)
            self.album_dict.setdefault(song.album, []).append(song)
            self.genre_dict.setdefault(song.genre, []).append(song)
            self.title_dict.setdefault(song.title, []).append(song)
            
    def get_songs_by_artist(self, artist):
        return self.artist_dict.get(artist, set())

    def get_songs_by_album(self, album):
        return self.album_dict.get(album, set())

    def get_songs_by_genre(self, genre):
        return self.genre_dict.get(genre, set())
    
    def get_songs_by_title(self, title):
        return self.title_dict.get(title, set())

    def display_songs(self,song):
        for song in self.songs:
            print(f"Song Title: {song.title} , Artist: {song.artist} , Album: {song.album} , Genre: {song.genre} , Length: {song.length} ")

    def export_to_csv(self, filename = "musicdata.csv"):
        with open(filename , mode= "a" , newline = "")  as file:
            writer = csv.writer(file)
            
            for song in self.songs:
                writer.writerow([song.title, song.artist , song.album , song.genre , song.length])

    def display_songs_from_csv(self , filename = "musicdata.csv"):
        with open(filename , mode ="r") as file :
            reader = csv.reader(file)
            for row in reader:
                print(f"Song Title: {row[0]}, Artist: {row[1]} , Album: {row[2]} , Genre: {row[3]} , Length: {row[4]}")

    def search_songs_from_csv(self, filename ="musicdata.csv" ):
        search_songs = input("Enter The Song Name: ")
        song_found = False
        with open(filename , mode= "r") as file :
            read = csv.reader(file)
            for row in read:
                if search_songs.lower() in row[0].lower() :
                    print(f"Song Title: {row[0]}, Artist: {row[1]} , Album: {row[2]} , Genre: {row[3]} , Length: {row[4]}")
                    song_found = True
            if not song_found:
                print("Song Not Found")
        
music = MusicLibrary("My Library")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist_songs = []

    def add_song(self):
        name_of_playlist = input("Enter The Name Of The Playlist: ")
        add_to_playlist = input("Enter The Song Name To The playlist: ")
        with open("musicdata.csv" , mode= "r") as file :
            reader = csv.reader(file)
            songs_in_file = [row[0] for row in reader]
        
        if add_to_playlist in songs_in_file:
            self.playlist_songs.append((name_of_playlist,add_to_playlist))
            print("Song Added To The Playlist")
        
            with open("playlist.csv" , mode= "a" , newline ="") as playlist_file:
                writer = csv.writer(playlist_file)
                writer.writerow([name_of_playlist,add_to_playlist])

        else:
            print(f"{add_to_playlist} Not Found in the Music Library")




    def remove_song(self):
        name_of_playlist = input("Enter The Name Of The Playlist: ")
        remove_from_playlist = input("Enter The Song Name To Remove from the playlist: ")

        with open("playlist.csv", mode="r") as playlist_file:
            reader = csv.reader(playlist_file)
            playlist_data = list(reader)

        found = False
        for row in playlist_data:
            if row[0] == name_of_playlist and row[1] == remove_from_playlist:
                playlist_data.remove(row)
                found = True
                break

        if found:
            print("Song Removed From The Playlist")
            with open("playlist.csv", mode="w", newline="") as playlist_file:
                writer = csv.writer(playlist_file)
                writer.writerows(playlist_data)
        else:
            print(f"{remove_from_playlist} Not Found in the Playlist")


           
        
                  


                
    
    def display_playlist(self):
        display_name = input("Enter The Name Of The Playlist: ")
        with open("playlist.csv", mode="r") as file:
            reader = csv.reader(file)
            playlist_songs = [row for row in reader if row[0] == display_name]

        if not any(row[0] == display_name for row in playlist_songs):
            print(f"No Playlist Founded with the name: {display_name}")
            return

        print(f"Playlist: {display_name}")

        for index, song in enumerate(playlist_songs, start=1):
            print(f"{index}. {song[1:]}")
    
    


playlist = Playlist("My Playlist 1")

    

def main():
    print("_____________________________________")
    print("Welcome to Music Streaming System ")
    print("Please select the option below:")
    print("1. Add Song")
    print("2. Display Song")
    print("3. Search Song")
    print("4. Create Playlist")
    print("5. Remove Song From Playlist")
    print("6. Display Playlist")
    print("7.Exit")
    print("_____________________________________")

    option = int(input("Enter the option: "))

    if option == 1:

        title = input("Enter song title:  ")
        artist = input("Enter artist name: ")
        album =  input("Enter alblum name: ")
        genre = input("Enter genre name: ")
        length = input("Enter length : ")
        user_song = Song(title, artist, album, genre, length)
        
        music.add_song(user_song)

        print(f"Song Title: {user_song.title} , Artist: {artist} , Album: {album} , Genre: {genre} , Length: {length} ")
        music.export_to_csv()
        print("Song Added Successfully")
        main()
    elif option == 2:
        music.display_songs_from_csv()
        main()
    elif option == 3 :
        music.search_songs_from_csv()
        main()
    elif option == 4 :
        playlist.add_song() 
        main()
    elif option == 5:
        playlist.remove_song()  
        main()
        # name_of_playlist = input("Enter The Name Of The Playlist:")
        # if name_of_playlist in playlist.playlist_songs: 
        #     playlist.remove_song(name_of_playlist)
        # else:
        #     print("Playlist Not Found")
    elif option == 6:
        playlist.display_playlist()
        main()       
    elif option == 7:
        print("Thank you for using Music Streaming System")
        exit()
    else:
        print("Invalid option, Please try again.")




main()










