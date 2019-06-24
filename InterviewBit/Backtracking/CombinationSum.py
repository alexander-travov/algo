# -*- coding: utf8 -*-
"""
Combination Sum
===============

Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.

Example:
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
"""

from __future__ import print_function


def sum_combinations(candidates, target):
    if target == 0:
        yield []
    elif not candidates or target < 0:
        yield
    else:
        c = candidates[0]
        for sc in sum_combinations(candidates, target-c):
            if sc is not None:
                yield [c] + sc
        for sc in sum_combinations(candidates[1:], target):
            if sc is not None:
                yield sc


for sc in sum_combinations([2, 3, 6, 7], 25):
    print(sc)
