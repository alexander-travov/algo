"""
Wave Array
==========

Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

NOTE: If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]

Solution
--------

If we assume that array is initially sorted, then:
a1 <= a2 <= a3 <= a4 <= a5 ...

If we swap elements for every pair (0,1), (2,3), (4,5) ...
we get the array in desired form.

One can prove that such array is indeed the lexicographically smallest.

Time complexity O(NlogN) if array in unsorted, O(N) if it is initially sorted.
"""

from __future__ import print_function


def wave(arr):
    arr.sort()
    N = len(arr)
    i = 0
    while i < N-1:
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
        i += 2
    return arr


print(wave([1, 2, 3, 4]))
print(wave([1, 2, 3, 5, 4]))
