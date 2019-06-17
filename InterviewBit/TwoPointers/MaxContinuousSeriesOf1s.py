"""
Max Continuous Series of 1s
===========================

You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input : 
Array = {1 1 0 1 1 0 0 1 1 1 } 
M = 1

Output : 
[0, 1, 2, 3, 4]
"""

from __future__ import print_function


def max_1series(a, max_num_zeros):
    l = 0
    r = -1
    num_zeros = 0
    max_len = -1
    while True:
        if num_zeros <= max_num_zeros:
            max_len = max(max_len, r-l+1)
            r += 1
            if r == len(a):
                break
            elif a[r] == 0:
                num_zeros += 1
        else:
            l += 1
            if a[l-1] == 0:
                num_zeros -= 1
    return max_len


print(max_1series([0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0], 2))
