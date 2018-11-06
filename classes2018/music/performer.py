"""Domain classes and functions related to the concept of performer
"""


import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the format_performer() method (converts a performer object to its name field for printing purposes).
    This can possibly be a static method.
    """

    def __init__(self, name, is_band=False):
        self.name = name
        self.is_band = is_band

    def __str__(self):
        return 'unknown' if not isinstance(self.name, str) or self.name == '' \
                         else self.name + (' (band)' if self.is_band else ' (musician)')

    # def __eq__(self, other):
    #     if not isinstance(other, Performer):
    #         return None
    #     return True if self.name == other.name else False

    def __eq__(self, other):
        if not isinstance(other, Performer):
            return False
        return self.name == other.name

    # def format_performer(self):
    #     return self.name if isinstance(self, Performer) and self.name else 'unknown'

    @staticmethod
    def format_performer(performer):
        performer_formatted = 'performer unknown'
        if isinstance(performer, Performer) and performer.name:
            performer_formatted = performer.name
        elif isinstance(performer, str):
            performer_formatted = performer
        return performer_formatted


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    # bruce = Performer('Bruce Springsteen')
    bruce = Performer('Bruce Springsteen', False)
    print(bruce)
    # print(bruce.format_performer())
    print(Performer.format_performer(bruce))


