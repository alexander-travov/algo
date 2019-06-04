# -*- coding: utf-8 -*-
"""
Flip
====

You are given a binary string (i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN.
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N
and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.
If you don’t want to perform the operation, return an empty array.
Else, return an array consisting of two elements denoting L and R.
If there are multiple solutions, return the lexicographically smallest pair of L and R.

Solution
--------

The idea is the same as in problem MaxSumContiguousSubarray.

We end up with linear solution with modification of Kadane's algorithm.

We find the contigious subarray with maximum difference #{0}-#{1}.
"""

from __future__ import print_function
from random import randint


def find_flip(s):
    sum_ending_here = 0
    b = 0

    sum_total = 0
    mb = me = 0

    for i, bit in enumerate(s):
        if bit == '0':
            sum_ending_here += 1
        else:
            sum_ending_here -= 1
            if sum_ending_here < 0:
                b = i+1
                sum_ending_here = 0
        if sum_total < sum_ending_here:
            sum_total = sum_ending_here
            mb = b
            me = i+1

    return mb, me


def flip(s, b, e):
    bits = list(s)
    for i in range(b, e):
        bits[i] = '1' if bits[i]=='0' else '0'
    return ''.join(bits)


def random_bitstring(k):
    return ''.join(str(randint(0, 1)) for _ in range(k))


for s in (
        '111',
        '000',
        '0001001',
        random_bitstring(20),
        random_bitstring(20),
        random_bitstring(20),
    ):
    b, e = find_flip(s)
    print("Before:", s, "After:", flip(s, b, e), 'B:', b, 'E:', e)
