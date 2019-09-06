"""
Smallest Multiple With 0 and 1
==============================

You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only. Since this multiple could be large, return it in form of a string.

Note:

Returned string should not contain leading zeroes.
For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
"""

from __future__ import print_function


def smallest_multiple(n):
    i = 1
    while True:
        m = int(bin(i)[2:])
        if m % n == 0:
            return m
        i += 1


print(smallest_multiple(557))
