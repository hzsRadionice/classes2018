"""Domain classes and functions related to the concept of song
"""
import json
import pickle
from pathlib import Path

import jsonpickle

from classes2018 import settings
from classes2018.music import performer, author
from classes2018.util import utility

from datetime import date


class Song:
    """The class describing the concept of song.
    It is assumed that a song is sufficiently described by its
    title, performer, author, duration and release date.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the play() method that "plays" the corresponding song.
    """

    definition = "A nice piece of music, often sung by a human voice " \
                 "(but can be instrumental only as well)"

    def __init__(self, title='', performer=None, author=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.author = author
        self.duration = duration
        self.release_date = release_date

    # def __str__(self):
    #     return '{}\n\tperformer(s): {}\n\tauthor(s): {}\n\tduration: {}\n\trelease date: {}'.\
    #         format(self.title, str(self.performer), str(self.author), str(self.duration), str(self.release_date), )

    def __str__(self):
        return '{}\n\tperformer(s): {}\n\tauthor(s): {}\n\tduration: {}\n\trelease date: {}'.\
            format(self.title,
                   # self.performer.format_performer() if self.performer else 'unknown',
                   performer.Performer.format_performer(self.performer) if self.performer else 'unknown',
                   # str(self.author),
                   author.Author.format_author(self.author),
                   # str(self.duration),
                   utility.format_duration(self.duration),
                   # str(self.release_date), )
                   utility.format_date(self.release_date), )

    # def __eq__(self, other):
    #     if not isinstance(other, Song):
    #         return False
    #     return True if self.title == other.title and self.performer == other.performer else False

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self.title == other.title and self.performer == other.performer

    def play(self):
        # print('Playing:', self.title)
        print('Playing: {} ({})'.format(self.title, performer.Performer.format_performer(self.performer)))


def py_to_json(song):
    if isinstance(song, Song):
        d = song.__dict__.copy()
        d['performer'] = json.dumps(song.performer, indent=4, cls=performer.PerformerEncoder)
        d['author'] = json.dumps(song.author, indent=4, cls=author.AuthorEncoder)
        d['release_date'] = utility.date_py_to_json(song.release_date)
        return {'__Song__': d}
    return {'__{}__'.format(song.__class__.__name__): song.__dict__}


def json_to_py(song_json):
    if '__Song__' in song_json:
        song = Song()
        song.__dict__.update(song_json['__Song__'])
        song.performer = json.loads(song.__dict__['performer'], object_hook=performer.json_to_py)
        song.author = json.loads(song.__dict__['author'], object_hook=author.json_to_py)
        song.release_date = utility.date_json_to_py(song.__dict__['release_date'])
        return song
    return song_json


if __name__ == "__main__":

    # because_the_night = Song('Because the Night', 'Patti Smith', 'Bruce Springsteen Patti Smith', 234)
    because_the_night = Song('Because the Night',
                             'Patti Smith',
                             'Bruce Springsteen, Patti Smith',
                             234,
                             date(1978, 3, 2))
    # b = Song('Because the Night',
    #          'Patti Smith',
    #          'Bruce Springsteen, Patti Smith',
    #          234,
    #          date(1978, 3, 2))
    #
    # print(because_the_night)
    # print(b == because_the_night)
    # print()

    # because_the_night.play()
    # print()
    #
    # bruce = Performer('Bruce Springsteen', True)
    # print(bruce)
    # because_the_night.performer = bruce
    # print(because_the_night)
    # print()
    #
    # because_the_night.play()
    # print()

    # Writing/Reading to/from a text file
    #
    # print('Writing data to a txt file...')
    # with open('because_the_night.txt', 'w') as out_file:
    #     out_file.write(str(because_the_night))
    # print('Data written to a txt file.')
    # print()
    #
    # print('Reading data from a txt file...')
    # with open('because_the_night.txt', 'r') as in_file:
    #     becauseTheNight = in_file.read()
    # print('Data read from a txt file.')
    # print()
    #
    # print(str(because_the_night) == becauseTheNight)
    # print()

    # Writing/Reading to/from a binary file

    # print('Writing data to a binary file...')
    # with open('because_the_night', 'wb') as out_file:
    #     # out_file.write(bytearray(str(because_the_night), encoding='ascii'))
    #     # out_file.write(bytes(str(because_the_night), encoding='ascii'))
    #     out_file.write(str.encode(str(because_the_night)))
    # print('Data written to a binary file.')
    # print()
    #
    # print('Reading data from a binary file...')
    # with open('because_the_night', 'rb') as in_file:
    #     becauseTheNight = in_file.read()
    # print('Data read from a binary file.')
    # print()
    #
    # print(becauseTheNight)
    # print(str(becauseTheNight))
    # print()
    # # print(str(because_the_night) == becauseTheNight)
    # print(str(because_the_night) == becauseTheNight.decode())
    # print()

    # Demonstrate pickle-serialization to a file

    # print('Pickle-serialize data to a file...')
    # with open('because_the_night', 'wb') as out_file:
    #     pickle.dump(because_the_night, out_file, protocol=pickle.HIGHEST_PROTOCOL)
    # print('Data pickle-serialized to a binary file.')
    # print()
    #
    # print('Deserializing data from a pickle-serialized file...')
    # with open('because_the_night', 'rb') as in_file:
    #     becauseTheNight = pickle.load(in_file)
    # print('Data deserialized from a pickle-serialized file.')
    # print()
    #
    # print(becauseTheNight)
    # print()
    # print(because_the_night == becauseTheNight)
    # print()

    # Demonstrate pickle-serialization to a string

    # print('Pickle-serialize to a string...')
    # s = pickle.dumps(because_the_night, protocol=pickle.HIGHEST_PROTOCOL)
    # print('Data pickle-serialized to a string.')
    # print()
    #
    # print('Deserializing data from a pickle-serialized string...')
    # becauseTheNight = pickle.loads(s)
    # print('Data deserialized from a pickle-serialized string.')
    # print()
    #
    # print(s)
    # print()
    # print(because_the_night == becauseTheNight)
    # print()

    # Demonstrate working with pathlib.Path

    # current_dir = Path('.')                                           # print() and str() return only '.'
    # current_dir = Path('.').absolute()
    # print('Current dir:', current_dir)
    # print('Parent dir:', current_dir.parent)
    # new_dir = current_dir.parent / 'new'
    # print('new_dir:', new_dir)
    # print('type(new_dir):', type(new_dir))
    # print('Path.cwd():', Path.cwd())
    # print(Path.cwd() / 'new')
    # print('PROJECT_DIR:', settings.PROJECT_DIR)
    # print('get_project_dir():', utility.get_project_dir())
    # print()
    # # new_dir = Path.cwd() / 'new/data/blues'
    # # new_dir.mkdir(parents=True, exist_ok=True)
    # # new_dir.rmdir()                                                     # rmdir() requires the dir to be empty
    # # print(new_dir)
    # # data_dir = Path.cwd() / 'new/data'
    # # print(data_dir)
    # # data_dir.rmdir()
    # data_dir = utility.get_data_dir()
    # print(data_dir)
    # print()

    # Writing/Reading to/from a file in a data dir

    # file = Path(utility.get_data_dir() / 'because_the_night.txt')
    # file.write_text(str(because_the_night))
    # becauseTheNight = file.read_text()
    # print(str(because_the_night) == becauseTheNight)
    #
    # file = Path(utility.get_data_dir() / 'because_the_night')
    # file.write_bytes(bytes(str(because_the_night), encoding='ascii'))
    # becauseTheNight = file.read_bytes()
    # print(str(because_the_night) == becauseTheNight.decode())

    # JSON

    bruce = author.Author("Bruce Springsteen", date(1949, 9, 23), "Freehold, NJ", "US")
    patti = performer.Performer("Patti Smith")
    becauseTheNight = Song('Because the Night', patti, bruce, 190, date(1978, 3, 2))

    becauseTheNight_json = json.dumps(becauseTheNight, indent=4, default=py_to_json)
    print(becauseTheNight_json)
    b = json.loads(becauseTheNight_json, object_hook=json_to_py)
    print(b == becauseTheNight)
    print()

    # jsonpickle
    becauseTheNight_json = jsonpickle.encode(becauseTheNight)
    b = jsonpickle.decode(becauseTheNight_json)
    print(b == becauseTheNight)
    print()


