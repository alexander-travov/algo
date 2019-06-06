"""
Max Distance
============

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
"""

from __future__ import print_function


def find_max_distance(a):
    # Find the array of min values for elems lefter than ith
    lm = a[0]
    lmin = []
    for el in a:
        lm = min(lm, el)
        lmin.append(lm)

    # Find the array of max values for elems righter than ith
    rm = a[-1]
    rmax = []
    for el in reversed(a):
        rm = max(rm, el)
        rmax.append(rm)
    rmax.reverse()
    # print(lmin, rmax)

    max_dist = -1
    r = 0
    N = len(a)
    for l in range(N):
        while r < N:
            if rmax[r] >= lmin[l]:
                max_dist = max(max_dist, r-l)
            if rmax[r] < lmin[l]:
                break
            # print(l, r, max_dist)
            r += 1
    return max_dist


print(find_max_distance([3,5,4,2]))
