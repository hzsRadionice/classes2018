"""Domain classes and functions related to the concept of song
"""

from classes2018.music.performer import Performer
from classes2018.music.author import Author
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
                   Performer.format_performer(self.performer) if self.performer else 'unknown',
                   # str(self.author),
                   Author.format_author(self.author),
                   # str(self.duration),
                   utility.format_duration(self.duration),
                   # str(self.release_date), )
                   utility.format_date(self.release_date), )

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return True if self.title == other.title and self.performer == other.performer else False

    def play(self):
        # print('Playing:', self.title)
        print('Playing: {} ({})'.
              format(self.title, self.performer.format_performer() if not self.performer else 'performer unknown'))


if __name__ == "__main__":

    # because_the_night = Song('Because the Night', 'Patti Smith', 'Bruce Springsteen Patti Smith', 234)
    because_the_night = Song('Because the Night',
                             'Patti Smith',
                             'Bruce Springsteen, Patti Smith',
                             234,
                             date(1978, 3, 2))
    # print(because_the_night)
    # print()
    # because_the_night.play()
    # print()

    bruce = Performer('Bruce Springsteen', True)
    print(bruce)
    because_the_night.performer = bruce
    print(because_the_night)
    print()



