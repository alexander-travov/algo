"""
Search for a Range
==================

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].


Solution
--------

Use binsearch to find the first and the last occurence of x.
Time complexity O(log(N))
"""

from __future__ import print_function


def first_occurence(a, x):
    l = 0
    r = len(a)-1
    res = -1

    while l <= r:
        m = l + (r-l)//2
        if a[m] == x:
            res = m
        if a[m] >= x:
            r = m-1
        else:
            l = m+1
    return res


def last_occurence(a, x):
    l = 0
    r = len(a)-1
    res = -1

    while l <= r:
        m = l + (r-l)//2
        if a[m] == x:
            res = m
        if a[m] <= x:
            l = m+1
        else:
            r = m-1
    return res


def search_range(a, x):
    first = first_occurence(a, x)
    if first == -1:
        return -1
    last = last_occurence(a, x)
    return (first, last)


print(search_range([5, 7, 7, 8, 8, 10], 7))
