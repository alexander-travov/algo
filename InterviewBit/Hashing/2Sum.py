"""
2 Sum
=====

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2.
Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ).
Note that, if no pair exists, return empty list.
If multiple solutions exist, output the one where index2 is minimum.
If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2

Note: Diffk II problem is solved with the same trick.
"""

from __future__ import print_function
import sys


def find_2_sum(arr, target):
    # First positions of numbers in array.
    positions = {}
    for i, el in enumerate(arr):
        if el not in positions:
            positions[el] = i

    min_i1 = min_i2 = sys.maxsize
    for el, i1 in positions.items():
        i2 = positions.get(target - el, -1)
        if i2 != -1 and i1 < i2 and i2 < min_i2:
            min_i1 = i1
            min_i2 = i2

    return (min_i1, min_i2)


print(find_2_sum([2, 7, 11, 15], 9))
