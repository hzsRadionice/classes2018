"""Domain classes and functions related to the concept of performer
"""


import json
from pathlib import Path

from classes2018.util import utility


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

    def default(self, o):
        if isinstance(o, Performer):
            return {'__Performer__': o.__dict__}
        return {'__{}__'.format(o.__class__.__name): o.__dict__}


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """

    # performer_json_no_whitespace = ''.join(performer_json.split)
    # if '__Performer__' in performer_json_no_whitespace:
    if '__Performer__' in performer_json:
        p = Performer('')
        # d = performer_json['__Performer__']
        p.__dict__.update(performer_json['__Performer__'])
        return p
    return performer_json


if __name__ == "__main__":

    # bruce = Performer('Bruce Springsteen')
    bruce = Performer('Bruce Springsteen', False)
    print(bruce)
    # print(bruce.format_performer())
    print(Performer.format_performer(bruce))
    print()

    # JSON

    # intro
    print(bruce.__class__)
    print(bruce.__class__.__name__)
    print(bruce.__dict__)
    print()

    print(json.dumps(True))
    print(json.dumps(12))
    print(json.dumps([1, 2, 3, 'Patti']))
    print(json.dumps(bruce.__dict__, indent=4))
    print()

    with open(utility.get_data_dir() / 'bruce.json', 'w') as f:
        json.dump(bruce.__dict__, f, indent=4)
    with open(utility.get_data_dir() / 'bruce.json') as f:
        d = json.load(f)
    print(d)
    b = Performer('', True)                                 # deliberately erroneous parameters in the constructor
    b.__dict__.update(d)
    print(b == bruce)
    print()

    # using JSONEncoder
    bruce_json = json.dumps(bruce, indent=4, cls=PerformerEncoder)
    print(bruce_json)
    print(type(bruce_json))
    print()

    b = json.loads(bruce_json, object_hook=json_to_py)      # just the function name in object_hook!
    print(b)
    print(bruce == b)
    print()

    patti = Performer("Patti Smith", False)
    bruce_and_patti_json = json.dumps([bruce, patti], indent=4, cls=PerformerEncoder)
    print(bruce_and_patti_json)
    bruce_and_patti_list = json.loads(bruce_and_patti_json, object_hook=json_to_py)
    print(bruce_and_patti_list)
    for performer in bruce_and_patti_list:
        print(performer)
    print()

