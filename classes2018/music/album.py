"""Domain classes and functions related to the concept of album
"""
from datetime import date

from classes2018.music.author import Author
from classes2018.music.performer import Performer
from classes2018.music.song import Song
from classes2018.util import utility


class Album:
    """The class describing the concept of album.
    It is assumed that an album is sufficiently described by its
    title, performer, songs, duration and release date.
    The class defines the __init__(), __str__(), __eq__(), __iter__() and __next__() methods.
    """

    def __init__(self, title='', performer=None, songs=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.songs = songs
        self.duration = duration
        self.release_date = release_date

        self.__i = 0                            # iterator counter

    def __str__(self):
        return '{}\n\tperformer(s): {}\n\tsongs:\n\t\t{}\n\tduration: {}\n\trelease date: {}\n'.\
            format(self.title, Performer.format_performer(self.performer), format_songs(self.songs),
                   utility.format_duration(self.duration), utility.format_date(self.release_date))

    def __eq__(self, other):
        return isinstance(other, Album) and other.title == self.title and other.performer == self.performer

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.songs):
            self.__i += 1
            return self.songs[self.__i - 1]
        else:
            raise StopIteration


def format_songs(songs):
    """Formats the album's song list for __str__().
    """

    return '\n\t\t'.join(song.title for song in songs) if isinstance(songs, list) and songs != [] \
        else '\n\t\tnot specified'


def generate_songs(songs):
    """A generator of Song objects, given the input list of songs.
    """


class AlbumError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class SongNotIncludedError(AlbumError):
    """Exception raised when a song from an album is requested,
    but is not included in the list of songs from that album.
    """


def play_song(song, album):
    """Play the requested song from the album.
    Raises SongNotIncludedError() if the requested song is not included on the album.
    """


if __name__ == "__main__":

    patti_smith = Performer("Patti Smith")
    patti = Author('Patti Smith', date(1946, 12, 30), 'Chicago', 'US')
    till_victory = Song('Till Victory', patti_smith, patti, 185, date(1978, 3, 3))
    space_monkey = Song('Space Monkey', patti_smith, patti, 198, date(1978, 3, 3))
    because_the_night = Song('Because the Night', patti_smith, patti, 189, date(1978, 3, 2))
    easter = Album('Easter', patti_smith, songs=[till_victory, space_monkey, because_the_night],
                   duration=594, release_date=date(1978, 3, 3))
    print()

    print(easter)
    for song in easter:
        print(song)

