"""
Rain Water Trapped
==================

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


Solution
--------

For some amount of water to be trapped on a bar H, there need to be a higher bar on the left L and on the right R.
The amount of water trapped would be: min(L, R)-H

We can go with two pointers l, r from both ends and keep max_left, max_right variables
with max height to the left from l pointer and max height to the right from r pointer.
We decide which pointer to move by comparing at which side current maximum is less.

Time complexity O(N), space complexity O(1)
"""

from __future__ import print_function


def trapped_water(bars):
    max_left = bars[0]
    l = 0
    max_right = bars[-1]
    r = len(bars)-1
    water = 0

    while l < r:
        if max_left < max_right:
            l += 1
            if bars[l] < max_left:
                water += max_left - bars[l]
            else:
                max_left = bars[l]
        else:
            r -= 1
            if bars[r] < max_right:
                water += max_right - bars[r]
            else:
                max_right = bars[r]

    return water


print(trapped_water([0,1,0,2,1,0,1,3,2,1,2,1]))
