"""
Divide Integers
===============

Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
"""

from __future__ import print_function


def bit_divmod(a, b):
    n = 0
    while a > b:
        n += 1
        b <<= 1

    res = 0
    while n >= 0:
        if a >= b:
            a -= b
            res += 1<<n
        b >>= 1
        n -= 1
    return res, a


print(bit_divmod(500, 13))
