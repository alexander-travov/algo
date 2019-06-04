# -*- coding: utf-8 -*-
"""
Maximum Absolute Difference
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

Solution
--------

The obvious quadratic solution would be to find all values of f(i,j) above the diagonal (i<j).

If we open the absolute values, we get one of 4 expressions:
1. i>=j and A(i)>=A(j) then f(i,j) = (A(i)+i) - (A(j)+j)
2. i>=j and A(i)<A(j)  then f(i,j) = (A(j)-j) - (A(i)-i)
3. i<j  and A(i)>=A(j) then f(i,j) = (A(i)-i) - (A(j)-j)
4. i<j  and A(i)<A(j)  then f(i,j) = (A(j)+j) - (A(i)+i)

If we find min and max for arrays [A(i)+i] and [A(i)-i]
then bigger difference max-min of two would give the answer.

The complexity of this solution is O(N).
"""

from __future__ import print_function


def find_max_abs_diff(arr):
    # a(i)+i
    for i in range(len(arr)):
        arr[i] += i
    res1 = max(arr) - min(arr)

    # a(i)-i
    for i in range(len(arr)):
        arr[i] -= 2*i
    res2 = max(arr) - min(arr)

    return max(res1, res2)


for arr in [
        [1, 3, -1],
        [-70, -64, -6, -56, 64, 61, -57, 16, 48, -98],
    ]:
    print(arr, find_max_abs_diff(arr))
