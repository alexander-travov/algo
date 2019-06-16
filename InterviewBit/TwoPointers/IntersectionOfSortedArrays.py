"""
Intersection Of Sorted Arrays
=============================

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
"""

from __future__ import print_function


def intersect(a, b):
    m = len(a)
    n = len(b)

    res = []
    i = j = 0
    while i<m and j<n:
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return res


print(intersect([1, 2, 3, 3, 5, 6], [3, 4, 5, 7]))
