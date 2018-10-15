"""Demonstrates how operators and expressions work in Python.
"""


# Demonstrate arithmetic operators (function demonstrate_arithmetic_operators())


def demonstrate_arithmetic_operators():
    a = ((7 // 3) ** 3) % 5 - 11
    print('Result:', a)


# Demonstrate relational operators (function demonstrate_relational_operators())
# - simple comparisons
# - comparing dates (== vs. is)
# - timedelta()
# - None in comparisons, type(None)


def demonstrate_relational_operators():
    if 1 > 3:
        print("1 > 3")
    else:
        print("1 <= 3")
    print()
    if 13:
        print(True)
    else:
        print(False)
    print()

    from datetime import date, timedelta
    d1 = date.today()
    print(d1)
    d2 = date(1978, 3, 2)
    if d1 > d2:
        print("Today is greater than 1978-03-02")
    else:
        print("Today is less than 1978-03-02")
    print()

    d3 = d1 - timedelta(1)
    print(d3)
    print()

    # d3 = d1
    d3 = date.today()
    if d3 == d1:
        print("d3 == d1")
    else:
        print("d3 != d1")
    if d3 is d1:
        print("d3 is d1")
    else:
        print("d3 is not d1")
    print()

    if None:
        print(True)
    else:
        print(False)
    print()


# Demonstrate logical operators (function demonstrate_logical_operators())
# - logical operations with True and False
# - logical operations with dates
# - logical operations with None (incl. None and int, None and date, etc.)
# - None and date vs. None > date


def demonstrate_logical_operators():
    if 13 and None:
        print(True)
    else:
        print(False)
    print()

    from datetime import date, timedelta
    d1 = date.today()
    print(d1 or False)
    print(d1 and False)
    # print(d1 > False)
    print()


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()

    # demonstrate_relational_operators()

    demonstrate_logical_operators()

