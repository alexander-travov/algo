"""
Minimum Characters required to make a String Palindromic
========================================================

You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
    Input: ABC
    Output: 2
    Input: AACECAAAA
    Output: 2

Solution
--------

The problem can be solved with prefix function for string s + '$' + reversed(s)
The last entry in prefix function will have the length of the longest palindrom
in the beginning of s.

Time complexity O(N), extra space O(N)
"""

from __future__ import print_function


def prefix_fn(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        j = p[i-1]
        while j>0 and s[i] != s[j]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


def min_for_palindrome(s):
    p = prefix_fn(s + '$' + s[::-1])
    return len(s) - p[-1]


print(min_for_palindrome('aacecaaaa'))
