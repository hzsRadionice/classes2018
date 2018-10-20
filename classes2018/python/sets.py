"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    authors = {"Bruce Springsteen", "Patti Smith", "Bruce Springsteen"}
    print(authors)
    print()

    authors.add("Eric Clapton")
    singers = {"Bruce Springsteen", "Patti Smith", "Stevie Nicks", "Mick Jagger", "Brian Ferry"}
    print(authors & singers)
    print(authors | singers)
    print(authors - singers)
    print(singers - authors)
    print(singers ^ authors)
    print()


if __name__ == '__main__':

    demonstrate_sets()

