"""
Matrix Search
=============

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return 1 (1 corresponds to true)

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

Solution
--------

In C/C++ we can just cast a pointer:
int A[n][m];
int * p = A
and binsearch in p array of size N*M

if Python idea is the same, but we need to calculate the indices in the original array.

Time complexity: O(log(n*m))
"""

from __future__ import print_function


def mat_search(mat, x):
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = n*m - 1

    while low <= high:
        mid = low + (high-low)//2
        i, j = divmod(mid, m)
        val = mat[i][j]
        if val == x:
            return 1
        elif val < x:
            low = mid + 1
        else:
            high = mid - 1

    return 0


mat = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(mat_search(mat, 51))
