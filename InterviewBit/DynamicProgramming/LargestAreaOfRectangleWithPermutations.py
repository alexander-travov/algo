# -*- coding: utf8 -*-
"""
Largest area of rectangle with permutations
===========================================

Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s,
find the area of the largest rectangle inside the grid such that all the cells
inside the chosen rectangle should have 1 in them. You are allowed to permutate
the columns matrix i.e. you can arrange each of the column in any order in the final grid.
Please follow the below example for more clarity.

Lets say we are given a binary grid of 3 * 3 size.

101
010
100

At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area
i.e either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix,
we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:

110
001
100

Now In this grid, first column is column 1, second column is column 3 and third column is column 2
from the original given grid. Now, we can see that if we calculate the max area rectangle,
we get max area as 1 * 2 = 2 which is bigger than the earlier case. Hence 2 will be the answer in this case.
"""

from __future__ import print_function


def find_max_rect_area(arr):
    # Input:
    # 101
    # 111
    # 100

    # 1. Calculate number of consecutive 1's in columns
    R = len(arr)
    C = len(arr[0])
    for r in range(1, R):
        for c in range(C):
            if arr[r][c]:
                arr[r][c] = arr[r-1][c] + 1
    # 101
    # 212
    # 300

    # 2. Sort rows. Here counting sort can be used.
    for r in range(R):
        arr[r].sort()
    # 110
    # 221
    # 300

    # Find max area
    max_area = 0
    for r in range(R):
        for c in range(C):
            max_area = max(max_area, c*arr[r][c])
    return max_area


print(find_max_rect_area([
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
]))
