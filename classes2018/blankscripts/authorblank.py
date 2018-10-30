"""Domain classes and functions related to the concept of author
"""


from datetime import date
from enum import Enum
import json

from classes2018.util import utility


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts.
    """


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts.
    """


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts.
    """


class Author:
    """The class describing the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, birth date, birth place, nationality, and whether he/she is still living or is deceased.
    """


class AuthorEncoder(json.JSONEncoder):
    """JSON encoder for Author objects.
    """


def json_to_py(author_json):
    """JSON decoder for Author objects (object_hook parameter in json.loads()).
    """


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s).
    """


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author,
    with addition of the type of poetry they create.
    """


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet.
    """


if __name__ == "__main__":

    pass
