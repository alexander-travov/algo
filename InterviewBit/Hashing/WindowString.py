"""
Window String
=============

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in linear time complexity.

Note that when the count of a character C in T is N,
then the count of C in minimum window in S should be at least N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

Note: "Distinct Numbers in Window" problem from Heaps and Maps
is very similar to that problem and can be solved with the same Counter data structure.
"""

from __future__ import print_function
from collections import Counter
import sys


def max_window(string, target):
    target_count = Counter()
    for l in target:
        target_count[l] += 1

    curr_count = Counter()

    def contains_target():
        return all(
            curr_count[l] >= target_count[l]
            for l in target_count
        )

    start = 0
    stop = -1
    min_len = sys.maxsize
    min_start = 0
    while True:
        if contains_target():
            cur_len = stop-start+1
            if cur_len < min_len:
                min_len = cur_len
                min_start = start
                
            # Remove first letter
            l = string[start]
            if l in target_count:
                curr_count[l] -= 1
            start += 1
        else:
            stop += 1
            if stop == len(string):
                break
            l = string[stop]
            if l in target_count:
                curr_count[l] += 1

    return string[min_start:min_start+min_len]


print(max_window("ADOBECODEBANC", "ABBC"))
