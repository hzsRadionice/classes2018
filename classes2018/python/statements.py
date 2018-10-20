"""Demonstrates peculiarities of if, for, while and other statements
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    authors1 = ["Bruce Springsteen", "Patti Smith"]
    authors2 = ["Bruce Springsteen", "Patti Smith"]
    if authors1 == authors2:
        print("authors1 == authors2")
    else:
        print("authors1 != authors2")
    if authors1 is authors2:
        print("authors1 is authors2")
    else:
        print("authors1 is not authors2")
    print()

    author1 = "Bruce Springsteen"
    author2 = "Bruce Springsteen"
    print(author1 is author2)
    print(authors1 is authors2)
    print()

    print(True) if authors1 else print(False)
    print(True) if 0 else print(False)
    print(True) if None else print(False)
    print()

    if "Eric Clapton" in authors1:
        print("Eric Clapton is in authors1")
    elif "Patti Smith" in authors1:
        print("Patti Smith is in authors1")
    elif "Bruce Springsteen" in authors1:
        print("Bruce Springsteen is in authors1")
    else:
        print(None)
    print()


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    because_the_night = {
        'author1': 'Bruce Springsteen',
        'author2': 'Patti Smith',
        'album1': 'Easter',
        'album2': 'Promise',
    }
    for i in range(0, 2):
        print(list(because_the_night.items())[i])
    print()

    for i in range(-1, -4, -1):
        print(list(because_the_night.items())[i])
    print()

    for _ in range(1, 5):
        print("Because the Night")
    print()

    for k, v in because_the_night.items():
        if v == 'Easter':
            # continue
            break
        print(v)
    print()

    i = 0
    while i <= len(because_the_night) - 1:
        print(list(because_the_night.items())[i])
        i += 1


if __name__ == '__main__':

    # demonstrate_branching()
    demonstrate_loops()
