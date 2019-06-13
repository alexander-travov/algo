"""
Number of 1 Bits
================

Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.
"""

from __future__ import print_function


def num_bits(n):
    # Time complexity: O(num 1 bits)
    # One can use popcnt instruction too.
    c = 0
    while n:
        n &= n-1
        c += 1
    return c


n = 111
print(n, bin(n), num_bits(111))
