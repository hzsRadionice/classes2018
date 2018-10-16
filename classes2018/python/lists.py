"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    l1 = ["Because the Night", "Patti Smith", 1978, True]
    print(l1)
    print(l1[0])
    print(l1[-2:])
    print()

    l2 = ["Because the Night", "Patti Smith", 1978, True]
    print(l1 == l2)
    print(l1 is l2)
    print('id(l1):', id(l1), ', id(l2):', id(l2))
    # print('id(l1):', id(l1), end='')
    # print(', id(l2):', id(l2))
    print()

    l3 = l1 + l2
    print(l3)
    print(l3.append("Bruce Springsteen"))
    print(l3)
    print()

    for e in l3:
        print('\t', e)


def demonstrate_list_methods():
    """Using append(), insert(), remove(), pop(), extend(),
    count(), index(), reverse(), len(),...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    l1 = ["Because the Night", "Patti Smith", 1978, True]
    l1.append("Bruce Springsteen")
    print(l1)
    print()

    l1.insert(2, "Easter")
    print(l1)
    print()

    easter = l1.pop(2)
    print('Popped:', easter)
    print('l1:', l1)
    print()

    l1.append(["25th Floor"])
    print(l1)
    l1.remove(["25th Floor"])
    print(l1)
    l1.extend(["25th Floor"])
    print(l1)
    l1.remove(l1[len(l1) - 1])
    print(l1)
    print()

    print(l1.index("Bruce Springsteen"))
    # l1_reversed = l1.reverse()
    # print(l1_reversed)
    l1.reverse()
    print(l1)
    l1.append("Patti Smith")
    print(l1)
    print(l1.count("Patti Smith"))
    print()


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [12, 45, 67])
    print(a)
    for e in a:
        print(e)
    l = [1, 2, 3]
    print(type(l))
    print()


def populate_empty_list():
    """Creating an empty list and populating it with random values."""

    import random
    l = []
    random.seed(345)
    for i in range(1, 1000):
        l.append(random.randint(1, 1000))
    print(l[0:10])
    print()


def duplicate_list():
    """Duplicating lists (carefully :))"""

    l1 = ["Because the Night", "Patti Smith", 1978, True]
    l2 = l1                                                 # no, it only copies references
    l2 = l1.copy()
    l3 = l1 + []
    l4 = l1[:]

    all = [l1, l2, l3, l4]
    for l in all:
        print(str(id(l)) + ':', l)


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [12, 45, 67])
    print(a)
    b = [e for e in a]
    print(b)
    b = [str(e) for e in a]
    print(b)
    print(''.join(b))
    print()

    songs = ['Because the Night', 'Till Victory', '25th Floor']
    first_words = [title.split()[0] for title in songs]
    print(' '.join(first_words))
    print()


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()
