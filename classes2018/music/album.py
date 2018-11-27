"""Domain classes and functions related to the concept of album
"""
from datetime import date, timedelta, datetime
from time import perf_counter
import random
import sys

import jsonpickle as jsonpickle

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

    def __init__(self, title, performer=None, songs=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.songs = songs
        self.duration = duration
        self.release_date = release_date

        self.__i = 0                        # iterator counter

    def __str__(self):
        a = 'Album: ' + self.title + '\n\tperformer: {}\n\tsongs: {}\n\tduration: {}\n\trelease date: {}\n'.\
            format(Performer.format_performer(self.performer), format_songs(self.songs),
                   utility.format_duration(self.duration), utility.format_date(self.release_date))
        return a

    def __eq__(self, other):
        return isinstance(other, Album) and self.title == other.title and self.performer == other.performer

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.songs):
            song = self.songs[self.__i]
            self.__i += 1
            return song
        else:
            raise StopIteration


def format_songs(songs):
    """Formats the album's song list for __str__().
    """

    return '\n\t\t'.join([s.title for s in songs]) if songs and isinstance(songs, list) else 'not specified'


# def generate_songs(songs):
#     """A generator of Song objects, given the input list of songs.
#     """


def shuffle(album, seed, play_time):
    """A generator of song titles from a given album in random order.
    Simulates shuffle-playing of songs from the album
    for play_time time (a float number expected by time.perf_counter()).
    """

    random.seed(seed)
    i = random.randint(0, len(album.songs) - 1)
    play_until = perf_counter() + play_time

    while perf_counter() < play_until:
        # print('Next song: ')
        yield album.songs[i].title
        i = random.randint(0, len(album.songs) - 1)

    # Alternatively:
    # while True:
    #     # print('Next song: ')
    #     yield album.songs[i].title
    #     if perf_counter() > play_until:
    #         break
    #     i = random.randint(0, len(album.songs) - 1)


class AlbumError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class SongNotIncludedError(AlbumError):
    """Exception raised when a song from an album is requested,
    but is not included in the list of songs from that album.
    """

    def __init__(self, song, album):
        self.song = song
        self.album = album
        self.message = 'Song \'{}\' not included on album \'{}\'\n'.format(self.song.title, self.album.title)


def play_song(song, album):
    """Play the requested song from the album.
    Raises SongNotIncludedError() if the requested song is not included on the album.
    """

    # if isinstance(song, Song) and isinstance(album, Album):
    #     if song in album.songs:
    #         print('Playing \'{}\'...'.format(song.title))
    #     else:
    #         raise SongNotIncludedError(song, album)
    # else:
    #     raise TypeError()
    if song in album.songs:
        print('Playing \'{}\'...'.format(song.title))
    else:
        raise SongNotIncludedError(song, album)


if __name__ == "__main__":

    patti_smith = Performer("Patti Smith")
    patti = Author('Patti Smith', date(1946, 12, 30), 'Chicago', 'US')
    till_victory = Song('Till Victory', patti_smith, patti, 185, date(1978, 3, 3))
    space_monkey = Song('Space Monkey', patti_smith, patti, 198, date(1978, 3, 3))
    because_the_night = Song('Because the Night', patti_smith, patti, 189, date(1978, 3, 2))
    easter = Album('Easter', patti_smith, songs=[till_victory, space_monkey, because_the_night],
                   duration=594, release_date=date(1978, 3, 3))
    print()

    # print(easter)
    # for song in easter:
    #     print(song)

    # for song in shuffle(easter, 23, 0.0001):                            # demonstrate generators
    #     print(song)
    # print()

    # songs = [till_victory, space_monkey, because_the_night]
    # for i in range(5):                                                  # demonstrate catching exceptions
    #     try:
    #         # print(songs[i] / 4)
    #         print(songs[i])
    #     # # except:
    #     # #     print('Caught an exception...')
    #     # #     break
    #     # except Exception as e:
    #     #     print(type(e).__name__, e.args)
    #     #     print(type(e).__name__ + ':', e.args[0])
    #     #     print(type(e).__name__ + ':', e.args[0], '(i = ' + str(i) + ')')
    #     #     break
    #     except IndexError as e:
    #         print('Caught exception:', e.args[0], '(i = ' + str(i) + ')')
    #         break
    #     except Exception as e:
    #         print(type(e).__name__ + ':', e.args[0])
    #         break
    #     else:
    #         print('Do something if no exception is caught...')
    #     finally:
    #         print('Finally...')
    # print('Done.')
    # print()

    # try:                                                            # demonstrate catching user-defined exceptions
    #     # play_song(because_the_night, easter)
    #     # play_song(Song('Dancing Barefoot'), 'ddd')
    #     play_song(Song('Dancing Barefoot'), easter)
    # except SongNotIncludedError as e:
    #     sys.stderr.write(e.message)
    #     # print(e.message, file=sys.stderr)
    #     print(e.args)
    #     print(e.message)
    # except TypeError as e:
    #     # sys.stderr.write(e.args)
    #     # print(e.args, file=sys.stderr)
    #     # print(e.args)
    #     # sys.stderr.write(e.__class__.__name__)
    #     print(e.__class__.__name__)
    # else:
    #     print('Nice song :)')
    # finally:
    #     print('Done')
    # print()

    # Attempt to use jsonpickle. Works only if __iter__() and __next__() are commented out.
    # With __iter__() and __next__() in place, jsonpickle.decode() returns a list_iterator object, not an Album object.

    easter_json = jsonpickle.encode(easter, make_refs=False)
    print(easter_json)
    easter_py = jsonpickle.decode(easter_json)
    print(easter == easter_py)
    print(type(easter_py))
    print(type(easter))
    print(easter_py)


