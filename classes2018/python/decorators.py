"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions and user-defined decorators
"""


import functools


def return_none():
    """Demonstrates returning None and the pass statement.
    """

    # a = 1
    # return a

    pass


def pass_function_as_parameter(f, *args):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    """

    f(*args)


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """

    def get_first_name():
        return full_name.split()[0]

    def get_family_name():
        return full_name.split()[1]

    if first_name_flag:
        return get_first_name
    else:
        return get_family_name


def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list or args, or...)
    """

    def empty_list():
        return []

    def tuple_of_args(*parameters):
        return tuple(parameters)

    return tuple_of_args if len(args) else empty_list


def show_author(artwork_f):
    """Demonstrates how to develop a decorator. Uses the decorator-writing pattern:
    import functools
    def decorator(func):
        @functools.wraps(func)			                # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    """

    def wrapper_show_author(*args, **kwargs):

        # Do something before
        authors = list(args)
        del authors[0]                                  # assume the first arg is the song title
        print(', '.join(author for author in authors) + ': ', end='')

        v = artwork_f(*args, **kwargs)

        # Do something after
        print(':)')

        return v

    return wrapper_show_author


@show_author
def print_song(title, *authors):
    """The corresponding decorator (@show_author); omit it if decorating manually.
    """

    print(title)


if __name__ == '__main__':

    from classes2018.python import functions

    print(return_none())
    print()

    pass_function_as_parameter(return_none)
    pass_function_as_parameter(functions.demonstrate_annotations, "Patti Smith", "Frederick")
    print()

    # print(return_function("Patti Smith", True)())
    print(return_function("Patti Smith", 0)())
    print()

    f = return_function_with_args("Patti")
    print(f("Smith", False, 11, 12))
    f = return_function_with_args("Patti", True)
    print(f())
    return_function_with_args = return_function_with_args("Patti", True)    # a wild thought :)
    print(return_function_with_args("Smith", False, 11, 12))                # but it's just a step away from decorators
    print()

    # print_song("Because the Night", "Bruce Springsteen", "Patti Smith")
    # print_song = show_author(print_song)                                    # decorate manually
    # print_song("Because the Night", "Bruce Springsteen", "Patti Smith")
    print_song("Because the Night", "Bruce Springsteen", "Patti Smith")


