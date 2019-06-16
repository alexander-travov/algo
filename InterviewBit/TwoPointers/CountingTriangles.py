# -*- coding: utf8 -*-
"""
Counting Triangles
==================

You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 10^9 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4

Solution
--------

If lengths a, b, c form a triangle, they adhere to triangle's inequalities:
a < b+c, b < a+c, c < a+b
If a, b, c are sorted we only need to check that c < a+b. Two other inequalities would be fulfilled.

1. Sort A
2. Fix lasgest length c. For all b's less than c, find minimal a, so that c<a+b. Increment sum.
We can do that in linear time with two pointers, one from the beginning, one from the end.

Time complexity O(n^2), Space complexity O(1)
"""

from __future__ import print_function


def count_triangles(A):
    A.sort()
    res = 0
    for k in range(len(A)-1, 1, -1):
        j = k-1
        i = 0
        while i < j:
            while A[k] >= A[i]+A[j]:
                i += 1
            res = (res + max(j-i, 0)) % 1000000007
            j -= 1
    return res


print(count_triangles([1, 1, 1, 1, 2, 2, 2, 3]))
