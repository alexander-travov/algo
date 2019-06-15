"""
Longest Palindromic Substring
=============================

Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"

Solution
--------

Problem can be solved in O(N) time, O(N) space with Manacher's algorithm.
"""

from __future__ import print_function


def manacher(s):
    n = len(s)

    # odd palindromes
    d1 = [0] * n
    l = 0
    r = -1
    for i in range(n):
        if i > r:
            k = 1
        else:
            k = min(r-i, d1[l+r-i])
        while 0 <= i-k and i+k < n and s[i-k] == s[i+k]:
            k += 1
        d1[i] = k
        if i+k-1 > r:
            l, r = i-k+1, i+k-1

    # even palindromes
    d2 = [0] * len(s)
    l = 0
    r = -1
    for i in range(n):
        if i > r:
            k = 0
        else:
            k = min(r-i+1, d2[l+r-i+1])
        while 0 <= i-k-1 and i+k < n and s[i-k-1] == s[i+k]:
            k += 1
        d2[i] = k
        if i+k-1 > r:
            l, r = i-k, i+k-1

    max_odd_len = max(d1)
    max_odd_ind = d1.index(max_odd_len)

    max_even_len = max(d2)
    max_even_ind = d2.index(max_even_len)

    if max_odd_len >= max_even_len:
        pal = s[max_odd_ind-max_odd_len+1 : max_odd_ind+max_odd_len]
    else:
        pal = s[max_even_ind-max_even_len : max_even_ind+max_even_len]

    return pal


print(manacher('defaabccbaaadfg'))
