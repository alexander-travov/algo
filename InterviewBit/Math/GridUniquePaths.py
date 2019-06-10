# -*- coding: utf8 -*-
"""
Grid Unique Paths
=================

A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)


Solution
--------

Problem can be solved with dynamic programming in O(n*m) time, O(min(n,m)) extra space.

a[i][0] = a[0][j] = 1
a[i][j] = a[i-1][j] + a[i][j-1]

1 1 1 1  1 1
1 2 3 4  5 6
1 3 6 10
1 4 10
1 5        ? - a[n][m]

Or one can notice that k'th diagonal of a grid forms a row from Pascal's triangle
so a[n][m] which is on (n+m-2)'th diagonal is C(n+m-2, m-1) and calculate that in O(min(n,m)) and O(1) extra space.
"""

from __future__ import print_function


def C(n, m):
    res = 1
    m = min(m, n-m)
    for i in range(n-m+1, n+1):
        res *= i
    for i in range(1, m+1):
        res //= i
    return res


def num_paths(n, m):
    return C(n+m-2, m-1)


print(num_paths(6, 4))
