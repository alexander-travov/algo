"""
3 Sum
=====

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""

from __future__ import print_function
import sys


def two_sum(arr, target, min_ind=0):
    l = min_ind
    r = len(arr)-1
    min_diff = sys.maxsize

    while l < r:
        s = arr[l] + arr[r]
        if abs(target - s) < min_diff:
            best_indices = (l, r)
            min_diff = abs(target - s)
        if s > target:
            l += 1
        elif s < target:
            r -= 1
        else:
            break

    return min_diff, best_indices


def three_sum(arr, target):
    arr.sort()
    min_diff = sys.maxsize
    for i, el in enumerate(arr[:-2]):
        diff, (l, r) = two_sum(arr, target - el, min_ind=i+1)
        if diff < min_diff:
            best_indices = i, l, r

    return best_indices, sum(arr[i] for i in best_indices)


print(three_sum([-1, 2, 1, -4], 1))
