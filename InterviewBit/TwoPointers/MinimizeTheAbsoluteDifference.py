"""
Minimize the absolute difference
================================

Given three sorted arrays A, B and C of not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number
from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
"""

from __future__ import print_function
import sys


def _find_min_diff(A, B, C):
    """
    Finds min abs difference for (a, b, c) where a is the least from the three.
    """
    i = j = k = 0
    diff = sys.maxsize

    while i<len(A) and j<len(B) and k<len(C):
        if B[j] < A[i]:
            j += 1
        elif C[k] < A[i]:
            k += 1
        else:
            diff = min(diff, max(B[j], C[k]) - A[i])
            i += 1

    return diff


def find_min_diff(A, B, C):
    return min([
        _find_min_diff(A, B, C),
        _find_min_diff(B, A, C),
        _find_min_diff(C, A, B)
    ])


A = [ 1, 4, 5, 8, 10]
B = [ 6, 9, 15]
C = [ 2, 3, 6, 6]


print(find_min_diff(A, B, C))
