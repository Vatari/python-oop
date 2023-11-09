from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album_: Album):
        for album_local in self.albums:
            if album_.name == album_local.name:
                return f"Band {self.name} already has {album_.name} in their library."
        self.albums.append(album_)
        return f"Band {self.name} has added their newest album {album_.name}."

    def remove_album(self, album_name: str):
        for album_ in self.albums:
            if album_.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album_)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}'
        for album_ in self.albums:
            result += '\n' + album_.details()
        return result


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
