# -*- coding: utf8 -*-
"""
Longest Common Prefix
=====================

Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[
  "abcdefgh",
  "aefghijk",
  "abcefgh"
]
The answer would be “a”.

Solution
--------

Use character by character approach to find the first position in strings at which different characters appear in string array.

Time complexity O(N*M)
"""

from __future__ import print_function


def lcp(strings):
    min_len = min(len(s) for s in strings)

    i = 0
    while i < min_len:
        c = strings[0][i]
        if not all(s[i]==c for s in strings):
            break
        i += 1

    return strings[0][:i]


print(lcp([
  "abcdefgh",
  "abfghijk",
  "abcefgh"
]))
