"""Demonstrates dictionaries
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - using the keys() and values() functions
    """

    songs = {}
    # songs = dict()
    print(songs)
    songs[1] = 'Because the Night'
    print(songs)
    print()

    songs = {
        1: 'Because the Night',
        2: 'Space Monkey',
        3: '25th Floor',
    }
    print(songs)
    print(songs.items())
    print(list(songs.items()))
    for k, v in songs.items():
        print(k, v)
    print()

    from pprint import pprint
    pprint(songs, width=1)
    print()

    del(songs[2])
    print(songs)
    print()

    print(songs.keys())
    print(songs.values())
    print(type(songs.keys()))
    # pprint(songs.keys())
    # pprint(songs.values())
    # pprint(list(songs.keys()), width=1)
    # pprint(list(songs.keys()), width=1)
    print()


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k':
    #     d_sorted = sorted(zip(d.keys(), d.values()))
    # elif by == 'v':
    #     d_sorted = sorted(zip(d.values(), d.keys()))
    # else:
    #     return None
    # # return d_sorted                                         # d_sorted is a list
    # return dict(d_sorted)

    # from operator import itemgetter
    # if by == 'k':
    #     d_sorted = sorted(d.items(), key=itemgetter(0))
    # elif by == 'v':
    #     d_sorted = sorted(d.items(), key=itemgetter(1))
    # else:
    #     return None
    # # return d_sorted                                         # d_sorted is a list
    # return dict(d_sorted)

    if by == 'k':
        d_sorted = sorted(d.items(), key=lambda i: i[0])
    elif by == 'v':
        d_sorted = sorted(d.items(), key=lambda i: i[1])
    else:
        return None
    # return d_sorted                                         # d_sorted is a list
    return dict(d_sorted)


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    because_the_night = {
        'author1': 'Bruce Springsteen',
        'author2': 'Patti Smith',
        'album1': 'Easter',
        'album2': 'Promise',
    }

    print(because_the_night.items())
    print()

    print(sort_dictionary(because_the_night, 'k'))
    print(sort_dictionary(because_the_night, 'v'))
    print(sort_dictionary(because_the_night, 33))


if __name__ == '__main__':

    # demonstrate_dictionaries()
    demonstrate_dict_sorting()
