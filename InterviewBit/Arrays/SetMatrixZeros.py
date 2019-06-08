"""
Set Matrix Zeros
================

Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1

On returning, the array A should be :

0 0 0
1 0 1
1 0 1

Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.


Solution
--------

Problem can be solved with in O(m*n) time with O(1) additional space.

1) We scan first row. If it is all ones, we save first_row_all_ones=True flag
2) We repeat the same for the first column -> first_col_all_ones=True flag

3) After that we can use first row and column as arrays of flags, whether corresponding row or column should be zeroed out
according to the content of the remaining part of the matrix.

4) Then we zero rows and columns from the second according to the flags in first row and column.

5) Last step is zeroing first row and column according to the first_row_all_ones, first_col_all_ones flags.
"""

from __future__ import print_function


def zero(a):
    m = len(a)
    n = len(a[0])

    first_row_all_ones = all(a[0])
    first_col_all_ones = all(a[i][0] for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if not a[i][j]:
                a[0][j] = 0
                a[i][0] = 0

    for i in range(1, m):
        if not a[i][0]:
            for j in range(1, n):
                a[i][j] = 0

    for j in range(1, n):
        if not a[0][j]:
            for i in range(1, m):
                a[i][j] = 0

    if not first_row_all_ones:
        for j in range(n):
            a[0][j] = 0

    if not first_col_all_ones:
        for i in range(m):
            a[i][0] = 0

    return a


print(zero([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1]
]))
