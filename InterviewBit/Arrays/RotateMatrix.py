"""
Rotate Matrix
=============

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""

from __future__ import print_function


def rotate(a):
    n = len(a)

    max_col = max_row = n // 2
    if n % 2:
        max_row += 1

    for i in range(max_row):
        for j in range(max_col):
            tmp = a[i][j]
            a[i][j] = a[n-1-j][i]
            a[n-1-j][i] = a[n-1-i][n-1-j]
            a[n-1-i][n-1-j] = a[j][n-1-i]
            a[j][n-1-i] = tmp

    return a


for r in rotate([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]):
    print(r)
