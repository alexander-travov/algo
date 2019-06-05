"""
Largest Number
==============

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Solution
--------

We should sort numbers in decreasing order, but the sort function if tricky:
5 > 30
3 > 30
34 > 30
"""

from __future__ import print_function
from itertools import cycle, islice


def cycled_digits(s, n):
    return "".join(islice(cycle(s), n))


def largest_number(l):
    l = [str(n) for n in l]
    max_len = max(len(s) for s in l)

    l.sort(
        key=lambda s: cycled_digits(s, max_len),
        reverse=True
    )
    return "".join(l)


print(largest_number([3, 30, 34, 5, 9]))
