"""Domain classes and functions related to the concept of performer
"""


import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band.
    """


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    """


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    pass

