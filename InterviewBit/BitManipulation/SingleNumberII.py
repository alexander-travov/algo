"""
Single Number II
================

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Solution
--------

For every bit we can implement three-state xor with 2 bits of memory or a counter.
00 -> 01 -> 10 -> 11 -> 00
Time complexity O(N), extra space O(1).
"""

from __future__ import print_function


def xor3sum(arr):
    count = [0] * 32

    for el in arr:
        for i in range(32):
            if el & (1<<i):
                count[i] = (count[i] + 1) % 3

    n = 0
    for i in range(32):
        n += (1<<i) * count[i]

    return n


print(xor3sum([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
