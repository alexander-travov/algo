# -*- coding: utf-8 -*-
"""
Kth Row of Pascal's Triangle
============================

Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]

Solution
--------

Given C(k+1,n)/C(k,n) = (n-k)/(k+1) we create a generator for Pascal's triangle row coefficients.
"""

from __future__ import print_function
import sys


def pascal(k):
    c = 1
    yield 1
    for i in range(k):
        c = c * (k-i) / (i+1)
        yield c


k = int(sys.argv[1] if len(sys.argv) > 1 else 3)
print(list(pascal(k)))
