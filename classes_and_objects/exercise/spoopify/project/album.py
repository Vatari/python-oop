from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song_: Song):
        for song_local in self.songs:
            if song_.name == song_local.name:
                return "Song is already in the album."
        if song_.single:
            return f"Cannot add {song_.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song_)
        return f"Song {song_.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for song in self.songs:
            if self.published:
                return f"Cannot remove songs. Album is published."
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        infos = []
        for song_ in self.songs:
            infos.append(f"=== "+song_.get_info())
        result = '\n'.join(infos)
        return f"Album {self.name}\n{result}"


