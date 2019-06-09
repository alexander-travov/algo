"""
Rearrange Array
===============
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]

Lets say N = size of the array. Then, following holds true:
All elements in the array are in the range [0, N-1]
N*N does not overflow for a signed integer

Solution
--------

As N*N does not overflow for a signed integer we can effectively save two arrays
of numbers 0..N-1 in one array
arr1 = [a1, a2, ...]
arr2 = [b2, b2, ...]

arr = [a1*n+b1, a2*n+b2, ...]
With this trick arr1[i] = arr[i]/n and arr2[i] = arr[i]%n
"""

from __future__ import print_function


def rearrange(a):
    n = len(a)

    for i, el in enumerate(a):
        a[i] = n * (a[el] % n) + el

    for i, el in enumerate(a):
        a[i] = el // n

    return a


print(rearrange([0, 2, 3, 1]))
