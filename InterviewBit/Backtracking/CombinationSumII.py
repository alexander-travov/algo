# -*- coding: utf8 -*-
"""
Combination Sum II
==================

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""

from __future__ import print_function


def sum_combinations(candidates, target):
    if target == 0:
        yield []
    elif target < 0 or not candidates:
        yield None
    else:
        c = candidates[0]
        for sc in sum_combinations(candidates[1:], target-c):
            if sc is not None:
                yield [c] + sc
        # Skip elements that are equal to c.
        # You can do binary search here as candidates are sorted,
        # but overall time complexity would not improve much.
        i = 1
        while i < len(candidates) and candidates[i] == c:
            i += 1
        for sc in sum_combinations(candidates[i:], target):
            if sc is not None:
                yield sc



candidates = [10, 1, 2, 7, 6, 1, 5]
candidates.sort()

for sc in sum_combinations(candidates, 8):
    print(sc)
