# -*- coding: utf8 -*-
"""
4 Sum
=====

Given an array S of n integers, are there elements a, b, c, and d in S
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
"""

from __future__ import print_function
from collections import defaultdict


def find_4_sum(arr, target):
    arr.sort()
    pair_sums = defaultdict(list)
    n = len(arr)
    for i in range(n-1):
        el = arr[i]
        for j in range(i+1, n):
            el2 = arr[j]
            pair = (min(el, el2), max(el, el2))
            if not pair in pair_sums[el + el2]:
                pair_sums[el + el2].append(pair)

    for s, pairs in pair_sums.items():
        complement_pairs = pair_sums[target - s]
        for c, d in complement_pairs:
            for a, b in pairs:
                if a <= b <= c <= d:
                    yield (a, b, c, d)


for quadruple in find_4_sum([1, 0, -1, 0, -2, 2], 0):
    print(quadruple)
