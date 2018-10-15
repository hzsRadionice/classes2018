"""The very first module in a more structured version of the project.
"""


# Moving code from main.py

# # print("Hi.")
# # print("Because the Night")
# # print()
# # print('Because the night' + '\n' +
# #       "belongs to lovers")
# # print()
# # # print('11' + 1)
# # print('11' + str(1))
# # print('11', 1)
#
#
# def print_it():
#     print("Because the Night")
#     print()
#     print('Because the night' + '\n' +
#           "belongs to lovers")
#     print()
#
#
# print_it()


def print_it():
    """
    Function docstring
    """

    print("Because the Night")
    print()
    print('Because the night' + '\n' +
          "belongs to lovers")
    print()

    # Taking care of the module __name__

    print('__name__:', __name__)


if __name__ == '__main__':

    print_it()

    for i in range(0, 3):
        print("Because the Night")
    print()

    # Printing a list using enumerate()

    songs = [
        "Because the Night",
        'Babelogue',
        'Till Victory',
    ]
    print(songs)
    print(enumerate(songs))
    print(list(enumerate(songs)))
    print()
    for i in list(enumerate(songs)):
        print(i)
    print()
    for i, s in list(enumerate(songs)):
        print(i, s)
    print()

    print('__name__:', __name__)
    print()

    for i in range(1, 5):
        print(i, "Because the Night")       # no ' ' before 'B', it is now inserted automatically
    print()

    # Printing with ' ' and printing without '\n'

    print('Because ', end='')               # end='...' avoids the newline after the output
    print("the Night")
    print()

    # Printing with classical formatting (%)

    print('%6.2f, %5d' % (4/3, 2))
    print()

    # Keyboard input

    title = 'Because the Night'
    a = input('Enter the year of release of ' + title + ': ')
    print(title, 'was first released in', a)
    print()

    # Printing docstrings

    print(print_it.__doc__)                 # demonstrate printing docstrings
    print()
    print(__doc__)
    print()
