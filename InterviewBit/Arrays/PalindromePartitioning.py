"""
Palindrome Partitioning
=======================

Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["a","a","b"]
  ["aa","b"],
]
"""

from __future__ import print_function


def is_palindrome(s):
    if len(s) <= 1:
        return True
    for n in range(len(s)//2):
        if s[n] != s[-n-1]:
            return False
    return True


def palindrome_partitions(s):
    if not s:
        yield []
    else:
        for i in range(1, len(s)+1):
            head = s[:i]
            if not is_palindrome(head):
                continue
            for pp in palindrome_partitions(s[i:]):
                yield [head] + pp


for pp in palindrome_partitions('aabaacfc'):
    print(pp)
