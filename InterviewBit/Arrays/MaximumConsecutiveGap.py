"""
Maximum Consecutive Gap
=======================

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

    Input : [1, 10, 5]
    Output : 5 


Solution
--------

The constraints of the problem can be met with sorting an array with radix sort, but there exists more elegant solution.

1. Find min and max of an array
2. If we divide segment [min; max] in N+1 equal parts:
d = (max-min)/(N+1), [min+i*d; min+d*(i+1)] for i in 0..N,
then according to the Dirichlet's principle at least on of the inner segments
would contain no point from the array. Therefore maximum gap can not be shorter than d.
Thus difference between two points from the same segment the can not be the greatest.
It can happen only between points from different segments.

Consecutive gaps are formed between max elem of the segment and min elem of the next nonempty segment.

If we keep arrays of segment mins and maxs we solve the problem in linear time, linear space.
"""

from __future__ import print_function


def max_gap(arr):
    n = len(arr)
    if n == 1:
        return 0
    arr_min = min(arr)
    arr_max = max(arr)
    d = (arr_max - arr_min)/(n+1.)

    # arr_max+1, arr_min-1 are used for empty buckets
    # We could use None or MAX_INT, MIN_INT instead
    mins = [arr_max+1]*(n+1)
    maxs = [arr_min-1]*(n+1)

    for el in arr:
        index = int((el-arr_min)/d)
        # max elem goes into last bucket
        if el == arr_max:
            index = n
        mins[index] = min(mins[index], el)
        maxs[index] = max(maxs[index], el)

    # skip empty segments
    mins = [m for m in mins if m != arr_max+1]
    maxs = [m for m in maxs if m != arr_min-1]

    gap = 0
    for i in range(len(mins)-1):
        gap = max(gap, mins[i+1] - maxs[i])

    return gap


print(max_gap([1, 10, 5, 7, 4]))
