"""Demonstrates working with strings in Python.
"""

import string


def demonstrate_formatting():
    """Using classical formatting.
    - classical format strings (e.g., "%7.3f, %5s")
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print("%7.3f, %5s" % (7/3, 'eee'))
    print('C:\nowhere')
    print(r'C:\nowhere')
    print("""Album: Easter
                songs
                    Till Victory
                    Ghost Dance
                    Because the Night
                    ...
    """)
    print("Patti Smith    " * 3)
    patti = "Patti Smith"
    print(patti[0])
    print(patti[-1])
    print(patti[0:5])
    print(patti[-5:])
    print()

    print(string.whitespace)
    print(str(string.whitespace))
    print(repr(string.whitespace))


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{0}: {1} ({2})'.format("Patti Smith Group", "Because the Night", 1978))
    print('{}: {} ({})'.format("Patti Smith Group", "Because the Night", 1978))
    print('{2}: {0} ({1})'.format("Patti Smith Group", "Because the Night", 1978))


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...)
    """

    patti = "Patti Smith"
    print(patti.endswith('Smith'))
    print(patti.split())
    print(patti.center(20, '#'))
    print('Patti' in patti)
    print('Patti Smith' == patti)
    print('Patti Smith' is patti)


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    demonstrate_string_operations()
