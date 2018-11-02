"""Domain classes and functions related to the concept of author
"""


from datetime import date
from enum import Enum
import json

from classes2018.util import utility


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """

    ALIVE = 1,
    DECEASED = 0


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts.
    """

    ROCK = 1,
    BLUES = 2,
    SOUL = 3,
    INDIE = 4


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts.
    """

    GUITAR = 1,
    KEYBOARDS = 2,
    BASS = 3,
    DRUMS = 4,
    VOCALS = 5,
    VOCALS_AND_OTHER = 6


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts.
    """

    LYRIC = 1,
    EPIC = 2,
    DRAMATIC = 3,
    REFLEXIVE = 4,
    HAIKU = 5


class Author:
    """The class describing the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, birth date, birth place, nationality, and whether he/she is still living or is deceased.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the author's name and age as properties (the age property is calculated from birth date),
    as well as:
        - the definition static field
        - the class methods show_definition(cls) and get_instance(cls, name) (alternative constructor)
        - the static methods show_generic_definition(), format_author(author) and alive_or_deceased(alive)
    """

    definition = "Creator of an artwork."

    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=Lives.ALIVE):
        self.name = name
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.nationality = nationality
        self.alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name if name and isinstance(name, str) else 'unknown'

    @property
    def age(self):
        return date.today().year - self.birth_date.year if isinstance(self.birth_date, date) else 'unknown'

    def __str__(self):
        return '{}\n\tborn: {}\n\tage: {}\n\tplace of birth: {}\n\tnationality: {}\n\t{}\n'.\
            format(self.name, str(self.birth_date) if isinstance(self.birth_date, date) else 'unknown',
                   str(self.age), self.birth_place, self.nationality, Author.alive_or_deceased(self.alive))

    @classmethod
    def show_definition(cls):
        print(cls.definition)

    @staticmethod
    def show_generic_definition():
        print(Author.definition)

    @staticmethod
    def format_author(author):
        return author.name if isinstance(author, Author) and isinstance(author.name, str) and author.name else 'unknown'

    @staticmethod
    def alive_or_deceased(alive):
        return 'alive' if alive == Lives.ALIVE else 'deceased' if alive == Lives.DECEASED else 'alive/deceased: unknown'

    @classmethod
    def get_instance(cls, name):
        return cls(name) if isinstance(name, str) else cls('unknown')

    def __eq__(self, other):
        return True if isinstance(other, Author) and other.name == self.name and other.birth_date == self.birth_date \
            else False


class AuthorEncoder(json.JSONEncoder):
    """JSON encoder for Author objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """


def json_to_py(author_json):
    """JSON decoder for Author objects (object_hook parameter in json.loads()).
    """


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s). These are defined as properties of the Musician class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author, with addition of
    the type of poetry they create. This is defined as a property of the Poet class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclasses.
    """


if __name__ == "__main__":

    bruce = Author('Bruce Springsteen', birth_date=date(1949, 9, 23), birth_place='Freehold', nationality='US')
    print(bruce)
    bruce1 = bruce.get_instance('Bruce')
    print(bruce1)
    bruce1.name = 'Bruce Springsteen'
    bruce1.birth_date = date(1949, 9, 23)
    print(bruce1)
    print(bruce == bruce1)
    Author.show_definition()
    Author.show_generic_definition()



