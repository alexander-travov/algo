"""
Calculation of prefix function and substring search in O(N+M) with Knuth-Morris-Pratt algorithm.
Extra space: O(M) M-length of a substring, N-length of text.
"""

from __future__ import print_function


def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        j = p[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[j] == s[i]:
            j += 1
        p[i] = j
    return p


def kmp(text, s):
    n = len(s)
    s += '#'
    p = prefix(s)
    count = 0
    j = 0
    for c in text:
        while j > 0 and c != s[j]:
            j = p[j-1]
        if c == s[j]:
            j += 1
        if j == n:
            count += 1
    return count


print(kmp('abcabcabc', 'abc'))
