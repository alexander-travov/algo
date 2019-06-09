# -*- coding: utf-8 -*-
"""
Next Permutation
================

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
"""

from __future__ import print_function


def swap(l, i, j):
    """
    Swap list elements
    """
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp


def next_perm(p):
    """
    Generates next permutation in O(N) time in place.
    """
    n = len(p) - 1

    # Find the first element from the end that breaks increase.
    while n > 0:
        if p[n-1] < p[n]:
            break
        n -= 1

    p[n:] = reversed(p[n:])

    if n == 0:
        # All numbers in permutation form a decreasing sequence.
        # This is last permutation.
        # After reversion we have the first permutation
        return p

    # Otherwise we should bring to the n-1 position the next bigger element
    for i in range(n, len(p)):
        if p[i] > p[n-1]:
            swap(p, i, n-1)
            break

    return p


l = [1, 2, 3, 4]
for _ in range(25):
    print(l)
    l = next_perm(l)
