#@staticmethod
from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name):
        self.name = name
        self.albums=[]

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for alb in self.albums:
            if alb.name == album_name:
                if alb.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(alb)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."


    def details(self):
        result=f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()
            result += "\n"
        return result
