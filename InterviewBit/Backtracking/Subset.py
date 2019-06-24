"""
Subset
======

Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""

from __future__ import print_function


def subsets(s):
    # Recursion base
    if not s:
        yield []
    else:
        el = s[0]
        tail = s[1:]

        # First is empty set
        yield []

        # Then subsets that start with first element
        for subs in subsets(tail):
            yield [el] + subs

        # Then subsets that do not have first element
        # excluding the empty set, that already was produced.
        tail_subsets = subsets(tail)
        next(tail_subsets) # skip []
        for subs in tail_subsets:
            yield subs


for subs in subsets([1, 2, 3, 4]):
    print(subs)
