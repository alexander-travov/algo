"""
Max Sum Contiguous Subarray
===========================

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

Solution
--------

The obvious solution in O(N^2):

max_sum = 0 for empty subarray
for l in 0..N-2:
    sum = a[l]:
    for r in l+1..N-1:
        sum += a[r]
        if sum > max_sum:
            max_sum = sum

But the problem can be solved in linear time with DP. See Kadane's algorithm.

The idea is for each position to save
- max sum of subarrays ending exactly on this element
- max sum of subarrays up to this element

If you want to find maximum subarray, you need to keep begin and end indexes during pass.
"""

from __future__ import print_function


def find_max_subarray_sum(arr):
    sum_ending_here = 0
    sum_total = 0

    for el in arr:
        sum_ending_here = max(sum_ending_here + el, 0)
        sum_total = max(sum_total, sum_ending_here)

    return sum_total


def find_max_subarray(arr):
    # begin and end index of subarray with max sum ending on this element
    # arr[b:e]
    # if b==e then subarray is empty
    b, e = 0, 0
    sum_ending_here = 0

    # begin and end index of subarray with max sum
    # arr[mb:me]
    mb, me = 0, 0
    sum_total = 0

    for i, el in enumerate(arr):
        e = i + 1
        if sum_ending_here + el < 0:
            b = e
            sum_ending_here = 0
        else:
            sum_ending_here += el

        if sum_total < sum_ending_here:
            mb = b
            me = e
            sum_total = sum_ending_here

    return arr[mb:me], sum_total


for arr in [
        [-2,1,-3,4,-1,2,1,-5],
        [1,2,3,-2,-3,-3,4,4],
    ]:
    print(arr, find_max_subarray(arr))
