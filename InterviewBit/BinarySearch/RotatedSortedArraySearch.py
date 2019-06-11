"""
Rotated Sorted Array Search
===========================

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

Solution
--------

First we binsearch for the pivot point, that breaks array increase.
Than we binsearch x in one of the parts.

Time complexity O(log(N))
"""

from __future__ import print_function


def pivot(a):
    # Works only in circularly sorted arrays without duplicates.
    n = len(a)
    low = 0
    high = n-1

    while low <= high:
        if a[low] < a[high]:
            return low

        mid = low + (high-low)//2
        prev = (mid-1) % n

        if a[mid] < a[prev]:
            return mid

        if a[mid] > a[low]:
            low = mid+1
        else:
            high = mid-1


def bin_search(a, x, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return -1


def rot_search(a, x):
    p = pivot(a)
    if x >= a[0]:
        return bin_search(a, x, 0, p-1)
    else:
        return bin_search(a, x, p, len(a)-1)


print(rot_search([4, 5, 6, 7, 0, 1, 2], 5))
