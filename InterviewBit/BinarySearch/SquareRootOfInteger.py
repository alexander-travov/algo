"""
Square Root of Integer
======================

Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

Solution
--------

We can use binsearch to find the last integer whose square is less that x.
Time complexity O(log(x))
"""

from __future__ import print_function


def sqrt(n):
    low = 1
    high = n

    while low <= high:
        mid = low + (high-low)//2
        if mid*mid <= n:
            res = mid
            low = mid+1
        else:
            high = mid-1
    return res


for i in range(1, 26):
    print(i, sqrt(i))
