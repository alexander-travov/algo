"""
Largest Continuous Sequence Zero Sum
====================================

Find the largest continuous sequence in a array which sums to zero.

Example:

Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

Solution
--------

Use hashtable for prefix sums.
If you encounter same prefix sum twice the subarray between two prefixes sums to zero.

Time complexity O(N), space complexity O(N).
"""

from __future__ import print_function


def find_largest_zero_sum(arr):
    sums = {0: -1}
    max_len = 0
    start = 0
    s = 0
    for i, el in enumerate(arr):
        s += el
        if s in sums:
            cur_len = i-sums[s]
            if cur_len > max_len:
                max_len = cur_len
                start = sums[s]+1
        else:
            sums[s] = i

    return arr[start:start+max_len]


print(find_largest_zero_sum([0, 2, 1, -1, -2, -3]))
