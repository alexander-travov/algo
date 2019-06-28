# -*- coding: utf8 -*-
"""
Intersecting Chords in a Circle
===============================

Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.

For example,

N=2
If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
{(1-2), (3-4)} and {(1-4), (2-3)}

So, we return 2.
Notes:

1 ≤ N ≤ 1000
Return answer modulo 10^9+7.

Solution
--------

Numbers form Catalan's sequence

So you can use formula:
C(0)=1, C(n+1) = 2(2n+1)C(n)/(n+2)

or calculate directly with:
C(N) = C(N-1)C(0) + C(N-2)C(1) + ... + C(1)C(N-2) + C(0)C(N-1)
"""

from __future__ import print_function


def num_chords(N, M=int(10**9+7)):
    arr = [1] # nums[0]
    for n in range(1, N+1):
        num = 0
        for i in range(n):
            num = (num + arr[i]*arr[n-1-i] % M) % M
        arr.append(num)
    return arr[N]


def catalan(N):
    res = 1
    for n in range(1, N):
        res = 2*(2*n+1)*res // (n+2)
    return res


print(num_chords(11), catalan(11))
