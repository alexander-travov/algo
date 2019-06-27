"""
Min Jumps Array
===============

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example :
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

If it is not possible to reach the end index, return -1.
"""

from __future__ import print_function


def min_jumps(arr):
    num_jumps = [-1] * len(arr)
    num_jumps[0] = 0

    for i, max_jump in enumerate(arr):
        if num_jumps[i] == -1:
            continue

        for jump in range(1, max_jump+1):
            if i+jump >= len(arr):
                continue
            cur_num = num_jumps[i+jump]
            if cur_num == -1 or cur_num > num_jumps[i]+1:
                num_jumps[i+jump] = num_jumps[i]+1

    return num_jumps[-1]


print(min_jumps([1, 2, 1, 1, 4]))
