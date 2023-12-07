"""Player object is stored here"""

# This code is modified version of github.com/abhishekmj303/ulauncher-playerctl/blob/main/playerctl/__init__.py file
# Original source code/file was published under GPLv3 license.


# pylint: disable=R0913
class Player:
    """Player class"""
    def __init__(self, name, state, artist, album, song):
        self.name = name
        self.state = state
        self.artist = artist
        self.album = album
        self.song = song

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player({self.name}, {self.state}, {self.artist}, {self.album}, {self.song})"
