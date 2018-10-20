"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    t1 = ('Because the Night', )
    t2 = ('Because the Night', 'Space Monkey')
    t4 = ('Because the Night', 'Space Monkey', 12, True)
    print(t1, '\n',
          t2, '\n',
          t4, '\n', )
    print(t4[2])

    # print(id(t1))
    # t1 = t1 + t2
    # print(t1)
    # print(id(t1))
    # print()
    #
    # l1 = [12]
    # print(id(l1))
    # l1.append(13)
    # print(id(l1))

    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    t1 = ("Bruce", "Patti", "Because the Night")
    t2 = ("Springsteen", "Smith", 1978)
    # t2 = ("Springsteen", "Smith", 1978, True)
    z = zip(t1, t2)
    print(z)
    for i, j in z:
        print(i, j)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    t1 = "Bruce", "Patti", "Because the Night"
    print(t1)
    bruce, patti, because_the_night = t1
    print(bruce, patti, because_the_night)

    print()


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_zip()
    demonstrate_packing()

