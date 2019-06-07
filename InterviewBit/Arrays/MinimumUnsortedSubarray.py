# -*- coding: utf-8 -*-
"""
Minimum Unsorted Subarray
=========================
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.
"""

from __future__ import print_function


def max_unsorted_subarray(a):
    # find first disorder from the left
    n = len(a)
    for l in range(n-1):
        if a[l+1] < a[l]:
            break
    else:
        return -1

    # find first disorder from the right
    for r in range(n-1, 0, -1):
        if a[r-1] > a[r]:
            break

    sub_min = min(a[l:r+1])
    sub_max = max(a[l:r+1])

    while l >= 1:
        if a[l-1] <= sub_min:
            break
        l -= 1

    while r < n-1:
        if a[r+1] >= sub_max:
            break
        r += 1

    return l, r, a[l:r+1]


arr = [0,1,3,2,5,4,6,7]
print(arr, max_unsorted_subarray(arr))
