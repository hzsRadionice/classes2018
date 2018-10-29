"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(artist: str, song: str = 'Because the Night') -> str:
    # """
    # Demonstrates annotations.
    # :param artist: an artist (string)
    # :param song: a song (string)
    # :return: string
    # """
    # print(demonstrate_annotations.__doc__)
    """Demonstrates how to use annotations of function parameters/arguments and of function return type.
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - return a formatted string (including function parameters/arguments)
    """
    print('Parameters/Arguments:', 'artist:', artist + ',', 'song:', song)
    print('Annotations:', demonstrate_annotations.__annotations__)
    return 'Returned: {}, {}'.format(artist, song)


def show_song(artist, song='Because the Night', duration=180):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """
    print('{}: {} ({})'.format(artist, song, duration))


def use_flexible_arg_list(prompt: str, *songs):
    """Demonstrates flexible number of arguments/parameters.
    - print the prompt and the list of songs in one line
    """
    # print(songs)
    # print(type(songs))
    print(*songs)                                                           # unpack tuple (no commas printed)
    print('{}: {}'.format(prompt, [song for song in songs]))
    print('{}: {}'.format(prompt, *songs))                                  # prints only the first song!

    print(prompt, end=': ')
    # for song in songs:
    #     print(song, end=', ')
    # print('...')
    print(', '.join(song for song in songs), end='')
    print('...')


def use_all_categories_of_args(prompt, *albums, song='Because the Night', **authors):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """
    print(prompt, song, end='')
    if albums or authors:
        print(' - ', end='')
    else:
        print()
    if albums:
        print('album(s):', ', '.join(album for album in albums), end='')
    if authors:
        # print('; authors:', ', '.join(v for _, v in authors.items()))
        print('; author(s):', ', '.join(v for v in authors.values()))
    else:
        print()                                                             # just print '\n' if no author is specified


if __name__ == "__main__":

    print(demonstrate_annotations("Bruce Springsteen"))
    # print(demonstrate_annotations(1))
    print()

    show_song("Patti Smith")
    show_song("Bruce Springsteen", "Darkness on the Edge of Town")
    print()

    use_flexible_arg_list("Songs", "Because the Night", "You and I", "Brilliant Disguise")
    print()

    # albums = ["Easter", "Promise"]
    # authors = {'1': 'Bruce Springsteen', '2': 'Patti Smith'}
    albums = ["Easter"]
    authors = {}
    use_all_categories_of_args('The song', "Easter", "Promise",
                               song='Because the Night',
                               a1='Bruce Springsteen', a2='Patti Smith')
    use_all_categories_of_args('The song', *albums,
                               song='Because the Night',
                               **authors)                               # unpack albums and authors
    use_all_categories_of_args('The song', "Easter", "Promise",
                               song='Because the Night',
                               **authors)
    print()


