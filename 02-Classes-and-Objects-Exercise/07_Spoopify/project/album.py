from project.song import Song
class Album:
    def __init__(self, name, *songs):
        self.name = name
        # self.list_songs_input = list_songs_input
        self.published=False
        self.songs=list(songs)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        for s in self.songs:
            if s.name==song.name:
                return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name==song:
                return f"Removed song {song} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published=True
        return f"Album {self.name} has been published."

    def details(self):
        result=f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.name} - {s.length}\n"
        return result

